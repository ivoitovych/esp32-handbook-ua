#!/usr/bin/env python3
"""Сліди: перетворити `ideya` на наряд по тих, що досяжні звідси.

## Навіщо

Штурм і міра класу `E` дають три відповіді, і середня — `ideya`:
«джерела не дістав, але можу назвати документ, де воно було б».

Це найдешевша половина роботи й найлегша для втрати. `ideya` не є
доказом і в реєстр не входить, тож без окремого наряду вона лежить у
звіті доти, доки про неї не забудуть. А саме вона перетворює
«неперевірне» на «ще не перевірене» — стан, у якого є адресат.

## Чому не всі сліди варті наряду

Політика мережі пускає лише `raw.githubusercontent.com`. Сліди, що
вказують на `espressif.com`, `bluetooth.com`, паспорти виробників чи
платні стандарти, звідси **не відпрацьовуються** — і посилати по них
помічника означає вигадати йому роботу, яку можна виконати лише
неправдою.

Гірше: М2 показали, що `espressif.com` на такі адреси віддає
**HTML-заглушку 15 495 байтів із кодом 200**. Помічник, якого туди
послали, отримає «успішну» відповідь без документа — і найімовірніший
наслідок відомий.

Тому наряд бере лише ті сліди, у яких названо репозиторій, досяжний
звідси. Решта лишається в звіті як борг із чесною причиною.

    tools/leads.py <каталог> [<каталог>…]   зібрати factcheck/BRIEF-LEADS.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
CIL = ROOT / "factcheck" / "BRIEF-LEADS.md"
NA_PAKET = 6

# Що досяжне з цієї мережі. Перелік навмисно з назв репозиторіїв, а не
# доменів: слід пише людина вільним текстом, і «ESP-IDF документація»
# трапляється частіше за адресу.
DOSYAZHNE = re.compile(
    r"esp-idf|espressif/|github|linux|kernel|arduino|esphome|micropython|"
    r"adafruit|radiolib|u8g2|lvgl|pubsubclient|tft_espi|freertos", re.I)

# Що **не** досяжне, навіть якщо поруч названо щось досяжне. Перевіряється
# першим: слід «Espressif Hardware Design Guidelines або документація
# ESP-IDF» містить обидва, і піти по ньому треба саме в ESP-IDF.
NEDOSYAZHNE = re.compile(
    r"hardware design guidelines|espressif\.com|bluetooth core|"
    r"технічний паспорт|datasheet виробник|платн|iec |iso |um10204", re.I)

ZAHOLOVOK = """# Наряд: сліди класу `E`, які можна відпрацювати звідси

**Генерується** `tools/leads.py`. Це **не** перевірка присуду — присуд
уже випробуваний. Це відпрацювання того, що штурм і міра лишили як
`ideya`: «джерела не дістав, але знаю, де воно».

Кожен рядок нижче — одиниця книги плюс здогад попереднього помічника
про те, у якому документі шукати. **Здогад ніхто не перевіряв**, і
серед них уже траплялися шляхи, яких не існує. Не знайшов за названою
адресою — це не поразка й не привід шукати «щось схоже».

## Три відповіді

| Вердикт | Коли |
|---|---|
| `znayshov` | знайшов: адреса + **дослівна** цитата з документа |
| `ne_znayshov` | документ є, місця в ньому немає — напиши, що дивився |
| `nedosyazhne` | документ звідси не дістається (403, 404, заглушка) |

**`ne_znayshov` — повноцінна відповідь.** Здогад попереднього помічника
міг бути хибним; сказати про це прямо цінніше, ніж підібрати схожий
документ. Цитата з «майже того» джерела гірша за її відсутність.

## Заборони

Ті самі п'ять, що в `factcheck/POMICHNYKY.md`, і найважливіші тут дві:

- **не переказувати** — усе в полі `cytata` звіряється підрядком;
- **знати відповідь — не підстава написати цитату.** Якщо факт відомий,
  а рядка в документі не видно, це `ne_znayshov`.

Досяжне звідси лише `raw.githubusercontent.com` (через `curl`). Усе
інше — 403. **Не повторюй запит, що дав 403.**

Окремо: `espressif.com` на деякі адреси віддає **HTML-заглушку
15 495 байтів із кодом 200**. Відповідь «успішна», документа немає. Якщо
завантажене не схоже на документ — це `nedosyazhne`.

## Формат

```yaml
- odynycya: T-42-023
  verdykt: znayshov
  dzherelo: https://raw.githubusercontent.com/espressif/esp-idf/master/...
  cytata: |
    дослівний рядок із документа
  komentar: що саме він підтверджує
```

"""


ZVIT = ROOT / "factcheck" / "TRACES.md"
KANDYDATY = ROOT / "factcheck" / "leady-kandydaty.yaml"

PIDPYSY_V = {
    "znayshov": "Джерело знайдено",
    "ne_znayshov": "Здогад не підтвердився",
    "nedosyazhne": "Документ звідси недосяжний",
}


def zvesty(katalogy: list[str]) -> int:
    """Звести відпрацьовані сліди, пропустивши `znayshov` через шар 3."""
    import vyvantazh
    import yaml

    zap = []
    for k in katalogy:
        chastyna, _, _ = vyvantazh.chytaty(Path(k))
        zap += chastyna

    kand = [{"title": str(z.get("odynycya", "?")),
             "source": str(z.get("source", "")).strip(),
             "quote": str(z.get("quote", "")),
             "zvidky": z.get("_fayl", "?")}
            for z in zap if str(z.get("verdykt")) == "znayshov"]
    KANDYDATY.write_text(
        "# Кандидати з відпрацьованих слідів. **Не реєстр.**\n"
        "# Клас присвоює супровідник, і лише після шару 3.\n"
        + yaml.safe_dump(kand, allow_unicode=True, sort_keys=False),
        encoding="utf-8")

    stany: dict[str, str] = {}
    if kand:
        try:
            import citaty
            naslidky, _ = citaty.perevirka(True, [KANDYDATY])
            stany = {str(n.get("nazva")): str(n.get("stan"))
                     for n in naslidky}
        except ImportError:
            pass
    vystoyalo = [k for k in kand if stany.get(k["title"]) == "ok"]

    c: dict[str, int] = {}
    for z in zap:
        v = str(z.get("verdykt", "?"))
        c[v] = c.get(v, 0) + 1

    r = [f"""# Відпрацьовані сліди класу `E`

**Генерується** `tools/leads.py --zvit`. Наряд —
`factcheck/BRIEF-LEADS.md`.

Слід (`ideya`) — це здогад попереднього помічника про те, де шукати.
Тут — що з нього вийшло, коли по ньому справді пішли.

## Результат

Відповідей: **{len(zap)}**.

| Вердикт | Скільки |
|---|---|"""]
    for k in ("znayshov", "ne_znayshov", "nedosyazhne"):
        r.append(f"| {PIDPYSY_V[k]} | {c.get(k, 0)} |")
    r.append("")
    r.append(f"\nІз **{len(kand)}** заявлених `znayshov` третій шар "
             f"витримали **{len(vystoyalo)}**. Решта — не докази: "
             f"цитати за названою адресою немає.\n")
    r.append("`ne_znayshov` тут — **не** провал помічника, а спростування "
             "здогаду: документ прочитано, місця в ньому немає. Здогад "
             "ніхто не перевіряв, коли записував, тож частина їх хибна "
             "за побудовою.\n")

    if vystoyalo:
        r.append("\n## Витримали третій шар — кандидати в реєстр\n")
        r.append("Дослівність доведено машиною. **Чи підпирає цитата саме "
                 "це твердження — вирішує супровідник** (шар 2), і доти "
                 "жоден із них не є доказом.\n")
        r.append("| Одиниця | Джерело |")
        r.append("|---|---|")
        for k in vystoyalo:
            dz = k["source"]
            r.append(f"| `{k['nazva']}` | [`{dz.rsplit('/', 1)[-1]}`]({dz}) |")
        r.append("")

    ne = [z for z in zap if str(z.get("verdykt")) == "ne_znayshov"]
    if ne:
        r.append("\n## Здогади, що не підтвердилися\n")
        r.append("| Одиниця | Що дивилися |")
        r.append("|---|---|")
        for z in ne:
            r.append(f"| `{z.get('odynycya', '?')}` | "
                     f"{str(z.get('komentar', '')).strip()[:130]} |")
        r.append("")

    ZVIT.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"leads: відповідей {len(zap)}, заявлено {len(kand)}, "
          f"витримали шар 3 {len(vystoyalo)} → {ZVIT.relative_to(ROOT)}")
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    if "--zvit" in sys.argv:
        i = sys.argv.index("--zvit")
        return zvesty(sys.argv[i + 1:])
    import vyvantazh

    # Кілька каталогів: сліди дає і штурм, і міра, і кожна наступна
    # хвиля. Збирати їх поодинці означає щоразу губити попередні.
    zap = []
    for katalog in sys.argv[1:]:
        if katalog.startswith("-"):
            continue
        chastyna, _, _ = vyvantazh.chytaty(Path(katalog))
        zap += chastyna
    ideyi = [z for z in zap if str(z.get("verdykt")) == "ideya"]
    prydatni = [z for z in ideyi
                if (p := str(z.get("propozyciya", "")))
                and DOSYAZHNE.search(p) and not NEDOSYAZHNE.search(p)]

    r = [ZAHOLOVOK.rstrip("\n"), ""]
    r.append(f"Слідів усього **{len(ideyi)}**, з них відпрацьовуються "
             f"звідси **{len(prydatni)}**. Решта — борг із чесною "
             f"причиною: названий документ за політикою мережі "
             f"недосяжний.\n")
    for i, z in enumerate(prydatni):
        if i % NA_PAKET == 0:
            r.append(f"\n## Пакет {i // NA_PAKET + 1}\n")
        r.append(f"**`{z.get('odynycya', '?')}`**\n")
        r.append(f"- де шукати (здогад, не перевірений): "
                 f"{str(z.get('propozyciya', '')).strip()}\n")
    CIL.write_text("\n".join(r) + "\n", encoding="utf-8")
    print(f"leads: слідів {len(ideyi)}, придатних {len(prydatni)}, "
          f"пакетів {(len(prydatni) + NA_PAKET - 1) // NA_PAKET} "
          f"→ {CIL.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
