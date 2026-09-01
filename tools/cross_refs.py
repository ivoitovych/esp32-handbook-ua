#!/usr/bin/env python3
"""Перевірка згадок «розділ NN» і «картка КN» у прозі.

`tools/linkcheck.py` перевіряє посилання виду `[текст](#слаг)` — ті, що
стають клікабельними. Але книга набагато частіше посилається словами:
«детальніше — розділ 32», «картка К7», «(розділ 18)». Таких згадок
кількасот, вони ніде не перевіряються, і помилка в номері нічим себе не
виявляє: текст лишається зв'язним, а читач іде не туди.

Ціна помилки тут вища за звичайну друкарську. Довідник для поля будується
на маршрутах: картка → розділ → додаток. Обірваний маршрут дорівнює
відсутньому матеріалу.

Перевіряє:
  · «розділ NN» — чи існує файл manual/NN-*.md
  · «картка КN» / «К7» — чи існує файл kartky/kNN-*.md
  · «додаток X» — чи існує файл dodatky/x-*.md
  · самопосилання: розділ, що відсилає сам на себе

    tools/cross_refs.py        перевірити
    tools/cross_refs.py -v     ще й показати всі згадки за адресатом
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
GRUPY = ("kartky", "manual", "dodatky", "inserts")

# «розділ 32», «розділи 07 і 16», «(розділ 4)» — з відмінками.
RE_ROZDIL = re.compile(r"розділ(?:и|ів|і|у|ах|ами)?\s+((?:\d{1,2}(?:\s*(?:,|і|та|—|–|-)\s*)?)+)")
# «картка К7», «карток К2», «К13» у тексті.
RE_KARTKA = re.compile(r"[Кк]арт(?:ка|ки|ку|ці|ок|ками|кою)\s+([КK]\d{1,2}(?:\s*(?:,|і|та)\s*[КK]?\d{1,2})*)")
RE_DODATOK = re.compile(r"[Дд]одат(?:ок|ка|ку|ки|ків)\s+([A-HА-Я])")


def naiavni() -> tuple[set, set, set]:
    rozdily = {f.name[:2] for f in (ROOT / "manual").glob("*.md")}
    kartky = {f.name[1:3] for f in (ROOT / "kartky").glob("k*.md")}
    dodatky = {f.name[0].upper() for f in (ROOT / "dodatky").glob("*.md")}
    return rozdily, kartky, dodatky


def main() -> int:
    rozdily, kartky, dodatky = naiavni()
    # Латинські імена файлів додатків проти кириличних букв у тексті.
    KYR = {"А": "A", "В": "B", "С": "C", "Д": "D", "Е": "E", "Ф": "F", "Г": "G", "Н": "H"}

    zhahy: list[str] = []
    de: dict[str, list[str]] = defaultdict(list)

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            rel = str(f.relative_to(ROOT))
            svij = f.name[:2] if g == "manual" else None
            for ln, ryadok in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
                for m in RE_ROZDIL.finditer(ryadok):
                    for n in re.findall(r"\d{1,2}", m.group(1)):
                        n = n.zfill(2)
                        de[f"розділ {n}"].append(f"{rel}:{ln}")
                        if n not in rozdily:
                            zhahy.append(f"{rel}:{ln}: немає розділу {n}")
                        elif n == svij:
                            zhahy.append(f"{rel}:{ln}: посилання саме на себе (розділ {n})")
                for m in RE_KARTKA.finditer(ryadok):
                    for n in re.findall(r"\d{1,2}", m.group(1)):
                        n = n.zfill(2)
                        de[f"картка К{int(n)}"].append(f"{rel}:{ln}")
                        if n not in kartky:
                            zhahy.append(f"{rel}:{ln}: немає картки К{int(n)}")
                for m in RE_DODATOK.finditer(ryadok):
                    b = KYR.get(m.group(1), m.group(1))
                    de[f"додаток {b}"].append(f"{rel}:{ln}")
                    if b not in dodatky:
                        zhahy.append(f"{rel}:{ln}: немає додатка {b}")

    if "-v" in sys.argv:
        for k, v in sorted(de.items()):
            print(f"  {len(v):>3}×  {k}\n        {', '.join(v[:8])}"
                  + (f" … +{len(v) - 8}" if len(v) > 8 else ""))
        print()

    for z in zhahy:
        print(f"   • {z}")
    print(f"cross_refs: згадок {sum(len(v) for v in de.values())}, "
          f"адресатів {len(de)}, помилок {len(zhahy)}")
    return 1 if zhahy else 0


if __name__ == "__main__":
    sys.exit(main())
