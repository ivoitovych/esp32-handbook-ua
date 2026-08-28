#!/usr/bin/env python3
"""Каркас реєстру фактчекінгу: паралельна структура до тіла книги.

Ідея. Рецензія читає розділ і питає «чи це узгоджено». Фактчекінг бере
**окреме твердження** і питає «звідки це відомо». Друге питання не
масштабується в голові: у книзі тисячі тверджень, і жодне читання не
гарантує, що жодне з них не пропущене.

Тому реєстр будується механічно й **повний за побудовою**: інструмент
розкладає кожен файл книги на одиниці тверджень і створює паралельний
документ, у якому кожна одиниця має свій запис. Далі проходи заповнюють
записи доказами. Одиниця без доказу — видима порожнеча, а не забутий
рядок.

    tools/factcheck.py sketch     створити або досинхронізувати каркас
    tools/factcheck.py status     зведення за класами доказів
    tools/factcheck.py stale      чи реєстр іще про цю книгу
    tools/factcheck.py blocked    перелік недоступних джерел на винос

Синхронізація. У кожному записі лежить хеш дослівного тексту книги. Якщо
текст у книзі змінили, `stale` це показує: доказ міг стосуватися
попереднього формулювання. Це те, що відрізняє живий реєстр від знімка,
який тихо розходиться з книгою.

Слово «якщо» тут довго було обіцянкою, а не описом: `stale` перевіряв
лише, чи існує файл. Формулювання лишили як є — тому й не помітили.
"""

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("kartky", "manual", "dodatky", "inserts")
FC = ROOT / "factcheck"

# Класи доказу. Порядок = спадання сили.
KLASY = {
    "A": "первинне дослівне — витяг із першоджерела отримано й процитовано",
    "B": "первинне похідне — першоджерело отримано, твердження випливає однозначно",
    "C": "вторинне — джерело не дістається звідси; URL записано, цитати немає",
    "D": "обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне",
    "E": "сигналу для звірки в тексті немає — присвоєно механічно, не перевірено",
    "L": "дивилися й не знайшли — робота зроблена, джерела не видно",
    "F": "не звірено",
    "G": "спростовано або потребує правки",
    "K": "контекст — блок коду цілком; твердження в його рядках",
}
ZNAK = {"A": "✅", "B": "🟢", "C": "🟡", "D": "🔵", "E": "⚪", "F": "🔴",
        "G": "⚠", "K": "▫", "L": "🔎"}

# Один перелік на всіх. Додавання класу `L` показало, навіщо: `status`
# перебирав рядок "ABCDEFG", і новий клас просто не з'явився у звіті —
# ані як помилка, ані як нуль. Ще шість тулів тримали свою копію того
# самого рядка.
#
# > Це рід 3 у `DEFECTS.md` збоку, з якого його не чекали: не перевірка
# > мовчить, а **перелік**, за яким вона ходить. Копія переліку — така
# > сама обіцянка не міняти його, як копія взірця.
USI_KLASY = "".join(KLASY)                      # A B C D E L F G K
KLASY_ODYNYC = "".join(k for k in KLASY if k != "K")   # без блоків коду

RE_ZAPYS = re.compile(
    r"<!--\s*fc\s+id:(?P<id>[\w.-]+)\s+sha:(?P<sha>[0-9a-f]{8})"
    r"\s+src:(?P<src>[^\s]+)\s+klas:(?P<klas>[A-GKL])\s*-->"
)


# Один взірець на всіх, хто читає з картки **короткий виклад
# твердження**. Раніше кожен споживач тримав свою копію рядка «Книга
# каже, дослівно:». Заголовок змінився на «Твердження, коротко» — і
# жоден із них не впав: `blocked`, `cherha`, `shukaty` та `podil.py`
# мовчки почали знаходити порожньо, а звіти лишилися на вигляд
# правильними.
#
# > Взірець, що читає чужий формат, мусить жити в одному місці з тим,
# > хто цей формат пише. Копія взірця — це обіцянка не міняти формат,
# > якої ніхто не давав.
RE_TVERDZHENNYA = re.compile(
    r"\*\*Твердження, коротко\*\*\n\n(?P<txt>(?:> [^\n]*\n)+)")


# Роди одиниць, чий текст у картці — **рендер**, а не текст книги.
#
# Комірка таблиці стає рядком `BME280 · Адреса → 0x76`, якого в книзі
# немає; такій картці потрібен окремий блок із сирим рядком.
#
# Проза — навпаки: `rozbyty()` бере речення **з книги**, тож текст
# одиниці вже дослівний (перевірено: 46 із 46 речень розділу 63
# знаходяться в книзі підрядком). Додавати їй «дослівний» блок не лише
# зайве — воно шкодить: книга переносить рядки посеред речення, і блок
# показував **обрізок**:
#
#     T-63-002  …льна роль ESP32 у чужій системі (розділ 57), і
#
# Це знайшов аудит М2: 5194 картки з 8331 обривалися на півслові. За
# моєю, суворішою мірою — 3851. Рід той самий, що ми вже тричі
# записували під іншими іменами («обрив думки», «комірка без
# контексту»): **виконавець судить половину думки.** Тільки цього разу
# половину нарізав інструмент, зроблений саме проти цього.
#
# > Умова була `syryy != txt` — тобто «показати, якщо відрізняється».
# > Для прози вона правдива через саме лише перенесення рядка. Умова
# > мала питати про **рід одиниці**, а не про нерівність рядків.
RENDER = ("komirka", "tablycya", "tablycya-shapka")


def sha(text: str) -> str:
    return hashlib.sha256(" ".join(text.split()).encode("utf-8")).hexdigest()[:8]


# Рядок коду, який щось стверджує про світ: виклик, константа, команда,
# запис у регістр. Решта (дужки, коментарі, оголошення змінних) нічого не
# стверджує і в реєстр не йде.
RE_KOD_TVERDZHENNYA = re.compile(
    r"^\s*(?:"
    r"#define\s+\w+|"
    r"#include\s*[<\"]|"
    r"[A-Za-z_][\w:.]*\s*\([^;]*\)\s*[;,]?\s*$|"          # виклик
    r"\.\w+\s*=|"                                          # ініціалізація поля
    r"(?:esptool|idf\.py|espefuse|pio|nvs_partition_gen|picocom|minicom|"
    r"screen|dd|python|strings|xtensa-|riscv32-|sudo|ls|dmesg|lsof|git|make)\b"
    r")"
)


# Зовнішньо перевірюваний сигнал у тексті одиниці.
#
# Навіщо. Реєстр повний за побудовою, і серед тисяч одиниць є такі, для
# яких зовнішнього джерела не існує й не буде: редакційне судження,
# порада, рамка викладу, зв'язка між розділами. Тримати їх у класі `F`
# («не звірено») — означає обіцяти роботу, якої ніхто не робитиме, і
# ховати за ними ті одиниці, які звірити справді треба.
#
# Тому одиниця **без жодного зовнішнього сигналу** переводиться в клас
# `E` — «сигналу для звірки в тексті немає»: ні цифри, ні ідентифікатора,
# ні назви, ні одиниці виміру. Це наслідок правила, а **не** висновок,
# що джерела не існує. Випадкова вибірка на 160 одиницях показала, що
# зовнішній референт має близько 37 % із них.
#
# Критерій навмисно перестрахований у бік `F`:
#   · будь-яка цифра — сигнал (числа перевіряються завжди);
#   · будь-що в зворотних лапках — сигнал (ідентифікатор, команда, рядок);
#   · назва чипа, шини, протоколу, бібліотеки, компонента — сигнал;
#   · одиниця виміру словами — сигнал.
# І застосовується він **лише до прози**. Таблиці, комірки, рядки коду й
# зв'язки схем не переводяться ніколи: саме там живуть факти, і комірка
# на кшталт «0 · Touch → T1» виглядає порожньою лише тому, що підмет
# рядка стоїть окремо.
RE_ZOVNISHNIY_SYGNAL = re.compile(
    r"`[^`]+`"                       # ідентифікатор, команда, рядок логу
    r"|\d"                           # будь-яке число
    r"|ESP32|ESP8266|S2|S3|C3|C6|H2|P4"
    r"|(?:I²C|SPI|UART|TWAI|CAN|RS-485|Modbus|LoRa|Wi-Fi|BLE|MQTT|HTTP|HTTPS|"
    r"TLS|NVS|OTA|JTAG|PWM|ADC|DAC|DMA|PSRAM|SRAM|GPIO|IEEE|USB|SDIO|NMEA|"
    r"FreeRTOS|ESP-IDF|ESP-NOW|Arduino|PlatformIO|MicroPython|ESPHome|Wokwi|"
    r"LVGL|U8g2|TFT_eSPI|LovyanGFX|RadioLib|GxEPD2|MOSFET|ESC|LDO|RTC|eFuse|"
    r"brownout|watchdog|bootloader|coredump|backtrace)"
    r"|(?:мікроампер|міліампер|ампер|вольт|герц|ват|ом|байт|біт|секунд|"
    r"мілісекунд|мікросекунд|градус)\w*"
)


# Строгий тест зовнішнього сигналу — для комірок таблиць і для прози.
#
# Широкий `RE_ZOVNISHNIY_SYGNAL` вище лишає одиницю в роботі від будь-якої
# цифри, і це правильно як обережність, але дорого як політика: номер
# пункту списку («…перевірити живлення. 4.») тримає в класі F твердження,
# у якому нема чого звіряти.
#
# Тут навпаки: сигналом вважається лише те, що **вказує на джерело** —
# число з одиницею, шістнадцяткова адреса, номер піна, номер каналу,
# версія, ідентифікатор у зворотних лапках, назва чипа, шини, протоколу
# чи мікросхеми. Усе інше — редакційне, і клас E для нього рішення, а не
# пропуск.
#
# Правило свідомо консервативне в один бік: сумнівне лишається в F.
RE_SYGNAL_STROGYY = re.compile(
    r"`[^`]+`"                                     # ідентифікатор, команда
    r"|\d+\s*(?:мА|мкА|А|В|мВ|кОм|Ом|МОм|МГц|кГц|Гц|МБ|КБ|ГБ|біт|байт|"
    r"мс|мкс|нс|°C|дБм|мм|см|Гн|нФ|мкФ|пФ|%)"      # число з одиницею
    r"|0x[0-9A-Fa-f]+|GPIO\s?\d+|IO\d+"            # адреса, пін
    r"|\bпін\w*\s+\d|\bканал\w*\s+\d|\d+\s*(?:пін|вивод|канал|розряд)"
    r"|\bv\d+(?:\.\d+)*"                          # версія
    r"|[A-Z]{2,}[0-9]{2,}[A-Z0-9-]*"               # BME280, MAX485, AT24C32
    r"|ESP32|ESP8266|\bS2\b|\bS3\b|\bC3\b|\bC6\b|\bH2\b|\bP4\b|\bC5\b|\bC2\b"
    r"|I²C|I²S|SPI|UART|TWAI|CAN|RS-485|Modbus|LoRa|Wi-Fi|BLE|MQTT|HTTP|TLS"
    r"|NVS|OTA|JTAG|PWM|ADC|DAC|DMA|PSRAM|SRAM|GPIO|USB|SDIO|RMT|LEDC|MCPWM"
    r"|SDMMC|eFuse|RTC|ULP|FreeRTOS|ESP-IDF|ESP-NOW|Arduino|PlatformIO"
    r"|MicroPython|ESPHome|brownout|watchdog|bootloader|coredump|backtrace"
    r"|strapping|menuconfig"
)


# Рядок ASCII-схеми: два виводи, з'єднані лінією. Кожен такий рядок —
# **окреме** твердження, і майже завжди з іншим джерелом, ніж сусідній:
# «3V3 ─── VCC» перевіряється за datasheet датчика, «SDA ─── GPIO21» —
# за документацією плати, «└─[4.7к]─ 3V3» — за специфікацією шини.
#
# Доти схема реєструвалася одним записом, і доказ на будь-яку її частину
# позначав звіреною всю. Зовнішня рецензія 2026-08-26 показала, чим це
# кінчається: повна схема проєкту 59 стояла з доказом на datasheet
# BME280, який ніколи не міг би підтвердити наявність `GPIO22` у S3.
RE_SCHEMA_ZVYAZOK = re.compile(r"[─━]{2,}|[│┬└┌┐┘├┤]|-{3,}[>\s]|→")


def rozbyty_tablycyu(ryadky: list[str], vid: int) -> list[tuple[str, str, int]]:
    """Таблиця → окреме твердження на кожну **комірку**, а не на рядок.

    Рядок «| UART | 3 | 2 | 3 | 2 | 3 | 2 |» — це шість незалежних
    тверджень про шість різних чипів, і звіреність п'яти з них нічого не
    каже про шосте. Тому комірка розкладається у формі «рядок · колонка →
    значення», яка читається як самостійне речення.

    Таблиці на дві колонки лишаються цілими: там рядок і є твердженням
    («симптом → причина»), і різати його безглуздо.
    """
    korysni = [r for r in ryadky if not re.match(r"^\|[\s:|-]+\|$", r.strip())]
    if not korysni:
        return []

    def komirky(r: str) -> list[str]:
        return [c.strip() for c in r.strip().strip("|").split("|")]

    shapka = komirky(korysni[0])
    if len(shapka) <= 2:
        return [("tablycya", r.strip(), vid + i) for i, r in enumerate(ryadky)
                if not re.match(r"^\|[\s:|-]+\|$", r.strip())]

    out: list[tuple[str, str, int]] = []
    out.append(("tablycya-shapka", korysni[0].strip(), vid))
    for i, r in enumerate(korysni[1:], 1):
        k = komirky(r)
        pidmet = k[0] if k else ""
        for j, v in enumerate(k[1:], 1):
            if j >= len(shapka) or not v or v in ("—", "-", ""):
                continue
            kolonka = shapka[j] or f"колонка {j}"
            out.append(("komirka", f"{pidmet} · {kolonka} → {v}", vid + i))
    return out


def rozbyty(text: str) -> list[tuple[str, str, int]]:
    """Файл → перелік (вид, дослівний текст, номер рядка).

    Види одиниць:
      proza            речення поза кодом і таблицями
      tablycya         рядок таблиці на дві колонки
      tablycya-shapka  шапка широкої таблиці
      komirka          окрема комірка широкої таблиці
      kod              блок коду цілком — як контекст
      kod-ryadok       окремий рядок коду, що щось стверджує

    Заголовки, порожні рядки й розмітку блоків пропускаємо: вони нічого
    не стверджують про світ.
    """
    odynyci: list[tuple[str, str, int]] = []
    ryadky = text.split("\n")
    i, n = 0, len(ryadky)
    # Кожен рядок несе свій номер: інакше всі речення абзацу дістають
    # номер його **початку**, і картка обіцяє точність, якої не має.
    #
    # Спіймано звіркою з `shar1.py` М2: п'ять карток списку в `k01`
    # стояли з одним номером 38, тоді як пункти лежать на 38–42. Мій
    # `stale` цього не бачив і побачити не міг — він звіряє генератор
    # сам із собою, а не з книгою.
    #
    # > Дві перевірки того самого шару розійшлися, і обидві мали рацію:
    # > одна питала «чи реєстр із цієї книги», друга — «чи номер веде
    # > туди, куди обіцяє». Друге питання ми не ставили ніколи.
    buf: list[tuple[int, str]] = []
    buf_vid = 0

    def zlyty_prozu():
        nonlocal buf, buf_vid
        if not buf:
            return
        # Зшиваємо блок і запам'ятовуємо, з якого символу починається
        # кожен рядок — щоб потім віддати реченню номер його власного
        # рядка, а не рядка абзацу.
        chastky, mezhi, poz = [], [], 0
        for nomer, x in buf:
            s = x.strip()
            if not s:
                continue
            mezhi.append((poz, nomer))
            chastky.append(s)
            poz += len(s) + 1
        blok = " ".join(chastky)
        buf = []
        if not blok:
            return

        def ryadok_dlya(zmishchennya: int) -> int:
            ostannij = buf_vid
            for p, nomer in mezhi:
                if p > zmishchennya:
                    break
                ostannij = nomer
            return ostannij

        # Речення. Крапка в «0x1000.» або «v5.5» не завершує речення, тому
        # ділимо лише там, де за розділовим знаком іде велика літера або тире.
        shukach = 0
        chastyny = re.split(r"(?<=[.!?])\s+(?=[«»А-ЯЇІЄҐA-Z\[`*—-])", blok)
        for c in chastyny:
            zm = blok.find(c, shukach)
            if zm < 0:
                zm = shukach
            shukach = zm + len(c)
            c = c.strip()
            if len(c) >= 25:
                odynyci.append(("proza", c, ryadok_dlya(zm)))

    while i < n:
        r = ryadky[i]
        if r.lstrip().startswith("```"):
            zlyty_prozu()
            start = i
            i += 1
            while i < n and not ryadky[i].lstrip().startswith("```"):
                i += 1
            tilo = ryadky[start + 1:i]
            odynyci.append(("kod", "\n".join(ryadky[start:i + 1]), start + 1))
            for j, kr in enumerate(tilo):
                if RE_SCHEMA_ZVYAZOK.search(kr):
                    odynyci.append(("schema-zvyazok", kr.strip(), start + 2 + j))
                elif RE_KOD_TVERDZHENNYA.match(kr) and len(kr.strip()) > 6:
                    odynyci.append(("kod-ryadok", kr.strip(), start + 2 + j))
            i += 1
            continue
        if r.startswith("|"):
            zlyty_prozu()
            start = i
            while i < n and ryadky[i].startswith("|"):
                i += 1
            odynyci += rozbyty_tablycyu(ryadky[start:i], start + 1)
            continue
        if r.startswith("#") or r.startswith(":::") or not r.strip():
            zlyty_prozu()
            i += 1
            continue
        if not buf:
            buf_vid = i + 1
        buf.append((i + 1, r))
        i += 1
    zlyty_prozu()
    return odynyci


def shlyakh_reyestru(f: Path) -> Path:
    return FC / f.relative_to(ROOT)


def prefiks(f: Path) -> str:
    """Стабільний префікс ідентифікатора: 06 з manual/06-zhyvlennya.md."""
    m = re.match(r"([a-z]?\d+|[a-z])-", f.stem)
    return (m.group(1) if m else f.stem[:3]).upper()


DOKAZY = FC / "dokazy"


def zavantazhyty_dokazy() -> list[dict]:
    """Докази з `factcheck/dokazy/*.yaml` — перелік записів.

    Запис прив'язується до тверджень двома способами.

    **`sha:`** — точний хеш дослівного тексту. Ключем узято хеш, а не
    ідентифікатор, бо ідентифікатор — це порядковий номер у файлі, і
    вставлене вище речення зсуває всі наступні. Хеш прив'язаний до самого
    твердження, тож доказ їде за ним при перевпорядкуванні — і навпаки,
    **відв'язується сам**, щойно формулювання змінили. Друге не менш
    важливе за перше: доказ стосувався тих слів, а не цих.

    **`zbih:`** — взірець. Одне й те саме твердження живе в книзі в
    кількох місцях (розділ, картка, додаток), і доводиться воно один раз.
    Взірець покриває всі входження, а `sketch` друкує, що саме покрив, —
    щоб зіставлення лишалося перевірюваним, а не магічним.
    """
    import yaml
    out: list[dict] = []
    if not DOKAZY.exists():
        return out
    for p in sorted(DOKAZY.glob("*.yaml")):
        for z in (yaml.safe_load(p.read_text(encoding="utf-8")) or []):
            z["_prokhid"] = p.stem
            out.append(z)
    return out


# Сила класу доказу. Менше — сильніше.
SYLA = {"A": 0, "B": 1, "D": 2, "C": 3, "L": 4, "E": 5, "G": 6, "F": 7}


def pidibraty(zapysy: list[dict], h: str, txt: str) -> dict | None:
    """Доказ для твердження: точний хеш має перевагу, далі — найсильніший.

    Одне твердження може підпадати під кілька доказів: прохід записав
    його в наряд як недосяжне, наступний знайшов обхідний шлях. Брати
    треба **найсильніший**, а не той, що трапився першим, — інакше
    порядок файлів у каталозі мовчки визначав би результат, і закриті
    пункти лишалися б у наряді назавжди.
    """
    kandydaty = vsi_kandydaty(zapysy, h, txt)
    if kandydaty:
        return min(kandydaty, key=lambda z: SYLA.get(z.get("klas", "F"), 9))
    return None


def klyuch(z: dict) -> tuple[str, str]:
    """Тотожність запису доказу для обліку покриття.

    Не назва: назви беруться з формулювань наряду, тож двоє супровідників
    природно приходять до однакових. За ключем-назвою слабший однойменний
    запис зникав і з «нічого не зачепив», і з «перекрито сильнішим» — а
    перший із цих переліків існує саме для того, щоб ловити хибний взірець.
    """
    return (str(z.get("_prokhid", "?")), str(z.get("nazva", "?")))


def rozbyty_alternatyvy(vzirets: str) -> list[str]:
    """Розібрати `zbih` по `|` **верхнього рівня**.

    Потрібне для аудиту окремих альтернатив. Знахідка М2 від 15:47Z:
    `sketch -v` бачить мертвий доказ, але не бачить мертву альтернативу
    в живому доказі. Перша альтернатива спрацювала — запис виглядає
    здоровим, і те, що друга не збіглася з жодним рядком, не видно
    ніде: ані в переліку покриття, ані в жодному чеку.

    Це важить саме тому, що альтернативи ми **нарощуємо**: доказ
    тягнеться з розділу на картки й додатки додаванням гілок, і кожна
    додана гілка — окрема нагода мовчки промахнутися.

    Рахуємо дужки і не ріжемо всередині `[...]`; `\|` — літерал.
    """
    chastyny: list[str] = []
    tek: list[str] = []
    hlyb = 0
    u_klasi = False
    i = 0
    while i < len(vzirets):
        c = vzirets[i]
        if c == "\\" and i + 1 < len(vzirets):
            tek.append(vzirets[i:i + 2])
            i += 2
            continue
        if u_klasi:
            tek.append(c)
            if c == "]":
                u_klasi = False
        elif c == "[":
            u_klasi = True
            tek.append(c)
        elif c == "(":
            hlyb += 1
            tek.append(c)
        elif c == ")":
            hlyb -= 1
            tek.append(c)
        elif c == "|" and hlyb == 0:
            chastyny.append("".join(tek))
            tek = []
        else:
            tek.append(c)
        i += 1
    chastyny.append("".join(tek))
    return [x for x in chastyny if x]


# Друга форма тихої брехні взірця (знахідка М2 від 16:39Z): альтернатива
# з самої лише назви предмета. `RP2040` збігається з **кожною** коміркою
# колонки RP2040 — зокрема з «Ціна плати → низька», яку доказ позначив
# класом B на підставі заголовка з адресами пам'яті.
#
# Ловити це за формою слова не вийде: `RP2040` і `264 КБ` обидва містять
# цифри, а `Raspberry Pi` і `40 мА` обидва мають пробіл. Ловиться це за
# **наслідком**: широка альтернатива зачіпає багато одиниць, а доказ
# говорить про одну. Тому аудит не судить про форму, а друкує число
# збігів кожної альтернативи окремо — і рішення лишає людині, яка бачить
# цитату поруч.
SHYROKA_ALTERNATYVA = 4


def prychyna(chastyna: str, teksty: list[str]) -> str:
    """Чому альтернатива не зачепила нічого — здогад, не вирок.

    Перебираємо послаблення взірця по одному. Те, від якого він оживає,
    і називає ваду. Три з них узято з випадків, що вже траплялися:

      регістр   — велика літера на початку речення. Двоє супровідників
                  наступили на це незалежно протягом години;
      перенос   — текст книги переносить рядок там, де взірець чекав
                  пробіл. З'являється, коли взірець пишуть, дивлячись у
                  зверстаний вигляд, а не в джерело;
      пробіли   — зайвий або відсутній пробіл усередині.

    Четвертий випадок — коли не оживає нічого: текст книги змінився
    після написання доказу. Це не вада взірця, а робота, яку треба
    зробити: перевірити, чи доказ ще стосується нового формулювання.
    """
    try:
        if any(re.search(chastyna, x, re.S | re.I) for x in teksty):
            return "оживає без урахування регістру — велика літера"
    except re.error:
        return "недійсний взірець сам по собі"
    bez_perenosu = [re.sub(r"\s+", " ", x) for x in teksty]
    ch_plaskyy = re.sub(r"\\s\*\\n\?|\\s\+|\\n", " ", chastyna)
    try:
        if any(re.search(ch_plaskyy, x, re.S | re.I) for x in bez_perenosu):
            return "оживає на злитих пробілах — перенос рядка в книзі"
    except re.error:
        pass
    # Голова взірця — перші літери до першого спецсимволу. Якщо навіть
    # вона не трапляється ніде, предмет із книги зник, а не з'їхав.
    holova = re.split(r"[\\(\[.*+?{|^$]", chastyna, 1)[0].strip()
    if len(holova) >= 4 and not any(holova.lower() in x.lower()
                                    for x in teksty):
        return f"у книзі немає навіть «{holova}» — текст змінився"
    return "початок є, решта розійшлася — звірити з новим текстом"


def vsi_kandydaty(zapysy: list[dict], h: str, txt: str) -> list[dict]:
    """Усі докази, що взагалі підпадають під це твердження.

    Потрібно окремо від вибору, щоб відрізнити доказ, перекритий
    сильнішим, від доказу, який не зачепив нічого: перше — норма
    (прохід закрив пункт наряду), друге — помилка у взірці.
    """
    tochni = [z for z in zapysy if h in [str(x) for x in (z.get("sha") or [])]]
    if tochni:
        return tochni
    return [z for z in zapysy
            if z.get("zbih") and _vzirets(z["zbih"]).search(txt)]


# Взірців 1337, а внутрішній кеш `re` тримає 512: без власного кешу
# кожен виклик перекомпільовував ті самі взірці, і повний обхід
# «одиниці × докази» тривав хвилини замість секунд.
_KESH_VZIRCIV: dict[str, "re.Pattern[str]"] = {}


def _vzirets(v: str) -> "re.Pattern[str]":
    rx = _KESH_VZIRCIV.get(v)
    if rx is None:
        rx = _KESH_VZIRCIV[v] = re.compile(v, re.S)
    return rx


SHABLON_DOKAZU = """**Доказ**

- **Клас:** F — не звірено
"""


def formatuvaty_dokaz(z: dict | None) -> str:
    if not z:
        return SHABLON_DOKAZU
    klas = z.get("klas", "F")
    ch = [f"**Доказ**\n", f"- **Клас:** {ZNAK.get(klas,'')} {klas} — {KLASY.get(klas,'')}"]
    if z.get("dzherelo"):
        ch.append(f"- **Джерело:** {z['dzherelo']}")
    if z.get("cytata"):
        tilo = "\n".join("  > " + x for x in str(z["cytata"]).rstrip().split("\n"))
        ch.append(f"- **Дослівно з джерела:**\n{tilo}")
    if z.get("rozrakhunok"):
        tilo = "\n".join("  " + x for x in str(z["rozrakhunok"]).rstrip().split("\n"))
        ch.append(f"- **Розрахунок:**\n{tilo}")
    if z.get("sposib"):
        ch.append(f"- **Спосіб і дата:** {z['sposib']}")
    if z.get("shukaty"):
        ch.append(f"- **Що шукати в джерелі:** {z['shukaty']}")
    if z.get("notatka"):
        ch.append(f"- **Нотатка:** {z['notatka']}")
    ch.append(f"- **Прохід:** {z.get('_prokhid','—')}")
    return "\n".join(ch) + "\n"


def ohorozha(vmist: str) -> str:
    """A fence longer than any backtick run inside the content.

    The context of a code claim **is** a fenced block, so wrapping it in
    ``` closes the wrapper at the inner fence and the rest of the card
    renders as loose text. Caught on `T-K01-030` by generating a single
    file instead of the whole registry.

    Markdown allows any fence of three or more backticks, and a longer
    one may contain a shorter one — so the fence is chosen from the
    content rather than fixed.
    """
    naydovsha = 0
    for shmatok in re.findall(r"`+", vmist):
        naydovsha = max(naydovsha, len(shmatok))
    return "`" * max(3, naydovsha + 1)


def dослівно_і_контекст(ryadky: list[str], ln: int,
                        tekst: str = "") -> tuple[str, str]:
    """Сирий рядок книги та його оточення.

    **Навіщо.** Досі картка несла лише рендер одиниці —
    `BME280 · Адреса → 0x76` — під заголовком «Книга каже, дослівно».
    Такого рядка в книзі немає, тож заголовок брехав, а картку не можна
    було віддати ані людині, ані помічникові: щоб зрозуміти твердження,
    треба було лізти в книгу.

    Ціна цього була вимірна. Три сесії поспіль ми записували роди
    хибних тривог — «поділ відрізає застереження», «комірка без
    контексту», «суперечка про ступінь» — і всі вони одна причина:
    **виконавець судив половину думки.** Одинадцять заявлених
    суперечностей, жодної справжньої.

    **Що вважається контекстом.** Для рядка таблиці — найближчий
    заголовок вище, речення перед таблицею, шапка таблиці й сама
    таблиця. Для прози — абзац і сусідні абзаци.

    Номер рядка тут — єдина річ, якій довіряють, і вона ненадійна: М2
    поміряли, що він застарілий у 1311 одиницях із 8090. Тому функція
    **не падає** на хибному номері: поза межами файлу вона чесно
    віддає порожнє, і картка це показує.
    """
    # Номер рядка — **локатор, а не якір**, і він застаріває від кожної
    # правки книги без перегенерації: М2 поміряли, що він хибний у 1311
    # одиницях із 8090.
    #
    # Перша редакція цієї функції брала рядок просто за номером — і
    # картка про `ESP8266 / ESP-12` дістала дослівний рядок про
    # `ESP32-C3-MINI-1`, бо номер зсунувся на одиницю. Нове поле брехало
    # **впевненіше** за старий рендер, який воно мало виправити.
    #
    # Тому спершу **пошук за вмістом**, і лише як запасний шлях — номер.
    # Ключі беруться з самої одиниці: для комірки це значення обабіч
    # роздільників рендеру.
    # Рендер комірки має вигляд `<рядок> · <колонка> → <значення>`.
    # **Назва колонки стоїть у шапці таблиці, а не в рядку даних** — і
    # саме вона провалила першу спробу пошуку: `all(...)` не збігався
    # ніколи, тож функція мовчки падала назад на застарілий номер.
    # Тому ключі — лише «рядок» і «значення».
    if " · " in tekst:
        label, _, resh = tekst.partition(" · ")
        _, _, znach = resh.partition(" → ")
        syrovyna = [label, znach]
    else:
        syrovyna = [tekst]
    klyuchi = [k.strip(" `*") for k in syrovyna if len(k.strip(" `*")) >= 3]
    i = -1
    if klyuchi:
        for j, r in enumerate(ryadky):
            if all(k in r for k in klyuchi):
                i = j
                break
    if i < 0:
        i = ln - 1
    if not (0 <= i < len(ryadky)):
        return "", ""
    doslivno = ryadky[i].rstrip()

    # Межі: назад до заголовка або порожнього рядка перед абзацом,
    # уперед до кінця абзацу чи таблиці.
    poch = i
    while poch > 0:
        pop = ryadky[poch - 1].rstrip()
        if pop.startswith("#"):
            break
        if not pop and not doslivno.startswith("|"):
            break
        if not pop and poch < i and not ryadky[poch].startswith("|"):
            break
        poch -= 1
    kin = i
    while kin + 1 < len(ryadky):
        nast = ryadky[kin + 1].rstrip()
        if not nast or nast.startswith("#"):
            break
        kin += 1

    # Заголовок розділу дає темі ім'я, а без імені комірка таблиці
    # читається як набір слів.
    zah = ""
    for j in range(poch, -1, -1):
        if ryadky[j].startswith("#"):
            zah = ryadky[j].rstrip()
            break

    tilo = [r.rstrip() for r in ryadky[poch:kin + 1]]
    if zah and zah not in tilo:
        tilo = [zah, ""] + tilo
    return doslivno, "\n".join(tilo).strip()


def sketch() -> int:
    FC.mkdir(exist_ok=True)
    dokazy = zavantazhyty_dokazy()
    vsjogo = z_dokazom = 0
    vzhyti: set[str] = set()
    # Ключем обліку служить пара «файл доказів + назва», а не сама
    # назва. Двоє супровідників беруть назви з того самого наряду, тож
    # збіг імен у різних файлах — очікуваний стан, а не випадковість.
    # За ключем-назвою слабший однойменний запис зникав з обох
    # переліків нижче, і доказ із хибним взірцем лишався невидимим.
    pokryttya: dict[tuple[str, str], list[str]] = {}
    zachepleni: set[tuple[str, str]] = set()
    # Тексти всіх одиниць — для окремого аудиту кожної альтернативи
    # взірця. Тримати їх коштує пам'яті, але дешевше, ніж другий обхід.
    usi_teksty: list[str] = []
    # `--only <substring>` limits the run to matching book files.
    #
    # Rebuilding the whole registry takes about half an hour, and a
    # format change that is wrong is only visible at the end of it.
    # Twice today a defect survived a full run: the card locator read a
    # stale line number, and the first fix searched for a key that lives
    # in the table header and so never matched.
    #
    # A format change is now tried on one file first. The rule is the
    # project's own `Р-ЗВІРКА`: test the instrument, then apply it.
    lyshe = None
    if "--only" in sys.argv:
        lyshe = sys.argv[sys.argv.index("--only") + 1]

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            if lyshe and lyshe not in str(f):
                continue
            tekst_knyhy = f.read_text(encoding="utf-8")
            ryadky_knyhy = tekst_knyhy.split("\n")
            odynyci = rozbyty(tekst_knyhy)
            cil = shlyakh_reyestru(f)
            cil.parent.mkdir(parents=True, exist_ok=True)
            pre = prefiks(f)
            chastyny = [
                f"# Фактчекінг: `{f.relative_to(ROOT)}`\n",
                f"Одиниць твердження: **{len(odynyci)}**. "
                "Клас доказу й формат запису — `factcheck/SCHEMA.md`.\n",
                "Цей файл **генерується**: текст книги береться з джерела, "
                "докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.\n",
                # Сказано раз на файл, а не на кожній із тисяч карток:
                # рецензентові потрібна ця гарантія, але вона однакова
                # для всіх карток файлу.
                "**Що в блоці «Твердження, коротко».** Для прози, рядка "
                "коду й зв'язки схеми — **дослівний текст книги**. Для "
                "комірки таблиці — рендер (`BME280 · Адреса → 0x76`), "
                "якого в книзі немає; дослівний рядок такої одиниці "
                "стоїть окремим блоком нижче.\n",
                "---\n",
            ]
            for k, (vyd, txt, ln) in enumerate(odynyci, 1):
                ident = f"T-{pre}-{k:03d}"
                h = sha(txt)
                usi_teksty.append(txt)
                kandydaty = vsi_kandydaty(dokazy, h, txt)
                for k_z in kandydaty:
                    zachepleni.add(klyuch(k_z))
                z = (min(kandydaty, key=lambda z: SYLA.get(z.get("klas", "F"), 9))
                     if kandydaty else None)
                if z:
                    vzhyti.add(h)
                    z_dokazom += 1
                    pokryttya.setdefault(klyuch(z), []).append(ident)
                # Блок коду цілком — **контекст**, а не твердження. Він
                # складається з рядків, у кожного з яких своє джерело, і
                # доказ на один рядок не звіряє решту. Тому клас блоку не
                # успадковується від доказу, а фіксований: `K`.
                if vyd == "kod":
                    klas = "K"
                elif z:
                    klas = z.get("klas", "F")
                elif vyd in ("proza", "komirka", "tablycya") \
                        and not RE_SYGNAL_STROGYY.search(txt):
                    # Одиниця без жодного сигналу, що вказував би на
                    # джерело, — редакційна. Клас E, і це рішення, а не
                    # пропуск (див. коментар біля RE_SYGNAL_STROGYY).
                    #
                    # Зв'язки схем (`vyd == "shema"`) сюди не потрапляють
                    # ніколи: саме там живуть факти, і рядок «3V3 ─── VCC»
                    # виглядає порожнім лише тому, що підмет стоїть окремо.
                    klas = "E"
                else:
                    klas = "F"
                cyt = "\n".join("> " + x for x in txt.split("\n"))
                # Картка мусить бути самодостатньою: її віддають людині
                # або виконавцеві **без** доступу до книги. Тому поруч
                # із коротким викладом стоять сирий рядок і оточення.
                syryy, kontekst = dослівно_і_контекст(ryadky_knyhy, ln, txt)
                dodatkovo = ""
                if vyd in RENDER and syryy and syryy.strip() != txt.strip():
                    # Комірка живе в рядку таблиці. Якщо локатор привів
                    # кудись іще — він **промахнувся**, і показати цей
                    # рядок було б гірше, ніж не показати нічого: картка
                    # твердила б дослівність про чужий текст.
                    #
                    # Тридцять один такий випадок: взірець комірки
                    # «SPI · …» збігся з прозовим пунктом «**Швидкі
                    # сигнали** — SPI на високих частотах…».
                    if syryy.lstrip().startswith("|"):
                        o = ohorozha(syryy)
                        dodatkovo += ("**Дослівно з книги**\n\n"
                                      f"{o}\n{syryy}\n{o}\n\n")
                    else:
                        dodatkovo += (
                            "**Дослівно з книги:** рядок таблиці не "
                            "знайдено — локатор привів у прозу. Дивіться "
                            "контекст нижче.\n\n")
                if kontekst:
                    o = ohorozha(kontekst)
                    dodatkovo += ("**Контекст**\n\n"
                                  f"{o}\n{kontekst}\n{o}\n\n")
                elif not syryy:
                    dodatkovo += ("**Контекст:** номер рядка застарів — "
                                  "рядок за ним у книзі не знайдено.\n\n")
                chastyny.append(
                    f"<!-- fc id:{ident} sha:{h} "
                    f"src:{f.relative_to(ROOT)}:{ln} klas:{klas} -->\n"
                    f"### {ident} · {vyd} · `{f.relative_to(ROOT)}`\n\n"
                    f"**Твердження, коротко**\n\n{cyt}\n\n{dodatkovo}"
                    f"{formatuvaty_dokaz(z)}\n---\n"
                )
                vsjogo += 1
            cil.write_text("\n".join(chastyny), encoding="utf-8")
    print(f"файлів реєстру: {sum(1 for _ in FC.rglob('*.md'))}")
    print(f"одиниць твердження: {vsjogo}; із доказом: {z_dokazom}")
    if "-v" in sys.argv:
        print("\nщо покрив кожен доказ:")
        for (prokhid, nazva), ids in sorted(pokryttya.items(),
                                           key=lambda kv: kv[0][1]):
            print(f"  {len(ids):>3}×  {nazva}  ({prokhid})"
                  f"\n        {', '.join(ids)}")
    # Доказ, який нічого не зачепив, — це або застаріле формулювання в
    # книзі, або помилка у взірці. Мовчати про це не можна: реєстр почне
    # обіцяти звіреність, якої немає.
    #
    # Інша річ — доказ, що зачепив твердження, але програв сильнішому.
    # Це норма й навіть мета: слабший запис проходу 3 («джерело не
    # дістається») перекритий класом A проходу 4 означає, що пункт
    # наряду закрито. Такий випадок показуємо окремо й без тривоги.
    holosti = [z for z in dokazy if klyuch(z) not in zachepleni]
    perekryti = [z for z in dokazy
                 if klyuch(z) in zachepleni
                 and klyuch(z) not in pokryttya]
    if holosti:
        print(f"\n⚠ доказів, що нічого не зачепили: {len(holosti)}")
        for z in holosti:
            print(f"    {z.get('nazva','?')}  ({z.get('_prokhid')})")
    if perekryti:
        print(f"\nперекрито сильнішим доказом: {len(perekryti)}")
        for z in perekryti:
            print(f"    {z.get('nazva','?')}  "
                  f"({z.get('_prokhid')}, клас {z.get('klas','?')})")

    # Аудит окремих альтернатив. Дві вади, невидимі вище:
    #
    #   мертва   — альтернатива не зачепила нічого, але сусідня
    #              спрацювала, тож доказ виглядає здоровим;
    #   широка   — альтернатива зачепила більше одиниць, ніж доказ
    #              узагалі стверджує.
    #
    # Обидві занижують або завищують покриття мовчки, і жоден чек на них
    # не падає. Тому це звіт, а не ворота: судити, чи 12 збігів широкі,
    # може лише той, хто бачить цитату.
    mertvi: list[tuple[dict, str, str]] = []
    shyroki: list[tuple[dict, str, int]] = []
    for z in dokazy:
        vz = z.get("zbih")
        if not vz:
            continue
        chastyny = rozbyty_alternatyvy(vz)
        if len(chastyny) < 2:
            continue
        for ch in chastyny:
            try:
                r = re.compile(ch, re.S)
            except re.error:
                # Альтернатива, вирвана з контексту, може бути
                # недійсним взірцем сама по собі — це не вада доказу.
                continue
            n = sum(1 for x in usi_teksty if r.search(x))
            if n == 0:
                mertvi.append((z, ch, prychyna(ch, usi_teksty)))
            elif n >= SHYROKA_ALTERNATYVA:
                shyroki.append((z, ch, n))
    if mertvi:
        print(f"\n⚠ альтернатив без жодного збігу: {len(mertvi)}")
        for z, ch, ch_prychyna in mertvi:
            print(f"    {z.get('nazva','?')}  ({z.get('_prokhid')})"
                  f"\n        ↳ {ch}"
                  f"\n          ({ch_prychyna})")
    if shyroki and "-v" in sys.argv:
        print(f"\nальтернатив від {SHYROKA_ALTERNATYVA} збігів: "
              f"{len(shyroki)}")
        for z, ch, n in sorted(shyroki, key=lambda x: -x[2]):
            print(f"  {n:>3}×  {z.get('nazva','?')}  ({z.get('_prokhid')})"
                  f"\n        ↳ {ch}")
    return 0


def zbir_usikh() -> list[dict]:
    out = []
    for p in sorted(FC.rglob("*.md")):
        if p.name in ("README.md", "SCHEMA.md", "STATUS.md", "dzherela.md"):
            continue
        t = p.read_text(encoding="utf-8")
        for sh in re.split(r"(?=<!--\s*fc\s)", t):
            m = RE_ZAPYS.search(sh)
            if m:
                d = m.groupdict()
                d["fajl"] = str(p.relative_to(FC))
                d["tilo"] = sh
                out.append(d)
    return out


def status() -> int:
    zapysy = zbir_usikh()
    c = Counter(z["klas"] for z in zapysy)
    kontekst = c.get("K", 0)
    # Блоки коду — контекст, а не твердження: відсотки рахуються від
    # тверджень, інакше знаменник роздувається тим, що ніхто й не збирався
    # звіряти.
    vsjogo = len(zapysy) - kontekst
    print(f"\nодиниць твердження: {vsjogo}"
          f"  (+ {kontekst} блоків коду як контекст)\n")
    zvireno = sum(c[k] for k in "ABD")
    for k in KLASY_ODYNYC:
        n = c.get(k, 0)
        if not n:
            continue
        print(f"  {ZNAK[k]} {k}  {n:>5}  {n*100/vsjogo:5.1f}%   {KLASY[k]}")
    print(f"\n  звірено з джерелом або обчисленням (A+B+D): "
          f"{zvireno} ({zvireno*100/vsjogo:.1f}%)")
    print(f"  закрито як рішення (E): {c.get('E',0)}")
    print(f"  лишається (C+F+G): {c.get('C',0)+c.get('F',0)+c.get('G',0)}")
    # за файлами: де найбільше незакритого
    per = Counter()
    for z in zapysy:
        if z["klas"] in "CFG":
            per[z["fajl"]] += 1
    if per:
        print("\n  найбільше незакритого:")
        for f, n in per.most_common(8):
            print(f"    {n:>4}  {f}")
    return 0


def stale() -> int:
    """Чи розійшовся реєстр із книгою — і чим саме.

    ## Що тут було до 2026-08-27

    Докстрінг обіцяв «записи, чий текст у книзі змінився». Тіло
    перевіряло, **чи існує файл**. Про текст — жодного рядка.

    Через це реєстр чотири дні тихо відставав від книги: шість правок
    друкованого накладу не зрушили лічильника, і `make check` усі ці
    дні казав «розбіжностей немає». Знайшов М2, написавши перевірку з
    нуля саме тому, що не повірив, ніби її ще нема.

    > Це вже другий випадок того самого роду за день (перший — `vorota`:
    > обіцяно дві перевірки, зроблено одну). Обидва прожили довго з тієї
    > самої причини: **лічильник, що показує нуль, виглядає однаково і
    > коли все гаразд, і коли він нічого не рахує.**

    ## Що тут тепер

    Книга розбирається тими самими `rozbyty()` і `sha()`, що будують
    реєстр, і результат звіряється з тим, що лежить на диску. Спільний
    розбирач тут не економія, а вимога: своя копія розбору розійшлася б
    із генератором, і перевірка почала б підтверджувати саму себе.

    Три роди розходження, і вони різні за ціною:

    · **текст змінився** — доказ, прив'язаний до старого формулювання,
      більше не про це твердження. Дорого: тихо хибний доказ.
    · **зник / з'явився** — правка додала або прибрала твердження.
    · **зсунувся рядок** — текст той самий, поїхав лише номер. Дешево
      само собою, дорого через довіру: кожен, хто бере `src:рядок` із
      реєстру, дістає адресу, яка може бути мимо.
    """
    na_dysku: dict[str, dict] = {}
    for z in zbir_usikh():
        na_dysku[z["id"]] = z

    zminyly: list[tuple[str, str]] = []
    znykly: list[str] = []
    novi: list[str] = []
    zsuv: Counter[str] = Counter()

    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            pre = prefiks(f)
            rel = str(f.relative_to(ROOT))
            bachyly: set[str] = set()
            for i, (_vyd, txt, ln) in enumerate(rozbyty(
                    f.read_text(encoding="utf-8")), 1):
                ident = f"T-{pre}-{i:03d}"
                bachyly.add(ident)
                z = na_dysku.get(ident)
                if z is None:
                    novi.append(ident)
                    continue
                if z["sha"] != sha(txt):
                    zminyly.append((ident, rel))
                elif z["src"] != f"{rel}:{ln}":
                    zsuv[rel] += 1
            for ident, z in na_dysku.items():
                if z["src"].split(":")[0] == rel and ident not in bachyly:
                    znykly.append(ident)

    print(f"  текст змінився   {len(zminyly)}")
    for ident, rel in zminyly[:20]:
        print(f"     ✗ {ident}  {rel}")
    print(f"  зникло записів   {len(znykly)}")
    for ident in znykly[:10]:
        print(f"     ✗ {ident}")
    print(f"  нових одиниць    {len(novi)}")
    for ident in novi[:10]:
        print(f"     + {ident}")
    print(f"  зсув номера рядка {sum(zsuv.values())} на {len(zsuv)} файлах")
    for rel, n in zsuv.most_common(6):
        print(f"     ~ {n:>4}  {rel}")

    if zminyly or znykly or novi or zsuv:
        print("\n  реєстр відстає від книги — `factcheck.py sketch` "
              "перед роботою")
    else:
        print("  реєстр збігається з книгою одиниця в одиницю")
    return 0
    return 0


NARYAD = FC / "UNREACHABLE-SOURCES.md"


def blocked() -> int:
    """Наряд на винос: усе, що впирається в недосяжне звідси джерело.

    Клас C — не «не перевірили», а «перевірити звідси неможливо». Різниця
    між ними головна: перше закривається роботою тут, друге не
    закривається ніколи, скільки не працюй, і мусить поїхати в інше
    середовище.

    Тому команда не просто рахує, а **пише документ**, придатний віддати
    людині з відкритим доступом: джерело, скільки тверджень від нього
    залежать, що саме в ньому шукати і які твердження книги це закриє.
    Уся підготовча робота вже зроблена — лишається відкрити документ.
    """
    grupy: dict[str, dict] = {}
    for z in zbir_usikh():
        if z["klas"] != "C":
            continue
        mu = re.search(r"\*\*Джерело:\*\*[ \t]*(.+)", z["tilo"])
        u = " ".join(mu.group(1).split()) if mu else "—"
        sh = (re.search(r"\*\*Що шукати в джерелі:\*\*\s*(.+)", z["tilo"]) or [None, ""])[1]
        m = RE_TVERDZHENNYA.search(z["tilo"])
        txt = " ".join(m.group(1).replace("> ", "").split()) if m else ""
        g = grupy.setdefault(u, {"shukaty": set(), "tverdzhennya": []})
        if sh:
            g["shukaty"].add(sh.strip())
        g["tverdzhennya"].append((z["id"], z["src"], txt))

    if not grupy:
        print("записів класу C немає")
        return 0

    vsjogo = sum(len(g["tverdzhennya"]) for g in grupy.values())
    ryadky = [
        "# Наряд: джерела, недосяжні з цього середовища\n",
        "**Це не перелік помилок.** Це перелік тверджень книги, які "
        "неможливо звірити з першоджерелом із контейнера, де книга "
        "робилася: політика egress відповідає `403` на домени виробників "
        "і стандартів.\n",
        "Кожен пункт підготовано до закриття: named джерело, що саме в "
        "ньому шукати, і які саме твердження книги від нього залежать. "
        "Людині з відкритим доступом лишається відкрити документ і "
        "звірити — робота вимірюється хвилинами на джерело.\n",
        "Закриті пункти повертаються сюди як докази класу `A` або `B` у "
        "`factcheck/dokazy/`, після чого цей файл перегенеровується "
        "(`tools/factcheck.py blocked`) і коротшає.\n",
        f"Станом на генерацію: **{vsjogo}** тверджень від "
        f"**{len(grupy)}** джерел.\n",
        "---\n",
    ]
    for u, g in sorted(grupy.items(), key=lambda kv: -len(kv[1]["tverdzhennya"])):
        ryadky.append(f"## {u}\n")
        ryadky.append(f"Залежить тверджень: **{len(g['tverdzhennya'])}**\n")
        if g["shukaty"]:
            ryadky.append("**Що шукати:**\n")
            for s in sorted(g["shukaty"]):
                ryadky.append(f"- {s}")
            ryadky.append("")
        ryadky.append("| Твердження | Де в книзі | Дослівно |")
        ryadky.append("|---|---|---|")
        for ident, src, txt in g["tverdzhennya"]:
            t = txt.replace("|", "\\|")[:160]
            ryadky.append(f"| `{ident}` | `{src}` | {t} |")
        ryadky.append("\n---\n")
    NARYAD.write_text("\n".join(ryadky), encoding="utf-8")

    print(f"\n{NARYAD.relative_to(ROOT)}: {vsjogo} тверджень від "
          f"{len(grupy)} джерел\n")
    for u, g in sorted(grupy.items(), key=lambda kv: -len(kv[1]["tverdzhennya"])):
        print(f"  {len(g['tverdzhennya']):>4}   {u}")
    return 0


# Ознаки, за якими твердження взагалі можна звірити із зовнішнім джерелом.
# Вага = наскільки дорого коштує помилка саме в цій ознаці.
SYGNALY = [
    (re.compile(r"0x[0-9A-Fa-f]{3,8}"), 5, "адреса"),
    (re.compile(r"GPIO\s?\d{1,2}"), 5, "пін"),
    (re.compile(r"\b(?:eFuse|strapping|Secure Boot|Flash Encryption)\b", re.I), 4, "незворотне"),
    (re.compile(r"\b[a-z_]+_[a-z_]+\("), 4, "виклик API"),
    (re.compile(r"\bCONFIG_[A-Z0-9_]+|menuconfig"), 4, "налаштування"),
    (re.compile(r"\d+(?:[.,]\d+)?\s*(?:мкА|мА|А|В|мВ|Ом|кОм|МОм|Гц|кГц|МГц|ГГц|"
                r"мкс|мс|с|год|КБ|МБ|ГБ|біт|бод|нФ|мкФ|°C|мм|см|м|Вт)\b"), 3, "число"),
    (re.compile(r"\b(?:esptool|idf\.py|espefuse|nvs_partition_gen|pio)\b"), 3, "команда"),
    (re.compile(r"\b(?:ESP32-[A-Z0-9]+|WROOM|WROVER|BME280|DS18B20|MAX\d+|"
                r"SN65HVD230|TP4056|SSD1306|HC-SR04|A4988|L298N)\b"), 3, "позиція"),
    (re.compile(r"\b(?:ADC|DAC|PWM|LEDC|MCPWM|RMT|PCNT|TWAI|I²C|SPI|UART|I²S|"
                r"NVS|OTA|PSRAM|IRAM|DMA)\b"), 2, "блок"),
]


def vaga(txt: str) -> tuple[int, list[str]]:
    v, chym = 0, []
    for rex, w, nazva in SYGNALY:
        if rex.search(txt):
            v += w
            chym.append(nazva)
    return v, chym


def cherga() -> int:
    """Незакриті твердження, найдорожчі першими.

    Прохід не має йти по книзі підряд: одиниця «Якщо в цій книзі є один
    розділ» і одиниця «GPIO 6–11 з'єднані з флешем» коштують різного.
    Черга ставить попереду те, де помилка коштує плати.
    """
    mezha = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    poz = []
    for z in zbir_usikh():
        if z["klas"] not in "CFG":
            continue
        m = RE_TVERDZHENNYA.search(z["tilo"])
        if not m:
            continue
        txt = m.group(1)
        v, chym = vaga(txt)
        if v:
            poz.append((v, z["id"], z["fajl"], ",".join(chym),
                        " ".join(txt.replace("> ", "").split())[:100]))
    poz.sort(key=lambda x: (-x[0], x[1]))
    print(f"\nнезакритих зі звірюваними ознаками: {len(poz)}"
          f"  (показано {min(mezha, len(poz))})\n")
    for v, ident, fajl, chym, txt in poz[:mezha]:
        print(f"  [{v:>2}] {ident:<12} {chym:<28} {txt}")
    return 0


def shukaty() -> int:
    """`factcheck.py shukaty <підрядок>` → sha і текст твердження.

    Ключ доказу — хеш, а хеш у голові не тримають. Ця команда — місток
    між «пам'ятаю формулювання» і «знаю, під яким ключем його записати».
    """
    if len(sys.argv) < 3:
        print("вкажіть підрядок")
        return 1
    goloka = " ".join(sys.argv[2:]).lower()
    n = 0
    for z in zbir_usikh():
        m = RE_TVERDZHENNYA.search(z["tilo"])
        if not m:
            continue
        txt = " ".join(m.group(1).replace("> ", "").split())
        if goloka in txt.lower():
            print(f"  {z['sha']}  {ZNAK[z['klas']]}{z['klas']}  {z['id']:<12} "
                  f"{z['src']}\n      {txt[:150]}")
            n += 1
            if n >= 30:
                print("  …")
                break
    if not n:
        print("не знайдено")
    return 0


def vorota() -> int:
    """Випускні ворота реєстру (Р-VYPUSK).

    Що тут перевіряється — і чого свідомо немає.

    **Є:** жодного твердження класу `G`. `G` означає «джерело
    спростувало» — книга з таким записом суперечить сама собі, і
    випускати її не можна за жодних обставин.

    **Є:** жодного доказу, що нічого не зачепив. Такий доказ — або
    застаріле формулювання в книзі, або помилка у взірці; в обох
    випадках реєстр обіцяє звіреність, якої немає.

    **Немає:** вимоги «нуль класу F». Це навмисно. Реєстр розкладає
    книгу на тисячі одиниць, серед яких є редакційні судження й поради,
    яким зовнішнє джерело не потрібне й не буває. Вимога нуля змусила б
    закривати їх фіктивно — тобто зробила б реєстр гіршим, а не кращим.
    Правило натомість таке: `F` видимий і рахований, а `C` має наряд.
    """
    dokazy = zavantazhyty_dokazy()
    g = [z for z in dokazy if str(z.get("klas", "")).upper() == "G"]
    for z in g:
        print(f"   ✗ спростоване твердження: {z.get('nazva','?')} "
              f"({z.get('_prokhid')})")

    # Друга обіцянка docstring, якої тут **не було**: доказ, що не
    # зачепив жодної одиниці.
    #
    # Знайдено зовнішньою рецензією: опис казав про дві перевірки,
    # реалізація робила одну. Це гірше за відсутню перевірку — читач
    # контракту вважає інваріант захищеним, а він не захищений ніким.
    #
    # Правило, яке з цього випливає: **на кожен інваріант має бути
    # рівно один авторитетний перевіряч, і опис не є перевірячем.**
    teksty: list[str] = []
    for grupa in GRUPY:
        for f in sorted((ROOT / grupa).glob("*.md")):
            for _vyd, txt, _ln in rozbyty(f.read_text(encoding="utf-8")):
                teksty.append(txt)

    holosti = []
    for z in dokazy:
        vz = str(z.get("zbih", ""))
        if not vz:
            continue
        try:
            rx = re.compile(vz)
        except re.error as e:
            print(f"   ✗ взірець не компілюється: {z.get('nazva','?')} "
                  f"({z.get('_prokhid')}) — {e}")
            holosti.append(z)
            continue
        if not any(rx.search(t) for t in teksty):
            holosti.append(z)
            print(f"   ✗ доказ нічого не зачепив: {z.get('nazva','?')} "
                  f"({z.get('_prokhid')})")

    print(f"factcheck-vorota: спростованих (G) {len(g)}, "
          f"холостих доказів {len(holosti)}")
    return 1 if (g or holosti) else 0


def vzirets() -> int:
    """Скільки одиниць реєстру зачепить цей взірець.

        tools/factcheck.py vzirets '<регулярний вираз>'

    ## Навіщо окрема команда на три рядки коду

    Бо без неї перевіряють **не тим джерелом**, і я зробив це тричі за
    вечір, знаючи про пастку й описавши її сам.

    Взірець `zbih` зіставляється з **текстом одиниці реєстру**, а не з
    розміткою книги. Для прози це те саме, і саме тому помилка не
    впадає в око. Для комірки таблиці — ні:

        книга:   | Частота | 160–240 МГц | 16 МГц | 133 МГц |
        реєстр:  Частота · RP2040 → 133 МГц

    Взірець `\\| 133 МГц \\|` збігається з книгою й **не збігається ні з
    чим** у реєстрі. Перевірка `grep` по `manual/` каже «усе гаразд», і
    доказ тихо не зачіпає нічого.

    М2 на цій самій пастці мало не видалили 124 справні записи, бо
    писали швидшу перевірку по тексту книги. Правило записане в
    `docs/DESIGN.md` як `Р-ЗВІРКА`. Правила виявилося замало: доки
    зробити правильно було дорожче, ніж `grep`, я щоразу робив `grep`.

    Тому команда. Тепер правильне дешевше за неправильне.
    """
    if len(sys.argv) < 3:
        print("вжиток: tools/factcheck.py vzirets '<вираз>'")
        return 2
    vyraz = sys.argv[2]
    try:
        rx = re.compile(vyraz)
    except re.error as e:
        print(f"негодящий вираз: {e}")
        return 2

    zbihy: list[tuple[str, str]] = []
    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            for _vyd, txt, _ln in rozbyty(f.read_text(encoding="utf-8")):
                if rx.search(txt):
                    zbihy.append((f.name, txt))

    print(f"взірець зачіпає одиниць: {len(zbihy)}")
    if not zbihy:
        print("  ⚠ ХОЛОСТИЙ — жодної одиниці. Доказ із таким взірцем "
              "нічого не звіряє.")
        return 1
    if len(zbihy) > 12:
        print("  ⚠ ЗАШИРОКИЙ? Широкий взірець небезпечніший за "
              "відсутній: він мовчки позначає «звірено» те, чого не "
              "звіряв.")
    for imya, txt in zbihy[:12]:
        print(f"    {imya}: {txt.strip()[:88]}")
    if len(zbihy) > 12:
        print(f"    … ще {len(zbihy) - 12}")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    return {"sketch": sketch, "status": status, "stale": stale,
            "blocked": blocked, "cherga": cherga, "vorota": vorota,
            "shukaty": shukaty, "vzirets": vzirets}.get(cmd, status)()


if __name__ == "__main__":
    sys.exit(main())
