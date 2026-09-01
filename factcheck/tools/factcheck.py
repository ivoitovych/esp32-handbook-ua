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
        # **A heading is not a claim, and never becomes a unit.**
        #
        # A heading names a topic. What it asserts — that this topic
        # exists and is in scope — is a statement about the BOOK'S OWN
        # STRUCTURE, and no external document could confirm or refute it.
        # The review that checks it is the table-of-contents review, not
        # fact-checking.
        #
        # Measured, so the exclusion is a decision rather than an
        # oversight: 850 heading lines, 744 distinct texts, and **0** of
        # 8331 units is a heading — by prefix or by content. Of the 850,
        # exactly two carry a VALUE rather than a name, and both are
        # covered by the units beneath them, which quote the heading
        # inside their own context block.
        #
        # `coverage.py` accounts for them as structural grounds and prints
        # the number; a heading is therefore visible as excluded rather
        # than quietly absent. `headers_are_not_claims()` below watches
        # for the case that would change this.
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
    # One notation for the status, not three in a row.
    #
    # This used to print sign, letter and description of one and the same
    # thing, in an order where the third explains the first two. The sign
    # and the letter carried nothing but an eleven-item legend the reader
    # had to keep in mind.
    #
    # The card's own headings below stay Ukrainian on purpose, and that is
    # not a mixture: a card is read beside the book, and the book is the
    # product. The status WORD is the technology's vocabulary and is
    # English; the description beside it is written for the book's reader.
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


def verbatim_and_context(ryadky: list[str], ln: int,
                        tekst: str = "") -> tuple[str, str]:
    """The book's raw line and its surroundings.

    **Why.** A card used to carry only the rendering of a unit —
    `BME280 · Address → 0x76` — under a heading reading "the book says,
    verbatim". No such line exists in the book, so the heading lied, and
    the card could be given neither to a person nor to an executor: to
    understand the claim you had to open the book.

    The cost was measurable. Three sessions running produced kinds of
    false alarm — "the split cuts off the caveat", "a cell with no
    context", "a dispute about degree" — and all of them had one cause:
    **the executor was judging half a thought.** Eleven claimed
    contradictions, not one real.

    **What counts as context.** For a table row: the nearest heading
    above, the sentence before the table, the table header and the table
    itself. For prose: the paragraph and its neighbours.

    The line number is the only thing trusted here, and it is unreliable:
    measured stale in 1311 units of 8090. So this function **does not
    fail** on a wrong number: past the end of the file it honestly returns
    nothing, and the card shows that.
    """
    # A line number is a **locator, not an anchor**, and it goes stale
    # with every edit to the book that is not followed by a regeneration:
    # measured wrong in 1311 units of 8090.
    #
    # The first version of this function took the line simply by number —
    # and a card about one chip got the verbatim line about a different
    # one, because the number had shifted by one. The new field lied
    # **more confidently** than the old rendering it was meant to fix.
    #
    # So: **search by content** first, and the number only as a fallback.
    # The keys come from the unit itself: for a cell, the values on either
    # side of the rendering's separators.
    # A cell renders as `<row> · <column> → <value>`. **The column name
    # stands in the table header, not in the data row** — and that is
    # what defeated the first search attempt: the conjunction never
    # matched, so the function silently fell back on the stale number.
    # Hence the keys are only "row" and "value".
    if " · " in tekst:
        label, _, resh = tekst.partition(" · ")
        _, _, znach = resh.partition(" → ")
        syrovyna = [label, znach]
    else:
        syrovyna = [tekst]
    # **The first match rather than the nearest put a card into the
    # wrong table.** After the separator bug was fixed, 42 cells remained
    # whose line stands in the book at a different number, and the shifts
    # were large — `−62`, not `±1`. The cause: the same leading cell
    # begins a row in **two** tables of one chapter, and a key made of
    # "row plus value" collides with the first of them whenever the value
    # is something as short as `2`:
    #
    #     p54   | I²C | дві лінії, багато пристроїв, невисока швидкість | 35 |
    #     p116  | I²C | 2 | 2 | 2 | **1** | 1 + 1 LP | 2 |
    #
    # This is a catalogued kind — keying on a value that is not unique.
    # Elsewhere it destroyed nineteen records, because one filename occurs
    # in a dozen directories of the same source tree.
    #
    # The cure is not a longer key but giving each half its own job:
    # **content identifies, the number discriminates**. A number goes
    # stale by one or two — which is exactly why it is fit to choose the
    # nearest among identical matches, though unfit on its own.
    #
    # Measured across all 1417 cells of the book:
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

    # Boundaries: back to a heading or the blank line before the
    # paragraph, forward to the end of the paragraph or table.
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
    # Forward boundary. **A blank line inside a code block is content,
    # not the end of a paragraph.** The first version did not know that
    # and cut the context at the first blank line in code: a panic dump
    # was shown as one line of eight, while the card asserted that it was
    # giving the surroundings.
    #
    # Found by the book-to-record layer asking a question never put
    # before: **does the context contain its own claim.** 58 cards, all of
    # kind `kod`.
    #
    # > The defect inside the antidote: a block built to show a thought
    # > whole was showing half of it.
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

    # A section heading gives the topic a name, and without a name a
    # table cell reads as a bag of words.
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
    # The accounting key is the pair "evidence file + title", not the
    # title alone. Maintainers take titles from the same order, so
    # identical names in different files are expected rather than
    # accidental. Keyed by title, a weaker same-named record vanished from
    # both lists below, and evidence with a faulty pattern stayed
    # invisible.
    pokryttya: dict[tuple[str, str], list[str]] = {}
    zachepleni: set[tuple[str, str]] = set()
    # The texts of every unit, for auditing each alternative of a
    # pattern separately. Holding them costs memory, but less than a
    # second pass.
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
    # project's own rule: test the instrument, then apply it.
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
                "докази — з `factcheck/evidence/`. Правити вручну нема "
                "сенсу.\n",
                # Said once per file rather than on each of thousands of
                # cards: a reviewer needs this guarantee, but it is the
                # same for every card in the file.
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
                # A whole code block is **context**, not a claim. It
                # consists of lines each with its own source, and evidence
                # for one line does not check the rest. So a block's
                # status is not inherited from evidence but fixed.
                if vyd == "kod":
                    klas = "K"
                elif z:
                    klas = class_letter_of(z)
                elif vyd in ("proza", "komirka", "tablycya") \
                        and not RE_SYGNAL_STROGYY.search(txt):
                    # A unit with no signal pointing at a source is
                    # editorial. `no-external-signal`, and that is a
                    # decision rather than an omission (see the comment
                    # beside the strict signal pattern).
                    #
                    # Schematic connections never arrive here: that is
                    # where the facts live, and a line like
                    # "3V3 ─── VCC" looks empty only because its subject
                    # stands apart from it.
                    klas = "E"
                else:
                    klas = "F"
                cyt = "\n".join("> " + x for x in txt.split("\n"))
                # A card must be self-sufficient: it is handed to a
                # person or an executor **without** access to the book.
                # So the raw line and its surroundings stand beside the
                # short statement.
                syryy, kontekst = verbatim_and_context(ryadky_knyhy, ln, txt)
                dodatkovo = ""
                if vyd in RENDER and syryy and syryy.strip() != txt.strip():
                    # A cell lives in a table row. If the locator led
                    # anywhere else it **missed**, and showing that line
                    # would be worse than showing nothing: the card would
                    # assert verbatimness about somebody else's text.
                    #
                    # Thirty-one such cases: a cell pattern beginning
                    # "SPI · …" matched a prose bullet that happened to
                    # mention SPI.
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
    print(f"registry files: {sum(1 for _ in FC.rglob('*.md'))}")
    print(f"claim units: {vsjogo}; with evidence: {z_dokazom}")
    if "-v" in sys.argv:
        print("\nwhat each evidence covered:")
        for (prokhid, nazva), ids in sorted(pokryttya.items(),
                                           key=lambda kv: kv[0][1]):
            print(f"  {len(ids):>3}×  {nazva}  ({prokhid})"
                  f"\n        {', '.join(ids)}")
    # Evidence that matched nothing is either a wording that has since
    # changed in the book or a fault in the pattern. It must not go
    # unmentioned: the registry would begin promising a checkedness it
    # does not have.
    #
    # Different from evidence that matched a claim but lost to something
    # stronger. That is normal and even the goal: a weaker record from an
    # early pass ("the source is unreachable") superseded by a later
    # `verbatim` means an item of the hand-off order was closed. Such
    # cases are shown separately and without alarm.
    holosti = [z for z in dokazy if klyuch(z) not in zachepleni]
    perekryti = [z for z in dokazy
                 if klyuch(z) in zachepleni
                 and klyuch(z) not in pokryttya]
    if holosti:
        print(f"\n⚠ evidence matching nothing: {len(holosti)}")
        for z in holosti:
            print(f"    {nazva_zapysu(z)}  ({z.get('_prokhid')})")
    if perekryti:
        print(f"\nsuperseded by stronger evidence: {len(perekryti)}")
        for z in perekryti:
            print(f"    {nazva_zapysu(z)}  "
                  f"({z.get('_prokhid')}, клас {class_letter_of(z, '?')})")

    # Auditing individual alternatives. Two faults invisible above:
    #
    #   dead  — the alternative matched nothing while its neighbour did,
    #           so the evidence looks healthy;
    #   wide  — the alternative matched more units than the evidence
    #           asserts anything about.
    #
    # Both understate or overstate coverage silently, and no check fails
    # on them. So this is a report, not a gate: only somebody who can see
    # the quote can judge whether 12 matches is too wide.
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
                # An alternative torn out of its context may be an
                # invalid pattern in itself — that is not a fault of the
                # evidence.
                continue
            n = sum(1 for x in usi_teksty if r.search(x))
            if n == 0:
                mertvi.append((z, ch, prychyna(ch, usi_teksty)))
            elif n >= SHYROKA_ALTERNATYVA:
                shyroki.append((z, ch, n))
    if mertvi:
        print(f"\n⚠ alternatives with no match at all: {len(mertvi)}")
        for z, ch, ch_prychyna in mertvi:
            print(f"    {nazva_zapysu(z)}  ({z.get('_prokhid')})"
                  f"\n        ↳ {ch}"
                  f"\n          ({ch_prychyna})")
    if shyroki and "-v" in sys.argv:
        print(f"\nalternatives with {SHYROKA_ALTERNATYVA}+ matches: "
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
    # Code blocks are context, not claims: percentages are computed over
    # claims, or the denominator is inflated by things nobody intended to
    # check.
    vsjogo = len(zapysy) - kontekst
    print(f"\nclaim units: {vsjogo}"
          f"  (+ {kontekst} code blocks as context)\n")
    zvireno = sum(c[k] for k in ("verbatim", "derived", "arithmetic"))
    for stan in STATUSES_OF_UNITS:
        n = c.get(stan, 0)
        if not n:
            continue
        print(f"  {stan:<20} {n:>5}  {n*100/vsjogo:5.1f}%   {STATUSES[stan]}")
    print(f"\n  checked against a source or by calculation "
          f"(verbatim + derived + arithmetic): "
          f"{zvireno} ({zvireno*100/vsjogo:.1f}%)")
    # `self-consistent` is deliberately **outside** this figure and
    # deliberately on its own line.
    #
    # Outside, because it says nothing about the world: a book that agrees
    # with itself may be wrong in both places at once. Separate, because
    # `no-external-signal` also says nothing about the world — but that
    # one means "no check was made", while this one means "a check was
    # made, mechanically and reproducibly, and it agreed". Merging them
    # throws away the only thing measured here.
    if c.get("self-consistent"):
        print(f"  self-consistent, no external confirmation "
              f"(self-consistent): "
              f"{c['self-consistent']}")
    print(f"  closed as a decision (no-external-signal): "
          f"{c.get('no-external-signal', 0)}")
    print(f"  still open (named-unreachable + unchecked + refuted): "
          f"{sum(c.get(s, 0) for s in ('named-unreachable', 'unchecked', 'refuted'))}")
    # by file: where the most open units are
    per = Counter()
    for z in zapysy:
        if z["status"] in ("named-unreachable", "unchecked", "refuted"):
            per[z["fajl"]] += 1
    if per:
        print("\n  most open units by file:")
        for f, n in per.most_common(8):
            print(f"    {n:>4}  {f}")
    return 0


def stale() -> int:
    """Has the registry drifted from the book — and in what way.

    ## What was here before

    The docstring promised "records whose text in the book has changed".
    The body checked **whether the file exists**. About the text, not a
    line.

    Because of that the registry lagged the book silently for four days:
    six corrections to a printed edition moved no counter, and the gate
    said "no divergences" throughout. It was found by somebody writing
    the check from scratch, precisely because they did not believe it did
    not already exist.

    > That was the second case of the same kind in one day (the first: a
    > gate promising two checks and performing one). Both survived a long
    > time for the same reason: **a counter showing zero looks the same
    > when all is well and when it is counting nothing.**

    ## What is here now

    The book is decomposed by the same splitter and hash that build the
    registry, and the result is compared with what lies on disk. A shared
    splitter here is not an economy but a requirement: a private copy of
    the decomposition would drift
    from the generator, and the check would begin confirming itself.

    Three kinds of divergence, and they differ in cost:

    · **the text changed** — evidence bound to the old wording is no
      longer about this claim. Expensive: quietly false evidence.
    · **gone / appeared** — an edit added or removed a claim.
    · **the line shifted** — the same text, only the number moved. Cheap
      in itself, expensive through trust: anybody taking `src:line` from
      the registry gets an address that may be off.
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

    print(f"  text changed       {len(zminyly)}")
    for ident, rel in zminyly[:20]:
        print(f"     ✗ {ident}  {rel}")
    print(f"  records gone       {len(znykly)}")
    for ident in znykly[:10]:
        print(f"     ✗ {ident}")
    print(f"  new units          {len(novi)}")
    for ident in novi[:10]:
        print(f"     + {ident}")
    print(f"  line-number shift  {sum(zsuv.values())} across "
          f"{len(zsuv)} files")
    for rel, n in zsuv.most_common(6):
        print(f"     ~ {n:>4}  {rel}")

    if zminyly or znykly or novi or zsuv:
        print("\n  the registry lags the book — run `factcheck.py sketch` "
              "before working")
    else:
        print("  the registry matches the book unit for unit")
    return 0
    return 0


NARYAD = FC / "reports" / "UNREACHABLE-SOURCES.md"


def blocked() -> int:
    """The hand-off order: everything blocked on a source out of reach.

    `named-unreachable` is not "we did not check" but "checking is
    impossible from here". The difference is the important one: the first
    is closed by work here, the second is never closed however much work
    is done, and must travel to another environment.

    So this command does not merely count but **writes a document** fit
    to give to somebody with open access: the source, how many claims
    depend on it, what exactly to look for in it, and which claims of the
    book it will close. All the preparation is already done — what remains
    is to open the document.
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
        # This is **not** an evidence record but a local grouping
        # dictionary. Same word, different schema — and that is exactly
        # why the field-name migration touched it: a string replacement
        # renamed three **reads** while leaving the one literal that
        # creates the key unchanged. This command died with a `KeyError`
        # for several commits, because it is in neither the gate nor any
        # baseline.
        g = grupy.setdefault(u, {"look_for": set(), "tverdzhennya": []})
        if sh:
            g["look_for"].add(sh.strip())
        g["tverdzhennya"].append((z["id"], z["src"], txt))

    if not grupy:
        print("no named-unreachable records")
        return 0

    vsjogo = sum(len(g["tverdzhennya"]) for g in grupy.values())
    ryadky = [
        "# Hand-off: sources unreachable from this environment\n",
        "> **generated** — `factcheck/tools/factcheck.py blocked`; editing "
        "it by hand is wasted work\n",
        "**This is not a list of errors.** It is a list of the book's "
        "claims that cannot be checked against a primary source from the "
        "container the book is made in: the egress policy answers `403` "
        "for vendor and standards domains.\n",
        "Every item is prepared for closing: the source named, what to "
        "look for in it, and which claims of the book depend on it. "
        "Somebody with open access has only to open the document and "
        "check — the work is measured in minutes per source.\n",
        "Closed items come back as `verbatim` or `derived` evidence in "
        "`factcheck/evidence/`, after which this file is regenerated and "
        "gets shorter.\n",
        f"As generated: **{vsjogo}** claims from **{len(grupy)}** "
        f"sources.\n",
        "---\n",
    ]
    for u, g in sorted(grupy.items(), key=lambda kv: -len(kv[1]["tverdzhennya"])):
        ryadky.append(f"## {u}\n")
        ryadky.append(f"Claims depending on it: "
                      f"**{len(g['tverdzhennya'])}**\n")
        if g["look_for"]:
            ryadky.append("**What to look for:**\n")
            for s in sorted(g["look_for"]):
                ryadky.append(f"- {s}")
            ryadky.append("")
        ryadky.append("| Claim | Where in the book | Verbatim |")
        ryadky.append("|---|---|---|")
        for ident, src, txt in g["tverdzhennya"]:
            t = txt.replace("|", "\\|")[:160]
            ryadky.append(f"| `{ident}` | `{src}` | {t} |")
        ryadky.append("\n---\n")
    NARYAD.write_text("\n".join(ryadky), encoding="utf-8")

    print(f"\n{NARYAD.relative_to(ROOT)}: {vsjogo} claims from "
          f"{len(grupy)} sources\n")
    for u, g in sorted(grupy.items(), key=lambda kv: -len(kv[1]["tverdzhennya"])):
        print(f"  {len(g['tverdzhennya']):>4}   {u}")
    return 0


# Signs by which a claim can be checked against an external source at
# all. The weight is how expensive an error in that particular sign is.
#
# This table is this book's data — addresses, pins, API calls, part
# numbers. Another book replaces it; what travels is the shape.
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
    """Open claims, most expensive first.

    A pass should not walk the book in order: a unit reading "if this
    book has one chapter" and a unit reading "GPIO 6–11 are wired to the
    flash" do not cost the same. The queue puts first what costs a board
    when wrong.
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
    print(f"\nopen claims carrying checkable signs: {len(poz)}"
          f"  (showing {min(mezha, len(poz))})\n")
    for v, ident, fajl, chym, txt in poz[:mezha]:
        print(f"  [{v:>2}] {ident:<12} {chym:<28} {txt}")
    return 0


def shukaty() -> int:
    """`factcheck.py shukaty <substring>` -> the sha and the claim text.

    Evidence is keyed by hash, and nobody keeps a hash in mind. This
    command is the bridge between "I remember the wording" and "I know the
    key to record it under".
    """
    if len(sys.argv) < 3:
        print("give a substring")
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
        print("not found")
    return 0


def vorota() -> int:
    """The registry's outbound gate.

    What is checked here, and what is deliberately absent.

    **Present:** no claim in the `refuted` status. That means "the
    source refuted it" — a book carrying such a record contradicts itself,
    and must not be released under any circumstances.

    **Present:** no evidence that matched nothing. Such evidence is
    either a wording that has since changed in the book or a fault in the
    pattern; in both cases the registry promises a checkedness it does not
    have.

    **Absent:** any requirement of "zero unchecked". Deliberately. The
    registry decomposes the book into thousands of units, among them
    editorial judgements and advice for which no external source is needed
    or exists. A requirement of zero would force closing them fictitiously
    — making the registry worse, not better.
    The rule instead is: `unchecked` is visible and counted, and
    `named-unreachable` has a hand-off order.
    """
    dokazy = zavantazhyty_dokazy()
    g = [z for z in dokazy if status_of(z) == "refuted"]
    for z in g:
        print(f"   ✗ refuted claim: {nazva_zapysu(z)} "
              f"({z.get('_prokhid')})")

    # The docstring's second promise, which was **not here**: evidence
    # that matched no unit at all.
    #
    # Found by an external review: the description spoke of two checks and
    # the implementation performed one. That is worse than a missing
    # check — a reader of the contract believes the invariant is guarded,
    # and it is guarded by nobody.
    #
    # The rule that follows: **every invariant must have exactly one
    # authoritative checker, and a description is not a checker.**
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
            print(f"   ✗ pattern does not compile: {nazva_zapysu(z)} "
                  f"({z.get('_prokhid')}) — {e}")
            holosti.append(z)
            continue
        if not any(rx.search(t) for t in teksty):
            holosti.append(z)
            print(f"   ✗ evidence matched nothing: {nazva_zapysu(z)} "
                  f"({z.get('_prokhid')})")

    print(f"factcheck gate: refuted {len(g)}, "
          f"evidence matching nothing {len(holosti)}")
    return 1 if (g or holosti) else 0


def vzirets() -> int:
    """How many registry units this pattern will match.

        factcheck/tools/factcheck.py vzirets '<regular expression>'

    ## Why a separate command for three lines of code

    Because without it people check against **the wrong corpus** — done
    three times in one evening by somebody who knew about the trap and had
    written it down.

    A pattern is matched against **the text of a registry unit**, not
    against the book's markup. For prose these are the same, which is
    exactly why the mistake does not catch the eye. For a table cell they
    are not:

        the book:      | Frequency | 160–240 MHz | 16 MHz | 133 MHz |
        the registry:  Frequency · RP2040 → 133 MHz

    A pattern written against the book's row matches the book and
    **matches nothing** in the registry. A `grep` over the book's
    directory says "all is well", and the evidence quietly touches
    nothing.

    The same trap nearly caused 124 sound records to be deleted, because
    somebody wrote a faster check over the book's text. The rule was
    already written down. The rule turned out not to be enough: as long
    as
    doing it right cost more than a `grep`, the `grep` won every time.

    Hence this command. Now the right thing is cheaper than the wrong
    one.
    """
    if len(sys.argv) < 3:
        print("usage: factcheck/tools/factcheck.py vzirets '<expression>'")
        return 2
    vyraz = sys.argv[2]
    try:
        rx = re.compile(vyraz)
    except re.error as e:
        print(f"invalid expression: {e}")
        return 2

    zbihy: list[tuple[str, str]] = []
    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            for _vyd, txt, _ln in rozbyty(f.read_text(encoding="utf-8")):
                if rx.search(txt):
                    zbihy.append((f.name, txt))

    print(f"units matched by the pattern: {len(zbihy)}")
    if not zbihy:
        print("  ⚠ IDLE — not one unit. Evidence with such a pattern "
              "checks nothing.")
        return 1
    if len(zbihy) > 12:
        print("  ⚠ TOO WIDE? A wide pattern is more dangerous than a "
              "missing one: it silently marks as checked what it never "
              "checked.")
    for imya, txt in zbihy[:12]:
        print(f"    {imya}: {txt.strip()[:88]}")
    if len(zbihy) > 12:
        print(f"    … and {len(zbihy) - 12} more")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    return {"sketch": sketch, "status": status, "stale": stale,
            "blocked": blocked, "cherga": cherga, "vorota": vorota,
            "shukaty": shukaty, "vzirets": vzirets}.get(cmd, status)()


if __name__ == "__main__":
    sys.exit(main())
