#!/usr/bin/env python3
"""Transliterated identifiers: an inventory that may shrink and never grow.

## Why

The technology is migrating from transliterated Ukrainian to English so it
can be lifted onto another book. Filenames and directories are done; record
field names are mid-migration; **code identifiers and CLI flags are not
started**, and there are roughly two hundred of them.

Until this file existed the owner was finding them one at a time — `KLASY`,
`SYLA`, `--stysnuty`, `klas` — faster than they were being fixed. That is
not a migration, it is whack-a-mole, and the score only looks like progress.

> A migration measured by what someone happens to notice is not measured.

## What this does, and what it deliberately does not

It does **not** decide what is transliterated: that judgement is baked into
a recorded baseline, `factcheck/reports/TRANSLITERATION.md`. The check compares
today's identifiers against that list and fails on anything **new**.

So the surface can only shrink. A false positive in the detector costs
nothing — it sits in the baseline and never fires again. A real new
transliteration fails immediately, in the commit that introduces it, which
is the only moment it is cheap to fix.

    factcheck/tools/naming.py            check against the baseline
    factcheck/tools/naming.py --write    re-record the baseline after a migration batch
    factcheck/tools/naming.py --proba    show the check firing on a new name
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import repo
import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
BASELINE = ROOT / "factcheck" / "reports" / "TRANSLITERATION.md"

# Англійські корені, які трапляються в іменах. Перелік навмисно
# щедрий: пропущене англійське слово лише додає запис у базу, а
# пропущена транслітерація — ні, бо вона теж туди потрапить.
ENG = set("""all and any args argv base bin block blocks body book build cache
calc call card cards case check checks class classes clean code col cols compare
context copy count data date debug def diff dir dirs doc docs done dry entry error
errors exit fail file files find fix flag flags force found gate get git group head
help hex host id ids in index info init input is json key keys kind kinds label
layer len limit limits line lines link links list load log logs main make map match
max md min miss missing mode model name names new no node none note notes num only
open order out output page pages parse part parts pass path paths pattern patterns
print quiet range raw read ref refs report reports result results root row rows run
runs safe sample scale schema scope seed self set sha show side sign signs size
sketch sort source sources spec split src stat state states status statuses step
steps stop str strength strict sum table tables tag tags task tasks test tests text
time title tool tools total trace traces type unit units url urls use used value
values verify version wave waves write yaml
architecture bridge bridges cache cell chip chips component components
datasheet datasheets default defaults defect defects display displays
electrical electronics evidence experiment experiments flash history
insert inserts iomux level levels module modules motor motors panic
peripheral peripherals pinout pinouts power project projects pullup
pullups pycache queue queues reproducible restructure sensor sensors
cyrillic semtech share snapshot snapshots solder switch switches symptom symptoms unchecked
unreachable wiring""".split())

RE_SYGNAL = re.compile(
    r"kh|zh|ya|yu|yi|ch|sh|ts|iy|yy|ovan|nnya|aty|yty|uva|klas|syla|stan|naryad"
    r"|kesh|zvir|dzher|kart|odyn|vzir|prokh|proba|tekst|imya|pole|rid|rody|vsi|usi")


def transliterovane(w: str) -> bool:
    lw = w.lower().strip("_-")
    if not lw or lw in ENG or not re.fullmatch(r"[a-z0-9_-]+", lw):
        return False
    if any(p in ENG for p in re.split(r"[_-]", lw) if p):
        return False
    return bool(RE_SYGNAL.search(lw))


# Теки карток дзеркалять книгу, а книга українська. Їхні імена — не
# борг: `manual/05-elektronika.md` названо так тому, що так зветься
# розділ. Решта `factcheck/` — технологія, і вона переїжджає.
CARD_DIRS = set(config.groups()) | {"triage",
             # `source-cache` — імена чужих файлів. `ch340.pdf`,
             # `adc_oneshot.rst`, `CMakeLists.txt` не наш борг: ми їх не
             # називали й перейменувати не можемо, не порвавши маніфест.
             "source-cache",
             # `factcheck/tools` — це наш код, і його імена міряє
             # `znaydeni()` як ІДЕНТИФІКАТОРИ. Міряти ще й імена самих
             # файлів означало б різати `bind_by_hash` на `bind`, `by`,
             # `hash` і рахувати кожне слово за борг. Один предмет — одна
             # міра.
             "tools"}


def stemy_knyhy() -> set[str]:
    """Імена файлів самої книги — вони українські й такими лишаються."""
    out = set()
    for d in config.groups():
        for f in (ROOT / d).glob("*.md"):
            out.add(f.stem)
            out.add(re.sub(r"^[0-9a-z]+-", "", f.stem))
    return out


def imena_faylivv() -> set[str]:
    """Імена файлів даних у `factcheck/`, а не лише ідентифікатори.

    Храповик міряв `tools/*.py` — сталі, функції, прапорці. Я подивився
    на його нуль і доповів власникові, що транслітерацію з `factcheck/`
    прибрано. У теці тоді лежало 11 файлів даних і 201 файл доказів із
    транслітерованими іменами; жодного з них храповик не бачив.

    Число було праве. Речення, яке я з нього зробив, — ні.

    > Міра каже, що виміряла. Що вона НЕ виміряла, вона не каже, і
    > мовчання читається як нуль.

    Ім'я доказу складене: родина, номер, тема. Тому міряємо **частини**,
    а не ім'я цілком — інакше `sweep-04-peryferiya` і `sweep-h-dzherela`
    йдуть в одну купу, хоч перше має борг в одному слові, а друге не має
    його зовсім: `h-dzherela` — це ім'я розділу книги, і книга
    українська. Назвати його боргом означало б вимагати, щоб доказ
    посилався на книгу неіснуючим ім'ям."""
    knyha = stemy_knyhy()
    out: set[str] = set()
    for f in (ROOT / "factcheck").rglob("*"):
        if not f.is_file():
            continue
        chastyny = set(f.relative_to(ROOT / "factcheck").parts)
        if CARD_DIRS & chastyny or {"archive", "__pycache__"} & chastyny:
            continue
        for imya in [f.stem] + list(chastyny - {f.name}):
            # Ім'я доказу — це родина, номер і **розділ книги**:
            # `sweep-18-rozdily-fleshu` цитує `manual/18-rozdily-fleshu.md`.
            # Перша спроба звіряла з книгою ім'я цілком, а на частини
            # різала до того, як зняти родину, — і розділ книги розпадався
            # на `rozdily` та `fleshu`, яких у книзі нема. Та сама вада,
            # яку цей файл і ловить: міра, зроблена на крок раніше, ніж
            # треба, міряє свій крок, а не предмет.
            chastky = re.split(r"[-_]", imya)
            if any("-".join(chastky[i:]) in knyha for i in range(len(chastky))):
                continue
            for c in chastky:
                if c and c not in knyha and transliterovane(c):
                    out.add(c)
    return out


def znaydeni() -> set[str]:
    out: set[str] = imena_faylivv()
    for f in repo.tool_files():
        t = f.read_text(encoding="utf-8")
        for pat in (r"^([A-Z][A-Z0-9_]{2,})\s*=",
                    r"^def ([a-z_][a-z0-9_]*)\(",
                    r'"(--[a-z][a-z0-9-]*)"'):
            for m in re.finditer(pat, t, re.M):
                if transliterovane(m.group(1)):
                    out.add(m.group(1))
    return out


def baza() -> set[str]:
    if not BASELINE.exists():
        return set()
    return set(re.findall(r"^- `([^`]+)`", BASELINE.read_text(encoding="utf-8"),
                          re.M))


def zapysaty(imena: set[str]) -> None:
    r = ["# Transliterated identifiers still in the tools",
         "",
         "> **generated** — `factcheck/tools/naming.py --write`. Editing it by hand only",
         "> moves the next run's diff, never the code it describes.",
         "",
         "**Generated by `factcheck/tools/naming.py --write`.** This list may shrink and",
         "must never grow: `make check` fails on any name not recorded here.",
         "",
         "It is not a list of things that are wrong to have written — it is the",
         "measured remainder of a migration, so that progress is a number rather",
         "than an impression. A false positive here is harmless: it sits in the",
         "list and never fires again.",
         "",
         f"**Remaining: {len(imena)}.**", ""]
    r += [f"- `{n}`" for n in sorted(imena)]
    BASELINE.write_text("\n".join(r) + "\n", encoding="utf-8")


def proba() -> int:
    """Показ на новому імені, якого в базі немає."""
    b = baza()
    vygadane = "ZOVSIM_NOVE_IMYA_ZH"
    spiymav = transliterovane(vygadane) and vygadane not in b
    print("   %s нове транслітероване ім'я поза базою — ловиться: %s"
          % ("✓" if spiymav else "✗ ПРОВАЛ", spiymav))
    anh = "SOURCE_LIMITS"
    tyxo = not transliterovane(anh)
    print("   %s англійське ім'я не спрацьовує: %s"
          % ("✓" if tyxo else "✗ ПРОВАЛ", tyxo))
    return 0 if (spiymav and tyxo) else 1


def main() -> int:
    if "--proba" in sys.argv:
        return proba()
    ye = znaydeni()
    if "--write" in sys.argv:
        zapysaty(ye)
        print("naming: recorded %d names -> %s" % (len(ye), BASELINE.name))
        return 0
    b = baza()
    novi = sorted(ye - b)
    znykli = len(b - ye)
    for n in novi:
        print("   ✗ new transliterated identifier: `%s` — rename it, or run "
              "--write if it is a false positive" % n)
    print("\nnaming: %d transliterated names remain (%d fewer than recorded), "
          "%d new" % (len(ye), znykli, len(novi)))
    return 1 if novi else 0


if __name__ == "__main__":
    sys.exit(main())
