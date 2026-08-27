#!/usr/bin/env python3
"""Модальність: припис у книзі проти дозволу в джерелі.

## Рід хиби, якого не ловив жоден із трьох шарів

Знайшов помічник за два долари, не інструмент. Одиниця `T-11-062`:

    книга:   «Саме він має лежати в git, а не `sdkconfig`.»
    джерело: «The sdkconfig file **may or may not** be added to the
              source control system … It is **recommended** to commit
              sdkconfig.defaults»

Цитата дослівна, джерело справжнє, факт правильний — **усі три шари
проходять**. Розходиться лише **модальність**: джерело дозволяє,
книга приписує.

> Це не хиба факту й не хиба джерела. Це припис, поданий так, ніби він
> задокументований, — і третій шар його не ловить за побудовою, бо
> звіряє символи, а не силу твердження.

Такий припис не обов'язково хибний: довідник для того й пишуть, щоб
давати обґрунтовану позицію. Але читач має бачити різницю між «так
велить документація» і «так вважає автор, і ось чому».

## Чому це звіт, а не ворота

Перша редакція виразу давала **50 збігів**, і перші ж два перевірені
виявилися хибними — причому повчально:

    книга:   «Потрібне зниження **обов'язково**»
    джерело: «Stresses above … **may cause** permanent damage»

`may` тут — не дозвіл, а **попередження**. Книжкове «обов'язково»
цілком виправдане межею 3.6 В.

Після виправлення виразу лишилося **6**. Тобто інструмент, який
починався з 88 % хибних спрацювань, став придатним лише після того,
як його перевірили на власних знахідках.

Судити все одно має людина: чи припис обґрунтований, чи його треба
пом'якшити. Тому це рядок звіту, а не зупинка випуску.

    tools/modalnist.py [-v]
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

# Припис у книзі: сила, яку джерело мусить підтверджувати.
RE_PRYPYS = re.compile(
    r"\b(має|мусить|мусять|не можна|завжди|ніколи|обов'язково)\b", re.I)

# Дозвіл у джерелі. **Обережно з `may`**: `may cause`, `may result`,
# `may lead` — це попередження про наслідок, протилежне дозволу.
# Перша редакція їх не відрізняла й давала 50 збігів замість 6.
RE_DOZVIL = re.compile(
    r"\b(?:it is )?recommended\b"
    r"|\bmay or may not\b"
    r"|\boptional(?:ly)?\b"
    r"|\bmay be\b(?!\s+(?:damaged|destroyed))"
    r"|\bcan optionally\b"
    r"|\bif desired\b"
    r"|\bis not required\b", re.I)


def main() -> int:
    import vybirka

    odyn = [u for k in "ABCDEFGK" for u in vybirka.odynyci(k)]
    znayd = []
    for f in sorted((ROOT / "factcheck" / "dokazy").glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for r in z:
            if not isinstance(r, dict) or str(r.get("klas")) not in ("A", "B"):
                continue
            m = RE_DOZVIL.search(str(r.get("cytata") or ""))
            if not m:
                continue
            try:
                rx = re.compile(str(r.get("zbih", "")))
            except re.error:
                continue
            for u in odyn:
                if rx.search(u["tekst"]) and RE_PRYPYS.search(u["tekst"]):
                    znayd.append((u["id"], f.name, u["tekst"], m.group(0)))

    if "-v" in sys.argv:
        for oid, fayl, tekst, slovo in znayd:
            print(f"   · {oid}: «{slovo}» у джерелі, припис у книзі")
            print(f"        {tekst[:96]}")
            print(f"        ← {fayl}")
    print(f"modalnist: приписів проти дозволу в джерелі: {len(znayd)} "
          f"— судить людина, це не помилка сама по собі")
    return 0


if __name__ == "__main__":
    sys.exit(main())
