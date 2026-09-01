#!/usr/bin/env python3
"""Звід суцільного проходу: третій шар для всього, що назбирали помічники.

## Навіщо

Помічник **заявляє** підтвердження. Заявка не є підтвердженням: у
попередніх хвилях приблизно половина заявлених цитат не знаходилася в
названому документі — переказ замість витягу, згадка з пам'яті,
правильний факт із неправильною адресою.

Тому тут: качаємо кожен названий документ **один раз**, і кожну цитату
шукаємо в ньому **підрядком**. Що не знайшлося — не підтверджено,
хоч би яке правильне воно було по суті.

## Три ворота перед лічбою, і чому саме до

    1. самопосилання   — довідник не є джерелом для себе
    2. без документа   — «не дивився» коштує нуль
    3. не той вердикт  — `pidtverdzheno` без цитати нічого не важить

`n` рахується **після** воріт. Перша редакція `measure_f.py` рахувала до —
інструмент, зроблений проти роздутої звітності, роздував власну. Тут
цієї помилки нема за побудовою: `prydatni` збирається окремим списком.

## Чого цей інструмент НЕ робить

Він не судить, чи витяг **підтримує** твердження. Це другий шар, і він
лишається за людиною: `sperechayetsya` на littlefs був дослівною
цитатою з правильного документа — і прочитаний навпаки.

    factcheck/tools/sweep_digest.py <тека з yaml> [--kesh <тека>]
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

# Довідник не є джерелом для себе. Гілки розробки цього проєкту в
# адресу теж не йдуть, тому перевіряємо власника й теки книги.
RE_SAMA_KNYHA = re.compile(
    r"esp32-handbook|ivoitovych|voytovych"
    r"|(?:^|/)(?:%s|factcheck)/" % "|".join(config.groups()), re.I)

POTREBUYE_CYTATY = {"pidtverdzheno", "sperechayetsya"}


def normalizuy(t: str) -> str:
    """Пробіли до одного, лапки й риски до простих.

    Документи переносять рядки де завгодно, а помічник копіює вже
    склеєне. Порівнювати треба зміст, а не розкладку — але **лише**
    пробіли й типографіку. Слова, числа й регістр лишаються як є:
    саме на них ловиться пам'ять замість документа.
    """
    t = t.replace("\u00a0", " ")
    t = t.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    # Лапки прибираються **зовсім**, а не зводяться до простих.
    #
    # Виміряно: `FreeRTOS Timer Task (Tmr Svc)` гинула проти документа,
    # де стоїть `FreeRTOS Timer Task ("Tmr Svc")`. Це чесний витяг,
    # убитий воротами. Лапки й зворотні апострофи — це розмітка,
    # і в порівнянні їм не місце.
    #
    # Слова, числа й регістр лишаються як є. Саме там ловиться пам'ять
    # замість документа: в тій самій вибірці `serial clock bus (SCL)`
    # проти `serial clock line (SCL)` — і це справжня хиба, яка мусить
    # гинути.
    t = re.sub(r"[\"'`\u00b4\u2018\u2019\u201c\u201d\u00ab\u00bb]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def zavantazh(url: str, kesh: Path) -> str | None:
    """Один документ — одне завантаження за весь звід."""
    fayl = kesh / (hashlib.sha256(url.encode()).hexdigest()[:24] + ".txt")
    if fayl.exists():
        return fayl.read_text(encoding="utf-8", errors="replace")
    r = subprocess.run(["curl", "-sS", "--max-time", "30", url],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    fayl.write_text(r.stdout, encoding="utf-8")
    return r.stdout


def chytay(teka: Path) -> tuple[list[dict], list[str]]:
    zapysy: list[dict] = []
    biti: list[str] = []
    for f in sorted(teka.glob("*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception:
            biti.append(f.name)
            continue
        if isinstance(z, list):
            zapysy += [r for r in z if isinstance(r, dict)]
        else:
            biti.append(f.name)
    return zapysy, biti


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("teka", type=Path)
    p.add_argument("--kesh", type=Path, default=None)
    a = p.parse_args()
    kesh = a.kesh or (a.teka.parent / "kesh-zvodu")
    kesh.mkdir(parents=True, exist_ok=True)

    zapysy, biti = chytay(a.teka)
    print(f"файлів нечитних: {len(biti)}"
          + (f" ({', '.join(biti[:6])}…)" if biti else ""))

    prydatni, samo, bez_dok = [], 0, 0
    for z in zapysy:
        dz = str(z.get("source", "")).strip()
        if RE_SAMA_KNYHA.search(dz):
            samo += 1
        elif not dz.startswith("http"):
            bez_dok += 1
        else:
            prydatni.append(z)

    n = len(prydatni)
    print(f"записів усього {len(zapysy)} | самопосилань {samo} | "
          f"без документа {bez_dok} | придатних {n}")
    if not n:
        return 1

    vydav = collections.Counter(str(z.get("verdykt")) for z in prydatni)
    print(" ".join(f"{k}={v}" for k, v in vydav.most_common()))

    zayavy = [z for z in prydatni
              if str(z.get("verdykt")) in POTREBUYE_CYTATY]
    print(f"\nзаявок із цитатою до перевірки: {len(zayavy)}")

    vyzhyly, zahynuly, nedosyazhni, bez_cytaty = [], [], [], []
    dokumenty: dict[str, str | None] = {}
    for i, z in enumerate(zayavy, 1):
        if i % 25 == 0:
            print(f"  … {i}/{len(zayavy)}", flush=True)
        cyt = str(z.get("quote") or "").strip()
        if not cyt:
            bez_cytaty.append(z)
            continue
        url = str(z["source"]).strip()
        if url not in dokumenty:
            dokumenty[url] = zavantazh(url, kesh)
        tekst = dokumenty[url]
        if tekst is None:
            nedosyazhni.append(z)
        elif normalizuy(cyt) in normalizuy(tekst):
            vyzhyly.append(z)
        else:
            zahynuly.append(z)

    print(f"\n── третій шар ──")
    print(f"  цитата знайшлася дослівно  {len(vyzhyly)}")
    print(f"  цитати в документі немає   {len(zahynuly)}")
    print(f"  документ не завантажився   {len(nedosyazhni)}")
    print(f"  вердикт без цитати         {len(bez_cytaty)}")
    if zayavy:
        print(f"  частка вцілілих заявок     "
              f"{100 * len(vyzhyly) / len(zayavy):.0f} %")

    vyzhyv_id = {str(z.get("odynycya")) for z in vyzhyly}
    (a.teka.parent / "zvid-vyzhyly.yaml").write_text(
        yaml.safe_dump(vyzhyly, allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    (a.teka.parent / "zvid-zahynuly.yaml").write_text(
        yaml.safe_dump(zahynuly, allow_unicode=True, sort_keys=False),
        encoding="utf-8")

    perehlyanuti = {str(z.get("odynycya")) for z in prydatni}
    print(f"\nодиниць переглянуто щонайменше раз: {len(perehlyanuti)}")
    print(f"з них із дослівно звіреним витягом:  {len(vyzhyv_id)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
