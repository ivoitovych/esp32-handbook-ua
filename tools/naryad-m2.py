#!/usr/bin/env python3
"""Складач наряду М2: одиниця + КОНКРЕТНИЙ файл у кеші.

## Чому наряд складається інструментом, а не рукою

Закон М1 (`POMICHNYKY.md`): найдешевша відповідь у наряді має бути
тією, що не стверджує нічого. Інакше наряд перетворює недбалість на
неправду — його хвиля на 247 записів дала 185 відхилених саме так.

Словами цього не втримати. Втримує будова наряду:

1. **Підтвердження мусить бути підрядком названого файлу.** Не «книга
   каже те саме» — а рядок, який механічно знайдеться в
   `dzherela-kesh/ds18b20.pdf`. Переписати текст книги назад більше не
   спрацює: тексту книги в тому файлі немає.
2. **Файл названо в наряді.** Помічник не шукає документ — він його
   відкриває. Дешева модель безпечна саме тут (`POMICHNYKY.md`); там,
   де документа може не бути, вона вигадує назву.
3. **Одиниці без файлу в наряд не йдуть узагалі.** Для них
   підтвердження неможливе за побудовою, отже найдешевша відповідь —
   єдина можлива й нічого не стверджує.

Тобто наряд не забороняє брехати. Він робить брехню дорожчою за
роботу, а не дешевшою.

    tools/naryad-m2.py <скільки> <насіння> [<ім'я-хвилі>]

Ім'я хвилі стає ім'ям файлу. Без нього наряд писався в те саме місце,
і хвиля 3 затерла наряд хвилі 2 — а наряд це запис про те, ЯК здобуто
докази, тож затирати його означає втратити пояснення до них.
"""
from __future__ import annotations

import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import vybirka  # noqa: E402  — добір і читання реєстру беремо в М1

KESH = ROOT / "dzherela-kesh"

# Ключ → взірець імені файлу в кеші. Ключ шукається в тексті одиниці
# без урахування регістру; що конкретніший ключ, то раніше він стоїть.
KLYUCHI: list[tuple[str, str]] = [
    (r"\bDS18B20\b", "ds18b20"), (r"\bBME280\b", "bme280"),
    (r"\bBMP280\b", "bmp280"), (r"\bSHT3[0-9x]\b", "sht3x"),
    (r"\bSHT4[0-9x]\b", "sht4x"), (r"\bBH1750\b", "bh1750"),
    (r"\bMPU-?6050\b", "mpu6050"), (r"\bMAX6675\b", "max6675"),
    (r"\bMAX31855\b", "max31855"), (r"\bINA219\b", "ina219"),
    (r"\bINA226\b", "ina226"), (r"\bMCP23017\b", "mcp23017"),
    (r"\bMCP2515\b", "mcp2515"), (r"\bPCF8574\b", "pcf8574"),
    (r"\bSSD1306\b", "ssd1306"), (r"\bST7789\b", "st7789"),
    (r"\bILI9341\b", "ili9341"), (r"\bTP4056\b", "tp4056"),
    (r"\bDW01\b", "dw01"), (r"\bHC-?SR04\b", "hc-sr04"),
    (r"\bL298N?\b", "l298n"), (r"\bCD4051\b", "cd4051"),
    (r"\b74HC595\b", "74hc595"), (r"\b74HC165\b", "74hc165"),
    (r"\bBSS138\b", "bss138"), (r"\bIRLZ44\b", "irlz44"),
    (r"\bIRF540\b", "irf540"), (r"\bCH340\b", "ch340"),
    (r"\bCP2102\b", "cp2102"), (r"\bRFM69\b", "rfm69hcw"),
    (r"\bSX127[68]\b", "sx1276"), (r"\bNCR18650B\b", "ncr18650b"),
    (r"\b18650\b", "ncr18650b"), (r"\bATmega328\b", "atmega328p"),
    (r"\bRP2040\b", "rp2040"), (r"\bWROOM\b", "wroom-32e_esp32"),
    (r"\bI²C\b|\bI2C\b", "i2c-um10204"),
    (r"бутлоадер|bootloader", "bootloader.rst"),
    (r"\bOTA\b|відкат|rollback", "ota.rst"),
    (r"розділ(?:и|ів)? флешу|partition|таблиц\w+ розділів", "partition-tables"),
    (r"\bPSRAM\b", "external-ram.rst"),
    (r"глибок\w+ сон|light sleep|deep sleep|сон", "sleep_modes.rst"),
    (r"\bTWAI\b|\bCAN\b", "twai.rst"),
    (r"\bNVS\b", "nvs_flash.rst"),
    (r"\bLEDC\b|ШІМ|\bPWM\b", "ledc.rst"),
    (r"\bJTAG\b", "configure-builtin-jtag"),
    (r"\bSPI\b", "spi_master.rst"),
    (r"\bADC\b", "adc_oneshot.rst"),
    (r"\bDAC\b", "dac.rst"),
    (r"паніка|panic|Guru Meditation|скидання|reset", "fatal-errors.rst"),
    # Один ключ може вести до кількох файлів: документація esptool
    # розкладена на команди й глобальні опції, і твердження про
    # `esptool --port /dev/ttyUSB0 flash-id` не перевіряється жодним
    # із них поодинці. Перша хвиля дала на цьому одинадцять
    # `ne_znayshov` поспіль — не тому, що джерела немає, а тому, що
    # наряд показав половину джерела.
    (r"esptool\b|flash[_-]id|read[_-]flash|write[_-]flash|erase[_-]flash",
     "basic-commands.rst|basic-options.rst|advanced-options.rst"),
    (r"\bGPIO\b", "gpio.rst"),
    (r"\beFuse\b", "burn-efuse-cmd"),
    (r"монітор|idf\.py monitor", "idf-monitor.rst"),
    # Додано після докачування 2026-08-27. Урок дорожчий за самі ключі:
    # завантажити документ мало. Я докачав тринадцять даташитів, і
    # число одиниць «з файлом у кеші» не зрушило взагалі — бо ключа
    # для них не було, і підбір їх не бачив. Кеш і підбір — це одна
    # річ у двох місцях, і поповнювати треба обидва.
    (r"\bESP8266\b|\bESP-12\b|\bESP-01\b", "esp8266"),
    (r"\bESP32-S3-WROOM-1\b", "esp32-s3-wroom-1"),
    (r"\bESP32-C3-MINI-1\b", "esp32-c3-mini-1"),
    (r"\bESP32-WROVER\b", "esp32-wrover-e"),
    (r"\bESP32-WROOM-32D\b", "esp32-wroom-32d"),
    (r"\bTCA9548A?\b", "tca9548a"),
    (r"\bULN2003A?\b", "uln2003"),
    (r"\bADS1256\b", "ads1256"),
    (r"\bESP32-P4\b", "esp32-p4"),
    (r"\bESP32-S2\b", "esp32-s2_datasheet"),
    (r"\bESP32-S3\b", "esp32-s3_datasheet"),
    (r"\bESP32-C5\b", "esp32-c5"),
    (r"ESP32-C3", "esp32-c3_datasheet|esp32c3.inc"),
]


# --- Другий закон: названий документ має бути ЗДАТНИЙ відповісти -----
#
# Хвиля 2 дала 78 «не знайшов» зі 98, і половина з них — не відсутність
# джерела, а мій хибний підбір. Ключ `GPIO` є і в твердженні про
# залізо, і в назві `gpio.rst`; збіг є, відповіді немає. Черга 1 дала
# 11 із 11 «не знайшов» саме так.
#
# Різниця, яку треба провести: посібник з API відповідає ПРО API —
# які функції, які аргументи, який порядок викликів. Твердження про
# залізо — скільки контролерів, який пін, яка напруга — там не
# описане й не має бути.

ZALIZO = re.compile(
    r"\d+\s*(?:МГц|кГц|Гц|мА|мкА|А\b|В\b|мВ|КБ|МБ|ГБ|°C|Ом|кОм|мс|мкс|нс)"
    r"|GPIO\s*\d+|пін\w*\s+\d+|розпіновк|корпус|кристал|кварц"
    r"|даташит|datasheet|модул\w+\s+(?:на|з)\b|напруг|струм|температур", re.I)

API = re.compile(
    r"`(?:esp_|xTask|vTask|nvs_|i2c_|spi_|gpio_|uart_|CONFIG_)[A-Za-z0-9_]*`"
    r"|menuconfig|Kconfig|ESP_ERROR_CHECK|виклик\w*\s+функц|аргумент", re.I)

# Документ-посібник з API впізнається за розширенням і теками ESP-IDF.
POSIBNYK = re.compile(r"\.rst$", re.I)
DANI = re.compile(r"\.(pdf|inc|csv)$|soc_caps|io_mux|spi_pins|_defs\.h$", re.I)


def prydatnyy(tekst: str, fayl: str) -> bool:
    """Чи здатен цей документ відповісти на це твердження.

    Правило одне й навмисно грубе: твердження про залізо, у якому
    немає жодної ознаки API, до посібника з API не йде. Помилка тут
    коштує одну пропущену одиницю; помилка в інший бік коштує
    помічникові повний обхід документа заради «не знайшов».
    """
    if POSIBNYK.search(fayl) and ZALIZO.search(tekst) and not API.search(tekst):
        return False
    return True


def kesh_fayly() -> list[str]:
    return sorted(p.name for p in KESH.iterdir() if p.is_file())


# Ключ, що називає ДЕТАЛЬ, завжди конкретніший за ключ, що називає
# тему. `DS18B20` каже, який саме документ відповість; `GPIO` каже
# лише, про що мова.
#
# Спершу підбір брав ПЕРШИЙ ключ, що збігся, а перелік ішов у довільному
# порядку — і загальні ключі стояли попереду. Наслідок побачив,
# докачавши тринадцять даташитів: число одиниць «з файлом у кеші»
# зрушило з 426 на 428, і лише два нових документи взагалі знайшли
# собі одиниці. Решту одинадцять перехопили `бутлоадер`, `скидання`,
# `GPIO` — ключі, що стояли вище.
#
# Ознака конкретності проста й перевірювана: у взірці є цифра,
# тобто номер деталі. Тематичні слова цифр не містять.
SPEC = re.compile(r"\d")


def pidibraty(tekst: str, fayly: list[str]) -> list[str]:
    """Файли найконкретнішого ключа, що збігся.

    Два проходи: спершу ключі з номером деталі, потім тематичні.
    Порядок усередині кожного рівня лишається як у переліку.
    """
    for riven in (True, False):
        z = poshuk_riven(tekst, fayly, riven)
        if z:
            return z
    return []


def poshuk_riven(tekst: str, fayly: list[str], spec: bool) -> list[str]:
    for vzir, chastky in KLYUCHI:
        if bool(SPEC.search(vzir)) != spec:
            continue
        if re.search(vzir, tekst, re.I):
            znaydeni = []
            for chastka in chastky.split("|"):
                for f in fayly:
                    if (chastka.lower() in f.lower() and f not in znaydeni
                            and prydatnyy(tekst, f)):
                        znaydeni.append(f)
            if znaydeni:
                return znaydeni
    return []


def main() -> int:
    skilky = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    nasinnya = int(sys.argv[2]) if len(sys.argv) > 2 else 20260827
    imya = sys.argv[3] if len(sys.argv) > 3 else "hvylya2"

    fayly = kesh_fayly()
    vsi = []
    for klas in ("C", "F"):
        for o in vybirka.odynyci(klas):
            o["klas"] = klas
            vsi.append(o)

    z_faylom = []
    bez_faylu = 0
    for o in vsi:
        f = pidibraty(o["tekst"], fayly)
        if f:
            o["fayl"] = f[0]
            o["fayly"] = f
            z_faylom.append(o)
        else:
            bez_faylu += 1

    rnd = random.Random(nasinnya)
    rnd.shuffle(z_faylom)
    vybrani = z_faylom[:skilky]

    print(f"популяція C+F: {len(vsi)}")
    print(f"  з файлом у кеші: {len(z_faylom)}")
    print(f"  без файлу (в наряд НЕ йдуть): {bez_faylu}")
    print(f"  відібрано: {len(vybrani)}, насіння {nasinnya}")

    out = ROOT / "factcheck" / ("naryad-m2-%s.yaml" % imya)
    import yaml
    out.write_text(yaml.dump(vybrani, allow_unicode=True, sort_keys=False,
                             default_flow_style=False, width=100),
                   encoding="utf-8")
    print(f"  → {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
