#!/usr/bin/env python3
"""Схема запису доказу і контракт картки — перевіряються, а не обіцяються.

## Навіщо

Аудит 2026-08-28 назвав три речі, яких у технології не було:

1. опису картки як формату — він жив лише в коді генератора;
2. **записаної вимоги самодостатності** картки;
3. одного місця, де сказано, який набір полів правильний.

Третє виглядало як безлад: 28 різних наборів полів на 1337 записів.
Вимір показав інше — **три поля є в кожному записі** (`title`,
`status`, `match`), а решта необов'язкова й залежить від класу. Схема
одна; 28 наборів — її підмножини.

Але головне не в цьому. Вимогу, записану без перевірки, ніхто не
перевіряє: саме тому 5194 картки з 8331 обривалися на півслові, поки
хтось не подивився очима. Тож `SCHEMA.md` описує, а цей скрипт
**тримає**.

## Що перевіряється

**Запис доказу:** обов'язкові поля є; поля, потрібні для класу, не
пропущені; невідомих полів немає.

**Картка:** блоки на місці; дослівний блок є **лише** там, де текст
одиниці — рендер, і містить **лише** рядок таблиці; номера рядка у
видимій частині немає.

    factcheck/tools/schema.py                перевірити
    factcheck/tools/schema.py --samoperevirka показ на зіпсованому вході
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

OBOVYAZKOVI = {"title", "status", "match"}

# Українські імена — стан переїзду, не помилка. Див. MIGRATION.md.
STARI = {"nazva", "zbih", "klas", "dzherelo", "cytata", "sposib",
         "notatka", "shukaty", "rozrakhunok"}
VIDOMI = OBOVYAZKOVI | STARI | {
    "sha", "source", "quote", "method", "note", "look_for", "calculation",
    "looked_at", "absent", "control", "perevireno-okom", "_prokhid"}

# Що клас зобов'язаний мати. Ключ — і літера, і слово: переїзд не
# скінчено, і перевірка мусить розуміти обидва записи.
POTREBUYE = {
    "A": ("source", "quote"), "verbatim": ("source", "quote"),
    "B": ("source",), "derived": ("source",),
    "C": ("source",), "named-unreachable": ("source",),
    "D": ("calculation",), "arithmetic": ("calculation",),
    # `looked_at` обов'язкове навмисно. Без нього стан повторив би долю
    # `C`, який теж мав називати документ — і в шести записах не називав.
    "L": ("looked_at",), "looked-not-found": ("looked_at",),
    # `S` мусить назвати **місце в книзі**, з яким звіряли, — інакше
    # він каже лише «ми подивилися», що вже є `E`. Поле те саме,
    # `source`, бо це і є джерело: просто внутрішнє.
    "S": ("source",), "self-consistent": ("source",),
    # `N` — доведення відсутністю. `absent` несе **рядок, якого в
    # документі немає**, і саме він робить твердження перевірним:
    # шар 3 має впасти, якщо рядок там усе-таки знайдеться.
    #
    # `control` не обов'язкове, але без нього доказ слабкий, і це
    # сказано в SCHEMA.md: мовчання документа доводить лише там, де
    # сусідній документ того самого роду говорить. `SOC_BT_SUPPORTED`
    # немає в `esp32s2/soc_caps.h` — і є в усіх десяти інших.
    "N": ("source", "absent"), "absent-from-source": ("source", "absent"),
}

# Словник станів. Досі не перевірявся **зовсім**: `POTREBUYE.get(klas)`
# на невідомому слові тихо віддавав порожнє, і запис проходив як
# бездоганний.
#
# Знайдено на шести записах зі `status: unverified` — слова, якого в
# схемі немає (правильне `unchecked`). Ворота мовчали, бо вони питали
# «чи є поля, потрібні цьому класу», а не «чи існує такий клас».
#
# > Перевірка вимог до значення, яка не перевіряє саме значення, —
# > це рід 3: працює, вертає нуль, і нуль нічого не означає.
STATUSES = set(POTREBUYE) | {
    "E", "no-external-signal", "F", "unchecked", "G", "refuted",
    "K", "code-context"}

RE_KARTKA = re.compile(
    r"<!-- fc id:(?P<id>\S+) sha:\S+ src:(?P<src>\S+) status:\S+ -->\n"
    r"### (?P<zah>[^\n]*)\n")
RE_DOSLIVNO = re.compile(
    r"\*\*Дослівно з книги\*\*\n\n(`{3,})\n(?P<syryy>.*?)\n\1", re.S)
RENDER = ("komirka", "tablycya", "tablycya-shapka")


def zapysy(teka: pathlib.Path) -> list[tuple[str, int, dict]]:
    out = []
    for f in sorted(teka.glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception as e:
            out.append((f.name, -1, {"_bida": f"YAML не читається: {e}"}))
            continue
        if not isinstance(z, list):
            out.append((f.name, -1, {"_bida": "файл не є переліком"}))
            continue
        for i, r in enumerate(z):
            out.append((f.name, i, r if isinstance(r, dict)
                        else {"_bida": "запис не є словником"}))
    return out


def perevir_zapysy(zap) -> list[str]:
    bidy = []
    for imya, i, r in zap:
        de = f"{imya}::{i}"
        if "_bida" in r:
            bidy.append(f"{de}: {r['_bida']}")
            continue
        brak = OBOVYAZKOVI - set(r)
        if brak:
            bidy.append(f"{de}: немає обов'язкових полів "
                        f"{', '.join(sorted(brak))}")
        nevidomi = set(r) - VIDOMI
        if nevidomi:
            bidy.append(f"{de}: невідомі поля {', '.join(sorted(nevidomi))}")
        klas = str(r.get("status") or r.get("klas") or "")
        if klas and klas not in STATUSES:
            bidy.append(f"{de}: невідомий стан `{klas}` — див. SCHEMA.md")
        for pole in POTREBUYE.get(klas, ()):
            # Переїзд: значення може стояти під старим іменем.
            stare = {"source": "dzherelo", "quote": "cytata",
                     "calculation": "rozrakhunok"}.get(pole)
            if not r.get(pole) and not (stare and r.get(stare)):
                bidy.append(f"{de}: клас `{klas}` вимагає поля `{pole}`")
    return bidy


def perevir_kartky() -> list[str]:
    bidy = []
    for g in config.groups():
        for f in sorted((config.cards_root() / g).glob("*.md")):
            t = f.read_text(encoding="utf-8")
            shmatky = RE_KARTKA.split(t)
            for i in range(1, len(shmatky), 4):
                ident, zah, tilo = shmatky[i], shmatky[i + 2], shmatky[i + 3]
                de = f"{f.name}::{ident}"
                vyd = zah.split(" · ")[1] if " · " in zah else "?"
                if "**Твердження, коротко**" not in tilo:
                    bidy.append(f"{de}: немає блоку «Твердження, коротко»")
                if "**Контекст" not in tilo:
                    bidy.append(f"{de}: немає блоку «Контекст»")
                if "**Доказ**" not in tilo:
                    bidy.append(f"{de}: немає блоку «Доказ»")
                # Номер рядка у **видимій** частині — застаріла адреса,
                # подана як факт. У службовому коментарі він доречний.
                if re.search(r"рядок \d+", zah):
                    bidy.append(f"{de}: номер рядка у видимому заголовку")
                m = RE_DOSLIVNO.search(tilo)
                if m and vyd not in RENDER:
                    bidy.append(f"{de}: дослівний блок у роді `{vyd}` — "
                                "текст одиниці вже дослівний, блок показує "
                                "обрізок рядка")
                if m and not m.group("syryy").lstrip().startswith("|"):
                    bidy.append(f"{de}: дослівний блок не є рядком таблиці")
    return bidy


def samoperevirka() -> int:
    """Показ на навмисно зіпсованому вході.

    Правило проєкту: перевірка, яка ніколи не спрацьовувала, не
    відрізняється від перевірки, якої немає.
    """
    vypadky = [
        ("повний запис", {"title": "т", "status": "verbatim",
                          "match": "x", "source": "u", "quote": "q"}, 0),
        ("без обов'язкового", {"status": "verbatim", "match": "x",
                               "source": "u", "quote": "q"}, 1),
        ("verbatim без цитати", {"title": "т", "status": "verbatim",
                                 "match": "x", "source": "u"}, 1),
        ("невідоме поле", {"title": "т", "status": "unchecked",
                           "match": "x", "vygadka": 1}, 1),
        ("старе ім'я замість нового", {"title": "т", "status": "verbatim",
                                       "match": "x", "dzherelo": "u",
                                       "cytata": "q"}, 0),
        # Новий стан: `looked_at` обов'язкове — інакше він повторить
        # долю `C`, який теж мав називати документ і не називав.
        ("looked-not-found повний",
         {"title": "т", "status": "looked-not-found", "match": "x",
          "looked_at": "factcheck/source-cache/xxx.pdf", "note": "чому шукали"}, 0),
        ("looked-not-found без looked_at",
         {"title": "т", "status": "looked-not-found", "match": "x",
          "note": "чому шукали"}, 1),
        # `S` мусить назвати місце в книзі — інакше він каже лише «ми
        # подивилися», тобто рівно те, що вже означає `E`.
        ("self-consistent повний",
         {"title": "т", "status": "self-consistent", "match": "x",
          "source": "ВНУТРІШНЯ ЗВІРКА: manual/60-proj-loger.md, рядок 199",
          "quote": "рядок книги"}, 0),
        ("self-consistent без джерела",
         {"title": "т", "status": "self-consistent", "match": "x",
          "quote": "рядок книги"}, 1),
        # Доведення відсутністю: без `absent` воно не перевірне
        # взагалі — нема чого не шукати.
        ("absent-from-source повний",
         {"title": "т", "status": "absent-from-source", "match": "x",
          "source": "esp32s2/soc_caps.h", "absent": "SOC_BT_SUPPORTED",
          "control": "esp32s3/soc_caps.h"}, 0),
        ("absent-from-source без absent",
         {"title": "т", "status": "absent-from-source", "match": "x",
          "source": "esp32s2/soc_caps.h"}, 1),
    ]
    pomylok = 0
    for imya, r, ochik in vypadky:
        dist = len(perevir_zapysy([("t.yaml", 0, r)]))
        znak = "✓" if dist == ochik else "✗"
        pomylok += dist != ochik
        print(f"  {znak} {imya:<28} очікували {ochik}, дістали {dist}")
    print("самоперевірка: усе як очікувано" if not pomylok
          else f"самоперевірка: РОЗБІЖНОСТЕЙ {pomylok}")
    return 1 if pomylok else 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--samoperevirka", action="store_true")
    p.add_argument("--suvoro", action="store_true",
                   help="ненульовий код виходу при знахідках")
    a = p.parse_args()
    if a.samoperevirka:
        return samoperevirka()

    zap = zapysy(ROOT / "factcheck" / "evidence")
    bz = perevir_zapysy(zap)
    bk = perevir_kartky()

    print(f"schema: записів {len(zap)}, порушень схеми {len(bz)}; "
          f"порушень контракту картки {len(bk)}")
    for b in bz[:15]:
        print(f"   ✗ {b}")
    if len(bz) > 15:
        print(f"   … ще {len(bz) - 15}")
    for b in bk[:15]:
        print(f"   ✗ {b}")
    if len(bk) > 15:
        print(f"   … ще {len(bk) - 15}")
    return 1 if (a.suvoro and (bz or bk)) else 0


if __name__ == "__main__":
    sys.exit(main())
