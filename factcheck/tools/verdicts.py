#!/usr/bin/env python3
"""Helper verdicts: one vocabulary, and one place that knows the old one.

## Why this file exists

The technology is meant to be lifted onto another book, by people who do
not read Ukrainian. A verdict spelled `ne_znayshov` is neither English nor
Ukrainian — it is a Ukrainian word in Latin letters, and it is the first
thing a new maintainer meets, because it is what the helpers write.

So the current vocabulary is English. This file holds it, and holds the
translation from the old spellings.

## Why the old spellings can never be deleted

`factcheck/archive/` is frozen: nothing there is renamed or translated,
because it is the record of what was actually done on the day it was done.
It holds about 1 500 answers in the old words. A reader that stopped
understanding them would not be tidier — it would be unable to read the
project's own history.

So this is not a migration with an end. It is a **boundary**: old words in,
one vocabulary out, and everything past the boundary knows exactly one set.

## Why it is not three copies

It was. `intake_f` had the map; `contest_e` had its own table; `sample`
grew a third on 2026-09-14, written by someone (me) who had not noticed
the first two. Three copies of a verdict table is the same defect this
project already recorded when a work order printed three verdict tables at
a helper — and the cost is identical: they drift, and the one that drifts
is the one nobody is looking at.

    factcheck/tools/verdicts.py --self-check
"""
from __future__ import annotations

import sys

# The current vocabulary. `[VERDICTS-EXTERNAL]` and `[VERDICTS-CONTEST-E]`
# in METHOD.md are the normative statements of what each one requires;
# this is only the set of legal words.
VERDICTS = (
    "confirmed",          # address plus a verbatim quote
    "disputes",           # the source contradicts the handbook
    "not_found",          # the document was read, the passage is not in it
    "unreachable",        # the document does not come down from here
    "advice",             # not obtained, but you can say where it would be
    "truly_none",         # looked; there is genuinely no external referent
    "absent_from_source",  # the document's SILENCE is itself the proof
)

# Old spellings → current. Read-only: nothing new is written in these.
#
# Three separate old vocabularies are folded in here, and they were never
# one set:
#   · the F queue      pidtverdzheno / sperechayetsya / ne_znayshov / …
#   · the E contest    znayshov / ideya / spravdi-e
#   · layer 3          zbihayetsya / rozbizhnist / ne_znaydeno
OLD_VERDICTS = {
    # F queue
    "pidtverdzheno": "confirmed",
    "sperechayetsya": "disputes",
    "ne_znayshov": "not_found",
    "nedosyazhne": "unreachable",
    "porada": "advice",
    "spravdi-e": "truly_none",
    "spravdi_e": "truly_none",
    # contesting `no-external-signal`
    "znayshov": "confirmed",
    "ideya": "advice",
    # layer 3
    "zbihayetsya": "confirmed",
    "rozbizhnist": "disputes",
    "ne_znaydeno": "not_found",
}

# Old field names of a helper's answer → current.
OLD_FIELDS = {
    "odynycya": "unit",
    "verdykt": "verdict",
    "dzherelo": "source",
    "cytata": "quote",
    "komentar": "comment",
    "potribno": "needed",
    "chomu": "why",
    "susidnye": "neighbours",
    "dyvyvsya": "looked_at",
}


def verdict_of(r: dict) -> str:
    """The verdict of one answer, in current words, whatever it arrived in.

    Returns the raw string unchanged when it is neither current nor known
    as old: a gate must be able to say "that is not a verdict", and a
    silent "" would read as "the helper gave no answer".
    """
    raw = str(r.get("verdict", r.get("verdykt", ""))).strip()
    return OLD_VERDICTS.get(raw, raw)


def to_english(r: dict) -> dict:
    """One answer in current field names and current verdict words.

    A gate has no business punishing a helper for the language of the
    order it was handed. Translating here is not indulgence, it is the
    boundary: past it, the rest of the pass knows exactly one vocabulary.
    """
    out = {}
    for k, v in r.items():
        out[OLD_FIELDS.get(k, k)] = v
    if "verdict" in out:
        out["verdict"] = OLD_VERDICTS.get(str(out["verdict"]).strip(),
                                          out["verdict"])
    return out


def self_check() -> int:
    bad = 0
    cases = [
        ({"verdykt": "ne_znayshov"}, "not_found", "old F-queue word"),
        ({"verdict": "confirmed"}, "confirmed", "already current"),
        ({"verdykt": "znayshov"}, "confirmed", "E-contest word"),
        ({"verdykt": "zbihayetsya"}, "confirmed", "layer-3 word"),
        ({"verdict": "nonsense"}, "nonsense", "unknown passes through"),
        ({}, "", "no verdict at all"),
    ]
    for r, want, name in cases:
        got = verdict_of(r)
        ok = got == want
        bad += not ok
        print(f"   {'✓' if ok else '✗ FAIL'} {name}: {got!r}, expected {want!r}")

    # Every old word must land on a legal current one, or the translation
    # quietly invents a verdict no gate accepts.
    stray = sorted(set(OLD_VERDICTS.values()) - set(VERDICTS))
    print(f"   {'✓' if not stray else '✗ FAIL'} every old word maps to a "
          f"legal verdict: {stray or 'yes'}")
    bad += bool(stray)

    r = to_english({"odynycya": "T-01-001", "verdykt": "pidtverdzheno",
                    "cytata": "x", "chomu": "y"})
    want = {"unit": "T-01-001", "verdict": "confirmed", "quote": "x", "why": "y"}
    ok = r == want
    bad += not ok
    print(f"   {'✓' if ok else '✗ FAIL'} a whole old answer translates: {r}")

    print(f"\nverdicts: {len(VERDICTS)} current words, "
          f"{len(OLD_VERDICTS)} old spellings understood; failures {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(self_check() if "--self-check" in sys.argv else self_check())
