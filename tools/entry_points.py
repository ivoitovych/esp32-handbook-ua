#!/usr/bin/env python3
"""Every entry point of the technology, and its output, captured.

## Why this exists, and why it nearly did not

`make check` runs eighteen targets. The technology has **fifty-two**
runnable entry points. On 2026-08-28 a field-name migration passed
`make check` green three times while nine places were broken — and every
one of them lived in a command no target invokes: `factcheck.py blocked`
raised `KeyError` for four hours; four tools keyed results by a field
their writers had stopped producing; a fallback expression had both
halves renamed and stopped being a fallback.

All nine were found by running everything and diffing the output. Then
the same harness caught three more during the tool renames: a directory
rename that turned a local variable into a Python keyword, a rule that
renamed a dictionary key belonging to a schema that is not migrating,
and the rename tool overwriting its own mapping table.

**And the harness itself lived in a scratch directory.** The method was
written down in `MIGRATION.md`; the runnable thing was not in the
repository at all, and would have died with the session that wrote it.

> A method described in a document and a method that can be run are not
> the same asset. The first one has to be rebuilt by whoever needs it
> next, from a description, under pressure.

## What it does

    tools/entry_points.py --list          what counts as an entry point
    tools/entry_points.py --capture DIR   run everything, save the output
    tools/entry_points.py --diff A B      compare two captures
    tools/entry_points.py --missing       entry points no target covers

A capture is a directory of `<point>.out` / `.err` files. Two captures
compare as text. Use it around any change that is supposed to be
behaviour-preserving — renames, refactors, migrations — where "it still
works" is a claim about fifty-two programs and not about one.

## Restoring the tree after each point

Several tools write generated files, and some ignore an unknown flag and
just do their work — a sweep with `--help` once rewrote the book's
index. So the tree is restored after every point. **Only files that were
clean before that point** are restored: an earlier version of this
harness ran `git checkout -- .` and ate uncommitted work twice.
"""
from __future__ import annotations

import argparse
import difflib
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Аргументи навмисно найдешевші: мета — стала поведінка, а не покриття
# гілок. Інструмент, що без аргументів друкує вжиток, теж придатний:
# його вжиток — така сама стала поведінка, і саме він ловить
# перейменування.
TOCHKY: list[list[str]] = [
    ["factcheck.py", "status"], ["factcheck.py", "stale"],
    ["factcheck.py", "vorota"], ["factcheck.py", "blocked"],
    ["factcheck.py", "cherga"], ["factcheck.py", "shukaty", "GPIO"],
    ["factcheck.py", "vzirets", "GPIO"],
    ["layer3.py", "--zvit"], ["layer1.py"], ["layer1.py", "--detali"],
    ["layer1_units.py"], ["coverage.py"], ["intake.py"],
    ["schema.py"], ["schema.py", "--samoperevirka"],
    ["leak.py"], ["leak.py", "--samoperevirka"],
    ["task_spec.py", "--version"], ["task_spec.py", "--blocks"],
    ["task_spec.py", "--samoperevirka"],
    ["modality.py"], ["cache_vs_book.py", "--tykho"], ["cache_identity.py"],
    ["cache.py", "--check"], ["cache.py", "--vidtvornist"],
    ["split_queue.py"], ["work_orders.py"], ["work_orders_f.py"],
    ["correspondence.py"], ["refuted.py"], ["struct_fields.py"],
    ["pins.py"], ["cross_refs.py"], ["linkcheck.py"], ["calques.py"],
    ["arithmetic.py"], ["spelling.py"], ["budgets.py", "--pages"],
    ["claims.py"], ["review.py"], ["field_names.py"],
    ["patterns_repair.py"], ["land_c.py"], ["sweep_land.py"],
    ["sweep_digest.py"], ["sweep.py"], ["leads.py"], ["measure_f.py"],
    ["contest_e.py"], ["sample.py"], ["helper_dumps.py"],
    ["deslang.py"], ["book_index.py"], ["bind_by_hash.py"],
]

# Цілі `make check` — щоб `--missing` могла сказати, чого вони не бачать.
U_VOROTAKH = {
    "schema.py", "leak.py", "layer3.py", "layer1.py", "coverage.py",
    "intake.py", "modality.py", "cache_vs_book.py", "cache.py",
    "correspondence.py", "refuted.py", "struct_fields.py", "pins.py",
    "cross_refs.py", "linkcheck.py", "calques.py", "arithmetic.py",
    "budgets.py", "factcheck.py", "task_spec.py",
}


def imya(t: list[str]) -> str:
    return "_".join(t).replace("/", "_").replace("-", "_").replace(".", "_")


def brudni() -> set[str]:
    r = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                       capture_output=True, text=True)
    return {x.split()[-1] for x in r.stdout.splitlines() if x.strip()}


def znyaty(kudy: pathlib.Path) -> int:
    kudy.mkdir(parents=True, exist_ok=True)
    do = brudni()
    for t in TOCHKY:
        r = subprocess.run([sys.executable, f"tools/{t[0]}", *t[1:]],
                           cwd=ROOT, capture_output=True, text=True,
                           timeout=1800)
        (kudy / f"{imya(t)}.out").write_text(r.stdout, encoding="utf-8")
        (kudy / f"{imya(t)}.err").write_text(r.stderr, encoding="utf-8")
        znak = "✓" if r.returncode == 0 else f"rc={r.returncode}"
        if "Traceback" in r.stderr:
            znak = "ПАДІННЯ"
        print(f"  {znak:>8}  {' '.join(t)}")
        # Відкотити лише те, що було чисте до цього запуску.
        for f in sorted(brudni() - do):
            subprocess.run(["git", "checkout", "-q", "--", f], cwd=ROOT)
    print(f"знято точок: {len(TOCHKY)} → {kudy}")
    return 0


def zvirty(a: pathlib.Path, b: pathlib.Path) -> int:
    rizn = 0
    for t in TOCHKY:
        fa, fb = a / f"{imya(t)}.out", b / f"{imya(t)}.out"
        if not fa.exists() or not fb.exists():
            print(f"  ? немає знімка: {' '.join(t)}")
            rizn += 1
            continue
        ta, tb = fa.read_text(encoding="utf-8"), fb.read_text(encoding="utf-8")
        if ta == tb:
            continue
        rizn += 1
        print(f"  ✗ РІЗНИЦЯ  {' '.join(t)}")
        for r in list(difflib.unified_diff(ta.splitlines(), tb.splitlines(),
                                           lineterm=""))[2:8]:
            print(f"        {r[:104]}")
    print(f"\nточок {len(TOCHKY)}, різних {rizn}")
    return 1 if rizn else 0


def nepokryti() -> int:
    poza = sorted({t[0] for t in TOCHKY} - U_VOROTAKH)
    print(f"точок входу {len(TOCHKY)} у {len({t[0] for t in TOCHKY})} "
          f"інструментах")
    print(f"інструментів поза `make check`: {len(poza)}")
    for p in poza:
        print(f"    {p}")
    print("\nСаме тут вижили всі дев'ять зламів переведення імен полів.")
    return 0


def main() -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--list", action="store_true")
    a.add_argument("--capture")
    a.add_argument("--diff", nargs=2)
    a.add_argument("--missing", action="store_true")
    o = a.parse_args()
    if o.list:
        for t in TOCHKY:
            print("  " + " ".join(t))
        return 0
    if o.missing:
        return nepokryti()
    if o.capture:
        return znyaty(pathlib.Path(o.capture))
    if o.diff:
        return zvirty(pathlib.Path(o.diff[0]), pathlib.Path(o.diff[1]))
    a.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
