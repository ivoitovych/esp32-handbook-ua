#!/usr/bin/env python3
"""Суцільний прохід: наряди на **всю** решту, згруповані за темою.

## Навіщо окремо від `sample.py`

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

    tools/sweep.py <файл-переліку> <куди>   наряди по 10 пакетів
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
#
# **Порожній рядок означає «кандидата немає», і пакет так і скаже.**
# Перша редакція мовчки не друкувала рядок про кандидата, тимчасом як
# шапка обіцяла його «для кожного пакета». Помічник, що дістав такий
# наряд, відмовився працювати — і мав рацію. Це той самий дефект, що
# раніше знайшли в `vorota` й `mira_f`: **документ обіцяє те, чого код
# не робить.** Обіцянка мусить або справджуватися, або бути знята.
TEMY: dict[str, tuple[str, str]] = {
    "05": ("основи електроніки", ""),
    "06": ("живлення", "I:docs/en/api-reference/system/power_management.rst"),
    "07": ("GPIO", "I:components/esp_driver_gpio/include/driver/gpio.h"),
    "08": ("плати розробки", "I:docs/en/hw-reference/index.rst"),
    "09": ("підключення до комп'ютера", "I:docs/en/get-started/establish-serial-connection.rst"),
    "11": ("ESP-IDF: збирання й конфігурація", "I:docs/en/api-guides/build-system.rst"),
    "12": ("Arduino на ESP32", "A:docs/en/guides/core_debug.rst"),
    "13": ("PlatformIO", ""),
    "14": ("швидкі шляхи", ""),
    "16": ("завантаження й boot", "I:docs/en/api-guides/startup.rst"),
    "17": ("esptool", "E:docs/en/esptool/basic-commands.rst"),
    "18": ("розділи флешу", "I:docs/en/api-guides/partition-tables.rst"),
    "19": ("OTA", "I:docs/en/api-reference/system/ota.rst"),
    "20": ("резервні копії", "E:docs/en/esptool/basic-commands.rst"),
    "21": ("серійна прошивка", "E:docs/en/esptool/basic-commands.rst"),
    "25": ("журнал і монітор", "I:docs/en/api-guides/tools/idf-monitor.rst"),
    "30": ("пам'ять", "I:docs/en/api-reference/system/mem_alloc.rst"),
    "33": ("периферія в коді", "I:docs/en/api-reference/peripherals/index.rst"),
    "35": ("I²C", "I:docs/en/api-reference/peripherals/i2c.rst"),
    "36": ("SPI", "I:docs/en/api-reference/peripherals/spi_master.rst"),
    "37": ("1-Wire і DS18B20", "I:docs/en/api-reference/peripherals/rmt.rst"),
    "42": ("ESP-NOW", "I:docs/en/api-reference/network/esp_now.rst"),
    "43": ("LoRa", "R:README.md"),
    "45": ("датчики", ""),
    "46": ("дисплеї", "U:README.md"),
    "47": ("ключі й навантаження", ""),
    "50": ("безпека", "I:docs/en/security/flash-encryption.rst"),
    "58": ("журналювання у виробі", "I:docs/en/api-reference/system/log.rst"),
    "59": ("проєкт: монітор", ""),
    "60": ("проєкт: логер", ""),
    "61": ("проєкт: канал", ""),
    "62": ("проєкт: керування", ""),
    "63": ("проєкт: міст", ""),
}
BAZY = {
    "I": "https://raw.githubusercontent.com/espressif/esp-idf/master/",
    "E": "https://raw.githubusercontent.com/espressif/esptool/master/",
    "A": "https://raw.githubusercontent.com/espressif/arduino-esp32/master/",
    "R": "https://raw.githubusercontent.com/jgromes/RadioLib/master/",
    "U": "https://raw.githubusercontent.com/olikraus/u8g2/master/",
}

BEZ_KANDYDATA = (
    "**Документа-кандидата немає.** Тему не покриває жодне зі сховищ, "
    "названих у шапці, настільки прямо, щоб назвати файл наперед. Обери "
    "документ сам із того переліку й назви в `dzherelo` саме той, який "
    "відкривав. Якщо жоден не підходить — це чесне `nedosyazhne` з назвою "
    "документа, який був би потрібен."
)


def tema_dlya(fayl: str) -> tuple[str, str]:
    """Тема й документ-кандидат. Назва файлу книги назовні не йде."""
    pref = fayl.split("-")[0]
    tema, dok = TEMY.get(pref, ("", ""))
    if not tema:
        tema = "різне"
    if not dok:
        return tema, ""
    baza, shlyah = dok.split(":", 1)
    return tema, BAZY[baza] + shlyah

SHAPKA_RAMKA = """# Наряд {nomer}: суцільний прохід — {skilky} одиниць

**Генерується** `tools/sweep.py`. Це **не** вибірка: це решта, яку
досі ніхто не дивився.
"""

# Спільні правила беруться з `factcheck/TASK-SPEC.md`, а не
# переписуються тут. До появи спеки їх було сім копій, і
# збігалося в усіх сімох рівно одне правило з восьми.
SHAPKA_BLOKY = ['ORIENTATION', 'VERBATIM', 'HONEST-MISS', 'NETWORK', 'STUB', 'NO-SELF-REFERENCE', 'VERDICTS-EXTERNAL', 'ABSENCE', 'FORMAT']


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



def main() -> int:
    import split_queue
    import sample

    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    kudy = Path(sys.argv[1])
    kudy.mkdir(parents=True, exist_ok=True)

    e1, _e2, _s1, _s2 = split_queue.podil_e()
    moyi = set(e1)
    vsi = sample.odynyci("E") + sample.odynyci("F")

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
        r = [shapka(nomer=naryadiv, skilky=skilky).rstrip("\n"), ""]
        for j, (fayl, odyn) in enumerate(chastyna, 1):
            tema, dok = tema_dlya(fayl)
            r.append(f"\n## Пакет {j} · тема: {tema}\n")
            r.append(f"Документ-кандидат: `{dok}`\n" if dok
                     else BEZ_KANDYDATA + "\n")
            for u in odyn:
                r.append(f"**`{u['id']}`**\n")
                r.append(f"> {u['tekst']}\n")
        (kudy / f"naryad-{naryadiv:03d}.md").write_text(
            "\n".join(r) + "\n", encoding="utf-8")

    print(f"sweep: одиниць {sum(len(p) for _f, p in pakety)}, "
          f"пакетів {len(pakety)}, нарядів {naryadiv} → {kudy}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
