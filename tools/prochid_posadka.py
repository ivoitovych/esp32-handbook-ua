#!/usr/bin/env python3
"""Посадка суцільного проходу: зі скрині помічників — у реєстр доказів.

## Навіщо окремий крок

Прохід, що лежить у тимчасовій теці, для реєстру **не існує**. Поки
його не посаджено у `factcheck/dokazy/`, жоден інструмент його не
бачить, `vorota` не боронять, а наступна хвиля пройде ті самі одиниці
вдруге. Робота без посадки — це робота, якої не було.

## Взірець виводиться сам, і це найтонше місце

Схема вимагає `zbih` — вираз, що чіпляє доказ до одиниць. Записані
закони проєкту тягнуть у різні боки:

* **широкий взірець небезпечніший за відсутній** — він мовчки позначає
  «звірено» те, чого ніхто не звіряв;
* **довгий взірець ламається** від першої ж правки того речення.

Ціль між ними одна: **найкоротший префікс, який у всьому реєстрі
відмітний**. Саме його тут і шукають — нарощуючи по слову, доки
збігів не лишиться рівно один, і не далі.

Числа з взірця не викидаються: у багатьох одиницях число і є тим,
що робить її відмітною. Але взірець **обривається до числа**, якщо
відмітності досягнуто раніше, — а правлять здебільшого саме числа.

## Чого посадка НЕ робить

Вона садить **лише** те, що пережило третій шар: цитата знайшлася в
названому документі дослівно. Заявка без такої перевірки сюди не
потрапляє ніколи — інакше посадка стала б способом узаконити переказ.

Другий шар (чи витяг справді підтримує твердження) лишається за
людиною. Тому кожен посаджений файл має рядок `sposib`, який прямо
каже: клас `A` тут означає «документ отримано, витяг звірено машинно»,
а не «супровідник прочитав і згоден».

    tools/prochid_posadka.py <файл-вижилих> [--pysaty]
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

MIN_SLIV = 4
MAX_SLIV = 14


def ekranuy(s: str) -> str:
    """Літерали, але пробіли — гнучкі.

    Реєстр і книга переносять рядки по-різному, тож жорсткий пробіл у
    взірці — це та сама пастка, що вбила два докази DS18B20.
    """
    # Кожне слово екранується окремо, а склеюються вони вже гнучким
    # пробілом. Робити навпаки не можна: `re.escape` перетворює пробіл
    # на `\ `, і заміна по `\s+` з'їдає лише сам пробіл, лишаючи
    # осиротілу похилу. Перша редакція так і робила — усі 223 взірці
    # вийшли нечинні й не чіпали **нічого**.
    return r"\s+".join(re.escape(w) for w in s.split())


def vzirets_dlya(tekst: str, vsi: list[str]) -> str | None:
    """Найкоротший префікс, відмітний у всьому реєстрі."""
    slova = tekst.split()
    if len(slova) < MIN_SLIV:
        return None
    for k in range(MIN_SLIV, min(len(slova), MAX_SLIV) + 1):
        vz = ekranuy(" ".join(slova[:k]))
        # Відмітність перевіряється **пошуком**, а не `startswith`.
        # Взірець вживають саме пошуком, і префікс однієї одиниці
        # цілком може стояти посеред іншої: перша редакція міряла
        # префіксом і випустила п'ять взірців шириною до семи одиниць.
        # Міряти треба тим способом, яким воно потім працюватиме.
        r = re.compile(vz)
        if sum(1 for t in vsi if r.search(t)) == 1:
            return vz
    return None


# Писач мусить писати **обидва** імені, доки триває переїзд.
#
# Перелік «хто читає старі імена» рахував читачів — і саме тому крок 1
# виглядав завершеним. Але стиснення тримається не тим, що старі імена
# прибрано, а тим, що їх **нема кому написати**: після `--stysnuty`
# перша ж посадка повернула б їх назад, по одному наряду за раз, і
# `znimok --zvirty` був би зелений того дня й червоний за тиждень.
#
# Знайшов це М2. Рядок нижче прибирається **разом** із прогоном
# `--stysnuty`, не раніше й не пізніше.
def obydva(z: dict) -> dict:
    """Запис доказу з англійськими іменами поруч зі старими."""
    MAPA = {"nazva": "title", "zbih": "match", "klas": "status",
            "dzherelo": "source", "cytata": "quote", "sposib": "method",
            "notatka": "note", "shukaty": "look_for",
            "rozrakhunok": "calculation"}
    SLOVO = {"A": "verbatim", "B": "derived", "C": "named-unreachable",
             "D": "arithmetic", "E": "no-external-signal", "F": "unchecked",
             "G": "refuted", "K": "code-context", "L": "looked-not-found"}
    for st, nov in MAPA.items():
        if st in z and nov not in z:
            z[nov] = SLOVO.get(str(z[st]), z[st]) if st == "klas" else z[st]
    return z


def main() -> int:
    import factcheck
    import vybirka

    p = argparse.ArgumentParser()
    p.add_argument("vyzhyly", type=Path)
    p.add_argument("--pysaty", action="store_true")
    # Префікс імені файлу. **Обов'язково різний для різної хвилі.**
    # Без нього друга посадка мовчки переписує файли першої: так
    # 335 доказів проходу стали 324, і помітив це лише перелік.
    p.add_argument("--prefiks", default="prochid")
    a = p.parse_args()

    reyestr: dict[str, dict] = {}
    for klas in factcheck.USI_KLASY:
        for u in vybirka.odynyci(klas):
            u["klas"] = klas
            reyestr[u["id"]] = u
    vsi_teksty = [u["tekst"] for u in reyestr.values()]
    print(f"реєстр: одиниць {len(reyestr)}")

    zapysy = yaml.safe_load(a.vyzhyly.read_text(encoding="utf-8")) or []
    print(f"вижили третій шар: {len(zapysy)}")

    posadka: dict[str, list[dict]] = collections.defaultdict(list)
    nema_odynyci = shyrokyy = vzhe_A = 0
    for z in zapysy:
        oid = str(z.get("odynycya", "")).strip()
        u = reyestr.get(oid)
        if u is None:
            nema_odynyci += 1
            continue
        if u["klas"] in ("A", "B"):
            # Одиниця вже має первинний доказ. Другий нічого не додає,
            # зате створює дві правди про одне — і рівно стільки ж
            # місць, які розійдуться після наступної правки.
            vzhe_A += 1
            continue
        vz = vzirets_dlya(u["tekst"], vsi_teksty)
        if vz is None:
            shyrokyy += 1
            continue
        fayl = u["src"].split("/")[-1].split(":")[0].removesuffix(".md")
        posadka[fayl].append(obydva({
            "nazva": f"{oid}: {' '.join(u['tekst'].split()[:8])}",
            "zbih": vz,
            "klas": "A",
            "dzherelo": str(z["source"]).strip(),
            "cytata": str(z["quote"]).strip() + "\n",
            "sposib": (
                "Суцільний прохід 2026-08-27. Документ отримано в сесії, "
                "витяг звірено з ним підрядком машинно "
                "(`tools/prochid_zvid.py`). Клас `A` тут означає "
                "«документ отримано, цитата дослівна», а **не** "
                "«супровідник прочитав і згоден»: змістовий шар "
                "лишається окремою роботою."),
            "notatka": str(z.get("komentar", "")).strip() or "—",
        }))

    vsoho = sum(len(v) for v in posadka.values())
    print(f"придатних до посадки {vsoho} | вже мають A/B {vzhe_A} | "
          f"одиниці немає в реєстрі {nema_odynyci} | "
          f"відмітного префікса немає {shyrokyy}")

    if not a.pysaty:
        print("\n(суха проба; `--pysaty` щоб записати)")
        return 0

    kudy = ROOT / "factcheck" / "dokazy"
    for fayl, zapys in sorted(posadka.items()):
        shlyakh = kudy / f"{a.prefiks}-{fayl}.yaml"
        shapka = (
            f"# Посадка {a.prefiks} — {fayl}.\n"
            f"#\n"
            f"# Посаджено `tools/prochid_posadka.py`. Сюди потрапляє лише\n"
            f"# те, що пережило третій шар: цитата знайшлася в названому\n"
            f"# документі дослівно. Заявок без такої перевірки тут немає.\n"
            f"#\n"
            f"# Взірці виведено механічно — найкоротший префікс, відмітний\n"
            f"# у всьому реєстрі. Це компроміс між двома законами:\n"
            f"# широкий взірець бреше, довгий ламається.\n\n")
        shlyakh.write_text(
            shapka + yaml.safe_dump(zapys, allow_unicode=True,
                                    sort_keys=False, width=88),
            encoding="utf-8")
    print(f"записано файлів: {len(posadka)} → {kudy}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
