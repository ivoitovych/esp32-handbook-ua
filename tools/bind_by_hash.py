#!/usr/bin/env python3
"""Migration stage 4: bind evidence to claims by hash, not by pattern.

## What a pattern actually is

An evidence record says which claims it covers with a regex over the
claim's text:

    match: Ядер\\s+·\\s+C3\\s+→\\s+1|Wi-Fi\\s+·\\s+C3\\s+→\\s+так|…

That text is a **render**: `factcheck.py` builds it from a table row,
and `·` / `→` exist nowhere in the book. So the pattern is written
against a format this repository owns and can change — and did change,
twice this week, silently.

The exact binding it should have used already exists and already works:

    sha: [f98283f2, 3161b4c1]

`vsi_kandydaty` prefers it over any pattern. Nothing had to be
invented; 1337 records simply never used it.

## Why not "match the raw book line" instead

That was the original plan for this stage, and measuring killed it:
**5225 of 8331 claims share a book line with another claim**, up to ten
per line — a table row holds many cells. A pattern over the raw line
cannot tell them apart, so it would take this project's worst failure
mode (a wide pattern silently marking unchecked claims as verified) and
make it structural for 63 % of the registry.

The hash has neither problem. It is exact, it survives renumbering, and
it **detaches itself** when the wording changes — which is correct: the
evidence was about those words, not these.

## Why records migrate in groups

Exact binding wins over patterns. So if record A gains a `sha` list
covering claim X while record B still reaches X by pattern, B **loses**
X — the migration would silently move a claim from one evidence record
to another.

Records that share a claim therefore migrate together. The connected
components are:

    713 records  alone            — safe one at a time
     49 pairs, 6 triples          — migrate as a unit
      1 component of 508 records  — 4444 bindings, all tangled

That last one is a finding in its own right: 508 evidence records are
transitively coupled because their patterns overlap.

This tool refuses to write a record whose component is not fully
selected. That refusal is the whole safety of the stage.

    tools/bind_by_hash.py --only pass-40           dry run
    tools/bind_by_hash.py --only pass-40 --write   write
    tools/bind_by_hash.py --components             sizes only
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

DOKAZY = ROOT / "factcheck" / "dokazy"


def zibraty() -> tuple[list[dict], dict[str, list[str]]]:
    """Records with a stable key, and what each currently binds."""
    import factcheck
    import vybirka

    odyn = [u for k in "ABCDEFGK" for u in vybirka.odynyci(k)]
    zapysy: list[dict] = []
    for f in sorted(DOKAZY.glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for i, r in enumerate(z):
            if isinstance(r, dict):
                r["_fayl"], r["_nomer"] = f.name, i
                r["_klyuch"] = f"{f.name}::{i}"
                zapysy.append(r)

    zv: dict[str, list[str]] = {z["_klyuch"]: [] for z in zapysy}
    for u in odyn:
        for z in factcheck.vsi_kandydaty(zapysy, u["sha"], u["tekst"]):
            zv[z["_klyuch"]].append(u["sha"])
    return zapysy, {k: sorted(set(v)) for k, v in zv.items()}


def komponenty(zv: dict[str, list[str]]) -> dict[str, str]:
    """Record key → representative of its component."""
    batko = {k: k for k in zv}

    def znayty(x: str) -> str:
        while batko[x] != x:
            batko[x] = batko[batko[x]]
            x = batko[x]
        return x

    vlasnyk: dict[str, list[str]] = collections.defaultdict(list)
    for k, v in zv.items():
        for s in v:
            vlasnyk[s].append(k)
    for ks in vlasnyk.values():
        for k in ks[1:]:
            a, b = znayty(ks[0]), znayty(k)
            if a != b:
                batko[a] = b
    return {k: znayty(k) for k in zv}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--only", default=None,
                   help="підрядок імені файлу доказів")
    p.add_argument("--safe", action="store_true",
                   help="усі записи, чия родина не більша за --do")
    p.add_argument("--do", type=int, default=3,
                   help="найбільша родина, яку беремо (типово 3)")
    p.add_argument("--limit", type=int, default=0,
                   help="узяти не більше N родин — щоб дивитися партіями")
    p.add_argument("--write", action="store_true")
    p.add_argument("--components", action="store_true")
    a = p.parse_args()

    zapysy, zv = zibraty()
    predst = komponenty(zv)
    rozmir = collections.Counter(predst.values())

    if a.components:
        print(f"записів {len(zv)}, компонент {len(set(predst.values()))}")
        for n, skilky in sorted(collections.Counter(
                rozmir.values()).items()):
            print(f"  компонент по {n:>3} записів: {skilky}")
        return 0

    if a.safe:
        # Родини беремо цілими й у сталому порядку: партія має бути
        # відтворюваною, інакше «перевірено на партії 1» нічого не
        # означає для того, хто повторить прогін.
        rodyny = sorted(
            {p for p in predst.values() if rozmir[p] <= a.do},
            key=lambda p: sorted(k for k in predst if predst[k] == p)[0])
        # Уже переїхалі — пропускаємо, щоб партії йшли вперед.
        gotovi = {z["_klyuch"] for z in zapysy if z.get("sha")}
        rodyny = [p for p in rodyny
                  if not {k for k in predst if predst[k] == p} <= gotovi]
        if a.limit:
            rodyny = rodyny[:a.limit]
        vybrani = {k for k in predst if predst[k] in set(rodyny)}
        print(f"родин узято {len(rodyny)}, записів {len(vybrani)} "
              f"(вже переїхало {len(gotovi)})")
    elif a.only:
        vybrani = {z["_klyuch"] for z in zapysy if a.only in z["_fayl"]}
    else:
        print("вкажіть --only, --safe або --components")
        return 1

    if not vybrani:
        print("нічого не вибрано")
        return 1

    # Ось та сама відмова, заради якої існує цей інструмент.
    nepovni: dict[str, set[str]] = {}
    for k in vybrani:
        rodyna = {x for x in predst if predst[x] == predst[k]}
        if not rodyna <= vybrani:
            nepovni[k] = rodyna - vybrani
    if nepovni:
        print(f"ВІДМОВА: {len(nepovni)} записів мають родичів поза вибіркою.")
        print("Точна прив'язка перебиває взірець, тож переїзд половини")
        print("родини мовчки відібрав би одиниці в другої половини.\n")
        for k, resh in list(nepovni.items())[:6]:
            print(f"  {k}\n      разом з: {', '.join(sorted(resh)[:4])}"
                  f"{' …' if len(resh) > 4 else ''}")
        return 1

    perepysaty = {k: zv[k] for k in vybrani if zv[k]}
    porozhni = [k for k in vybrani if not zv[k]]

    print(f"вибрано записів {len(vybrani)}, з них із прив'язками "
          f"{len(perepysaty)}, холостих {len(porozhni)}")
    for k in sorted(perepysaty):
        print(f"  {k:<44} одиниць {len(perepysaty[k])}")
    for k in porozhni:
        print(f"  ⚠ {k}: взірець не чіпляє нічого — переїзд лишив би "
              f"порожній `sha`, тож запис пропущено")

    if not a.write:
        print("\n(суха проба; `--write` щоб записати)")
        return 0

    torknuly: dict[str, list] = {}
    for z in zapysy:
        if z["_klyuch"] in perepysaty:
            torknuly.setdefault(z["_fayl"], []).append(z)

    for imya, zap in torknuly.items():
        f = DOKAZY / imya
        vsi = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        for z in zap:
            vsi[z["_nomer"]]["sha"] = perepysaty[z["_klyuch"]]
        tekst = f.read_text(encoding="utf-8")
        shapka = "".join(ln for ln in tekst.splitlines(keepends=True)
                         if ln.startswith("#") or not ln.strip())
        shapka = (shapka[:shapka.rfind("\n\n") + 2]
                  if "\n\n" in shapka else shapka)
        f.write_text(shapka + yaml.safe_dump(vsi, allow_unicode=True,
                                             sort_keys=False, width=88),
                     encoding="utf-8")
        print(f"  записано {imya}: {len(zap)} записів")

    print("\nтепер: tools/znimok.py <знімок> --zvirty — має бути нуль змін")
    return 0


if __name__ == "__main__":
    sys.exit(main())
