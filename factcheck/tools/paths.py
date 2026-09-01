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

    factcheck/tools/paths.py           check every literal path
    factcheck/tools/paths.py --list    print them all, resolved
    factcheck/tools/paths.py --demo    demonstration on a broken input
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
FC = ROOT / "factcheck"

# `"factcheck" / "a" / "b"`, `FC / "a" / "b"`, or `"tools" / "a"` — however
# many segments.
#
# The `"tools"` arm was added after two tools imported `order_m2.py` from
# `ROOT / "tools"`, where it no longer lives. This check had been reading
# only paths into `factcheck/`, so a path into the OTHER tool directory
# was outside its subject — and both call sites failed at import time,
# days after the move, in tools the gate does not run.
#
# A check scoped to one directory reports about that directory. What it
# leaves out, it leaves out silently.
RE_PATH = re.compile(
    r'(?:"factcheck"|\bFC\b|(?<![\w"])"tools")((?:\s*/\s*"[^"]*")+)')
RE_PART = re.compile(r'"([^"]*)"')

# Demonstration paths: these MUST NOT exist — that is what they show.
# The list is explicit, because a silent pattern-based exemption would
# itself become a hole of the kind this file is written against.
# Both tool directories. The moment the fact-check tools moved into
# `factcheck/tools/`, this file was still globbing `tools/` alone — and
# reported "0 literal paths, 0 broken", which reads exactly like success.
# The defect this file was written to catch, appearing in this file, on
# the first move after it was written.
#
# So the count is not decoration: a run that finds no paths at all is now
# a failure, because it can only mean the check is looking in the wrong
# place.
TOOL_DIRS = ("tools", "factcheck/tools")

# name_lists: not-files
EXEMPT = {
    ("factcheck/tools/language.py", "factcheck/work/snapshots/a.json"),
    ("factcheck/tools/language.py", "factcheck/x.md"),
    ("factcheck/tools/docs.py", "factcheck/GHOST.md"),
}


def demo_spans(text: str) -> list[tuple[int, int]]:
    """Line ranges of demonstration bodies.

    A demonstration builds paths that MUST NOT exist — that is what it
    shows. Listing them in an EXEMPT set here would put a copy of another
    file's strings inside this one, which is the defect `name_lists.py`
    exists to catch. So the exemption is a rule, not a list: whatever a
    function named `demo`/`proba` constructs is a demonstration."""
    import ast
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    return [(n.lineno, n.end_lineno or n.lineno)
            for n in ast.walk(tree)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
            and n.name in {"demo", "proba", "samoperevirka"}]


def literal_paths(source: dict[str, str] | None = None):
    """(tool, path) for every literal path into factcheck/."""
    # This file is not its own subject: it holds deliberately broken
    # demonstration paths. A check that fires on its own demonstration
    # reports about itself, and hides real findings among its own noise.
    # (The same case as the comment in `language.py` that contained the
    # very literal it was describing.)
    files = ({Path(k): v for k, v in source.items()} if source
             else {f: f.read_text(encoding="utf-8")
                   for d in TOOL_DIRS
                   for f in sorted((ROOT / d).glob("*.py"))
                   if f.name != "paths.py"})
    for f, t in files.items():
        spans = demo_spans(t)
        for m in RE_PATH.finditer(t):
            ryadok = t.count("\n", 0, m.start()) + 1
            if any(a <= ryadok <= b for a, b in spans):
                continue
            parts = [x for x in RE_PART.findall(m.group(1)) if x]
            if not parts:
                continue
            # A segment may itself contain a slash: `"queues/x.yaml"`.
            # That is exactly the form that survived both rewrites.
            segments = [c for part in parts for c in part.split("/") if c]
            if any("*" in c or "{" in c for c in segments):
                continue
            try:
                imya = str(f.resolve().relative_to(ROOT))
            except ValueError:
                imya = f.name          # a demonstration input, not a file
            korin = "tools" if m.group(0).lstrip().startswith('"tools"') \
                else "factcheck"
            yield imya, korin + "/" + "/".join(segments)


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
    check("every tool parses under strict warnings", not parses_strictly())
    print("\nfailures:", 0 if ok else 1)
    return 0 if ok else 1


def parses_strictly() -> list[str]:
    """Every tool must parse with SyntaxWarnings as errors.

    Not pedantry. `doc_kind` reads the tools with `ast.parse` to learn
    which tool writes which document, and swallowed failures with a bare
    `continue`. Two tools carrying `\\s` in a docstring stopped parsing
    under strict warnings, so the tool that writes UNREACHABLE-SOURCES.md
    ceased to exist for the check — and a generated document was declared
    canonical, which is the kind error that gets a file edited by hand.

    It happened again while translating `snapshot.py`. Caught by eye the
    second time; this is so there is no third.
    """
    import ast
    import warnings
    problems = []
    for d in TOOL_DIRS:
        for f in sorted((ROOT / d).glob("*.py")):
            with warnings.catch_warnings():
                warnings.simplefilter("error", SyntaxWarning)
                try:
                    ast.parse(f.read_text(encoding="utf-8"))
                except (SyntaxWarning, SyntaxError) as e:
                    problems.append(f"{d}/{f.name}: {e}")
    return problems


def main() -> int:
    if "--demo" in sys.argv:
        return demo()
    if "--list" in sys.argv:
        for tool, s in sorted(set(literal_paths())):
            print(f"  {'OK ' if (ROOT / s).exists() else 'MISSING'}  "
                  f"{tool:<26}{s}")
        return 0
    problems = check_all() + parses_strictly()
    znaydeno = len(set(literal_paths()))
    if not znaydeno:
        print("   ✗ no literal paths found at all — this check is looking "
              "in the wrong place, it is not reporting a clean tree")
        return 1
    for b in problems:
        print(f"   ✗ {b}")
    print(f"\npaths: {len(set(literal_paths()))} literal paths into "
          f"factcheck/ and tools/, "
          f"{len(problems)} broken")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
