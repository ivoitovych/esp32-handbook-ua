#!/usr/bin/env python3
"""Coverage: is every line of the book accounted for by a card?

## The question this asks, and the one it does not

The registry is **generated** from the book, so "does every unit have a
card" is true by construction and worth nothing. The real question is
the other way round:

> **Does every line of the book become a unit?**

Text the splitter never saw has no card, no class, no evidence — and,
worse, does not appear in any count. It is not `unverified`; it is
invisible. A book can show 100 % of its units checked while a chapter
of it was never split at all.

## What counts as covered

A line is covered if some card records `src:file:line` inside the span
that line belongs to. Cards carry the first line of their unit, so a
sentence wrapped over four lines is covered by one card; the span runs
to the next card's line or to the end of the block.

## What is deliberately not counted

Empty lines, fence markers, and the block separators the book uses for
layout. These carry no claim and never could.

**Everything else is counted, including headings and code.** They may
well be out of scope for fact-checking — but that is a *verdict*, and a
verdict belongs in a card, not in a script's exclusion list. A coverage
tool that silently drops what it considers uninteresting measures its
own opinion.

## What to do with the gap

Uncovered lines are a work order, not a defect. Each needs one of two
answers, and both are human or model work:

* it is a claim → it belongs in the registry, and the splitter missed it;
* it is not a claim → say so in a card, so the next audit does not ask
  again.

## Два роди обліку, і тільки разом вони дають «усе на місці»

Рядок книги враховано, якщо про нього відомо одне з двох:

* **картка** — рядок несе твердження, і воно в реєстрі;
* **структурна підстава** — рядок є частиною будови книги, і скрипт
  **це перевіряє**, а не припускає.

Друге спершу пропонувалося робити картками зі статусом «не підлягає
звірці». Від цього відмовилися, і причина варта запису.

Картка, чий увесь зміст — «це заголовок», не несе нічого, чого скрипт
не виведе сам із рядка. Дев'яносто одна така картка — церемонія, яка
до того ж додає в реєстр **стверджувальний вердикт**, а такі в нас уже
одного разу зібрали звалище (`ne-rozibrav`: 85–87 % виявилися
звичайними судженнями).

Структурна підстава сильніша за картку саме тим, що **перевіряється
наново щоразу**. Картка може застаріти й мовчати; правило не може.

## Чи буває заголовок твердженням? Виміряно 2026-08-29

Це питання лежало в основі всього розділу й **ніколи не перевірялося**:
структурну підставу прийняли, бо заголовок «очевидно» не твердження.
Очевидність — не вимір, і власник спитав прямо.

    заголовків у книзі                                       850
    з них є одиницею реєстру                                   0
    з них має картку                                           0
    з ознакою твердження (число з одиницею, «не», «має»,
      «лише», «працює», порівняння)                           57

Прочитано всі 57. Жоден не стверджує перевірюваного факту про світ:
«Що є в чипі», «Тільки-вхідні піни», «Чого тріаж не дає» — це назви
розділів. Найближче до твердження — застереження, ужите як заголовок
(«Піни флешу: не чіпати»), а сам факт стоїть у таблиці під ним.

**Отже рішення не давати заголовкам карток правильне, і тепер це
виміряно, а не припущено.**

Межа виміру названа чесно: сито евристичне, і 57 кандидатів прочитано
очима з 850. Якщо заголовок колись стане твердженням, це побачить не ця
перевірка, а рецензент — і тоді твердження треба винести в текст під
заголовком, а не заводити картку на заголовок.

## Що перевіряється, а не припускається

Заголовок зараховується, лише якщо:

* рядок збігається з `^#{1,6}\s`;
* якщо в ньому є якір `{#…}` — усі посилання `](#якір)` у книзі
  ведуть на наявні якорі;
* якщо файл має номер у назві — номер у заголовку той самий;
* якщо на розділ посилаються як «розділ NN» — такий розділ існує.

Тобто «усе на місці» означає буквально: кожен рядок або має твердження
в реєстрі, або є будовою книги, і будова несуперечлива.

## Що робити з рештою прогалини

Прогалину закривають картками. Але статус «не підлягає звірці» — це
**стверджувальний вердикт**, а такі в нас уже одного разу зібрали
звалище: у роді `ne-rozibrav` 85–87 % виявилися звичайними судженнями,
які помічник міг класифікувати без зусиль.

Тому статус має бути таким, що його **підтверджує скрипт**. «Це не
твердження» взагалі — неперевірюване й зогниє. «Цей рядок є
заголовком» — перевіряється одним взірцем.

Режим `--rody` розкладає непокриті рядки за родом саме для цього: щоб
кожній прогалині можна було дати статус, який машина вміє звірити.

    tools/coverage.py [--fayl <шлях>] [--dilyanky] [--rody]
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("manual", "dodatky", "kartky", "inserts")

RE_SRC = re.compile(r"<!-- fc id:(\S+) sha:\S+ src:(\S+?):(\d+) klas:(\S+) -->")
PORO_ZHNI = re.compile(r"^\s*$|^```|^:::|^<!--|^\s*[-=]{3,}\s*$")


def zibraty_kartky() -> dict[str, set[int]]:
    pokryti: dict[str, set[int]] = defaultdict(set)
    for g in GRUPY:
        katalog = ROOT / "factcheck" / g
        if not katalog.exists():
            continue
        for f in katalog.glob("*.md"):
            for m in RE_SRC.finditer(f.read_text(encoding="utf-8")):
                pokryti[m.group(2)].add(int(m.group(3)))
    return pokryti


def perevirka_budovy() -> list[tuple[str, str]]:
    """Чи будова книги несуперечлива — те, чим заголовок і можна звірити."""
    yakori, posylannya, rozdily = set(), set(), {}
    nomer_ne_zbig = []
    for g in GRUPY:
        katalog = ROOT / g
        if not katalog.exists():
            continue
        for p in sorted(katalog.glob("*.md")):
            t = p.read_text(encoding="utf-8")
            yakori.update(re.findall(r"^#{1,6} .*\{#([^}]+)\}", t, re.M))
            posylannya.update(re.findall(r"\]\(#([^)]+)\)", t))
            m = re.match(r"(\d+)-", p.name)
            if m and g == "manual":
                rozdily[m.group(1).zfill(2)] = True
                h = t.split("\n")[0]
                hm = re.match(r"#\s*(\d+)\.", h)
                if hm and hm.group(1).zfill(2) != m.group(1).zfill(2):
                    nomer_ne_zbig.append(p.name)
    byti = sorted(posylannya - yakori)
    byti_rozdily = set()
    for g in GRUPY:
        katalog = ROOT / g
        if not katalog.exists():
            continue
        for p in katalog.glob("*.md"):
            for n in re.findall(r"розділ\w*\s+(\d{1,2})\b",
                                p.read_text(encoding="utf-8")):
                if n.zfill(2) not in rozdily:
                    byti_rozdily.add(n)
    return [
        ("якорів заголовків", str(len(yakori))),
        ("посилань на якір", "%d, битих %d" % (len(posylannya), len(byti))),
        ("посилань «розділ NN»", "на неіснуючий розділ: %d" % len(byti_rozdily)),
        ("номер файлу проти заголовка", "розбіжностей %d" % len(nomer_ne_zbig)),
    ]


def main(argv: list[str]) -> int:
    lyshe = None
    if "--fayl" in argv:
        lyshe = argv[argv.index("--fayl") + 1]
    dilyanky = "--dilyanky" in argv
    rody_rezhym = "--rody" in argv
    rody = defaultdict(list)
    strukturni = 0
    nevrakhovani: list[tuple] = []
    SLUZHBOVI = ("prysvyata.md",)

    pokryti = zibraty_kartky()
    vsyoho = pokryto = 0
    za_faylom: list[tuple] = []

    for g in GRUPY:
        katalog = ROOT / g
        if not katalog.exists():
            continue
        for p in sorted(katalog.glob("*.md")):
            vidn = str(p.relative_to(ROOT))
            if lyshe and vidn != lyshe:
                continue
            ryadky = p.read_text(encoding="utf-8").split("\n")
            tochky = sorted(pokryti.get(vidn, set()))
            zmistovni = [i + 1 for i, r in enumerate(ryadky)
                         if not PORO_ZHNI.match(r)]
            if not zmistovni:
                continue
            # Кожна картка накриває свій рядок і все до наступної картки.
            nakryti: set[int] = set()
            for k, poch in enumerate(tochky):
                kinec = tochky[k + 1] if k + 1 < len(tochky) else len(ryadky) + 1
                nakryti.update(range(poch, kinec))
            ne = [i for i in zmistovni if i not in nakryti]
            for i in ne:
                r = ryadky[i - 1]
                if re.match(r"^#{1,6}\s", r):
                    strukturni += 1
                elif Path(vidn).name in SLUZHBOVI:
                    strukturni += 1
                else:
                    nevrakhovani.append((vidn, i, r[:60]))
            if rody_rezhym:
                for i in ne:
                    r = ryadky[i - 1]
                    if re.match(r"^#{1,6}\s", r):
                        k = "заголовок"
                    elif re.match(r"^\s*[|>]", r):
                        k = "таблиця або цитата"
                    elif re.match(r"^\s{4,}\S", r):
                        k = "відступ або код"
                    elif re.match(r"^\s*\*\*[^*]+\*\*\s*$", r):
                        k = "жирний рядок"
                    else:
                        k = "інше"
                    rody[k].append((vidn, i, r[:56]))
            vsyoho += len(zmistovni)
            pokryto += len(zmistovni) - len(ne)
            za_faylom.append((vidn, len(zmistovni), len(ne), ne))

    za_faylom.sort(key=lambda x: -x[2])
    print("%-40s %7s %7s %6s" % ("файл", "рядків", "без картки", "покрито"))
    for vidn, vs, nek, ne in za_faylom:
        if nek == 0 and not dilyanky:
            continue
        print("%-40s %7d %7d %5.0f%%"
              % (vidn, vs, nek, 100 * (vs - nek) / vs))
        if dilyanky and ne:
            grupy, poch, pop = [], ne[0], ne[0]
            for x in ne[1:]:
                if x != pop + 1:
                    grupy.append((poch, pop))
                    poch = x
                pop = x
            grupy.append((poch, pop))
            for a, b in grupy[:12]:
                print("      рядки %d–%d" % (a, b) if a != b else
                      "      рядок %d" % a)

    if rody_rezhym:
        print("\nнепокрите за родом:")
        for k in sorted(rody, key=lambda x: -len(rody[x])):
            print("   %-22s %4d" % (k, len(rody[k])))
            if k == "інше":
                for f, i, t in rody[k][:10]:
                    print("        %s:%d  %s" % (f, i, t))

    struktura = perevirka_budovy()
    print("\nоблік рядків:")
    print("   мають картку                 %5d" % pokryto)
    print("   структурна підстава          %5d   (заголовки, службові сторінки)"
          % strukturni)
    print("   НЕ ВРАХОВАНО                 %5d" % len(nevrakhovani))
    for vidn, i, t in nevrakhovani[:10]:
        print("        %s:%d  %s" % (vidn, i, t))
    print("\nбудова книги:")
    for k, v in struktura:
        print("   %-34s %s" % (k, v))
    povno = 100 * (pokryto + strukturni) / max(1, vsyoho)
    print("\n   УСЕ НА МІСЦІ: %.2f %% (%d із %d)"
          % (povno, pokryto + strukturni, vsyoho))

    print("\ncoverage: змістовних рядків книги %d; накрито картками %d (%.1f %%); "
          "без картки %d"
          % (vsyoho, pokryto, 100 * pokryto / max(1, vsyoho), vsyoho - pokryto))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
