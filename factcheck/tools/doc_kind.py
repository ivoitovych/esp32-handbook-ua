#!/usr/bin/env python3
"""Every document says what kind it is, and the kind is checked.

## The problem this closes

`factcheck/` holds thirty-one documents. Some are rewritten by a tool on
every run; some are the authoritative statement of a rule; some are the
record of a wave that finished days ago. Nothing said which was which.

The cost was not theoretical. `QUOTES.md` was hand-merged during a
conflict resolution — a file a tool overwrites minutes later. Five
`*-m2.md` files duplicate a canonical document because nobody could tell
they were finished records rather than live ones. And a maintainer
reading a number in a historical file has no way to know it was true
only on the day it was written.

    generated   a tool rewrites it; editing it by hand is wasted work
    canonical   the authoritative statement; one owner, no copies
    historical  a record of a past wave; never edited, numbers frozen

## Why the label is checked and not merely written

A label nobody verifies is a comment. This checks both directions:

- a document labelled **generated** must actually be written by a tool,
  and the named tool must be the one that writes it;
- a document **not** labelled generated must not be written by any tool
  — otherwise someone is editing a file that gets overwritten.

Detection is by AST: the assignment that names the file and the
`.write_text` that uses it. The first version of that detector searched
for double-quoted names and found **zero** generators, because
`ast.unparse` emits single quotes — the same single-versus-double-quote
trap that cost nine silent breakages during the field migration. It is
recorded here because the trap is evidently not learnable once.

    factcheck/tools/doc_kind.py              check
    factcheck/tools/doc_kind.py --label      write the missing labels
    factcheck/tools/doc_kind.py --samoperevirka
"""
from __future__ import annotations

import argparse
import ast
import pathlib
import re
import sys

import repo
from repo import ROOT  # noqa: E402  (root is found, not counted)
FC = ROOT / "factcheck"

RE_IMYA = r'''["']([A-Za-z0-9._-]+\.md)["']'''
RE_POZNAKA = re.compile(
    r"^> \*\*(?P<rid>generated|canonical|historical)\*\*(?P<hvist>[^\n]*)",
    re.M)

# Роди, які не виводяться з коду. Породжений рід виводиться завжди;
# решту треба назвати, і назвати один раз.
# УВАГА до наступного перейменування. Це не посилання на файли — це
# ПЕРЕЛІК ІМЕН, і кожне ім'я тут є твердженням про документ під ним.
# 2026-08-29 прохід sed по керівних документах замінив тут
# `WORK-ORDER-EXAMPLE.md` на `TASK-SPEC.md`, і чинна специфікація
# завдання миттєво стала «історичною». Зловив цей же скрипт, за хвилину.
# Рід 26: перейменування переписало правило, чиїм предметом було ім'я.
ISTORYCHNI = {
    "ARCHITECTURE-M2.md", "SOURCES-M2.md", "LESSONS-M2.md", "NETWORK-M2.md",
    "TO-VERIFY-M2.md", "REFUTED-M2.md", "TO-VERIFY.md",
    "MEASURE-UNCHECKED.md", "WAVE-W1.md",
}

# Позначка англійською навмисно. Половина керівних документів уже
# англійською, і українська позначка в англійському документі — та сама
# суміш, від якої власник просив піти: читач мусить спершу здогадатися,
# з якої мови слово, перш ніж зрозуміти, що воно значить.
POYASNENNYA = {
    "generated": "a tool rewrites this file; editing it by hand is wasted work",
    "canonical": "the decision lives here; there are to be no copies",
    "historical": "a record of a finished wave; not edited, numbers frozen",
}


def hto_pyshe() -> dict[str, set[str]]:
    """Документ → інструменти, що його переписують. За AST, не за очима."""
    out: dict[str, set[str]] = {}
    nerozibrani: list[str] = []
    for p in repo.tool_files():
        # `newbook.py` пише README.md і REPORT.md — але **чужого** дерева,
        # яке щойно створило. Цей аналіз зіставляє за голим іменем файлу,
        # тож він побачив тут «README.md пише інструмент» і оголосив наш
        # README породженим. Правки в ньому нібито згорять при наступному
        # прогоні, якого не буде.
        #
        # Ім'я файлу знову не визначає файл. Тут воно ще й не визначає
        # ДЕРЕВО.
        if p.name == "newbook.py":
            continue
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except SyntaxError as e:
            # Мовчазний `continue` тут коштував рівно те, чого цей файл
            # і шукає. Під `-W error::SyntaxWarning` два тули з `\s` у
            # рядку документації переставали розбиратися, doc_kind їх
            # пропускав — і `UNREACHABLE-SOURCES.md` ставав `canonical`,
            # бо тула, що його пише, для перевірки більше не існувала.
            #
            # Породжений документ, оголошений канонічним, — найдорожча
            # з можливих помилок роду: його починають правити рукою.
            print(f"   ✗ tools/{p.name}: не розбирається ({e}) — "
                  f"рід документів, які він пише, не перевірено")
            nerozibrani.append(p.name)
            continue
        stali: dict[str, str] = {}
        for n in ast.walk(tree):
            if (isinstance(n, ast.Assign) and len(n.targets) == 1
                    and isinstance(n.targets[0], ast.Name)):
                m = re.search(RE_IMYA, ast.unparse(n.value))
                if m:
                    stali[n.targets[0].id] = m.group(1)
        for n in ast.walk(tree):
            if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                    and n.func.attr == "write_text"):
                tgt = ast.unparse(n.func.value)
                m = re.search(RE_IMYA, tgt)
                imya = stali.get(tgt) or (m.group(1) if m else None)
                if imya:
                    out.setdefault(imya, set()).add(p.stem)
    return out


# Документи лежать у підтеках за родом (`reports/`, `history/`, `book/`),
# а не всі в корені. Плаский `glob("*.md")` після перебудови 2026-08-29
# бачив шість файлів із тридцяти одного — і звітував «порушень 0» про
# двадцять п'ять документів, яких не відкривав. Рід 3: перевірка є,
# нуль є, і нуль про більшість предмета мовчить.
#
# Картки книги сюди не входять: вони породжуються `factcheck.py sketch`
# і не є документами супровідника.
# Не документи супровідника: картки (породжує `sketch`), наряди й
# відповіді прогонів (`runs/`), і заморожений `archive/`.
# `source-cache` — чужі документи, а не наші. Вимагати від
# `f3f48735-README.md` з ESP-IDF позначки роду означало б вимагати, щоб
# ми правили чужий текст; а рід «канонічний» на завантаженій копії був
# би прямою неправдою про те, хто ним володіє.
NE_DOKUMENTY = {"manual", "dodatky", "kartky", "inserts", "runs", "archive",
                "source-cache"}


def dokumenty() -> list:
    return [p for p in FC.rglob("*.md")
            if not (NE_DOKUMENTY & set(p.relative_to(FC).parts))]


def rid_dokumenta(p: pathlib.Path, pyshe: dict[str, set[str]]) -> str:
    if p.name in pyshe:
        return "generated"
    if p.name in ISTORYCHNI:
        return "historical"
    return "canonical"


# Породжений документ **не може** нести дописану рукою позначку: його
# переписує інструмент, і позначка гине з наступним прогоном. Саме це й
# сталося за годину після розстановки — `QUOTES.md` втратив її під час
# `make check`.
#
# Тож для породжених приймається їхня власна заява «Генерується
# `tools/X.py`», яку пише сам інструмент. Вимога та сама: **інструмент
# має бути названий**, і названий правильно.
RE_ZAYAVA = re.compile(
    r"^\*\*(?:Генерується|Generated by)\*\*[^\n]*", re.M)


def poznaka(p: pathlib.Path) -> tuple[str, str] | None:
    t = p.read_text(encoding="utf-8")
    m = RE_POZNAKA.search(t)
    if m:
        return (m.group("rid"), m.group("hvist"))
    z = RE_ZAYAVA.search(t)
    return ("generated", z.group(0)) if z else None


def perevirka() -> list[str]:
    pyshe = hto_pyshe()
    bidy: list[str] = []
    for p in sorted(dokumenty()):
        ye = poznaka(p)
        maye = rid_dokumenta(p, pyshe)
        if not ye:
            bidy.append(f"{p.relative_to(FC)}: немає позначки роду (мав би `{maye}`)")
            continue
        rid, hvist = ye
        if rid != maye:
            bidy.append(f"{p.relative_to(FC)}: позначено `{rid}`, а насправді `{maye}`")
            continue
        if rid == "generated":
            tuly = pyshe[p.name]
            if not any(f"tools/{t}.py" in hvist for t in tuly):
                bidy.append(
                    f"{p.relative_to(FC)}: labelled generated, but the tool is not named — "
                    f"it is written by {', '.join(sorted(tuly))}")
    # Зворотний бік: щось переписує документ, а той про це не каже.
    for imya, tuly in sorted(pyshe.items()):
        p = FC / imya
        if not p.exists():
            continue
        ye = poznaka(p)
        if ye and ye[0] != "generated":
            bidy.append(f"{imya}: позначено `{ye[0]}`, а його переписує "
                        f"{', '.join(sorted(tuly))} — правки згорять")
    return bidy


def rozstavyty() -> int:
    pyshe = hto_pyshe()
    n = 0
    for p in sorted(dokumenty()):
        if poznaka(p):
            continue
        rid = rid_dokumenta(p, pyshe)
        hvist = POYASNENNYA[rid]
        if rid == "generated":
            hvist = (f"written by "
                     f"{', '.join(f'`tools/{t}.py`' for t in sorted(pyshe[p.name]))}"
                     f"; editing it by hand is wasted work")
        t = p.read_text(encoding="utf-8")
        ryadky = t.split("\n")
        # Після заголовка першого рівня, якщо він є.
        i = 1 if ryadky and ryadky[0].startswith("# ") else 0
        ryadky.insert(i, f"\n> **{rid}** — {hvist}")
        p.write_text("\n".join(ryadky), encoding="utf-8")
        n += 1
        print(f"  {rid:<12} {p.relative_to(FC)}")
    print(f"позначено документів: {n}")
    return 0


def samoperevirka() -> int:
    pomylok = 0

    def probа(imya, umova):
        nonlocal pomylok
        pomylok += not umova
        print(f"  {'✓' if umova else '✗'} {imya}")

    pyshe = hto_pyshe()
    probа(f"породжені знайдено ({len(pyshe)})", len(pyshe) >= 10)
    probа("QUOTES.md серед породжених", "QUOTES.md" in pyshe)
    probа("METHOD.md не серед породжених", "METHOD.md" not in pyshe)
    # Взірець позначки читається в обидва боки.
    probа("позначку видно", RE_POZNAKA.search("# Т\n\n> **canonical** — x")
          is not None)
    probа("чужий рід не читається як позначка",
          RE_POZNAKA.search("> **invented** — x") is None)
    print("самоперевірка: усе як очікувано" if not pomylok
          else f"самоперевірка: РОЗБІЖНОСТЕЙ {pomylok}")
    return 1 if pomylok else 0


def main() -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--label", action="store_true")
    a.add_argument("--samoperevirka", action="store_true")
    a.add_argument("--suvoro", action="store_true")
    o = a.parse_args()
    if o.samoperevirka:
        return samoperevirka()
    if o.label:
        return rozstavyty()
    b = perevirka()
    print(f"doc_kind: документів {len(dokumenty())}, "
          f"порушень {len(b)}")
    for x in b[:20]:
        print(f"   ✗ {x}")
    return 1 if (b and o.suvoro) else 0


if __name__ == "__main__":
    sys.exit(main())
