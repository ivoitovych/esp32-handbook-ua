#!/usr/bin/env python3
"""Lists of file names in the code: no duplicates, no names of nothing.

## Why this exists

M1's observation, and it is the reason this file is not another one-off
fix:

> One `sed` pass produced six defects in three lists of names, and every
> one of them was found by a different check or a different person. We
> still have no common detector: we catch this in a new place each time.

The six, all from the same afternoon:

    .gitignore          a rename rewrote the rule whose subject was the
                        old path — 236 cache files lost their protection
    MIGRATION.md        the left column of the rename table, whose whole
                        job is to hold names that no longer exist
    doc_kind.ISTORYCHNI the live task specification silently marked
                        historical, because its name replaced a deleted
                        file's name in a list of NAMES
    docs.KERIVNI        the same substitution twice, so the list counted
                        14 governing documents while holding 13
    README index        one document listed twice
    tools/refuted.py    a glob `SPROSTOVANE*.md` the replace did not
                        match, because it required `.md` right after

## The shape they share

> **A list of names is not a list of references.** A reference points at
> a thing and is correct while the thing exists. A name in a list is a
> *statement about* the thing under it — and a rename pass, which is
> right to update references, is wrong to update these.

Nothing detects that a name has become a statement. But two consequences
of getting it wrong are mechanical, and this checks them:

    duplicates      two entries became one name; the list now says less
                    than it claims, and its length lies
    dangling        the name refers to no file that exists

Neither catches the `.gitignore` case, where the name was correct before
and after and only the *meaning* was destroyed. That one is named in
`DEFECTS.md` as kind 26 and has no automatic check, and saying so here is
part of reporting this honestly.

    tools/name_lists.py            check
    tools/name_lists.py --proba    show it firing on a duplicate and on a
                                   name of nothing
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RE_SPYSOK = re.compile(
    r"^([A-Z][A-Z0-9_]*)\s*=\s*[\[\{\(]((?:[^\]\}\)]|\n)*?)[\]\}\)]", re.M)
RE_LITERAL = re.compile(r'"([^"]+)"|\'([^\']+)\'')
# Щось мусить стояти ПЕРЕД крапкою: `.rst` — це розширення, а не файл.
# Перший прогін зібрав набір розширень із `layer3.TEKSTOVI` і оголосив
# шість неіснуючих файлів. Хибна тривога в перевірці проти хибних
# переліків — доречне нагадування, що детектор теж перелік.
RE_FAYL = re.compile(r"[\w-]\.(md|py|yaml|json|rst|txt)$")

# Де шукати названий файл. Перелік може називати документ без теки —
# `TASK-SPEC.md`, а не `factcheck/TASK-SPEC.md`.
TEKY = ("", "factcheck", "tools", "zvyazok", "manual", "dodatky")


def isnuye(imya: str) -> bool:
    if "*" in imya or "?" in imya:          # глоб — не ім'я одного файлу
        return True
    for t in TEKY:
        if (ROOT / t / imya).exists():
            return True
    return False


def perevirka(dzherelo: dict[str, str] | None = None) -> list[str]:
    bidy: list[str] = []
    fajly = ({Path(k): v for k, v in dzherelo.items()} if dzherelo
             else {f: f.read_text(encoding="utf-8")
                   for f in sorted((ROOT / "tools").glob("*.py"))})
    for f, t in fajly.items():
        for m in RE_SPYSOK.finditer(t):
            imena = [a or b for a, b in RE_LITERAL.findall(m.group(2))]
            imena = [i for i in imena if RE_FAYL.search(i)]
            if len(imena) < 2:
                continue
            bachyly: set[str] = set()
            for i in imena:
                if i in bachyly:
                    bidy.append(f"{f.name}: {m.group(1)} names `{i}` twice — "
                                f"a rename most likely collapsed two entries")
                bachyly.add(i)
                if not isnuye(i):
                    bidy.append(f"{f.name}: {m.group(1)} names `{i}`, "
                                f"which is not a file")
    return bidy


def proba() -> int:
    vypadky = [
        ("duplicate in a list",
         'SPYSOK = ["METHOD.md", "SCHEMA.md", "METHOD.md"]\n', True),
        ("a name of nothing",
         'SPYSOK = ["METHOD.md", "NEMAYE-TAKOHO.md"]\n', True),
        ("a sound list",
         'SPYSOK = ["METHOD.md", "SCHEMA.md"]\n', False),
        ("a glob is not a missing file",
         'SPYSOK = ["METHOD.md", "REFUTED*.md"]\n', False),
    ]
    provaliv = 0
    for nazva, tekst, ocik in vypadky:
        b = perevirka({"proba.py": tekst})
        ok = bool(b) == ocik
        print("   %s %-34s expected %-5s got %s"
              % ("✓" if ok else "✗ FAIL", nazva, ocik, bool(b)))
        provaliv += not ok
    print("\nfailures: %d" % provaliv)
    return 1 if provaliv else 0


def main() -> int:
    if "--proba" in sys.argv:
        return proba()
    bidy = perevirka()
    for b in bidy:
        print("   ✗ " + b)
    print("\nname_lists: %d problems" % len(bidy))
    return 1 if bidy else 0


if __name__ == "__main__":
    sys.exit(main())
