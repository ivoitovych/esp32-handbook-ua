#!/usr/bin/env python3
"""Правописна перевірка українського тексту книги.

Навіщо. Дев'ять інструментів у `make check` перевіряють посилання, піни,
адреси, поля структур, обсяги, арифметику, авторство й листування — і
жоден не дивиться на орфографію. Для книги на 413 сторінок це не
дрібниця: **вичитка людиною — критичний шлях до друку**, і все, що можна
зняти механічно, знімається до неї, а не після.

Ця перевірка не замінює вичитки. Вона не бачить ані узгодження, ані
поганого стилю, ані слова, правильного за формою й не того за змістом.
Вона знімає з людини одну річ — механічну описку — і робить це на 50 000
слововживань за секунди.

    factcheck/tools/spelling.py            перелік невідомих слів за частотою
    factcheck/tools/spelling.py --файли    де саме кожне трапляється
    factcheck/tools/spelling.py --suvoro   ненульовий вихід, якщо є невідомі

## Що не перевіряється

Із тексту прибирається все, що не є українською прозою: блоки коду,
вміст зворотних лапок, посилання, HTML-коментарі, маркери сімейств
`[[S3]]`, YAML-шапки. Там живуть ідентифікатори, і словник про них
нічого не знає.

## Словник і чому його немає в репозиторії

`uk_UA` з LibreOffice — чужий матеріал (правило Р-КЕШ у
`docs/DESIGN.md`). Він завантажується в кеш і записується в маніфест із
`sha256`; сюди йде лише вказівка, звідки брати.

    factcheck/tools/cache.py https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.aff
    factcheck/tools/cache.py https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.dic

## Власний словник проєкту

`docs/slovnyk-proyektu.txt` — слова, яких немає в загальному словнику й
які в цій книзі правильні: терміни, транслітерації, назви. Він **у
репозиторії**, бо це наш текст, а не чужий.

Правило поповнення одне, і воно строге: слово додається туди тоді, коли
його перевірили, а не тоді, коли воно набридло в переліку. Словник, у
який зсипають усе незнайоме, перестає ловити описки — а описка в
терміні виглядає точно так само, як термін.
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
KESH = ROOT / "factcheck" / "source-cache"
VLASNYY = ROOT / "docs" / "slovnyk-proyektu.txt"
# `GRUPY` була вісьмома копіями того самого факту — теками цієї
# книги. Копії збігалися, і саме тому були небезпечні: набір копій
# не бреше, доки факт не зміниться, а тоді бреше всіма одразу.
# Тепер це дані: `factcheck/book.yaml`.
GRUPY = config.groups()

# Що вирізається з тексту перед перевіркою. Порядок має значення:
# спершу найбільші блоки, потім дрібні вкраплення.
PRYBRATY = [
    re.compile(r"^---\n.*?\n---\n", re.S),          # YAML-шапка
    re.compile(r"```.*?```", re.S),                  # блок коду
    re.compile(r"`[^`\n]*`"),                        # інлайн-код
    re.compile(r"<!--.*?-->", re.S),                 # коментар
    re.compile(r"\[\[[^\]]+\]\]"),                   # маркер сімейства
    re.compile(r"\]\([^)]*\)"),                      # ціль посилання
    re.compile(r"https?://\S+"),                     # URL
    re.compile(r"^:::.*$", re.M),                    # межа блоку
]

# Українське слово. Апостроф у всіх вживаних формах — частина слова.
SLOVO = re.compile(r"[А-ЯІЇЄҐа-яіїєґ][а-яіїєґ'’ʼʼ-]*")


def ochystyty(t: str) -> str:
    for p in PRYBRATY:
        t = p.sub(" ", t)
    return t


def slovnyk():
    """Hunspell через spylls; словник — із кешу джерел."""
    try:
        from spylls.hunspell import Dictionary
    except ImportError:
        sys.exit("немає spylls: pip install spylls")
    aff, dic = KESH / "uk_UA.aff", KESH / "uk_UA.dic"
    if not (aff.exists() and dic.exists()):
        sys.exit(
            "немає словника uk_UA в factcheck/source-cache/.\n"
            "  factcheck/tools/cache.py https://raw.githubusercontent.com/LibreOffice/"
            "dictionaries/master/uk_UA/uk_UA.aff\n"
            "  factcheck/tools/cache.py https://raw.githubusercontent.com/LibreOffice/"
            "dictionaries/master/uk_UA/uk_UA.dic")
    return Dictionary.from_files(str(KESH / "uk_UA"))


def vlasni() -> set[str]:
    if not VLASNYY.exists():
        return set()
    return {r.split("#")[0].strip().lower()
            for r in VLASNYY.read_text(encoding="utf-8").splitlines()
            if r.split("#")[0].strip()}


def main() -> int:
    d = slovnyk()
    svoyi = vlasni()
    nevidomi: collections.Counter[str] = collections.Counter()
    de: dict[str, set[str]] = collections.defaultdict(set)
    perevireno = 0

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            t = ochystyty(f.read_text(encoding="utf-8"))
            for m in SLOVO.finditer(t):
                w = m.group()
                if len(w) < 3:
                    continue
                perevireno += 1
                nyzhnye = w.lower()
                if nyzhnye in svoyi:
                    continue
                # Слово з великої на початку речення перевіряємо і як є,
                # і в нижньому регістрі: словник тримає власні назви
                # окремо, і «Живлення» не має ставати помилкою.
                if d.lookup(w) or d.lookup(nyzhnye):
                    continue
                nevidomi[nyzhnye] += 1
                de[nyzhnye].add(str(f.relative_to(ROOT)))

    pokazaty_fajly = "--файли" in sys.argv or "--files" in sys.argv
    for w, n in nevidomi.most_common():
        if pokazaty_fajly:
            fajly = ", ".join(sorted(de[w])[:3])
            hvist = f" +{len(de[w]) - 3}" if len(de[w]) > 3 else ""
            print(f"  {n:4}  {w:28} {fajly}{hvist}")
        else:
            print(f"  {n:4}  {w}")

    print(f"\nправопис: слововживань {perevireno}, невідомих слів "
          f"{len(nevidomi)} ({sum(nevidomi.values())} вживань), "
          f"власний словник {len(svoyi)}")
    if "--suvoro" in sys.argv and nevidomi:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
