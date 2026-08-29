#!/usr/bin/env python3
"""Чи не потрапив файл книги до кешу джерел.

## Навіщо

Кеш джерел і книга — дві протилежні речі: перше доводить друге. Файл
книги, що опинився в кеші, робить самопосилання **невидимим для всіх
трьох шарів**:

* джерело назване файлом із кешу — умова воріт виконана;
* цитата дослівно стоїть у названому файлі — шар 3 задоволений;
* взірець чіпляє одиницю — шар 1 задоволений.

І при цьому доказ доводить книгу книгою.

## Куплено

2026-08-28: у кеші знайшлося **сім файлів книги**, байт у байт —
`06-zhyvlennya.md`, `20-bekap.md`, `21-seriyna.md`,
`22-zberezhennya-stanu.md`, `23-triazh.md`, `31-freertos.md`,
`39-wifi.md`. Поклала їх хвиля 27 серпня, коли помічникам уперше
дозволили качати джерела самим: помічник «завантажив» файл книги.

Доказів, що на них спираються, було **нуль** — міна не вибухнула. Але
ворота її не бачили, і побачити не могли: за побудовою вони питають
«чи джерело у кеші», а не «чи джерело не є книгою».

## І окремо — маніфест

Перевіряти самі файли мало. **Джерелом книги може бути записаний сам
маніфест**: рядок із адресою
`raw.githubusercontent.com/<власник>/<книга>/main/manual/…` реєструє
книгу як зовнішнє джерело офіційно. Тоді кожне перезавантаження
відновлює файл, і прибирання з кешу не тримається.

Знайдено 2026-08-28: вісім таких рядків. Спершу я вилучив сім файлів
із кешу й вважав ваду закритою; наступне ж качання повернуло чотири,
бо адреси лишалися в маніфесті. **Прибирати наслідок, лишаючи
причину, — це не виправлення, а відкладення.**

## Чому за вмістом, а не за іменем

Ім'я можна змінити. Перевірка порівнює **sha256 вмісту**, тож копія
під іншим іменем теж знайдеться.

## І чому не лише за файлами на диску

Перша редакція дивилася тільки в каталог кешу. Файли з нього прибрали
— і вона показала нуль, тоді як **чотири рядки маніфесту й далі
називали книгу джерелом**:

    | `20-bekap.md` | … | <https://raw.githubusercontent.com/
                          ivoitovych/esp32-handbook-ua/main/manual/20-bekap.md> |

Маніфест — це те, що йде в git і що бачить третя сторона; файли не
йдуть узагалі. Тобто перевірка звітувала «чисто» саме про той бік,
який нікуди не подорожує, і мовчала про той, який подорожує.

> Рід 3 з каталогу, у власному виконанні: лічильник рахував не той
> артефакт. Ознака та сама — нуль, який нічого не означає.

Тому перевіряються обидва боки: вміст файлів **і** адреси в маніфесті.

    tools/cache_vs_book.py [--tykho]
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KESH = ROOT / "factcheck" / "source-cache"
KNYHA = ("manual", "dodatky", "kartky", "inserts")

# Адреса самого довідника. Довідник не є джерелом для себе — те саме
# правило, що вже стоїть у наряді помічникові.
VLASNE = re.compile(r"esp32-handbook|ivoitovych|voytovych", re.I)

# Шлях книги в будь-якому репозиторії: форк під іншим власником має ті
# самі каталоги.
ZA_SHLYAKHOM = re.compile(r"/(?:%s)/" % "|".join(KNYHA))


def main(argv: list[str]) -> int:
    tykho = "--tykho" in argv
    vidbytky: dict[str, str] = {}
    for g in KNYHA:
        katalog = ROOT / g
        if not katalog.exists():
            continue
        for p in katalog.glob("*.md"):
            vidbytky[hashlib.sha256(p.read_bytes()).hexdigest()] = str(
                p.relative_to(ROOT))

    # Маніфест: адреса на власну книгу реєструє її як джерело.
    manifest = KESH / "MANIFEST.md"
    ryadky_man = []
    if manifest.exists():
        tekst = manifest.read_text(encoding="utf-8")
        for ln in tekst.split("\n"):
            if re.search(r"raw\.githubusercontent\.com/[^/]+/[^/]+/"
                         r"\S*/(manual|dodatky|kartky|inserts)/", ln):
                m = re.search(r"\| `([^`]+)` \|", ln)
                ryadky_man.append(m.group(1) if m else ln[:60])

    znaydeno = []
    n = 0
    if KESH.exists():
        for p in sorted(KESH.iterdir()):
            if not p.is_file():
                continue
            n += 1
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            if h in vidbytky:
                znaydeno.append((p.name, vidbytky[h]))

    # Маніфест — єдине, що з кешу потрапляє в git. Самопосилання в
    # ньому переживає видалення файлу й **відновлює його** при
    # наступному качанні: причина живе тут, наслідок у каталозі.
    #
    # Дві ознаки, бо обидва супровідники написали цю перевірку
    # незалежно й кожен пропустив те, що бачив другий:
    #
    #   за шляхом  — `…/manual/…` у будь-якому репозиторії; ловить форк
    #                під чужим іменем власника;
    #   за іменем  — власне ім'я репозиторію; ловить адресу поза
    #                `raw.githubusercontent`, скажімо на реліз чи `docs/`.
    #
    # Жодна поодинці не покриває обидва випадки.
    v_manifesti = []
    manifest = KESH / "MANIFEST.md"
    if manifest.exists():
        for ln in manifest.read_text(encoding="utf-8").split("\n"):
            if not ln.startswith("| `"):
                continue
            m = re.search(r"<([^>]+)>", ln)
            url = m.group(1) if m else ""
            if ZA_SHLYAKHOM.search(url) or VLASNE.search(url):
                imya = re.search(r"\| `([^`]+)` \|", ln)
                v_manifesti.append((imya.group(1) if imya else ln[:60], url))

    for imya, dzherelo in znaydeno:
        print("   ✗ файл книги в кеші джерел: %s = %s" % (imya, dzherelo))
    for imya, url in v_manifesti:
        print("   ✗ маніфест реєструє книгу як джерело: %s → %s" % (imya, url))
    if not tykho or znaydeno or v_manifesti:
        print("cache_vs_book: файлів у кеші %d; файлів книги серед них %d; "
              "рядків маніфесту на книгу %d"
              % (n, len(znaydeno), len(v_manifesti)))
    return 1 if (znaydeno or v_manifesti) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
