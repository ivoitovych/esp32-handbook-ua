#!/usr/bin/env python3
"""Поділ незвіреного між супровідниками — за досяжністю джерела.

Черга (`factcheck.py cherga`) сортує за вартістю помилки й показує сорок
рядків. Для роботи вдвох цього замало: треба знати не «що найдорожче», а
**хто це взагалі може закрити**.

Поділ тут не за темами й не за розділами, а за одним питанням: у якому
джерелі лежить відповідь.

    ESP-IDF, esptool, заголовки `soc/`   → М1, у контейнері вони є
    datasheet мікросхем, електричні дані → М2, у контейнері 403

Решта — одиниці зі слабким сигналом (згадка чипа чи терміна в лапках без
числа й ідентифікатора). Вони лишаються в `F` свідомо: серед них
переважно редакційне, але механічно відрізнити його від фактичного не
вдається, тож вони чекають на суцільні проходи, а не на поділ.

    tools/podil.py            зведення
    tools/podil.py --naryad   згенерувати factcheck/PODIL.md
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FC = ROOT / "factcheck"
GRUPY = ("manual", "kartky", "dodatky", "inserts")

# Порядок важливий: одиниця потрапляє в перший кошик, який її впізнав.
# Тому специфічне (назва мікросхеми) стоїть перед загальним (число з
# одиницею) — інакше «BME280 живиться 3.3 В» пішло б у електричні.
KOSHYKY: list[tuple[str, str, str, re.Pattern]] = [
    ("M1", "api", "виклики й константи ESP-IDF — заголовки компонентів",
     re.compile(r'`(esp_|gpio_|i2c_|spi_|uart_|nvs_|xTask|vTask|xQueue|'
                r'heap_caps|ledc_|adc_|rmt_|twai_|CONFIG_|SOC_|MALLOC_CAP|'
                r'ESP_[A-Z])')),
    ("M1", "komandy", "командний рядок esptool та idf.py",
     re.compile(r'`(esptool|idf\.py|espefuse|espsecure|otatool|parttool)\b'
                r'|`(write-flash|read-flash|erase-flash|merge-bin|chip-id|'
                r'flash-id)')),
    ("M1", "piny", "номери GPIO — заголовки soc/ і маски дійсних пінів",
     re.compile(r'GPIO\s?\d+|`IO\d+`')),
    ("M1", "adresy", "шістнадцяткові адреси й обсяги",
     re.compile(r'0x[0-9A-Fa-f]{3,}')),
    ("M1", "log", "рядки, які книга обіцяє побачити в консолі",
     re.compile(r'E \(\d|W \(\d|I \(\d|`[A-Z][A-Za-z_ ]{8,}`')),
    ("M2", "detali", "конкретні мікросхеми — datasheet виробника",
     re.compile(r'\b(BME280|BMP280|BMP180|DS18B20|DS3231|DHT11|DHT22|SHT[234]\d|'
                r'SSD1306|SH1106|ILI9341|ST7789|MAX485|MAX3232|MAX31855|MAX6675|'
                r'SN65HVD\d+|TP4056|DW01|MCP23017|MCP2515|PCF8574|PCA9685|'
                r'74HC\d+|CD4051|HC-SR04|SX12\d\d|RFM\d\d|MAX170\d\d|INA219|'
                r'ADS1115|W5500|ENC28J60|CH340|CP210\d|FT232|CH9102|AMS1117|'
                r'LM2596|MT3608|XL6009|18650|LiFePO4|AT24C\d+|24LC\d+|NEO-\d|'
                r'ATmega\d+|RP2040|STM32)')),
    ("M2", "elektro", "електричні величини — datasheet і специфікації",
     re.compile(r'\d+\s*(мА|мкА|А\b|В\b|мВ|кОм|Ом|МОм|мА·год|нФ|мкФ|пФ|Вт|'
                r'дБм|°C)')),
]

RE_F = re.compile(
    r'<!-- fc id:(?P<id>\S+) sha:\S+ src:(?P<src>[^\s:]+):(?P<ln>\d+) '
    r'klas:F -->\n### \S+ · (?P<vyd>\w+) · [^\n]*\n\n'
    r'\*\*Книга каже, дослівно:\*\*\n\n(?P<txt>(?:> [^\n]*\n)+)')


def zibraty() -> tuple[list[dict], dict[str, list[dict]]]:
    vsi: list[dict] = []
    for g in GRUPY:
        for f in sorted((FC / g).glob("*.md")):
            for m in RE_F.finditer(f.read_text(encoding="utf-8")):
                vsi.append(m.groupdict())
    rozklad: dict[str, list[dict]] = collections.defaultdict(list)
    for r in vsi:
        for hto, klyuch, _, p in KOSHYKY:
            if p.search(r["txt"]):
                rozklad[f"{hto}-{klyuch}"].append(r)
                break
        else:
            rozklad["—"].append(r)
    return vsi, rozklad


def zvedennya() -> int:
    vsi, rozklad = zibraty()
    print(f"незвіреного (клас F): {len(vsi)}\n")
    for hto, klyuch, opys, _ in KOSHYKY:
        k = f"{hto}-{klyuch}"
        print(f"  {hto}  {klyuch:9} {len(rozklad[k]):5}   {opys}")
    m1 = sum(len(v) for k, v in rozklad.items() if k.startswith("M1"))
    m2 = sum(len(v) for k, v in rozklad.items() if k.startswith("M2"))
    print(f"\n  М1 разом: {m1}    М2 разом: {m2}")
    print(f"  слабкий сигнал, поза поділом: {len(rozklad['—'])}")
    return 0


def naryad() -> int:
    vsi, rozklad = zibraty()
    m1 = sum(len(v) for k, v in rozklad.items() if k.startswith("M1"))
    m2 = sum(len(v) for k, v in rozklad.items() if k.startswith("M2"))
    r = [
        "# Поділ незвіреного між супровідниками\n",
        "**Генерується** `tools/podil.py --naryad`. Правити вручну нема "
        "сенсу.\n",
        "Поділ за одним питанням: **у якому джерелі лежить відповідь**. "
        "ESP-IDF, esptool і заголовки `soc/` дістаються з контейнера М1; "
        "datasheet мікросхем і електричні дані — ні, і це робота М2.\n",
        f"| | Кошик | Одиниць | Джерело |",
        "|---|---|---|---|",
    ]
    for hto, klyuch, opys, _ in KOSHYKY:
        r.append(f"| **{hto}** | `{klyuch}` | {len(rozklad[f'{hto}-{klyuch}'])} "
                 f"| {opys} |")
    r += [
        f"\n**М1 разом: {m1}. М2 разом: {m2}.** Поза поділом — "
        f"{len(rozklad['—'])} одиниць зі слабким сигналом: згадка чипа чи "
        "терміна в лапках без числа й ідентифікатора. Вони лишаються в `F` "
        "свідомо й чекають на суцільні проходи.\n",
    ]
    for hto, klyuch, opys, _ in KOSHYKY:
        k = f"{hto}-{klyuch}"
        if not rozklad[k]:
            continue
        r.append(f"\n## {hto} · `{klyuch}` — {len(rozklad[k])}\n")
        r.append(f"{opys.capitalize()}.\n")
        za_faylom = collections.defaultdict(list)
        for u in rozklad[k]:
            za_faylom[u["src"]].append(u)
        for src in sorted(za_faylom):
            r.append(f"\n### `{src}` — {len(za_faylom[src])}\n")
            r.append("| Твердження | Рядок | Дослівно |")
            r.append("|---|---|---|")
            for u in za_faylom[src]:
                t = " ".join(x[2:] for x in u["txt"].strip().split("\n"))
                t = t.replace("|", "\\|")[:150]
                r.append(f"| `{u['id']}` | {u['ln']} | {t} |")
    (FC / "PODIL.md").write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"factcheck/PODIL.md: М1 {m1}, М2 {m2}, поза поділом "
          f"{len(rozklad['—'])}")
    return 0


if __name__ == "__main__":
    sys.exit(naryad() if "--naryad" in sys.argv else zvedennya())
