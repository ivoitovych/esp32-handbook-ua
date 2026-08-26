#!/usr/bin/env python3
"""Штурм класу `E`: зведення того, що помічники знайшли проти присуду.

## Навіщо

Клас `E` означає «зовнішнього джерела не існує **за побудовою**». Цей
присуд винесено майже чотири тисячі разів — і жодного разу не
перевірявся сам присуд.

За один вечір він упав двічі незалежно: М2 знайшов 31 надмірний `E`,
перевірка на їхньому ж тригері — ще 32. Отже найбільша частина реєстру
трималася на судженні, якого ніхто не випробовував.

Цей інструмент зводить те, що помічники повернули зі штурму.

## Три відповіді, і всі три цінні

| Вердикт | Означає |
|---|---|
| `znayshov` | джерело є, ось адреса й дослівна цитата |
| `ideya` | не знайшов, але можу назвати, **де воно було б** |
| `spravdi-e` | подивився, зовнішнього референта справді немає |

Третій — **не поразка**. Підтвердити, що `E` поставлено правильно, так
само цінно, як спростувати: це перша перевірка присуду. Без цього виходу
помічник під тиском «знайди щось» починає вигадувати джерело — це вже
двічі спіймано на обох супровідниках.

`ideya` перетворює «неперевірне» на «ще не перевірене». Це різні стани, і
другий набагато кращий: він має адресата.

## Чому зведення терпить зламані файли

Один файл із двадцяти одного не розібрався: незакритий рядок із двокрапкою
всередині. Якби зведення на цьому падало, робота решти двадцяти зникла б
разом із ним. Тому зламані файли **називаються поіменно й пропускаються**.

    tools/shturm.py            зібрати factcheck/SHTURM-E.md
    tools/shturm.py --korotko  лише числа
"""
from __future__ import annotations

import collections
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CIL = ROOT / "factcheck" / "SHTURM-E.md"

# Кандидати на перевірку третім шаром. Не реєстр і не докази: сюди
# лягають самі лише `znayshov`, переведені у форму запису доказу, щоб
# `tools/citaty.py` міг їх звірити **до** того, як їх побачить
# супровідник.
KANDYDATY = ROOT / "factcheck" / "shturm-kandydaty.yaml"

# Каталоги вивантажень помічників. Тимчасові за природою: самі файли в
# репозиторій не входять, входить це зведення.
DZHERELA = [
    Path("/tmp/claude-0/-home-user-esp32-handbook-ua"
         "/f0bbd6f0-ee1b-56af-b4a7-e7c66e76d34a/scratchpad/vyklad3"),
]

PIDPYSY = {
    "znayshov": "Джерело знайдено",
    "ideya": "Названо, де шукати",
    "spravdi-e": "Підтверджено як чесний E",
}


def zibraty() -> tuple[list[dict], list[tuple[str, str]]]:
    zap: list[dict] = []
    bidy: list[tuple[str, str]] = []
    for katalog in DZHERELA:
        if not katalog.exists():
            continue
        for f in sorted(katalog.glob("*.yaml")):
            try:
                recs = yaml.safe_load(f.read_text(encoding="utf-8")) or []
            except yaml.YAMLError as e:
                bidy.append((f.name, str(e).split("\n")[0]))
                continue
            for z in recs:
                if isinstance(z, dict):
                    z["_fayl"] = f.stem
                    zap.append(z)
    return zap, bidy


STAN_PIDPYS = {
    "ok": "**витримав**",
    "ne_znaydeno": "цитати немає",
    "nedosyazhne": "джерело недосяжне",
    "nichoho": "без цитати",
    "vygadane": "джерело вигадане",
    "zaglushka": "заглушка",
    "okom": "лише очима",
    "pomylka": "хибний запис",
    "nechytne": "нечитний формат",
}


def tretiy_shar() -> dict[str, str]:
    """Прогнати кандидатів через `tools/citaty.py` і повернути стан кожного.

    Викликається як бібліотека, а не через `subprocess`: розбирати чужий
    друк назад у дані — це другий формат тих самих відомостей, і він
    роз'їжджається з першим за тиждень.
    """
    sys.path.insert(0, str(ROOT / "tools"))
    try:
        import citaty
    except ImportError:
        return {}
    naslidky, _ = citaty.perevirka(True, [KANDYDATY])
    return {str(n.get("nazva")): str(n.get("stan")) for n in naslidky}


ZAHOLOVOK = """# Штурм класу `E`

**Генерується** `tools/shturm.py`. Правити вручну нема сенсу.

Клас `E` означає «зовнішнього джерела не існує за побудовою». Присуд
винесено майже чотири тисячі разів і **жодного разу не перевірявся**.
Тут — що повернули помічники, коли їх послали його штурмувати.

Це **не докази**. Жоден запис звідси не входить у реєстр, доки
супровідник не звірить його сам: `znayshov` треба перевірити по суті
(шар 2), `ideya` — відпрацювати.

Зокрема адреси в колонці «де шукати» **ніхто не відкривав**. Це здогад
помічника про те, який документ мав би це містити, і серед них уже
трапляються шляхи, яких не існує. Здогад — теж робота: він перетворює
«неперевірне» на «ще не перевірене», а це різні стани, і другий має
адресата. Але доказом він не стає.

## Що з цим зробив третій шар

Кандидатів `znayshov` пропущено через `tools/citaty.py` **до** того, як
їх побачив супровідник. Шість не витримали, і кожен по-своєму:

- три — джерело за адресою просто не існує (404), а в полі цитати
  стоїть власна проза помічника, не текст документа. Обидві вигадки
  зловлено без жодного судження про зміст;
- один — рядок ядра Linux, **перенабраний з великої літери**
  (`Static struct` замість `static struct`). Факт правильний; цитата —
  ні. Відрізнити перенабір від вигадки, не дивлячись у джерело, не
  можна, тому підрядок і не пробачає;
- два — переказ замість цитати.

Це і є довід на користь дешевої моделі. Вигадка не проходить не тому,
що її хтось розпізнав, а тому, що її **нема за адресою**.

"""


def main() -> int:
    zap, bidy = zibraty()
    c = collections.Counter(str(z.get("verdykt", "?")) for z in zap)

    if "--korotko" in sys.argv:
        print(f"shturm: записів {len(zap)}, зламаних файлів {len(bidy)}; "
              + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
        return 0

    # Клас у кандидатах **не** проставляється. Його присвоює
    # супровідник, і саме на цьому тримається правило «чуже слово не
    # потрапляє в реєстр неперевіреним». `citaty.py` вміє читати запис
    # без класу — це стан вивантаження помічника, а не брак.
    kand = [{"nazva": str(z.get("odynycya", "?")),
             "dzherelo": str(z.get("dzherelo", "")).strip(),
             "cytata": str(z.get("cytata", "")),
             "syla": str(z.get("syla", "?")),
             "zvidky": z.get("_fayl", "?")}
            for z in zap if str(z.get("verdykt")) == "znayshov"]
    KANDYDATY.write_text(
        "# Згенеровано `tools/shturm.py`. Не реєстр: кандидати на\n"
        "# перевірку третім шаром. `tools/citaty.py "
        f"{KANDYDATY.relative_to(ROOT)}`\n"
        + yaml.safe_dump(kand, allow_unicode=True, sort_keys=False),
        encoding="utf-8")

    # Ворота стоять **перед** звітом, а не після. Інакше в реєстрі
    # з'явився б рядок «джерело знайдено» там, де джерела немає, — а
    # саме цього ця книга й обіцяла не робити.
    stany = tretiy_shar()
    vystoyalo = sum(1 for k in kand if stany.get(k["nazva"]) == "ok")

    r = [ZAHOLOVOK.rstrip("\n"), ""]
    r.append(f"Записів: **{len(zap)}**. "
             + ", ".join(f"{PIDPYSY.get(k, k)} — **{v}**"
                         for k, v in sorted(c.items(), key=lambda x: -x[1]))
             + ".\n")
    if bidy:
        r.append("## Файли, що не розібралися\n")
        r.append("Пропущені, а не приховані: робота решти від цього не "
                 "зникає.\n")
        for imya, chomu in bidy:
            r.append(f"- `{imya}` — {chomu}")
        r.append("")

    for verdykt in ("znayshov", "ideya", "spravdi-e"):
        grupa = [z for z in zap if str(z.get("verdykt")) == verdykt]
        if not grupa:
            continue
        r.append(f"\n## {PIDPYSY[verdykt]} — {len(grupa)}\n")
        if verdykt == "znayshov":
            r.append(f"З них третій шар витримали **{vystoyalo}**. Решта "
                     "лишається тут із позначкою: спростування помічника "
                     "теж результат, і ховати його нема за чим.\n")
            r.append("| Одиниця | Третій шар | Сила | Джерело | Що каже |")
            r.append("|---|---|---|---|---|")
            for z in grupa:
                dz = str(z.get("dzherelo", "")).strip()
                korotko = dz.rsplit("/", 1)[-1] if dz else "—"
                r.append(f"| `{z.get('odynycya','?')}` "
                         f"| {STAN_PIDPYS.get(stany.get(str(z.get('odynycya'))), '?')} "
                         f"| {z.get('syla','?')} "
                         f"| [`{korotko}`]({dz}) "
                         f"| {str(z.get('komentar','')).strip()[:110]} |")
        elif verdykt == "ideya":
            r.append("| Одиниця | Де шукати |")
            r.append("|---|---|")
            for z in grupa:
                r.append(f"| `{z.get('odynycya','?')}` "
                         f"| {str(z.get('propozyciya','')).strip()[:150]} |")
        else:
            r.append("| Одиниця | Чому джерела немає |")
            r.append("|---|---|")
            for z in grupa:
                r.append(f"| `{z.get('odynycya','?')}` "
                         f"| {str(z.get('chomu','')).strip()[:150]} |")
        r.append("")

    CIL.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"shturm: записів {len(zap)}, зламаних {len(bidy)} "
          f"→ {CIL.relative_to(ROOT)}; кандидатів {len(kand)}, "
          f"вистояло третій шар {vystoyalo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
