# Wave w1 — the first randomised measurement of the whole method

> **historical** — a record of a finished wave; not edited, numbers frozen

Ten helpers, twenty tickets each, drawn at random and judged by layer 3.
The first time the technology built on 2026-08-28 — the versioned task
spec, the self-contained card, the English verdict vocabulary — was
measured end to end against a judge that cannot be argued with.

    tools/wave.py --plan DIR --agents 10 --tickets 20 --seed 20260829
    tools/wave.py --judge DIR

    seed            20260829
    order_version   17034152
    pool            469 of 5715 unverified units — those whose candidate
                    document is present in this container's cache
    drawn           200, class mix C 3 · E 43 · F 154
    raw data        factcheck/waves/w1/

The tickets themselves are not stored: `--plan` with that seed and that
`order_version` rebuilds them byte for byte. The answers cannot be
rebuilt, so they are.

## Why the pool is restricted, and why that is not cheating

Egress is an organisation-level `403` on every manufacturer domain. A
ticket whose document is unreachable can only ever come back
`unreachable`, which measures the network and not the method. So the
pool is the units whose document is already on disk. Within that pool
the draw is random and therefore proportional across classes — nothing
was picked for winnability.

## The numbers

    tickets handed out        200
    answers returned          200      (no helper dropped a ticket)
    verdicts                  confirmed 29 · not_found 171
    claimed to have evidence   29
    survived layer 3           15      (52 %)

Seven of ten helpers produced at least one `confirmed`; three produced
none. Per helper: 4 · 0 · 0 · 0 · 1 · 1 · 7 · 4 · 8 · 4. Cost was flat
at roughly 125 000 tokens each, 24–74 tool calls, 2–6 minutes.

**171 of 200 came back `not_found`.** That is the number the method was
built to make cheap and it worked: a helper that cannot support a claim
says so and stops, instead of producing something that reads like
evidence. The honest-miss block earns its place in the spec.

## The fourteen rejected confirmations, read one at a time

Fourteen `confirmed` answers failed the substring test. Every one was
opened by hand — fourteen is small enough that a classifier is worse
than reading.

**All fourteen named a document that exists and is in the cache.** Zero
invented filenames.

**Thirteen of fourteen point at a passage that really is in that
document.** They fail on the copying step, in four shapes:

- *inline markup removed from the middle* — `fatal-errors.rst` has
  ``Print registers and reboot (``CONFIG_ESP_SYSTEM_PANIC_PRINT_REBOOT``)
  — default option``; the helper wrote `Print registers and reboot —
  default option`. Also `idf-monitor.rst` (`esp-idf-monitor_` → the bare
  name), `basic-commands.rst`, `configure-builtin-jtag.rst` (an RST
  hyperlink dropped), `partition-tables.rst` (a `:menuitem:` role
  flattened), `ota.rst` (a `:doc:` role flattened).
- *truncation with a full stop added* — `twai.rst`: 94 of 95 characters
  verbatim, and the sentence in the source continues past where the
  helper ended it.
- *two fragments stitched into one sentence* — `fatal-errors.rst`,
  `basic-commands.rst`: both halves are real and they are not adjacent.
- *a table or comment block re-flowed into prose* —
  `bootloader.rst`: the per-chip offsets exist, as a code comment
  block; the helper wrote them as a semicolon list.

**One of fourteen has no support at all.** `T-A-044`, claim *GPIO 23 →
typical SPI MOSI*, quote `MOSI - 23`, source `spi_master.rst`. The
document defines MOSI and gives IOMUX pins through a substitution
placeholder; the number 23 is not in it. This is the only invention in
two hundred tickets.

> The failure mode is not fabrication. It is tidying — a helper that has
> the passage on screen and writes down what it means rather than what
> it says.

That matches what was found earlier the same day inside our own
registry, where 31 divergences turned out to be markup only, and it
matches the other maintainer's independently measured survival rates of
9/18 and 13/19.

## The obvious fix was measured before it was written, and it is wrong

If most failures are markup, make layer 3 tolerant of markup. That
proposal was run against the whole registry before a line of it was
committed:

    strict (as it stands)     verified 538   not found 72
    tolerant to RST markup    verified 531   not found 79

    would recover    3 records
    would break     10 records

It recovers `partition-tables.rst` — the same passage a helper lost in
this wave — and it costs seven records net.

The mechanism, from `T-05-064`. The source reads

    :cpp:func:`gpio_config` is an all-in-one API that can be used to …

and our quote begins at the backtick: `` `gpio_config` is an all-in-one
API … ``. Today that is a plain substring and passes. A normaliser that
rewrites the *role* `:cpp:func:`…`` as a unit changes the source but not
the quote, because the quote does not contain the role — only its tail.
The two sides normalise differently and the containment is gone.

> `a ⊂ b` does not imply `norm(a) ⊂ norm(b)`. A normaliser that can
> swallow the point where a quote begins cannot be used underneath a
> substring test.

Recorded as defect kind 27. Layer 3 is unchanged.

## What the wave says about the method

- The **spec works as a spec**: 200 of 200 answers came back in the
  requested format, with the requested vocabulary, from a single order
  no maintainer edited afterwards. The one-ticket-at-a-time rule held.
- The **honest miss works**: 171 refusals, and spot-reading them shows
  refusals, not laziness — they name the document they read.
- The **card works**: no helper asked where the claim lived, and no
  answer referred to a book line the ticket had not shown it.
- **Layer 3 is the load-bearing part.** Half of what came back claiming
  evidence would have entered the registry as class `A` on a maintainer's
  reading. It did not, because nothing enters on a reading.
- The remaining loss is a **copying discipline** problem, and it is
  addressable in the order — a rule that says *paste the line including
  its markup, do not clean it* — not in the judge.

## Reproduction

    tools/wave.py --plan <dir> --agents 10 --tickets 20 --seed 20260829
    # answers: factcheck/waves/w1/answers-*.yaml
    tools/wave.py --judge <dir>
