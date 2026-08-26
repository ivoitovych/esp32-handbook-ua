#!/usr/bin/env python3
"""Перевірка номерів GPIO проти сімейств, які називає сам текст.

Причина існування. Книга описує кілька сімейств, і речення «S3-DevKitC-1
або classic DevKitC» у переліку складових — це не побажання, а **контракт
на розпіновку**. Схема під ним мусить бути дійсною для обох плат.

Так не було. Проєкт 59 радив S3 першим рядком і давав `GPIO22`, якого в
S3 не існує; проєкт 60 радив C3 і давав `GPIO22`, `GPIO23` і `GPIO34` —
жодного з них у C3 немає. Обидві помилки прожили всі рецензії, бо ніщо
не зіставляло числа з переліком плат.

Джерело істини — `SOC_GPIO_VALID_GPIO_MASK` і `SOC_GPIO_PIN_COUNT` із
`components/soc/<чип>/include/soc/soc_caps.h` ESP-IDF v5.5, звірені
проходом 17 фактчекінгу.

Область перевірки для кожного номера визначається так:
  · маркер сімейства в тому самому рядку — перевіряти лише проти нього;
  · рядок таблиці, де в заголовку названі сімейства — проти сімейства
    своєї колонки;
  · інакше — проти **всіх** сімейств, які файл називає у складових.

    tools/piny.py        перевірити
    tools/piny.py -v     показати, що визнано за область кожного рядка
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("kartky", "manual", "dodatky", "inserts")

# Дійсні номери GPIO. Джерело — soc_caps.h; коментар пояснює виняток.
SIMEYSTVA: dict[str, set[int]] = {
    # PIN_COUNT 40, маска вирізає 24 і 28–31
    "classic": set(range(40)) - {24, 28, 29, 30, 31},
    # PIN_COUNT 47, маска вирізає 22–25
    "S2": set(range(47)) - {22, 23, 24, 25},
    # PIN_COUNT 49, маска вирізає 22–25
    "S3": set(range(49)) - {22, 23, 24, 25},
    # PIN_COUNT 22 — суцільно 0…21
    "C3": set(range(22)),
    # PIN_COUNT 31
    "C6": set(range(31)),
    # PIN_COUNT 28
    "H2": set(range(28)),
}

# Як сімейство називають у тексті: маркер [[X]] і слова в переліку складових.
NAZVY = {
    "classic": ("classic", "ESP32 classic", "DevKitC V4", "WROOM-32"),
    "S2": ("S2",),
    "S3": ("S3",),
    "C3": ("C3",),
    "C6": ("C6",),
    "H2": ("H2",),
}

RE_MARKER = re.compile(r"\[\[(classic|S2|S3|C3|C6|H2)\]\]")
RE_GPIO = re.compile(r"\bGPIO_?NUM_?(\d{1,2})\b|\bGPIO\s?(\d{1,2})\b")

# Підпис прямо в коді чи схемі: «classic: GPIO21   S3: GPIO8».
RE_PIDPYS = re.compile(r"\b(classic|S2|S3|C3|C6|H2)\s*:")
# Умовна компіляція за чипом — теж область дії, і найточніша з усіх.
RE_IFDEF = re.compile(r"#\s*(?:el)?if.*CONFIG_IDF_TARGET_ESP32(S2|S3|C3|C6|H2)\b")
RE_ELSE = re.compile(r"^\s*#\s*else\b")
RE_ENDIF = re.compile(r"^\s*#\s*endif\b")


def simeystva_fajlu(text: str) -> set[str]:
    """Сімейства, які файл оголошує в переліку складових.

    Беремо тільки рядки таблиці складових: саме там стоїть обіцянка
    «працює на цьому». Згадка сімейства в прозі обіцянкою не є.
    """
    out: set[str] = set()
    for ln in text.split("\n"):
        if not ln.startswith("|"):
            continue
        nyzhche = ln.lower()
        if not any(k in nyzhche for k in ("devkit", "esp32 classic", "esp32-c", "esp32-s")):
            continue
        for sim, slova in NAZVY.items():
            if any(s.lower() in nyzhche for s in slova):
                out.add(sim)
    return out


def kolonky(zagolovok: str) -> dict[int, str]:
    """Номер колонки → сімейство, якщо заголовок таблиці їх називає."""
    out = {}
    for i, k in enumerate(zagolovok.strip().strip("|").split("|")):
        nyzhche = k.strip().lower()
        for sim, slova in NAZVY.items():
            if any(re.search(rf"(^|\W){re.escape(s.lower())}(\W|$)", nyzhche)
                   for s in slova):
                out[i] = sim
    return out


def main() -> int:
    zhahy: list[str] = []
    perevireno = 0

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            rel = str(f.relative_to(ROOT))
            fajlovi = simeystva_fajlu(text)
            zag: dict[int, str] = {}
            ostannij: str | None = None       # маркер із попереднього рядка
            ifdef: set[str] | None = None     # область від #if CONFIG_IDF_TARGET_*
            vynyatok = False                  # абзац пояснює відсутність піна
            bulo_ifdef: set[str] = set()      # що вже перебрали в цьому #if

            for ln, ryadok in enumerate(text.split("\n"), 1):
                m = RE_IFDEF.search(ryadok)
                if m:
                    ifdef = {m.group(1)}
                    bulo_ifdef |= ifdef
                    continue
                if RE_ELSE.match(ryadok) and bulo_ifdef:
                    # Гілка #else — усе, що файл обіцяє, крім уже перебраного.
                    ifdef = (fajlovi or set(SIMEYSTVA)) - bulo_ifdef
                    continue
                if RE_ENDIF.match(ryadok):
                    ifdef, bulo_ifdef = None, set()
                    continue

                if ryadok.startswith("|"):
                    if re.fullmatch(r"\|[\s|:-]+\|?", ryadok.strip()):
                        pass                      # роздільник — заголовок вище
                    elif not zag:
                        zag = kolonky(ryadok)
                else:
                    zag = {}

                # Рядок, який стверджує відсутність піна, — не помилка,
                # а якраз те попередження, заради якого перевірка існує.
                if re.search(r"не існу|немає пін|немає GPIO|бути не може|вирізає", ryadok):
                    # Виняток діє до кінця абзацу: пояснення «GPIO22 на S3
                    # немає» триває кілька рядків і повторює те саме число.
                    vynyatok = True
                    ostannij = None
                    continue
                if not ryadok.strip():
                    ostannij, vynyatok = None, False
                    continue
                if vynyatok:
                    continue

                markery_poz = [(m.start(), m.group(1))
                               for m in RE_MARKER.finditer(ryadok)]
                pidpysy = [(m.start(), m.group(1)) for m in RE_PIDPYS.finditer(ryadok)]
                nomery = [(m.start(), int(m.group(1) or m.group(2)))
                          for m in RE_GPIO.finditer(ryadok)]

                # Область для чисел цього рядка береться з попереднього
                # стану: маркер, що стоїть **правіше** числа, стосується
                # наступного речення, а не цього.
                poperednij = ostannij
                if markery_poz:
                    ostannij = markery_poz[-1][1]

                for poz, n in nomery:
                    # Область числа — найточніша з доступних, у порядку:
                    # умовна компіляція → підпис у рядку → маркер ліворуч →
                    # колонка таблиці → маркер із попереднього рядка →
                    # усе, що файл обіцяє в складових.
                    if ifdef is not None:
                        oblast, chomu = set(ifdef), "#if"
                    elif [s2 for p2, s2 in pidpysy if p2 < poz]:
                        oblast = {[s2 for p2, s2 in pidpysy if p2 < poz][-1]}
                        chomu = "підпис"
                    elif [s2 for p2, s2 in markery_poz if p2 < poz]:
                        oblast = {[s2 for p2, s2 in markery_poz if p2 < poz][-1]}
                        chomu = "маркер"
                    elif markery_poz and ryadok.startswith("|"):
                        # Рядок таблиці: мітка сімейства стоїть у першій
                        # комірці й діє на весь рядок.
                        oblast, chomu = {markery_poz[0][1]}, "рядок таблиці"
                    elif zag and ryadok.startswith("|"):
                        komirky = ryadok.strip().strip("|").split("|")
                        zsuv, i_kom = 0, 0
                        for i_kom, k in enumerate(komirky):
                            if zsuv + len(k) + 1 > poz:
                                break
                            zsuv += len(k) + 1
                        if i_kom not in zag:
                            continue
                        oblast, chomu = {zag[i_kom]}, "колонка"
                    elif poperednij:
                        oblast, chomu = {poperednij}, "абзац"
                    elif fajlovi:
                        oblast, chomu = set(fajlovi), "складові"
                    else:
                        continue

                    perevireno += 1
                    if "-v" in sys.argv:
                        print(f"  {rel}:{ln} {sorted(oblast)} ({chomu}) ← GPIO{n}")
                    for sim in sorted(oblast):
                        if n not in SIMEYSTVA[sim]:
                            zhahy.append(f"{rel}:{ln}: GPIO{n} не існує в {sim} "
                                         f"(область: {chomu} {'/'.join(sorted(oblast))})")

    for z in dict.fromkeys(zhahy):
        print(f"   • {z}")
    print(f"piny: перевірено згадок {perevireno}, помилок {len(set(zhahy))}")
    return 1 if zhahy else 0


if __name__ == "__main__":
    sys.exit(main())
