# v1.0-print-1 — first attempt at the first print run

This file records the state of the handbook submitted for its first
commercial print run, so that errata can be keyed to it.

It is a **first attempt**: the text is believed correct, not proven
complete.

    commit  285b3e0
    date    2026-08-27

## How this state is pinned

The session that prepared this print run **could not push tags** — its
credentials are scoped to branches, and the tag push was refused with
HTTP 403. A branch serves the same purpose, so the exact state sent to
print is pinned by one:

    backup/main-2026-08-27-1211Z   →   285b3e0

**Reason for the backup: first attempt at the first print run.** The
branch is a marker, not a line of development. Nothing should be
committed onto it; if this print run needs corrections, they belong on
`main` and are recorded as errata against this state.

To also create the proper tag, from any checkout whose credentials
allow tag pushes:

    git tag -a v1.0-print-1 285b3e0 -F PRINT-1.md
    git push origin v1.0-print-1

## Print specification

| | |
|---|---|
| `esp32-dovidnyk.pdf` | **448 pages = 28 signatures of 16** |
| `esp32-kartky.pdf` | 15 pages |
| `esp32-proekty.pdf` | 32 pages |
| Toolchain | pandoc 3.1.3, typst 0.15.0 |
| Source fingerprint | `792d9a1b02ec5a9c` |

## Release gates, all green at this commit

| Gate | Result |
|---|---|
| `release-check` | passed in full |
| refuted formulations | 27 patterns, 97 files, **0 occurrences** |
| fact-check gates | 0 refuted claims, 0 evidence records matching nothing |
| correspondence | 0 unanswered questions between maintainers |
| authorship policy | verified |

## Fact-check state of the 8090 checkable statements

| Class | Count | Meaning |
|---|---:|---|
| **A** | 1919 | primary verbatim: source retrieved, quoted word for word |
| **B** | 422 | primary derived: source retrieved, statement follows from it |
| **C** | 150 | source named but unreachable; what to look for is recorded |
| **D** | 161 | verified by arithmetic; no external source needed |
| **E** | 3969 | no externally checkable signal in the text — assigned mechanically by absence of signal, **not** by a conclusion that no source exists |
| **F** | 1469 | not yet checked |

**Verified against a source or by arithmetic: 2502 (30.9 %).**

## What this record does not claim

Every defect found during fact-checking has been corrected in the text
and is guarded against silent return by the refuted-formulation
registry. That is a statement about **what was found**, not about what
exists.

The 1469 unchecked statements were not judged. The largest class, `E`,
means "no signal to check against" — not "verified".

## Known open items, recorded rather than hidden

* **24 class-`E` statements contain a number** and therefore deserve a
  second look; the registry flags them itself.
* **17 evidence records** whose quotation check disagrees between two
  tools — one is strict about markup, the other is not. At least one
  disagreement is a false alarm caused by reStructuredText role syntax.
* **No human has reviewed the page layout** across these 448 pages.
* The semantic layer — whether a verbatim quote actually *supports* the
  statement it is attached to — was not performed by a human on the 335
  records landed by the final sweep. Each such record says so in its
  own `sposib` field.

Errata for this print run are keyed to `v1.0-print-1`.
