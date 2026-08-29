#!/usr/bin/env python3
"""Every literal path into `factcheck/` written in a tool must resolve.

## Why

Reorganising `factcheck/` moved directories twice in two days. Each time I
rewrote the path constants with a pattern, and each time the pattern
matched one spelling of the path and missed another:

    "factcheck" / "evidence"          caught by the first sweep
    FC / "evidence"                   missed — a different base
    "factcheck" / "queues/x.yaml"     missed — directory and file in one
                                      string, so the directory name was
                                      not a whole token

Six live constants pointed at directories that no longer existed, and
`make check` was green through all of it, because no gate exercises the
paths a tool would use only when someone runs that tool.

> A broken path is not found by running the checks. It is found by
> running the tool that holds it, and that may be a week later, in the
> middle of a wave, when it writes its output somewhere nobody looks.

So the check does not run the tools. It reads them, extracts every
literal path under `factcheck/`, and asks the filesystem.

## What it cannot do

It sees literals. A path assembled from variables — `katalog / imya` —
is invisible to it, and so is anything built at run time. It measures
**intent written down**, which is the same limit `docs.py`'s root guard
carries, and for the same reason.

    tools/paths.py           check every literal path
    tools/paths.py --list    print them all, resolved
    tools/paths.py --demo    demonstration on a broken input
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FC = ROOT / "factcheck"

# `"factcheck" / "a" / "b"` або `FC / "a" / "b"`, скільки б ланок не було.
RE_PATH = re.compile(r'(?:"factcheck"|\bFC\b)((?:\s*/\s*"[^"]*")+)')
RE_LANKA = re.compile(r'"([^"]*)"')

# Показові й вигадані шляхи: вони НЕ мусять існувати, у тому й показ.
# Перелік явний, бо мовчазний виняток за взірцем сам став би дірою.
VYNYATKY = {
    ("tools/language.py", "factcheck/data/snapshots/a.json"),
    ("tools/language.py", "factcheck/x.md"),
    ("tools/docs.py", "factcheck/GHOST.md"),
}


def shlyakhy(dzherelo: dict[str, str] | None = None):
    """(tool, path) for every literal path into factcheck/."""
    # Власний файл — не предмет: у ньому живуть навмисно зламані шляхи
    # показу. Перевірка, що спрацьовує на власному показі, повідомляє
    # про себе, а не про код — і цим ховає справжні знахідки серед
    # своїх. (Той самий випадок, що з коментарем у `language.py`, який
    # містив літерал, описаний ним же.)
    fajly = ({Path(k): v for k, v in dzherelo.items()} if dzherelo
             else {f: f.read_text(encoding="utf-8")
                   for f in sorted((ROOT / "tools").glob("*.py"))
                   if f.name != "paths.py"})
    for f, t in fajly.items():
        for m in RE_PATH.finditer(t):
            lanky = [x for x in RE_LANKA.findall(m.group(1)) if x]
            if not lanky:
                continue
            # Ланка може сама містити слеш: `"queues/x.yaml"`. Саме ця
            # форма й пережила обидва переписування.
            chastyny = [c for lanka in lanky for c in lanka.split("/") if c]
            if any("*" in c or "{" in c for c in chastyny):
                continue
            yield f"tools/{f.name}", "factcheck/" + "/".join(chastyny)


def perevirka(dzherelo: dict[str, str] | None = None) -> list[str]:
    bidy = []
    for tula, shlyakh in shlyakhy(dzherelo):
        if (tula, shlyakh) in VYNYATKY:
            continue
        if not (ROOT / shlyakh).exists():
            bidy.append(f"{tula}: names `{shlyakh}`, which does not exist")
    return bidy


def demo() -> int:
    ok = True

    def check(nazva: str, umova: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if umova else '✗'} {nazva}: {umova}")
        ok &= umova

    check("зламаний шлях ловиться",
          bool(perevirka({"tools/x.py": 'A = ROOT / "factcheck" / "nemaye"'})))
    check("інша вимова того самого шляху теж ловиться",
          bool(perevirka({"tools/x.py": 'A = FC / "nemaye"'})))
    check("тека й файл в одній ланці — ловиться",
          bool(perevirka({"tools/x.py": 'A = FC / "queues/nemaye.yaml"'})))
    check("справжній шлях мовчить",
          not perevirka({"tools/x.py": 'A = FC / "METHOD.md"'}))
    check("глоб не перевіряється",
          not perevirka({"tools/x.py": 'A = FC / "*.md"'}))
    print("\nfailures:", 0 if ok else 1)
    return 0 if ok else 1


def main() -> int:
    if "--demo" in sys.argv:
        return demo()
    if "--list" in sys.argv:
        for tula, s in sorted(set(shlyakhy())):
            print(f"  {'OK ' if (ROOT / s).exists() else 'MISSING'}  "
                  f"{tula:<26}{s}")
        return 0
    bidy = perevirka()
    for b in bidy:
        print(f"   ✗ {b}")
    print(f"\npaths: {len(set(shlyakhy()))} literal paths into factcheck/, "
          f"{len(bidy)} broken")
    return 1 if bidy else 0


if __name__ == "__main__":
    sys.exit(main())
