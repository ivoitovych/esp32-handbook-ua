# Catalogue of defect kinds

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

Eight of the seventeen kinds below are one family. The check runs, it
returns zero, and the zero means nothing — because it was never
measuring the thing its name claims.

> **Zero looks the same whether all is well or the counter is counting
> nothing.** And it is read as the first, every time.

The rule that follows from it governs every contribution here:

> **Every new check must be demonstrated working on a deliberately
> broken input**, and that demonstration is part of the contribution. A
> check that has never fired is indistinguishable from a check that
> does not exist.

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

**Held by.** `tools/techa.py` (with self-check).

## 3. A zero that counts nothing

**Symptom.** A check runs, reports zero, and is not measuring what its
name says.

**Case.** Five in one day:

| Where | Promised | Did |
|---|---|---|
| `vorota` | two checks | one |
| `prochid.py` | a candidate per packet | none, silently |
| `stale` | compare the book's text | check the file exists |
| card regex | readers share the format | each kept a private copy |
| `zvyazok.py` name pattern | bad filename is a violation | the letter vanished |

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

**Held by.** `factcheck.py stale`, `znimok.py` (hash-keyed), hash
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

**Held by.** `skhema.py` (card contract: context on every card, the
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

**Held by.** `tools/modalnist.py` — a report, not a gate. Its first
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

**Measure.** `kesh.py --vidtvornist`: is the source's URL or filename
in the committed manifest, with a sha256.

**Case.** 587 of 1025 `A`/`B` records. Not fraud — the cache is
deliberately not committed (the datasheets are copyright, and a book
resting on "the source is named honestly" cannot republish them). The
manifest is the bridge; it simply had not been kept. Fetching the
reachable ones and merging the other maintainer's manifest took
reproducibility 42 % → 71 %.

**Held by.** `kesh.py --vidtvornist`, `make vidtvornist`.

## 10. Silent substitution of a document

**Symptom.** The cache replaces the document underneath an evidence
record that was already written. The evidence keeps verifying —
against a different file.

**Case.** `kesh.py` keyed the manifest by the URL's last path segment.
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

**Held by.** `znimok.py --zvirty` before and after every bulk change.

## 12. An inventory made from filenames

**Symptom.** Files are classified — kept, deleted, moved — without
being opened.

**Case.** A migration plan ordered "spent work orders deleted"; two of
them were a generated report and the specimen work order that is the
evidence for kind 13's measurement. The other maintainer's audit listed
ten files as misplaced letters; one is generated by `mira_f.py`.

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

**Held by.** `citaty.py` fails on a fabricated source; the work-order
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
named, which `skhema.py` flags (class `C` exists precisely to name the
unreachable document). They were closed by changing the class to
`unchecked` — which trips the older, stricter gate in `citaty.py`: an
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

**Held by.** `tools/kesh-bez-knyhy.py` — by sha256 of contents (a copy
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

---

## What has no automatic check

Stated plainly, because a catalogue that hides its gaps is kind 3.

- **Kind 6** — nothing detects a verdict wearing a state's clothes.
- **Kind 8** — nothing detects a check filtering on its own author's
  field. Found by reading, twice.
- **Kind 12** — nothing can tell whether a file was opened before it
  was classified.
- **Kind 15** — caught only because two gates happened to disagree.
  The missing state it exposed is still missing.
- **Layer 2 entirely** — whether a quote actually *supports* a claim is
  human work and always will be.
