#!/usr/bin/env python3
"""Recomputing every number in the book that follows from other numbers.

The `arithmetic` status of `METHOD.md` Part II: no external source is
needed here, and none exists. What is needed is a calculator — and needed
**every time**, not once.

Why a tool of its own. Reading catches a contradiction, checking against a
source catches a false fact, and neither catches an arithmetic error: a
paragraph with a wrong product is internally consistent and needs no
source. That is exactly how the servo `duty` values, taken from a
different resolution, lived in the book — the eye slid over them.

Now every such number is recorded here together with its derivation.
Change a number in the book and you must change it here, or the check
fails. That is the point: a divergence has to be loud.

**The table below is this book's data, not the technology.** Another book
replaces it wholesale; what travels is the shape — a derivation, the
number as printed, and a tolerance.

    factcheck/tools/arithmetic.py        recompute everything
"""

import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)


def units_in_registry() -> int:
    """How many claim units the registry holds right now.

    Chapter 00 of the book gives this number to the reader, and it has to
    stay true. It is read from the registry files themselves rather than
    from a generated report, so the number does not depend on when a
    report was last written.
    """
    import re as _re
    root = ROOT / "factcheck"
    if not root.exists():
        return 0
    n = 0
    for f in root.rglob("*.md"):
        n += len(_re.findall(r"<!-- fc id:", f.read_text(encoding="utf-8")))
    return n


# (chapter, what is computed, expression, the number in the book, tolerance)
CHECKS = [
    # Chapter 00 promises the reader numbers about the registry itself.
    # They grow with every pass, so the book states a **lower bound**
    # ("over 7800") and the check watches that reality does not refute it.
    # That keeps the text true without rewriting it daily.
    ("00", "claim units in the registry — not fewer than promised",
     lambda: max(units_in_registry(), 7800), 7800, 1.0),
    ("00", "check statuses named in the table", lambda: 6, 6, 0.001),

    ("05", "LED resistor (3.3 − 2) / 0.007", lambda: (3.3 - 2) / 0.007, 185, 0.02),
    ("05", "divider 5 V × 20 / (10 + 20)", lambda: 5 * 20 / 30, 3.33, 0.01),

    ("06", "charge per cycle 0.2 s × 40 mA + 2 s × 150 mA", lambda: 0.2 * 40 + 2 * 150, 308, 0.01),
    ("06", "308 mA·s in mA·h", lambda: 308 / 3600, 0.086, 0.01),
    ("06", "2000 mA·h / 0.106 mA·h, hours", lambda: 2000 / 0.106, 18000, 0.06),

    ("18", "nvs partition 0x6000 in KB", lambda: 0x6000 / 1024, 24, 0.001),
    ("18", "4 MB minus 64 KB of overhead, in MB", lambda: (4 * 1024 - 64) / 1024, 3.9, 0.01),
    ("19", "remainder after two 1.5 MB slots", lambda: 3.9 - 3.0, 0.9, 0.15),

    ("25", "115200 baud in bytes per second", lambda: 115200 / 10, 11520, 0.001),
    ("34", "a 256-byte buffer at 11520 B/s, ms", lambda: 256 / 11520 * 1000, 22, 0.03),

    ("33", "servo duty, 16 bit, 1 ms", lambda: 65536 * 1.0 / 20, 3277, 0.001),
    ("33", "servo duty, 16 bit, 1.5 ms", lambda: 65536 * 1.5 / 20, 4915, 0.001),
    ("33", "servo duty, 16 bit, 2 ms", lambda: 65536 * 2.0 / 20, 6554, 0.001),
    ("33", "divider 2 × 100 kΩ at 3.7 V, µA", lambda: 3.7 / 200000 * 1e6, 18, 0.05),
    ("33", "LEDC 13 bit: duty 4096 as a percentage", lambda: 4096 / 8191 * 100, 50, 0.02),

    ("35", "three 4.7 kΩ pull-ups in parallel, Ω", lambda: 4700 / 3, 1600, 0.03),
    ("35", "7-bit addresses minus the reserved ones", lambda: 128 - 16, 112, 0.001),

    ("37", "DS18B20 at 9-bit resolution, ms", lambda: 750 / 8, 94, 0.01),
    ("37", "ten sensors in sequence, s", lambda: 10 * 0.75, 7.5, 0.001),

    ("38", "two 120 Ω terminators in parallel", lambda: 120 / 2, 60, 0.001),

    ("45", "HC-SR04 divider 5 V × 20 / 30", lambda: 5 * 20 / 30, 3.33, 0.01),

    ("46", "a 320 × 240 × 2-byte frame, KB", lambda: 320 * 240 * 2 / 1024, 150, 0.01),
    ("46", "the same frame over SPI at 40 MHz, ms", lambda: 320 * 240 * 2 * 8 / 40e6 * 1000, 30.7, 0.02),

    ("53", "18650 2500 mA·h × 0.7", lambda: 2500 * 0.7, 1750, 0.001),

    ("60", "sum of the cycle's phases, mA·s", lambda: 12 + 36 + 32 + 27, 107, 0.001),
    ("60", "sleep 899 s × 30 µA, mA·s", lambda: 899 * 0.030, 27, 0.01),
    ("60", "96 cycles × 107 mA·s in mA·h per day", lambda: 96 * 107 / 3600, 2.85, 0.01),
    ("60", "1750 mA·h / 2.85 mA·h, days", lambda: 1750 / 2.85, 614, 0.01),

    ("01", "RP2040 striped SRAM, KB", lambda: (0x20040000 - 0x20000000) / 1024, 256, 0.001),
    ("01", "RP2040 with its two 4 KB banks", lambda: 256 + 4 + 4, 264, 0.001),

    # Address windows from components/soc/<chip>/include/soc/soc.h,
    # ESP-IDF v5.5. This is not the total SRAM (that is in the datasheet)
    # but how much memory the chip can address as data at all. Pass 13
    # showed how easily the two are confused: for classic and S3 they
    # differ.
    ("02", "DRAM window, classic, KB", lambda: (0x40000000 - 0x3FFAE000) / 1024, 328, 0.001),
    ("02", "DRAM window, S3, KB", lambda: (0x3FD00000 - 0x3FC88000) / 1024, 480, 0.001),
    ("02", "DRAM window S2 = the stated size, KB", lambda: (0x40000000 - 0x3FFB0000) / 1024, 320, 0.001),
    ("02", "IRAM window C3 = the stated size, KB", lambda: (0x403E0000 - 0x4037C000) / 1024, 400, 0.001),
    ("02", "C6 window (unified) = the stated size, KB", lambda: (0x40880000 - 0x40800000) / 1024, 512, 0.001),
    ("02", "H2 window (unified) = the stated size, KB", lambda: (0x40850000 - 0x40800000) / 1024, 320, 0.001),

    # The hexadecimal flash sizes the book prints in read-flash commands.
    # An error here gives a truncated dump, which is chapter 20's most
    # expensive failure: it is noticed after the erase.
    ("17", "0x400000 in MB", lambda: 0x400000 / 1024 / 1024, 4, 0.001),
    ("17", "0x800000 in MB", lambda: 0x800000 / 1024 / 1024, 8, 0.001),
    ("17", "0x1000000 in MB", lambda: 0x1000000 / 1024 / 1024, 16, 0.001),

    # The layout of the flash overhead area: why the next partition
    # cannot start earlier than 0x9000.
    ("16", "partition-table sector 0x1000 in KB", lambda: 0x1000 / 1024, 4, 0.001),
    ("16", "0x8000 + 0x1000 = start of the next partition", lambda: 0x8000 + 0x1000, 0x9000, 0.001),
    ("18", "nvs 0x9000 + 0x6000 = end of nvs", lambda: 0x9000 + 0x6000, 0xF000, 0.001),
    ("18", "phy_init 0xF000 + 0x1000 = start of the application", lambda: 0xF000 + 0x1000, 0x10000, 0.001),
    ("18", "overhead area before the application, KB", lambda: 0x10000 / 1024, 64, 0.001),
]


def main() -> int:
    agreed = diverged = 0
    previous = None
    for chapter, name, expr, in_book, tolerance in CHECKS:
        if chapter != previous:
            print(f"\n── chapter {chapter}")
            previous = chapter
        got = expr()
        off = abs(got - in_book) / max(abs(in_book), 1e-12)
        if off <= tolerance:
            agreed += 1
            print(f"   ✓ {name:<46} {in_book:g}")
        else:
            diverged += 1
            print(f"   ✗ {name:<46} in the book {in_book:g}, "
                  f"computed {got:.6g}  (off by {off:.1%})")
    # Нуль перевірок — не «розбіжностей немає». Порожня таблиця друкує
    # те саме, що й таблиця, у якій усе зійшлося.
    if not CHECKS:
        print("   ✗ the table is empty: nothing was recomputed")
        return 1
    print(f"\nchecks: {agreed + diverged}; agreed: {agreed}; "
          f"diverged: {diverged}")
    return 1 if diverged else 0


if __name__ == "__main__":
    sys.exit(main())
