#!/usr/bin/env python3
"""Витяг перевірюваних тверджень для сесії фактчекінгу.

Читання прози ловить суперечності й прогалини, але погано ловить хибне
число: око ковзає по «40 мА» і не питає, звідки воно. Цей інструмент
витягає з книги все, що взагалі можна звірити з першоджерелом, і зводить
у перелік, який проходять по пунктах.

    tools/claims.py           усе
    tools/claims.py adresy    лише шістнадцяткові адреси
    tools/claims.py chysla    числа з одиницями
    tools/claims.py komandy   командні рядки
    tools/claims.py piny      номери GPIO
    tools/claims.py api       імена функцій ESP-IDF

Групує однакові твердження: якщо число трапляється в семи місцях, це один
пункт перевірки, а не сім — і водночас видно, що правка має піти в сім
файлів.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("kartky", "manual", "dodatky", "inserts")

ODYNYCI = r"(?:мкА|мА|А|мкФ|нФ|мкс|мс|с|год|кГц|МГц|ГГц|Гц|кОм|МОм|Ом|" \
          r"В|мВ|КБ|МБ|ГБ|біт/с|кбіт/с|Мбіт/с|бод|мкА·год|мА·год|мА·с|" \
          r"°C|м|см|мм|Вт|AWG|пін(?:и|ів)?|канал(?:и|ів)?)"

RE_CHYSLO = re.compile(rf"(?<![\w.])(\d+(?:[.,]\d+)?(?:\s*[–—-]\s*\d+(?:[.,]\d+)?)?)\s*({ODYNYCI})(?![\w])")
RE_ADRESA = re.compile(r"0x[0-9A-Fa-f]{3,8}")
RE_GPIO = re.compile(r"GPIO\s?(\d{1,2})")
RE_API = re.compile(r"\b((?:esp|nvs|gpio|i2c|spi|uart|twai|ledc|adc|rmt|pcnt|"
                    r"httpd|mdns|xTask|xQueue|xSemaphore|xEventGroup|vTask|"
                    r"heap_caps|idf|mcpwm|sdmmc|led_strip)_?[a-zA-Z0-9_]*)\s*\(")
RE_KOMANDA = re.compile(r"^\s*((?:esptool|idf\.py|espefuse|pio|nvs_partition_gen|"
                        r"picocom|minicom|screen|dmesg|lsof|usermod|sudo|git|"
                        r"xtensa-|riscv32-|mklittlefs|mkspiffs)[^\n]*)$", re.M)

# Повідомлення, які книга обіцяє читачеві побачити в консолі. Окрема
# категорія, бо ціна помилки тут особлива: читач шукає рядок у своєму
# логу дослівно, і зайва кома робить пораду непридатною.
RE_POVIDOMLENNYA = re.compile(
    r"`([A-Z][^`\n]{6,}?"
    r"(?:failed|error|Error|timeout|timed out|invalid|Invalid|not |no |"
    r"prohibited|Prohibited|triggered|mismatch|overflow|corrupt|CORRUPT|"
    r"disabled|Meditation|reset|abort|panic|wdt|WDT|ESP_ERR_|E \(|W \(|"
    r"assert)[^`\n]*)`")


def fajly():
    out = []
    for g in GRUPY:
        out += sorted((ROOT / g).glob("*.md"))
    return out


def zbir(rex, tilky_kod=False, grupa=0):
    """→ {твердження: [файли]}. tilky_kod: шукати всередині блоків коду."""
    de = defaultdict(set)
    for f in fajly():
        t = f.read_text(encoding="utf-8")
        rel = str(f.relative_to(ROOT))
        if tilky_kod:
            shmatky = re.findall(r"```.*?```", t, flags=re.S)
            t = "\n".join(shmatky)
        else:
            t = re.sub(r"```.*?```", " ", t, flags=re.S)
        for m in rex.finditer(t):
            klych = m.group(grupa) if grupa else m.group(0)
            de[klych.strip()].add(rel)
    return de


def druk(nazva, de, mezha=0):
    poz = sorted(de.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    poz = [p for p in poz if len(p[1]) >= mezha] if mezha else poz
    print(f"\n══ {nazva}: унікальних {len(poz)}")
    for klych, files in poz:
        fs = sorted(files)
        de_str = ", ".join(fs[:3]) + (f" … +{len(fs) - 3}" if len(fs) > 3 else "")
        print(f"  {len(fs):>2}×  {klych:<28} {de_str}")


def main():
    shho = sys.argv[1] if len(sys.argv) > 1 else "vse"

    if shho in ("vse", "chysla"):
        de = zbir(RE_CHYSLO)
        zvedeno = defaultdict(set)
        for k, v in de.items():
            zvedeno[re.sub(r"\s+", " ", k)] |= v
        druk("числа з одиницями", zvedeno)

    if shho in ("vse", "adresy"):
        druk("шістнадцяткові адреси", zbir(RE_ADRESA))
        druk("адреси в блоках коду", zbir(RE_ADRESA, tilky_kod=True))

    if shho in ("vse", "piny"):
        druk("номери GPIO", zbir(RE_GPIO))

    if shho in ("vse", "api"):
        druk("виклики API", zbir(RE_API, tilky_kod=True, grupa=1))

    if shho in ("vse", "komandy"):
        druk("командні рядки", zbir(RE_KOMANDA, tilky_kod=True, grupa=1))

    if shho in ("vse", "povidomlennya"):
        de = zbir(RE_POVIDOMLENNYA, grupa=1)
        for f in fajly():
            for blok in re.findall(r"```.*?```", f.read_text(encoding="utf-8"),
                                   flags=re.S):
                for ln in blok.split("\n"):
                    ln = ln.strip()
                    if re.match(r"^[EWI] \(\d+\)|^Guru Meditation|"
                                r"^rst:0x|^[A-Z][a-z]+ [a-z]+ .*(failed|error)",
                                ln):
                        de[ln].add(str(f.relative_to(ROOT)))
        druk("повідомлення в консолі", de)


if __name__ == "__main__":
    main()
