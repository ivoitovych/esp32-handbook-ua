#!/usr/bin/env python3
"""Поділ незвіреного між супровідниками — за досяжністю джерела.

Черга (`factcheck.py cherga`) сортує за вартістю помилки й показує сорок
рядків. Для роботи вдвох цього замало: треба знати не «що найдорожче», а
**хто це взагалі може закрити**.

Поділ тут не за темами й не за розділами, а за одним питанням: у якому
джерелі лежить відповідь.

    ESP-IDF, esptool, заголовки `soc/`   → М1, у контейнері вони є
    datasheet мікросхем, електричні дані → М2, у контейнері 403

Решта — одиниці зі слабким сигналом (згадка чипа чи терміна в лапках без
числа й ідентифікатора). Вони лишаються в `F` свідомо: серед них
переважно редакційне, але механічно відрізнити його від фактичного не
вдається, тож вони чекають на суцільні проходи, а не на поділ.

    factcheck/tools/split_queue.py            зведення
    factcheck/tools/split_queue.py --naryad   згенерувати factcheck/reports/SPLIT.md
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(Path(__file__).resolve().parent))

import factcheck  # noqa: E402  — після правки sys.path
FC = ROOT / "factcheck"
# `GRUPY` була вісьмома копіями того самого факту — теками цієї
# книги. Копії збігалися, і саме тому були небезпечні: набір копій
# не бреше, доки факт не зміниться, а тоді бреше всіма одразу.
# Тепер це дані: `factcheck/book.yaml`.
GRUPY = config.groups()

# Порядок важливий: одиниця потрапляє в перший кошик, який її впізнав.
# Тому специфічне (назва мікросхеми) стоїть перед загальним (число з
# одиницею) — інакше «BME280 живиться 3.3 В» пішло б у електричні.
KOSHYKY: list[tuple[str, str, str, re.Pattern]] = [
    ("M1", "api", "виклики й константи ESP-IDF — заголовки компонентів",
     re.compile(r'`(esp_|gpio_|i2c_|spi_|uart_|nvs_|xTask|vTask|xQueue|'
                r'heap_caps|ledc_|adc_|rmt_|twai_|CONFIG_|SOC_|MALLOC_CAP|'
                r'ESP_[A-Z])')),
    ("M1", "komandy", "командний рядок esptool та idf.py",
     re.compile(r'`(esptool|idf\.py|espefuse|espsecure|otatool|parttool)\b'
                r'|`(write-flash|read-flash|erase-flash|merge-bin|chip-id|'
                r'flash-id)')),
    ("M1", "piny", "номери GPIO — заголовки soc/ і маски дійсних пінів",
     re.compile(r'GPIO\s?\d+|`IO\d+`')),
    ("M1", "adresy", "шістнадцяткові адреси й обсяги",
     re.compile(r'0x[0-9A-Fa-f]{3,}')),
    ("M1", "log", "рядки, які книга обіцяє побачити в консолі",
     re.compile(r'E \(\d|W \(\d|I \(\d|`[A-Z][A-Za-z_ ]{8,}`')),
    ("M2", "detali", "конкретні мікросхеми — datasheet виробника",
     re.compile(r'\b(BME280|BMP280|BMP180|DS18B20|DS3231|DHT11|DHT22|SHT[234]\d|'
                r'SSD1306|SH1106|ILI9341|ST7789|MAX485|MAX3232|MAX31855|MAX6675|'
                r'SN65HVD\d+|TP4056|DW01|MCP23017|MCP2515|PCF8574|PCA9685|'
                r'74HC\d+|CD4051|HC-SR04|SX12\d\d|RFM\d\d|MAX170\d\d|INA219|'
                r'ADS1115|W5500|ENC28J60|CH340|CP210\d|FT232|CH9102|AMS1117|'
                r'LM2596|MT3608|XL6009|18650|LiFePO4|AT24C\d+|24LC\d+|NEO-\d|'
                r'ATmega\d+|RP2040|STM32)')),
    ("M2", "elektro", "електричні величини — datasheet і специфікації",
     re.compile(r'\d+\s*(мА|мкА|А\b|В\b|мВ|кОм|Ом|МОм|мА·год|нФ|мкФ|пФ|Вт|'
                r'дБм|°C)')),
]

# Хвіст узято з `factcheck.RE_TVERDZHENNYA`, а не переписано вдруге:
# своя копія цього рядка вже одного разу мовчки перестала збігатися,
# коли заголовок картки змінили.
RE_F = re.compile(
    r'<!-- fc id:(?P<id>\S+) sha:\S+ src:(?P<src>[^\s:]+):(?P<ln>\d+) '
    r'klas:F -->\n### \S+ · (?P<vyd>\w+) · [^\n]*\n\n'
    + factcheck.RE_TVERDZHENNYA.pattern)


def zibraty() -> tuple[list[dict], dict[str, list[dict]]]:
    vsi: list[dict] = []
    for g in GRUPY:
        for f in sorted((config.cards_root() / g).glob("*.md")):
            for m in RE_F.finditer(f.read_text(encoding="utf-8")):
                vsi.append(m.groupdict())
    rozklad: dict[str, list[dict]] = collections.defaultdict(list)
    for r in vsi:
        for hto, klyuch, _, p in KOSHYKY:
            if p.search(r["txt"]):
                rozklad[f"{hto}-{klyuch}"].append(r)
                break
        else:
            rozklad["—"].append(r)
    return vsi, rozklad


# ── Повний облік решти, а не лише сильного сигналу ────────────────────
#
# Перша редакція цього інструмента ділила тільки клас `F` із виразною
# ознакою — 80 одиниць. Решта лишалася «поза поділом», і поки нікому не
# траплялося запитати «а скільки всього», це виглядало як поділ роботи.
#
# Насправді поза ним лишалося **майже все**: 1303 одиниці `F` зі слабким
# сигналом і **весь** клас `E`. Про `E` тоді думали, що він закритий за
# побудовою; вимірювання показало, що приблизно третина його одиниць має
# зовнішнє джерело.
#
# Тому поділ тепер перелічує всі стани, включно з тими, яких ніхто не
# візьме найближчим часом. Пункт «ніхто, і ось чому» — теж поділ; мовчазна
# прогалина — ні.

# Частка `E`, що має зовнішній референт. Не здогад: випадкова вибірка
# 160 одиниць, насіння в наряді, 95 % Вілсон 30–45 %.
CHASTKA_E_Z_REFERENTOM = 0.37


def klasy() -> dict[str, int]:
    """Скільки одиниць у кожному стані — з реєстру, а не з пам'яті.

    Ключ — **слово**. Літера в коментарі картки зводиться до слова тут
    же, одним рядком, який зникне разом із нею; власного розбору
    коментаря тут більше немає — це був третій примірник того самого
    правила, і при стисненні його ніхто б не згадав.
    """
    import re as _re
    import factcheck
    lich: dict[str, int] = collections.Counter()
    vz = _re.compile(r"klas:(\w+) -->")
    for g in GRUPY:
        for f in sorted((config.cards_root() / g).glob("*.md")):
            for m in vz.finditer(f.read_text(encoding="utf-8")):
                lich[factcheck.LETTER_TO_STATUS.get(m.group(1),
                                                    m.group(1))] += 1
    return dict(lich)


def podil_za_fajlamy(klasy: tuple[str, ...]) -> tuple[list[str], list[str], int, int]:
    """Поділ названих класів за файлами — жадібно, у бік меншої суми.

    Той самий механізм, що вже перевірений на класі `E`; `podil_e` тепер
    його окремий випадок. М2 назвав поділ решти «не очевидним» — але
    очевидність тут не потрібна, потрібен `assert`: перетин файлів нуль,
    і його видно.

        C+F  1935 одиниць у 91 файлі → 968 / 967, перетин 0
    """
    import sample
    za: dict[str, int] = collections.Counter()
    for k in klasy:
        for u in sample.odynyci(k):
            za[u["src"].split("/")[-1].split(":")[0]] += 1
    m1: list[str] = []
    m2: list[str] = []
    s1 = s2 = 0
    for f, n in sorted(za.items(), key=lambda kv: (-kv[1], kv[0])):
        if s1 <= s2:
            m1.append(f)
            s1 += n
        else:
            m2.append(f)
            s2 += n
    assert not (set(m1) & set(m2)), "файл потрапив обом"
    return sorted(m1), sorted(m2), s1, s2


def podil_e() -> tuple[list[str], list[str], int, int]:
    """Поділ класу `E` за файлами — жадібно, у бік меншої суми.

    Ділиться **файлами, а не одиницями**: два супровідники, що правлять
    той самий файл, дають конфлікт злиття на кожному записі.

    Перша редакція ділила за полем `src`, у якому стоїть `файл:рядок`, —
    і розкидала той самий файл по обидва боки, тобто робила рівно те,
    від чого мала берегти. Перетин тепер перевіряється явно.
    """
    import sample
    za: dict[str, int] = collections.Counter(
        u["src"].split("/")[-1].split(":")[0] for u in sample.odynyci("no-external-signal"))
    m1: list[str] = []
    m2: list[str] = []
    s1 = s2 = 0
    for f, n in sorted(za.items(), key=lambda kv: (-kv[1], kv[0])):
        if s1 <= s2:
            m1.append(f)
            s1 += n
        else:
            m2.append(f)
            s2 += n
    assert not (set(m1) & set(m2)), "файл потрапив обом"
    return sorted(m1), sorted(m2), s1, s2


def remonty() -> list[tuple[str, str, int, str]]:
    """Борг, який не є новою звіркою: полагодити наявні записи.

    Це окремий рід роботи. Він не додає звіреного, але без нього
    відсотки брешуть — а реєстр, який брешe про себе, гірший за менший
    чесний.
    """
    import layer3
    naslidky, _ = layer3.perevirka(False)
    lich = collections.Counter(str(n.get("stan")) for n in naslidky)
    return [
        ("обидва", "цитата не збігається", lich.get("ne_znaydeno", 0),
         "супровідник причесав цитату; звірити книгу, потім переписати"),
        ("М1", "джерело не в кеші", lich.get("nedosyazhne", 0),
         "докачати або перевести в `C` з чесною причиною"),
        ("М2", "вигадане джерело", lich.get("vygadane", 0),
         "клас каже «звірено», у полі джерела — міркування"),
        ("М2", "клас F у полі доказу", lich.get("pomylka", 0),
         "`F` означає відсутність доказу; запис не означає нічого"),
        ("М2", "надмірний E з числом", lich.get("nadmirnyy_e", 0),
         "«джерела не існує» на твердженні з номіналом"),
    ]


def zvedennya() -> int:
    vsi, rozklad = zibraty()
    print(f"незвіреного (клас F): {len(vsi)}\n")
    for hto, klyuch, opys, _ in KOSHYKY:
        k = f"{hto}-{klyuch}"
        print(f"  {hto}  {klyuch:9} {len(rozklad[k]):5}   {opys}")
    m1 = sum(len(v) for k, v in rozklad.items() if k.startswith("M1"))
    m2 = sum(len(v) for k, v in rozklad.items() if k.startswith("M2"))
    print(f"\n  М1 разом: {m1}    М2 разом: {m2}")
    print(f"  слабкий сигнал, поза поділом: {len(rozklad['—'])}")

    k = klasy()
    e_ref = round(k.get("no-external-signal", 0) * CHASTKA_E_Z_REFERENTOM)
    print(f"\n── решта, якої в поділі вище немає ──")
    print(f"  клас E, оцінка з референтом  {e_ref:5}   "
          f"({CHASTKA_E_Z_REFERENTOM:.0%} від {k.get('no-external-signal', 0)}, випадкова вибірка)")
    print(f"  клас C, джерело недосяжне    {k.get('named-unreachable', 0):5}   "
          f"М2: у них мережа ширша")
    print(f"\n── ремонт наявних записів ──")
    for hto, shcho, skilky, chomu in remonty():
        if skilky:
            print(f"  {hto:7} {shcho:24} {skilky:4}   {chomu}")
    return 0


def naryad() -> int:
    vsi, rozklad = zibraty()
    m1 = sum(len(v) for k, v in rozklad.items() if k.startswith("M1"))
    m2 = sum(len(v) for k, v in rozklad.items() if k.startswith("M2"))
    r = [
        "# Поділ незвіреного між супровідниками\n",
        "**Генерується** `factcheck/tools/split_queue.py --naryad`. Правити вручну нема "
        "сенсу.\n",
        "Поділ за одним питанням: **у якому джерелі лежить відповідь**. "
        "ESP-IDF, esptool і заголовки `soc/` дістаються з контейнера М1; "
        "datasheet мікросхем і електричні дані — ні, і це робота М2.\n",
        f"| | Кошик | Одиниць | Джерело |",
        "|---|---|---|---|",
    ]
    for hto, klyuch, opys, _ in KOSHYKY:
        r.append(f"| **{hto}** | `{klyuch}` | {len(rozklad[f'{hto}-{klyuch}'])} "
                 f"| {opys} |")
    r += [
        f"\n**М1 разом: {m1}. М2 разом: {m2}.**\n",
    ]

    # Повний облік. Таблиця вище — лише те, де джерело **вгадується з
    # тексту**. Це менша частина решти, і подавати її як «поділ роботи»
    # означало б показати десяту частину боргу за весь борг.
    k = klasy()
    e_ref = round(k.get("no-external-signal", 0) * CHASTKA_E_Z_REFERENTOM)
    slabki = len(rozklad["—"])
    r += [
        "## Уся решта, а не лише сильний сигнал\n",
        "Таблиця вище ділить те, де джерело видно з самого тексту "
        "одиниці. Це менша частина боргу. Нижче — увесь він, включно з "
        "тим, чого найближчим часом не візьме ніхто: **пункт «ніхто, і "
        "ось чому» — теж поділ, а мовчазна прогалина — ні.**\n",
        "| Пласт | Одиниць | Кому | Чому саме так |",
        "|---|---|---|---|",
        f"| `F`, джерело видно з тексту | {m1 + m2} | М1 {m1}, М2 {m2} "
        "| за досяжністю джерела з контейнера |",
        f"| `F`, слабкий сигнал | {slabki} | **нікому** "
        "| ознаки, за якою ділити, немає; чекає на суцільні проходи |",
        f"| `E`, оцінка з референтом | ~{e_ref} | обом порівну "
        f"| {CHASTKA_E_Z_REFERENTOM:.0%} від {k.get('no-external-signal', 0)} за випадковою "
        "вибіркою; ділиться розділами, бо джерело наперед невідоме |",
        f"| `C`, джерело недосяжне звідси | {k.get('named-unreachable', 0)} | М2 "
        "| у них ширша мережа; для М1 це 403 за побудовою |",
        "",
        "### Ремонт наявних записів\n",
        "Окремий рід роботи: він не додає звіреного, але без нього "
        "відсотки брешуть. Реєстр, який бреше про себе, гірший за менший "
        "чесний.\n",
        "| Що | Скільки | Кому |",
        "|---|---|---|",
    ]
    for hto, shcho, skilky, chomu in remonty():
        if skilky:
            r.append(f"| {shcho} — {chomu} | {skilky} | {hto} |")
    r.append("")
    e1, e2, s1, s2 = podil_e()
    r.append(f"### Поділ класу `E` за файлами — М1 {s1}, М2 {s2}\n")
    r.append("Ділиться **файлами, не одиницями**: двоє в одному файлі "
             "дають конфлікт злиття на кожному записі. Перетин "
             "перевіряється в інструменті.\n")
    r.append(f"**М1 ({len(e1)}):** " + ", ".join(f"`{x}`" for x in e1) + "\n")
    r.append(f"**М2 ({len(e2)}):** " + ", ".join(f"`{x}`" for x in e2) + "\n")
    r.append("### Чому `E` ділиться розділами, а не джерелами\n")
    r.append("Бо джерело там наперед **невідоме** — у цьому вся суть "
             "класу. Ділити за досяжністю можна лише те, про що вже "
             "знаєш, де воно лежить. Тому `E` ділиться діапазонами "
             "розділів: це єдиний поділ, який гарантує, що двоє не "
             "візьмуть ту саму одиницю.\n")
    for hto, klyuch, opys, _ in KOSHYKY:
        k = f"{hto}-{klyuch}"
        if not rozklad[k]:
            continue
        r.append(f"\n## {hto} · `{klyuch}` — {len(rozklad[k])}\n")
        r.append(f"{opys.capitalize()}.\n")
        za_faylom = collections.defaultdict(list)
        for u in rozklad[k]:
            za_faylom[u["src"]].append(u)
        for src in sorted(za_faylom):
            r.append(f"\n### `{src}` — {len(za_faylom[src])}\n")
            r.append("| Твердження | Рядок | Дослівно |")
            r.append("|---|---|---|")
            for u in za_faylom[src]:
                t = " ".join(x[2:] for x in u["txt"].strip().split("\n"))
                t = t.replace("|", "\\|")[:150]
                r.append(f"| `{u['id']}` | {u['ln']} | {t} |")
    (FC / "reports" / "SPLIT.md").write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"factcheck/reports/SPLIT.md: М1 {m1}, М2 {m2}, поза поділом "
          f"{len(rozklad['—'])}")
    return 0


if __name__ == "__main__":
    sys.exit(naryad() if "--naryad" in sys.argv else zvedennya())
