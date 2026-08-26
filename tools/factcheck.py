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
    tools/factcheck.py stale      твердження, текст яких змінився в книзі
    tools/factcheck.py blocked    перелік недоступних джерел на винос

Синхронізація. У кожному записі лежить хеш дослівного тексту книги. Якщо
текст у книзі змінили, запис позначається як застарілий: доказ міг
стосуватися попереднього формулювання. Це те, що відрізняє живий реєстр
від знімка, який тихо розходиться з книгою.
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
    "E": "поза зовнішньою звіркою — редакційне рішення, порада, рамка викладу",
    "F": "не звірено",
    "G": "спростовано або потребує правки",
}
ZNAK = {"A": "✅", "B": "🟢", "C": "🟡", "D": "🔵", "E": "⚪", "F": "🔴", "G": "⚠"}

RE_ZAPYS = re.compile(
    r"<!--\s*fc\s+id:(?P<id>[\w.-]+)\s+sha:(?P<sha>[0-9a-f]{8})"
    r"\s+src:(?P<src>[^\s]+)\s+klas:(?P<klas>[A-G])\s*-->"
)


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
    buf: list[str] = []
    buf_vid = 0

    def zlyty_prozu():
        nonlocal buf, buf_vid
        if not buf:
            return
        blok = " ".join(x.strip() for x in buf if x.strip())
        buf = []
        if not blok:
            return
        # Речення. Крапка в «0x1000.» або «v5.5» не завершує речення, тому
        # ділимо лише там, де за розділовим знаком іде велика літера або тире.
        chastyny = re.split(r"(?<=[.!?])\s+(?=[«»А-ЯЇІЄҐA-Z\[`*—-])", blok)
        for c in chastyny:
            c = c.strip()
            if len(c) >= 25:
                odynyci.append(("proza", c, buf_vid))

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
                if RE_KOD_TVERDZHENNYA.match(kr) and len(kr.strip()) > 6:
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
        buf.append(r)
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
SYLA = {"A": 0, "B": 1, "D": 2, "C": 3, "E": 4, "G": 5, "F": 6}


def pidibraty(zapysy: list[dict], h: str, txt: str) -> dict | None:
    """Доказ для твердження: точний хеш має перевагу, далі — найсильніший.

    Одне твердження може підпадати під кілька доказів: прохід записав
    його в наряд як недосяжне, наступний знайшов обхідний шлях. Брати
    треба **найсильніший**, а не той, що трапився першим, — інакше
    порядок файлів у каталозі мовчки визначав би результат, і закриті
    пункти лишалися б у наряді назавжди.
    """
    tochni = [z for z in zapysy if h in [str(x) for x in (z.get("sha") or [])]]
    if tochni:
        return min(tochni, key=lambda z: SYLA.get(z.get("klas", "F"), 9))
    zbihy = [z for z in zapysy
             if z.get("zbih") and re.search(z["zbih"], txt, re.S)]
    if zbihy:
        return min(zbihy, key=lambda z: SYLA.get(z.get("klas", "F"), 9))
    return None


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


def sketch() -> int:
    FC.mkdir(exist_ok=True)
    dokazy = zavantazhyty_dokazy()
    vsjogo = z_dokazom = 0
    vzhyti: set[str] = set()
    pokryttya: dict[str, list[str]] = {}
    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            odynyci = rozbyty(f.read_text(encoding="utf-8"))
            cil = shlyakh_reyestru(f)
            cil.parent.mkdir(parents=True, exist_ok=True)
            pre = prefiks(f)
            chastyny = [
                f"# Фактчекінг: `{f.relative_to(ROOT)}`\n",
                f"Одиниць твердження: **{len(odynyci)}**. "
                "Клас доказу й формат запису — `factcheck/SCHEMA.md`.\n",
                "Цей файл **генерується**: текст книги береться з джерела, "
                "докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.\n",
                "---\n",
            ]
            for k, (vyd, txt, ln) in enumerate(odynyci, 1):
                ident = f"T-{pre}-{k:03d}"
                h = sha(txt)
                z = pidibraty(dokazy, h, txt)
                if z:
                    vzhyti.add(h)
                    z_dokazom += 1
                    pokryttya.setdefault(z.get("nazva", "?"), []).append(ident)
                klas = z.get("klas", "F") if z else "F"
                cyt = "\n".join("> " + x for x in txt.split("\n"))
                chastyny.append(
                    f"<!-- fc id:{ident} sha:{h} "
                    f"src:{f.relative_to(ROOT)}:{ln} klas:{klas} -->\n"
                    f"### {ident} · {vyd} · рядок {ln}\n\n"
                    f"**Книга каже, дослівно:**\n\n{cyt}\n\n"
                    f"{formatuvaty_dokaz(z)}\n---\n"
                )
                vsjogo += 1
            cil.write_text("\n".join(chastyny), encoding="utf-8")
    print(f"файлів реєстру: {sum(1 for _ in FC.rglob('*.md'))}")
    print(f"одиниць твердження: {vsjogo}; із доказом: {z_dokazom}")
    if "-v" in sys.argv:
        print("\nщо покрив кожен доказ:")
        for nazva, ids in sorted(pokryttya.items()):
            print(f"  {len(ids):>3}×  {nazva}\n        {', '.join(ids)}")
    # Доказ, який нічого не покрив, — це або застаріле формулювання в
    # книзі, або помилка у взірці. Мовчати про це не можна: реєстр почне
    # обіцяти звіреність, якої немає.
    holosti = [z for z in dokazy
               if not any(z.get("nazva") == n for n in pokryttya)]
    if holosti:
        print(f"\n⚠ доказів, що нічого не покрили: {len(holosti)}")
        for z in holosti:
            print(f"    {z.get('nazva','?')}  ({z.get('_prokhid')})")
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
    vsjogo = len(zapysy)
    print(f"\nодиниць твердження: {vsjogo}\n")
    zvireno = sum(c[k] for k in "ABD")
    for k in "ABCDEFG":
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
    """Записи, чий текст у книзі змінився після останнього доказу."""
    n = 0
    for z in zbir_usikh():
        src, ln = z["src"].rsplit(":", 1)
        p = ROOT / src
        if not p.exists():
            print(f"  ⚠ {z['id']}: файл {src} зник")
            n += 1
    print(f"розбіжностей: {n}" if n else "розбіжностей немає")
    return 0


NARYAD = FC / "NARYAD-nedostupni.md"


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
        m = re.search(r"\*\*Книга каже, дослівно:\*\*\n\n(.+?)\n\n\*\*Доказ", z["tilo"], re.S)
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
        m = re.search(r"\*\*Книга каже, дослівно:\*\*\n\n(.+?)\n\n\*\*Доказ",
                      z["tilo"], re.S)
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
        m = re.search(r"\*\*Книга каже, дослівно:\*\*\n\n(.+?)\n\n\*\*Доказ",
                      z["tilo"], re.S)
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


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    return {"sketch": sketch, "status": status, "stale": stale,
            "blocked": blocked, "cherga": cherga,
            "shukaty": shukaty}.get(cmd, status)()


if __name__ == "__main__":
    sys.exit(main())
