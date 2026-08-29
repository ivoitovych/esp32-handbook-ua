# The fact-checking registry

> **canonical** — the decision lives here; there are to be no copies

A structure parallel to the book in which **every claim has its own
record**, and each record holds the book's verbatim text beside the
source's verbatim text.

```
factcheck/
  THE TECHNOLOGY — six documents, and exactly these travel to another book
    README.md          this file: index, state, the limits of the environment
    METHOD.md          the whole method in one document: three layers,
                       the laws of a work order, gates, sources, measurement
    SCHEMA.md          the record format and the **normative** list of statuses
    DEFECTS.md         catalogue of defect kinds: sign, measure, case, what holds it
    TASK-SPEC.md       the brief given to a helper: the blocks an order is built from
    HELPERS.md         the log of waves: what was tried and how it failed

  book/     about this book, not about the technology — stays Ukrainian
    MIGRATION.md · RETROSPECTIVE.md · SOURCES.md · REFUTED.md
    UNREACHABLE-SOURCES.md

  reports/  written by a tool — editing them by hand only moves the next diff
    QUOTES.md · SPLIT.md · RUNS.md · TRACES.md · TRANSLITERATION.md
    LANGUAGE.md · MEASURE-NO-SIGNAL.md · MEASURE-UNCHECKED.md
    SWEEP-NO-SIGNAL.md · BOOK-VS-SOURCES.md
    BRIEF-SAMPLE.md · BRIEF-QUOTES.md · BRIEF-LEADS.md

  archive/  spent work; nothing here is deleted, translated or renamed
    history/  8 frozen registries — the numbers past reports stand on
    runs/     11 run directories: waves, trials, experiments, orders
    orders/   orders already carried out

  DATA
    evidence/*.yaml    the evidence itself: source, quote, pattern, status
    manual/ dodatky/ kartky/ inserts/   cards, parallel to the book
    triage/            units sorted by kind
    runs/              where the NEXT run writes; empty by design
    queues/            inputs for the next orders
    snapshots/         bindings taken before and after migrations
```

**Why this shape.** For a long time everything lay here together:
thirty-one documents and twenty-one directories in the root, nine of them
the same kind of thing (`wave2`, `wave3`, `test-run`, `trial-100`…). The
owner called it a rubbish bin, and was right twice — once when he said it,
and again days later when he saw nothing had changed.

> The root of `factcheck/` holds **only what travels to another book**.
> Everything else sits in a directory named after what it is.

Two ratchets hold that shape. `tools/doc_kind.py` checks each document's
kind marker against whether a tool actually writes it, in both directions.
`tools/language.py` checks that the technology is in English and the book
is not — because the foundation acquired two new Ukrainian documents in a
single afternoon while every other check stayed green.

One book file → one registry file with the same name.
`manual/06-zhyvlennya.md` → `factcheck/manual/06-zhyvlennya.md`. Card
names stay Ukrainian on purpose: they cite the book, and the book is the
product.

**Where to start reading.** `METHOD.md` §3 — why there are three layers
and why none of them replaces the other two. Then `SCHEMA.md` for what a
record looks like. Then `HELPERS.md` if you are going to brief a pool.

**If you are lifting this onto another book**, the six documents above are
the whole of it. `METHOD.md` carries the reasoning; `DEFECTS.md` and
`TASK-SPEC.md` are its reference works. Nothing in them is about ESP32.

**The shortest path to the weakest place** is `reports/MEASURE-NO-SIGNAL.md`.
The `no-external-signal` status is nearly half the registry, and it is the
only status that certifies itself: `verbatim` says "here is the document",
`named-unreachable` says "here is where to look", `no-external-signal`
says "do not look". A random sample of 160 units says roughly **37 %** of
that status do have an external referent — closed too generously.

`MEASURE-NO-SIGNAL.md` and `SWEEP-NO-SIGNAL.md` answer **different**
questions, and their numbers must not be mixed: the sweep took units
picked by hand where a source was most likely, so its percentage is high
by construction. A percentage may only be quoted from the measurement.

> The status words above are what `SCHEMA.md` and `METHOD.md` use. The
> stored records still carry single letters (`klas: E`); the contraction
> that drops them is agreed with M1 and waiting on his word.

## Why this is separate from `docs/fakty.md`

`docs/fakty.md` is the registry of **verified facts**: what was checked,
with source and date. It answers "what do we know for certain".

This directory answers the opposite question: **"is anything left
unchecked"**. The difference matters. The first list grows from work; the
second grows from the book itself and shrinks from work. Only the second
can prove completeness.

Briefly: `docs/fakty.md` is the shop window, `factcheck/` is the
stocktake.

## Why the registry is complete by construction

`tools/factcheck.py sketch` builds the skeleton: it breaks **every** file
of the book into claim units and opens a record for each. Not "for the
ones that seemed important" — for all of them.

This is the same idea as `docs/coverage-checklist.md`: an absence must be
a decision, not forgetfulness. A unit nobody checked stays visible as
`unchecked`; a unit not worth checking becomes `no-external-signal` — also
a recorded decision.

The consequence has to be accepted: the registry is large. That is not
excess, it is the honest size of the job.

## State

```sh
tools/factcheck.py sketch    create or re-sync the skeleton
tools/factcheck.py status    summary by status
tools/factcheck.py cherga    what is open, most expensive first
tools/factcheck.py blocked   unreachable sources, as a hand-off
```

After the book's text changes, `sketch` runs again. Records whose text
changed return automatically to `unchecked`: the evidence may have applied
to the previous wording.

## The environment limit that shapes the method

From the container this book is made in, **most primary sources are
unreachable**: the egress policy answers `403` for `docs.espressif.com`,
`espressif.com`, `analog.com`, `bosch-sensortec.com`, `ti.com`, `nxp.com`,
`wikipedia.org` and the rest.

What is reachable:

| Source | What it gives |
|---|---|
| `raw.githubusercontent.com` | **all of ESP-IDF's code**: `soc_caps.h`, `Kconfig`, driver headers, `SUPPORT_POLICY.md`, and — importantly — the **`.rst` sources of the documentation itself**; then `arduino-esp32`, `esptool`, component repositories |
| search | document titles and URLs; **paraphrase, not verbatim text** |

For ESP-IDF and the chips themselves this is better than
docs.espressif.com: code and Kconfig are the primary source, and the
rendered documentation is its retelling.

For third-party component datasheets (BME280, DS18B20, MAX485, TP4056)
and for standards (the I²C specification, Bluetooth Core) there is no
direct path. Such claims get `named-unreachable` with a recorded URL and a
statement of what to look for there. **A verbatim quote is never written
into `named-unreachable`** — see the rule in `SCHEMA.md`.

`tools/factcheck.py blocked` prints that list as a hand-off: a person with
open access closes it quickly, because all the preparation is already
done.

## Passes

The registry is filled by passes of increasing depth. Each pass leaves a
report in `reviews/` under the same rule as reviews: a finding with no
response is an unfinished pass.

| Pass | Scope | State |
|---|---|---|
| 0 — sketch | skeleton for every unit, triage by cost of error | done |
| 1 — hard core | addresses, `soc_caps`, Kconfig, API signatures, IOMUX pins | done: 12 verbatim, 2 findings |
| 2 — peripheral behaviour | the `.rst` sources of the ESP-IDF documentation | done: 9 verbatim, 3 findings |
| 3 — unreachable sources | registration as `named-unreachable` + a hand-off order | done: 13 sources, 237 claims |
| 4 — ways around | the part of `named-unreachable` closable via vendor GitHub | done: 8 evidences, order 237 → 192 |
| 5 — arithmetic | the book's arithmetic | done: 30 checks, **0 discrepancies** |
| 6 — depth | finer splitting (table cells, code lines), bootloader Kconfig | done: 4 findings |
| 7 — continuous API check | **all** 104 calls the book makes, against the headers | done: **0 discrepancies**, 2 additions |
| 8 — strapping and boot log | esptool documentation on boot mode selection | done: 1 addition, 2 confirmations |
| 9 — continuous command check | **every** `esptool` and `idf.py` command the book prints | done: **3 corrections**, 2 additions |
| 10 — console messages | lines the book promises you will see, against the lines in the code | done: **6 corrections**, 2 additions |
| 11 — menuconfig paths | menu names against the `Kconfig` files the menu is built from | done: **3 corrections**, 1 addition |
| 12 — pinouts | ADC, touch, IOMUX, USB, strapping against the `soc/` headers | done: **1 correction**, 1 addition |
| 13 — chip capabilities | the summary tables of chapters 02 and 04 against `soc_caps.h` | done: **2 corrections**, 1 addition |
| 14 — internal routes | 689 mentions of "chapter NN" and "card KN" in prose | done: **0 corrections**, now a standing check |
| 15 — versions | toolchain and components against tags and version files | done: **0 corrections** |
| 16 — interface reference | I²C addresses and SPI modes against drivers on GitHub | done: **1 correction**, 1 addition |
| 17 — families in projects | each project's pins against **every** board in its BOM | done: **4 corrections**, of which 2 "will not build" and 1 safety |
| 18 — project schematics | every schematic connection from both ends; splitting compound claims | done: 1 addition, **verbatim 803 → 657** after the split |
| 19 — triage and closure | mechanical `no-external-signal` for prose without a signal; flash sizes and addresses | done: **unchecked 6712 → 3649**, queue 1176 |
| 20 — working the queue | JTAG pins, example wiring | done: 2 of 4 JTAG pins closed `verbatim`, 2 deliberately into the order |
| 21 — struct fields | 39 field names in 8 structs against ESP-IDF headers | done: **0 discrepancies**, now a standing check |
| 22 — evidence reach | widening patterns to wordings that repeat | done: verbatim 679 → 698 with no new sources |
| 23 — DAC propagation | pass 17's own correction, which never reached chapter 07 | done: 1 correction, pattern into the refuted registry |
| 24 — offsets and the matrix | flash offsets, JTAG classic, the SPI limit through the matrix | done: **3 corrections, all three in explanations, not in numbers** |
| 25 — PSRAM | MSPI pins, support by family, allocation through malloc | done: **1 behavioural correction**, 1 addition |
| 26 — strapping, continuous | **all** of `boot-mode-selection.rst` against every mention of strapping | done: **0 discrepancies**, 3 additions — all from the unwritten |
| 27 — GPIO current | the first pass **driven by M2's findings**: a datasheet M1 has no access to | done: **4 corrections**, 3 of them in one paragraph |

After this come repeat passes until a pass stops yielding corrections. The
stopping criterion is double: **zero corrections** among what is checkable
from here **and** a granularity that cannot be usefully improved further.

Pass 17 was done on an external review, and it changed the understanding
of the method's limits: the registry could check numbers, names and
documents, but could not check **compound engineering claims**, where one
half rests on a sensor datasheet and the other on the board's
documentation. Two "will not build" errors lived in exactly that gap. The
conclusion is held by `tools/pins.py`, not by intention.

Pass 24 added a second observation to that. Every number it checked turned
out to be right, and all three corrections landed in the **explanations** —
"why the offset is what it is", "what `0x7000` means", "what a native pin
buys you". The registry is still built so that numbers in it are visible
while reasons hide in prose and drift toward `no-external-signal`. That is
the next place the method can be deepened: a reader remembers an
explanation better than a number and carries it further, so a wrong
explanation costs more.

Pass 26 named a third place where errors live — **the unwritten**. It gave
zero discrepancies and three additions, and none of the three was an
error: each was a correct statement with half of it cut off ("there is a
pull-up" without the value, "this pin is dangerous" without the direction,
a table of modes with no "otherwise" row). The registry cannot see such
places by construction: it checks what is written, not what is not. Only
continuous reading of the source with the question "what is there that is
not here" catches them.

Pass 27 and M2's findings named a fourth — **the direction of the
inference**. Chapter 35 said: "three modules of 4.7 kΩ give 1.6 kΩ — too
much current, the line does not rise properly". The arithmetic is right
(`4.7/3 = 1.567`), the source is right, and the consequence is the
opposite of the physics: lower resistance shortens the edge, it does not
lengthen it. A reader with a slow edge would have removed resistors on the
strength of that paragraph and made it worse.

What all four have in common is numbers, and numbers do not lie. The
registry sees the number itself; that what stands beside it does **not
follow** from that number is something it does not check by construction.
That is caught only by reading with the question "does this follow", not
"is this true".

Passes 5, 7 and 14 gave zero corrections in their domains — arithmetic,
API and internal routes. That is not a stop to the whole job but the
closing of three dimensions: there is nothing further to check there until
the book changes. All three are held by a tool in `make check`, so the
closure stays closed after later edits.

## The hand-off order

`factcheck/book/UNREACHABLE-SOURCES.md` is what cannot be closed from this
environment, in a form fit to give to a person with open access: the
source, how many claims depend on it, **what exactly to look for in it**,
and the claims themselves with the book's verbatim text.

This is the main thing that makes the environment limit manageable. An
unreachable source does not drop out of sight and does not pretend to have
been checked: it becomes a line in an order. Closed items come back as
`verbatim` or `derived` evidence in `factcheck/evidence/`, the order is
regenerated and gets shorter.

```sh
tools/factcheck.py blocked    # regenerate the order
```

The ordering is not arbitrary: pass 1 takes what costs a board when wrong
(`GPIO12` high at boot, the bootloader address, `espefuse burn-*`) and
where the primary source **is reachable** — that is, where `verbatim` is
achievable.
