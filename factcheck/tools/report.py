#!/usr/bin/env python3
"""The fact-check of THIS book, as one document.

## Why this exists

The owner opened `factcheck/` and said the directory should hold two
documents: the technology, and the report on the fact-check of the current
book. The first existed. **The second never had.**

Not misplaced — absent. There were thirteen generated reports and five
registries, eighteen files each answering a fragment, and anyone who
wanted the state of the work had to open all eighteen and add them up.
Nobody ever did, which is why nobody noticed that the answer was nowhere.

> A number that exists only as a fragment of a report is not a finding.
> Somebody still has to be the one who adds them up, and if that is the
> reader, it does not happen.

The fragments stay where they are: they are the working output of the
tools that produce them, and each is regenerated on its own schedule.
This assembles the parts of them that answer one question — **how far is
this book checked, by what, and what is left** — into a document a person
can read from the top.

## What it does not do

It computes nothing new. Every number here comes from a tool that already
measured it, and every section names that tool, so a disputed number is
traceable to the thing that produced it in one step.

    factcheck/tools/report.py            write factcheck/REPORT.md
    factcheck/tools/report.py --show     print it without writing
    factcheck/tools/report.py --demo    demonstration on a broken input
"""
from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from repo import ROOT  # noqa: E402  (root is found, not counted)
FC = ROOT / "factcheck"
TARGET = FC / "REPORT.md"
REPORTS = FC / "reports"


def number_from(fname: str, pattern: str, default: str = "—") -> str:
    """One number out of a generated report, by pattern.

    Returns the default rather than raising: a report that has not been
    regenerated yet is a normal state, and a missing number must look
    missing rather than look like zero."""
    p = REPORTS / fname
    if not p.exists():
        return default
    m = re.search(pattern, p.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else default


def registry_state() -> tuple[int, Counter, int]:
    import factcheck
    records = factcheck.zbir_usikh()
    c = Counter(z["klas"] for z in records)
    context = c.get("K", 0)
    return len(records) - context, c, context


def number_from_tool(cmd: list[str], pattern: str, default: str = "—") -> str:
    """A number from a tool that has to be run to produce it."""
    try:
        out = subprocess.run([sys.executable] + cmd, capture_output=True,
                             text=True, cwd=ROOT, timeout=1800).stdout
    except Exception:
        return default
    m = re.search(pattern, out, re.M)
    return m.group(1) if m else default


def assemble() -> str:
    import factcheck
    total, c, context = registry_state()
    checked = sum(c[k] for k in "ABD")
    open_units = c.get("C", 0) + c.get("F", 0) + c.get("G", 0)

    def share(n: int) -> str:
        return f"{n * 100 / total:.1f} %"

    r: list[str] = []
    a = r.append
    a("# The fact-check of this book")
    a("")
    a("> **generated** — `factcheck/tools/report.py`. Editing it by hand only moves the")
    a("> next run's diff, never the state it describes.")
    a("")
    a("What has been checked in *Довідник ESP32*, against what, and what is")
    a("left. The method that produced these numbers — and the reasoning "
      "behind")
    a("every status below — is in `METHOD.md`; this document is only the "
      "state.")
    a("")
    a("## Where the book stands")
    a("")
    a("```")
    a(f"  claim units            {total:>6}   (+ {context} code blocks "
      f"as context)")
    a(f"  checked against a source or by calculation")
    a(f"                         {checked:>6}   {share(checked)}")
    a(f"  closed as a decision   {c.get('E', 0):>6}   {share(c.get('E', 0))}"
      f"   no external signal in the text")
    a(f"  still open             {open_units:>6}   {share(open_units)}")
    a("```")
    a("")
    a("The three lines do not add to the whole, and the gap is deliberate:")
    a(f"**{c.get('S', 0)} units are self-consistent** — checked against "
      f"another")
    a("place in this same book, mechanically and reproducibly. That says")
    a("something checkable about the book and nothing at all about the "
      "world,")
    a("so it is counted in neither column. `METHOD.md`, Part II, says why.")
    a("")
    a("### By status")
    a("")
    a("| Status | Units | Share | What it asserts |")
    a("|---|---:|---:|---|")
    for k in factcheck.CLASSES_OF_UNITS:
        n = c.get(k, 0)
        if not n:
            continue
        a(f"| `{factcheck.LETTER_TO_STATUS[k]}` | {n} | {share(n)} | "
          f"{factcheck.CLASS_TEXT[k]} |")
    a("")
    a("## The weakest number on this page")
    a("")
    signal = c.get("E", 0)
    a(f"`no-external-signal` is {share(signal)} of the book — the largest")
    a("single status, and the only one that certifies itself. It is assigned")
    a("mechanically, for want of a digit, identifier or unit in the text, "
      "and")
    a("it reads to a reader as *no source exists*. Those are not the same")
    a("thing.")
    a("")
    a(f"A random sample of "
      f"{number_from('MEASURE-NO-SIGNAL.md', r'\\*\\*(\\d+)\\*\\*')} units "
      f"measured how often that")
    a("reading is wrong. The measurement, its seed and its sample are in")
    a("`reports/MEASURE-NO-SIGNAL.md`; the sweep that harvested sources from")
    a("the same status is in `reports/SWEEP-NO-SIGNAL.md`, and **its "
      "percentage")
    a("may not be carried over** — its sample was picked where the light "
      "was.")
    a("")
    a("## What was found")
    a("")
    a("Corrections to the book that came out of this work are recorded per")
    a("pass in `METHOD.md`, Part I. Refuted claims and the patterns that")
    a("caught them are in `reports/REFUTED.md`.")
    a("")
    a("## Sources")
    a("")
    a("```")
    a(f"  evidence records       "
      f"{len(list((FC / 'data' / 'evidence').glob('*.yaml'))):>6}")
    a(f"  quotes checked verbatim against the source document")
    a(f"                         "
      f"{number_from('QUOTES.md', r'\\*\\*(\\d+)\\*\\*'):>6}   reports/QUOTES.md")
    a("```")
    a("")
    a("Sources that cannot be reached from the environment this book is made")
    a("in are not dropped and do not pretend to have been checked: they")
    a("become a hand-off in `reports/UNREACHABLE-SOURCES.md`, with the")
    a("document, what to look for in it, and the claims that depend on it.")
    a("")
    a("## Runs")
    a("")
    a("Every helper wave is recorded in `reports/RUNS.md` with the")
    a("`order_version` it was given, so two waves are comparable exactly "
      "when")
    a("they were told the same thing. A wave whose result did not survive")
    a("that comparison is recorded as not a result, which is what the ledger")
    a("is for.")
    a("")
    a("## What is left")
    a("")
    a(f"{open_units} units are open: {c.get('F', 0)} never looked at,")
    a(f"{c.get('C', 0)} waiting on a source that cannot be reached from here.")
    a("")
    a("The registry is complete by construction — every line of the book has")
    a("a record, whether or not anyone has worked on it — so this number")
    a("shrinks only from work and grows only from the book. That is the one")
    a("property that lets it prove completeness rather than effort.")
    return "\n".join(r) + "\n"


def demo() -> int:
    """Demonstration on a broken input.

    The thing that can break silently here is `number_from()`: a report was
    not regenerated, the pattern did not match, and a zero went into the
    document instead of a number. A zero taken from something not found
    reads exactly like a measurement."""
    ok = True

    def check(name: str, holds: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if holds else '✗'} {name}: {holds}")
        ok &= holds

    check("a missing report gives a dash, not a zero",
          number_from("NEMAYE-TAKOHO.md", r"(\d+)") == "—")
    check("a pattern that does not match gives a dash, not a zero",
          number_from("QUOTES.md", r"^ЦЬОГО ТАМ НЕМАЄ (\d+)$") == "—")
    check("a present number is read",
          number_from("QUOTES.md", r"\*\*(\d+)\*\*").isdigit())
    t = assemble()
    check("the document carries its kind marker", "> **generated**" in t)
    check("the document is not empty", len(t.splitlines()) > 40)
    print("\nfailures:", 0 if ok else 1)
    return 0 if ok else 1


def main() -> int:
    if "--demo" in sys.argv:
        return demo()
    t = assemble()
    if "--show" in sys.argv:
        print(t)
        return 0
    TARGET.write_text(t, encoding="utf-8")
    print(f"report: {TARGET.name} written, {len(t.splitlines())} lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())
