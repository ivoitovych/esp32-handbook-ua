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

    tools/kesh-bez-knyhy.py [--tykho]
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KESH = ROOT / "dzherela-kesh"
KNYHA = ("manual", "dodatky", "kartky", "inserts")


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

    for imya in ryadky_man:
        print("   ✗ маніфест реєструє книгу як джерело: %s" % imya)
    for imya, dzherelo in znaydeno:
        print("   ✗ файл книги в кеші джерел: %s = %s" % (imya, dzherelo))
    if not tykho or znaydeno or ryadky_man:
        print("kesh-bez-knyhy: файлів у кеші %d; файлів книги серед них %d; "
              "рядків маніфесту на книгу %d"
              % (n, len(znaydeno), len(ryadky_man)))
    return 1 if (znaydeno or ryadky_man) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
