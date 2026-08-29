#!/usr/bin/env python3
"""The maintenance record, re-measured instead of remembered.

## Why a tool and not just a document

Every number we have ever written into a document went stale, and none
of them announced it. `MIGRATION.md` said "43 of 52 tools still
transliterated" for a day after it was 2 of 54. `METHOD.md` carried a
class list without `N` under a paragraph explaining that copies without
an owner are never repaired everywhere.

So the state is not written down at all. It is a list of **questions**
with a measurement each, answered from the tree every time it is asked.
A reviewer needs no knowledge of the project to check it: run it, and
every figure was computed a second ago.

    tools/maintenance.py            the measured state
    tools/maintenance.py --md       the same, as the report body
    tools/maintenance.py --open     only what is still open
    tools/maintenance.py --samoperevirka

## What counts as open

An item is open when its **own** measurement says so — each question
carries its own closing condition, not a shared "zero is good". The
first draft used `> 0` for everything and flagged "five orders composed
from the spec" as a defect: a measure that measures, but not the thing.

An item nobody can measure does not belong here at all. Putting it here
with a hand-maintained status would recreate exactly what this replaces.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

STARI_POLYA = {"nazva", "zbih", "klas", "dzherelo", "cytata", "sposib",
               "notatka", "shukaty", "rozrakhunok"}
KNYZHKOVI_TEKY = {"manual", "dodatky", "kartky", "inserts"}


def _yaml_zapysy():
    import yaml
    for p in sorted((ROOT / "factcheck" / "data" / "evidence").glob("*.yaml")):
        try:
            for z in yaml.safe_load(p.read_text(encoding="utf-8")) or []:
                if isinstance(z, dict):
                    yield p, z
        except Exception:
            continue


def mira_polya() -> tuple[int, int]:
    """Старі імена полів у записах доказів: скільки лишилось."""
    n = st = 0
    for _p, z in _yaml_zapysy():
        n += 1
        st += len(set(z) & STARI_POLYA)
    return n, st


def mira_instrumenty() -> list[str]:
    """Інструменти, чиє ім'я — транслітерована українська."""
    import renames
    vidomi = set(renames.TABLYCYA.values()) | {
        "build", "preview", "review", "linkcheck", "budgets", "bind_by_hash",
        "claims", "kod-stubs", "pdf-smoke", "coverage", "layer1",
        "layer1_units", "intake", "intake_f", "intake_triage", "intake_wave2",
        "intake_wave3", "patterns_repair", "cache_vs_book", "cache_identity",
        "triage", "factcheck", "renames", "task_spec", "entry_points",
        "maintenance", "docs", "runs", "doc_kind"}
    return sorted(p.stem for p in (ROOT / "tools").glob("*.py")
                  if p.stem not in vidomi)


def mira_katalohy() -> list[str]:
    import renames
    stari = {s.split("/")[-1] for s in renames.KATALOHY}
    ye = {p.name for p in (ROOT / "factcheck").iterdir() if p.is_dir()}
    ye |= {p.name for p in ROOT.iterdir()
           if p.is_dir() and not p.name.startswith(".")}
    return sorted((ye & stari) | ({"zvyazok"} if (ROOT / "zvyazok").exists()
                                  else set()))


def mira_zavdannya() -> tuple[int, int, list[str]]:
    """Наряди: скільки складаються зі спеки, і чи всі мають версію."""
    import task_spec
    zi_speky, versiy = 0, []
    for imya, var in (("leads", "zaholovok"), ("sample", "zaholovok"),
                      ("sweep", "shapka"), ("work_orders", "zaholovok"),
                      ("work_orders_f", "shapka")):
        try:
            m = __import__(imya)
            h = getattr(m, var)(skilky=1, nomer=1, klas="F", nasinnya=1,
                                vsyoho=1, n=1, tema="t", k=1, kandydat="x")
        except Exception:
            continue
        zi_speky += 1
        v = re.search(r"Task spec `([0-9a-f]{8})`", h)
        if v:
            versiy.append(v.group(1))
    return zi_speky, len(set(versiy)), sorted(set(versiy))


def mira_vorota() -> dict[str, int | str]:
    """Стан воріт: те, що `make check` каже про себе сам."""
    out: dict[str, int | str] = {}
    r = subprocess.run([sys.executable, "tools/docs.py"], cwd=ROOT,
                       capture_output=True, text=True)
    m = re.search(r"розбіжностей (\d+)", r.stdout)
    out["розбіжності керівних документів"] = int(m.group(1)) if m else -1
    r = subprocess.run([sys.executable, "tools/correspondence.py"], cwd=ROOT,
                       capture_output=True, text=True)
    m = re.search(r"борг М1 (\d+), борг М2 (\d+)", r.stdout)
    out["наш борг у листуванні"] = int(m.group(1)) if m else -1
    out["борг іншого супровідника"] = int(m.group(2)) if m else -1
    r = subprocess.run([sys.executable, "tools/intake.py"], cwd=ROOT,
                       capture_output=True, text=True)
    m = re.search(r"\((\d+) блокують", r.stdout)
    out["блокуючі знахідки прийому"] = int(m.group(1)) if m else -1
    return out


def mira_dokumenty() -> tuple[int, int, list[str]]:
    """Документи `factcheck/`: скільки, скільки без правильної позначки.

    Питає `doc_kind`, а не міряє сама. Перша редакція мала **власний**
    взірець позначки — і за годину розійшлася з тим, що ставить
    `doc_kind`: показувала 22 без позначки, коли їх було нуль. Рід 19 у
    двох інструментах, написаних того самого вечора одним автором.
    """
    import doc_kind
    # Список теж у `doc_kind`, не свій. Докстрінг вище обіцяв саме це, а
    # рядок під ним робив власний плаский `glob("*.md")` — і після
    # перебудови 2026-08-29 порахував шість документів із тридцяти
    # одного, тоді як `doc_kind.perevirka()` дивилася на всі. Половинне
    # делегування гірше за жодне: воно виглядає як делегування.
    usi = doc_kind.dokumenty()
    bidy = doc_kind.perevirka()
    return len(usi), len(bidy), bidy


def mira_tochky() -> tuple[int, int]:
    import entry_points
    poza = {t[0] for t in entry_points.TOCHKY} - entry_points.U_VOROTAKH
    return len(entry_points.TOCHKY), len(poza)


# Кожне питання несе **свою** умову «закрито», а не спільне «нуль».
# Перша редакція вважала відкритим усе, де число більше за нуль, — і
# позначала вадою те, що «п'ять нарядів складаються зі спеки». Це рід 3
# у власному звіті: міра є, і вона міряє не те.
PYTANNYA = [
    ("поля запису доказу — старих імен", lambda: mira_polya()[1],
     lambda v: v == 0,
     "0 після кроку 2; потребує обох супровідників того самого дня"),
    ("інструментів із транслітерованим іменем",
     lambda: len(mira_instrumenty()), lambda v: v == 0,
     "0; лишок — інструменти М2"),
    ("каталогів із транслітерованим іменем",
     lambda: len(mira_katalohy()), lambda v: v == 0,
     "0; `zvyazok/` — рішення за двох"),
    ("нарядів, складених зі спеки завдання", lambda: mira_zavdannya()[0],
     lambda v: v >= 5, "усі 5"),
    ("різних версій завдання серед них", lambda: mira_zavdannya()[1],
     lambda v: v == mira_zavdannya()[0],
     "стільки ж, скільки нарядів — збіг версій означав би діру"),
    ("розбіжностей керівних документів",
     lambda: mira_vorota()["розбіжності керівних документів"],
     lambda v: v == 0, "0"),
    ("блокуючих знахідок прийому",
     lambda: mira_vorota()["блокуючі знахідки прийому"],
     lambda v: v == 0, "0"),
    ("наш борг у листуванні",
     lambda: mira_vorota()["наш борг у листуванні"], lambda v: v == 0, "0"),
    ("документів `factcheck/` без позначки роду",
     lambda: mira_dokumenty()[1], lambda v: v == 0,
     "0 — кожен документ каже, породжений він, канонічний чи історичний"),
    ("інструментів поза `make check`", lambda: mira_tochky()[1],
     lambda v: True, "довідково: саме там вижили дев'ять зламів"),
]


def zvit(md: bool = False, lyshe_vidkryti: bool = False) -> int:
    ryadky = []
    vidkrytykh = 0
    for imya, mira, zakryte, tsil in PYTANNYA:
        try:
            v = mira()
            vidkryte = not zakryte(v)
        except Exception as e:
            v, vidkryte = f"! {str(e)[:40]}", True
        vidkrytykh += bool(vidkryte)
        if lyshe_vidkryti and not vidkryte:
            continue
        znak = "✗" if vidkryte else "·"
        if md:
            ryadky.append(f"| {znak} | {imya} | `{v}` | {tsil} |")
        else:
            ryadky.append(f"  {znak} {imya:<44} {str(v):>6}   {tsil}")
    if md:
        print("| | Питання | Виміряно | Ціль |")
        print("|---|---|---|---|")
    print("\n".join(ryadky))
    if not lyshe_vidkryti:
        print(f"\nвідкритих пунктів: {vidkrytykh} із {len(PYTANNYA)}")
    return 0


def samoperevirka() -> int:
    """Показ на зіпсованому вході."""
    pomylok = 0

    def probа(imya, umova):
        nonlocal pomylok
        pomylok += not umova
        print(f"  {'✓' if umova else '✗'} {imya}")

    n, st = mira_polya()
    probа(f"записи читаються ({n})", n > 1000)
    probа("міра полів рахує старі імена, а не всі", st < n * 9)
    zi, riznyh, _ = mira_zavdannya()
    probа(f"наряди складаються зі спеки ({zi})", zi >= 5)
    probа(f"версії нарядів різні ({riznyh})", riznyh == zi)
    usi, bez, _ = mira_dokumenty()
    probа(f"документи перелічено ({usi})", usi > 20)
    probа("кожне питання має свою умову закриття",
          all(callable(m) and callable(z)
              for _i, m, z, _t in PYTANNYA))
    print("самоперевірка: усе як очікувано" if not pomylok
          else f"самоперевірка: РОЗБІЖНОСТЕЙ {pomylok}")
    return 1 if pomylok else 0


def main() -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--md", action="store_true")
    a.add_argument("--open", action="store_true")
    a.add_argument("--samoperevirka", action="store_true")
    o = a.parse_args()
    if o.samoperevirka:
        return samoperevirka()
    return zvit(md=o.md, lyshe_vidkryti=o.open)


if __name__ == "__main__":
    sys.exit(main())
