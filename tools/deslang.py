#!/usr/bin/env python3
"""Stage 2 of the migration: process slang out of the records.

## The defect

A record's `method` field is meant to say **how and when** the source
was obtained. Instead it carried our internal workflow vocabulary:

    "Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг
     звірено з ним підрядком машинно (`tools/sweep_digest.py`)…"

`суцільний прохід`, `посадка`, `хвиля`, `наряд` are two maintainers'
private words. They mean nothing to anyone else, and they were written
into **710 records** that an outside reader is supposed to read.

Worse, most of them are mine: I generated that boilerplate this
afternoon, in the same hours I was writing rules about clarity.

## Why the tool name also goes

`(tools/sweep_digest.py)` is an implementation detail of *this*
repository. A record that names it cannot travel to another book — and
travelling to another book is the whole point of the migration.

What survives is the fact: the document was retrieved on a date, and
the quote was checked against it mechanically.

## Scope

22 distinct formulations; six of them cover about 570 records, so the
rewrite is keyed by phrase rather than done by hand.

Anything not matched is **left alone and reported** — a silent
best-effort rewrite of prose nobody re-read would be its own defect.

    tools/deslang.py --pysaty   rewrite
    tools/deslang.py            dry run: what is left
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

SLENG = re.compile(
    r"наряд|помічник|посадк|присуд|прохід|проход|помірк|хвил[яію]"
    r"|холост|штурм|вибірк|tools/\w+\.py", re.I)

# Ключ — початок наявного формулювання; значення — що ставимо замість.
# Порядок важить: перший збіг виграє.
ZAMINY: list[tuple[str, str]] = [
    ("Суцільний прохід",
     "Source document retrieved 2026-08-27 and the quote verified "
     "against it by substring match. Status `verbatim` means the "
     "document was obtained and the quote is exact — it does **not** "
     "mean a maintainer read the passage and agreed. That judgement "
     "is separate work."),
    ("хвиля 3",
     "Source document retrieved 2026-08-27 from the local cache; "
     "quote verified against it by substring match."),
    ("хвиля 2",
     "Source document retrieved 2026-08-26 from the local cache; "
     "quote verified against it by substring match."),
    ("наряди «деталі»",
     "Source document retrieved 2026-08-27; quote verified against it "
     "by substring match."),
    ("curl raw.githubusercontent (повторно",
     "Retrieved with `curl` from raw.githubusercontent.com, "
     "2026-08-26; quote verified by substring match."),
    ("помічник пулу",
     "Source document retrieved 2026-08-26; quote verified against it "
     "by substring match."),
]


def novyy(stare: str) -> str | None:
    for pochatok, zamina in ZAMINY:
        if stare.startswith(pochatok):
            return zamina
    return None


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--pysaty", action="store_true")
    a = p.parse_args()

    teka = ROOT / "factcheck" / "data" / "evidence"
    zmineno = lyshylos = 0
    reshta: dict[str, int] = {}
    for f in sorted(teka.glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        if not isinstance(z, list):
            continue
        torknuly = False
        for r in z:
            if not isinstance(r, dict):
                continue
            for pole in ("method", "sposib"):
                v = str(r.get(pole) or "")
                if not v or not SLENG.search(v):
                    continue
                n = novyy(v)
                if n is None:
                    if pole == "method":
                        lyshylos += 1
                        reshta[v[:64]] = reshta.get(v[:64], 0) + 1
                    continue
                r[pole] = n
                torknuly = True
                if pole == "method":
                    zmineno += 1
        if a.pysaty and torknuly:
            tekst = f.read_text(encoding="utf-8")
            shapka = "".join(ln for ln in tekst.splitlines(keepends=True)
                             if ln.startswith("#") or not ln.strip())
            shapka = (shapka[:shapka.rfind("\n\n") + 2]
                      if "\n\n" in shapka else shapka)
            f.write_text(
                shapka + yaml.safe_dump(z, allow_unicode=True,
                                        sort_keys=False, width=88),
                encoding="utf-8")

    print(f"bez-slenhu: переписано {zmineno}, лишилося без правила {lyshylos}")
    for k, v in sorted(reshta.items(), key=lambda x: -x[1])[:10]:
        print(f"   {v:4}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
