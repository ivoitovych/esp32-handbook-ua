#!/usr/bin/env python3
"""Is a file of the book itself sitting in the source cache?

## The defect

A file of the book that ends up in the cache makes a self-reference
**invisible to all three layers**:

* the source names a file from the cache — the gate is satisfied;
* the quote stands verbatim in that file — layer 3 is satisfied;
* the pattern matches a unit — layer 1 is satisfied.

And the evidence proves the book by the book.

## What it cost

2026-08-28: **seven files of the book** were found in the cache, byte for
byte. They were put there by the wave of 27 August, when helpers were
first allowed to download sources themselves: a helper "downloaded" a
file of the book.

The number of evidences resting on them was **zero** — the mine did not
go off. But the gates could not see it, and could not have: by
construction they ask "is the source in the cache", not "is the source
the book".

## And the manifest, separately

Checking the files alone is not enough. **The manifest itself can
register the book as a source**: a line whose address is
`raw.githubusercontent.com/<owner>/<book>/main/manual/…` registers the
book as an external source officially. Then every re-download restores
the file, and removing it from the cache does not hold.

Found 2026-08-28: eight such lines. At first I deleted the seven files
and considered the fault closed; the next download brought four back,
because the addresses were still in the manifest. **Removing an effect
while leaving its cause is not a fix, it is a delay.**

## Why by content, not by name

A name can be changed. The check compares the **sha256 of the content**,
so a copy under another name is found too.

## And why not by the files on disk alone

The first version looked only in the cache directory. The files were
removed from it — and it reported zero, while **four manifest lines went
on naming the book as a source**:

    | `20-bekap.md` | … | <https://raw.githubusercontent.com/
                          owner/book/main/manual/20-bekap.md> |

The manifest is what goes into git and what a third party sees; the files
do not travel at all. So the check was reporting "clean" about exactly
the side that goes nowhere, and staying silent about the side that goes.

> Kind 3 from the catalogue, committed by the check itself: the counter
> counted the wrong artefact. The sign is the same — a zero that means
> nothing.

So both sides are checked: the content of the files **and** the addresses
in the manifest.

    factcheck/tools/cache_vs_book.py [--quiet]
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
CACHE = ROOT / "factcheck" / "source-cache"

# A ninth copy of the book's directories lived here under another name,
# and the sweep that replaced the eight `GRUPY` copies did not see it —
# a list is not found by the name of the fact it holds. From `book.yaml`
# now, like the rest.
BOOK = config.groups()

# The book's own address. A handbook is not a source for itself — the
# same rule that already stands in a helper's work order.
#
# It used to name THIS repository literally, which on another book would
# have matched nothing and reported a confident zero. Derived from the
# git remote, with the config title as a fallback for a tree that has no
# remote (`newbook.py` produces exactly that).
def _own_names() -> re.Pattern:
    import subprocess
    parts = []
    try:
        r = subprocess.run(["git", "remote", "get-url", "origin"],
                           capture_output=True, text=True, cwd=ROOT)
        if r.returncode == 0:
            parts += [x for x in re.split(r"[/:.]", r.stdout.strip())
                      if len(x) > 3 and x not in ("github", "com", "git")]
    except Exception:
        pass
    parts.append(ROOT.name)
    return re.compile("|".join(re.escape(x) for x in dict.fromkeys(parts)),
                      re.I)


OWN = _own_names()

# The book's path in any repository: a fork under another owner has the
# same directories.
BY_PATH = re.compile(r"/(?:%s)/" % "|".join(BOOK))


def main(argv: list[str]) -> int:
    quiet = "--quiet" in argv
    prints: dict[str, str] = {}
    for g in BOOK:
        directory = ROOT / g
        if not directory.exists():
            continue
        for p in directory.glob("*.md"):
            prints[hashlib.sha256(p.read_bytes()).hexdigest()] = str(
                p.relative_to(ROOT))

    # The manifest: an address pointing at our own book registers it as a
    # source.
    manifest = CACHE / "MANIFEST.md"
    _manifest_rows = []
    if manifest.exists():
        tekst = manifest.read_text(encoding="utf-8")
        for ln in tekst.split("\n"):
            if re.search(r"raw\.githubusercontent\.com/[^/]+/[^/]+/"
                         r"\S*/(?:%s)/" % "|".join(BOOK), ln):
                m = re.search(r"\| `([^`]+)` \|", ln)
                _manifest_rows.append(m.group(1) if m else ln[:60])

    found = []
    n = 0
    if CACHE.exists():
        for p in sorted(CACHE.iterdir()):
            if not p.is_file():
                continue
            n += 1
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            if h in prints:
                found.append((p.name, prints[h]))

    # The manifest is the only part of the cache that reaches git. A
    # self-reference in it survives deleting the file and **restores it**
    # on the next download: the cause lives here, the effect in the
    # directory.
    #
    # Two signs, because both maintainers wrote this check independently
    # and each missed what the other saw:
    #
    #   by path  — `…/manual/…` in any repository; catches a fork under
    #              somebody else's owner name;
    #   by name  — our own repository's name; catches an address outside
    #              `raw.githubusercontent`, say a release or `docs/`.
    #
    # Neither alone covers both cases.
    in_manifest = []
    manifest = CACHE / "MANIFEST.md"
    if manifest.exists():
        for ln in manifest.read_text(encoding="utf-8").split("\n"):
            if not ln.startswith("| `"):
                continue
            m = re.search(r"<([^>]+)>", ln)
            url = m.group(1) if m else ""
            if BY_PATH.search(url) or OWN.search(url):
                name = re.search(r"\| `([^`]+)` \|", ln)
                in_manifest.append((name.group(1) if name else ln[:60], url))

    for name, source in found:
        print("   ✗ a file of the book is in the source cache: "
              "%s = %s" % (name, source))
    for name, url in in_manifest:
        print("   ✗ the manifest registers the book as a source: "
              "%s → %s" % (name, url))
    if not quiet or found or in_manifest:
        print("cache_vs_book: files in the cache %d; files of the book "
              "among them %d; manifest rows naming the book %d"
              % (n, len(found), len(in_manifest)))
    return 1 if (found or in_manifest) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
