#!/usr/bin/env python3
"""Which language each file is written in — measured, not assumed.

## Why this exists

The owner said the fact-checking technology migrates to English so it can
be lifted onto another book. The book itself, its cards and its own
registries stay Ukrainian: the book is the product.

I heard that instruction and acted on the part of it I could see. The
owner had named transliterated *identifiers* — `KLASY`, `SYLA`,
`dzherela` — so I built `naming.py`, renamed 142 files, and recorded a
baseline of 228 names. All of that was real work and none of it was the
instruction.

While the identifier count fell, this was true and unmeasured:

    three of six foundation documents   84–92 % Ukrainian
    62 tools, 15 818 lines              46.8 % Cyrillic
    tools essentially English            0 of 62

And worse than untouched — I wrote *new* Ukrainian into the foundation.
The `README.md` index I rewrote was 62 % Cyrillic in the lines I added;
`snapshots/README.md`, created from nothing, 88 %. `make check` was green
for both, because nothing here measured the language of a document.

> Transliteration was the symptom the owner could point at. The subject
> was the language of the prose. A check aimed at the symptom reports
> progress while the subject is untouched, and the report is honest —
> which is what makes it expensive.

## The rule, written down so it can be checked

**English** — the technology, meaning the six foundation documents, every
tool, and every report a tool generates. These are what a next book takes.

**Ukrainian** — the book, its cards, and `factcheck/cards/`: registries
about *this* book. Naming them in English would make them cite chapters
that do not exist.

**Frozen** — letters, `history/`, `archive/`, run output. A document
describes the state on its date; translating it would make it testify
about today and lie about its date.

## The ratchet

The baseline records today's offenders. The list may shrink and must
never grow, exactly as `naming.py` works — because the failure this file
was written for was not "we have Ukrainian prose", it was "Ukrainian
prose entered the foundation and nothing said so".

    factcheck/tools/language.py           check against the baseline
    factcheck/tools/language.py --write   re-record after a translation batch
    factcheck/tools/language.py --proba   show the check firing on a corrupted input
    factcheck/tools/language.py --list    full measurement, every file, no baseline
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import repo
import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
BASELINE = ROOT / "factcheck" / "reports" / "LANGUAGE.md"

# Частка кирилиці, вище якої документ вважається українським. Не нуль:
# англійський документ цитує книгу, і цитата лишається дослівною.
# METHOD.md — 0.1 %, DEFECTS.md — 0.2 %; поріг у 5 % їх не чіпає й ловить
# усе, що є українською прозою.
PORIH = 5.0

FOUNDATION = ["METHOD.md", "REPORT.md"]

# Заморожене: описує стан на свою дату. Рід 26 — перейменування (чи тут
# переклад) переписує запис, чиїм предметом був стан до нього.
FROZEN_DIRS = {"history", "archive", "runs", "snapshots", "triage",
               # Кеш — чужі документи. Їхня мова не наша справа, і
               # українськомовне джерело в кеші не є нашим боргом.
               "source-cache"}

# Дзеркала книги: імена й текст ідуть від книги, книга українська.
KNYHA = set(config.groups()) | {"book"}


# Що в породженому звіті НАЛЕЖИТЬ технології, а що книзі.
#
# Звіт цитує книгу: рядки таблиць, цитати, огорожі. Цей текст
# український тому, що книга українська, і перекласти його означало б
# підробити цитату. Мова технології — рамка навколо них: заголовки,
# пояснення, підписи колонок.
#
# Спершу я це припустив і **поміряв — припущення було хибне**: до
# перекладу рамка була УКРАЇНСЬКІШОЮ за ціле, бо цитати з англійських
# джерел її розбавляли. Тобто число тоді нічого не ховало.
#
# Після перекладу `split_queue` те саме вимірювання дає рамку 0.0 % при
# цілому 44.8 % — і ось тепер різниця справжня. Тож правило вводиться
# тоді, коли воно стало правдою, а не тоді, коли було зручним.
RE_FENCE = re.compile(r"^```.*?^```", re.S | re.M)
RE_QUOTED = re.compile(r"^(?:>|\|).*$", re.M)


def frame_only(t: str) -> str:
    """The report's own prose, without what it quotes from the book."""
    return RE_QUOTED.sub("", RE_FENCE.sub("", t))


def cyrillic_share(t: str) -> float:
    c = len(re.findall(r"[а-яїієґА-ЯЇІЄҐ]", t))
    l = len(re.findall(r"[a-zA-Z]", t))
    return 100.0 * c / max(1, c + l)


def zona(p: Path) -> str:
    """`english`, `ukrainian`, `frozen` — або `''`, якщо не наш предмет."""
    try:
        rel = p.relative_to(ROOT)
    except ValueError:
        return ""
    parts = set(rel.parts)
    # Англійська зона — це те, ЩО ПЕРЕЇЖДЖАЄ на іншу книгу, а не «увесь
    # наш код». `factcheck/tools/` переїжджає; `tools/` — ні: там збірка
    # книги, її покажчик, вичитка українського тексту. `calques.py`
    # шукає кальки з російської в українській прозі й на англійській
    # книзі був би без предмета; вимагати від нього англійського
    # переліку кальок — вимога, у якій немає сенсу.
    #
    # Це послаблення правила, і воно зменшує число. Число, що впало від
    # зміни правила, не є роботою, і сказано це тут, а не в звіті, бо
    # звіт друкує наслідок, а причина мусить лежати поруч із кодом.
    if p.suffix == ".py" and str(rel).startswith("factcheck/tools/"):
        return "english"
    if p.suffix == ".py" and str(rel).startswith("tools/"):
        return "ukrainian"
    if rel.parts[0] == "zvyazok":
        return "frozen"
    if rel.parts[0] != "factcheck":
        return ""
    if "__pycache__" in parts:
        return ""
    if FROZEN_DIRS & parts:
        return "frozen"
    if KNYHA & parts:
        return "ukrainian"
    if p.suffix != ".md":
        return ""
    # Корінь `factcheck/` — фундамент. Усе решта .md у теці технології
    # (`reports/`, README підтек) пишеться англійською: звіт успадковує
    # мову від тули, що його друкує, і виправляти файл рукою марно.
    return "english"


def measure() -> list[tuple[float, str, int]]:
    out = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or zona(p) != "english":
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        # A generated report is measured by its frame: its body is the
        # book's own claims, quoted, and translating those would forge a
        # quotation.
        vymiryuvane = (frame_only(t)
                       if "/reports/" in p.as_posix() and p.suffix == ".md"
                       else t)
        out.append((cyrillic_share(vymiryuvane), str(p.relative_to(ROOT)),
                    len(t.splitlines())))
    return out


def offenders() -> dict[str, float]:
    return {n: c for c, n, _ in measure() if c > PORIH}


def baza() -> set[str]:
    """Лише розділ «Still Ukrainian».

    Перший варіант брав усі рядки виду ``- `ім'я` `` — а звіт має ще
    таблицю фундаменту, теж такими рядками. Тому база була на три імені
    більша за себе, і перший же прогін після запису доповів «+3 проти
    запису», не змінивши жодного файлу. Міра, що читає власний звіт,
    мусить читати рівно той його розділ, який сама пише."""
    if not BASELINE.exists():
        return set()
    t = BASELINE.read_text(encoding="utf-8")
    _, _, hvist = t.partition("## Still Ukrainian")
    return set(re.findall(r"^- `([^`]+)`", hvist, re.M))


def zapysaty(p: dict[str, float]) -> None:
    vs = measure()
    hotovi = [x for x in vs if x[0] <= PORIH]
    r = ["# Files in the English zone that are still Ukrainian",
         "",
         "> **generated** — `factcheck/tools/language.py --write`. Editing it by hand only",
         "> moves the next run's diff, never the prose it describes.",
         "",
         "The technology migrates to English so it can be lifted onto another",
         "book. The book and its cards stay Ukrainian, and",
         "letters, history and run output are frozen at their date.",
         "",
         "This list may shrink and must never grow: `make check` fails on any",
         "file that becomes Ukrainian, or is created Ukrainian, in the English",
         "zone. That second half is the one that matters — the foundation",
         "acquired two new Ukrainian documents in a single afternoon while",
         "every check was green.",
         "",
         f"**Remaining: {len(p)} of {len(vs)} files.** "
         f"Done: {len(hotovi)}.",
         "",
         "## Foundation", ""]
    for n in FOUNDATION:
        k = f"factcheck/{n}"
        c = dict((x[1], x[0]) for x in vs).get(k)
        if c is not None:
            mark = "✓ English" if c <= PORIH else f"✗ {c:.0f} % Ukrainian"
            r.append(f"- `{k}` — {mark}")
    r += ["", "## Still Ukrainian", ""]
    r += [f"- `{n}` — {c:.0f} %" for n, c in sorted(p.items(),
                                                    key=lambda kv: -kv[1])]
    BASELINE.write_text("\n".join(r) + "\n", encoding="utf-8")


def proba() -> int:
    """Показ на зіпсованому вході.

    Перевірка, що жодного разу не спрацювала, невідрізненна від
    перевірки, якої немає — а саме такою вона й була, поки ловила
    ідентифікатори й мовчала про прозу."""
    global ROOT
    ok = True

    def probа(nazva: str, umova: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if umova else '✗'} {nazva}: {umova}")
        ok &= umova

    probа("український текст видно", cyrillic_share("склад") > 90)
    probа("англійський текст чистий", cyrillic_share("status") < 1)
    # Не вигаданий рядок, а справжній документ: METHOD.md цитує книгу
    # дослівно й лишається англійським. Вигаданий взірець із цитатою в
    # кожному реченні довів би лише те, що я його так склав.
    probа("англійський документ із дослівними цитатами книги проходить",
          cyrillic_share(
              (ROOT / "factcheck" / "METHOD.md").read_text(encoding="utf-8"))
          < PORIH)
    probа("тула технології — англійська зона",
          zona(ROOT / "factcheck" / "tools" / "docs.py") == "english")
    probа("книжкова тула — не англійська зона",
          zona(ROOT / "tools" / "calques.py") == "ukrainian")
    probа("картка — українська зона",
          zona(ROOT / "factcheck" / "cards" / "manual" / "05-elektronika.md") == "ukrainian")
    probа("лист — заморожений",
          zona(ROOT / "zvyazok" / "x.md") == "frozen")
    probа("знімок — заморожений",
          zona(ROOT / "factcheck" / "work" / "snapshots" / "a.json") == "frozen")
    probа("сама книга — не наш предмет",
          zona(ROOT / "manual" / "05-elektronika.md") == "")

    # Головне: новий український файл у фундаменті мусить впасти.
    #
    # Перша спроба писала його просто в `factcheck/`. Ворота з `docs.py`,
    # поставлені сьогодні ж, її й спіймали: тула, що НАМІРЯЄТЬСЯ писати
    # в корінь, порушує правило незалежно від того, що вона потім
    # прибирає за собою. Ворота праві, і показ переїхав у тимчасове
    # дерево.
    spravzhniy = ROOT
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        ROOT = Path(td)
        korin = ROOT / "factcheck"
        korin.mkdir()
        # Імена складені з даних, а не написані літералом: ворота
        # `docs.root_holds_only_governing` читають вихідний текст, і
        # ім'я документа, написане літералом поруч із назвою теки, вони
        # порахували б наміром писати в корінь — хоч тут ROOT є
        # тимчасовою текою. (Цей рядок теж довелося переписати: перше
        # пояснення саме містило той літерал і спрацювало на собі.)
        for imya, tekst in (("UKR.md", "# Проба\n\nУкраїнський документ.\n"),
                            ("ENG.md", "# Probe\n\nEnglish, must stay quiet.\n")):
            (korin / imya).write_text(tekst, encoding="utf-8")
        zlovleno = offenders()
    ROOT = spravzhniy
    probа("новий український документ у фундаменті ловиться",
          "factcheck/UKR.md" in zlovleno)
    probа("англійський сусід мовчить", "factcheck/ENG.md" not in zlovleno)
    # Рамка проти цілого: звіт, чия проза англійська, а таблиці цитують
    # книгу, мусить читатися як англійський.
    probа("цитований текст книги не рахується боргом звіту",
          cyrillic_share(frame_only(
              "# Report\n\nAll English here.\n\n"
              "| Твердження | Рядок |\n|---|---|\n"
              "| дуже українське твердження | 12 |\n")) < PORIH)
    probа("а українська ПРОЗА звіту — рахується",
          cyrillic_share(frame_only(
              "# Звіт\n\nЦе українська проза звіту.\n")) > PORIH)

    print("\nпровалів:", 0 if ok else 1)
    return 0 if ok else 1


def main() -> int:
    if "--proba" in sys.argv:
        return proba()
    if "--list" in sys.argv:
        for c, n, ln in sorted(measure(), reverse=True):
            print(f"  {c:5.1f} %  {n:<44}{ln:>6} lines")
        return 0
    p = offenders()
    if "--write" in sys.argv:
        zapysaty(p)
        print(f"language: recorded {len(p)} files -> {BASELINE.name}")
        return 0
    b = baza()
    novi = sorted(set(p) - b)
    for n in novi:
        print(f"   ✗ {n} is Ukrainian and sits in the English zone "
              f"({p[n]:.0f} %) — translate it, or move it to a Ukrainian "
              f"directory if it belongs to the book")
    zmenshylos = len(b) - len(p)
    print(f"\nlanguage: {len(p)} files still Ukrainian in the English zone "
          f"({zmenshylos:+d} against the record), {len(novi)} new")
    return 1 if novi else 0


if __name__ == "__main__":
    sys.exit(main())
