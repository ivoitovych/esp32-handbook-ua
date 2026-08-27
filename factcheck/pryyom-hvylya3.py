#!/usr/bin/env python3
"""Приймання хвилі 2: цитата мусить стояти в НАЗВАНОМУ файлі.

## Що додано проти хвилі 2

Свідчення роботи в негативному вердикті. Закон М1, куплений його
четвертою хвилею: відповідь, яку можна дати не працюючи, коштує нуль,
байдуже, чесна вона на вигляд чи ні. У хвилі 2 `ne_znayshov` можна
було написати, не відкривши нічого, — і 78 таких відповідей із 98 не
давали способу відрізнити «в документі цього немає» від «не дивився».

Тепер `ne_znayshov` вимагає поля `dyvyvsya`, у якому має стояти ім'я
файлу з кешу. Скрипт перевіряє, що такий файл справді є.

## Чим це відрізняється від `pryyom-m2.py`

Той перевіряє форму запису: чи не книга в джерелі, чи є цитата при
класі A, чи не завищено E. Цей перевіряє **єдине, але головне**:
чи справді рядок із поля `cytata` стоїть у файлі, який названо в
полі `fayl`.

Саме ця перевірка робить наряд чесним, а не заборони в його тексті.
Переписати текст книги назад у `cytata` тепер не спрацює: у
`dzherela-kesh/ds18b20.pdf` тексту книги немає. Підтвердити можна
лише те, що справді відкрив.

Звірка нежорстка рівно в тому, у чому винен видобувач тексту з PDF:
пробіли схлопуються, м'які переноси й переноси рядків знімаються,
різні тире зводяться до одного. Усе інше — дослівно.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KESH = ROOT / "dzherela-kesh"
sys.path.insert(0, str(ROOT / "tools"))

import yaml
import citaty  # витягання тексту беремо в М1, а не пишемо втретє

_kesh_tekst: dict[str, str] = {}


def normal(s: str) -> str:
    # Розмітка reStructuredText — оформлення, не зміст. `:cpp:func:` та
    # зворотні лапки навколо імені функції стоять у джерелі й не стоять
    # ні в книзі, ні в тому, що бачить читач. Знімати їх — це звести
    # два записи того самого рядка, а не послабити звірку.
    s = re.sub(r":[a-z:]+:`~?([^`]+)`", r"\1", s)
    s = re.sub(r"``([^`]+)``", r"\1", s)
    s = s.replace("­", "").replace("‑", "-")
    s = re.sub(r"[–—−]", "-", s)
    s = re.sub(r"[’‘`´]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    s = re.sub(r"-\s*\n\s*", "", s)      # перенос зі скісною
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def tekst_fayla(imya: str) -> str | None:
    # Помічник пише то `ds18b20.pdf`, то `dzherela-kesh/ds18b20.pdf` —
    # у наряді ім'я стоїть із текою. Обидва варіанти правильні по суті,
    # і відхиляти за це означало б рахувати чесну роботу за брехню.
    imya = imya.strip().split("/")[-1]
    if imya in _kesh_tekst:
        return _kesh_tekst[imya]
    p = KESH / imya
    if not p.exists():
        return None
    # `citaty.tekst_dzherela` віддає PDF у двох виглядах одразу:
    # порядок читання плюс рядки таблиць, відновлені за координатами
    # слів. Мій колишній `pdftotext -layout` на двоколонковій сторінці
    # вставляв текст сусідньої колонки посеред речення — і чесна
    # цитата падала. Три записи цієї хвилі впали саме так.
    t = citaty.tekst_dzherela(p)
    if t is None:
        return None
    _kesh_tekst[imya] = normal(t)
    return _kesh_tekst[imya]


def perevirka(shlyakh: Path) -> list[tuple[str, str]]:
    bidy = []
    try:
        zapysy = yaml.safe_load(shlyakh.read_text(encoding="utf-8")) or []
    except Exception as e:
        return [("БИТИЙ YAML", str(e).split("\n")[0][:90])]
    for z in zapysy:
        if not isinstance(z, dict):
            bidy.append(("НЕ ЗАПИС", str(z)[:60]))
            continue
        ident = str(z.get("id", z.get("nazva", "?")))[:40]
        verdykt = str(z.get("verdykt", "")).strip()
        cyt = str(z.get("cytata", "")).strip()
        fayl = str(z.get("fayl", "")).strip()

        if verdykt not in ("pidtverdzheno", "sperechayetsya",
                           "ne_znayshov", "nedosyazhne"):
            bidy.append(("ВЕРДИКТ НЕВІДОМИЙ: " + verdykt[:30], ident))
            continue
        if verdykt in ("ne_znayshov", "nedosyazhne"):
            if cyt:
                bidy.append(("ЦИТАТА ПРИ ВЕРДИКТІ " + verdykt, ident))
                continue
            dyv = str(z.get("dyvyvsya", "")).strip()
            if not dyv:
                bidy.append(("НЕМАЄ СВІДЧЕННЯ РОБОТИ (dyvyvsya)", ident))
                continue
            # У полі має стояти ім'я реального файлу кешу. Без цієї
            # перевірки поле заповнюється будь-чим і не коштує нічого.
            nazvano = [w.strip(" ,;:'\"") for w in re.split(r"[\s,;]+", dyv)]
            if not any((KESH / w.split("/")[-1]).exists()
                       for w in nazvano if w):
                bidy.append(("dyvyvsya НЕ НАЗИВАЄ ФАЙЛУ З КЕШУ: "
                             + dyv[:40], ident))
            continue
        if not cyt:
            bidy.append(("%s БЕЗ ЦИТАТИ" % verdykt.upper(), ident))
            continue
        if not fayl:
            bidy.append(("ЦИТАТА БЕЗ НАЗВАНОГО ФАЙЛУ", ident))
            continue
        t = tekst_fayla(fayl)
        if t is None:
            bidy.append(("ФАЙЛУ НЕМАЄ В КЕШІ: " + fayl[:40], ident))
            continue
        if normal(cyt) not in t:
            bidy.append(("ЦИТАТИ НЕМАЄ В " + fayl[:34], ident))
    return bidy


def main(argv: list[str]) -> int:
    shlyakhy = [Path(a) for a in argv[1:]]
    vsyoho = 0
    prynyato = 0
    for s in shlyakhy:
        if not s.exists():
            continue
        b = perevirka(s)
        try:
            n = len(yaml.safe_load(s.read_text(encoding="utf-8")) or [])
        except Exception:
            n = 0
        prynyato += n - len(b)
        vsyoho += len(b)
        if b:
            print(s.name)
            for rid, ident in b:
                print("   %-44s %s" % (rid, ident))
    print("\nприйнято %d, відхилено %d" % (prynyato, vsyoho))
    return 1 if vsyoho else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
