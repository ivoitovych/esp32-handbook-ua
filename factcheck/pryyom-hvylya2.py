#!/usr/bin/env python3
"""Приймання хвилі 2: цитата мусить стояти в НАЗВАНОМУ файлі.

## Чим це відрізняється від `pryyom-m2.py`

Той перевіряє форму запису: чи не книга в джерелі, чи є цитата при
класі A, чи не завищено E. Цей перевіряє **єдине, але головне**:
чи справді рядок із поля `cytata` стоїть у файлі, який названо в
полі `fayl`.

Саме ця перевірка робить наряд чесним, а не заборони в його тексті.
Переписати текст книги назад у `cytata` тепер не спрацює: у
`dzherela-kesh/ds18b20.pdf` тексту книги немає. Підтвердити можна
лише те, що справді відкрив.

Звірка нежорстка рівно в тому, у чому винен видобувач тексту з PDF:
пробіли схлопуються, м'які переноси й переноси рядків знімаються,
різні тире зводяться до одного. Усе інше — дослівно.
"""
from __future__ import annotations

import re
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KESH = ROOT / "dzherela-kesh"
import yaml

_kesh_tekst: dict[str, str] = {}


def normal(s: str) -> str:
    s = s.replace("­", "").replace("‑", "-")
    s = re.sub(r"[–—−]", "-", s)
    s = re.sub(r"[’‘`´]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    s = re.sub(r"-\s*\n\s*", "", s)      # перенос зі скісною
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def tekst_fayla(imya: str) -> str | None:
    if imya in _kesh_tekst:
        return _kesh_tekst[imya]
    p = KESH / imya
    if not p.exists():
        return None
    if p.suffix.lower() == ".pdf":
        try:
            t = subprocess.run(["pdftotext", "-layout", str(p), "-"],
                               capture_output=True, text=True, timeout=120).stdout
        except Exception:
            return None
    else:
        t = p.read_text(encoding="utf-8", errors="replace")
    _kesh_tekst[imya] = normal(t)
    return _kesh_tekst[imya]


def perevirka(shlyakh: Path) -> list[tuple[str, str]]:
    bidy = []
    try:
        zapysy = yaml.safe_load(shlyakh.read_text(encoding="utf-8")) or []
    except Exception as e:
        return [("БИТИЙ YAML", str(e).split("\n")[0][:90])]
    for z in zapysy:
        if not isinstance(z, dict):
            bidy.append(("НЕ ЗАПИС", str(z)[:60]))
            continue
        ident = str(z.get("id", z.get("nazva", "?")))[:40]
        verdykt = str(z.get("verdykt", "")).strip()
        cyt = str(z.get("cytata", "")).strip()
        fayl = str(z.get("fayl", "")).strip()

        if verdykt not in ("pidtverdzheno", "sperechayetsya",
                           "ne_znayshov", "nedosyazhne"):
            bidy.append(("ВЕРДИКТ НЕВІДОМИЙ: " + verdykt[:30], ident))
            continue
        if verdykt in ("ne_znayshov", "nedosyazhne"):
            if cyt:
                bidy.append(("ЦИТАТА ПРИ ВЕРДИКТІ " + verdykt, ident))
            continue
        if not cyt:
            bidy.append(("%s БЕЗ ЦИТАТИ" % verdykt.upper(), ident))
            continue
        if not fayl:
            bidy.append(("ЦИТАТА БЕЗ НАЗВАНОГО ФАЙЛУ", ident))
            continue
        t = tekst_fayla(fayl)
        if t is None:
            bidy.append(("ФАЙЛУ НЕМАЄ В КЕШІ: " + fayl[:40], ident))
            continue
        if normal(cyt) not in t:
            bidy.append(("ЦИТАТИ НЕМАЄ В " + fayl[:34], ident))
    return bidy


def main(argv: list[str]) -> int:
    shlyakhy = [Path(a) for a in argv[1:]]
    vsyoho = 0
    prynyato = 0
    for s in shlyakhy:
        if not s.exists():
            continue
        b = perevirka(s)
        try:
            n = len(yaml.safe_load(s.read_text(encoding="utf-8")) or [])
        except Exception:
            n = 0
        prynyato += n - len(b)
        vsyoho += len(b)
        if b:
            print(s.name)
            for rid, ident in b:
                print("   %-44s %s" % (rid, ident))
    print("\nприйнято %d, відхилено %d" % (prynyato, vsyoho))
    return 1 if vsyoho else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
