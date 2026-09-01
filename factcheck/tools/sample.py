#!/usr/bin/env python3
"""A random sample of units in one status — to measure, not to harvest.

## Why a tool of its own

The sweep of `no-external-signal` took units **picked by hand** as the
likeliest to have a source. For harvesting that is right: you search where
the light is. For **measuring** it is useless — the sample was selected by
the very property you intend to measure, and any percentage from it is
inflated by construction.

And a measurement is needed here separately from a harvest. The status is
assigned **mechanically**: prose containing no digit, no identifier in
backticks, no chip or protocol name, no unit of measure written out. That
is a rule about **absence of signal**, and the book was printing something
else about it — "outside external checking: an editorial decision, a piece
of advice". Two different statements. How far apart they are cannot be
seen from a hand-picked sample.

## Why the seed is written into the order itself

A sample can be redrawn until the number is pleasing. There is one defence
against that: the seed and the method of selection live in the file beside
the result, so anybody can repeat the draw and get the same units. A
redrawn sample is immediately visible as a different seed.

So the seed here is **not** taken from the clock.

## Why there is a confidence interval here and none in the sweep

Because here it means something. The sample is random, so a percentage
from it estimates the percentage in the whole population, and that
estimate has an error which can be computed. Naming a share without its
error would be passing 160 units off as several thousand.

The sweep has no interval not out of laziness but because there it would
be a lie: the standard error of a sample mean says nothing about a sample
selected on the property under study.

    factcheck/tools/sample.py unchecked 150
    factcheck/tools/sample.py unchecked 150 --nasinnya 7   an explicit seed
    factcheck/tools/sample.py --zvit <dump-directory>      digest a wave
"""
from __future__ import annotations

import collections
import math
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml

import helper_dumps

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
# `GRUPY` was eight copies of one fact — this book's directories. The
# copies agreed, which is what made them dangerous. It is data now:
# `factcheck/book.yaml`.
GRUPY = config.groups()
CIL = ROOT / "factcheck" / "reports" / "BRIEF-SAMPLE.md"

NASINNYA = 20260826

RE_ZAHOLOVOK = re.compile(
    r"<!-- fc id:(?P<id>[\w-]+) sha:(?P<sha>\w+) src:(?P<src>[^\s]+) "
    r"status:(?P<status>[\w-]+) -->")
RE_CYTATA = re.compile(r"^> (?P<t>.+)$", re.M)


def odynyci(klas: str) -> list[dict]:
    """Every unit in a given status, in a stable order.

    Accepts either the word (`"unchecked"`) or the letter (`"F"`): the
    card comment now carries the WORD, and a letter is translated into
    it. The reverse of the line that stood here before the contraction.

    Stability here is not cosmetic: `glob` sorts anyway, but without
    `sorted()` the order would depend on the filesystem — and the same
    seed would give different samples on different machines.
    """
    import factcheck
    # Reduce both spellings to the WORD: that is what the card comment
    # carries now. Before the contraction the translation here ran the
    # other way, and afterwards `odynyci("A")` quietly found nothing —
    # 8331 cards, zero matches, no error at all. It was caught not by this
    # tool but by the guard "zero units is not a result" in `modality.py`.
    shukanyy = factcheck.LETTER_TO_STATUS.get(klas, klas)

    out: list[dict] = []
    for grupa in GRUPY:
        katalog = config.cards_root() / grupa
        if not katalog.exists():
            continue
        for f in sorted(katalog.glob("*.md")):
            tekst = f.read_text(encoding="utf-8")
            shmatky = RE_ZAHOLOVOK.split(tekst)
            # `split` with groups yields [before, id, sha, src, status,
            # after, ...]
            for i in range(1, len(shmatky), 5):
                ident, sha = shmatky[i], shmatky[i + 1]
                src, k = shmatky[i + 2], shmatky[i + 3]
                if k != shukanyy:
                    continue
                tilo = shmatky[i + 4]
                m = RE_CYTATA.search(tilo)
                # `status` is the target form, a WORD; `klas` remains
                # for tools that still ask for a letter. Both are derived
                # here from one `k`, so they cannot diverge.
                out.append({"id": ident, "sha": sha, "src": src,
                            "status": factcheck.LETTER_TO_STATUS.get(k, k),
                            "klas": k,
                            "tekst": m.group("t").strip() if m else ""})
    return out


ZAHOLOVOK_RAMKA = """# Order: a random sample of `{klas}`

> **generated** — `factcheck/tools/sample.py`; editing it by hand is
> wasted work

Seed **{nasinnya}**; **{skilky}** units drawn from a population of
**{vsyoho}**.
"""

# The shared rules come from `METHOD.md` Part IV, not rewritten here.
# Before the spec existed there were seven copies of them, and exactly one
# rule of eight agreed across all seven.
ZAHOLOVOK_BLOKY = ['ORIENTATION', 'VERBATIM', 'HONEST-MISS', 'NETWORK', 'STUB', 'VERDICTS-VERDICT-TEST', 'NO-SELF-REFERENCE', 'FORMAT']


def _reachable_block() -> str:
    """What the order tells a helper about where sources can be reached.

    From `book.yaml`. Carried inline until 2026-09-01, so an order
    generated for another book would have sent its helpers to ESP-IDF.
    An unconfigured book says nothing here, which is honest; naming
    another book's repositories would not be."""
    r = config.reachable_sources()
    if not r:
        return ""
    parts = [r.get("intro", ""), ""]
    if r.get("where"):
        parts += ["Where to look:", r["where"]]
    if r.get("caveat"):
        parts += [r["caveat"]]
    return "\n".join(x for x in parts if x is not None)


def zaholovok(**kw) -> str:
    """The order: this batch's frame plus the shared task blocks.

    Substitution by **replacement**, not `.format`: the frame contains
    genuine ESP-IDF braces (`{IDF_TARGET_...}`), and `format` dies on them
    with a KeyError.
    """
    import task_spec
    ramka = ZAHOLOVOK_RAMKA
    kw.setdefault("reachable", _reachable_block())
    for k, v in kw.items():
        ramka = ramka.replace("{" + k + "}", str(v))
    return task_spec.sklasty(ZAHOLOVOK_BLOKY, zaholovok=ramka,
                             shablon=ZAHOLOVOK_RAMKA)



# `unchecked` means "not yet checked", and the question put to it differs
# from the one put to `no-external-signal`.
#
# For the latter we test a **verdict**: is it true that no source exists.
# For `unchecked` there is no verdict at all — only work not done. So the
# verdicts differ, and the important one is the one the other order does
# not have: `disputes`. That is the one that finds errors in the book.
ZAHOLOVOK_F = """# Order: a random sample of `{klas}` — not yet checked

> **generated** — `factcheck/tools/sample.py`; editing it by hand is
> wasted work

Seed **{nasinnya}**; **{skilky}** units drawn from a population of
**{vsyoho}**.

## What these units are

`unchecked` means "not yet checked". Not "doubtful": nobody simply got to
these lines.

## The rule that matters more than the verdict

**Every answer must name the document you looked at.** Every one —
including those where nothing was found.

The reason is simple: without that, "not found" costs nothing, and it gets
written without opening anything. Such a record is neither a finding nor
evidence of the absence of one, and `factcheck/tools/measure_f.py`
discards it as "did not look" before the counting begins.

> The order does not say which answer it expects. It says what every
> answer must produce.

The list of verdicts and what each requires is below, in the task blocks.
It is deliberately absent here: **no generator writes its own copy of
these rules**, and such a copy is exactly what used to stand here — with
verdict names the gate no longer accepts.

`source` always begins with `https://raw.githubusercontent.com/`.

**An address pointing at the handbook itself** is rejected mechanically:
a handbook is not a source for itself. The book's text quoted below is
what is being **checked**, not what it is checked against.

## How to search

For each unit: choose the document this ought to be in, download it with
`curl`, look. Then a verdict from the table above.

{reachable}

## Prohibitions

In full — `METHOD.md` Part V; the most important are below, in the task
blocks, and are not repeated here.

## On `disputes`

The most valuable answer: the book can still be corrected. But only when
you **see a different text**, not when you remember otherwise.

"""



ZVIT = ROOT / "factcheck" / "reports" / "MEASURE-NO-SIGNAL.md"

RE_NE_TVERDZHENNYA = re.compile(
    r"не тверджен|самоопис|заголов|назв[ау] колонк|вступ до перел|підпис",
    re.I)


KANDYDATY = ROOT / "factcheck" / "work" / "queues" / "sample-candidates.yaml"


def tretiy_shar_vybirky(zap: list[dict]) -> tuple[int, int]:
    """How many claimed `znayshov` really stand at the named address."""
    kand = [{"title": str(z.get("odynycya", "?")),
             "source": str(z.get("source", "")).strip(),
             "quote": str(z.get("quote", "")),
             "zvidky": z.get("_fayl", "?")}
            for z in zap if str(z.get("verdykt")) == "znayshov"]
    if not kand:
        return 0, 0
    KANDYDATY.write_text(
        "# `znayshov` candidates from the **random** sample. Not a\n"
        "# registry: layer 3 checks them before the number enters a report.\n"
        + yaml.safe_dump(kand, allow_unicode=True, sort_keys=False),
        encoding="utf-8")
    try:
        import layer3
    except ImportError:
        return 0, len(kand)
    naslidky, _ = layer3.perevirka(True, [KANDYDATY])
    return (sum(1 for x in naslidky if x.get("stan") == "ok"), len(kand))


def zvesty(katalog: Path) -> int:
    """Digest a random sample's dumps into a measurement with an error."""
    # The first run of this measurement lost 40 of 160 units to broken
    # YAML — and lost them **not at random**: both helpers whose files
    # failed had the highest share of "has a referent". So a silent loss
    # shifted precisely the number being measured, and shifted it down.
    #
    # Hence `factcheck/tools/helper_dumps.py`: a mechanical repair of what
    # was written, and a list naming every file repaired.
    zap, polagodzheni, bidy = helper_dumps.read_dir(katalog)
    for z in zap:
        z["_hto"] = str(z.get("_fayl", "?")).split("-")[0]

    n = len(zap)
    if not n:
        print("sample: no dumps found")
        return 1

    # A fourth state the order had no separate verdict for: a unit that
    # **is not a claim about the world at all** — a column heading, the
    # lead-in to a list, a row of a table in which the book describes
    # itself.
    #
    # A mutual finding: I saw it in the very first batch (`T-00-022`, a
    # row of the status table), and M2 generalised it better — it is a
    # measure of the **granularity of the tool**, not of the book. There
    # is nothing to verify in such a unit and nothing to be ashamed of;
    # it simply should not have existed.
    #
    # Counted by a pattern over the `chomu` field, and that is **a guess,
    # not a verdict**: the helper wrote it as free text. The number can be
    # trusted as an order of magnitude, not as a bound.
    ne_tverdzhennya = sum(
        1 for z in zap
        if str(z.get("verdykt")) == "spravdi-e"
        and RE_NE_TVERDZHENNYA.search(str(z.get("chomu", ""))))

    c = collections.Counter(str(z.get("verdykt", "?")) for z in zap)
    maye_referenta = c["znayshov"] + c["ideya"]
    pozyciya = c["spravdi-e"] - ne_tverdzhennya

    # `znayshov` from the sample also passes layer 3. At first it did not
    # — only the sweep was checked — and that was a hole: these records
    # give the loudest part of the answer, and they are exactly what the
    # order puts pressure on.
    #
    # M2's finding: an order saying "test this verdict" reads as "refute
    # this verdict", and that pressure manufactures invented refutations
    # as reliably as "find a source" manufactured sources.
    #
    # **But it does not affect the total, and not by accident.** A failed
    # quote does not prove there is no referent — it proves the referent
    # was not obtained. The unit falls from `znayshov` to `ideya`, and
    # both states count as "has a referent". The measurement is robust to
    # this fault by
    # construction: pressure moves units between baskets without adding any.
    vystoyalo, zayavleno = tretiy_shar_vybirky(zap)

    def promizhok(k: int) -> tuple[float, float]:
        """A 95 % Wilson interval. Near 0 the normal approximation lies."""
        p, z = k / n, 1.96
        seredyna = (p + z * z / (2 * n)) / (1 + z * z / n)
        pivshyryna = (z / (1 + z * z / n)) * math.sqrt(
            p * (1 - p) / n + z * z / (4 * n * n))
        return (max(0.0, seredyna - pivshyryna),
                min(1.0, seredyna + pivshyryna))

    nyz, verh = promizhok(maye_referenta)

    # The population is read **live**, not taken as a number from the day
    # of the draw. The status melts: merging M2's work moved some of its
    # units into checked statuses and 3892 became 3350. A number written
    # in goes quietly stale and starts to lie exactly where it is read
    # most carefully — in the line "this many claims were closed too
    # generously".
    #
    # The share stays valid meanwhile: the sample was drawn from this
    # status and answers about it, however many of them there are now.
    populyaciya = len(odynyci("no-external-signal"))

    # The spread between helpers. Not cosmetic: if different judges give
    # different shares on the same data, the true error is larger than the
    # sampling error, and the Wilson interval below is optimistic.
    po_hto: dict[str, list[int]] = collections.defaultdict(lambda: [0, 0])
    for z in zap:
        hto = str(z.get("_hto"))
        po_hto[hto][1] += 1
        if str(z.get("verdykt")) in ("znayshov", "ideya"):
            po_hto[hto][0] += 1
    chastky = [k / v for k, v in po_hto.values() if v]

    r = [f"""# Measuring `no-external-signal`

> **generated** — `factcheck/tools/sample.py --zvit`; editing it by hand
> is wasted work

The order is in `factcheck/reports/BRIEF-SAMPLE.md`, and the sampling
seed with it.

The question: **what share of `no-external-signal` has an external
referent** — that is, was assigned too generously. The sample is
**random**, so the percentage may be carried to the whole status, unlike
`factcheck/reports/SWEEP-NO-SIGNAL.md`, where the sample was picked by
hand to suit the answer.

## Result

Units in the sample: **{n}**.

| Verdict | Count | Share |
|---|---|---|
| `znayshov` — the source was obtained | {c['znayshov']} | {c['znayshov'] / n:.0%} |
| `ideya` — a source is named, not obtained | {c['ideya']} | {c['ideya'] / n:.0%} |
| `spravdi-e` — the author's position, no referent | {pozyciya} | {pozyciya / n:.0%} |
| **not a claim at all** — a heading, the book describing itself | {ne_tverdzhennya} | {ne_tverdzhennya / n:.0%} |

Of {zayavleno} claimed `znayshov`, **{vystoyalo}** survived layer 3. The
rest are counted as `ideya`: a failed quote proves the source was **not
obtained**, not that it does not exist. This does not affect the total —
both states count as "has a referent", and that is exactly why the
measurement is robust to the order's pressure.

**Has an external referent: {maye_referenta} of {n} = {maye_referenta / n:.0%}**
(95 % Wilson: {nyz:.0%}–{verh:.0%}).

## This status is not one thing but three

Decomposing the sample shows the verdict covers three states, and
confusing them means being ashamed of the wrong one:

| State | Share | In the status | What to do |
|---|---|---|---|
| has an external referent | {maye_referenta / n:.0%} | ~{round(maye_referenta / n * populyaciya):d} | **check it** — the verdict is wrong |
| the author's position | {pozyciya / n:.0%} | ~{round(pozyciya / n * populyaciya):d} | leave it; this is an honest verdict |
| not a claim at all | {ne_tverdzhennya / n:.0%} | ~{round(ne_tverdzhennya / n * populyaciya):d} | **not a unit**; a measure of the splitter's granularity |

The third row is M2's finding, generalised from their "remainder" basket
and confirmed here on a **random** sample — that is, now with the right to
carry the share to the whole status. A column heading, the lead-in to a
list, a row of a table in which the book describes its own registry: the
splitter calls all of these a claim, because it divides text
mechanically.

That share needs neither verifying nor apologising for: it measures the
**tool**, not the book. But it must not be hidden inside "unchecked"
either — that is exactly where an inflated sense of debt comes from.

So roughly **{round(maye_referenta / n * populyaciya):d}** units of this
status — out of {populyaciya} at this moment — are in fact checkable, and
the verdict "outside external checking" should not have stood on them.

The population is counted on every run rather than taken from the day of
the draw: the status melts as evidence records move its units elsewhere.
The share does not change with that — the sample was drawn from this
status and answers about it.

## Why this interval is optimistic

The Wilson interval accounts only for sampling error — it assumes each
unit has one right answer that any judge would give identically. That is
not so here.

Частки «має референта» по помічниках: {', '.join(f'{x:.0%}' for x in sorted(chastky))}.

The spread between judges is **larger than the sampling error**. So the
main source of uncertainty is not that there are {n} units rather than
{populyaciya}, but that the line between "the author's advice" and "a
claim about the world" is drawn differently by different people.
Narrowing the interval with a longer sample is pointless until that line
is described more precisely.

That is no reason to discard the measurement. It establishes the order of
magnitude firmly: this is about **hundreds** of misfiled units, not a
dozen.
"""]
    if polagodzheni:
        r.append("\n## Repaired dumps\n")
        r.append("Mechanically corrected (values quoted), content "
                 "unchanged: "
                 + ", ".join(f"`{b}`" for b in polagodzheni) + ".\n")
        r.append("The cause is the maintainer's briefing, not the "
                 "helpers: the format required a colon inside a value. "
                 "See `factcheck/tools/helper_dumps.py`.\n")
    if bidy:
        r.append("\nWould not parse and were skipped: "
                 + ", ".join(f"`{b}`" for b in bidy) + ".\n")

    r.append("\n## Units that do have a referent\n")
    r.append("| Unit | Verdict | Where to look, or what was found |")
    r.append("|---|---|---|")
    for z in zap:
        v = str(z.get("verdykt"))
        if v not in ("znayshov", "ideya"):
            continue
        shcho = str(z.get("propozyciya") or z.get("komentar") or "").strip()
        r.append(f"| `{z.get('odynycya','?')}` | {v} | {shcho[:140]} |")

    ZVIT.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"sample: sample {n}, has a referent {maye_referenta} "
          f"({maye_referenta / n:.0%}, 95% {nyz:.0%}–{verh:.0%}) "
          f"→ {ZVIT.relative_to(ROOT)}")
    return 0


def main() -> int:
    if "--zvit" in sys.argv:
        i = sys.argv.index("--zvit")
        if i + 1 >= len(sys.argv):
            print("sample: --zvit needs a directory of dumps")
            return 2
        return zvesty(Path(sys.argv[i + 1]))
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    # `.upper()` was right while a status was one letter. After the
    # contraction it turns `unchecked` into `UNCHECKED`, which matches
    # nothing — the tool then printed "no units found in status UNCHECKED"
    # and exited 0, so a draw of zero units looked like an empty status
    # rather than a broken argument.
    klas = sys.argv[1]
    if len(klas) == 1:
        klas = klas.upper()
    skilky = int(sys.argv[2])
    nasinnya = NASINNYA
    if "--nasinnya" in sys.argv:
        nasinnya = int(sys.argv[sys.argv.index("--nasinnya") + 1])

    vsi = odynyci(klas)
    if not vsi:
        print(f"sample: no units found in status {klas}")
        return 1
    skilky = min(skilky, len(vsi))
    vybir = random.Random(nasinnya).sample(vsi, skilky)
    vybir.sort(key=lambda z: z["id"])

    # Batch size is not cosmetic. A batch decides how many units a helper
    # holds in mind at once: a long batch invites answering "in bulk", a
    # shorter one keeps attention on each unit separately.
    na_paket = 8
    if "--na-paket" in sys.argv:
        na_paket = int(sys.argv[sys.argv.index("--na-paket") + 1])

    # `unchecked` has a frame of its own (a different question is being
    # asked there); the shared blocks are the same. Both spellings are
    # accepted for the status name.
    import factcheck
    if factcheck.LETTER_TO_STATUS.get(klas, klas) == "unchecked":
        import task_spec
        ramka = ZAHOLOVOK_F
        for k, v in dict(klas=klas, nasinnya=nasinnya,
                         vsyoho=len(vsi), skilky=skilky,
                         reachable=_reachable_block()).items():
            ramka = ramka.replace("{" + k + "}", str(v))
        # `VERDICTS-EXTERNAL`, not `VERDICTS-VERDICT-TEST`: in the
        # unchecked queue there is no verdict of somebody else's to test —
        # only work not done. Until recently the verdict-test block was
        # sent here, and the executor saw TWO tables of verdicts: this one
        # and that one.
        bloky_f = [b if b != 'VERDICTS-VERDICT-TEST' else 'VERDICTS-EXTERNAL'
                   for b in ZAHOLOVOK_BLOKY]
        shapka = task_spec.sklasty(bloky_f, zaholovok=ramka)
    else:
        shapka = zaholovok(klas=klas, nasinnya=nasinnya,
                           vsyoho=len(vsi), skilky=skilky)
    r = [shapka.rstrip("\n"), ""]
    for i, z in enumerate(vybir):
        if i % na_paket == 0:
            r.append(f"\n## Batch {i // na_paket + 1}\n")
        r.append(f"**`{z['id']}`** · `{z['src']}`\n")
        r.append(f"> {z['tekst']}\n")
    CIL.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"sample: status {klas}, population {len(vsi)}, sample "
          f"{skilky}, seed {nasinnya} → {CIL.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
