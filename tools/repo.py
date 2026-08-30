#!/usr/bin/env python3
"""Where the repository root is — found, not counted.

Every tool used to write this:

    ROOT = Path(__file__).resolve().parent.parent

which is not a location but an **assumption about depth**. It was true
while every tool sat exactly one directory below the root, and it became
false the moment any of them moved. Nothing would have raised: `ROOT`
would simply have become `factcheck/`, every path under it would have
resolved, and files would have been written one directory away from where
anything looks for them.

This is the same defect that has now surfaced five times in this project
in three days, each time in a different file:

    doc_kind.dokumenty        globbed one level, saw 6 documents of 31
    docs.index_complete       resolved names at the root only
    name_lists.isnuye         the same, and called 9 existing files missing
    naming.imena_faylivv      split a name before stripping its prefix
    task_spec.RE_BLOK         ended a block at end-of-file, ate 823 lines

Every one is a shape assumed instead of asked for. So the fix is not to
change `parent.parent` to `parent.parent.parent` when the tools move one
level deeper — that would carry the assumption along, one notch quieter.
The fix is to stop assuming: walk up until the directory that contains
`.git`, which is the actual definition of "the repository root".

A tool that imports this works at any depth, and moving it is no longer
an edit to it.
"""
from __future__ import annotations

from pathlib import Path


def find_root(start: Path | None = None) -> Path:
    """The nearest ancestor containing `.git`.

    Falls back to two levels up — the old assumption — only if no `.git`
    is found at all, which happens when the tree is copied without its
    history (`newbook.py` does exactly that). The fallback is named here
    rather than left implicit, because a silent wrong root is the whole
    failure this module exists to prevent."""
    p = (start or Path(__file__)).resolve()
    for d in p.parents:
        if (d / ".git").exists():
            return d
    return p.parent.parent


ROOT = find_root()
