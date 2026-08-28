#!/usr/bin/env python3
"""Імена полів: із транслітерованої української в англійську.

## Навіщо

Поля запису звалися `nazva`, `zbih`, `klas`, `dzherelo`, `cytata`,
`sposib`, `notatka`. Це транслітерація — непридатна для англомовної
книги й несмачна в українській.

Технологію фактчекінгу задумано переносити на інші книги. Переносити
її в такому вигляді означало б перекладати **код**, а не вміст, тобто
робити форк замість перенесення.

## Чому розширення, а не заміна

Над тими самими файлами працює другий супровідник. Одномоментна заміна
зламала б його інструменти тієї ж хвилини.

Тому класичні три кроки, і зараз перший:

    1. розширити  — нові імена **поруч** зі старими, обидва чинні
    2. переїхати  — інструменти переходять на нові, кожен своїм темпом
    3. звузити    — старі імена прибираються, коли обидва переїхали

Між кроками 1 і 3 файл важчий, і це свідома ціна: два супровідники
не зупиняються ані на хвилину.

## Мапа

| Було | Стало | Чому саме так |
|---|---|---|
| `nazva` | `title` | коротка назва запису |
| `zbih` | `match` | **внутрішнє**: регулярний вираз прив'язки |
| `klas` | `status` | стан перевірки |
| `dzherelo` | `source` | джерело |
| `cytata` | `quote` | дослівний витяг |
| `sposib` | `method` | як і коли отримано |
| `notatka` | `note` | примітка |
| `shukaty` | `look_for` | що шукати в недосяжному документі |
| `rozrakhunok` | `calculation` | обчислення для класу `arithmetic` |

    tools/field_names.py --rozshyryty   додати англійські поруч зі старими
    tools/field_names.py --zvirty       чи всі записи мають обидва набори
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

MAPA = {
    "nazva": "title",
    "zbih": "match",
    "klas": "status",
    "dzherelo": "source",
    "cytata": "quote",
    "sposib": "method",
    "notatka": "note",
    "shukaty": "look_for",
    "rozrakhunok": "calculation",
}

# Стан перевірки: літера нічого не каже тому, хто бачить її вперше.
STANY = {
    "A": "verbatim",
    "B": "derived",
    "C": "named-unreachable",
    "D": "arithmetic",
    "E": "no-external-signal",
    "F": "unchecked",
    "G": "refuted",
    "K": "code-context",
}


def znachennya(pole: str, v):
    """`status` окремо: літера лишається, поруч стає слово."""
    if pole == "status" and isinstance(v, str) and v in STANY:
        return STANY[v]
    return v


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--rozshyryty", action="store_true")
    p.add_argument("--zvirty", action="store_true")
    a = p.parse_args()

    teka = ROOT / "factcheck" / "evidence"
    zminen = zapysiv = nepovnyh = 0
    for f in sorted(teka.glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        if not isinstance(z, list):
            continue
        bulo = False
        for r in z:
            if not isinstance(r, dict):
                continue
            zapysiv += 1
            brakuye = [s for s in MAPA if s in r and MAPA[s] not in r]
            if a.zvirty:
                if brakuye:
                    nepovnyh += 1
                continue
            for stare in brakuye:
                nove = MAPA[stare]
                r[nove] = znachennya(nove, r[stare])
                bulo = True
        if a.rozshyryty and bulo:
            # Шапка з коментарями губиться при перезаписі, тож зберігаємо
            # її окремо: вона несе причини, а причини дорожчі за дані.
            tekst = f.read_text(encoding="utf-8")
            shapka = "".join(ln for ln in tekst.splitlines(keepends=True)
                             if ln.startswith("#") or not ln.strip())
            shapka = shapka[:shapka.rfind("\n\n") + 2] if "\n\n" in shapka else shapka
            f.write_text(
                shapka + yaml.safe_dump(z, allow_unicode=True,
                                        sort_keys=False, width=88),
                encoding="utf-8")
            zminen += 1

    if a.zvirty:
        print(f"field_names: записів {zapysiv}, без англійських імен {nepovnyh}")
        return 1 if nepovnyh else 0
    print(f"field_names: розширено файлів {zminen}, записів {zapysiv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
