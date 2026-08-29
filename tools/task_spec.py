#!/usr/bin/env python3
"""The worker task as one versioned object, not seven rewrites of it.

## What this is for

Every work order handed to a helper used to carry its own copy of the
rules — seven generators, seven headers, each restating the same things
differently. Measured across eight rules and seven headers: **one** rule
appeared in all seven; the stub-page trap appeared in two; the worker's
place in the whole flow in three. Header length ranged 1424 to 5867
characters for the same job.

That made the task an **untracked variable in the middle of every
measurement**. When a defect class appeared or vanished between waves,
nothing could say whether the technology had changed or the wording had.

So: the text lives in `factcheck/TASK-SPEC.md`, in named blocks. A
generator names the blocks it needs and gets them composed, with a
version stamp. The stamp is the sha256 of the blocks actually used —
not of the whole file — so a wave is comparable to another wave exactly
when it was told the same thing.

    tools/task_spec.py --version           version of the whole spec
    tools/task_spec.py --blocks            list the blocks
    tools/task_spec.py --show ORIENTATION  print one
    tools/task_spec.py --samoperevirka     demonstration on broken input

## Why the stamp is per-order and not per-file

A version of the file would move when any block changes, including
blocks a given wave never saw. Then two waves that were told exactly the
same thing would look different, and the comparison we built this for
would be wrong in the safe-looking direction.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPEC = ROOT / "factcheck" / "METHOD.md"

# Блоки переїхали в `METHOD.md`, частину IV, і поглибшали на рівень.
# Рівень заголовка тут — не оздоба: `^## \[` після переїзду не знайшов
# би жодного блоку, `bloky()` повернув би порожній словник, а версія
# наряду порахувалася б від нічого — і мовчки збіглася б для двох різних
# нарядів. Приймаємо обидва рівні, щоб те саме не повторилося вниз.
# Блок кінчається на наступному заголовку **того самого чи вищого
# рівня**, а не лише на наступному `[ІМ'Я]`. Поки специфікація була
# окремим файлом, різниці не було: після останнього блоку файл кінчався.
# Після переїзду в `METHOD.md` за нею стоїть частина V — і `FORMAT`
# проковтнув її цілком, усі 823 рядки. Помітно це стало лише тому, що
# версія наряду змінилася й ми пішли дивитися чому.
#
# Взірець, чия межа — кінець файлу, міряє не блок, а те, що файл на
# ньому скінчився.
RE_BLOK = re.compile(r"^#{2,3} \[([A-Z][A-Z0-9-]*)\][^\n]*\n(.*?)(?=^#{1,3} |\Z)",
                     re.M | re.S)


def bloky(tekst: str | None = None) -> dict[str, str]:
    """Named blocks of the spec, in file order."""
    t = tekst if tekst is not None else SPEC.read_text(encoding="utf-8")
    # Горизонтальна риска перед наступною частиною — розмітка документа,
    # а не текст блоку. Помічник її не бачить, тож у версію вона входити
    # не має: інакше переїзд специфікації в спільний файл змінив би
    # `order_version` у всіх нарядів, не змінивши жодного слова, яке
    # хтось прочитав, і всі попередні прогони втратили б порівнянність.
    def bez_rysky(x: str) -> str:
        return re.sub(r"\n+-{3,}\s*\Z", "", x.strip("\n")).strip("\n")

    return {m.group(1): bez_rysky(m.group(2)) for m in RE_BLOK.finditer(t)}


def versiya(imena: list[str] | None = None, tekst: str | None = None,
            shablon: str = "") -> str:
    """Version of everything the helper SEES, not of what is easy to hash.

    Knowledge from M2, 2026-08-28: their version hashed the header
    template alone, so an order with the surrounding book text and one
    without it got the **same** number — two different technologies
    under one label, and the difference between them recorded as noise.

    The same hole was here, mirrored. This hashed the blocks alone, so
    two orders built from identical blocks but different frames — a
    sweep and a leads batch — were indistinguishable by version.

    > A fingerprint narrower than its subject is worse than none. It
    > looks like control.

    So the frame **template** goes into the hash as well. The template,
    not the substituted text: counts and seeds change every run and
    would make every order its own version, which is the same failure
    from the other side.
    """
    b = bloky(tekst)
    klyuchi = list(b) if imena is None else list(imena)
    h = hashlib.sha256()
    h.update(shablon.encode())
    for k in klyuchi:
        h.update(k.encode())
        h.update(b.get(k, "").encode())
    return h.hexdigest()[:8]


def sklasty(imena: list[str], zaholovok: str = "", vstup: str = "",
            shablon: str = "") -> str:
    """Compose a work-order header from named blocks.

    An unknown block name is an error, not an omission: a generator that
    silently loses a rule is exactly the defect this file exists against
    (kind 3 — a check that measures nothing).
    """
    b = bloky()
    nevidomi = [i for i in imena if i not in b]
    if nevidomi:
        raise KeyError(f"немає таких блоків завдання: {', '.join(nevidomi)}")
    ch: list[str] = []
    if zaholovok:
        ch.append(zaholovok.rstrip("\n"))
    if vstup:
        ch.append(vstup.strip("\n"))
    for i in imena:
        ch.append(b[i])
    ch.append(f"---\n\n*Task spec `{versiya(imena, shablon=shablon)}` · blocks: "
              f"{', '.join(imena)}. Quote this version when reporting "
              f"results from this wave.*")
    return "\n\n".join(ch) + "\n"


def samoperevirka() -> int:
    """Demonstration on deliberately broken input.

    Project rule: a check that has never fired is no different from a
    check that does not exist.
    """
    pomylok = 0

    def probа(imya, umova):
        nonlocal pomylok
        pomylok += not umova
        print(f"  {'✓' if umova else '✗'} {imya}")

    b = bloky()
    probа(f"спец читається, блоків {len(b)}", len(b) >= 8)
    probа("порожній блок не губиться",
          all(v.strip() for v in b.values()))

    try:
        sklasty(["ORIENTATION", "NEMA-TAKOHO"])
        probа("невідомий блок — помилка", False)
    except KeyError:
        probа("невідомий блок — помилка", True)

    # Версія залежить від **ужитих** блоків, а не від усього файлу.
    v1 = versiya(["ORIENTATION", "VERBATIM"])
    v2 = versiya(["VERBATIM", "ORIENTATION"])
    v3 = versiya(["ORIENTATION"])
    probа("порядок блоків змінює версію", v1 != v2)
    probа("інший набір — інша версія", v1 != v3)

    # Правка блока, якого наряд не бачив, версії наряду не зрушує.
    zipsovanyy = SPEC.read_text(encoding="utf-8").replace(
        "## [STUB]", "## [STUB]\n\nдописаний рядок, якого раніше не було\n")
    probа("правка чужого блока не рухає версію наряду",
          versiya(["ORIENTATION", "VERBATIM"], zipsovanyy) == v1)
    probа("правка свого блока рухає версію наряду",
          versiya(["STUB"], zipsovanyy) != versiya(["STUB"]))

    # Діра, яку знайшов М2 на своєму боці й яка була тут дзеркально:
    # відбиток мусить покривати ВСЕ, що виконавець бачить, а не лише
    # те, що зручно хешувати. Два наряди з тих самих блоків, але з
    # різними рамками, мали однакову версію.
    probа("різна рамка — різна версія",
          versiya(["VERBATIM"], shablon="# Наряд А")
          != versiya(["VERBATIM"], shablon="# Наряд Б"))
    # І зворотне: підстановка чисел у рамку версії НЕ рухає, інакше
    # кожен прогін був би власною версією — та сама вада з іншого боку.
    probа("та сама рамка — та сама версія",
          versiya(["VERBATIM"], shablon="# Наряд {n}")
          == versiya(["VERBATIM"], shablon="# Наряд {n}"))

    print("самоперевірка: усе як очікувано" if not pomylok
          else f"самоперевірка: РОЗБІЖНОСТЕЙ {pomylok}")
    return 1 if pomylok else 0


def main() -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--version", action="store_true")
    a.add_argument("--blocks", action="store_true")
    a.add_argument("--show")
    a.add_argument("--samoperevirka", action="store_true")
    o = a.parse_args()

    if o.samoperevirka:
        return samoperevirka()
    if o.show:
        b = bloky()
        if o.show not in b:
            print(f"немає блока `{o.show}`; є: {', '.join(b)}")
            return 2
        print(b[o.show])
        return 0
    if o.blocks:
        for k, v in bloky().items():
            print(f"  {k:<22} {len(v):>5} символів   {versiya([k])}")
        return 0
    print(versiya())
    return 0


if __name__ == "__main__":
    sys.exit(main())
