#!/usr/bin/env python3
"""Measuring `unchecked`: how much of what was never checked is wrong.

## Why this is separate from measuring `no-external-signal`

The questions differ, and confusing them is expensive.

`no-external-signal` carried a **verdict**: "no external source exists".
Measuring it tested that verdict — is it true that none exists.

`unchecked` carries no verdict at all. It is simply work not done: nobody
got to these lines. So the question is direct — **is what the book says
correct** — and among the verdicts appears one the earlier order did not
have: `sperechayetsya`, disputes.

That one is the point. Everything else is bookkeeping.

## What a random sample buys here

A number the book has never had: **the error rate among the unchecked**.

The book prints how much has been checked, and says honestly that the
rest has not. But "not checked" says nothing about how much of it is
wrong. The reader is entitled to know whether that is one per cent or
twenty.

The estimate may be carried to the whole `unchecked` population precisely
because the sample is random — and **only** because of that. A percentage
from a hand-assembled order confers no such right (see `METHOD.md`
Part II, "What makes `no-external-signal` dangerous").

## Why a claimed refutation is checked twice

A helper under pressure to "find an error" manufactures errors as
reliably as it manufactured sources under pressure to "find a source": in
one evening 18 were claimed and **none** held.

So every `sperechayetsya` passes layer 3 (does the quote stand in the
document) and **the maintainer's own reading** (is it about this). None
enters the report as a finding until it has passed both.

    factcheck/tools/measure_f.py <dump-directory>
"""
from __future__ import annotations

import collections
import re
import math
import sys
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402

import helper_dumps  # noqa: E402

REPORT = ROOT / "factcheck" / "reports" / "MEASURE-UNCHECKED.md"

EMPTY_REPORT = """# Measuring `unchecked` — the wave is rejected

**Generated** by `factcheck/tools/measure_f.py`.

All **{total}** records in this wave cited **the book itself**. No
external testimony was obtained, so there is nothing to measure.

## What happened

Helpers took the book's sentence, quoted in the order itself, substituted
the handbook repository's address, and wrote `pidtverdzheno`. One of them
described it plainly in its report: "all confirmed in manual files".

## Why this is the order's fault, not the helpers'

Compare the order for `no-external-signal`. There **the cheapest answer
was the honest one**: `spravdi-e` asserts nothing — "looked, there is no
external referent". A helper taking the path of least resistance told the
truth.

In the order for `unchecked` the cheapest answer turned out to be
`pidtverdzheno`, and that **asserts**. The book's text was right there in
the order; to "confirm" it you only had to copy it back. Laziness stopped
being safe.

> **Law.** The cheapest answer in an order must be the one that asserts
> nothing. Otherwise the order converts carelessness into untruth.

The prohibition "the book is not a source for itself" stood in the order
in words and held nothing: a verbal prohibition is powerless against an
action cheaper than the work. It is now a **gate** — an address pointing
at the handbook is rejected mechanically.
"""
CANDIDATES = ROOT / "factcheck" / "work" / "queues" / "measure-f-candidates.yaml"

LABELS = {
    "pidtverdzheno": "The book is confirmed",
    "sperechayetsya": "The source disputes the book",
    "ne_znayshov": "The document exists, the passage does not",
    "nedosyazhne": "The document is unreachable from here",
}


# A source pointing at the book itself. A gate, not advice.
#
# The prohibition "the book is not a source for itself" stood in the order
# in words, and the very first `unchecked` wave violated it **82 times out
# of 161**: helpers took the book's sentence from the order, substituted
# the handbook repository's address, and wrote `pidtverdzheno`.
#
# A verbal prohibition is powerless here by construction: it asks people
# not to do the thing that is cheaper than the work. Hence a mechanical
# check of the address.
RE_SAMA_KNYHA = re.compile(
    r"esp32-handbook"           # the handbook repo under any owner
    r"|ivoitovych|voytovych"    # including ones invented from the author's name
    r"|(?:^|/)(?:%s|factcheck)/" % "|".join(config.groups()),
    re.I)


def no_source(z: dict) -> bool:
    """Not an address, not testimony.

    An empty field, or a path instead of a URL
    (`manual/01-platforma.md`), or the name of a book file. In the first
    `unchecked` wave there were **104 of 224** — nearly half, and all of
    them under `pidtverdzheno`.
    """
    d = str(z.get("source", "")).strip()
    return not d or not d.startswith("http")


def did_not_look(z: dict) -> bool:
    """`ne_znayshov` with no document named is "did not look", not "did
    not find".

    ## Why this is a category of its own rather than plain `ne_znayshov`

    The law "the cheapest answer must assert nothing" saved the
    **registry**: after the order was rewritten, a careless helper writes
    `ne_znayshov` and no false record comes of it.

    But it does not save the **measurement**. A helper who opened no
    document and wrote "not found" twenty-five times gives a flawlessly
    harmless and flawlessly wrong statistical result: the share of
    "nothing is checkable" shoots up, and the book looks worse than it is.

    Found on the very first run of the rewritten order: one helper of ten
    returned 25 of 25 `ne_znayshov` in 17 tool calls, and in not one
    record named the document it had looked at. In the reason field, a
    judgement about the **kind of claim** ("a high-level recommendation,
    not a specification") — that is, an answer taken from the batch
    itself.

    Hence the requirement: `ne_znayshov` must name **where** the search
    happened. Without that the record is neither a finding nor evidence
    of the absence of one.
    """
    return (str(z.get("verdykt")) == "ne_znayshov"
            and not str(z.get("source", "")).strip())


def wilson(k: int, n: int) -> tuple[float, float]:
    """A 95 % Wilson interval. Near zero the normal approximation lies."""
    if not n:
        return (0.0, 0.0)
    p, z = k / n, 1.96
    seredyna = (p + z * z / (2 * n)) / (1 + z * z / n)
    pivshyryna = (z / (1 + z * z / n)) * math.sqrt(
        p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, seredyna - pivshyryna), min(1.0, seredyna + pivshyryna))


def population() -> int:
    import sample
    return len(sample.odynyci("unchecked"))


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    records, repaired, broken = helper_dumps.read_dir(Path(sys.argv[1]))
    n = len(records)
    if not n:
        print("measure_f: no dumps found")
        return 1
    # A gate before the counting: a record citing the book itself counts
    # as nothing at all. Not as a refutation, not as a confirmation, not
    # as "not found" — it is **void**, because it contains no external
    # testimony whatsoever.
    #
    # `ne_znayshov` with no document is filtered out **first**: otherwise
    # it would land in `no_source` and look like the same violation as an
    # invented source. These are different failures: one asserts an
    # untruth, the other does no work.
    not_done = [z for z in records if did_not_look(z)]
    records = [z for z in records if z not in not_done]
    self_refs = [z for z in records
                      if no_source(z)
                      or RE_SAMA_KNYHA.search(str(z.get("source", "")))]
    records = [z for z in records if z not in self_refs]
    if not records:
        REPORT.write_text(EMPTY_REPORT.format(
            total=len(self_refs)), encoding="utf-8")
        print(f"measure_f: ⚠ WAVE VOID — all {len(self_refs)} records "
              f"cite the book itself → "
              f"{REPORT.relative_to(ROOT)}")
        return 1

    # `n` is **recomputed after the gates**. The first version counted it
    # before them — and the report would have printed "234 answers" while
    # working with 49. That is, a tool written against inflated reporting
    # would itself have inflated its reporting.
    n = len(records)
    c = collections.Counter(str(z.get("verdykt", "?")) for z in records)

    # Layer 3 on everything that carries a quote, not only on refutations.
    candidates = [{"title": str(z.get("odynycya", "?")),
             "source": str(z.get("source", "")).strip(),
             "quote": str(z.get("quote", "")),
             "verdykt": str(z.get("verdykt", "")),
             "zvidky": z.get("_fayl", "?")}
            for z in records if str(z.get("quote", "")).strip()]
    CANDIDATES.write_text(
        "# Candidates from the `unchecked` measurement. **Not a registry.**\n"
        + yaml.safe_dump(candidates, allow_unicode=True, sort_keys=False),
        encoding="utf-8")

    states: dict[str, str] = {}
    if candidates:
        try:
            import layer3
            naslidky, _ = layer3.perevirka(True, [CANDIDATES])
            states = {str(x.get("nazva")): str(x.get("stan"))
                     for x in naslidky}
        except ImportError:
            pass

    disputes = [z for z in records if str(z.get("verdykt")) == "sperechayetsya"]
    disputes_ok = [z for z in disputes
                  if states.get(str(z.get("odynycya"))) == "ok"]
    population_n = population()
    low, high = wilson(len(disputes_ok), n)

    r = [f"""# Measuring `unchecked` — how much of it is actually wrong

> **Did not look: {len(not_done)} records** — the verdict `ne_znayshov`
> with no document named. That is not "no source exists" but "did not
> search": such a record enters neither the numerator nor the denominator.
>
> **Rejected by the gates: {len(self_refs)} records of
> {len(self_refs) + n}.** These name the book itself as the "source", or
> a path instead of an address, or nothing. They count as nothing at all —
> they contain no external testimony by construction.

**Generated** by `factcheck/tools/measure_f.py`. The order is in
`factcheck/reports/BRIEF-SAMPLE.md`, and the sampling seed with it.

`unchecked` means "not yet checked": nobody got to these lines. The
question is not about a verdict but direct: **is what the book says
correct**.

The sample is **random**, so the share may be carried to the whole
`unchecked` population — and only for that reason.

## Result

Answers: **{n}** out of {population_n} `unchecked` units.

| Verdict | Count | Share |
|---|---|---|"""]
    for k in ("pidtverdzheno", "sperechayetsya", "ne_znayshov",
              "nedosyazhne"):
        v = c.get(k, 0)
        r.append(f"| {LABELS[k]} | {v} | {v / n:.0%} |")
    r.append("")

    r.append(f"""
## Refutations: {len(disputes)} claimed, {len(disputes_ok)} survived layer 3

A claimed refutation is **not yet a finding**. A helper under pressure to
"find an error" manufactures errors as reliably as it manufactured
sources under pressure to "find a source": in one evening 18 were claimed
and none held.

So each passes two checks: the mechanical one (does the quote stand in
the document) and the personal one (is it about this). Below are those
that passed the first. The second is done by a maintainer, and until then
none of them is grounds for editing the book.
""")

    if disputes_ok:
        r.append("| Unit | Source | What it says |")
        r.append("|---|---|---|")
        for z in disputes_ok:
            dz = str(z.get("source", "")).strip()
            r.append(f"| `{z.get('odynycya', '?')}` "
                     f"| [`{dz.rsplit('/', 1)[-1]}`]({dz}) "
                     f"| {str(z.get('komentar', '')).strip()[:120]} |")
        r.append("")
        r.append(f"\nIf all of them hold up on substance, the error rate "
                 f"among the unchecked is **{len(disputes_ok) / n:.1%}** "
                 f"(95 % Wilson: {low:.1%}–{high:.1%}), that is about "
                 f"**{round(len(disputes_ok) / n * population_n)}** units "
                 f"across the whole `unchecked` population.\n")
    else:
        r.append("Not one claimed refutation survived layer 3.\n")

    # A breakdown by helper. Not cosmetic: in a broken wave the
    # difference between honest work and rubber-stamping was visible
    # exactly here — one helper gave 5 confirmations and 20 "not found",
    # another 25 of 25. The wave average hid both.
    by_helper: dict[str, collections.Counter] = collections.defaultdict(
        collections.Counter)
    for z in records:
        by_helper[str(z.get("_fayl", "?")).split("-")[0]][
            str(z.get("verdykt", "?"))] += 1
    if len(by_helper) > 1:
        r.append("\n## Breakdown by helper\n")
        r.append("A wave with identical columns across the board is "
                 "suspect. A helper who confirmed everything either found "
                 "a document for every claim, or searched for none.\n")
        # The last column is the decisive one. A count of "confirmed"
        # says nothing until you can see how many of those quotes really
        # stand in the document: in the first usable run one helper gave
        # 16 confirmations and **zero** verbatim quotes, another 3 and
        # three.
        r.append("| Helper | confirmed | disputes | not found "
                 "| unreachable | quotes verbatim |")
        r.append("|---|---|---|---|---|---|")
        layer3_by_helper: dict[str, list[int]] = collections.defaultdict(
            lambda: [0, 0])
        for z in records:
            if not str(z.get("quote", "")).strip():
                continue
            h = str(z.get("_fayl", "?")).split("-")[0]
            layer3_by_helper[h][1] += 1
            if states.get(str(z.get("odynycya"))) == "ok":
                layer3_by_helper[h][0] += 1
        for who in sorted(by_helper):
            k = by_helper[who]
            ok, total = layer3_by_helper.get(who, [0, 0])
            share = f"{ok}/{total} ({ok / total:.0%})" if total else "—"
            r.append(f"| `{who}` | {k['pidtverdzheno']} "
                     f"| {k['sperechayetsya']} | {k['ne_znayshov']} "
                     f"| {k['nedosyazhne']} | {share} |")
        r.append("")

    if repaired:
        r.append("\nRepaired mechanically: "
                 + ", ".join(f"`{b}`" for b in repaired) + ".\n")
    if broken:
        r.append("\nWould not parse and were skipped: "
                 + ", ".join(f"`{b}`" for b in broken) + ".\n")

    REPORT.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"measure_f: answers {n}, refutations claimed {len(disputes)}, "
          f"survived layer 3 {len(disputes_ok)} → {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
