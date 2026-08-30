#!/usr/bin/env python3
"""Шар 1 над ОДИНИЦЯМИ реєстру — не над картками; пор. `layer1.py`.

Двоє їх не через недогляд. `layer1.py` питає, чи картка чесно подає
книгу читачеві, який книги не бачив; цей файл питає, чи одиниця
реєстру походить із книги. Перше — про подання, друге — про походження.
Перше знайшло 58 зламаних контекстів, яких друге не бачить у принципі.

Шар 1: чи справді одиниця реєстру — це те, що написано в книзі.

## Що вже було і чого бракувало

Реєстр **генерується** з книги (`factcheck.py sketch`), тож для прози
рівність тексту виходить сама собою. Доказ прив'язується хешем `sha`,
і правка формулювання відв'язує доказ — це ми бачили в дії, коли М1
переписав рядок про похибку DS18B20 і два докази відчепилися самі.

Отже шар 1 частково автоматичний. Але три дірки лишалися.

**Перша.** `factcheck.py stale` називається «записи, чий текст у книзі
змінився після останнього доказу», а перевіряє лише, **чи існує
файл**. Тобто інваріант вважався захищеним і не був захищений ніким —
той самий рід, що М1 знайшов у своїх `vorota`.

**Друга.** Над кожною одиницею стоїть заголовок «**Книга каже,
дослівно:**». Для прози це правда. Для **комірки таблиці** — ні:
книга каже

    | BME280 | `0x76`, `0x77` | ... |

а реєстр подає

    BME280 · Адреса → `0x76`, `0x77`

Це рендер, не цитата. Слово «дослівно» там неправдиве, і саме воно
породило рід хибної тривоги «комірка без контексту».

**Третя.** Ніщо не перевіряє, що сам **розбирач** не помилився. Якщо
він з'їсть половину речення чи зсуне номер рядка, реєстр буде
внутрішньо несуперечливий і невірний.

## Що робить цей скрипт

Для кожної одиниці бере `src:рядок` із самого реєстру, відкриває
книгу й питає:

* **проза** — чи стоїть текст одиниці в книзі дослівно;
* **комірка** — чи всі значення комірки трапляються в рядку книги;
* **будь-яка** — чи рядок узагалі існує (файл міг скоротитися).

    tools/layer1-m2.py [--vsi]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from repo import ROOT  # noqa: E402  (root is found, not counted)
GRUPY = ("manual", "dodatky", "kartky", "inserts")
RE_ZAH = re.compile(
    r"<!-- fc id:(\S+) sha:(\S+) src:(\S+?):(\d+) klas:(\S+) -->\n"
    r"### \S+ · (\S+) · [^\n]*\n\n\*\*Книга каже, дослівно:\*\*\n\n"
    r"((?:> [^\n]*\n)+)")


def normal(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main(argv: list[str]) -> int:
    vsi = "--vsi" in argv
    knyha: dict[str, list[str]] = {}
    knyha_ciле: dict[str, str] = {}
    zsuv: list[str] = []
    bidy: list[tuple[str, str, str]] = []
    n = proza = komirka = 0

    for g in GRUPY:
        for f in sorted((ROOT / "factcheck" / g).glob("*.md")):
            tekst = f.read_text(encoding="utf-8")
            for m in RE_ZAH.finditer(tekst):
                ident, sha, src, ln, klas, vyd, cyt = m.groups()
                n += 1
                p = ROOT / src
                if src not in knyha:
                    knyha[src] = (p.read_text(encoding="utf-8").split("\n")
                                  if p.exists() else [])
                ryadky = knyha[src]
                i = int(ln) - 1
                if not ryadky:
                    bidy.append((ident, "ФАЙЛУ НЕМАЄ", src))
                    continue
                if i >= len(ryadky):
                    bidy.append((ident, "РЯДКА НЕМАЄ (файл коротший)",
                                 "%s:%s, рядків %d" % (src, ln, len(ryadky))))
                    continue
                t = normal("\n".join(x[2:] for x in cyt.strip().split("\n")))
                # вікно: речення може займати кілька рядків книги
                vikno = normal(" ".join(ryadky[max(0, i - 1):i + 6]))
                # Два різні роди, і плутати їх дорого. Текст може бути
                # в книзі, але НЕ НА ТОМУ РЯДКУ — це не помилка тексту,
                # а застарілий рендер: книгу правили після нього, і всі
                # номери нижче правки зсунулися.
                #
                # Перший прогін дав 1317 «розбіжностей» саме так, і я
                # мало не доповів, що шістнадцять відсотків реєстру
                # хибні. Текст був на місці — зсунувся номер.
                cilyy = knyha_ciле.setdefault(src, normal(" ".join(ryadky)))
                if vyd == "proza":
                    proza += 1
                    if t in vikno:
                        pass
                    elif t in cilyy:
                        zsuv.append(ident)
                    else:
                        bidy.append((ident, "ТЕКСТУ НЕМАЄ В КНИЗІ ВЗАГАЛІ",
                                     t[:70]))
                elif vyd == "komirka":
                    komirka += 1
                    # значення комірки — те, що після стрілки
                    chastyny = [normal(x) for x in re.split(r"·|→", t) if normal(x)]
                    vtracheni = [c for c in chastyny if c not in vikno]
                    if vtracheni:
                        if all(c in cilyy for c in vtracheni):
                            zsuv.append(ident)
                        else:
                            bidy.append((ident, "КОМІРКА: значень немає в книзі",
                                         "; ".join(c for c in vtracheni
                                                   if c not in cilyy)[:70]))

    for ident, rid, det in (bidy if vsi else bidy[:25]):
        print("   %-12s %-34s %s" % (ident, rid, det))
    if not vsi and len(bidy) > 25:
        print("   ... ще %d" % (len(bidy) - 25))
    print("\nодиниць %d (проза %d, комірок %d)" % (n, proza, komirka))
    print("  текст на місці, зсунувся НОМЕР РЯДКА: %d — рендер застарів"
          % len(zsuv))
    print("  ТЕКСТУ НЕМАЄ В КНИЗІ: %d — оце справжня розбіжність"
          % len(bidy))
    return 1 if bidy else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
