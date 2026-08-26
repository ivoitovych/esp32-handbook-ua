#!/usr/bin/env python3
"""Збирання PDF довідника: Markdown → Typst → PDF.

Конвеєр:
  1. препроцесор проєктної розмітки (блоки-застереження, маркери області дії)
  2. pandoc: markdown → typst-фрагмент
  3. згенерований кореневий .typ підключає шаблон і фрагменти по порядку
  4. typst: → PDF

Проєктна розмітка, якої немає в звичайному Markdown:

  ::: uvaha           блок-застереження; клас — один із:
  текст блоку           zhyvlennya · uvaha · zakupivlya · nezvorotne
  :::

  [[classic]]         маркер області дії; всередині — classic, S3, C3, …
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"

NOTE_CLASSES = {
    "zhyvlennya": "zhyvlennya",
    "uvaha": "hrabli",
    "hrabli": "hrabli",
    "zakupivlya": "zakupivlya",
    "nezvorotne": "nezvorotne",
}

RE_HEADING = re.compile(r"^(#{1,5})(\s)")
RE_DIV_OPEN = re.compile(r"^:::+\s*([a-z-]+)\s*$")
RE_DIV_CLOSE = re.compile(r"^:::+\s*$")
RE_SCOPE = re.compile(r"\[\[([^\]\[]+)\]\]")


def preprocess(md: str, src: Path) -> str:
    """Розгортає проєктну розмітку в raw-typst, який pandoc пропускає наскрізь."""
    out, stack, in_fence = [], [], False

    for lineno, line in enumerate(md.splitlines(), 1):
        # Усередині ``` … ``` розмітка не діє — там код.
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        # Заголовки зсуваються на рівень униз: рівень 1 у книзі — частина.
        line = RE_HEADING.sub(lambda m: "#" + m.group(1) + m.group(2), line)

        m = RE_DIV_OPEN.match(line)
        if m:
            cls = m.group(1)
            if cls not in NOTE_CLASSES:
                sys.exit(f"{src}:{lineno}: невідомий клас блоку «{cls}»; "
                         f"дозволені: {', '.join(sorted(NOTE_CLASSES))}")
            stack.append(cls)
            out += ["", "```{=typst}", f"#{NOTE_CLASSES[cls]}[", "```", ""]
            continue

        if RE_DIV_CLOSE.match(line) and stack:
            stack.pop()
            out += ["", "```{=typst}", "]", "```", ""]
            continue

        # Маркери області дії — інлайновий raw typst.
        line = RE_SCOPE.sub(
            lambda m: '`#scope("' + '", "'.join(
                p.strip() for p in m.group(1).split(",")) + '")`{=typst}',
            line,
        )
        out.append(line)

    if stack:
        sys.exit(f"{src}: не закрито блок(и) {stack}")
    return "\n".join(out) + "\n"


def md_to_typst(src: Path) -> str:
    md = preprocess(src.read_text(encoding="utf-8"), src)
    proc = subprocess.run(
        ["pandoc", "-f",
         "markdown+fenced_divs+pipe_tables+header_attributes+raw_attribute"
         "+backtick_code_blocks+auto_identifiers-smart",
         "-t", "typst", "--wrap=preserve"],
        input=md, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        sys.exit(f"pandoc не впорався з {src}:\n{proc.stderr}")
    return strip_table_centering(proc.stdout)


def strip_table_centering(typ: str) -> str:
    """Знімає обгортку #align(center)[…] навколо таблиць, яку ставить pandoc.

    У книзі таблиця стоїть по лівому краю смуги набору, як і решта тексту;
    центрування створює зайвий вертикальний відступ перед таблицею.
    """
    out, i, marker = [], 0, "#align(center)[#table("
    while True:
        j = typ.find(marker, i)
        if j < 0:
            out.append(typ[i:])
            return "".join(out)
        out.append(typ[i:j])
        start = j + len("#align(center)[")
        depth, end = 1, start
        for end in range(start, len(typ)):
            if typ[end] == "[":
                depth += 1
            elif typ[end] == "]":
                depth -= 1
                if depth == 0:
                    break
        out.append(typ[start:end])
        i = end + 1


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build(name: str, cfg: dict, meta: dict) -> Path:
    tdir = BUILD / name
    if tdir.exists():
        shutil.rmtree(tdir)
    tdir.mkdir(parents=True)

    # Typst обчислює кожен #include у власній області видимості,
    # тому шаблон імпортується і в корені, і в кожному фрагменті.
    IMPORT = '#import "/typst/handbook.typ": *'

    root = [
        IMPORT,
        "",
        "#let meta = (",
    ]
    for k, v in meta.items():
        root.append(f'  "{k}": "{esc(str(v))}",')
    root += [")", "", f"#show: {cfg['template']}.with(meta)", ""]

    missing, seq = [], 0
    for part in cfg.get("parts") or []:
        files = part.get("files") or []
        if not part.get("silent") and part.get("title"):
            root += [
                "#part-divider(",
                f'  "{esc(part["title"])}",',
                f'  blurb: "{esc(part.get("blurb", ""))}",',
                ")",
                "",
            ]
        for rel in files:
            src = ROOT / rel
            if not src.exists():
                missing.append(rel)
                continue
            seq += 1
            frag = tdir / f"{seq:03d}-{Path(rel).stem}.typ"
            frag.write_text(IMPORT + "\n\n" + md_to_typst(src), encoding="utf-8")
            root.append(f'#include "{frag.name}"')
    if cfg.get("back_matter", True):
        root += ["", "#back-matter(meta)", ""]

    if missing:
        print(f"  ! пропущено (немає файлу): {', '.join(missing)}")

    root_typ = tdir / "root.typ"
    root_typ.write_text("\n".join(root), encoding="utf-8")

    out = BUILD / cfg["output"]
    import typst
    typst.compile(str(root_typ), output=str(out), root=str(ROOT))
    return out


def main() -> None:
    cfg = yaml.safe_load((ROOT / "book.yaml").read_text(encoding="utf-8"))
    meta = cfg["meta"]
    wanted = sys.argv[1:] or list(cfg["targets"])

    BUILD.mkdir(exist_ok=True)
    for name in wanted:
        if name not in cfg["targets"]:
            sys.exit(f"немає такої цілі: {name}; є: {', '.join(cfg['targets'])}")
        print(f"→ {name}")
        out = build(name, cfg["targets"][name], meta)
        print(f"  ✓ {out.relative_to(ROOT)}  ({out.stat().st_size // 1024} КБ)")


if __name__ == "__main__":
    main()
