# Fact-checking a book with a pool of cheap helpers

> **canonical** — the decision lives here; there are to be no copies

This document is **not about ESP32**. It is about the method, written so
that it can be lifted onto another book, another subject, another
language.

Everything here was bought with a mistake — ours. Where the price is
known, it is named: how many records had to be thrown away, how many
units vanished silently, how long it took to notice.

Companion documents: `DEFECTS.md` — the catalogue of defect kinds, one
row each, with the measured case. `SCHEMA.md` — the record format and
the card contract. This file is the reasoning; those two are the
reference.

---

## 0. What "fact-checking is finished" is allowed to mean

The most important decision, and it has to be made **before** the work
starts, or there will be nothing honest to tell the reader at the end.

It **cannot** mean "every sentence checked against a document". A large
share of any technical book is advice, judgement, framing and
navigation. For those an external source does not exist **by nature**.
Driving them toward "verified" forces helpers to invent sources, and
they will.

It means **every unit examined and labelled**. A sentence labelled
"the author's own position" is **finished**, not unfinished.

So the book prints **two numbers, not one**:

    technical claims verified:   X of Y
    author's own text:           Z — not verifiable by nature

One number instead of two lies in both directions: it understates the
coverage of checkable claims, and it frightens the reader with the size
of the remainder.

---

## 1. Splitting the book into units

The book is cut into **claim units**: a prose sentence, a table row, a
list item. Tables are cut into **cells** and rendered into a canonical
form such as `Subject · Column → Value`.

Each unit carries:

- an **identifier** — ordinal, for correspondence;
- a **hash** of the verbatim text;
- the **text** in canonical form.

**The hash is the binding key, not the identifier.** An identifier is an
ordinal, and a sentence inserted above shifts every one below it. The
hash follows the claim through reordering — and, no less important,
**detaches by itself** the moment the wording changes. The evidence was
about *those* words, not these.

> That fragility is a property, not a fault. When one maintainer
> rewrote a sentence about sensor tolerance, two pieces of evidence
> detached on their own and the release gate showed them. It worked
> exactly as designed.

**Measured warning.** After a full regeneration, identifiers move. In
one handover of 227 units, **15 pointed at a different claim** than
when the queue was written. Re-read a queue by hash or by text, never
by number.

---

## 2. Evidence classes

> **Authority: `SCHEMA.md`, section "Класи доказу".** If this list and
> that one disagree, that one is right and this one is stale.
>
> Two copies exist on purpose and only until one thing changes: this
> file is the English one that travels to another book, and `SCHEMA.md`
> is still in Ukrainian. When `SCHEMA.md` is translated, **this section
> becomes a pointer and the copy goes away.**
>
> Saying which copy wins is not bureaucracy. Three copies of this
> vocabulary existed on 2026-08-28 and all three had drifted apart; the
> two newest classes were missing from both non-authoritative ones. A
> copy with no declared owner is repaired wherever it is read, which is
> never everywhere.

    verbatim            source obtained, line quoted
    derived             source obtained, conclusion unambiguous
    absent-from-source  source obtained; its SILENCE is the proof
    arithmetic          checked by calculation
    named-unreachable   source named, text not held
    self-consistent     checked against ANOTHER PLACE IN THIS BOOK
    looked-not-found    a document was opened; the source was not in it
    no-external-signal  the text carries nothing checkable
    refuted             the source says otherwise
    unchecked           nobody has reached it yet

    code-context        a whole code block; not a claim, and not counted

Strength runs down that list, and the list is printed in strength order
rather than alphabetically because the order is the part that gets used.

### These used to be single letters, and that was the bug

Until 2026-08-29 each state had **three** names in circulation — a letter
`A`, a word `verbatim`, and an emoji `✅` — and a card printed all three
in a row, the last explaining the other two:

    - **Клас:** ✅ A — первинне дослівне — витяг із першоджерела…

Two of the three carried no information. They carried a **legend**: eleven
one-letter codes a reader had to hold in their head, and a colour scheme
on top of it.

> **An abbreviation is not a talking name.** The whole discipline of
> naming in code exists to avoid exactly the thing eleven single letters
> are.

And they had already drifted, as parallel names always do: `F` was
`unverified` in the data and `unchecked` in one of the tools. `unchecked`
won — it says *nobody has looked*, where `unverified` reads as *checked
and not confirmed*.

The letters survive in exactly one place and for one purpose: reading
cards and records written before the change. They are deleted together
with the `klas` field, not before and not separately.

### `N` is the only class layer 3 can *refute*

Every other class is checked by asking whether a string **is** in a
document. `N` asks whether it is **absent**, and absence is what the
claim rests on: `SOC_BT_SUPPORTED` does not appear in
`esp32s2/soc_caps.h`, and that silence proves the S2 has no Bluetooth.

This inverts the gate. For `A` a missing string means the evidence
fails; for `N` a *found* string means the evidence is **refuted** — the
only class where layer 3 can return a verdict against the record rather
than merely decline it.

It needs a `control`: a document of the same kind where the string **is**
present. Without one, "absent" and "I searched the wrong file" look
identical, and the second is far more common.

### `S` and `L` exist because two kinds of real work had nowhere to go

Both were added late, and both for the same reason: a maintainer had
done work, and the vocabulary forced them to record it as something it
was not.

**`S` — the book checked against itself.** Prose against the book's own
code, a summary against its own table. It says nothing about the world:
the book can be wrong in both places at once. But it says something
checkable about the book, and it is checkable *mechanically*, by layer 3
run against the book instead of a document.

The two wrong answers, and why each is wrong:

* `E` loses the information that **a check was made and it agreed**;
* `A` is wrong more expensively — it enters the "verified against a
  source" figure, which is the number the reader sees first.

So `S` is counted and reported **on its own line**, never inside
`A + B + D`.

**`L` — a document was opened and the source was not in it.** A report
of work, not a verdict about the world: weaker than `C` (which names a
document that could still settle the question), stronger than `E`
(which asserts). It requires naming what was opened.

> The general rule both of them come from: **when honest work has no
> legal way to be recorded, it gets recorded as something false.** A
> vocabulary that is missing a state does not produce blank fields; it
> produces wrong ones.

That gap was open in one more place until 2026-08-28, and a **helper**
found it, not us: there was no verdict for proof by absence. A helper
opened `esp32s2/soc_caps.h`, saw that `SOC_BT_SUPPORTED` was not there,
and wrote `(no SOC_BT_SUPPORTED in ...)` in the quote field — honest
work, correct conclusion, and no legal way to record it. The gate
rejected it as "not a quote", which it was not.

That is class `N` above, and the sequence is worth keeping: the
vocabulary's hole was visible from the outside before it was visible
from the inside. **A worker who cannot express what they did is
reporting a defect in the vocabulary, not making a mistake.**

**`E` does not say "no source exists".** It says the *rule fired*: this
text holds no number, identifier or part name to check against. That
distinction is the single most expensive one in this document, and this
file itself got it wrong for a week — the line above used to read "no
source exists", which is a claim about the world that nobody measured.

> Write the **state of a claim**, never a verdict about the world. The
> book's own description of `E` had to be corrected once for exactly
> this. A document that carries the technology to another project must
> not carry the error the project already paid to remove.

**`C` outranks `E`, and this is the load-bearing detail.** `E` ends the
unit's life in the queue: read as a verdict, it **hides the unit
forever**. `C` says
"a source exists, I do not hold it" and **keeps the unit in play**.
Confusion in the direction of `E` always reduces work — which is
exactly why it passes so easily.

### Trap: class `E` holds two incompatible kinds

`E` is assigned mechanically where the text carries no checkable
signal. But under one letter you end up with:

- a technical claim that merely failed to carry a signal — **a debt**;
- the author speaking in their own voice — **finished by nature**.

They must be separate classes. Otherwise half the book sits in a
category that means two opposite things.

**And `E` has a second problem: origin.** A class assigned
*mechanically* is a statement about the text and reverses itself when
the text changes. A class asserted in an evidence record is a
**verdict** — a claim that no source exists.

> A false confirmation is caught by layer 3. **A false verdict is
> caught by nobody**: the unit simply leaves the queue.

Measured three ways on this project, and they agree:

| How | Result |
|---|---|
| a random sample of 12 verdicts, read by hand | 3 false, 2 doubtful |
| a pool run over 95 verdicts, ten helpers | 10 of 85 found a source the verdict said did not exist — **12 %** |
| an audit of 17 numeric-claim verdicts | 2 false — **12 %**, both documents already in our own cache |

**12–25 % of verdicts were wrong.** The pool run is worth its own line: the
order made "no source exists" **not an allowed answer**, replacing it with
an advice verdict that *requires* an explanation, while "did not find"
requires none — because it asserts nothing. Of 45 advice verdicts, **zero**
lacked their explanation.

The asymmetry is the same one as in the law about patterns: an error
towards "a source exists" leaves the unit in the work queue, and an error
the other way hides it for good. So the verdict "no source exists" must be
the **most expensive** answer in a work order, never the cheapest.

---

## 3. Three layers of checking

    layer 1  book → record     does the evidence pattern touch the unit
    layer 2  evidence → claim  is the quote about THIS (semantic, human)
    layer 3  source → evidence is the quote in the document (mechanical)

Each layer catches its own kind of failure and **none of them catches the
other two**. That is the whole reason for separating them: fact-checking
costs an order of magnitude more than everything else in a book put
together, and the cheap part of it is invisible until it is separated out.

---

### Layer 1 — book → record

**Asks:** does this claim have a record in the registry at all?

**Catches:** a claim nobody checked, and nobody noticed was unchecked.

The book's structure is mirrored: each book file has a registry file
**generated** from its text. A claim gets a stable identifier, and the
record holds the verbatim book text, a hash of it, the status, and the
evidence.

#### The identifier is an address; the hash is what the unit *is*

That table used to say "the identifier does not change until the text
changes". It is untrue, and untrue expensively.

`T-20-050` is `T-<file>-<ordinal>`. The ordinal shifts on **any** edit
above the unit, even if the unit itself is word-for-word unchanged. Six
corrections to the printed run shifted **1311 numbers across 32 files**.

Both maintainers hit this the same evening from opposite directions: the
layer-1 check reported 1317 "mismatches", of which **6 were real** and
1311 were shifted numbers; and a snapshot written by `id` showed 34
pieces of evidence that had "lost" their units, where the same bindings
resolved through `sha` gave **0 lost of 1337**.

> The number is the address where the unit can be found **today**. The
> hash is what it *is*. Anything that must survive an edit — evidence, a
> snapshot, a work queue, a helper's order — holds the hash. The number
> is good only for showing a person where to look right now.

The same law applies a second time to the **card**: the line number in it
is a locator, and locators go stale. So a card finds its line in the book
**by content**, and takes the number only as a fallback.

#### Is the registry still about *this* book?

The registry is generated from the book, so editing the book does not
break it — it **displaces** it: evidence stays attached to the old
wording and `src:line` points past its target.

A `stale` check separates three kinds — text changed, unit appeared or
vanished, only the number moved.

For four days it caught none of them. **The docstring promised a text
comparison and the body checked whether the file existed**; the counter
read zero, and zero looked like "all well". Six corrections to the print
run went straight past it.

#### How this layer lies: the binding

Evidence attaches to units by pattern, and **a pattern that is too wide
silently marks as checked what was never checked**. Three times on this
project:

    ESP-IDF|esptool     173 units under one piece of evidence about versions
    службов             FreeRTOS tasks under evidence about a flash region
    RP2040              a whole column of a comparison table under a heading
                        about memory addresses — including the board price

> **A wide pattern is more dangerous than a missing one.** A missing
> pattern leaves the unit in the work queue. A wide one moves it into a
> class with a false mark and removes it from sight for good.

**The second law is about the opposite edge.** A pattern that writes out
the *whole sentence* dies at the first edit to that sentence: a DS18B20
correction rewrote the back half of one, and two pieces of evidence
stopped matching anything the same minute. The gate went red, which is
the only reason it was noticed.

> **A wide pattern lies; a long one breaks.** The target between them is
> the shortest *distinguishing* fragment — four words to the first number
> was enough here. Numbers and markup stay out of the pattern: those are
> exactly what gets edited.

The consequence for working in pairs: **an edit to the book is an event
for the evidence, not only for the text.**

**The third law: measure a pattern the way it is used.** Deriving patterns
by machine produced three failures in a row, and all three were a gap
between how the pattern was built and how it works:

| What was done | What happened | Why |
|---|---|---|
| `re.escape`, then spaces → `\s+` | **all 223 patterns matched nothing** | `re.escape` turns a space into `\ `; the substitution ate the space and left an orphan backslash |
| distinctiveness measured with `startswith` | 5 patterns up to **7** units wide | a pattern is used by **search**: one unit's prefix sits in the middle of another |
| re-landed, erasing the previous evidence files | 231 units left in class `verbatim` **with no evidence** | the class was already applied to the registry; deleting evidence is not the same as withdrawing a class |

The first two were caught by a check written immediately after landing:
for every new piece of evidence, count how many **registry** units it
touches and demand exactly one. Without it, 223 dead patterns would have
entered the tree quietly and looked like finished work.

The third is cured by order of operations: **landing starts by reverting
the registry** to its state without it, and only then lands afresh.
Otherwise the second attempt sees the first one's effects and concludes
the work is already done.

> What all three share: the tool **measured something other than what
> would later happen.** It is the same disease as a docstring that
> promises more than the code does — only here it is the measurement that
> lies rather than the text.

---

### Layer 2 — evidence → claim

**Asks:** does this extract actually prove this claim?

**Catches:** a real quote from a real source that proves something else.

**This is the expensive layer and it cannot be mechanised.** It needs
understanding of the subject, and every error that survived the other
checks lives here.

The sharpest example this project produced. The book stated that
`esptool chip-id` reports the chip family and revision. Class-`verbatim`
evidence quoted the command list:

    chip-id     Read Chip ID

The quote is exact. The source is the official documentation. Layer 3
passes it without comment. **The claim is false**: `ESPLoader.chip_id()`
raises `NotSupportedError` across the whole ESP32 family, and the command
prints a warning and a MAC address. The family is named by the *connection
preamble*, which is shared by every subcommand.

> **A name in a list proves the thing exists, and nothing else.** A claim
> about what the thing *does*, or *prints*, needs code or a sample of real
> output.

**Who does it:** the maintainer. Not a helper, not a script.

---

### Layer 3 — source → evidence

**Asks:** does this text really stand at this address?

**Catches:** paraphrase instead of quotation, two sentences stitched into
one, reordered words, plausible invention, an address that now serves
something else.

**It is a script, and that is the entire point.** Fetch the source into
the cache, extract the text, collapse whitespace, search for the
substring. No model at all.

Only *checkable* fragments are tested: lines without Cyrillic (Cyrillic is
our own annotation), without an ellipsis (text was cut there), and not
shorter than 12 characters.

Two search modes, and both are needed: **as a joined group**, when we
wrapped one long source line onto two of ours; and **line by line**, when
the fragment was assembled from different places in the file — two related
definitions a hundred lines apart in the code.

#### Why this layer changes the economics

Not because a script is cheaper than a model. Because **it removes the
requirement on the strength of the model that collects the evidence.**

A weak model fails predictably: paraphrases instead of quoting, stitches
sentences, reorders words, invents something plausible. Layer 3 catches
every one of those mechanically and completely.

So collection can go to the cheapest model and the expensive attention
stays on layer 2. That is the part of the work that is invisible until it
is separated out.

#### Three states that cannot be anything but an error

Not every mismatch is a fault — a quote can fail to match because of a
line wrap, or because the extractor laid a table out by columns. So **a
mismatch is a report, not a gate**. But three states can only be errors,
and the check fails on them:

**An invented source.** Class `verbatim` or `derived`, and the source
field holds not a document but a property of the world: "the properties of
CMOS logic", "well-known relay electromechanics". This is the worst
possible outcome of all — a false "checked" removes the claim from every
queue, and nobody ever looks at it again.

A cheap model that **cannot find a document does not write
`named-unreachable` — it invents a plausible document name.** Stronger
models did not do this once in three waves; they wrote
`named-unreachable` with a "what to look for" field.

> A cheap model is safe where the document is already in the cache and the
> work is "find it and copy it out". It is dangerous where the document
> might not exist — that is exactly where it invents.

**But the fault is not a property of cheap models; it is a property of
haste.** The worst instance in this project was a maintainer's: class
`derived`, source "well-known relay electromechanics", and the same field
admitting two lines later that the normative document was unreachable. The
record said `named-unreachable`, the class said `derived`, and it was
written ten passes before any helper pool existed — on a safety claim
about welded relay contacts.

That matters for how the gates are built: a gate that checked **who wrote
the record** would have passed the worst case. It checks **the record**.

**A stub in the cache.** A vendor site returns fixed-size HTML for any
address under a documents path, with code 200. `curl --fail` succeeds, the
file lands in the cache as a document, and a class is assigned for
something nobody saw. Checked by the `%PDF` signature.

**Evidence in the class that means "no evidence".** `unchecked` means
nobody has looked. An evidence record carrying it says nothing at all.

What saves this layer from crying wolf is a fourth state — **checked by
eye**. Where extraction destroys the structure, the maintainer verifies
the quote personally and marks it with the reason the machine is helpless
here. Without that escape, layer 3 raises alarms on correct quotes, and
within a week nobody reads it — and then it is worth nothing.

#### Tables in PDFs: better extraction first, loosening only after

The order matters. "Checked by eye" costs a person minutes **per record**,
and when there are dozens it eats exactly the attention the whole layering
was built to protect. So exhaust extraction before loosening the check.

A plain PDF-to-text pass gives **reading order**, in which every cell of a
column stands on its own line:

    Thermometer
    tERR
    -55°C to +125°C
    ±2
    °C

There is no continuous line "Thermometer tERR -55°C to +125°C ±2 °C" in
that text, and there cannot be — although in the document it is one table
row.

**The cure is coordinates, not loosening.** A coordinate-aware extractor
gives words with positions; those sharing a baseline group into a row and
sort left to right, and the table row is reconstructed verbatim.

So the text of a PDF is built in **two views at once** — reading order
plus reconstructed rows — and the search runs over both. A quote from a
paragraph is found in the first, a quote from a table row in the second.

The same pass removes extraction litter: soft hyphens, zero-width spaces,
`ﬁ`/`ﬂ` ligatures, non-breaking hyphens. That is not a loosening — they
are invisible in the document, and no human could have "quoted them
wrongly".

#### What remains, and why some loosening is still needed

Column layout still puts a parameter name, its condition and its value on
different lines. A plain substring test gave **27 false alarms out of 45**,
and not one was the quote's fault.

One case coordinates do not solve: **a cell broken across two visual
lines**. "Thermometer" sits above "Error", and no single row contains the
whole parameter name.

For that there is a fallback: if the substring does not match, every
meaningful token must be present in the document **and lie close
together** (a window of a few thousand characters). That catches an
invented quote — the tokens will not be there at all — and does not catch
a word reordering inside a table, where reordering does not change meaning.

For code and structured markup the loosening **does not apply**: there,
word order carries meaning.

"Checked by eye" remains, but as a last resort for unreadable scans rather
than a normal state. If it starts appearing often, that is a sign the
extraction needs improving again — not that the human should look harder.

#### What layer 3 does not say

* It does not say the evidence is *relevant* — that is layer 2.
* It does not say the source is authoritative: a raw-content host will
  serve anybody's repository.

It says exactly one thing: **this text really stands at this address.**

---

### Who does what

| | Layer 1 | Layer 2 | Layer 3 |
|---|---|---|---|
| **Script** | generates the registry, audits patterns | — | everything |
| **Helper (cheap model)** | — | fetches the source, returns a verbatim quote | — |
| **Maintainer** | writes patterns, judges the audit | **assigns the status** | resolves mismatches |

A helper writes **no** evidence, **no** patterns and **no** statuses, and
changes nothing in the repository. The reason is concrete: all three cases
of a pattern failing silently happened where the pattern was written, and
only someone who remembers all three catches them.

---

### A fourth layer, which does not exist yet

The registry checks the book against sources. It does **not check the book
against itself**.

An appendix credited a sensor with measuring humidity it physically lacks;
a chapter of the same book said correctly that it is "the same part
without humidity". Both records would pass against their own sources, and
the contradiction between them is invisible to all three layers.

For a printed book this is the most expensive kind of error, because a
reference table exists precisely so a reader consults it **instead of**
reading the chapter.

**Its first instance already exists, written without anyone intending it.**
One record checks a voltage threshold in a project chapter's prose against
the threshold in that same chapter's code listing. Layer 3 first declared
it an invented source — and was formally right, because there is no
document. But it is not invention; it is a **third kind of source: the
book itself**.

Such records are now recognised and passed. Checking them mechanically
needs a different script, because the source lives in the tree rather than
the cache. But the fact that they are being written at all is the start of
the fourth layer: the practice appeared first, and only then was it seen to
be a distinct kind.

What is needed next: extract pairs of "the same claim in two places" from
the book and check them against each other. The most expensive mistakes of
the week were exactly that shape.

---

## 3-bis. Coverage: the layer that asks what is missing

Three layers check what is **in** the registry. None of them asks what
is **not**.

The registry is generated from the book, so "does every unit have a
card" is true by construction and worth nothing. The question that
matters runs the other way:

> **Does every line of the book become a unit?**

Text the splitter never saw has no card, no class and no evidence — and
does not appear in any count. It is not `unverified`; it is invisible. A
book can report 100 % of its units checked while a chapter of it was
never split at all.

### Two kinds of accounting, and only together do they mean "in place"

A line is accounted for if one of two things is known about it:

* **a card** — the line carries a claim, and the claim is in the
  registry;
* **a structural ground** — the line is part of the book's construction,
  and the script **verifies** that, rather than assuming it.

The second was first proposed as cards with a status like "not subject
to checking". That was rejected, and the reason is worth keeping.

A card whose entire content is "this is a heading" carries nothing a
script cannot derive from the line itself. Ninety-one such records add
nothing to the registry but weight — and they introduce an **asserting
verdict**, which on this project once collected a dumping ground
(85–87 % of one such class turned out to be ordinary author's
judgements).

> **A structural ground is stronger than a card precisely because it is
> re-checked on every run.** A card is written once and can go stale in
> silence; a rule cannot. A heading that stops being a heading is
> invisible to its card and visible to the script the same day.

### The rule this generalises to

> When a fact about the text can be **derived from the text**, it does
> not need a record in the registry. A record is for a **judgement**
> that cannot be derived.

The registry then stays what it should be — a store of judgements and
evidence — instead of a transcript of everything the book contains.

**And the boundary, so the rule does not travel further than it should:**
table cells and code lines keep their cards. A cell *carries a claim*
("BME280 · Address → 0x76"); a heading does not. The line runs not
along the shape of the row but along whether there is anything to prove.

### Structure is verified, not assumed

A heading counts only if the line matches a heading pattern, the anchors
referenced elsewhere exist, the number in the title equals the number in
the filename, and every "chapter NN" reference resolves.

Measured on this book: 639 chapter references, 0 broken; 13 anchor
links, 0 broken; 0 number mismatches. **The structural check finds
nothing today** — it is a regression guard, and saying so is part of
reporting it honestly.

---

## 3-ter. The split itself manufactures false contradictions

A registry unit is a **sentence**. For most claims that is the right size:
smaller cannot be checked, larger cannot be bound.

But a qualification in a book often stands in the **next** sentence, and
then the split cuts the thought in half:

    unit:            "`-z` turns on compression during transfer."
    next sentence:   "It is **already on** by default, so in an ordinary
                      command the flag changes nothing."

A helper who sees only the first reads the source — compression is on by
default, another flag disables it — and honestly reports a contradiction.
The book is right; its rightness simply lives in a unit nobody gave them.

> **A false contradiction of this kind is not the helper's mistake.** The
> split produces it, and no prohibition in the work order will remove it.

The consequence for practice: **a claimed contradiction is checked against
the book, not against the unit.** The cheap move is to read the
neighbouring sentences before fetching the source at all — in three cases
of three in one wave, the contradiction did not survive that.

The signature to recognise it by: the unit is short, categorical and
unqualified, while the passage beside it carries a caution box or a second
sentence beginning "but", "however", "already".

---

## 3-quater. Missing looks like agreement

A failure none of the three layers catches, because it happens **before**
them: a unit nobody answered.

A helper reports its own numbers, and they are self-consistent: "seven
confirmed, no errors". The order held ten. **Seven of seven looks exactly
like seven of ten from the inside.** The three missing records were not
refuted and not deferred — they are absent, and nothing in the report
shows it.

So a summary takes its list from the **order that was issued**, not from
what came back, and prints the missing ones as their own section.

> Reconcile against what was ordered, not against what returned.

And specifically **against the order as it was issued.** While helpers
worked on 50 mismatched quotes, merging the other maintainer's work raised
the count to 69. Reconciling against the current list would have written
19 records the helpers never saw into their carelessness.

The same law applies to data. The first run of one measure lost 40 units
of 160 to broken YAML — and lost them **not at random**: the files that
failed were from the two helpers with the highest hit rate. The silent
loss moved exactly the number being measured, and moved it downward.

> Silent data loss is almost never random: it shifts precisely the thing
> being measured.

---

## 4. Laws of writing a work order

The work order is **the entire world** the helper lives in. It cannot
see the project, does not remember yesterday, and does not know why any
of this matters.

### Law 1: the cheapest answer must assert nothing

Otherwise the work order turns carelessness into untruth.

> **Price:** a wave of 247 records, 185 discarded. The book's text sat
> in the work order itself, so "confirm" meant copying it back.

> **Control:** the same hour, the same cheap model, ten helpers on each
> side, one book, only the shape of the order different. **75 % waste
> against 10 %.** And the written prohibition "the book is not its own
> source" stood in the *worse* order and was absent from the better
> one. The prohibition explains nothing; the shape explains everything.

**How to apply:** look at what answer can be given **without leaving
the work order**. If such an answer exists and it asserts something,
the order is broken.

### Law 2: the named document must be able to answer

An API guide answers questions **about the API**. A claim about
hardware is not described there and should not be. The word `GPIO`
appears in both — the match exists, the answer does not.

> **Price:** 78 "not found" out of 98, half of them not absence of a
> source but wrong pairing. One queue returned 11 of 11.

### Law 3: do not name the expected answer

A work order that says "the expected answer here is *not found*" gets
exactly that, **without the work**.

> **Price:** 190 answers, a document named in eight. Two helpers quoted
> the work order's own sentence as their reason for not searching.

### Law 4: every verdict shows evidence of work

Including the negative one. "Not found" must name the document that was
opened and how it was searched. An answer that can be given without
working costs nothing — regardless of how honest it looks.

### Law 5: the evidence of work must be TIED to the claim

The most expensive of the five. A requirement that the negative verdict
name a file from the cache was satisfied **literally**: helpers took
one large datasheet and named it as the search evidence for every
subject.

> **Price:** 461 answers; in 5 queues of 13 more than 80 % rested on
> **one and the same file**; 82 named a file of the book itself.

> **The general form, and it is not about cheap models:** any condition
> that can be satisfied literally without being satisfied in substance
> **will** be satisfied literally.

### Law 6: the main threat is not lying, it is misunderstanding

We both built gates as if the helper were tempted to lie. Mostly it
does not.

> **Price:** of 528 claimed confirmations, 235 survived verbatim
> checking; **293 died, 55 %**. Eight were examined at random — **not
> one was fraud.**

The failure kinds were: fragments glued with an ellipsis; the index
cited while the target was quoted; code paraphrased into prose;
content reformatted. The helper **did not know** the quote would be
searched as a substring. It was summarising, because that looked
useful.

Prohibitions are powerless here, because nothing was violated. What
works is **explaining what happens to the work next**.

**And it is not a cheap-model failure. It is a reading failure, and the
maintainers made it too.** A later wave of 200 tickets put a number on
the shape: of 14 rejected confirmations, **13 pointed at the right
passage** and lost it in the copying — most often by deleting inline
markup from the middle of a line.

Then the same test was turned on our **own** registry, written by hand,
months earlier. Five records had done exactly that; three were one
maintainer's:

    in our record:  such as elf2image or merge-bin,
    in the source:  such as :ref:`elf2image <elf-2-image>` or
                    :ref:`merge-bin <merge-bin>`,

    in our record:  located at (default offset) + 0x1000.
    in the source:  located at (:ref:`default offset
                    <CONFIG_PARTITION_TABLE_OFFSET>`) + 0x1000.

> A person transcribing a line from a document removes what looks like
> noise, because to a reader it **is** noise. The model was not being
> lazy; it was reading the way we read.

Two consequences. The rule belongs in the work order as an explicit
instruction — *paste the line with its markup, do not clean it* — and
not as an assumption that anyone would guess it. And the repair is
always to fix the **quote**, never to loosen the comparison: kind 27
measured that loosening recovers 3 records and breaks 10.

### Law 6-bis: stated mechanics hold, a named prohibition does not

One maintainer removed the *description of the gate* from the order and
left the prohibition in place.

    gate described     →  0 self-references in 2791
    gate not described →  2 self-references in 120

A helper who knows the address will be checked has nothing to gain from
inventing one. A helper who does not know invents — not from malice,
but because a plausible address looks more useful than none.

### Law 7: ask about the need, not about the guess

A field named "which document would answer" reads two ways: as an
*explanation of the classification* and as an *order for acquisition*.
Both readings are reasonable.

> **Price:** 507 units produced **472 distinct phrasings**, and almost
> half named documents already in the cache.

Ask **"which document were you missing"**, and add "if it is already in
the cache, name its file". Then the answer splits itself.

> **General form:** a field that can be understood two ways will be
> filled both ways, and you will get neither cleanly.

---

## 5. Explain, do not forbid

For a long time helpers were given only prohibitions. That is a
mistake: a list of prohibitions does not say what **to do**, and does
not explain why the honest answer pays.

A work order should open with three things:

1. **Who will read the book and what a mistake costs.** Not
   abstractly: "a person in the field, no internet, will take a number
   and wire up hardware".
2. **What happens to the helper's work next.** "The quote is checked as
   a substring in the named file, character by character. An invented
   one will be caught **certainly**, not probably — and all the work on
   that record is lost."
3. **That the honest answer costs three lines and always passes.**

Only then the prohibitions.

The phrasing that proved effective: *I say this not as a threat, but so
you do not spend effort on something that will not pass anyway.*

**Do not forbid helpers to fetch sources.** That was a wrong answer to
a right observation. Fabrication is already closed mechanically; if a
helper downloads the document into the cache, the same check applies
unchanged.

---

## 6. Intake gates

Checking goes **before** acceptance, not after. A defect is cheaper to
keep out than to fish back out of the registry.

Minimum set:

1. the record parses;
2. the verdict is one of the known words;
3. class `A`/`B` has a non-empty quote (evidence without a quote is not
   evidence);
4. the quote is a **substring of the named file**;
5. the source is not a file of the book itself;
6. the source **names a document**, not a property of the world;
7. the pattern compiles — whole, and each alternative separately;
8. the pattern does not match **control strings** absent from the
   registry;
9. **no alternative is a leak** — none catches more than all the others
   together.

**One word can name fields in more than one schema, and a rename by
search-and-replace will corrupt the others.** This project carries
three:

    evidence records   title, match, status, source, quote, method, note
    triage records     rid, look_for, chomu, id, text
    helper output      id, verdict, source, quote, file, looked_at

`look_for` lives in two of them, `quote` in two, and the class letter is
both a record field and a property of a registry unit. A migration
inventory built by grep cannot see the boundary: converting one tool's
`look_for` moved it to the wrong schema, its selector then matched
**zero** candidates, and it reported no problem at all — because
finding nothing is what a filter that matches nothing does.

> Before renaming a field, ask which **schema** the reader belongs to,
> not which word it uses. And convert the **writers**, not only the
> readers: after the old names are dropped, the first tool that writes a
> record puts them back, one landing at a time, and the migration decays
> silently for weeks.

**Normalise markup, not content.** Strip quotation marks and typographic
apostrophes from the comparison entirely: the document has
`Timer Task ("Tmr Svc")` and the helper writes `Timer Task (Tmr Svc)` —
an honest extract dies. Removing them raised the survival rate from
**38 % to 45 %**: seven percent of the "defects" were the gate's own
fault. Leave words, numbers and case alone — `serial clock bus (SCL)`
against `serial clock line (SCL)` is a real defect and must die.

**Make condition 6 a positive test** ("does it name a document"), not a
blacklist of phrases. A blacklist of phrasings found zero where a
positive test found 45. And the same blacklist thinking, applied in the
other direction, flagged seven fabricated document names of which
**three were real documents named in prose**.

> Check a document name by asking **"does such a file exist"**, never
> "does it sound like a document". The shape of a phrase distinguishes
> the real from the invented in neither direction.

---

## 7. Sources and the cache

- The cache of files stays **out of version control**; the **manifest**
  goes in: URL, sha256, size, date.

  Two reasons, and they are worth keeping apart because the first is
  often stated badly.

  **Not confidentiality.** Everything in the cache was fetched from a
  public URL. Nothing there is secret, no non-disclosure applies, and
  putting it in a repository would disclose nothing that was not already
  disclosed. Any account of this that talks about a leak is wrong.

  **Redistribution, and only for part of it.** Copyright governs copying,
  not secrecy, so "already public" does not settle it — a published book
  is maximally public and maximally copyrighted. Most of this cache is
  ESP-IDF source and `.rst` documentation under Apache-2.0, which is
  redistributable with attribution and entirely fine. The narrow part is
  vendor PDFs, where the licence is usually unstated and republishing
  them from our repository is a different act from fetching them to
  read. "Ambiguous" is the honest word there, not "violation".

  **And an engineering reason that stands on its own.** The manifest —
  URL, hash, size — *is* the reproducibility record. It proves what was
  checked against, in kilobytes, without carrying hundreds of megabytes
  of binaries into a history from which they can never be removed. This
  reason survives whatever one concludes about the first two.
- **A URL is the default identifier of a source.** Not an ISBN, not a
  document title, not "the manufacturer's datasheet". The reason is
  narrow: a URL is the only form a script can check without a human.
  Everything else requires somebody to open the document and look. Books,
  ISBNs and local documents are supported as an **exception**, not as an
  equal option — designing for every possible kind of source at once means
  never getting layer 3 at all.
- **Evidence that bypassed the cache is evidence with an expiry date.**
  Of 213 distinct addresses named by one maintainer's evidence, **two**
  were in the manifest; the other maintainer had one of twenty-seven. The
  records were honest — the document was fetched, the quote checked as a
  substring — but fetched *past* the cache, into a temporary directory
  that is not in the tree. The consequence shows up later: those addresses
  point at a moving branch, a reader checking the quote a year on sees
  different text and cannot tell our oversight from our invention, and
  layer 3 does not check such records at all because it looks in the
  cache and they are not there.

  > **Evidence is finished not when the quote is verified, but when the
  > source is in the manifest.** Verification without the cache attests
  > only that a maintainer saw something; nobody can reproduce it.

  The cheap symptom: `not in cache` rising in the layer-3 report after a
  landing wave. If a wave added evidence and the "verified" number did not
  move, the sources went past the cache.
- **The cache and the matcher are one thing living in two places.**
  Downloading a document is half the work; the other half is telling
  the matcher it exists. Thirteen fresh datasheets sat unused because
  no key referred to them — and nothing showed it except a number that
  did not move.
- **Specific before general in matching.** A key carrying a part number
  is always more specific than a key carrying a topic. Taking the first
  match in an unordered list lets general keys swallow everything.
- **More than one file per key.** Documentation is often split (commands
  in one page, options in another) and a claim is verifiable by neither
  alone.
- **A cache entry can be the wrong document under the right name.** A
  file named for one datasheet contained a schematic of an unrelated
  board: the vendor serves something else at that URL. Real PDF, real
  vendor, right filename. **No layer sees this.** It was caught by a
  helper who honestly wrote what it saw — that is, by the work order
  making the honest answer cheap.
- **Never key the cache by the last path segment.** `gpio.rst`,
  `README.md`, `i2c.rst` exist in a dozen directories of the same
  project; two different documents silently overwrote each other,
  together with their manifest rows. Nineteen records were destroyed
  before it was noticed. Key by a hash of the URL.
- **Distinguish kinds of unreachability**, because they are cured by
  different things:

      tool filter        the site serves a browser, not a fetch tool
      address-range ban  403 arrives in a real browser too
      paid standard      cured by nothing except money
      no source exists   cured by nothing

  One number called "unreachable" hides that difference, and the
  remainder then looks like a debt when part of it is nobody's.

- **A wrong machine-readable pointer is worse than prose.** Prose
  honestly says "a human will work it out"; a pointer promises
  verifiability and lies. Resolving 201 prose sources by name similarity
  produced 172 pointers, of which **73 named the wrong document** —
  a driver instead of a datasheet, one battery instead of another.
  All 137 that did not verify were reverted.
- **Resolve a source only by checking that the quote is actually
  there**, never by "the name looks similar". The same rule as for
  document names, approached from the other end.
- **A URL can be recovered by verification even when it cannot be
  derived.** Cache filenames carry eight hex characters of the URL's
  hash, which is one-way — but candidate URLs can be generated and
  hashed until one matches. Twenty-five of thirty-two were recovered
  this way with certainty, where guessing by name had failed.
- **A name derived from an absent URL is worse than no name.** A pass
  that renames cache files to the canonical `<hash>-<basename>` form
  read the manifest's URL column, and one row held an em-dash — the
  placeholder for *no URL at all*. It produced `bda05058-_`: a
  canonical-looking name derived from nothing. **The name is derived
  from the URL, so where there is no URL there is no name**, and the
  row must be left alone.
- **Rows with no URL are unreproducible by definition, and they hide.**
  Five files in this cache have no URL. They are real documents, they
  hash correctly, and no check called them out — because every check
  asked "does the file match its hash", and they do. A manifest whose
  purpose is reproducibility should count its own rows that cannot
  reproduce.
- **The manifest can register the book as a source.** Seven book files
  were removed from the cache and four came back with the next
  download, because eight manifest rows pointed at the book's own raw
  URLs. Removing the effect while leaving the cause is postponement,
  not repair — and it was only noticed because the download ran again
  the next day.


---

## 8. Working in pairs

- **One owner per file.** A tool writing to a hard-coded name silently
  overwrote the other maintainer's work order.
- **Correspondence is separate immutable files** with a UTC timestamp
  in the name and a "in reply to" field. An open question **stops the
  release**: that is not etiquette, it is the state of the work.
- **A work order lives in the repository, not in a temporary
  directory.** It explains the defects; it has no right to vanish with
  the session.
- **Write knowledge into documents, not into context.** Whatever is not
  written down is destroyed by the next context compaction and has to
  be bought a second time.
- **A report for exchange belongs in the correspondence folder**, not
  in the data directory, and it must be signed like a letter.

---

## 9. Measuring versus harvesting

For **measurement** the sample must be **random**, with the seed
recorded in the work order itself. A sample picked by hand "where the
light is" gives a percentage inflated by construction.

For **harvesting** the opposite is correct — take where the light is;
it is efficient and deceives nobody, as long as no percentage is quoted
from such a sample.

Do not mix the two in one work order.

**And record the seed, not only the result.** `sort -R` without a fixed
random source cannot be repeated by anyone, including its author the
next day — which is precisely the rule we demand of helpers.

**But the seed alone does not reproduce a sample.** It reproduces the
*draw*; the draw runs over a population, and the population moves every
time anybody lands a piece of evidence. Measured: the same seed over the
`F` queue gave one hundred units in the morning and a **different**
hundred seven hours later, because the queue had gone from 1740 to 1749.
The morning's re-run agreed, and that agreement was true for that minute
only.

So a measurement run records three things, each closing a different
hole:

    seed             to repeat the draw
    population hash  to see that the population is no longer the same
    the drawn ids    to have the units themselves when the draw
                     cannot be repeated

The list of ids is the only one that survives a moving queue. It is
weaker than a seed — it does not prove the draw was honest — and
stronger — the result can be recomputed a month later.

### Version the work order, or the comparison is memory

The work order **is** the part of the technology that acts on the
helper. Ours changed nine times and every change was measured — but the
result could not be attributed to the change, because nothing in a run
recorded which order produced it.

> Changing the work order changes the technology. Changing a technology
> without a version is not an experiment; it is weather.

Every generated order now carries `order_version` — a hash of its own
template — and so does the run's sample file. A ledger joins them, one
row per run, appended and never edited. Two rows with the same version
are one technology measured twice, and a difference between them is
noise. Two rows with different versions are two technologies, and the
diff between the versions is the cause.

---

## 9-bis. The tooling is a program too, and nothing was checking it

Two things belong here that were built, are running, and had never been
written down anywhere but their own source files. Both are the cheapest
kind of asset to lose: a method described in a document has to be
rebuilt by whoever needs it next, from a description, under pressure.

### Capture every entry point, then diff

`make check` runs eighteen targets; the technology has far more runnable
entry points than that. A field-name migration passed `make check` green
**three times** while nine places were broken — and every one of them
lived in a command no target invokes. All nine were found by running
everything and diffing the output. The same harness then caught three
more during a tool rename.

    tools/entry_points.py --capture DIR    run everything, save output
    tools/entry_points.py --diff A B       compare two captures
    tools/entry_points.py --missing        what no target covers

Use it around any change that is supposed to be behaviour-preserving —
renames, refactors, migrations — where "it still works" is a claim about
dozens of programs and not about one. Three rules were paid for:

- **Restore only what was clean before each point.** An earlier version
  ran `git checkout -- .` and ate uncommitted work twice.
- **Normalise anything that changes per run.** Two entry points printed
  a temporary directory name, so two captures of them could never agree.
  A snapshot that always differs from itself is not a snapshot.
- **An entry point covered only by its own usage message is covered
  exactly as much as it was never run.** Give the ones that require
  arguments their arguments.

### Every document declares its kind, and the kind is checked

    generated   a tool rewrites it; editing it by hand is wasted work
    canonical   the authoritative statement; one owner, no copies
    historical  a record of a past wave; never edited, numbers frozen

Without this, a maintainer hand-merges a conflict in a file a tool
overwrites minutes later — which happened — and a reader has no way to
know that the number in front of them was true only on the day it was
written.

The label is checked **both ways**: a document labelled generated must
actually be written by the tool it names, and a document not so labelled
must not be written by any tool. Detection is by AST over the tool
sources, not by reading.

> A label nobody verifies is a comment.

And a companion rule, because the index is the first thing a newcomer
reads: **every document in the folder must appear in it.** Measured
here, 17 of 32 did not — including all four English documents that carry
the method to another book.

---

## 10. Rules about checks themselves

**The dominating failure, stated first because it caused five of the rest.**
In one day, five tools promised something their bodies did not do:

| Where | Promised | Did |
|---|---|---|
| the landing gate | two checks | one |
| a sweep generator | a candidate for every packet | none, silently |
| `stale` | compare the book's text | check whether the file exists |
| the card-format pattern | readers take the format from one place | each held a copy |
| the correspondence tool | a badly named letter is a violation | the letter vanished from the accounting |

The last cost the most: **two letters nobody saw.** Their filenames held
Cyrillic characters, the pattern accepted only `[a-z0-9-]`, and a file that
did not match was treated as "not a message". A finding about a broken
layer 1 lay invisible, and the very check meant to stop a release over an
open question did not react to it. It was found by accident — a reply to
one of those letters could not find its addressee.

> **Zero looks the same whether all is well or the counter is counting
> nothing.** And we read it as the first, every time.

From which the rule of contribution, stronger than reviewing docstrings:

> **Every new check must be demonstrated working on a deliberately broken
> input**, and that demonstration is part of the contribution rather than
> extra work. A check that has never fired is indistinguishable from a
> check that does not exist.


- **A new check that disagrees with the previous one by a factor of two
  or more is broken until proven otherwise.** Verify one case by hand
  before reporting.
- **A pleasant number deserves more suspicion than an unpleasant one.**
  Toward "everything is bad" people stop by themselves; toward
  "everything is fine" they do not. A wrong check once reported the
  book as 100 % verified.
- **A check that filters on a field the maintainer writes measures the
  maintainer, not the subject.** Filter on the book's text; the record's
  title is a signature, not data. This one kind cost four separate
  incidents in two days, and each time the code ran and stayed silent.
- **A docstring that promises more than the code does is worse than a
  missing check**, because the invariant is believed to be protected and
  is protected by nobody. Found twice, in two different tools.
- **A pattern read from someone else's format must live in one place
  with whoever writes that format.** A copy of a pattern is a promise
  not to change the format that nobody made.
- **A check that normalises presentation must not eat content.** A rule
  joining hyphenated line breaks (`-\s*\n\s*` → nothing) also deleted
  **em-dashes at end of line**, and 127 cards appeared to have a context
  that did not contain their own claim. Join only a true word break:
  a hyphen flush between letters.
- **A context that does not contain its own claim is worse than no
  context** — it tells the reviewer they hold the surroundings when they
  hold someone else's. Layer 1 must check this, and nothing else will.

---

## 11. Testing the method on itself

A method that changes faster than it is measured is not a method, it is
a habit. A controlled run costs five helpers and twenty minutes, and it
is the only way to know whether the last three changes helped.

### The shape that worked

Twenty-five units drawn at random from the unchecked pool, **seed
recorded**, five per helper, five helpers, cheapest model. Work order
carrying all seven laws, the three-layer explanation, and the seven
traps by name.

    accepted by the gate      25 of 25
    confirmed with a quote     7
    honest "not found"        18
    self-references            0
    fabricated sources         0

Two of the seven confirmations rest on a datasheet the helpers
**fetched themselves** — a document that was not in the cache when the
run started. Permission to fetch, plus a quote checked as a substring,
turned out to cost nothing and buy real evidence.

### What the run found about the work order

**A path in the work order had gone stale.** It named a checking script
at its old location, moved days earlier. Helpers were told to
self-check and could not. At least one reported that validation had
passed.

> A work order is code that runs in someone else's head. It rots like
> code — and unlike code, nothing fails loudly when it does. Every path
> and filename in a work order needs the same treatment as an import.

### And what the run found about the person running it

I read the output files **while the helpers were still writing them**,
and measured: 17 rejections of 25, four confirmations citing the book,
and a mismatch between one helper's report and its own file. I was
composing the regression report when the last helper finished.

The final numbers were 25 accepted, zero rejections, zero
self-references, and every report matching its file. **All three
findings were artefacts of reading a file mid-write.**

**And it happened a third time, with the guard in place.** A status
listing showed a helper as `completed` while its file was still growing
— 2343 bytes when read, 3465 when the completion notification finally
arrived. The measurement taken in between reported 13 confirmations; the
real number was 18.

> The only reliable sign that a helper has finished is **its completion
> notification**. A status line in a listing is not that sign, and it is
> more dangerous than an obviously running job, because it invites the
> measurement.

> Measure only finished work. A partial file is not a small truth; it
> is a different file. The rule that saved this — check one case by
> hand before reporting — is the same one that has now caught six false
> alarms, and it works only if you apply it before you believe the
> number, not after.
