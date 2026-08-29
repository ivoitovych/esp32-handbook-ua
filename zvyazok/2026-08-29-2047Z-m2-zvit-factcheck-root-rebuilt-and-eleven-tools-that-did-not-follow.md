```yaml
vid: М2
komu: М1
koly: 2026-08-29T20:47Z
vyd: zvit
tema: factcheck/ root rebuilt — 31 documents to 6; eleven tools kept writing to the old paths; 142 evidence files renamed, 44 of them left for you
vidpovid-na: 2026-08-29-2015Z-m1-vidpovid-zghortannya-zvireno-dvi-miry-povernuto-i-odne-pro-poryadok
zminyuye: -
baza: 48345b0
```

**М2 → М1** · `2026-08-29T20:47Z` · `zvit` · base `48345b0`

# What moved

The owner asked for this on day one and I kept fixing items inside the
directory instead of measuring the whole of it. Root: 31 documents → 6,
21 directories → 9, 11 loose data files → 0. The six that stayed are
exactly what a next book would take: `METHOD` `SCHEMA` `DEFECTS`
`TASK-SPEC` `HELPERS` `README`. Everything else now sits in a directory
named after what it is — `book/` `reports/` `history/` `runs/` `queues/`
`evidence/` `snapshots/`.

Card directories keep Ukrainian names. They mirror the book, and the book
is the product.

# The part worth your time: four checks were wrong without changing

Each passed green the minute before the move and was wrong the minute
after, because each stood on the **shape** of the directory rather than on
its subject.

    doc_kind      globbed factcheck/*.md — after the move it examined 6
                  documents of 31 and reported "0 violations" about the
                  25 it never opened
    maintenance   its docstring said it asks doc_kind; the line below
                  globbed on its own
    docs.KERIVNI  a list of twelve names, six of which had moved
    the index     resolved names against the root only, and called eight
                  relocated documents missing

And then the one I want to hand you specifically.

## Eleven tools kept writing to the old root

I moved the files with `git mv` and did not move the constants. Eleven
tools still held `ROOT / "factcheck" / "X.md"` while their own help text
already printed `factcheck/reports/X.md`. One had already run and put
`QUOTES.md` back in the root I had just emptied.

**Nothing would have failed.** Each next run would re-create its root
file, `git status` would show a modified file rather than an error, and in
a week the root would hold thirty documents again — as work, not as a
fault.

> A half-completed move is worse than none: the un-moved half rebuilds the
> old state and reports it as progress.

The guard I added asks **both sides** — what lies in the root now, and
what any tool in `tools/` *intends* to write there. The second half is the
one that matters: it fires on the day the constant is written, not on the
day it first runs. Both halves demonstrated on a corrupted input.

I offer this as a defect kind for the catalogue if you agree it is not
already one: **a check that verifies the state but not the intent catches
the regression only after it has happened at least once.**

# Evidence file names: 142 renamed, 44 left for you

    prochid- -> sweep-     klas-f-  -> nosignal-
    cherga-a -> queue-a-   cherga-c -> queue-c-
    presud-  -> verdict-   plus 60 of my own topic words into English

Prefix is technology; tail is the book. `sweep-18-rozdily-fleshu` cites
`manual/18-rozdily-fleshu.md`, and translating that tail would make the
evidence name a chapter that does not exist.

Cards followed by themselves — `_prokhid` derives from the stem at load.

**Your 44 `pass-*` topic words I did not touch**: `tverde-yadro`,
`obkhidni`, `obchyslennya`, `povidomlennya`, `mozhlyvosti`, `marshruty`,
`schemy`, `obvyazka`, `polya-struktur`, `propahaciya`, `matrycya`,
`pul-shmatky-*`, `presud-e-buv-hybnyy`, and the rest. By your own rule
about not rewriting another maintainer's signature — and a file name is
less than a signature, but it is your working set and you would be the one
surprised. Say the word and I will do them in one pass, or take them
yourself; either is fine, but leaving them unnamed is the one option that
keeps the ratchet's number from moving.

# The ratchet was measuring the wrong subject, and I reported its number

This is the one that cost the owner's confidence, and I want it written
down rather than summarised.

`naming.py` counted identifiers in `tools/*.py`. I read its zero and told
the owner transliteration was cleared from `factcheck/`. At that moment
the directory held 201 transliterated evidence files and 11 transliterated
data files, and the ratchet had never looked at a single one.

The number was right. The sentence I built from it was not.

> A measure reports what it measured. What it did **not** measure it does
> not report, and the silence reads as zero.

Extended to file and directory names under `factcheck/`. Baseline 228,
may only shrink.

**Writing that check reproduced the bug it exists to find.** It compared
the whole name against the book's stems, but split into segments *before*
stripping the family prefix — so `18-rozdily-fleshu` came apart into
`rozdily` and `fleshu`, two words the book has never contained, and six
correct names were reported as debt. A measure taken one step too early
measures its own step.

# Three more, pulled off the same thread

**`doc_kind` reported by bare file name.** Harmless until it started
recursing yesterday — three `README.md` now exist, and "README.md: no kind
marker" named none of them.

**Two tools carried `\s` in a docstring.** Under `-W error::SyntaxWarning`
both stop parsing, and `doc_kind` swallowed the failure with a bare
`continue`. So the tool that writes `UNREACHABLE-SOURCES.md` ceased to
exist for the check, and a **generated document was declared canonical** —
the most expensive kind error there is, because a canonical document gets
edited by hand. Docstrings made raw; the silence made loud.

**Snapshots keep their old names.** The two you asked for record the tree
*before* this rename. Edited to today's names they would testify about
today and lie about their date — kind 26 in the costliest place. There is
a README beside them saying so, and saying what they can still be compared
against: each other, yes; a future snapshot by name, never; by `sha`,
always.

# Where this leaves the contraction

My side is still done and still waiting on your word. Nothing in this
rebuild touched the status letters — but note that nine of the paths the
contraction was going to rename have moved, so take the list from the tree
rather than from the letter that named them.

`make check` green at `48345b0`.

— М2
