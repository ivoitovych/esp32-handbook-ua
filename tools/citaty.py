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


# Поле `dzherelo`, у якому стоїть не документ, а **міркування**. Знахідка
# М2 від 19:40Z, і найдорожча з усіх: помічник на Haiku, не знайшовши
# документа, не пише клас `C` — він **вигадує правдоподібну назву
# джерела**. «Властивості логіки CMOS», «фундаментальне правило
# електроніки», «типова побудова модульних плат».
#
# Це найгірший можливий наслідок з усіх: хибний клас `A` оголошує
# твердження звіреним, прибирає його з кожної черги, і більше його не
# перевіряє ніхто ніколи.
#
# Шар 3 таке бачив як «джерела немає в кеші» — сигнал є, тривоги немає.
# Тепер для класів `A` і `B` це помилка. Класи `C` і `E` під правило не
# підпадають: у них джерела або немає, або воно недосяжне за задумом.
# Що вважається названим документом. Перший підхід був завузький і
# позначив вигаданими чотирнадцять записів, з яких тринадцять — чесні
# посилання М2 на PDF, у якого немає сталої адреси: «Texas Instruments,
# PCF8574 Remote 8-Bit I/O Expander for I2C Bus (SCPS068), розділ
# Features». Це повноцінна цитата, просто не URL.
#
# Різниця між нею й вигаданим джерелом не в наявності адреси, а в тому,
# **чи названо документ**: видавця, заголовок, номер редакції. Вигадане
# джерело описує не документ, а властивість світу — «властивості логіки
# CMOS», «загальновідома електромеханіка реле».
RE_ADRESA = re.compile(
    r"https?://|\b[\w-]+\.(?:com|org|net|io|dev)/"
    r"|\.pdf\b|\.h\b|\.c\b|\.py\b|\.rst\b|\.inc\b|\.csv\b"
    r"|components/|tools/|docs/|Kconfig", re.I)
# Дві поспіль великі латинські лексеми — назва видавця або заголовок
# документа: `Texas Instruments`, `Product Brief`, `Register Map`.
RE_NAZVA_DOKUMENTA = re.compile(r"\b[A-Z][A-Za-z0-9-]+ [A-Z][A-Za-z0-9-]+")
# Ідентифікатор документа: `SCPS068`, `DS40002061B`, `RM-MPU-6000A-00`,
# `Rev 1.1`, `UM10204`, `IEC 61190-1-3`.
RE_ID_DOKUMENTA = re.compile(
    r"\b[A-Z]{2,}[0-9][\w-]*\b|\bRev\.?\s*\d|\b(?:IEC|ISO|EN|UL)\s*\d",
    re.I)


# Джерело всередині книги. М2 звірив твердження проєкту 60 з **власним
# кодом того самого розділу**: поріг у прозі проти порога в лістингу.
#
# Це не зовнішня цитата й не вигадане джерело — це третій рід, якого в
# архітектурі не було. Саме він і є той «четвертий шар», що його бракує:
# реєстр звіряє книгу з джерелами, але не книгу з книгою, а найгірші
# помилки цього тижня були саме внутрішніми суперечностями (BMP280 у
# додатку E проти розділу 45).
#
# Тож такий запис правомірний, і шар 3 його пропускає. Але перевірити
# його механічно тут нічим: джерело — сама книга, і потрібен інший
# інструмент, не цей.
RE_DZHERELO_VSEREDYNI = re.compile(
    r"власн\w* (?:код|твердженн|текст)|розділ[ауі]?\s*\d|"
    r"додат\w+\s+[A-EА-Д]|картк\w+\s+К?\d|"
    r"manual/|kartky/|dodatky/|inserts/", re.I)


def dzherelo_vseredyni(z: dict) -> bool:
    return bool(RE_DZHERELO_VSEREDYNI.search(str(z.get("dzherelo") or "")))


def dzherelo_rozvyazne(z: dict) -> bool:
    """Чи в полі `dzherelo` названо документ, а не властивість світу."""
    d = str(z.get("dzherelo") or "")
    return bool(RE_ADRESA.search(d)
                or RE_ID_DOKUMENTA.search(d)
                or RE_NAZVA_DOKUMENTA.search(d)
                or dzherelo_vseredyni(z))


# Сторінка-заглушка, віддана з кодом 200. Знахідка М2: `semtech.com`
# віддає HTML рівно того самого розміру на **будь-яку** адресу в
# `/uploads/documents/`, і `curl --fail` завершується успішно. Без цієї
# перевірки заглушка лягає в кеш як документ, а клас `A` ставиться за
# те, чого ніхто не бачив.
def pidmineno_zaglushkoyu(p: Path) -> bool:
    if p.suffix.lower() != ".pdf":
        return False
    try:
        with p.open("rb") as f:
            pochatok = f.read(1024)
    except OSError:
        return True
    return not pochatok.startswith(b"%PDF")


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


VIKNO_TABLYCI = 4000
RE_LEKSEMA = re.compile(r"[\w.°±×/+-]{2,}")


def u_tablyci(ryadok: str, tekst: str) -> bool:
    """Чи є рядок **читанням таблиці**, розкиданої по документу.

    Узято з `factcheck/perevirka-tsytat-m2.py`, функція `znayty_ryadok`
    (М2, знахідка 19:40Z). Проста перевірка підрядком дала їм **27
    хибних тривог із 45**, і жодна не була провиною цитати.

    Причина: `pdftotext` розкладає стовпці так, що назва параметра,
    умова й значення опиняються на різних рядках. У datasheet DS18B20:

        tERR                                    °C      3
      Error        -55°C to +125°C              ±2

    Рядка «Thermometer Error tERR -55°C to +125°C ±2 °C» у документі
    немає й бути не може, хоч цитата точна.

    Тому: всі змістовні лексеми мусять бути в документі **і лежати
    компактно**. Це свідоме послаблення — ловить вигадану цитату
    (лексем не буде взагалі), не ловить перестановку слів у межах
    таблиці, де перестановка змісту не міняє.

    Вживається **лише як запасний хід** і лише для PDF: для коду й RST
    порядок слів значущий, і послаблювати його там нема причин.
    """
    leksemy = RE_LEKSEMA.findall(ryadok)
    if len(leksemy) < 3:
        return False
    poz = []
    for l in leksemy:
        i = tekst.find(l)
        if i < 0:
            return False
        poz.append(i)
    return (max(poz) - min(poz)) < VIKNO_TABLYCI


def znayty(grupa: list[str], teksty: list[str],
           tablychni: bool = False) -> list[str]:
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
    promakhy = [r for r in grupa
                if not any(plaskyy(r) in t for t in teksty)]
    if tablychni:
        promakhy = [r for r in promakhy
                    if not any(u_tablyci(plaskyy(r), t) for t in teksty)]
    return promakhy


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
    pidsumok = {"ok": 0, "ne_znaydeno": 0, "nedosyazhne": 0, "nichoho": 0,
                "vygadane": 0, "zaglushka": 0, "okom": 0, "pomylka": 0}
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
            klas = str(z.get("klas") or "F").strip().upper()

            # Клас `F` — це «не звірено», типовий стан **відсутності**
            # доказу. Запис доказу з класом `F` не означає нічого й
            # трапляється лише як помилка помічника (знахідка М2).
            if klas == "F":
                pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="pomylka",
                    detali="доказ класу F — F означає відсутність доказу"))
                continue

            # Вигадане джерело: клас каже «звірено», а в полі джерела
            # стоїть міркування. Див. RE_SCHOS_SCHO_MOZHE_BUTY_DOKUMENTOM.
            if klas in ("A", "B") and not dzherelo_rozvyazne(z):
                pidsumok["vygadane"] = pidsumok.get("vygadane", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="vygadane",
                    detali=f"клас {klas}, а джерело — не документ: "
                           f"«{str(z.get('dzherelo') or '')[:60]}»"))
                continue

            # Цитата, яку супровідник звірив очима там, де витягання
            # тексту руйнує структуру. Знахідка М2: без цього стану шар 3
            # б'є на сполох на **правильних** цитатах, і за тиждень його
            # перестають читати. Позначку ставить людина і лише разом із
            # поясненням, чому машина тут безсила.
            if z.get("perevireno-okom"):
                pidsumok["okom"] = pidsumok.get("okom", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="okom",
                    detali=str(z.get("perevireno-okom"))[:90]))
                continue

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
            zaglushky: list[str] = []
            tablychni = False
            for u in urly:
                if u not in kesh_tekstu:
                    cil = KESH / imya_dlya(u)
                    if not cil.exists() and kachaty:
                        zavantazhyty(u, cil)
                    if cil.exists() and pidmineno_zaglushkoyu(cil):
                        kesh_tekstu[u] = None
                        zaglushky.append(u)
                    else:
                        kesh_tekstu[u] = (plaskyy(tekst_dzherela(cil) or "")
                                          if cil.exists() else None) or None
                if u.lower().endswith(".pdf"):
                    tablychni = True
                if kesh_tekstu[u]:
                    teksty.append(kesh_tekstu[u])
                elif u in zaglushky:
                    pass
                else:
                    nedosyazhni.append(u)

            if zaglushky and not teksty:
                pidsumok["zaglushka"] = pidsumok.get("zaglushka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="zaglushka",
                    detali=f"{len(zaglushky)}: у кеші не PDF, а сторінка "
                           f"з кодом 200"))
                continue

            if not teksty:
                pidsumok["nedosyazhne"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nedosyazhne",
                    detali=f"{len(nedosyazhni)} джерел не в кеші"))
                continue

            vsjogo_ryadkiv = sum(len(g) for g in frahmenty)
            promakhy: list[str] = []
            for grupa in frahmenty:
                promakhy += znayty(grupa, teksty, tablychni=tablychni)
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
| `джерело вигадане` | клас `A` чи `B`, а в полі джерела — міркування, не документ |
| `у кеші заглушка` | сервер віддав HTML із кодом 200 замість PDF |
| `звірено очима` | витягання тексту руйнує структуру; звірив супровідник, причина названа |

"""


def zvit(naslidky: list[dict], pidsumok: dict[str, int]) -> None:
    pidpysy = {"ok": "звірено", "ne_znaydeno": "**не знайдено**",
               "nedosyazhne": "джерело не в кеші",
               "nichoho": "нема чого звіряти",
               "vygadane": "**джерело вигадане**",
               "zaglushka": "**у кеші заглушка, не документ**",
               "okom": "звірено очима",
               "pomylka": "**хибний запис**"}
    r = [ZAHOLOVOK_ZVITU.rstrip("\n"), ""]
    r.append(f"Записів доказів: **{sum(pidsumok.values())}**. "
             f"Звірено дослівно: **{pidsumok['ok']}**. "
             f"Не знайдено: **{pidsumok['ne_znaydeno']}**. "
             f"Джерело не в кеші: **{pidsumok['nedosyazhne']}**. "
             f"Нема чого звіряти: **{pidsumok['nichoho']}**.\n")
    r.append(f"Станом на {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC.\n")
    for stan in ("vygadane", "zaglushka", "pomylka", "ne_znaydeno",
                 "nedosyazhne", "okom", "ok", "nichoho"):
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
          f"без цитати {pidsumok['nichoho']}; "
          f"звірено очима {pidsumok['okom']}")
    if pidsumok["vygadane"] or pidsumok["zaglushka"] or pidsumok["pomylka"]:
        print(f"   ⚠ вигаданих джерел {pidsumok['vygadane']}; "
              f"заглушок у кеші {pidsumok['zaglushka']}; "
              f"хибних записів {pidsumok['pomylka']}")

    # Вигадане джерело, заглушка й доказ класу F — це **ворота**, а не
    # звіт. Розбіжність цитати вимагає розгляду й може бути хибною
    # тривогою; ці три не можуть бути нічим, крім помилки.
    bidy = pidsumok["vygadane"] + pidsumok["zaglushka"] + pidsumok["pomylka"]
    if "--suvoro" in a:
        bidy += pidsumok["ne_znaydeno"] + pidsumok["nedosyazhne"]
    return 1 if bidy else 0


if __name__ == "__main__":
    sys.exit(main())
