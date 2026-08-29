#!/usr/bin/env python3
"""Пошук спростованих формулювань по всьому дереву.

Проходи фактчекінгу знаходять хибне твердження і виправляють його там,
де знайшли. Далі спрацьовує єдиний ненадійний механізм — пам'ять
людини: «треба ще пошукати по книзі». Рецензія 2026-08-26 показала, що
він не витримує: три виправлення прижилися в розділі й не дійшли до
картки та `docs/fakty.md`.

Цей інструмент замінює пам'ять на перевірку. Кожне спростоване
формулювання лежить у `factcheck/data/book/REFUTED.md` разом із взірцем, і
взірець шукається в **усьому** дереві — книзі, картках, додатках,
довідкових документах, реєстрі.

Наслідок для процесу: виправлення більше не може «недоїхати» тихо.
Або воно доїхало скрізь, або збірка про це скаже.

    tools/refuted.py        перевірити
    tools/refuted.py -v     показати взірці
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
# Реєстрів може бути кілька: головний і по одному на паралельного
# супровідника (`REFUTED-M2.md`). Так вони не б'ються при злитті —
# кожен пише лише у свій файл.
REYESTRY = sorted((ROOT / "factcheck").glob("REFUTED*.md"))

# Де шукаємо. Реєстр спростованого й звіти рецензій цитують хибні
# формулювання за призначенням — там вони доречні.
DE = ("kartky", "manual", "dodatky", "inserts", "docs")
NE_CHIPATY = ("factcheck/REFUTED", "reviews/", "zvyazok/")


def zapysy() -> list[dict]:
    out: list[dict] = []
    for f in REYESTRY:
        for b in re.findall(r"```yaml\n(.*?)```", f.read_text(encoding="utf-8"), re.S):
            dani = yaml.safe_load(b)
            if isinstance(dani, list):
                out += [z for z in dani if isinstance(z, dict) and z.get("zbih")]
    return out


def main() -> int:
    zap = zapysy()
    if "-v" in sys.argv:
        for z in zap:
            print(f"  {z['shcho']}\n      {z['zbih']}")
        print()

    zhahy: list[str] = []
    perevireno = 0

    for d in DE:
        kataloh = ROOT / d
        if not kataloh.exists():
            continue
        for f in sorted(kataloh.rglob("*.md")):
            rel = str(f.relative_to(ROOT))
            if any(rel.startswith(x) for x in NE_CHIPATY):
                continue
            text = f.read_text(encoding="utf-8")
            perevireno += 1
            for z in zap:
                vynyatky = z.get("vynyatky") or []
                if any(rel.startswith(str(v)) for v in vynyatky):
                    continue
                dozvil = z.get("dozvil")
                for m in re.finditer(z["zbih"], text):
                    ln = text[:m.start()].count("\n") + 1
                    if dozvil:
                        # Абзац навколо знахідки: чи названо там версію,
                        # тобто чи цитує книга стару форму свідомо.
                        pochatok = text.rfind("\n\n", 0, m.start()) + 1
                        kinec = text.find("\n\n", m.end())
                        abzac = text[pochatok:kinec if kinec > 0 else len(text)]
                        if re.search(dozvil, abzac):
                            continue
                    zhahy.append(
                        f"{rel}:{ln}: спростоване формулювання — "
                        f"{z['shcho']} (прохід {z.get('prokhid','?')})\n"
                        f"        знайдено: «{m.group(0)[:70]}»\n"
                        f"        замість:  {z.get('zamist','—')}")

    for zh in zhahy:
        print(f"   • {zh}")
    print(f"refuted: реєстрів {len(REYESTRY)}, взірців {len(zap)}, "
          f"файлів {perevireno}, знахідок {len(zhahy)}")
    return 1 if zhahy else 0


if __name__ == "__main__":
    sys.exit(main())
