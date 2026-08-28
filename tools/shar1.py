#!/usr/bin/env python3
"""Layer 1: does the card faithfully represent the book?

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

    tools/shar1.py [--vsi] [--tykho]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("manual", "dodatky", "kartky", "inserts")

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
    r" klas:(?P<klas>\S+) -->\n"
    r"### \S+ · (?P<vyd>\S+) · [^\n]*\n\n"
    r"\*\*[^*\n]+\*\*\n\n(?P<tverd>(?:> [^\n]*\n)+)"
    r"(?:\n\*\*Дослівно з книги\*\*\n\n(?P<og1>`{3,})\n(?P<doslivno>.*?)\n(?P=og1)\n)?"
    r"(?:\n\*\*Контекст\*\*\n\n(?P<og2>`{3,})\n(?P<kontekst>.*?)\n(?P=og2)\n)?",
    re.S)

VIKNO = 8   # рядків книги навколо записаного номера


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

    knyha: dict[str, list[str]] = {}
    cile: dict[str, str] = {}
    nemaye: list[tuple] = []
    zsuv: list[str] = []
    bez_kontekstu: list[str] = []
    kontekst_bez_tverdzhennya: list[tuple] = []
    n = proza = komirka = 0

    for g in GRUPY:
        katalog = ROOT / "factcheck" / g
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
                vikno = normal(" ".join(ryadky[max(0, i - 1):i + VIKNO]))

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

    granyca = None if vsi else 20
    for ident, rid, det in nemaye[:granyca]:
        print("   ✗ %-12s %-32s %s" % (ident, rid, det))
    if not vsi and len(nemaye) > 20:
        print("   ... ще %d" % (len(nemaye) - 20))
    for ident, t in kontekst_bez_tverdzhennya[:granyca]:
        print("   ✗ %-12s %-32s %s" % (ident, "КОНТЕКСТ НЕ МІСТИТЬ ТВЕРДЖЕННЯ", t))

    if not tykho or nemaye or kontekst_bez_tverdzhennya:
        print("\nshar1: карток %d (прози %d, комірок %d)" % (n, proza, komirka))
        print("   тексту немає в книзі          %4d   ← справжня розбіжність"
              % len(nemaye))
        print("   контекст не містить твердження %4d   ← картка зламана як картка"
              % len(kontekst_bez_tverdzhennya))
        print("   текст на місці, номер зсунувся %4d   ← рендер застарів"
              % len(zsuv))
        print("   без блоку контексту            %4d" % len(bez_kontekstu))
    return 1 if (nemaye or kontekst_bez_tverdzhennya) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
