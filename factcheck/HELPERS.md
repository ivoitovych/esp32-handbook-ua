# The helper pool: how to brief it, and why exactly this way

> **canonical** — the decision lives here; there are to be no copies

This document used to live in a temporary directory, which is to say it
vanished with the session. That was wrong: a helper's work order is as much
a part of the technology as the registry and `layer3.py`, and yesterday's
order explains yesterday's waste.

---

## Why a cheap model is possible at all

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

## The line a cheap model must not be sent past

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

## What a helper does and does not do

**Does:** downloads the primary source, reads it **in full** against a list
of claims, returns YAML with verbatim quotes.

**Does not:** write patterns, assign statuses, or change anything in the
repository.

The reason is specific: over this project a wide pattern has **three times**
silently marked as "checked" something it never checked. That failure is
invisible, and only an audit in context — one that remembers all three
cases — catches it.

---

## Six prohibitions on what counts as a source

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

### Never name the expected answer

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

### What works instead

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

### Test the order on one helper before releasing ten

Two waves of 250 units were spent on what is visible from two batches. An
order is as much a tool as a script, and `Р-ЗВІРКА` applies to it: try it
first, then use it.

---

## The log of attempts: what was tried, how it failed, what cured it

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

### Wave 6: a refusal is a working outcome, not a breakdown

A helper handed an order with an unkept promise did not invent a document
and did not write "not found". It stopped and named what was missing.

This is worth learning to recognise: **a refusal costs one tool call and
looks like a broken wave by every quantitative sign.** What distinguishes
it is that the helper named a cause, and the cause held up. Before writing
a wave off to a lazy model — read what it actually said.

### The law this wave added to two earlier cases

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

### What a continuous pass does **not** give, and how to say so aloud

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

### Wave 7: prohibiting is not enough — you have to explain

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

### Gates are wrong too, and that has to be measured separately

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

### The continuous pass, summed up: what actually came of it

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

### Wave 8: I removed the mention of the gates — and self-references came back

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

### Also from that wave: three claimed contradictions, none real

| Unit | Why it turned out false |
|---|---|
| `T-12-023` | took an ESP-IDF document for a claim about Arduino — and **said so itself** in the comment |
| `T-19-023` | stopped at the ready-made partition-table presets, never reached line 137, which says the opposite |
| `T-17-063` | the registry split cut the caveat into the next unit (see `METHOD.md` §3) |

Together with earlier sessions that is **six claimed contradictions and not
one real** after a maintainer checked. So `sperechayetsya` from a helper is
not a finding but **grounds for reading the document in full**; two of the
six even turned out to be evidence **in the book's favour**.

### Wave 9: the `unchecked` queue gave 82 % — the best we have seen

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

### Wave 10: a helper's yield is a warning sign, not a success

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

#### The main point: more confirmations ≠ more truth

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

#### A candidate is worth half the work

Four helpers of ten gave **10 of 10 `ne_znayshov`**. That is not laziness —
they had nowhere to look.

    topical sample, 25 cards     7 confirmations, 0 self-references
    random, 100 cards           18 confirmations, 4 self-references

The shares cannot be compared here (different queues, different sizes), but
the direction is unambiguous: **naming a candidate document is not a
convenience of the order, it is half the work.** `TEMY` in
`work_orders_f.py` does more than it looks.

#### A refinement to wave 8, and it runs against it

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

#### The gap was found by a helper, not by us

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

### Claimed contradictions: eight of eight false

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

### The law about a document's **capacity**, bought by M2's wave

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

### What follows for every subsequent order

There is **one question** to check, and it is the same every time:

> What answer can be given **without leaving the order**? If such an answer
> exists and it asserts something, the order is broken, however many
> prohibitions it contains.

A prohibition in words has not held once in three attempts. In wave 1 the
prohibition "the book is not a source for itself" **was** in the order. In
M2's wave, which gave 10 % waste instead of 75 %, it **was not**. The
difference was not the prohibition.

### The working form of an order

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

### The numbers that identify a broken wave

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

### What to expect from an honest wave

So as not to mistake the truth for a failure:

- the predominant answer is `not_found`, and that is **normal**;
- of the claimed `confirmed`, about **half** turn out verbatim (layer 3);
- of those that survive layer 3, layer 2 rejects about **another quarter**
  (the quote is verbatim but proves something else);
- the final yield of checked material is **about 6 %** of the units
  submitted.

A wave that gives noticeably more is more suspect than one that gives less.

### The hit distribution is bimodal — M2's finding

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

### The cheapest answer must be the one that asserts nothing

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

### The natural experiment that supports this law

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

### Why the sixth is separate from the first

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

### Why there came to be five prohibitions rather than three

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

## The dump format

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

### A colon in a value is the maintainer's waste, not the helper's

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

## Queues and reusing an agent

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

## What to do with what the maintainer did not check personally

`verbatim` means "the quote was genuinely obtained", not "I was told it was
obtained".

Reports the maintainer did not verify by hand go to
`factcheck/archive/history/TO-VERIFY.md` — that is **a work queue, not
coverage**. The difference is not formal: coverage promises somebody looked.

---

## Why an order is sometimes long

The helper is given not only a list of units but a **lesson from previous
waves**, verbatim. For instance:

> The name of a command in a list of commands proves the command exists, and
> nothing else. A claim about what it **prints** requires the implementation
> or a sample of real output.

That costs a few lines of the order and saves a pass. A lesson that stays
only in the maintainer's head will be repeated by the next wave.
