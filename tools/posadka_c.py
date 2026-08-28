#!/usr/bin/env python3
"""Посадка класу `C`: одиниці, для яких документ названо, але він недосяжний.

## Навіщо це окремо від `prochid_posadka.py`

Той садить `A` — цитату, звірену з документом. Тут документа немає й не
буде звідси: даташит конкретної мікросхеми на GitHub не лежить, а
платний стандарт (IEC, ETSI, ISO) не лежить ніде публічно.

Клас `C` саме для цього й існує: **джерело назване, цитати немає,
записано що саме в ньому шукати.** Це не доказ, а розписка — але
розписка з адресою, і вона чесніша за `F`, який каже «до цього ніхто
не дійшов».

## Звідки береться матеріал

З розбору М2 (`factcheck/rozbir/`), рід `dzherelo-ye` — там, де поле
`shukaty` називає **конкретну деталь або стандарт із номером**, а не
тему. Різниця вимірна: з 111 таких одиниць 43 називають `PMS5003`,
`IEC 60908`, `ETSI EN303645`, `FAT Specification`; решта 68 кажуть
«Electronics Fundamentals textbook» — і це не документ.

**Тему в клас `C` не переводимо.** Інакше `C` перестане означати
«є що замовити» й стане другим `E`.

## Взірець

Той самий закон, що й у посадці `A`: найкоротший префікс, відмітний у
всьому реєстрі, і відмітність міряється **пошуком**, бо саме так
взірець потім і працює.

    tools/posadka_c.py [--pysaty]
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

# Конкретна деталь (літери + цифри) або стандарт із номером.
RE_KONKRETNE = re.compile(
    r"\b[A-Z]{2,}[0-9]{2,}[A-Z0-9-]*\b|IEC\s*\d|ETSI\s*EN\s*\d"
    r"|ISO\s*\d|IEEE\s*\d|RFC\s*\d|POSIX|FAT\d*\s*Spec", re.I)

# Ці рід джерела мають, але його дістає М2 або воно на GitHub —
# сюди вони не йдуть, бо для них можлива справжня цитата.
RE_DOSYAZHNE = re.compile(
    r"esp-idf|programming guide|esptool|arduino|documentation|api "
    r"|github|\.rst|\.h\b|README|micropython|esphome|radiolib|u8g2|lvgl"
    r"|datasheet|reference manual|technical reference|hardware design"
    r"|errata", re.I)

MIN_SLIV, MAX_SLIV = 4, 14


def ekranuy(s: str) -> str:
    return r"\s+".join(re.escape(w) for w in s.split())


def vzirets_dlya(tekst: str, vsi: list[str]) -> str | None:
    slova = tekst.split()
    if len(slova) < MIN_SLIV:
        return None
    for k in range(MIN_SLIV, min(len(slova), MAX_SLIV) + 1):
        vz = ekranuy(" ".join(slova[:k]))
        r = re.compile(vz)
        if sum(1 for t in vsi if r.search(t)) == 1:
            return vz
    return None


def main() -> int:
    import factcheck
    import vybirka

    p = argparse.ArgumentParser()
    p.add_argument("--pysaty", action="store_true")
    a = p.parse_args()

    reyestr: dict[str, dict] = {}
    for klas in factcheck.USI_KLASY:
        for u in vybirka.odynyci(klas):
            u["klas"] = klas
            reyestr[u["id"]] = u
    vsi = [u["tekst"] for u in reyestr.values()]

    rozbir = pathlib.Path("factcheck/rozbir")
    kandydaty = []
    for f in sorted(rozbir.glob("*.yaml")):
        for r in yaml.safe_load(f.read_text(encoding="utf-8")) or []:
            if not isinstance(r, dict) or str(r.get("rid")) != "dzherelo-ye":
                continue
            sh = str(r.get("shukaty", "")).strip()
            if RE_DOSYAZHNE.search(sh) or not RE_KONKRETNE.search(sh):
                continue
            kandydaty.append((str(r.get("id")), sh))

    posadka: dict[str, list[dict]] = collections.defaultdict(list)
    vzhe = shyrokyy = nema = 0
    for oid, sh in kandydaty:
        u = reyestr.get(oid)
        if u is None:
            nema += 1
            continue
        if u["klas"] in ("A", "B", "C"):
            vzhe += 1
            continue
        vz = vzirets_dlya(u["tekst"], vsi)
        if vz is None:
            shyrokyy += 1
            continue
        fayl = u["src"].split("/")[-1].split(":")[0].removesuffix(".md")
        posadka[fayl].append({
            "nazva": f"{oid}: {' '.join(u['tekst'].split()[:8])}",
            "zbih": vz,
            "klas": "C",
            "dzherelo": sh,
            "shukaty": sh,
            "sposib": (
                "Розбір черги 2026-08-27. Документ названо розбором "
                "як конкретну деталь або стандарт із номером; звідси "
                "він недосяжний (даташити мікросхем на GitHub не "
                "лежать, платні стандарти — ніде публічно). Клас `C` "
                "означає «джерело назване, цитати немає», а **не** "
                "«перевірено»."),
            "notatka": "цитати немає; що саме шукати — у полі `shukaty`",
        })

    vsoho = sum(len(v) for v in posadka.values())
    print(f"кандидатів {len(kandydaty)} | придатних до посадки {vsoho} | "
          f"вже A/B/C {vzhe} | немає в реєстрі {nema} | "
          f"без відмітного префікса {shyrokyy}")
    if not a.pysaty:
        print("\n(суха проба; `--pysaty` щоб записати)")
        return 0

    kudy = ROOT / "factcheck" / "dokazy"
    for fayl, zapys in sorted(posadka.items()):
        shapka = (
            f"# Черга з названим, але недосяжним джерелом — {fayl}.\n"
            f"#\n"
            f"# Посаджено `tools/posadka_c.py`. Клас `C` — розписка з\n"
            f"# адресою, не доказ: документ названо, звідси не дістати.\n"
            f"# Чесніше за `F` («ніхто не дійшов») рівно на одне —\n"
            f"# тут відомо, що саме замовляти.\n\n")
        (kudy / f"cherga-c-{fayl}.yaml").write_text(
            shapka + yaml.safe_dump(zapys, allow_unicode=True,
                                    sort_keys=False, width=88),
            encoding="utf-8")
    print(f"записано файлів: {len(posadka)} → {kudy}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
