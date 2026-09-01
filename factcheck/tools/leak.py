#!/usr/bin/env python3
"""Теча у взірці: коли ширину дає одна коротка альтернатива.

## Рід хиби

Взірець доказу — диз'юнкція. Якщо одна альтернатива сама чіпляє
більше, ніж усі інші разом, вона не звужує взірець, а **підміняє** його:

    доказ: «GPIO при старті не налаштований, лінія "висить"»
    zbih:  старт|завантаж|GPIO.*?висить|невідом|стан
                                                 ↑
                                        чіпляє 242 одиниці

П'ять альтернатив специфічні, і саме тому взірець не викликає підозри
при читанні. Працює ж шоста.

> Взірець ховає свою ширину в найкоротшій альтернативі. Читаєш
> найдовшу, а чіпляє найкоротша.

## Чому не досить міряти ширину цілком

`pass-07-api-rozbyvka` чіпляє 210 одиниць і **правильний**: це одна
перевірка «всі виклики API книги існують у заголовках», і вона справді
стосується всіх двохсот десяти. Ширина сама по собі не хиба.

Хиба — коли ширину дає одна коротка альтернатива, а назва доказу
обіцяє вузьке твердження. Тому міра тут відносна: **найширша
альтернатива проти суми решти**. На 1337 записах вона дає 22 — тобто
не б'є на сполох і не ловить `pass-07`.

## Наслідок, поміряний 2026-08-28

    записів із течею                              22
    одиниць, чий клас походить від течі          956
      з них лишилися б узагалі без доказу        873
      з них подані як `A`/`B` (звірено з джерелом) 237

    factcheck/tools/leak.py            перелік
    factcheck/tools/leak.py --naslidky що тримається на течах (повільніше)
    factcheck/tools/leak.py --samoperevirka  показ на навмисно зіпсованому вході
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Скільки одиниць мусить дати альтернатива, щоб вважатися течею.
# Нижче цього широка альтернатива нікому не шкодить.
MEZHA = 20


def alternatyvy(v: str) -> list[str]:
    import factcheck
    try:
        return factcheck.rozbyty_alternatyvy(v)
    except Exception:
        return [v]


def znayty(zapysy: list[dict], teksty: list[str]) -> list[dict]:
    """Записи, чия ширина тримається на одній альтернативі."""
    out = []
    for z in zapysy:
        # Тут стояло `z.get("match") or z.get("match")` — заміна за
        # рядком перейменувала **обидві половини** запасного виразу, і
        # запас перестав бути запасом, лишившись на вигляд запасом.
        # Самоперевірка це ловила й мовчала: `make check` кличе `techa`
        # без `--samoperevirka`.
        import factcheck
        v = factcheck.pole(z, "match", "zbih")
        # Запис, що переїхав на хеш, взірцем більше не чіпляє нічого.
        if not v or z.get("sha"):
            continue
        alt = alternatyvy(str(v))
        if len(alt) < 2:
            continue
        shyr: list[tuple[int, str]] = []
        for a in alt:
            try:
                rx = re.compile(a, re.S)
            except re.error:
                continue
            shyr.append((sum(1 for t in teksty if rx.search(t)), a))
        if not shyr:
            continue
        shyr.sort(reverse=True)
        naybilsha, reshta = shyr[0][0], sum(n for n, _ in shyr[1:])
        if naybilsha > MEZHA and naybilsha > reshta:
            out.append({"zapys": z, "shyryna": naybilsha, "reshta": reshta,
                        "alt": shyr[0][1]})
    out.sort(key=lambda d: -d["shyryna"])
    return out


def samoperevirka() -> int:
    """Показ на навмисно зіпсованому вході.

    Правило проєкту: перевірка, яка ніколи не спрацьовувала, не
    відрізняється від перевірки, якої немає. Тож тут будуються три
    штучні записи з відомою відповіддю.
    """
    # 40 текстів зі словом «стан» і лише 2 з конкретним «GPIO висить» —
    # саме та нерівновага, заради якої міра існує.
    teksty = (["стан лінії невідомий"] * 40 + ["GPIO висить"] * 2
              + ["SPI на 40 МГц"] * 5)
    vypadky = [
        # ширину дає коротка альтернатива, а назва обіцяє вузьке
        ("теча", {"title": "т", "match": r"GPIO.*?висить|стан"}, True),
        # обидві альтернативи однаково широкі — це просто широкий взірець,
        # інший рід, і ловить його інша перевірка
        ("рівні альтернативи",
         {"title": "р", "match": r"стан лінії|стан лінії невідомий"}, False),
        # без диз'юнкції течі не буває за означенням
        ("одна альтернатива", {"title": "о", "match": r"стан"}, False),
        # **Той самий випадок, але старими іменами.** Доти всі три
        # випадки були старими, тож самоперевірка міряла лише запасний
        # шлях — і коли запас зламався, вона показала «чисто» на течі
        # замість того, щоб упасти. Тепер міряються обидва шляхи.
        ("теча старими іменами",
         {"nazva": "т", "zbih": r"GPIO.*?висить|стан"}, True),
    ]
    global MEZHA
    stara, MEZHA = MEZHA, 5
    try:
        pomylok = 0
        for imya, z, ochik in vypadky:
            spraviy = bool(znayty([z], teksty))
            znak = "✓" if spraviy == ochik else "✗"
            if spraviy != ochik:
                pomylok += 1
            print(f"  {znak} {imya:<22} очікували "
                  f"{'течу' if ochik else 'чисто'}, дістали "
                  f"{'течу' if spraviy else 'чисто'}")
    finally:
        MEZHA = stara
    print("самоперевірка: усе як очікувано" if not pomylok
          else f"самоперевірка: РОЗБІЖНОСТЕЙ {pomylok}")
    return 1 if pomylok else 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--naslidky", action="store_true")
    p.add_argument("--samoperevirka", action="store_true")
    a = p.parse_args()

    if a.samoperevirka:
        return samoperevirka()

    import factcheck
    import sample

    odyn = [u for k in factcheck.ALL_CLASSES for u in sample.odynyci(k)]
    teksty = [u["tekst"] for u in odyn]
    zapysy = factcheck.zavantazhyty_dokazy()
    techi = znayty(zapysy, teksty)

    print(f"записів із течею: {len(techi)} із {len(zapysy)}\n")
    for d in techi:
        z = d["zapys"]
        print(f"  {d['shyryna']:>4} (решта {d['reshta']:>3})  "
              f"{str(z.get('_prokhid','?')):<26} "
              f"{factcheck.nazva_zapysu(z)[:46]}")
        print(f"          теча: {d['alt']!r}")

    if not a.naslidky:
        return 0

    for i, z in enumerate(zapysy):
        z["_i"] = i
    techni = {d["zapys"]["_i"] for d in techi}
    bez = [z for z in zapysy if z["_i"] not in techni]

    zmina: collections.Counter = collections.Counter()
    for u in odyn:
        kand_a = factcheck.vsi_kandydaty(zapysy, u["sha"], u["tekst"])
        kand_b = factcheck.vsi_kandydaty(bez, u["sha"], u["tekst"])
        ka = (min(kand_a, key=lambda x: factcheck.STRENGTH.get(
            factcheck.status_of(x), 99)) if kand_a else None)
        kb = (min(kand_b, key=lambda x: factcheck.STRENGTH.get(
            factcheck.status_of(x), 99)) if kand_b else None)
        if ka != kb:
            zmina[(ka, kb)] += 1

    vsjogo = sum(zmina.values())
    ab = sum(n for (ka, _), n in zmina.items()
             if ka in ("verbatim", "derived"))
    print(f"\nодиниць, чий клас походить від течі: {vsjogo}")
    print(f"  з них подані як звірені з джерелом "
          f"(`verbatim`/`derived`): {ab}")
    for (ka, kb), n in zmina.most_common():
        print(f"    {ka} → {kb or 'без доказу'}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
