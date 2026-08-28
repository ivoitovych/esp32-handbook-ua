# What we set out to build, and what we actually have

A plan-versus-actual account of the fact-checking technology, written
so that the next book does not have to rediscover any of it.

**Figures below are dated `2026-08-28 19:43 UTC`** and come from
`tools/factcheck.py status` and `tools/schema.py`: **8110 claims (plus
221 code blocks carried as context), 1360 evidence records, 92 book
files, 53 tools.**

The date is not decoration. This file previously said "figures at the
time of writing" **without naming the time**, and within two days every
one of them had moved — claims by 221, records by 23, the verified share
by a full point. A number with no date reads as current, is believed as
current, and cannot be checked by anyone including its author.

> **Every measured number in a document carries its date and the command
> that produced it, or it does not belong in a document.** `README.md`
> gets this right by holding commands instead of numbers; this file did
> not.

---

## The six things we wanted

### 1. Completeness by construction — **achieved, and it held**

**Wanted.** No claim silently unexamined. Not "we reviewed the book"
but "here are the claims, and here is the state of each."

**Have.** The registry is generated from the book, so a claim cannot
fail to appear: 8331 units, each with an identifier, a content hash and
a recorded state. A claim without evidence is a *visible* gap, not a
forgotten line.

This is the one thing that worked from the first day and never
regressed. Everything else in this document is a correction to
something; this is not.

### 2. Provenance for every claim — **achieved in part, and the part matters**

**Wanted.** For each claim: where is this known from.

**Have.**

| State | Claims | |
|---|---:|---|
| State | Claims | | |
|---|---:|---:|---|
| `A` verbatim — source retrieved and quoted | 2032 | 25.1 % | |
| `B` derived — source retrieved, claim follows | 226 | 2.8 % | |
| `D` arithmetic — settled by calculation | 93 | 1.1 % | |
| `C` named-unreachable — source named, not reachable here | 178 | 2.2 % | |
| `S` internal — checked against another place in this book | 44 | 0.5 % | new |
| `L` looked-not-found — a document was opened, nothing there | 8 | 0.1 % | new |
| `E` no external signal — the rule fired, nothing checkable in the text | 3780 | 46.6 % | |
| `F` unchecked | 1749 | 21.6 % | |
| `K` code context | 221 | — | |

**Verified against a source or a calculation: 2351, or 29.0 %.**

`S` is reported on its own line and **not** added to that figure. The
book agreeing with itself is checkable and worth recording; it is not
external verification, and folding it in would inflate the one number a
reader looks at first.

This figure has now fallen twice, and both falls are the point:

    32.9 %  →  30.0 %   pattern leaks closed; 239 claims went back to F
    30.0 %  →  29.0 %   more leaks closed, and `D` fell 140 → 93

The first fall was traced to its cause. **The second was not**, and
saying so is part of reporting it: 28 arithmetic records now cover 93
units where they once covered 140, and narrowing one leaked pattern
accounts for roughly 28 of the 47. The rest is unattributed. An
unattributed movement in a coverage figure is a thing to chase, not a
thing to round off.

> A coverage number that only ever rises is a number nobody is checking.

The honest sentence the book can print is *not* "everything is
verified". It is: **every claim was looked at at least once, and the
state of each is recorded.** The difference between those two sentences
is the whole point of the exercise.

`E` deserves its own warning. It is a **decision**, not a check: the
rule says "this text contains no number, identifier, or part name to
check against, so no external source will settle it." A random sample
put a genuine external referent behind roughly 37 % of them. So `E` is
not "verified" and never was — and the book's own description of `E`
had to be corrected once because it implied otherwise.

### 3. No fabricated sources — **achieved mechanically, with a known hole**

**Wanted.** A source that was never opened must not be citable. The
rule: class `A` only when the document was retrieved *in this session*
and quoted.

**Have.** Layer 3 checks it by machine — the quote must occur in the
cached source as a substring:

    evidence records          1337
    verified verbatim          330
    quote not found             89   ← repair queue
    source not in the cache    218   ← the hole
    nothing to check against   676

The hole is real and named: **218 records cite a source that is not in
the cache**, so their claim cannot be reproduced by anyone else. That
is not fabrication, but it is not reproducible either, and the
distinction has to stay visible rather than be averaged away.

Worth recording: cheap assistants fabricated sources in measurable
numbers until the work order was rewritten to *explain the gates rather
than only forbid*. With the explanation: 0 self-citations in 85. With
that section dropped: 2 in 120. The prohibition was not what worked.

### 4. A card you can hand to a person — **achieved for the book side**

**Wanted** (the owner's criticism, and the sharpest one made all week):
a fact-check card must contain a direct quote from the book and a
direct quote from the source, plus context — so that it is
self-sufficient. A line reference is not a quote; it sends the reader
somewhere else.

**Have.** Context stands on **8331 of 8331** cards. The card finds its
line by **content**, falling back to the line number only if content
fails — because the line number drifts (see §7).

The first version of this shipped broken, and the audit caught it. The
card emitted a "verbatim from the book" block whenever the raw line
differed from the claim text — and for prose that is true merely
because the book wraps lines mid-sentence. Result: thousands of cards
showing a **fragment**:

    T-63-002  …льна роль ESP32 у чужій системі (розділ 57), і

The condition asked about string inequality when it should have asked
about the **kind** of unit:

| Kind | What "claim, briefly" is | Extra verbatim block |
|---|---|---|
| prose, code line, schema link | the book's own text | not needed |
| table cell, table row | a render (`BME280 · Address → 0x76`) | the raw row |

Now: 1385 verbatim blocks, **all of them table rows**; 34 cards say
plainly that the locator missed rather than showing a wrong line; and
the registry file states the rule once at the top instead of the card
repeating it 8331 times.

> Same defect family as three previous ones, recorded under three
> different names: **the reader is judging half a thought.** This time
> the half was cut by the tool built to prevent exactly that.

The source side is present wherever evidence exists — the same 30 % as
above. The card is self-sufficient; the evidence behind it is as
complete as the evidence is.

### 5. Portable to another book, in English — **roughly half done**

**Wanted.** The technology must move to other, English-language books.
It cannot, while it speaks a private dialect: *наряд*, *помічник*,
*комірка*, *помірка*, and field names `nazva / zbih / klas / dzherelo /
cytata / sposib / notatka`.

**Have.**

| | |
|---|---|
| English field names alongside the old | ✅ 1337 / 1337 |
| Word states (`verbatim`, `derived`, …) | ✅ |
| Process slang out of `method` | ✅ 582 rewritten, 22 kept deliberately |
| Evidence bound by hash, not by a render pattern | ◐ 829 / 1337 |
| Documents renamed | ◐ 5 of ~14 |
| Technology documents rewritten in English | ✗ 8 remain |
| Directories and tools renamed | ✗ planned, not started |

"Expand, then migrate, then contract" throughout, because two
maintainers work the same files concurrently: new names stand **beside**
the old, and nothing is removed until both sides are ready.

### 6. Proof that restructuring loses nothing — **achieved, and it paid for itself repeatedly**

**Wanted.** A way to restructure without the quiet loss that had
already happened once (re-landing a wave overwrote its predecessor;
335 evidence records became 324, recovered only by `git`).

**Have.** A snapshot of what every evidence record binds, taken
*before* each change and compared after. Every stage since has reported
zero lost claims, and it caught the one genuine change (§8) precisely
and by itself.

> This is the investment to copy into the next project first. Not the
> classes, not the layers — **the thing that proves the work survived
> the change.**

---

## What we planned and then abandoned — with the reason

**Stage 4 as written: "patterns stop matching the render, match the raw
book line instead."** Killed by measurement before any code was
touched: **5225 of 8331 claims share a book line with another claim,
up to ten per line** — a table row holds many cells. A pattern over the
raw line cannot tell them apart. The plan would have taken this
project's worst failure mode — a wide pattern silently marking
unchecked claims as verified — and made it structural for 63 % of the
registry.

*What replaced it:* binding by content hash, which is exact, survives
renumbering, and detaches itself when the wording changes. It **already
existed and already worked** — `vsi_kandydaty` had preferred it over
patterns all along, and not one of the 1337 records used it.

**Stage 5: "remove the render."** Cancelled because it contradicts §4.
The render *is* the "claim, briefly" line the card was required to
have. Removing it would delete one of the three parts the rework
existed for.

**"Spent work orders are deleted, not renamed."** Wrong twice in one
batch. One of them is *generated* by a tool; another is the specimen
work order whose gates section is the evidence for the self-citation
measurement above. The plan had never opened the files it sentenced.

> An inventory made from file names is a guess wearing a table's
> clothes.

---

## What we believed we had, and did not

This is the most valuable section, and the least comfortable.

### 7. The first layer was never checked at all

The registry is generated from the book, so nobody thought to check
that it still *matches* the book. `factcheck.py stale` was named
"records whose text in the book changed" and did exactly one thing:

    if not p.exists(): print("file is gone")

Four days. Six corrections made for the print run went past a counter
that read zero the entire time. Found by the second maintainer, who
went to write the check convinced it already existed.

Alongside it, a second discovery from the opposite direction: the
snapshot reported 34 records "losing" claims after a full regeneration.
Nothing was lost. It was keyed by claim **id**, and an id is
`T-<file>-<ordinal>` — it shifts from any edit *above* it. Six edits
moved **1311 ids across 32 files**. Re-keyed by content hash: 0 of 1337.

> The number is an address — where to find the claim today. The hash is
> what the claim *is*. Anything that must survive an edit holds the
> hash.

### 8. Patterns leak, and the leak hides in the shortest alternative

Found while measuring why 508 evidence records refuse to migrate one at
a time: they are chained together through overlapping patterns.

A pattern is a disjunction. When one alternative matches more than all
the others combined, it does not narrow the pattern — it replaces it:

    evidence: "GPIO unconfigured at boot, the line floats"
    pattern:  старт|завантаж|GPIO.*?висить|невідом|стан
                                                    ↑ 242 claims

Five alternatives are specific, which is exactly why the pattern
survives reading. The sixth does the work.

    records that leak this way                        22
    claims taking their state from a leak            956
      would have no evidence at all without it       873
      presented as verified (`A`/`B`)                237

Closed by the second maintainer the same day — 15 of their patterns
narrowed:

    records that leak                        22 → 5
    claims resting on a leak                956 → 81
    of those presented as verified          237 → 54

This is **not** the wide-pattern problem caught three times before —
there the record was visibly broad. Measuring total width does not find
these: one record binds 210 claims and is *correct* (a single check
that genuinely covers all of them). The measure has to be relative:
widest alternative against the sum of the rest. That flags 22 of 1337
and leaves the legitimate one alone.

Consequence for the book: the printed sentence stays true, but the
**coverage figure** does not — 237 claims carry a state they did not
earn, and the number should be recomputed after the narrowing rather
than quoted as it stands.

### 9. Five silent failures in one day, all of one family

| Where | Promised | Did |
|---|---|---|
| `vorota` | two checks | one |
| `sweep.py` | a candidate per packet | none, silently |
| `stale` | compare the book's text | check the file exists |
| card regex | four readers share the format | each kept a private copy |
| `correspondence.py` name pattern | a bad filename is a violation | the letter vanished from the ledger |

The last one cost the most: **two of the second maintainer's letters
were invisible to the correspondence protocol** — Cyrillic in the
filename slug, and a non-matching file was treated as "not a message".
The finding that layer 1 was broken sat unseen, and the release gate
that blocks on an unanswered question never reacted. Found by accident,
when a reply could not locate its addressee.

> **Zero looks the same whether all is well or the counter is counting
> nothing.** And we read it as the first, every time.

Hence the contribution rule, which is stronger than reviewing
docstrings:

> Every new check must be demonstrated working on a **deliberately
> broken input**, and that demonstration is part of the contribution. A
> check that has never fired is indistinguishable from a check that
> does not exist.

Applied immediately: the leak detector's self-check failed on its first
run — and was right. The example was wrong, not the tool.

---

## What this technology does not do

Stated plainly, because the gaps are load-bearing.

- **It does not judge whether a quote supports a claim.** That is layer
  2, and it is human-only. A machine can prove the quote is *in* the
  document; nothing here proves it is *about* the claim.
- **It does not check the book against itself.** Two chapters can
  contradict each other with every claim in both perfectly sourced.
  A fourth layer is designed and not built.
- **It catches modality only as a report.** "Presented as documented"
  — the book says *must*, the source says *recommended* — passes all
  three layers, because the quote is verbatim. A detector exists; the
  judgement is a person's.
- **Claims spread across several paragraphs remain hard.** Context does
  not save them, because the context would itself need context. A
  narrow tail, but real.

---

## If you are starting this on another book

In order of what returns the most:

1. **Generate the registry from the book.** Completeness by
   construction is the only property here that never had to be
   repaired.
2. **Build the snapshot before the first restructuring**, not after.
   After a format change, nothing remains that knows what the old
   patterns meant.
3. **Anchor on content hashes from day one.** Ordinals and line numbers
   are addresses; they drift, and a checker built on them cries wolf
   until nobody listens.
4. **Bind evidence to claims explicitly, not by pattern.** Patterns are
   convenient for landing a wave and dangerous forever after.
5. **Demand a broken-input demonstration for every check.** Four of our
   worst defects were checks that ran, returned zero, and meant
   nothing.
6. **Write the state of a claim, never a verdict about the world.**
   `no-external-signal` means the rule fired, not that no source
   exists. We had to correct the book itself on this point.
