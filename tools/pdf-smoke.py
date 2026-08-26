#!/usr/bin/env python3
"""Найпростіша перевірка зібраних PDF — що вони справді книги.

Збирання може завершитися нулем і дати файл, який ніхто не відкриє: у
Typst бували випадки, коли порожній фрагмент давав документ на дві
сторінки, а помилки в консолі не було. Ця перевірка ловить саме такі
випадки — не якість верстки, а те, що результат узагалі є результатом.

Перевіряється:
  · файл існує й починається з %PDF;
  · кількість сторінок не менша за очікувану знизу;
  · розмір не менший за очікуваний знизу (порожній PDF маленький);
  · `release/BUILD.txt` збігається з відбитком поточних джерел.

Останнє важливе окремо: `release/` — це те, що бачить читач на GitHub.
Розбіжність означає, що опублікована книга не відповідає джерелам, і
помітити це без перевірки неможливо.

Порівнювати самі PDF байт у байт не можна: Typst вписує в них час
збирання, тож два збирання того самого тексту дають різні файли. Тому
звіряється не результат, а вхід — хеш джерел, який `build.py` кладе
поруч (`vidbytok()`).

    tools/pdf-smoke.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (файл, мінімум сторінок, мінімум кілобайтів)
OCHIKUVANNYA = [
    ("esp32-dovidnyk.pdf", 350, 3000),
    ("esp32-kartky.pdf", 15, 200),
    ("esp32-proekty.pdf", 20, 200),
]


def storinok(dani: bytes) -> int:
    return len(re.findall(rb"/Type\s*/Page[^s]", dani))


def main() -> int:
    zhahy: list[str] = []
    for imya, min_st, min_kb in OCHIKUVANNYA:
        b = ROOT / "build" / imya
        r = ROOT / "release" / imya
        if not b.exists():
            zhahy.append(f"{imya}: немає в build/")
            continue
        dani = b.read_bytes()
        if not dani.startswith(b"%PDF"):
            zhahy.append(f"{imya}: не схожий на PDF")
            continue
        st, kb = storinok(dani), len(dani) // 1024
        if st < min_st:
            zhahy.append(f"{imya}: сторінок {st}, очікувалося щонайменше {min_st}")
        if kb < min_kb:
            zhahy.append(f"{imya}: {kb} КБ, очікувалося щонайменше {min_kb}")
        if not r.exists():
            zhahy.append(f"{imya}: немає в release/ — опубліковане відстає")
        else:
            print(f"   ✓ {imya}: {st} с., {kb} КБ")

    # Відбиток джерел: чи зібрано опубліковане з поточного тексту.
    sys.path.insert(0, str(ROOT / "tools"))
    import importlib
    build = importlib.import_module("build")
    teper = build.vidbytok()
    rb = ROOT / "release" / "BUILD.txt"
    if not rb.exists():
        zhahy.append("release/BUILD.txt відсутній — з чого зібрано, невідомо")
    elif rb.read_text(encoding="utf-8").strip() != teper:
        zhahy.append(f"release/ зібрано з інших джерел: у ньому "
                     f"{rb.read_text(encoding='utf-8').strip()}, зараз {teper}. "
                     f"Потрібно `make release`")
    else:
        print(f"   ✓ відбиток джерел збігається: {teper}")

    for z in zhahy:
        print(f"   ✗ {z}")
    print(f"pdf-smoke: файлів {len(OCHIKUVANNYA)}, помилок {len(zhahy)}")
    return 1 if zhahy else 0


if __name__ == "__main__":
    sys.exit(main())
