#!/usr/bin/env python3
"""Consistency gate over the foundation documents.

## Why this exists

The owner's complaint, measured and confirmed: *"the technology keeps
drifting — we find new classes of problem and forget the ones already
found."*

On 2026-08-28 the class vocabulary lived in **three** documents and all
three had drifted apart; the two newest classes were missing from both
non-authoritative copies. That was found by reading. Reading does not
scale and does not run in CI.

Two answers were considered and rejected:

* **merge every document into one.** A three-thousand-line file is not
  re-read whole by anybody, so drift stops being visible instead of
  stopping.
* **move content between documents on a fixed cadence.** That is a
  discipline, and this project's own law says disciplines do not hold:
  *stated mechanics hold, a named prohibition does not.* A cadence is a
  prohibition against drift.

What holds is a check. This is the check.

## What it verifies

    vocabulary   every class letter a document names must exist in the
                 code, and every code class must appear in the
                 authoritative document
    tools        every `tools/*.py` a document names must exist
    verdicts     every verdict a work-order template offers must be one
                 the intake gate knows how to check
    defects      every defect kind referenced by number must exist

## What it deliberately does NOT verify

Prose. Two documents may explain the same idea in different words and
that is not drift — `HELPERS.md` is the raw log and `METHOD.md` is
the distilled law, and both say so in their first lines. Only **facts
with one right answer** are checked here.

    factcheck/tools/docs.py            check
    factcheck/tools/docs.py --demo    show the check working on broken input
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import repo
from repo import ROOT  # noqa: E402  (root is found, not counted)
FC = ROOT / "factcheck"
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Who is authoritative for which fact. Without this line people "fix the
# copy they happen to be reading", and the copies drift further apart.
#
# Until recently there were three different documents here, one owner per
# question. After the consolidation two of the three are the same
# `METHOD.md`, and `name_lists` rightly complained about the duplicate: a
# repeated name in a list like this almost always means a substitution
# collapsed two entries into one (kind 26).
#
# Here it is not a collapse but a genuine consolidation: the owner really
# is one. So instead of two identical values there is one entry, and the
# code asks it twice.
OWNER = {
    "technology": "METHOD.md",
    "order verdicts": "factcheck/tools/intake_f.py",
}
OWNER["statuses"] = OWNER["defect kinds"] = OWNER["technology"]

# "Governing" here is not the same as `canonical` in `doc_kind.py`, and
# the two lists deliberately differ. `doc_kind` asks **who owns the
# content**: a historical document is frozen and must not be edited. This
# list asks something else — **whose references must stay valid** — and a
# frozen document naming a renamed tool lies to a reader exactly as a live
# one does. So historical documents appear here, and that is not a
# disagreement between gates but two different questions about one file.
#
# Cache directories that no longer exist in THIS tree but may still exist
# in somebody else's container. This is history, not a definition: the
# definition is below, in `cache_not_in_git`, and it asks whether a
# manifest is present. Nothing renames these lines — the past cannot be
# renamed.
HISTORICAL_CACHES = ("dzherela-kesh",)

# The governing documents are the ones describing the TECHNOLOGY, and
# they live in the root of `factcheck/`. Everything else has a directory
# named after what it is: `reports/`, `evidence/`, `cards/`, `work/`.
#
# The list stays explicit rather than a `glob`, deliberately: it is a
# STATEMENT that the technology consists of exactly these documents. A
# file somebody adds to the root must either be admitted here on purpose
# or live in a directory by kind — and `name_lists.py` watches that a name
# here does not become the name of nothing.
GOVERNING = ["METHOD.md", "REPORT.md", "LESSONS.md"]

# `README.md` is not a governing document: it decides nothing and travels
# nowhere — on another book it is written fresh. But it must be in the
# root, and these are different questions:
#
#     GOVERNING   what is the technology, and what travels
#     IN_ROOT     what a person must see on opening the directory
#
# The first time I conflated them and deleted the README along with the
# index, because "two files need no map". The index really was
# unnecessary; the orientation was not, and the owner said so plainly. A
# map and a sign on the door are not the same thing.
IN_ROOT = GOVERNING + ["README.md"]

# The same sed pass that once marked `TASK-SPEC.md` historical in
# `doc_kind.ISTORYCHNI` left a **second** trace — here. Both lines
# carrying `WORK-ORDER-EXAMPLE.md` (a document deleted as obsolete)
# became `TASK-SPEC.md`, and the list began reporting "14 governing" while
# holding 13 distinct names. The number the list printed had diverged from
# the list itself.
#
# M2 found and fixed the case in `doc_kind`; this one survived because
# nobody asked. So we ask: the check below admits neither a duplicate nor
# the name of a document that does not exist.


def governing_list_sound() -> list[str]:
    """The governing list is a list of NAMES, and nobody checked it.

    Kind 26 in its pure form, twice in one day and in a different file: a
    rename pass rewrites a name whose subject WAS the old name, and no
    check asks about it, because every check asks about the **content** of
    the documents rather than about the list itself.

        GOVERNING  14 entries, 13 distinct
    """
    problems = []
    for n in sorted(set(GOVERNING)):
        if GOVERNING.count(n) > 1:
            problems.append(f"GOVERNING: `{n}` named {GOVERNING.count(n)} "
                            f"times — the trace of a rename, not a list")
        if not (FC / n).exists():
            problems.append(f"GOVERNING: `{n}` is in the list, the document "
                            f"is not")
    return problems


# A line listing the statuses. THERE ARE THREE FORMATS, and not by whim:
#
#     | **A** | ✅ | …        SCHEMA.md
#     | `A`   | …            ARCHITECTURE.md (folded away 2026-08-29)
#         A  primary …       METHOD.md
#
# The first version knew only the first. A run on the pre-edit tree caught
# METHOD.md and did NOT catch ARCHITECTURE.md — precisely the document the
# whole thing had started from. A check that knows one form sees one form,
# and stays silent about the rest just as confidently.
#
# NOTE: this comment contrasts TWO documents, and a blanket substitution of
# `ARCHITECTURE.md` -> `METHOD.md` during the fold turned it into "caught
# METHOD.md and did not catch METHOD.md" — a sentence with no content. The
# name of the folded document here is not a reference but **testimony
# about the past**; kind 26, and `name_lists.py` does not catch it,
# because this is prose, not a list.
#
# Only the table under the statuses heading, not any table in the
# document. The first version searched for `| **word** |` across the whole
# file and collected record field names and unit kinds — that is,
# "statuses" that do not exist in the code, because they are not statuses.
#
# A section heading is a name too, and it travels with the document. When
# `SCHEMA.md` became English this pattern stopped finding the section at
# all, `statuses_section` returned an empty string, and the check reported
# that the normative list knows NONE of the code's statuses — the loudest
# possible conclusion drawn from having read nothing.
#
# This is kind 26 in a shape we had not seen: the rename rewrote not the
# rule but the **subject** of the rule, and the rule stayed whole and
# blind.
RE_STATUSES_SECTION = re.compile(
    r"^##+ .*(Класи доказу|Стани перевірки|Стани"
    r"|Evidence statuses|Statuses)\s*$", re.M)
RE_STATUS_TABLE = re.compile(
    r"^\|\s*(?:\*\*([a-z][a-z-]{3,})\*\*|`([a-z][a-z-]{3,})`)\s*\|", re.M)


def statuses_section(t: str) -> str:
    """The text of the section describing the statuses, and only that."""
    m = RE_STATUSES_SECTION.search(t)
    if not m:
        return ""
    nxt = re.search(r"^##+ ", t[m.end():], re.M)
    return t[m.end():m.end() + (nxt.start() if nxt else len(t))]


RE_STATUS_LIST = re.compile(r"^\s{2,}([a-z][a-z-]{3,})\s{2,}[—a-zа-яїєґ]", re.M)

# Tools live in two directories. A pattern without `factcheck/` does not
# merely miss — it MATCHES the substring `tools/layer3.py` inside
# `factcheck/tools/layer3.py`, checks a path that never existed, and
# declares a sound document broken. A miss is at least visible; a false
# hit is not.
RE_TOOL = re.compile(r"`?((?:factcheck/)?tools/[a-z0-9_.-]+\.py)`?")
RE_KIND = re.compile(r"(?:рід|kind)\s+(\d{1,2})\b", re.I)


def code_statuses() -> set[str]:
    """The current vocabulary of statuses, as WORDS.

    It was letters until 2026-08-29. The letters went out of the registry
    as an abbreviation: eleven single-character codes demand a legend
    nobody keeps in their head, and beside each of them the same word and
    the same description had always stood anyway.
    """
    import factcheck
    return set(factcheck.STATUSES)


def check_all() -> list[str]:
    problems: list[str] = []
    code = code_statuses()
    authoritative = (FC / OWNER["statuses"]).read_text(encoding="utf-8")
    section = statuses_section(authoritative)

    # An empty section and a section with no statuses are different
    # events, and confusing them is expensive. When `SCHEMA.md` was
    # translated the heading pattern stopped finding it, the section came
    # back empty — and the check reported "the list knows none of eleven
    # statuses", i.e. drew the loudest possible conclusion from having
    # read nothing.
    #
    # A zero obtained from an empty input is not a measurement. We say so
    # on its own line, so that next time it is visible which it was.
    if not section.strip():
        return [f"{OWNER['statuses']}: the statuses section was not found — "
                f"was the heading translated? The status check was NOT "
                f"PERFORMED, not passed"]
    listed = {a or b for a, b in RE_STATUS_TABLE.findall(section)}

    missing = code - listed
    if missing:
        problems.append(
            f"{OWNER['statuses']}: the normative list does not know the "
            f"statuses {sorted(missing)}, which exist in the code")
    extra = listed - code
    if extra:
        problems.append(
            f"{OWNER['statuses']}: lists statuses {sorted(extra)}, which do "
            f"not exist in the code")

    for name in GOVERNING:
        p = FC / name
        if not p.exists():
            problems.append(f"{name}: governing document is missing")
            continue
        t = p.read_text(encoding="utf-8")

        # A copy of the status vocabulary that has drifted from the code.
        named = ({a or b for a, b in RE_STATUS_TABLE.findall(statuses_section(t))}
                 | set(RE_STATUS_LIST.findall(t)))
        # Sieve with WHAT IS IN THE CODE, and never with a private list.
        #
        # There used to be `set("ABCDEFGKLS")` here — a private list of
        # letters, typed by hand. M1 introduced the status `N`, and the
        # check built against stale copies of the vocabulary HID it behind
        # its own stale copy: `N` dropped out of "named" and appeared
        # immediately in "absent". The document was right; the check was
        # not.
        #
        # M1's phrasing, sharper than mine: the check **masked `N` before
        # the comparison — and would not have seen the very correction it
        # was demanding.**
        #
        # We found this separately and fixed it identically, minutes
        # apart. The copy was living inside the tool built against copies.
        named &= code
        if len(named) >= 4 and name != OWNER["statuses"]:
            absent = code - named
            if absent:
                problems.append(
                    f"{name}: a copy of the status vocabulary missing "
                    f"{sorted(absent)} — either complete it, or replace it "
                    f"with a reference to {OWNER['statuses']}")

        for tool in set(RE_TOOL.findall(t)):
            if not (ROOT / tool).exists():
                problems.append(f"{name}: names a nonexistent {tool}")

        for n in set(RE_KIND.findall(t)):
            if name == OWNER["defect kinds"]:
                continue
            if not re.search(rf"^#{{2,3}} {n}\.", (FC / OWNER["defect kinds"])
                             .read_text(encoding="utf-8"), re.M):
                problems.append(f"{name}: refers to kind {n}, which is not in "
                                f"{OWNER['defect kinds']}")

    # The order's verdicts against the gate that accepts them.
    try:
        import intake_f
        znani = set(intake_f.POTREBUYE)
    except Exception as e:
        problems.append(f"the gate will not import: {str(e)[:60]}")
        znani = set()
    # The verdicts no longer live in a tool's template: they are in
    # `METHOD.md` Part IV, from which an order is assembled. The check
    # reads the **source**, not one of the copies — otherwise it guards a
    # copy and stays silent about the rest.
    if znani:
        try:
            import task_spec
            bloky = task_spec.bloky()
        except Exception as e:
            problems.append(f"the task spec will not parse: {str(e)[:60]}")
            bloky = {}
        for fname, tekst in bloky.items():
            if not fname.startswith("VERDICTS"):
                continue
            vsi = set(re.findall(r"^\| `([a-z_-]+)` \|", tekst, re.M))
            unknown = vsi - znani
            if unknown:
                problems.append(
                    f"TASK-SPEC [{name}]: the order offers verdicts "
                    f"{sorted(unknown)}, which the gate does not check")
    problems += governing_list_sound()
    problems += index_complete()
    problems += cache_not_in_git()
    problems += root_holds_only_governing()
    return problems


def root_holds_only_governing() -> list[str]:
    """Does the root of `factcheck/` hold **only** what travels.

    The rebuild of 2026-08-29 cut the root from 31 documents to six — and
    almost at once it turned out the move was half done. Eleven tools
    still held `factcheck/X.md` in a constant, while their own help text
    already said `factcheck/reports/X.md`. The files had moved; the tools
    that write them had not.

    That is worse than an ordinary description-versus-code divergence:
    none of them would have failed. The next run would simply have
    **created the root file again**, quietly, and within a week thirty
    documents would have been back in the root — with `git status` showing
    not an error but work.

    So the check asks both sides:
      * what lies in the root now;
      * and what any tool **intends** to write there.

    The second side catches the fault on the day it is introduced, not on
    the day it first fires.

    **What the second side cannot do.** It reads source text, not what
    happens at run time. A path assembled from data — `directory / name` —
    it will not see; a path written as a literal inside a temporary tree
    it will count as a violation although it is not (which is exactly what
    happened with the demonstration in `language.py`). So it measures
    **intent written as a literal**, and stays silent about the rest.
    Recorded here, because a measure that hides its limit would itself be
    kind 3."""
    problems = []
    dozvoleni = set(IN_ROOT)
    for p in sorted(FC.glob("*.md")):
        if p.name not in dozvoleni:
            problems.append(f"{p.name}: sits in the root of factcheck/, "
                            f"and the root holds only the governing documents")
    vzir = re.compile(r'"factcheck"\s*/\s*"([A-Z][A-Z0-9-]*\.md)"')
    for t in repo.tool_files():
        for fname in set(vzir.findall(t.read_text(encoding="utf-8"))):
            if fname not in dozvoleni:
                problems.append(f"tools/{t.name}: writes {name} into the "
                                f"root of factcheck/, where only the "
                                f"governing documents belong")
    return problems


def index_complete() -> list[str]:
    """Formerly: does `README.md`'s index name every document in the tree.

    The index existed because there were six documents and without a map a
    reader did not know which to open. The owner called that a defect
    rather than a convenience — "the directory should hold two documents"
    — and then an index describes what `ls` already shows.

    The check was withdrawn with the index. Keeping it would have meant
    keeping a mechanism whose subject had been abolished, and such a
    mechanism does not stay quiet: it fails on an empty input and looks
    like a breakage.

    Its work was taken over by two others: `root_holds_only_governing`
    admits nothing to the root but the documents, and `name_lists` watches
    that a name in a list is the name of a file that exists."""
    return []


def demo() -> int:
    """A demonstration on a corrupted input. A check that has never fired
    is indistinguishable from a check that is not there."""
    import tempfile
    global FC
    real_fc = FC
    cases = [
        ("a document names a nonexistent tool",
         {"METHOD.md": "see `tools/no-such-thing.py`\n"}, True),
        ("a document refers to a nonexistent kind",
         {"METHOD.md": "this is kind 99 of the catalogue\n"}, True),
        # The "clean" case used to substitute a two-word stub. While
        # METHOD.md was only reasoning, the stub really was clean. After
        # the consolidation METHOD.md OWNS the list of statuses — and the
        # stub became a violation, rightly: there is no such thing as a
        # document with no statuses section.
        #
        # So the case was testing not "a clean document" but "a document
        # with nothing in it to check". The difference shows only once the
        # subject of the check moves into that same file.
        ("a clean document",
         {"METHOD.md": (real_fc / "METHOD.md").read_text("utf-8")
                       + "\n\nNothing in particular.\n"}, False),
    ]
    failures = 0
    for name, files, expected in cases:
        with tempfile.TemporaryDirectory() as d:
            t = Path(d)

            for fname in GOVERNING:
                (t / fname).write_text((real_fc / fname).read_text("utf-8")
                                      if fname not in files else files[fname],
                                      encoding="utf-8")
            FC = t
            try:
                b = [x for x in check_all() if "METHOD.md" in x]
            finally:
                FC = real_fc
            caught = bool(b)
            ok = "✓" if caught == expected else "✗ FAIL"
            print("   %s %-42s expected %-5s got %s"
                  % (ok, name, expected, caught))
            failures += caught != expected
    failures += cache_selftest()
    print("\nfailures: %d" % failures)
    return 1 if failures else 0


def cache_selftest() -> int:
    """The cache gate against a directory whose name is in no file.

    The name here is deliberately invented and occurs nowhere else. That
    й перевіряється: якби означення кешу знову звелося до переліку
    імен, ця проба провалилася б **першою** — а перелік, який стереже
    лише те, що в ньому названо, від наступного перейменування не
    рятує (знахідка М2, рід 26 проти самих воріт).
    """
    import subprocess
    import tempfile
    global ROOT
    real_root = ROOT
    failures = 0
    with tempfile.TemporaryDirectory() as d:
        t = Path(d)
        subprocess.run(["git", "init", "-q"], cwd=t)
        cases = [("a cache under a name never invented before", True),
                 ("the same directory, manifest only", False)]
        (t / "kesh-yakoho-nikoly-ne-bulo").mkdir()
        (t / "kesh-yakoho-nikoly-ne-bulo" / "MANIFEST.md").write_text(
            "# manifest\n", encoding="utf-8")
        (t / "kesh-yakoho-nikoly-ne-bulo" / "chuzhyy.pdf").write_text(
            "x\n", encoding="utf-8")
        ROOT = t
        try:
            for name, expected in cases:
                if not expected:
                    (t / "kesh-yakoho-nikoly-ne-bulo" / "chuzhyy.pdf").unlink()
                    subprocess.run(["git", "rm", "-q", "--cached",
                                    "kesh-yakoho-nikoly-ne-bulo/chuzhyy.pdf"],
                                   cwd=t, capture_output=True)
                else:
                    subprocess.run(["git", "add", "-A"], cwd=t,
                                   capture_output=True)
                caught = bool(cache_not_in_git())
                ok = "✓" if caught == expected else "✗ FAIL"
                print("   %s %-42s expected %-5s got %s"
                      % (ok, name, expected, caught))
                failures += caught != expected
        finally:
            ROOT = real_root
    return failures


def main() -> int:
    if "--demo" in sys.argv:
        return demo()
    problems = check_all()
    for b in problems:
        print("   ✗ " + b)
    print("\ndocs: governing documents %d, divergences %d"
          % (len(GOVERNING), len(problems)))
    return 1 if problems else 0


def cache_not_in_git() -> list[str]:
    """No file of the cache but the manifest may be tracked.

    The incident of 2026-08-28: renaming `dzherela-kesh` -> `source-cache`
    rewrote **both** `.gitignore` lines to the new path, including the one
    whose subject WAS the old name. In the container where the rename was
    done the old directory no longer existed, so the consequence was not
    visible at all. In the other maintainer's container it did — and 236
    third-party documents landed in the index. Caught in time; nothing
    reached git.

    > An ignore rule for a path is a statement about everyone who **still
    > has** that path. Renaming it removes the protection exactly where it
    > is needed, and never where the rename was done.

    So this is not a check of `.gitignore` but a check of the
    **consequence**: we ask git what it tracks rather than reading the
    rules and believing them. Kind 26.

    ## Second version: the first was vulnerable to the same fault

    M2's finding at `05:26Z`, and they tested it rather than read it. In
    the first version the cache directories were simply listed here:

        git ls-files -- source-cache dzherela-kesh

    They put a tracked file in `sources-v3/` and the gate said nothing.

    > A gate built against kind 26 is vulnerable to kind 26: the list of
    > names inside it **is itself a copy of a path name**, and the next
    > rename either rewrites it (removing cover from the old name) or
    > misses the new one.

    So the cache **declares itself** — the same way our generated
    documents name their generator and every document names its kind:

    > **A directory containing a `MANIFEST.md` is a cache.**

    The list of names stays, but no longer as the definition of a cache —
    as **history**: `dzherela-kesh` exists nowhere any more and never will
    again, and that is exactly why it must be named, because in somebody
    else's container it still does. No rename rewrites these lines; they
    describe the past, and the past is not renamed.

    What this form does **not** catch, said aloud: a cache directory with
    no manifest. We have none and should have none — the manifest is the
    whole point of keeping a cache."""
    import subprocess
    dirs = set(HISTORICAL_CACHES)
    for p in ROOT.rglob("MANIFEST.md"):
        if ".git/" in p.as_posix():
            continue
        dirs.add(p.parent.relative_to(ROOT).as_posix())
    r = subprocess.run(["git", "ls-files"], cwd=ROOT,
                       capture_output=True, text=True)
    for x in r.stdout.split():
        if x.endswith("/MANIFEST.md"):
            dirs.add(x.rsplit("/", 1)[0])
    if not dirs:
        return []
    r = subprocess.run(["git", "ls-files", "--", *sorted(dirs)], cwd=ROOT,
                       capture_output=True, text=True)
    extra = [x for x in r.stdout.split()
             if x and not x.endswith("/MANIFEST.md")]
    if not extra:
        return []
    return [f"git tracks {len(extra)} cache files — there must be only "
            f"MANIFEST.md; first: {', '.join(extra[:3])}"]


if __name__ == "__main__":
    sys.exit(main())
