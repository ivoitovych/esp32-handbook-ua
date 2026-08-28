# The worker task — one definition, versioned

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

## [ORIENTATION] Where you are in this

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

## [HONEST-MISS] "I looked and did not find it" is a complete answer

It is not a failure and not a lesser result. It records where we have
already looked, and those records are what let us print a sentence at
all.

A quote from an almost-right source is worse than no quote. Invented
support does not go unnoticed — layer 2 discards it and the unit returns
to the queue — so guessing is cheaper than reading only inside your own
answer. Past that boundary it costs everyone, and you most: your work
disappears entirely.

## [VERBATIM] Copy, do not retell

Everything in `quote` is checked as a substring of the document. A
retelling does not pass. Neither does a line you assembled by hand from
a table, nor two sentences joined across an ellipsis.

**Knowing the answer is not grounds for writing a quote.** If the fact is
familiar but you cannot see the line in the document, that is
`not_found`.

## [NETWORK] What is reachable from here

Only `raw.githubusercontent.com`, via `curl`. Everything else answers
`403` — this is an organisation-level policy, not your doing and not
ours. Chip datasheets are not on GitHub, and that is nobody's fault.

**Do not repeat a request that returned 403.**

## [STUB] A 200 that is not a document

Some `espressif.com` addresses return an **HTML placeholder of about
15 500 bytes with status 200**. The request "succeeds" and there is no
document. If what came back does not look like the document you asked
for, the verdict is `unreachable`.

## [NO-SELF-REFERENCE] The handbook cannot be its own source

An address inside this repository, or a chapter of the handbook cited as
the source for a claim in the handbook, is rejected mechanically. If a
claim is supported only by another part of the book, say so plainly —
there is a class for it, and it is not a failure.

## [VERDICTS-EXTERNAL] The verdicts for finding an external source

| Verdict | When |
|---|---|
| `confirmed` | address plus a **verbatim** quote from the document |
| `not_found` | the document exists, the passage is not in it — say what you read |
| `unreachable` | the document does not come down from here (403, 404, stub) |
| `advice` | you did not get the document, but can name where it would be |
| `disputes` | the source **contradicts** the handbook — the most valuable answer there is |

## [VERDICTS-VERDICT-TEST] The verdicts for testing an existing verdict

Used when the unit already carries a class and the question is whether
that class is right.

| Verdict | When |
|---|---|
| `confirmed` | the existing class is correct |
| `disputes` | the source contradicts the handbook |
| `truly_none` | there really is no external referent: this is the author's position |
| `not_found` | you could not tell — say what you read |

## [ABSENCE] Proving something by what a document does not say

Sometimes the proof is a silence: `SOC_BT_SUPPORTED` does not appear in
`esp32s2/soc_caps.h`, and that is what shows the S2 has no Bluetooth.

This is a real answer with its own verdict, `absent_from_source`. It
needs the document, the exact string that is **missing**, and — where one
exists — a `control`: a document of the same kind where that string **is**
present. Silence proves something only where a comparable document
speaks.

It is **not** `not_found`. `not_found` says you could not establish the
claim; this says you established it, and the document's silence is how.

## [FORMAT] How to answer

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
