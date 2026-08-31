# The fact-check of this book

> **generated** — `factcheck/tools/report.py`. Editing it by hand only moves the
> next run's diff, never the state it describes.

What has been checked in *Довідник ESP32*, against what, and what
is left. The method that produced these numbers — and the reasoning
behind every status below — is in `METHOD.md`; this document is only
the state.

## Where the book stands

```
  claim units              8111   (+ 221 code blocks as context)
  checked against a source or by calculation
                           2359   29.1 %
  closed as a decision     3780   46.6 %   no external signal in the text
  still open               1920   23.7 %
```

The three lines do not add to the whole, and the gap is deliberate:
**44 units are self-consistent** — checked against another
place in this same book, mechanically and reproducibly. That says
something checkable about the book and nothing at all about the world,
so it is counted in neither column. `METHOD.md`, Part II, says why.

### By status

| Status | Units | Share | What it asserts |
|---|---:|---:|---|
| `verbatim` | 2036 | 25.1 % | primary, quoted — the source was obtained and the extract copied |
| `derived` | 230 | 2.8 % | primary, inferred — the source was obtained; the claim follows unambiguously |
| `arithmetic` | 93 | 1.1 % | calculation — checked by arithmetic; no external source is needed |
| `named-unreachable` | 178 | 2.2 % | secondary — the source cannot be reached from here; URL recorded, no quote |
| `self-consistent` | 44 | 0.5 % | internal check — the book agrees with itself; no external confirmation |
| `looked-not-found` | 8 | 0.1 % | looked and did not find — the work was done, the source is not visible |
| `no-external-signal` | 3780 | 46.6 % | no signal in the text to check against — assigned mechanically, not checked |
| `unchecked` | 1742 | 21.5 % | not checked |

## The weakest number on this page

`no-external-signal` is 46.6 % of the book — the largest
single status, and the only one that certifies itself. It is assigned
mechanically, for want of a digit, identifier or unit in the text, and
it reads to a reader as *no source exists*. Those are not the same
thing.

A random sample of — units measured how often that
reading is wrong. The measurement, its seed and its sample are in
`reports/MEASURE-NO-SIGNAL.md`; the sweep that harvested sources from
the same status is in `reports/SWEEP-NO-SIGNAL.md`, and **its percentage
may not be carried over** — its sample was picked where the light was.

## What was found

Corrections to the book that came out of this work are recorded per
pass in `METHOD.md`, Part I. Refuted claims and the patterns that
caught them are in `reports/REFUTED.md`.

## Sources

```
  evidence records            0
  quotes checked verbatim against the source document
                              —   reports/QUOTES.md
```

Sources that cannot be reached from the environment this book is made
in are not dropped and do not pretend to have been checked: they
become a hand-off in `reports/UNREACHABLE-SOURCES.md`, with the
document, what to look for in it, and the claims that depend on it.

## Runs

Every helper wave is recorded in `reports/RUNS.md` with the
`order_version` it was given, so two waves are comparable exactly when
they were told the same thing. A wave whose result did not survive
that comparison is recorded as not a result, which is what the ledger
is for.

## What is left

1920 units are open: 1742 never looked at,
178 waiting on a source that cannot be reached from here.

The registry is complete by construction — every line of the book has
a record, whether or not anyone has worked on it — so this number
shrinks only from work and grows only from the book. That is the one
property that lets it prove completeness rather than effort.
