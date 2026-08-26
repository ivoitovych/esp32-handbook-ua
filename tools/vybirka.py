#!/usr/bin/env python3
"""Випадкова вибірка одиниць одного класу — щоб міряти, а не збирати.

## Навіщо окремий інструмент

Штурм класу `E` брав одиниці, **відібрані рукою** як найімовірніші
носії джерела. Для здобичі це правильно: шукаєш там, де світло. Для
**міри** це нікуди не годиться — вибірка відібрана саме за тією
ознакою, яку збираєшся виміряти, і будь-який відсоток із неї завищений
за побудовою.

А міра тут потрібна окремо від здобичі. Клас `E` присвоюється
**механічно**: проза, у якій немає ані цифри, ані ідентифікатора в
зворотних лапках, ані назви чипа чи протоколу, ані одиниці виміру
словами. Це правило про **брак сигналу**, а книга друкує про нього
інше — «поза зовнішньою звіркою: редакційне рішення, порада». Два різні
твердження. Наскільки вони розходяться, з відібраної рукою вибірки
не видно.

## Чому насіння записується в сам наряд

Вибірку можна перекидати доти, доки число не сподобається. Захист від
цього один: насіння й спосіб добору лежать у файлі поряд із
результатом, тож будь-хто повторить добір і отримає ті самі одиниці.
Перекинута вибірка одразу видно як інше насіння.

Тому насіння тут **не** береться з годинника.

    tools/vybirka.py E 150          наряд на 150 одиниць класу E
    tools/vybirka.py E 150 --nasinnya 7   інше насіння, явно назване
"""
from __future__ import annotations

import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("manual", "kartky", "dodatky", "inserts")
CIL = ROOT / "factcheck" / "NARYAD-vybirka.md"

NASINNYA = 20260826

RE_ZAHOLOVOK = re.compile(
    r"<!-- fc id:(?P<id>[\w-]+) sha:\w+ src:(?P<src>[^\s]+) klas:(?P<klas>\w+) -->")
RE_CYTATA = re.compile(r"^> (?P<t>.+)$", re.M)


def odynyci(klas: str) -> list[dict]:
    """Усі одиниці заданого класу, у сталому порядку.

    Сталість тут не косметика: `glob` і так сортується, але без
    `sorted()` порядок залежав би від файлової системи — і те саме
    насіння давало б різні вибірки на різних машинах.
    """
    out: list[dict] = []
    for grupa in GRUPY:
        katalog = ROOT / "factcheck" / grupa
        if not katalog.exists():
            continue
        for f in sorted(katalog.glob("*.md")):
            tekst = f.read_text(encoding="utf-8")
            shmatky = RE_ZAHOLOVOK.split(tekst)
            # `split` із групами віддає [до, id, src, klas, після, ...]
            for i in range(1, len(shmatky), 4):
                ident, src, k = shmatky[i], shmatky[i + 1], shmatky[i + 2]
                if k != klas:
                    continue
                tilo = shmatky[i + 3]
                m = RE_CYTATA.search(tilo)
                out.append({"id": ident, "src": src,
                            "tekst": m.group("t").strip() if m else ""})
    return out


ZAHOLOVOK = """# Наряд: випадкова вибірка класу `{klas}`

**Генерується** `tools/vybirka.py`. Насіння **{nasinnya}**, з популяції
**{vsyoho}** одиниць відібрано **{skilky}**.

## Що саме міряємо

Не «чи можна знайти джерело, якщо старатися» — це міряв штурм, і його
вибірка була відібрана рукою під відповідь.

Тут питання інше: **яка частка класу `E` справді не має зовнішнього
референта.** Клас присвоюється механічно, за браком цифри чи
ідентифікатора в тексті. Твердження «підтягувальний резистор потрібен
завжди» цифри не має — і потрапляє в `E`, хоча це перевірюване
твердження про світ, і воно може бути хибним.

Вибірка випадкова саме для цього: відсоток із неї можна переносити на
всі {vsyoho} одиниць, а відсоток зі штурму — не можна.

## Три дозволені відповіді, і третя не гірша за першу

| Вердикт | Коли |
|---|---|
| `znayshov` | зовнішнє джерело є: адреса + **дослівна** цитата |
| `ideya` | джерела не дістав, але можу назвати документ, де воно було б |
| `spravdi-e` | зовнішнього референта справді немає: це позиція автора |

`spravdi-e` — **повноцінна відповідь і повноцінний результат.** Ми
міряємо частку, а не збираємо здобич: підтвердити, що клас поставлено
правильно, тут рівно так само цінно, як спростувати. Вигадане джерело
псує міру сильніше, ніж чесне «немає».

Цитату **не переказувати й не набирати з пам'яті**: усе, що в полі
`cytata`, звіряється підрядком у самому документі, і переказ туди не
проходить.

"""


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    klas = sys.argv[1].upper()
    skilky = int(sys.argv[2])
    nasinnya = NASINNYA
    if "--nasinnya" in sys.argv:
        nasinnya = int(sys.argv[sys.argv.index("--nasinnya") + 1])

    vsi = odynyci(klas)
    if not vsi:
        print(f"vybirka: одиниць класу {klas} не знайдено")
        return 1
    skilky = min(skilky, len(vsi))
    vybir = random.Random(nasinnya).sample(vsi, skilky)
    vybir.sort(key=lambda z: z["id"])

    r = [ZAHOLOVOK.format(klas=klas, nasinnya=nasinnya,
                          vsyoho=len(vsi), skilky=skilky).rstrip("\n"), ""]
    for i, z in enumerate(vybir):
        if i % 8 == 0:
            r.append(f"\n## Пакет {i // 8 + 1}\n")
        r.append(f"**`{z['id']}`** · `{z['src']}`\n")
        r.append(f"> {z['tekst']}\n")
    CIL.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"vybirka: клас {klas}, популяція {len(vsi)}, вибірка {skilky}, "
          f"насіння {nasinnya} → {CIL.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
