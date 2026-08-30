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
    """The nearest ancestor that is a repository root.

    Two markers, tried in order, and neither is a depth:

      `.git`        the repository itself
      `factcheck/`  a tree using this technology, copied without history —
                    which is exactly what `newbook.py` produces

    The second marker exists because the first attempt fell back to
    "two levels up" when no `.git` was found, and that fallback was
    calibrated for tools living at `<root>/tools/`. After they moved to
    `<root>/factcheck/tools/` it returned `<root>/factcheck`, so every
    path became `<root>/factcheck/factcheck/...`.

    `newbook.py` caught it on its first run, because it does not merely
    copy the tree — it runs the copy. That is the whole reason it runs
    the copy.
    """
    p = (start or Path(__file__)).resolve()
    for d in p.parents:
        if (d / ".git").exists():
            return d
    for d in p.parents:
        if (d / "factcheck").is_dir():
            return d
    return p.parent.parent


ROOT = find_root()


# Both directories that hold our code. Each check used to carry its own
# idea of where the tools live, and each was right exactly as long as
# there was one directory. After the split, five of them silently saw 15
# files out of 66 and reported on those as if they were all of it.
#
# Lists that each hold their own copy of one fact are a defect kind of
# their own: they do not lie until the fact changes, and then they lie in
# every copy at once.
TOOL_DIRS = ("tools", "factcheck/tools")


def tool_files():
    """Every .py of ours, from both directories, in a stable order."""
    return sorted((p for d in TOOL_DIRS for p in (ROOT / d).glob("*.py")),
                  key=lambda p: (p.parent.name, p.name))
