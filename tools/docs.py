#!/usr/bin/env python3
"""Consistency gate over the foundation documents.

## Why this exists

The owner's complaint, measured and confirmed: *"the technology keeps
drifting — we find new classes of problem and forget the ones already
found."*

On 2026-08-28 the class vocabulary lived in **three** documents and all
three had drifted apart; the two newest classes were missing from both
non-authoritative copies. That was found by reading. Reading does not
scale and does not run in CI.

Two answers were considered and rejected:

* **merge every document into one.** A three-thousand-line file is not
  re-read whole by anybody, so drift stops being visible instead of
  stopping.
* **move content between documents on a fixed cadence.** That is a
  discipline, and this project's own law says disciplines do not hold:
  *stated mechanics hold, a named prohibition does not.* A cadence is a
  prohibition against drift.

What holds is a check. This is the check.

## What it verifies

    vocabulary   every class letter a document names must exist in the
                 code, and every code class must appear in the
                 authoritative document
    tools        every `tools/*.py` a document names must exist
    verdicts     every verdict a work-order template offers must be one
                 the intake gate knows how to check
    defects      every defect kind referenced by number must exist

## What it deliberately does NOT verify

Prose. Two documents may explain the same idea in different words and
that is not drift — `POMICHNYKY.md` is the raw log and `METHOD.md` is
the distilled law, and both say so in their first lines. Only **facts
with one right answer** are checked here.

    tools/docs.py            check
    tools/docs.py --proba    show the check working on broken input
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FC = ROOT / "factcheck"
sys.path.insert(0, str(ROOT / "tools"))

# Хто нормативний для якого факту. Без цього рядка «полагоджують ту
# копію, що читається», і копії розходяться далі.
VLASNYK = {
    "класи доказу": "SCHEMA.md",
    "роди хиб": "DEFECTS.md",
    "вердикти наряду": "tools/intake_f.py",
}

KERIVNI = ["METHOD.md", "DEFECTS.md", "LESSONS-M2.md", "RETROSPECTIVE.md",
           "SCHEMA.md", "ARCHITECTURE.md", "POMICHNYKY.md", "README.md",
           "MIGRATION.md", "WORK-ORDER-EXAMPLE.md"]

# Рядок, що перелічує класи. ФОРМАТІВ ТРИ, і це не примха:
#
#     | **A** | ✅ | …        SCHEMA.md
#     | `A`   | …            ARCHITECTURE.md (до 2026-08-28)
#         A  primary …       METHOD.md
#
# Перша редакція знала лише перший. Прогін на дереві до правок зловив
# METHOD.md і НЕ зловив ARCHITECTURE.md — саме той документ, з якого
# все й почалося. Перевірка з однією формою бачить одну форму, і
# мовчить про решту так само впевнено.
RE_KLAS_TABL = re.compile(
    r"^\|\s*(?:\*\*([A-Z])\*\*|`([A-Z])`)\s*\|", re.M)
RE_KLAS_SPYS = re.compile(r"^\s{2,}([A-Z])\s{2,}[a-zа-яїєґ]", re.M)
RE_TUL = re.compile(r"`?(tools/[a-z0-9_.-]+\.py)`?")
RE_RID = re.compile(r"(?:рід|kind)\s+(\d{1,2})\b", re.I)


def klasy_kodu() -> set[str]:
    import factcheck
    return set(factcheck.KLASY)


def perevirka() -> list[str]:
    bidy: list[str] = []
    kod = klasy_kodu()
    avt = (FC / VLASNYK["класи доказу"]).read_text(encoding="utf-8")
    avt_klasy = {a or b for a, b in RE_KLAS_TABL.findall(avt)}

    brak = kod - avt_klasy
    if brak:
        bidy.append(
            f"{VLASNYK['класи доказу']}: нормативний перелік не знає класів "
            f"{sorted(brak)}, які є в коді")
    zayvi = avt_klasy - kod
    if zayvi:
        bidy.append(
            f"{VLASNYK['класи доказу']}: перелічено класи {sorted(zayvi)}, "
            f"яких у коді немає")

    for imya in KERIVNI:
        p = FC / imya
        if not p.exists():
            bidy.append(f"{imya}: керівний документ відсутній")
            continue
        t = p.read_text(encoding="utf-8")

        # Копія словника класів, що розійшлася з кодом.
        nazvani = ({a or b for a, b in RE_KLAS_TABL.findall(t)}
                   | set(RE_KLAS_SPYS.findall(t)))
        nazvani &= set("ABCDEFGKLS")
        if len(nazvani) >= 4 and imya != VLASNYK["класи доказу"]:
            vidsutni = kod - nazvani
            if vidsutni:
                bidy.append(
                    f"{imya}: копія словника класів без {sorted(vidsutni)} — "
                    f"або доповнити, або замінити посиланням на "
                    f"{VLASNYK['класи доказу']}")

        for tul in set(RE_TUL.findall(t)):
            if not (ROOT / tul).exists():
                bidy.append(f"{imya}: названо неіснуючий {tul}")

        for n in set(RE_RID.findall(t)):
            if imya == VLASNYK["роди хиб"]:
                continue
            if not re.search(rf"^## {n}\.", (FC / VLASNYK["роди хиб"])
                             .read_text(encoding="utf-8"), re.M):
                bidy.append(f"{imya}: посилання на рід {n}, якого немає в "
                            f"{VLASNYK['роди хиб']}")

    # Вердикти наряду проти воріт, які їх приймають.
    try:
        import intake_f
        znani = set(intake_f.POTREBUYE)
    except Exception as e:
        bidy.append(f"ворота не імпортуються: {str(e)[:60]}")
        znani = set()
    if znani:
        for shabl in (ROOT / "tools" / "naryad_f.py",):
            t = shabl.read_text(encoding="utf-8")
            vsi = set(re.findall(r"^\| `([a-z_]+)` \|", t, re.M))
            chuzhi = vsi - znani
            if chuzhi:
                bidy.append(
                    f"{shabl.name}: наряд пропонує вердикти {sorted(chuzhi)}, "
                    f"яких ворота не перевіряють")
    return bidy


def proba() -> int:
    """Показ на зіпсованому вході. Перевірка, що жодного разу не
    спрацювала, невідрізненна від перевірки, якої немає."""
    import tempfile
    global FC
    spravzhnya = FC
    vypadky = [
        ("документ називає неіснуючий тул",
         {"METHOD.md": "див. `tools/nemaye-takoho.py`\n"}, True),
        ("документ посилається на неіснуючий рід",
         {"METHOD.md": "це рід 99 каталогу\n"}, True),
        ("чистий документ", {"METHOD.md": "нічого особливого\n"}, False),
    ]
    provaliv = 0
    for nazva, fajly, ocik in vypadky:
        with tempfile.TemporaryDirectory() as d:
            t = Path(d)
            for imya in KERIVNI:
                (t / imya).write_text((spravzhnya / imya).read_text("utf-8")
                                      if imya not in fajly else fajly[imya],
                                      encoding="utf-8")
            FC = t
            try:
                b = [x for x in perevirka() if "METHOD.md" in x]
            finally:
                FC = spravzhnya
            spiymav = bool(b)
            ok = "✓" if spiymav == ocik else "✗ ПРОВАЛ"
            print("   %s %-42s очікувано %-5s дістав %s"
                  % (ok, nazva, ocik, spiymav))
            provaliv += spiymav != ocik
    print("\nпровалів: %d" % provaliv)
    return 1 if provaliv else 0


def main() -> int:
    if "--proba" in sys.argv:
        return proba()
    bidy = perevirka()
    for b in bidy:
        print("   ✗ " + b)
    print("\ndocs: керівних документів %d, розбіжностей %d"
          % (len(KERIVNI), len(bidy)))
    return 1 if bidy else 0


if __name__ == "__main__":
    sys.exit(main())
