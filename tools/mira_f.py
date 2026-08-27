#!/usr/bin/env python3
"""Міра класу `F`: скільки незвіреного справді хибне.

## Навіщо це окремо від міри класу `E`

Питання різні, і плутати їх дорого.

Клас `E` мав **присуд**: «зовнішнього джерела не існує». Міра `E`
випробовувала присуд — чи правда, що не існує.

Клас `F` присуду не має взагалі. Це просто нероблена робота: до цих
рядків ніхто не дійшов. Тому й питання пряме — **чи правильне те, що
написано в книзі**, — і серед вердиктів з'являється той, якого в наряді
на `E` не було: `sperechayetsya`.

Саме він і є метою. Усе інше — облік.

## Що дає випадкова вибірка тут

Число, якого в книги досі не було: **частка помилок серед незвіреного**.

Книга друкує, що звірено стільки-то відсотків, і чесно каже, що решта
не звірена. Але «не звірено» мовчить про те, скільки там хибного.
Читач має право знати, чи це один відсоток, чи двадцять.

Оцінку можна перенести на всю популяцію `F` саме тому, що вибірка
випадкова — і **тільки** тому. Відсоток із наряду, зібраного рукою,
такого права не дає (див. `factcheck/SCHEMA.md`, «Чим `E` небезпечний»).

## Чому заявлене спростування перевіряється двічі

Помічник під тиском «знайди помилку» виробляє помилки так само справно,
як під тиском «знайди джерело» виробляв джерела: за один вечір їх
заявили 18 і підтвердилося **нуль**.

Тому кожне `sperechayetsya` проходить третій шар (чи стоїть цитата в
документі) і **особисту звірку супровідника** (чи вона про це). Жодне
не потрапляє у звіт як знахідка, доки не пройшло обидва.

    tools/mira_f.py <каталог-вивантажень>
"""
from __future__ import annotations

import collections
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import yaml  # noqa: E402

import vyvantazh  # noqa: E402

ZVIT = ROOT / "factcheck" / "MIRA-F.md"
KANDYDATY = ROOT / "factcheck" / "mira-f-kandydaty.yaml"

PIDPYSY = {
    "pidtverdzheno": "Книга підтверджена",
    "sperechayetsya": "Джерело сперечається з книгою",
    "ne_znayshov": "Документ є, місця немає",
    "nedosyazhne": "Документ звідси недосяжний",
}


def promizhok(k: int, n: int) -> tuple[float, float]:
    """Вілсонів проміжок 95%. Біля нуля нормальний бреше."""
    if not n:
        return (0.0, 0.0)
    p, z = k / n, 1.96
    seredyna = (p + z * z / (2 * n)) / (1 + z * z / n)
    pivshyryna = (z / (1 + z * z / n)) * math.sqrt(
        p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, seredyna - pivshyryna), min(1.0, seredyna + pivshyryna))


def populyaciya() -> int:
    import vybirka
    return len(vybirka.odynyci("F"))


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    zap, polagodzheni, zlamani = vyvantazh.chytaty(Path(sys.argv[1]))
    n = len(zap)
    if not n:
        print("mira_f: вивантажень не знайдено")
        return 1
    c = collections.Counter(str(z.get("verdykt", "?")) for z in zap)

    # Третій шар — на все, що має цитату, а не лише на спростування.
    kand = [{"nazva": str(z.get("odynycya", "?")),
             "dzherelo": str(z.get("dzherelo", "")).strip(),
             "cytata": str(z.get("cytata", "")),
             "verdykt": str(z.get("verdykt", "")),
             "zvidky": z.get("_fayl", "?")}
            for z in zap if str(z.get("cytata", "")).strip()]
    KANDYDATY.write_text(
        "# Кандидати з міри класу `F`. **Не реєстр.**\n"
        + yaml.safe_dump(kand, allow_unicode=True, sort_keys=False),
        encoding="utf-8")

    stany: dict[str, str] = {}
    if kand:
        try:
            import citaty
            naslidky, _ = citaty.perevirka(True, [KANDYDATY])
            stany = {str(x.get("nazva")): str(x.get("stan"))
                     for x in naslidky}
        except ImportError:
            pass

    sperech = [z for z in zap if str(z.get("verdykt")) == "sperechayetsya"]
    sperech_ok = [z for z in sperech
                  if stany.get(str(z.get("odynycya"))) == "ok"]
    pop = populyaciya()
    nyz, verh = promizhok(len(sperech_ok), n)

    r = [f"""# Міра класу `F` — скільки незвіреного справді хибне

**Генерується** `tools/mira_f.py`. Наряд —
`factcheck/NARYAD-vybirka.md`, там же насіння добору.

Клас `F` — «ще не звірено»: до цих рядків ніхто не дійшов. Питання не
про присуд, а пряме: **чи правильне те, що написано в книзі**.

Вибірка **випадкова**, тож частку можна переносити на всю популяцію
`F` — і лише тому.

## Результат

Відповідей: **{n}** із {pop} одиниць класу `F`.

| Вердикт | Скільки | Частка |
|---|---|---|"""]
    for k in ("pidtverdzheno", "sperechayetsya", "ne_znayshov",
              "nedosyazhne"):
        v = c.get(k, 0)
        r.append(f"| {PIDPYSY[k]} | {v} | {v / n:.0%} |")
    r.append("")

    r.append(f"""
## Спростування: заявлено {len(sperech)}, витримало третій шар {len(sperech_ok)}

Заявлене спростування — **ще не знахідка**. Помічник під тиском «знайди
помилку» виробляє помилки так само справно, як під тиском «знайди
джерело» виробляв джерела: за один вечір їх заявили 18 і підтвердилося
нуль.

Тому кожне проходить дві перевірки: машинну (чи стоїть цитата в
документі) і особисту (чи вона про це). Нижче — ті, що пройшли першу.
Другу робить супровідник, і доти жодне не є підставою правити книгу.
""")

    if sperech_ok:
        r.append("| Одиниця | Джерело | Що каже |")
        r.append("|---|---|---|")
        for z in sperech_ok:
            dz = str(z.get("dzherelo", "")).strip()
            r.append(f"| `{z.get('odynycya', '?')}` "
                     f"| [`{dz.rsplit('/', 1)[-1]}`]({dz}) "
                     f"| {str(z.get('komentar', '')).strip()[:120]} |")
        r.append("")
        r.append(f"\nЯкщо всі вони підтвердяться по суті, частка помилок "
                 f"серед незвіреного — **{len(sperech_ok) / n:.1%}** "
                 f"(95% Вілсон: {nyz:.1%}–{verh:.1%}), тобто близько "
                 f"**{round(len(sperech_ok) / n * pop)}** одиниць на весь "
                 f"клас `F`.\n")
    else:
        r.append("Жодне заявлене спростування третій шар не витримало.\n")

    if polagodzheni:
        r.append("\nПолагоджено механічно: "
                 + ", ".join(f"`{b}`" for b in polagodzheni) + ".\n")
    if zlamani:
        r.append("\nНе розібралися й пропущені: "
                 + ", ".join(f"`{b}`" for b in zlamani) + ".\n")

    ZVIT.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"mira_f: відповідей {n}, спростувань заявлено {len(sperech)}, "
          f"витримали шар 3 {len(sperech_ok)} → {ZVIT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
