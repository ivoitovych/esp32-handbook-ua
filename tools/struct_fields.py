#!/usr/bin/env python3
"""Перевірка імен полів структур ESP-IDF у прикладах книги.

Що перевіряється. Кожне `.field = …` у прикладах C зіставляється з
переліком полів відповідної структури, знятим із заголовків ESP-IDF
(`tools/kod-stubs.py`, словник `STRUKT`). Поле, якого в структурі немає,
— це код, що не збереться в читача.

Чому саме так, а не компіляцією. Спроба зібрати приклади цілком
(`tools/kod.py`) не дійшла до придатної якості: приклади в книзі —
фрагменти, які спираються на змінні з сусіднього блоку й на прозу, і
компілятор тоне в наслідках відсутнього контексту. Перевірка, що глушить
ці наслідки достатньо широко, перестає бачити й справжні вади —
випробування підкинутою помилкою це показало прямо.

Тому взято вужчу задачу, яка **повністю** розв'язується без контексту:
ім'я поля не залежить ні від чого, крім самої структури.

Межа названа чесно: тут не перевіряються ні типи, ні синтаксис, ні
значення. Лише імена полів — і лише тих структур, що перелічені в
`STRUKT`.

    tools/struct_fields.py        перевірити
    tools/struct_fields.py -v     показати всі знайдені пари структура → поле
"""

import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
GRUPY = ("kartky", "manual", "dodatky", "inserts")

RE_BLOK = re.compile(r"```c\n(.*?)```", re.S)
# `i2c_master_bus_config_t bus_cfg = { … };` — тип, ім'я, тіло.
RE_INIT = re.compile(
    r"\b([a-z_][a-z0-9_]*_t)\s+\w+\s*=\s*\{(.*?)\n\s*\}", re.S)
RE_POLE = re.compile(r"\.([a-zA-Z_]\w*(?:\.\w+)*)\s*=")


def dozvoleni() -> dict[str, set[str]]:
    """Поля структур із генератора заглушок — тобто із заголовків ESP-IDF."""
    sys.path.insert(0, str(ROOT / "tools"))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "kod_stubs", ROOT / "tools" / "kod-stubs.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    out: dict[str, set[str]] = {}
    for typ, polya in m.STRUKT.items():
        imena = set()
        for p in polya:
            # «int sda_io_num» → sda_io_num; «struct { … } flags» → flags
            # плюс вкладені імена, щоб `.flags.enable_internal_pullup` теж
            # мало що звіряти.
            imena |= set(re.findall(r"(\w+)\s*(?:\[[^\]]*\])?\s*;", p))
            # Поле-вказівник на функцію: `esp_err_t (*handler)(…)`.
            imena |= set(re.findall(r"\(\s*\*\s*(\w+)\s*\)", p))
            m2 = re.search(r"\}\s*(\w+)$", p.strip())
            if m2:
                imena.add(m2.group(1))
            else:
                m3 = re.search(r"(\w+)\s*(?:\[[^\]]*\])?$", p.strip())
                if m3:
                    imena.add(m3.group(1))
        out[typ] = imena
    return out


def main() -> int:
    struktury = dozvoleni()
    zhahy, perevireno = [], 0

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            rel = str(f.relative_to(ROOT))
            for mb in RE_BLOK.finditer(text):
                bazovyy = text[:mb.start()].count("\n") + 2
                for mi in RE_INIT.finditer(mb.group(1)):
                    typ, tilo = mi.group(1), mi.group(2)
                    if typ not in struktury:
                        continue           # тип книги або не в переліку
                    ln = bazovyy + mb.group(1)[:mi.start()].count("\n")
                    for mp in RE_POLE.finditer(tilo):
                        shlyakh = mp.group(1)
                        perevireno += 1
                        korin = shlyakh.split(".")[0]
                        if "-v" in sys.argv:
                            print(f"  {rel}:{ln} {typ}.{shlyakh}")
                        if korin not in struktury[typ]:
                            zhahy.append(
                                f"{rel}:{ln}: у `{typ}` немає поля "
                                f"`{korin}` (з `.{shlyakh}`)")

    for z in zhahy:
        print(f"   • {z}")
    print(f"struct_fields: структур у переліку {len(struktury)}, "
          f"перевірено полів {perevireno}, помилок {len(zhahy)}")
    return 1 if zhahy else 0


if __name__ == "__main__":
    sys.exit(main())
