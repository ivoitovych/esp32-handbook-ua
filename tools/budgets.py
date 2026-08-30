#!/usr/bin/env python3
"""Орієнтири обсягу (Р9, у редакції рішення Р9-а).

ЯКІСТЬ МАТЕРІАЛУ ВИЩА ЗА ОБСЯГ. Жоден факт не викидається з тексту через
те, що розділ переріс орієнтир. Ця перевірка нічого не забороняє: вона
показує, де текст розрісся, щоб автор подивився — там справді потрібна
кожна фраза чи туди заповзло повторення сусіднього розділу.

Тому вихідний код завжди 0: `make budgets` не ламає збирання.

Орієнтири:
  розділ (manual/)   орієнтир 1200–2500 слів, ~2 схеми
                     нижня межа перевірки — 600: це детектор заготовки,
                     а не вимога до обсягу
  картка (kartky/)   ~400 слів
  додаток (dodatky/) без межі: це довідкові таблиці

Одна сторінка картки — виняток, і це не бюджет, а фізична умова:
картка, що не влізла в аркуш A4, перестає бути карткою. Але вирішується
перевищення НЕ викиданням фактів, а поділом на дві картки або винесенням
глибини в додаток (Р10). Факт не зникає — він змінює місце.
"""

import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)

RE_FENCE = re.compile(r"^```")
RE_IMAGE = re.compile(r"!\[[^\]]*\]\([^)]+\)")

LIMITS = {
    "manual":  {"words": (600, 2500), "code": 8, "img": 2},
    "kartky":  {"words": (0, 400),     "code": 3, "img": 1},
    "dodatky": {"words": (0, 0),       "code": 99, "img": 99},
    "inserts": {"words": (0, 0),       "code": 99, "img": 99},
}


def measure(path: Path) -> tuple[int, int, int]:
    """→ (слів у прозі, блоків коду, зображень). Код у слова не рахується."""
    words = code = images = 0
    in_fence = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if RE_FENCE.match(line.lstrip()):
            in_fence = not in_fence
            if in_fence:
                code += 1
            continue
        if in_fence:
            continue
        images += len(RE_IMAGE.findall(line))
        line = re.sub(r"`[^`]*`", "", line)
        line = re.sub(r"\{#[a-z0-9-]+\}", "", line)
        if line.strip().startswith(":::"):
            continue
        words += len([w for w in re.split(r"\s+", line.strip()) if w])
    return words, code, images


def main() -> int:
    over = 0
    rows = []
    for group, lim in LIMITS.items():
        for f in sorted((ROOT / group).glob("*.md")):
            w, c, i = measure(f)
            lo, hi = lim["words"]
            max_code, max_img = lim["code"], lim["img"]
            # Проєкти ярусу 2 — це переважно код із поясненнями,
            # тому орієнтир на прозу до них не застосовується (Р9-а).
            if "-proj-" in f.name:
                lo, hi, max_code, max_img = 0, 0, 99, 99
            flags = []
            if hi and w > hi:
                flags.append(f"слів {w} > {hi}")
            if lo and w < lo:
                flags.append(f"слів {w} < {lo} — схоже, це ще заготовка")
            if c > max_code:
                flags.append(f"коду {c} > {max_code}")
            if i > max_img:
                flags.append(f"схем {i} > {max_img}")
            rows.append((str(f.relative_to(ROOT)), w, c, i, flags))
            if flags:
                over += 1

    width = max((len(r[0]) for r in rows), default=10)
    for name, w, c, i, flags in rows:
        mark = "!" if flags else "·"
        note = ("  " + "; ".join(flags)) if flags else ""
        print(f"  {mark} {name:<{width}}  слів {w:>5}  код {c}  схем {i}{note}")

    print(f"обсяги: файлів {len(rows)}, поза орієнтиром {over} "
          f"(це попередження, не помилка)")
    return 0


def check_card_pages() -> int:
    """Картка мусить вміщатися в одну сторінку A4 — рахуємо по зібраному PDF."""
    import yaml
    cfg = yaml.safe_load((ROOT / "book.yaml").read_text(encoding="utf-8"))
    files = [rel for part in cfg["targets"]["kartky"]["parts"]
             for rel in (part.get("files") or [])]
    pdf = ROOT / "build" / cfg["targets"]["kartky"]["output"]
    if not pdf.exists():
        print("  · PDF карток не зібрано — пропускаю перевірку сторінок")
        return 0
    data = pdf.read_bytes()
    pages = data.count(b"/Type /Page") - data.count(b"/Type /Pages")
    if pages <= 0:
        pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
    extra = pages - len(files)
    status = "!" if extra > 0 else "·"
    print(f"  {status} карток {len(files)}, сторінок у PDF {pages}"
          + (f" — перевищення на {extra}: поділити картку або винести "
             f"глибину в додаток, не викидати факти" if extra > 0 else ""))
    return 0


if __name__ == "__main__":
    rc = main()
    if "--pages" in sys.argv:
        rc |= check_card_pages()
    sys.exit(rc)
