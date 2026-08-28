#!/usr/bin/env python3
"""Ворота для нарядів `naryad_f.py` — де джерело названо URL, а не файлом.

## Чим це відрізняється від `intake_wave3.py`

Той чекає поля `fayl` з іменем у кеші: наряд хвилі 3 називав документ,
і помічник лише підтверджував цитату. Наряд `naryad_f` документа не
називає — помічник **шукає його сам** і повертає URL. Отже й ворота
інші: документ треба спершу дістати за тим URL, і аж потім шукати в
ньому цитату.

## Восьмий закон, у коді а не в проханні

Закон М1: **що качаєш — те й у маніфест, у тому самому кроці.** Купили
його дорого: контрольний прогін дав два підтвердження на
`sn65hvd230.pdf`, який помічник узяв сам, — і докази народилися
невідтворними, бо маніфест про той файл не знав.

Тут це не порада в наряді, а частина проходу: файл, завантажений під
час звірки, лягає в маніфест **до того**, як його текст піде на
порівняння. Розірвати ці два кроки не можна, бо їх робить один цикл.

## Що саме перевіряється

    покриття     чи опрацьовано рівно ті одиниці, що у вибірці
    ворота       самопосилання на довідник — відкидається механічно
    форма        поля, обов'язкові для кожного вердикту
    дослівність  цитата мусить бути ПІДРЯДКОМ названого документа

Нежорсткість береться з `intake_wave3.normal` без змін: вона куплена
вимірами (лапки коштували сім відсотків чесних витягів), і другий її
примірник розійшовся б із першим.

    tools/intake_f.py <тека прогону>
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
KESH = ROOT / "dzherela-kesh"
sys.path.insert(0, str(ROOT / "tools"))

KNYHA = re.compile(
    r"esp32-handbook|ivoitovych|voytovych|/(manual|kartky|dodatky|inserts)/",
    re.I)

# Що вимагає кожен вердикт. Джерело — таблиця в самому наряді; якщо
# вона розійдеться з цим словником, розійдуться наряд і ворота, і
# помічник буде покараний за те, чого йому не казали.
POTREBUYE = {
    "pidtverdzheno": ("dzherelo", "cytata"),
    "sperechayetsya": ("dzherelo", "cytata", "susidnye"),
    "ne_znayshov": ("dzherelo",),
    "nedosyazhne": ("dzherelo", "potribno"),
    "porada": ("chomu",),
}


def imya_dlya(url: str) -> str:
    baza = re.sub(r"[^\w.-]", "_", url.rsplit("/", 1)[-1] or "bez-imeni")
    return f"{hashlib.sha256(url.encode()).hexdigest()[:8]}-{baza}"[:96]


def dodaty_v_manifest(imya: str, sha: str, rozmir: int, url: str) -> None:
    """Восьмий закон. Викликається ПЕРЕД звіркою тексту, не після."""
    m = KESH / "MANIFEST.md"
    t = m.read_text(encoding="utf-8")
    if f"| `{imya}` |" in t:
        return
    ryadky = re.findall(r"^\| `[^`]+` \| `[0-9a-f]{64}` \|[^\n]*$", t, re.M)
    novyy = f"| `{imya}` | `{sha}` | {rozmir} | 2026-08-28 | <{url}> |"
    m.write_text(t.replace(ryadky[-1], ryadky[-1] + "\n" + novyy),
                 encoding="utf-8")


def dokument(url: str, kachaty: bool) -> str | None:
    """Текст документа за URL. Качає, якщо його ще немає в кеші."""
    import citaty
    import intake_wave3
    cil = KESH / imya_dlya(url)
    if not cil.exists():
        if not kachaty or not citaty.zavantazhyty(url, cil):
            return None
        syri = cil.read_bytes()
        dodaty_v_manifest(cil.name, hashlib.sha256(syri).hexdigest(),
                          len(syri), url)
    t = citaty.tekst_dzherela(cil)
    return intake_wave3.normal(t) if t else None


def main() -> int:
    import intake_wave3

    p = argparse.ArgumentParser()
    p.add_argument("teka", type=pathlib.Path)
    p.add_argument("--bez-merezhi", action="store_true")
    a = p.parse_args()

    vyb = json.loads((a.teka / "vybirka.json").read_text(encoding="utf-8"))
    chekaly = set(vyb["vzyato"])

    vidpovidi: dict[str, dict] = {}
    dubli, bytyy = [], []
    for f in sorted(a.teka.glob("q*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception as e:
            bytyy.append(f"{f.name}: {str(e).splitlines()[0][:80]}")
            continue
        if not isinstance(z, list):
            bytyy.append(f"{f.name}: не список")
            continue
        for r in z:
            if not isinstance(r, dict):
                continue
            ident = str(r.get("odynycya") or r.get("id") or "?").strip()
            if ident in vidpovidi:
                dubli.append(ident)
            vidpovidi[ident] = dict(r, _fayl=f.name)

    lishnі = sorted(set(vidpovidi) - chekaly)
    bez = sorted(chekaly - set(vidpovidi))

    rody = collections.Counter()
    bidy: list[tuple[str, str, str]] = []
    dosl = collections.Counter()
    for ident, r in sorted(vidpovidi.items()):
        v = str(r.get("verdykt") or "").strip()
        rody[v or "(немає вердикту)"] += 1
        if v not in POTREBUYE:
            bidy.append((ident, "ВЕРДИКТ ПОЗА НАРЯДОМ", v[:40]))
            continue
        brak = [k for k in POTREBUYE[v] if not str(r.get(k) or "").strip()]
        if brak:
            bidy.append((ident, "БРАКУЄ ПОЛІВ", ",".join(brak)))
        dzh = str(r.get("dzherelo") or "")
        if dzh and KNYHA.search(dzh):
            bidy.append((ident, "САМОПОСИЛАННЯ НА ДОВІДНИК", dzh[:46]))
        elif dzh and not dzh.startswith("http"):
            bidy.append((ident, "ДЖЕРЕЛО НЕ Є АДРЕСОЮ", dzh[:46]))

        if v not in ("pidtverdzheno", "sperechayetsya"):
            continue
        cyt = str(r.get("cytata") or "").strip()
        if not cyt or not dzh.startswith("http"):
            continue
        t = dokument(dzh, not a.bez_merezhi)
        if t is None:
            dosl["документ не дістався"] += 1
            bidy.append((ident, "ДОКУМЕНТ НЕ ДІСТАВСЯ", dzh[:46]))
        elif intake_wave3.normal(cyt) in t:
            dosl["цитата дослівна"] += 1
        else:
            dosl["ЦИТАТИ В ДОКУМЕНТІ НЕМАЄ"] += 1
            bidy.append((ident, "ЦИТАТИ В ДОКУМЕНТІ НЕМАЄ", cyt[:46]))

    print("вибірка %d · відповідей %d · без відповіді %d · зайвих %d · дублів %d"
          % (len(chekaly), len(vidpovidi), len(bez), len(lishnі), len(dubli)))
    if bytyy:
        print("\nбиті файли:")
        for b in bytyy:
            print("   ✗ " + b)
    print("\nвердикти:")
    for k, n in rody.most_common():
        print("   %-18s %3d  (%4.1f %%)" % (k, n, 100 * n / max(len(vidpovidi), 1)))
    if dosl:
        print("\nтретій шар — цитати, що заявлені дослівними:")
        for k, n in dosl.most_common():
            print("   %-28s %d" % (k, n))
    print("\nпорушень: %d" % len(bidy))
    for ident, rid, dod in bidy[:40]:
        print("   ✗ %-11s %-28s %s" % (ident, rid, dod))
    if bez:
        print("\nбез відповіді: %s" % ", ".join(bez))
    return 1 if (bidy or bytyy or bez) else 0


if __name__ == "__main__":
    sys.exit(main())
