# Fact-checking a book with a pool of cheap helpers

> **canonical** — the decision lives here; there are to be no copies

This document is **not about ESP32**. It is about the method, written so
that it can be lifted onto another book, another subject, another
language.

Everything here was bought with a mistake — ours. Where the price is
known, it is named: how many records had to be thrown away, how many
units vanished silently, how long it took to notice.

This file is the whole of it. Part I is the reasoning; Parts II–V are
the reference works it leans on — the record format, the catalogue of
defect kinds, the specification of a work order, and the log of what was
tried on the helper pool and how it failed.

It was five separate documents until 2026-08-29, and the split cost more
than it bought: a reader had to know which of five to open, and four of
the five drifted from the code because nothing joined them.

---

---

# Part I — The method

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

> **Authority: Part II, "Evidence statuses".** If this list and that one
> disagree, that one is right and this one is stale.
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

**And yet the class has to exist, which is easy to forget after four
sections of warnings about it.** `no-external-signal` is what gives the
queue a **floor**. Without it **79 % of this book's units** would hang
in `unchecked` for ever, and the genuine work would drown in editorial
prose that was never going to have a source. Every danger listed above
is the price of that floor, not an argument against it.

### Trap: class `E` holds two incompatible kinds

`E` is assigned mechanically where the text carries no checkable
signal. But under one letter you end up with:

- a technical claim that merely failed to carry a signal — **a debt**;
- the author speaking in their own voice — **finished by nature**.

They must be separate classes. Otherwise half the book sits in a
category that means two opposite things.

**How large this is.** There are **152** such verdicts in the tree, and
they sit on **247** units that contain a number with a unit of measure —
that is, on exactly the claims most likely to have a document behind them.

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

That rule — **an assertion must pay for itself** — held a second time in
the other maintainer's run, at **931 of 931**. One clean result is a
result; two, from different hands on different queues, is a property of
the order's shape rather than a coincidence.

The full distribution of that pool run is worth printing, because it shows
what replaced the forbidden answer rather than merely that it was
forbidden:

| Verdict | Records | Share |
|---|---:|---:|
| advice — the verdict was justified | 45 | 53 % |
| unreachable | 16 | 19 % |
| did not find | 13 | 15 % |
| **confirmed — a source was found** | **10** | **12 %** |
| disputes | 1 | 1 % |

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
by machine — 335 pieces of evidence in one sweep — produced three failures
in a row, and all three were a gap
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
  move, the sources went past the cache. **That report read `not in cache
  188` for weeks and was taken for noise; it was a bill.**
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

---

# Part II — The record format

One record = one claim of the book. A record is never edited by hand above
the `**Доказ**` line: everything above it is generated by
`tools/factcheck.py` from the book itself, and that is exactly why it is
verbatim.

```
<!-- fc id:T-06-047 sha:9f3c1a20 src:manual/06-zhyvlennya.md:55 klas:A -->
#### T-06-047 · proza · `manual/06-zhyvlennya.md`

**Твердження, коротко**

> джерело для ESP32 з Wi-Fi має тягнути щонайменше 1 А

**Контекст**

```
### Скільки треба струму

…the whole paragraph…
```

**Доказ**

- **Статус:** verbatim — primary, quoted
- **Джерело:** https://raw.githubusercontent.com/…
- **Дослівно з джерела:**
  > …
- **Спосіб і дата:** obtained 2026-08-26, checked as a substring
- **Нотатка:** …
```

The card's own headings stay Ukrainian: a card is read beside the book,
and the book is Ukrainian. The technology that produces it is not.

### The card as a format — and what it promises

The card format used to live **only in the generator's code**. The audit of
2026-08-28 showed where that ends: a promise written nowhere is checked by
nobody, and 5194 cards out of 8331 broke off mid-sentence until somebody
looked.

> **The requirement.** A living person or an outside reviewer picks up a
> card **knowing neither the book nor this technology**, and must be able
> to say: here is the claim, here is its surrounding, here is the source —
> and it checks out. A card you must open the book to understand is
> defective by definition, even if everything in it is true.

The blocks of a card, in order:

| Block | Always? | What is in it |
|---|---|---|
| service comment | yes | `id`, `sha`, `src`, `klas` — for the machine |
| heading | yes | `id`, kind of unit, book file |
| **the claim, briefly** | yes | for prose, a code line, a schematic connection — the **book's verbatim text**; for a table cell — the rendering |
| **verbatim from the book** | renderings only | the raw table row as it stands in the file |
| **context** | yes | section heading, table header, paragraph or neighbouring lines |
| **evidence** | yes | status and record fields; with no evidence, an `unchecked` stub |

Two limits worth knowing when reading a card:

**The evidence block is always there — it is a rubric, not coverage.**
With no evidence it holds "unchecked". A hundred per cent of cards have
that block, and it means nothing. Coverage is a separate number, in
`factcheck.py status`.

**The line number appears only in the service comment, and it goes stale.**
It is deliberately absent from the visible part of the card: any edit to
the book above the unit shifts it. The unit's anchor is `sha`. A
divergence is shown by `factcheck.py stale`.

### Fields of the service comment

| Field | What it is |
|---|---|
| `id` | stable identifier `T-<file prefix>-<number>` |
| `sha` | hash of the book's verbatim text; if the text changed, the evidence is in doubt |
| `src` | book file and line |
| `klas` | the evidence status, duplicating the field below for machine summaries |

`sha` is the heart of this schema. A registry that does not notice the book
changing underneath it is worse than no registry: it asserts checkedness
where the check applied to a previous wording. `factcheck.py sketch` is
re-run after every text edit and marks such records unchecked again.

### Evidence statuses

| Status | What it means |
|---|---|
| **verbatim** | **primary, quoted.** The primary source was obtained in this session and the extract is quoted verbatim. The strongest. |
| **derived** | **primary, inferred.** The primary source was obtained and the claim follows from it unambiguously, but there is no verbatim phrase. Example: the value `#define SOC_UART_NUM 3` proves "three UART controllers", although it does not say so. |
| **named-unreachable** | **secondary.** The source exists and is known, but **cannot be reached from this environment** (egress policy). The URL is recorded, and what to look for in it. A verbatim quote **is not given**. |
| **arithmetic** | **calculation.** Checked by arithmetic; no external source is needed and none exists. The calculation is given. |
| **no-external-signal** | **the text carries no signal for an external check.** Assigned mechanically — for want of a number, identifier, name or unit of measure. It does **not** mean "no source exists": it is the consequence of a rule, not a conclusion about the world. Mostly it is the author's position, but not always — see below. |
| **absent-from-source** | **proof by absence.** The document was obtained, and what was named **is not in it** — the document's silence is the proof. `SOC_BT_SUPPORTED` is absent from `esp32s2/soc_caps.h`, and that proves the S2 has no Bluetooth. Requires `source` and `absent` (the line that is not there); `control` — a document of the same kind where the line **is** present — is optional, but without it the evidence is weak. The only status layer 3 can **refute**: if the line is found in the document, the evidence is not divergent but false. |
| **self-consistent** | **internal check.** The claim is checked not against an external document but against **another place in this same book**: a chapter against its own code, a summary against a table, a project against a pinout. It says nothing about the world — the book may be wrong in both places together — but it says something checkable about the book: that it agrees with itself. Stronger than `looked-not-found` (a check was made, and it agreed), weaker than `named-unreachable` (which names a document that could settle the question outside). Requires `source` holding a **path to a book file**; passes layer 3 against the book. It is **not** counted in the "checked" figure and is shown on its own line. |
| **looked-not-found** | **looked and did not find.** A maintainer or helper opened the document and did not see the source in it. This is a **report of work**, not a verdict about the world: weaker than `named-unreachable` (which names a source), stronger than `no-external-signal` (which is a verdict). Requires `looked_at`. |
| **unchecked** | **not checked.** The default state. |
| **refuted** | **refuted, or needs an edit.** A finding; goes to `reviews/`. |
| **code-context** | **context.** A whole code or schematic block. Not a claim: the claims live in its lines. Not counted in percentages. |

### Fields of an evidence record

Evidence lives in `factcheck/evidence/*.yaml`. **This is the normative list
of fields**; until now it existed nowhere, and helpers guessed the format —
which accounts for half the waste of the pool's first wave.

Field names are English. The Ukrainian ones (`nazva`, `zbih`, `klas`, …)
still stand **beside** them in every record — that is the state of a
migration, not two formats: see `book/MIGRATION.md`. You may read either;
you must write English.

**Three fields are present in every one of the 1337 records**, and that is
the whole of the mandatory part:

| Field | What it is |
|---|---|
| `title` | short name of the evidence; with the file it forms the accounting key |
| `status` | a status from the table above (`verbatim`, `derived`, …) |
| `match` | the pattern binding the evidence to units of the book |

**The rest is optional, and that is exactly why the record seems to have
many forms.** The audit counted 28 different field sets and called it the
main obstacle to portability. That conclusion is wrong: 28 sets are not 28
dictionaries but subsets of one. There is one schema, ten fields, and which
of them are present depends on the status:

| Field | Records | When it must be there |
|---|---:|---|
| `sha` | 829 | once the binding has moved to a hash (see `book/MIGRATION.md`) |
| `source` | 1315 | for `verbatim`, `derived`, `named-unreachable` |
| `quote` | 1208 | for `verbatim` — the verbatim extract, copied from the file |
| `method` | 1268 | how and when it was obtained; who assigned the status |
| `note` | 1323 | what follows from it for the book |
| `look_for` | 98 | for `named-unreachable` — what to look for in the unreachable document |
| `calculation` | 20 | for `arithmetic` — the calculation itself |
| `looked_at` | — | for `looked-not-found` — **what exactly was opened** |

> A field set that depends on the status is not disorder, it is normal
> form. Disorder would be the same information written sometimes into one
> field and sometimes into another.

**And that is precisely what was here.** The very first run of
`tools/schema.py` found 18 violations, four of them mine: `arithmetic`
records in which the calculation itself stood in `quote` instead of
`calculation`. That is "the same thing in different fields" — exactly what
the paragraph above had just called disorder.

The paragraph originally ended with the words "checked, every field means
the same thing in all 1337 records". That was written **before** the check
existed, and turned out to be untrue within minutes.

> The word "checked" in a description of a format is worth exactly as much
> as the check that holds it up. Without one it is not a description but a
> hope.

The remaining fourteen are M2's records: eight `arithmetic` with no
calculation, and six `named-unreachable` **with no source named**. The
second is worse: `named-unreachable` exists precisely to name an
unreachable document, and without one the record can be neither carried out
nor refuted.

#### Where `looked-not-found` came from

Not from wanting more statuses. Seven records fell between two rules:
`named-unreachable` requires a named source, which they did not have;
`unchecked` means there is no evidence, and then the record means nothing.
Trying to close that by changing the status produced kind 15 in
`DEFECTS.md`.

The argument that settled it belongs to M2: **we already had this state** —
in the vocabulary of work orders. The verdict `ne_znayshov` has lived in
`leads.py` since wave 3 and requires a field naming the document that was
opened. Helpers had been recording "looked and did not find" for three
days, and the schema had nowhere to put it, so we translated it by hand
into either `named-unreachable` or `unchecked` — each time untruthfully.

`looked_at` is mandatory for exactly the reason that `named-unreachable`
was also supposed to name a document — and in six records did not.

This table is checked by `tools/schema.py`, in both directions: that the
mandatory fields are present, and that nothing a status requires is
missing. Along with it, the tool holds the **card contract** from the
section above.

#### Where `absent-from-source` came from, and how it differs

M2's finding at 19:22Z, and it was found not by a tool but by a **helper**.

On `T-02-087` the helper opened `esp32s2/include/soc/soc_caps.h` and wrote
into the quote field:

    (no SOC_BT_SUPPORTED in esp32s2/include/soc/soc_caps.h)

The gate rejected it: that is not a quote, it is a description of an
absence. But **the work was right and the conclusion was right** — the S2
really has no Bluetooth. M2 proved it the same way that day and had to
invent a way around it: `derived` with an explanation in `method`.

> The order had no verdict for proof by absence. The helper did honest work
> and had no lawful way to record it.

**This is not `looked-not-found`.** That one says "we looked for a source
and did not find it" — a report of work, weak. Here it is the opposite:
**the source was found, opened, and its silence is the proof**. The
strength is entirely different, which is why it sits next to `derived` and
not next to `looked-not-found`.

### Why the `control` field is needed

Silence does not always prove. A file may be silent because it is of a
different format, or because the property is called something else there.

Measured on this same case: `SOC_BT_SUPPORTED` is present in **all ten**
other `soc_caps.h` files in the cache — `esp32`, `c3`, `c6`, `h2`, `s3` —
and absent from `esp32s2` exactly. That is what makes the silence a
statement.

    esp32     SOC_BT_SUPPORTED: present
    esp32c3   present    esp32c6   present
    esp32h2   present    esp32s3   present
    esp32s2   ABSENT     ← and that is the proof

So `control` names a document of the same kind where the line **is**
present. Not mandatory — because it does not always exist — but the
evidence is weaker without it, and that is said here rather than implied.

### The only status layer 3 refutes

For every other status layer 3 asks "does this line stand in the document",
and "no" means a quote divergence — often a false alarm: a line wrap, a
table in a PDF, markup. Here the question is inverted, and the answer is
unambiguous:

> If the line whose **absence** is the evidence is found in the document,
> the evidence is not divergent — it is false.

Demonstrated on three cases: a genuine absence (S2) — `ok`; the same line
against the S3, where it is present — `REFUTED`; a record with no `absent`
field — an error, because there is nothing to not look for.

#### Where `self-consistent` came from

From the same place as `looked-not-found`, and with the same mistake at the
start.

Twenty-one of M2's records proved a claim of the book **by the book
itself** — `ВНУТРІШНЯ ЗВІРКА (книга проти себе)` — under `verbatim`.
Eighteen `verbatim`, three `derived`. M2 raised the question and left the
vocabulary to M1: is this `no-external-signal`, or a new status?

`no-external-signal` is wrong, and the reason is exact: it means **no check
was made**, whereas here one was — mechanical, reproducible, and it agreed.
Merging them would throw away the only thing these records had measured.

`verbatim` is wrong from the other side, and more expensively: it counts
towards the "checked against a source" figure that a reader sees first.
Twenty-one records with no external confirmation were inflating that
figure. After the move: 2383 → 2362, 29.4 % → 29.1 %. **The registry shows
less checked, and that is the honest number** — the same operation M2
performed on 22 records when narrowing leaking patterns.

**A status without a check would have been worse than either option.**
`self-consistent` asserts that a check was made; if nobody made it
mechanically, it would be a label instead of a fact — kind 24 in
`DEFECTS.md`, recorded the same day. So `self-consistent` passes layer 3,
and its corpus is the book.

The first run of that layer gave **15 of 21 "nothing to check"** — and the
cause turned out to be more instructive than the status itself. `uryvky()`
discards lines in Cyrillic, because for an English datasheet Cyrillic is
our own note, not a quote. The rule is sound exactly as long as the source
is English: for `self-consistent` the source is **the book**, and every
genuine extract is Cyrillic.

> A filter that is sound for one corpus, applied to another, discards
> everything — and stays silent with the same word it uses for "clean".

After the `vlasna_mova` flag: **21 of 21 agreed verbatim**. One record had
had no path in its source at all ("chapter 60's own code") — so the status
worked within its first hour: it requires an address, and without an
address the record does not pass.

#### `source` — a named document, not a topic

The requirement is not "a URL" but **the identity of the document**. The
first rule was "URL-first", and it would have marked as invented thirteen
honest references to PDFs with no stable address:

```yaml
dzherelo: >-
  Texas Instruments, PCF8574 Remote 8-Bit I/O Expander for I2C Bus
  (SCPS068), розділ «Features»
```

That is a full citation. Hence: **a URL is an advantage, the identity of
the document is the requirement.** Publisher + title + revision number will
do; "the properties of CMOS logic" or "well-known relay electromechanics"
will not.

The abbreviation `.../components/...` for the second and later files
**must not be written**. It is readable to a person and uncheckable by a
script; a quarter of the records were silently uncheckable because of it.

A separate case is a **source inside the book**: its own listing against
its own prose. That is legitimate and is named plainly; `layer3.py` does
not check such records, and that is stated in `METHOD.md` §3.

#### `match` — the pattern is written against the **registry**, not the book

The pattern is matched against **the text of a registry unit**, not against
the book's markup. For prose these are the same thing, which is exactly why
the mistake does not catch the eye. For a table cell they are different
strings:

```
book:      | Частота | 160–240 МГц | 16 МГц | 133 МГц |
registry:  Частота · RP2040 → 133 МГц
```

The pattern `\| 133 МГц \|` matches the book and matches **nothing** in the
registry. `grep` over `manual/` says "all is well", and the evidence
silently touches nothing.

**Check it only this way:**

    tools/factcheck.py vzirets '<expression>'

The command counts how many **registry** units a pattern touches, and warns
separately about two states: idle (zero) and too wide (more than a dozen).

The price of this rule is known. M2 wrote a faster coverage check over the
book's text: it declared 182 evidences idle instead of 58, and deletion had
already begun — 124 sound records survived. I, knowing about the trap and
having written it into `docs/DESIGN.md` as `Р-ЗВІРКА`, stepped on it
**three times in the same evening**, because `grep` over the book is
cheaper than the correct check.

Hence the command: as long as the right thing is more expensive than the
wrong one, the rule does not work.

#### An idle alternative inside a live evidence — kind 2, `DEFECTS.md`

A separate state that no gate ever showed: a pattern of several
alternatives where the first one fired and the rest match nothing. The
record looks perfectly healthy.

This matters precisely because alternatives **accumulate**: an evidence is
stretched from a chapter onto cards and appendices by adding branches, and
each branch is a fresh chance to miss silently. `sketch -v` counts them
separately; the usual causes are a capital letter at the start of a
sentence, a line wrap in the book where the pattern has a space, and a
change to the text itself.

**An alternative may be revived only after measurement.** A loosened
alternative that starts touching a dozen units is worse than an idle one: a
wide pattern is more dangerous than a missing one.

#### `verbatim` with no quote — a contradiction by definition

`verbatim` means "the primary source was obtained, the extract is quoted".
A `verbatim` record **without** a `quote` field means nothing — and it is
in exactly that emptiness that the subtlest kind of forgery in this project
took up residence.

M2's finding: the source field held

    ESP32 Series Datasheet v5.3, Table 6-21 та Pin Definitions
    ESP32 Series Datasheet v5.3, Boot Mode Selection section

The document name is right, the revision is right, the table number is
specific. **Neither `Table 6-21` nor `Boot Mode Selection` exists in that
document:** `Boot Mode Selection` is a heading from the esptool
documentation, and `Table 6-21` is Technical Reference Manual numbering,
whereas the Series Datasheet numbers its tables `2-1`, `5-3`.

What was invented was not the source but **a coordinate inside it**. And a
coordinate is more convincing than any argument: a table number looks like
work.

Why this passed through everything we have:

| Check | What it asks | Why it is silent |
|---|---|---|
| the source gate | is this a document? | the document is real |
| the cache gate | does the file download? | it downloads |
| layer 3 | is the quote in the source? | there is **no quote at all** |

Hence the gate: **`verbatim` (or a table-cell quote) with no extract is a
false record.** Requiring the extract where the status promises one is the
only way to keep out a coordinate with no text behind it.

#### Proof by absence — what the format cannot do

The commonest kind of negative claim in this book is proved by what is
**not** in a document. And that is exactly what our format could not
express.

The example was found by the `unchecked` measure. The book says "BLE · S2 →
**no**". The claim is right, and it is proved unambiguously: there is no
`SOC_BLE_SUPPORTED` line anywhere in `esp32s2/include/soc/soc_caps.h`,
whereas it is present in `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3`.

But the `quote` field is checked **by substring**, and an absence has no
substring. It cannot be filled in correctly.

The consequence is predictable and was duly observed: a helper obliged to
fill the field substituted the nearest line from the same file —
`SOC_WIFI_SUPPORTED 1`. The quote is verbatim, layer 3 passed it, and it
proves something else entirely about the same chip. **This is a defect of
the format, not of the helper:** he was given a form in which no correct
answer exists.

The interim rule, while the format lacked one:

> A claim of the form "this is not in the document" is `derived`, not
> `verbatim`. Into `quote` goes what **is** in the document and what
> narrows the list (for instance the line about a neighbouring chip where
> the macro is present), and `note` explains that the proof is the absence.

What the format lacked: a field of the form `absent` — a pattern that must
not be in the document, checked as "the source was obtained **and** the
pattern does not occur in it". Then absence would become mechanically
checkable, just as presence is. That field now exists; see
`absent-from-source` above.

#### `quote` — a copy, not a retelling

Copied byte for byte out of a file that was genuinely opened. Do not rewrap
lines, do not strip RST markup, do not stitch two sentences into one, do
not correct the case.

Our own notes inside a quote are written **in Cyrillic**, or in brackets on
a separate line — that is how `tools/layer3.py` tells them from the
source's text.

#### `perevireno-okom` — a last resort, with a reason

It takes **a string with an explanation**, not `true`. A mark with no
reason is the same quiet lie from the other side.

It is used when, and only when, extracting the text destroys the structure
beyond repair. If that happens often, the extraction is what needs
improving, not the looking.

### The rule that is not up for discussion

**`verbatim` is assigned only when the source text was genuinely obtained
in this session and copied.** Never "I remember it says that".

The reason is simple: the fact-checking registry exists so that a reader
need not take the author's word. A quote reproduced from memory destroys
the very thing the registry was built for — and does so invisibly, because
it looks exactly like an honest one.

**I broke this rule myself, having it written down.** The `pass-31` record
gave the OTA error-code offsets as `+0x02` and `+0x04`; in the header they
are `+0x01` and `+0x03`. I reproduced the line from memory instead of
copying it, and assigned `verbatim`. Five passes and a stronger model went
past it, because the quote looked plausible; it was found by the cheapest
model in the set, comparing character by character.

Hence a conclusion wider than the rule: **the defect is not a property of
cheap models — it is a property of haste.** A cheap model makes it more
often, but does not invent it. The false `verbatim` in `pass-17` — "well-
known relay electromechanics" — I assigned ten passes before any pool
existed.

If the source is unreachable, that is `named-unreachable`, and it is a
normal, honest state. The list of such records is handed to a person with
open access (`tools/factcheck.py blocked`), and each is closed in minutes,
because all the preparation is done: what to look for, and in which
document.

### How `no-external-signal` is assigned

It is assigned **mechanically**, not by eye, and by one rule only: a unit
of kind `proza` whose text contains no externally checkable signal at all.

A signal is:

- any digit;
- anything in backticks — an identifier, a command, a log line;
- the name of a chip, bus, protocol, library or component;
- a unit of measure written out in words.

The criterion is deliberately biased towards `unchecked`: better to leave a
sentence that leads nowhere in the work queue than to close something that
should have been checked.

**The rule is never applied to tables, cells, code lines or schematic
connections.** That is exactly where the facts live, and a cell like
"0 · Touch → T1" looks empty only because the subject of the row stands
apart from it.

Why this exists at all. The registry is complete by construction, and among
thousands of units there are those for which no external source exists or
ever will: an editorial judgement, a piece of advice, a framing sentence, a
link between chapters. Keeping them `unchecked` promises work nobody will
do — and hides behind them the units that genuinely need checking.

#### What makes `no-external-signal` dangerous, and why it is measured apart

The rule above speaks of **an absence of signal in the text**. The verdict
it assigns reads as **"no source exists"**. These are not the same, and the
whole difference falls in our favour: a generous `no-external-signal` looks
like work done.

It is the only status that certifies itself. The others point outward:
`verbatim` says "here is the document", `named-unreachable` says "here is
where to look". `no-external-signal` says "do not look", and there is only
one way to check that — to look anyway.

Hence two different exercises, which **must not be confused**:

| Exercise | Question | Sample |
|---|---|---|
| the sweep (`tools/contest_e.py`) | what can be obtained | picked by hand — where the light is |
| the measure (`tools/sample.py`) | what share of the status is false | **random**, with a seed in the order |

A percentage from the sweep **may not** be carried over to the whole
status: the sample was selected by the very property being measured. A
percentage from a random sample may be, and only that one may be quoted as
a number.

One more thing the first sample showed: within `no-external-signal` there
are units that **are not claims about the world at all** — rows of a table
in which the book describes its own registry. That is a third state
alongside "the author's position" and "a misfiled claim", and it too has to
be counted separately.

### Kinds of unit

| Kind | What it is | How it is checked |
|---|---|---|
| `proza` | a sentence outside code and tables | a claim about the world; with no signal → `no-external-signal` |
| `tablycya` | **one row** of a narrow table | each row is a separate claim |
| `tablycya-shapka` | the header of a wide table | column names as claims |
| `komirka` | **one cell** of a wide table, in the form "row · column → value" | the table "UART \| 3 \| 2 \| 3 …" is six claims about six chips |
| `kod` | a whole code or schematic block | **context**, `code-context`; not checked |
| `kod-ryadok` | a code line that asserts something | a call, a constant, a command |
| `schema-zvyazok` | one connection of an ASCII schematic | **both ends**: the board pin and the peripheral pin are different sources |

A table row is broken out deliberately. A twenty-row "pin → limit" table is
twenty independent claims, and nineteen of them being checked says nothing
about the twentieth.

### What counts as one claim

A sentence with two independent facts is split into two records **during a
pass**, not automatically: a machine cannot see where a fact ends and its
restatement begins. The order is this — the tool gives a complete if coarse
decomposition; a pass refines the granularity where it is too coarse.

If a record is split, the new one takes the next free number in the file,
and a note remains in the old one: "split into T-…, T-…".

---

# Part III — The catalogue of defect kinds

Every kind of defect this project has found in **its own checking**, in
one place, so that finding it again is not the same work as finding it
the first time.

This exists because of a measured complaint: *"the technology keeps
drifting — we find new classes of problem and forget the ones already
found."* That is literally true. Both maintainers repeated, within two
days, a mistake described in a document one of them had written.

**How to use it.** A work order cites a row by name in one line. A new
check names the kind it defends against. A review of new evidence walks
the Symptom column.

**How to add to it.** A kind enters only with a measured case — a
number, not an impression — and with whatever check now holds it, or an
explicit note that nothing does.

---

### The family that dominates: a check that measures nothing

Thirteen of the thirty kinds below are one family. The check runs, it
returns a number, and the number means nothing — because it was never
measuring the thing its name claims.

> **Zero looks the same whether all is well or the counter is counting
> nothing.** And it is read as the first, every time.

Four of the thirteen were added the same day and sharpen the family,
each by weakening an assumption the earlier ones still made:

- kind 22 — the number need not be **zero**. An unchanged number is a
  better disguise than a zero, because a zero at least invites the
  question.
- kind 23 — the broken check need not be **wrong-looking**. An
  expression can keep the exact shape of a fallback and not be one.
- kind 24 — the check need not be **passing**. It can be red, correct,
  and uncalled, which is the same thing as green.
- kind 25 — the number need not be **wrong at all**. A correct count of
  a bucket holding two different worlds is a false statement that no
  counter can contradict.

The rule that follows from the family governs every contribution here:

> **Every new check must be demonstrated working on a deliberately
> broken input**, and that demonstration is part of the contribution. A
> check that has never fired is indistinguishable from a check that
> does not exist.

And its corollary, bought with kind 24:

> **A check that fires where nothing listens is indistinguishable from
> both.** The demonstration must be wired into a target, not left
> behind a flag.

---

### 1. Pattern too wide

**Symptom.** One evidence record marks many more claims "checked" than
its source could possibly settle.

**Measure.** Claims bound per record. Legitimate breadth exists (one
record covering 210 API-existence claims is correct), so width alone is
not the test — see kind 2.

**Case.** `ESP-IDF|esptool` bound 173 claims to one record about
version numbers. Three separate occurrences before it was named.

**Held by.** `factcheck.py sketch -v` prints what each record covered.

### 2. Pattern leak — the width hides in the shortest alternative

**Symptom.** A pattern reads as narrow: five specific alternatives and
one short one. The short one does all the work.

    evidence: "GPIO unconfigured at boot, the line floats"
    pattern:  старт|завантаж|GPIO.*?висить|невідом|стан
                                                    ↑ 242 claims

**Measure.** Widest alternative against the **sum of the rest**. Not
total width — that flags the legitimate case in kind 1.

**Case.** 22 records; 956 claims took their state from a leak; 237 were
presented as verified against a retrieved source. Closed down to 5
records / 81 claims; coverage fell 32.9 % → 30.0 % as a result.

**Held by.** `tools/leak.py` (with self-check).

### 3. A zero that counts nothing

**Symptom.** A check runs, reports zero, and is not measuring what its
name says.

**Case.** Five in one day:

| Where | Promised | Did |
|---|---|---|
| `vorota` | two checks | one |
| `sweep.py` | a candidate per packet | none, silently |
| `stale` | compare the book's text | check the file exists |
| card regex | readers share the format | each kept a private copy |
| `correspondence.py` name pattern | bad filename is a violation | the letter vanished |

`stale` ran for four days while six print-run corrections passed it.
The `zvyazok` one hid two of M2's letters, including the finding that
layer 1 was broken.

**Held by.** The demonstration rule above. Nothing else can.

### 4. A number used as an anchor

**Symptom.** Something durable — evidence, a queue, a snapshot — holds
a claim by its ordinal or line number. Both drift from any edit *above*
the claim.

**Measure.** `factcheck.py stale` separates three kinds: text changed,
unit appeared/vanished, line number shifted only.

**Case.** Six edits moved 1311 ids across 32 files. An id-keyed
snapshot reported 34 records "losing" claims; re-keyed by hash, 0 of
1337. The card locator once showed the ESP32-C3 row on the ESP8266
card.

> The number is the address where the claim lives today. The hash is
> what the claim **is**.

**Held by.** `factcheck.py stale`, `snapshot.py` (hash-keyed), hash
binding in evidence records.

### 5. Half a thought

**Symptom.** The reviewer is shown a fragment and judges it as if it
were whole.

**Case.** Four occurrences under three different names before it was
recognised as one kind: claim splitting cut a caveat into the next
unit; a table cell arrived without its header; a "verbatim" block cut
sentences mid-word on **5194 of 8331 cards** — cut by the tool built to
prevent exactly this.

Eleven claimed contradictions were traced to this. **Zero were real.**

**Held by.** `schema.py` (card contract: context on every card, the
verbatim block only where the claim is a render).

### 6. A verdict wearing the clothes of a state

**Symptom.** A state that records *what the rule did* is read as a
statement about the world.

**Case.** `E` means "this text has no number, identifier or part name
to check against". It was read, and once printed in the book, as "no
source exists". Two `E` verdicts were proven wrong outright; sampling
put the true rate near a quarter of those carrying a number.

**Held by.** Nothing automatic. `SCHEMA.md` states it; the book's own
description had to be corrected.

### 7. Prescription presented as documented

**Symptom.** The book says *must*; the source says *recommended* or
*may*. Every layer passes, because the quote is verbatim.

**Case.** `sdkconfig.defaults` in git — the source recommends, the book
forbids the alternative. The position is defensible and the book gives
its reason; what was wrong was presenting it as documented.

**Held by.** `tools/modality.py` — a report, not a gate. Its first
version was 88 % false positives; three rounds of exclusion brought 50
matches down to one real.

### 8. Filtering on the adjacent field

**Symptom.** A check filters on a field the maintainer writes, and so
measures the maintainer instead of the subject.

**Case.** An audit of "excessive `E`" filtered by the **record's own
title** rather than the book text; the title is a signature, not data.
It therefore missed both verdicts already proven wrong. Same maintainer
nearly destroyed 124 records with a check that searched the book where
it should have searched the registry.

> Filter on the book's text. The record's title is a signature, not
> data.

### 9. A source reproducible only in the container that wrote it

**Symptom.** Evidence cites a document nobody else can obtain or
identify. The record looks checkable and is not.

**Measure.** `cache.py --vidtvornist`: is the source's URL or filename
in the committed manifest, with a sha256.

**Case.** 587 of 1025 `A`/`B` records. Not fraud — the cache is
deliberately not committed (the datasheets are copyright, and a book
resting on "the source is named honestly" cannot republish them). The
manifest is the bridge; it simply had not been kept. Fetching the
reachable ones and merging the other maintainer's manifest took
reproducibility 42 % → 71 %.

**Held by.** `cache.py --vidtvornist`, `make vidtvornist`.

### 10. Silent substitution of a document

**Symptom.** The cache replaces the document underneath an evidence
record that was already written. The evidence keeps verifying —
against a different file.

**Case.** `cache.py` keyed the manifest by the URL's last path segment.
`gpio.rst`, `i2c.rst`, `README.md`, `adc_channel.h` each exist in a
dozen ESP-IDF directories. Downloading 116 sources destroyed **19
manifest rows and their cached files**, silently.

Found only because reproducibility went *down* after adding entries.

**Held by.** Filenames now carry eight characters of the URL hash; a
write under a different URL refuses instead of overwriting.

### 11. Silent data loss

**Symptom.** Records disappear during a bulk operation and nothing
says so.

**Case.** Re-landing a wave overwrote its predecessor: 335 evidence
records became 324, recovered only by `git`. A measurement of class `E`
lost 40 units of 160 to malformed YAML — and lost them **not at
random**: the two assistants with the highest finding rate were the
ones whose files failed.

> Silent data loss is almost never random. It moves exactly the number
> being measured.

**And a third case, from the tool built to prevent the other two.**
`entry_points.py` restores the tree after each entry point so that a
tool ignoring an unknown flag cannot leave the book rewritten. It has
now destroyed uncommitted work **three times, in three different
shapes**:

    version 1   `git checkout -- .`             ate work twice
    version 2   baseline of dirty files taken
                ONCE, at the start of the run   ate a document mid-run
    version 3   baseline retaken before each
                point                           only that point's writes

Version 2 was written specifically to fix version 1 and it is correct
for tools and wrong for people. A capture takes minutes; a maintainer
editing a document during it finds the edit gone, because the file was
clean when the run began and the harness therefore filed the
maintainer's writing under "leftovers from a tool". That is how the two
paragraphs above this one were lost while being written.

> A guard written against the way you were burned last time protects
> against exactly that. The next fire comes in through the shape you did
> not write down.

The restore also now **names every file it reverts**. A silent revert is
indistinguishable from a tool that wrote nothing, and those are the two
cases the harness exists to tell apart.

**And a fourth, an hour after the third: structured data edited as
text.** Three evidence files needed one line of a quote replaced. The
replacement was done by string substitution on the file. A quote is a
**multi-line YAML scalar**; substituting its first physical line left
the second dangling, the block stopped parsing, and the registry went
from 1366 records to **1361** — five records gone, silently.

Nothing caught it. `schema.py` validates what parses, so a file that
does not parse contributes zero violations and zero records, and both
numbers look like success. It was noticed only because the record count
was printed immediately after the edit and read.

    text substitution   1366 → 1361, no gate fired
    parse → modify the field → dump   1366 → 1366, verified field
                                      by field against HEAD

> Never edit structured data as text. Parse it, change the value, write
> it back — and diff the **parsed** structures, not the file, so
> reformatting cannot hide a content change.

**Held by.** `snapshot.py --zvirty` before and after every bulk change —
which exists, and which the author of this case did not run;
`entry_points.py` re-reads its baseline per point and prints each
revert. The record count printed by any tool that loads the registry is
the cheapest tripwire there is, and it works only if someone looks at
it.

### 12. An inventory made from filenames

**Symptom.** Files are classified — kept, deleted, moved — without
being opened.

**Case.** A migration plan ordered "spent work orders deleted"; two of
them were a generated report and the specimen work order that is the
evidence for kind 13's measurement. The other maintainer's audit listed
ten files as misplaced letters; one is generated by `measure_f.py`.

Both of us, within a day, from the same shortcut.

> An inventory made from file names is a guess wearing a table's
> clothes.

### 13. A fabricated source

**Symptom.** An assistant cites a document that does not exist, or
cites the project's own repository as an external authority.

**Measure.** Self-citations per batch of returned evidence.

**Case.** 2 of 120 when the work order's gates section was dropped; **0
of 85** when it was restored. What worked was not the prohibition — it
was **explaining why the gate exists**, so the assistant could see its
own constraints as reasonable rather than arbitrary.

**Held by.** `layer3.py` fails on a fabricated source; the work-order
template keeps the gates section.

### 14. A heading mistaken for coverage

**Symptom.** A field or block present on 100 % of records is read as
100 % done.

**Case.** Every card carries an **Evidence** block — with a class-`F`
placeholder when there is no evidence. "8331 of 8331 have Evidence" is
true and means nothing. Real coverage is 30 %.

The same shape fooled both maintainers twice in one week.

**Held by.** `SCHEMA.md` states it beside the card format; `status`
reports coverage separately.

### 15. Closing a violation by changing the class

**Symptom.** A record breaks a rule, and the fix moves it to a class
where that rule does not apply — instead of supplying what the rule
asked for. The first check goes quiet; a different one goes red, or
nothing does.

**Case.** Six records were class `named-unreachable` with no source
named, which `schema.py` flags (class `C` exists precisely to name the
unreachable document). They were closed by changing the class to
`unchecked` — which trips the older, stricter gate in `layer3.py`: an
evidence record of class `F` asserts nothing at all, so it is not
evidence.

Both rules are right. The class was the wrong place to fix it.

**What the case actually exposed.** Reading the notes, none of the six
names a retrievable document — they say *"the source would have to be
an Espressif document"*, *"the source ought to be the module's
datasheet"*. That is not a named source, so `C` was never right either.
And `F` is not right, because the record then claims to be evidence
while asserting nothing.

> The schema has **no state for "a maintainer looked and found no
> source."** That is a real fact, worth keeping, and there is nowhere
> to put it. Both wrong classes were attempts to store it somewhere.

**Held by.** Nothing yet — the missing state is an open schema
question. The symptom is caught only because two gates disagree, which
is luck, not design.

### 16. The book smuggled into the source cache

**Symptom.** A file of the book itself sits in the cache of external
sources. Evidence then proves the book with the book — and **passes all
three layers at once**: the source is a cache file (gate satisfied), the
quote is verbatim in it (layer 3 satisfied), the pattern binds a claim
(layer 1 satisfied).

**Case.** Seven book files, byte for byte, placed by the wave of 27
August — the first in which assistants were allowed to fetch sources
themselves. One "downloaded" a chapter of the book. Records relying on
them: **zero**; the mine never went off.

Found by M2. The first check compared file contents in the cache
directory — and after the files were deleted it reported clean while
**four manifest rows still named the book as a source**. The manifest is
the only part of the cache that reaches git and third parties; the files
never travel at all.

> Kind 3 in its own right: the counter was measuring the artefact that
> does not travel, and staying silent about the one that does.

**Held by.** `tools/cache_vs_book.py` — by sha256 of contents (a copy
under another name is still found) **and** by the manifest's URLs.

### 17. A machine pointer that is worse than prose

**Symptom.** A source named only in prose is upgraded to a filename or
URL by **name similarity**. The record now looks machine-checkable and
points at the wrong document.

**Case.** Aliases resolved 172 of 201 prose sources. Line-by-line
verification: 41 matched fully, 61 partly, **73 by no line at all** —
SSD1306 pointed at a driver instead of the datasheet; "18650 capacity"
at `ncr18650b` while the quote came from `samsung25r`; MAX6675 at the
datasheet while the quote came from an Adafruit library. 137 were rolled
back.

> A false machine pointer is worse than prose. Prose says honestly "a
> human will work it out"; a pointer promises verifiability and lies.

**Held by.** The rule M2 drew from it: **a source may be resolved only
by checking that the quote is actually there, never by name
similarity.** Same law as naming the document, approached from the
other end.

### 18. Removing the effect and leaving the cause

**Symptom.** A defect is cleaned out of the place it was noticed, while
the record that recreates it stays. The next routine run restores it.

**Case.** Kind 16's seven book files were deleted from the cache and the
matter considered closed. **The next download brought four of them
back** — because eight manifest rows still named the book as a source,
and the manifest is what downloads are driven from. Found only because
the same person happened to download again the next day.

Both maintainers then wrote the manifest check independently, within an
hour, and each missed what the other saw: one keyed on the repository's
name (catches an address outside `raw.githubusercontent`), the other on
the path `…/manual/…` (catches a fork under a different owner). Neither
alone covers both.

> Removing the effect and leaving the cause is not a fix, it is a
> postponement — and the postponement is invisible, because the place
> you looked is genuinely clean.

**Held by.** `tools/cache_vs_book.py`, both conditions, in `make check`.

### 19. Two copies of the same datum, one of them repaired

**Symptom.** A field exists twice during a migration — old name and new
name side by side. A fix is applied to one copy. The other keeps the
defect, silently, until the day it becomes the one that is read.

**Case.** Measured across all **9202 field pairs** while converting
tools to the English names: **29 had diverged.** Fifteen were `zbih` /
`match` in the other maintainer's leak repairs — they had narrowed the
Ukrainian field, and the English one still carried the **old wide
pattern**. The generator reads the Ukrainian field, so the repair was in
effect; contracting to English names would have reverted fifteen leaks
without a word.

A second divergence hid in the class itself: six records read
`klas: F` with `status: unverified` — a word that **does not exist in
the schema** (`unchecked` does). The schema checker asked "does this
class have its required fields" and looked the class up in a table;
an unknown class returned an empty requirement list and the record
passed as flawless.

> Two copies of a datum are not double safety. They are double surface.
> The one that is read is right by accident, and the accident changes
> the day the other becomes authoritative.

**Held by.** `schema.py` now validates the status vocabulary itself,
not just the fields a status demands (demonstrated on a fabricated
state). Divergence between copies is checked by comparing all pairs;
the contraction step removes the second copy for good.

**A second substrate, same shape.** The source cache's manifest — the
only part of the cache that is in git — records one row per file:
name, sha256, URL. A change to the filename rule **appended** a row
instead of replacing one, so **78 URLs are recorded twice**, under the
old name and the new. 357 rows for 276 URLs.

The rows are sorted by filename, so the hash-prefixed name sorts first
— and in any given container that is precisely the name the file is
*not* under. Reading "the first row for this URL" would have been
worse than not reading the manifest at all.

> The right question is not *which name is recorded* but *which name
> the file is under here*. An index with two entries answers the first
> question confidently and the second one wrongly.

### 20. One unit carrying two claims

**Symptom.** A unit states two things. Evidence settles one. The unit's
class takes the **stronger half**, and nothing shows that the weaker
half is unsourced — so the unit reads as fully verified.

**Case.** Found by the other maintainer while closing six records:

    "Modern routers often share one name across both bands"  ← no source
    "ESP32 cannot see 5 GHz"                                 ← datasheet, p.1

    "Lithium will not charge below 0 °C"   ← specification, verbatim
    "and loses capacity in the cold"       ← a GRAPH in the Samsung 25R
                                             sheet, and a graph is not a
                                             substring of text

> This is the mirror of the split defect. There, splitting **cut** a
> thought in half and produced a false contradiction. Here, splitting
> **fused** two thoughts and produces a false verification. The flaw is
> the same one — the boundary of a unit — and no check asks about it.

**Held by.** Nothing. The maintainer wrote it out in the note instead of
hiding it in the class, which is the only defence available today.

### 21. A boundary scan that does not know its own format

**Symptom.** A tool walks text to find where a block ends, using a rule
from one syntax while standing inside another.

**Case.** The card's context stopped at the first blank line — correct
for a paragraph, wrong inside a fenced code block, where a blank line is
content. A panic dump was shown as **one line of eight**, while the card
claimed to be giving surroundings.

**58 cards, all of kind `kod`.** Invisible to every check we had, and
found by the other maintainer's `layer1.py` asking a question neither of
us had asked: *does the context contain its own claim?*

> Kind 5 inside its own antidote: the block built to show a whole
> thought was showing half of one.

**Held by.** `layer1.py` — and the boundary scan is now fence-aware.

### 22. The same number, meaning something else

**Symptom.** A check keeps returning the value it returned yesterday.
Nothing looks wrong, because nothing moved. What moved is what the
number is a count **of**.

**Case.** Proposed by the other maintainer with a reproducible example.
`layer3.py` decided whether a record was checkable with
`maye_klas = "klas" in z` — a test for the presence of an **old field
name**. Under the contraction dress rehearsal:

    before   verified 508 · not found 104 · nothing to check 672
    after    verified 508 · not found 104 · nothing to check 695

> The headline did not move by one. "Verified 508" before, "verified
> 508" after — while twenty-three records migrated from *is checked* to
> *there is nothing to check*.

This is kind 3 with the volume turned down. Kind 3 says a check returns
zero and the zero means nothing; this says a check returns **the same
number**, and the sameness is the disguise. A reviewer who looked at the
headline would have been right about exactly what they looked at.

**Why no pattern finds it.** `"klas" in z` reads no value and raises
nothing. It is correct code for as long as the field exists — and every
baseline run is made on data where the field still exists.

**Held by.** Nothing automatic, and probably nothing can be. It is held
by a **procedure**: run the contraction clean on a copy, diff every
tool's output, revert. Adopted as mandatory step 1-bis before the
migration's contraction. Everything below was found by that procedure
and by nothing else.

### 23. A replacement that renamed both sides of the fallback

**Symptom.** A migration replaces an old name with a new one across a
file. Somewhere the old name appears as the **fallback** of the new one.
Both halves are replaced. The expression still parses, still runs, still
looks like a fallback — and no longer is one.

**Case.** Converting tools to English field names produced:

    v = z.get("match") or z.get("match")

The intent was `z.get("match") or z.get("zbih")`. A record carrying only
the Ukrainian name was silently skipped. `leak.py`'s own self-check
**caught this** — it reported *expected a leak, got clean* — and said so
into an empty room, because `make check` ran `techa` without
`--samoperevirka`. Neither self-check in the project was called by
anything: see kind 24.

The same replacement, in the same commit, also produced three other
shapes worth naming separately because each needs a different question:

- **A reader renamed away from its writer.** `factcheck.py blocked`
  created a local dict `{"shukaty": set()}` and then read
  `g["look_for"]` three times. The three reads were replaced, the one
  literal that creates the key was not. `blocked` raised `KeyError`
  from that commit until it was run again — and it is in no baseline
  and in no `make check` target, so nothing ran it.
- **A writer renamed away from its reader.** Four tools wrote candidate
  files with `nazva`/`dzherelo`/`cytata` and then keyed results by
  `k["title"]`.
- **A schema renamed that was never migrating.** The findings returned
  by `citaty.perevirka` use `nazva` and always will; three tools were
  converted to read `n.get("title")` from them, which is `None` for
  every finding. Measured: every candidate came back named `?`, so the
  third-layer state map for all four tools collapsed into one bucket.

**Count.** Fourteen reads, then nine more sites of these four shapes.
The first pass of the conversion had searched for `z.get("nazva")` with
double quotes; the code also contained `z.get('nazva')`.

> A replacement that searches for a string finds exactly the spelling
> of that string. The rest stays — and looks converted.

**Held by.** Kind 22's procedure, plus a rule this cost us: **during a
name migration, run every entry point, not the ones in `make check`.**
`blocked`, `cherga`, `vzirets` and four helper tools are in no gate, and
that is where all of this survived.

### 24. A check that is red and is not called

**Symptom.** A check exists, works, and disagrees with reality — and no
target, gate or habit invokes it. Its redness is indistinguishable from
green.

**Case.** Two, within a day of each other.

The other maintainer's `intake.py` had **21 blocking findings** and no
Makefile target: `make check` was green because the check with the
findings simply was not called. Then `leak.py --samoperevirka` sat red
for the length of kind 23 above, saying *expected a leak, got clean* to
nobody. Both self-checks in the project — `skhema` and `techa` — were
behind flags that nothing ran.

> This is worse than a missing check, and it costs more than kind 3. A
> missing check is an admitted gap. A check nobody calls is an
> **asserted** guarantee, and the assertion is in the contributor's
> head, where no diff can reach it.

**Held by.** `make samoperevirky`, now part of `make check`: every
self-check runs on its deliberately broken input on every gate run. The
project rule *a check that has never fired is no different from a check
that does not exist* now has its corollary — **a check that fires where
nothing listens is no different either.**

`make intake` exists as a target but is deliberately **not** in `check`
while its 21 findings are worked through; that is a stated exception
with a date, not an omission.

**The shape recurs one level up, in the shell, and it recurred twice.**
Both times the check was called, printed its findings, exited non-zero —
and the commit went out anyway, because the command line joined the
gate to the commit with `;` instead of `&&`:

    make check ; git commit ; git push        conflict markers shipped
    correspondence.py ; git commit ; push     a malformed letter shipped

Nothing was missing and nothing was unwired. The gate ran, the output
was on screen, and the separator discarded the verdict. Two days apart,
same hand.

> A gate's exit code is only a gate if something branches on it. `;`
> turns a check into a printout, and a printout scrolls.

**Held by.** Nothing automatic here either — a shell line is not
reviewable by CI. The habit that does hold: **never put a commit in the
same command as its gate.** Run the gate, read the number, then commit
as a separate act.

### 25. Two states of the world under one word

**Symptom.** A report has one bucket for two situations that call for
opposite actions. Because the count is right, nothing looks wrong.

**Case.** Layer 3 reported **162 records** as *source not in cache*.
That phrase covered two entirely different worlds:

- the source is genuinely unreachable — an organisation-level `403`,
  nothing to be done from this container, correctly a work order;
- the file is sitting right there, under the previous generation of the
  filename rule, and the tool derived the new name and did not find it.

**108 of the 162 were the second.** Their evidence was unverifiable for
as long as the two shared a word, and the queue built from that bucket
sent people to fetch documents that were already on disk.

Reading the name from the manifest instead of deriving it moved 108
records out of the bucket in one change: verified 407 → 538, not in
cache 162 → 54.

> A bucket is a claim about the world. Two worlds in one bucket is a
> false claim that no counter can contradict, because the counter is
> right.

**Held by.** `layer3.py` already separates *file present but
unreadable*, *stub served instead of a document*, and *file absent* —
each its own state, for exactly this reason. The filename case is now
closed at the source: the manifest is authoritative for the name, so
absence means absence. What remains unheld is the general principle;
nothing detects a newly-merged pair of states except reading the
report and asking what each number is a count of.

### 26. A rename rewrote the rule whose subject was the old name

**Symptom.** A rename updates every reference to the old name — including
a rule whose entire job was to be *about* the old name. The reference was
correct before and is correct after; the rule is destroyed by being
updated.

**Case.** `dzherela-kesh/` became `source-cache/`. `.gitignore` held two
entries: `dzherela-kesh/*` (the live rule) and `dzherela-kesh/` (a
belt-and-braces rule for the same path). The rename rewrote both — the
second into `dzherela-cache/`, a directory that has never existed.

In the container that did the rename, nothing sat at the old path, so
nothing happened. In the **other maintainer's** container the old
directory was still there with its downloaded documents, and the merge
handed them a tree where **236 third-party documents** were no longer
ignored. They were staged before anyone noticed.

> An ignore rule for a path is not a reference to that path. It is a
> statement about anyone who still has one. Renaming it removes the
> protection exactly where it was still needed — and never where the
> rename was done, so the author cannot see it.

The same shape applies to any rule keyed on an old name: a redirect, a
deprecation warning, a migration guard, a compatibility shim.

**Held by.** `tools/docs.py`, which asks `git ls-files` on the cache
directories and requires that nothing but the manifest is tracked.

The check first proposed here was different, and it was wrong. It read:
*no `.gitignore` entry may name a path that does not exist and never
has*. Run against the tree before it was written, it produced seven
findings, six of them legitimate — `.DS_Store`, `Thumbs.db`,
`.linkcheck-*`, `.budgets-*`, `__pycache__/`, a local editor settings
file — and the seventh was the restored rule protecting the other
maintainer's container. The check proposed as the antidote to this very
incident would have ordered the deletion of the protection that stopped
it.

The reason is in the definition: an ignore rule speaks about what may
**not be here yet**. `.DS_Store` appears tomorrow; the old cache
directory exists in one container and not the other. Absence of the path
is the rule's normal state, not evidence of a defect. What distinguishes
the broken entry is that it was *born from a rename* and never existed
anywhere — and that is not mechanically visible.

> Ask the consequence, not the rule. A rule can be rewritten into
> nonsense and still parse; a tracked file cannot lie.

---

### 27. A normaliser that swallows the start of the quote

**Symptom.** A comparison is loosened to forgive a difference that does
not change meaning, and it rejects records that passed before.

**Case.** Wave w1 (`factcheck/history/WAVE-W1.md`) showed that most rejected
quotes were correct passages with RST markup removed. The obvious
remedy — strip inline markup from both sides before comparing — was
measured against the whole registry first:

    strict (as it stands)     verified 538   not found 72
    tolerant to RST markup    verified 531   not found 79

    recovered  3     broken  10

The mechanism is `T-05-064`. The source reads
`` :cpp:func:`gpio_config` is an all-in-one API … ``; our quote begins
at the backtick, `` `gpio_config` is an all-in-one API … ``. Today that
is a plain substring. A normaliser that rewrites the role
`` :cpp:func:`…` `` as a unit changes the source and not the quote —
the quote contains the role's tail, not the role — so the two sides
normalise to different strings and the containment is gone.

> `a ⊂ b` does not imply `norm(a) ⊂ norm(b)`. Any normaliser used
> underneath a substring test must be substring-preserving, and one that
> can consume the point where a quote begins is not.

This generalises past markup: case folding, quote unification and
whitespace collapse are safe because they are per-character; anything
that rewrites a *construct* is not.

**Held by.** Nothing automatic, and nothing needs to be: the discipline
is to measure a proposed loosening against the existing corpus before
writing it. That discipline caught kind 26's candidate check and this
one, on consecutive days.

---

### 27-bis. A test stricter than the gate it stands in for

**Symptom.** Work is tested with a comparison built for the occasion,
the comparison rejects it, and the work was correct. Unlike kind 27 this
one never reaches the tree: it destroys good work *before* the commit,
and it looks careful doing it.

**Case.** M2, verifying six pinout quotes before landing them, tested
them with `pdftotext -layout`. **Four of six came back "not a
substring"** and they were about to rewrite them. The gate uses
`layer3.tekst_dzherela`, which extracts a table differently — a newline
between cells, collapsed later by the gate's own normalisation:

    the ad-hoc test saw   'GPIO4, ADC2_CH0'           → not found
    the gate holds        'GPIO4,⏎ADC2_CH0,⏎RT'       → found, after the
                                                        gate collapses
                                                        whitespace

All six were correct. A stricter test is not a safer test: it rejects
true things, and its rigour is what makes the rejection convincing.

**Why it sits beside 27, not inside it.** Kind 27 is a comparison made
**looser** than the gate — it recovered 3 records and broke 10. This is
a comparison made **stricter** than the gate — it would have destroyed 4
correct records. Opposite directions, one cause:

> The comparison used to judge evidence must be **the same comparison
> that will judge it**. Any other measures your own tooling.

The two together give the working rule: **never hand-roll the
comparison.** Import the gate's extractor and the gate's normalisation,
or run the gate.

**Held by.** Nothing automatic — an ad-hoc test in a scratch directory
is outside every gate by definition. What holds is that `layer3` exposes
`tekst_dzherela`, `plaskyy` and `uryvky` as importable functions, so
using the real ones is cheaper than writing new ones.

---

### 28. Several checks around one number, none of them asking about it

**Symptom.** A value is guarded by two or three checks, all green, and
the value is wrong — because each check asks a question *adjacent* to
the one that matters.

**Case.** Cards for table cells carry a line number and a verbatim block
quoting the book at that line. An off-by-N in the cell locator meant the
block quoted a **neighbouring** row, very often the `|---|---|`
separator itself. **1360 cards of 1383** showed the worker the wrong
line.

Three checks stood around that number, and all three passed:

    layer 1   compares the verbatim block to a WINDOW around the number
              — a block off by one row is inside the window
    stale     compares registry to book BY TEXT HASH
              — the number does not enter the comparison
    schema    requires the block to be a table row
              — a separator is a table row

> Three checks around one number, and none of them asked *"is **this**
> at **this** number"*. Coverage counted three; the answer was zero.

The question turned out to be one line of code. It was asked only
because an unrelated measurement came back surprising — not because
anything looked wrong.

**And the honest number went up.** Layer 1's "line shifted" count rose
from 51 to 67 once the blocks were correct, because a wrong block used
to land inside the window and keep the check quiet. Cross-checked: of 40
mismatches, 33 were what layer 1 now reports and **0** were false
alarms. See kind 22 for the general form — the same number meaning
something else.

**Held by.** A direct check: the verbatim block must equal the book line
at the number the card names. Nothing weaker substitutes for it, and
nothing weaker did.

**And the fix uncovered a second bug underneath, which is the normal
case.** M2 rebuilt the comparison independently, confirmed 1343, and
found the residual 42 were not off-by-one at all — offsets of −62, in
six files. The locator resolves a cell by searching the book for its
row-label and its value and taking the **first** match; `| I²C |` begins
a row in *two* tables of chapter 04, and a value like `2` matches
anything:

    p54    | I²C | дві лінії, багато пристроїв, невисока швидкість | 35 |
    p116   | I²C | 2 | 2 | 2 | **1** | 1 + 1 LP | 2 |

That is **kind 10** — keying by a value that is not unique — in a
different subsystem, four months later, found by the other maintainer.
Neither of us thought of kind 10 while writing a row locator. The
catalogue only pays if it is read at the moment of writing, and it was
not.

The repair gives each half its own job: **content identifies, the number
disambiguates.** Take the match *nearest* the recorded line rather than
the first. Measured over all 1417 cells: first match 1327 correct,
nearest match **1401**.

---

### 29. A report claiming a change the tree does not contain

**Symptom.** A letter, status line or commit message states that
something was fixed. It was not. Everything downstream is now reasoning
from a false premise, and the author is the last person who will check.

**Case.** Two letters, an hour apart, both said kind 26's entry had been
corrected. The correction had been written in the letter and never in
`DEFECTS.md`. It was found a day later, by reading the file for an
unrelated reason.

This is the same defect the whole technology exists to catch in helpers
— an assertion with no artefact behind it — committed by the maintainer,
where nobody was checking. A helper's claim goes through layer 3. A
maintainer's claim about their own tree goes through nothing.

> The gate we point at the helper is not pointed at us, and we make the
> same class of mistake.

**Held by.** Nothing automatic, and the general case cannot be: no
checker reads a letter's prose against a diff. What is cheap and does
hold: **make the change first, then describe it** — a report written
from `git show` cannot claim what is not there. Where a letter must
promise future work, say "taking this next", never "done".

---

### What has no automatic check

Stated plainly, because a catalogue that hides its gaps is kind 3.

- **Kind 6** — nothing detects a verdict wearing a state's clothes.
- **Kind 8** — nothing detects a check filtering on its own author's
  field. Found by reading, twice.
- **Kind 12** — nothing can tell whether a file was opened before it
  was classified.
- **Kind 20** — nothing detects a unit that carries two claims.
- **Kind 15** — caught only because two gates happened to disagree.
  The missing state it exposed is still missing.
- **Layer 2 entirely** — whether a quote actually *supports* a claim is
  human work and always will be.

---

# Part IV — The work order specification

Every work order handed to a helper is composed from the blocks below.
No generator writes its own copy of these rules.

**Why this file exists.** The task was being synthesised from scratch by
each generator: seven work-order headers, each restating the same rules
in its own words. Measured before this file existed — eight rules across
seven headers:

    stated in all seven                        1  (quote verbatim)
    stated in three or fewer                   5
    the stub-page trap                         2 of 7
    the worker's place in the whole flow       3 of 7
    header length                       1424 … 5867 characters

So a wave's results depended on which generator produced it, and nobody
could say how. When a defect class appeared or vanished between waves, we
could not tell whether the technology changed or the wording did.

> A task that is rewritten for every run is not a constant. It is an
> untracked variable sitting in the middle of every measurement we take.

**What this buys.** The composed header carries a version stamp. Every
helper answer is therefore attributable to an exact task text, and two
waves are comparable — or knowably not. Change a block, the version
changes, and the next wave's numbers can be set beside the last one's.

**How to change it.** Edit a block, run `tools/task_spec.py --version`,
and record the new version in the wave's notes. Never edit a block and a
generator in the same commit: the point is that the task is one thing
that moves on its own.

---

### [ORIENTATION] Where you are in this

This is a printed field handbook. Its reader has no network and no time
to check anything. Our job is to put every factual claim in it beside an
external document that supports it — and to record where we looked.

Your answer does not go into the book. It goes through three layers:

1. **Mechanical.** An address pointing at the handbook itself is
   rejected. A verdict with no source is rejected as "did not look".
2. **Literal.** Every `quote` is searched for **as a substring** in the
   document you named — we fetch it again and check. Spaces and quote
   marks do not count; words, numbers and capitals do.
3. **Human.** A maintainer reads the extract and judges whether it
   actually supports the claim.

Layer 2 is not a formality. In one earlier wave, of **528** claimed
confirmations only **235** survived it. The other 293 died as
paraphrase, as fragments glued across an ellipsis, or as a correct fact
with the wrong file's address.

### [HONEST-MISS] "I looked and did not find it" is a complete answer

It is not a failure and not a lesser result. It records where we have
already looked, and those records are what let us print a sentence at
all.

A quote from an almost-right source is worse than no quote. Invented
support does not go unnoticed — layer 2 discards it and the unit returns
to the queue — so guessing is cheaper than reading only inside your own
answer. Past that boundary it costs everyone, and you most: your work
disappears entirely.

### [VERBATIM] Copy, do not retell

Everything in `quote` is checked as a substring of the document. A
retelling does not pass. Neither does a line you assembled by hand from
a table, nor two sentences joined across an ellipsis.

**Knowing the answer is not grounds for writing a quote.** If the fact is
familiar but you cannot see the line in the document, that is
`not_found`.

**Paste the line with its markup. Do not clean it up.** This is the one
that costs most, because it does not feel like an error. The document
says

    Print registers and reboot (``CONFIG_ESP_SYSTEM_PANIC_PRINT_REBOOT``) — default option

and the tidy version — `Print registers and reboot — default option` —
is the same fact, reads better, and **fails**. So does dropping a
`:doc:` role, a trailing underscore on a link, or the brackets around an
option name. Measured over 200 tickets: of the confirmations that
failed, 13 of 14 had found the right passage and lost it in the copying.

Copy the characters that are there — backticks, colons, brackets,
underscores and all. If two useful sentences are not adjacent, send two
entries or one entry and say so; do not join them.

### [NETWORK] What is reachable from here

Only `raw.githubusercontent.com`, via `curl`. Everything else answers
`403` — this is an organisation-level policy, not your doing and not
ours. Chip datasheets are not on GitHub, and that is nobody's fault.

**Do not repeat a request that returned 403.**

### [STUB] A 200 that is not a document

Some `espressif.com` addresses return an **HTML placeholder of about
15 500 bytes with status 200**. The request "succeeds" and there is no
document. If what came back does not look like the document you asked
for, the verdict is `unreachable`.

### [NO-SELF-REFERENCE] The handbook cannot be its own source

An address inside this repository, or a chapter of the handbook cited as
the source for a claim in the handbook, is rejected mechanically. If a
claim is supported only by another part of the book, say so plainly —
there is a class for it, and it is not a failure.

### [VERDICTS-EXTERNAL] The verdicts for finding an external source

| Verdict | When |
|---|---|
| `confirmed` | address plus a **verbatim** quote from the document |
| `not_found` | the document exists, the passage is not in it — say what you read |
| `unreachable` | the document does not come down from here (403, 404, stub) |
| `advice` | you did not get the document, but can name where it would be |
| `disputes` | the source **contradicts** the handbook — the most valuable answer there is |

### [VERDICTS-VERDICT-TEST] The verdicts for testing an existing verdict

Used when the unit already carries a class and the question is whether
that class is right.

| Verdict | When |
|---|---|
| `confirmed` | the existing class is correct |
| `disputes` | the source contradicts the handbook |
| `truly_none` | there really is no external referent: this is the author's position |
| `not_found` | you could not tell — say what you read |

### [ABSENCE] Proving something by what a document does not say

Sometimes the proof is a silence: `SOC_BT_SUPPORTED` does not appear in
`esp32s2/soc_caps.h`, and that is what shows the S2 has no Bluetooth.

This is a real answer with its own verdict, `absent_from_source`. It
needs the document, the exact string that is **missing**, and — where one
exists — a `control`: a document of the same kind where that string **is**
present. Silence proves something only where a comparable document
speaks.

It is **not** `not_found`. `not_found` says you could not establish the
claim; this says you established it, and the document's silence is how.

### [CARD-PLACE] Printed on each card, so the reason is visible where the work is

*Where this card sits in the job.* The book has been cut into claims;
each one carries a state. This is one of the claims nobody has reached
yet. Your answer becomes its state — and after you it is checked by
machine: the quote is searched for **as a substring** in the document
you named. That is why a retelling dies, and why an honest "did not
find it" survives and saves the next person the same search.

### [FORMAT] How to answer

```yaml
- unit: T-42-023
  verdict: confirmed
  source: https://raw.githubusercontent.com/espressif/esp-idf/master/...
  quote: |
    the verbatim line from the document
  comment: one sentence, optional
```

One entry per unit. Do not reorder or renumber the units. If you have
nothing for a unit, still write an entry with the honest verdict — a
missing entry is indistinguishable from work not done.

**YAML:** if a value contains `: ` or starts with a quote mark, wrap the
whole value in single quotes. Otherwise the file will not parse and the
whole batch is lost, not just that entry.

---

# Part V — The log of helper waves

This document used to live in a temporary directory, which is to say it
vanished with the session. That was wrong: a helper's work order is as much
a part of the technology as the registry and `layer3.py`, and yesterday's
order explains yesterday's waste.

---

### Why a cheap model is possible at all

Not because it is cheaper. Because **layer 3 removes the requirement on its
strength** (`METHOD.md` §3).

A weak model fails predictably: it paraphrases instead of quoting, stitches
sentences together, reorders words, invents the plausible. Every one of
those failures is caught by a script, mechanically and completely. So the
gathering can go to the cheapest model, and expensive attention can stay
with layer 2.

The first wave's numbers on Haiku: **143 records, 94 quotes passed layer 3
verbatim.** The waste was exactly what had been predicted, and no instance
of it required understanding the subject to spot.

---

### The line a cheap model must not be sent past

**Haiku is safe where the document is already in the cache and the job
reduces to "find it and copy it out". It is dangerous where the document
may not exist.**

Having failed to find a document, it does not write `named-unreachable` —
it **invents a plausible source name**: "the properties of CMOS logic", "a
fundamental rule of electronics". M2 rejected an entire evidence file over
this.

So the order **names a specific file**, not a topic. "Check this in
`esp32c3.inc`" will do. "Find out whether GPIO2 on the C3 is a strapping
pin" will not.

A refinement bought expensively: **the defect is not a property of cheap
models, it is a property of haste.** The worst instance of it in this
project is my own, ten passes before any pool existed. Which is why the
gate against it is mechanical, and not "do not use a cheap model".

---

### What a helper does and does not do

**Does:** downloads the primary source, reads it **in full** against a list
of claims, returns YAML with verbatim quotes.

**Does not:** write patterns, assign statuses, or change anything in the
repository.

The reason is specific: over this project a wide pattern has **three times**
silently marked as "checked" something it never checked. That failure is
invisible, and only an audit in context — one that remembers all three
cases — catches it.

---

### Six prohibitions on what counts as a source

The first three were bought by the sweep of `no-external-signal`; the
fourth and fifth are M2's finding from their own sweep the same evening;
the sixth comes from wave 8.

> There are six prohibitions here, and the heading said "five" until
> somebody measured. A document that disagrees with itself about a number
> it prints itself is kind 3 of our own catalogue in its cheapest form.

1. **A paraphrase is not a quote.** Everything in the `quote` field is
   checked as a substring of the document itself. A paraphrase does not
   pass.
2. **Memory is not a document.** A line typed from memory kills the record
   even when the fact is right: `Static struct` instead of `static struct` —
   a real case, the real Linux kernel, rejected.
3. **An unreachable document is not an obtained document.** If it did not
   download, that is `unreachable`, not `confirmed`.
4. **The book is not a source for itself.** If the only thing found is
   another chapter of this same book, that is `truly_none`. Otherwise the
   verdict we are checking certifies itself — precisely the defect the
   sweep was mounted against.
5. **"Physics confirms", "logic confirms", "standard practice" are not a
   source.** If you cannot give a document address and a line from it, that
   is `advice` or `truly_none`.
6. **Knowing the answer is not grounds for writing a quote.** If the fact
   is known but the line is not visible in the document, that is `advice`
   or `not_found`.

#### Never name the expected answer

The most expensive lesson of two waves, and both failed **for the same
reason in opposite directions**.

**Wave one.** The order listed `pidtverdzheno` first. Of 247 answers, 185
came back "confirmed" citing the book itself.

**Wave two.** I rewrote the order and wrote in black and white: "**the
expected answer here is `ne_znayshov`**". Of 190 answers, **eight** named a
document. The rest were solid `ne_znayshov` with no attempt to open
anything.

Two helpers cited **my own sentence** as their justification:

> "This is the expected and correct result, as documented in the NARYAD
> file: *Очікувана відповідь тут — `ne_znayshov`*."

> **Law.** An order that names the expected answer gets exactly that answer
> — **with no work done**. It does not matter which answer it is.

This is not the same law as the one below, but its other half. The lower
one saves the **registry**: when the cheapest answer asserts nothing,
carelessness does not manufacture untruth. But it does not save the
**measurement**: a helper who opened no document and wrote "not found"
twenty-five times gives a flawlessly harmless and flawlessly wrong
statistical result.

#### What works instead

Do not name the distribution at all. Instead of "which answer we expect" —
**what each answer must produce**:

| Verdict | Mandatory evidence of work |
|---|---|
| `confirmed` | document address + a verbatim line from it |
| `disputes` | document address + a verbatim line that contradicts |
| `not_found` | **the address of the document that was looked at** |
| `unreachable` | the address that was tried, and the response code |

> The verdicts themselves are not here. The list the executor sees lives in
> `factcheck/TASK-SPEC.md`, blocks `[VERDICTS-*]`, and every order is
> assembled from there; the gate `tools/intake_f.py` checks that same list,
> and `tools/docs.py` compares the two. This table shows **what to demand
> of a verdict**, not which set of them exists.
>
> Until 2026-08-28 the verdicts were written in transliterated Ukrainian
> (`pidtverdzheno`, `ne_znayshov`, `sperechayetsya`, `nedosyazhne`). The log
> below quotes those words where they genuinely stood in the order of that
> day; the gate still accepts them and translates them to the current ones.

The key row is the third. As long as `not_found` can be written without
naming anything, it costs zero and will be the default answer. The moment
it requires an address, it costs the same as the rest and stops being the
path of least resistance.

`tools/measure_f.py` counts `not_found` with no address as a separate
category, "did not look": such a record enters neither the numerator nor
the denominator of the measure.

#### Test the order on one helper before releasing ten

Two waves of 250 units were spent on what is visible from two batches. An
order is as much a tool as a script, and `Р-ЗВІРКА` applies to it: try it
first, then use it.

---

### The log of attempts: what was tried, how it failed, what cured it

**This is the main section of this file.** The laws above are conclusions;
here is the material they were made from. Before composing a new order,
this is the table to read: each row is a wave already spent, and there is
no need to repeat it.

| # | The order's design | What came out | Cause | What cured it |
|---|---|---|---|---|
| 1 | "confirm or refute", the book's text inside the order | **185 of 247** named the book as the source | the cheapest answer `pidtverdzheno` **asserts**, and the text was right there | the `RE_SAMA_KNYHA` gate + a rewritten order |
| 2 | the same, but stating "the expected answer is `ne_znayshov`" | a document was named by **8 of 190** | the order **named the expected answer**; two cited that sentence as justification | remove any mention of the distribution |
| 3 | `dzherelo` required **on every** verdict, distribution unnamed | 196 usable, "did not look" **zero** | — | **this is the working form** |
| 4 | batch = "one chapter of the book", "pick one document per batch" | **249 of 274** — self-references | the word "chapter" points at a book file; the cheapest document matching the description is the chapter itself | topic instead of chapter + the order names a candidate document |
| 5 | form 3 + topic + candidate document, continuous pass | 149 records, self-references **zero**, without a document **zero** | — | **the working form, confirmed a second time** |
| 10 | `unchecked` queue, **random** sample, no candidate by construction | 71 % `ne_znayshov`; 18 confirmations, **9** survived layer 3 | the sample is random, so there is nowhere to name a candidate; the helper searches blind | **nothing — this is a measurement, not a fault.** The number is the price of a missing candidate |
| 6 | the same order, but the batch topic had no candidate | the helper **refused to work** and said why | the header promised a candidate "for every batch", the generator silently omitted the line | a batch with no candidate now says plainly that there is none |

#### Wave 6: a refusal is a working outcome, not a breakdown

A helper handed an order with an unkept promise did not invent a document
and did not write "not found". It stopped and named what was missing.

This is worth learning to recognise: **a refusal costs one tool call and
looks like a broken wave by every quantitative sign.** What distinguishes
it is that the helper named a cause, and the cause held up. Before writing
a wave off to a lazy model — read what it actually said.

#### The law this wave added to two earlier cases

This is the **third** time the same defect stopped work:

| Where | What the document promised | What the code did |
|---|---|---|
| `factcheck.py vorota` | two checks | one |
| `tools/measure_f.py` | counts usable records | counted **before** its own gate |
| `tools/sweep.py` | a candidate "for every batch" | silently skipped the line |

> **A promise in the text is an invariant too.** It must either hold or be
> removed from the text. An unkept promise is worse than an absent one: an
> absent one is visible, and an unkept one is relied upon.

Two of the three were found by someone other than me: `vorota` by an
external review, `prochid` by a two-dollar helper. Both found it because
they **tried to use** the promise. Reading your own text does not do that.

#### What a continuous pass does **not** give, and how to say so aloud

35 of 58 orders are single-topic: all ten batches take one document. In
such an order the helper downloads it once and walks all 50 units through
it — 18 tool calls for 50 units, that is **three times below the honest-wave
floor** in the table further down.

This is not forgery. There are no self-references, the document is named,
it really was read. But the honesty sign does not work here either: **the
call count measures how scattered the topic is, not how diligent the work
was.** On a single-topic order it must be counted per *document*, not per
unit.

The main point is something else — what earns the right to go into the
book:

> `ne_znayshov` in a continuous pass means **"this is not in the named
> document"**, not "this is nowhere".

So the sentence we are entitled to print is not "every claim was checked"
but: **"every unit was checked against at least one relevant document, and
its address was recorded"**. The second is narrower, but it carries an
address at which a reader can check us.

Orders from № 13 require a **second** document before `ne_znayshov` may be
written, and a list of every address opened in `komentar`. That does not
lift the limitation — it only raises the floor from one document to two.

#### Wave 7: prohibiting is not enough — you have to explain

The first six waves treated the order with **prohibitions and gates**. Wave
7 showed what that does not cure.

A layer 3 digest over 1661 usable records:

| | |
|---|---|
| claimed confirmations | 528 |
| survived the verbatim check | **235** |
| died | **293** |

Examining eight at random from those that died found **no fraud at all**.
It found four kinds of conscientious work pointed the wrong way:

| Kind | What the helper did |
|---|---|
| stitched quote | joined two distant places with `…` |
| index instead of target | named `peripherals/index.rst`, quoted `ledc.rst` |
| code retold as prose | "handles SerialException errors with context" |
| reformatted content | glued JSON into one line, because it reads better |

All of these are attempts to be useful. The helper **did not know** the
quote would be downloaded a second time and searched for as a substring.
That was not in the order.

> **The order is the entire world the helper lives in.** What is not
> written in it does not exist for the helper: not layer 3, and not the
> fact that a paraphrase destroys their own work entirely.

A prohibition with no reason leaves guessing as the cheapest path. A reason
changes the arithmetic: if a paraphrase **will be discarded anyway**, an
honest "looked, did not find" becomes not a defeat but the best available
result.

So the order from wave 7 onward carries three explanations (not
prohibitions):

1. **a description of all three layers with numbers** — "of 528 claims, 235
   survived";
2. **a plain admission that `ne_znayshov` is a full result**, because it
   says where the search has already been;
3. **the `potribno` field** — the name of the document that is missing. The
   maintainer obtains it by other means and puts it in the cache; the unit
   goes into the next order with the document already in hand. An
   unreachable claim stops being a dead end.

#### Gates are wrong too, and that has to be measured separately

The same wave: `FreeRTOS Timer Task (Tmr Svc)` was dying against a document
that reads `FreeRTOS Timer Task ("Tmr Svc")`. An honest extract, killed by
our own tool.

I removed quotation marks from the comparison entirely (quotes are markup).
The survival share went **38 % → 45 %**: seven per cent of "helper waste"
was mine.

Words, numbers and case in the comparison were left untouched — in the same
sample, `serial clock bus (SCL)` against `serial clock line (SCL)`, and
that is a genuine defect which must die.

> **Before explaining someone else's waste by their carelessness — measure
> your own tool.** Compare content, not markup; but no loosening may ever
> touch words, numbers or capital letters.

#### The continuous pass, summed up: what actually came of it

58 orders, 2787 units in M1's half. Completed **2775** — 99.6 %.

| | Count |
|---:|---|
| records in total | 2791 |
| **self-references** | **0** |
| with no document named | 16 |
| "read the document, it is not there" | 1704 |
| claimed confirmations | 850 |
| **survived the verbatim check** | **374 (44 %)** |
| unreachable (datasheets not on GitHub) | 219 |
| disputes the book | 2 |

For comparison: wave 1 gave **75 %** waste from self-references alone. Here
there are none in 2791 records — the form of the order holds.

**Landing (`tools/sweep_land.py`) is a separate mandatory step.** A pass
left in a temporary directory does not exist for the registry: no tool sees
it, no gate defends it, and the next wave will walk the same units a second
time. The lessons of landing itself are in `METHOD.md` §3, the third law
about patterns.

#### Wave 8: I removed the mention of the gates — and self-references came back

I rewrote from scratch the order for a queue **with a source named for
every unit** and, shortening it, threw out two sections: "a handbook is not
a source for itself" and the mention that gates exist.

The result over 120 units:

| | Waves 5–7 (sections present) | Wave 8 (I removed them) |
|---|---:|---:|
| records | 2791 | 120 |
| **self-references** | **0** | **2** |

Two in a hundred and twenty is 1.7 %, not the 75 % of the first wave: **a
document named for each unit holds strongly on its own.** But what brought
it to zero was the mention of the gates, and I removed that with my own
hands.

Both self-references also named an **invented repository**:

    raw.githubusercontent.com/yaroslav-voytovych/esp32-handbook-ua

No such owner exists. So what disappeared was not only the prohibition —
what disappeared was the reason not to invent.

> The written law said: **a prohibition in words does not hold, mechanism
> holds.** That is true, but it does not follow that the mechanism may go
> unmentioned. What holds is a **stated** mechanism: a helper who knows the
> address will be checked has nothing to gain from an invented one.

Mandatory in every order, however much it is shortened:

1. a handbook is not a source for itself;
2. **gates exist, and what exactly they reject**;
3. `dzherelo` on every verdict, the negative ones included.

#### Also from that wave: three claimed contradictions, none real

| Unit | Why it turned out false |
|---|---|
| `T-12-023` | took an ESP-IDF document for a claim about Arduino — and **said so itself** in the comment |
| `T-19-023` | stopped at the ready-made partition-table presets, never reached line 137, which says the opposite |
| `T-17-063` | the registry split cut the caveat into the next unit (see `METHOD.md` §3) |

Together with earlier sessions that is **six claimed contradictions and not
one real** after a maintainer checked. So `sperechayetsya` from a helper is
not a finding but **grounds for reading the document in full**; two of the
six even turned out to be evidence **in the book's favour**.

#### Wave 9: the `unchecked` queue gave 82 % — the best we have seen

The `unchecked` queue (simply what nobody had got to), topic + candidate
document, all three mandatory sections in place.

| Wave | Queue | Survived layer 3 |
|---|---|---:|
| 5–7 | continuous pass, topic | 44 % |
| 8 | a source named per unit | 63 % |
| verdicts | `no-external-signal` on numeric claims | 36 % |
| **9** | **`unchecked`, topic + candidate** | **82 %** |

The verdict distribution is different too: `pidtverdzheno` **41 %** against
12 % in the verdict audit.

**This is not to the order's credit but a property of the queue.**
`unchecked` means "nobody looked" — ordinary documentation material lies
there: builds, OTA, BLE, ESP-NOW. `no-external-signal` verdicts, by
contrast, have already passed through somebody's judgement of "there is no
source", so what remains is harder.

The practical conclusion for planning: **queues are not equivalent, and you
should start with `unchecked`.** An `unchecked` unit costs the same work as
a `no-external-signal` verdict and yields six times more.

#### Wave 10: a helper's yield is a warning sign, not a success

Ten Haiku helpers, ten cards each, **random sample** from the whole
`unchecked` queue (seed `20260828`, the list of `id`s in
`factcheck/archive/runs/trial-100/vybirka.json`). There is no candidate **by
construction**: a random draw has no topic to name one for.

    coverage         100 of 100 · no gaps, extras or duplicates
    ne_znayshov       71
    pidtverdzheno     18   survived layer 3:  9  (50 %)
    porada            10   all with `chomu`
    nedosyazhne        1
    self-references    4

##### The main point: more confirmations ≠ more truth

    file   confirmations   verbatim   share
    q01          9             3        33 %
    q05          2             0         0 %
    q06          4             3        75 %
    q10          3             3       100 %

**The helper that gave the most confirmations gave the worst quotes.** Six
of the nine false extracts in the whole run came from one file — the one
that looked like it was working best: 59 tool calls against 30 for its
neighbours, the longest time, the most "result".

> A helper that appears twice as productive as the rest is subject to
> checking, not thanks.

This is the order-of-magnitude rule we had been applying to **counters**,
carried over to **helpers**. And without layer 3 it would have been
invisible: on the reports alone, `q01` looked the best of the ten. It is
the worst.

##### A candidate is worth half the work

Four helpers of ten gave **10 of 10 `ne_znayshov`**. That is not laziness —
they had nowhere to look.

    topical sample, 25 cards     7 confirmations, 0 self-references
    random, 100 cards           18 confirmations, 4 self-references

The shares cannot be compared here (different queues, different sizes), but
the direction is unambiguous: **naming a candidate document is not a
convenience of the order, it is half the work.** `TEMY` in
`work_orders_f.py` does more than it looks.

##### A refinement to wave 8, and it runs against it

Wave 8 showed: remove the description of the gates and self-references come
back. Hence law 6-bis. Here the gates **are described** in all ten orders
(each one checked), and self-references appear anyway: 4 of 100.

But they are of a different kind, and that difference matters more than the
number:

    all four    from ONE helper
    all four    under `ne_znayshov` — they assert nothing
    repository  real, not invented

In wave 8 the self-references were **confirmations** with an invented
repository. Here not one false piece of evidence was born.

> Law 6-bis is refined, not refuted: **a stated mechanism holds against
> false evidence, but not against an empty field.** A helper who was not
> given a document reaches for the one whose existence they know for
> certain — the book itself.

This is testable by experiment: the same set with and without a candidate.

##### The gap was found by a helper, not by us

`T-02-087`. The helper opened `esp32s2/include/soc/soc_caps.h` and wrote
`cytata: (no SOC_BT_SUPPORTED in ...)`. The gate rejected it: that is a
description of an absence, not a quote.

The work was **right**, the conclusion right. **The order had no verdict for
proof by absence** — and that is exactly how a negative claim about a die's
capabilities is established.

Proposal: a verdict `nemaye_v_dzhereli` with mandatory `dzherelo` and
`shukav`, and a gate checking the inverse — the `shukav` line must **not**
stand in the document. Mechanically checkable, unlike the other negative
verdicts. (This became the `absent-from-source` status; see `SCHEMA.md`.)

#### Claimed contradictions: eight of eight false

| Unit | Cause |
|---|---|
| `T-12-009` | the code **shows** what the book says; the helper wrote that itself and still called it a contradiction |
| `T-42-060` | "Wi-Fi is not used" read as "the radio is off"; the book says a line above that the radio is shared |

Across all sessions: **eight claimed, none real**, three of which turned out
to be evidence **in the book's favour**.

> `sperechayetsya` from a helper is not a finding but **grounds for reading
> the document and the book's neighbouring sentences in full.** So far none
> has survived that check.

This does not mean contradictions do not happen: M2 found three real ones in
a session, all three by reading the document in full. It means only that
**a helper's claim of a contradiction carries different weight from a claim
of a confirmation**: the second dies at layer 3, the first must be killed or
resurrected by a person.

#### The law about a document's **capacity**, bought by M2's wave

Rescued from `archive/orders/NARYAD-m2-hvylya3.md`: it was the only copy in
that file. The order was not deleted but put into `archive/` — precisely
because such findings surface after the decision that something is spent and
can be wiped.

> **A named document must be CAPABLE of answering.** An API guide answers
> about the API; a claim about the hardware is not described there.

M2 rebuilt the selection so that hardware claims do not lead to `.rst`
guides, and that **removed 81 pairs** which would have yielded nothing but
"not found".

This explains a bimodality we had been measuring without understanding:
datasheets gave about 43 % hits, API guides **zero**. Not because the
executors worked worse, but because they were sent to the wrong place.

The practical conclusion for building a queue: **before asking "is this true
according to this document", ask "is this document about this at all".** The
second question is cheaper and rejects more.

#### What follows for every subsequent order

There is **one question** to check, and it is the same every time:

> What answer can be given **without leaving the order**? If such an answer
> exists and it asserts something, the order is broken, however many
> prohibitions it contains.

A prohibition in words has not held once in three attempts. In wave 1 the
prohibition "the book is not a source for itself" **was** in the order. In
M2's wave, which gave 10 % waste instead of 75 %, it **was not**. The
difference was not the prohibition.

#### The working form of an order

1. **Do not name the expected distribution of answers.** Not "most will be
   like this", not "the expected answer is this".
2. **Require evidence of work from every verdict**, the negative ones
   included: `not_found` must name the document that was opened.
3. **Name a candidate document in the order itself** (M2's second law). Once
   an address is named, the book's text is not in that file and cannot be
   copied back — and the honest answer becomes the cheapest.
4. **Do not use words that point at book files** ("chapter", "section",
   names like `35-i2c.md`). Group by **topic**: "I²C", "esptool", "flash
   partitions".
5. **Say that gates exist and what exactly they reject.** A forgery that
   gains nothing stops being the cheapest path.
6. **Try it on one helper** before releasing ten.

#### The numbers that identify a broken wave

Do not wait for the end — look at the first fifty records:

- **all verdicts identical** (especially all `confirmed`) — almost always
  forgery; on a random sample that does not happen;
- **the share of records with no `dzherelo`** above a few per cent — the
  order permits answering without looking;
- **the domain in `dzherelo`**: if it is the handbook's own repository, the
  wave is void, however many records it holds;
- **tool calls per unit** below about 1 — the helper downloaded nothing. The
  most honest wave gave 66–89 calls for 25–30 units; broken ones, 14–18 for
  25.

#### What to expect from an honest wave

So as not to mistake the truth for a failure:

- the predominant answer is `not_found`, and that is **normal**;
- of the claimed `confirmed`, about **half** turn out verbatim (layer 3);
- of those that survive layer 3, layer 2 rejects about **another quarter**
  (the quote is verbatim but proves something else);
- the final yield of checked material is **about 6 %** of the units
  submitted.

A wave that gives noticeably more is more suspect than one that gives less.

#### The hit distribution is bimodal — M2's finding

Documents fall into two kinds, and this determines where it is worth sending
a helper at all:

| Kind of document | Hits |
|---|---|
| datasheets, documents about **behaviour** (`ota.rst`, `fatal-errors.rst`) | ~43 % |
| **API** guides (`gpio.rst`, `twai.rst`, `adc_oneshot.rst`) | **0 %** |

The cause is not difficulty: an API guide answers questions **about the
API**, and the book's claims in those units are **about the hardware**. The
question and the document do not match in kind, however long they are read.

Do not put into an order units whose only plausible source is an API guide.
This is not "hard to find", it is "not to be found there".

#### The cheapest answer must be the one that asserts nothing

This is a law about the **order**, not about the helper, and it was bought
expensively: with a wave of 250 units, of which 185 had to be thrown away.

Compare two orders.

In the order for `no-external-signal` the cheapest answer is `spravdi-e`:
"looked, there is no external referent". It **asserts nothing**. A helper
taking the path of least resistance told the truth, and the waves came out
usable.

In the order for `unchecked` the cheapest turned out to be
`pidtverdzheno`. And that **asserts**. Worse: the book's text was right
there in the order — to "confirm" it, all you had to do was copy it back and
substitute a path for an address. And so it went: 185 records of 244 named
the book itself as the "source", a path with no address, or nothing. One
helper described it plainly in its report: "all confirmed in manual files".

> **Law.** The cheapest answer in an order must be the one that asserts
> nothing. Otherwise the order converts carelessness into untruth.

#### The natural experiment that supports this law

On its own the law was a guess from one failed wave. M2 supplied the
numbers, and better than a deliberate design would have.

The same hour, the same cheap model, ten helpers on each side, on one book —
two waves with different orders:

| | M1's order | M2's order |
|---|---|---|
| what it asked | confirm or refute | sort into statuses |
| cheapest answer | `pidtverdzheno` — **asserts** | `no-external-signal` or `unchecked` — **assert nothing** |
| waste | **~75 %** | **~10 %** |

The decisive detail, which none of us noticed at first: **the written
prohibition "the book is not a source for itself" stood in the order that
gave 75 %, and was absent from the order that gave 10 %.**

So the prohibition in words does not explain the difference. The structure
does: **what answer can be given without leaving the order**.

M2 writes that this was not designed deliberately — the form of the order
came out well by accident. That is what makes the experiment valuable:
nobody tuned the result.

What follows for composing orders:

1. look at what answer can be given **without leaving the order**. If such
   an answer exists and it asserts something, the order is broken;
2. do not put into the order what is supposed to be found. The book's text
   is needed there (otherwise there is nothing to check against), but then a
   confirmation **may not** rest on it;
3. a verbal prohibition does not restrain an action cheaper than the work.
   "The book is not a source for itself" stood in the order — and was
   violated 185 times. The same rule as a **gate** in `tools/measure_f.py`
   filtered all 185 out in a second.

The difference is clear from the one helper of ten that did the job
honestly: 5 confirmations and 20 "not found" over 66 tool calls. The one
that reported 25 confirmations out of 25 spent 16.

#### Why the sixth is separate from the first

The first prohibition ("a paraphrase is not a quote") describes
**carelessness**: the helper paraphrased because it was faster. The sixth
describes **confidence**, and it is more dangerous.

Measurement showed this directly. Of nine `znayshov` in a random sample,
three survived layer 3. The three failures were like this:

```
"Bootloader is flashed at offset 0x1000 for ESP32 and ESP32-S2…"
"GPIO pins 6-11 are occupied by the SPI flash interface…"
```

Both **facts are right**. Both sentences are **absent** from the documents.
The helper knew the answer and wrote a sentence to fit it.

So invention happens not where it is hard, but where the answer is
**certain and only the line is missing**. The same mechanism produced the
project's worst confabulation, and it was a maintainer who produced it, not
a helper: `pass-31`, the OTA offsets, reconstructed from memory under
`verbatim`.

#### Why there came to be five prohibitions rather than three

Because pressure works in both directions, and that is the evening's main
lesson.

An order saying "find a source" manufactures **invented sources**. An order
saying "test this `no-external-signal` verdict" reads as "refute this
verdict" — and manufactures **invented refutations** just as reliably. M2
claimed 18 refutations and confirmed **none**; of those, two helpers
produced invented quotes and three cited the book itself.

And not just anywhere: the pressure told precisely where the basket **looked
as though it held something to find**. Where the title carried a number, the
helper searched until it "found". Where there were table headings, the
honest answer was obvious, and it gave it.

Hence the third permitted outcome (`spravdi-e`) and these five prohibitions:
they remove the pressure, not the question. A helper with an honest way to
say "there is nothing here" does not have to invent.

---

### The dump format

The helper puts its result in its own file, and `tools/layer3.py <file>`
checks it **before** anything reaches the registry.

```yaml
- odynycya: T-17-035
  nazva: коротка назва
  verdykt: zbihayetsya | rozbizhnist | ne_znaydeno | nedosyazhne
  dzherelo: https://... (one full address the helper genuinely opened)
  cytata: |
    lines copied byte for byte
  komentar: one sentence
```

`dzherelo` is a **full file address**. Not a directory, not "the ESP-IDF
documentation", not an abbreviated `.../`. A directory instead of a file was
the second most frequent waste of the first wave.

`cytata` is the source's text only. Own prose in that field ("Not found in
esptool documentation") is the third most frequent; that is what
`verdykt: ne_znaydeno` is for.

#### A colon in a value is the maintainer's waste, not the helper's

In one evening broken YAML ate helpers' work **three times**, and not once
through a helper's carelessness. Two lines ordinary in Ukrainian prose broke
it:

```yaml
chomu: не твердження: самоопис книги          # a second colon
chomu: "Simulation is not reality" reflects…  # a value starting with a quote
```

The first line was **verbatim from the briefing**, which the maintainer
wrote. So the format silently demanded of the helper a knowledge of YAML
that nobody had asked of it — and punished the lack of it by losing a whole
batch.

Therefore:

- **in the briefing**, do not show values containing `: `;
- **in the dump**, single-quote any value that contains `: `, starts with a
  quote mark, or starts with a bracket;
- **in the digest**, read through `tools/helper_dumps.py`, which repairs
  this mechanically and names the repaired files individually.

The last is no excuse for skipping the first two. A silent loss of files is
dangerous for the further reason that it is **not random**: in the
`no-external-signal` measure, the files that fell were those of the two
helpers with the highest share of findings, and without the repair the
measure would have drifted downward.

---

### Queues and reusing an agent

Work divides into **sequences**, and a sequence into **batches**. One agent
runs one sequence, batches in a row from start to finish.

**Do not stop an agent while its sequence still has batches.** Every new
agent pays the systemic part over again — the instructions, the tool
schemas, the preamble; only after that does the work become incremental.
Continuing an existing agent costs only the difference.

The first wave did not do this: five agents finished their sequences and
exited, and the next wave paid for the startup a second time. That is a
management error, not a model one.

There is a limit here too, worth remembering: a live agent's context grows,
so from some point the increment per call exceeds the cost of a fresh start.
The rule: **keep an agent alive within homogeneous work, restart it when the
subject changes.**

---

### What to do with what the maintainer did not check personally

`verbatim` means "the quote was genuinely obtained", not "I was told it was
obtained".

Reports the maintainer did not verify by hand go to
`factcheck/archive/history/TO-VERIFY.md` — that is **a work queue, not
coverage**. The difference is not formal: coverage promises somebody looked.

---

### Why an order is sometimes long

The helper is given not only a list of units but a **lesson from previous
waves**, verbatim. For instance:

> The name of a command in a list of commands proves the command exists, and
> nothing else. A claim about what it **prints** requires the implementation
> or a sample of real output.

That costs a few lines of the order and saves a pass. A lesson that stays
only in the maintainer's head will be repeated by the next wave.
