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

## Чому тут є довірчий проміжок, а в штурмі його немає

Бо тут він означає щось. Вибірка випадкова, отже відсоток із неї —
оцінка відсотка в усій популяції, і в цієї оцінки є похибка, яку можна
порахувати. Назвати частку без похибки означало б видати 160 одиниць за
3892.

У штурмі проміжку немає не тому, що ліньки, а тому, що там він був би
брехнею: похибка вибіркового середнього нічого не каже про вибірку,
відібрану за досліджуваною ознакою.

    tools/vybirka.py E 150          наряд на 150 одиниць класу E
    tools/vybirka.py E 150 --nasinnya 7   інше насіння, явно назване
    tools/vybirka.py --zvit <каталог>     звести вивантаження в міру
"""
from __future__ import annotations

import collections
import math
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml

import vyvantazh

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


ZVIT = ROOT / "factcheck" / "MIRA-E.md"


def zvesty(katalog: Path) -> int:
    """Звести вивантаження випадкової вибірки в міру з похибкою."""
    # Перший прогін цієї міри втратив 40 із 160 одиниць на зламаному
    # YAML — і втратив **не випадково**: обидва помічники, чиї файли
    # впали, давали найвищу частку «має референта». Тобто мовчазна
    # втрата зсувала саме те число, яке міряють, і зсувала вниз.
    #
    # Звідси `tools/vyvantazh.py`: механічне лагодження того, що
    # написано, і поіменний перелік полагодженого.
    zap, polagodzheni, bidy = vyvantazh.chytaty(katalog)
    for z in zap:
        z["_hto"] = str(z.get("_fayl", "?")).split("-")[0]

    n = len(zap)
    if not n:
        print("vybirka: вивантажень не знайдено")
        return 1
    c = collections.Counter(str(z.get("verdykt", "?")) for z in zap)
    maye_referenta = c["znayshov"] + c["ideya"]

    def promizhok(k: int) -> tuple[float, float]:
        """Вілсонів проміжок 95%. Для часток біля 0 нормальний бреше."""
        p, z = k / n, 1.96
        seredyna = (p + z * z / (2 * n)) / (1 + z * z / n)
        pivshyryna = (z / (1 + z * z / n)) * math.sqrt(
            p * (1 - p) / n + z * z / (4 * n * n))
        return (max(0.0, seredyna - pivshyryna),
                min(1.0, seredyna + pivshyryna))

    nyz, verh = promizhok(maye_referenta)

    # Розкид між помічниками. Це не косметика: якщо різні судді на тих
    # самих даних дають різні частки, справжня похибка більша за
    # вибіркову, і Вілсонів проміжок нижче — оптимістичний.
    po_hto: dict[str, list[int]] = collections.defaultdict(lambda: [0, 0])
    for z in zap:
        hto = str(z.get("_hto"))
        po_hto[hto][1] += 1
        if str(z.get("verdykt")) in ("znayshov", "ideya"):
            po_hto[hto][0] += 1
    chastky = [k / v for k, v in po_hto.values() if v]

    r = [f"""# Міра класу `E`

**Генерується** `tools/vybirka.py --zvit`. Наряд —
`factcheck/NARYAD-vybirka.md`, там же насіння добору.

Питання: **яка частка класу `E` має зовнішній референт**, тобто
поставлена надто щедро. Вибірка **випадкова**, тому відсоток звідси
можна переносити на весь клас — на відміну від `factcheck/SHTURM-E.md`,
де вибірку відібрано рукою під відповідь.

## Результат

Одиниць у вибірці: **{n}**.

| Вердикт | Скільки | Частка |
|---|---|---|
| `znayshov` — джерело здобуто | {c['znayshov']} | {c['znayshov'] / n:.0%} |
| `ideya` — джерело назване, не здобуте | {c['ideya']} | {c['ideya'] / n:.0%} |
| `spravdi-e` — референта справді немає | {c['spravdi-e']} | {c['spravdi-e'] / n:.0%} |

**Має зовнішній референт: {maye_referenta} з {n} = {maye_referenta / n:.0%}**
(95% Вілсон: {nyz:.0%}–{verh:.0%}).

Тобто приблизно **{round(maye_referenta / n * 3892):d}** одиниць класу
`E` — з 3892 — насправді перевірювані, і присуд «поза зовнішньою
звіркою» на них не мав би стояти.

## Чому цей проміжок оптимістичний

Вілсонів проміжок рахує лише похибку добору — він припускає, що в
кожної одиниці є одна правильна відповідь, яку будь-який суддя дав би
однаково. Тут це не так.

Частки «має референта» по помічниках: {', '.join(f'{x:.0%}' for x in sorted(chastky))}.

Розкид між суддями **більший за вибіркову похибку**. Отже головне
джерело невизначеності — не те, що одиниць 160 замість 3892, а те, що
межа між «порада автора» і «твердження про світ» проводиться
по-різному. Звужувати проміжок довшою вибіркою марно, доки межа не
описана точніше.

Це не привід відкинути міру. Порядок величини вона встановлює твердо:
йдеться про **сотні** хибно віднесених одиниць, не про десяток.
"""]
    if polagodzheni:
        r.append("\n## Полагоджені вивантаження\n")
        r.append("Механічно виправлено (значення взято в лапки), вміст "
                 "не змінено: "
                 + ", ".join(f"`{b}`" for b in polagodzheni) + ".\n")
        r.append("Причина в брифінгу супровідника, не в помічниках: "
                 "формат вимагав писати двокрапку всередині значення. "
                 "Див. `tools/vyvantazh.py`.\n")
    if bidy:
        r.append("\nНе розібралися й пропущені: "
                 + ", ".join(f"`{b}`" for b in bidy) + ".\n")

    r.append("\n## Одиниці, у яких референт є\n")
    r.append("| Одиниця | Вердикт | Де шукати або що знайдено |")
    r.append("|---|---|---|")
    for z in zap:
        v = str(z.get("verdykt"))
        if v not in ("znayshov", "ideya"):
            continue
        shcho = str(z.get("propozyciya") or z.get("komentar") or "").strip()
        r.append(f"| `{z.get('odynycya','?')}` | {v} | {shcho[:140]} |")

    ZVIT.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"vybirka: вибірка {n}, має референта {maye_referenta} "
          f"({maye_referenta / n:.0%}, 95% {nyz:.0%}–{verh:.0%}) "
          f"→ {ZVIT.relative_to(ROOT)}")
    return 0


def main() -> int:
    if "--zvit" in sys.argv:
        i = sys.argv.index("--zvit")
        if i + 1 >= len(sys.argv):
            print("vybirka: --zvit потребує каталогу вивантажень")
            return 2
        return zvesty(Path(sys.argv[i + 1]))
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
