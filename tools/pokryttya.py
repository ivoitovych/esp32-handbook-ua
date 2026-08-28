#!/usr/bin/env python3
"""Coverage: is every line of the book accounted for by a card?

## The question this asks, and the one it does not

The registry is **generated** from the book, so "does every unit have a
card" is true by construction and worth nothing. The real question is
the other way round:

> **Does every line of the book become a unit?**

Text the splitter never saw has no card, no class, no evidence — and,
worse, does not appear in any count. It is not `unverified`; it is
invisible. A book can show 100 % of its units checked while a chapter
of it was never split at all.

## What counts as covered

A line is covered if some card records `src:file:line` inside the span
that line belongs to. Cards carry the first line of their unit, so a
sentence wrapped over four lines is covered by one card; the span runs
to the next card's line or to the end of the block.

## What is deliberately not counted

Empty lines, fence markers, and the block separators the book uses for
layout. These carry no claim and never could.

**Everything else is counted, including headings and code.** They may
well be out of scope for fact-checking — but that is a *verdict*, and a
verdict belongs in a card, not in a script's exclusion list. A coverage
tool that silently drops what it considers uninteresting measures its
own opinion.

## What to do with the gap

Uncovered lines are a work order, not a defect. Each needs one of two
answers, and both are human or model work:

* it is a claim → it belongs in the registry, and the splitter missed it;
* it is not a claim → say so in a card, so the next audit does not ask
  again.

    tools/pokryttya.py [--fayl <шлях>] [--dilyanky]
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("manual", "dodatky", "kartky", "inserts")

RE_SRC = re.compile(r"<!-- fc id:(\S+) sha:\S+ src:(\S+?):(\d+) klas:(\S+) -->")
PORO_ZHNI = re.compile(r"^\s*$|^```|^:::|^<!--|^\s*[-=]{3,}\s*$")


def zibraty_kartky() -> dict[str, set[int]]:
    pokryti: dict[str, set[int]] = defaultdict(set)
    for g in GRUPY:
        katalog = ROOT / "factcheck" / g
        if not katalog.exists():
            continue
        for f in katalog.glob("*.md"):
            for m in RE_SRC.finditer(f.read_text(encoding="utf-8")):
                pokryti[m.group(2)].add(int(m.group(3)))
    return pokryti


def main(argv: list[str]) -> int:
    lyshe = None
    if "--fayl" in argv:
        lyshe = argv[argv.index("--fayl") + 1]
    dilyanky = "--dilyanky" in argv

    pokryti = zibraty_kartky()
    vsyoho = pokryto = 0
    za_faylom: list[tuple] = []

    for g in GRUPY:
        katalog = ROOT / g
        if not katalog.exists():
            continue
        for p in sorted(katalog.glob("*.md")):
            vidn = str(p.relative_to(ROOT))
            if lyshe and vidn != lyshe:
                continue
            ryadky = p.read_text(encoding="utf-8").split("\n")
            tochky = sorted(pokryti.get(vidn, set()))
            zmistovni = [i + 1 for i, r in enumerate(ryadky)
                         if not PORO_ZHNI.match(r)]
            if not zmistovni:
                continue
            # Кожна картка накриває свій рядок і все до наступної картки.
            nakryti: set[int] = set()
            for k, poch in enumerate(tochky):
                kinec = tochky[k + 1] if k + 1 < len(tochky) else len(ryadky) + 1
                nakryti.update(range(poch, kinec))
            ne = [i for i in zmistovni if i not in nakryti]
            vsyoho += len(zmistovni)
            pokryto += len(zmistovni) - len(ne)
            za_faylom.append((vidn, len(zmistovni), len(ne), ne))

    za_faylom.sort(key=lambda x: -x[2])
    print("%-40s %7s %7s %6s" % ("файл", "рядків", "без картки", "покрито"))
    for vidn, vs, nek, ne in za_faylom:
        if nek == 0 and not dilyanky:
            continue
        print("%-40s %7d %7d %5.0f%%"
              % (vidn, vs, nek, 100 * (vs - nek) / vs))
        if dilyanky and ne:
            grupy, poch, pop = [], ne[0], ne[0]
            for x in ne[1:]:
                if x != pop + 1:
                    grupy.append((poch, pop))
                    poch = x
                pop = x
            grupy.append((poch, pop))
            for a, b in grupy[:12]:
                print("      рядки %d–%d" % (a, b) if a != b else
                      "      рядок %d" % a)

    print("\npokryttya: змістовних рядків книги %d; накрито картками %d (%.1f %%); "
          "без картки %d"
          % (vsyoho, pokryto, 100 * pokryto / max(1, vsyoho), vsyoho - pokryto))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
