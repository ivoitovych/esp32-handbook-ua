#!/usr/bin/env python3
"""Наряди на клас `F` — те, до чого просто ще не дійшли.

## Чим ця черга відрізняється від попередніх

`E` присвоюють за браком сигналу, `C` — коли документ названо й він
недосяжний. **`F` не означає нічого, крім «ніхто не дивився».** Тобто
тут немає ані чужого присуду, який треба спростовувати, ані назви
джерела, з якої можна почати: лише текст книги й тема розділу.

Тому наряд називає **документ-кандидат за темою**, як у суцільному
проході, — і це єдине, що в нього можна вкласти наперед.

## Що в цьому наряді обов'язкове, скільки б його не скорочували

Перевірено дослідом, не міркуванням. Скорочуючи наряд для черги з
названим джерелом, я викинув розділ про ворота — і двоє помічників зі
120 назвали джерелом сам довідник, обидва з вигаданим сховищем.
Розділ повернуто — наступна хвиля дала нуль із 85.

Отже в кожному наряді лишаються три речі:

1. довідник не є джерелом для себе;
2. **ворота існують, і сказано, що саме вони відкидають**;
3. `dzherelo` на кожен вердикт, включно з негативним.

## Випадкова вибірка проти тематичної

Тематичний добір бере лише те, для чого документ-кандидат відомий
наперед, — тобто міряє технологію на найлегших випадках черги. Для
досліду це підмінює питання: замість «як працює технологія на черзі
`F`» виходить «як вона працює там, де ми вже знаємо відповідь».

`--vypadkovo N` бере N одиниць з **усієї** черги `F`, включно з тими,
де кандидата немає. Частка «не знайшов» від цього зросте — і це не
хиба досліду, а його результат: вона й є мірою того, скільки в черзі
взагалі робочого.

**Насіння обов'язкове.** Три мої досліди виявилися невідтворними,
бо `sort -R` не записував насіння. Тут воно і в параметрі, і в
шапці кожного наряду, і перелік узятих `id` лягає поруч файлом.

    factcheck/tools/work_orders_f.py <куди> [--na-naryad 10]
    factcheck/tools/work_orders_f.py <куди> --vypadkovo 100 --nasinnya 20260828
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

IDF = "https://raw.githubusercontent.com/espressif/esp-idf/master/"
ARD = "https://raw.githubusercontent.com/espressif/arduino-esp32/master/"

# Тема й документ-кандидат за префіксом файлу книги. Назва файлу книги
# в наряд не потрапляє ніколи — саме вона колись перетворила хвилю на
# 249 самопосилань.
TEMY: dict[str, tuple[str, str]] = {
    "02": ("чипи й сімейства", IDF + "docs/en/api-reference/system/soc_caps.rst"),
    "11": ("ESP-IDF: збирання й конфігурація", IDF + "docs/en/api-guides/build-system.rst"),
    "12": ("Arduino на ESP32", ARD + "docs/en/guides/tools_menu.rst"),
    "13": ("PlatformIO", ""),
    "14": ("швидкі шляхи й вибір інструмента", ""),
    "15": ("робота без мережі", IDF + "docs/en/get-started/linux-macos-setup.rst"),
    "19": ("OTA", IDF + "docs/en/api-reference/system/ota.rst"),
    "41": ("BLE", IDF + "docs/en/api-reference/bluetooth/index.rst"),
    "42": ("ESP-NOW", IDF + "docs/en/api-reference/network/esp_now.rst"),
    "b-": ("симптоми й діагностика", IDF + "docs/en/api-guides/fatal-errors.rst"),
}

RE_DOSYAZHNE = re.compile(
    r"ESP-IDF|esptool|idf\.py|menuconfig|FreeRTOS|NVS|OTA|GPIO|I²C|SPI"
    r"|UART|Wi-Fi|BLE|ESP-NOW|partition|sdkconfig|CMake|Arduino"
    r"|MicroPython|`[a-z_]+\(\)`|`esp_[a-z_]+`", re.I)

SHAPKA_RAMKA = """# Наряд {n}: {tema} — {k} одиниць
"""

# Спільні правила беруться з `factcheck/TASK-SPEC.md`, а не
# переписуються тут. До появи спеки їх було сім копій, і
# збігалося в усіх сімох рівно одне правило з восьми.
SHAPKA_BLOKY = ['ORIENTATION', 'VERBATIM', 'HONEST-MISS', 'NETWORK', 'STUB', 'NO-SELF-REFERENCE', 'VERDICTS-EXTERNAL', 'ABSENCE', 'FORMAT']


RE_KONTEKST = re.compile(
    r"<!-- fc id:(?P<id>\S+) sha:\S+ src:\S+ klas:\S+ -->\n"
    r"### [^\n]*\n\n\*\*[^*\n]+\*\*\n\n(?P<tverd>(?:> [^\n]*\n)+)"
    r"(?:.*?\*\*Контекст\*\*\n\n(?P<og>`{3,})\n(?P<kontekst>.*?)\n(?P=og)\n)?",
    re.S)

def konteksty() -> dict[str, str]:
    """`id` одиниці → її оточення в книзі, з уже зрендерених карток.

    Береться з карток, а не з книги, навмисно: там контекст уже
    обмежено й перевірено шаром 1. Другий видобувач розійшовся б із
    першим, і картка обіцяла б оточення, якого ніхто не звіряв.
    """
    out: dict[str, str] = {}
    for grupa in ("manual", "dodatky", "kartky", "inserts"):
        for f in sorted((ROOT / "factcheck" / grupa).glob("*.md")):
            for m in RE_KONTEKST.finditer(f.read_text(encoding="utf-8")):
                k = (m.group("kontekst") or "").strip()
                if k:
                    out[m.group("id")] = k
    return out


def versiya_naryadu(rich: bool = False) -> str:
    """Відбиток усього, що бачить виконавець — вісім знаків.

    Механізм один зі спекою завдання, а не другий поруч: `rich`
    додає блок `CARD-PLACE` і оточення картки, тобто **міняє те, що
    виконавець бачить**, і мусить міняти версію. Наряд з оточенням і без
    нього — це дві різні технології, і книга прогонів має розрізняти їх,
    а не записувати різницю в шум (знахідка М2).
    """
    import task_spec
    bloky = SHAPKA_BLOKY + (["CARD-PLACE"] if rich else [])
    return task_spec.versiya(bloky, shablon=SHAPKA_RAMKA
                             + ("\n+kontekst" if rich else ""))


def shapka(**kw) -> str:
    """Наряд: рамка цієї партії плюс спільні блоки завдання.

    Підстановка **заміною**, а не `.format`: у рамці стоять
    справжні фігурні дужки ESP-IDF (`{IDF_TARGET_...}`), і
    `format` на них падає з KeyError.
    """
    import task_spec
    ramka = SHAPKA_RAMKA
    for k, v in kw.items():
        ramka = ramka.replace("{" + k + "}", str(v))
    return task_spec.sklasty(SHAPKA_BLOKY, zaholovok=ramka,
                             shablon=SHAPKA_RAMKA)



def vypadkova(a) -> int:
    """Випадкова вибірка з усієї черги `F`, з насінням і переліком."""
    import json
    import random

    import sample

    usi = sorted(sample.odynyci("F"), key=lambda u: u["id"])
    vzyato = random.Random(a.nasinnya).sample(usi, min(a.vypadkovo, len(usi)))
    (a.kudy / "vybirka.json").write_text(json.dumps(
        {"order_version": versiya_naryadu(getattr(a, "rich", False)),
         # `queue` пише і цей прогін теж: попарний режим порівнює з ним
         # клас кожної одиниці, і без нього він рахував **усі** одиниці
         # такими, що вийшли з черги — 10 із 10 у першій же пробі.
         "queue": "F", "rich_cards": bool(getattr(a, "rich", False)),
         "nasinnya": a.nasinnya, "z_cherhy": len(usi),
         "vzyato": [u["id"] for u in vzyato]},
        ensure_ascii=False, indent=1), encoding="utf-8")


def za_perelikom(a, sample) -> int:
    """Ті самі одиниці, що в попередньому прогоні.

    ## Навіщо це окремо від `--vypadkovo`

    Щоб виміряти зміну **наряду**, змінювати треба наряд і **тільки**
    його. Новий випадковий жереб змінює водночас дві речі — версію
    наряду й самі одиниці, — і різниця між прогонами стає нічийною.

    Тут вибірка береться з попереднього прогону дослівно. Порівняння
    виходить **попарним**: та сама одиниця під двома нарядами, тож
    видно не лише зсув часток, а й те, які саме одиниці змінили
    вердикт і в який бік.

    Сукупність при цьому вже інша (черга живе), і насіння тут не
    вживається взагалі — саме тому, що воно її не відтворює.
    """
    import json

    poperednye = json.loads(a.z_pereliku.read_text(encoding="utf-8"))
    treba = list(poperednye["vzyato"])
    reyestr = {}
    import factcheck
    # Не власний рядок літер: без `N` і `K` попарний прогін
    # мовчки губив би одиниці тих класів. Третій випадок
    # копії переліку класів за добу.
    for kl in factcheck.ALL_CLASSES:
        try:
            for u in sample.odynyci(kl):
                reyestr[u["id"]] = dict(u, klas=kl)
        except Exception:
            continue
    vzyato = [reyestr[i] for i in treba if i in reyestr]
    znykly = [i for i in treba if i not in reyestr]
    # Якщо попередній прогін не назвав черги, «вийшли з черги»
    # порахувати НЕМОЖЛИВО — і рахувати не треба. Порожній список
    # чесніший за число, що дорівнює розміру вибірки.
    cherha = poperednye.get("queue")
    zminyly = ([i for i in treba
                if i in reyestr and reyestr[i]["klas"] != cherha]
               if cherha else [])

    (a.kudy / "vybirka.json").write_text(json.dumps(
        {"order_version": versiya_naryadu(a.rich),
         "paired_with": str(a.z_pereliku.parent.name),
         "prev_order_version": poperednye.get("order_version"),
         "queue": poperednye.get("queue"), "sample_size": len(vzyato),
         "rich_cards": bool(a.rich),
         "units_gone": znykly, "units_left_queue": zminyly,
         "vzyato": [u["id"] for u in vzyato]},
        ensure_ascii=False, indent=1), encoding="utf-8")

    kont = konteksty() if a.rich else {}
    n = 0
    for i in range(0, len(vzyato), a.na_naryad):
        ch = vzyato[i:i + a.na_naryad]
        n += 1
        kand = ("**Документа-кандидата немає.** Ці одиниці взято "
                "**випадково** з усієї черги, а не за темою, тож жодного "
                "документа наперед не названо. Шукай сам — і якщо не "
                "знайшов, `not_found` із адресою того, що відкривав, "
                "це повноцінна відповідь.")
        r = [shapka(n=n, tema="випадкова вибірка (повтор попарно)",
                    k=len(ch), kandydat=kand),
             f"\n<!-- order_version:{versiya_naryadu(a.rich)} "
             f"paired:{a.z_pereliku.parent.name} -->\n"]
        for u in ch:
            r.append(f"\n**`{u['id']}`**\n")
            r.append(f"> {u['tekst']}\n")
            if a.rich:
                if kont.get(u["id"]):
                    r.append("\nОточення в книзі — щоб було видно, про що "
                             "саме йдеться:\n\n```\n" + kont[u["id"]]
                             + "\n```\n")
                # Версія наряду для `rich` рахує блок `CARD-PLACE`, тож
                # він мусить у наряді бути. Раніше цей шлях його не
                # ставив, а версію стемпив ту саму, що й шлях, який
                # ставить: два наряди з ОДНАКОВОЮ версією й різним
                # змістом — рівно те, чого версія й мала не допускати.
                import task_spec
                r.append("\n" + task_spec.bloky()["CARD-PLACE"] + "\n")
        (a.kudy / f"f-{n:02d}.md").write_text("\n".join(r) + "\n",
                                              encoding="utf-8")
    print(f"нарядів {n}, одиниць {len(vzyato)} (попарно з "
          f"{a.z_pereliku.parent.name}); зникли {len(znykly)}, "
          f"вийшли з черги {len(zminyly)} → {a.kudy}")
    return 0



def vypadkova(a) -> int:
    """Випадкова вибірка з усієї черги `F`, з насінням і переліком."""
    import json
    import random

    import sample

    usi = sorted(sample.odynyci("F"), key=lambda u: u["id"])
    vzyato = random.Random(a.nasinnya).sample(usi, min(a.vypadkovo, len(usi)))
    (a.kudy / "vybirka.json").write_text(json.dumps(
        {"order_version": versiya_naryadu(getattr(a, "rich", False)),
         # `queue` пише і цей прогін теж: попарний режим порівнює з ним
         # клас кожної одиниці, і без нього він рахував **усі** одиниці
         # такими, що вийшли з черги — 10 із 10 у першій же пробі.
         "queue": "F", "rich_cards": bool(getattr(a, "rich", False)),
         "nasinnya": a.nasinnya, "z_cherhy": len(usi),
         "vzyato": [u["id"] for u in vzyato]},
        ensure_ascii=False, indent=1), encoding="utf-8")

    n = 0
    for i in range(0, len(vzyato), a.na_naryad):
        ch = vzyato[i:i + a.na_naryad]
        n += 1
        kand = ("**Документа-кандидата немає.** Ці одиниці взято "
                "**випадково** з усієї черги, а не за темою, тож жодного "
                "документа наперед не названо. Шукай сам — і якщо не "
                "знайшов, `not_found` із адресою того, що відкривав, "
                "це повноцінна відповідь.")
        rich = getattr(a, "rich", False)
        r = [shapka(n=n, tema=f"випадкова вибірка (насіння {a.nasinnya})",
                    k=len(ch), kandydat=kand),
             f"\n<!-- order_version:{versiya_naryadu(rich)} "
             f"rich:{int(rich)} -->\n"]
        kont = konteksty() if rich else {}
        for u in ch:
            r.append(f"\n**`{u['id']}`**\n")
            r.append(f"> {u['tekst']}\n")
            if rich:
                # Оточення — з уже зрендерених карток, а не з книги
                # вдруге: там воно обмежене й перевірене шаром 1.
                k = kont.get(u["id"])
                if k:
                    r.append("\nОточення в книзі:\n")
                    r.append("```\n" + k + "\n```\n")
                import task_spec
                r.append("\n" + task_spec.bloky()["CARD-PLACE"] + "\n")
        (a.kudy / f"f-{n:02d}.md").write_text("\n".join(r) + "\n",
                                              encoding="utf-8")
    print(f"нарядів {n}, одиниць {len(vzyato)} з {len(usi)} у черзі F; "
          f"насіння {a.nasinnya} → {a.kudy}")
    return 0


def main() -> int:
    import sample

    p = argparse.ArgumentParser()
    p.add_argument("kudy", type=Path)
    p.add_argument("--na-naryad", type=int, default=10)
    p.add_argument("--vypadkovo", type=int, default=0,
                   help="взяти N одиниць випадково з усієї черги F")
    p.add_argument("--z-pereliku", type=Path, default=None,
                   help="take the same units as a previous run's "
                        "vybirka.json — paired comparison of task versions")
    p.add_argument("--rich-cards", action="store_true", dest="rich",
                   help="кожна картка несе своє оточення в книзі й абзац "
                        "про своє місце в потоці (М2)")
    p.add_argument("--nasinnya", type=int, default=0,
                   help="насіння; обов'язкове разом із --vypadkovo")
    a = p.parse_args()
    if a.vypadkovo and not a.nasinnya:
        p.error("--vypadkovo без --nasinnya: дослід буде невідтворний")
    a.kudy.mkdir(parents=True, exist_ok=True)

    if a.z_pereliku:
        import sample
        return za_perelikom(a, sample)

    if a.vypadkovo:
        return vypadkova(a)

    za: dict[str, list[dict]] = collections.defaultdict(list)
    for u in sample.odynyci("F"):
        if not RE_DOSYAZHNE.search(u["tekst"]):
            continue
        pref = u["src"].split("/")[-1][:2]
        if pref in TEMY:
            za[pref].append(u)

    n = 0
    for pref in sorted(za, key=lambda k: -len(za[k])):
        tema, dok = TEMY[pref]
        odyn = za[pref]
        for i in range(0, len(odyn), a.na_naryad):
            ch = odyn[i:i + a.na_naryad]
            n += 1
            kand = (f"**Документ-кандидат:** `{dok}`" if dok else
                    "**Документа-кандидата немає** — тему не покриває жодне зі "
                    "сховищ настільки прямо, щоб назвати файл наперед. Обери "
                    "сам із переліку нижче.")
            r = [shapka(n=n, tema=tema, k=len(ch), kandydat=kand)]
            for u in ch:
                r.append(f"\n**`{u['id']}`**\n")
                r.append(f"> {u['tekst']}\n")
            (a.kudy / f"f-{n:02d}.md").write_text("\n".join(r) + "\n",
                                                  encoding="utf-8")
    print(f"нарядів {n}, одиниць {sum(len(v) for v in za.values())} "
          f"→ {a.kudy}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
