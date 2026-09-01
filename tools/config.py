#!/usr/bin/env python3
"""What is specific to THIS book — read from data, not written in tools.

## Why

`newbook.py` proves a copy of the technology **runs**. It did not say what
to change so the copy runs on *your* book, and two facts about this book
were spread through the code where nobody would find them:

    GRUPY = ("manual", "kartky", "dodatky", "inserts")   in 8 tools
    "Довідник ESP32"                                     in report.py

The eight copies agreed, which is the dangerous state: a set of copies
does not lie until the fact changes, and then it lies in all of them at
once. And a new book would have found them by grep, on the day it was
in a hurry.

> A thing that differs per book is configuration. Configuration written
> into tools is not configuration — it is eight identical decisions
> waiting to disagree.

So: one file of data, `factcheck/book.yaml`, and one module that reads it.
Changing books is an edit to data.

## Deliberately loud when missing

No silent defaults. A missing or malformed `book.yaml` raises with the
text to write, because a default that quietly works would let a new book
run the whole technology against the wrong directories and report a
confident zero — the defect family this project catalogues more than any
other.

    factcheck/tools/config.py           show the configuration
    factcheck/tools/config.py --demo    demonstration on a broken input
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

from repo import ROOT  # noqa: E402  (root is found, not counted)

FILE = ROOT / "factcheck" / "book.yaml"

TEMPLATE = """# What is specific to this book. The technology reads it; no tool
# repeats it.
title: The book's name, as it should appear in REPORT.md
groups:            # the book's own directories, in reading order
  - manual
"""


class ConfigError(RuntimeError):
    pass


def load(path: Path | None = None) -> dict:
    p = path or FILE
    if not p.exists():
        raise ConfigError(
            f"{p} is missing. The technology cannot know which directories\n"
            f"are this book without being told. Write:\n\n{TEMPLATE}")
    try:
        d = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        raise ConfigError(f"{p} does not parse: {e}") from None
    if not isinstance(d, dict):
        raise ConfigError(f"{p} must be a mapping, not {type(d).__name__}")
    for key in ("title", "groups"):
        if not d.get(key):
            raise ConfigError(f"{p}: `{key}` is missing or empty")
    if not isinstance(d["groups"], list) or \
            not all(isinstance(x, str) for x in d["groups"]):
        raise ConfigError(f"{p}: `groups` must be a list of directory names")
    missing = [g for g in d["groups"] if not (ROOT / g).is_dir()]
    if missing and path is None:
        # Only for a real tree: the demonstration has no directories.
        raise ConfigError(
            f"{p}: `groups` names {missing}, which are not directories of "
            f"this repository. A group that does not exist is silently "
            f"empty, and an empty group reads as a book with no text in it.")
    return d


_d = None


def _cfg() -> dict:
    global _d
    if _d is None:
        _d = load()
    return _d


def title() -> str:
    return _cfg()["title"]


def groups() -> tuple[str, ...]:
    """The book's own directories. Was `GRUPY`, copied into eight tools."""
    return tuple(_cfg()["groups"])


# Where the mirror of the book lives. Nine tools computed this path for
# themselves as `ROOT / "factcheck" / <group>`, and after the cards moved
# into `cards/` every one of them was looking at a directory that no
# longer existed.
#
# `layer1` did not fail. It `continue`d past the missing directory,
# examined ZERO cards, and printed a zero on every line of its report.
# `make check` stayed green for days, asserting that there were no
# discrepancies — because it had found no card in which to look for one.
#
# > A check that found no files and a check that found no faults print
# > the same number.
CARDS = "cards"


def cards_root() -> Path:
    return ROOT / "factcheck" / CARDS


def card_dirs() -> list[Path]:
    """The card directories, parallel to the book's. One definition."""
    return [cards_root() / g for g in groups()]


def demo() -> int:
    import tempfile
    ok = True

    def check(name: str, holds: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if holds else '✗'} {name}: {holds}")
        ok &= holds

    def raises(text: str | None) -> bool:
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "book.yaml"
            if text is not None:
                p.write_text(text, encoding="utf-8")
            try:
                load(p)
                return False
            except ConfigError:
                return True

    check("a missing file is loud", raises(None))
    check("a file that does not parse is loud", raises("title: [unclosed\n"))
    check("a missing title is loud", raises("groups: [manual]\n"))
    check("empty groups is loud", raises("title: x\ngroups: []\n"))
    check("groups as a string is loud", raises("title: x\ngroups: manual\n"))
    check("a sound file loads",
          not raises("title: x\ngroups: [manual]\n"))
    # In a fresh tree there is no book yet, and `book.yaml` deliberately
    # does not load — that IS check 5 in `newbook.py`. The demonstration
    # must SAY SO rather than fall over with a stack trace: a
    # configuration error is not a broken tool, and confusing the two is
    # expensive on the first day of a new book.
    try:
        configured = bool(title()) and bool(groups())
        print(f"   ✓ this tree is configured: {title()}")
    except ConfigError as e:
        configured = None
        print(f"   · this tree is NOT configured yet — expected in a fresh\n"
              f"     copy. Edit factcheck/book.yaml. Reason:\n"
              f"     {str(e).splitlines()[0]}")
    if configured is not None:
        check("this book's own file loads", configured)
        check("the card mirror is where config says",
              cards_root().is_dir() and
              all(d.is_dir() for d in card_dirs()))
    print("\nfailures:", 0 if ok else 1)
    return 0 if ok else 1


def main() -> int:
    if "--demo" in sys.argv:
        return demo()
    try:
        print(f"  title  {title()}")
        print(f"  groups {', '.join(groups())}")
    except ConfigError as e:
        print(f"   ✗ {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
