#!/usr/bin/env python3
"""Чи справді документ у кеші — той, за який себе видає.

## Навіщо

`tools/cache.py` перевіряє, що завантажене — справжній PDF, і цього
досить проти заглушки чи сторінки помилки. Але не проти цього:

    dzherela-kesh/bh1750.pdf
      ← https://www.pololu.com/file/0J1112/BH1750FVI.pdf
      = схема A-Star 32U4 (піни PE6/INT6/AIN0 — це ATmega32U4)

Справжній PDF, справжній постачальник, адреса обіцяє даташит BH1750 —
а всередині зовсім інший документ. Жодна з наших перевірок цього не
бачить: файл відкривається, цитата з нього звірилася б підрядком
успішно, ім'я в полі джерела виглядало б правильним.

Спіймав це помічник, який чесно написав `ne_znayshov`: «документ
виявився схемою A-Star 32U4». Тобто врятувала не перевірка, а те, що
наряд робив чесну відповідь дешевою.

## Що робить

Для кожного PDF питає, чи згадує він власний предмет — назву з імені
файлу в кількох написаннях. Це **не ворота**, а перелік на перегляд:
на 67 файлах дає близько 16 скарг, і більшість хибні (даташит
NCR18650B зве себе «NCR18650B» лише на титулі, а Kester взагалі
зветься за виробником). Читати його має людина, і один раз на
документ.

    tools/cache_identity.py [шлях-до-кешу]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import layer3  # noqa: E402


def varianty(imya: str) -> set[str]:
    yadro = re.sub(r"^[0-9a-f]{6,10}-", "", imya).rsplit(".", 1)[0].lower()
    return {yadro, yadro.replace("-", ""), yadro.replace("_", "-"),
            re.sub(r"[-_]", "", yadro), yadro.split("_")[0],
            yadro.split("-")[0]}


def main(argv: list[str]) -> int:
    kesh = Path(argv[1]) if len(argv) > 1 else ROOT / "dzherela-kesh"
    pidozr = []
    vsyoho = 0
    for p in sorted(kesh.glob("*.pdf")):
        vsyoho += 1
        t = (layer3.tekst_dzherela(p) or "").lower()
        if not t:
            pidozr.append((p.name, "не читається"))
            continue
        tt = re.sub(r"[-_\s]", "", t)
        if not any(v in t or re.sub(r"[-_]", "", v) in tt
                   for v in varianty(p.name) if len(v) > 3):
            pochatok = " ".join(t.split())[:76]
            pidozr.append((p.name, pochatok))
    for n, d in pidozr:
        print("   %-42s %s" % (n[:42], d))
    print("\nPDF %d; не згадують власного предмета %d — переглянути очима"
          % (vsyoho, len(pidozr)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
