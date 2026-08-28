#!/usr/bin/env python3
"""Шар 3 — ЗАСТАРІЛИЙ. Уживайте tools/layer3.py від М1: він потужніший
і перевіряє вихід помічника ДО того, як той потрапляє в реєстр.

Цей файл лишається лише через функцію znayty_ryadok (табличне
зіставлення), якої в layer3.py немає. Решта — дублювання.

Чи справді цитата є в джерелі.

Детермінований скрипт без жодної моделі. Бере кожен доказ класу `A`,
знаходить документ у кеші й перевіряє, що поле `cytata` справді в ньому є.

Що він ловить: вигадану цитату, зіпсований файл, підмінений документ,
цитату, приписану не тому джерелу.

Чого він НЕ ловить, і це головне: правильну цитату під хибним
твердженням. Джерело може містити число «40 мА» і не підпирати
твердження «40 мА — абсолютна межа». Це шар 2, і скрипт тут безсилий.

    tools/perevirka-tsytat-m2.py            перевірити все
    tools/perevirka-tsytat-m2.py -v         показати кожен рядок
"""
import re, sys, hashlib, pathlib, subprocess

KORIN = pathlib.Path(__file__).resolve().parent.parent
KESH = pathlib.Path.home() / "dzherela-cache"
DOKAZY = KORIN / "factcheck" / "dokazy"


def normalizuvaty(t: str) -> str:
    """Зняти переноси й повторні пробіли.

    Обов'язково: `pdftotext` розриває речення довільно, а в PDF
    трапляються дивні пробіли (`3 /4 wire` у datasheet SSD1306). Без
    цього кроку правильні цитати дають хибну тривогу — на цьому
    спіткнулися тричі за день.
    """
    t = t.replace("­", "").replace("‑", "-")
    return re.sub(r"\s+", " ", t).strip()



def znayty_ryadok(ryadok: str, tekst: str) -> bool:
    """Чи є рядок цитати в документі — з поправкою на таблиці.

    Спершу звичайний підрядок. Якщо не збігся — рядок може бути **читанням
    таблиці**, а не суцільним фрагментом: `pdftotext` розкладає стовпці так,
    що назва параметра, умова й значення опиняються на різних рядках.

    Приклад із datasheet DS18B20:

        tERR                                    °C      3
      Error        -55°C to +125°C              ±2

    Рядка «Thermometer Error tERR -55°C to +125°C ±2 °C» у документі немає
    й не буде, хоч цитата точна. Тому для таких випадків перевіряємо, що
    **всі змістовні лексеми** трапляються у вікні документа, а не поспіль.

    Це свідоме послаблення: воно ловить вигадану цитату (лексем не буде
    взагалі), але не ловить перестановку слів у межах таблиці. Для
    табличних даних перестановка не міняє змісту.
    """
    if ryadok in tekst:
        return True
    leksemy = [x for x in re.findall(r"[\w.°±×/+-]{2,}", ryadok) if not x.isdigit() or len(x) > 1]
    if len(leksemy) < 3:
        return False
    # усі лексеми мають бути в документі
    if any(l not in tekst for l in leksemy):
        return False
    # і лежати компактно: перше й останнє входження в межах вікна
    poz = []
    for l in leksemy:
        i = tekst.find(l)
        if i < 0:
            return False
        poz.append(i)
    return (max(poz) - min(poz)) < 4000


def rozvyazne(z: dict) -> bool:
    """Чи є в полі `dzherelo` щось, що взагалі може бути документом.

    URL, шлях у репозиторії, назва файлу, назва стандарту з номером —
    так. «Властивості логіки CMOS», «фундаментальне правило електроніки» —
    ні: це міркування в полі джерела, тобто клас A без джерела.
    """
    d = str(z.get("source", ""))
    if re.search(r"https?://|\.pdf|\.h\b|\.c\b|\.rst\b|components/|datasheet|Datasheet|IEC \d|UM\d|SCLS|Table \d", d):
        return True
    return False

def tekst_dokumenta(shlyah: pathlib.Path) -> str:
    kesh_txt = shlyah.with_suffix(".txt")
    if not kesh_txt.exists():
        if shlyah.suffix.lower() == ".pdf":
            subprocess.run(["pdftotext", "-layout", str(shlyah), str(kesh_txt)],
                           check=False, capture_output=True)
        else:
            kesh_txt.write_text(shlyah.read_text(encoding="utf-8", errors="replace"),
                                encoding="utf-8")
    if not kesh_txt.exists():
        return ""
    return normalizuvaty(kesh_txt.read_text(encoding="utf-8", errors="replace"))


def znayty_dokument(z: dict) -> pathlib.Path | None:
    """Документ шукається за іменем файлу з поля `sposib`, потім за назвою."""
    sposib = str(z.get("method", ""))
    for m in re.finditer(r"`([\w.\-]+)`", sposib):
        p = KESH / m.group(1)
        if p.exists():
            return p
        for suf in (".pdf", ".txt", ".h", ".c"):
            if (KESH / (m.group(1) + suf)).exists():
                return KESH / (m.group(1) + suf)
    return None


def main() -> int:
    import yaml
    detal = "-v" in sys.argv
    vsogo = pereveryly = zbih = bez_dok = ne_znayshly = ne_rozvyazne = 0
    bidy: list[str] = []

    for f in sorted(DOKAZY.glob("*.yaml")):
        for z in (yaml.safe_load(f.read_text(encoding="utf-8")) or []):
            if str(z.get("status", "")) != "verbatim":
                continue
            vsogo += 1
            cyt = z.get("quote")
            if not cyt:
                bidy.append(f"{f.name}: «{z.get('title','?')[:44]}» — клас verbatim без цитати")
                continue
            dok = znayty_dokument(z)
            if dok is None:
                # Найважливіше рішення в цьому скрипті, і воно з практики.
                # «Джерела немає в кеші» — не пропуск, а РОЗБІЖНІСТЬ. Саме в
                # цьому мовчазному кошику ховалися записи класу A, у полі
                # `dzherelo` яких стояв не документ, а міркування:
                # «Властивості логіки CMOS», «Типовий дизайн модульних плат».
                # Доки скрипт лише мовчки їх пропускав, вони виглядали як
                # чесні докази, для яких просто не завантажили файл.
                bez_dok += 1
                if rozvyazne(z):
                    if detal:
                        print(f"  ?  {z['title'][:52]} — джерело назване, файла нема")
                else:
                    ne_rozvyazne += 1
                    print(f"  ✗✗ {z['title'][:56]}")
                    print(f"       джерело не є документом: {str(z.get('source',''))[:74]}")
                continue
            tekst = tekst_dokumenta(dok)
            if not tekst:
                bidy.append(f"{f.name}: {dok.name} не витягається в текст")
                continue
            pereveryly += 1
            # Кожен непорожній рядок цитати шукається окремо: витяг
            # часто склеєний із кількох місць документа (таблиця + примітка).
            ryadky = [normalizuvaty(r) for r in str(cyt).splitlines()]
            ryadky = [r for r in ryadky if len(r) > 12]
            promakh = [r for r in ryadky if not znayty_ryadok(r, tekst)]
            if not promakh:
                zbih += 1
                if detal:
                    print(f"  ok {z['title'][:52]}  ({dok.name})")
            else:
                ne_znayshly += 1
                print(f"  ✗  {z['title'][:56]}")
                print(f"       документ: {dok.name}")
                for r in promakh[:2]:
                    print(f"       не знайдено: {r[:88]}")

    print(f"\nшар 3: доказів класу A {vsogo}; перевірено {pereveryly}; "
          f"збіглося {zbih}; не знайдено {ne_znayshly}; без документа {bez_dok}"
          f"; ДЖЕРЕЛО НЕ ДОКУМЕНТ {ne_rozvyazne}")
    for b in bidy:
        print(f"  ⚠ {b}")
    return 1 if (ne_znayshly or bidy or ne_rozvyazne) else 0


if __name__ == "__main__":
    sys.exit(main())
