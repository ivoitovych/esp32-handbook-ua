# Fact-checking a book with a pool of cheap helpers

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

    A  primary verbatim    — source obtained, line quoted
    B  primary derived     — source obtained, conclusion unambiguous
    C  named-unreachable   — source named, text not held
    D  arithmetic          — checked by calculation
    E  no source exists    — author's judgement; no external referent
    F  unverified          — nobody has reached it yet
    G  refuted             — the source says otherwise

Strength for picking the best evidence: `A < B < D < C < E < G < F`.

**`C` outranks `E`, and this is the load-bearing detail.** `E` says "no
source exists" and **hides the unit from the queue forever**. `C` says
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
