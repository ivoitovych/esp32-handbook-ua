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
# джерела**. «Властивості логіки CMOS», «фундаментальне правило
# електроніки», «типова побудова модульних плат».
#
# Це найгірший можливий наслідок з усіх: хибний клас `A` оголошує
# твердження звіреним, прибирає його з кожної черги, і більше його не
# перевіряє ніхто ніколи.
#
# Шар 3 таке бачив як «джерела немає в кеші» — сигнал є, тривоги немає.
# Тепер для класів `A` і `B` це помилка. Класи `C` і `E` під правило не
# підпадають: у них джерела або немає, або воно недосяжне за задумом.
# Що вважається названим документом. Перший підхід був завузький і
# позначив вигаданими чотирнадцять записів, з яких тринадцять — чесні
# посилання М2 на PDF, у якого немає сталої адреси: «Texas Instruments,
# PCF8574 Remote 8-Bit I/O Expander for I2C Bus (SCPS068), розділ
# Features». Це повноцінна цитата, просто не URL.
#
# Різниця між нею й вигаданим джерелом не в наявності адреси, а в тому,
# **чи названо документ**: видавця, заголовок, номер редакції. Вигадане
# джерело описує не документ, а властивість світу — «властивості логіки
# CMOS», «загальновідома електромеханіка реле».
RE_ADRESA = re.compile(
    r"https?://|\b[\w-]+\.(?:com|org|net|io|dev)/"
    r"|\.pdf\b|\.h\b|\.c\b|\.py\b|\.rst\b|\.inc\b|\.csv\b"
    r"|components/|tools/|docs/|Kconfig", re.I)
# Дві поспіль великі латинські лексеми — назва видавця або заголовок
# документа: `Texas Instruments`, `Product Brief`, `Register Map`.
RE_NAZVA_DOKUMENTA = re.compile(r"\b[A-Z][A-Za-z0-9-]+ [A-Z][A-Za-z0-9-]+")
# Ідентифікатор документа: `SCPS068`, `DS40002061B`, `RM-MPU-6000A-00`,
# `Rev 1.1`, `UM10204`, `IEC 61190-1-3`.
RE_ID_DOKUMENTA = re.compile(
    r"\b[A-Z]{2,}[0-9][\w-]*\b|\bRev\.?\s*\d|\b(?:IEC|ISO|EN|UL)\s*\d",
    re.I)


# Джерело всередині книги. М2 звірив твердження проєкту 60 з **власним
# кодом того самого розділу**: поріг у прозі проти порога в лістингу.
#
# Це не зовнішня цитата й не вигадане джерело — це третій рід, якого в
# архітектурі не було. Саме він і є той «четвертий шар», що його бракує:
# реєстр звіряє книгу з джерелами, але не книгу з книгою, а найгірші
# помилки цього тижня були саме внутрішніми суперечностями (BMP280 у
# додатку E проти розділу 45).
#
# Тож такий запис правомірний, і шар 3 його пропускає. Але перевірити
# його механічно тут нічим: джерело — сама книга, і потрібен інший
# інструмент, не цей.
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
    """Які рядки групи не знайшлися в жодному з джерел.

    Два способи, і потрібні обидва, бо ми цитуємо двома способами.

    **Злитою групою** — коли ми перенесли довгий рядок джерела на два
    своїх. Тоді жоден наш рядок окремо в джерелі не стоїть, а разом
    вони стоять дослівно.

    **Порядково** — коли ми зібрали уривок із **різних місць** файлу:
    `#define IO_MUX_GPIO11_REG` із рядка 107 і `PERIPHS_IO_MUX_VDD_SPI_U`
    із рядка 223. Разом вони не стоять ніде, і це не вада цитати, а
    звичайний спосіб показати два пов'язані означення поруч.

    Спершу пробуємо злиту: вона строгіша, бо вимагає ще й порядку.
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


# `\S+`, а НЕ `[^\s,;]+`, і це не недогляд.
#
# Кома тут не завжди роздільник: у скороченнях стоїть розкриття дужок —
# `.../components/esp_psram/{esp32,esp32s3}/Kconfig.spiram`, — і кома
# всередині `{…}` є частиною лексеми. Я був звузив клас символів, щоб
# відрізати хвостову кому в `.../Adafruit_ST7789.cpp,`; вимір показав
# **дві регресії**: обидва записи з дужками дістали обрізаний шлях
# `…/{esp32` і втратили джерело, яке доти мали.
#
# Хвостову кому й так знімає `rstrip(".,")` нижче — тобто «виправлення»
# лікувало те, що вже було виліковане, і ламало те, що працювало.
#
# > Звуження, зроблене «про всяк випадок», ламає рівно ті випадки, яких
# > автор не тримав у голові, коли звужував.
RE_SKOROCHENNYA = re.compile(r"(?<![\w/])\.\.\./(\S+)")


def korin_dlya(povnyy: str, skorocheno: str) -> str | None:
    """Корінь дерева, проти якого розгортається скорочення.

    Рахувати сегменти адреси не можна: гілка `release/v5.5` містить
    скісну риску, і `owner/repo/ref` виявляється то трьома сегментами,
    то чотирма. Перша спроба це робила й мовчки давала неробочі адреси.

    Надійніше запитати саме скорочення. Його перший сегмент —
    `components`, `docs`, `tools` — це каталог, який є і в повній
    адресі. Ріжемо повну там, де він починається, і корінь виходить
    правильним незалежно від того, скільки скісних рисок у назві гілки.
    """
    persh = skorocheno.lstrip("/").split("/", 1)[0]
    if not persh:
        return None
    i = povnyy.find(f"/{persh}/")
    return povnyy[:i + 1] if i > 0 else None


def root_by_verification(povnyy: str, skorocheno: str) -> str | None:
    """Корінь, знайдений **перевіркою**, а не здогадом.

    ## Навіщо, якщо `korin_dlya` уже є

    Бо його засновок хибний частіше, ніж правдивий. Він вимагає, щоб
    перший сегмент скорочення був каталогом, який є і в повній адресі, —
    а це не так у трьох звичайних випадках:

        .../docs/en/esptool/basic-options.rst
            повна адреса веде в `esptool/__init__.py`; `/docs/` у ній
            немає взагалі — скорочення відлічене від кореня репозиторію

        .../Adafruit_ST7789.cpp
            перший сегмент — сам файл, каталогу немає

        .../esp32/include/soc/touch_sensor_channel.h
            у повній адресі стоїть `/soc/{esp32,esp32s3,esp32c3}/`,
            тож `/esp32/` літерально не трапляється

    Виміряно на реєстрі: **29 скорочень із 60 відкидалися мовчки**, у 28
    записах. Тобто шар 3 звіряв цитату проти меншої кількості
    документів, ніж запис називає, і звітував «не знайдено» про рядки,
    які лежали в невиведеному джерелі.

    ## Чому перевірка, а не краще вгадування

    Порахувати сегменти не можна — гілка `release/v5.5` містить скісну
    риску, і саме на цьому попередня спроба мовчки видавала неробочі
    адреси. Але **перебрати** корені можна, а прийняти лише той, чий
    файл справді лежить у кеші:

    > Адресу, якої не вивести, можна **відновити звіркою**: породжуємо
    > кандидатів і лишаємо того, чиє ім'я в кеші існує.

    Це те саме правило, яким уже відновлено 25 URL із 32 (`METHOD.md`,
    розділ про кеш). Головне тут не кількість, а те, що **хибної адреси
    ця форма видати не може**: невірний корінь дає ім'я, якого в кеші
    немає, і відкидається. Рід 17 — машинний покажчик, гірший за прозу —
    закритий за побудовою, а не обіцянкою.

    Виміряно: з 31 скорочення, що не працювало, відновлено **15**.
    Решта 16 не відновлюються, бо їхнього файлу немає в цьому кеші, — і
    це чесно інша річ, ніж хибний покажчик.
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
    """Усі адреси запису, з розгорнутими скороченнями.

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

            # **Читання таблиці — не цитата, і це два різні роди.**
            # Знахідка М2 від 22:05Z, і вона стосується самої побудови
            # поля `cytata`.
            #
            # У datasheet факт часто живе в перетині рядка й стовпця, а
            # назва параметра стоїть у комірці, розтягнутій на кілька
            # рядків. Зібрати з цього «рядок таблиці» можна лише рукою —
            # злити клітинки, дописати `Typ`, `Min`, `(note 3)`. Факт
            # при цьому правильний, а суцільного рядка в документі
            # **немає й не буде**, скільки б ми не покращували витягання.
            #
            # М2 знайшов це в себе, назвавши прямо: «це рівно те, що ми
            # звемо помилкою помічника — коментар, вписаний у поле
            # цитати; я робив це власноруч і водночас перевіряв за це
            # інших».
            #
            # Тому окреме поле: перелік клітинок, кожна перевіряється
            # підрядком **окремо**, без вигаданих відступів і дописаних
            # слів. Пояснення йде в нотатку, де йому й місце.
            tablychna = z.get("cytata-tablytsya")
            if tablychna:
                frahmenty = [[str(k).strip()] for k in tablychna
                             if str(k).strip()]
            else:
                frahmenty = uryvky(
                    str(factcheck.pole(z, "quote", "cytata") or ""),
                    vlasna_mova=(stan == "self-consistent"))
            urly = dzherela_zapysu(z)
            # Клас `S` адресує книгу, а не мережу, тож відсутність URL
            # у нього — норма, а не «нема чого звіряти».
            #
            # Клас `N` не має цитати **за означенням**: він доводить
            # відсутністю, і те, чого немає, стоїть у полі `absent`.
            # Вимагати від нього уривків означало б відкидати його як
            # «нема чого звіряти» — тобто мовчки скасувати клас.
            if stan == "absent-from-source":
                if not urly:
                    pidsumok["nichoho"] += 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="nichoho",
                        detali="клас N без URL джерела"))
                    continue
            elif not frahmenty or (not urly and stan != "self-consistent"):
                pidsumok["nichoho"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nichoho",
                    detali=("немає URL" if frahmenty else
                            "немає придатних уривків")))
                continue

            teksty: list[str] = []
            nedosyazhni: list[str] = []
            zaglushky: list[str] = []
            nechytni: list[str] = []
            tablychni = False

            # Внутрішня звірка: корпус — названі файли книги.
            if stan == "self-consistent":
                shlyakhy = knyzhkovi_dzherela(z)
                if not shlyakhy:
                    pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="pomylka",
                        detali="клас S, а в джерелі немає шляху до файлу "
                               "книги — звіряти нема з чим"))
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

            # «Файл є, прочитати нічим» і «файлу немає» — різні стани, і
            # плутати їх небезпечно. Досі PDF без витягача мовчки падав у
            # «немає в кеші», тобто виглядав як проблема егресу, а не як
            # брак інструмента на цій машині.
            if nechytni and not teksty:
                pidsumok["nechytne"] = pidsumok.get("nechytne", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nechytne",
                    detali=f"{len(nechytni)}: файл у кеші є, витягти текст "
                           f"нічим"))
                continue

            if zaglushky and not teksty:
                pidsumok["zaglushka"] = pidsumok.get("zaglushka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="zaglushka",
                    detali=f"{len(zaglushky)}: у кеші не PDF, а сторінка "
                           f"з кодом 200"))
                continue

            if not teksty:
                pidsumok["nedosyazhne"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nedosyazhne",
                    detali=f"{len(nedosyazhni)} джерел не в кеші"))
                continue

            # **Доведення відсутністю — єдиний клас, який шар 3 може
            # спростувати, а не лише не підтвердити.**
            #
            # Для решти класів шар 3 питає «чи стоїть цей рядок у
            # документі», і відповідь «ні» означає розбіжність цитати —
            # часто хибну тривогу (переніс рядка, таблиця в PDF). Тут
            # питання обернене й відповідь однозначна: якщо рядок, чия
            # ВІДСУТНІСТЬ і є доказом, у документі знайдено, то доказ
            # не розбіжний — він хибний.
            if stan == "absent-from-source":
                shukane = str(z.get("absent") or "").strip()
                if not shukane:
                    pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="pomylka",
                        detali="клас N без поля `absent` — нема чого не "
                               "шукати"))
                    continue
                znaydeno = [u for u, tx in zip(urly, teksty) if shukane in tx]
                if znaydeno:
                    pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="pomylka",
                        detali=f"клас N СПРОСТОВАНО: «{shukane[:40]}» "
                               f"СТОЇТЬ у названому документі"))
                    continue
                # Контроль: документ того самого роду, де рядок Є. Без
                # нього мовчання може означати просто інший формат
                # файлу, а не відсутність властивості.
                kontrol = str(z.get("control") or "").strip()
                if kontrol:
                    kt = [tx for u, tx in zip(urly, teksty) if u != kontrol]
                    ku = [u for u in urly if u == kontrol]
                    if ku and not any(shukane in tx for u, tx in
                                      zip(urly, teksty) if u == kontrol):
                        pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                        naslidky.append(dict(
                            fayl=f.stem, nazva=nazva, stan="pomylka",
                            detali=f"клас N: у контрольному документі "
                                   f"«{shukane[:30]}» теж немає — "
                                   f"мовчання нічого не доводить"))
                        continue
                pidsumok["ok"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ok",
                    detali=f"відсутність «{shukane[:40]}» підтверджено"))
                continue

            vsjogo_ryadkiv = sum(len(g) for g in frahmenty)
            promakhy: list[str] = []
            for grupa in frahmenty:
                promakhy += znayty(grupa, teksty, tablychni=tablychni)
            if promakhy:
                # **Промах при НЕПОВНОМУ наборі джерел — не промах.**
                #
                # Гілка `nedosyazhne` вище спрацьовує лише тоді, коли в
                # кеші немає ЖОДНОГО джерела. Якщо ж запис називає два, а
                # є один, цитата звірялася проти половини того, на що
                # запис посилається, — і «не знайдено» приписує браку
                # цитати те, що може лежати в ненайденому файлі.
                #
                # Рід 25: два стани світу під одним словом. «Цитата не
                # збігається» і «ми не тримали документа» вимагають
                # різної роботи — першу править супровідник, другу
                # закриває завантаження.
                #
                # Виміряно: з 69 записів «не знайдено» **8** судилися на
                # неповному наборі.
                if nedosyazhni:
                    pidsumok["nedosyazhne"] += 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="nedosyazhne",
                        detali=f"{len(nedosyazhni)} з "
                               f"{len(nedosyazhni) + len(teksty)} джерел не "
                               f"в кеші; решта не покрила "
                               f"{len(promakhy)} з {vsjogo_ryadkiv} рядків"))
                    continue
                pidsumok["ne_znaydeno"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ne_znaydeno",
                    detali=f"{len(promakhy)} з {vsjogo_ryadkiv} рядків",
                    promakhy=promakhy[:3]))
            else:
                pidsumok["ok"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ok",
                    detali=f"{vsjogo_ryadkiv} рядків"))
    return naslidky, pidsumok


ZAHOLOVOK_ZVITU = """# Третій шар: цитати проти джерел

**Генерується** `factcheck/tools/layer3.py --zvit`. Правити вручну нема сенсу.

Перевірено механічно: чи справді уривок, наведений у доказі, стоїть за
названою адресою. Це **не** оцінка того, чи доказ доречний — це окреме
питання, і його вирішує людина.

| Стан | Означає |
|---|---|
| `звірено` | усі придатні уривки знайдено в джерелі дослівно |
| `не знайдено` | уривка в джерелі немає — переказ, помилка адреси або джерело змінилося |
| `джерело не в кеші` | нема з чим звіряти: `--kachaty`, або егрес не пускає |
| `нема чого звіряти` | доказ без URL або без дослівного уривка (клас `C`, `E`, `K`) |
| `джерело вигадане` | клас `A` чи `B`, а в полі джерела — міркування, не документ |
| `у кеші заглушка` | сервер віддав HTML із кодом 200 замість PDF |
| `звірено очима` | витягання тексту руйнує структуру; звірив супровідник, причина названа |

"""


def zvit(naslidky: list[dict], pidsumok: dict[str, int]) -> None:
    pidpysy = {"ok": "звірено", "ne_znaydeno": "**не знайдено**",
               "nedosyazhne": "джерело не в кеші",
               "nichoho": "нема чого звіряти",
               "vygadane": "**джерело вигадане**",
               "zaglushka": "**у кеші заглушка, не документ**",
               "okom": "звірено очима",
               "nechytne": "**файл є, витягти текст нічим**",
               "nadmirnyy_e": "клас E на твердженні з числом — перевірити",
               "pomylka": "**хибний запис**"}
    r = [ZAHOLOVOK_ZVITU.rstrip("\n"), ""]
    r.append(f"Записів доказів: **{sum(pidsumok.values())}**. "
             f"Звірено дослівно: **{pidsumok['ok']}**. "
             f"Не знайдено: **{pidsumok['ne_znaydeno']}**. "
             f"Джерело не в кеші: **{pidsumok['nedosyazhne']}**. "
             f"Нема чого звіряти: **{pidsumok['nichoho']}**.\n")
    r.append(f"Станом на {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC.\n")
    for stan in ("vygadane", "zaglushka", "pomylka", "nechytne",
                 "nadmirnyy_e", "ne_znaydeno",
                 "nedosyazhne", "okom", "ok", "nichoho"):
        grupa = [n for n in naslidky if n["stan"] == stan]
        if not grupa:
            continue
        r.append(f"\n## {pidpysy[stan]} — {len(grupa)}\n")
        r.append("| Доказ | Файл | Деталі |")
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
        print(f"layer3: звіт у {ZVIT.relative_to(ROOT)}")

    for n in naslidky:
        if n["stan"] == "ne_znaydeno":
            print(f"   ✗ {n['nazva']}  ({n['fayl']}) — {n['detali']}")
            for p in n.get("promakhy", []):
                print(f"        не знайдено: «{p[:100]}»")
        elif n["stan"] == "pomylka":
            print(f"   ✗ {n['nazva']}  ({n['fayl']}) — {n['detali']}")

    print(f"layer3: записів {sum(pidsumok.values())}; "
          f"звірено {pidsumok['ok']}; "
          f"не знайдено {pidsumok['ne_znaydeno']}; "
          f"не в кеші {pidsumok['nedosyazhne']}; "
          f"без цитати {pidsumok['nichoho']}; "
          f"звірено очима {pidsumok['okom']}")
    if pidsumok["nadmirnyy_e"]:
        print(f"   · клас E на твердженні з числом: "
              f"{pidsumok['nadmirnyy_e']} — перевірити, чи джерела справді "
              f"немає")
    if pidsumok["vygadane"] or pidsumok["zaglushka"] or pidsumok["pomylka"]:
        print(f"   ⚠ вигаданих джерел {pidsumok['vygadane']}; "
              f"заглушок у кеші {pidsumok['zaglushka']}; "
              f"хибних записів {pidsumok['pomylka']}")

    # Вигадане джерело, заглушка й доказ класу F — це **ворота**, а не
    # звіт. Розбіжність цитати вимагає розгляду й може бути хибною
    # тривогою; ці три не можуть бути нічим, крім помилки.
    bidy = pidsumok["vygadane"] + pidsumok["zaglushka"] + pidsumok["pomylka"]
    if "--suvoro" in a:
        bidy += pidsumok["ne_znaydeno"] + pidsumok["nedosyazhne"]
    # Нуль записів — не «жодної підробки», а «нема чого перевіряти».
    # `layer1` і `coverage` прожили в цьому стані кілька днів після
    # переїзду карток, друкуючи нулі як чистоту. Третій шар читає теку
    # доказів і вразливий так само.
    if not sum(pidsumok.values()):
        print("   ✗ ЖОДНОГО запису не прочитано — це не «чисто», це "
              "«нема чого перевіряти».\n     Перевір, що "
              "`factcheck/evidence/` на місці.")
        return 1
    return 1 if bidy else 0


def demo() -> int:
    """Показ на зіпсованому вході.

    Три випадки, і третій — головний: порожня тека доказів мусить бути
    провалом, а не тишею."""
    import tempfile
    global DOKAZY
    ok = True

    def check(nazva: str, umova: bool) -> None:
        nonlocal ok
        print(f"   {'✓' if umova else '✗'} {nazva}: {umova}")
        ok &= umova

    check("цитата, якої немає в тексті, не знаходиться підрядком",
          "цього рядка немає" not in "текст джерела, у якому її нема")
    check("дослівна цитата знаходиться",
          "SOC_UART_NUM" in "#define SOC_UART_NUM 3")

    spravzhni = DOKAZY
    with tempfile.TemporaryDirectory() as d:
        DOKAZY = pathlib.Path(d)
        try:
            got = main()
        finally:
            DOKAZY = spravzhni
        check("порожня тека доказів — це провал, а не тиша", got == 1)
    print("\nпровалів:", 0 if ok else 1)
    return 0 if ok else 1


if __name__ == "__main__":
    if "--demo" in sys.argv:
        sys.exit(demo())
    sys.exit(main())
