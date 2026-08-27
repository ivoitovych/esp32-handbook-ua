#!/usr/bin/env python3
"""Суцільний прохід: наряди на **всю** решту, згруповані за темою.

## Навіщо окремо від `vybirka.py`

`vybirka` бере випадкову вибірку — щоб **міряти**. Тут завдання інше:
пройти все, що лишилося, по одному разу, щоб жодна одиниця не лишилася
в стані «до неї ніхто не дійшов».

Різниця не косметична. Читач у полі не має ані часу, ані мережі
розбиратися, що означає «фактчек неповний». Незакінчена робота для
нього — сигнал, що книзі можна не вірити. Перетворити «не звірено» на
«подивилися, зовнішнього джерела немає, ось де шукали» — це не менша
чесність, а більша: у другому реченні є адреса, за якою можна
перевірити нас самих.

## Чому пакет збирається за темою — і чому НЕ за «розділом книги»

Одиниці однієї теми питають про одне й те саме, тож один завантажений
документ відповідає на весь пакет. Це і швидше, і чесніше: помічник
читає джерело **цілком**, а не вихоплює рядок під конкретне твердження.

**Але тему не можна називати «розділом книги», і це куплено хвилею на
274 записи, з яких 249 виявилися посиланням на сам довідник.**

Перша редакція цього файлу писала в наряді «пакет — це один розділ
книги» й доручала «вибрати один документ на весь пакет». Найпростіший
документ, що відповідає опису «цей розділ», — **сам файл розділу**.
Помічники його й качали, з репозиторію довідника.

Заборона «книга не є джерелом для себе» стояла в тому ж наряді. Не
втримала — як не втримувала жодного разу з трьох.

Тому тут: тема називається **предметно** («I²C», «esptool», «розділи
флешу»), назва файлу книги в наряд не потрапляє **взагалі**, і наряд
сам називає документ-кандидат, з якого починати.

    tools/prochid.py <файл-переліку> <куди>   наряди по 10 пакетів
"""
from __future__ import annotations

import collections
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

NA_PAKET = 5
PAKETIV_NA_NARYAD = 10

# Тема й документ-кандидат за префіксом файлу книги.
#
# **Ключ використовується лише тут, у генераторі. У наряд потрапляє
# тільки тема й адреса.** Назва файлу книги не пишеться в наряд ніколи:
# саме вона перетворила попередню хвилю на 249 самопосилань.
TEMY: dict[str, tuple[str, str]] = {
    "05": ("основи електроніки", ""),
    "06": ("живлення", ""),
    "07": ("GPIO", "components/esp_driver_gpio/include/driver/gpio.h"),
    "08": ("плати розробки", "docs/en/hw-reference/index.rst"),
    "09": ("підключення до комп'ютера", "docs/en/get-started/establish-serial-connection.rst"),
    "11": ("ESP-IDF: збирання й конфігурація", "docs/en/api-guides/build-system.rst"),
    "12": ("Arduino на ESP32", ""),
    "13": ("PlatformIO", ""),
    "14": ("швидкі шляхи", ""),
    "16": ("завантаження й boot", "docs/en/api-guides/startup.rst"),
    "17": ("esptool", ""),
    "18": ("розділи флешу", "docs/en/api-guides/partition-tables.rst"),
    "19": ("OTA", "docs/en/api-reference/system/ota.rst"),
    "20": ("резервні копії", ""),
    "21": ("серійна прошивка", ""),
    "25": ("журнал і монітор", "docs/en/api-guides/tools/idf-monitor.rst"),
    "30": ("пам'ять", "docs/en/api-reference/system/mem_alloc.rst"),
    "33": ("периферія в коді", ""),
    "35": ("I²C", "docs/en/api-reference/peripherals/i2c.rst"),
    "36": ("SPI", "docs/en/api-reference/peripherals/spi_master.rst"),
    "37": ("1-Wire і DS18B20", ""),
    "42": ("ESP-NOW", "docs/en/api-reference/network/esp_now.rst"),
    "43": ("LoRa", ""),
    "45": ("датчики", ""),
    "46": ("дисплеї", ""),
    "47": ("ключі й навантаження", ""),
    "50": ("безпека", "docs/en/security/flash-encryption.rst"),
    "58": ("журналювання у виробі", ""),
    "59": ("проєкт: монітор", ""),
    "60": ("проєкт: логер", ""),
    "61": ("проєкт: канал", ""),
    "62": ("проєкт: керування", ""),
    "63": ("проєкт: міст", ""),
}
BAZA_IDF = "https://raw.githubusercontent.com/espressif/esp-idf/master/"


def tema_dlya(fayl: str) -> tuple[str, str]:
    """Тема й документ-кандидат. Назва файлу книги назовні не йде."""
    pref = fayl.split("-")[0]
    tema, dok = TEMY.get(pref, ("", ""))
    if not tema:
        tema = "різне"
    return tema, (BAZA_IDF + dok if dok else "")

SHAPKA = """# Наряд {nomer}: суцільний прохід — {skilky} одиниць

**Генерується** `tools/prochid.py`. Це **не** вибірка: це решта, яку
досі ніхто не дивився.

## Правило, яке важить більше за вердикт

**Кожна відповідь мусить назвати документ, який ти відкривав** — у полі
`dzherelo`, і ті відповіді, де нічого не знайшлося, теж.

Без цього «не знайшов» коштує нуль, і його пишуть, не відкривши нічого.
Такий запис не є ані знахідкою, ані свідченням її відсутності:
`tools/mira_f.py` відкидає його як «не дивився» ще до лічби, тобто це
змарнована робота.

> Наряд не каже, якої відповіді чекає. Він каже, що кожна відповідь
> мусить пред'явити.

## Пакет — це одна тема

Одиниці в пакеті питають про одне. Для кожного пакета нижче названо
**документ-кандидат**: почни з нього, завантаж один раз і прочитай, а
вже потім проходь одиниці. Не шукай новий документ під кожен рядок.

Кандидат — здогад, не вирок. Якщо він виявився не тим, візьми інший і
назви в `dzherelo` саме той, який відкривав.

**Джерелом ніколи не є довідник, який ти перевіряєш.** Адреса з
`esp32-handbook`, `ivoitovych` чи `voytovych` відкидається механічно
ще до лічби — такий запис не рахується ані підтвердженням, ані
запереченням, тобто це змарнована робота.

## Вердикти й що кожен вимагає

| Вердикт | Обов'язково |
|---|---|
| `pidtverdzheno` | `dzherelo` + `cytata` — дослівний рядок із документа |
| `sperechayetsya` | `dzherelo` + `cytata` — рядок, що каже **інакше** |
| `ne_znayshov` | `dzherelo` — **адреса документа, який відкривав** |
| `nedosyazhne` | `dzherelo` + код відповіді в `komentar` |

`dzherelo` завжди починається з `https://raw.githubusercontent.com/`.

**Адреса, що вказує на сам довідник** (`esp32-handbook`, `ivoitovych`,
`voytovych`, шляхи `manual/`, `kartky/`, `dodatky/`) відкидається
механічно: довідник не є джерелом для себе. Текст книги нижче — це те,
що **перевіряють**, а не те, чим перевіряють.

## Заборони

- **переказ — не цитата.** Поле `cytata` звіряється підрядком у
  завантаженому документі;
- **пам'ять — не документ.** Велика літера замість малої валить запис
  навіть при правильному факті;
- **«стандартна практика» — не джерело**;
- **знати відповідь — не підстава написати цитату.**

## Мережа

Досяжне лише `raw.githubusercontent.com`. Усе інше — 403; **не повторюй
запит, що дав 403**.

`espressif/esp-idf` (`docs/en/…`, `components/…`, `examples/…`),
`espressif/esptool`, `espressif/arduino-esp32`, `torvalds/linux`,
`esphome/esphome`, `micropython/micropython`, `adafruit/*`,
`jgromes/RadioLib`, `olikraus/u8g2`, `Bodmer/TFT_eSPI`, `lvgl/lvgl`.

Даташити мікросхем на GitHub **не лежать**. Якщо твердження про
конкретну мікросхему — це чесне `nedosyazhne` з назвою документа, який
був би потрібен.

## Формат

```yaml
- odynycya: T-35-042
  verdykt: ne_znayshov
  dzherelo: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/i2c.rst
  komentar: документ прочитано, про це в ньому не сказано

- odynycya: T-35-043
  verdykt: pidtverdzheno
  dzherelo: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/i2c.rst
  cytata: |
    дослівний рядок
  komentar: що саме він підтверджує
```

**YAML:** якщо значення містить `: ` або починається з лапки — бери все
значення в одинарні лапки.

"""


def main() -> int:
    import podil
    import vybirka

    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    kudy = Path(sys.argv[1])
    kudy.mkdir(parents=True, exist_ok=True)

    e1, _e2, _s1, _s2 = podil.podil_e()
    moyi = set(e1)
    vsi = vybirka.odynyci("E") + vybirka.odynyci("F")

    # Групуємо за розділом книги — саме це робить пакет дешевим.
    za_rozdilom: dict[str, list[dict]] = collections.defaultdict(list)
    for u in vsi:
        fayl = u["src"].split("/")[-1].split(":")[0]
        if fayl in moyi:
            za_rozdilom[fayl].append(u)

    pakety: list[tuple[str, list[dict]]] = []
    for fayl in sorted(za_rozdilom):
        odyn = za_rozdilom[fayl]
        for i in range(0, len(odyn), NA_PAKET):
            pakety.append((fayl, odyn[i:i + NA_PAKET]))

    naryadiv = 0
    for i in range(0, len(pakety), PAKETIV_NA_NARYAD):
        chastyna = pakety[i:i + PAKETIV_NA_NARYAD]
        naryadiv += 1
        skilky = sum(len(p) for _f, p in chastyna)
        r = [SHAPKA.format(nomer=naryadiv, skilky=skilky).rstrip("\n"), ""]
        for j, (fayl, odyn) in enumerate(chastyna, 1):
            tema, dok = tema_dlya(fayl)
            r.append(f"\n## Пакет {j} · тема: {tema}\n")
            if dok:
                r.append(f"Документ-кандидат: `{dok}`\n")
            for u in odyn:
                r.append(f"**`{u['id']}`**\n")
                r.append(f"> {u['tekst']}\n")
        (kudy / f"naryad-{naryadiv:03d}.md").write_text(
            "\n".join(r) + "\n", encoding="utf-8")

    print(f"prochid: одиниць {sum(len(p) for _f, p in pakety)}, "
          f"пакетів {len(pakety)}, нарядів {naryadiv} → {kudy}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
