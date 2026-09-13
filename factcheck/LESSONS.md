# What this project learned

> **canonical** — the decision lives here; there are to be no copies

A record of what was learned building a fact-checking technology for a
book, kept so that the next attempt starts where this one arrived rather
than where it began.

It is deliberately **not** a method — `METHOD.md` is that. This is the
empirical residue: what was tried, what it cost, what turned out to be
true, and which beliefs did not survive measurement. Most entries carry
the number that bought them, because a lesson without its number is an
opinion.

Attribution is omitted throughout. Who found what is a matter for the
project's history; what was found is a matter for the next book.

---

## 1. The one defect that keeps coming back

More than half of everything catalogued here is one shape:

> **A check runs, returns zero, and the zero means nothing.**

A check that found no files and a check that found no faults print the
same number. Green is the colour of both.

This is not carelessness. It is structural, and it follows from what
fact-checking checks: **absence**. Nothing unverified, nothing
contradicting, nothing missing. An absence-check that breaks returns the
value it returns when all is well. Software tests mostly go red when they
break; these go green.

### Measured instances

| The check | What it reported | What was true |
|---|---|---|
| book-to-record layer | four zeros, exit 0 | it examined **0 of 8331** cards; the directory had moved |
| unit provenance | three zeros, exit 0 | it matched a card heading the generator had renamed |
| refuted-wordings check | 0 findings across 97 files | it globbed a registry that had moved: **0 registries, 0 patterns** |
| coverage | "0 lines, 0 covered, 0.0 %" | an empty tree; `max(1, total)` in the denominator hid it |
| sample selector | 0 matches on 8331 cards | it translated a word back into a letter after the vocabulary changed |
| a CLI | "no units found in status UNCHECKED" | `.upper()` on an argument that had stopped being a letter |
| path checker | "0 literal paths, 0 broken" | it globbed one tool directory of two |
| document-kind checker | "0 violations" | it saw **6 documents of 31** after a restructure |
| a work-order gate | passed everything | it named three of four book directories |
| self-consistency layer | "nothing to check" on 15 of 21 | a filter correct for one corpus, applied to another |

### The countermeasure

Every check must fail on an empty input, and say which input was empty.

    if not units_examined:
        print("NOT ONE unit was examined — that is not clean, "
              "it means there was nowhere to look")
        return 1

Eight tools carry that guard now. Four of the eight were found in the
silent state *while the guard was being added to a different tool*.

A related form: **a zero obtained from an empty section is not a
measurement**. When a document's heading was translated, a pattern
stopped finding the section, the section came back empty, and the check
reported that the normative list "knows none of" all eleven statuses —
the loudest possible conclusion drawn from having read nothing. An empty
section is now its own violation, worded as *the check was NOT PERFORMED,
not passed*.

---

## 2. Copies of one fact

Sixteen live copies of "which directories are the book" existed inside
one technology, in six different shapes:

    a set          four tools
    a tuple        two tools
    a loop         four tools
    a regex        five tools
    a comparison   `if group == "manual"`
    spelled inside another regex   one tool

Two separate sweeps went looking and each missed copies the other found.
The reason:

> **A copy is not found by searching for the name of the fact it holds.
> It is found by searching for the fact.**

The copies **agreed**. That is what made them dangerous, not safe: a set
of copies does not lie until the fact changes, and then it lies in every
copy at once.

Two of the sixteen were also *wrong*, not merely duplicated — one named
three of four directories, so a whole category was never checked; another
pinned the repository by name, so on any other book it would match
nothing and report a confident zero.

### Where copies hide

- a list of names inside the very tool written to catch stale lists;
- a private regex parsing a format another tool writes (three copies of
  one card-comment parser existed simultaneously);
- a **string** rather than a pattern: one tool shared the regex for a
  card heading but not the heading text, and a second tool held its own
  copy of the string and went silent when the heading changed.

> A copy of a pattern is a promise not to change the format. A copy of
> the string itself is the same promise, shorter and therefore less
> visible.

---

## 3. Renames rewrite the rule whose subject was the old name

A search-and-replace pass over a repository rewrites prose that is
*about* the old name, not only references to it.

Measured instances:

- an ignore rule for a cache directory: both lines were rewritten to the
  new path, including the one whose entire purpose was the **old** path.
  In the container where the rename ran, the old directory no longer
  existed, so nothing was visible. In another container it did, and 236
  third-party documents lost their protection.
- a document listing which files are historical had a live document's
  name substituted into it, making the live document "historical".
- a table documenting this exact defect had its left column rewritten,
  turning `| OLD.md | NEW.md |` into `| NEW.md | NEW.md |` — one minute
  after the rename was announced as dangerous.
- a comment contrasting two documents became "caught X and did not catch
  X" — a sentence with no content.

### Countermeasures

**Check the consequence, not the rule.** Do not read `.gitignore` and
believe it; ask the version-control system what it actually tracks.

**Let the thing declare itself.** A list of cache directory names inside
the guard is itself a copy of a path name. The definition that survives
renaming is: *a directory containing a manifest is a cache*.

**Frozen records are not renamed.** Letters, archives and binding
snapshots keep the names things had on their date:

> A record edited to today's names testifies about today and lies about
> its date.

---

## 4. Paths, and assumptions about depth

    ROOT = Path(__file__).resolve().parent.parent

That is not a location. It is an assumption about depth, true only while
every tool sits exactly one directory below the root, and false the
moment one moves — silently, because every path under a wrong root still
resolves.

The same assumption appeared five times in five files: a one-level glob,
a root-only name resolution twice, a name split before its prefix was
stripped, and a block pattern that ended at end-of-file.

**The fix is not to change the count.** Walk up until the directory
containing the version-control marker. Then a tool works at any depth,
and moving it is no longer an edit to it.

Two further lessons from the same area:

**One path has several spellings.** A sweep matching one spelling of a
path constant missed another, and missed
`"root" / "dir/file.yaml"` — the directory name was not a whole token
there. Six live constants stayed broken and every gate was green, because
those paths are only touched when someone runs that particular tool.

**A false hit is worse than a miss.** Once tools lived in two
directories, a pattern written for a tool path in one of them also
matched that path as a *substring* of the other — then checked an address
that had never existed and declared a sound document broken. A miss is at
least visible; a false hit reads as a finding.

The same trap caught a check of the checks. A sweep for stale tool
references searched for the qualified form — the tool directory, a
slash, the file name — and reported zero, while the documents it was
auditing name a tool the way prose does: bare, with no directory. Seven
dead names sat in plain sight behind a clean report.

**Scope named after a directory stops at that directory.** Every
document-level check took `factcheck/` as its subject, because that is
where the technology lives. Six documents in the repository root were
therefore outside all of them — unlabelled, unlinked, unchecked — and two
had been quietly rotting for months. Nothing failed; there was simply no
check whose subject they were. The remedy is the same one as for depth:
name the subject by what it *is* (a maintainer's document) rather than by
where it happens to sit, and give the scope itself a probe, because a
scope that silently shrinks back to one directory reads as a clean run.

**A sweep for your own names collects other people's.** Auditing those
same documents for stale tool names picked up `idf.py` — Espressif's
build tool, discussed as a subject of the book, never ours and not stale.
Seven of the eight names it flagged were real; the eighth would have sent
a reader hunting through the rename map for something that was never in
it. A pattern that recognises the *shape* of your names (`*.py`) has not
established their *ownership*.

---

## 5. Work orders are mechanism design, not instructions

This is the most transferable thing the project produced, and it did not
come from software engineering.

> **The cheapest answer in a work order must be the one that asserts
> nothing. Otherwise the order converts carelessness into untruth.**

Measured, in a natural experiment: two orders, same hour, same cheap
model, ten executors each, same book.

| | order A | order B |
|---|---|---|
| what it asked | confirm or refute | sort into statuses |
| cheapest answer | "confirmed" — **asserts** | "no signal" — **asserts nothing** |
| waste | **~75 %** | **~10 %** |

The decisive detail: the written prohibition *"the book is not a source
for itself"* stood in the order that produced 75 % waste and was **absent
from** the order that produced 10 %. The prohibition explains nothing.
The structure explains everything.

### The laws that followed

**Never name the expected answer.** An order that stated "the expected
answer here is *not found*" received exactly that, without work: of 190
answers, **8** named a document. Two executors quoted the order's own
sentence back as justification.

> An order that names the expected answer gets exactly that answer —
> with no work done. It does not matter which answer it is.

**Require evidence of work from every verdict, including the negative
one.** As long as "not found" can be written without naming anything, it
costs zero and becomes the default. Once it must name the document that
was opened, it costs the same as the rest.

**Name a candidate document in the order.** Without one, executors reach
for the only document whose existence they are certain of — the book
itself. With a hand-picked topical sample: 0 self-references. With a
random sample and no candidate possible: 4 of 100.

**A verbal prohibition does not restrain an action cheaper than the
work.** "The book is not a source for itself" was violated 185 times
while written in the order. The same rule as a mechanical gate filtered
all 185 in a second.

**But stated mechanics do hold.** When the paragraph explaining *that
gates exist and what they reject* was removed to shorten an order,
self-references returned. Not because the prohibition was gone — because
the reason not to invent was gone. An executor who knows the address will
be checked has nothing to gain from inventing one.

**Explain, do not forbid.** A prohibition without a reason leaves guessing
as the cheapest path. Told that a paraphrase will be discarded mechanically,
an honest "looked, did not find" becomes the best available result rather
than a defeat.

**The order is the entire world the executor lives in.** What is not
written in it does not exist for them — including the fact that their
work will be re-checked.

### Reading the results

**Caution and laziness look identical in the counts and separate under
reading.** One arm of a paired run returned nearly twice as many
"unreachable" verdicts as the other, which reads as giving up. Reading
the eight units where the arms directly contradicted each other: the
cautious arm had genuinely given up on **2**, and the confident arm was
**fabricating on 6** — three of the six citing a repository's README as
the source, one citing an operating-system kernel's README as the source
for a user-space tool.

> Before calling an executor lazy, take the units where it refused and
> another did not, and check the other one's work.

**Agreement between independent runs predicts quality.** On the same 200
units judged twice, 16 of 27 layer-2 passes were agreed by both runs, but
only 3 of 13 failures were. Agreement is cheap to compute and worth more
than either run's confidence.

**High yield is an alarm, not a success.** The executor producing the
most confirmations produced the worst quotes: six of the run's nine false
extracts came from the one file that looked best by every other measure —
most tool calls, longest time, most "result".

> An executor that appears twice as productive as the rest is subject to
> checking, not thanks.

**Refusal is a working outcome.** An executor handed an order with an
unkept promise stopped and said what was missing. That costs one tool
call and looks like a broken wave by every quantitative sign. What
distinguishes it is that the stated cause turns out to be true.

**Claimed contradictions are not findings.** Across every wave, **8
contradictions were claimed and 0 were real**; three turned out to be
evidence in the book's favour. A claimed contradiction is grounds for
reading the document and the book's neighbouring sentences in full —
nothing more. Meanwhile the real contradictions that were found came from
a person reading a source in full.

**Ask whether the document can answer at all.** Datasheets and
behavioural documents yielded ~43 % hits; API reference guides yielded
**0 %** — not because the work was worse but because the question and the
document did not match in kind. Removing those pairings from a queue
eliminated 81 units that could only ever have returned "not found".

---

## 6. What the three layers can and cannot do

    layer 1   book -> record     is every claim covered
    layer 2   evidence -> claim  does this quote support this claim
    layer 3   source -> quote    does this text stand at this address

**Layer 3 is the only one with a cheap exact oracle**, and that is what
makes cheap executors safe: a weak model fails predictably — paraphrase,
stitching, reordering, plausible invention — and every one of those
failures is caught mechanically.

**Layer 2 has no mechanical form and never will.** Whether an extract
supports a claim is human work. Saying so plainly is better than
pretending a percentage covers it.

**And it rejects a large fraction of what layer 3 passes.** Measured
twice: about a quarter on one wave, **32 % on another** (13 of 40
survivors). The failures are verbatim and irrelevant — a table heading
offered as proof of a capability, a quote about protocols offered as
proof about a different feature, a US timezone string offered as proof of
another country's daylight-saving rule.

> A verbatim quote proves the text exists. It does not begin to prove
> the text is about the claim. Reporting layer-3 survival as if it were
> correctness overstates the work by a third.

**A fourth layer is missing: book against book.** The registry checks the
book against sources but not against itself, and some of the worst errors
found were internal contradictions between chapters.

### The reframe that fits

**This is audit, not unit testing.** A unit test's expected value is
authored by the same person as the code; a fact's truth is external.
There is no `assert`.

What an auditor does, and what this project reinvented without naming:
enumerate the population, stratify by risk, sample with a stated frame,
measure the error rate, publish a confidence bound.

**What transferred from software engineering:** the ratchet, content-hash
reproducibility, and demonstrating every check against a corrupted input.

**What did not:** assertions, coverage as a goal, and green-means-good.

---

## 7. Coverage inverts into Goodhart's law

A registry can be complete by construction: every line of the book gets a
record whether or not anyone works on it. That is worth having — an
absence becomes a decision rather than forgetfulness.

But "every claim has a recorded status" is not "every claim was checked".
In this book, **46.6 %** of records carry a status meaning *the project decided
not to look*. That status is assigned mechanically, for want of a digit
or identifier in the text — and it reads to a reader as *no source
exists*. Those are different statements, and the difference falls in the
project's favour, which is exactly why it must be measured.

A random sample of 160 units found that roughly **37 %** of that status
does have an external referent. The status is not one thing but three:

| state | share | what to do |
|---|---:|---|
| has an external referent | ~37 % | check it; the verdict was wrong |
| genuinely the author's position | ~50 % | leave it; the verdict is honest |
| not a claim at all — a heading, a self-describing table row | ~13 % | not a unit; this measures the splitter, not the book |

The third row is worth separating: it measures the **granularity of the
tool**, not the quality of the book, and hiding it inside "unchecked"
manufactures an inflated sense of debt.

> **The number to publish is not coverage.** It is what was read in full,
> plus the sampled error rate with its bound. "Every claim has a recorded
> status" invites the reader to hear "every claim was checked".

---

## 8. Measurement discipline

**A random sample and a hand-picked sample answer different questions,
and their percentages must never be mixed.** A harvest picks where the
light is — correct for harvesting, useless for measuring, because the
sample is selected on the very property being measured.

**Write the seed into the order.** A sample can be redrawn until the
number is pleasing; the defence is that the seed and the method sit in
the file beside the result, so a redraw is visible as a different seed.
Never take the seed from the clock.

**Publish the interval only where it means something.** For a random
sample it estimates a population share and has a computable error. For a
hand-picked one it would be a lie.

**And say when the interval is optimistic.** It accounts only for
sampling error, assuming each unit has one right answer any judge would
give identically. When the spread between judges exceeds the sampling
error, the dominant uncertainty is the definition, not the sample size,
and lengthening the sample is pointless until the definition is sharper.

**Read the population live.** A number written down on the day of the
draw goes stale and starts to lie exactly where it is read most
carefully. The share stays valid; the population does not.

**Two measures of one thing that differ tenfold do not contradict each
other if each names what it measures.** One counted the presence of a
mechanically checkable signal; the other counted judgements about whether
a referent exists. Without those names, both read as estimates of the
same quantity.

**A measure reports what it measured.** What it did *not* measure it does
not report, and that silence reads as zero. A ratchet counting
identifiers was read as a statement about a whole directory; the number
was right and the sentence built from it was false.

**Verify by numbers, not by ideas.** Checking a document consolidation by
reading for lost ideas missed losses that a comparison of the numbers
found immediately.

> Numbers survive a translation; a measure without its number is no
> longer a measure.

**A check that diverges by an order of magnitude is broken until proven
otherwise.** This rule caught four false reports in one week.

---

## 9. Reproducibility

**Bind by content, not by identifier or line number.** A snapshot written
by unit id showed 34 evidences that had "lost" their units after a book
edit shifted the numbering. Nothing had been lost. Rewritten against a
content hash: 0 of 1337.

> A number is the address at which a unit can be found today. A hash is
> what it is.

The same rule appeared independently for cards: a line number is a
locator, not an anchor.

**Take the snapshot before, not after.** Once a format changes, the old
patterns match nothing and there is nobody left to ask what they used to
match.

**Version what the executor actually sees.** Hashing a template alone
made an order with the surrounding book text and one without it produce
the *same* version — two different technologies under one label, and the
difference between them recorded as noise.

**Downloaded sources need a manifest, and the manifest is the record.**
The files themselves stay out of version control; the manifest — URL,
name, size, hash, date — goes in, weighing kilobytes against gigabytes.
Anyone can re-download and compare hashes.

**Do not derive what has already been recorded.** Deriving a cache
filename from a URL is a promise that the derivation rule will never
change. It changed once, stranding 54 files that the checker then
reported as "not in the cache" — indistinguishable from genuine
unreachability.

**An address that cannot be derived can be recovered by verification:**
generate candidates and keep the one whose file actually exists. This
form cannot emit a false address, which is better than a form that
guesses well.

---

## 10. Checks about checks

**A check that has never fired is indistinguishable from one that is not
there.** Every check carries a demonstration against a corrupted input.
Adding the first demonstration to one layer revealed that the layer had
been examining nothing.

**A demonstration must use the real format.** One written against an
invented card format passed for the wrong reason; the format is now taken
from the generator rather than retyped.

**Demonstrations go stale with the tree.** A "sound list" case named a
document that had since been absorbed elsewhere, and the case began
failing although nothing was wrong. Only running it showed that.

**A check exercised only by its clean path is tested only where it does
not matter.** A partially-renamed function reported "0 divergences" while
every one of its error branches was a `NameError` waiting for the first
real violation — that is, it would have crashed on the day it had
something to say.

**A gate outside the gate is a gate nobody passes through.** Two ratchets
ran only when invoked by hand for days, because the target that ran them
was not a dependency of the main check.

**Record what a check cannot do, beside the check.** A path checker reads
literals, so a path assembled from variables is invisible to it — and
that limit was real: a computed card path went wrong exactly there. A
measure that hides its limit is itself the defect it hunts.

**Swallowed failures blind the checker.** A bare `except SyntaxError:
continue` made two tools invisible to the tool that reads them, and a
generated document was consequently declared canonical — the most
expensive kind error available, because a canonical document gets edited
by hand.

**An exception must never be printed where a number belongs.** One
report rendered a failed measurement as `! name 'x' is not defined` in a
right-aligned numeric column. It read as a number, and the item merely
looked open. Broken measures and bad measures are different events.

---

## 11. Editing, migration, and destruction

**Structured data is edited as structure, never as text.** Substituting
inside a multi-line YAML scalar left the continuation dangling and the
file unparseable. Where a line-level edit *is* safe, prove it first: every
line was verified to be a bare scalar before 1366 of them were removed.

**Verify before removing, not after.** Before dropping a duplicated
field, every record was confirmed to carry its replacement. Zero would
have lost information — that was the one irreversible step.

**Expand, migrate, contract.** Write both forms, move every reader, then
remove the old form. During the middle phase the two forms *will* drift:
15 and 14 records diverged in one pair, because a repair tool wrote one
side of the pair only.

**A migration that changes a number has changed the thing it was
migrating.** A baseline is taken before the first edit and compared after
every step. The contraction of 1366 records and 8331 comments moved no
number at all.

**Enumerate, then judge; never substitute blindly.** A pattern intended
for one directory matched across a slash and rewrote 92 card files,
replacing verbatim book text. Later, the same class of change was done by
listing every occurrence and deciding each: 2 moved, 7 stayed — those
seven being the book itself.

**Narrowing "just in case" breaks the cases the author did not have in
mind.** Tightening a character class to strip a trailing comma broke two
records whose paths legitimately contained commas — and the trailing
comma was already handled elsewhere. The fix cured what was cured and
broke what worked.

**Half a move is worse than none.** Files moved; the tools that write
them did not. Nothing failed. Each next run would have recreated the old
files, and version control would have shown not an error but work.

---

## 12. Portability: the seam must be executable

The technology is meant to lift onto another book. That seam was prose
for a long time — a sentence naming what travels — and a sentence drifts.

> A promise in the text is an invariant too. It must either hold or be
> removed from the text. An unkept promise is worse than an absent one:
> an absent one is visible, and an unkept one is relied upon.

Three documented cases of a document promising something the code did not
do; each was found by someone *trying to use* the promise, never by
reading it.

**So "what travels" is a script.** It copies the technology, creates the
directories, and then **runs the new tree's own self-checks**. It also
asserts that the work-order version carries over identically, because
otherwise the next book briefs its executors with different text under
the same number and the two books' runs are silently incomparable.

**And it asserts that a fresh copy refuses to run until configured.** A
copy that runs unconfigured is worse than one that fails: it runs against
the wrong directories and reports a confident zero.

### What turned out to be per-book, not technology

Every item below was found inside a tool, where it would have made that
tool silently wrong elsewhere:

- the book's own directory names — sixteen copies;
- the book's title, in the report generator;
- words for "chapter", "appendix", "card" — used by a gate that catches
  the book being cited as its own source; on another book it would have
  admitted every self-citation;
- modal verbs, for the check comparing a prescription in the book against
  a permission in the source;
- unit abbreviations that mark a checkable signal;
- the repository's own name, in the check that catches self-citation;
- the topic buckets that decide who can close which unit — part numbers
  and API prefixes;
- the list of reachable source repositories and the local egress caveat.

They live in one data file now. The general rule:

> A thing that differs per book is configuration. Configuration written
> into tools is not configuration — it is N identical decisions waiting
> to disagree.

And configuration must be **loud when missing**. A silent default lets a
new book run the whole technology against the wrong directories and
report a confident zero.

---

## 13. Directory structure, and what "legible" means

Three shapes were tried:

    flat        32 documents, 21 directories, 11 loose files in one root
    grouped     6 documents, 12 directories, grouped by kind
    minimal     3 documents, 3 directories — everything behind `data/`

The first and third fail for the same reason: **neither tells you where a
new thing goes.** In the flat one, everything went in the root because
that is where things went. In the minimal one, everything goes in `data/`
because the name means nothing and therefore accepts anything.

> A bucket named `data` is a flat root with one extra keystroke.

The properties that make a directory legible are testable, not aesthetic:

1. you can guess where a new file goes without asking;
2. nothing important is hidden;
3. nothing unimportant is in the way;
4. a newcomer knows what the place is for without reading anything.

The grouping that survived is **by how long a thing lives** — permanent,
regenerated, transient, frozen, external — because that is the question
you can actually answer about a new file.

Two more rules that earned their place:

**The root holds what a reader needs to orient, and what travels.**
Everything else lives in a directory named after what it is.

**Nothing is deleted.** Spent work is archived, not removed: a paired
experiment is the only reason either of its numbers means anything, and
deleting the data leaves the conclusion standing on nothing.

---

## 14. Language, and why it was a technical problem

The technology's prose migrated to English so it could be lifted onto
another book; the book, its cards and its registries stayed in their own
language.

The instruction was initially misread as being about **transliterated
identifiers** — names like `klas`, `dzherela` — because those were what
could be pointed at. A ratchet was built, hundreds of names recorded,
progress reported against it. Meanwhile half the foundation documents and
every tool's prose remained untranslated.

> The visible symptom is not the subject. A check aimed at the symptom
> reports real progress while the subject is untouched — and the report is
> honest, which is what makes it expensive.

What made the migration tractable:

- **a ratchet per subject**, recording today's remainder so it can only
  shrink;
- **zones written down**: which files must be in which language, and why
  — the technology travels, the book does not;
- **measuring generated reports by their frame**, excluding quoted book
  text, since translating a quotation would forge it. This rule was
  *rejected* when first proposed, because measurement showed the frame
  was more foreign-language than the whole; it was adopted later, when
  the same measurement showed the opposite. A rule goes in when it becomes
  true, not when it becomes convenient.

And the incidental finding, repeated in every batch:

> **Translating a file is the cheapest audit available.** Every tool
> translated had something wrong with it — a stale pattern, a hardcoded
> value, a silent zero, a copy of somebody else's fact. Reading closely
> is what finds these; nothing else did.

---

## 15. Vocabulary

Three parallel systems for one set of statuses existed at once: single
letters, words, and emoji. All three were removed in favour of words.

The argument that settled it: **an abbreviation is a legend somebody has
to keep in their head**, and beside every letter the same word already
stood. Nothing was gained by the letter except brevity in a place where
brevity had no value.

The migration is instructive on its own:

- both forms coexisted while every reader was moved, with the word
  derived from the letter in exactly **one place per tool**, so that the
  contraction would *delete a line* rather than add a second way to read;
- the contraction then reversed that single line, and every number stayed
  identical;
- four tools outside the main gate broke anyway, in ways only found by
  reading them.

**A status must not certify itself.** Of the eleven statuses, one means
"no external source exists" and is assigned mechanically for want of a
signal. It is the only status that points inward, and therefore the only
one that needs measuring rather than trusting.

**A status introduced to record a check must actually run that check.**
When "the book agrees with itself" was introduced, it was made to pass
layer 3 against the book — otherwise it would have been a label asserting
a check that nobody performs.

**Missing states force lies.** Executors had been reporting "looked and
did not find" for days with nowhere to record it, so it was translated by
hand into one of two wrong statuses each time. Similarly, proof by
absence had no verdict, so an executor doing correct work had no lawful
way to write it down: it wrote a description of an absence into a field
checked as a literal quote, and was rejected for it.

> A form in which the correct answer cannot be expressed is a defect of
> the form, not of whoever fills it in.

---

## 16. Where errors were actually found

Worth stating plainly, because it contradicts what the machinery seems to
promise.

The mechanical layers caught **fabrication**: invented sources, invented
coordinates inside real documents, paraphrases presented as quotes,
patterns matching everything. That is what makes cheap labour safe.

They caught almost no **errors in the book**. Those came from passes
where a person or an agent read a source in full and asked *"does this
actually follow?"* — and the four places where errors lived turned out to
be:

1. **compound claims** whose halves rest on different documents;
2. **explanations rather than numbers** — every number checked was right,
   and the corrections all landed in "why the offset is what it is";
3. **the unwritten** — a correct statement with half of it cut off: "there
   is a pull-up" without the value, "this pin is dangerous" without the
   direction;
4. **the direction of the inference** — right arithmetic, right source,
   and a consequence that reverses the physics.

What all four have in common is that a number is present and correct. The
registry sees the number; that what stands beside it does *not follow*
from that number is not something it can check.

> The mechanical layer is a filter against fabrication, not a detector of
> error. Detection is done by reading. Stating that plainly stops the
> machinery from being asked for something it cannot give.

---

## 17. Open problems

Recorded so the next attempt does not rediscover them as surprises.

**Layer 2 has no mechanical form.** Whether a quote supports a claim is
human work, permanently.

**Book-against-book has no tool.** Designed, unbuilt. Some of the worst
errors found were internal contradictions.

**Five catalogued defect kinds have no automatic check**, including: a
verdict wearing a status's clothes; a check filtering on its own author's
field; whether a file was opened before it was classified; a unit
carrying two claims.

**A heading is not a claim, and neither is anything else that speaks
about the book rather than the world.** A heading names a topic; what it
asserts — that this topic exists and is in scope — has no external
referent even in principle, and the review that settles it is the
table-of-contents review. Measured: 850 heading lines, 744 distinct
texts, **0** of 8331 units a heading. Two headings carry a value rather
than a name; both are covered by the units beneath them, which quote the
heading in their own context block.

The general form is worth more than the case: **before asking how a claim
is known, ask what it is about.** A statement about the book's structure,
its own registry, or its table of contents is not a candidate for
external checking, and putting it in the base inflates the denominator of
every percentage with work that could never be done.

**The granularity of the splitter is itself a measured quantity** —
roughly an eighth of one status is not claims at all — and no tool
distinguishes "not checked" from "not a claim".

**Nothing detects a copy of a fact.** Sixteen were found by reading; a
seventeenth would be found the same way.

**A naming convention standing in for a definition.** A run gate read
`q*.yaml` because every batch file had happened to start with `q`. A wave
whose files were named otherwise would have been read as **zero
answers** — and "no answers" is indistinguishable from a wave nobody ran.
A dump is a file whose records name units; that is a definition, and the
glob was not one. The same shape as a cache defined by a list of
directory names rather than by containing a manifest.

**A batching decision can disable an honesty signal.** Tool calls per
unit told diligence from rubber-stamping — until an order permitted
fetching every document up front, after which every executor fell below
the floor. The replacement was to require the **location within** the
document, not only the document: twenty units judged honestly against one
file give twenty different locations. Worth stating generally: **changing
how work is done can silently retire the measure that watched it.**

**A check that reads source literals cannot see computed paths.** The one
case that fell into that gap wrote 92 files into a deleted directory and
nothing failed.

---

## 18. The shortest version

If everything above were lost but one page survived:

1. A check that returns zero must prove it looked at something.
2. One fact, one place. Copies agree until they don't, and then they all
   lie at once.
3. Bind to content, never to a number or a name.
4. The cheapest answer available to an executor is the answer you will
   get. Make it the one that asserts nothing.
5. A verbal prohibition does not restrain an action cheaper than the
   work; a stated mechanism does.
6. Measure with a random sample and publish the interval, or do not
   publish a percentage.
7. Coverage is not checking. Say what was read in full and what the
   sampled error rate was.
8. A promise in prose is an invariant. Make it executable or delete it.
9. Anything that differs per book is configuration, and configuration
   must be loud when missing.
10. Read the file. It is the cheapest audit there is.

---
---

# Part II — The working journal

Everything above is distilled. This part is the raw state: where the work
stands, what was decided and why, what was abandoned, and what the next
session should pick up. It is appended rather than merged on purpose —
merging costs judgement, and losing it costs more.

> **On the name.** This file is called `LESSONS.md`, and the name is
> narrower than the contents. It is the project's memory: lessons, yes,
> but also decisions, measurements, abandoned approaches, and the state of
> play. Read it as a journal. Do not decline to write something here
> because it is not a "lesson".

---

## 19. Where the work stands

Numbers are the ones measured at the time of writing; every one is
reproducible by the named command.

### The registry

    claim units                      8331  (8110 claims + 221 code blocks)
    checked against a source          2385   29.4 %
    closed as a decision              3780   46.6 %   no external signal
    still open                        1920   23.7 %
    self-consistent                     44           counted in neither
    evidence records                  1393
    sources in the cache               380 manifest rows, 310 files, 136 MB
    reproducible from the manifest     ~79 %

    book lines with a card           11948 of 12041   99.2 %
    structural grounds (headings)       93            named, not dropped

### The migration to English

    files still Ukrainian in the English zone   41   (was 76)
    transliterated identifiers                 208   (was 227)
    tools translated                            22   of 53

Zones: `factcheck/tools/` and the three root documents are English,
because they travel. `tools/` at the repository root is not claimed to
travel and keeps the book's language. Cards, `book/` registries and the
book itself are Ukrainian. Letters, archive and snapshots are frozen.

Generated reports are measured by their **frame** — outside fences,
blockquotes and table rows — because their bodies quote the book, and
translating a quotation forges it.

### The directory

    factcheck/
      README.md  METHOD.md  REPORT.md  LESSONS.md
      tools/          53 fact-check tools
      cards/          92 files mirroring the book
      evidence/      201 records
      reports/        15 generated
      work/           queues, triage, runs, snapshots
      archive/        spent work
      source-cache/   not in git; MANIFEST.md is

Grouped by **how long a thing lives** — permanent, regenerated,
transient, frozen, external. That is the question you can answer about a
new file, which is why it is the grouping that survived.

---

## 20. The eight per-book blocks, and why each was extracted

`factcheck/book.yaml` holds everything that differs between books. Every
entry was found inside a tool, where it would have made that tool
silently wrong elsewhere. This list is the single most useful thing for
starting a second book.

| block | what it is | what carrying it inline would have done |
|---|---|---|
| `title` | the book's name | the report would name the wrong book |
| `groups` | the book's own directories | **sixteen copies** across the tools; on another book, everything reads as empty |
| `signal.broad` / `signal.strict` | what counts as an externally checkable signal | **the entire book swept into one status by default** — the most consequential of all |
| `split_buckets` | who can close which unit | every unit falls into "nobody"; the split prints a complete, empty division of work |
| `intake.*` | the book's words for "chapter", "card", "appendix"; unit abbreviations | the gate against citing the book as its own source admits everything |
| `layer3.*` | a self-declaring editorial title; a number with a unit | the "over-generous status" question stops being asked |
| `modality.*` | the book's modal verbs | the prescription-versus-permission check silently passes everything |
| `reachable_sources` | which hosts answer from this container | executors are sent to another book's repositories |

`signal` is **required**; the rest are optional, and an unconfigured
optional block makes its tool say *"SKIPPED, not passed"* rather than
report a clean run.

> A thing that differs per book is configuration. Configuration written
> into tools is not configuration — it is N identical decisions waiting
> to disagree. And configuration must be loud when missing.

---

## 21. Decisions taken, with their reasons

**Statuses are words, not letters, and not emoji.** Three parallel
notations existed for one thing and had already drifted. An abbreviation
is a legend somebody must keep in their head, and beside every letter the
same word already stood. The migration ran expand → migrate → contract,
with the word derived from the letter in exactly one place per tool so
the contraction deleted a line rather than adding a second way to read.
Every number was identical before and after.

**The root of the fact-check directory holds what a reader needs to
orient and what travels.** Everything else lives in a directory named
after what it is. Two earlier shapes failed for the same reason: neither
told you where a new file goes. A bucket named `data` is a flat root with
one extra keystroke.

**Nothing is deleted; spent work is archived.** A paired experiment is
the only reason either of its numbers means anything.

**Frozen records are never renamed or translated.** Letters, archives and
binding snapshots keep the names things had on their date.

**The cache stays out of version control; the manifest goes in.** The
manifest is the reproducibility record and weighs kilobytes against
gigabytes. The rule is enforced by asking version control what it tracks,
not by reading the ignore file.

**Headings never become units.** A heading names a topic; what it asserts
is about the book's structure, settled by the table-of-contents review.
Measured: 850 heading lines, 0 units. Two headings carry a value rather
than a name and are watched by a standing check.

**What travels is a script, not a sentence.** Provisioning copies the
technology, then runs the new tree's self-checks and asserts the order
version carries over — and asserts the copy REFUSES to run unconfigured.

---

## 22. What was tried and abandoned

**Merging every document into one.** A three-thousand-line file is not
re-read whole, so drift stops being visible instead of stopping. What
replaced it: a consistency check that compares documents against the
code.

**Moving content between documents on a cadence.** A discipline, and the
project's own law says disciplines do not hold. A check holds.

**Deleting spent trial output.** Proposed and rejected: the paired
experiment's two halves are the only reason either number means
anything.

**Registering headings as units.** Would create thousands of claims with
no verb.

**Requiring zero unchecked before release.** Deliberately absent from the
release gate. The registry decomposes the book into thousands of units,
among them editorial judgements for which no external source exists.
Demanding zero would force closing them fictitiously.

**Narrowing a character class "just in case".** Broke two records whose
paths legitimately contained commas, while curing something already
cured.

**A verdict of `not_found` that names nothing.** Retired: it costs zero
and becomes the default answer.

---

## 23. The tools, in one place

Not an inventory — a map of which tool answers which question, because
that is what a newcomer needs and what a grep does not give.

    factcheck.py    the skeleton: split the book, render cards, status,
                    staleness, the hand-off order, the release gate
    layer3.py       does the quote stand in the named source
    layer1.py       does the card present the book honestly
    layer1_units.py does the unit come from the book at all
    coverage.py     is every line of the book accounted for
    schema.py       the record format and the card contract
    intake.py       may this evidence enter the registry
    intake_f.py     was this run of executors valid
    sample.py       draw a random sample; build an order; digest a wave
    measure_f.py    how much of the unchecked is actually wrong
    split_queue.py  who can close which unit
    sweep_land.py   land what survived into the registry
    patterns_repair.py  rebuild idle patterns from the unit's text
    snapshot.py     which units each evidence binds to, by content hash
    cache.py        fetch a source, record it in the manifest
    cache_vs_book.py is a file of the book sitting in the source cache
    docs.py         do the documents agree with the code
    doc_kind.py     is each document's kind marker true
    paths.py        does every literal path resolve; do all tools parse
    name_lists.py   is every name in a list the name of something
    naming.py       the transliteration ratchet
    language.py     the language ratchet
    report.py       assemble REPORT.md from what the tools measured
    newbook.py      provision another book, and prove the copy runs
    config.py       what differs per book
    repo.py         where the repository root is, found not counted

Eight of these refuse to report a clean run on an empty input. Four were
found in exactly that state during one week.

---

## 24. How a wave actually runs

The economics, because they are not obvious and they decide how much to
attempt.

    a batch          20 units per executor
    a wave           10–20 executors, run concurrently
    cost per batch   40–95k tokens, 25–60 tool calls, 2–5 minutes
    yield            of 200 units, ~30–55 claimed confirmations,
                     of which ~half survive layer 3,
                     of which ~two thirds survive layer 2
                     -> roughly 25–35 units genuinely closed per 200

That final ratio — **about one unit closed for every six or seven
attempted** — is the number to plan with. Earlier prose said "about 6 %
final yield"; the measured figure on a random sample of the unchecked
queue is closer to 13–17 %, because that queue is richer than the one
that produced the 6 %.

The steps, in order, none skippable:

1. draw a random sample, seed recorded **in the order**;
2. generate the order from the spec blocks; note its `order_version`;
3. take the before-baseline;
4. run the executors; each writes one YAML dump;
5. read the dumps — repair broken YAML mechanically, name what was
   repaired, skip anything that is not a dump;
6. layer 3 on everything carrying a quote;
7. **layer 2 by a person** on what survived;
8. fetch every cited source into the cache and the manifest **before**
   landing;
9. land; regenerate; compare against the baseline;
10. append one row to the run ledger.

Step 7 is the one that cannot be automated and the one most often
skipped. It rejects about a third.

---

## 25. Working with a second maintainer

The coordination model, stated impersonally because it generalises.

**Letters, dated, in a directory, with a header naming the sender,
recipient, kind, what it answers, and the commit it was written against.**
A protocol check enforces the header and tracks whose turn it is. This
matters more than it sounds: two maintainers on one registry produce
merge conflicts on every record unless the work is divided by **file**,
not by unit.

**Divide by reachability, not by topic.** What one maintainer's container
can fetch and the other's cannot is the only division that both halves
can act on independently.

**Do not rewrite another maintainer's evidence.** A record is a
signature. Narrow your own leaking patterns; report theirs.

**When a letter says "waiting for your word", the next thing sent is
either that word or a new letter saying why you proceeded.** Not work. A
promise that does not hold is decoration, not a mechanism.

**Both maintainers find the same defect independently, often within an
hour.** This happened repeatedly. It is not waste — the second finding
usually has the sharper formulation, and having two is how the
formulation improves.

---

## 26. What to do next, in order

For whoever picks this up.

**1. Finish the language migration.** 41 files, of which ~31 are tools
and ~10 are reports that follow from their tools. Translating a tool has
found something wrong in *every single case*: a stale pattern, a
hardcoded per-book fact, a silent zero, a copy of somebody else's list.
Treat it as an audit that happens to leave English behind.

**2. Land the remaining wave survivors and run another wave.** The queue
is 1715 units and 88 % of them carry a checkable signal. The triage
strategy measured better; use it.

**3. Retire the "not a claim at all" units.** Roughly an eighth of the
largest status is not claims — column headings, list lead-ins, rows of
tables in which the book describes its own registry. There is no verdict
for this and no tool distinguishes "not checked" from "not a claim". That
is the cheapest large win available: those units can be retired outright
rather than researched.

**4. Build the fourth layer: book against book.** Designed, never built.
Some of the worst errors found were internal contradictions between
chapters, and nothing looks for them.

**5. Decide what number the book publishes.** Not coverage. What was read
in full, plus the sampled error rate with its bound. This is a decision,
not a measurement, and it should be made before the next book starts
rather than after.

---

## 27. How this project works, as a practice

The habits that produced everything above, worth copying before any of
the specific findings.

**Measure before claiming, and name the measure.** Every number in this
file has a command behind it. A claim without one is an impression.

**When a check disagrees with expectation by an order of magnitude, the
check is broken until proven otherwise.** This rule caught four false
reports in one week.

**Report the failure with the number, not the intention.** A comment
reading "this nearly caused an announcement that sixteen per cent of the
registry was false" is worth more than any amount of care taken
afterwards.

**Write the reason beside the code, not in a document.** Nearly every
long comment in these tools is a case history: what was tried, what it
cost, why the current shape. The documents distil; the code remembers.

**Demonstrate every check against a corrupted input.** A check that has
never fired is indistinguishable from one that is not there.

**Prefer a mechanism to a rule, and a stated mechanism to a silent one.**
A prohibition does not restrain an action cheaper than the work. But a
mechanism nobody knows about does not deter either: what holds is a
mechanism that is *stated*.

**Say what a measure does not measure.** Silence reads as zero.

**When you are about to substitute across many files, enumerate
instead.** List every occurrence, judge each. Substitution has broken
this project more often than any other single action.

**Fix the cause, not the instance.** Repairing data while leaving the
tool that corrupted it is postponement.

**And the one that recurs most.** Before asking how a claim is known, ask
what it is about. Before asking whether a check passed, ask whether it
looked at anything.
