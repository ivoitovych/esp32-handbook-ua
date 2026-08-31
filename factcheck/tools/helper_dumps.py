#!/usr/bin/env python3
"""Reading helper dumps, resilient to the usual ways YAML breaks.

## Why a reader of its own

In one evening broken files ate helpers' work **three times**, and not
once through a helper's carelessness. YAML breaks on ordinary Ukrainian
prose:

    chomu: не твердження: самоопис книги
                        ^ a second colon — and the file will not parse

    chomu: "Simulation is not reality" reflects ...
           ^ the value starts with a quote — an unterminated string

Both lines were written not by a model but by **the maintainer's own
briefing**: they stood there verbatim. So the format demanded of the
helper a knowledge of YAML that nobody had asked of it.

The briefing needed fixing, and it is fixed. But a briefing is a request,
not a gate: sooner or later the next wave of helpers writes a colon in a
sentence. Hence this reader.

## What it does, and what it will not do

It performs exactly one mechanical transformation: if a line looks like
`  key: value`, and the value breaks YAML (contains `: `, or starts with
a quote, `[`, `{`, `&`, `*`), the value is single-quoted, with inner
quotes doubled.

**It does not**: guess missing fields, splice truncated records, or infer
intent. Only what is already written can be repaired; anything else is
invention, and invention is precisely what we are here to prevent.

If a file still will not parse after repair, it is **named individually
and skipped**, not allowed to kill the run: losing one file is losing one
file, not twenty.

## Why the repair is not silent

Repaired files come back as their own list. A silent repair would mean
nobody ever learns how many dumps were malformed — and that is testimony
about the quality of the briefing, which we need.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

# `  key: rest of line`. The key carries no spaces and no quotes; anything
# else is no longer a simple pair, and touching it would be unsafe.
RE_PAIR = re.compile(r"^(\s*(?:- )?)([A-Za-z_][\w-]*): (\S.*)$")

# The indicator of a block scalar: `|`, `>` and their variants with an
# indentation digit and a chomping sign. This is **not** a broken value
# but the most correct way to write a quote, and exactly what we ask
# helpers for.
RE_BLOCK = re.compile(r"^[|>][+-]?\d*$")


def breaks_yaml(value: str) -> bool:
    """Values YAML will read as something other than text.

    A colon followed by a space turns the line into a nested mapping; a
    leading quote starts a quoted string that is almost certainly never
    closed; brackets start a flow collection."""
    v = value.strip()
    if not v or RE_BLOCK.match(v):
        return False
    if v[0] in "\"'[{&*!%@`":
        return True
    return ": " in v or v.endswith(":")


def indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def repair(text: str) -> str:
    """Quote the values that break parsing. Line positions are preserved.

    **The body of a block scalar is not touched at all.** The first
    version of this function did not know that and quoted the indicator
    itself: `cytata: |` became `cytata: '|'`, after which the lines of the
    quote stopped being a quote and began to parse as fields. A file that
    had one fault before the "repair" would not parse at all after it.

    So the repair damaged five of a helper's answers, and in the report
    that looked like the helper's carelessness. Hence the rule: inside a
    block, not one character changes.
    """
    out: list[str] = []
    block_indent: int | None = None
    for line in text.split("\n"):
        if block_indent is not None:
            # A block continues while the line is empty or more indented.
            if not line.strip() or indent(line) > block_indent:
                out.append(line)
                continue
            block_indent = None

        m = RE_PAIR.match(line)
        if m and RE_BLOCK.match(m.group(3).strip()):
            block_indent = indent(line)
            out.append(line)
            continue
        if m and breaks_yaml(m.group(3)):
            value = m.group(3).rstrip()
            out.append(f"{m.group(1)}{m.group(2)}: "
                       f"'{value.replace(chr(39), chr(39) * 2)}'")
        else:
            out.append(line)
    return "\n".join(out)


def read_dir(directory: Path) -> tuple[list[dict], list[str], list[str]]:
    """Every record in a directory of dumps.

    Returns `(records, repaired, broken)`. Each record gets a `_fayl`
    field saying which file it came from — without it the spread between
    helpers cannot be counted, and that spread is the main quantity here.
    """
    records: list[dict] = []
    repaired: list[str] = []
    broken: list[str] = []
    if not directory.exists():
        return records, repaired, broken

    for f in sorted(directory.glob("*.yaml")):
        raw = f.read_text(encoding="utf-8")
        try:
            recs = yaml.safe_load(raw) or []
        except yaml.YAMLError:
            try:
                recs = yaml.safe_load(repair(raw)) or []
                repaired.append(f.name)
            except yaml.YAMLError:
                broken.append(f.name)
                continue
        if not isinstance(recs, list):
            broken.append(f.name)
            continue
        for z in recs:
            if isinstance(z, dict):
                z["_fayl"] = f.stem
                records.append(z)
    return records, repaired, broken
