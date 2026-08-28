#!/usr/bin/env python3
"""Перейменування інструментів: транслітерована українська → англійська.

## Навіщо окремий інструмент, а не заміна за рядком

Бо заміну за рядком ми вже робили, і вона коштувала дев'яти зламів,
кожен із яких виглядав як робочий код. Роди 23 і 25 у `DEFECTS.md`
описують рівно це: заміна перейменувала обидві сторони запасного
виразу; читач поїхав, а писач лишився; схему, яка не переїжджає, теж
зачепило.

Тому тут не «замінити слово», а три різні дії з різними правилами:

    у коді      `import X`, `from X import`, і `X.щось` — **лише** якщо
                цей файл справді імпортує `X`. Інакше `polya.` в
                місцевому словнику стане `struct_fields.`
    у шляхах    `tools/X.py` і `` `X.py` `` — усюди, крім незмінного
    у даних     поле `method` записів доказів: воно каже, **як
                перевірити ще раз**, тож ім'я в ньому має лишатися
                чинним, інакше запис перестає бути виконуваним

## Чого не чіпає, і чому

    zvyazok/        листування супровідників незмінне за протоколом
    HISTORY.*.md    журнал зробленого: це розповідь про той день
    reviews/        отримані рецензії — чужі документи

Посилання на старі імена там лишаються навмисно. Документ про минуле,
переписаний під сьогоднішні імена, перестає бути документом про
минуле.

    tools/renames.py --pokazaty          що буде перейменовано
    tools/renames.py --tilky citaty      один інструмент
    tools/renames.py --usi               усі з таблиці
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Ім'я має казати, **що інструмент робить**, а не як це слово звучить
# українською. Тому не `citaty → quotes`, а `citaty → layer3`: він і є
# третій шар, і поруч уже стоять `layer1` та `layer1_units`.
TABLYCYA = {
    "arytmetyka": "arithmetic",
    "bez_slenhu": "deslang",
    "citaty": "layer3",
    "imena": "field_names",
    "kalky": "calques",
    "kesh": "cache",
    "leady": "leads",
    "mira_f": "measure_f",
    "modalnist": "modality",
    "naryad": "work_orders",
    "naryad_f": "work_orders_f",
    "piny": "pins",
    "podil": "split_queue",
    "pokazhchyk": "book_index",
    # НЕ `fields`: цей інструмент перевіряє імена полів **структур
    # ESP-IDF у прикладах книги**, а не поля записів доказів. Два різні
    # «поля», і сплутати їх — рід 23.
    "polya": "struct_fields",
    "posadka_c": "land_c",
    "posylannya": "cross_refs",
    "pravopys": "spelling",
    "prochid": "sweep",
    "prochid_posadka": "sweep_land",
    "prochid_zvid": "sweep_digest",
    "shturm": "contest_e",
    "skhema": "schema",
    "sprostovane": "refuted",
    "techa": "leak",
    "vybirka": "sample",
    "vyvantazh": "helper_dumps",
    "znimok": "snapshot",
    "zvyazok": "correspondence",
}

# Інструменти М2 (`*-m2.py`) не чіпаємо: перейменувати чужий інструмент
# посеред їхньої хвилі — це рівно та колізія, від якої ми весь день
# тікаємо. Пропозиція піде листом.
NE_CHIPATY = {"naryad-m2", "perevirka-tsytat-m2"}

NEZMINNI = ("zvyazok/", "HISTORY.", "reviews/", ".git/", "__pycache__")


def obhid():
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        vidn = str(p.relative_to(ROOT))
        if any(vidn.startswith(x) or f"/{x}" in vidn for x in NEZMINNI):
            continue
        if p.suffix in (".pdf", ".png", ".jpg", ".bin", ".pyc"):
            continue
        yield p, vidn


def importuye(tekst: str, modul: str) -> bool:
    return bool(re.search(rf"^\s*(?:import\s+{re.escape(modul)}\b"
                          rf"|from\s+{re.escape(modul)}\s+import)",
                          tekst, re.M))


def perepysaty(tekst: str, stare: str, nove: str, kod: bool) -> tuple[str, int]:
    n = 0

    def lich(m):
        nonlocal n
        n += 1
        return m.group(0).replace(stare, nove)

    # Шлях і згадка файлу — усюди.
    tekst = re.sub(rf"\b{re.escape(stare)}\.py\b", lich, tekst)

    if kod:
        # Імпорт — лише в коді.
        tekst = re.sub(rf"^\s*import\s+{re.escape(stare)}\b",
                       lich, tekst, flags=re.M)
        tekst = re.sub(rf"^(\s*)from\s+{re.escape(stare)}\s+import",
                       lich, tekst, flags=re.M)
        # Доступ до модуля — **лише якщо файл його імпортує**.
        if importuye(tekst, stare) or importuye(tekst, nove):
            tekst = re.sub(rf"\b{re.escape(stare)}\.(?=[a-zA-Z_])", lich, tekst)
    return tekst, n


def zrobyty(pary: dict[str, str], suho: bool) -> int:
    torknuto = 0
    for stare, nove in pary.items():
        dzherelo = ROOT / "tools" / f"{stare}.py"
        if not dzherelo.exists():
            print(f"  ! немає {dzherelo.relative_to(ROOT)}")
            continue
        if not suho:
            subprocess.run(["git", "mv", str(dzherelo),
                            str(ROOT / "tools" / f"{nove}.py")],
                           cwd=ROOT, check=True)
        print(f"  {stare}.py → {nove}.py")

    for p, vidn in obhid():
        try:
            t = st = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        vsjogo = 0
        for stare, nove in pary.items():
            t, n = perepysaty(t, stare, nove, kod=p.suffix == ".py")
            vsjogo += n
        if vsjogo and t != st:
            torknuto += 1
            print(f"    {vidn}: {vsjogo}")
            if not suho:
                p.write_text(t, encoding="utf-8")
    return torknuto


def main() -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--tilky", action="append", default=[],
                   help="перейменувати лише названі")
    a.add_argument("--usi", action="store_true")
    a.add_argument("--pokazaty", action="store_true",
                   help="нічого не міняти, лише показати")
    o = a.parse_args()

    pary = ({k: v for k, v in TABLYCYA.items() if k in o.tilky}
            if o.tilky else TABLYCYA if (o.usi or o.pokazaty) else {})
    if not pary:
        print("вкажіть --tilky <ім'я> або --usi (чи --pokazaty)")
        return 2
    nevidomi = set(o.tilky) - set(TABLYCYA)
    if nevidomi:
        print(f"невідомі імена: {', '.join(sorted(nevidomi))}")
        return 2

    print(f"перейменувань: {len(pary)}"
          f"{'  (СУХИЙ ПРОГІН)' if o.pokazaty else ''}")
    n = zrobyty(pary, suho=o.pokazaty)
    print(f"файлів торкнуто: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
