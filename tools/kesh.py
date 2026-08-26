#!/usr/bin/env python3
"""Кеш зовнішніх джерел: файли поруч, маніфест у репозиторії.

Навіщо. Одне datasheet закриває десятки тверджень, але лише доки воно
відкрите. Качати його наново на кожен запис — найдорожча частина
фактчекінгу, і саме вона гальмує роботу вдвох.

Що робить. Кладе завантажене в `dzherela-kesh/`, рахує sha256 і пише
рядок у `dzherela-kesh/MANIFEST.md`: URL, ім'я, розмір, хеш, дата.

    tools/kesh.py <URL> [ім'я]   завантажити й записати в маніфест
    tools/kesh.py --list         що вже є
    tools/kesh.py --check        чи збігаються хеші з маніфестом
    tools/kesh.py --size         скільки займає

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
KESH = ROOT / "dzherela-kesh"
MANIFEST = KESH / "MANIFEST.md"
MEZHA_GB = 1.0

ZAHOLOVOK = """# Кеш зовнішніх джерел — маніфест

**Генерується** `tools/kesh.py`. Самі файли в git **не входять**: це
чужий матеріал під копірайтом, і перевидавати його ми не маємо права
(докладно — у шапці `tools/kesh.py`).

У git іде цей перелік. За ним будь-хто завантажує ті самі файли й
звіряє `sha256`: збігся — читає дослівно те саме, що цитував автор
доказу.

```sh
tools/kesh.py <URL>      завантажити й записати сюди
tools/kesh.py --check    звірити хеші наявних файлів
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
    KESH.mkdir(exist_ok=True)
    if imya is None:
        imya = re.sub(r"[^\w.-]", "_", url.rsplit("/", 1)[-1] or "bez-imeni")
    cil = KESH / imya
    r = subprocess.run(["curl", "-sSL", "--fail", "-o", str(cil), url])
    if r.returncode != 0 or not cil.exists():
        print(f"   ✗ не завантажилося: {url}")
        return 1
    z = zapysy()
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
    print(f"kesh: записів {len(z)}, розбіжностей {bidy}")
    return 1 if bidy else 0


def rozmir() -> int:
    if not KESH.exists():
        print("kesh: каталогу немає")
        return 0
    b = sum(p.stat().st_size for p in KESH.rglob("*") if p.is_file())
    gb = b / 1e9
    print(f"kesh: {gb:.3f} ГБ із {MEZHA_GB} ГБ")
    if gb > MEZHA_GB:
        print("   · межу перевищено — вирішіть, що видалити")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "--list":
        sys.exit(perelik())
    if a[0] == "--check":
        sys.exit(zvirka())
    if a[0] == "--size":
        sys.exit(rozmir())
    sys.exit(zavantazhyty(a[0], a[1] if len(a) > 1 else None))
