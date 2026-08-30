#!/usr/bin/env python3
"""Наряд помічникам на цитати, яких немає в джерелі.

## Що це за робота і чому вона не та, яку зробив третій шар

Третій шар уже сказав: цитати за названою адресою немає. Причина
здебільшого відома й нецікава — **супровідник причепурив цитату**.
Скоротив `{IDF_TARGET_STRAP_BOOT_2_GPIO}` до `{STRAP_BOOT_2_GPIO}`,
зібрав рядок таблиці рукою, вирівняв відступи. М2 у цьому зізнався
першим, і мої власні записи виявилися такі самі.

Це брак **реєстру**. Виправляє його супровідник, і на друк це не
впливає.

Але з нього не випливає стан **книги**, а на друк впливає саме він.
Причесана цитата над правильним фактом — дрібниця. Причесана цитата, за
якою джерело каже щось інше, — помилка, яка поїде в наклад. Ці два
випадки третій шар не розрізняє **за побудовою**: він порівнює рядки, а
не смисли.

Тому окремий наряд і окреме питання: **чи правильне те, що написано в
книзі.**

## Чому питання ставиться саме так

Помічникові легко догодити супровідникові, підтвердивши все підряд.
Тому в наряді прямо сказано, що `sperechayetsya` — бажаний результат, і
що книгу ще можна виправити. І там же — обмеження, без якого перше
перетворюється на вигадування: ставити `sperechayetsya`, лише **бачачи**
інший текст, а не пам'ятаючи інакше.

Обидві половини потрібні разом. Сама перша дає вигадані знахідки, сама
друга — мовчазне «все гаразд».

## Чому зведення рахує нестачу, а не лише вердикти

Помічник звітує числами, і числа сходяться самі з собою: «сім
підтверджено, помилок нема». Але в наряді було десять. Три записи
просто не згадані — не спростовані, не відкладені, а **зниклі**, і в
звіті помічника цього не видно ніяк.

Тому зведення бере перелік із наряду, а не з вивантажень, і кожен
запис, на який ніхто не відповів, друкує окремим розділом. Нестача —
теж результат, і найнебезпечніший: вона виглядає як згода.

    tools/work_orders.py                    зібрати factcheck/data/reports/BRIEF-QUOTES.md
    tools/work_orders.py --krim <каталог>   лише ті, на які ще не відповіли
    tools/work_orders.py --zvit <каталог>   звести відповіді помічників
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(ROOT / "tools"))

import factcheck  # noqa: E402  — після sys.path
CIL = ROOT / "factcheck" / "data" / "reports" / "BRIEF-QUOTES.md"
NA_PAKET = 5

ZAHOLOVOK_RAMKA = """# Наряд: {skilky} цитат, яких немає в джерелі

**Генерується** `tools/work_orders.py`. Питання **не** про цитату.

Третій шар уже сказав, що цитати за адресою немає. Причина відома і
здебільшого та сама: супровідник **причепурив** цитату — скоротив
`{IDF_TARGET_STRAP_BOOT_2_GPIO}` до `{STRAP_BOOT_2_GPIO}`, зібрав рядок
таблиці рукою, переставив відступи. Це брак реєстру, і його виправляє
супровідник.

**Твоє питання інше й важливіше: чи правильне те, що написано в книзі.**

Цитата може бути причесана, а факт — правильний. Може бути й навпаки:
причесування іноді ховає те, що джерело каже щось інше. Книга йде в
друк, тож нас цікавить саме другий випадок.
"""

# Спільні правила беруться з `factcheck/TASK-SPEC.md`, а не
# переписуються тут. До появи спеки їх було сім копій, і
# збігалося в усіх сімох рівно одне правило з восьми.
ZAHOLOVOK_BLOKY = ['ORIENTATION', 'VERBATIM', 'HONEST-MISS', 'NETWORK', 'STUB', 'VERDICTS-VERDICT-TEST', 'NO-SELF-REFERENCE', 'FORMAT']


def zaholovok(**kw) -> str:
    """Наряд: рамка цієї партії плюс спільні блоки завдання.

    Підстановка **заміною**, а не `.format`: у рамці стоять
    справжні фігурні дужки ESP-IDF (`{IDF_TARGET_...}`), і
    `format` на них падає з KeyError.
    """
    import task_spec
    ramka = ZAHOLOVOK_RAMKA
    for k, v in kw.items():
        ramka = ramka.replace("{" + k + "}", str(v))
    return task_spec.sklasty(ZAHOLOVOK_BLOKY, zaholovok=ramka,
                             shablon=ZAHOLOVOK_RAMKA)



def zapysy() -> dict[tuple[str, str], dict]:
    rec: dict[tuple[str, str], dict] = {}
    for f in sorted((ROOT / "factcheck" / "data" / "evidence").glob("*.yaml")):
        try:
            for z in (yaml.safe_load(f.read_text(encoding="utf-8")) or []):
                if isinstance(z, dict):
                    rec[(f.stem, factcheck.nazva_zapysu(z))] = z
        except yaml.YAMLError:
            continue
    return rec


ZVIT = ROOT / "factcheck" / "data" / "reports" / "BOOK-VS-SOURCES.md"

PIDPYSY = {
    "pidtverdzheno": "Книга підтверджена",
    "sperechayetsya": "Джерело сперечається з книгою",
    "ne_vyrishyv": "Не вирішено",
}


RE_ZAPYS = re.compile(r"^\*\*`([\w-]+)`\*\* · (.+)$", re.M)


def z_naryadu() -> list[str]:
    """Назви записів **із виданого наряду**, а не з поточного стану.

    Різниця не теоретична. Наряд роздали на 50 записів; поки помічники
    працювали, злиття роботи М2 додало ще 19 розбіжних цитат. Якби
    зведення бралося з поточного переліку, 19 записів, яких помічники
    ніколи не бачили, лягли б у графу «без відповіді» — і виглядали б
    як недбалість помічників.

    Наряд — це домовленість. Питати з помічника можна рівно те, що в
    ньому стояло.
    """
    if not CIL.exists():
        return []
    return [m.group(2).strip() for m in RE_ZAPYS.finditer(
        CIL.read_text(encoding="utf-8"))]


def zvesty(katalog: Path) -> int:
    import helper_dumps

    zap, polagodzheni, zlamani = helper_dumps.chytaty(katalog)

    # Ключ — назва запису доказу. Помічники пишуть `zapys` і `nazva`;
    # звіряємо за назвою, бо саме вона стоїть у наряді.
    vidpovidi: dict[str, dict] = {}
    for z in zap:
        klyuch = str(z.get("title", "")).strip()
        if klyuch:
            vidpovidi[klyuch] = z

    ochikuvano = z_naryadu()
    znykli = [n for n in ochikuvano if n not in vidpovidi]

    c: dict[str, int] = {}
    for n in ochikuvano:
        v = str(vidpovidi.get(n, {}).get("verdykt", "—"))
        c[v] = c.get(v, 0) + 1

    sperechayutsya = [n for n in ochikuvano
                      if str(vidpovidi.get(n, {}).get("verdykt"))
                      == "sperechayetsya"]

    r = [f"""# Книга проти джерел: {len(ochikuvano)} розбіжних цитат

**Генерується** `tools/work_orders.py --zvit`. Наряд —
`factcheck/data/reports/BRIEF-QUOTES.md`.

Третій шар сказав, що цих цитат немає за названою адресою. Питання тут
інше: **чи правильне те, що написано в книзі.**

Причина розбіжностей відома й нецікава — супровідник причепурив цитату:
скоротив `{{IDF_TARGET_STRAP_BOOT_2_GPIO}}` до `{{STRAP_BOOT_2_GPIO}}`,
зібрав рядок таблиці рукою. Це брак реєстру, не книги. Небезпечний лише
той випадок, коли за причесаною цитатою джерело каже **інше**.

## Результат

Записів у наряді: **{len(ochikuvano)}**. Відповідей: **{len(ochikuvano) - len(znykli)}**.

| Вердикт | Скільки |
|---|---|"""]
    for k in ("pidtverdzheno", "sperechayetsya", "ne_vyrishyv"):
        r.append(f"| {PIDPYSY[k]} | {c.get(k, 0)} |")
    if znykli:
        r.append(f"| **Без відповіді** | {len(znykli)} |")
    r.append("")

    if sperechayutsya:
        r.append("\n## Джерело сперечається з книгою\n")
        r.append("**Це знахідки.** Кожну звіряє супровідник особисто "
                 "перед тим, як щось правити в книзі.\n")
        for n in sperechayutsya:
            z = vidpovidi[n]
            r.append(f"### {n}\n")
            r.append(f"- джерело: {str(z.get('dzherelo', '?')).strip()}")
            r.append(f"- каже: {str(z.get('komentar', '')).strip()}\n")
            r.append("```")
            r.append(str(z.get("quote", "")).strip()[:600])
            r.append("```\n")
    else:
        r.append("\n## Спростувань немає\n")
        r.append("Жодне джерело не заперечило книзі. Це **не** означає, "
                 "що книга правильна — означає, що на цих п'ятдесяти "
                 "місцях причесана цитата стояла над правильним фактом. "
                 "Брак тут у реєстрі, і виправляти його — реєстрові.\n")

    if znykli:
        r.append("\n## Без відповіді\n")
        r.append("Записи з наряду, яких немає в жодному вивантаженні. "
                 "**Не підтверджені й не спростовані — просто зниклі.** "
                 "Помічник звітує власними числами, і в них нестача "
                 "невидима: сім із десяти виглядають як сім із семи.\n")
        for n in znykli:
            r.append(f"- {n}")
        r.append("")

    if polagodzheni:
        r.append("\nПолагоджено механічно (значення взято в лапки): "
                 + ", ".join(f"`{b}`" for b in polagodzheni) + ".\n")
    if zlamani:
        r.append("\nНе розібралися й пропущені: "
                 + ", ".join(f"`{b}`" for b in zlamani) + ".\n")

    r.append("\n## Усі відповіді\n")
    r.append("| Запис | Вердикт | Що каже джерело |")
    r.append("|---|---|---|")
    for n in ochikuvano:
        z = vidpovidi.get(n)
        if z is None:
            r.append(f"| {n[:70]} | **без відповіді** | — |")
            continue
        r.append(f"| {n[:70]} | {z.get('verdykt', '?')} "
                 f"| {str(z.get('komentar', '')).strip()[:110]} |")

    ZVIT.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"work_orders: очікувано {len(ochikuvano)}, відповідей "
          f"{len(ochikuvano) - len(znykli)}, спростувань "
          f"{len(sperechayutsya)}, без відповіді {len(znykli)} "
          f"→ {ZVIT.relative_to(ROOT)}")
    return 0


def main() -> int:
    import layer3

    naslidky, _ = layer3.perevirka(False)
    bidy = [n for n in naslidky if n.get("stan") == "ne_znaydeno"]

    vidpovidzheni: set[str] = set()
    if "--krim" in sys.argv:
        import helper_dumps
        katalog = Path(sys.argv[sys.argv.index("--krim") + 1])
        zap, _, _ = helper_dumps.chytaty(katalog)
        vidpovidzheni = {str(z.get("title", "")).strip() for z in zap}
        bidy = [n for n in bidy
                if str(n.get("nazva", "")).strip() not in vidpovidzheni]

    if "--zvit" in sys.argv:
        i = sys.argv.index("--zvit")
        if i + 1 >= len(sys.argv):
            print("naryad: --zvit потребує каталогу вивантажень")
            return 2
        return zvesty(Path(sys.argv[i + 1]))

    rec = zapysy()

    # `.replace`, а не `.format`: у тексті наряду стоять справжні
    # фігурні дужки ESP-IDF (`{IDF_TARGET_...}`), і `format` на них
    # падає з KeyError.
    r = [zaholovok(skilky=len(bidy)).rstrip("\n")]
    for i, n in enumerate(bidy):
        if i % NA_PAKET == 0:
            r.append(f"\n## Пакет {i // NA_PAKET + 1}\n")
        z = rec.get((n["fayl"], n["nazva"]), {})
        # `n` — звіт помічника (своя схема, не переїжджає), `z` — запис
        # доказу (переїжджає). Однакові слова, різні структури: тому
        # `n['nazva']` лишається, а `z` читається через `factcheck.pole`.
        dzh = str(factcheck.pole(z, "source", "dzherelo", "?")).strip()
        vz = str(factcheck.pole(z, "match", "zbih", "?"))[:200]
        r.append(f"**`{n['fayl']}`** · {n['nazva']}\n")
        r.append(f"- джерело: {dzh}")
        r.append(f"- у книзі шукати за взірцем: `{vz}`")
        r.append(f"- третій шар: {str(n.get('detali', ''))[:150]}\n")

    CIL.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"work_orders: записів {len(bidy)}, "
          f"пакетів {(len(bidy) + NA_PAKET - 1) // NA_PAKET} "
          f"→ {CIL.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
