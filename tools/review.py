#!/usr/bin/env python3
"""Механічні перевірки для сесії рецензування.

Знаходить те, що можна знайти автоматично, щоб читання йшло на суть, а не
на звірку структури. Нічого не виправляє — лише друкує знахідки.

    tools/review.py            усі перевірки
    tools/review.py --dubli    лише пошук повторів

Перевіряє:
  структура   заголовок, якір, підсумковий розділ
  посилання   на які розділи посилається кожен файл; неіснуючі номери
  повтори     однакові речення в різних файлах (Р10)
  блоки       незакриті ::: і невідомі класи
  таблиці     різна кількість колонок у рядках однієї таблиці
  мова        типові одруки й невідповідності термінології
  кирилиця    кирилична літера всередині латинського слова в блоці коду
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("kartky", "manual", "dodatky", "inserts")

RE_ANCHOR = re.compile(r"\{#([a-z0-9][a-z0-9-]*)\}")
RE_ROZDIL_REF = re.compile(r"\bрозділ(?:и|ів|ах|у|і)?\s+(\d{1,2})")
RE_KARTKA_REF = re.compile(r"\bкартк\w*\s+К(\d{1,2})")
RE_DIV = re.compile(r"^:::+\s*([a-z-]*)\s*$")

KLASY = {"zhyvlennya", "uvaha", "hrabli", "zakupivlya", "nezvorotne"}

# Пари «неправильно → правильно», що вже траплялися в тексті.
ODRUKY = [
    (r"психічн\w*\s+пам", "псевдостатична пам'ять (PSRAM)"),
    (r"\bна протязі\b", "протягом"),
    (r"\bв залежності\b", "залежно"),
    (r"\bпо замовчуванню\b", "за замовчуванням"),
    (r"\bна рахунок\b", "щодо"),
    (r"\bприймати участь\b", "брати участь"),
    (r"\bдійсно\b", "справді (якщо не про чинність)"),
    # «знаходиться» русизм лише у значенні «розташований»; як пасив від
    # «знаходити» («пристрій не знаходиться») це нормально. Тому шукаємо
    # саме локативні звороти.
    (r"знаходи(?:ть|мо)ся\s+(?:на|в|у|біля|поруч|усередині)\b",
     "перебуває / лежить / стоїть"),
    (r"\bслідуючий\b", "наступний"),
    (r"\bмісцезнаходження\b", "розташування"),
    (r"\bвиключення\b(?!\s+живлення)", "виняток"),
]


def fajly() -> list[Path]:
    out = []
    for g in GRUPY:
        out += sorted((ROOT / g).glob("*.md"))
    return out


def bez_kodu(text: str) -> str:
    """Текст без блоків коду й інлайнового коду — для мовних перевірок."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return re.sub(r"`[^`]*`", " ", text)


def rechennya(text: str) -> list[str]:
    text = bez_kodu(text)
    text = re.sub(r"^[#>|\-\*\s].*$", " ", text, flags=re.M)   # заголовки, списки, таблиці
    text = re.sub(r"\s+", " ", text)
    out = []
    for r in re.split(r"(?<=[.!?])\s+", text):
        r = r.strip()
        if len(r) > 60:
            out.append(r)
    return out


def perevirka_struktury(fs: list[Path]) -> list[str]:
    znaxidky = []
    for f in fs:
        t = f.read_text(encoding="utf-8")
        rel = str(f.relative_to(ROOT))
        rядки = t.splitlines()
        if not rядки or not rядки[0].startswith("# "):
            znaxidky.append(f"{rel}: перший рядок не заголовок рівня 1")
            continue
        if not RE_ANCHOR.search(rядки[0]):
            znaxidky.append(f"{rel}: у заголовку немає якоря {{#слаг}}")
        if (f.parent.name == "manual" and "-proj-" not in f.name
                and f.name != "00-pro-dovidnyk.md"):
            if "## Що з цього треба запам'ятати" not in t:
                znaxidky.append(f"{rel}: немає підсумкового розділу")
        if t.count("\n\n\n"):
            znaxidky.append(f"{rel}: подвійні порожні рядки")
    return znaxidky


def perevirka_posylan(fs: list[Path]) -> list[str]:
    znaxidky = []
    rozdily, kartky = set(), set()
    for f in fs:
        if f.parent.name == "manual":
            n = f.name.split("-", 1)[0]
            if n.isdigit():
                rozdily.add(int(n))
        if f.parent.name == "kartky":
            n = f.name[1:3]
            if n.isdigit():
                kartky.add(int(n))
    for f in fs:
        t = bez_kodu(f.read_text(encoding="utf-8"))
        rel = str(f.relative_to(ROOT))
        vlasnyj = int(f.name.split("-", 1)[0]) if (
            f.parent.name == "manual" and f.name.split("-", 1)[0].isdigit()) else None
        for m in RE_ROZDIL_REF.finditer(t):
            n = int(m.group(1))
            if n not in rozdily:
                znaxidky.append(f"{rel}: посилання на неіснуючий розділ {n}")
            elif n == vlasnyj:
                znaxidky.append(f"{rel}: посилання саме на себе (розділ {n})")
        for m in RE_KARTKA_REF.finditer(t):
            n = int(m.group(1))
            if n not in kartky:
                znaxidky.append(f"{rel}: посилання на неіснуючу картку К{n}")
    return znaxidky


def perevirka_blokiv(fs: list[Path]) -> list[str]:
    znaxidky = []
    for f in fs:
        rel = str(f.relative_to(ROOT))
        stack, fence = [], False
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                fence = not fence
                continue
            if fence:
                continue
            m = RE_DIV.match(line)
            if not m:
                continue
            if m.group(1):
                if m.group(1) not in KLASY:
                    znaxidky.append(f"{rel}:{i}: невідомий клас блоку «{m.group(1)}»")
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                znaxidky.append(f"{rel}:{i}: закриття ::: без відкриття")
        for i in stack:
            znaxidky.append(f"{rel}:{i}: блок не закрито")
    return znaxidky


def perevirka_tablyc(fs: list[Path]) -> list[str]:
    znaxidky = []
    for f in fs:
        rel = str(f.relative_to(ROOT))
        blok, start, fence = [], 0, False
        lines = f.read_text(encoding="utf-8").splitlines() + [""]
        for i, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                fence = not fence
            if fence:
                continue
            if line.startswith("|"):
                if not blok:
                    start = i
                blok.append(line)
                continue
            if blok:
                shyryny = {r.count("|") for r in blok}
                if len(shyryny) > 1:
                    znaxidky.append(
                        f"{rel}:{start}: у таблиці різна кількість колонок "
                        f"({sorted(shyryny)})")
                blok = []
    return znaxidky


def perevirka_movy(fs: list[Path]) -> list[str]:
    znaxidky = []
    for f in fs:
        t = bez_kodu(f.read_text(encoding="utf-8"))
        rel = str(f.relative_to(ROOT))
        for pat, zamina in ODRUKY:
            for m in re.finditer(pat, t, re.I):
                kontekst = t[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")
                znaxidky.append(f"{rel}: «{m.group(0)}» → {zamina}   …{kontekst}…")
    return znaxidky


RE_ZMISH = re.compile(r"[A-Za-z][а-щьюяїієґА-ЩЬЮЯЇІЄҐ]|[а-щьюяїієґА-ЩЬЮЯЇІЄҐ][A-Za-z]")


def perevirka_kyrylyci_v_kodi(fs: list[Path]) -> list[str]:
    """Кирилиця всередині латинського слова в блоці коду.

    Ловить те, чого око не бачить взагалі: кириличну «о» посеред URL або
    імені функції. Такий код компілюється або не компілюється, але читач
    не має жодного шансу зрозуміти, чому. Коментарі українською в коді
    сюди не потрапляють: там кирилиця не межує з латиницею впритул.
    """
    znaxidky = []
    for f in fs:
        rel = str(f.relative_to(ROOT))
        for blok in re.finditer(r"```.*?```", f.read_text(encoding="utf-8"), re.S):
            for ryadok in blok.group(0).split("\n"):
                m = RE_ZMISH.search(ryadok)
                if m:
                    znaxidky.append(f"{rel}: «{m.group(0)}» у рядку   {ryadok.strip()[:80]}")
    return znaxidky


def perevirka_povtoriv(fs: list[Path]) -> list[str]:
    """Однакові речення в різних файлах — кандидати на порушення Р10."""
    de = defaultdict(list)
    for f in fs:
        rel = str(f.relative_to(ROOT))
        for r in rechennya(f.read_text(encoding="utf-8")):
            de[r].append(rel)
    znaxidky = []
    for r, files in sorted(de.items()):
        unik = sorted(set(files))
        if len(unik) > 1:
            znaxidky.append(f"повтор у {', '.join(unik)}:\n      «{r[:110]}…»")
    return znaxidky


def main() -> int:
    fs = fajly()
    lyshe = sys.argv[1][2:] if len(sys.argv) > 1 else None

    bloky = [
        ("структура", perevirka_struktury),
        ("posylannya", perevirka_posylan),
        ("bloky", perevirka_blokiv),
        ("tablyci", perevirka_tablyc),
        ("mova", perevirka_movy),
        ("kyrylycya-v-kodi", perevirka_kyrylyci_v_kodi),
        ("dubli", perevirka_povtoriv),
    ]
    vsjogo = 0
    for nazva, fn in bloky:
        if lyshe and lyshe != nazva:
            continue
        z = fn(fs)
        vsjogo += len(z)
        print(f"\n── {nazva}: {len(z)}")
        for r in z[:60]:
            print(f"   • {r}")
        if len(z) > 60:
            print(f"   … і ще {len(z) - 60}")

    print(f"\nфайлів перевірено: {len(fs)}; знахідок: {vsjogo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
