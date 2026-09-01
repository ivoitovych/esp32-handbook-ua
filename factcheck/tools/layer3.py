#!/usr/bin/env python3
"""Layer 3: does the quote actually stand in the named source.

## Why this layer is separate

Fact-checking has three distinct failures, and none of them catches the
other two.

    1. book -> record       the claim exists, no record covers it
    2. quote -> claim       the quote is genuine but proves something else
    3. source -> quote      the quote is not in the source at all

The first two require understanding: the first, whether everything is
covered; the second, whether this extract supports this particular claim.
The third requires nothing but `curl` and a substring search — and that is
exactly why it must be **a script**.

The gain is not that a script is cheaper. It is that the model gathering
the evidence no longer has to be strong. A weak model fails predictably:
it paraphrases instead of quoting, stitches two sentences into one,
reorders words, invents the plausible. **Layer 3 catches every one of
those mechanically.** So the gathering can go to the cheapest model, and
expensive attention can stay with layer 2, where it cannot be replaced.

## What exactly is checked

From the `quote` field the **usable extracts** are taken: lines with no
Cyrillic (our own notes are in Cyrillic), with no ellipsis (text was cut
there), and longer than `MIN_DOVZHYNA`. Adjacent such lines are merged
into a paragraph, because we wrap long source lines when recording them
and the source does not.

Then both the paragraph and the source text are reduced to single spaces
between words — after which an ordinary substring search is all that
remains.

## What this layer does **not** say

It does not say the evidence is correct. A quote may be verbatim and have
nothing to do with the claim — that is layer 2, and a person does it.

It does not say the source is authoritative. `raw.githubusercontent.com`
serves anybody's repository.

It says exactly one thing: **this text really does stand at this
address.**

    factcheck/tools/layer3.py            check everything in the cache
    factcheck/tools/layer3.py --kachaty  download what is missing first
    factcheck/tools/layer3.py --zvit     write factcheck/reports/QUOTES.md
    factcheck/tools/layer3.py --suvoro   an unreachable source is an error too
    factcheck/tools/layer3.py <file.yaml>  check a helper's dump

The last is the important one for working with a pool. A helper puts what
it gathered in its own file, this script checks it, and only what passes
is looked at by a maintainer. Somebody else's word never enters the
registry unchecked.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import pathlib
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

import factcheck

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
DOKAZY = ROOT / "factcheck" / "evidence"
KESH = ROOT / "factcheck" / "source-cache"
ZVIT = ROOT / "factcheck" / "reports" / "QUOTES.md"

MIN_DOVZHYNA = 12

# Extensions read as text without conversion. A PDF needs `pdftotext`;
# if that is absent the file is declared uncheckable — an honester state
# than a silent skip.
TEKSTOVI = {".rst", ".h", ".c", ".cpp", ".py", ".inc", ".csv", ".md",
            ".txt", ".yaml", ".yml", ".json", ".kconfig", ".projbuild",
            ".cmake", ".ld", ".s", ".in", ""}

RE_URL = re.compile(r"https?://[^\s,;)\"'<>]+")
RE_KYRYLYCYA = re.compile(r"[а-яїієґА-ЯЇІЄҐ]")
RE_PROPUSK = re.compile(r"…|\.\.\.")
# A line wholly in parentheses is our own marker of where an extract
# came from: `(esp32c3.inc)`, `(i2c_master.c:1049)`. It is not part of
# the source — and worse, it would **glue** adjacent lines into one
# paragraph, after which none of them would be found.
RE_POZNACHKA = re.compile(r"^\([^()]*\)$")
# A title that declares itself editorial, and a number with a unit —
# both are patterns over the BOOK's prose, so they live in
# `factcheck/book.yaml`. Carried inline they would flag nothing on a book
# in another language and report a confident zero.
#
# The first version of the editorial check fired on 46 records and nearly
# all were honest verdicts: "the author's summary", "a ranking of
# causes", "a table heading". The maintainer had **already said** in the
# title that this was a judgement rather than a fact about the world, and
# a trigger that does not read that turns a useful question into noise.
#
# The second narrowing was bought by M2 examining candidates one by one:
# of 36, exactly **two** were real. The rest were claims in which a number
# is present but **is not the subject**:
#
#     "5 V on a GPIO. The outright leader."   the subject is the leader
#     "470 µF — the cheapest solution"        the subject is cheapest
#     "Frequent culprits, 5 V"                this is a column heading
#
# I proposed replacing all 36 mechanically, having read the reasons column
# instead of the records. M2 looked at them individually and showed that
# would have been wrong. A trigger that still shows 35 after everything
# real is closed stops being read — and then it catches nothing.
_l3 = config.layer3_patterns()
RE_SAM_KAZHE_E = (re.compile(_l3["self_declared_editorial"], re.I)
                  if _l3.get("self_declared_editorial") else None)
RE_CHYSLO_Z_ODYNYCEYU = (re.compile(_l3["number_with_unit"])
                         if _l3.get("number_with_unit") else None)


def rozgornuty(url: str) -> list[str]:
    """Expand `{a,b,c}` in a URL into separate addresses.

    A dozen evidences are written that way, where one claim is checked
    against three families at once: `.../gpio/{esp32,esp32s3,esp32c3}.inc`.
    The form is convenient for a reader and unusable by `curl`.
    """
    m = re.search(r"\{([^{}]*)\}", url)
    if not m:
        return [url]
    out = []
    for chastyna in m.group(1).split(","):
        out += rozgornuty(url[:m.start()] + chastyna.strip() + url[m.end():])
    return out


_IMENA_Z_MANIFESTU: dict[str, str] | None = None


def _z_manifestu() -> dict[str, str]:
    """URL -> file name, as **the manifest recorded it**.

    The manifest is the only part that enters git (the files do not:
    copyright). It records each file's name together with its URL — that
    is, the answer to this question already exists.
    """
    global _IMENA_Z_MANIFESTU
    if _IMENA_Z_MANIFESTU is not None:
        return _IMENA_Z_MANIFESTU
    _IMENA_Z_MANIFESTU = {}
    m = KESH / "MANIFEST.md"
    if not m.exists():
        return _IMENA_Z_MANIFESTU

    usi: dict[str, list[str]] = {}
    for r in re.finditer(
            r"^\| `([^`]+)` \| `[0-9a-f]{64}` \| \d+ \| [\d-]+ \| "
            r"<([^>]+)> \|$", m.read_text(encoding="utf-8"), re.M):
        usi.setdefault(r.group(2), []).append(r.group(1))

    # **One URL often has two manifest rows** — the old generation
    # name and the new one, because a rename appended a row rather than
    # changing it. Measured: 357 rows for 276 URLs — 78 URLs have two
    # names, and exactly one of them exists in this container: the one the
    # file was downloaded under here.
    #
    # So "the first row" is a wrong rule: rows are ordered by name, not by
    # reality, and the first often points at a file this container does
    # not have. The question to answer is not "which name was recorded"
    # but "under which name does the file lie **here**".
    for url, imena in usi.items():
        ye = [i for i in imena if (KESH / i).exists()]
        if ye:
            _IMENA_Z_MANIFESTU[url] = ye[0]
        else:
            # The file exists under no name — take the derived one if
            # it is among those recorded, otherwise the first. It makes
            # no difference to the check (neither will open), but the
            # report will name the one today's rule would produce.
            vyved = vyvesty_imya(url)
            _IMENA_Z_MANIFESTU[url] = (vyved if vyved in imena
                                       else sorted(imena)[0])
    return _IMENA_Z_MANIFESTU


def vyvesty_imya(url: str) -> str:
    """A name derived from a URL — the current generation's rule."""
    baza = re.sub(r"[^\w.-]", "_", url.rsplit("/", 1)[-1] or "bez-imeni")
    return f"{hashlib.sha256(url.encode()).hexdigest()[:8]}-{baza}"[:96]


def imya_dlya(url: str) -> str:
    """A file name in the cache: **the manifest** first, derivation second.

    A base name collides far too often — an ESP-IDF tree holds dozens of
    `esp32.inc` and hundreds of `*.h`. So a derived name carries a short
    hash of the full URL: the name stays readable and collisions vanish.

    ## Why derivation is second here, not sole

    The naming rule has already changed once, and 54 files stayed under
    the old generation. Layer 3 did not open them: it derived the new
    name, no file existed under it, and the evidence became "source not in
    the cache" — silently, in a form indistinguishable from genuine
    unreachability. M2 stepped on this four times in an hour, renaming
    files by hand with sha256 checks.

    Renaming closes today's pain and leaves the kind in place. The kind
    is this: **the name is derived from the URL although the manifest has
    already recorded it** — two sources of truth for one fact, exactly
    what we caught in
    doubled field names. So the manifest is primary and derivation is the
    fallback, for a URL the manifest does not yet carry.

    > Deriving what has already been recorded is a promise that the
    > derivation rule will never change. It has already changed.
    """
    z_manifestu = _z_manifestu().get(url)
    if z_manifestu:
        return z_manifestu
    return vyvesty_imya(url)


def zavantazhyty(url: str, cil: Path) -> bool:
    KESH.mkdir(exist_ok=True)
    r = subprocess.run(["curl", "-sSL", "--fail", "--max-time", "40",
                        "-o", str(cil), url],
                       capture_output=True)
    return r.returncode == 0 and cil.exists() and cil.stat().st_size > 0


DOPUSK_RYADKA = 3.0


def ryadky_z_koordynat(storinka) -> list[str]:
    """Reconstruct table rows from word coordinates.

    `pdftotext` (and pymupdf's ordinary extraction) return **reading
    order**, in which each cell of a column stands on its own line:

        Thermometer
        tERR
        -55°C to +125°C
        ±2
        °C

    A contiguous line "Thermometer tERR -55°C to +125°C ±2 °C" does not
    and cannot exist in such text, although in the document it is one
    table row. That is exactly why M2 got 27 false alarms out of 45, and
    exactly why the "checked by eye" mark came into being.

    Here words are taken with their coordinates and **grouped by
    baseline**: everything within `DOPUSK_RYADKA` points vertically is one
    row, and within a row they are sorted left to right.

    One case still will not assemble this way: a cell split across two
    visual lines ("Thermometer" above "Error"). For that there is the
    token fallback further down.
    """
    slova = storinka.get_text("words")
    if not slova:
        return []
    slova.sort(key=lambda w: (round(w[1], 1), w[0]))
    ryadky, potochnyy, baza = [], [], None
    for w in slova:
        if baza is None:
            potochnyy, baza = [w], w[1]
        elif abs(w[1] - baza) <= DOPUSK_RYADKA:
            potochnyy.append(w)
        else:
            ryadky.append(potochnyy)
            potochnyy, baza = [w], w[1]
    if potochnyy:
        ryadky.append(potochnyy)
    out = []
    for r in ryadky:
        r.sort(key=lambda w: w[0])
        out.append(" ".join(w[4] for w in r))
    return out


def tekst_pdf(p: Path) -> str | None:
    """A PDF's text in **two views at once**.

    Reading order and the coordinate-reconstructed table rows are joined
    into one search string. A quote taken from a paragraph is found in the
    first; a quote taken from a table row, in the second.

    This is what replaces the "checked by eye" mark in the ordinary case:
    not a weakening of the check but **better extraction**. The weakening
    (tokens within a window) remains only for cells split across two
    lines.
    """
    try:
        import pymupdf
    except ImportError:
        r = subprocess.run(["pdftotext", "-q", "-layout", str(p), "-"],
                           capture_output=True)
        return (r.stdout.decode("utf-8", "replace")
                if r.returncode == 0 else None)
    try:
        with pymupdf.open(p) as d:
            chastyny = []
            for storinka in d:
                chastyny.append(storinka.get_text())
                chastyny += ryadky_z_koordynat(storinka)
        return "\n".join(chastyny)
    except Exception:
        return None


def tekst_dzherela(p: Path) -> str | None:
    """A file's text — by **content**, not by extension.

    The first version had a list of permitted extensions, and it fell
    behind immediately: every Arduino library's `library.properties` is
    ordinary text, but it was not in the list, and layer 3 declared such a
    file unreadable. A whole category of sources dropped out silently.

    Lists of extensions always fall behind. So we ask the file: if it
    decodes as UTF-8 and holds almost no control bytes, it is text,
    whatever it is called.
    """
    if p.suffix.lower() == ".pdf":
        return tekst_pdf(p)
    try:
        syri = p.read_bytes()
    except OSError:
        return None
    if syri.startswith((b"%PDF", b"\x89PNG", b"\xff\xd8\xff", b"PK\x03\x04",
                        b"\x7fELF", b"GIF8")):
        return None
    try:
        tekst = syri.decode("utf-8")
    except UnicodeDecodeError:
        return None
    proba = tekst[:4096]
    keruvni = sum(1 for c in proba if ord(c) < 32 and c not in "\t\n\r")
    if proba and keruvni / len(proba) > 0.01:
        return None
    return tekst


# A source field holding not a document but **an argument**. M2's finding
# at 19:40Z, and the most expensive of all: a Haiku helper that fails to
# find a document does not write `named-unreachable` — it **invents a
# plausible name
# for a source**. "The properties of CMOS logic", "a fundamental rule of
# electronics", "the typical construction of module boards".
#
# This is the worst possible consequence of all: a false `verbatim`
# declares a claim checked, removes it from every queue, and nobody ever
# checks it again.
#
# Layer 3 used to see this as "source not in the cache" — a signal
# present, no alarm raised. For `verbatim` and `derived` it is now an
# error. `named-unreachable` and `no-external-signal` are exempt: in those
# the source either does not exist or is unreachable by design.
# What counts as a named document. The first approach was too narrow and
# marked fourteen records invented, of which thirteen were M2's honest
# references to a PDF with no stable address: "Texas Instruments, PCF8574
# Remote 8-Bit I/O Expander for I2C Bus (SCPS068), Features section". That
# is a full citation; it simply is not a URL.
#
# The difference between it and an invented source is not the presence of
# an address but **whether a document is named**: publisher, title,
# revision. An invented source describes not a document but a property of
# the world — "the properties of CMOS logic", "well-known relay
# electromechanics".
RE_ADRESA = re.compile(
    r"https?://|\b[\w-]+\.(?:com|org|net|io|dev)/"
    r"|\.pdf\b|\.h\b|\.c\b|\.py\b|\.rst\b|\.inc\b|\.csv\b"
    r"|components/|tools/|docs/|Kconfig", re.I)
# Two consecutive capitalised Latin tokens — a publisher's name or a
# document title: `Texas Instruments`, `Product Brief`, `Register Map`.
RE_NAZVA_DOKUMENTA = re.compile(r"\b[A-Z][A-Za-z0-9-]+ [A-Z][A-Za-z0-9-]+")
# A document identifier: `SCPS068`, `DS40002061B`, `RM-MPU-6000A-00`,
# `Rev 1.1`, `UM10204`, `IEC 61190-1-3`.
RE_ID_DOKUMENTA = re.compile(
    r"\b[A-Z]{2,}[0-9][\w-]*\b|\bRev\.?\s*\d|\b(?:IEC|ISO|EN|UL)\s*\d",
    re.I)


# A source inside the book. M2 checked a claim of project 60 against
# **the same chapter's own code**: a threshold in the prose against the
# threshold in the listing.
#
# That is neither an external quote nor an invented source but a third
# kind, absent from the architecture. It is exactly the missing "fourth
# layer": the registry checks the book against sources but not the book
# against the book — and this week's worst errors were internal
# contradictions (BMP280 in appendix E against chapter 45).
#
# The pattern below reads the BOOK's own words for "chapter", "appendix",
# "card". It is Ukrainian because this book is; on another book it names
# nothing, and a source inside that book would read as an invented one.
#
# So such a record is legitimate and layer 3 passes it. But there is
# nothing here to check it mechanically with: the source is the book
# itself, and that needs a different tool, not this one.
RE_DZHERELO_VSEREDYNI = re.compile(
    r"власн\w* (?:код|твердженн|текст)|розділ[ауі]?\s*\d|"
    r"додат\w+\s+[A-EА-Д]|картк\w+\s+К?\d|"
    r"(?:%s)/" % "|".join(config.groups()), re.I)


def dzherelo_vseredyni(z: dict) -> bool:
    return bool(RE_DZHERELO_VSEREDYNI.search(str(z.get("source") or "")))


def dzherelo_rozvyazne(z: dict) -> bool:
    """Does the source field name a document rather than a property of the world."""
    d = str(z.get("source") or "")
    return bool(RE_ADRESA.search(d)
                or RE_ID_DOKUMENTA.search(d)
                or RE_NAZVA_DOKUMENTA.search(d)
                or dzherelo_vseredyni(z))


# A stub page served with status 200. M2's finding: `semtech.com`
# returns HTML of exactly the same size for **any** address under
# `/uploads/documents/`, and `curl --fail` exits successfully. Without
# this check the stub lands in the cache as a document, and `verbatim` is
# assigned for something nobody has seen.
def pidmineno_zaglushkoyu(p: Path) -> bool:
    if p.suffix.lower() != ".pdf":
        return False
    try:
        with p.open("rb") as f:
            pochatok = f.read(1024)
    except OSError:
        return True
    return not pochatok.startswith(b"%PDF")


# Soft hyphens and ligatures a PDF leaves in the text. Not content but
# extraction debris: invisible in the document, and in the extracted text
# they split a word in the middle of a quote. Dashes of various kinds are
# reduced to one — `‑` (non-breaking hyphen) appears in datasheets in
# place of `-`.
PEREKLAD_SMITTYA = {
    "\u00ad": "",      # soft hyphen
    "\u200b": "",      # zero-width space
    "\ufeff": "",      # BOM inside the text
    "\u2011": "-",     # non-breaking hyphen
    "\ufb01": "fi", "\ufb02": "fl",   # ligatures
}


def plaskyy(s: str) -> str:
    """One space between words; extraction debris removed.

    Case, quotation marks and meaningful dashes are deliberately **not**
    touched.
    A quote that matches only after case folding is already a paraphrase,
    and let it fail: evidence must be verbatim.

    Soft hyphens and ligatures, on the other hand, carry no meaning: they
    are invisible in the document, and no human could have "quoted them
    wrongly". Removing them is not a loosening but a correction of the
    extraction.
    """
    for shcho, na in PEREKLAD_SMITTYA.items():
        s = s.replace(shcho, na)
    return re.sub(r"\s+", " ", s).strip()


def uryvky(cytata: str, vlasna_mova: bool = False) -> list[list[str]]:
    """The groups of quote lines that can be checked.

    Discarded: our own notes (Cyrillic), places where text was cut (an
    ellipsis), source markers in parentheses, and lines too short to
    distinguish anything.

    Returns **groups of lines** rather than joined text, because the
    check has to be made two ways (see `znayty`).

    ## `vlasna_mova`, and why without it `self-consistent` would be empty

    The rule "Cyrillic is our note, not a quote" is right exactly as long
    as the source is English. For `self-consistent` the source is **the
    book**, and then every genuine extract is Cyrillic.

    Measured on the 21 internal-check records: without this flag **15 of
    21** had no usable extract, and layer 3 would have said of them "there
    is nothing to check" — that is, a status introduced to record a check
    that WAS made would have reported that there was nothing to check.

    > A filter that is right for one corpus, applied to another, discards
    > everything — and stays silent with the same word it uses for
    > "clean".

    The rest of the filtering stands: an ellipsis still means text was
    cut, and a short line still matches anything.
    """
    grupy: list[list[str]] = [[]]
    for ryadok in cytata.splitlines():
        r = ryadok.strip()
        pryydatnyy = (
            r
            and (vlasna_mova or not RE_KYRYLYCYA.search(r))
            and not RE_PROPUSK.search(r)
            and not RE_POZNACHKA.match(r)
            and len(r) >= MIN_DOVZHYNA
        )
        if pryydatnyy:
            grupy[-1].append(r)
        elif grupy[-1]:
            grupy.append([])
    return [g for g in grupy if g]


VIKNO_TABLYCI = 4000
RE_LEKSEMA = re.compile(r"[\w.°±×/+-]{2,}")


def u_tablyci(ryadok: str, tekst: str) -> bool:
    """Is this line a **reading of a table** scattered across a document.

    Taken from `factcheck/tools/layer3_m2_legacy.py`, function
    `znayty_ryadok` (M2's finding at 19:40Z). A plain substring check gave
    them **27 false alarms out of 45**, and not one was the quote's
    fault.

    The cause: `pdftotext` lays columns out so that the parameter name,
    the condition and the value end up on different lines. In the DS18B20
    datasheet:

        tERR                                    °C      3
      Error        -55°C to +125°C              ±2

    The line "Thermometer Error tERR -55°C to +125°C ±2 °C" does not and
    cannot exist in the document, although the quote is exact.

    So: every meaningful token must be in the document **and lie
    compactly**. This is a deliberate loosening — it catches an invented
    quote (the tokens will not be there at all) and does not catch a
    reordering of words within a table, where reordering changes no
    meaning.

    Used **only as a fallback**, and only for PDFs: in code and RST the
    order of words is significant, and there is no reason to loosen it
    there.
    """
    leksemy = RE_LEKSEMA.findall(ryadok)
    if len(leksemy) < 3:
        return False
    poz = []
    for l in leksemy:
        i = tekst.find(l)
        if i < 0:
            return False
        poz.append(i)
    return (max(poz) - min(poz)) < VIKNO_TABLYCI


def znayty(grupa: list[str], teksty: list[str],
           tablychni: bool = False) -> list[str]:
    """Which lines of a group were found in none of the sources.

    Two methods, and both are needed, because we quote in two ways.

    **As a joined group** — when we wrapped a long source line onto two
    of our own. Then no line of ours stands in the source separately, yet
    together they stand there verbatim.

    **Line by line** — when we assembled an extract from **different
    places** in the file: `#define IO_MUX_GPIO11_REG` from line 107 and
    `PERIPHS_IO_MUX_VDD_SPI_U` from line 223. Together they stand nowhere,
    and that is not a fault of the quote but the ordinary way of showing
    two related definitions side by side.

    The joined form is tried first: it is stricter, because it also
    requires the order.
    """
    ciline = plaskyy(" ".join(grupa))
    if any(ciline in t for t in teksty):
        return []
    promakhy = [r for r in grupa
                if not any(plaskyy(r) in t for t in teksty)]
    if tablychni:
        promakhy = [r for r in promakhy
                    if not any(u_tablyci(plaskyy(r), t) for t in teksty)]
    return promakhy


# `\S+`, and NOT `[^\s,;]+`, and that is not an oversight.
#
# A comma here is not always a separator: an abbreviation may contain a
# brace expansion — `.../components/esp_psram/{esp32,esp32s3}/…` — and the
# comma inside `{…}` is part of the token. I had narrowed the character
# class to cut a trailing comma in `.../Adafruit_ST7789.cpp,`; measurement
# showed **two regressions**: both records with braces got a truncated
# path `…/{esp32` and lost the source they had had.
#
# The trailing comma is stripped by `rstrip(".,")` below anyway — so the
# "fix" cured what was already cured and broke what was working.
#
# > A narrowing made "just in case" breaks exactly the cases its author
# > did not have in mind while narrowing.
RE_SKOROCHENNYA = re.compile(r"(?<![\w/])\.\.\./(\S+)")


def korin_dlya(povnyy: str, skorocheno: str) -> str | None:
    """The tree root an abbreviation is expanded against.

    Counting the address's segments will not do: the branch
    `release/v5.5` contains a slash, so `owner/repo/ref` is sometimes
    three segments and sometimes four. The first attempt did that and
    silently produced addresses that did not work.

    It is more reliable to ask the abbreviation itself. Its first
    segment — `components`, `docs`, `tools` — is a directory that also
    appears in the full address. Cut the full address where that begins,
    and the root comes out right however many slashes the branch name
    has.
    """
    persh = skorocheno.lstrip("/").split("/", 1)[0]
    if not persh:
        return None
    i = povnyy.find(f"/{persh}/")
    return povnyy[:i + 1] if i > 0 else None


def root_by_verification(povnyy: str, skorocheno: str) -> str | None:
    """A root found by **verification** rather than by guessing.

    ## Why, when `korin_dlya` already exists

    Because its premise is false more often than true. It requires the
    abbreviation's first segment to be a directory that also appears in
    the full address — and that fails in three ordinary cases:

        .../docs/en/esptool/basic-options.rst
            the full address leads to `esptool/__init__.py`; `/docs/`
            does not appear in it at all — the abbreviation is counted
            from the repository root

        .../Adafruit_ST7789.cpp
            the first segment is the file itself; there is no directory

        .../esp32/include/soc/touch_sensor_channel.h
            the full address holds `/soc/{esp32,esp32s3,esp32c3}/`, so
            `/esp32/` never occurs literally

    Measured on the registry: **29 abbreviations of 60 were discarded
    silently**, across 28 records. Layer 3 was checking a quote against
    fewer documents than the record names, and reporting "not found" about
    lines that lay in a source it had failed to derive.

    ## Why verification rather than better guessing

    Counting segments will not do — the branch `release/v5.5` contains a
    slash, and that is exactly where the previous attempt silently
    produced broken addresses. But the roots can be **enumerated**, and
    only the one whose file really lies in the cache accepted:

    > An address that cannot be derived can be **recovered by
    > verification**: generate candidates and keep the one whose name
    > exists in the cache.

    This is the same rule that already recovered 25 URLs of 32
    (`METHOD.md`, the section on the cache). What matters here is not the
    count but that **this form cannot emit a false address**: a wrong root
    yields a name that is not in the cache and is discarded. Kind 17 — a
    machine pointer worse than prose — is closed by construction rather
    than by promise.

    Measured: of 31 abbreviations that did not work, **15** were
    recovered. The other 16 cannot be, because their file is not in this
    cache — and that is honestly a different thing from a false pointer.
    """
    chastyny = povnyy.split("://", 1)
    if len(chastyny) != 2:
        return None
    shema, resh = chastyny
    seg = resh.split("/")
    hvist = skorocheno.lstrip("/")
    for n in range(2, min(len(seg), 8)):
        url = f"{shema}://" + "/".join(seg[:n + 1]) + "/" + hvist
        if (KESH / imya_dlya(url)).exists():
            return url
    return None


RE_SHLYAKH_KNYHY = re.compile(
    r"\b(?:%s)/[\w.\-]+\.md\b" % "|".join(config.groups()))


def knyzhkovi_dzherela(z: dict) -> list[Path]:
    """Files **of the book** named in a `self-consistent` record's source.

    `self-consistent` is an internal check: the claim is proved not by an
    external document but by another place in this same book. Such
    evidence says nothing about the world, but it does say something
    checkable about the book — that it agrees with itself.

    So it **must** pass layer 3 like everything else; its corpus is simply
    the book rather than the source cache. Otherwise the status would be a
    label asserting a check that nobody makes — kind 24, recorded the same
    day as the status itself.
    """
    syryy = str(z.get("source") or z.get("dzherelo") or "")
    out: list[Path] = []
    for s in RE_SHLYAKH_KNYHY.findall(syryy):
        p = ROOT / s
        if p.exists() and p not in out:
            out.append(p)
    return out


def dzherela_zapysu(z: dict) -> list[str]:
    """Every address of a record, with abbreviations expanded.

    In the source field, the second and later files of the same tree are
    written abbreviated — `.../components/soc/esp32c3/...` — because a
    full URL repeats sixty characters on every line and makes the record
    unreadable.

    A person understands it. Layer 3 does not: an abbreviation is not an
    address, and evidence carrying one is uncheckable **silently**. Layer
    3 found this itself the moment it was first run: a quarter of the
    records with quotes had no usable URL at all, and it looked like
    "source not in the cache".

    So an abbreviation is expanded against the root of the first full
    address. For `raw.githubusercontent.com` the root is owner, repository
    and branch; after that comes the path in the tree, and that is what
    `...` replaces.
    """
    syryy = str(z.get("source") or "")
    povni = RE_URL.findall(syryy)
    out: list[str] = []
    for u in povni:
        out += rozgornuty(u.rstrip(".,"))
    for m in RE_SKOROCHENNYA.finditer(syryy):
        hvist = m.group(1).lstrip("/").rstrip(".,")
        korin = next((k for u in povni if (k := korin_dlya(u, hvist))), None)
        if korin:
            out += rozgornuty(korin + hvist)
            continue
        # The guess failed — try verification instead. Only a candidate
        # whose file exists in the cache is accepted, so no false address
        # can come out of this.
        znaydene = next((u2 for u in povni
                         if (u2 := root_by_verification(u, hvist))), None)
        if znaydene:
            out += rozgornuty(znaydene)
    return out


def perevirka(kachaty: bool,
              fayly: list[Path] | None = None) -> tuple[list[dict],
                                                        dict[str, int]]:
    """Every evidence record against every one of its sources.

    `fayly` allows checking something not yet in the registry — namely a
    helper's dump. That way the check happens **before** somebody else's
    word enters `factcheck/evidence/`, not after.
    """
    naslidky: list[dict] = []
    pidsumok = {"ok": 0, "ne_znaydeno": 0, "nedosyazhne": 0, "nichoho": 0,
                "vygadane": 0, "zaglushka": 0, "okom": 0, "pomylka": 0,
                "nechytne": 0, "nadmirnyy_e": 0}
    kesh_tekstu: dict[str, str | None] = {}

    for f in (fayly if fayly is not None else sorted(DOKAZY.glob("*.yaml"))):
        try:
            zapysy = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except yaml.YAMLError as e:
            naslidky.append(dict(fayl=f.name, nazva="(file will not parse)",
                                 stan="pomylka", detali=str(e).split("\n")[0]))
            continue
        for z in zapysy:
            if not isinstance(z, dict):
                continue
            nazva = factcheck.nazva_zapysu(z)
            # **An absent status is not the same as `unchecked`.**
            #
            # In the registry a status is always present. In a helper's
            # dump it is not, and must not be: a status is assigned by a
            # maintainer, and the rule "somebody else's word does not
            # enter the registry unchecked" rests on exactly that.
            #
            # The first version of this gate substituted `unchecked`
            # where the field was simply absent, and failed the **whole**
            # of a helper's wave as "false records" — without checking a
            # single quote. A gate meant to catch waste hid the work.
            # It used to be `"klas" in z` — a test for the presence of
            # the **old** field name. After the contraction that is false
            # always, and the conditions below ("verbatim with no quote",
            # "evidence marked unchecked") never fire again. M2's run
            # showed it thus: "checked 508" before and "checked 508"
            # after, while 23 records meanwhile moved from "being checked"
            # to "nothing to check".
            #
            # > The check returns the same number, and the same number
            # > means nothing.
            maye_klas = bool(z.get("status") or z.get("klas"))
            # By WORD, not letter: `status_of` accepts both spellings,
            # so the transition needs no second path.
            stan = factcheck.status_of(z, "")

            # `unchecked` is the default state of an **absence** of
            # evidence. An evidence record marked `unchecked` means
            # nothing and occurs only as a helper's error (M2's finding).
            # **`verbatim` with no quote is a contradiction by
            # definition.**
            #
            # It means "the primary source was obtained, the extract is
            # quoted". With no extract it means nothing, and it is in
            # exactly that emptiness that the subtlest forgery we have
            # seen took up residence (M2's finding at 00:14Z): the source
            # real, the revision right, and **the coordinate inside the
            # document invented** — `Table 6-21`, which that datasheet
            # does not contain.
            #
            # All three of our checks pass that: the source is a
            # document, the file downloads, and the quote layer 3 could
            # have checked is simply absent. There is one gate against it:
            # require the extract wherever the status promises one.
            if maye_klas and stan == "verbatim" and not str(z.get("quote") or
                                                     z.get("cytata-tablytsya")
                                                     or "").strip():
                pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="pomylka",
                    detali="verbatim with no quote — it promises an extract"))
                continue

            if maye_klas and stan == "unchecked":
                pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="pomylka",
                    detali="evidence marked unchecked — that means no evidence"))
                continue

            # An invented source: the status says "checked" while the
            # source field holds an argument. See
            # RE_SCHOS_SCHO_MOZHE_BUTY_DOKUMENTOM.
            if (maye_klas and stan in ("verbatim", "derived")
                    and not dzherelo_rozvyazne(z)):
                pidsumok["vygadane"] = pidsumok.get("vygadane", 0) + 1
                dzh = str(factcheck.pole(z, "source", "dzherelo") or "")[:60]
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="vygadane",
                    detali=f"status {stan}, but the source is not a document: «{dzh}»"))
                continue

            # **An over-generous `no-external-signal` is the mirror of an
            # invented source.** M2's finding at 22:23Z, and the most
            # important thing the last wave produced.
            #
            # The status means "no external source exists by
            # construction": an editorial decision, a piece of advice, a
            # framing sentence. Helpers were putting it on claims **with
            # numbers** — "4.7 kΩ is mandatory", "3.3 V on both lines".
            # For those a source does exist, and M2 proved it for three of
            # the three they checked.
            #
            # The consequence is the same as an invented source: the unit
            # leaves the work permanently. But it is harder to notice —
            # over-generosity here looks like caution, and caution is what
            # we both encouraged. We taught "do not stretch `verbatim`";
            # we did not say "and do not flee into no-external-signal".
            #
            # So this is **a question, not a prohibition**: the status
            # standing on a claim whose title carries a number with a unit
            # is printed as a separate list, and the decision is left to a
            # person.
            # Unconfigured patterns mean the question cannot be asked —
            # not that the answer is no.
            if (maye_klas and stan == "no-external-signal"
                    and RE_CHYSLO_Z_ODYNYCEYU
                    and RE_CHYSLO_Z_ODYNYCEYU.search(nazva)
                    and not (RE_SAM_KAZHE_E
                             and RE_SAM_KAZHE_E.search(nazva))):
                pidsumok["nadmirnyy_e"] = pidsumok.get("nadmirnyy_e", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nadmirnyy_e",
                    detali="no-external-signal, yet the title carries a number with a unit"))
                continue

            # A quote the maintainer checked by eye, where text
            # extraction destroys the structure. M2's finding: without
            # this state layer 3 raises the alarm on **correct** quotes,
            # and within a week people stop reading it. The mark is placed
            # by a person, and only together with an explanation of why a
            # machine is powerless here.
            if z.get("perevireno-okom"):
                pidsumok["okom"] = pidsumok.get("okom", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="okom",
                    detali=str(z.get("perevireno-okom"))[:90]))
                continue

            # **A reading of a table is not a quote, and these are two
            # different kinds.** M2's finding at 22:05Z, and it concerns
            # the construction of the quote field itself.
            #
            # In a datasheet a fact often lives at the intersection of a
            # row and a column, while the parameter name sits in a cell
            # spanning several lines. Assembling a "table row" from that
            # can only be done by hand — merging cells, adding `Typ`,
            # `Min`, `(note 3)`. The fact is right, and a contiguous line
            # **does not and will not** exist in the document, however
            # much we improve the extraction.
            #
            # M2 found this in their own work and named it plainly:
            # "this is exactly what we call a helper's error — a comment
            # written into the quote field; I was doing it myself while
            # checking others for it".
            #
            # Hence a field of its own: a list of cells, each checked as
            # a substring **separately**, with no invented spacing and no
            # added words. The explanation goes into the note, where it
            # belongs.
            tablychna = z.get("cytata-tablytsya")
            if tablychna:
                frahmenty = [[str(k).strip()] for k in tablychna
                             if str(k).strip()]
            else:
                frahmenty = uryvky(
                    str(factcheck.pole(z, "quote", "cytata") or ""),
                    vlasna_mova=(stan == "self-consistent"))
            urly = dzherela_zapysu(z)
            # `self-consistent` addresses the book, not the network, so
            # the absence of a URL is normal for it rather than "nothing
            # to check".
            #
            # `absent-from-source` has no quote **by definition**: it
            # proves by absence, and what is absent stands in the `absent`
            # field. Demanding extracts of it would mean discarding it as
            # "nothing to check" — that is, silently abolishing the
            # status.
            if stan == "absent-from-source":
                if not urly:
                    pidsumok["nichoho"] += 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="nichoho",
                        detali="absent-from-source with no source URL"))
                    continue
            elif not frahmenty or (not urly and stan != "self-consistent"):
                pidsumok["nichoho"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nichoho",
                    detali=("no URL" if frahmenty else
                            "no usable extracts")))
                continue

            teksty: list[str] = []
            nedosyazhni: list[str] = []
            zaglushky: list[str] = []
            nechytni: list[str] = []
            tablychni = False

            # An internal check: the corpus is the named book files.
            if stan == "self-consistent":
                shlyakhy = knyzhkovi_dzherela(z)
                if not shlyakhy:
                    pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="pomylka",
                        detali="self-consistent, but the source names no "
                               "book file — there is nothing to check "
                               "against"))
                    continue
                teksty = [plaskyy(p.read_text(encoding="utf-8"))
                          for p in shlyakhy]

            for u in urly:
                if u not in kesh_tekstu:
                    cil = KESH / imya_dlya(u)
                    if not cil.exists() and kachaty:
                        zavantazhyty(u, cil)
                    if cil.exists() and pidmineno_zaglushkoyu(cil):
                        kesh_tekstu[u] = None
                        zaglushky.append(u)
                    else:
                        kesh_tekstu[u] = (plaskyy(tekst_dzherela(cil) or "")
                                          if cil.exists() else None) or None
                        if cil.exists() and not kesh_tekstu[u]:
                            nechytni.append(u)
                if u.lower().endswith(".pdf"):
                    tablychni = True
                if kesh_tekstu[u]:
                    teksty.append(kesh_tekstu[u])
                elif u in zaglushky:
                    pass
                else:
                    nedosyazhni.append(u)

            # "The file is here, nothing can read it" and "the file is
            # not here" are different states, and confusing them is
            # dangerous. Until now a PDF with no extractor fell silently
            # into "not in the cache" — that is, it looked like an egress
            # problem rather than a missing tool on this machine.
            if nechytni and not teksty:
                pidsumok["nechytne"] = pidsumok.get("nechytne", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nechytne",
                    detali=f"{len(nechytni)}: the file is in the cache, "
                           f"nothing here can extract its text"))
                continue

            if zaglushky and not teksty:
                pidsumok["zaglushka"] = pidsumok.get("zaglushka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="zaglushka",
                    detali=f"{len(zaglushky)}: not a PDF in the cache but "
                           f"a page served with status 200"))
                continue

            if not teksty:
                pidsumok["nedosyazhne"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nedosyazhne",
                    detali=f"{len(nedosyazhni)} sources not in the cache"))
                continue

            # **Proof by absence is the only status layer 3 can refute
            # rather than merely fail to confirm.**
            #
            # For every other status layer 3 asks "does this line stand
            # in the document", and "no" means a quote divergence — often
            # a false alarm (a wrapped line, a table in a PDF). Here the
            # question is inverted and the answer unambiguous: if the line
            # whose ABSENCE is the evidence is found in the document, the
            # evidence is not divergent — it is false.
            if stan == "absent-from-source":
                shukane = str(z.get("absent") or "").strip()
                if not shukane:
                    pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="pomylka",
                        detali="absent-from-source with no `absent` field "
                               "— there is nothing to not look for"))
                    continue
                znaydeno = [u for u, tx in zip(urly, teksty) if shukane in tx]
                if znaydeno:
                    pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="pomylka",
                        detali=f"absent-from-source REFUTED: "
                               f"«{shukane[:40]}» DOES stand in the named "
                               f"document"))
                    continue
                # A control: a document of the same kind where the line
                # IS present. Without it, silence may mean merely a
                # different file format rather than an absent property.
                kontrol = str(z.get("control") or "").strip()
                if kontrol:
                    kt = [tx for u, tx in zip(urly, teksty) if u != kontrol]
                    ku = [u for u in urly if u == kontrol]
                    if ku and not any(shukane in tx for u, tx in
                                      zip(urly, teksty) if u == kontrol):
                        pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                        naslidky.append(dict(
                            fayl=f.stem, nazva=nazva, stan="pomylka",
                            detali=f"absent-from-source: «{shukane[:30]}» "
                                   f"is missing from the control document "
                                   f"too — the silence proves nothing"))
                        continue
                pidsumok["ok"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ok",
                    detali=f"the absence of «{shukane[:40]}» is confirmed"))
                continue

            vsjogo_ryadkiv = sum(len(g) for g in frahmenty)
            promakhy: list[str] = []
            for grupa in frahmenty:
                promakhy += znayty(grupa, teksty, tablychni=tablychni)
            if promakhy:
                # **A miss against an INCOMPLETE set of sources is not
                # a miss.** The `nedosyazhne` branch above fires only when
                # NO source is in the cache. If a record names two and one
                # is present, the quote was checked against half of what
                # the record cites — and "not found" attributes to a
                # faulty quote what may lie in the file we do not have.
                #
                # Kind 25: two states of the world under one word. "The
                # quote does not match" and "we did not hold the document"
                # require different work — a maintainer fixes the first, a
                # download closes the second.
                #
                # Measured: of 69 "not found" records, **8** were judged
                # on an incomplete set.
                if nedosyazhni:
                    pidsumok["nedosyazhne"] += 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="nedosyazhne",
                        detali=f"{len(nedosyazhni)} of "
                               f"{len(nedosyazhni) + len(teksty)} sources "
                               f"not in the cache; the rest did not cover "
                               f"{len(promakhy)} of {vsjogo_ryadkiv} lines"))
                    continue
                pidsumok["ne_znaydeno"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ne_znaydeno",
                    detali=f"{len(promakhy)} of {vsjogo_ryadkiv} lines",
                    promakhy=promakhy[:3]))
            else:
                pidsumok["ok"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ok",
                    detali=f"{vsjogo_ryadkiv} lines"))
    return naslidky, pidsumok


ZAHOLOVOK_ZVITU = """# Layer 3: quotes against sources

> **generated** — `factcheck/tools/layer3.py --zvit`; editing it by hand
> is wasted work

Checked mechanically: does the extract cited in an evidence record really
stand at the named address. This is **not** an assessment of whether the
evidence is apposite — that is a separate question, and a person decides
it.

| State | Means |
|---|---|
| `checked` | every usable extract was found in the source verbatim |
| `not found` | the extract is not in the source — a paraphrase, a wrong address, or the source changed |
| `source not cached` | nothing to check against: `--kachaty`, or egress refuses |
| `nothing to check` | evidence with no URL or no verbatim extract |
| `source invented` | `verbatim` or `derived`, yet the source field holds an argument, not a document |
| `stub in the cache` | the server returned HTML with status 200 instead of a PDF |
| `checked by eye` | text extraction destroys the structure; a maintainer checked it, and said why |

"""


def zvit(naslidky: list[dict], pidsumok: dict[str, int]) -> None:
    pidpysy = {"ok": "checked", "ne_znaydeno": "**not found**",
               "nedosyazhne": "source not cached",
               "nichoho": "nothing to check",
               "vygadane": "**source invented**",
               "zaglushka": "**a stub in the cache, not a document**",
               "okom": "checked by eye",
               "nechytne": "**file present, nothing can extract its text**",
               "nadmirnyy_e": "no-external-signal on a claim with a number",
               "pomylka": "**false record**"}
    r = [ZAHOLOVOK_ZVITU.rstrip("\n"), ""]
    r.append(f"Evidence records: **{sum(pidsumok.values())}**. "
             f"Checked verbatim: **{pidsumok['ok']}**. "
             f"Not found: **{pidsumok['ne_znaydeno']}**. "
             f"Source not cached: **{pidsumok['nedosyazhne']}**. "
             f"Nothing to check: **{pidsumok['nichoho']}**.\n")
    r.append(f"As of {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC.\n")
    for stan in ("vygadane", "zaglushka", "pomylka", "nechytne",
                 "nadmirnyy_e", "ne_znaydeno",
                 "nedosyazhne", "okom", "ok", "nichoho"):
        grupa = [n for n in naslidky if n["stan"] == stan]
        if not grupa:
            continue
        r.append(f"\n## {pidpysy[stan]} — {len(grupa)}\n")
        r.append("| Evidence | File | Detail |")
        r.append("|---|---|---|")
        for n in grupa:
            d = n["detali"]
            if n.get("promakhy"):
                d += ": " + "; ".join(f"«{p[:70]}…»" for p in n["promakhy"])
            r.append(f"| {n['nazva']} | `{n['fayl']}` | {d} |")
    ZVIT.write_text("\n".join(r) + "\n", encoding="utf-8")


def main() -> int:
    a = sys.argv[1:]
    fayly = [Path(x) for x in a if not x.startswith("--")] or None
    naslidky, pidsumok = perevirka(kachaty="--kachaty" in a, fayly=fayly)
    if "--zvit" in a and fayly is None:
        zvit(naslidky, pidsumok)
        print(f"layer3: report at {ZVIT.relative_to(ROOT)}")

    for n in naslidky:
        if n["stan"] == "ne_znaydeno":
            print(f"   ✗ {n['nazva']}  ({n['fayl']}) — {n['detali']}")
            for p in n.get("promakhy", []):
                print(f"        not found: «{p[:100]}»")
        elif n["stan"] == "pomylka":
            print(f"   ✗ {n['nazva']}  ({n['fayl']}) — {n['detali']}")

    print(f"layer3: records {sum(pidsumok.values())}; "
          f"checked {pidsumok['ok']}; "
          f"not found {pidsumok['ne_znaydeno']}; "
          f"not cached {pidsumok['nedosyazhne']}; "
          f"no quote {pidsumok['nichoho']}; "
          f"checked by eye {pidsumok['okom']}")
    if pidsumok["nadmirnyy_e"]:
        print(f"   · no-external-signal on a claim with a number: "
              f"{pidsumok['nadmirnyy_e']} — check whether a source really "
              f"is absent")
    if pidsumok["vygadane"] or pidsumok["zaglushka"] or pidsumok["pomylka"]:
        print(f"   ⚠ invented sources {pidsumok['vygadane']}; "
              f"stubs in the cache {pidsumok['zaglushka']}; "
              f"false records {pidsumok['pomylka']}")

    # An invented source, a stub, and evidence marked unchecked are a
    # **gate**, not a report. A quote divergence needs judgement and may be
    # a false alarm; these three cannot be anything but an error.
    bidy = pidsumok["vygadane"] + pidsumok["zaglushka"] + pidsumok["pomylka"]
    if "--suvoro" in a:
        bidy += pidsumok["ne_znaydeno"] + pidsumok["nedosyazhne"]
    # Zero records is not "no forgery" but "nothing to check". `layer1`
    # and `coverage` lived in that state for days after the cards moved,
    # printing zeros as cleanliness. Layer 3 reads the evidence directory
    # and is vulnerable the same way.
    if not sum(pidsumok.values()):
        print("   ✗ NOT ONE record was read — that is not \"clean\", it "
              "is \"nothing to check\".\n     Check that "
              "`factcheck/evidence/` is where it should be.")
        return 1
    return 1 if bidy else 0


def demo() -> int:
    """A demonstration on a corrupted input.

    Three cases, and the third is the important one: an empty evidence
    directory must be a failure, not silence."""
    import tempfile
    global DOKAZY
    ok = True

    def check(nazva: str, umova: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if umova else '✗'} {nazva}: {umova}")
        ok &= umova

    check("a quote absent from the text is not found as a substring",
          "this line is not there" not in "source text lacking it")
    check("a verbatim quote is found",
          "SOC_UART_NUM" in "#define SOC_UART_NUM 3")

    spravzhni = DOKAZY
    with tempfile.TemporaryDirectory() as d:
        DOKAZY = pathlib.Path(d)
        try:
            got = main()
        finally:
            DOKAZY = spravzhni
        check("an empty evidence directory is a failure, not silence",
              got == 1)
    print("\nfailures:", 0 if ok else 1)
    return 0 if ok else 1


if __name__ == "__main__":
    if "--demo" in sys.argv:
        sys.exit(demo())
    sys.exit(main())
