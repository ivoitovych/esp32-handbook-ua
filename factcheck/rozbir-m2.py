#!/usr/bin/env python3
"""Розкласти всі одиниці БЕЗ документа на черги для розбору.

Наряд — `factcheck/NARYAD-m2-rozbir.md`. Перевірка — `pryyom-rozbir-m2.py`.

    factcheck/rozbir-m2.py <агентів> <одиниць-на-агента> [каталог]
"""
from __future__ import annotations

import collections
import importlib.util
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import vybirka  # noqa: E402

spec = importlib.util.spec_from_file_location("nm", ROOT / "factcheck" / "naryad-m2.py")
nm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nm)


def main(argv: list[str]) -> int:
    agentiv = int(argv[1]) if len(argv) > 1 else 40
    na_agenta = int(argv[2]) if len(argv) > 2 else 30
    katalog = Path(argv[3]) if len(argv) > 3 else Path("/tmp/hr")
    katalog.mkdir(parents=True, exist_ok=True)

    fayly = nm.kesh_fayly()
    bez = []
    for klas in ("C", "F", "E"):
        for o in vybirka.odynyci(klas):
            if not nm.pidibraty(o["tekst"], fayly):
                bez.append({**o, "klas": klas})
    # Сталий порядок: одиниці одного розділу поруч, щоб помічник тримав
    # у голові один контекст, а не стрибав книгою.
    bez.sort(key=lambda o: (o["src"], o["id"]))

    cherhy = [bez[i::agentiv] for i in range(agentiv)]
    n = 0
    for i, ch in enumerate(cherhy, 1):
        ch = ch[:na_agenta]
        if not ch:
            continue
        L = []
        for x in ch:
            L.append("[%s]  %s" % (x["id"], x["src"]))
            for ln in textwrap.wrap(" ".join(x["tekst"].split())[:300], 74):
                L.append("     | " + ln)
            L.append("")
        (katalog / ("q%d.txt" % i)).write_text("\n".join(L), encoding="utf-8")
        n += len(ch)
    print("одиниць без документа: %d" % len(bez))
    print("роздано %d по %d чергах (до %d на чергу)" % (n, agentiv, na_agenta))
    print("лишиться на наступний захід: %d" % (len(bez) - n))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
