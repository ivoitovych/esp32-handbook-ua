#!/usr/bin/env python3
"""Intake: mechanical conditions a record must pass before it is committed.

Not to be confused with `factcheck.py vorota` — those gates are outbound,
asking whether the book may be printed. These are inbound: whether this
evidence may enter the registry at all. A defect is cheaper not to admit
than to hunt down later.

The conditions:

  1. the YAML parses;
  2. the source is not a file of the book itself (except
     `no-external-signal` and declared internal checks — see below);
  3. `verbatim`/`derived` carries a non-empty quote;
  4. the `match` pattern compiles — as a whole and alternative by
     alternative;
  4a. the pattern does not match foreign text (see CONTROLS);
  4b. no alternative LEAKS — matching more than all the others together,
      and matching a lot;
  5. `no-external-signal` does not stand on a claim carrying a number, an
     address or a GPIO — not an error, but grounds for a second look: the
     index and the author's own measurement legitimately stay there.

## The book's language is in book.yaml, not here

Four of these patterns read the book's own prose — the words for
"chapter", "card", "appendix", the unit abbreviations. They are Ukrainian
because this book is. Carried to an English book they would match
nothing, and this gate would pass everything in silence, which is the
worst way for an inbound gate to fail.
"""
import glob
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config      # noqa: E402
import factcheck   # noqa: E402  (the pattern splitter is M1's)

# A tenth copy of the book's directories lived here. The sweep that
# replaced the eight `GRUPY` copies did not find it, and neither did the
# one that found the ninth in `cache_vs_book`: a list is not found by the
# name of the fact it holds.
BOOK_PATH = re.compile(r"\b(%s)/[a-z0-9]" % "|".join(config.groups()))

_words = config.intake()
RE_BOOK_IN_WORDS = (re.compile(_words["book_in_words"], re.I)
                    if _words.get("book_in_words") else None)
RE_INTERNAL = (re.compile(_words["internal_check"])
               if _words.get("internal_check") else None)
RE_SIGNAL = (re.compile(_words["signal"]) if _words.get("signal") else None)
RE_INDEX = (re.compile(_words["index"], re.I) if _words.get("index") else None)

# Naming an external document is not naming the book. "UM10204, section
# 7.1" and "DHT11 datasheet, parameters section" are sections of OTHER
# people's documents and must not be caught here.
RE_EXTERNAL = re.compile(
    r"datasheet|specification|reference manual|user manual|programming guide"
    r"|documentation"
    r"|UM\d|SBOS|DS\d|IEC\s*\d|ISO\s*\d|IEEE\s*\d|RFC\s*\d|Rev\."
    r"|esp-idf|espressif|esptool|nxp|texas|microchip|vishay|maxim|aosong"
    r"|sitronix|solomon|invensense|silicon labs|raspberry|https?://", re.I)

# Control strings: they do not belong to the registry, and no pattern has
# the right to match them. A pattern matching all three matches the whole
# registry — and silently moves every unit into its own status.
#
# Bought expensively: seven such patterns from wave 1 showed 8083 units of
# 8083 as `verbatim`, i.e. "the book is 100 % checked". None of them
# failed or looked idle. Five were raw table rows —
# `| \`0xe\` | EXT_CPU_RESET | норма |` — where a pipe is not a pipe but an
# OR, so the pattern reads as "empty or 0xe or … or empty" and matches
# anything. Two had a doubled escape `\\|`, which does the same.
#
# That is the third and worst form of the pipe trap. The first two are
# visible: the pattern either fails or matches nothing. This one looks
# like success.
CONTROLS = ("ESP32 має два ядра",
            "Зовсім інший текст про каву",
            "12345")

# **A leaking pattern.** M1's finding of 2026-08-28 06:30Z, and the third
# form of the disjunction trap — after the idle one and the all-matching
# one.
#
# A pattern is an OR of alternatives. If one of them matches more than all
# the others together, and matches a lot, it does not narrow the pattern —
# it REPLACES it.
#
# The worst example is mine: an evidence about an unpulled GPIO had the
# bare word `стан` among its alternatives, and it matched 242 units — so
# the evidence put its status on nearly every claim in the book containing
# that word. The pattern compiled, was not idle, and did not match the
# control strings, so every earlier gate passed it.
#
# Leaks in my patterns: 15. In M1's: 2.
LEAK_MIN = 25   # fewer is not worth an alarm; a word may simply be rare


def unit_texts():
    """Texts of the registry's units — needed only for the leak check."""
    try:
        import sample
        # Not a private string of letters: the one that used to be here
        # had no `N`, `K`, `S`, `L`, so the leak check silently did not
        # see units in those statuses. The source of the list is the
        # code, and only the code.
        return [o["tekst"] for k in factcheck.STATUSES
                for o in sample.odynyci(k)]
    except Exception:
        return None


texts = None


def check_file(path):
    problems = []
    try:
        records = yaml.safe_load(open(path)) or []
    except Exception as e:
        return [("BROKEN YAML", str(e).split("\n")[0][:90], "")]
    for z in records:
        if not isinstance(z, dict):
            problems.append(("NOT A RECORD", str(z)[:60], ""))
            continue
        name = str(z.get("title", ""))[:58]
        status = z.get("status", "?")
        source = str(z.get("source", ""))
        quote = str(z.get("quote", "")).strip()

        # `self-consistent` is the **right** answer to "the book as its own
        # source", not a violation. M1 introduced it on 2026-08-28T19:15Z
        # for exactly these 21 records; it requires a path to a book file
        # and passes layer 3 against the book, so the check here is work
        # done rather than a promise.
        #
        # `no-external-signal` stays permitted for a different reason:
        # there no check was made and none will be.
        if (BOOK_PATH.search(source)
                and status not in ("no-external-signal", "self-consistent")):
            if RE_INTERNAL and RE_INTERNAL.match(source):
                problems.append(("INTERNAL CHECK UNDER " + status, name, ""))
            else:
                problems.append(("THE BOOK AS ITS OWN SOURCE", name, status))
        if (status in ("verbatim", "derived") and RE_BOOK_IN_WORDS
                and RE_BOOK_IN_WORDS.search(source)
                and not RE_EXTERNAL.search(source)):
            problems.append(("THE BOOK AS A SOURCE, NAMED IN WORDS", name,
                             source[:40]))
        # A pattern that does not compile is not merely a dead record. It
        # kills `factcheck.py sketch` for the WHOLE registry, breaking the
        # rendering for both maintainers. Three arrived with wave 1 (raw
        # book text with `**bold**` in the pattern field: an asterisk at
        # position zero — "nothing to repeat"), and because of them
        # neither wave appeared in the status counts at all, though every
        # evidence was in place. So this condition blocks.
        pattern = str(z.get("match", ""))
        if pattern:
            try:
                re.compile(pattern)
                for alt in factcheck.rozbyty_alternatyvy(pattern):
                    re.compile(alt)
            except re.error as e:
                problems.append(("PATTERN DOES NOT COMPILE: %s" % e, name, ""))
            else:
                rx = re.compile(pattern)
                if all(rx.search(k) for k in CONTROLS):
                    problems.append(("PATTERN MATCHES EVERYTHING", name, ""))
                elif texts is not None:
                    alt = factcheck.rozbyty_alternatyvy(pattern)
                    if len(alt) > 1:
                        counts = sorted(((sum(1 for t in texts
                                              if re.search(a, t)), a)
                                         for a in alt), reverse=True)
                        if (counts[0][0] >= LEAK_MIN
                                and counts[0][0] > sum(x for x, _ in counts[1:])):
                            problems.append(
                                ("LEAK: «%s» matches %d"
                                 % (counts[0][1][:20], counts[0][0]), name, ""))
        if status in ("verbatim", "derived") and not quote:
            problems.append(("%s WITH NO QUOTE" % status.upper(), name, ""))
        if (status == "no-external-signal" and RE_SIGNAL
                and RE_SIGNAL.search(name)
                and not (RE_INDEX and RE_INDEX.search(name))):
            problems.append(("?  no-external-signal on a claim with a number",
                             name, ""))
    return problems


def main(argv):
    global texts
    texts = unit_texts()
    paths = argv[1:] or sorted(glob.glob("factcheck/evidence/*.yaml"))
    total = 0
    blocking = 0
    for s in paths:
        b = check_file(s)
        total += len(b)
        blocking += sum(1 for x in b if not x[0].startswith("?"))
        if b:
            print(os.path.basename(s))
            for kind, name, extra in b:
                print("   %-38s %s %s" % (kind, name, extra))
    # Zero files is not "no problems" — it is "nothing was read".
    if not paths:
        print("   ✗ no evidence files found — this is not a clean intake")
        return 1
    if texts is None:
        print("   · unit texts unavailable: the LEAK check was SKIPPED, "
              "not passed")
    print("\nproblems: %d in %d files (%d blocking, %d to review)"
          % (total, len(paths), blocking, total - blocking))
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
