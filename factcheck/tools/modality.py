#!/usr/bin/env python3
"""Modality: a prescription in the book against a permission in the source.

## A kind of fault none of the three layers caught

Found by a two-dollar helper, not by a tool. Unit `T-11-062`:

    the book:   «Саме він має лежати в git, а не `sdkconfig`.»
    the source: "The sdkconfig file **may or may not** be added to the
                 source control system … It is **recommended** to commit
                 sdkconfig.defaults"

The quote is verbatim, the source is real, the fact is right — **all
three layers pass**. What differs is only the **modality**: the source
permits, the book prescribes.

> This is not a fault of fact nor a fault of source. It is a prescription
> presented as though documented — and layer 3 cannot catch it by
> construction, because it compares characters, not the force of a claim.

Such a prescription is not necessarily wrong: a handbook exists partly to
give a reasoned position. But the reader must be able to tell "the
documentation requires this" from "the author holds this, and here is
why".

## Why this is a report, not a gate

The first version of the pattern gave **50 matches**, and the first two
checked were both false — instructively so:

    the book:   «Потрібне зниження **обов'язково**»
    the source: "Stresses above … **may cause** permanent damage"

`may` here is not a permission but a **warning**. The book's
"обов'язково" is entirely justified by the 3.6 V limit.

## Three rounds of filtering, and what they cost

| Version | Matches | False | What was filtered out |
|---|---:|---:|---|
| first | 50 | ~48 | `may cause` — a warning, not a permission |
| second | 6 | 4 | "має ціну", "має бути" — possession and expectation |
| third | 2 | 1 | `Recommended` in a datasheet **table heading** |
| current | **1** | 0 | — |

So of fifty initial matches exactly **one** is real, and seeing it took
three corrections to the tool — each time on its own findings, not on
reasoning.

That is the price of this kind of check: **it looks for a difference in
the force of a claim, and force is a property of language.** The three
filters above are not tricks but three ways language imitates modality
where there is none.

The last of them is worth knowing separately. `T-06-027`, the book: "a
supply for an ESP32 with Wi-Fi **must** deliver at least 1 A" — while the
datasheet gives a minimum of 0.5 A. It looks like a prescription against
the source. But the very next paragraph the book says: "500 mA is not
somebody's naivety, it is Espressif's own rated minimum", and explains
why it advises more.

> **A deliberate divergence from the source, stated aloud, is not a fault
> of modality — it is what a handbook is written for.** The fault is a
> divergence the reader is not told about.

A person still has to judge whether a prescription is justified or should
be softened. So this is a line in a report, not a stop on the release.

## The words are the book's, not the tool's

The patterns live in `factcheck/book.yaml`. They are Ukrainian here
because this book is; on another book they are different words, and a
tool carrying these would match nothing and print a confident zero.
Absent configuration means the check says so and skips.

    factcheck/tools/modality.py [-v]
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

# A permission in the source. **Careful with `may`**: `may cause`,
# `may result`, `may lead` are warnings about a consequence — the
# opposite of a permission. The first version did not tell them apart and
# gave 50 matches instead of 6.
#
# `Recommended` in a **table heading** ("Table 5-2. Recommended Power
# Supply Characteristics") is the name of a datasheet section, not the
# modality of a claim. The third kind of false positive, found on
# `T-06-027`.
RE_HEADING = re.compile(r"[Rr]ecommended\s+[A-Z]\w+\s+[A-Z]\w+")

RE_PERMISSION = re.compile(
    r"\b(?:it is )?recommended\b"
    r"|\bmay or may not\b"
    r"|\boptional(?:ly)?\b"
    r"|\bmay be\b(?!\s+(?:damaged|destroyed))"
    r"|\bcan optionally\b"
    r"|\bif desired\b"
    r"|\bis not required\b", re.I)


def main() -> int:
    import factcheck
    import sample

    words = config.modality()
    if not words:
        print("modality: no `modality` block in factcheck/book.yaml — the "
              "check is SKIPPED,\n   not passed. The words that carry a "
              "prescription are the book's language.")
        return 0
    re_prescriptive = re.compile(words["prescriptive"], re.I)
    re_not = (re.compile(words["not_prescriptive"], re.I)
              if words.get("not_prescriptive") else None)

    units = [u for k in factcheck.ALL_CLASSES for u in sample.odynyci(k)]
    found = []
    for f in sorted((ROOT / "factcheck" / "evidence").glob("*.yaml")):
        try:
            recs = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for r in recs:
            if (not isinstance(r, dict)
                    or factcheck.status_of(r) not in ("verbatim", "derived")):
                continue
            quote = str(r.get("quote") or "")
            m = RE_PERMISSION.search(quote)
            if not m or RE_HEADING.search(quote):
                continue
            try:
                rx = re.compile(str(r.get("match", "")))
            except re.error:
                continue
            for u in units:
                if (rx.search(u["tekst"])
                        and re_prescriptive.search(u["tekst"])
                        and not (re_not and re_not.search(u["tekst"]))):
                    found.append((u["id"], f.name, u["tekst"], m.group(0)))

    # Нуль одиниць — не «нуль розходжень». Порожній реєстр друкує те саме.
    if not units:
        print("   ✗ no units read at all — this is not a clean result")
        return 1

    if "-v" in sys.argv:
        for uid, fname, text, word in found:
            print(f"   · {uid}: «{word}» in the source, a prescription in "
                  f"the book")
            print(f"        {text[:96]}")
            print(f"        ← {fname}")
    print(f"modality: prescriptions against a permission in the source: "
          f"{len(found)} — a person judges; this is not an error in itself")
    return 0


if __name__ == "__main__":
    sys.exit(main())
