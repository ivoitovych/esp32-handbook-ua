#!/usr/bin/env python3
"""Перебудувати холості взірці з тексту ОДИНИЦІ РЕЄСТРУ.

## Чому холостими вони стають

Взірець пишеться під розмітку книги, а зіставляється з рендером
реєстру. Для прози це те саме; для комірки таблиці — ні:

    книга:   | `0xf` | RTCWDT_BROWN_OUT_RESET | просіло живлення |
    реєстр:  0xf · Причина → просіло живлення

Взірець із рисками збігається з книгою й не збігається ні з чим у
реєстрі. Доказ живий на вигляд і мертвий насправді: він обіцяє
звіреність, якої немає.

Моїх таких 44 знайшов М1 новою половиною `vorota`; ще 16 я зробив сам
того ж дня, зібравши взірець із НАЗВИ ЗАПИСУ замість тексту одиниці.
Назва запису — це мій підпис, а не текст книги; збігтися з реєстром
вона може лише випадково.

## Що робить цей скрипт

Для кожного холостого запису шукає одиницю реєстру, до якої він
насправді стосується, і будує взірець із її тексту: екранує як текст,
пробіли робить гнучкими. Кандидата обирає за часткою спільних лексем
із назвою запису й цитатою, і бере лише тоді, коли перевага одного
кандидата над наступним переконлива.

Нічия — не привід відступати, а привід придивитися. З 59 холостих 26
не мали одного переможця, і в усіх причина була однакова й законна:
**запис навмисне накриває кілька одиниць**. Один доказ на MAX31855 і
MAX6675 однаково стосується обох рядків таблиці:

    MAX31855 · Що дає → термопара
    MAX6675 · Що дає → термопара, дешевший

Для цього в `zbih` і є альтернативи. Тому при нічиї будується
альтернація по всіх кандидатах, що йдуть урівень із першим, — не
вибір навмання, а покриття.

Чого НЕ робить: не вгадує. Якщо жоден кандидат не дотягує до порога,
запис лишається холостим і друкується в переліку. Мовчазна прив'язка
не до тієї одиниці гірша за холостий взірець — холостий видно, а
хибну прив'язку ні.

    tools/patterns_repair.py            показати, що зробить
    tools/patterns_repair.py --pysaty   записати
"""
from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import yaml  # noqa: E402
import factcheck  # noqa: E402
import sample  # noqa: E402

LEKSEMA = re.compile(r"[0-9A-Za-zА-Яа-яЇїІіЄєҐґ_.\-]{3,}")
POROG = 0.34      # мінімальна частка спільних лексем
KONTROLNI = ("ESP32 має два ядра", "Зовсім інший текст про каву", "12345")


def leksemy(s: str) -> set[str]:
    return {w.lower() for w in LEKSEMA.findall(s or "")}


def slova_vzirtsya(v: str) -> set[str]:
    """Літеральні слова зі старого взірця, без регулярної машинерії."""
    t = re.sub(r"\\([|.*+?()\[\]{}^$])", r"\1", v)   # зняти екранування
    t = re.sub(r"\\s\+|\\s\*|\.\*|\.\+|\[[^\]]*\]|[|()?*+{}^$]", " ", t)
    return leksemy(t)


def vzirets_z(tekst: str) -> str:
    yadro = re.sub(r"\s+", " ", tekst.strip())[:110].rstrip(" .,;:—-")
    return re.escape(yadro).replace(r"\ ", r"\s+")


def main(argv: list[str]) -> int:
    pysaty = "--pysaty" in argv

    odynyci = []
    # Був рядок "ABCDEFG" — власна копія переліку класів, яка вже
    # не мала `K` і `L` і не дістала б `S`. Саме про це попереджає
    # коментар при `ALL_CLASSES`: копія переліку — така сама обіцянка
    # не міняти його, як копія взірця.
    for klas in factcheck.ALL_CLASSES:
        for o in sample.odynyci(klas):
            odynyci.append((o["tekst"], leksemy(o["tekst"])))

    teksty = [t for t, _ in odynyci]
    zhyvi = set()
    for z in factcheck.zavantazhyty_dokazy():
        v = str(z.get("match") or "")
        if not v:
            continue
        try:
            rx = re.compile(v)
        except re.error:
            continue
        if any(rx.search(t) for t in teksty):
            zhyvi.add((str(z.get("_prokhid")), str(z.get("title"))))

    polagodzheno = nezmineno = 0
    for shlyakh in sorted(glob.glob(str(ROOT / "factcheck" / "evidence" / "m2-*.yaml"))):
        recs = yaml.safe_load(Path(shlyakh).read_text(encoding="utf-8")) or []
        prokhid = Path(shlyakh).stem
        tor = False
        for r in recs:
            if not isinstance(r, dict) or not r.get("match"):
                continue
            if (prokhid, str(r.get("title"))) in zhyvi:
                continue
            klyuch = slova_vzirtsya(str(r.get("match", "")))
            if len(klyuch) < 3:
                klyuch |= leksemy(str(r.get("title", "")))
            if not klyuch:
                continue
            ocinky = sorted(
                ((len(klyuch & lk) / max(1, len(klyuch)), t) for t, lk in odynyci),
                key=lambda p: -p[0])
            o1 = ocinky[0][0]
            if o1 < POROG:
                nezmineno += 1
                print("   ? %-26s %s" % (prokhid[:26], str(r.get("title"))[:48]))
                continue
            # Урівень із першим — усе, що не гірше за 95 % його оцінки.
            urnyven = [t for o, t in ocinky if o >= o1 * 0.95][:4]
            novyy = "|".join(vzirets_z(t) for t in urnyven)
            # Взірець мусить компілюватися й не збігатися з чужим текстом.
            try:
                rx = re.compile(novyy)
            except re.error:
                nezmineno += 1
                continue
            if all(rx.search(k) for k in KONTROLNI):
                nezmineno += 1
                continue
            # Писати ОБИДВА імені, поки переїзд не скінчено.
            #
            # Саме тут народилися 15 розходжень `zbih`/`match`: цей
            # інструмент звужував `zbih` і не чіпав `match`, а в
            # `match` лишалася теча. Дані я звірив 2026-08-28, але
            # звірити наслідок і лишити причину — це відкласти, а не
            # полагодити. Прибрати цей рядок можна лише разом із
            # прогоном `field_names.py --stysnuty`.
            r["zbih"] = r["match"] = novyy
            if len(urnyven) > 1:
                print("      (альтернація на %d одиниць)" % len(urnyven))
            r["notatka"] = r["note"] = (
                str(r.get("note", "") or "").strip() +
                " | Взірець перебудовано з тексту одиниці реєстру "
                "2026-08-27: попередній писався під розмітку книги "
                "(риски таблиці) і не чіпав нічого.").strip(" |")
            polagodzheno += 1
            tor = True
            print("   ✓ %-26s %s" % (prokhid[:26], str(r.get("title"))[:48]))
        if tor and pysaty:
            Path(shlyakh).write_text(
                yaml.dump(recs, allow_unicode=True, sort_keys=False,
                          default_flow_style=False, width=100), encoding="utf-8")

    print("\nперебудовано %d; кандидата не видно для %d%s"
          % (polagodzheno, nezmineno, "" if pysaty else "  (проба, нічого не записано)"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
