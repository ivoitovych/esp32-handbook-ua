#!/usr/bin/env python3
"""Landing a continuous pass: from an executor's dump into the registry.

## Why a separate step

A pass that stays in a temporary directory **does not exist** for the
registry. Until it is landed in `factcheck/evidence/`, no tool sees it,
the gates do not defend it, and the next wave walks the same units again.
Work without landing is work that did not happen.

## The pattern derives itself, and that is the subtlest part

The schema requires a `match` — an expression binding evidence to units.
The project's written laws pull in opposite directions:

* **a wide pattern is more dangerous than a missing one** — it silently
  marks as checked what nobody checked;
* **a long pattern breaks** at the first edit to that sentence.

There is one target between them: **the shortest prefix that is unique
across the whole registry**. That is what is searched for here — grown
word by word until exactly one match remains, and no further.

Numbers are not stripped from the pattern: in many units the number is
what makes them distinctive. But the pattern is **cut before a number**
if uniqueness was reached earlier — and numbers are what mostly get
edited.

## What landing does NOT do

It lands **only** what survived layer 3: the quote was found verbatim in
the named document. A claim without that check never arrives here —
otherwise landing would become a way of legitimising a paraphrase.

Layer 2 — whether the extract genuinely supports the claim — remains with
a person. So every landed file carries a `method` line saying plainly
that `verbatim` here means "the document was obtained, the extract was
machine-checked", not "a maintainer read it and agrees".

    factcheck/tools/sweep_land.py <survivors-file> [--pysaty]
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

import yaml

from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

MIN_SLIV = 4
MAX_SLIV = 14


def ekranuy(s: str) -> str:
    """Literals, but spaces stay flexible.

    The registry and the book wrap lines differently, so a rigid space in
    a pattern is the same trap that killed two sensor evidences.
    """
    # Each word is escaped separately and they are joined by a flexible
    # space. Doing it the other way round does not work: `re.escape`
    # turns a space into `\ `, and substituting on `\s+` eats only the
    # space itself, leaving an orphaned backslash. The first version did
    # exactly that — all 223 patterns came out invalid and matched
    # **nothing**.
    return r"\s+".join(re.escape(w) for w in s.split())


def vzirets_dlya(tekst: str, vsi: list[str]) -> str | None:
    """The shortest prefix that is unique across the whole registry."""
    slova = tekst.split()
    if len(slova) < MIN_SLIV:
        return None
    for k in range(MIN_SLIV, min(len(slova), MAX_SLIV) + 1):
        vz = ekranuy(" ".join(slova[:k]))
        # Uniqueness is tested by **search**, not by `startswith`. A
        # pattern is used by searching, and one unit's prefix may well
        # stand in the middle of another: the first version measured by
        # prefix and let through five patterns up to seven units wide.
        # Measure the way the thing will actually be used.
        r = re.compile(vz)
        if sum(1 for t in vsi if r.search(t)) == 1:
            return vz
    return None


# The writer must write **both** names while a migration is running.
#
# A list of "who reads the old names" counted readers, which is why step
# one looked finished. But a contraction holds not because the old names
# were removed but because **nobody is left to write them**: after the
# contraction the very next landing would have brought them back, one
# order at a time, and the binding snapshot would have been green that
# day and red a week later.
#
# The line below is removed **together** with the contraction run,
# neither earlier nor later.
def obydva(z: dict) -> dict:
    """An evidence record carrying the English names beside the old."""
    MAPA = {"nazva": "title", "zbih": "match", "klas": "status",
            "dzherelo": "source", "cytata": "quote", "sposib": "method",
            "notatka": "note", "shukaty": "look_for",
            "rozrakhunok": "calculation"}
    SLOVO = {"A": "verbatim", "B": "derived", "C": "named-unreachable",
             "D": "arithmetic", "E": "no-external-signal", "F": "unchecked",
             "G": "refuted", "K": "code-context", "L": "looked-not-found"}
    for st, nov in MAPA.items():
        if st in z and nov not in z:
            z[nov] = SLOVO.get(str(z[st]), z[st]) if st == "klas" else z[st]
    return z


def main() -> int:
    import factcheck
    import sample

    p = argparse.ArgumentParser()
    p.add_argument("vyzhyly", type=Path)
    p.add_argument("--pysaty", action="store_true")
    # The filename prefix. **It must differ between waves.** Without it a
    # second landing silently overwrites the first one's files: that is
    # how 335 evidences from a pass became 324, and only a listing
    # noticed.
    p.add_argument("--prefiks", default="prochid")
    a = p.parse_args()

    reyestr: dict[str, dict] = {}
    for klas in factcheck.ALL_CLASSES:
        for u in sample.odynyci(klas):
            u["klas"] = klas
            reyestr[u["id"]] = u
    vsi_teksty = [u["tekst"] for u in reyestr.values()]
    print(f"registry: units {len(reyestr)}")

    zapysy = yaml.safe_load(a.vyzhyly.read_text(encoding="utf-8")) or []
    print(f"survived layer 3: {len(zapysy)}")

    posadka: dict[str, list[dict]] = collections.defaultdict(list)
    nema_odynyci = shyrokyy = vzhe_A = 0
    for z in zapysy:
        oid = str(z.get("odynycya", "")).strip()
        u = reyestr.get(oid)
        if u is None:
            nema_odynyci += 1
            continue
        if u["status"] in ("verbatim", "derived"):
            # The unit already has primary evidence. A second adds
            # nothing and creates two truths about one thing — and
            # exactly that many places to diverge at the next edit.
            vzhe_A += 1
            continue
        vz = vzirets_dlya(u["tekst"], vsi_teksty)
        if vz is None:
            shyrokyy += 1
            continue
        fayl = u["src"].split("/")[-1].split(":")[0].removesuffix(".md")
        posadka[fayl].append(obydva({
            "nazva": f"{oid}: {' '.join(u['tekst'].split()[:8])}",
            "zbih": vz,
            "klas": "A",
            "dzherelo": str(z["source"]).strip(),
            "cytata": str(z["quote"]).strip() + "\n",
            "sposib": (
                "Continuous pass. The document was obtained in session and "
                "the extract checked against it as a substring, "
                "mechanically (`factcheck/tools/sweep_digest.py`). "
                "`verbatim` here means \"the document was obtained, the "
                "quote is exact\", NOT \"a maintainer read it and "
                "agrees\": the semantic layer remains separate work."),
            "notatka": str(z.get("komentar", "")).strip() or "—",
        }))

    vsoho = sum(len(v) for v in posadka.values())
    print(f"landable {vsoho} | already primary {vzhe_A} | "
          f"unit not in the registry {nema_odynyci} | "
          f"no unique prefix {shyrokyy}")

    if not a.pysaty:
        print("\n(dry run; use `--pysaty` to write)")
        return 0

    kudy = ROOT / "factcheck" / "evidence"
    for fayl, zapys in sorted(posadka.items()):
        shlyakh = kudy / f"{a.prefiks}-{fayl}.yaml"
        shapka = (
            f"# Landing {a.prefiks} — {fayl}.\n"
            f"#\n"
            f"# Landed by `factcheck/tools/sweep_land.py`. Only what\n"
            f"# survived layer 3 arrives here: the quote was found in the\n"
            f"# named document verbatim. No unchecked claim is here.\n"
            f"#\n"
            f"# Patterns derived mechanically — the shortest prefix unique\n"
            f"# across the registry. A compromise between two laws: a wide\n"
            f"# pattern lies, a long one breaks.\n\n")
        shlyakh.write_text(
            shapka + yaml.safe_dump(zapys, allow_unicode=True,
                                    sort_keys=False, width=88),
            encoding="utf-8")
    print(f"files written: {len(posadka)} → {kudy}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
