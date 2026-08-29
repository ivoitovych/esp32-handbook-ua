# Lessons of maintainer M2: what cost most, and what the code does not show

> **historical** — a record of a finished wave; not edited, numbers frozen

This is the record of one maintainer's own failures on this project.
The general method lives in `METHOD.md`; the catalogue of defect kinds
lives in `DEFECTS.md`. This file exists because the two of those state
rules, and rules are cheap to read and expensive to learn.

The section on my own failures is deliberately longer than the section
on findings about the book. That proportion is honest: I found more
faults in my own checking than in the text I was checking.

---

## I. The four incidents of one shape

Each of these is the same defect wearing different clothes: **a check
that looks at a neighbouring field, runs cleanly, and stays silent.**

**Nearly destroyed 124 valid records.** My "faster" audit searched the
book's text where it should have searched the registry, and reported
182 idle patterns against the other maintainer's 58. What stopped me
was the size of the disagreement, not understanding. Reverted from git.

**Built patterns from the record's own title.** The title is my
signature under the evidence, not the book's words; it can match the
registry only by accident. Sixteen new idle patterns, created the same
day I was repairing forty-four old ones.

**Filtered verdicts by my own heading.** I audited "excessive `E`" by
selecting records whose *title* contained a number with a unit. The
signal lives in the **book's text**. The correct denominator was 84;
my filter selected 45 and I reviewed 24 of them — and missed both
verdicts the other maintainer later proved false.

**Matched documents by the unit's text when the document was already
named.** A handover arrived with the document named in its own field; my
matcher looked at the claim text instead and reported 28 workable units
out of 227. The true number was 184. I almost reported the queue as
nearly impossible.

> The rule, written after the third and violated the same day:
> **a check that filters on a field the maintainer writes measures the
> maintainer, not the subject.**

---

## II. Duplicated work I did not check for

**Rewrote ~570 lines of tooling** that already existed on the other
branch, because I never ran `git ls-tree` before starting.

**Diagnosed 51 discrepancies wrongly** by asserting PDF table artefacts
without looking at the data. The sources were `.rst`, `.h` and `.py` —
no PDFs at all.

**Read the other maintainer's document instead of his code** and sent
him, as a delta, a normalisation he already had.

---

## III. Fabrication of my own

**Seven "verbatim" quotes assembled by hand** from table cells: I
merged columns, invented alignment, added labels (`Typ`, `Min`, `Max`,
a `LEAD-FREE` heading, an `(SAC305)` tag) that appear nowhere in the
document — and filed them as verbatim quotes. Exactly what I was
catching helpers doing.

The worst example: three lines about power domains labelled
`Typ 40 mA` under a current-drive record. No such lines exist. The real
extract reads `IOH VOH >= 2.64 V, — 40 — mA`, and 40 mA is not a
typical value but the maximum at full drive strength.

Rewritten cell by cell a day later. Each record now carries a note
saying what was invented in the previous version — erasing the trace of
a fault would have been a second fault.

---

## IV. Repeating a mistake after reading its description

**Capital letter in a pattern**, one hour after the other maintainer
reported the same. Mine was worse: the first alternative matched, so
the dead one was invisible to every audit.

**A blacklist of phrasings instead of a positive test.** I wrote the
rule "check whether a file exists, do not judge by how a phrase sounds"
in the morning, and by evening had built a category called "sounds
invented" that flagged seven document names — of which three were real
documents named in prose.

**Cyrillic letters inside a Latin filename slug.** Two of my letters
were invisible to the correspondence protocol for a day, because the
name matcher accepts `[a-z0-9-]` and my typo put `р` and `явся` in the
middle of otherwise Latin words. One of them was a significant finding.

---

## V. Where a design choice had a price I should have named

**`unsorted` as the cheapest answer.** I made "did not work it out"
the cheapest verdict on purpose, so that laziness would produce an
honest "I don't know" rather than a judgement. The goal was reached:
zero fabrications in 3221 accepted records.

The price took two random samples of 100 to see: **87 % and 85 %** of
that class were ordinary author's judgements that any helper could have
classified without effort.

> A cheapest answer that asserts nothing collects not only the genuinely
> doubtful but everything attention ran out on. It saves you from
> untruth and does **not** save you from carelessness — carelessness
> merely becomes visible and cheap to sort.

---

## VI. Two things I got right, recorded because rules need evidence

**Requiring a reason on the asserting verdict.** The class that claims
"no external source exists" must carry a one-line justification; the
class that claims nothing must not. Held twice on other people's data:
931 of 931, then 45 of 45.

**Random draw over hand-picked sampling.** A `sort -R` sample of 100
found a *repetition* of a defect I had already reported elsewhere and
predicted would recur — in a table nobody would have thought to open.
The prediction was confirmed by a sample that knew nothing about it.

---

## VII. Discipline that came out of all this

- **Checking goes before acceptance, not after.**
- **One owner per file.** I once overwrote the other maintainer's work
  order with a tool that wrote silently to a fixed name.
- **The work order lives in the repository, not in `/tmp`.**
- **The cache and the matcher are one thing in two places.**
- **Do not ask for a justification where you can check mechanically.**
  Requiring a reason for "this is not a claim" produced 23 rejections
  in the first hundred, all identical, all pointless.
- **Record the sample, not only the result.** Three experiments used
  `sort -R` with no recorded seed and cannot be redrawn by anyone.
