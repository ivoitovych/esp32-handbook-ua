#!/usr/bin/env python3
"""Знімок прив'язок: до яких одиниць чіпляється кожен доказ **сьогодні**.

## Навіщо це існує

Формат картки міняється: одиниця перестане бути рендером
(`BME280 · Адреса → 0x76`) і стане дослівним рядком книги
(`| BME280 | `0x76`, `0x77` | … |`).

Взірці `zbih` писані під **рендер** — усі 1337 доказів, з них 1265
чіпляють саме комірки. Після зміни формату жоден із них не збігся б.

Але доказ прив'язаний не до **тексту**, а до **одиниці**. Текст —
лише спосіб її назвати. Тож якщо зафіксувати, яку одиницю кожен доказ
називає **зараз**, то після зміни можна перебудувати взірець із нового
тексту тієї самої одиниці — і **довести**, що прив'язка та сама.

> Робота не переробляється — вона переїжджає. І переїзд перевірний:
> знімок до й знімок після мають збігтися одиниця в одиницю.

## Чому знімок мусить бути **до**, а не після

Після зміни формату старі взірці не збігаються ні з чим, і питати
«а що воно чіпляло?» буде нікого. Знімок — єдиний носій цього знання,
і він мусить лежати в git до того, як щось зміниться.

Це те саме, на чому я вже спіймався сьогодні: пересадив хвилю, стерши
файли попередньої, і 335 доказів стали 324. Тоді врятував `git`. Тут
рятувати буде нічому — рендер зникне з дерева зовсім.

## Чому якір — вміст, а не номер

Перший знімок писано за `id` (`T-20-050`), і на першому ж повному
перегенеруванні реєстру він показав **34 докази, що «загубили»
одиниці**. Жодної втрати не було.

`id` — це `T-<файл>-<порядковий номер>`. Він зсувається від будь-якої
правки книги **вище** за одиницю: я виправив абзац у `20-bekap.md`, і
все, що нижче, поїхало на один номер. Взірці доказів чіпляли ті самі
речення — але вже під іншими номерами, і звіряння за номерами назвало
це втратою.

Переклад тих самих прив'язок у `sha` (хеш нормалізованого тексту
одиниці) дав **0 із 1337 із втратою**.

> Номер — адреса, за якою одиницю сьогодні знайти. Хеш — те, чим вона
> є. Знімок мусить триматися за друге: інакше він репетує на кожну
> правку книги, а на такий сигнал перестають дивитися — і справжню
> втрату пропустять разом з рештою.

Той самий закон уже записаний про картку (номер рядка — локатор, не
якір). Тут він виявився вдруге, з іншого боку, і коштував півгодини
розбору. Тож він стоїть у двох місцях навмисно.

    tools/znimok.py <куди.json>          зняти (за `sha`)
    tools/znimok.py <куди.json> --zvirty звірити з поточним станом
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

# `T-45-001` — номер одиниці; `f98283f2` — хеш її вмісту. За першим
# символом видно, у чому писано знімок.
RE_ID = re.compile(r"[A-Z]-\d+-\d+")


def zibraty(za: str = "sha") -> dict[str, list[str]]:
    """Ключ — `файл-доказу::назва`, значення — впорядковані якорі одиниць.

    Якір — `sha`, а не `id`. Про різницю — у docstring модуля, розділ
    «Чому якір — вміст, а не номер».
    """
    import factcheck
    import vybirka

    odyn = [u for k in factcheck.USI_KLASY for u in vybirka.odynyci(k)]

    # Ключ запису мусить пережити перевпорядкування файлу, тож у ньому
    # стоїть порядковий номер: назви в межах файлу повторюються, і без
    # номера два докази злилися б в один.
    zapysy: list[dict] = []
    for f in sorted((ROOT / "factcheck" / "dokazy").glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for i, r in enumerate(z):
            if not isinstance(r, dict):
                continue
            r["_znimok_klyuch"] = f"{f.name}::{i}::{str(r.get('nazva'))[:60]}"
            zapysy.append(r)

    zv: dict[str, list[str]] = {k["_znimok_klyuch"]: [] for k in zapysy}
    # Питаємо **тим самим** добирачем, що й генератор реєстру, і питаємо
    # його з боку одиниці, а не запису.
    #
    # Різниця не косметична. `vsi_kandydaty` має старшинство: якщо хоч
    # один запис накриває одиницю точним `sha`, взірці інших записів на
    # неї вже не діють. Знімок, що рахував би взірці окремо, показував би
    # прив'язку, якої насправді немає, — і мовчав би саме тоді, коли
    # прив'язки переїжджають зі взірця на хеш, тобто рівно тоді, коли
    # він потрібен.
    for u in odyn:
        for z in factcheck.vsi_kandydaty(zapysy, u["sha"], u["tekst"]):
            zv[z["_znimok_klyuch"]].append(u[za])
    return {k: sorted(v) for k, v in zv.items()}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("fayl", type=Path)
    p.add_argument("--zvirty", action="store_true")
    a = p.parse_args()

    za = "sha"
    if a.zvirty and a.fayl.exists():
        zrazok = next((v[0] for v in
                       json.loads(a.fayl.read_text(encoding="utf-8")).values()
                       if v), "")
        if RE_ID.fullmatch(zrazok):
            za = "id"
            print("УВАГА: знімок писано за `id`. Номер одиниці зсувається від "
                  "будь-якої правки книги вище за неї, тож перенумерацію тут "
                  "буде показано як втрату. Звіряти варто знімок за `sha`.")

    teper = zibraty(za)
    if not a.zvirty:
        a.fayl.write_text(
            json.dumps(teper, ensure_ascii=False, indent=1, sort_keys=True),
            encoding="utf-8")
        pryv = sum(len(v) for v in teper.values())
        pusti = sum(1 for v in teper.values() if not v)
        print(f"знімок: доказів {len(teper)}, прив'язок {pryv}, "
              f"з них холостих {pusti} → {a.fayl}")
        return 0

    bulo = json.loads(a.fayl.read_text(encoding="utf-8"))
    znykly = [k for k in bulo if k not in teper]
    novi = [k for k in teper if k not in bulo]
    zminyly = {k: (bulo[k], teper[k]) for k in bulo
               if k in teper and bulo[k] != teper[k]}
    vtracheni = {k: sorted(set(v[0]) - set(v[1]))
                 for k, v in zminyly.items() if set(v[0]) - set(v[1])}

    print(f"доказів у знімку {len(bulo)}, зараз {len(teper)}")
    print(f"  зникло записів     {len(znykly)}")
    print(f"  нових записів      {len(novi)}")
    print(f"  змінили прив'язку  {len(zminyly)}")
    print(f"  **втратили одиниці** {len(vtracheni)}")
    for k, v in list(vtracheni.items())[:12]:
        print(f"     ✗ {k[:70]}\n        загубив: {', '.join(v[:6])}")
    return 1 if (vtracheni or znykly) else 0


if __name__ == "__main__":
    sys.exit(main())
