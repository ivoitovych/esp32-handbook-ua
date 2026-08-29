# Catalogue of defect kinds

> **canonical** — the decision lives here; there are to be no copies

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

## The family that dominates: a check that measures nothing

Thirteen of the twenty-nine kinds below are one family. The check runs, it
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

## 1. Pattern too wide

**Symptom.** One evidence record marks many more claims "checked" than
its source could possibly settle.

**Measure.** Claims bound per record. Legitimate breadth exists (one
record covering 210 API-existence claims is correct), so width alone is
not the test — see kind 2.

**Case.** `ESP-IDF|esptool` bound 173 claims to one record about
version numbers. Three separate occurrences before it was named.

**Held by.** `factcheck.py sketch -v` prints what each record covered.

## 2. Pattern leak — the width hides in the shortest alternative

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

## 3. A zero that counts nothing

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

## 4. A number used as an anchor

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

## 5. Half a thought

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

## 6. A verdict wearing the clothes of a state

**Symptom.** A state that records *what the rule did* is read as a
statement about the world.

**Case.** `E` means "this text has no number, identifier or part name
to check against". It was read, and once printed in the book, as "no
source exists". Two `E` verdicts were proven wrong outright; sampling
put the true rate near a quarter of those carrying a number.

**Held by.** Nothing automatic. `SCHEMA.md` states it; the book's own
description had to be corrected.

## 7. Prescription presented as documented

**Symptom.** The book says *must*; the source says *recommended* or
*may*. Every layer passes, because the quote is verbatim.

**Case.** `sdkconfig.defaults` in git — the source recommends, the book
forbids the alternative. The position is defensible and the book gives
its reason; what was wrong was presenting it as documented.

**Held by.** `tools/modality.py` — a report, not a gate. Its first
version was 88 % false positives; three rounds of exclusion brought 50
matches down to one real.

## 8. Filtering on the adjacent field

**Symptom.** A check filters on a field the maintainer writes, and so
measures the maintainer instead of the subject.

**Case.** An audit of "excessive `E`" filtered by the **record's own
title** rather than the book text; the title is a signature, not data.
It therefore missed both verdicts already proven wrong. Same maintainer
nearly destroyed 124 records with a check that searched the book where
it should have searched the registry.

> Filter on the book's text. The record's title is a signature, not
> data.

## 9. A source reproducible only in the container that wrote it

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

## 10. Silent substitution of a document

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

## 11. Silent data loss

**Symptom.** Records disappear during a bulk operation and nothing
says so.

**Case.** Re-landing a wave overwrote its predecessor: 335 evidence
records became 324, recovered only by `git`. A measurement of class `E`
lost 40 units of 160 to malformed YAML — and lost them **not at
random**: the two assistants with the highest finding rate were the
ones whose files failed.

> Silent data loss is almost never random. It moves exactly the number
> being measured.

**Held by.** `snapshot.py --zvirty` before and after every bulk change.

## 12. An inventory made from filenames

**Symptom.** Files are classified — kept, deleted, moved — without
being opened.

**Case.** A migration plan ordered "spent work orders deleted"; two of
them were a generated report and the specimen work order that is the
evidence for kind 13's measurement. The other maintainer's audit listed
ten files as misplaced letters; one is generated by `measure_f.py`.

Both of us, within a day, from the same shortcut.

> An inventory made from file names is a guess wearing a table's
> clothes.

## 13. A fabricated source

**Symptom.** An assistant cites a document that does not exist, or
cites the project's own repository as an external authority.

**Measure.** Self-citations per batch of returned evidence.

**Case.** 2 of 120 when the work order's gates section was dropped; **0
of 85** when it was restored. What worked was not the prohibition — it
was **explaining why the gate exists**, so the assistant could see its
own constraints as reasonable rather than arbitrary.

**Held by.** `layer3.py` fails on a fabricated source; the work-order
template keeps the gates section.

## 14. A heading mistaken for coverage

**Symptom.** A field or block present on 100 % of records is read as
100 % done.

**Case.** Every card carries an **Evidence** block — with a class-`F`
placeholder when there is no evidence. "8331 of 8331 have Evidence" is
true and means nothing. Real coverage is 30 %.

The same shape fooled both maintainers twice in one week.

**Held by.** `SCHEMA.md` states it beside the card format; `status`
reports coverage separately.

## 15. Closing a violation by changing the class

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

## 16. The book smuggled into the source cache

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

## 17. A machine pointer that is worse than prose

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

## 18. Removing the effect and leaving the cause

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

## 19. Two copies of the same datum, one of them repaired

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

## 20. One unit carrying two claims

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

## 21. A boundary scan that does not know its own format

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

## 22. The same number, meaning something else

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

## 23. A replacement that renamed both sides of the fallback

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

## 24. A check that is red and is not called

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

## 25. Two states of the world under one word

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

## 26. A rename rewrote the rule whose subject was the old name

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

## 27. A normaliser that swallows the start of the quote

**Symptom.** A comparison is loosened to forgive a difference that does
not change meaning, and it rejects records that passed before.

**Case.** Wave w1 (`factcheck/WAVE-W1.md`) showed that most rejected
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

## 28. Several checks around one number, none of them asking about it

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

---

## 29. A report claiming a change the tree does not contain

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

## What has no automatic check

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
