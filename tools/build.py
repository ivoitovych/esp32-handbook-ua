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

# Перехресні посилання «розділ 21» і «картка К5» у джерелах пишуться
# звичайним текстом — так їх зручно читати й правити. У книзі вони мають
# бути посиланнями на якорі (Р7): і клікабельними в PDF, і перевірюваними
# через linkcheck. Перетворення робиться тут, а не в джерелах.
RE_ROZDIL = re.compile(r"\b(розділ(?:и|ів|ах|у|і)?)\s+((?:\d{2}|\d)"
                       r"(?:\s*(?:,|та|і|—|–)\s*(?:\d{2}|\d))*)\b")
RE_KARTKA = re.compile(r"\b(картк(?:а|и|у|ою|ах|ам)?)\s+(К\d{1,2})\b")
RE_NUM = re.compile(r"\d{1,2}")


def _slug_maps() -> tuple[dict, dict]:
    """Номер розділу → слаг, номер картки → слаг. З імен файлів і якорів."""
    rozdily, kartky = {}, {}
    for f in sorted((ROOT / "manual").glob("*.md")):
        num = f.name.split("-", 1)[0]
        m = RE_ANCHOR_DEF.search(f.read_text(encoding="utf-8"))
        if m and num.isdigit():
            rozdily[int(num)] = m.group(1)
    for f in sorted((ROOT / "kartky").glob("k*.md")):
        num = f.name[1:3]
        m = RE_ANCHOR_DEF.search(f.read_text(encoding="utf-8"))
        if m and num.isdigit():
            kartky[int(num)] = m.group(1)
    return rozdily, kartky


RE_ANCHOR_DEF = re.compile(r"\{#([a-z0-9][a-z0-9-]*)\}")
_ROZDILY, _KARTKY = None, None


def linkify(line: str) -> str:
    """Замінює «розділ 21» і «картку К5» на посилання на відповідні якорі."""
    global _ROZDILY, _KARTKY
    if _ROZDILY is None:
        _ROZDILY, _KARTKY = _slug_maps()

    def rozdil(m):
        slova = m.group(2)
        nums = RE_NUM.findall(slova)
        # посилання ставимо лише коли всі номери відомі
        if not all(int(n) in _ROZDILY for n in nums):
            return m.group(0)
        out, pos = [], 0
        for mm in RE_NUM.finditer(slova):
            out.append(slova[pos:mm.start()])
            n = int(mm.group(0))
            out.append(f"[{mm.group(0)}](#{_ROZDILY[n]})")
            pos = mm.end()
        out.append(slova[pos:])
        return m.group(1) + " " + "".join(out)

    def kartka(m):
        n = int(m.group(2)[1:])
        if n not in _KARTKY:
            return m.group(0)
        return f"{m.group(1)} [{m.group(2)}](#{_KARTKY[n]})"

    return RE_KARTKA.sub(kartka, RE_ROZDIL.sub(rozdil, line))
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
        out.append(linkify(line))

    if stack:
        sys.exit(f"{src}: не закрито блок(и) {stack}")
    return "\n".join(out) + "\n"


def md_to_typst(src: Path) -> str:
    md = preprocess(src.read_text(encoding="utf-8"), src)
    proc = subprocess.run(
        ["pandoc", "-f",
         "markdown+fenced_divs+pipe_tables+header_attributes+raw_attribute"
         "+backtick_code_blocks-auto_identifiers-smart",
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

    Дужки рахуються лише поза raw-фрагментами: комірка виду [`Ctrl+]`]
    цілком законна, і дужка всередині коду не має закривати блок.
    """
    out, i, marker = [], 0, "#align(center)[#table("
    while True:
        j = typ.find(marker, i)
        if j < 0:
            out.append(typ[i:])
            return "".join(out)
        out.append(typ[i:j])
        start = j + len("#align(center)[")
        end = _match_bracket(typ, start)
        out.append(typ[start:end])
        i = end + 1


def _match_bracket(typ: str, start: int) -> int:
    """Індекс «]», що закриває «[» перед start. Пропускає raw-фрагменти."""
    depth, k, n = 1, start, len(typ)
    while k < n:
        c = typ[k]
        if c == "\\":                      # екранований символ
            k += 2
            continue
        if c == "`":                       # raw: пропустити до парного руна
            run = len(typ[k:]) - len(typ[k:].lstrip("`"))
            close = typ.find("`" * run, k + run)
            k = n if close < 0 else close + run
            continue
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return k
        k += 1
    return n - 1


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


RE_LABEL_DEF = re.compile(r"^<([^<>\s]+)>\s*$", re.M)
RE_LINK_REF = re.compile(r"#link\(<([^<>()]+)>\)")


def resolve_links(frags: list[Path]) -> set[str]:
    """Знімає посилання на якорі, яких у цьому PDF немає.

    Книга мусить збиратися на будь-якому етапі написання, тому посилання
    на ще не написаний розділ не може ламати збирання. Typst відмовляється
    компілювати #link на неоголошену мітку — такі посилання перетворюємо
    на звичайний текст, зберігаючи підпис. Перелік друкується при збиранні,
    щоб жодне з них не лишилося непоміченим у готовій книзі.
    """
    texts = [f.read_text(encoding="utf-8") for f in frags]
    defined = {m for t in texts for m in RE_LABEL_DEF.findall(t)}
    dangling: set[str] = set()

    for f, t in zip(frags, texts):
        refs = set(RE_LINK_REF.findall(t))
        gone = refs - defined
        if not gone:
            continue
        dangling |= gone
        for a in gone:
            t = t.replace(f"#link(<{a}>)", "")
        f.write_text(t, encoding="utf-8")
    return dangling


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

    missing, seq, frags = [], 0, []
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
            frags.append(frag)
            root.append(f'#include "{frag.name}"')
    if cfg.get("back_matter", True):
        root += ["", "#back-matter(meta)", ""]

    dangling = resolve_links(frags)
    if dangling:
        top = ", ".join(f"#{a}" for a in sorted(dangling)[:5])
        extra = f" … і ще {len(dangling) - 5}" if len(dangling) > 5 else ""
        print(f"  · посилання вперед, знято до звичайного тексту "
              f"({len(dangling)}): {top}{extra}")

    if missing:
        head = ", ".join(missing[:4])
        tail = f" … і ще {len(missing) - 4}" if len(missing) > 4 else ""
        print(f"  · ще не написано ({len(missing)}): {head}{tail}")

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
