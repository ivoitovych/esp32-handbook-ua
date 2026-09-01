#!/usr/bin/env python3
"""The registry skeleton: a structure parallel to the body of the book.

The idea. A review reads a chapter and asks "is this coherent".
Fact-checking takes **one claim** and asks "how is this known". The second
question does not scale in anybody's head: a book holds thousands of
claims, and no amount of reading guarantees that none was missed.

So the registry is built mechanically and is **complete by
construction**: the tool decomposes every file of the book into claim
units and creates a parallel document in which every unit has its own
record. Passes then fill those records with evidence. A unit with no
evidence is a visible emptiness rather than a forgotten line.

    factcheck/tools/factcheck.py sketch   create or re-sync the skeleton
    factcheck/tools/factcheck.py status   a summary by evidence status
    factcheck/tools/factcheck.py stale    is the registry still about this book
    factcheck/tools/factcheck.py blocked  unreachable sources, as a hand-off

Synchronisation. Every record holds a hash of the book's verbatim text.
If the text in the book changed, `stale` shows it: the evidence may have
applied to the previous wording. That is what distinguishes a living
registry from a snapshot quietly drifting away from the book.

The word "if" above was a promise rather than a description for a long
time: `stale` checked only whether the file existed. The wording was left
as it stood, which is why nobody noticed.
"""

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
# `GRUPY` was eight copies of one fact — this book's directories. The
# copies agreed, which is what made them dangerous: a set of copies does
# not lie until the fact changes, and then it lies in all of them at once.
# It is data now: `factcheck/book.yaml`.
GRUPY = config.groups()
FC = ROOT / "factcheck"

# The evidence statuses. One table for everybody, and its key is the
# WORD.
#
# ## Why not a letter
#
# Until 2026-08-29 a status lived in three parallel notations — the letter
# `A`, the word `verbatim`, the sign `✅` — and a card printed all three
# in a row:
#
#     - **Class:** ✅ A — primary, quoted — the extract from the source…
#
# Two of the three carry nothing the third does not; they merely require
# the reader to remember an eleven-item legend. The sharpest phrasing of
# the objection: **an abbreviation is not a talking name**, and the whole
# discipline of naming in code rests on talking names.
#
# And they had already drifted, as copies always do. One status carried
# TWO English words at once — `unverified` in the data and `unchecked` in
# a tool. `unchecked` was chosen: it means "nobody looked", whereas
# `unverified` reads as "we checked and it did not hold up".
#
# The key order IS the descending strength; `STRENGTH_BY_LETTER` is
# derived from it rather than kept as a separate dictionary that could
# drift.
# These strings are not only console output: the report generator prints
# them into `REPORT.md`, and the consistency gate compares the list
# against `METHOD.md`. They are normative text of the technology, and are
# in English along with it.
STATUSES = {
    "verbatim": "primary, quoted — the source was obtained and the extract copied",
    "derived": "primary, inferred — the source was obtained; the claim follows unambiguously",
    "absent-from-source": "proof by absence — the document was obtained and what was named is not in it; the silence is the proof",
    "arithmetic": "calculation — checked by arithmetic; no external source is needed",
    "named-unreachable": "secondary — the source cannot be reached from here; URL recorded, no quote",
    "self-consistent": "internal check — the book agrees with itself; no external confirmation",
    "looked-not-found": "looked and did not find — the work was done, the source is not visible",
    "no-external-signal": "no signal in the text to check against — assigned mechanically, not checked",
    "refuted": "refuted, or needs an edit",
    "unchecked": "not checked",
    "code-context": "context — a whole code block; the claims live in its lines",
}

# The letters remain only as a translation for tools and callers that
# still pass one. Nothing new is labelled with them. The registry itself
# carries words: the `klas` field was removed from all 1366 records and
# from all 8331 card comments on 2026-08-31.
LETTER_TO_STATUS = {
    "A": "verbatim", "B": "derived", "N": "absent-from-source",
    "D": "arithmetic", "C": "named-unreachable", "S": "self-consistent",
    "L": "looked-not-found", "E": "no-external-signal", "G": "refuted",
    "F": "unchecked", "K": "code-context",
}
STATUS_TO_LETTER = {v: k for k, v in LETTER_TO_STATUS.items()}

CLASS_TEXT = {k: STATUSES[v] for k, v in LETTER_TO_STATUS.items()}
SIGN = {"A": "✅", "B": "🟢", "C": "🟡", "D": "🔵", "E": "⚪", "F": "🔴",
        "G": "⚠", "K": "▫", "L": "🔎", "S": "🔁", "N": "🚫"}

ALL_CLASSES = "".join(CLASS_TEXT)
CLASSES_OF_UNITS = "".join(k for k in CLASS_TEXT if k != "K")  # no code blocks
# The same thing as WORDS, derived from the same source rather than
# written out beside it.
STATUSES_OF_UNITS = [s for s in STATUSES if s != "code-context"]

RE_ZAPYS = re.compile(
    r"<!--\s*fc\s+id:(?P<id>[\w.-]+)\s+sha:(?P<sha>[0-9a-f]{8})"
    r"\s+src:(?P<src>[^\s]+)\s+status:(?P<status>[\w-]+)\s*-->"
)


# One pattern for everybody who reads the **short statement of the
# claim** from a card. Each consumer used to hold its own copy of the old
# heading. The heading was renamed — and not one of them failed: four
# tools silently began finding nothing, and their reports went on looking
# correct.
#
# > A pattern that reads somebody else's format must live in the same
# > place as whoever writes that format. A copy of the pattern is a
# > promise not to change the format, and nobody made that promise.
#
# The heading itself is shared too, and that was what had been missing:
# the pattern above lived in one place while another tool held its own
# copy of the STRING, and that copy stayed on the old heading. That tool
# examined zero units and printed three zeros in a row.
#
# A copy of a pattern is a promise not to change the format. A copy of the
# string itself is the same promise, shorter and therefore less
# visible.
CLAIM_HEADING = "Твердження, коротко"

RE_TVERDZHENNYA = re.compile(
    r"\*\*" + re.escape(CLAIM_HEADING)
    + r"\*\*\n\n(?P<txt>(?:> [^\n]*\n)+)")


# The kinds of unit whose card text is a **rendering** rather than the
# book's text.
#
# A table cell becomes a line like `BME280 · Address → 0x76`, which does
# not exist in the book; such a card needs a separate block holding the
# raw row.
#
# Prose is the opposite: the splitter takes sentences **from the book**,
# so a unit's text is already verbatim (verified: 46 of 46 sentences in
# one chapter are substrings of the book). Adding a "verbatim" block to it
# is not merely redundant but harmful: the book wraps lines in the middle
# of a sentence, and the block showed a **fragment**:
#
#     T-63-002  …le role of the chip in somebody else's system, and
#
# An audit found this: 5194 cards of 8331 broke off mid-word. By a
# stricter measure, 3851. The kind is the same one already recorded three
# times under other names ("a thought cut in half", "a cell with no
# context"): **the executor judges half a thought.** Only this time the
# half was cut by the very tool built against that.
#
# > The condition was `raw != text` — "show it if it differs". For prose
# > that is true through line wrapping alone. The condition should have
# > asked about the **kind of unit**, not about the inequality of two
# > strings.
RENDER = ("komirka", "tablycya", "tablycya-shapka")


def sha(text: str) -> str:
    return hashlib.sha256(" ".join(text.split()).encode("utf-8")).hexdigest()[:8]


# A line of code that asserts something about the world: a call, a
# constant, a command, a register write. The rest — braces, comments,
# variable declarations — asserts nothing and does not enter the
# registry.
RE_KOD_TVERDZHENNYA = re.compile(
    r"^\s*(?:"
    r"#define\s+\w+|"
    r"#include\s*[<\"]|"
    r"[A-Za-z_][\w:.]*\s*\([^;]*\)\s*[;,]?\s*$|"          # a call
    r"\.\w+\s*=|"                                          # a field initialiser
    r"(?:esptool|idf\.py|espefuse|pio|nvs_partition_gen|picocom|minicom|"
    r"screen|dd|python|strings|xtensa-|riscv32-|sudo|ls|dmesg|lsof|git|make)\b"
    r")"
)


# An externally checkable signal in a unit's text.
#
# What counts as an externally checkable signal — from
# `factcheck/book.yaml`, because these words are the book's, not the
# technology's.
#
# Among thousands of units there are those for which no external source
# exists or ever will: an editorial judgement, a piece of advice, a
# framing sentence, a link between chapters. Keeping them "unchecked"
# promises work nobody will do, and hides behind them the units that
# genuinely need checking.
#
# So a unit with **no external signal at all** moves to
# `no-external-signal`: no digit, no identifier, no name, no unit of
# measure. That is the consequence of a rule and **not** a conclusion that
# no source exists. A random sample of 160 units found that about 37 % of
# them do have an external referent.
#
# The broad criterion is deliberately biased toward keeping a unit in the
# work queue, and it applies **only to prose**. Tables, cells, code lines
# and schematic connections are never moved: that is where the facts live,
# and a cell like "0 · Touch → T1" looks empty only because the row's
# subject stands apart from it.
#
# The strict criterion is the opposite: a signal is only what **points at
# a source**. The broad rule's "any digit" keeps a list ordinal
# ("…check the supply. 4.") in the queue forever, which is right as
# caution and expensive as policy.
_sig = config.signal()
RE_ZOVNISHNIY_SYGNAL = re.compile(_sig["broad"])
RE_SYGNAL_STROGYY = re.compile(_sig["strict"])


# A line of an ASCII schematic: two pins joined by a line. Each such line
# is a **separate** claim, and almost always has a different source from
# its neighbour: "3V3 ─── VCC" is checked against the sensor's datasheet,
# "SDA ─── GPIO21" against the board's documentation, "└─[4.7k]─ 3V3"
# against the bus specification.
#
# Until then a schematic was registered as one record, and evidence for
# any part of it marked the whole thing checked. An external review showed
# where that ends: a complete project schematic stood with evidence
# pointing at a sensor datasheet, which could never have confirmed the
# presence of a particular GPIO on a particular chip.
RE_SCHEMA_ZVYAZOK = re.compile(r"[─━]{2,}|[│┬└┌┐┘├┤]|-{3,}[>\s]|→")


def rozbyty_tablycyu(ryadky: list[str], vid: int) -> list[tuple[str, str, int]]:
    """A table -> one claim per **cell**, not per row.

    The row `| UART | 3 | 2 | 3 | 2 | 3 | 2 |` is six independent claims
    about six different chips, and five of them being checked says nothing
    about the sixth. So a cell is rendered as "row · column → value",
    which reads as a sentence in its own right.

    Two-column tables stay whole: there the row IS the claim ("symptom →
    cause"), and cutting it up is pointless.
    """
    # Pairs of **(real line number, line)**, not bare lines.
    #
    # There was a defect here invisible to every check we had. The filter
    # discards the `|---|---|` separator, and the enumeration that
    # followed gave an index into the **filtered** list, which was then
    # added to an offset into the **unfiltered** one. Every cell after a
    # separator slid by as many lines as had been discarded above it.
    #
    # The consequence is worse than a wrong address: the renderer takes
    # the book's line **by that number**, so the "verbatim from the book"
    # block held a neighbouring line — often the separator itself.
    #
    # Measured by asking directly whether the line shown in a card really
    # stands in the book at the recorded number: **1360 cells of 1383**
    # did not. Neither the book-to-record layer nor the staleness check
    # saw it: the first compares against a **window** around the number,
    # the second by the hash of the text. Both were answering their own
    # question correctly.
    pary = [(i, r) for i, r in enumerate(ryadky)
            if not re.match(r"^\|[\s:|-]+\|$", r.strip())]
    korysni = [r for _i, r in pary]
    if not korysni:
        return []

    def komirky(r: str) -> list[str]:
        return [c.strip() for c in r.strip().strip("|").split("|")]

    shapka = komirky(korysni[0])
    if len(shapka) <= 2:
        return [("tablycya", r.strip(), vid + i) for i, r in enumerate(ryadky)
                if not re.match(r"^\|[\s:|-]+\|$", r.strip())]

    out: list[tuple[str, str, int]] = []
    out.append(("tablycya-shapka", korysni[0].strip(), vid + pary[0][0]))
    for i, r in pary[1:]:
        k = komirky(r)
        pidmet = k[0] if k else ""
        for j, v in enumerate(k[1:], 1):
            if j >= len(shapka) or not v or v in ("—", "-", ""):
                continue
            kolonka = shapka[j] or f"column {j}"
            out.append(("komirka", f"{pidmet} · {kolonka} → {v}", vid + i))
    return out


def rozbyty(text: str) -> list[tuple[str, str, int]]:
    """A file -> a list of (kind, verbatim text, line number).

    Kinds of unit:
      proza            a sentence outside code and tables
      tablycya         a row of a two-column table
      tablycya-shapka  the header of a wide table
      komirka          a single cell of a wide table
      kod              a whole code block — as context
      kod-ryadok       one line of code that asserts something

    Headings, blank lines and block markup are skipped: they assert
    nothing about the world.
    """
    odynyci: list[tuple[str, str, int]] = []
    ryadky = text.split("\n")
    i, n = 0, len(ryadky)
    # Every line carries its own number: otherwise every sentence of a
    # paragraph gets
    # the number of its **start**, and the card promises a precision it
    # does not have.
    #
    # Caught by comparison with the book-to-record layer: five list cards
    # stood with the same line number 38, while the items lie on 38–42.
    # The staleness check could not see it and could not have — it
    # compares the generator with itself, not with the book.
    #
    # > Two checks of the same layer disagreed, and both were right: one
    # > asked "is this registry from this book", the other "does the
    # > number lead where it promises". The second question had never
    # > been asked.
    buf: list[tuple[int, str]] = []
    buf_vid = 0

    def zlyty_prozu():
        nonlocal buf, buf_vid
        if not buf:
            return
        # Stitch the block together and remember at which character each
        # each line — so that a sentence can later be given the number
        # of its own line rather than the paragraph's.
        chastky, mezhi, poz = [], [], 0
        for nomer, x in buf:
            s = x.strip()
            if not s:
                continue
            mezhi.append((poz, nomer))
            chastky.append(s)
            poz += len(s) + 1
        blok = " ".join(chastky)
        buf = []
        if not blok:
            return

        def ryadok_dlya(zmishchennya: int) -> int:
            ostannij = buf_vid
            for p, nomer in mezhi:
                if p > zmishchennya:
                    break
                ostannij = nomer
            return ostannij

        # Sentences. A dot in `0x1000.` or `v5.5` does not end a
        # sentence, so we split only where the punctuation is followed by
        # a capital letter or a dash.
        shukach = 0
        chastyny = re.split(r"(?<=[.!?])\s+(?=[«»А-ЯЇІЄҐA-Z\[`*—-])", blok)
        for c in chastyny:
            zm = blok.find(c, shukach)
            if zm < 0:
                zm = shukach
            shukach = zm + len(c)
            c = c.strip()
            if len(c) >= 25:
                odynyci.append(("proza", c, ryadok_dlya(zm)))

    while i < n:
        r = ryadky[i]
        if r.lstrip().startswith("```"):
            zlyty_prozu()
            start = i
            i += 1
            while i < n and not ryadky[i].lstrip().startswith("```"):
                i += 1
            tilo = ryadky[start + 1:i]
            odynyci.append(("kod", "\n".join(ryadky[start:i + 1]), start + 1))
            for j, kr in enumerate(tilo):
                if RE_SCHEMA_ZVYAZOK.search(kr):
                    odynyci.append(("schema-zvyazok", kr.strip(), start + 2 + j))
                elif RE_KOD_TVERDZHENNYA.match(kr) and len(kr.strip()) > 6:
                    odynyci.append(("kod-ryadok", kr.strip(), start + 2 + j))
            i += 1
            continue
        if r.startswith("|"):
            zlyty_prozu()
            start = i
            while i < n and ryadky[i].startswith("|"):
                i += 1
            odynyci += rozbyty_tablycyu(ryadky[start:i], start + 1)
            continue
        if r.startswith("#") or r.startswith(":::") or not r.strip():
            zlyty_prozu()
            i += 1
            continue
        if not buf:
            buf_vid = i + 1
        buf.append((i + 1, r))
        i += 1
    zlyty_prozu()
    return odynyci


# Where a card is written. The book's mirror lives under `cards/`, not in
# the root of
# `factcheck/`.
#
# This line is a COMPUTED path, and that is exactly why the path checker
# cannot see it: that one reads literals. After the cards moved, the
# generator silently wrote into a directory that no longer existed, and
# `mkdir(parents=True)` obligingly created it. Ninety-two cards landed
# beside the real ones, no check failed, and version control would have
# shown not an error but work.
#
# > A check that reads literals cannot see a computed path. Its limit is
# > recorded in the path checker, and this is the case that fell into
# > that limit.
KARTKY = "cards"


def shlyakh_reyestru(f: Path) -> Path:
    return FC / KARTKY / f.relative_to(ROOT)


def prefiks(f: Path) -> str:
    """A stable identifier prefix: 06 from manual/06-zhyvlennya.md."""
    m = re.match(r"([a-z]?\d+|[a-z])-", f.stem)
    return (m.group(1) if m else f.stem[:3]).upper()


DOKAZY = FC / "evidence"


def zavantazhyty_dokazy() -> list[dict]:
    """Evidence from `factcheck/evidence/*.yaml` — a list of records.

    A record binds to claims in two ways.

    **`sha:`** — the exact hash of the verbatim text. The hash is the key
    rather than the identifier, because an identifier is an ordinal within
    a file and a sentence inserted above shifts every one below it. A hash
    is bound to the claim itself, so evidence travels with it through a
    reordering — and, equally, **detaches itself** the moment the wording
    changes. The second is no less important than the first: the evidence
    was about those words, not these.

    **`zbih:`** — a pattern. One and the same claim lives in several
    places in the book (a chapter, a card, an appendix) and is proved
    once. The pattern covers every occurrence, and the generator prints
    what it covered, so the matching stays checkable rather than magical.
    """
    import yaml
    out: list[dict] = []
    if not DOKAZY.exists():
        return out
    for p in sorted(DOKAZY.glob("*.yaml")):
        for z in (yaml.safe_load(p.read_text(encoding="utf-8")) or []):
            z["_prokhid"] = p.stem
            out.append(z)
    return out


# Status word -> letter. The **value**, not merely the field name, is
# what made the letter the last thing to go: strength ordering, the
# description table and every comparison against "A"/"B" were keyed by
# letter, so a simple key rename would silently have started comparing
# words with letters.
SLOVO_V_LITERU = {
    "verbatim": "A", "derived": "B", "named-unreachable": "C",
    "arithmetic": "D", "no-external-signal": "E", "unchecked": "F",
    "refuted": "G", "code-context": "K", "looked-not-found": "L",
    "self-consistent": "S", "absent-from-source": "N",
}


def status_of(z: dict, typovo: str = "unchecked") -> str:
    """A record's status as a **word** — one accessor for everybody.

    This is the target form. `class_letter_of` below works through this
    one: while any caller still asks for a letter, both must give the same
    answer, and it is better that this be the same code than two copies of
    one rule.
    """
    s = str(z.get("status") or "").strip()
    if s in STATUSES:
        return s
    l = str(z.get("klas") or "").strip().upper()
    if l in LETTER_TO_STATUS:
        return LETTER_TO_STATUS[l]
    return typovo


def class_letter_of(z: dict, typovo: str = "F") -> str:
    """An evidence record's status letter, derived from the word.

    One accessor for everybody. Before it, every tool read the field
    itself, and contracting the names would have broken them all at once;
    now one place breaks, or does not.

    The order is deliberate: `status` first, because it is the target
    field. But two copies of one field were once found to have **diverged**
    in 29 records — while a migration is in progress a divergence here is
    not hypothetical, so the older field remains a fallback rather than
    the primary.
    """
    s = str(z.get("status") or "").strip()
    if len(s) == 1:
        return s
    if s in SLOVO_V_LITERU:
        return SLOVO_V_LITERU[s]
    # A word absent from the dictionary is no reason to forget the old
    # field.
    # Found on six records carrying a status word that was almost but not
    # quite the right one: the first version returned the default here and
    # the gates went quiet on them. An unknown word is a reason to reach
    # for the fallback field, not to invent an answer.
    return str(z.get("klas") or typovo)


# The strength of an evidence status. Lower is stronger.
# Proof by absence sits beside `derived`: the source **was obtained** and
# the claim follows from it unambiguously — the only difference is that it
# follows from silence rather than from a line. A hair weaker, because
# silence proves only where a neighbouring document of the same kind
# speaks (see the `control` field).
# Derived from `STATUSES` rather than kept as a separate dictionary: two
# records of one ordering drift, and that is exactly how the description
# table once asserted "the order is descending strength" while not being
# in that order.
STRENGTH_BY_LETTER = {STATUS_TO_LETTER[w]: i
        for i, w in enumerate(x for x in STATUSES if x != "code-context")}
STRENGTH = {w: i
              for i, w in enumerate(x for x in STATUSES if x != "code-context")}


def pidibraty(zapysy: list[dict], h: str, txt: str) -> dict | None:
    """Evidence for a claim: an exact hash wins, then the strongest.

    One claim may fall under several evidences: one pass recorded it as
    unreachable, a later one found a way around. The **strongest** must be
    taken, not the first encountered — otherwise the order of files in a
    directory would silently decide the result, and closed items would
    stay in the hand-off order for ever.
    """
    kandydaty = vsi_kandydaty(zapysy, h, txt)
    if kandydaty:
        return min(kandydaty, key=lambda z: STRENGTH_BY_LETTER.get(class_letter_of(z), 9))
    return None


def klyuch(z: dict) -> tuple[str, str]:
    """The identity of an evidence record, for coverage accounting.

    Not the title: titles come from the order's own wording, so two
    maintainers naturally arrive at identical ones. Keyed by title, a
    weaker same-named record vanished from both "matched nothing" and
    "superseded by a stronger one" — and the first of those lists exists
    precisely to catch a faulty pattern.
    """
    return (str(z.get("_prokhid", "?")), str(z.get("title", "?")))


def rozbyty_alternatyvy(vzirets: str) -> list[str]:
    r"""Split a pattern on its **top-level** `|`.

    Needed to audit individual alternatives. A dead evidence record is
    visible; a dead alternative inside a live record is not. The first
    alternative matched, so the record looks healthy, and the fact that
    the second matched no line at all appears nowhere — not in the
    coverage list, not in any check.

    This matters precisely because alternatives **accumulate**: an
    evidence is stretched from a chapter onto cards and appendices by
    adding branches, and every added branch is a fresh chance to miss
    silently.

    Brackets are counted and nothing is split inside `[...]`; `\|` is a
    literal.
    """
    chastyny: list[str] = []
    tek: list[str] = []
    hlyb = 0
    u_klasi = False
    i = 0
    while i < len(vzirets):
        c = vzirets[i]
        if c == "\\" and i + 1 < len(vzirets):
            tek.append(vzirets[i:i + 2])
            i += 2
            continue
        if u_klasi:
            tek.append(c)
            if c == "]":
                u_klasi = False
        elif c == "[":
            u_klasi = True
            tek.append(c)
        elif c == "(":
            hlyb += 1
            tek.append(c)
        elif c == ")":
            hlyb -= 1
            tek.append(c)
        elif c == "|" and hlyb == 0:
            chastyny.append("".join(tek))
            tek = []
        else:
            tek.append(c)
        i += 1
    chastyny.append("".join(tek))
    return [x for x in chastyny if x]


# The second form of a pattern's quiet lie: an alternative consisting of
# a bare subject name. Such a token matches **every** cell of that
# subject's column — including "board price → low", which an evidence
# about memory addresses then marked as derived.
#
# Catching this by the shape of the word will not work: a part number and
# a quantity both contain digits, and a vendor name and a measurement both
# contain a space. It is caught by **consequence**: a wide alternative
# touches many units while the evidence speaks about one. So the audit
# does not judge the shape — it prints each alternative's match count
# separately and leaves the decision to a person who can see the quote
# beside it.
SHYROKA_ALTERNATYVA = 4


def prychyna(chastyna: str, teksty: list[str]) -> str:
    """Why an alternative matched nothing — a guess, not a verdict.

    Loosenings of the pattern are tried one at a time. Whichever brings
    it back to life names the fault. Three are taken from cases that have
    actually occurred:

      case     — a capital letter at the start of a sentence. Two
                 maintainers stepped on this independently within an hour;
      wrapping — the book wraps a line where the pattern expected a space.
                 It appears when a pattern is written while looking at the
                 rendered form rather than the source;
      spacing  — an extra or missing space inside.

    A fourth case is when nothing revives it: the book's text changed
    after the evidence was written. That is not a fault of the pattern but
    work to be done — check whether the evidence still applies to the new
    wording.
    """
    try:
        if any(re.search(chastyna, x, re.S | re.I) for x in teksty):
            return "revives when case is ignored — a capital letter"
    except re.error:
        return "the pattern is invalid in itself"
    bez_perenosu = [re.sub(r"\s+", " ", x) for x in teksty]
    ch_plaskyy = re.sub(r"\\s\*\\n\?|\\s\+|\\n", " ", chastyna)
    try:
        if any(re.search(ch_plaskyy, x, re.S | re.I) for x in bez_perenosu):
            return "revives with spaces collapsed — a line wrap in the book"
    except re.error:
        pass
    # The head of a pattern is its first letters up to the first special
    # character. If even that occurs nowhere, the subject has left the
    # book rather than moved within it.
    holova = re.split(r"[\\(\[.*+?{|^$]", chastyna, 1)[0].strip()
    if len(holova) >= 4 and not any(holova.lower() in x.lower()
                                    for x in teksty):
        return f"the book does not even contain «{holova}» — the text changed"
    return "the beginning is there, the rest diverged — check against the new text"


def vsi_kandydaty(zapysy: list[dict], h: str, txt: str) -> list[dict]:
    """Every evidence that falls under this claim at all.

    Needed separately from the selection, to distinguish evidence
    superseded by something stronger from evidence that matched nothing:
    the first is normal (a pass closed an item), the second is a fault in
    the pattern.
    """
    tochni = [z for z in zapysy if h in [str(x) for x in (z.get("sha") or [])]]
    if tochni:
        return tochni
    return [z for z in zapysy
            if z.get("match") and _vzirets(z["match"]).search(txt)]


# There are 1337 patterns and `re`'s internal cache holds 512: without a
# cache of our own every call recompiled the same patterns, and a full
# units-by-evidence pass took minutes instead of seconds.
_KESH_VZIRCIV: dict[str, "re.Pattern[str]"] = {}


def _vzirets(v: str) -> "re.Pattern[str]":
    rx = _KESH_VZIRCIV.get(v)
    if rx is None:
        rx = _KESH_VZIRCIV[v] = re.compile(v, re.S)
    return rx


SHABLON_DOKAZU = """**Доказ**

- **Статус:** unchecked — не звірено
"""


def pole(z: dict, nove: str, stare: str, typovo=None):
    """A field of an evidence record: English name, old one as fallback.

    A dress rehearsal of the contraction showed that the card renderer
    reached for fields by **direct access** — and with the old names
    removed the generator died with a `KeyError`, which would have left
    both maintainers without cards that same day.

    > A single accessor saves only those who go through it. The status
    > accessor was correct and did not help four places that went round
    > it.

    A second rehearsal found seven more such places — and all seven had
    survived for one reason: **they were written with single quotes.** The
    migration searched for the double-quoted form, and the substitution
    did not see them.

    > A migration that searches for a string finds exactly the spelling
    > of that string it searched for. The rest remains — and looks
    > migrated.
    """
    v = z.get(nove)
    return v if v not in (None, "") else z.get(stare, typovo)


def nazva_zapysu(z: dict) -> str:
    """The title of an evidence record — one accessor, like the status.

    Eight display sites reached for the title directly. After the
    contraction all eight would have shown `?` — not a crash but a silent
    loss: the report would have stayed intact and become unreadable.
    """
    return str(pole(z, "title", "nazva", "?"))


def formatuvaty_dokaz(z: dict | None) -> str:
    if not z:
        return SHABLON_DOKAZU
    # Один запис стану, а не три поспіль.
    #
    # Тут стояло `{SIGN} {klas} — {CLASS_TEXT}`, тобто знак, літера й опис
    # одного й того самого, у такому порядку, що третій пояснює перші два.
    # Знак і літера не несли нічого, крім легенди з одинадцяти позицій,
    # яку читач мав тримати в голові.
    #
    # Слово лишається англійським, а опис українським, і це не суміш:
    # стан — це словник ТЕХНОЛОГІЇ, а опис написано для читача книги.
    stan = status_of(z)
    ch = [f"**Доказ**\n", f"- **Статус:** {stan} — {STATUSES.get(stan,'')}"]
    # The condition goes through the accessor too. Otherwise a record
    # whose value stands **only** under the old name would silently lose
    # its line: the access was fixed and the guard was not.
    dzh = pole(z, "source", "dzherelo")
    if dzh:
        ch.append(f"- **Джерело:** {dzh}")
    cyt = pole(z, "quote", "cytata")
    if cyt:
        tilo = "\n".join("  > " + x for x in str(cyt).rstrip().split("\n"))
        ch.append(f"- **Дослівно з джерела:**\n{tilo}")
    rozr = pole(z, "calculation", "rozrakhunok")
    if rozr:
        tilo = "\n".join("  " + x for x in str(rozr).rstrip().split("\n"))
        ch.append(f"- **Розрахунок:**\n{tilo}")
    sp = pole(z, "method", "sposib")
    if sp:
        ch.append(f"- **Спосіб і дата:** {sp}")
    shuk = pole(z, "look_for", "shukaty")
    if shuk:
        ch.append(f"- **Що шукати в джерелі:** {shuk}")
    nt = pole(z, "note", "notatka")
    if nt:
        ch.append(f"- **Нотатка:** {nt}")
    ch.append(f"- **Прохід:** {z.get('_prokhid','—')}")
    return "\n".join(ch) + "\n"


def ohorozha(vmist: str) -> str:
    """A fence longer than any backtick run inside the content.

    The context of a code claim **is** a fenced block, so wrapping it in
    ``` closes the wrapper at the inner fence and the rest of the card
    renders as loose text. Caught on `T-K01-030` by generating a single
    file instead of the whole registry.

    Markdown allows any fence of three or more backticks, and a longer
    one may contain a shorter one — so the fence is chosen from the
    content rather than fixed.
    """
    naydovsha = 0
    for shmatok in re.findall(r"`+", vmist):
        naydovsha = max(naydovsha, len(shmatok))
    return "`" * max(3, naydovsha + 1)


def dослівно_і_контекст(ryadky: list[str], ln: int,
                        tekst: str = "") -> tuple[str, str]:
    """Сирий рядок книги та його оточення.

    **Навіщо.** Досі картка несла лише рендер одиниці —
    `BME280 · Адреса → 0x76` — під заголовком «Книга каже, дослівно».
    Такого рядка в книзі немає, тож заголовок брехав, а картку не можна
    було віддати ані людині, ані помічникові: щоб зрозуміти твердження,
    треба було лізти в книгу.

    Ціна цього була вимірна. Три сесії поспіль ми записували роди
    хибних тривог — «поділ відрізає застереження», «комірка без
    контексту», «суперечка про ступінь» — і всі вони одна причина:
    **виконавець судив половину думки.** Одинадцять заявлених
    суперечностей, жодної справжньої.

    **Що вважається контекстом.** Для рядка таблиці — найближчий
    заголовок вище, речення перед таблицею, шапка таблиці й сама
    таблиця. Для прози — абзац і сусідні абзаци.

    Номер рядка тут — єдина річ, якій довіряють, і вона ненадійна: М2
    поміряли, що він застарілий у 1311 одиницях із 8090. Тому функція
    **не падає** на хибному номері: поза межами файлу вона чесно
    віддає порожнє, і картка це показує.
    """
    # Номер рядка — **локатор, а не якір**, і він застаріває від кожної
    # правки книги без перегенерації: М2 поміряли, що він хибний у 1311
    # одиницях із 8090.
    #
    # Перша редакція цієї функції брала рядок просто за номером — і
    # картка про `ESP8266 / ESP-12` дістала дослівний рядок про
    # `ESP32-C3-MINI-1`, бо номер зсунувся на одиницю. Нове поле брехало
    # **впевненіше** за старий рендер, який воно мало виправити.
    #
    # Тому спершу **пошук за вмістом**, і лише як запасний шлях — номер.
    # Ключі беруться з самої одиниці: для комірки це значення обабіч
    # роздільників рендеру.
    # Рендер комірки має вигляд `<рядок> · <колонка> → <значення>`.
    # **Назва колонки стоїть у шапці таблиці, а не в рядку даних** — і
    # саме вона провалила першу спробу пошуку: `all(...)` не збігався
    # ніколи, тож функція мовчки падала назад на застарілий номер.
    # Тому ключі — лише «рядок» і «значення».
    if " · " in tekst:
        label, _, resh = tekst.partition(" · ")
        _, _, znach = resh.partition(" → ")
        syrovyna = [label, znach]
    else:
        syrovyna = [tekst]
    # **Перший збіг, а не найближчий, ставив картку в чужу таблицю.**
    # Знахідка М2 від `05:26Z`: після виправлення роздільника лишилося
    # 42 комірки, чий рядок стоїть у книзі за іншим номером, і зсуви
    # великі — `−62`, а не `±1`. Причина: `| I²C |` починає рядок у
    # **двох** таблицях розділу 04, і ключі («рядок» плюс «значення»)
    # у короткому значенні на кшталт `2` збігаються з першою-ліпшою:
    #
    #     p54   | I²C | дві лінії, багато пристроїв, невисока швидкість | 35 |
    #     p116  | I²C | 2 | 2 | 2 | **1** | 1 + 1 LP | 2 |
    #
    # Це рід 10 у нашому ж каталозі — ключування за значенням, яке не
    # унікальне; там воно знищило дев'ятнадцять записів через `gpio.rst`
    # у десятку каталогів ESP-IDF. М2 назвали цей зв'язок першими.
    #
    # Лікування не в тому, щоб зробити ключ довшим, а в тому, щоб дати
    # кожній половині її роботу: **вміст ототожнює, номер розрізняє**.
    # Номер застаріває на одиниці — і саме тому він годиться обрати
    # найближчий із однакових збігів, хоч і не годиться сам собою.
    #
    # Виміряно на всіх 1417 комірках книги:
    #
    #     перший збіг  = рядок за номером   1327
    #     найближчий   = рядок за номером   1401
    klyuchi = [k.strip(" `*") for k in syrovyna if len(k.strip(" `*")) >= 3]
    i = -1
    if klyuchi:
        zbihy = [j for j, r in enumerate(ryadky)
                 if all(k in r for k in klyuchi)]
        if zbihy:
            i = min(zbihy, key=lambda j: abs(j - (ln - 1)))
    if i < 0:
        i = ln - 1
    if not (0 <= i < len(ryadky)):
        return "", ""
    doslivno = ryadky[i].rstrip()

    # Межі: назад до заголовка або порожнього рядка перед абзацом,
    # уперед до кінця абзацу чи таблиці.
    poch = i
    while poch > 0:
        pop = ryadky[poch - 1].rstrip()
        if pop.startswith("#"):
            break
        if not pop and not doslivno.startswith("|"):
            break
        if not pop and poch < i and not ryadky[poch].startswith("|"):
            break
        poch -= 1
    # Межі вперед. **Порожній рядок усередині блоку коду — це вміст, а
    # не кінець абзацу.** Перша редакція цього не знала й обривала
    # контекст на першому ж порожньому рядку в коді: дамп паніки
    # показувався одним рядком із восьми, а картка при цьому твердила,
    # що дає оточення.
    #
    # Знайшов `layer1.py` М2 питанням, якого ми не ставили ніколи: **чи
    # містить контекст своє твердження.** 58 карток — усі роду `kod`.
    #
    # > Рід 5 у самій протиотруті: блок, зроблений показувати думку
    # > цілком, показував половину.
    v_kodi = ryadky[i].lstrip().startswith("```")
    kin = i
    while kin + 1 < len(ryadky):
        nast = ryadky[kin + 1].rstrip()
        if v_kodi:
            kin += 1
            if nast.lstrip().startswith("```"):
                break
            continue
        if not nast or nast.startswith("#"):
            break
        kin += 1

    # Заголовок розділу дає темі ім'я, а без імені комірка таблиці
    # читається як набір слів.
    zah = ""
    for j in range(poch, -1, -1):
        if ryadky[j].startswith("#"):
            zah = ryadky[j].rstrip()
            break

    tilo = [r.rstrip() for r in ryadky[poch:kin + 1]]
    if zah and zah not in tilo:
        tilo = [zah, ""] + tilo
    return doslivno, "\n".join(tilo).strip()


def sketch() -> int:
    FC.mkdir(exist_ok=True)
    dokazy = zavantazhyty_dokazy()
    vsjogo = z_dokazom = 0
    vzhyti: set[str] = set()
    # Ключем обліку служить пара «файл доказів + назва», а не сама
    # назва. Двоє супровідників беруть назви з того самого наряду, тож
    # збіг імен у різних файлах — очікуваний стан, а не випадковість.
    # За ключем-назвою слабший однойменний запис зникав з обох
    # переліків нижче, і доказ із хибним взірцем лишався невидимим.
    pokryttya: dict[tuple[str, str], list[str]] = {}
    zachepleni: set[tuple[str, str]] = set()
    # Тексти всіх одиниць — для окремого аудиту кожної альтернативи
    # взірця. Тримати їх коштує пам'яті, але дешевше, ніж другий обхід.
    usi_teksty: list[str] = []
    # `--only <substring>` limits the run to matching book files.
    #
    # Rebuilding the whole registry takes about half an hour, and a
    # format change that is wrong is only visible at the end of it.
    # Twice today a defect survived a full run: the card locator read a
    # stale line number, and the first fix searched for a key that lives
    # in the table header and so never matched.
    #
    # A format change is now tried on one file first. The rule is the
    # project's own `Р-ЗВІРКА`: test the instrument, then apply it.
    lyshe = None
    if "--only" in sys.argv:
        lyshe = sys.argv[sys.argv.index("--only") + 1]

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            if lyshe and lyshe not in str(f):
                continue
            tekst_knyhy = f.read_text(encoding="utf-8")
            ryadky_knyhy = tekst_knyhy.split("\n")
            odynyci = rozbyty(tekst_knyhy)
            cil = shlyakh_reyestru(f)
            cil.parent.mkdir(parents=True, exist_ok=True)
            pre = prefiks(f)
            chastyny = [
                f"# Фактчекінг: `{f.relative_to(ROOT)}`\n",
                f"Одиниць твердження: **{len(odynyci)}**. "
                "Статус доказу й формат запису — `factcheck/METHOD.md`, "
                "частина II.\n",
                "Цей файл **генерується**: текст книги береться з джерела, "
                "докази — з `factcheck/evidence/`. Правити вручну нема сенсу.\n",
                # Сказано раз на файл, а не на кожній із тисяч карток:
                # рецензентові потрібна ця гарантія, але вона однакова
                # для всіх карток файлу.
                "**Що в блоці «Твердження, коротко».** Для прози, рядка "
                "коду й зв'язки схеми — **дослівний текст книги**. Для "
                "комірки таблиці — рендер (`BME280 · Адреса → 0x76`), "
                "якого в книзі немає; дослівний рядок такої одиниці "
                "стоїть окремим блоком нижче.\n",
                "---\n",
            ]
            for k, (vyd, txt, ln) in enumerate(odynyci, 1):
                ident = f"T-{pre}-{k:03d}"
                h = sha(txt)
                usi_teksty.append(txt)
                kandydaty = vsi_kandydaty(dokazy, h, txt)
                for k_z in kandydaty:
                    zachepleni.add(klyuch(k_z))
                z = (min(kandydaty, key=lambda z: STRENGTH_BY_LETTER.get(class_letter_of(z), 9))
                     if kandydaty else None)
                if z:
                    vzhyti.add(h)
                    z_dokazom += 1
                    pokryttya.setdefault(klyuch(z), []).append(ident)
                # Блок коду цілком — **контекст**, а не твердження. Він
                # складається з рядків, у кожного з яких своє джерело, і
                # доказ на один рядок не звіряє решту. Тому клас блоку не
                # успадковується від доказу, а фіксований: `K`.
                if vyd == "kod":
                    klas = "K"
                elif z:
                    klas = class_letter_of(z)
                elif vyd in ("proza", "komirka", "tablycya") \
                        and not RE_SYGNAL_STROGYY.search(txt):
                    # Одиниця без жодного сигналу, що вказував би на
                    # джерело, — редакційна. Клас E, і це рішення, а не
                    # пропуск (див. коментар біля RE_SYGNAL_STROGYY).
                    #
                    # Зв'язки схем (`vyd == "shema"`) сюди не потрапляють
                    # ніколи: саме там живуть факти, і рядок «3V3 ─── VCC»
                    # виглядає порожнім лише тому, що підмет стоїть окремо.
                    klas = "E"
                else:
                    klas = "F"
                cyt = "\n".join("> " + x for x in txt.split("\n"))
                # Картка мусить бути самодостатньою: її віддають людині
                # або виконавцеві **без** доступу до книги. Тому поруч
                # із коротким викладом стоять сирий рядок і оточення.
                syryy, kontekst = dослівно_і_контекст(ryadky_knyhy, ln, txt)
                dodatkovo = ""
                if vyd in RENDER and syryy and syryy.strip() != txt.strip():
                    # Комірка живе в рядку таблиці. Якщо локатор привів
                    # кудись іще — він **промахнувся**, і показати цей
                    # рядок було б гірше, ніж не показати нічого: картка
                    # твердила б дослівність про чужий текст.
                    #
                    # Тридцять один такий випадок: взірець комірки
                    # «SPI · …» збігся з прозовим пунктом «**Швидкі
                    # сигнали** — SPI на високих частотах…».
                    if syryy.lstrip().startswith("|"):
                        o = ohorozha(syryy)
                        dodatkovo += ("**Дослівно з книги**\n\n"
                                      f"{o}\n{syryy}\n{o}\n\n")
                    else:
                        dodatkovo += (
                            "**Дослівно з книги:** рядок таблиці не "
                            "знайдено — локатор привів у прозу. Дивіться "
                            "контекст нижче.\n\n")
                if kontekst:
                    o = ohorozha(kontekst)
                    dodatkovo += ("**Контекст**\n\n"
                                  f"{o}\n{kontekst}\n{o}\n\n")
                elif not syryy:
                    dodatkovo += ("**Контекст:** номер рядка застарів — "
                                  "рядок за ним у книзі не знайдено.\n\n")
                chastyny.append(
                    f"<!-- fc id:{ident} sha:{h} "
                    f"src:{f.relative_to(ROOT)}:{ln} status:{LETTER_TO_STATUS.get(klas, klas)} -->\n"
                    f"### {ident} · {vyd} · `{f.relative_to(ROOT)}`\n\n"
                    f"**Твердження, коротко**\n\n{cyt}\n\n{dodatkovo}"
                    f"{formatuvaty_dokaz(z)}\n---\n"
                )
                vsjogo += 1
            cil.write_text("\n".join(chastyny), encoding="utf-8")
    print(f"файлів реєстру: {sum(1 for _ in FC.rglob('*.md'))}")
    print(f"одиниць твердження: {vsjogo}; із доказом: {z_dokazom}")
    if "-v" in sys.argv:
        print("\nщо покрив кожен доказ:")
        for (prokhid, nazva), ids in sorted(pokryttya.items(),
                                           key=lambda kv: kv[0][1]):
            print(f"  {len(ids):>3}×  {nazva}  ({prokhid})"
                  f"\n        {', '.join(ids)}")
    # Доказ, який нічого не зачепив, — це або застаріле формулювання в
    # книзі, або помилка у взірці. Мовчати про це не можна: реєстр почне
    # обіцяти звіреність, якої немає.
    #
    # Інша річ — доказ, що зачепив твердження, але програв сильнішому.
    # Це норма й навіть мета: слабший запис проходу 3 («джерело не
    # дістається») перекритий класом A проходу 4 означає, що пункт
    # наряду закрито. Такий випадок показуємо окремо й без тривоги.
    holosti = [z for z in dokazy if klyuch(z) not in zachepleni]
    perekryti = [z for z in dokazy
                 if klyuch(z) in zachepleni
                 and klyuch(z) not in pokryttya]
    if holosti:
        print(f"\n⚠ доказів, що нічого не зачепили: {len(holosti)}")
        for z in holosti:
            print(f"    {nazva_zapysu(z)}  ({z.get('_prokhid')})")
    if perekryti:
        print(f"\nперекрито сильнішим доказом: {len(perekryti)}")
        for z in perekryti:
            print(f"    {nazva_zapysu(z)}  "
                  f"({z.get('_prokhid')}, клас {class_letter_of(z, '?')})")

    # Аудит окремих альтернатив. Дві вади, невидимі вище:
    #
    #   мертва   — альтернатива не зачепила нічого, але сусідня
    #              спрацювала, тож доказ виглядає здоровим;
    #   широка   — альтернатива зачепила більше одиниць, ніж доказ
    #              узагалі стверджує.
    #
    # Обидві занижують або завищують покриття мовчки, і жоден чек на них
    # не падає. Тому це звіт, а не ворота: судити, чи 12 збігів широкі,
    # може лише той, хто бачить цитату.
    mertvi: list[tuple[dict, str, str]] = []
    shyroki: list[tuple[dict, str, int]] = []
    for z in dokazy:
        vz = z.get("match")
        if not vz:
            continue
        chastyny = rozbyty_alternatyvy(vz)
        if len(chastyny) < 2:
            continue
        for ch in chastyny:
            try:
                r = re.compile(ch, re.S)
            except re.error:
                # Альтернатива, вирвана з контексту, може бути
                # недійсним взірцем сама по собі — це не вада доказу.
                continue
            n = sum(1 for x in usi_teksty if r.search(x))
            if n == 0:
                mertvi.append((z, ch, prychyna(ch, usi_teksty)))
            elif n >= SHYROKA_ALTERNATYVA:
                shyroki.append((z, ch, n))
    if mertvi:
        print(f"\n⚠ альтернатив без жодного збігу: {len(mertvi)}")
        for z, ch, ch_prychyna in mertvi:
            print(f"    {nazva_zapysu(z)}  ({z.get('_prokhid')})"
                  f"\n        ↳ {ch}"
                  f"\n          ({ch_prychyna})")
    if shyroki and "-v" in sys.argv:
        print(f"\nальтернатив від {SHYROKA_ALTERNATYVA} збігів: "
              f"{len(shyroki)}")
        for z, ch, n in sorted(shyroki, key=lambda x: -x[2]):
            print(f"  {n:>3}×  {nazva_zapysu(z)}  ({z.get('_prokhid')})"
                  f"\n        ↳ {ch}")
    return 0


def zbir_usikh() -> list[dict]:
    out = []
    for p in sorted(FC.rglob("*.md")):
        if p.name in ("README.md", "METHOD.md", "REPORT.md"):
            continue
        t = p.read_text(encoding="utf-8")
        for sh in re.split(r"(?=<!--\s*fc\s)", t):
            m = RE_ZAPYS.search(sh)
            if m:
                d = m.groupdict()
                d["fajl"] = str(p.relative_to(FC))
                d["tilo"] = sh
                # Коментар картки несе СЛОВО. Доти він ніс літеру, а
                # слово виводилося тут — навмисно в одному місці, щоб
                # стиснення прибрало рядок, а не додало другий шлях
                # читання. Рядок прибрано; літери в картках більше немає.
                d["klas"] = STATUS_TO_LETTER.get(d.get("status", ""), "F")
                out.append(d)
    return out


def status() -> int:
    zapysy = zbir_usikh()
    c = Counter(z["status"] for z in zapysy)
    kontekst = c.get("code-context", 0)
    # Блоки коду — контекст, а не твердження: відсотки рахуються від
    # тверджень, інакше знаменник роздувається тим, що ніхто й не збирався
    # звіряти.
    vsjogo = len(zapysy) - kontekst
    print(f"\nодиниць твердження: {vsjogo}"
          f"  (+ {kontekst} блоків коду як контекст)\n")
    zvireno = sum(c[k] for k in ("verbatim", "derived", "arithmetic"))
    for stan in STATUSES_OF_UNITS:
        n = c.get(stan, 0)
        if not n:
            continue
        print(f"  {stan:<20} {n:>5}  {n*100/vsjogo:5.1f}%   {STATUSES[stan]}")
    print(f"\n  звірено з джерелом або обчисленням "
          f"(verbatim + derived + arithmetic): "
          f"{zvireno} ({zvireno*100/vsjogo:.1f}%)")
    # `S` навмисно **поза** цим числом і навмисно окремим рядком.
    #
    # Поза — бо він не каже нічого про світ: книга, що сходиться сама з
    # собою, може дружно помилятися в обох місцях. Окремо — бо `E` теж
    # нічого не каже про світ, але `E` означає «звірки не було», а `S`
    # означає «звірка була, механічна, відтворна, і вона зійшлася».
    # Злити їх — значить викинути єдине, що тут виміряно.
    if c.get("self-consistent"):
        print(f"  внутрішня звірка, зовнішнього підтвердження немає "
              f"(self-consistent): "
              f"{c['self-consistent']}")
    print(f"  закрито як рішення (no-external-signal): "
          f"{c.get('no-external-signal', 0)}")
    print(f"  лишається (named-unreachable + unchecked + refuted): "
          f"{sum(c.get(s, 0) for s in ('named-unreachable', 'unchecked', 'refuted'))}")
    # за файлами: де найбільше незакритого
    per = Counter()
    for z in zapysy:
        if z["status"] in ("named-unreachable", "unchecked", "refuted"):
            per[z["fajl"]] += 1
    if per:
        print("\n  найбільше незакритого:")
        for f, n in per.most_common(8):
            print(f"    {n:>4}  {f}")
    return 0


def stale() -> int:
    """Чи розійшовся реєстр із книгою — і чим саме.

    ## Що тут було до 2026-08-27

    Докстрінг обіцяв «записи, чий текст у книзі змінився». Тіло
    перевіряло, **чи існує файл**. Про текст — жодного рядка.

    Через це реєстр чотири дні тихо відставав від книги: шість правок
    друкованого накладу не зрушили лічильника, і `make check` усі ці
    дні казав «розбіжностей немає». Знайшов М2, написавши перевірку з
    нуля саме тому, що не повірив, ніби її ще нема.

    > Це вже другий випадок того самого роду за день (перший — `vorota`:
    > обіцяно дві перевірки, зроблено одну). Обидва прожили довго з тієї
    > самої причини: **лічильник, що показує нуль, виглядає однаково і
    > коли все гаразд, і коли він нічого не рахує.**

    ## Що тут тепер

    Книга розбирається тими самими `rozbyty()` і `sha()`, що будують
    реєстр, і результат звіряється з тим, що лежить на диску. Спільний
    розбирач тут не економія, а вимога: своя копія розбору розійшлася б
    із генератором, і перевірка почала б підтверджувати саму себе.

    Три роди розходження, і вони різні за ціною:

    · **текст змінився** — доказ, прив'язаний до старого формулювання,
      більше не про це твердження. Дорого: тихо хибний доказ.
    · **зник / з'явився** — правка додала або прибрала твердження.
    · **зсунувся рядок** — текст той самий, поїхав лише номер. Дешево
      само собою, дорого через довіру: кожен, хто бере `src:рядок` із
      реєстру, дістає адресу, яка може бути мимо.
    """
    na_dysku: dict[str, dict] = {}
    for z in zbir_usikh():
        na_dysku[z["id"]] = z

    zminyly: list[tuple[str, str]] = []
    znykly: list[str] = []
    novi: list[str] = []
    zsuv: Counter[str] = Counter()

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            pre = prefiks(f)
            rel = str(f.relative_to(ROOT))
            bachyly: set[str] = set()
            for i, (_vyd, txt, ln) in enumerate(rozbyty(
                    f.read_text(encoding="utf-8")), 1):
                ident = f"T-{pre}-{i:03d}"
                bachyly.add(ident)
                z = na_dysku.get(ident)
                if z is None:
                    novi.append(ident)
                    continue
                if z["sha"] != sha(txt):
                    zminyly.append((ident, rel))
                elif z["src"] != f"{rel}:{ln}":
                    zsuv[rel] += 1
            for ident, z in na_dysku.items():
                if z["src"].split(":")[0] == rel and ident not in bachyly:
                    znykly.append(ident)

    print(f"  текст змінився   {len(zminyly)}")
    for ident, rel in zminyly[:20]:
        print(f"     ✗ {ident}  {rel}")
    print(f"  зникло записів   {len(znykly)}")
    for ident in znykly[:10]:
        print(f"     ✗ {ident}")
    print(f"  нових одиниць    {len(novi)}")
    for ident in novi[:10]:
        print(f"     + {ident}")
    print(f"  зсув номера рядка {sum(zsuv.values())} на {len(zsuv)} файлах")
    for rel, n in zsuv.most_common(6):
        print(f"     ~ {n:>4}  {rel}")

    if zminyly or znykly or novi or zsuv:
        print("\n  реєстр відстає від книги — `factcheck.py sketch` "
              "перед роботою")
    else:
        print("  реєстр збігається з книгою одиниця в одиницю")
    return 0
    return 0


NARYAD = FC / "reports" / "UNREACHABLE-SOURCES.md"


def blocked() -> int:
    """Наряд на винос: усе, що впирається в недосяжне звідси джерело.

    Клас C — не «не перевірили», а «перевірити звідси неможливо». Різниця
    між ними головна: перше закривається роботою тут, друге не
    закривається ніколи, скільки не працюй, і мусить поїхати в інше
    середовище.

    Тому команда не просто рахує, а **пише документ**, придатний віддати
    людині з відкритим доступом: джерело, скільки тверджень від нього
    залежать, що саме в ньому шукати і які твердження книги це закриє.
    Уся підготовча робота вже зроблена — лишається відкрити документ.
    """
    grupy: dict[str, dict] = {}
    for z in zbir_usikh():
        if z["status"] != "named-unreachable":
            continue
        mu = re.search(r"\*\*Джерело:\*\*[ \t]*(.+)", z["tilo"])
        u = " ".join(mu.group(1).split()) if mu else "—"
        sh = (re.search(r"\*\*Що шукати в джерелі:\*\*\s*(.+)", z["tilo"]) or [None, ""])[1]
        m = RE_TVERDZHENNYA.search(z["tilo"])
        txt = " ".join(m.group(1).replace("> ", "").split()) if m else ""
        # Це **не** запис доказу, а місцевий словник групування. Слово
        # те саме, схема інша — і саме тому переведення імен полів його
        # зачепило: заміна за рядком перейменувала три **читання**
        # (`g["look_for"]`), а один літерал, що ключ і створює, лишила
        # старим. `blocked` падав із `KeyError` від fbfa0c2 і до цієї
        # правки, бо його немає ні в `make check`, ні в жодній базі.
        g = grupy.setdefault(u, {"look_for": set(), "tverdzhennya": []})
        if sh:
            g["look_for"].add(sh.strip())
        g["tverdzhennya"].append((z["id"], z["src"], txt))

    if not grupy:
        print("записів класу C немає")
        return 0

    vsjogo = sum(len(g["tverdzhennya"]) for g in grupy.values())
    ryadky = [
        "# Наряд: джерела, недосяжні з цього середовища\n",
        "**Генерується** `factcheck/tools/factcheck.py blocked`. Правити вручну "
        "нема сенсу.\n",
        "**Це не перелік помилок.** Це перелік тверджень книги, які "
        "неможливо звірити з першоджерелом із контейнера, де книга "
        "робилася: політика egress відповідає `403` на домени виробників "
        "і стандартів.\n",
        "Кожен пункт підготовано до закриття: named джерело, що саме в "
        "ньому шукати, і які саме твердження книги від нього залежать. "
        "Людині з відкритим доступом лишається відкрити документ і "
        "звірити — робота вимірюється хвилинами на джерело.\n",
        "Закриті пункти повертаються сюди як докази класу `A` або `B` у "
        "`factcheck/evidence/`, після чого цей файл перегенеровується "
        "(`factcheck/tools/factcheck.py blocked`) і коротшає.\n",
        f"Станом на генерацію: **{vsjogo}** тверджень від "
        f"**{len(grupy)}** джерел.\n",
        "---\n",
    ]
    for u, g in sorted(grupy.items(), key=lambda kv: -len(kv[1]["tverdzhennya"])):
        ryadky.append(f"## {u}\n")
        ryadky.append(f"Залежить тверджень: **{len(g['tverdzhennya'])}**\n")
        if g["look_for"]:
            ryadky.append("**Що шукати:**\n")
            for s in sorted(g["look_for"]):
                ryadky.append(f"- {s}")
            ryadky.append("")
        ryadky.append("| Твердження | Де в книзі | Дослівно |")
        ryadky.append("|---|---|---|")
        for ident, src, txt in g["tverdzhennya"]:
            t = txt.replace("|", "\\|")[:160]
            ryadky.append(f"| `{ident}` | `{src}` | {t} |")
        ryadky.append("\n---\n")
    NARYAD.write_text("\n".join(ryadky), encoding="utf-8")

    print(f"\n{NARYAD.relative_to(ROOT)}: {vsjogo} тверджень від "
          f"{len(grupy)} джерел\n")
    for u, g in sorted(grupy.items(), key=lambda kv: -len(kv[1]["tverdzhennya"])):
        print(f"  {len(g['tverdzhennya']):>4}   {u}")
    return 0


# Ознаки, за якими твердження взагалі можна звірити із зовнішнім джерелом.
# Вага = наскільки дорого коштує помилка саме в цій ознаці.
SYGNALY = [
    (re.compile(r"0x[0-9A-Fa-f]{3,8}"), 5, "адреса"),
    (re.compile(r"GPIO\s?\d{1,2}"), 5, "пін"),
    (re.compile(r"\b(?:eFuse|strapping|Secure Boot|Flash Encryption)\b", re.I), 4, "незворотне"),
    (re.compile(r"\b[a-z_]+_[a-z_]+\("), 4, "виклик API"),
    (re.compile(r"\bCONFIG_[A-Z0-9_]+|menuconfig"), 4, "налаштування"),
    (re.compile(r"\d+(?:[.,]\d+)?\s*(?:мкА|мА|А|В|мВ|Ом|кОм|МОм|Гц|кГц|МГц|ГГц|"
                r"мкс|мс|с|год|КБ|МБ|ГБ|біт|бод|нФ|мкФ|°C|мм|см|м|Вт)\b"), 3, "число"),
    (re.compile(r"\b(?:esptool|idf\.py|espefuse|nvs_partition_gen|pio)\b"), 3, "команда"),
    (re.compile(r"\b(?:ESP32-[A-Z0-9]+|WROOM|WROVER|BME280|DS18B20|MAX\d+|"
                r"SN65HVD230|TP4056|SSD1306|HC-SR04|A4988|L298N)\b"), 3, "позиція"),
    (re.compile(r"\b(?:ADC|DAC|PWM|LEDC|MCPWM|RMT|PCNT|TWAI|I²C|SPI|UART|I²S|"
                r"NVS|OTA|PSRAM|IRAM|DMA)\b"), 2, "блок"),
]


def vaga(txt: str) -> tuple[int, list[str]]:
    v, chym = 0, []
    for rex, w, nazva in SYGNALY:
        if rex.search(txt):
            v += w
            chym.append(nazva)
    return v, chym


def cherga() -> int:
    """Незакриті твердження, найдорожчі першими.

    Прохід не має йти по книзі підряд: одиниця «Якщо в цій книзі є один
    розділ» і одиниця «GPIO 6–11 з'єднані з флешем» коштують різного.
    Черга ставить попереду те, де помилка коштує плати.
    """
    mezha = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    poz = []
    for z in zbir_usikh():
        if z["status"] not in ("named-unreachable", "unchecked", "refuted"):
            continue
        m = RE_TVERDZHENNYA.search(z["tilo"])
        if not m:
            continue
        txt = m.group(1)
        v, chym = vaga(txt)
        if v:
            poz.append((v, z["id"], z["fajl"], ",".join(chym),
                        " ".join(txt.replace("> ", "").split())[:100]))
    poz.sort(key=lambda x: (-x[0], x[1]))
    print(f"\nнезакритих зі звірюваними ознаками: {len(poz)}"
          f"  (показано {min(mezha, len(poz))})\n")
    for v, ident, fajl, chym, txt in poz[:mezha]:
        print(f"  [{v:>2}] {ident:<12} {chym:<28} {txt}")
    return 0


def shukaty() -> int:
    """`factcheck.py shukaty <підрядок>` → sha і текст твердження.

    Ключ доказу — хеш, а хеш у голові не тримають. Ця команда — місток
    між «пам'ятаю формулювання» і «знаю, під яким ключем його записати».
    """
    if len(sys.argv) < 3:
        print("вкажіть підрядок")
        return 1
    goloka = " ".join(sys.argv[2:]).lower()
    n = 0
    for z in zbir_usikh():
        m = RE_TVERDZHENNYA.search(z["tilo"])
        if not m:
            continue
        txt = " ".join(m.group(1).replace("> ", "").split())
        if goloka in txt.lower():
            print(f"  {z['sha']}  {status_of(z):<20} {z['id']:<12} "
                  f"{z['src']}\n      {txt[:150]}")
            n += 1
            if n >= 30:
                print("  …")
                break
    if not n:
        print("не знайдено")
    return 0


def vorota() -> int:
    """Випускні ворота реєстру (Р-VYPUSK).

    Що тут перевіряється — і чого свідомо немає.

    **Є:** жодного твердження класу `G`. `G` означає «джерело
    спростувало» — книга з таким записом суперечить сама собі, і
    випускати її не можна за жодних обставин.

    **Є:** жодного доказу, що нічого не зачепив. Такий доказ — або
    застаріле формулювання в книзі, або помилка у взірці; в обох
    випадках реєстр обіцяє звіреність, якої немає.

    **Немає:** вимоги «нуль класу F». Це навмисно. Реєстр розкладає
    книгу на тисячі одиниць, серед яких є редакційні судження й поради,
    яким зовнішнє джерело не потрібне й не буває. Вимога нуля змусила б
    закривати їх фіктивно — тобто зробила б реєстр гіршим, а не кращим.
    Правило натомість таке: `F` видимий і рахований, а `C` має наряд.
    """
    dokazy = zavantazhyty_dokazy()
    g = [z for z in dokazy if status_of(z) == "refuted"]
    for z in g:
        print(f"   ✗ спростоване твердження: {nazva_zapysu(z)} "
              f"({z.get('_prokhid')})")

    # Друга обіцянка docstring, якої тут **не було**: доказ, що не
    # зачепив жодної одиниці.
    #
    # Знайдено зовнішньою рецензією: опис казав про дві перевірки,
    # реалізація робила одну. Це гірше за відсутню перевірку — читач
    # контракту вважає інваріант захищеним, а він не захищений ніким.
    #
    # Правило, яке з цього випливає: **на кожен інваріант має бути
    # рівно один авторитетний перевіряч, і опис не є перевірячем.**
    teksty: list[str] = []
    for grupa in GRUPY:
        for f in sorted((ROOT / grupa).glob("*.md")):
            for _vyd, txt, _ln in rozbyty(f.read_text(encoding="utf-8")):
                teksty.append(txt)

    holosti = []
    for z in dokazy:
        vz = str(z.get("match", ""))
        if not vz:
            continue
        try:
            rx = re.compile(vz)
        except re.error as e:
            print(f"   ✗ взірець не компілюється: {nazva_zapysu(z)} "
                  f"({z.get('_prokhid')}) — {e}")
            holosti.append(z)
            continue
        if not any(rx.search(t) for t in teksty):
            holosti.append(z)
            print(f"   ✗ доказ нічого не зачепив: {nazva_zapysu(z)} "
                  f"({z.get('_prokhid')})")

    print(f"factcheck-vorota: спростованих (G) {len(g)}, "
          f"холостих доказів {len(holosti)}")
    return 1 if (g or holosti) else 0


def vzirets() -> int:
    """Скільки одиниць реєстру зачепить цей взірець.

        factcheck/tools/factcheck.py vzirets '<регулярний вираз>'

    ## Навіщо окрема команда на три рядки коду

    Бо без неї перевіряють **не тим джерелом**, і я зробив це тричі за
    вечір, знаючи про пастку й описавши її сам.

    Взірець `zbih` зіставляється з **текстом одиниці реєстру**, а не з
    розміткою книги. Для прози це те саме, і саме тому помилка не
    впадає в око. Для комірки таблиці — ні:

        книга:   | Частота | 160–240 МГц | 16 МГц | 133 МГц |
        реєстр:  Частота · RP2040 → 133 МГц

    Взірець `\\| 133 МГц \\|` збігається з книгою й **не збігається ні з
    чим** у реєстрі. Перевірка `grep` по `manual/` каже «усе гаразд», і
    доказ тихо не зачіпає нічого.

    М2 на цій самій пастці мало не видалили 124 справні записи, бо
    писали швидшу перевірку по тексту книги. Правило записане в
    `docs/DESIGN.md` як `Р-ЗВІРКА`. Правила виявилося замало: доки
    зробити правильно було дорожче, ніж `grep`, я щоразу робив `grep`.

    Тому команда. Тепер правильне дешевше за неправильне.
    """
    if len(sys.argv) < 3:
        print("вжиток: factcheck/tools/factcheck.py vzirets '<вираз>'")
        return 2
    vyraz = sys.argv[2]
    try:
        rx = re.compile(vyraz)
    except re.error as e:
        print(f"негодящий вираз: {e}")
        return 2

    zbihy: list[tuple[str, str]] = []
    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            for _vyd, txt, _ln in rozbyty(f.read_text(encoding="utf-8")):
                if rx.search(txt):
                    zbihy.append((f.name, txt))

    print(f"взірець зачіпає одиниць: {len(zbihy)}")
    if not zbihy:
        print("  ⚠ ХОЛОСТИЙ — жодної одиниці. Доказ із таким взірцем "
              "нічого не звіряє.")
        return 1
    if len(zbihy) > 12:
        print("  ⚠ ЗАШИРОКИЙ? Широкий взірець небезпечніший за "
              "відсутній: він мовчки позначає «звірено» те, чого не "
              "звіряв.")
    for imya, txt in zbihy[:12]:
        print(f"    {imya}: {txt.strip()[:88]}")
    if len(zbihy) > 12:
        print(f"    … ще {len(zbihy) - 12}")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    return {"sketch": sketch, "status": status, "stale": stale,
            "blocked": blocked, "cherga": cherga, "vorota": vorota,
            "shukaty": shukaty, "vzirets": vzirets}.get(cmd, status)()


if __name__ == "__main__":
    sys.exit(main())
