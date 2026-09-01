#!/usr/bin/env python3
"""Dividing the unchecked between maintainers — by reachability of the source.

The queue (`factcheck.py cherga`) sorts by cost of error and shows forty
rows. For two people working together that is not enough: what matters is
not "what is most expensive" but **who can close it at all**.

The split here is not by topic and not by chapter but by one question: in
which document does the answer lie.

    ESP-IDF, esptool, `soc/` headers   -> M1, they are in his container
    part datasheets, electrical data   -> M2; M1's container answers 403

The rest are units with a weak signal (a chip or a term in backticks with
no number and no identifier). They stay `unchecked` deliberately: mostly
editorial, but telling that apart from the factual mechanically does not
work, so they wait for continuous passes rather than for a split.

The baskets themselves are this book's data — `factcheck/book.yaml`.

    factcheck/tools/split_queue.py            summary
    factcheck/tools/split_queue.py --naryad   write factcheck/reports/SPLIT.md
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

import factcheck  # noqa: E402  (after the sys.path adjustment)
FC = ROOT / "factcheck"
# `GRUPY` was eight copies of one fact — this book's directories. The
# copies agreed, which is what made them dangerous: a set of copies does
# not lie until the fact changes, and then it lies in all of them at once.
# It is data now: `factcheck/book.yaml`.
GRUPY = config.groups()

# The baskets are this book's data — see `factcheck/book.yaml`. Carried
# inline until 2026-09-01, which made this tool silent on any other book:
# every unit would land in the "nobody" basket and the split would look
# complete.
BUCKETS = [(b["who"], b["key"], b.get("what", ""),
            re.compile(b["pattern"]))
           for b in config.split_buckets()]

# The tail is taken from `factcheck.RE_TVERDZHENNYA` rather than written
# a second time: a private copy of that line has already once silently
# stopped matching, when the card heading was renamed.
RE_F = re.compile(
    r'<!-- fc id:(?P<id>\S+) sha:\S+ src:(?P<src>[^\s:]+):(?P<ln>\d+) '
    r'status:unchecked -->\n### \S+ · (?P<vyd>\w+) · [^\n]*\n\n'
    + factcheck.RE_TVERDZHENNYA.pattern)


def zibraty() -> tuple[list[dict], dict[str, list[dict]]]:
    vsi: list[dict] = []
    for g in GRUPY:
        for f in sorted((config.cards_root() / g).glob("*.md")):
            for m in RE_F.finditer(f.read_text(encoding="utf-8")):
                vsi.append(m.groupdict())
    rozklad: dict[str, list[dict]] = collections.defaultdict(list)
    for r in vsi:
        for hto, klyuch, _, p in BUCKETS:
            if p.search(r["txt"]):
                rozklad[f"{hto}-{klyuch}"].append(r)
                break
        else:
            rozklad["—"].append(r)
    return vsi, rozklad


# ── A full account of the remainder, not only of the strong signal ────
#
# The first version of this tool divided only `unchecked` units with a
# clear marker — 80 of them. The rest stayed "outside the split", and as
# long as nobody happened to ask "how many are there in total", that
# looked like a division of work.
#
# In fact **almost everything** was outside it: 1303 weak-signal
# `unchecked` units and the **whole** of `no-external-signal`. The latter
# was then believed closed by construction; measurement showed that about
# a third of its units do have an external source.
#
# So the split now enumerates every status, including those nobody will
# take up soon. An entry saying "nobody, and here is why" is also a
# division; a silent gap is not.

# The share of `no-external-signal` that has an external referent. Not a
# guess: a random sample of 160 units, seed recorded in the order, 95 %
# Wilson 30–45 %.
SHARE_WITH_REFERENT = 0.37


def klasy() -> dict[str, int]:
    """How many units are in each status — from the registry, not memory.

    The key is the **word**. The card comment now carries the word; the
    line that used to translate a letter into it is gone. There is no
    private parse of the comment here any more — that was the third copy
    of the same rule, and on the day of the contraction nobody would have
    remembered it.
    """
    import re as _re
    import factcheck
    lich: dict[str, int] = collections.Counter()
    vz = _re.compile(r"status:([\w-]+) -->")
    for g in GRUPY:
        for f in sorted((config.cards_root() / g).glob("*.md")):
            for m in vz.finditer(f.read_text(encoding="utf-8")):
                lich[factcheck.LETTER_TO_STATUS.get(m.group(1),
                                                    m.group(1))] += 1
    return dict(lich)


def podil_za_fajlamy(klasy: tuple[str, ...]) -> tuple[list[str], list[str], int, int]:
    """Divide the named statuses by file — greedily, toward the smaller sum.

    The same mechanism already proven on `no-external-signal`; that split
    is now a special case of this one. M2 called the split of the
    remainder "not obvious" — but obviousness is not what is needed here,
    an `assert` is: the intersection of files is zero, and it is visible.

        C+F  1935 units in 91 files -> 968 / 967, intersection 0
    """
    import sample
    za: dict[str, int] = collections.Counter()
    for k in klasy:
        for u in sample.odynyci(k):
            za[u["src"].split("/")[-1].split(":")[0]] += 1
    m1: list[str] = []
    m2: list[str] = []
    s1 = s2 = 0
    for f, n in sorted(za.items(), key=lambda kv: (-kv[1], kv[0])):
        if s1 <= s2:
            m1.append(f)
            s1 += n
        else:
            m2.append(f)
            s2 += n
    assert not (set(m1) & set(m2)), "a file went to both"
    return sorted(m1), sorted(m2), s1, s2


def podil_e() -> tuple[list[str], list[str], int, int]:
    """Divide `no-external-signal` by file — greedily, toward the smaller sum.

    It divides **files, not units**: two maintainers editing the same file
    produce a merge conflict on every record.

    The first version divided by the `src` field, which holds
    `file:line` — and scattered the same file across both sides, doing
    exactly what it was meant to prevent. The intersection is now
    asserted explicitly.
    """
    import sample
    za: dict[str, int] = collections.Counter(
        u["src"].split("/")[-1].split(":")[0] for u in sample.odynyci("no-external-signal"))
    m1: list[str] = []
    m2: list[str] = []
    s1 = s2 = 0
    for f, n in sorted(za.items(), key=lambda kv: (-kv[1], kv[0])):
        if s1 <= s2:
            m1.append(f)
            s1 += n
        else:
            m2.append(f)
            s2 += n
    assert not (set(m1) & set(m2)), "a file went to both"
    return sorted(m1), sorted(m2), s1, s2


def remonty() -> list[tuple[str, str, int, str]]:
    """Debt that is not new checking: repairing the records we have.

    A separate kind of work. It adds nothing to the checked count, but
    without it the percentages lie — and a registry that lies about
    itself is worse than a smaller honest one.
    """
    import layer3
    naslidky, _ = layer3.perevirka(False)
    lich = collections.Counter(str(n.get("stan")) for n in naslidky)
    return [
        ("both", "the quote does not match", lich.get("ne_znaydeno", 0),
         "a maintainer tidied the quote; check the book, then rewrite"),
        ("M1", "source not in the cache", lich.get("nedosyazhne", 0),
         "download it, or move to `named-unreachable` with an honest reason"),
        ("M2", "invented source", lich.get("vygadane", 0),
         "the status says checked; the source field holds an argument"),
        ("M2", "`unchecked` in the evidence field", lich.get("pomylka", 0),
         "that means there is no evidence; the record means nothing"),
        ("M2", "no-external-signal on a number", lich.get("nadmirnyy_e", 0),
         "\"no source exists\" on a claim carrying a rated value"),
    ]


def zvedennya() -> int:
    vsi, rozklad = zibraty()
    print(f"unchecked units: {len(vsi)}\n")
    for hto, klyuch, opys, _ in BUCKETS:
        k = f"{hto}-{klyuch}"
        print(f"  {hto}  {klyuch:9} {len(rozklad[k]):5}   {opys}")
    m1 = sum(len(v) for k, v in rozklad.items() if k.startswith("M1"))
    m2 = sum(len(v) for k, v in rozklad.items() if k.startswith("M2"))
    print(f"\n  M1 total: {m1}    M2 total: {m2}")
    print(f"  weak signal, outside the split: {len(rozklad['—'])}")

    k = klasy()
    e_ref = round(k.get("no-external-signal", 0) * SHARE_WITH_REFERENT)
    print(f"\n── the remainder, absent from the split above ──")
    print(f"  no-external-signal, estimated with a referent  {e_ref:5}   "
          f"({SHARE_WITH_REFERENT:.0%} of {k.get('no-external-signal', 0)}, random sample)")
    print(f"  named-unreachable, source out of reach    {k.get('named-unreachable', 0):5}   "
          f"M2: their network reaches further")
    print(f"\n── repairing the records we have ──")
    for hto, shcho, skilky, chomu in remonty():
        if skilky:
            print(f"  {hto:7} {shcho:24} {skilky:4}   {chomu}")
    return 0


def naryad() -> int:
    vsi, rozklad = zibraty()
    m1 = sum(len(v) for k, v in rozklad.items() if k.startswith("M1"))
    m2 = sum(len(v) for k, v in rozklad.items() if k.startswith("M2"))
    r = [
        "# Dividing the unchecked between maintainers\n",
        "> **generated** — written by `factcheck/tools/split_queue.py "
        "--naryad`; editing it by hand is wasted work\n",
        "Divided by one question: **in which document does the answer "
        "lie**. ESP-IDF, esptool and the `soc/` headers are reachable from "
        "M1's container; part datasheets and electrical data are not, and "
        "that is M2's work.\n",
        f"| | Basket | Units | Source |",
        "|---|---|---|---|",
    ]
    for hto, klyuch, opys, _ in BUCKETS:
        r.append(f"| **{hto}** | `{klyuch}` | {len(rozklad[f'{hto}-{klyuch}'])} "
                 f"| {opys} |")
    r += [
        f"\n**M1 total: {m1}. M2 total: {m2}.**\n",
    ]

    # A full account. The table above covers only what has a source
    # **guessable from the text**. That is the smaller part of the
    # remainder, and presenting it as "the division of work" would show a
    # tenth of the debt as the whole of it.
    k = klasy()
    e_ref = round(k.get("no-external-signal", 0) * SHARE_WITH_REFERENT)
    slabki = len(rozklad["—"])
    r += [
        "## The whole remainder, not only the strong signal\n",
        "The table above divides what has a source visible in the unit's "
        "own text. That is the smaller part of the debt. Below is all of "
        "it, including what nobody will take up soon: **an entry saying "
        "\"nobody, and here is why\" is also a division; a silent gap is "
        "not.**\n",
        "| Layer | Units | To whom | Why |",
        "|---|---|---|---|",
        f"| `unchecked`, source visible in the text | {m1 + m2} "
        f"| M1 {m1}, M2 {m2} | by reachability of the source |",
        f"| `unchecked`, weak signal | {slabki} | **nobody** "
        "| there is no marker to divide by; waits for continuous passes |",
        f"| `no-external-signal`, estimated with a referent | ~{e_ref} "
        f"| both equally | {SHARE_WITH_REFERENT:.0%} of "
        f"{k.get('no-external-signal', 0)} by random sample; divided by "
        "chapter, because the source is unknown in advance |",
        f"| `named-unreachable` | {k.get('named-unreachable', 0)} | M2 "
        "| their network reaches further; for M1 it is 403 by construction |",
        "",
        "### Repairing the records we have\n",
        "A separate kind of work: it adds nothing to the checked count, "
        "but without it the percentages lie. A registry that lies about "
        "itself is worse than a smaller honest one.\n",
        "| What | How many | To whom |",
        "|---|---|---|",
    ]
    for hto, shcho, skilky, chomu in remonty():
        if skilky:
            r.append(f"| {shcho} — {chomu} | {skilky} | {hto} |")
    r.append("")
    e1, e2, s1, s2 = podil_e()
    r.append(f"### `no-external-signal` divided by file — M1 {s1}, M2 {s2}\n")
    r.append("Divided by **files, not units**: two people in one file "
             "produce a merge conflict on every record. The intersection "
             "is asserted in the tool.\n")
    r.append(f"**M1 ({len(e1)}):** " + ", ".join(f"`{x}`" for x in e1) + "\n")
    r.append(f"**M2 ({len(e2)}):** " + ", ".join(f"`{x}`" for x in e2) + "\n")
    r.append("### Why this status is divided by chapter, not by source\n")
    r.append("Because the source there is **unknown in advance** — that is "
             "the whole point of the status. Reachability can only divide "
             "what you already know the location of. So it is divided by "
             "ranges of chapters: the only division that guarantees two "
             "people will not take the same unit.\n")
    for hto, klyuch, opys, _ in BUCKETS:
        k = f"{hto}-{klyuch}"
        if not rozklad[k]:
            continue
        r.append(f"\n## {hto} · `{klyuch}` — {len(rozklad[k])}\n")
        r.append(f"{opys.capitalize()}.\n")
        za_faylom = collections.defaultdict(list)
        for u in rozklad[k]:
            za_faylom[u["src"]].append(u)
        for src in sorted(za_faylom):
            r.append(f"\n### `{src}` — {len(za_faylom[src])}\n")
            r.append("| Claim | Line | Verbatim |")
            r.append("|---|---|---|")
            for u in za_faylom[src]:
                t = " ".join(x[2:] for x in u["txt"].strip().split("\n"))
                t = t.replace("|", "\\|")[:150]
                r.append(f"| `{u['id']}` | {u['ln']} | {t} |")
    (FC / "reports" / "SPLIT.md").write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"factcheck/reports/SPLIT.md: M1 {m1}, M2 {m2}, outside the split "
          f"{len(rozklad['—'])}")
    return 0


if __name__ == "__main__":
    sys.exit(naryad() if "--naryad" in sys.argv else zvedennya())
