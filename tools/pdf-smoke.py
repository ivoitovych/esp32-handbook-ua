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

from repo import ROOT  # noqa: E402  (root is found, not counted)

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
    for name, min_st, min_kb in OCHIKUVANNYA:
        b = ROOT / "build" / name
        r = ROOT / "release" / name
        if not b.exists():
            zhahy.append(f"{name}: немає в build/")
            continue
        dani = b.read_bytes()
        if not dani.startswith(b"%PDF"):
            zhahy.append(f"{name}: не схожий на PDF")
            continue
        st, kb = storinok(dani), len(dani) // 1024
        if st < min_st:
            zhahy.append(f"{name}: сторінок {st}, очікувалося щонайменше {min_st}")
        if kb < min_kb:
            zhahy.append(f"{name}: {kb} КБ, очікувалося щонайменше {min_kb}")
        if not r.exists():
            zhahy.append(f"{name}: немає в release/ — опубліковане відстає")
        else:
            print(f"   ✓ {name}: {st} с., {kb} КБ")

    # Кратність 16 — вимога друкарні: аркуш складається з шістнадцяти
    # сторінок. Обсяг книги пливе від кожної правки тексту, і з'їхати з
    # кратності можна непомітно — а помітить це вже друкар, коли буде
    # пізно. Регулятор — сторінки для нотаток у `book.yaml`.
    b = ROOT / "build" / "esp32-dovidnyk.pdf"
    if b.exists():
        st = storinok(b.read_bytes())
        if st % 16:
            zhahy.append(
                f"esp32-dovidnyk.pdf: {st} сторінок, це не кратно 16 "
                f"(бракує {16 - st % 16} до {st + 16 - st % 16}). "
                f"Регулятор — `storinok:` у розділі «Нотатки» book.yaml")
        else:
            print(f"   ✓ обсяг кратний 16: {st} с. = {st // 16} аркушів")

    # Числа сторінок, надруковані в README. Репозиторій публічний, і саме
    # README — перше, що бачить читач; застаріле число там обіцяє йому
    # іншу книгу, ніж лежить поруч. Це вже траплялося: у головному
    # README стояло 400 сторінок, у `release/` — 413, а в файлі 422.
    for name, _, _ in OCHIKUVANNYA:
        b = ROOT / "build" / name
        if not b.exists():
            continue
        st = storinok(b.read_bytes())
        for readme in (ROOT / "README.md", ROOT / "release" / "README.md"):
            if not readme.exists():
                continue
            tekst = readme.read_text(encoding="utf-8")
            for line in tekst.split("\n"):
                if name not in line:
                    continue
                m = re.search(r"(\d+)\s*стор\.", line)
                if m and int(m.group(1)) != st:
                    zhahy.append(
                        f"{readme.relative_to(ROOT)}: обіцяє "
                        f"{m.group(1)} стор. для {name}, а в ньому {st}")

    # Відбиток джерел: чи зібрано опубліковане з поточного тексту.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import importlib
    build = importlib.import_module("build")
    teper = build.vidbytok()
    rb = ROOT / "release" / "BUILD.txt"
    if not rb.exists():
        zhahy.append("release/BUILD.txt відсутній — з чого зібрано, невідомо")
    else:
        lines = rb.read_text(encoding="utf-8").strip().split("\n")
        if lines[0].strip() != teper:
            zhahy.append(f"release/ зібрано з інших джерел: у ньому "
                         f"{lines[0].strip()}, зараз {teper}. "
                         f"Потрібно `make release`")
        else:
            print(f"   ✓ відбиток джерел збігається: {teper}")

        # Виготовлювач — попередження, не помилка.
        #
        # Хеш джерел доводить «зібрано з цього тексту» і не доводить
        # «зібрано так само»: ті самі джерела на іншій версії pandoc чи
        # typst дають інший PDF. Для GitHub це дрібниця; для друку — ні,
        # бо кількість сторінок задає товщину корінця.
        #
        # Розбіжність версії сама по собі ще не помилка — помилка
        # непомічена розбіжність. Тому друкуємо, а не спиняємо.
        zapysanyy = lines[1].strip() if len(lines) > 1 else None
        teperishniy = build.vygotovlyuvach()
        if zapysanyy is None:
            print("   · виготовлювача не записано — перезберіть `make release`")
        elif zapysanyy != teperishniy:
            print(f"   · виготовлювач інший: у release/ «{zapysanyy}», "
                  f"тут «{teperishniy}»")
            print("     кількість сторінок може відрізнятися; для друку "
                  "звірте з `toolchain-baseline.yaml`")
        else:
            print(f"   ✓ виготовлювач збігається: {teperishniy}")

    for z in zhahy:
        print(f"   ✗ {z}")
    print(f"pdf-smoke: файлів {len(OCHIKUVANNYA)}, помилок {len(zhahy)}")
    return 1 if zhahy else 0


if __name__ == "__main__":
    sys.exit(main())
