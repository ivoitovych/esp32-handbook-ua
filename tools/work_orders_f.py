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

    tools/work_orders_f.py <куди> [--na-naryad 10]
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

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

SHAPKA = """# Наряд {n}: {tema} — {k} одиниць

## Що це за одиниці

До них **просто ще ніхто не дійшов**. Ні чужого висновку, ні назви
джерела — лише текст книги. Тому документ доводиться шукати, і нижче
названо той, з якого варто почати.

{kandydat}

Кандидат — здогад, не вирок. Не той — візьми інший і назви в
`dzherelo` саме той, який відкривав.

## Довідник не є джерелом для себе

Адреса з `esp32-handbook`, `ivoitovych`, `voytovych` чи шляхами
`manual/`, `kartky/`, `dodatky/` **відкидається механічно** ще до
лічби. Такий запис не рахується ані підтвердженням, ані запереченням —
це змарнована робота.

Текст книги нижче — це те, що **перевіряють**, а не те, чим
перевіряють.

## Що стається з твоєю відповіддю потім

1. **механічно** — самопосилання й вердикт без `dzherelo`
   відкидаються;
2. **дослівно** — цитату качають ще раз і шукають **підрядком** у
   названому тобою документі. Пробіли й лапки не рахуються; слова,
   числа й великі літери — рахуються;
3. **змістово** — людина судить, чи витяг підтримує твердження.

Числа минулих хвиль: із 528 заявлених підтверджень другий шар пережили
235. **Переказана цитата не дає нічого** — її просто викидають разом із
роботою, що на неї пішла.

> Чесне «шукав, не знайшов» — повноцінний результат. Воно каже, де вже
> шукали, і саме з таких записів складається те, що ми маємо право
> надрукувати.

## Вердикти

| Вердикт | Обов'язково |
|---|---|
| `pidtverdzheno` | `dzherelo` + `cytata` — дослівний рядок |
| `sperechayetsya` | `dzherelo` + `cytata` + `susidnye` — див. нижче |
| `ne_znayshov` | `dzherelo` — адреса документа, який відкривав |
| `nedosyazhne` | `dzherelo` + `potribno` — назва документа, якого бракує |
| `porada` | `chomu` — чому це судження автора, а не факт про світ |

`porada` **вимагає пояснення**: вона стверджує, що джерела не буває.
`ne_znayshov` пояснення не вимагає — він нічого не стверджує.
**Найдешевша відповідь тут та, що нічого не стверджує.**

`dzherelo` завжди починається з `https://raw.githubusercontent.com/`.

### `sperechayetsya` коштує дорожче за всі інші вердикти

За всі хвилі помічники заявили **одинадцять** суперечностей. Справжніх
серед них **нуль**; три виявилися доказами **на користь** книги.

Роди, які повторюються:

* **обірвана думка** — застереження стоїть у **наступному** реченні
  книги, а тобі його не показали;
* **суперечка про ступінь** — джерело каже «менше пам'яті», книга
  каже «різниця вирішальна»; це не заперечення;
* **не той документ** — джерело про ESP-IDF, а твердження про Arduino.

Тому `sperechayetsya` вимагає ще одного поля — **`susidnye`**: дослівно
речення книги **перед** і **після** того, яке ти спростовуєш. Вони в
наряді не надруковані, тож візьми їх із того самого розділу книги, а
якщо не маєш до них доступу — напиши `susidnye: недоступні`.

Це не перешкода, а перевірка самого себе: у більшості випадків
сусіднє речення знімає суперечність за секунду, і тоді правильний
вердикт — `pidtverdzheno` або `ne_znayshov`.

## Мережа

Досяжне лише `raw.githubusercontent.com`; усе інше — 403, **не
повторюй запит, що дав 403**.

`espressif/esp-idf` (`docs/en/…`, `components/…`, `examples/…`),
`espressif/esptool`, `espressif/arduino-esp32`,
`micropython/micropython`, `esphome/esphome`, `adafruit/*`,
`jgromes/RadioLib`, `olikraus/u8g2`, `lvgl/lvgl`, `torvalds/linux`.

Даташити мікросхем на GitHub **не лежать** — це чесне `nedosyazhne` з
полем `potribno`.

## Формат

```yaml
- odynycya: T-19-023
  verdykt: pidtverdzheno
  dzherelo: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
  cytata: |
    дослівний рядок із документа
  komentar: що саме він підтверджує
```

**YAML:** значення з `: ` або з лапки на початку — брати в одинарні лапки.

"""


def main() -> int:
    import vybirka

    p = argparse.ArgumentParser()
    p.add_argument("kudy", type=Path)
    p.add_argument("--na-naryad", type=int, default=10)
    a = p.parse_args()
    a.kudy.mkdir(parents=True, exist_ok=True)

    za: dict[str, list[dict]] = collections.defaultdict(list)
    for u in vybirka.odynyci("F"):
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
            r = [SHAPKA.format(n=n, tema=tema, k=len(ch), kandydat=kand)]
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
