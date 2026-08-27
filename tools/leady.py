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

    tools/leady.py <каталог> [<каталог>…]   зібрати factcheck/NARYAD-leady.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
CIL = ROOT / "factcheck" / "NARYAD-leady.md"
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

**Генерується** `tools/leady.py`. Це **не** перевірка присуду — присуд
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


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
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
    print(f"leady: слідів {len(ideyi)}, придатних {len(prydatni)}, "
          f"пакетів {(len(prydatni) + NA_PAKET - 1) // NA_PAKET} "
          f"→ {CIL.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
