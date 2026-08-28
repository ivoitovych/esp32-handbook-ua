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
    tools/citaty.py --zvit     згенерувати factcheck/QUOTES.md
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

import factcheck

ROOT = Path(__file__).resolve().parent.parent
DOKAZY = ROOT / "factcheck" / "dokazy"
KESH = ROOT / "dzherela-kesh"
ZVIT = ROOT / "factcheck" / "QUOTES.md"

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
# Назва, що сама себе оголошує редакційною. Перша редакція перевірки
# спрацювала на 46 записах, і майже всі виявилися чесним `E`: «авторський
# підсумок», «рейтинг причин», «заголовок таблиці». Супровідник у назві
# **уже сказав**, що це судження, а не факт про світ — і тригер, який
# цього не читає, перетворює корисне питання на шум.
RE_SAM_KAZHE_E = re.compile(
    r"авторськ|підсум|рейтинг|спостереж|узагальн|заголов|назви колонок|"
    r"рамка|порада|редакційн|вибір автора|оцінка|міркуванн|формулюванн|"
    r"ринков|маршрут|позиція|"
    # Друге звуження, куплене поштучним розбором М2: з 36 кандидатів
    # справжніх виявилося **дві**. Решта — твердження, у яких число
    # присутнє, але **не є предметом**:
    #
    #     «5 В на GPIO. Абсолютний лідер.»       предмет — лідер
    #     «470 мкФ — найдешевше рішення»         предмет — найдешевше
    #     «Часті винуватці 5 В»                  це заголовок стовпця
    #
    # Я пропонував замінити всі 36 механічно, прочитавши колонку причин
    # замість самих записів. М2 подивилися поштучно й показали, що це
    # була б помилка. Тригер, який лишається на 35 після того, як усе
    # справжнє закрито, перестають читати — і тоді він не ловить нічого.
    r"найдешевш|найдорожч|лідер|найчастіш|найпоширеніш|"
    r"винуватц|типов[аоиі]\b|звичайн|практик|стандартн", re.I)

# Число з одиницею виміру: те, для чого джерело майже завжди існує.
RE_CHYSLO_Z_ODYNYCEYU = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:мА|мкА|нА|А\b|мВ|В\b|кВ|Ом|кОм|МОм|Гц|кГц|МГц|"
    r"ГГц|мс|мкс|нс|с\b|°C|дБм|дБ|мм|см|м\b|Вт|мВт|Гн|мГн|нФ|мкФ|пФ|"
    r"КБ|МБ|ГБ|біт|байт|%)")


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


_IMENA_Z_MANIFESTU: dict[str, str] | None = None


def _z_manifestu() -> dict[str, str]:
    """URL → ім'я файлу, як його **записав маніфест**.

    Маніфест — єдине, що входить у git (самі файли ні: копірайт). Він
    записує ім'я кожного файлу разом із URL, тобто відповідь на це
    питання вже існує.
    """
    global _IMENA_Z_MANIFESTU
    if _IMENA_Z_MANIFESTU is not None:
        return _IMENA_Z_MANIFESTU
    _IMENA_Z_MANIFESTU = {}
    m = KESH / "MANIFEST.md"
    if not m.exists():
        return _IMENA_Z_MANIFESTU

    usi: dict[str, list[str]] = {}
    for r in re.finditer(
            r"^\| `([^`]+)` \| `[0-9a-f]{64}` \| \d+ \| [\d-]+ \| "
            r"<([^>]+)> \|$", m.read_text(encoding="utf-8"), re.M):
        usi.setdefault(r.group(2), []).append(r.group(1))

    # **Один URL часто має в маніфесті два рядки** — старе покоління
    # імені й нове, бо перейменування дописувало рядок, а не міняло
    # його. Виміряно: 357 рядків на 276 URL, тобто 78 URL мають по два
    # імені, і в контейнері існує рівно одне з них — те, під яким файл
    # качали тут.
    #
    # Тому «перший рядок» — хибне правило: рядки впорядковані за
    # іменем, а не за дійсністю, і перший часто вказує на файл, якого в
    # цьому контейнері немає. Питання, на яке треба відповісти, не «яке
    # ім'я записане», а «під яким іменем файл лежить **тут**».
    for url, imena in usi.items():
        ye = [i for i in imena if (KESH / i).exists()]
        if ye:
            _IMENA_Z_MANIFESTU[url] = ye[0]
        else:
            # Файлу немає ні під яким іменем — беремо виведене, якщо
            # воно серед записаних, інакше перше. Різниці для звірки
            # немає (обидва не відкриються), але звіт назве те ім'я,
            # яке дало б сьогоднішнє правило.
            vyved = vyvesty_imya(url)
            _IMENA_Z_MANIFESTU[url] = (vyved if vyved in imena
                                       else sorted(imena)[0])
    return _IMENA_Z_MANIFESTU


def vyvesty_imya(url: str) -> str:
    """Ім'я з URL — правило поточного покоління."""
    baza = re.sub(r"[^\w.-]", "_", url.rsplit("/", 1)[-1] or "bez-imeni")
    return f"{hashlib.sha256(url.encode()).hexdigest()[:8]}-{baza}"[:96]


def imya_dlya(url: str) -> str:
    """Ім'я файлу в кеші: спершу **маніфест**, і лише потім виведення.

    Базове ім'я збігається надто часто — у дереві ESP-IDF десятки файлів
    `esp32.inc` і сотні `*.h`. Тому виведене ім'я несе короткий хеш
    повного URL: ім'я лишається читним, а зіткнення зникають.

    ## Чому виведення тут друге, а не єдине

    Правило іменування вже мінялося раз, і 54 файли лишилися під старим
    поколінням. Шар 3 їх не відкривав: він виводив нове ім'я, файл під
    ним не існував, і доказ ставав «джерело не в кеші» — мовчки, у
    вигляді, не відрізнюваному від справжньої недосяжності. М2
    перейшли на це чотири рази за годину, перейменовуючи файли руками
    зі звіркою sha256.

    Перейменування закриває сьогоднішній біль і лишає рід. Рід ось
    який: **ім'я виводиться з URL, хоча маніфест його вже записав** —
    два джерела істини для одного факту, рівно те, що ми впіймали в
    подвійних іменах полів. Тому маніфест головний, а виведення —
    запасне, для URL, якого в маніфесті ще немає.

    > Виводити те, що вже записано, — значить обіцяти, що правило
    > виведення ніколи не зміниться. Воно вже змінилося.
    """
    z_manifestu = _z_manifestu().get(url)
    if z_manifestu:
        return z_manifestu
    return vyvesty_imya(url)


def zavantazhyty(url: str, cil: Path) -> bool:
    KESH.mkdir(exist_ok=True)
    r = subprocess.run(["curl", "-sSL", "--fail", "--max-time", "40",
                        "-o", str(cil), url],
                       capture_output=True)
    return r.returncode == 0 and cil.exists() and cil.stat().st_size > 0


DOPUSK_RYADKA = 3.0


def ryadky_z_koordynat(storinka) -> list[str]:
    """Відновити рядки таблиці з координат слів.

    `pdftotext` (і звичайне витягання pymupdf) віддають **порядок
    читання**, у якому кожна комірка стовпця стоїть окремим рядком:

        Thermometer
        tERR
        -55°C to +125°C
        ±2
        °C

    Суцільного рядка «Thermometer tERR -55°C to +125°C ±2 °C» у такому
    тексті немає й бути не може, хоч у документі це один рядок таблиці.
    Саме через це М2 дістав 27 хибних тривог із 45, і саме через це
    з'явилася позначка «звірено очима».

    Тут слова беруться з координатами й **групуються за базовою
    лінією**: усе, що лежить у межах `DOPUSK_RYADKA` пунктів по
    вертикалі, — один рядок; усередині рядка сортуємо зліва направо.

    Лишається один випадок, який так не збирається: комірка, розбита на
    два візуальні рядки («Thermometer» над «Error»). Для нього далі є
    запасний хід із лексемами.
    """
    slova = storinka.get_text("words")
    if not slova:
        return []
    slova.sort(key=lambda w: (round(w[1], 1), w[0]))
    ryadky, potochnyy, baza = [], [], None
    for w in slova:
        if baza is None:
            potochnyy, baza = [w], w[1]
        elif abs(w[1] - baza) <= DOPUSK_RYADKA:
            potochnyy.append(w)
        else:
            ryadky.append(potochnyy)
            potochnyy, baza = [w], w[1]
    if potochnyy:
        ryadky.append(potochnyy)
    out = []
    for r in ryadky:
        r.sort(key=lambda w: w[0])
        out.append(" ".join(w[4] for w in r))
    return out


def tekst_pdf(p: Path) -> str | None:
    """Текст PDF у **двох виглядах одразу**.

    Порядок читання й відновлені за координатами рядки таблиць
    склеюються в один рядок пошуку. Цитата, взята з абзацу, знайдеться
    в першому; цитата, взята з рядка таблиці, — у другому.

    Це і є заміна позначці «звірено очима» для типового випадку: не
    послаблення перевірки, а **краще витягання**. Послаблення (лексеми
    у вікні) лишається тільки для комірок, розбитих на два рядки.
    """
    try:
        import pymupdf
    except ImportError:
        r = subprocess.run(["pdftotext", "-q", "-layout", str(p), "-"],
                           capture_output=True)
        return (r.stdout.decode("utf-8", "replace")
                if r.returncode == 0 else None)
    try:
        with pymupdf.open(p) as d:
            chastyny = []
            for storinka in d:
                chastyny.append(storinka.get_text())
                chastyny += ryadky_z_koordynat(storinka)
        return "\n".join(chastyny)
    except Exception:
        return None


def tekst_dzherela(p: Path) -> str | None:
    """Текст файлу — за **вмістом**, а не за розширенням.

    Перша редакція мала перелік дозволених розширень, і він одразу
    відстав: `library.properties` кожної бібліотеки Arduino — звичайний
    текст, але в переліку його не було, і шар 3 оголошував такий файл
    нечитним. Тобто ціла категорія джерел випадала мовчки.

    Переліки розширень відстають завжди. Тому питаємо файл: якщо він
    декодується як UTF-8 і в ньому майже немає керівних байтів — це
    текст, хай як він називається.
    """
    if p.suffix.lower() == ".pdf":
        return tekst_pdf(p)
    try:
        syri = p.read_bytes()
    except OSError:
        return None
    if syri.startswith((b"%PDF", b"\x89PNG", b"\xff\xd8\xff", b"PK\x03\x04",
                        b"\x7fELF", b"GIF8")):
        return None
    try:
        tekst = syri.decode("utf-8")
    except UnicodeDecodeError:
        return None
    proba = tekst[:4096]
    keruvni = sum(1 for c in proba if ord(c) < 32 and c not in "\t\n\r")
    if proba and keruvni / len(proba) > 0.01:
        return None
    return tekst


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
    return bool(RE_DZHERELO_VSEREDYNI.search(str(z.get("source") or "")))


def dzherelo_rozvyazne(z: dict) -> bool:
    """Чи в полі `dzherelo` названо документ, а не властивість світу."""
    d = str(z.get("source") or "")
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


# М'який перенос і ліґатури, які PDF лишає в тексті. Це не зміст, а
# сміття витягання: у документі їх не видно, у витягнутому тексті вони
# розривають слово посеред цитати. Тире різних видів зводимо до одного —
# `‑` (non-breaking hyphen) у datasheet трапляється замість `-`.
PEREKLAD_SMITTYA = {
    "\u00ad": "",      # м'який перенос
    "\u200b": "",      # нульової ширини пробіл
    "\ufeff": "",      # BOM усередині
    "\u2011": "-",     # нерозривний дефіс
    "\ufb01": "fi", "\ufb02": "fl",   # ліґатури
}


def plaskyy(s: str) -> str:
    """Один пробіл між словами; сміття витягання прибрано.

    Свідомо **не** чіпаємо ні регістр, ні лапки, ні змістовні тире.
    Цитата, яка збігається лише після приведення регістру, — це вже
    переказ, і хай вона падає: доказ мусить бути дослівним.

    А от м'який перенос і ліґатури змісту не несуть: їх у документі не
    видно, і жодна людина не могла б їх «процитувати неправильно».
    Прибирати їх — не послаблення, а виправлення витягання.
    """
    for shcho, na in PEREKLAD_SMITTYA.items():
        s = s.replace(shcho, na)
    return re.sub(r"\s+", " ", s).strip()


def uryvky(cytata: str, vlasna_mova: bool = False) -> list[list[str]]:
    """Придатні до перевірки групи рядків цитати.

    Відкидаємо: наші примітки (кирилиця), місця з вирізаним текстом
    (багатокрапка), позначки джерела в дужках і надто короткі рядки,
    які збіглися б із чим завгодно.

    Повертаємо **групи рядків**, а не злитий текст, бо перевіряти
    доводиться двома способами (див. `znayty`).

    ## `vlasna_mova` — і чому без нього клас `S` був би порожній

    Правило «кирилиця — це наша примітка, а не цитата» правильне рівно
    доти, доки джерело англійське. Для класу `S` джерелом є **книга**,
    і тоді кожен справжній уривок кирилицею.

    Виміряно на 21 записі внутрішньої звірки: без цього прапорця
    придатних уривків не мали **15 із 21**, і шар 3 сказав би про них
    «нема чого звіряти» — тобто клас, заведений щоб зафіксувати
    зроблену звірку, звітував би, що звіряти нічого.

    > Фільтр, слушний для одного корпусу, застосований до іншого,
    > викидає все — і мовчить тим самим словом, яким каже «чисто».

    Решта відсіву лишається чинною: багатокрапка й тут означає
    вирізаний текст, а короткий рядок і тут збіжиться з чим завгодно.
    """
    grupy: list[list[str]] = [[]]
    for ryadok in cytata.splitlines():
        r = ryadok.strip()
        pryydatnyy = (
            r
            and (vlasna_mova or not RE_KYRYLYCYA.search(r))
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

    Узято з `tools/perevirka-tsytat-m2.py`, функція `znayty_ryadok`
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


RE_SHLYAKH_KNYHY = re.compile(
    r"\b(?:manual|kartky|dodatky|inserts)/[\w.\-]+\.md\b")


def knyzhkovi_dzherela(z: dict) -> list[Path]:
    """Файли **книги**, названі в джерелі запису класу `S`.

    `S` — внутрішня звірка: твердження доводиться не зовнішнім
    документом, а іншим місцем цієї ж книги. Такий доказ нічого не
    каже про світ, зате каже щось перевірне про книгу — що вона
    сходиться сама з собою.

    Тому він **мусить** проходити третій шар, як і всі інші, просто
    корпусом йому є книга, а не кеш джерел. Інакше `S` був би ярликом,
    що стверджує звірку, якої ніхто не робить, — рід 24 у `DEFECTS.md`,
    записаний того самого дня, що й цей клас.
    """
    syryy = str(z.get("source") or z.get("dzherelo") or "")
    out: list[Path] = []
    for s in RE_SHLYAKH_KNYHY.findall(syryy):
        p = ROOT / s
        if p.exists() and p not in out:
            out.append(p)
    return out


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
    syryy = str(z.get("source") or "")
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
                "vygadane": 0, "zaglushka": 0, "okom": 0, "pomylka": 0,
                "nechytne": 0, "nadmirnyy_e": 0}
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
            nazva = factcheck.nazva_zapysu(z)
            # **Відсутність класу — не те саме, що клас `F`.**
            #
            # У реєстрі клас є завжди. У вивантаженні помічника його
            # немає й не має бути: клас присвоює супровідник, і саме на
            # цьому тримається правило «чуже слово не потрапляє в реєстр
            # неперевіреним».
            #
            # Перша редакція цих воріт підставляла `F` там, де поля
            # просто немає, і валила **всю** хвилю помічника як «хибні
            # записи» — не перевіривши жодної цитати. Тобто ворота, що
            # мали ловити брак, приховали роботу.
            # Було `"klas" in z` — перевірка наявності **старого**
            # імені. Після стиснення воно хибне завжди, і умови нижче
            # («A без цитати», «доказ класу F») не спрацьовують більше
            # ніколи. Прогін М2 показав це так: «звірено 508» до і
            # «звірено 508» після, а 23 записи тим часом переїхали з
            # «перевіряється» в «нема чого звіряти».
            #
            # > Перевірка вертає те саме число, і те саме число нічого
            # > не означає.
            maye_klas = bool(z.get("status") or z.get("klas"))
            klas = factcheck.klas_zapysu(z, "").strip().upper()

            # Клас `F` — це «не звірено», типовий стан **відсутності**
            # доказу. Запис доказу з класом `F` не означає нічого й
            # трапляється лише як помилка помічника (знахідка М2).
            # **Клас `A` без цитати — суперечність за означенням.**
            #
            # `A` означає «першоджерело отримано, витяг наведено
            # дослівно». Без витягу він не означає нічого, і саме в цій
            # порожнечі оселився найтонший рід підробки, який ми бачили
            # (знахідка М2 від 00:14Z): джерело справжнє, редакція
            # правильна, а **координата всередині документа вигадана** —
            # `Table 6-21`, якої в цьому datasheet немає.
            #
            # Усі три наші перевірки таке пропускають: джерело — документ,
            # файл завантажується, а цитати, яку міг би звірити третій
            # шар, просто немає. Ворота проти цього одні: вимагати витяг
            # там, де клас його обіцяє.
            if maye_klas and klas == "A" and not str(z.get("quote") or
                                                     z.get("cytata-tablytsya")
                                                     or "").strip():
                pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="pomylka",
                    detali="клас A без цитати — A обіцяє дослівний витяг"))
                continue

            if maye_klas and klas == "F":
                pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="pomylka",
                    detali="доказ класу F — F означає відсутність доказу"))
                continue

            # Вигадане джерело: клас каже «звірено», а в полі джерела
            # стоїть міркування. Див. RE_SCHOS_SCHO_MOZHE_BUTY_DOKUMENTOM.
            if maye_klas and klas in ("A", "B") and not dzherelo_rozvyazne(z):
                pidsumok["vygadane"] = pidsumok.get("vygadane", 0) + 1
                dzh = str(factcheck.pole(z, "source", "dzherelo") or "")[:60]
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="vygadane",
                    detali=f"клас {klas}, а джерело — не документ: «{dzh}»"))
                continue

            # **Надмірний `E` — дзеркало вигаданого джерела.** Знахідка
            # М2 від 22:23Z, і найважливіше, що дала остання хвиля.
            #
            # Клас `E` означає «зовнішнього джерела не існує за
            # побудовою»: редакційне рішення, порада, рамка викладу.
            # Помічники ставили його твердженням **із числами** — «4.7
            # кОм обов'язкове», «3.3 В на обох лініях». Для таких
            # джерело існує, і М2 довів це для трьох із трьох, що
            # перевірив.
            #
            # Наслідок той самий, що у вигаданого джерела: одиниця
            # виходить із роботи назавжди. Але помітити важче — надмірний
            # `E` схожий на обережність, а обережність ми заохочували
            # обидва. Учили «не натягуй `A`»; не сказали «і не тікай
            # у `E`».
            #
            # Тому це **питання, а не заборона**: `E` на твердженні, у
            # назві якого число з одиницею виміру, друкується окремим
            # переліком і рішення лишає людині.
            if (maye_klas and klas == "E"
                    and RE_CHYSLO_Z_ODYNYCEYU.search(nazva)
                    and not RE_SAM_KAZHE_E.search(nazva)):
                pidsumok["nadmirnyy_e"] = pidsumok.get("nadmirnyy_e", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nadmirnyy_e",
                    detali="клас E, а в назві число з одиницею"))
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

            # **Читання таблиці — не цитата, і це два різні роди.**
            # Знахідка М2 від 22:05Z, і вона стосується самої побудови
            # поля `cytata`.
            #
            # У datasheet факт часто живе в перетині рядка й стовпця, а
            # назва параметра стоїть у комірці, розтягнутій на кілька
            # рядків. Зібрати з цього «рядок таблиці» можна лише рукою —
            # злити клітинки, дописати `Typ`, `Min`, `(note 3)`. Факт
            # при цьому правильний, а суцільного рядка в документі
            # **немає й не буде**, скільки б ми не покращували витягання.
            #
            # М2 знайшов це в себе, назвавши прямо: «це рівно те, що ми
            # звемо помилкою помічника — коментар, вписаний у поле
            # цитати; я робив це власноруч і водночас перевіряв за це
            # інших».
            #
            # Тому окреме поле: перелік клітинок, кожна перевіряється
            # підрядком **окремо**, без вигаданих відступів і дописаних
            # слів. Пояснення йде в нотатку, де йому й місце.
            tablychna = z.get("cytata-tablytsya")
            if tablychna:
                frahmenty = [[str(k).strip()] for k in tablychna
                             if str(k).strip()]
            else:
                frahmenty = uryvky(
                    str(factcheck.pole(z, "quote", "cytata") or ""),
                    vlasna_mova=(klas == "S"))
            urly = dzherela_zapysu(z)
            # Клас `S` адресує книгу, а не мережу, тож відсутність URL
            # у нього — норма, а не «нема чого звіряти».
            if not frahmenty or (not urly and klas != "S"):
                pidsumok["nichoho"] += 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nichoho",
                    detali=("немає URL" if frahmenty else
                            "немає придатних уривків")))
                continue

            teksty: list[str] = []
            nedosyazhni: list[str] = []
            zaglushky: list[str] = []
            nechytni: list[str] = []
            tablychni = False

            # Внутрішня звірка: корпус — названі файли книги.
            if klas == "S":
                shlyakhy = knyzhkovi_dzherela(z)
                if not shlyakhy:
                    pidsumok["pomylka"] = pidsumok.get("pomylka", 0) + 1
                    naslidky.append(dict(
                        fayl=f.stem, nazva=nazva, stan="pomylka",
                        detali="клас S, а в джерелі немає шляху до файлу "
                               "книги — звіряти нема з чим"))
                    continue
                teksty = [plaskyy(p.read_text(encoding="utf-8"))
                          for p in shlyakhy]

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
                        if cil.exists() and not kesh_tekstu[u]:
                            nechytni.append(u)
                if u.lower().endswith(".pdf"):
                    tablychni = True
                if kesh_tekstu[u]:
                    teksty.append(kesh_tekstu[u])
                elif u in zaglushky:
                    pass
                else:
                    nedosyazhni.append(u)

            # «Файл є, прочитати нічим» і «файлу немає» — різні стани, і
            # плутати їх небезпечно. Досі PDF без витягача мовчки падав у
            # «немає в кеші», тобто виглядав як проблема егресу, а не як
            # брак інструмента на цій машині.
            if nechytni and not teksty:
                pidsumok["nechytne"] = pidsumok.get("nechytne", 0) + 1
                naslidky.append(dict(
                    fayl=f.stem, nazva=nazva, stan="nechytne",
                    detali=f"{len(nechytni)}: файл у кеші є, витягти текст "
                           f"нічим"))
                continue

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
               "nechytne": "**файл є, витягти текст нічим**",
               "nadmirnyy_e": "клас E на твердженні з числом — перевірити",
               "pomylka": "**хибний запис**"}
    r = [ZAHOLOVOK_ZVITU.rstrip("\n"), ""]
    r.append(f"Записів доказів: **{sum(pidsumok.values())}**. "
             f"Звірено дослівно: **{pidsumok['ok']}**. "
             f"Не знайдено: **{pidsumok['ne_znaydeno']}**. "
             f"Джерело не в кеші: **{pidsumok['nedosyazhne']}**. "
             f"Нема чого звіряти: **{pidsumok['nichoho']}**.\n")
    r.append(f"Станом на {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC.\n")
    for stan in ("vygadane", "zaglushka", "pomylka", "nechytne",
                 "nadmirnyy_e", "ne_znaydeno",
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
    if pidsumok["nadmirnyy_e"]:
        print(f"   · клас E на твердженні з числом: "
              f"{pidsumok['nadmirnyy_e']} — перевірити, чи джерела справді "
              f"немає")
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
