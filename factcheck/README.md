# `factcheck/`

> **canonical** — the decision lives here; there are to be no copies

Two documents, and everything they are about.

    METHOD.md   the technology — three layers, the laws of a work order,
                gates, sources, measurement. Not about ESP32; this is the
                part that lifts onto another book.

    REPORT.md   the fact-check of *this* book: how much is checked,
                against what, what is left. Generated — `tools/report.py`.

Read `METHOD.md` if you want the method. Read `REPORT.md` if you want the
state. Nothing else here needs opening to understand either.

## Everything else

    source-cache/  the source documents themselves, as downloaded.
                   **Not in git** — a local arrangement, ignored by
                   `factcheck/.gitignore`. `MANIFEST.md` IS in git: URL,
                   name, size, sha256, date, for every file. That line is
                   the reproducibility record, and it weighs kilobytes
                   against the cache's 136 MB.

    data/          what the tools read and write: the evidence records,
                   the cards that mirror the book, the working queues,
                   and the generated reports behind `REPORT.md`.

    archive/       spent work. Nothing here is deleted, translated or
                   renamed — a record edited to today's names testifies
                   about today and lies about its date.

## Why the directory looks like this

It held thirty-one documents and twenty-one directories, nine of them the
same kind of thing. The owner called it a rubbish bin and was right twice:
once when he said it, and again days later when he saw nothing had
changed.

Then it was cut too far the other way — six documents to two, everything
else swept into one directory called `data`, which named nothing. This is
the correction: the root shows what a person needs, and hides only what
they do not.

> The root of `factcheck/` holds what a reader needs to orient, and what
> travels to another book. Everything else lives in a directory named
> after what it is.

Three ratchets hold that. `tools/doc_kind.py` checks each document's kind
marker against whether a tool actually writes it, in both directions.
`tools/language.py` checks that the technology is in English and the book
is not. `tools/docs.py` refuses anything in this root that is not one of
the two documents — including a tool that merely *intends* to write here.

## The book itself is not here

`manual/`, `dodatky/`, `kartky/` and `inserts/` exist twice on purpose: at
the repository root they are the book, and under `data/` they are the
cards that mirror it, one file to one file. The card names stay Ukrainian
because they cite the book, and the book is the product.
