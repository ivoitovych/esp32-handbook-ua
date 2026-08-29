#!/usr/bin/env python3
"""Ворота для нарядів `work_orders_f.py` — де джерело названо URL, а не файлом.

## Чим це відрізняється від `intake_wave3.py`

Той чекає поля `fayl` з іменем у кеші: наряд хвилі 3 називав документ,
і помічник лише підтверджував цитату. Наряд `work_orders_f` документа не
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
    tools/intake_f.py --self-check      import-and-run smoke test

`--self-check` exists because this tool sat broken for an hour: a merge
renamed `citaty` to `layer3`, the import at the top of `dokument()` was
never reached during a dry read, and nothing failed until a real run.
The tool had no `make` target, so nothing ran it.

> A tool outside the check suite is a tool whose breakage is discovered
> by the next person who needs it, at the moment they need it.
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
KESH = ROOT / "source-cache"
sys.path.insert(0, str(ROOT / "tools"))

KNYHA = re.compile(
    r"esp32-handbook|ivoitovych|voytovych|/(manual|kartky|dodatky|inserts)/",
    re.I)

# Що вимагає кожен вердикт. Джерело — таблиця в самому наряді; якщо
# вона розійдеться з цим словником, розійдуться наряд і ворота, і
# помічник буде покараний за те, чого йому не казали.
# Англійські імена — чинні; транслітеровані приймаються, поки живі
# наряди попередніх версій. Розширити → переїхати → звузити, той самий
# порядок, що й для полів запису доказу.
POTREBUYE = {
    "confirmed": ("source", "quote"),
    "disputes": ("source", "quote", "neighbours"),
    "not_found": ("source",),
    "unreachable": ("source", "needed"),
    "advice": ("why",),
    # Додано М1 разом зі спекою завдання. Обидва — не зручність, а
    # **розрізнення, яке інакше зникає**:
    #
    #   truly_none          зовнішнього референта справді немає; це
    #                       позиція автора. Не те саме, що `advice`
    #                       («не дістав, але знаю де») і не те саме, що
    #                       `not_found` («не зміг встановити»)
    #   absent_from_source  документ отримано, і його МОВЧАННЯ і є
    #                       доказ (клас `N`). Протилежність
    #                       `not_found`: там не встановили, тут
    #                       встановили саме відсутністю
    #
    # Звести їх до наявних означало б попросити помічника відповісти
    # словом, яке каже не те, що він зробив, — і втратити різницю в
    # обліку назавжди.
    "truly_none": ("why",),
    "absent_from_source": ("source", "absent"),
}
STARI_VERDYKTY = {
    "pidtverdzheno": "confirmed", "sperechayetsya": "disputes",
    "ne_znayshov": "not_found", "nedosyazhne": "unreachable",
    "porada": "advice",
    "spravdi-e": "truly_none", "spravdi_e": "truly_none",
}
STARI_POLYA = {
    "odynycya": "unit", "verdykt": "verdict", "dzherelo": "source",
    "cytata": "quote", "komentar": "comment", "potribno": "needed",
    "chomu": "why", "susidnye": "neighbours",
}


def na_anhliysku(r: dict) -> dict:
    """Запис у чинних іменах, звідки б він не прийшов.

    Ворота не мають права карати помічника за те, якою мовою був наряд,
    що йому дали. Переклад тут — не поблажливість, а межа: після нього
    решта проходу знає рівно один словник.
    """
    out = {STARI_POLYA.get(k, k): v for k, v in r.items()}
    v = str(out.get("verdict") or "").strip()
    if v in STARI_VERDYKTY:
        out["verdict"] = STARI_VERDYKTY[v]
    return out


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
    import layer3
    import intake_wave3
    cil = KESH / imya_dlya(url)
    if not cil.exists():
        if not kachaty or not layer3.zavantazhyty(url, cil):
            return None
        syri = cil.read_bytes()
        dodaty_v_manifest(cil.name, hashlib.sha256(syri).hexdigest(),
                          len(syri), url)
    t = layer3.tekst_dzherela(cil)
    return intake_wave3.normal(t) if t else None


def self_check() -> int:
    """Прогін на порожньому входу: імпорти, шляхи, кеш."""
    import tempfile
    import json as _json
    bidy = []
    try:
        import layer3, intake_wave3  # noqa: F401
    except Exception as e:
        bidy.append("import: %s" % str(e)[:70])
    if not KESH.exists():
        bidy.append("кеш джерел не там: %s" % KESH)
    if not (KESH / "MANIFEST.md").exists():
        bidy.append("маніфесту немає в %s" % KESH)
    try:
        with tempfile.TemporaryDirectory() as d:
            t = pathlib.Path(d)
            (t / "vybirka.json").write_text(
                _json.dumps({"vzyato": [], "queue": "F"}), encoding="utf-8")
            import subprocess
            r = subprocess.run([sys.executable, __file__, str(t)],
                               capture_output=True, text=True, timeout=120)
            if "вибірка 0" not in r.stdout:
                bidy.append("порожній прогін не пройшов: %s"
                            % (r.stderr or r.stdout)[-90:])
    except Exception as e:
        bidy.append("порожній прогін: %s" % str(e)[:70])
    for b in bidy:
        print("   ✗ " + b)
    print("intake_f self-check: %d проблем" % len(bidy))
    return 1 if bidy else 0


def main() -> int:
    if "--self-check" in sys.argv:
        return self_check()
    import intake_wave3

    p = argparse.ArgumentParser()
    p.add_argument("teka", type=pathlib.Path)
    p.add_argument("--bez-merezhi", action="store_true")
    p.add_argument("--ledger", action="store_true",
                   help="дописати підсумок прогону у factcheck/reports/RUNS.md")
    p.add_argument("--model", default="haiku-4.5")
    p.add_argument("--note", default="")
    p.add_argument("--compare", type=pathlib.Path, default=None,
                   help="попарне порівняння з іншим прогоном тих самих одиниць")
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
            r = na_anhliysku(r)
            ident = str(r.get("unit") or r.get("id") or "?").strip()
            if ident in vidpovidi:
                dubli.append(ident)
            vidpovidi[ident] = dict(r, _fayl=f.name)

    lishnі = sorted(set(vidpovidi) - chekaly)
    bez = sorted(chekaly - set(vidpovidi))

    rody = collections.Counter()
    bidy: list[tuple[str, str, str]] = []
    dosl = collections.Counter()
    for ident, r in sorted(vidpovidi.items()):
        v = str(r.get("verdict") or "").strip()
        rody[v or "(немає вердикту)"] += 1
        if v not in POTREBUYE:
            bidy.append((ident, "ВЕРДИКТ ПОЗА НАРЯДОМ", v[:40]))
            continue
        brak = [k for k in POTREBUYE[v] if not str(r.get(k) or "").strip()]
        if brak:
            bidy.append((ident, "БРАКУЄ ПОЛІВ", ",".join(brak)))
        dzh = str(r.get("source") or "")
        if dzh and KNYHA.search(dzh):
            bidy.append((ident, "САМОПОСИЛАННЯ НА ДОВІДНИК", dzh[:46]))
        elif dzh and not dzh.startswith("http"):
            bidy.append((ident, "ДЖЕРЕЛО НЕ Є АДРЕСОЮ", dzh[:46]))

        if v not in ("confirmed", "disputes"):
            continue
        cyt = str(r.get("quote") or "").strip()
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

    if a.compare:
        porivnyaty(a.compare, a.teka, vidpovidi)
    if a.ledger:
        zapysaty_ledger(a, vyb, vidpovidi, rody, dosl, bidy)
    return 1 if (bidy or bytyy or bez) else 0


def chytaty(teka: pathlib.Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted(teka.glob("q*.yaml")):
        try:
            z = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for r in z:
            if isinstance(r, dict):
                r = na_anhliysku(r)
                out[str(r.get("unit") or r.get("id") or "?").strip()] = r
    return out


def porivnyaty(bula: pathlib.Path, stala: pathlib.Path,
               teper: dict[str, dict]) -> None:
    """Та сама одиниця під двома нарядами.

    ## Навіщо попарно, а не за частками

    Частки двох прогонів на РІЗНИХ вибірках різняться завжди, і
    приписати різницю нарядові не можна: змінилися дві речі. Тут
    вибірка та сама, тож видно не лише зсув чисел, а й **які саме
    одиниці змінили вердикт і в який бік** — а це вже привід відкрити
    їх і подивитися.

    Одне застереження, і воно суттєве: **помічник недетермінований.**
    Той самий наряд на тих самих одиницях дав би теж не те саме. Тому
    різниця тут — це різниця наряду ПЛЮС шум, і без третього прогону
    під першою версією їх не розділити. Кажу це тут, щоб таблиця не
    читалася як доказ.
    """
    ranishe = chytaty(bula)
    spilni = sorted(set(ranishe) & set(teper))
    if not spilni:
        print("\nпорівняти нема з чим: спільних одиниць 0")
        return
    perekhody: dict[tuple, int] = {}
    for i in spilni:
        a = str(ranishe[i].get("verdict") or "?")
        b = str(teper[i].get("verdict") or "?")
        perekhody[(a, b)] = perekhody.get((a, b), 0) + 1
    tryvko = sum(n for (a, b), n in perekhody.items() if a == b)
    print("\n=== попарно з `%s`: %d спільних одиниць ===" % (bula.name, len(spilni)))
    print("   вердикт не змінився: %d (%.0f %%)" % (tryvko, 100 * tryvko / len(spilni)))
    zmin = {k: v for k, v in perekhody.items() if k[0] != k[1]}
    if zmin:
        print("   переходи:")
        for (a, b), n in sorted(zmin.items(), key=lambda x: -x[1]):
            print("      %-14s → %-14s %d" % (a, b, n))


LEDGER_SHAPKA = """# Runs of the helper pool

**Generated by `tools/intake_f.py --ledger`.** One row per run, appended,
never edited.

## Why this file exists

The work order **is** the part of the technology that acts on the
helper. It changed nine times, and each change was measured — but the
result could not be attributed to the change, because nothing in a run
recorded which order produced it. Comparing waves rested on a
maintainer's memory.

Every generated order now carries `order_version` — eight characters of
the hash of its own template — and so does the run's sample file. This
table joins the two.

> Changing the work order changes the technology. Changing a technology
> without a version is not an experiment; it is weather.

**How to read it.** Two rows with the same `order_version` are the same
technology measured twice: a difference between them is noise, queue, or
model. Two rows with different versions are two technologies: a
difference between them is a **result**, and the diff between the two
versions is its cause.

**What a row cannot tell you.** Sample size here is small, the queues
are not equivalent (`F` yields several times what an `E`-verdict audit
does), and a run is not repeated. A row is evidence, not proof.

| date | order | seed | queue | n | model | confirmed | survived L3 | not found | advice | self-ref | violations |
|---|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
"""


def zapysaty_ledger(a, vyb, vidpovidi, rody, dosl, bidy) -> None:
    """Дописати рядок прогону. Дописати, не переписати: попередні
    прогони — це вимір, а не чернетка."""
    f = ROOT / "factcheck" / "RUNS.md"
    if not f.exists():
        f.write_text(LEDGER_SHAPKA, encoding="utf-8")
    t = f.read_text(encoding="utf-8")
    samo = sum(1 for _, rid, _ in bidy if "САМОПОСИЛАННЯ" in rid)
    ryadok = ("| %s | `%s` | %s | %s | %d | %s | %d | %d | %d | %d | %d | %d |"
              % (a.teka.name,
                 vyb.get("task_version", "?"),
                 vyb.get("nasinnya", "?"),
                 vyb.get("queue", "?"),
                 len(vidpovidi),
                 a.model,
                 rody.get("confirmed", 0),
                 dosl.get("цитата дослівна", 0),
                 rody.get("not_found", 0),
                 rody.get("advice", 0),
                 samo,
                 len(bidy)))
    if a.note:
        ryadok += "\n\n> `%s`: %s\n" % (a.teka.name, a.note)
    f.write_text(t.rstrip("\n") + "\n" + ryadok + "\n", encoding="utf-8")
    print("\nдописано в factcheck/reports/RUNS.md")


if __name__ == "__main__":
    sys.exit(main())
