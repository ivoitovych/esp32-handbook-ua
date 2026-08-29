#!/usr/bin/env python3
"""Every entry point of the technology, and its output, captured.

## Why this exists, and why it nearly did not

`make check` runs eighteen targets. The technology has far more runnable
entry points — `--list` prints how many, and the number is deliberately
not repeated in this sentence: an earlier draft said "fifty-two" while
the list held fifty-seven, and a document that miscounts the thing it
exists to count is worse than one that declines to. On 2026-08-28 a field-name migration passed
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
works" is a claim about every one of those programs and not about one.

## Restoring the tree after each point

Several tools write generated files, and some ignore an unknown flag and
just do their work — a sweep with `--help` once rewrote the book's
index. So the tree is restored after every point.

**And the restore ate uncommitted work three times before the cause was
admitted.** Each repair kept the same wrong premise — that the harness
can tell a tool's leftovers from a person's writing by looking at which
files are dirty. It cannot, and no refinement of that test can.

    version 1  `git checkout -- .`              ate work twice
    version 2  baseline of dirty files, taken
               once at the start of the run     ate a document mid-run
    version 3  baseline retaken before each
               point                            ate it again: the edit
                                                lands DURING a point,
                                                not between two
    version 4  the live tree is never written   nothing to restore

Version 3 was measured, not assumed: a thread edited `DEFECTS.md` six
seconds into a capture and the edit was gone at the end. A point runs
for anywhere from a fraction of a second to minutes, so "between two
points" is the rare case, not the common one.

> Three repairs in a row asked *how do I restore more carefully*. The
> question was *why is this program writing to the tree I am working
> in*.

So the capture now runs in a **git worktree of its own**, created at
`HEAD` and carrying the uncommitted diff so the behaviour measured is
the behaviour of the tree you actually have. Tools may rewrite anything
they like in there; it is deleted afterwards. The source cache is
symlinked, not copied — it is read-only to every tool and 364 documents
of it.
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
    # Інструменти, що ВИМАГАЮТЬ аргументів. Без них гарнес доходив лише
    # до повідомлення про вжиток — і саме там пройшов `NameError` у
    # `work_orders_f --vypadkovo`, бо модуль `sample` імпортувався в
    # `main()`, а вживався в іншій функції.
    #
    # > Точка входу, покрита лише своїм повідомленням про вжиток,
    # > покрита рівно настільки, наскільки її не запускали.
    #
    # `{TMP}` заміняється на тимчасовий каталог; ці точки нічого не
    # пишуть у дерево.
    ["work_orders_f.py", "{TMP}/wof", "--vypadkovo", "6",
     "--nasinnya", "20260828"],
    ["work_orders_f.py", "{TMP}/wofr", "--vypadkovo", "6",
     "--nasinnya", "20260828", "--rich-cards"],
    ["sample.py", "F", "6", "--nasinnya", "20260828"],
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


def work_copy():
    """Окреме дерево з ТИМ САМИМ вмістом, включно з незакоміченим.

    Контекстний менеджер: віддає шлях, прибирає за собою. Кеш джерел
    **прив'язується символьно**, а не копіюється: він читається всіма
    інструментами й ніким не пишеться, і його 364 документи важать
    більше, ніж уся решта дерева.

    Незакомічене переноситься латкою, бо без нього гарнес міряв би не
    те дерево, яке ми правимо, — а саме заради «до і після правки» він
    і існує.
    """
    import contextlib
    import shutil
    import tempfile

    @contextlib.contextmanager
    def _kopiya():
        tmp = tempfile.mkdtemp(prefix="entry-points-tree-")
        derevo = pathlib.Path(tmp) / "w"
        subprocess.run(["git", "worktree", "add", "-q", "--detach",
                        str(derevo), "HEAD"], cwd=ROOT, check=True)
        try:
            latka = subprocess.run(["git", "diff", "HEAD"], cwd=ROOT,
                                   capture_output=True, text=True).stdout
            if latka.strip():
                subprocess.run(["git", "apply", "-"], cwd=derevo,
                               input=latka, text=True, check=True)
            kesh = ROOT / "source-cache"
            if kesh.is_dir():
                cil = derevo / "source-cache"
                if cil.exists():
                    shutil.rmtree(cil)
                cil.symlink_to(kesh)
            yield derevo
        finally:
            subprocess.run(["git", "worktree", "remove", "--force",
                            str(derevo)], cwd=ROOT, capture_output=True)
            shutil.rmtree(tmp, ignore_errors=True)
    return _kopiya()


def znyaty(kudy: pathlib.Path) -> int:
    import tempfile
    kudy.mkdir(parents=True, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="entry-points-")
    with work_copy() as derevo:
        return _capture_into(kudy, tmp, derevo)


def _capture_into(kudy: pathlib.Path, tmp: str, derevo: pathlib.Path) -> int:
    for t in TOCHKY:
        argv = [x.replace("{TMP}", tmp) for x in t[1:]]
        r = subprocess.run([sys.executable, f"tools/{t[0]}", *argv],
                           cwd=derevo, capture_output=True, text=True,
                           timeout=1800)
        # Ім'я тимчасового каталогу міняється щопрогону, тож два знімки
        # тих точок, що його друкують, НІКОЛИ не збігалися б — і
        # порівняння вічно показувало б різницю там, де її немає.
        # Знімок, який завжди відрізняється від себе, не знімок.
        def bez_tmp(s: str) -> str:
            # І шлях самої робочої копії теж: він новий щопрогону, тож
            # без нормалізації два знімки не збіглися б ніколи — та
            # сама вада, що з `{TMP}`, лише на рівень вище.
            return s.replace(tmp, "{TMP}").replace(str(derevo), "{ROOT}")

        (kudy / f"{imya(t)}.out").write_text(bez_tmp(r.stdout), encoding="utf-8")
        (kudy / f"{imya(t)}.err").write_text(bez_tmp(r.stderr), encoding="utf-8")
        znak = "✓" if r.returncode == 0 else f"rc={r.returncode}"
        if "Traceback" in r.stderr:
            znak = "ПАДІННЯ"
        print(f"  {znak:>8}  {' '.join(t)}")
        # Відкату більше немає й бути не має: інструменти пишуть у
        # робочу копію, яка існує рівно на час прогону. Дерево, у якому
        # хтось працює, гарнес не чіпає взагалі.
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
        print(f"\nточок входу {len(TOCHKY)} у "
              f"{len({t[0] for t in TOCHKY})} інструментах")
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
