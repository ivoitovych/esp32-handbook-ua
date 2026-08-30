#!/usr/bin/env python3
"""Every literal path into `factcheck/` written in a tool must resolve.

## Why

Reorganising `factcheck/` moved directories twice in two days. Each time I
rewrote the path constants with a pattern, and each time the pattern
matched one spelling of the path and missed another:

    "factcheck" / "evidence"          caught by the first sweep
    FC / "evidence"                   missed — a different base
    "factcheck" / "queues/x.yaml"     missed — directory and file in one
                                      string, so the directory name was
                                      not a whole token

Six live constants pointed at directories that no longer existed, and
`make check` was green through all of it, because no gate exercises the
paths a tool would use only when someone runs that tool.

> A broken path is not found by running the checks. It is found by
> running the tool that holds it, and that may be a week later, in the
> middle of a wave, when it writes its output somewhere nobody looks.

So the check does not run the tools. It reads them, extracts every
literal path under `factcheck/`, and asks the filesystem.

## What it cannot do

It sees literals. A path assembled from variables — `katalog / imya` —
is invisible to it, and so is anything built at run time. It measures
**intent written down**, which is the same limit `docs.py`'s root guard
carries, and for the same reason.

    tools/paths.py           check every literal path
    tools/paths.py --list    print them all, resolved
    tools/paths.py --demo    demonstration on a broken input
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
FC = ROOT / "factcheck"

# `"factcheck" / "a" / "b"` or `FC / "a" / "b"`, however many segments.
RE_PATH = re.compile(r'(?:"factcheck"|\bFC\b)((?:\s*/\s*"[^"]*")+)')
RE_PART = re.compile(r'"([^"]*)"')

# Demonstration paths: these MUST NOT exist — that is what they show.
# The list is explicit, because a silent pattern-based exemption would
# itself become a hole of the kind this file is written against.
# name_lists: not-files
EXEMPT = {
    ("tools/language.py", "factcheck/data/snapshots/a.json"),
    ("tools/language.py", "factcheck/x.md"),
    ("tools/docs.py", "factcheck/GHOST.md"),
}


def literal_paths(source: dict[str, str] | None = None):
    """(tool, path) for every literal path into factcheck/."""
    # This file is not its own subject: it holds deliberately broken
    # demonstration paths. A check that fires on its own demonstration
    # reports about itself, and hides real findings among its own noise.
    # (The same case as the comment in `language.py` that contained the
    # very literal it was describing.)
    files = ({Path(k): v for k, v in source.items()} if source
             else {f: f.read_text(encoding="utf-8")
                   for f in sorted((ROOT / "tools").glob("*.py"))
                   if f.name != "paths.py"})
    for f, t in files.items():
        for m in RE_PATH.finditer(t):
            parts = [x for x in RE_PART.findall(m.group(1)) if x]
            if not parts:
                continue
            # A segment may itself contain a slash: `"queues/x.yaml"`.
            # That is exactly the form that survived both rewrites.
            segments = [c for part in parts for c in part.split("/") if c]
            if any("*" in c or "{" in c for c in segments):
                continue
            yield f"tools/{f.name}", "factcheck/" + "/".join(segments)


def check_all(source: dict[str, str] | None = None) -> list[str]:
    problems = []
    for tool, path in literal_paths(source):
        if (tool, path) in EXEMPT:
            continue
        if not (ROOT / path).exists():
            problems.append(f"{tool}: names `{path}`, which does not exist")
    return problems


def demo() -> int:
    ok = True

    def check(name: str, holds: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if holds else '✗'} {name}: {holds}")
        ok &= holds

    check("a broken path is caught",
          bool(check_all({"tools/x.py": 'A = ROOT / "factcheck" / "nemaye"'})))
    check("the other spelling of the same path is caught too",
          bool(check_all({"tools/x.py": 'A = FC / "nemaye"'})))
    check("a directory and file in one string is caught",
          bool(check_all({"tools/x.py": 'A = FC / "queues/nemaye.yaml"'})))
    check("a real path stays quiet",
          not check_all({"tools/x.py": 'A = FC / "METHOD.md"'}))
    check("a glob is not checked",
          not check_all({"tools/x.py": 'A = FC / "*.md"'}))
    print("\nfailures:", 0 if ok else 1)
    return 0 if ok else 1


def main() -> int:
    if "--demo" in sys.argv:
        return demo()
    if "--list" in sys.argv:
        for tool, s in sorted(set(literal_paths())):
            print(f"  {'OK ' if (ROOT / s).exists() else 'MISSING'}  "
                  f"{tool:<26}{s}")
        return 0
    problems = check_all()
    for b in problems:
        print(f"   ✗ {b}")
    print(f"\npaths: {len(set(literal_paths()))} literal paths into factcheck/, "
          f"{len(problems)} broken")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
