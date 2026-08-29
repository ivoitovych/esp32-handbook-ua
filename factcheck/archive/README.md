# Archive — kept, not deleted

> **historical** — records the state on its own date; nothing here is edited

Spent work: finished waves, run output, orders that have been carried out,
and registries whose numbers are frozen. It is here so that no measurement
we have ever reported loses the evidence it was made from.

    history/   8 frozen registries — the numbers behind past reports
    runs/      11 run directories and their orders: waves, trials,
               experiments, the pass and pass-rejected sets
    orders/    orders already carried out

## Two rules, and the reason for each

**Nothing is deleted.** The alternative was proposed and rejected: I had
suggested deleting the spent trial output, and the owner said to archive
it instead. That is the right call. `trial-100` and `trial-100b` are a
paired experiment — the same units under two different work orders — and
the pair is the only reason either number means anything. Deleting the
data would leave the conclusion standing with nothing under it.

**Nothing here is translated or renamed.** The technology migrates to
English; this directory does not follow, for the same reason the letters
and the binding snapshots do not:

> A record edited to today's names testifies about today and lies about
> its date.

So `NARYAD-m2-hvylya3.md` keeps its name, and the Ukrainian prose in
`trial-100/f-07.md` stays Ukrainian. `tools/language.py` and
`tools/naming.py` both skip this directory by rule, not by oversight.

## What is still live

`factcheck/runs/` is where the **next** run writes. It is empty by design.
If it fills up again with finished waves, they belong here.

## Reading an archived run

Paired sampling still works against it — `--z-pereliku` takes an explicit
path, so an order can be paired with an archived run by pointing at it:

    tools/work_orders_f.py --z-pereliku factcheck/archive/runs/trial-100/…

The run ledger in `reports/RUNS.md` joins results to their order version
and references no paths, so archiving changed nothing it records.
