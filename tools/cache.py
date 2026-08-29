#!/usr/bin/env python3
"""Кеш зовнішніх джерел: файли поруч, маніфест у репозиторії.

Навіщо. Одне datasheet закриває десятки тверджень, але лише доки воно
відкрите. Качати його наново на кожен запис — найдорожча частина
фактчекінгу, і саме вона гальмує роботу вдвох.

Що робить. Кладе завантажене в `source-cache/`, рахує sha256 і пише
рядок у `source-cache/MANIFEST.md`: URL, ім'я, розмір, хеш, дата.

    tools/cache.py <URL> [ім'я]   завантажити й записати в маніфест
    tools/cache.py --list         що вже є
    tools/cache.py --check        чи збігаються хеші з маніфестом
    tools/cache.py --size         скільки займає
    tools/cache.py --vidtvornist  чи може третя сторона звірити доказ

## Чому самі файли не комітяться

Datasheet виробників — **чужий матеріал під копірайтом**. Espressif,
Bosch, Semtech, Analog і решта дозволяють завантажувати й
використовувати, але не перевидавати. Покласти їхні PDF у публічний
репозиторій означає саме перевидати.

Проєкт, чия головна теза — «кожне твердження має джерело, і джерело
названо чесно», не може дозволити собі порушення авторського права в
службовому каталозі.

Тому в git іде **маніфест**, а не вміст: URL, за яким файл беруть, і
sha256, за яким перевіряють, що взяли той самий. Це дає все, заради чого
кеш заводили:

* відтворюваність — інший супровідник качає за тим самим URL і звіряє
  хеш; якщо збігся, він читає дослівно те саме, що цитував перший;
* швидкість — у межах однієї сесії файл качається один раз;
* чесність — видно, звідки взято, і видно, коли.

Розмір кешу обмежений `MEZHA_GB`. Перевищення — не помилка, а
попередження: вирішує людина, що видалити.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KESH = ROOT / "source-cache"
MANIFEST = KESH / "MANIFEST.md"
MEZHA_GB = 1.0

ZAHOLOVOK = """# Кеш зовнішніх джерел — маніфест

**Генерується** `tools/cache.py`. Самі файли в git **не входять**: це
чужий матеріал під копірайтом, і перевидавати його ми не маємо права
(докладно — у шапці `tools/cache.py`).

У git іде цей перелік. За ним будь-хто завантажує ті самі файли й
звіряє `sha256`: збігся — читає дослівно те саме, що цитував автор
доказу.

```sh
tools/cache.py <URL>      завантажити й записати сюди
tools/cache.py --check    звірити хеші наявних файлів
```

| Файл | sha256 | Байтів | Коли | URL |
|---|---|---|---|---|
"""


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def zapysy() -> dict[str, dict]:
    if not MANIFEST.exists():
        return {}
    out = {}
    for m in re.finditer(r"^\| `([^`]+)` \| `([0-9a-f]{64})` \| (\d+) \| "
                         r"([\d-]+) \| <([^>]+)> \|$",
                         MANIFEST.read_text(encoding="utf-8"), re.M):
        out[m.group(1)] = dict(sha=m.group(2), rozmir=int(m.group(3)),
                               koly=m.group(4), url=m.group(5))
    return out


def zapysaty(z: dict[str, dict]) -> None:
    r = [ZAHOLOVOK.rstrip("\n")]
    for imya in sorted(z):
        d = z[imya]
        r.append(f"| `{imya}` | `{d['sha']}` | {d['rozmir']} | {d['koly']} "
                 f"| <{d['url']}> |")
    vsjogo = sum(d["rozmir"] for d in z.values())
    r.append(f"\nФайлів: **{len(z)}**, разом **{vsjogo / 1e6:.1f} МБ** "
             f"(межа {MEZHA_GB} ГБ).\n")
    MANIFEST.write_text("\n".join(r) + "\n", encoding="utf-8")


def zavantazhyty(url: str, imya: str | None) -> int:
    """Завантажити й записати в маніфест.

    ## Ім'я береться з URL цілком, а не з останнього сегмента

    Було: `imya = url.rsplit("/", 1)[-1]`. Тобто ключем маніфесту ставав
    **базовий файлу**, і два різні документи з однаковою назвою
    затирали один одного — мовчки, разом із рядком маніфесту й самим
    файлом у кеші.

    Таких назв у документації ESP-IDF повно: `gpio.rst`, `i2c.rst`,
    `README.md`, `adc_channel.h` існують у десятку різних каталогів.

    Спіймано так: докачування 116 джерел **зменшило** число відтворних
    доказів. Дев'ятнадцять записів маніфесту зникло — кожен затерто
    однойменним файлом з іншої адреси.

    > Інструмент, чия єдина мета — відтворність, міг мовчки підмінити
    > документ під уже написаним доказом. Доказ і далі звірявся б — з
    > іншим файлом.

    Тепер до імені додається вісім знаків хешу URL. Це той самий вигляд,
    який уже мають 274 файли в кеші (`0015e29e-esp_log.h`) — тобто
    домовленість існувала, її просто не було в коді.
    """
    KESH.mkdir(exist_ok=True)
    if imya is None:
        bazove = re.sub(r"[^\w.-]", "_", url.rsplit("/", 1)[-1] or "bez-imeni")
        imya = f"{hashlib.sha256(url.encode()).hexdigest()[:8]}-{bazove}"
    cil = KESH / imya
    z = zapysy()
    # Той самий URL перекачати можна; чужий запис затерти — ні.
    if imya in z and z[imya].get("url") != url:
        print(f"   ✗ ім'я `{imya}` вже належить іншому URL:\n"
              f"       у маніфесті: {z[imya].get('url')}\n"
              f"       качаємо:     {url}")
        return 1
    r = subprocess.run(["curl", "-sSL", "--fail", "-o", str(cil), url])
    if r.returncode != 0 or not cil.exists():
        print(f"   ✗ не завантажилося: {url}")
        return 1
    z[imya] = dict(sha=sha256(cil), rozmir=cil.stat().st_size,
                   koly=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                   url=url)
    zapysaty(z)
    print(f"   ✓ {imya}  {cil.stat().st_size / 1e6:.2f} МБ")
    rozmir()
    return 0


def perelik() -> int:
    z = zapysy()
    if not z:
        print("kesh: порожньо")
        return 0
    for imya in sorted(z):
        d = z[imya]
        yе = "на місці" if (KESH / imya).exists() else "**немає локально**"
        print(f"  {d['rozmir'] / 1e6:8.2f} МБ  {imya:44} {yе}")
    return rozmir()


def zvirka() -> int:
    z = zapysy()
    bidy = 0
    for imya, d in sorted(z.items()):
        p = KESH / imya
        if not p.exists():
            print(f"   · {imya}: немає локально — качати за URL із маніфесту")
            continue
        s = sha256(p)
        if s != d["sha"]:
            print(f"   ✗ {imya}: sha256 не збігається з маніфестом")
            bidy += 1
        else:
            print(f"   ✓ {imya}")
    bezridni = unlisted_in_manifest(z)
    for imya, nazva in bezridni:
        print(f"   ✗ {imya}: доказ «{nazva[:44]}» цитує файл, якого в "
              f"маніфесті немає")
    bidy += len(bezridni)
    print(f"cache: записів {len(z)}, розбіжностей {bidy}")
    return 1 if bidy else 0


def unlisted_in_manifest(z: dict) -> list[tuple[str, str]]:
    """Докази, що цитують файл кешу без рядка в маніфесті.

    ## Чому це не те саме, що `--check`

    `--check` бере **рядки маніфесту** й питає, чи файл на місці й чи
    збігається хеш. Файл, якого в маніфесті немає взагалі, у це питання
    не потрапляє ніколи — його ніхто не перебирає.

    А саме такий файл і небезпечний: доказ на нього посилається,
    звіряється проти нього успішно, і **відтворити його не може ніхто,
    крім контейнера, який його викачав**. Це рід 9 каталогу, і до цього
    моменту він не мав жодної автоматичної перевірки.

    ## Міряно, перш ніж писати

        файлів у кеші без рядка в маніфесті       119
        джерел у доказах                          746
        з них цитують файл без рядка                2

    Сто дев'ятнадцять — не вада: це документи, які помічники качали під
    час хвиль і які доказом не стали. Вадою є **два**, і саме їх ця
    перевірка називає. Різниця між 119 і 2 — причина, чому перевірка
    питає про доказ, а не про кеш: питання «чи все в кеші записано»
    дало б сто дев'ятнадцять тривог, з яких сто сімнадцять хибні.

    Обидва знайдені реєстровано (`components/bt/Kconfig` і
    `esp_psram/esp32/Kconfig.spiram`, обидва з `raw.githubusercontent`),
    тож перевірка стає на нулі — і тому нижче стоїть проба на
    зіпсованому вході.
    """
    import yaml
    layer3 = _layer3()
    bidy: list[tuple[str, str]] = []
    for f in sorted((ROOT / "factcheck" / "evidence").glob("*.yaml")):
        try:
            zap = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for zapys in zap:
            if not isinstance(zapys, dict):
                continue
            for url in layer3.dzherela_zapysu(zapys):
                try:
                    imya = layer3.imya_dlya(url)
                except Exception:
                    continue
                if (KESH / imya).exists() and imya not in z:
                    nazva = str(zapys.get("nazva") or zapys.get("title") or "?")
                    bidy.append((imya, nazva))
    return bidy


def _layer3():
    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    import layer3
    return layer3


def proba() -> int:
    """Показ на зіпсованому вході: перевірка, що не спрацювала жодного
    разу, невідрізненна від перевірки, якої немає."""
    z = zapysy()
    spravzhni = unlisted_in_manifest(z)
    print(f"   {'✓' if not spravzhni else '✗ ПРОВАЛ'} чистий маніфест: "
          f"тривог {len(spravzhni)}, очікувано 0")
    # Прибираємо з копії маніфесту рядок файлу, який доказ таки цитує.
    import yaml
    layer3 = _layer3()
    vzhytyy = None
    for f in sorted((ROOT / "factcheck" / "evidence").glob("*.yaml")):
        try:
            zap = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for zapys in zap:
            if not isinstance(zapys, dict):
                continue
            for url in layer3.dzherela_zapysu(zapys):
                try:
                    imya = layer3.imya_dlya(url)
                except Exception:
                    continue
                if imya in z and (KESH / imya).exists():
                    vzhytyy = imya
                    break
            if vzhytyy:
                break
        if vzhytyy:
            break
    if not vzhytyy:
        print("   ✗ ПРОВАЛ: не знайшлося жодного вжитого файлу для проби")
        return 1
    kaliche = {k: v for k, v in z.items() if k != vzhytyy}
    zlamani = unlisted_in_manifest(kaliche)
    ok = any(i == vzhytyy for i, _ in zlamani)
    print(f"   {'✓' if ok else '✗ ПРОВАЛ'} рядок `{vzhytyy}` прибрано з "
          f"маніфесту: тривог {len(zlamani)}, очікувано ≥1")
    return 0 if (not spravzhni and ok) else 1


def rozmir() -> int:
    if not KESH.exists():
        print("kesh: каталогу немає")
        return 0
    b = sum(p.stat().st_size for p in KESH.rglob("*") if p.is_file())
    gb = b / 1e9
    print(f"cache: {gb:.3f} ГБ із {MEZHA_GB} ГБ")
    if gb > MEZHA_GB:
        print("   · межу перевищено — вирішіть, що видалити")
    return 0


def _fc():
    """`factcheck` завантажується ліниво: `cache.py` живе й без нього."""
    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    import factcheck
    return factcheck


def vidtvornist() -> int:
    """Чи може **третя сторона** перевірити доказ.

    ## Навіщо окремо від `--check`

    `--check` питає: чи файли на диску збігаються з маніфестом. Це
    перевірка **мого** кешу, і вона нічого не каже про того, хто прийде
    з боку.

    Кеш у git не входить (копірайт), тож єдиний місток назовні — рядок
    маніфесту: URL і `sha256`. Доказ, чиє джерело в маніфесті не
    названо, відтворний лише в тому контейнері, де його писали. Для
    всіх інших він — слово супровідника.

    Аудит 2026-08-28 показав, що таких **більшість**: 587 із 1025
    записів класів `A`/`B`. Докачування закритого списку підняло
    відтворність з 42 % до 67 %; решта впирається або в егрес, або в
    джерело, назване самою лише прозою.
    """
    import collections
    import yaml

    z = zapysy()
    man_url = {d["url"] for d in z.values()}
    man_bez = {(n.split("-", 1)[1] if re.match(r"^[0-9a-f]{8}-", n) else n)
               for n in z}
    k: collections.Counter = collections.Counter()
    prykl: dict[str, str] = {}
    teka = ROOT / "factcheck" / "evidence"
    for f in sorted(teka.glob("*.yaml")):
        try:
            zap = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception:
            continue
        for r in zap:
            if not isinstance(r, dict):
                continue
            if _fc().class_letter_of(r) not in ("A", "B"):
                continue
            d = " ".join(str(r.get("source") or r.get("source") or "").split())
            fajly = [x.split("-", 1)[1] if re.match(r"^[0-9a-f]{8}-", x) else x
                     for x in re.findall(r"source-cache/([\w.-]+)", d)]
            u = re.match(r"(https?://[^\s,;)]+)", d)
            if fajly:
                key = ("відтворно: файл у маніфесті"
                       if all(x in man_bez for x in fajly)
                       else "НІ: файл поза маніфестом")
            elif u:
                key = ("відтворно: URL у маніфесті" if u.group(1) in man_url
                       else "НІ: URL поза маніфестом")
            else:
                key = "НІ: джерело названо лише прозою"
            k[key] += 1
            prykl.setdefault(key, d[:76])

    vsjogo = sum(k.values())
    vidt = sum(n for key, n in k.items() if key.startswith("відтворно"))
    for key, n in k.most_common():
        print(f"  {n:>5}  {key}\n            {prykl[key]}")
    print(f"\nвідтворність доказів A/B: {vidt} із {vsjogo} "
          f"({100 * vidt // vsjogo if vsjogo else 0} %)")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "--list":
        sys.exit(perelik())
    if a[0] == "--check":
        sys.exit(zvirka())
    if a[0] == "--samoperevirka":
        sys.exit(proba())
    if a[0] == "--size":
        sys.exit(rozmir())
    if a[0] == "--vidtvornist":
        sys.exit(vidtvornist())
    sys.exit(zavantazhyty(a[0], a[1] if len(a) > 1 else None))
