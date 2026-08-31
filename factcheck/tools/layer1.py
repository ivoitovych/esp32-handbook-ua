#!/usr/bin/env python3
"""Layer 1: does the card faithfully represent the book?

About CARDS — what a reviewer actually sees. Compare `layer1_units.py`,
which asks a different question: does a registry unit come from the
book? Presentation and provenance break apart, and this file found 58
broken contexts the other one cannot see in principle.

The registry is generated from the book, so equality holds by
construction — until something between the two drifts. This script is
the check that says so out loud, in seconds, without a human and
without a language model.

## What it verifies, per card

**The claim.** The `Твердження, коротко` block must appear in the book
at the recorded location. For a prose unit that is the sentence itself.
For a table cell the registry renders `Subject · Column → Value`, which
is **not** a quotation — so the cell's parts are checked separately
against the row.

**The context.** The `Контекст` block must appear in the book too, and
must **contain the claim**. A context that does not contain its own
claim is worse than no context: it tells the reviewer they have the
surroundings when they have someone else's.

**The location.** `src:file:line` must still point at the claim. A
drifting line number is not an error of the text — it is the sign that
the registry was rendered before the book was last edited.

## What "matches" means

The book carries markup, line breaks inside sentences, typographic
dashes and non-breaking spaces. A comparison that demands byte equality
would report thousands of false defects, and a check that cries wolf
gets switched off.

So the comparison normalises **presentation** and keeps **content**:
whitespace collapses, hyphenated line breaks join, dash and quote
variants fold together, `**bold**` markers drop. Words, numbers and
case stay as they are.

## Why the three counts are reported separately

    text absent from the book        a real defect
    text present, line has moved     the render is stale
    context does not hold its claim  the card is broken as a card

Merged into one number they would be indistinguishable, and the first
kind — the only one that matters — would drown in the second. The first
run of this check reported 1317 problems; 1311 were stale line numbers
and 6 were real.

**The second bucket held two worlds of its own, and its label named the
wrong cause.** The window around the recorded line was a constant eight
lines, so any unit longer than eight lines could not fit in it and was
counted as a moved line — while its line number was exactly right.
Measured on the 60 prose cards in that bucket: **52 were this**, and
regenerating the cards could never have cleared them. `T-11-064` is a
sixteen-line project-tree block recorded at line 154, and the book has
it at line 154.

The window is now sized to the unit (`vikno_dlya`): 111 → 51. This is
kind 25 in the catalogue — a correct count of a bucket that holds two
different situations — found in this file within an hour of the kind
being written down.

    factcheck/tools/layer1.py [--vsi] [--tykho] [--detali]

`--detali` друкує кожну зламану картку з її родом і файлом — щоб
половину, яка належить генератору, можна було забрати без вгадування.
"""
from __future__ import annotations

import re
import pathlib
import sys
from collections import defaultdict
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
# `GRUPY` була вісьмома копіями того самого факту — теками цієї
# книги. Копії збігалися, і саме тому були небезпечні: набір копій
# не бреше, доки факт не зміниться, а тоді бреше всіма одразу.
# Тепер це дані: `factcheck/book.yaml`.
GRUPY = config.groups()

# Огорожа блоку — ЗМІННОЇ ДОВЖИНИ. Генератор бере довшу за будь-який
# ряд лапок усередині вмісту, бо контекст картки на рядок коду сам є
# блоком коду. Взірець, що чекав рівно трьох лапок, не розбирав 684
# картки — і показував по них нуль замість правди.
#
# Знайшов М1: «нуль був тому, що ці картки взагалі не розбиралися».
# Це третій випадок того самого роду в моїх же інструментах: лічильник
# показує нуль, бо нічого не рахує.
#
# Між «Твердження» і «Контекст» може стояти ще блок «Дослівно з
# книги» — він є в комірок, і саме він, а не рендер `X · Y → Z`, є
# цитатою книги. Перший взірець його не передбачав і рахував 2069
# карток такими, що не мають контексту; контекст був у всіх.
#
# Огорожа блоку — **три зворотні лапки або більше**. Генератор бере
# довшу, коли сам контекст містить огорожу (`factcheck.ohorozha`): у
# картки на рядок коду контекст — це блок коду, і трьома лапками його
# не обгородиш. Взірець із жорсткими трьома лапками рахував такі
# картки безконтекстними — 684 з 8331, і **всі вони контекст мали**.
#
# > Рід із каталогу: взірець, що читає чужий формат, мусить знати той
# > формат цілком. Тут читач і письменник розійшлися на одному знаку.
RE_KARTKA = re.compile(
    r"<!-- fc id:(?P<id>\S+) sha:(?P<sha>\S+) src:(?P<src>\S+?):(?P<ln>\d+)"
    r" status:(?P<status>\S+) -->\n"
    r"### \S+ · (?P<vyd>\S+) · [^\n]*\n\n"
    r"\*\*[^*\n]+\*\*\n\n(?P<tverd>(?:> [^\n]*\n)+)"
    r"(?:\n\*\*Дослівно з книги\*\*\n\n(?P<og1>`{3,})\n(?P<doslivno>.*?)\n(?P=og1)\n)?"
    r"(?:\n\*\*Контекст\*\*\n\n(?P<og2>`{3,})\n(?P<kontekst>.*?)\n(?P=og2)\n)?",
    re.S)

VIKNO = 8      # мінімум рядків книги навколо записаного номера
VIKNO_MEZHA = 240   # стеля, щоб вікно не виродилося у весь файл


def vikno_dlya(ryadky: list[str], ln: int, tverd: str) -> str:
    """Вікно книги, **розміряне під одиницю**, а не під сталу.

    Стале вікно на вісім рядків мовчки перетворювало довгу одиницю на
    «зсув номера». Виміряно на 60 прозових картках: **52** з них мали
    номер рядка **точно правильний**, а твердження просто не вміщалося
    у вісім рядків — `T-11-064` це блок дерева проєкту на шістнадцять
    рядків, записаний під рядком 154, і книга має його рівно там.

    Тобто третє відро звіту («текст на місці, номер зсунувся ← рендер
    застарів») складалося з двох різних дійсностей: восьми справжніх
    зсувів на 1–2 рядки й п'ятдесяти двох одиниць, довших за вікно.
    Підпис відра називав причину, і для 52 з 60 вона була хибна:
    перегенерація карток не могла зарадити нічому, бо зсуву не було.

    > Рід 25 у `DEFECTS.md`, знайдений у власному вимірі за годину
    > після того, як його записали.

    Вікно тепер росте, доки не вмістить твердження за довжиною, з
    невеликим запасом і зі стелею.
    """
    i = max(0, ln - 1 - 1)
    treba = len(tverd)
    kin = min(len(ryadky), i + VIKNO)
    while kin < len(ryadky) and kin - i < VIKNO_MEZHA:
        if len(normal(" ".join(ryadky[i:kin]))) >= treba + 40:
            break
        kin += 1
    return normal(" ".join(ryadky[i:kin]))


def normal(s: str) -> str:
    """Знімає подання, лишає зміст."""
    s = re.sub(r"[’‘`´\"“”«»„]", "", s)
    s = re.sub(r"[–—−]", "-", s)
    s = s.replace(" ", " ").replace("‑", "-")
    # Склеювати лише СПРАВЖНІЙ перенос слова: дефіс упритул між
    # літерами. Тире з пробілами в кінці рядка — розділовий знак, і
    # знищувати його не можна. Перше правило («-\s*\n\s*» → «»)
    # з'їдало тире, і 127 карток виглядали так, ніби контекст не
    # містить власного твердження.
    s = re.sub(r"(?<=\w)-\n\s*(?=\w)", "", s)
    s = re.sub(r"\n", " ", s)
    s = re.sub(r"\*\*|\*|__", "", s)     # розмітка жирного й курсиву
    return re.sub(r"\s+", " ", s).strip()


def chastyny_komirky(t: str) -> list[str]:
    """Комірка рендериться як `X · Колонка → Значення`; це не цитата."""
    return [normal(x) for x in re.split(r"·|→", t) if len(normal(x)) > 1]


def main(argv: list[str]) -> int:
    vsi = "--vsi" in argv
    tykho = "--tykho" in argv
    detali = "--detali" in argv
    kontekst_povno: list[tuple] = []

    knyha: dict[str, list[str]] = {}
    cile: dict[str, str] = {}
    nemaye: list[tuple] = []
    zsuv: list[str] = []
    bez_kontekstu: list[str] = []
    kontekst_bez_tverdzhennya: list[tuple] = []
    n = proza = komirka = 0

    for g in GRUPY:
        katalog = config.cards_root() / g
        if not katalog.exists():
            continue
        for f in sorted(katalog.glob("*.md")):
            for m in RE_KARTKA.finditer(f.read_text(encoding="utf-8")):
                n += 1
                src, ln, vyd = m["src"], int(m["ln"]), m["vyd"]
                ident = m["id"]
                p = ROOT / src
                if src not in knyha:
                    knyha[src] = (p.read_text(encoding="utf-8").split("\n")
                                  if p.exists() else [])
                    cile[src] = normal(" ".join(knyha[src]))
                ryadky = knyha[src]
                if not ryadky:
                    nemaye.append((ident, "ФАЙЛУ НЕМАЄ", src))
                    continue

                tverd = normal("\n".join(
                    x[2:] for x in m["tverd"].strip().split("\n")))
                i = ln - 1
                # Вікно розміряне під **довшу** з двох речей: самого
                # твердження і дослівного блоку комірки.
                vikno = vikno_dlya(
                    ryadky, ln,
                    max(tverd, normal(m["doslivno"] or ""), key=len))

                if vyd == "komirka":
                    komirka += 1
                    # Для комірки цитатою книги є блок «Дослівно з
                    # книги»; рендер `X · Y → Z` цитатою не є.
                    if m["doslivno"]:
                        d = normal(m["doslivno"])
                        if d in vikno:
                            chast = []
                        elif d in cile[src]:
                            zsuv.append(ident)
                            chast = []
                        else:
                            nemaye.append((ident, "РЯДКА ТАБЛИЦІ НЕМАЄ В КНИЗІ",
                                           d[:64]))
                            chast = []
                    else:
                        chast = chastyny_komirky(tverd)
                    vtrach = [c for c in chast if c not in vikno]
                    if vtrach:
                        if all(c in cile[src] for c in vtrach):
                            zsuv.append(ident)
                        else:
                            nemaye.append((ident, "КОМІРКА: значень немає в книзі",
                                           "; ".join(c for c in vtrach
                                                     if c not in cile[src])[:64]))
                else:
                    proza += 1
                    if tverd in vikno:
                        pass
                    elif tverd in cile[src]:
                        zsuv.append(ident)
                    else:
                        nemaye.append((ident, "ТВЕРДЖЕННЯ НЕМАЄ В КНИЗІ",
                                       tverd[:64]))

                kont = m["kontekst"]
                if kont is None:
                    bez_kontekstu.append(ident)
                    continue
                kn = normal(kont)
                if vyd != "komirka" and tverd and tverd not in kn:
                    kontekst_bez_tverdzhennya.append((ident, tverd[:56]))
                    kontekst_povno.append((ident, tverd, vyd, src))

    granyca = None if vsi else 20
    for ident, rid, det in nemaye[:granyca]:
        print("   ✗ %-12s %-32s %s" % (ident, rid, det))
    if not vsi and len(nemaye) > 20:
        print("   ... ще %d" % (len(nemaye) - 20))
    if detali:
        print("\nкартки, чий контекст не містить власного твердження:")
        for ident, t, vyd, src in kontekst_povno:
            print("   %-12s %-14s %-30s %s" % (ident, vyd, src, t[:44]))
        rody_zlam = defaultdict(int)
        for _, _, vyd, _ in kontekst_povno:
            rody_zlam[vyd] += 1
        print("\n   за родом одиниці: %s" % dict(rody_zlam))
    else:
        for ident, t in kontekst_bez_tverdzhennya[:granyca]:
            print("   ✗ %-12s %-32s %s"
                  % (ident, "КОНТЕКСТ НЕ МІСТИТЬ ТВЕРДЖЕННЯ", t))

    if not tykho or nemaye or kontekst_bez_tverdzhennya:
        print("\nlayer1: карток %d (прози %d, комірок %d)" % (n, proza, komirka))
        print("   тексту немає в книзі          %4d   ← справжня розбіжність"
              % len(nemaye))
        print("   контекст не містить твердження %4d   ← картка зламана як картка"
              % len(kontekst_bez_tverdzhennya))
        print("   текст на місці, номер зсунувся %4d   ← рендер застарів"
              % len(zsuv))
        print("   без блоку контексту            %4d" % len(bez_kontekstu))
    # Нуль оглянутих карток — не «розбіжностей немає», а «шукати не було
    # де». Ці два стани друкували ОДНЕ Й ТЕ САМЕ, і саме так цей файл
    # прожив кілька днів після переїзду карток у `cards/`: він дивився в
    # `factcheck/manual/`, тихо `continue` на відсутній теці, оглядав нуль
    # карток і звітував чотири нулі. `make check` був зелений і означав
    # рівно ніщо.
    if n == 0:
        print("\nlayer1: ЖОДНОЇ картки не оглянуто — це не «чисто», це "
              "«нема де шукати».\n   Перевір, що дзеркало книги лежить "
              "там, куди вказує `factcheck/book.yaml`.")
        return 1
    return 1 if (nemaye or kontekst_bez_tverdzhennya) else 0


def demo() -> int:
    """Показ на зіпсованому вході — і на порожньому.

    Другий випадок важливіший за перший. Перевірка, що ловить підроблену
    картку, але мовчки приймає порожній вхід, ловить рівно доти, доки
    хтось не пересуне теку."""
    import tempfile
    global ROOT, GRUPY
    ok = True

    def check(nazva: str, umova: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if umova else '✗'} {nazva}: {umova}")
        ok &= umova

    spravzhniy, spravzhni_g = ROOT, GRUPY
    # Формат — той самий, що друкує `factcheck.py`: твердження цитатою,
    # контекст в огорожі. Показ на вигаданому форматі довів би лише те,
    # що я його вигадав.
    kartka = ("<!-- fc id:T-01-001 sha:deadbeef src:rozdily/01.md:3 "
              "status:unchecked -->\n"
              "### T-01-001 · proza · `rozdily/01.md`\n\n"
              "**Твердження, коротко**\n\n> {tv}\n\n"
              "**Контекст**\n\n```\n{kx}\n```\n\n---\n")
    vypadky = [
        ("справна картка мовчить", "рядок книги", "рядок книги і ще щось", 0),
        ("текст, якого в книзі немає, ловиться",
         "цього в книзі немає", "рядок книги і ще щось", 1),
        ("контекст без твердження ловиться",
         "рядок книги", "зовсім інший абзац", 1),
    ]
    for nazva, tv, kx, ocik in vypadky:
        with tempfile.TemporaryDirectory() as d:
            t = pathlib.Path(d)
            (t / "rozdily").mkdir()
            (t / "rozdily" / "01.md").write_text(
                "# Р\n\nрядок книги і ще щось\n", encoding="utf-8")
            kart = t / "factcheck" / "cards" / "rozdily"
            kart.mkdir(parents=True)
            (kart / "01.md").write_text(kartka.format(tv=tv, kx=kx),
                                        encoding="utf-8")
            ROOT, GRUPY = t, ("rozdily",)
            config.ROOT = t
            try:
                got = main(["layer1", "--tykho"])
            finally:
                ROOT, GRUPY, config.ROOT = spravzhniy, spravzhni_g, spravzhniy
            check(nazva, got == ocik)

    with tempfile.TemporaryDirectory() as d:
        t = pathlib.Path(d)
        (t / "factcheck").mkdir()
        ROOT, GRUPY = t, ("rozdily",)
        config.ROOT = t
        try:
            got = main(["layer1", "--tykho"])
        finally:
            ROOT, GRUPY, config.ROOT = spravzhniy, spravzhni_g, spravzhniy
        check("НУЛЬ карток — це провал, а не «чисто»", got == 1)

    print("\nпровалів:", 0 if ok else 1)
    return 0 if ok else 1


if __name__ == "__main__":
    if "--demo" in sys.argv:
        sys.exit(demo())
    sys.exit(main(sys.argv))
