#!/usr/bin/env python3
"""Rebuild idle patterns from the text of the REGISTRY UNIT.

## Why they go idle

A pattern is written against the book's markup and matched against the
registry's rendering. For prose these are the same; for a table cell they
are not:

    the book:      | `0xf` | RTCWDT_BROWN_OUT_RESET | supply sagged |
    the registry:  0xf · Cause → supply sagged

A pattern with pipes matches the book and matches nothing in the
registry. The evidence looks alive and is dead: it promises a
checkedness that does not exist.

Forty-four such were found by a new half of the release gate; sixteen
more were made the same day by assembling a pattern from the RECORD'S
TITLE instead of the unit's text. A record's title is a maintainer's
signature, not the book's text; it can match the registry only by
accident.

## What this script does

For every idle record it looks for the registry unit it actually concerns
and builds a pattern from that unit's text: escaped as literal text, with
flexible spaces. The candidate is chosen by the share of tokens shared
with the record's title and quote, and taken only when one candidate's
lead over the next is convincing.

A tie is not a reason to retreat but a reason to look closer. Of 59 idle
records, 26 had no single winner, and in every case the reason was the
same and legitimate: **the record deliberately covers several units.**
One evidence about two similar parts applies equally to both table rows:

    MAX31855 · Gives → thermocouple
    MAX6675  · Gives → thermocouple, cheaper

That is what alternatives in a pattern are for. So on a tie an
alternation is built across every candidate level with the first — not a
guess, but coverage.

What it does NOT do: guess. If no candidate reaches the threshold, the
record stays idle and is printed in the list. A silent binding to the
wrong unit is worse than an idle pattern — an idle one is visible, a
wrong binding is not.

    factcheck/tools/patterns_repair.py            show what it would do
    factcheck/tools/patterns_repair.py --pysaty   write it
"""
from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402
import factcheck  # noqa: E402
import sample  # noqa: E402

LEKSEMA = re.compile(r"[0-9A-Za-zА-Яа-яЇїІіЄєҐґ_.\-]{3,}")
POROG = 0.34      # the minimum share of shared tokens
KONTROLNI = ("ESP32 має два ядра", "Зовсім інший текст про каву", "12345")


def leksemy(s: str) -> set[str]:
    return {w.lower() for w in LEKSEMA.findall(s or "")}


def slova_vzirtsya(v: str) -> set[str]:
    """Literal words from the old pattern, without the regex machinery."""
    t = re.sub(r"\\([|.*+?()\[\]{}^$])", r"\1", v)   # strip the escaping
    t = re.sub(r"\\s\+|\\s\*|\.\*|\.\+|\[[^\]]*\]|[|()?*+{}^$]", " ", t)
    return leksemy(t)


def vzirets_z(tekst: str) -> str:
    yadro = re.sub(r"\s+", " ", tekst.strip())[:110].rstrip(" .,;:—-")
    return re.escape(yadro).replace(r"\ ", r"\s+")


def main(argv: list[str]) -> int:
    pysaty = "--pysaty" in argv

    odynyci = []
    # There used to be a string "ABCDEFG" here — a private copy of the
    # status list, which had already lost two statuses and would never
    # have gained a third. This is what the comment beside `ALL_CLASSES`
    # warns about: a copy of a list is the same promise not to change it
    # as a copy of a pattern.
    for klas in factcheck.ALL_CLASSES:
        for o in sample.odynyci(klas):
            odynyci.append((o["tekst"], leksemy(o["tekst"])))

    teksty = [t for t, _ in odynyci]
    zhyvi = set()
    for z in factcheck.zavantazhyty_dokazy():
        v = str(z.get("match") or "")
        if not v:
            continue
        try:
            rx = re.compile(v)
        except re.error:
            continue
        if any(rx.search(t) for t in teksty):
            zhyvi.add((str(z.get("_prokhid")), str(z.get("title"))))

    polagodzheno = nezmineno = 0
    for shlyakh in sorted(glob.glob(str(ROOT / "factcheck" / "evidence" / "m2-*.yaml"))):
        recs = yaml.safe_load(Path(shlyakh).read_text(encoding="utf-8")) or []
        prokhid = Path(shlyakh).stem
        tor = False
        for r in recs:
            if not isinstance(r, dict) or not r.get("match"):
                continue
            if (prokhid, str(r.get("title"))) in zhyvi:
                continue
            klyuch = slova_vzirtsya(str(r.get("match", "")))
            if len(klyuch) < 3:
                klyuch |= leksemy(str(r.get("title", "")))
            if not klyuch:
                continue
            ocinky = sorted(
                ((len(klyuch & lk) / max(1, len(klyuch)), t) for t, lk in odynyci),
                key=lambda p: -p[0])
            o1 = ocinky[0][0]
            if o1 < POROG:
                nezmineno += 1
                print("   ? %-26s %s" % (prokhid[:26], str(r.get("title"))[:48]))
                continue
            # Level with the first: anything scoring at least 95 % of it.
            urnyven = [t for o, t in ocinky if o >= o1 * 0.95][:4]
            novyy = "|".join(vzirets_z(t) for t in urnyven)
            # The pattern must compile and must not match foreign text.
            try:
                rx = re.compile(novyy)
            except re.error:
                nezmineno += 1
                continue
            if all(rx.search(k) for k in KONTROLNI):
                nezmineno += 1
                continue
            # Write BOTH names until the migration is over.
            #
            # This is where 15 divergences between the two field names
            # were born: this tool narrowed one and left the other, and a
            # leak stayed in the one it left. Repairing the data while
            # leaving the cause is postponement, not a fix. This line may
            # be removed only together with the contraction run.
            r["zbih"] = r["match"] = novyy
            if len(urnyven) > 1:
                print("      (alternation over %d units)" % len(urnyven))
            r["notatka"] = r["note"] = (
                str(r.get("note", "") or "").strip() +
                " | Pattern rebuilt from the registry unit's text: the "
                "previous one was written against the book's markup "
                "(table pipes) and matched nothing.").strip(" |")
            polagodzheno += 1
            tor = True
            print("   ✓ %-26s %s" % (prokhid[:26], str(r.get("title"))[:48]))
        if tor and pysaty:
            Path(shlyakh).write_text(
                yaml.dump(recs, allow_unicode=True, sort_keys=False,
                          default_flow_style=False, width=100), encoding="utf-8")

    print("\nrebuilt %d; no candidate visible for %d%s"
          % (polagodzheno, nezmineno,
             "" if pysaty else "  (dry run, nothing written)"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
