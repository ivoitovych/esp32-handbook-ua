#!/usr/bin/env python3
"""Третій шар: чи справді цитата стоїть у названому джерелі.

## Навіщо цей шар окремо

Фактчекінг має три різні відмови, і жодна з них не ловить дві інші.

    1. книга → запис     твердження існує, запису на нього немає
    2. цитата → твердження   цитата справжня, але доводить не те
    3. джерело → цитата   цитати в джерелі немає взагалі

Перші два шари вимагають розуміння: перший — чи охоплено все, другий —
чи підпирає цей уривок саме це твердження. Третій не вимагає нічого,
крім `curl` і пошуку підрядка, — і саме тому має бути **скриптом**.

Вигода не в тому, що скрипт дешевший. Вона в тому, що модель, яка
збирає докази, більше не мусить бути сильною. Слабка модель помиляється
передбачувано: переказує замість цитувати, зшиває два речення в одне,
переставляє слова, вигадує правдоподібне. **Кожну з цих відмов третій
шар ловить механічно.** Тож збирання можна віддати найдешевшій моделі,
а дорогу увагу лишити другому шарові, де вона незамінна.

## Що саме перевіряється

З поля `cytata` беруться **придатні уривки**: рядки без кирилиці (наші
власні примітки — кирилицею), без багатокрапки (там вирізано текст) і
довші за `MIN_DOVZHYNA`. Сусідні такі рядки зливаються в абзац, бо ми
переносимо довгі рядки джерела при записі, а джерело їх не переносить.

Далі і абзац, і текст джерела зводяться до одного пробілу між словами —
після цього залишається звичайний пошук підрядка.

## Чого цей шар **не** каже

Він не каже, що доказ правильний. Цитата може бути дослівною й не
стосуватися твердження — це другий шар, і його робить людина.

Він не каже, що джерело авторитетне. `raw.githubusercontent.com` віддає
будь-чий репозиторій.

Він каже рівно одне: **цей текст справді стоїть за цією адресою.**

    tools/citaty.py            перевірити все, що є в кеші
    tools/citaty.py --kachaty  спершу докачати те, чого бракує
    tools/citaty.py --zvit     згенерувати factcheck/CYTATY.md
    tools/citaty.py --suvoro   недосяжне джерело теж помилка
    tools/citaty.py <файл.yaml>  перевірити вивантаження помічника

Останнє — головне для роботи з пулом. Помічник кладе зібране у
власний файл, цей скрипт його звіряє, і лише те, що пройшло, розглядає
супровідник. Чуже слово не потрапляє в реєстр неперевіреним ніколи.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOKAZY = ROOT / "factcheck" / "dokazy"
KESH = ROOT / "dzherela-kesh"
ZVIT = ROOT / "factcheck" / "CYTATY.md"

MIN_DOVZHYNA = 12

# Розширення, які читаються як текст без перетворення. PDF потребує
# `pdftotext`; якщо його немає, файл оголошується неперевірним — і це
# чесніший стан, ніж мовчазний пропуск.
TEKSTOVI = {".rst", ".h", ".c", ".cpp", ".py", ".inc", ".csv", ".md",
            ".txt", ".yaml", ".yml", ".json", ".kconfig", ".projbuild",
            ".cmake", ".ld", ".s", ".in", ""}

RE_URL = re.compile(r"https?://[^\s,;)\"'<>]+")
RE_KYRYLYCYA = re.compile(r"[а-яїієґА-ЯЇІЄҐ]")
RE_PROPUSK = re.compile(r"…|\.\.\.")
# Рядок, що цілком узятий у дужки, — наша позначка, звідки уривок:
# `(esp32c3.inc)`, `(i2c_master.c:1049)`, `(basic-commands.rst)`. Вона
# не лише не є частиною джерела — вона ще й **склеювала** б сусідні
# рядки в один абзац, і тоді не знаходився б жоден.
RE_POZNACHKA = re.compile(r"^\([^()]*\)$")


def rozgornuty(url: str) -> list[str]:
    """Розгорнути `{a,b,c}` у URL на окремі адреси.

    Так записано десяток доказів, де одне твердження звірене по трьох
    сімействах одразу: `.../gpio/{esp32,esp32s3,esp32c3}.inc`. Форма
    зручна для читача й непридатна для `curl`.
    """
    m = re.search(r"\{([^{}]*)\}", url)
    if not m:
        return [url]
    out = []
    for chastyna in m.group(1).split(","):
        out += rozgornuty(url[:m.start()] + chastyna.strip() + url[m.end():])
    return out


def imya_dlya(url: str) -> str:
    """Ім'я файлу в кеші, унікальне за URL.

    Базове ім'я збігається надто часто — у дереві ESP-IDF десятки файлів
    `esp32.inc` і сотні `*.h`. Тому до нього додається короткий хеш
    повного URL: ім'я лишається читним, а зіткнення зникають.
    """
    baza = re.sub(r"[^\w.-]", "_", url.rsplit("/", 1)[-1] or "bez-imeni")
    return f"{hashlib.sha256(url.encode()).hexdigest()[:8]}-{baza}"[:96]


def zavantazhyty(url: str, cil: Path) -> bool:
    KESH.mkdir(exist_ok=True)
    r = subprocess.run(["curl", "-sSL", "--fail", "--max-time", "40",
                        "-o", str(cil), url],
                       capture_output=True)
    return r.returncode == 0 and cil.exists() and cil.stat().st_size > 0


def tekst_dzherela(p: Path) -> str | None:
    if p.suffix.lower() == ".pdf":
        r = subprocess.run(["pdftotext", "-q", str(p), "-"],
                           capture_output=True)
        if r.returncode != 0:
            return None
        return r.stdout.decode("utf-8", "replace")
    if p.suffix.lower() not in TEKSTOVI:
        return None
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def plaskyy(s: str) -> str:
    """Один пробіл між словами, решта як є.

    Свідомо **не** чіпаємо ні регістр, ні лапки, ні тире. Цитата, яка
    збігається лише після приведення регістру, — це вже переказ, і хай
    вона падає: доказ мусить бути дослівним.
    """
    return re.sub(r"\s+", " ", s).strip()


def uryvky(cytata: str) -> list[list[str]]:
    """Придатні до перевірки групи рядків цитати.

    Відкидаємо: наші примітки (кирилиця), місця з вирізаним текстом
    (багатокрапка), позначки джерела в дужках і надто короткі рядки,
    які збіглися б із чим завгодно.

    Повертаємо **групи рядків**, а не злитий текст, бо перевіряти
    доводиться двома способами (див. `znayty`).
    """
    grupy: list[list[str]] = [[]]
    for ryadok in cytata.splitlines():
        r = ryadok.strip()
        pryydatnyy = (
            r
            and not RE_KYRYLYCYA.search(r)
            and not RE_PROPUSK.search(r)
            and not RE_POZNACHKA.match(r)
            and len(r) >= MIN_DOVZHYNA
        )
        if pryydatnyy:
            grupy[-1].append(r)
        elif grupy[-1]:
            grupy.append([])
    return [g for g in grupy if g]


def znayty(grupa: list[str], teksty: list[str]) -> list[str]:
    """Які рядки групи не знайшлися в жодному з джерел.

    Два способи, і потрібні обидва, бо ми цитуємо двома способами.

    **Злитою групою** — коли ми перенесли довгий рядок джерела на два
    своїх. Тоді жоден наш рядок окремо в джерелі не стоїть, а разом
    вони стоять дослівно.

    **Порядково** — коли ми зібрали уривок із **різних місць** файлу:
    `#define IO_MUX_GPIO11_REG` із рядка 107 і `PERIPHS_IO_MUX_VDD_SPI_U`
    із рядка 223. Разом вони не стоять ніде, і це не вада цитати, а
    звичайний спосіб показати два пов'язані означення поруч.

    Спершу пробуємо злиту: вона строгіша, бо вимагає ще й порядку.
    """
    ciline = plaskyy(" ".join(grupa))
    if any(ciline in t for t in teksty):
        return []
    return [r for r in grupa
            if not any(plaskyy(r) in t for t in teksty)]


RE_SKOROCHENNYA = re.compile(r"(?<![\w/])\.\.\./(\S+)")


def korin_dlya(povnyy: str, skorocheno: str) -> str | None:
    """Корінь дерева, проти якого розгортається скорочення.

    Рахувати сегменти адреси не можна: гілка `release/v5.5` містить
    скісну риску, і `owner/repo/ref` виявляється то трьома сегментами,
    то чотирма. Перша спроба це робила й мовчки давала неробочі адреси.

    Надійніше запитати саме скорочення. Його перший сегмент —
    `components`, `docs`, `tools` — це каталог, який є і в повній
    адресі. Ріжемо повну там, де він починається, і корінь виходить
    правильним незалежно від того, скільки скісних рисок у назві гілки.
    """
    persh = skorocheno.lstrip("/").split("/", 1)[0]
    if not persh:
        return None
    i = povnyy.find(f"/{persh}/")
    return povnyy[:i + 1] if i > 0 else None


def dzherela_zapysu(z: dict) -> list[str]:
    """Усі адреси запису, з розгорнутими скороченнями.

    У полі `dzherelo` другий і подальші файли того самого дерева
    записані скорочено — `.../components/soc/esp32c3/...` — бо повний
    URL повторює шістдесят символів на кожен рядок і робить запис
    нечитним.

    Для людини це зрозуміло. Для шару 3 — ні: скорочення не адреса, і
    доказ із ним неперевірний **мовчки**. Це виявив сам шар 3, щойно
    його запустили: чверть записів з цитатами не мала жодного придатного
    URL, і виглядало це як «джерело не в кеші».

    Тому скорочення розгортається проти кореня першої повної адреси.
    Для `raw.githubusercontent.com` корінь — це власник, репозиторій і
    гілка; далі йде шлях у дереві, і саме його заміняє `...`.
    """
    syryy = str(z.get("dzherelo") or "")
    povni = RE_URL.findall(syryy)
    out: list[str] = []
    for u in povni:
        out += rozgornuty(u.rstrip(".,"))
    for m in RE_SKOROCHENNYA.finditer(syryy):
        hvist = m.group(1).lstrip("/").rstrip(".,")
        korin = next((k for u in povni if (k := korin_dlya(u, hvist))), None)
        if korin:
            out += rozgornuty(korin + hvist)
    return out


def perevirka(kachaty: bool,
              fayly: list[Path] | None = None) -> tuple[list[dict],
                                                        dict[str, int]]:
    """Кожен запис доказу проти кожного зі своїх джерел.

    `fayly` дозволяє перевірити щось, чого в реєстрі ще немає, — а саме
    вивантаження помічника. Так перевірка стається **до** того, як чуже
    слово потрапляє в `factcheck/dokazy/`, а не після.
    """
    naslidky: list[dict] = []
    pidsumok = {"ok": 0, "ne_znaydeno": 0, "nedosyazhne": 0, "nichoho": 0}
    kesh_tekstu: dict[str, str | None] = {}

    for f in (fayly if fayly is not None else sorted(DOKAZY.glob("*.yaml"))):
        try:
            zapysy = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except yaml.YAMLError as e:
            naslidky.append(dict(fayl=f.name, nazva="(файл не читається)",
                                 stan="pomylka", detali=str(e).split("\n")[0]))
            continue
        for z in zapysy:
            if not isinstance(z, dict):
                continue
            nazva = str(z.get("nazva", "?"))
            frahmenty = uryvky(str(z.get("cytata") or ""))
            urly = dzherela_zapysu(z)
            if not frahmenty or not urly:
                pidsumok["nichoho"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nichoho",
                    detali=("немає URL" if frahmenty else
                            "немає придатних уривків")))
                continue

            teksty: list[str] = []
            nedosyazhni: list[str] = []
            for u in urly:
                if u not in kesh_tekstu:
                    cil = KESH / imya_dlya(u)
                    if not cil.exists() and kachaty:
                        zavantazhyty(u, cil)
                    kesh_tekstu[u] = (plaskyy(tekst_dzherela(cil) or "")
                                      if cil.exists() else None) or None
                if kesh_tekstu[u]:
                    teksty.append(kesh_tekstu[u])
                else:
                    nedosyazhni.append(u)

            if not teksty:
                pidsumok["nedosyazhne"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nedosyazhne",
                    detali=f"{len(nedosyazhni)} джерел не в кеші"))
                continue

            vsjogo_ryadkiv = sum(len(g) for g in frahmenty)
            promakhy: list[str] = []
            for grupa in frahmenty:
                promakhy += znayty(grupa, teksty)
            if promakhy:
                pidsumok["ne_znaydeno"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ne_znaydeno",
                    detali=f"{len(promakhy)} з {vsjogo_ryadkiv} рядків",
                    promakhy=promakhy[:3]))
            else:
                pidsumok["ok"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="ok",
                    detali=f"{vsjogo_ryadkiv} рядків"))
    return naslidky, pidsumok


ZAHOLOVOK_ZVITU = """# Третій шар: цитати проти джерел

**Генерується** `tools/citaty.py --zvit`. Правити вручну нема сенсу.

Перевірено механічно: чи справді уривок, наведений у доказі, стоїть за
названою адресою. Це **не** оцінка того, чи доказ доречний — це окреме
питання, і його вирішує людина.

| Стан | Означає |
|---|---|
| `звірено` | усі придатні уривки знайдено в джерелі дослівно |
| `не знайдено` | уривка в джерелі немає — переказ, помилка адреси або джерело змінилося |
| `джерело не в кеші` | нема з чим звіряти: `--kachaty`, або егрес не пускає |
| `нема чого звіряти` | доказ без URL або без дослівного уривка (клас `C`, `E`, `K`) |

"""


def zvit(naslidky: list[dict], pidsumok: dict[str, int]) -> None:
    pidpysy = {"ok": "звірено", "ne_znaydeno": "**не знайдено**",
               "nedosyazhne": "джерело не в кеші",
               "nichoho": "нема чого звіряти", "pomylka": "**файл не читається**"}
    r = [ZAHOLOVOK_ZVITU.rstrip("\n"), ""]
    r.append(f"Записів доказів: **{sum(pidsumok.values())}**. "
             f"Звірено дослівно: **{pidsumok['ok']}**. "
             f"Не знайдено: **{pidsumok['ne_znaydeno']}**. "
             f"Джерело не в кеші: **{pidsumok['nedosyazhne']}**. "
             f"Нема чого звіряти: **{pidsumok['nichoho']}**.\n")
    r.append(f"Станом на {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC.\n")
    for stan in ("pomylka", "ne_znaydeno", "nedosyazhne", "ok", "nichoho"):
        grupa = [n for n in naslidky if n["stan"] == stan]
        if not grupa:
            continue
        r.append(f"\n## {pidpysy[stan]} — {len(grupa)}\n")
        r.append("| Доказ | Файл | Деталі |")
        r.append("|---|---|---|")
        for n in grupa:
            d = n["detali"]
            if n.get("promakhy"):
                d += ": " + "; ".join(f"«{p[:70]}…»" for p in n["promakhy"])
            r.append(f"| {n['nazva']} | `{n['fayl']}` | {d} |")
    ZVIT.write_text("\n".join(r) + "\n", encoding="utf-8")


def main() -> int:
    a = sys.argv[1:]
    fayly = [Path(x) for x in a if not x.startswith("--")] or None
    naslidky, pidsumok = perevirka(kachaty="--kachaty" in a, fayly=fayly)
    if "--zvit" in a and fayly is None:
        zvit(naslidky, pidsumok)
        print(f"citaty: звіт у {ZVIT.relative_to(ROOT)}")

    for n in naslidky:
        if n["stan"] == "ne_znaydeno":
            print(f"   ✗ {n['nazva']}  ({n['fayl']}) — {n['detali']}")
            for p in n.get("promakhy", []):
                print(f"        не знайдено: «{p[:100]}»")
        elif n["stan"] == "pomylka":
            print(f"   ✗ {n['nazva']}  ({n['fayl']}) — {n['detali']}")

    print(f"citaty: записів {sum(pidsumok.values())}; "
          f"звірено {pidsumok['ok']}; "
          f"не знайдено {pidsumok['ne_znaydeno']}; "
          f"не в кеші {pidsumok['nedosyazhne']}; "
          f"без цитати {pidsumok['nichoho']}")

    bidy = pidsumok["ne_znaydeno"]
    if "--suvoro" in a:
        bidy += pidsumok["nedosyazhne"]
    return 1 if bidy else 0


if __name__ == "__main__":
    sys.exit(main())
