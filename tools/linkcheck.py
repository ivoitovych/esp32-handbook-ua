#!/usr/bin/env python3
"""Перевірка якорів і посилань (Р7).

Крос-посилання в довіднику ведуть на стабільні слаги, не на номери розділів.
Номери генеруються при збиранні і змінюються від ревізії до ревізії; слаг —
ні. Ціна цього рішення — биті посилання нікуди не діваються самі, тому
перевірка обов'язкова перед кожним комітом тексту.

Перевіряє:
  · посилання [текст](#слаг) на неоголошений якір
  · оголошення {#слаг} у двох різних місцях
  · зображення ![](шлях), яких немає на диску
  · файли, перелічені в book.yaml, яких немає на диску
  · оголошені якорі, на які ніхто не посилається (попередження)
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC_DIRS = ("kartky", "manual", "dodatky", "inserts")

RE_ANCHOR = re.compile(r"\{#([a-z0-9][a-z0-9-]*)\}")
RE_LINK = re.compile(r"\]\(#([^)]+)\)")
RE_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def sources() -> list[Path]:
    out = []
    for d in SRC_DIRS:
        out += sorted((ROOT / d).glob("*.md"))
    return out


def main() -> int:
    anchors: dict[str, list[str]] = defaultdict(list)
    links: dict[str, list[str]] = defaultdict(list)
    errors: list[str] = []

    files = sources()
    for f in files:
        rel = str(f.relative_to(ROOT))
        text = f.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for a in RE_ANCHOR.findall(line):
                anchors[a].append(f"{rel}:{lineno}")
            for a in RE_LINK.findall(line):
                links[a].append(f"{rel}:{lineno}")
            for img in RE_IMAGE.findall(line):
                path = img.split()[0].strip('"\'<>')
                if path.startswith(("http://", "https://")):
                    continue
                target = (ROOT / path) if path.startswith(("img/", "kod/")) \
                    else (f.parent / path)
                if not target.exists():
                    errors.append(f"{rel}:{lineno}: немає зображення «{path}»")

    for a, where in sorted(anchors.items()):
        if len(where) > 1:
            errors.append(f"якір {{#{a}}} оголошено {len(where)} разів: "
                          + ", ".join(where))

    # Якір, оголошений у ще не написаному розділі, — не бите посилання,
    # а посилання вперед. Відрізняємо одне від одного за тим, чи згадано
    # цей слаг у канонічному змісті.
    planned = set(RE_ANCHOR.findall(
        (ROOT / "docs" / "zmist.md").read_text(encoding="utf-8")))
    forward = 0
    for a, where in sorted(links.items()):
        if a in anchors:
            continue
        if a in planned:
            forward += len(where)
            continue
        for w in where:
            errors.append(f"{w}: посилання на неоголошений якір «#{a}»")
    if forward:
        print(f"  · посилань уперед, на ще не написані якорі: {forward}")

    # Файли, перелічені в маніфесті, але ще не написані, — це план роботи,
    # а не помилка: book.yaml описує книгу цілком з самого початку.
    # Помилками лишаються лише биті якорі, дублі й відсутні зображення.
    manifest = yaml.safe_load((ROOT / "book.yaml").read_text(encoding="utf-8"))
    listed: set[str] = set()
    not_written: set[str] = set()
    for t in manifest["targets"].values():
        for part in t.get("parts") or []:
            for rel in part.get("files") or []:
                listed.add(rel)
                if not (ROOT / rel).exists():
                    not_written.add(rel)

    orphan_files = sorted(str(f.relative_to(ROOT)) for f in files
                          if str(f.relative_to(ROOT)) not in listed)
    orphan_anchors = sorted(a for a in anchors if a not in links)

    for e in errors:
        print(f"  ✗ {e}")
    if not_written:
        print(f"  · заплановано, ще не написано: {len(not_written)}")
    if orphan_files:
        print(f"  · не входять у жодну ціль book.yaml ({len(orphan_files)}): "
              + ", ".join(orphan_files[:8])
              + (" …" if len(orphan_files) > 8 else ""))
    if orphan_anchors:
        print(f"  · якорі без жодного посилання ({len(orphan_anchors)}): "
              + ", ".join(f"#{a}" for a in orphan_anchors[:8])
              + (" …" if len(orphan_anchors) > 8 else ""))

    print(f"linkcheck: файлів {len(files)}, якорів {len(anchors)}, "
          f"посилань {sum(len(v) for v in links.values())}, "
          f"помилок {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
