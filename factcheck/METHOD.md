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

    A  primary verbatim    — source obtained, line quoted
    B  primary derived     — source obtained, conclusion unambiguous
    N  absent-from-source  — source obtained; its SILENCE is the proof
    D  arithmetic          — checked by calculation
    C  named-unreachable   — source named, text not held
    S  self-consistent     — checked against ANOTHER PLACE IN THIS BOOK
    L  looked-not-found    — a document was opened; the source was not in it
    E  no external signal  — the text carries nothing checkable
    G  refuted             — the source says otherwise
    F  unverified          — nobody has reached it yet

    K  context             — a whole code block; not a claim, and not counted

Strength for picking the best evidence, in the order printed above:
`A < B < N < D < C < S < L < E < G < F`. The list is deliberately
printed in strength order rather than alphabetically, because the order
is the part that gets used.

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

Measured twice on this project: a random sample of 12 verdicts gave 3
false and 2 doubtful; a pool run over 85 gave 10 confirmed sources
where the verdict said none. **12–25 % of verdicts were wrong.**

---

## 3. Three layers of checking

    layer 1  book → record     does the evidence pattern touch the unit
    layer 2  evidence → claim  is the quote about THIS (semantic, human)
    layer 3  source → evidence is the quote in the document (mechanical)

**Layer 3 removes the requirement for a strong model.** A weak model
fails predictably: it paraphrases instead of quoting, stitches
sentences together, reorders words. Every one of those failures is
caught mechanically and completely. So collection can go to the
cheapest model and expensive attention stays on layer 2.

**Layer 1 must also be automatic, and for a long time it was not.** The
registry is generated from the book, so for prose the equality holds by
construction. But nothing checked that the *generator* was faithful.
When a check was finally written it found 6 genuine mismatches — and
all six were that day's corrections, which is the best confirmation a
check can give itself.


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
  goes in: URL, sha256, size, date. Vendor datasheets are someone
  else's copyrighted material. A project whose thesis is "every claim
  has an honestly named source" cannot afford a copyright violation in
  its own working directory.
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

## 10. Rules about checks themselves

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
