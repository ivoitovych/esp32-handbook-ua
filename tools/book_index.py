#!/usr/bin/env python3
"""Предметний покажчик: терміни книги з друкованими номерами сторінок.

Навіщо. Довідник на чотириста сторінок без покажчика на папері майже
некерований: у PDF працює пошук, у надрукованій книзі — ні. А ця книга
призначена саме для паперу: її беруть на стіл поруч із платою.

## Звідки беруться номери сторінок

Не з джерел книги — там номерів немає й бути не може, доки її не
зверстано. Тому покажчик будується **з готового PDF**: кожна сторінка
дає свій текст і свою друковану колонцифру.

Двопрохідне збирання: зібрати книгу без покажчика → витягти номери →
згенерувати покажчик → зібрати ще раз. Пагінація тіла при цьому не
змінюється, бо покажчик стоїть **в кінці**.

## Що потрапляє в покажчик

Не всі слова, а ті, які шукають у довіднику: номери пінів, назви чипів
і модулів, команди, виклики API, позначення мікросхем і терміни ремесла.
Кожна група має свій взірець — і кожен взірець тут навмисно вужчий, ніж
міг би бути.

Терміни, що трапляються більш ніж на `MEZHA_STORINOK` сторінках,
відкидаються: покажчик, який на слово «GPIO» дає сорок номерів, не
допомагає, а заважає. Такі слова шукають не через покажчик, а через
зміст.

    tools/book_index.py            згенерувати dodatky/z-pokazhchyk.md
    tools/book_index.py --pokazaty показати, що знайдено, без запису
"""
from __future__ import annotations

import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNYHA = ROOT / "build" / "esp32-dovidnyk.pdf"
CIL = ROOT / "dodatky" / "z-pokazhchyk.md"

MEZHA_STORINOK = 20
MIN_DOVZHYNA = 3

# Групи термінів. Порядок важливий: перший взірець, що збігся, вирішує,
# як термін нормалізується.
VZIRTSI = [
    # Піни — головне, що шукають у цій книзі.
    re.compile(r"\bGPIO\s?\d{1,2}\b"),
    # Сімейства й модулі.
    re.compile(r"\bESP32-[A-Z0-9-]+\b|\bESP8266\b|\bWROOM(?:-\d+\w*)?\b"
               r"|\bWROVER\w*\b|\bDevKit\w*\b|\bSuperMini\b"),
    # Виклики API та константи ESP-IDF.
    re.compile(r"\b(?:esp|gpio|nvs|i2c|spi|uart|twai|adc|dac|ledc|rmt|"
               r"pcnt|mcpwm|httpd|wifi)_[a-z0-9_]{3,}\b"),
    re.compile(r"\b(?:CONFIG|ESP_ERR|ESP_LOG|MALLOC_CAP|SOC)_[A-Z0-9_]{3,}\b"),
    re.compile(r"\bx(?:Task|Queue|Semaphore|EventGroup)[A-Za-z]+\b"
               r"|\bvTask[A-Za-z]+\b|\bportYIELD_FROM_ISR\b"),
    # Команди.
    re.compile(r"\b(?:write-flash|read-flash|erase-flash|verify-flash|"
               r"flash-id|read-mac|merge-bin|elf2image|chip-id|"
               r"espefuse|espsecure|menuconfig|monitor|set-target|"
               r"fullclean|size-components)\b"),
    # Позначення мікросхем і модулів: літери + цифри.
    re.compile(r"\b(?:[A-Z]{2,}\d{2,}[A-Z0-9]*|MAX\d+|SX\d+|CP\d+|CH\d+|"
               r"TP\d+|AMS\d+|MCP\d+|PCF\d+|SSD\d+|ILI\d+|ST\d{4})\b"),
]

# Терміни ремесла — цих взірцем не вловиш, бо це звичайні слова. Перелік
# короткий і ручний: у покажчик іде те, що читач справді шукатиме, коли
# зіткнеться з проблемою.
RUCHNI = [
    "brownout", "watchdog", "backtrace", "strapping", "bootloader",
    "coredump", "eFuse", "PSRAM", "OTA", "NVS", "JTAG", "PWM", "DMA",
    "I²C", "I²S", "SPI", "UART", "TWAI", "RS-485", "Modbus", "LoRa",
    "ESP-NOW", "MQTT", "FreeRTOS", "ESP-IDF", "PlatformIO", "MicroPython",
    "ESPHome", "Arduino", "деку́плінг", "підтягування", "дільник напруги",
    "конвертер рівнів", "паразитне живлення", "гальванічна розв'язка",
    "антидребезг", "мультиплексор", "термопара", "енкодер", "серво",
    "таблиця розділів", "серійна прошивка", "паспорт виробу",
    "заводські налаштування", "деградація акумулятора",
]

RE_KOLONCYFRA = re.compile(r"^\d{1,3}$")


def klyuch_sortuvannya(s: str) -> tuple:
    """Українська абетка спершу, латина після, цифри в кінці.

    Просте `sorted()` кидає кирилицю після латини за кодами Unicode, і
    покажчик виходить із двома окремими абетками без пояснення чому.
    """
    b = s.lstrip("`").lstrip()
    perш = b[:1]
    if perш.isdigit():
        rozryad = 2
    elif "А" <= perш.upper() <= "Я" or perш.upper() in "ІЇЄҐ":
        rozryad = 0
    else:
        rozryad = 1
    return (rozryad, unicodedata.normalize("NFKD", b).casefold())


def storinky_knyhy() -> list[tuple[int, str]]:
    """(друкована колонцифра, текст) для кожної сторінки."""
    import pymupdf

    if not KNYHA.exists():
        print(f"book_index: немає {KNYHA.relative_to(ROOT)} — спершу `make dovidnyk`")
        return []
    out = []
    with pymupdf.open(KNYHA) as d:
        for st in d:
            t = st.get_text()
            ryadky = [r.strip() for r in t.strip().split("\n") if r.strip()]
            nomer = None
            for r in (ryadky[-1:] + ryadky[:1]) if ryadky else []:
                if RE_KOLONCYFRA.match(r):
                    nomer = int(r)
                    break
            if nomer is not None:
                out.append((nomer, t))
    # Покажчик збирається з **попереднього** збирання, у якому він уже
    # був. Якщо його власні сторінки не відкинути, кожен термін отримає
    # ще й номер сторінки покажчика — і майже всі рядки закінчаться
    # одним і тим самим числом. Так і сталося на першому прогоні.
    for i, (_, tekst) in enumerate(out):
        if "Предметний покажчик" in tekst and i > len(out) // 2:
            return out[:i]
    return out


def zibraty() -> dict[str, set[int]]:
    znaydeno: dict[str, set[int]] = defaultdict(set)
    for nomer, tekst in storinky_knyhy():
        for vz in VZIRTSI:
            for m in vz.finditer(tekst):
                slovo = re.sub(r"\s+", "", m.group(0))
                if len(slovo) >= MIN_DOVZHYNA:
                    znaydeno[slovo].add(nomer)
        nyzhniy = tekst.lower()
        for term in RUCHNI:
            if term.lower() in nyzhniy:
                znaydeno[term].add(nomer)
    return znaydeno


def diapazony(nomery: list[int]) -> str:
    """`12, 14–17, 20` замість `12, 14, 15, 16, 17, 20`."""
    nomery = sorted(set(nomery))
    chastyny, i = [], 0
    while i < len(nomery):
        j = i
        while j + 1 < len(nomery) and nomery[j + 1] == nomery[j] + 1:
            j += 1
        chastyny.append(str(nomery[i]) if j == i
                        else f"{nomery[i]}–{nomery[j]}")
        i = j + 1
    return ", ".join(chastyny)


ZAHOLOVOK = """# Предметний покажчик {#pokazhchyk}

Номери сторінок — ті самі, що внизу сторінки.

Слова, які трапляються більш ніж на двох десятках сторінок, сюди не
входять: покажчик, який на «GPIO» дає сорок номерів, заважає більше, ніж
допомагає. Такі теми шукають у змісті.

"""


def main() -> int:
    znaydeno = zibraty()
    if not znaydeno:
        return 1
    korysni = {t: s for t, s in znaydeno.items()
               if 1 <= len(s) <= MEZHA_STORINOK}
    vidkynuto = len(znaydeno) - len(korysni)

    if "--pokazaty" in sys.argv:
        for t in sorted(korysni, key=klyuch_sortuvannya)[:60]:
            print(f"  {t:32} {diapazony(list(korysni[t]))}")
        print(f"\npokazhchyk: термінів {len(korysni)}, "
              f"відкинуто заширокі {vidkynuto}")
        return 0

    ryadky = [ZAHOLOVOK.rstrip("\n"), "", "::: pokazhchyk"]
    litera = None
    for t in sorted(korysni, key=klyuch_sortuvannya):
        persha = t.lstrip("`")[:1].upper()
        if persha != litera:
            litera = persha
            ryadky += ["", f"**{litera}**", ""]
        ryadky.append(f"{t} — {diapazony(list(korysni[t]))}")
        ryadky.append("")
    ryadky.append(":::")
    CIL.write_text("\n".join(ryadky) + "\n", encoding="utf-8")
    print(f"book_index: термінів {len(korysni)}, "
          f"відкинуто заширокі {vidkynuto}, "
          f"→ {CIL.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
