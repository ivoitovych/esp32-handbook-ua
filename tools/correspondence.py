#!/usr/bin/env python3
"""Перевірка листування супровідників — `zvyazok/PROTOKOL.md`.

Три речі, і всі три — про те, щоб через тиждень було видно, хто, коли і
на що відповів.

1. **Форма.** Ім'я файлу, поле `koly` і автор мусять сходитися. Якщо
   ім'я каже одне, а заголовок інше — файл перейменували замість
   надіслати новий, і порядок подій уже не відновити.

2. **Зв'язність.** `vidpovid-na` мусить указувати на наявне
   повідомлення, і відповідь не може передувати тому, на що відповідає.

3. **Відкрите.** Питання й знахідка лишаються відкритими, доки на них
   немає відповіді. Це головне, заради чого інструмент існує: правило
   «знахідка без реакції — незавершена робота» тут стає перевіркою, а не
   доброю волею.

Вихід: 1 — порушено форму або зв'язність; 0 — усе гаразд. Відкриті
повідомлення самі по собі не помилка (`make check` показує їх
попередженням), але `--suvoro` робить їх помилкою — так `make
release-check` не випускає реліз із неотриманою відповіддю.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KAT = ROOT / "zvyazok"

# 2026-08-26-1408Z-m1-vidpovid-protokol-lystuvannya.md
IMYA = re.compile(
    r"^(?P<data>\d{4}-\d{2}-\d{2})-(?P<chas>\d{4})Z"
    r"-(?P<vid>m1|m2)-(?P<vyd>[a-z]+)-(?P<slug>[a-z0-9-]+)\.md$")

# Те саме, але лише до супровідника: цього досить, щоб відрізнити
# «це не повідомлення» від «це повідомлення з поламаним іменем».
POCHATOK = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}Z-(?:m1|m2)-")

VYDY = {"zavdannya", "pryynyato", "zvit",
        "pytannya", "vidpovid", "znakhidka", "rishennya"}
# Доручення без прийняття — те саме, що знахідка без реакції: видане й
# невідомо, чи дійшло. Прийняття тут не ввічливість, а єдине місце, де
# видно, що доручення зрозуміли так само, як його писали.
POTREBUYUT_VIDPOVIDI = {"zavdannya", "pytannya", "znakhidka"}
# Хто веде це дерево. Потрібно, щоб відрізнити власний борг від
# очікування на відповідь іншого супровідника.
YA = "М1"
OBOVYAZKOVI = ("vid", "komu", "koly", "vyd", "tema", "baza")
AVTOR = {"m1": "М1", "m2": "М2"}


def zagolovok(tekst: str) -> dict[str, str]:
    """Перше поле-значення з першого блоку ```yaml файлу."""
    m = re.search(r"```yaml\n(.*?)\n```", tekst, re.S)
    if not m:
        return {}
    polya: dict[str, str] = {}
    for ryadok in m.group(1).splitlines():
        ryadok = ryadok.split("#")[0].rstrip()
        if ":" not in ryadok:
            continue
        k, _, v = ryadok.partition(":")
        polya[k.strip()] = v.strip()
    return polya


def zibraty() -> tuple[list[dict], list[str]]:
    povidomlennya: list[dict] = []
    bidy: list[str] = []
    for f in sorted(KAT.glob("*.md")):
        m = IMYA.match(f.name)
        if not m:
            # Файли протоколу й листування до нього — не повідомлення.
            #
            # Але «не повідомлення» і «повідомлення з поламаним іменем»
            # виглядали тут однаково, і друге тихо зникало з обліку.
            # Так пропав лист М2 від 2026-08-27T21:16Z: у слузі стояло
            # «перевірявся» кирилицею, `slug` бере лише `[a-z0-9-]`, і
            # знахідка про шар 1 не потрапила ні в «чекаємо», ні в
            # «борг», ні навіть у порушення форми. Виявилося це лише
            # тому, що відповідь на нього не знайшла адресата.
            #
            # Тому: усе, що починається як повідомлення (дата, час, `Z`,
            # супровідник), але далі не збігається, — порушення форми.
            if POCHATOK.match(f.name):
                bidy.append(
                    f"{f.name}: ім'я починається як повідомлення, але не "
                    "збігається з формою (у слузі лише `a-z0-9-`) — "
                    "лист не потрапляє в облік узагалі")
            continue
        z = zagolovok(f.read_text(encoding="utf-8"))
        if not z:
            bidy.append(f"{f.name}: немає заголовка ```yaml")
            continue
        brak = [k for k in OBOVYAZKOVI if not z.get(k)]
        if brak:
            bidy.append(f"{f.name}: немає полів {', '.join(brak)}")
            continue

        ochik = f"{m.group('data')}T{m.group('chas')[:2]}:{m.group('chas')[2:]}Z"
        if z["koly"] != ochik:
            bidy.append(
                f"{f.name}: `koly: {z['koly']}` не збігається з іменем "
                f"(мало б бути {ochik})")
        if z["vid"] != AVTOR[m.group("vid")]:
            bidy.append(
                f"{f.name}: `vid: {z['vid']}` не збігається з іменем "
                f"({AVTOR[m.group('vid')]})")
        if z["vyd"] != m.group("vyd"):
            bidy.append(
                f"{f.name}: `vyd: {z['vyd']}` не збігається з іменем "
                f"({m.group('vyd')})")
        if z["vyd"] not in VYDY:
            bidy.append(
                f"{f.name}: вид `{z['vyd']}` невідомий; "
                f"є {', '.join(sorted(VYDY))}")

        # Видимий відбиток дублює заголовок навмисне: заголовок читає
        # машина, відбиток — людина. Звіряємо, щоб вони не розійшлися.
        vidb = f"**{z['vid']} → {z['komu']}**"
        tilo = f.read_text(encoding="utf-8")
        ryadok = next((r for r in tilo.splitlines() if r.startswith(vidb)), None)
        if ryadok is None:
            bidy.append(
                f"{f.name}: немає видимого відбитка — рядка, що починається "
                f"з `{vidb}`")
        elif z["koly"] not in ryadok or z["vyd"] not in ryadok:
            bidy.append(
                f"{f.name}: видимий відбиток розійшовся із заголовком "
                f"({z['koly']}, {z['vyd']})")

        zmin = z.get("zminyuye", "-").strip() or "-"
        if zmin != "-" and z["vyd"] != "zavdannya":
            bidy.append(
                f"{f.name}: `zminyuye` має сенс лише для `zavdannya`")

        povidomlennya.append({
            "imya": f.stem, "fayl": f.name, "koly": ochik,
            "vid": z["vid"], "vyd": z["vyd"], "tema": z["tema"],
            "baza": z["baza"],
            "na": z.get("vidpovid-na", "-").strip() or "-",
            "zminyuye": zmin,
        })
    return povidomlennya, bidy


def perevirka(suvoro: bool) -> int:
    povid, bidy = zibraty()
    imena = {p["imya"] for p in povid}
    chasy = {p["imya"]: p["koly"] for p in povid}

    vidpovidi: dict[str, list[dict]] = {}
    for p in povid:
        if p["na"] == "-":
            continue
        if p["na"] not in imena:
            bidy.append(
                f"{p['fayl']}: `vidpovid-na: {p['na']}` — такого "
                "повідомлення немає")
            continue
        if p["koly"] < chasy[p["na"]]:
            bidy.append(
                f"{p['fayl']}: відповідь ({p['koly']}) раніша за те, "
                f"на що відповідає ({chasy[p['na']]})")
        vidpovidi.setdefault(p["na"], []).append(p)

    for p in povid:
        if p["zminyuye"] != "-" and p["zminyuye"] not in imena:
            bidy.append(
                f"{p['fayl']}: `zminyuye: {p['zminyuye']}` — такого "
                "повідомлення немає")

    vidkryti = [p for p in povid
                if p["vyd"] in POTREBUYUT_VIDPOVIDI and p["imya"] not in vidpovidi]
    # Відкрите відкритому не рівне. Питання, надіслане **вам**, — ваш
    # борг: доки ви не відповіли, супровідник на тому боці чекає, і
    # випускати книгу через його голову не можна.
    #
    # Питання, надіслане **вами**, — не борг, а очікування. Спиняти на
    # ньому випуск означає спиняти роботу на тому, чого ви зробити не
    # можете; а ворота, які не дають нічого вдіяти, за тиждень
    # обходять — і тоді вони не спинять і справжнього боргу.
    #
    # Тому строгість рахує лише вхідні.
    nash_borh = [p for p in vidkryti if p["vid"] != YA]
    chekayemo = [p for p in vidkryti if p["vid"] == YA]

    for b in bidy:
        print(f"   ✗ {b}")

    if nash_borh:
        znak = "✗" if suvoro else "·"
        print(f"\n{znak} чекають нашої відповіді: {len(nash_borh)}")
        for p in sorted(nash_borh, key=lambda p: p["koly"]):
            print(f"    {p['koly']}  {p['vid']} → {p['vyd']}: {p['tema']}")
            print(f"        {p['fayl']}")
    if chekayemo:
        print(f"\n· надіслано, чекаємо відповіді: {len(chekayemo)}")
        for p in sorted(chekayemo, key=lambda p: p["koly"]):
            print(f"    {p['koly']}  → {p['vyd']}: {p['tema']}")

    print(f"\ncorrespondence: повідомлень {len(povid)}, "
          f"порушень форми {len(bidy)}, "
          f"наш борг {len(nash_borh)}, чекаємо {len(chekayemo)}")
    if bidy:
        return 1
    return 1 if (suvoro and nash_borh) else 0


def indeks() -> int:
    povid, _ = zibraty()
    vidpovidi: dict[str, list[dict]] = {}
    for p in povid:
        if p["na"] != "-":
            vidpovidi.setdefault(p["na"], []).append(p)

    ryadky = [
        "# Листування: покажчик\n",
        "**Генерується** `tools/correspondence.py --index`. Правити вручну нема "
        "сенсу; формат і правила — `zvyazok/PROTOKOL.md`.\n",
        "| Коли (UTC) | Від | Вид | Тема | База | Відповідь |",
        "|---|---|---|---|---|---|",
    ]
    for p in sorted(povid, key=lambda p: p["koly"]):
        vidp = vidpovidi.get(p["imya"], [])
        if vidp:
            stan = ", ".join(f"[{v['koly']}]({v['fayl']})" for v in vidp)
        elif p["vyd"] in POTREBUYUT_VIDPOVIDI:
            stan = "**відкрите**"
        else:
            stan = "—"
        ryadky.append(
            f"| [{p['koly']}]({p['fayl']}) | {p['vid']} | {p['vyd']} | "
            f"{p['tema']} | `{p['baza']}` | {stan} |")

    (KAT / "INDEX.md").write_text("\n".join(ryadky) + "\n", encoding="utf-8")
    print(f"correspondence: покажчик оновлено, повідомлень {len(povid)}")
    return 0


if __name__ == "__main__":
    if "--index" in sys.argv:
        sys.exit(indeks())
    sys.exit(perevirka("--suvoro" in sys.argv))
