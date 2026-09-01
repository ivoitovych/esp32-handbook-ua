#!/usr/bin/env python3
"""A snapshot of bindings: which units each evidence attaches to **today**.

## Why this exists

The card format changes: a unit stops being a rendering
(`BME280 · Адреса → 0x76`) and becomes the book's verbatim row
(`| BME280 | `0x76`, `0x77` | … |`).

The `match` patterns were written against the **rendering** — all 1337
evidences, of which 1265 attach to cells. After the format changes not
one of them would match.

But an evidence is bound not to the **text** but to the **unit**. The
text is only a way of naming it. So if we record which unit each evidence
names **now**, then after the change we can rebuild the pattern from the
new text of that same unit — and **prove** the binding is the same.

> The work is not redone, it moves. And the move is checkable: the
> snapshot before and the snapshot after must agree unit for unit.

## Why the snapshot must be taken BEFORE

After the format changes the old patterns match nothing, and there is
nobody left to ask what they used to match. The snapshot is the only
carrier of that knowledge, and it has to be in git before anything
changes.

This is the same thing I was caught by earlier the same day: I landed a
wave having deleted the previous one's files, and 335 evidences became
324. `git` saved it that time. Here there would be nothing to save from —
the rendering would leave the tree entirely.

## Why the anchor is content, not a number

The first snapshot was written by `id` (`T-20-050`), and on the very
first full regeneration of the registry it showed **34 evidences that had
"lost" their units**. Nothing had been lost.

`id` is `T-<file>-<ordinal>`. It shifts with any edit to the book
**above** the unit: I fixed a paragraph in `20-bekap.md`, and everything
below moved by one. The evidences' patterns matched the same sentences —
under different numbers, and comparing by number called that a loss.

Translating the same bindings to `sha` (the hash of the unit's normalised
text) gave **0 of 1337 with a loss**.

> A number is the address at which a unit can be found today. A hash is
> what it IS. A snapshot must hold on to the second: otherwise it cries
> out at every edit to the book, and a signal like that stops being
> looked at — and a real loss goes past with the rest.

The same law is already written about the card (a line number is a
locator, not an anchor). Here it appeared a second time, from the other
side, and cost half an hour to diagnose. So it stands in two places
deliberately.

    factcheck/tools/snapshot.py <out.json>           take one (by `sha`)
    factcheck/tools/snapshot.py <out.json> --compare compare with the
                                                     current state
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import yaml

from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

# `T-45-001` is a unit's number; `f98283f2` is the hash of its content.
# The first character tells you which one a snapshot was written in.
RE_ID = re.compile(r"[A-Z]-\d+-\d+")


def collect(by: str = "sha") -> dict[str, list[str]]:
    """Key: `evidence-file::name`; value: the unit anchors, ordered.

    The anchor is `sha`, not `id`. On the difference, see the module
    docstring, "Why the anchor is content, not a number".
    """
    import factcheck
    import sample

    units = [u for k in factcheck.ALL_CLASSES for u in sample.odynyci(k)]

    # A record's key must survive the file being reordered, so it carries
    # an ordinal: names repeat within a file, and without the ordinal two
    # evidences would merge into one.
    records: list[dict] = []
    for f in sorted((ROOT / "factcheck" / "evidence").glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for i, r in enumerate(z):
            if not isinstance(r, dict):
                continue
            nz = factcheck.nazva_zapysu(r)[:60]
            r["_znimok_klyuch"] = f"{f.name}::{i}::{nz}"
            records.append(r)

    zv: dict[str, list[str]] = {k["_znimok_klyuch"]: [] for k in records}
    # We ask the **same** selector the registry generator uses, and we ask
    # it from the unit's side, not the record's.
    #
    # The difference is not cosmetic. `vsi_kandydaty` has precedence: if
    # any record covers a unit by exact `sha`, the patterns of other
    # records no longer apply to it. A snapshot that counted patterns
    # separately would show a binding that does not exist — and would go
    # quiet exactly when bindings move from pattern to hash, which is
    # exactly when it is needed.
    for u in units:
        for z in factcheck.vsi_kandydaty(records, u["sha"], u["tekst"]):
            zv[z["_znimok_klyuch"]].append(u[by])
    return {k: sorted(v) for k, v in zv.items()}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("out_file", type=Path)
    p.add_argument("--compare", "--zvirty", dest="compare",
                   action="store_true")
    a = p.parse_args()

    by = "sha"
    if a.compare and a.out_file.exists():
        sample_value = next((v[0] for v in
                       json.loads(a.out_file.read_text(encoding="utf-8")).values()
                       if v), "")
        if RE_ID.fullmatch(sample_value):
            by = "id"
            print("WARNING: this snapshot was written by `id`. A unit's "
                  "number shifts with any edit to the book above it, so "
                  "renumbering will be shown here as loss. Compare a "
                  "snapshot taken by `sha`.")

    now = collect(by)
    if not a.compare:
        a.out_file.write_text(
            json.dumps(now, ensure_ascii=False, indent=1, sort_keys=True),
            encoding="utf-8")
        bindings = sum(len(v) for v in now.values())
        idle = sum(1 for v in now.values() if not v)
        print(f"snapshot: evidences {len(now)}, bindings {bindings}, "
              f"of them idle {idle} → {a.out_file}")
        # Нуль доказів — не «нічого не прив'язано», а «нема чого знімати».
        # Знімок порожнього дерева виглядає як знімок, і звірка з ним
        # згодом покаже «втрачено все» або «не змінилося нічого» —
        # залежно від того, з якого боку дивитися.
        if not now:
            print("   ✗ no evidences collected — this snapshot would record "
                  "nothing and\n     compare clean against anything")
            return 1
        return 0

    was = json.loads(a.out_file.read_text(encoding="utf-8"))
    gone = [k for k in was if k not in now]
    added = [k for k in now if k not in was]
    changed = {k: (was[k], now[k]) for k in was
               if k in now and was[k] != now[k]}
    lost = {k: sorted(set(v[0]) - set(v[1]))
                 for k, v in changed.items() if set(v[0]) - set(v[1])}

    print(f"evidences in the snapshot {len(was)}, now {len(now)}")
    print(f"  records gone       {len(gone)}")
    print(f"  records added      {len(added)}")
    print(f"  bindings changed   {len(changed)}")
    print(f"  **units lost**     {len(lost)}")
    for k, v in list(lost.items())[:12]:
        print(f"     ✗ {k[:70]}\n        lost: {', '.join(v[:6])}")
    return 1 if (lost or gone) else 0


if __name__ == "__main__":
    sys.exit(main())
