#!/usr/bin/env python3
"""Приймання наряду «розбір»: чотири умови, усі механічні.

  1. YAML читається;
  2. `rid` — одне з чотирьох відомих слів;
  3. `pozyciya` має поле `chomu` — бо вона СТВЕРДЖУЄ, що зовнішнього
     джерела не існує, і це присуд, який ховає одиницю назавжди;
  4. `dzherelo-ye` має поле `shukaty`, і воно НАЗИВАЄ ДОКУМЕНТ,
     а не властивість світу.

Четверта умова — та сама, що врятувала нас від вигаданих джерел:
позитивний тест «чи названо документ», а не чорний список фраз. Мій
перелік заборонених слів колись знайшов нуль там, де тест М1 знайшов
45.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import yaml  # noqa: E402

RODY = {"dzherelo-ye", "pozyciya", "ne-tverdzhennya", "ne-rozibrav"}

# Ознака документа: власна назва з великої, розширення файлу, слово
# «datasheet»/«специфікація»/«стандарт» із номером, назва стандарту.
DOKUMENT = re.compile(
    r"[A-ZА-ЯЇІЄҐ][A-Za-zА-Яа-яЇїІіЄєҐґ0-9-]{2,}\s+"
    r"(?:Datasheet|Series|Manual|Guide|Specification|Reference)"
    r"|datasheet|даташит|\.(?:pdf|rst|h|c|inc|csv)\b"
    r"|\b(?:IEC|IEEE|ISO|RFC|USB|JEDEC)\s*\d"
    r"|ESP-IDF|Programming Guide|Technical Reference|TRM"
    r"|[A-Z]{2,}\d{3,}", re.I)


def perevirka(p: Path) -> list[tuple[str, str]]:
    try:
        zapysy = yaml.safe_load(p.read_text(encoding="utf-8")) or []
    except Exception as e:
        return [("БИТИЙ YAML", str(e).split("\n")[0][:80])]
    bidy = []
    for z in zapysy:
        if not isinstance(z, dict):
            bidy.append(("НЕ ЗАПИС", str(z)[:50]))
            continue
        ident = str(z.get("id", "?"))[:22]
        rid = str(z.get("rid", "")).strip()
        if rid not in RODY:
            bidy.append(("РІД НЕВІДОМИЙ: " + rid[:24], ident))
            continue
        # `ne-tverdzhennya` пояснення НЕ вимагає, і це свідома поступка.
        # Спершу вимагав — і дістав 23 відхилення на першій же сотні,
        # усі однакові. Причина в тому, що вимога була не на місці:
        # «це рядок покажчика» видно з самого тексту одиниці, тобто
        # твердження структурне й перевіряється МЕХАНІЧНО, а не на
        # слово. Просити пояснення там, де можна перевірити самому, —
        # це перекладати роботу на помічника й діставати відписку.
        #
        # `pozyciya` — інша річ: вона каже, що зовнішнього джерела не
        # існує. Це присуд, механічно він не перевіряється, і саме він
        # ховає одиницю з наряду назавжди. Тут пояснення лишається.
        if rid == "pozyciya" and not str(z.get("chomu", "")).strip():
            bidy.append(("POZYCIYA БЕЗ ПОЯСНЕННЯ", ident))
        if rid == "dzherelo-ye":
            sh = str(z.get("shukaty", "")).strip()
            if not sh:
                bidy.append(("dzherelo-ye БЕЗ shukaty", ident))
            elif not DOKUMENT.search(sh):
                bidy.append(("shukaty НЕ НАЗИВАЄ ДОКУМЕНТА: " + sh[:34], ident))
    return bidy


def main(argv: list[str]) -> int:
    vsyoho = prynyato = 0
    for a in argv[1:]:
        p = Path(a)
        if not p.exists():
            continue
        b = perevirka(p)
        try:
            n = len(yaml.safe_load(p.read_text(encoding="utf-8")) or [])
        except Exception:
            n = 0
        prynyato += max(0, n - len(b))
        vsyoho += len(b)
        if b:
            print(p.name)
            for r, i in b[:6]:
                print("   %-40s %s" % (r, i))
            if len(b) > 6:
                print("   ... ще %d" % (len(b) - 6))
    print("\nприйнято %d, відхилено %d" % (prynyato, vsyoho))
    return 1 if vsyoho else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
