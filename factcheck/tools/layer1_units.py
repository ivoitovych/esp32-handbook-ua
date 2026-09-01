#!/usr/bin/env python3
"""Layer 1 over the registry's UNITS — not over its cards; cf. `layer1.py`.

There are two of these, and not by oversight. `layer1.py` asks whether a
card presents the book honestly to a reader who has not seen the book;
this file asks whether a unit of the registry comes from the book at all.
The first is about presentation, the second about provenance. The first
found 58 broken contexts that the second cannot see in principle.

## What already existed, and what was missing

The registry is **generated** from the book (`factcheck.py sketch`), so
for prose the texts match by construction. Evidence is bound by the `sha`
hash, and editing a wording detaches the evidence — we have seen that
work: when M1 rewrote the line about the DS18B20's tolerance, two
evidences detached on their own.

So layer 1 is partly automatic. But three holes remained.

**First.** `factcheck.py stale` was named "records whose text in the book
changed since the evidence", and checked only **whether the file exists**.
The invariant was considered guarded and was guarded by nobody — the same
kind M1 found in his own `vorota`.

**Second.** Above each unit stood the heading "**The book says,
verbatim:**". For prose that is true. For a **table cell** it is not; the
book says

    | BME280 | `0x76`, `0x77` | ... |

and the registry presents

    BME280 · Адреса → `0x76`, `0x77`

That is a rendering, not a quote. The word "verbatim" there was untrue,
and it is what produced the false-alarm kind "a cell with no context".

**Third.** Nothing checks that the **splitter** itself did not err. If it
eats half a sentence or shifts a line number, the registry is internally
consistent and wrong.

## What this script does

For each unit it takes `src:line` from the registry itself, opens the
book, and asks:

* **prose** — does the unit's text stand in the book verbatim;
* **cell** — do all of the cell's values occur in the book's line;
* **any** — does the line exist at all (the file may have shrunk).

## It was examining nothing

This tool matched on the card heading `**Книга каже, дослівно:**`. That
heading was renamed in the generator — the very rename described under
"Second" above — and this pattern was not. It has been reporting

    одиниць 0 · ТЕКСТУ НЕМАЄ В КНИЗІ: 0

ever since: three zeros and exit 0, which reads exactly like a clean run.
The heading it looks for is now taken from the generator rather than
copied here, and zero units is a failure.

    factcheck/tools/layer1_units.py [--all]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)

GROUPS = config.groups()

# The heading is asked of the generator, not copied. A copy of it here is
# what made this tool silent: the generator renamed the heading and the
# copy did not follow.
def _claim_heading() -> str:
    import factcheck
    return getattr(factcheck, "CLAIM_HEADING", "Твердження, коротко")


RE_CARD = re.compile(
    r"<!-- fc id:(\S+) sha:(\S+) src:(\S+?):(\d+) status:(\S+) -->\n"
    r"### \S+ · (\S+) · [^\n]*\n\n\*\*" + re.escape(_claim_heading())
    + r"\*\*\n\n((?:> [^\n]*\n)+)")


def normal(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main(argv: list[str]) -> int:
    show_all = "--all" in argv or "--vsi" in argv
    book: dict[str, list[str]] = {}
    whole: dict[str, str] = {}
    shifted: list[str] = []
    faults: list[tuple[str, str, str]] = []
    n = prose = cells = 0

    for g in GROUPS:
        for f in sorted((config.cards_root() / g).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            for m in RE_CARD.finditer(text):
                ident, sha, src, ln, status, kind, quote = m.groups()
                n += 1
                p = ROOT / src
                if src not in book:
                    book[src] = (p.read_text(encoding="utf-8").split("\n")
                                 if p.exists() else [])
                lines = book[src]
                i = int(ln) - 1
                if not lines:
                    faults.append((ident, "FILE MISSING", src))
                    continue
                if i >= len(lines):
                    faults.append((ident, "LINE MISSING (file is shorter)",
                                   "%s:%s, %d lines" % (src, ln, len(lines))))
                    continue
                t = normal("\n".join(x[2:] for x in quote.strip().split("\n")))
                # a window: a sentence may span several lines of the book
                window = normal(" ".join(lines[max(0, i - 1):i + 6]))
                # Two different kinds, and confusing them is expensive.
                # The text may be in the book but NOT ON THAT LINE — that
                # is not a fault of the text but a stale rendering: the
                # book was edited after it, and every number below the
                # edit shifted.
                #
                # The first run reported 1317 "divergences" exactly this
                # way, and I nearly announced that sixteen per cent of the
                # registry was false. The text was there; the number moved.
                entire = whole.setdefault(src, normal(" ".join(lines)))
                if kind == "proza":
                    prose += 1
                    if t in window:
                        pass
                    elif t in entire:
                        shifted.append(ident)
                    else:
                        faults.append((ident, "TEXT NOT IN THE BOOK AT ALL",
                                       t[:70]))
                elif kind == "komirka":
                    cells += 1
                    # a cell's values are what follows the arrow
                    parts = [normal(x) for x in re.split(r"·|→", t) if normal(x)]
                    lost = [c for c in parts if c not in window]
                    if lost:
                        if all(c in entire for c in lost):
                            shifted.append(ident)
                        else:
                            faults.append(
                                (ident, "CELL: values not in the book",
                                 "; ".join(c for c in lost
                                           if c not in entire)[:70]))

    for ident, kind_, detail in (faults if show_all else faults[:25]):
        print("   %-12s %-34s %s" % (ident, kind_, detail))
    if not show_all and len(faults) > 25:
        print("   ... and %d more" % (len(faults) - 25))
    print("\nunits %d (prose %d, cells %d)" % (n, prose, cells))
    print("  text present, LINE NUMBER shifted: %d — the rendering is stale"
          % len(shifted))
    print("  TEXT NOT IN THE BOOK: %d — this is the real divergence"
          % len(faults))
    # Zero units is not "no divergences" — it is "nowhere to look".
    if n == 0:
        print("   ✗ NOT ONE unit was examined. That is not clean; it means "
              "the card\n     heading this tool matches on no longer "
              "matches what the generator prints.")
        return 1
    return 1 if faults else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
