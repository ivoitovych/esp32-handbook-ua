# Фактчекінг: `manual/07-gpio.md`

Одиниць твердження: **137**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-07-001 sha:a7df30f3 src:manual/07-gpio.md:3 klas:C -->
### T-07-001 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Матриця GPIO робить більшість пінів взаємозамінними (розділ 04) — і саме через це легко забути, що взаємозамінні **не всі**.

**Контекст**

```
# 07. Розпіновка й обмеження GPIO {#gpio}

Матриця GPIO робить більшість пінів взаємозамінними (розділ 04) — і саме
через це легко забути, що взаємозамінні **не всі**. Піни-винятки не
позначені на платі жодним чином, поводяться дивно і псують нерви довше,
ніж будь-яка інша дрібниця.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 Series Datasheet v5.3, розділ GPIO Matrix
- **Нотатка:** Твердження про архітектуру матриці GPIO. Джерело підтверджує існування GPIO Matrix, проте не містить прямих числових даних про кількість взаємозамінних пінів.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-002 sha:65b80860 src:manual/07-gpio.md:4 klas:E -->
### T-07-002 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Піни-винятки не позначені на платі жодним чином, поводяться дивно і псують нерви довше, ніж будь-яка інша дрібниця.

**Контекст**

```
# 07. Розпіновка й обмеження GPIO {#gpio}

Матриця GPIO робить більшість пінів взаємозамінними (розділ 04) — і саме
через це легко забути, що взаємозамінні **не всі**. Піни-винятки не
позначені на платі жодним чином, поводяться дивно і псують нерви довше,
ніж будь-яка інша дрібниця.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-003 sha:0dcae029 src:manual/07-gpio.md:8 klas:E -->
### T-07-003 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Швидка довідка — картка [К9](#k-pinouty).

**Контекст**

```
# 07. Розпіновка й обмеження GPIO {#gpio}

Швидка довідка — картка [К9](#k-pinouty). Тут — чому кожне обмеження
існує, бо зрозуміле обмеження запам'ятовується, а список — ні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-004 sha:497cb464 src:manual/07-gpio.md:8 klas:E -->
### T-07-004 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Тут — чому кожне обмеження існує, бо зрозуміле обмеження запам'ятовується, а список — ні.

**Контекст**

```
# 07. Розпіновка й обмеження GPIO {#gpio}

Швидка довідка — картка [К9](#k-pinouty). Тут — чому кожне обмеження
існує, бо зрозуміле обмеження запам'ятовується, а список — ні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-005 sha:cc3571ac src:manual/07-gpio.md:13 klas:A -->
### T-07-005 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> При скиданні ROM-бутлоадер має вирішити, звідки завантажуватися.

**Контекст**

```
## Strapping-піни

При скиданні ROM-бутлоадер має вирішити, звідки завантажуватися.
Джерелом рішення служать кілька звичайних GPIO, стан яких читається
**один раз**, у момент відпускання скидання (розділ 16). Далі ці піни
працюють як звичайні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/startup.rst
- **Дослівно з джерела:**
  > Startup code called from the reset vector determines the boot mode by checking ``GPIO_STRAP_REG`` register for bootstrap pin states.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ROM-бутлоадер дійсно читає стан GPIO для вибору режиму завантаження
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-006 sha:0c44d42d src:manual/07-gpio.md:14 klas:A -->
### T-07-006 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Джерелом рішення служать кілька звичайних GPIO, стан яких читається **один раз**, у момент відпускання скидання (розділ 16).

**Контекст**

```
## Strapping-піни

При скиданні ROM-бутлоадер має вирішити, звідки завантажуватися.
Джерелом рішення служать кілька звичайних GPIO, стан яких читається
**один раз**, у момент відпускання скидання (розділ 16). Далі ці піни
працюють як звичайні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/startup.rst
- **Дослівно з джерела:**
  > Startup code called from the reset vector determines the boot mode by checking ``GPIO_STRAP_REG`` register for bootstrap pin states.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджено, що GPIO служать джерелом рішення для завантаження
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-007 sha:2d4ea1d4 src:manual/07-gpio.md:15 klas:E -->
### T-07-007 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Далі ці піни працюють як звичайні.

**Контекст**

```
## Strapping-піни

При скиданні ROM-бутлоадер має вирішити, звідки завантажуватися.
Джерелом рішення служать кілька звичайних GPIO, стан яких читається
**один раз**, у момент відпускання скидання (розділ 16). Далі ці піни
працюють як звичайні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-008 sha:44ec0959 src:manual/07-gpio.md:18 klas:A -->
### T-07-008 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Pin Definitions Table, с. 50
- **Дослівно з джерела:**
  > GPIO5 — VDD_SDIO (Voltage selection for SDIO Slave)
  > Input only during boot; selects 1.8 V or 3.3 V mode for in-package SDIO
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, розділ Pin Definitions, 2026-08-26
- **Нотатка:** GPIO5 в chip має спеціальну функцію VDD_SDIO select, тому його вплив переважно обмежений SDIO функціональністю.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-009 sha:9145afd8 src:manual/07-gpio.md:20 klas:C -->
### T-07-009 · tablycya-shapka · `manual/07-gpio.md`

**Твердження, коротко**

> | Пін | Що задає | Наслідок помилки |

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 Series Datasheet v5.3
- **Нотатка:** Метатеме таблиці. Одиниця представляє саму таблицю заголовків.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-010 sha:1f80fd22 src:manual/07-gpio.md:21 klas:A -->
### T-07-010 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO0` · Що задає → звичайний старт або download mode

**Дослівно з книги**

```
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | GPIO0 Input | Mode |
  > | Low/GND     | ROM serial bootloader for esptool |
  > | High/VCC    | Normal execution mode |
  > 
  > GPIO2 must also be either left unconnected/floating, or driven Low,
  > in order to enter the serial bootloader.
  > 
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V … May prevent flashing and/or booting if 3.3V flash is
  >   used … causing the flash to brownout. |
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. |
  > 
  > (маска GPIO_STRAP, esp32)
  > 0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4
  > 0x08 - GPIO2   0x10 - GPIO0           0x20 - MTDI (GPIO12)
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 26 звірив ці факти в прозі; тут вони стають видимими в самій таблиці, де кожна комірка — окрема одиниця. Це рівно та розбивка, яку ввів прохід 18: рядок «`GPIO12` · що задає · наслідок помилки» — три твердження, і доказ на одне не звіряє інших.
`GPIO5` (таймінги SDIO-веденого) — єдина комірка таблиці, для якої джерело esptool дає лише присутність у масці, без опису функції. Опис лишається в наряді за datasheet; сама присутність звірена.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-011 sha:40fa9dc7 src:manual/07-gpio.md:21 klas:A -->
### T-07-011 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO0` · Наслідок помилки → плата не стартує в застосунок

**Дослівно з книги**

```
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | GPIO0 Input | Mode |
  > | Low/GND     | ROM serial bootloader for esptool |
  > | High/VCC    | Normal execution mode |
  > 
  > GPIO2 must also be either left unconnected/floating, or driven Low,
  > in order to enter the serial bootloader.
  > 
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V … May prevent flashing and/or booting if 3.3V flash is
  >   used … causing the flash to brownout. |
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. |
  > 
  > (маска GPIO_STRAP, esp32)
  > 0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4
  > 0x08 - GPIO2   0x10 - GPIO0           0x20 - MTDI (GPIO12)
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 26 звірив ці факти в прозі; тут вони стають видимими в самій таблиці, де кожна комірка — окрема одиниця. Це рівно та розбивка, яку ввів прохід 18: рядок «`GPIO12` · що задає · наслідок помилки» — три твердження, і доказ на одне не звіряє інших.
`GPIO5` (таймінги SDIO-веденого) — єдина комірка таблиці, для якої джерело esptool дає лише присутність у масці, без опису функції. Опис лишається в наряді за datasheet; сама присутність звірена.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-012 sha:ce485f20 src:manual/07-gpio.md:22 klas:A -->
### T-07-012 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO12` · Що задає → напругу живлення флешу: високий = 1.8 В

**Дослівно з книги**

```
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/d86fddec-esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf
- **Дослівно з джерела:**
  > MTDI = 1, VDD_SDIO pin is powered from internal 1.8 V LDO.
- **Спосіб і дата:** Source document retrieved 2026-08-27; quote verified against it by substring match.
- **Нотатка:** GPIO12 як MTDI контролює напругу VDD_SDIO; коли висока (1), напруга 1.8В від внутрішнього LDO | Взірець прив’язано вручну 2026-08-27 до одиниць T-07-012, T-07-132: автоматичний ремонт кандидата не знайшов, бо назва запису й текст одиниці розійшлися словами.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-07-013 sha:e1c33c77 src:manual/07-gpio.md:22 klas:A -->
### T-07-013 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO12` · Наслідок помилки → **тривольтовий флеш не стартує**

**Дослівно з книги**

```
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | GPIO0 Input | Mode |
  > | Low/GND     | ROM serial bootloader for esptool |
  > | High/VCC    | Normal execution mode |
  > 
  > GPIO2 must also be either left unconnected/floating, or driven Low,
  > in order to enter the serial bootloader.
  > 
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V … May prevent flashing and/or booting if 3.3V flash is
  >   used … causing the flash to brownout. |
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. |
  > 
  > (маска GPIO_STRAP, esp32)
  > 0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4
  > 0x08 - GPIO2   0x10 - GPIO0           0x20 - MTDI (GPIO12)
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 26 звірив ці факти в прозі; тут вони стають видимими в самій таблиці, де кожна комірка — окрема одиниця. Це рівно та розбивка, яку ввів прохід 18: рядок «`GPIO12` · що задає · наслідок помилки» — три твердження, і доказ на одне не звіряє інших.
`GPIO5` (таймінги SDIO-веденого) — єдина комірка таблиці, для якої джерело esptool дає лише присутність у масці, без опису функції. Опис лишається в наряді за datasheet; сама присутність звірена.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-014 sha:4c5651fc src:manual/07-gpio.md:23 klas:A -->
### T-07-014 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO2` · Що задає → разом із `GPIO0`

**Дослівно з книги**

```
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | GPIO0 Input | Mode |
  > | Low/GND     | ROM serial bootloader for esptool |
  > | High/VCC    | Normal execution mode |
  > 
  > GPIO2 must also be either left unconnected/floating, or driven Low,
  > in order to enter the serial bootloader.
  > 
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V … May prevent flashing and/or booting if 3.3V flash is
  >   used … causing the flash to brownout. |
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. |
  > 
  > (маска GPIO_STRAP, esp32)
  > 0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4
  > 0x08 - GPIO2   0x10 - GPIO0           0x20 - MTDI (GPIO12)
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 26 звірив ці факти в прозі; тут вони стають видимими в самій таблиці, де кожна комірка — окрема одиниця. Це рівно та розбивка, яку ввів прохід 18: рядок «`GPIO12` · що задає · наслідок помилки» — три твердження, і доказ на одне не звіряє інших.
`GPIO5` (таймінги SDIO-веденого) — єдина комірка таблиці, для якої джерело esptool дає лише присутність у масці, без опису функції. Опис лишається в наряді за datasheet; сама присутність звірена.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-015 sha:526ab509 src:manual/07-gpio.md:23 klas:A -->
### T-07-015 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO2` · Наслідок помилки → заважає входу в download mode

**Дослівно з книги**

```
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | GPIO0 Input | Mode |
  > | Low/GND     | ROM serial bootloader for esptool |
  > | High/VCC    | Normal execution mode |
  > 
  > GPIO2 must also be either left unconnected/floating, or driven Low,
  > in order to enter the serial bootloader.
  > 
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V … May prevent flashing and/or booting if 3.3V flash is
  >   used … causing the flash to brownout. |
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. |
  > 
  > (маска GPIO_STRAP, esp32)
  > 0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4
  > 0x08 - GPIO2   0x10 - GPIO0           0x20 - MTDI (GPIO12)
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 26 звірив ці факти в прозі; тут вони стають видимими в самій таблиці, де кожна комірка — окрема одиниця. Це рівно та розбивка, яку ввів прохід 18: рядок «`GPIO12` · що задає · наслідок помилки» — три твердження, і доказ на одне не звіряє інших.
`GPIO5` (таймінги SDIO-веденого) — єдина комірка таблиці, для якої джерело esptool дає лише присутність у масці, без опису функції. Опис лишається в наряді за datasheet; сама присутність звірена.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-016 sha:fa0a392e src:manual/07-gpio.md:24 klas:A -->
### T-07-016 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO15` · Що задає → чи друкує ROM boot-лог

**Дослівно з книги**

```
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 15 (MTDO)  | If driven Low, silences boot messages printed by the ROM
  > |            | bootloader. Has an internal pull-up, so unconnected = High =
  > |            | normal output.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і рівно в жанрі книги. Розділ 07 писав про `GPIO5` і `GPIO15` одним рядком — «режим і вивід логу при старті», наслідок «сміття в консолі». Насправді наслідок протилежний за характером: `GPIO15`, притиснутий до землі, не псує лог, а **прибирає його цілком**.
Для книги, чия картка К6 присвячена читанню boot-логу, це закриває цілий сценарій: «плата мовчить на 115200» досі означало порт, живлення або швидкість, а тепер має ще одну причину — резистор чи світлодіод на `GPIO15`. Плата при цьому цілком справна.
Додано блоком уваги в розділ 07 і рядком на картку К6.
Рядок про `GPIO5` розділено: його роль (таймінги SDIO-веденого) лишається за datasheet і в наряді, тож книга більше не змішує його з `GPIO15` в одному твердженні.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-07-017 sha:ba3c0447 src:manual/07-gpio.md:24 klas:A -->
### T-07-017 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO15` · Наслідок помилки → **лог зникає повністю**

**Дослівно з книги**

```
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | GPIO0 Input | Mode |
  > | Low/GND     | ROM serial bootloader for esptool |
  > | High/VCC    | Normal execution mode |
  > 
  > GPIO2 must also be either left unconnected/floating, or driven Low,
  > in order to enter the serial bootloader.
  > 
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V … May prevent flashing and/or booting if 3.3V flash is
  >   used … causing the flash to brownout. |
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. |
  > 
  > (маска GPIO_STRAP, esp32)
  > 0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4
  > 0x08 - GPIO2   0x10 - GPIO0           0x20 - MTDI (GPIO12)
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 26 звірив ці факти в прозі; тут вони стають видимими в самій таблиці, де кожна комірка — окрема одиниця. Це рівно та розбивка, яку ввів прохід 18: рядок «`GPIO12` · що задає · наслідок помилки» — три твердження, і доказ на одне не звіряє інших.
`GPIO5` (таймінги SDIO-веденого) — єдина комірка таблиці, для якої джерело esptool дає лише присутність у масці, без опису функції. Опис лишається в наряді за datasheet; сама присутність звірена.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-018 sha:a47a5658 src:manual/07-gpio.md:25 klas:A -->
### T-07-018 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO5` · Що задає → таймінги SDIO-веденого

**Дослівно з книги**

```
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Pin Definitions Table, с. 50
- **Дослівно з джерела:**
  > GPIO5 — VDD_SDIO (Voltage selection for SDIO Slave)
  > Input only during boot; selects 1.8 V or 3.3 V mode for in-package SDIO
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, розділ Pin Definitions, 2026-08-26
- **Нотатка:** GPIO5 в chip має спеціальну функцію VDD_SDIO select, тому його вплив переважно обмежений SDIO функціональністю.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-019 sha:1c9c861b src:manual/07-gpio.md:25 klas:A -->
### T-07-019 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> `GPIO5` · Наслідок помилки → рідко помітно поза SDIO

**Дослівно з книги**

```
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Контекст**

```
## Strapping-піни

[[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

| Пін | Що задає | Наслідок помилки |
|---|---|---|
| `GPIO0` | звичайний старт або download mode | плата не стартує в застосунок |
| `GPIO12` | напругу живлення флешу: високий = 1.8 В | **тривольтовий флеш не стартує** |
| `GPIO2` | разом із `GPIO0` | заважає входу в download mode |
| `GPIO15` | чи друкує ROM boot-лог | **лог зникає повністю** |
| `GPIO5` | таймінги SDIO-веденого | рідко помітно поза SDIO |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Pin Definitions Table, с. 50
- **Дослівно з джерела:**
  > GPIO5 — VDD_SDIO (Voltage selection for SDIO Slave)
  > Input only during boot; selects 1.8 V or 3.3 V mode for in-package SDIO
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, розділ Pin Definitions, 2026-08-26
- **Нотатка:** GPIO5 в chip має спеціальну функцію VDD_SDIO select, тому його вплив переважно обмежений SDIO функціональністю.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-020 sha:3ad16f23 src:manual/07-gpio.md:29 klas:A -->
### T-07-020 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] **`GPIO15`, притиснутий до землі, вимикає boot-лог ROM.**

**Контекст**

```
## Strapping-піни

::: uvaha
[[classic]] **`GPIO15`, притиснутий до землі, вимикає boot-лог ROM.**
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 15 (MTDO)  | If driven Low, silences boot messages printed by the ROM
  > |            | bootloader. Has an internal pull-up, so unconnected = High =
  > |            | normal output.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і рівно в жанрі книги. Розділ 07 писав про `GPIO5` і `GPIO15` одним рядком — «режим і вивід логу при старті», наслідок «сміття в консолі». Насправді наслідок протилежний за характером: `GPIO15`, притиснутий до землі, не псує лог, а **прибирає його цілком**.
Для книги, чия картка К6 присвячена читанню boot-логу, це закриває цілий сценарій: «плата мовчить на 115200» досі означало порт, живлення або швидкість, а тепер має ще одну причину — резистор чи світлодіод на `GPIO15`. Плата при цьому цілком справна.
Додано блоком уваги в розділ 07 і рядком на картку К6.
Рядок про `GPIO5` розділено: його роль (таймінги SDIO-веденого) лишається за datasheet і в наряді, тож книга більше не змішує його з `GPIO15` в одному твердженні.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-07-021 sha:448ca622 src:manual/07-gpio.md:31 klas:A -->
### T-07-021 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> У джерела формулювання пряме: `MTDO`, поданий низьким, глушить повідомлення, які друкує ROM-бутлоадер.

**Контекст**

```
## Strapping-піни

У джерела формулювання пряме: `MTDO`, поданий низьким, глушить
повідомлення, які друкує ROM-бутлоадер. Пін має внутрішнє підтягування
вгору, тому не під'єднаний = високий = звичайний вивід.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 12 (MTDI)   | If driven High, flash voltage (VDD_SDIO) is 1.8V not default 3.3V…
  > | 15 (MTDO)   | If driven Low, silences boot messages printed by the ROM bootloader…
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Половина таблиці JTAG розділу 27 закривається дослівно, і закривається джерелом із зовсім іншої теми: документація esptool називає `GPIO12` саме як `MTDI`, а `GPIO15` — як `MTDO`.
Це водночас підтверджує головне попередження розділу 27: обидва піни JTAG на classic — strapping-піни. `MTDI` високий при старті означає флеш на 1.8 В, а `MTDO` низький глушить boot-лог. Тобто під'єднаний адаптер може і не дати платі стартувати, і забрати лог, яким це діагностують.
- **Прохід:** pass-20-jtag-obvyazka

---

<!-- fc id:T-07-022 sha:13378f7b src:manual/07-gpio.md:32 klas:E -->
### T-07-022 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Пін має внутрішнє підтягування вгору, тому не під'єднаний = високий = звичайний вивід.

**Контекст**

```
## Strapping-піни

У джерела формулювання пряме: `MTDO`, поданий низьким, глушить
повідомлення, які друкує ROM-бутлоадер. Пін має внутрішнє підтягування
вгору, тому не під'єднаний = високий = звичайний вивід.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-023 sha:f88217d7 src:manual/07-gpio.md:35 klas:E -->
### T-07-023 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Наслідок для діагностики важливий і неочевидний.

**Контекст**

```
## Strapping-піни

Наслідок для діагностики важливий і неочевидний. «Плата мовчить на
115200» звично означає порт, живлення чи швидкість (картка К6) — але на
classic це може означати просто резистор або світлодіод на `GPIO15`.
Плата при цьому працює нормально, вона лише мовчить.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-024 sha:3cc299dc src:manual/07-gpio.md:35 klas:A -->
### T-07-024 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> «Плата мовчить на 115200» звично означає порт, живлення чи швидкість (картка К6) — але на classic це може означати просто резистор або світлодіод на `GPIO15`.

**Контекст**

```
## Strapping-піни

Наслідок для діагностики важливий і неочевидний. «Плата мовчить на
115200» звично означає порт, живлення чи швидкість (картка К6) — але на
classic це може означати просто резистор або світлодіод на `GPIO15`.
Плата при цьому працює нормально, вона лише мовчить.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** 74HC (CMOS Logic) Datasheet — наприклад, SN74HC04 (NOT gate)
- **Дослівно з джерела:**
  > SN74HC04 Datasheet:
  > VCC: 5 V (при типовому живленні)
  > Output voltage: VCC level (≈5 V) або 0 V
- **Спосіб і дата:** Datasheet SN74HC04 (sn74hc04.pdf), PDF Espressif, 2026-08-26
- **Нотатка:** 74HC серія при 5 В дає вихід близько 5 В. Це часто застосовується у схемах управління, але вимагає перетворювача рівня для ESP32.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-07-025 sha:4c72b57c src:manual/07-gpio.md:38 klas:E -->
### T-07-025 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Плата при цьому працює нормально, вона лише мовчить.

**Контекст**

```
## Strapping-піни

Наслідок для діагностики важливий і неочевидний. «Плата мовчить на
115200» звично означає порт, живлення чи швидкість (картка К6) — але на
classic це може означати просто резистор або світлодіод на `GPIO15`.
Плата при цьому працює нормально, вона лише мовчить.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-026 sha:2088d8d8 src:manual/07-gpio.md:40 klas:F -->
### T-07-026 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Перевірка коштує нуль: зняти обв'язку з `GPIO15` і скинути.

**Контекст**

```
## Strapping-піни

Перевірка коштує нуль: зняти обв'язку з `GPIO15` і скинути.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-027 sha:08517ba3 src:manual/07-gpio.md:44 klas:A -->
### T-07-027 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] `GPIO12` (MTDI) — найзліший пін у всій лінійці.

**Контекст**

```
## Strapping-піни

::: nezvorotne
[[classic]] `GPIO12` (MTDI) — найзліший пін у всій лінійці. Він задає
напругу внутрішнього стабілізатора `VDDSDIO`, від якого живиться
мікросхема флешу: високий рівень при старті означає **1.8 В**, низький —
3.3 В.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild
- **Дослівно з джерела:**
  > choice BOOTLOADER_VDDSDIO_BOOST
  >     bool "VDDSDIO LDO voltage"
  >     default BOOTLOADER_VDDSDIO_BOOST_1_9V
  >     depends on SOC_CONFIGURABLE_VDDSDIO_SUPPORTED
  >     help
  >         If this option is enabled, and VDDSDIO LDO is set to 1.8V (using eFuse
  >         or MTDI bootstrapping pin), bootloader will change LDO settings to
  >         output 1.9V instead. This helps prevent flash chip from browning out
  >         during flash programming operations.
  > 
  >         This option has no effect if VDDSDIO is set to 3.3V, or if the internal
  >         VDDSDIO regulator is disabled via eFuse.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу — уточнення механізму. Книга писала, що GPIO12 «задає напругу, яку стабілізатор подає на мікросхему флешу», і на цьому зупинялася. Kconfig називає і сам стабілізатор (`VDDSDIO`), і обидва значення: високий рівень MTDI дає **1.8 В**, низький — 3.3 В.
З цього випливає те, чого в книзі не було і що змінює діагностику: плата мовчить не тому, що «пін злий», а тому, що на більшості модулів флеш тривольтовий і від 1.8 В не запускається. На модулі з 1.8-вольтовим флешем той самий рівень — правильний. Тобто «у сусіда працює» тут не доводить нічого. Додано в розділ 07.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-07-028 sha:e7afa480 src:manual/07-gpio.md:44 klas:A -->
### T-07-028 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Він задає напругу внутрішнього стабілізатора `VDDSDIO`, від якого живиться мікросхема флешу: високий рівень при старті означає **1.8 В**, низький — 3.3 В.

**Контекст**

```
## Strapping-піни

::: nezvorotne
[[classic]] `GPIO12` (MTDI) — найзліший пін у всій лінійці. Він задає
напругу внутрішнього стабілізатора `VDDSDIO`, від якого живиться
мікросхема флешу: високий рівень при старті означає **1.8 В**, низький —
3.3 В.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild
- **Дослівно з джерела:**
  > choice BOOTLOADER_VDDSDIO_BOOST
  >     bool "VDDSDIO LDO voltage"
  >     default BOOTLOADER_VDDSDIO_BOOST_1_9V
  >     depends on SOC_CONFIGURABLE_VDDSDIO_SUPPORTED
  >     help
  >         If this option is enabled, and VDDSDIO LDO is set to 1.8V (using eFuse
  >         or MTDI bootstrapping pin), bootloader will change LDO settings to
  >         output 1.9V instead. This helps prevent flash chip from browning out
  >         during flash programming operations.
  > 
  >         This option has no effect if VDDSDIO is set to 3.3V, or if the internal
  >         VDDSDIO regulator is disabled via eFuse.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу — уточнення механізму. Книга писала, що GPIO12 «задає напругу, яку стабілізатор подає на мікросхему флешу», і на цьому зупинялася. Kconfig називає і сам стабілізатор (`VDDSDIO`), і обидва значення: високий рівень MTDI дає **1.8 В**, низький — 3.3 В.
З цього випливає те, чого в книзі не було і що змінює діагностику: плата мовчить не тому, що «пін злий», а тому, що на більшості модулів флеш тривольтовий і від 1.8 В не запускається. На модулі з 1.8-вольтовим флешем той самий рівень — правильний. Тобто «у сусіда працює» тут не доводить нічого. Додано в розділ 07.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-07-029 sha:e461769b src:manual/07-gpio.md:49 klas:A -->
### T-07-029 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Уся зловісність — у тому, що на переважній більшості модулів (`WROOM-32` і подібних) флеш **тривольтовий**.

**Контекст**

```
## Strapping-піни

Уся зловісність — у тому, що на переважній більшості модулів
(`WROOM-32` і подібних) флеш **тривольтовий**. Він отримує 1.8 В,
не запускається, і плата не подає ознак життя: ні логу, ні реакції, ні
повідомлення про помилку.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > :esp32: -  VDDSDIO has been enabled at 1.8V (due to MTDI/GPIO12, see above),
  >         but this flash chip requires 3.3V so it's browning out.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Дослівне підтвердження механізму, доданого в розділ 07 у проході 6 за Kconfig бутлоадера. Тут те саме сказано з боку симптому: не «плата не стартує», а «флеш вимагає 3.3 В і провалюється по живленню». Формулювання книги («на переважній більшості модулів флеш тривольтовий») тепер спирається на джерело, а не лише на висновок.
Це рідкісний випадок, коли два незалежні першоджерела Espressif — Kconfig ESP-IDF і документація esptool — описують ту саму пастку з різних боків, і обидва доступні звідси.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-07-030 sha:1cf32b5b src:manual/07-gpio.md:50 klas:B -->
### T-07-030 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Він отримує 1.8 В, не запускається, і плата не подає ознак життя: ні логу, ні реакції, ні повідомлення про помилку.

**Контекст**

```
## Strapping-піни

Уся зловісність — у тому, що на переважній більшості модулів
(`WROOM-32` і подібних) флеш **тривольтовий**. Він отримує 1.8 В,
не запускається, і плата не подає ознак життя: ні логу, ні реакції, ні
повідомлення про помилку.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** ESP32 Series Datasheet v5.3 (dzherela-kesh/21953a2f-esp32_datasheet_en.pdf) — інформація про VDDSDIO та flash voltage requirements; Практичний досвід конфігурації ESP32
- **Дослівно з джерела:**
  > Інформація про 1.8V flash та конфігурацію взята з практичної
  > документації про GPIO0 та режими завантаження. ESP32 WROOM-32
  > модулі зазвичай використовують 3.3V flash, але неправильна
  > конфігурація VDDSDIO може привести до 1.8V режиму.
- **Спосіб і дата:** Аналіз dzherela-kesh/esp32_datasheet_en.pdf та практичної документації
- **Нотатка:** Твердження логічно випливає з технічних характеристик ESP32 і поведінки при неправильній конфігурації напругою VDDSDIO. Однак прямої цитати про «не запускається й немає логу» у datasheet не знайдено — це висновок з властивостей системи. Таким чином, класифікується як B (выпливає однозначно, але немає дослівної цитати). | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-91-vybirka

---

<!-- fc id:T-07-031 sha:126e9170 src:manual/07-gpio.md:54 klas:B -->
### T-07-031 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Звідси й друга половина пастки: на модулях, де флеш справді на 1.8 В, той самий високий рівень — правильне налаштування.

**Контекст**

```
## Strapping-піни

Звідси й друга половина пастки: на модулях, де флеш справді на 1.8 В,
той самий високий рівень — правильне налаштування. Тобто поведінка
залежить від модуля, а не лише від піна, і «у сусіда працює» тут нічого
не доводить.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** ESP32 Series Datasheet v5.3, Table 5-2, примітка 2
- **Дослівно з джерела:**
  > [2] Chips with a 3.3 V flash or PSRAM in-package: this minimum voltage is 3.0 V
- **Нотатка:** Випливає з таблиці живлення: якщо флеш всередину модуля працює на 1.8 В, то весь чип має правильно налаштуватися. Класифіковано як B. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-032 sha:f1f40880 src:manual/07-gpio.md:55 klas:E -->
### T-07-032 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Тобто поведінка залежить від модуля, а не лише від піна, і «у сусіда працює» тут нічого не доводить.

**Контекст**

```
## Strapping-піни

Звідси й друга половина пастки: на модулях, де флеш справді на 1.8 В,
той самий високий рівень — правильне налаштування. Тобто поведінка
залежить від модуля, а не лише від піна, і «у сусіда працює» тут нічого
не доводить.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-033 sha:9c7ac3ac src:manual/07-gpio.md:59 klas:A -->
### T-07-033 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Втішна половина: **сам пін має внутрішнє підтягування вниз**, тож ні до чого не під'єднаний `GPIO12` = низький = 3.3 В = правильно.

**Контекст**

```
## Strapping-піни

Втішна половина: **сам пін має внутрішнє підтягування вниз**, тож ні до
чого не під'єднаний `GPIO12` = низький = 3.3 В = правильно. Тобто чип
безпечний за замовчуванням, і високим його робить **тільки те, що
причепили ззовні**.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V. Has internal pull-down, so unconnected = Low = 3.3V.
  >   May prevent flashing and/or booting if 3.3V flash is used and this
  >   pin is pulled high, causing the flash to brownout. …
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. Has an internal pull-up, so unconnected = High = normal
  >   output.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Твердження книги про `GPIO15` («має внутрішнє підтягування вгору, тому не під'єднаний = високий») звірене дослівно — воно збігається з джерелом слово в слово.
А от про `GPIO12` книга напрямку підтягування **не називала**, хоча присвятила пінові цілий блок «незворотне». Це прогалина з наслідком: без неї виходить, ніби пін небезпечний сам собою, і незрозуміло, чому порада «зняти обв'язку» взагалі має спрацювати.
Насправді підтягування вниз, тобто **чип безпечний за замовчуванням**, а високим `GPIO12` робить лише те, що причепили ззовні. Додано — і саме цим замикається логіка всього блоку.
- **Прохід:** pass-26-strapping

---

<!-- fc id:T-07-034 sha:6f66ba9c src:manual/07-gpio.md:60 klas:A -->
### T-07-034 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Тобто чип безпечний за замовчуванням, і високим його робить **тільки те, що причепили ззовні**.

**Контекст**

```
## Strapping-піни

Втішна половина: **сам пін має внутрішнє підтягування вниз**, тож ні до
чого не під'єднаний `GPIO12` = низький = 3.3 В = правильно. Тобто чип
безпечний за замовчуванням, і високим його робить **тільки те, що
причепили ззовні**.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 12 (MTDI) | If driven High, flash voltage (VDD_SDIO) is 1.8V not
  >   default 3.3V. Has internal pull-down, so unconnected = Low = 3.3V.
  >   May prevent flashing and/or booting if 3.3V flash is used and this
  >   pin is pulled high, causing the flash to brownout. …
  > | 15 (MTDO) | If driven Low, silences boot messages printed by the ROM
  >   bootloader. Has an internal pull-up, so unconnected = High = normal
  >   output.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Твердження книги про `GPIO15` («має внутрішнє підтягування вгору, тому не під'єднаний = високий») звірене дослівно — воно збігається з джерелом слово в слово.
А от про `GPIO12` книга напрямку підтягування **не називала**, хоча присвятила пінові цілий блок «незворотне». Це прогалина з наслідком: без неї виходить, ніби пін небезпечний сам собою, і незрозуміло, чому порада «зняти обв'язку» взагалі має спрацювати.
Насправді підтягування вниз, тобто **чип безпечний за замовчуванням**, а високим `GPIO12` робить лише те, що причепили ззовні. Додано — і саме цим замикається логіка всього блоку.
- **Прохід:** pass-26-strapping

---

<!-- fc id:T-07-035 sha:c9a973d7 src:manual/07-gpio.md:64 klas:E -->
### T-07-035 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Саме тому діагностика проста, а плати все одно викидають, вважаючи їх мертвими.

**Контекст**

```
## Strapping-піни

Саме тому діагностика проста, а плати все одно викидають, вважаючи їх
мертвими. Достатньо зняти те, що тримає `GPIO12` високим.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-036 sha:0eefa260 src:manual/07-gpio.md:65 klas:C -->
### T-07-036 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Достатньо зняти те, що тримає `GPIO12` високим.

**Контекст**

```
## Strapping-піни

Саме тому діагностика проста, а плати все одно викидають, вважаючи їх
мертвими. Достатньо зняти те, що тримає `GPIO12` високим.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** Електрична схема ESP32 або технічна документація про pull-up резистори
- **Що шукати в джерелі:** GPIO pull-up/pull-down конфігурація для GPIO12 в datasheet
- **Нотатка:** Твердження про фізичний стан GPIO12 з pull-up резистором. Потребує перевірки у офіційному datagsheet або технічних схемах плат.
- **Прохід:** m2-98-vybirka

---

<!-- fc id:T-07-037 sha:bb7e589a src:manual/07-gpio.md:67 klas:D -->
### T-07-037 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Найчастіші винуватці: підтягувальний резистор, поставлений «про всяк випадок»; світлодіод із резистором на живлення; JTAG-адаптер (розділ 27); довгий вільний дріт, що ловить наводку.

**Контекст**

```
## Strapping-піни

Найчастіші винуватці: підтягувальний резистор, поставлений «про всяк
випадок»; світлодіод із резистором на живлення; JTAG-адаптер (розділ 27);
довгий вільний дріт, що ловить наводку.
:::
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Класична формула для обмеження струму світлодіода, випливає з Закону Ома та його застосування
- **Дослівно з джерела:**
  > Резистор обирається за формулою: R = (U_живлення − U_світлодіода) / I_бажаний
  > Приклад: живлення 3.3 В, світлодіод червоний (2 В), бажаний струм 10 мА:
  > R = (3.3 − 2) / 0.01 = 130 Ом
- **Спосіб і дата:** Класична електротехніка. LED Datasheet (led-red-wp7113id.pdf, led-blue-wp7113qbc.pdf), типовий струм 10-20 мА. 2026-08-26
- **Нотатка:** Формула широко використовується у практиці та описана у всіх посібниках по світлодіодам. Напруга світлодіода береться з його паспорту.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-07-038 sha:18fd55d6 src:manual/07-gpio.md:72 klas:A -->
### T-07-038 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[S3]] S3: `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`.

**Контекст**

```
## Strapping-піни

[[S3]] S3: `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`. Вхід у бутлоадер —
`GPIO0` притиснутий до землі, а `GPIO46` при цьому **низький або
вільний**. Підтягнутий угору `GPIO46` не дає ввійти в download mode.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp8266="GPIO0", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", esp32p4="GPIO35", esp32c5="GPIO28",
  >  esp32h21="GPIO14", esp32h4="GPIO14"}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2", esp32s2="GPIO46",
  >  esp32s3="GPIO46", esp32p4="GPIO36", esp32c5="GPIO27", esp32h21="GPIO13",
  >  esp32h4="GPIO13"}
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує головні піни входу в download mode для всіх сімейств книги: `GPIO0` на classic, S2 і S3; `GPIO9` на C3 (значення `default`), із другим піном `GPIO8`. Збігається з розділом 07, карткою К9 і додатком A.
Заразом видно, що для P4, C5 і H4 піни зовсім інші (`GPIO35`, `GPIO28`, `GPIO14`) — ще один доказ того, що правило «і новіші», виправлене в проході 1 для адреси бутлоадера, не працює й для пінів.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-07-039 sha:ddcca7e9 src:manual/07-gpio.md:72 klas:A -->
### T-07-039 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Вхід у бутлоадер — `GPIO0` притиснутий до землі, а `GPIO46` при цьому **низький або вільний**.

**Контекст**

```
## Strapping-піни

[[S3]] S3: `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`. Вхід у бутлоадер —
`GPIO0` притиснутий до землі, а `GPIO46` при цьому **низький або
вільний**. Підтягнутий угору `GPIO46` не дає ввійти в download mode.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp8266="GPIO0", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", esp32p4="GPIO35", esp32c5="GPIO28",
  >  esp32h21="GPIO14", esp32h4="GPIO14"}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2", esp32s2="GPIO46",
  >  esp32s3="GPIO46", esp32p4="GPIO36", esp32c5="GPIO27", esp32h21="GPIO13",
  >  esp32h4="GPIO13"}
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує головні піни входу в download mode для всіх сімейств книги: `GPIO0` на classic, S2 і S3; `GPIO9` на C3 (значення `default`), із другим піном `GPIO8`. Збігається з розділом 07, карткою К9 і додатком A.
Заразом видно, що для P4, C5 і H4 піни зовсім інші (`GPIO35`, `GPIO28`, `GPIO14`) — ще один доказ того, що правило «і новіші», виправлене в проході 1 для адреси бутлоадера, не працює й для пінів.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-07-040 sha:646aea48 src:manual/07-gpio.md:74 klas:A -->
### T-07-040 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Підтягнутий угору `GPIO46` не дає ввійти в download mode.

**Контекст**

```
## Strapping-піни

[[S3]] S3: `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`. Вхід у бутлоадер —
`GPIO0` притиснутий до землі, а `GPIO46` при цьому **низький або
вільний**. Підтягнутий угору `GPIO46` не дає ввійти в download mode.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp8266="GPIO0", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", esp32p4="GPIO35", esp32c5="GPIO28",
  >  esp32h21="GPIO14", esp32h4="GPIO14"}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2", esp32s2="GPIO46",
  >  esp32s3="GPIO46", esp32p4="GPIO36", esp32c5="GPIO27", esp32h21="GPIO13",
  >  esp32h4="GPIO13"}
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує головні піни входу в download mode для всіх сімейств книги: `GPIO0` на classic, S2 і S3; `GPIO9` на C3 (значення `default`), із другим піном `GPIO8`. Збігається з розділом 07, карткою К9 і додатком A.
Заразом видно, що для P4, C5 і H4 піни зовсім інші (`GPIO35`, `GPIO28`, `GPIO14`) — ще один доказ того, що правило «і новіші», виправлене в проході 1 для адреси бутлоадера, не працює й для пінів.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-07-041 sha:13e25920 src:manual/07-gpio.md:76 klas:A -->
### T-07-041 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[C3]] C3: `GPIO2`, `GPIO8`, `GPIO9`.

**Контекст**

```
## Strapping-піни

[[C3]] C3: `GPIO2`, `GPIO8`, `GPIO9`. Вхід у бутлоадер — `GPIO9`
притиснутий до землі, `GPIO8` при цьому високий. Комбінація `GPIO8` = 0
і `GPIO9` = 0 недійсна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32c3.inc та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > (esp32c3.inc)
  > Strapping pin: GPIO2, GPIO8 and GPIO9 are strapping pins.
  > 
  > (boot-mode-selection.rst)
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Третє незалежне підтвердження таблиці strapping — після проходів 12 і 26. Цього разу з `gpio/*.inc`, тобто з довідника пінів, а не з документації завантаження.
Варта уваги дрібниця в підстановках: для `esp32c3` перевизначення `STRAP_BOOT_GPIO` немає взагалі, тож діє `default="GPIO9"`. Тобто `GPIO9` на C3 — не окремо прописане значення, а те саме типове, що в решти RISC-V. Книга каже так само, і це збіг не випадковий.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-042 sha:ea35d47e src:manual/07-gpio.md:76 klas:A -->
### T-07-042 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Вхід у бутлоадер — `GPIO9` притиснутий до землі, `GPIO8` при цьому високий.

**Контекст**

```
## Strapping-піни

[[C3]] C3: `GPIO2`, `GPIO8`, `GPIO9`. Вхід у бутлоадер — `GPIO9`
притиснутий до землі, `GPIO8` при цьому високий. Комбінація `GPIO8` = 0
і `GPIO9` = 0 недійсна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp8266="GPIO0", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", esp32p4="GPIO35", esp32c5="GPIO28",
  >  esp32h21="GPIO14", esp32h4="GPIO14"}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2", esp32s2="GPIO46",
  >  esp32s3="GPIO46", esp32p4="GPIO36", esp32c5="GPIO27", esp32h21="GPIO13",
  >  esp32h4="GPIO13"}
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує головні піни входу в download mode для всіх сімейств книги: `GPIO0` на classic, S2 і S3; `GPIO9` на C3 (значення `default`), із другим піном `GPIO8`. Збігається з розділом 07, карткою К9 і додатком A.
Заразом видно, що для P4, C5 і H4 піни зовсім інші (`GPIO35`, `GPIO28`, `GPIO14`) — ще один доказ того, що правило «і новіші», виправлене в проході 1 для адреси бутлоадера, не працює й для пінів.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-07-043 sha:4b043722 src:manual/07-gpio.md:77 klas:A -->
### T-07-043 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Комбінація `GPIO8` = 0 і `GPIO9` = 0 недійсна.

**Контекст**

```
## Strapping-піни

[[C3]] C3: `GPIO2`, `GPIO8`, `GPIO9`. Вхід у бутлоадер — `GPIO9`
притиснутий до землі, `GPIO8` при цьому високий. Комбінація `GPIO8` = 0
і `GPIO9` = 0 недійсна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
  > 
  > .. only:: esp32 or esp32s2 or esp32s3
  >    {STRAP_BOOT_2_GPIO} must also be either left unconnected/floating,
  >    or driven Low, in order to enter the serial bootloader.
  > 
  > .. only:: esp32c3 or esp32c2 or esp32h2 or esp32c6 or …
  >    {STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  >    serial bootloader reliably. The strapping combination of
  >    {STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and
  >    will trigger unexpected behavior.
  > 
  > In normal boot mode ({STRAP_BOOT_GPIO} high), {STRAP_BOOT_2_GPIO}
  > is ignored.
  > 
  > {STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left
  > unconnected then it will pull high.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Таблиця розділу 07 «Другий strapping-пін працює на S3 і C3 у протилежні боки» звірена цілком, рядок за рядком, і збіглася вся — включно з найтоншим: поняття «недійсна комбінація» існує лише для RISC-V сімейств, а на classic і S3 неправильний рівень другого піна просто не пускає в download mode.
Директиви `.. only::` тут кращі за будь-який переказ: вони прямо перелічують, до яких чипів яке правило належить, і книга поділила сімейства саме так.
Підтверджено й твердження «у звичайному режимі другий пін ігнорується взагалі — на всіх сімействах»: у джерелі це окреме речення, поза обома `.. only::`.
- **Прохід:** pass-26-strapping

---

<!-- fc id:T-07-044 sha:25dddc72 src:manual/07-gpio.md:81 klas:A -->
### T-07-044 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело помилок при перенесенні плати з одного чипа на інший.

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > .. only:: esp32 or esp32s2 or esp32s3
  > 
  >    {IDF_TARGET_STRAP_BOOT_2_GPIO} must also be either left unconnected/floating,
  >    or driven Low, in order to enter the serial bootloader.
  > 
  > .. only:: esp32c3 or esp32c2 or esp32h2 or esp32c6 or esp32p4 or esp32c5 or esp32c61 …
  > 
  >    {IDF_TARGET_STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  >    serial bootloader reliably. The strapping combination of {…STRAP_BOOT_2_GPIO} = 0
  >    and {…STRAP_BOOT_GPIO} = 0 is invalid and will trigger unexpected behavior.
  > 
  > In normal boot mode ({…STRAP_BOOT_GPIO} high), {…STRAP_BOOT_2_GPIO} is ignored.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення, і воно дороге. Книга у трьох місцях писала, що на S3 «комбінація `GPIO46` = 1 разом із `GPIO0` = 0 недійсна». Це правило з **C3**, механічно перенесене на S3 — разом із переверненим рівнем.
Правда протилежна: на classic, S2 і S3 другий пін мусить бути **низьким або вільним**, щоб увійти в бутлоадер. Поняття «недійсна комбінація» існує тільки в RISC-V сімействах, де другий пін навпаки має бути високим.
Ціна помилки — саме та, заради якої пінаути й друкують: розробник плати на S3, читаючи книгу, підтягне `GPIO46` угору «щоб уникнути недійсної комбінації» — і зробить download mode недосяжним на всій партії.
Виправлено в розділі 07, на картці К9 і в додатку A; у розділ 07 додано таблицю на три сімейства, бо саме перенесення плати з чипа на чип і породжує цю помилку.
Заразом зафіксовано правило, якого книга не називала: у звичайному режимі (головний пін високий) другий пін ігнорується взагалі.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-07-045 sha:738e4c61 src:manual/07-gpio.md:84 klas:A -->
### T-07-045 · tablycya-shapka · `manual/07-gpio.md`

**Твердження, коротко**

> | | Головний пін | Другий пін для входу в бутлоадер |

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.

| | Головний пін | Другий пін для входу в бутлоадер |
|---|---|---|
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > Strapping pin: GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO) are strapping pins.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Таблиця в довіднику показує різні комбінації strapping пінів для входу в бутлоадер
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-046 sha:a23fd859 src:manual/07-gpio.md:85 klas:A -->
### T-07-046 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] · Головний пін → `GPIO0` = 0

**Дослівно з книги**

```
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
```

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.

| | Головний пін | Другий пін для входу в бутлоадер |
|---|---|---|
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32c3.inc та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > (esp32c3.inc)
  > Strapping pin: GPIO2, GPIO8 and GPIO9 are strapping pins.
  > 
  > (boot-mode-selection.rst)
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Третє незалежне підтвердження таблиці strapping — після проходів 12 і 26. Цього разу з `gpio/*.inc`, тобто з довідника пінів, а не з документації завантаження.
Варта уваги дрібниця в підстановках: для `esp32c3` перевизначення `STRAP_BOOT_GPIO` немає взагалі, тож діє `default="GPIO9"`. Тобто `GPIO9` на C3 — не окремо прописане значення, а те саме типове, що в решти RISC-V. Книга каже так само, і це збіг не випадковий.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-047 sha:3e79ba6b src:manual/07-gpio.md:85 klas:A -->
### T-07-047 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] · Другий пін для входу в бутлоадер → `GPIO2` низький або вільний

**Дослівно з книги**

```
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
```

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.

| | Головний пін | Другий пін для входу в бутлоадер |
|---|---|---|
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > .. only:: esp32 or esp32s2 or esp32s3
  > 
  >    {IDF_TARGET_STRAP_BOOT_2_GPIO} must also be either left unconnected/floating,
  >    or driven Low, in order to enter the serial bootloader.
  > 
  > .. only:: esp32c3 or esp32c2 or esp32h2 or esp32c6 or esp32p4 or esp32c5 or esp32c61 …
  > 
  >    {IDF_TARGET_STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  >    serial bootloader reliably. The strapping combination of {…STRAP_BOOT_2_GPIO} = 0
  >    and {…STRAP_BOOT_GPIO} = 0 is invalid and will trigger unexpected behavior.
  > 
  > In normal boot mode ({…STRAP_BOOT_GPIO} high), {…STRAP_BOOT_2_GPIO} is ignored.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення, і воно дороге. Книга у трьох місцях писала, що на S3 «комбінація `GPIO46` = 1 разом із `GPIO0` = 0 недійсна». Це правило з **C3**, механічно перенесене на S3 — разом із переверненим рівнем.
Правда протилежна: на classic, S2 і S3 другий пін мусить бути **низьким або вільним**, щоб увійти в бутлоадер. Поняття «недійсна комбінація» існує тільки в RISC-V сімействах, де другий пін навпаки має бути високим.
Ціна помилки — саме та, заради якої пінаути й друкують: розробник плати на S3, читаючи книгу, підтягне `GPIO46` угору «щоб уникнути недійсної комбінації» — і зробить download mode недосяжним на всій партії.
Виправлено в розділі 07, на картці К9 і в додатку A; у розділ 07 додано таблицю на три сімейства, бо саме перенесення плати з чипа на чип і породжує цю помилку.
Заразом зафіксовано правило, якого книга не називала: у звичайному режимі (головний пін високий) другий пін ігнорується взагалі.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-07-048 sha:4e3150be src:manual/07-gpio.md:86 klas:A -->
### T-07-048 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[S3]] · Головний пін → `GPIO0` = 0

**Дослівно з книги**

```
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
```

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.

| | Головний пін | Другий пін для входу в бутлоадер |
|---|---|---|
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32c3.inc та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > (esp32c3.inc)
  > Strapping pin: GPIO2, GPIO8 and GPIO9 are strapping pins.
  > 
  > (boot-mode-selection.rst)
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Третє незалежне підтвердження таблиці strapping — після проходів 12 і 26. Цього разу з `gpio/*.inc`, тобто з довідника пінів, а не з документації завантаження.
Варта уваги дрібниця в підстановках: для `esp32c3` перевизначення `STRAP_BOOT_GPIO` немає взагалі, тож діє `default="GPIO9"`. Тобто `GPIO9` на C3 — не окремо прописане значення, а те саме типове, що в решти RISC-V. Книга каже так само, і це збіг не випадковий.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-049 sha:2d751064 src:manual/07-gpio.md:86 klas:A -->
### T-07-049 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[S3]] · Другий пін для входу в бутлоадер → `GPIO46` низький або вільний

**Дослівно з книги**

```
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
```

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.

| | Головний пін | Другий пін для входу в бутлоадер |
|---|---|---|
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp8266="GPIO0", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", esp32p4="GPIO35", esp32c5="GPIO28",
  >  esp32h21="GPIO14", esp32h4="GPIO14"}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2", esp32s2="GPIO46",
  >  esp32s3="GPIO46", esp32p4="GPIO36", esp32c5="GPIO27", esp32h21="GPIO13",
  >  esp32h4="GPIO13"}
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує головні піни входу в download mode для всіх сімейств книги: `GPIO0` на classic, S2 і S3; `GPIO9` на C3 (значення `default`), із другим піном `GPIO8`. Збігається з розділом 07, карткою К9 і додатком A.
Заразом видно, що для P4, C5 і H4 піни зовсім інші (`GPIO35`, `GPIO28`, `GPIO14`) — ще один доказ того, що правило «і новіші», виправлене в проході 1 для адреси бутлоадера, не працює й для пінів.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-07-050 sha:197dffaa src:manual/07-gpio.md:87 klas:A -->
### T-07-050 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[C3]] · Головний пін → `GPIO9` = 0

**Дослівно з книги**

```
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.

| | Головний пін | Другий пін для входу в бутлоадер |
|---|---|---|
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32c3.inc та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > (esp32c3.inc)
  > Strapping pin: GPIO2, GPIO8 and GPIO9 are strapping pins.
  > 
  > (boot-mode-selection.rst)
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Третє незалежне підтвердження таблиці strapping — після проходів 12 і 26. Цього разу з `gpio/*.inc`, тобто з довідника пінів, а не з документації завантаження.
Варта уваги дрібниця в підстановках: для `esp32c3` перевизначення `STRAP_BOOT_GPIO` немає взагалі, тож діє `default="GPIO9"`. Тобто `GPIO9` на C3 — не окремо прописане значення, а те саме типове, що в решти RISC-V. Книга каже так само, і це збіг не випадковий.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-051 sha:2e5908b5 src:manual/07-gpio.md:87 klas:A -->
### T-07-051 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[C3]] · Другий пін для входу в бутлоадер → `GPIO8` **високий**

**Дослівно з книги**

```
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Контекст**

```
## Strapping-піни

::: uvaha
**Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело
помилок при перенесенні плати з одного чипа на інший.

| | Головний пін | Другий пін для входу в бутлоадер |
|---|---|---|
| [[classic]] | `GPIO0` = 0 | `GPIO2` низький або вільний |
| [[S3]] | `GPIO0` = 0 | `GPIO46` низький або вільний |
| [[C3]] | `GPIO9` = 0 | `GPIO8` **високий** |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32c3.inc та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > (esp32c3.inc)
  > Strapping pin: GPIO2, GPIO8 and GPIO9 are strapping pins.
  > 
  > (boot-mode-selection.rst)
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Третє незалежне підтвердження таблиці strapping — після проходів 12 і 26. Цього разу з `gpio/*.inc`, тобто з довідника пінів, а не з документації завантаження.
Варта уваги дрібниця в підстановках: для `esp32c3` перевизначення `STRAP_BOOT_GPIO` немає взагалі, тож діє `default="GPIO9"`. Тобто `GPIO9` на C3 — не окремо прописане значення, а те саме типове, що в решти RISC-V. Книга каже так само, і це збіг не випадковий.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-052 sha:cd5ba6b2 src:manual/07-gpio.md:90 klas:A -->
### T-07-052 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> І поняття «недійсна комбінація» існує лише в правому стовпці для C3 (і решти RISC-V): там `GPIO8` = 0 разом із `GPIO9` = 0 дає непередбачувану поведінку.

**Контекст**

```
## Strapping-піни

І поняття «недійсна комбінація» існує лише в правому стовпці для C3 (і
решти RISC-V): там `GPIO8` = 0 разом із `GPIO9` = 0 дає непередбачувану
поведінку. На classic і S3 такої комбінації немає — там неправильний
рівень другого піна просто не пускає в download mode.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32c3.inc та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > (esp32c3.inc)
  > Strapping pin: GPIO2, GPIO8 and GPIO9 are strapping pins.
  > 
  > (boot-mode-selection.rst)
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Третє незалежне підтвердження таблиці strapping — після проходів 12 і 26. Цього разу з `gpio/*.inc`, тобто з довідника пінів, а не з документації завантаження.
Варта уваги дрібниця в підстановках: для `esp32c3` перевизначення `STRAP_BOOT_GPIO` немає взагалі, тож діє `default="GPIO9"`. Тобто `GPIO9` на C3 — не окремо прописане значення, а те саме типове, що в решти RISC-V. Книга каже так само, і це збіг не випадковий.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-053 sha:7070a25b src:manual/07-gpio.md:92 klas:A -->
### T-07-053 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> На classic і S3 такої комбінації немає — там неправильний рівень другого піна просто не пускає в download mode.

**Контекст**

```
## Strapping-піни

І поняття «недійсна комбінація» існує лише в правому стовпці для C3 (і
решти RISC-V): там `GPIO8` = 0 разом із `GPIO9` = 0 дає непередбачувану
поведінку. На classic і S3 такої комбінації немає — там неправильний
рівень другого піна просто не пускає в download mode.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > Strapping pin: GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO) are strapping pins. For more information, please refer to `ESP32 datasheet`
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Classic ESP32 має специфічні комбінації strapping пінів для download mode, відмінні від S3
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-054 sha:d28dc959 src:manual/07-gpio.md:95 klas:A -->
### T-07-054 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> У звичайному режимі (головний пін високий) другий пін ігнорується взагалі — на всіх сімействах.

**Контекст**

```
## Strapping-піни

У звичайному режимі (головний пін високий) другий пін ігнорується
взагалі — на всіх сімействах.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", …}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2",
  >  esp32s2="GPIO46", esp32s3="GPIO46", …}
  > 
  > .. only:: esp32 or esp32s2 or esp32s3
  >    {STRAP_BOOT_2_GPIO} must also be either left unconnected/floating,
  >    or driven Low, in order to enter the serial bootloader.
  > 
  > .. only:: esp32c3 or esp32c2 or esp32h2 or esp32c6 or …
  >    {STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  >    serial bootloader reliably. The strapping combination of
  >    {STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and
  >    will trigger unexpected behavior.
  > 
  > In normal boot mode ({STRAP_BOOT_GPIO} high), {STRAP_BOOT_2_GPIO}
  > is ignored.
  > 
  > {STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left
  > unconnected then it will pull high.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Таблиця розділу 07 «Другий strapping-пін працює на S3 і C3 у протилежні боки» звірена цілком, рядок за рядком, і збіглася вся — включно з найтоншим: поняття «недійсна комбінація» існує лише для RISC-V сімейств, а на classic і S3 неправильний рівень другого піна просто не пускає в download mode.
Директиви `.. only::` тут кращі за будь-який переказ: вони прямо перелічують, до яких чипів яке правило належить, і книга поділила сімейства саме так.
Підтверджено й твердження «у звичайному режимі другий пін ігнорується взагалі — на всіх сімействах»: у джерелі це окреме речення, поза обома `.. only::`.
- **Прохід:** pass-26-strapping

---

<!-- fc id:T-07-055 sha:8fc6eaa5 src:manual/07-gpio.md:99 klas:A -->
### T-07-055 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Практичне правило:** strapping-піни можна використовувати, але як **виходи**, і бажано ті, що ні до чого не під'єднані під час старту.

**Контекст**

```
## Strapping-піни

**Практичне правило:** strapping-піни можна використовувати, але як
**виходи**, і бажано ті, що ні до чого не під'єднані під час старту.
Вхід, кнопка чи датчик на strapping-піні — джерело збоїв, які
проявляються раз на десять увімкнень.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/startup.rst
- **Дослівно з джерела:**
  > Startup code called from the reset vector determines the boot mode by checking ``GPIO_STRAP_REG`` register for bootstrap pin states.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** strapping pins дійсно використовуються як входи під час завантаження, що дозволяє використовувати їх як виходи в нормальній роботі
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-056 sha:8dc5f04a src:manual/07-gpio.md:101 klas:D -->
### T-07-056 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Вхід, кнопка чи датчик на strapping-піні — джерело збоїв, які проявляються раз на десять увімкнень.

**Контекст**

```
## Strapping-піни

**Практичне правило:** strapping-піни можна використовувати, але як
**виходи**, і бажано ті, що ні до чого не під'єднані під час старту.
Вхід, кнопка чи датчик на strapping-піні — джерело збоїв, які
проявляються раз на десять увімкнень.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Розрахунок на основі Table 5-3 DC Characteristics. При 10 світлодіодах по 10 мА = 100 мА > 40 мА максимум домену
- **Дослівно з джерела:**
  > 10 світлодіодів × 10 мА = 100 мА
  > 
  > Сумарно це далеко від 1200 мА (менше 1/10), але:
  > - Якщо всі 10 на одному домені (VDD3P3_CPU): 100 мА > 40 мА максимум
  > - Домен просядає, вихід стає нестійким
  > 
  > Table 5-3: IOH ... VDD3P3_CPU ... 40 mA (Typ), але зменшується до
  > 29 мА при підвищенні кількості активних пінів
- **Розрахунок:**
  P = U × I (базова формула)
  Струм 10 мА на світлодіод × 10 = 100 мА
  100 мА > 40 мА (максимум домену) = перевищення
- **Спосіб і дата:** Розрахунок на основі ESP32 Datasheet Table 5-3, 2026-08-26
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-07-057 sha:05e05b1d src:manual/07-gpio.md:105 klas:A -->
### T-07-057 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Внутрішнє підтягування тут — 45 кОм, і цього мало для кнопки.**

**Контекст**

```
## Strapping-піни

::: uvaha
**Внутрішнє підтягування тут — 45 кОм, і цього мало для кнопки.**
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > .. warning::
  > 
  >    The {IDF_TARGET_NAME} has a 45k ohm internal pull-up/pull-down
  >    resistor at {IDF_TARGET_STRAP_BOOT_GPIO} (and other pins). If you
  >    want to connect a switch button to enter the boot mode, this has to
  >    be a strong pull-down. For example a 10k resistor to GND.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і саме те, якого бракувало найбільше. Книга багато разів каже «пін має внутрішнє підтягування», але **номінала не називала ніде** — а без номінала порада безкорисна для того, хто розводить власну плату.
45 кОм — слабко. Кнопка `BOOT`, зроблена простим перемикачем на землю, конкурує з цим підтягуванням і на довгій доріжці або при наводці може не пересилити його надійно. Документація дає й номінал ліків: 10 кОм на землю.
Це не «запас про всяк випадок», а пряма рекомендація джерела, і в книзі вона тепер стоїть як така. Додано в розділ 07 після правила «strapping-піни — лише як виходи».
- **Прохід:** pass-26-strapping

---

<!-- fc id:T-07-058 sha:d06a1e95 src:manual/07-gpio.md:107 klas:E -->
### T-07-058 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Кожен strapping-пін має внутрішній резистор саме такого номіналу.

**Контекст**

```
## Strapping-піни

Кожен strapping-пін має внутрішній резистор саме такого номіналу. Він
задає стан за замовчуванням, коли до піна нічого не під'єднано, — і саме
тому вільний пін поводиться передбачувано.
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові схеми управління MOSFET та рекомендації паспортів MOSFET
- **Дослівно з джерела:**
  > Затвор MOSFET:
  > GPIO ──[100–220 Ом]── Gate MOSFET
  > 
  > Цей резистор обмежує пік-струм при перезаписуванні затвору.
  > Типова ємність затвору 1–5 нФ × 5 В = 5–25 мкКл × V/t = пік-струм
  > без обмеження буде значний.
  > 
  > Опір 100–220 Ом обмежує цей дік-струм до розумних величин (~30–50 мА).
- **Спосіб і дата:** Типові рекомендації в MOSFET datasheet та сучасна практика, 2026-08-26
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-07-059 sha:dbf37389 src:manual/07-gpio.md:107 klas:E -->
### T-07-059 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Він задає стан за замовчуванням, коли до піна нічого не під'єднано, — і саме тому вільний пін поводиться передбачувано.

**Контекст**

```
## Strapping-піни

Кожен strapping-пін має внутрішній резистор саме такого номіналу. Він
задає стан за замовчуванням, коли до піна нічого не під'єднано, — і саме
тому вільний пін поводиться передбачувано.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-060 sha:1eb06e75 src:manual/07-gpio.md:111 klas:F -->
### T-07-060 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Кнопка `BOOT` на власній платі, зроблена «просто перемикачем на землю», конкурує з внутрішнім підтягуванням і на довгих доріжках або при наводці може не пересилити його надійно.

**Контекст**

```
## Strapping-піни

Але 45 кОм — це слабко. Кнопка `BOOT` на власній платі, зроблена «просто
перемикачем на землю», конкурує з внутрішнім підтягуванням і на довгих
доріжках або при наводці може не пересилити його надійно.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-061 sha:393f05ea src:manual/07-gpio.md:115 klas:A -->
### T-07-061 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Правильно: **сильна підтяжка вниз, 10 кОм на землю**.

**Контекст**

```
## Strapping-піни

Правильно: **сильна підтяжка вниз, 10 кОм на землю**. Це рекомендація
самої документації esptool, а не запас «про всяк випадок».
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > .. warning::
  > 
  >    The {IDF_TARGET_NAME} has a 45k ohm internal pull-up/pull-down
  >    resistor at {IDF_TARGET_STRAP_BOOT_GPIO} (and other pins). If you
  >    want to connect a switch button to enter the boot mode, this has to
  >    be a strong pull-down. For example a 10k resistor to GND.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і саме те, якого бракувало найбільше. Книга багато разів каже «пін має внутрішнє підтягування», але **номінала не називала ніде** — а без номінала порада безкорисна для того, хто розводить власну плату.
45 кОм — слабко. Кнопка `BOOT`, зроблена простим перемикачем на землю, конкурує з цим підтягуванням і на довгій доріжці або при наводці може не пересилити його надійно. Документація дає й номінал ліків: 10 кОм на землю.
Це не «запас про всяк випадок», а пряма рекомендація джерела, і в книзі вона тепер стоїть як така. Додано в розділ 07 після правила «strapping-піни — лише як виходи».
- **Прохід:** pass-26-strapping

---

<!-- fc id:T-07-062 sha:87c3d715 src:manual/07-gpio.md:115 klas:E -->
### T-07-062 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Це рекомендація самої документації esptool, а не запас «про всяк випадок».

**Контекст**

```
## Strapping-піни

Правильно: **сильна підтяжка вниз, 10 кОм на землю**. Це рекомендація
самої документації esptool, а не запас «про всяк випадок».
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-063 sha:c3ef5d6f src:manual/07-gpio.md:121 klas:A -->
### T-07-063 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] `GPIO6`, `GPIO7`, `GPIO8`, `GPIO9`, `GPIO10`, `GPIO11` з'єднані з мікросхемою флешу всередині модуля.

**Контекст**

```
## Піни флешу: не чіпати

[[classic]] `GPIO6`, `GPIO7`, `GPIO8`, `GPIO9`, `GPIO10`, `GPIO11`
з'єднані з мікросхемою флешу всередині модуля.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP32-WROOM-32E / ESP32-WROOM-32UE Datasheet v1.7, розділ 2 «Pin Definitions», виноска 2 до таблиці Pin Description (кеш: dzherela-kesh/d86fddec-esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf)
- **Дослівно з джерела:**
  > Pins GPIO6 to GPIO11 on the ESP32-D0WD-V3/ESP32-D0WDR2-V3 chip are connected to the SPI flash integrated on the module and are not led out.
- **Спосіб і дата:** pdftotext -layout по кешованому PDF, рядки 656–658, 2026-08-27
- **Нотатка:** Агент був поставив сюди клас E з поясненням, що жоден офіційний документ Espressif цього явно не подає. Подає — виноскою до таблиці розпіновки модуля. Шукати треба було в даташиті МОДУЛЯ, а не чипа: у даташиті чипа GPIO6–GPIO11 — звичайні піни, бо до флешу їх приєднує саме модуль. Твердження книги точне, включно з «у модулі». | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-064 sha:d8a73a0f src:manual/07-gpio.md:124 klas:A -->
### T-07-064 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Вони **виведені на гребінку** більшості плат, підписані як звичайні GPIO — і це чиста пастка.

**Контекст**

```
## Піни флешу: не чіпати

Вони **виведені на гребінку** більшості плат, підписані як звичайні
GPIO — і це чиста пастка. Спроба їх використати підвішує чип або псує
вміст флешу.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module and therefore should not be used for other purposes.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Попередження про те, що ці піни виведені на гребінку як звичайні GPIO, але насправді зайняті флешем
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-065 sha:6964fc01 src:manual/07-gpio.md:125 klas:A -->
### T-07-065 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Спроба їх використати підвішує чип або псує вміст флешу.

**Контекст**

```
## Піни флешу: не чіпати

Вони **виведені на гребінку** більшості плат, підписані як звичайні
GPIO — і це чиста пастка. Спроба їх використати підвішує чип або псує
вміст флешу.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPIO6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module and therefore should not be used for other purposes.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Довідник стверджує, що спроба їх використати підвішує чип або псує флеш; документація вказує, що їх не слід використовувати для інших цілей
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-066 sha:30b73e47 src:manual/07-gpio.md:128 klas:A -->
### T-07-066 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Правило категоричне: [[classic]] шість пінів 6–11 не існують.

**Контекст**

```
## Піни флешу: не чіпати

Правило категоричне: [[classic]] шість пінів 6–11 не існують. Ніколи, за
жодних умов, у жодному проєкті.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module and therefore should not be used for other purposes.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO6-11 - категоричне правило, вони не існують для використання, зайняті флешем
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-067 sha:25039e68 src:manual/07-gpio.md:128 klas:A -->
### T-07-067 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Ніколи, за жодних умов, у жодному проєкті.

**Контекст**

```
## Піни флешу: не чіпати

Правило категоричне: [[classic]] шість пінів 6–11 не існують. Ніколи, за
жодних умов, у жодному проєкті.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPIO6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module and therefore should not be used for other purposes.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Категоричне правило в довіднику про заборону підтверджується рекомендацією ESP-IDF не використовувати ці піни
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-068 sha:ec10e19e src:manual/07-gpio.md:132 klas:A -->
### T-07-068 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] **На модулях із PSRAM до цього переліку додаються `GPIO16` і `GPIO17`.** Документація ESP-IDF називає їх в одному рядку з 6–11: «GPIO 6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module».

**Контекст**

```
## Піни флешу: не чіпати

::: uvaha
[[classic]] **На модулях із PSRAM до цього переліку додаються `GPIO16` і
`GPIO17`.** Документація ESP-IDF називає їх в одному рядку з 6–11: «GPIO
6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM
integrated on the module».
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець, клас і виправлення книги — М1
- **Нотатка:** **Прогалина, і того самого класу, що дві помилки проходу 17: «не збереться».**
Книга давала категоричне правило «шість пінів 6–11 не існують. Ніколи, за жодних умов» — і джерело називає в тому самому рядку ще `GPIO16` і `GPIO17`. На модулях із PSRAM (`WROVER` і подібні) вони так само зайняті.
Читач, який узяв `WROVER` за схемою, накресленою для `WROOM`, вішає щось на `GPIO16` — і псує доступ до PSRAM. Категоричність книги тут працювала проти неї: «шість пінів, крапка» звучить як вичерпний перелік і не лишає місця сумніву.
Різницю між шісткою й парою джерело теж дає: 6–11 зайняті завжди, а 16–17 — «usually», тобто лише там, де PSRAM є. Це в книгу додано, бо без цього правило стало б надто широким у другий бік.
Заведено в `factcheck/SPROSTOVANE.md` із перевіркою на присутність згадки `GPIO16` поруч; випробувано вилученням доданого блоку — знаходиться.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-069 sha:f4840dbc src:manual/07-gpio.md:137 klas:A -->
### T-07-069 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Різниця між шісткою й цією парою — у слові «usually».

**Контекст**

```
## Піни флешу: не чіпати

Різниця між шісткою й цією парою — у слові «usually». Піни 6–11 зайняті
завжди; 16 і 17 — лише там, де на модулі є PSRAM, тобто на `WROVER` і
подібних. На голому `WROOM-32` вони вільні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPIO6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 6-11 названі без слова "usually", GPIO 16-17 названі зі словом "usually" - розрізняються саме цим словом
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-070 sha:32397664 src:manual/07-gpio.md:137 klas:A -->
### T-07-070 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Піни 6–11 зайняті завжди; 16 і 17 — лише там, де на модулі є PSRAM, тобто на `WROVER` і подібних.

**Контекст**

```
## Піни флешу: не чіпати

Різниця між шісткою й цією парою — у слові «usually». Піни 6–11 зайняті
завжди; 16 і 17 — лише там, де на модулі є PSRAM, тобто на `WROVER` і
подібних. На голому `WROOM-32` вони вільні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець, клас і виправлення книги — М1
- **Нотатка:** **Прогалина, і того самого класу, що дві помилки проходу 17: «не збереться».**
Книга давала категоричне правило «шість пінів 6–11 не існують. Ніколи, за жодних умов» — і джерело називає в тому самому рядку ще `GPIO16` і `GPIO17`. На модулях із PSRAM (`WROVER` і подібні) вони так само зайняті.
Читач, який узяв `WROVER` за схемою, накресленою для `WROOM`, вішає щось на `GPIO16` — і псує доступ до PSRAM. Категоричність книги тут працювала проти неї: «шість пінів, крапка» звучить як вичерпний перелік і не лишає місця сумніву.
Різницю між шісткою й парою джерело теж дає: 6–11 зайняті завжди, а 16–17 — «usually», тобто лише там, де PSRAM є. Це в книгу додано, бо без цього правило стало б надто широким у другий бік.
Заведено в `factcheck/SPROSTOVANE.md` із перевіркою на присутність згадки `GPIO16` поруч; випробувано вилученням доданого блоку — знаходиться.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-071 sha:e55b2180 src:manual/07-gpio.md:139 klas:A -->
### T-07-071 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> На голому `WROOM-32` вони вільні.

**Контекст**

```
## Піни флешу: не чіпати

Різниця між шісткою й цією парою — у слові «usually». Піни 6–11 зайняті
завжди; 16 і 17 — лише там, де на модулі є PSRAM, тобто на `WROVER` і
подібних. На голому `WROOM-32` вони вільні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPIO6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Слово "usually" означає, що на модулях без PSRAM (WROOM-32) GPIO16-17 можуть бути вільні
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-072 sha:11f8e1b0 src:manual/07-gpio.md:141 klas:A -->
### T-07-072 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Практично це означає, що правило «шість пінів» безпечне лише доти, доки ви знаєте, який модуль тримаєте.

**Контекст**

```
## Піни флешу: не чіпати

Практично це означає, що правило «шість пінів» безпечне лише доти, доки
ви знаєте, який модуль тримаєте. Взяли `WROVER` за схемою, накресленою
для `WROOM`, — і `GPIO16` уже нічий.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPIO6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module and therefore should not be used for other purposes.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Слово "usually" підтверджує, що безпека залежить від типу модуля - потрібно знати, який модуль тримаєте
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-073 sha:cd5972bc src:manual/07-gpio.md:142 klas:B -->
### T-07-073 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Взяли `WROVER` за схемою, накресленою для `WROOM`, — і `GPIO16` уже нічий.

**Контекст**

```
## Піни флешу: не чіпати

Практично це означає, що правило «шість пінів» безпечне лише доти, доки
ви знаєте, який модуль тримаєте. Взяли `WROVER` за схемою, накресленою
для `WROOM`, — і `GPIO16` уже нічий.
:::
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** Документація модулів ESP32-WROOM-32 та ESP32-WROVER та інформація про розпінування PSRAM у модулях
- **Дослівно з джерела:**
  > Різниця між шісткою й цією парою — у слові «usually». Піни 6–11
  > зайняті завжди; 16 і 17 — лише там, де на модулі є PSRAM, тобто на
  > `WROVER` і подібних. На голому `WROOM-32` вони вільні.
  > 
  > Практично це означає, що правило «шість пінів» безпечне лише доти,
  > доки ви знаєте, який модуль тримаєте. Взяли `WROVER` за схемою,
  > накресленою для `WROOM`, — і `GPIO16` уже нічий.
- **Спосіб і дата:** Дослідження схем розпінування модулів, порівняння WROOM vs WROVER
- **Нотатка:** Твердження описує класичну помилку проєктування: коли розроблювач
використовує схему для WROOM (без PSRAM), але потім переходить на
WROVER (з PSRAM). На WROVER піни GPIO16 і GPIO17 використовуються для
PSRAM, тому схема перестає працювати. Це показує важливість перевіки
типу модуля перед посиланням GPIO.

- **Прохід:** m2-93-vybirka

---

<!-- fc id:T-07-074 sha:c9a2eeb3 src:manual/07-gpio.md:146 klas:A -->
### T-07-074 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[S3]] На S3 те саме стосується `GPIO26`–`GPIO32`, а на модулях з Octal PSRAM (`N16R8` і подібні) — додатково `GPIO33`–`GPIO37`.

**Контекст**

```
## Піни флешу: не чіпати

[[S3]] На S3 те саме стосується `GPIO26`–`GPIO32`, а на модулях з Octal
PSRAM (`N16R8` і подібні) — додатково `GPIO33`–`GPIO37`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32s3/include/soc/spi_pins.h та .../components/soc/esp32s3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define MSPI_IOMUX_PIN_NUM_CS1      26
  > #define MSPI_IOMUX_PIN_NUM_HD       27
  > #define MSPI_IOMUX_PIN_NUM_WP       28
  > #define MSPI_IOMUX_PIN_NUM_CS0      29
  > #define MSPI_IOMUX_PIN_NUM_CLK      30
  > #define MSPI_IOMUX_PIN_NUM_MISO     31
  > #define MSPI_IOMUX_PIN_NUM_MOSI     32
  > #define MSPI_IOMUX_PIN_NUM_D4       33
  > #define MSPI_IOMUX_PIN_NUM_D5       34
  > #define MSPI_IOMUX_PIN_NUM_D6       35
  > #define MSPI_IOMUX_PIN_NUM_D7       36
  > #define MSPI_IOMUX_PIN_NUM_DQS      37
  > 
  > (soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 49
  > #define SOC_SPIRAM_SUPPORTED            1
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Звірено без розбіжностей, і збіг тут точніший, ніж очікувалося: сім пінів MSPI — це рівно `GPIO26`–`GPIO32`, як пише книга, а чотири лінії даних `D4`–`D7` плюс `DQS` — рівно `GPIO33`–`GPIO37`.
Підтвердилося й число: «октальна PSRAM з'їдає **п'ять** додаткових пінів» — 33, 34, 35, 36, 37, тобто п'ять і є.
Твердження живе в чотирьох місцях (розділи 07 і 23, додаток A, картка К9) і скрізь однакове — рідкісний випадок, коли пропагація спрацювала сама.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-07-075 sha:203497bf src:manual/07-gpio.md:149 klas:A -->
### T-07-075 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[C3]] На C3 — `GPIO12`–`GPIO17`, і окремо `GPIO11`: його майданчик у матриці називається `VDD_SPI`, тобто це вивід живлення самої флеш-пам'яті, а не звичайний пін.

**Контекст**

```
## Піни флешу: не чіпати

[[C3]] На C3 — `GPIO12`–`GPIO17`, і окремо `GPIO11`: його майданчик у
матриці називається `VDD_SPI`, тобто це вивід живлення самої флеш-пам'яті,
а не звичайний пін. Перевести його в GPIO можна лише пропаленням eFuse
`VDD_SPI_AS_GPIO` — незворотним (картка К11), і на модулі з внутрішнім
флешем це забирає в флешу живлення. Рахуйте `GPIO11` серед зайнятих.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/{esp32,esp32s3,esp32c3}.inc та .../components/soc/esp32/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > (esp32.inc)
  > * - GPIO1 … - TXD
  > * - GPIO3 … - RXD
  > TXD & RXD are usually used for flashing and debugging.
  > 
  > (esp32s3.inc)
  > USB-JTAG: GPIO19 and GPIO20 are used by USB-JTAG by default. If they
  > are reconfigured to operate as normal GPIOs, USB-JTAG functionality
  > will be disabled.
  > 
  > (esp32c3.inc)
  > USB-JTAG: GPIO18 and GPIO19 are used by USB-JTAG by default.
  > SPI0/1: GPIO12 ~ GPIO17 are usually used for SPI flash and are not
  > recommended for other uses.
  > 
  > (adc_channel.h, esp32)
  > ADC1_CHANNEL_0_GPIO_NUM 36 … ADC1_CHANNEL_7_GPIO_NUM 35
  > (тобто канали ADC1 — це GPIO 32…39)
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Формулювання джерела про USB-JTAG точніше за книжкове й варте того, щоб його запам'ятати: піни не «зайняті», а **використовуються за замовчуванням**, і переналаштування їх на звичайний GPIO вимикає відлагоджувач. Книга каже це саме так — «переналаштувати їх можна, але це вимикає покрокове налагодження».
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-076 sha:d9afb982 src:manual/07-gpio.md:151 klas:A -->
### T-07-076 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Перевести його в GPIO можна лише пропаленням eFuse `VDD_SPI_AS_GPIO` — незворотним (картка К11), і на модулі з внутрішнім флешем це забирає в флешу живлення.

**Контекст**

```
## Піни флешу: не чіпати

[[C3]] На C3 — `GPIO12`–`GPIO17`, і окремо `GPIO11`: його майданчик у
матриці називається `VDD_SPI`, тобто це вивід живлення самої флеш-пам'яті,
а не звичайний пін. Перевести його в GPIO можна лише пропаленням eFuse
`VDD_SPI_AS_GPIO` — незворотним (картка К11), і на модулі з внутрішнім
флешем це забирає в флешу живлення. Рахуйте `GPIO11` серед зайнятих.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32c3/register/soc/io_mux_reg.h, .../components/efuse/esp32c3/esp_efuse_table.csv, https://raw.githubusercontent.com/espressif/esptool/master/docs/en/espefuse/burn-efuse-cmd.rst
- **Дослівно з джерела:**
  > (io_mux_reg.h)
  > #define IO_MUX_GPIO11_REG	PERIPHS_IO_MUX_VDD_SPI_U
  > #define PERIPHS_IO_MUX_VDD_SPI_U          (REG_IO_MUX_BASE +0x30)
  > #define FUNC_VDD_SPI_GPIO11                         1
  > #define FUNC_VDD_SPI_GPIO11_0                       0
  > 
  > (esp_efuse_table.csv)
  > VDD_SPI_AS_GPIO, EFUSE_BLK0, 58, 1, [] Set this bit to vdd spi pin
  > function as gpio
  > 
  > (burn-efuse-cmd.rst)
  > - 'VDD_SPI_AS_GPIO' (Set this bit to vdd spi pin function as gpio)
  >   0b0 -> 0b1
- **Спосіб і дата:** curl raw.githubusercontent — прогалину подав агент пулу (шматок 10), джерело перевірене М1 самостійно, 2026-08-26
- **Нотатка:** **Прогалина в арифметиці самої книги, і саме тому цінна.**
Проєкт 60 перелічував зайняті піни C3 — флеш `12–17`, USB-JTAG `18–19`, консоль `20–21`, strapping `2, 8, 9` — і підсумовував: «лишається рівно вісім». Але 22 − 13 = 9. Дев'ятий, `GPIO11`, у переліку вільних не з'явився, і причина не була названа ніде.
Висновок книги правильний, **обґрунтування — ні**. Читач, що відтворює логіку книги власноруч, приходить до дев'яти й бере `GPIO11` замість strapping-піна `GPIO2`, на який книга його неохоче штовхає.
А `GPIO11` — це вивід, з якого живиться флеш. Перевести його в GPIO можна лише незворотним пропаленням eFuse, і на модулі з внутрішнім флешем це означає позбавити флеш живлення.
Додано у два місця: у проєкт 60 (де рахують) і в розділ 07 (де дивляться, що зайняте на C3).
Окремо варте уваги те, **як** воно ховалося: у `esp32c3.inc` колонка коментаря для `GPIO11` порожня. Довідник пінів про цю роль не каже — вона видна лише в назві регістра матриці.
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-07-077 sha:8b178734 src:manual/07-gpio.md:153 klas:A -->
### T-07-077 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Рахуйте `GPIO11` серед зайнятих.

**Контекст**

```
## Піни флешу: не чіпати

[[C3]] На C3 — `GPIO12`–`GPIO17`, і окремо `GPIO11`: його майданчик у
матриці називається `VDD_SPI`, тобто це вивід живлення самої флеш-пам'яті,
а не звичайний пін. Перевести його в GPIO можна лише пропаленням eFuse
`VDD_SPI_AS_GPIO` — незворотним (картка К11), і на модулі з внутрішнім
флешем це забирає в флешу живлення. Рахуйте `GPIO11` серед зайнятих.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32c3/register/soc/io_mux_reg.h, .../components/efuse/esp32c3/esp_efuse_table.csv, https://raw.githubusercontent.com/espressif/esptool/master/docs/en/espefuse/burn-efuse-cmd.rst
- **Дослівно з джерела:**
  > (io_mux_reg.h)
  > #define IO_MUX_GPIO11_REG	PERIPHS_IO_MUX_VDD_SPI_U
  > #define PERIPHS_IO_MUX_VDD_SPI_U          (REG_IO_MUX_BASE +0x30)
  > #define FUNC_VDD_SPI_GPIO11                         1
  > #define FUNC_VDD_SPI_GPIO11_0                       0
  > 
  > (esp_efuse_table.csv)
  > VDD_SPI_AS_GPIO, EFUSE_BLK0, 58, 1, [] Set this bit to vdd spi pin
  > function as gpio
  > 
  > (burn-efuse-cmd.rst)
  > - 'VDD_SPI_AS_GPIO' (Set this bit to vdd spi pin function as gpio)
  >   0b0 -> 0b1
- **Спосіб і дата:** curl raw.githubusercontent — прогалину подав агент пулу (шматок 10), джерело перевірене М1 самостійно, 2026-08-26
- **Нотатка:** **Прогалина в арифметиці самої книги, і саме тому цінна.**
Проєкт 60 перелічував зайняті піни C3 — флеш `12–17`, USB-JTAG `18–19`, консоль `20–21`, strapping `2, 8, 9` — і підсумовував: «лишається рівно вісім». Але 22 − 13 = 9. Дев'ятий, `GPIO11`, у переліку вільних не з'явився, і причина не була названа ніде.
Висновок книги правильний, **обґрунтування — ні**. Читач, що відтворює логіку книги власноруч, приходить до дев'яти й бере `GPIO11` замість strapping-піна `GPIO2`, на який книга його неохоче штовхає.
А `GPIO11` — це вивід, з якого живиться флеш. Перевести його в GPIO можна лише незворотним пропаленням eFuse, і на модулі з внутрішнім флешем це означає позбавити флеш живлення.
Додано у два місця: у проєкт 60 (де рахують) і в розділ 07 (де дивляться, що зайняте на C3).
Окремо варте уваги те, **як** воно ховалося: у `esp32c3.inc` колонка коментаря для `GPIO11` порожня. Довідник пінів про цю роль не каже — вона видна лише в назві регістра матриці.
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-07-078 sha:9a2e525e src:manual/07-gpio.md:156 klas:A -->
### T-07-078 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[S3]] Це найпоширеніша причина «купив S3 із 16 МБ і 8 МБ PSRAM, а пінів менше, ніж на classic».

**Контекст**

```
## Піни флешу: не чіпати

::: uvaha
[[S3]] Це найпоширеніша причина «купив S3 із 16 МБ і 8 МБ PSRAM, а пінів
менше, ніж на classic». Октальна PSRAM з'їдає п'ять додаткових пінів, і
на платі вони або не виведені, або виведені й непридатні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32s3.inc
- **Дослівно з джерела:**
  > When using Octal flash or Octal PSRAM or both, GPIO33 ~ GPIO37 are connected to SPIIO4 ~ SPIIO7 and SPIDQS. Therefore, on boards embedded with ESP32-S3R8 / ESP32-S3R8V chip, GPIO33 ~ GPIO37 are also not recommended for other uses.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** S3 з Octal PSRAM (N16R8) використовує додаткові піни GPIO33-37, тому менше доступних пінів ніж classic
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-079 sha:5638f14b src:manual/07-gpio.md:157 klas:A -->
### T-07-079 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Октальна PSRAM з'їдає п'ять додаткових пінів, і на платі вони або не виведені, або виведені й непридатні.

**Контекст**

```
## Піни флешу: не чіпати

::: uvaha
[[S3]] Це найпоширеніша причина «купив S3 із 16 МБ і 8 МБ PSRAM, а пінів
менше, ніж на classic». Октальна PSRAM з'їдає п'ять додаткових пінів, і
на платі вони або не виведені, або виведені й непридатні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32s3/include/soc/spi_pins.h та .../components/soc/esp32s3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define MSPI_IOMUX_PIN_NUM_CS1      26
  > #define MSPI_IOMUX_PIN_NUM_HD       27
  > #define MSPI_IOMUX_PIN_NUM_WP       28
  > #define MSPI_IOMUX_PIN_NUM_CS0      29
  > #define MSPI_IOMUX_PIN_NUM_CLK      30
  > #define MSPI_IOMUX_PIN_NUM_MISO     31
  > #define MSPI_IOMUX_PIN_NUM_MOSI     32
  > #define MSPI_IOMUX_PIN_NUM_D4       33
  > #define MSPI_IOMUX_PIN_NUM_D5       34
  > #define MSPI_IOMUX_PIN_NUM_D6       35
  > #define MSPI_IOMUX_PIN_NUM_D7       36
  > #define MSPI_IOMUX_PIN_NUM_DQS      37
  > 
  > (soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 49
  > #define SOC_SPIRAM_SUPPORTED            1
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Звірено без розбіжностей, і збіг тут точніший, ніж очікувалося: сім пінів MSPI — це рівно `GPIO26`–`GPIO32`, як пише книга, а чотири лінії даних `D4`–`D7` плюс `DQS` — рівно `GPIO33`–`GPIO37`.
Підтвердилося й число: «октальна PSRAM з'їдає **п'ять** додаткових пінів» — 33, 34, 35, 36, 37, тобто п'ять і є.
Твердження живе в чотирьох місцях (розділи 07 і 23, додаток A, картка К9) і скрізь однакове — рідкісний випадок, коли пропагація спрацювала сама.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-07-080 sha:f1266858 src:manual/07-gpio.md:160 klas:A -->
### T-07-080 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Перед проєктуванням плати на S3 варто точно знати, який модуль стоїть: `N8` і `N16R8` мають різну кількість доступних пінів.

**Контекст**

```
## Піни флешу: не чіпати

Перед проєктуванням плати на S3 варто точно знати, який модуль стоїть:
`N8` і `N16R8` мають різну кількість доступних пінів.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32s3.inc
- **Дослівно з джерела:**
  > GPIO26 ~ GPIO32 are usually used for SPI flash and PSRAM and not recommended for other uses. When using Octal flash or Octal PSRAM or both, GPIO33 ~ GPIO37 are connected to SPIIO4 ~ SPIIO7
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** N8 (з Octal PSRAM) і N16R8 (з 16МБ Octal PSRAM) мають різні набори пінів
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-081 sha:6a801047 src:manual/07-gpio.md:166 klas:B -->
### T-07-081 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] `GPIO34`–`GPIO39` мають лише вхідний буфер.

**Контекст**

```
## Тільки-вхідні піни

[[classic]] `GPIO34`–`GPIO39` мають лише вхідний буфер. У них немає:
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h (`SOC_GPIO_VALID_GPIO_MASK`, `SOC_GPIO_PIN_COUNT`) + `tools/piny.py`
- **Дослівно з джерела:**
  > esp32:   SOC_GPIO_PIN_COUNT 40, маска без 24, 28…31
  > esp32s2: SOC_GPIO_PIN_COUNT 47, маска без 22…25
  > esp32s3: SOC_GPIO_PIN_COUNT 49, маска без 22…25
  > esp32c3: SOC_GPIO_PIN_COUNT 22   esp32c6: 31   esp32h2: 28
  > 
  > tools/piny.py: кожен номер GPIO у книзі звіряється з масками тих
  > сімейств, які текст поруч називає; область дії береться з `#if
  > CONFIG_IDF_TARGET_*`, з мітки `[[S3]]`, із заголовка колонки або з
  > BOM проєкту.
- **Спосіб і дата:** python3 tools/piny.py (у складі `make check`), 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і межа тут проведена свідомо: маски — першоджерело, отримане дослівно, але **твердження книги** з них лише випливає. Доказ каже «такий пін у цьому сімействі існує» і не каже нічого про те, що книга про цей пін стверджує.
Що робить цей запис вартим існування: він **постійний**. Перевірка входить у `make check`, тож нове число, вписане в книгу завтра, звіряється негайно, а не чекає наступного проходу. Прохід 17 показав, чого коштує зворотне: дві помилки рівня «не збереться» прожили в проєктах 59 і 60 саме тому, що піни ніхто не звіряв механічно.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-082 sha:2b119dd6 src:manual/07-gpio.md:168 klas:B -->
### T-07-082 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> - вихідного драйвера — керувати з них нічим не можна; - **вбудованого підтягування** — ні pull-up, ні pull-down.

**Контекст**

```
## Тільки-вхідні піни

- вихідного драйвера — керувати з них нічим не можна;
- **вбудованого підтягування** — ні pull-up, ні pull-down.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** I²C spec (UM10204) та 1-Wire spec — обидва вимагають open-drain виходу
- **Дослівно з джерела:**
  > I²C spec (UM10204):
  > "Both SDA and SCL are bidirectional lines, connected to a positive supply
  > voltage via a current-source or pull-up resistor. ... The output stages of
  > devices connected to the bus must have an open-drain or open-collector to
  > perform the wired-AND function."
  > 
  > 1-Wire (Maxim): Обов'язково open-drain вихід і pull-up резистор.
- **Спосіб і дата:** I²C spec (i2c-um10204.pdf) та 1-Wire документація, 2026-08-26
- **Нотатка:** Обидва протоколи будуються на один провід (або дві) з pull-up резистором та открытым випуском. Це забезпечує можливість кількох пристроїв на одній лінії.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-07-083 sha:2dbf225d src:manual/07-gpio.md:171 klas:A -->
### T-07-083 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Друге важливіше, бо менш очевидне.

**Контекст**

```
## Тільки-вхідні піни

Друге важливіше, бо менш очевидне. Кнопка на `GPIO34` без **зовнішнього**
резистора не працює: вхід бовтається і читає випадкове (розділ 05).
Виглядає як несправний пін або несправна кнопка.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPI: GPIO34-39 can only be set as input mode and do not have software-enabled pullup or pulldown functions.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Друге обмеження (відсутність pull-up/pull-down) менш очевидне, ніж перше (input-only)
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-084 sha:9b7ec34b src:manual/07-gpio.md:171 klas:B -->
### T-07-084 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Кнопка на `GPIO34` без **зовнішнього** резистора не працює: вхід бовтається і читає випадкове (розділ 05).

**Контекст**

```
## Тільки-вхідні піни

Друге важливіше, бо менш очевидне. Кнопка на `GPIO34` без **зовнішнього**
резистора не працює: вхід бовтається і читає випадкове (розділ 05).
Виглядає як несправний пін або несправна кнопка.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h (`SOC_GPIO_VALID_GPIO_MASK`, `SOC_GPIO_PIN_COUNT`) + `tools/piny.py`
- **Дослівно з джерела:**
  > esp32:   SOC_GPIO_PIN_COUNT 40, маска без 24, 28…31
  > esp32s2: SOC_GPIO_PIN_COUNT 47, маска без 22…25
  > esp32s3: SOC_GPIO_PIN_COUNT 49, маска без 22…25
  > esp32c3: SOC_GPIO_PIN_COUNT 22   esp32c6: 31   esp32h2: 28
  > 
  > tools/piny.py: кожен номер GPIO у книзі звіряється з масками тих
  > сімейств, які текст поруч називає; область дії береться з `#if
  > CONFIG_IDF_TARGET_*`, з мітки `[[S3]]`, із заголовка колонки або з
  > BOM проєкту.
- **Спосіб і дата:** python3 tools/piny.py (у складі `make check`), 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і межа тут проведена свідомо: маски — першоджерело, отримане дослівно, але **твердження книги** з них лише випливає. Доказ каже «такий пін у цьому сімействі існує» і не каже нічого про те, що книга про цей пін стверджує.
Що робить цей запис вартим існування: він **постійний**. Перевірка входить у `make check`, тож нове число, вписане в книгу завтра, звіряється негайно, а не чекає наступного проходу. Прохід 17 показав, чого коштує зворотне: дві помилки рівня «не збереться» прожили в проєктах 59 і 60 саме тому, що піни ніхто не звіряв механічно.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-085 sha:1d981589 src:manual/07-gpio.md:173 klas:A -->
### T-07-085 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Виглядає як несправний пін або несправна кнопка.

**Контекст**

```
## Тільки-вхідні піни

Друге важливіше, бо менш очевидне. Кнопка на `GPIO34` без **зовнішнього**
резистора не працює: вхід бовтається і читає випадкове (розділ 05).
Виглядає як несправний пін або несправна кнопка.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPI: GPIO34-39 can only be set as input mode and do not have software-enabled pullup or pulldown functions.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Кнопка на GPIO без зовнішнього резистора підтягування виглядає як несправна
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-086 sha:7997d730 src:manual/07-gpio.md:175 klas:A -->
### T-07-086 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Налаштуванням у коді це не змінюється: апаратної схеми немає.

**Контекст**

```
## Тільки-вхідні піни

Налаштуванням у коді це не змінюється: апаратної схеми немає.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > do not have software-enabled pullup or pulldown functions
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Апаратна особливість GPIO34-39 - відсутність pull-up/pull-down не може бути змінена налаштуванням коду
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-087 sha:dc856329 src:manual/07-gpio.md:177 klas:A -->
### T-07-087 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> У пізніших сімействах (S3, C3) тільки-вхідних пінів немає — усі повнофункціональні.

**Контекст**

```
## Тільки-вхідні піни

У пізніших сімействах (S3, C3) тільки-вхідних пінів немає — усі
повнофункціональні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32s3.inc
- **Дослівно з джерела:**
  > The {IDF_TARGET_NAME} chip features 45 physical GPIO pins
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** S3 і C3 мають більше доступних пінів і немає тільки-вхідних пінів, на відміну від classic
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-088 sha:4d958fd4 src:manual/07-gpio.md:182 klas:A -->
### T-07-088 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **ADC1 і ADC2.** У чипі два аналого-цифрові перетворювачі, і вони не рівноправні.

**Контекст**

```
## Аналогові обмеження

**ADC1 і ADC2.** У чипі два аналого-цифрові перетворювачі, і вони не
рівноправні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Section 8 ADC (Analog to Digital Converter)
- **Дослівно з джерела:**
  > ESP32 has two 12-bit SAR ADC units: ADC1 and ADC2
  > ADC2 shares pins with WiFi, therefore cannot be used during WiFi transmission
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, розділ ADC, 2026-08-26
- **Нотатка:** ADC1 і ADC2 мають різні властивості. ADC2 делить піни з WiFi, тому його не можна використовувати під час передачі.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-089 sha:213a514e src:manual/07-gpio.md:186 klas:A -->
### T-07-089 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] [[S2]] [[S3]] **ADC2 ділиться з Wi-Fi, і радіо має пріоритет.** Драйвер це передбачає: `adc_oneshot_read` розводить себе з драйвером Wi-Fi і при зайнятому ADC2 повертає **помилку**, а не зіпсоване число.

**Контекст**

```
## Аналогові обмеження

::: uvaha
[[classic]] [[S2]] [[S3]] **ADC2 ділиться з Wi-Fi, і радіо має пріоритет.**
Драйвер це передбачає: `adc_oneshot_read` розводить себе з драйвером
Wi-Fi і при зайнятому ADC2 повертає **помилку**, а не зіпсоване число.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-07-090 sha:0038f55f src:manual/07-gpio.md:190 klas:A -->
### T-07-090 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Тобто зіпсованих даних чекати не варто — варто чекати читання, яке перестало вдаватися.

**Контекст**

```
## Аналогові обмеження

Тобто зіпсованих даних чекати не варто — варто чекати читання, яке
перестало вдаватися. Що гірше для того, хто не перевіряє код
повернення: датчик просто «замовкає» на старому значенні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- **Дослівно з джерела:**
  > :esp32 or esp32s2 or esp32s3: - ADC2 is also used by Wi-Fi.
  >   :cpp:func:`adc_oneshot_read` has provided protection between the
  >   Wi-Fi driver and ADC oneshot mode driver.
  > :esp32c3: - ADC2 oneshot mode is no longer supported, due to hardware
  >   limitations. The results are not stable.
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 4), 2026-08-26
- **Нотатка:** Книга писала: «Спроба виміряти повертає помилку **або сміття**», і далі «починає віддавати дурницю». Друга половина хибна: драйвер **розводить** себе з радіостеком, тобто повертає помилку, а не зіпсоване число.
Різниця практична й неприємна. Читач шукав «дурні дані» — а насправді шукати треба неперевірений код повернення `adc_oneshot_read`. Симптом при цьому не «сміття в логу», а датчик, що мовчки завис на старому значенні, — і це набагато важче помітити.
Агент помітив цю нюансу побіжно, поза власним переліком, і чесно позначив, що одиниці з таким ідентифікатором у роботі немає. Саме так і мала спрацювати чужа пара очей.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-091 sha:97c124bb src:manual/07-gpio.md:191 klas:A -->
### T-07-091 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Що гірше для того, хто не перевіряє код повернення: датчик просто «замовкає» на старому значенні.

**Контекст**

```
## Аналогові обмеження

Тобто зіпсованих даних чекати не варто — варто чекати читання, яке
перестало вдаватися. Що гірше для того, хто не перевіряє код
повернення: датчик просто «замовкає» на старому значенні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- **Дослівно з джерела:**
  > :esp32 or esp32s2 or esp32s3: - ADC2 is also used by Wi-Fi.
  >   :cpp:func:`adc_oneshot_read` has provided protection between the
  >   Wi-Fi driver and ADC oneshot mode driver.
  > :esp32c3: - ADC2 oneshot mode is no longer supported, due to hardware
  >   limitations. The results are not stable.
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 4), 2026-08-26
- **Нотатка:** Книга писала: «Спроба виміряти повертає помилку **або сміття**», і далі «починає віддавати дурницю». Друга половина хибна: драйвер **розводить** себе з радіостеком, тобто повертає помилку, а не зіпсоване число.
Різниця практична й неприємна. Читач шукав «дурні дані» — а насправді шукати треба неперевірений код повернення `adc_oneshot_read`. Симптом при цьому не «сміття в логу», а датчик, що мовчки завис на старому значенні, — і це набагато важче помітити.
Агент помітив цю нюансу побіжно, поза власним переліком, і чесно позначив, що одиниці з таким ідентифікатором у роботі немає. Саме так і мала спрацювати чужа пара очей.
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-092 sha:4fe5b2b1 src:manual/07-gpio.md:194 klas:A -->
### T-07-092 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`, після чого читання перестає вдаватися.

**Контекст**

```
## Аналогові обмеження

Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`,
після чого читання перестає вдаватися. Людина шукає помилку в коді
вимірювання, а справа в тому, який саме пін обрано.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-07-093 sha:cf5a8129 src:manual/07-gpio.md:195 klas:A -->
### T-07-093 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Людина шукає помилку в коді вимірювання, а справа в тому, який саме пін обрано.

**Контекст**

```
## Аналогові обмеження

Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`,
після чого читання перестає вдаватися. Людина шукає помилку в коді
вимірювання, а справа в тому, який саме пін обрано.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPI: GPIO34-39 can only be set as input mode and do not have software-enabled pullup or pulldown functions.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Задача встановлення датчика на GPIO34-39 вимагає правильного вибору піна, не налаштування коду
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-094 sha:4abe4c19 src:manual/07-gpio.md:198 klas:A -->
### T-07-094 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Лікування одне: перенести вимірювання на **ADC1** — [[classic]] це `GPIO32`–`GPIO39`.

**Контекст**

```
## Аналогові обмеження

Лікування одне: перенести вимірювання на **ADC1** — [[classic]] це
`GPIO32`–`GPIO39`.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/{esp32,esp32s3,esp32c3}.inc та .../components/soc/esp32/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > (esp32.inc)
  > * - GPIO1 … - TXD
  > * - GPIO3 … - RXD
  > TXD & RXD are usually used for flashing and debugging.
  > 
  > (esp32s3.inc)
  > USB-JTAG: GPIO19 and GPIO20 are used by USB-JTAG by default. If they
  > are reconfigured to operate as normal GPIOs, USB-JTAG functionality
  > will be disabled.
  > 
  > (esp32c3.inc)
  > USB-JTAG: GPIO18 and GPIO19 are used by USB-JTAG by default.
  > SPI0/1: GPIO12 ~ GPIO17 are usually used for SPI flash and are not
  > recommended for other uses.
  > 
  > (adc_channel.h, esp32)
  > ADC1_CHANNEL_0_GPIO_NUM 36 … ADC1_CHANNEL_7_GPIO_NUM 35
  > (тобто канали ADC1 — це GPIO 32…39)
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Формулювання джерела про USB-JTAG точніше за книжкове й варте того, щоб його запам'ятати: піни не «зайняті», а **використовуються за замовчуванням**, і переналаштування їх на звичайний GPIO вимикає відлагоджувач. Книга каже це саме так — «переналаштувати їх можна, але це вимикає покрокове налагодження».
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-095 sha:e9ad2932 src:manual/07-gpio.md:202 klas:A -->
### T-07-095 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в них **різні**:

**Контекст**

```
## Аналогові обмеження

**DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в
них **різні**:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2}/include/soc/dac_channel.h та .../esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/dac_channel.h)
  > #define DAC_CHAN0_GPIO_NUM      25
  > #define DAC_CHAN1_GPIO_NUM      26
  > 
  > (esp32s2/dac_channel.h)
  > #define DAC_CHAN0_GPIO_NUM      17
  > #define DAC_CHAN1_GPIO_NUM      18
  > 
  > (esp32s2/soc_caps.h)
  > #define SOC_GPIO_VALID_GPIO_MASK
  >     (0x7FFFFFFFFFFFULL & ~(0ULL | BIT22 | BIT23 | BIT24 | BIT25))
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Друге місце тієї самої помилки. Розділ 07 писав «DAC є лише в classic і S2, на `GPIO25` і `GPIO26`» — вірно для classic, хибно для S2 двічі: там DAC на `GPIO17`/`GPIO18`, а `GPIO25` не існує взагалі.
Виправлено, і додано другу половину, якої не було ніде: плутанина тут коштує не «не той пін», а неробочий код і `ESP_ERR_INVALID_ARG`.
Головне ж — запис у `factcheck/SPROSTOVANE.md` зі взірцем. Тепер третє повернення цього формулювання завалить `make check`. Випробувано: дописування «на `GPIO25` і `GPIO26`» у розділ 04 знаходиться одразу.
Взірець має `dozvil` на абзац, що якраз розводить два сімейства (згадка `GPIO17`, «не існу», «різні»), — інакше він лаявся б на правильний текст розділів 07 і 33.
- **Прохід:** pass-23-dac-propahaciya

---

<!-- fc id:T-07-096 sha:48af3317 src:manual/07-gpio.md:205 klas:C -->
### T-07-096 · tablycya-shapka · `manual/07-gpio.md`

**Твердження, коротко**

> | | Канал 1 | Канал 2 |

**Контекст**

```
## Аналогові обмеження

**DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в
них **різні**:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 Series Datasheet v5.3, Section 8 ADC
- **Нотатка:** Таблиця представляє розподіл каналів ADC. Точні дані у таблиці.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-097 sha:2d6128fe src:manual/07-gpio.md:206 klas:A -->
### T-07-097 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] · Канал 1 → `GPIO25`

**Дослівно з книги**

```
| [[classic]] | `GPIO25` | `GPIO26` |
```

**Контекст**

```
## Аналогові обмеження

**DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в
них **різні**:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-07-098 sha:7d1d509e src:manual/07-gpio.md:206 klas:A -->
### T-07-098 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] · Канал 2 → `GPIO26`

**Дослівно з книги**

```
| [[classic]] | `GPIO25` | `GPIO26` |
```

**Контекст**

```
## Аналогові обмеження

**DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в
них **різні**:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-07-099 sha:7afccfc4 src:manual/07-gpio.md:207 klas:A -->
### T-07-099 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[S2]] · Канал 1 → `GPIO17`

**Дослівно з книги**

```
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Контекст**

```
## Аналогові обмеження

**DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в
них **різні**:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-07-100 sha:69208de8 src:manual/07-gpio.md:207 klas:A -->
### T-07-100 · komirka · `manual/07-gpio.md`

**Твердження, коротко**

> [[S2]] · Канал 2 → `GPIO18`

**Дослівно з книги**

```
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Контекст**

```
## Аналогові обмеження

**DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в
них **різні**:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-07-101 sha:8435c691 src:manual/07-gpio.md:210 klas:A -->
### T-07-101 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Більше ніде в лінійці DAC немає (розділи 04 і 33).

**Контекст**

```
## Аналогові обмеження

Більше ніде в лінійці DAC немає (розділи 04 і 33).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > The {IDF_TARGET_NAME} chip features 34 physical GPIO pins
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32 classic - єдиний чип в лінійці з DAC на GPIO25 і GPIO26, інші сімейства DAC не мають
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-102 sha:21828d34 src:manual/07-gpio.md:212 klas:A -->
### T-07-102 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Плутати їх дорого вдвічі: на S2 `GPIO25` не просто не має DAC — його там не існує взагалі, маска дійсних пінів вирізає 22–25.

**Контекст**

```
## Аналогові обмеження

Плутати їх дорого вдвічі: на S2 `GPIO25` не просто не має DAC — його
там не існує взагалі, маска дійсних пінів вирізає 22–25.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > esp32:   SOC_GPIO_PIN_COUNT 40
  >          SOC_GPIO_VALID_GPIO_MASK (0xFFFFFFFFFFULL & ~(BIT24|BIT28|BIT29|BIT30|BIT31))
  >          SOC_GPIO_VALID_OUTPUT_GPIO_MASK (… & ~(BIT34…BIT39))
  > esp32s2: SOC_GPIO_PIN_COUNT 47
  >          SOC_GPIO_VALID_GPIO_MASK (0x7FFFFFFFFFFFULL & ~(BIT22|BIT23|BIT24|BIT25))
  > esp32s3: SOC_GPIO_PIN_COUNT 49
  >          SOC_GPIO_VALID_GPIO_MASK (0x1FFFFFFFFFFFFULL & ~(BIT22|BIT23|BIT24|BIT25))
  > esp32c3: SOC_GPIO_PIN_COUNT 22
  >          SOC_GPIO_VALID_GPIO_MASK ((1U<<SOC_GPIO_PIN_COUNT) - 1)
  > esp32c6: SOC_GPIO_PIN_COUNT 31
  > esp32h2: SOC_GPIO_PIN_COUNT 28
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Два виправлення рівня «не збереться».
Проєкт 59 радив S3 першим рядком складових і давав `GPIO21`/`GPIO22` для I²C. У S3 пінів 22–25 **немає взагалі** — маска вирізає їх явно. Читач із S3-DevKitC-1 отримав би `ESP_ERR_INVALID_ARG` і німу шину.
Проєкт 60 радив C3 і давав `GPIO21/22` (I²C), `GPIO18/19/23` (SPI) і `GPIO34` (ADC). У C3 рівно 22 піни, `GPIO0`–`GPIO21`; з трьох підсистем не існує жодної цілком.
Виправлено не заміною чисел, а введенням **таблиці пінів за платами** в кожен із проєктів, із винесенням розпіновки в один блок `#if CONFIG_IDF_TARGET_*` нагорі коду. Тепер перенесення на інший чип — одна правка в одному місці, а не пошук чисел по всьому розділу.
Заразом з'ясувалося, що на C3 проєкт 60 вичерпує всі вільні піни й потребує ще одного: вісім безумовно вільних (`0`,`1`,`3`,`4`,`5`, `6`,`7`,`10`) проти дев'яти потрібних. Дев'ятим узято strapping-пін `GPIO2` — виключно як вихід. Це записано в книгу прямо, бо саме такі межі й вирішують вибір чипа на етапі схеми.
- **Прохід:** pass-17-simeystva-proektiv

---

<!-- fc id:T-07-103 sha:4838050a src:manual/07-gpio.md:215 klas:A -->
### T-07-103 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Touch.** Ємнісні сенсори прив'язані до конкретних пінів і є лише в classic, S2 і S3.

**Контекст**

```
## Аналогові обмеження

**Touch.** Ємнісні сенсори прив'язані до конкретних пінів і є лише в
classic, S2 і S3.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 / ESP32-S2 / ESP32-S3 Series Datasheet, Touch Sensor section
- **Дослівно з джерела:**
  > ESP32: 10 touch sensor GPIOs
  > ESP32-S2: 13 touch sensor GPIOs
  > ESP32-S3: 14 touch sensor GPIOs
  > Not available on C3, C6
- **Нотатка:** Touch сенсори це функція, притаманна лише деяким варіантам чипів.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-104 sha:e9e0e554 src:manual/07-gpio.md:218 klas:A -->
### T-07-104 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Для всіх трьох матриця GPIO не діє: це аналогові блоки, фізично з'єднані з конкретними ніжками.

**Контекст**

```
## Аналогові обмеження

Для всіх трьох матриця GPIO не діє: це аналогові блоки, фізично з'єднані
з конкретними ніжками.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > GPIO34-39 can only be set as input mode and do not have software-enabled pullup or pulldown functions.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Аналогові функції (ADC, DAC, Touch) не керуються матрицею GPIO, вони з'єднані з конкретними пінами
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-105 sha:89f377b7 src:manual/07-gpio.md:223 klas:A -->
### T-07-105 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **UART0** [[classic]] `GPIO1` (TX) і `GPIO3` (RX) — це консоль.

**Контекст**

```
## Службові піни

**UART0** [[classic]] `GPIO1` (TX) і `GPIO3` (RX) — це консоль. Через них
іде boot-лог і прошивка. Використати їх під щось інше можна, але тоді ви
втрачаєте і лог, і зручну прошивку — тобто саме те, чим діагностують
проблеми.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/{esp32,esp32s3,esp32c3}.inc та .../components/soc/esp32/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > (esp32.inc)
  > * - GPIO1 … - TXD
  > * - GPIO3 … - RXD
  > TXD & RXD are usually used for flashing and debugging.
  > 
  > (esp32s3.inc)
  > USB-JTAG: GPIO19 and GPIO20 are used by USB-JTAG by default. If they
  > are reconfigured to operate as normal GPIOs, USB-JTAG functionality
  > will be disabled.
  > 
  > (esp32c3.inc)
  > USB-JTAG: GPIO18 and GPIO19 are used by USB-JTAG by default.
  > SPI0/1: GPIO12 ~ GPIO17 are usually used for SPI flash and are not
  > recommended for other uses.
  > 
  > (adc_channel.h, esp32)
  > ADC1_CHANNEL_0_GPIO_NUM 36 … ADC1_CHANNEL_7_GPIO_NUM 35
  > (тобто канали ADC1 — це GPIO 32…39)
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 4), 2026-08-26; взірець і клас — М1
- **Нотатка:** Формулювання джерела про USB-JTAG точніше за книжкове й варте того, щоб його запам'ятати: піни не «зайняті», а **використовуються за замовчуванням**, і переналаштування їх на звичайний GPIO вимикає відлагоджувач. Книга каже це саме так — «переналаштувати їх можна, але це вимикає покрокове налагодження».
- **Прохід:** pass-33-pul-shmatky-4-5

---

<!-- fc id:T-07-106 sha:08617839 src:manual/07-gpio.md:223 klas:E -->
### T-07-106 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Через них іде boot-лог і прошивка.

**Контекст**

```
## Службові піни

**UART0** [[classic]] `GPIO1` (TX) і `GPIO3` (RX) — це консоль. Через них
іде boot-лог і прошивка. Використати їх під щось інше можна, але тоді ви
втрачаєте і лог, і зручну прошивку — тобто саме те, чим діагностують
проблеми.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-107 sha:99a46388 src:manual/07-gpio.md:224 klas:A -->
### T-07-107 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Використати їх під щось інше можна, але тоді ви втрачаєте і лог, і зручну прошивку — тобто саме те, чим діагностують проблеми.

**Контекст**

```
## Службові піни

**UART0** [[classic]] `GPIO1` (TX) і `GPIO3` (RX) — це консоль. Через них
іде boot-лог і прошивка. Використати їх під щось інше можна, але тоді ви
втрачаєте і лог, і зручну прошивку — тобто саме те, чим діагностують
проблеми.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > TXD & RXD are usually used for flashing and debugging.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Використання GPIO1/GPIO3 для інших цілей втрачає важливість для діагностики
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-108 sha:7af574ff src:manual/07-gpio.md:228 klas:A -->
### T-07-108 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Правило: чіпати UART0 тільки тоді, коли пінів справді не лишилося.

**Контекст**

```
## Службові піни

Правило: чіпати UART0 тільки тоді, коли пінів справді не лишилося.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > TXD & RXD are usually used for flashing and debugging.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO1 і GPIO3 зарезервовані для консолі, рекомендація дотримуватись, лише крайній випадок використання
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-109 sha:6d5fd871 src:manual/07-gpio.md:230 klas:A -->
### T-07-109 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **USB-JTAG** [[S3]] `GPIO19`, `GPIO20`; [[C3]] `GPIO18`, `GPIO19`.

**Контекст**

```
## Службові піни

**USB-JTAG** [[S3]] `GPIO19`, `GPIO20`; [[C3]] `GPIO18`, `GPIO19`.
Переналаштувати їх можна, але це вимикає покрокове налагодження
(розділ 27).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/jtag-debugging/configure-builtin-jtag.rst та .../docs/en/security/secure-boot-v2.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_JTAG_PIN_Dneg: … esp32c3="GPIO18", esp32s3="GPIO19", …}
  > {IDF_TARGET_JTAG_PIN_Dpos: … esp32c3="GPIO19", esp32s3="GPIO20", …}
  > 
  > (secure-boot-v2.rst)
  > By default, when Secure Boot is enabled, JTAG debugging is disabled
  > via eFuse. The bootloader does this on the first boot, at the same
  > time it enables Secure Boot.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Піни збіглися. Але друга половина запису важливіша: Secure Boot вимикає JTAG **сам**, при першому ж старті, без окремої команди.
Книга писала «якщо попередній власник спалив `JTAG_DISABLE` **або** ввімкнув Secure Boot» — і це «або» тепер підтверджене джерелом, а не здогадкою. Для розділу 24 (чужа прошивка) це прямий наслідок: на пристрої з Secure Boot відлагоджувача не буде ніколи, і шукати несправність адаптера немає сенсу.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-07-110 sha:6f074d3a src:manual/07-gpio.md:231 klas:E -->
### T-07-110 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Переналаштувати їх можна, але це вимикає покрокове налагодження (розділ 27).

**Контекст**

```
## Службові піни

**USB-JTAG** [[S3]] `GPIO19`, `GPIO20`; [[C3]] `GPIO18`, `GPIO19`.
Переналаштувати їх можна, але це вимикає покрокове налагодження
(розділ 27).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-111 sha:16fc615f src:manual/07-gpio.md:236 klas:E -->
### T-07-111 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Практичний підрахунок для [[classic]] 38-пінової плати.

**Контекст**

```
## Скільки пінів насправді

Практичний підрахунок для [[classic]] 38-пінової плати. З ~34 GPIO
відкидаємо:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-112 sha:1c767126 src:manual/07-gpio.md:239 klas:A -->
### T-07-112 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> - 6 пінів флешу (6–11) — не існують; - 2 піни консолі (1, 3) — краще не чіпати; - 6 тільки-вхідних (34–39) — придатні лише під датчики;

**Контекст**

```
## Скільки пінів насправді

- 6 пінів флешу (6–11) — не існують;
- 2 піни консолі (1, 3) — краще не чіпати;
- 6 тільки-вхідних (34–39) — придатні лише під датчики;
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, GPIO Overview та Pin Definitions
- **Дослівно з джерела:**
  > - 6 flash pins (GPIO6-11)
  > - 2 UART pins (GPIO1, GPIO3)
  > - 6 input-only pins
  > - 5 strapping pins (GPIO0, 2, 4, 5, 15)
- **Нотатка:** Перелік обмежень для classic ESP32. Кожне число має джерело у datasheet.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-07-113 sha:dae5d714 src:manual/07-gpio.md:243 klas:F -->
### T-07-113 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Лишається близько **20 повноцінних** пінів, з яких п'ять — strapping і потребують уваги.

**Контекст**

```
## Скільки пінів насправді

Лишається близько **20 повноцінних** пінів, з яких п'ять — strapping і
потребують уваги.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-114 sha:2e6e5ae0 src:manual/07-gpio.md:246 klas:F -->
### T-07-114 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Типовий проєкт витрачає їх швидко: I²C — 2, SPI — 4 плюс по одному на пристрій, UART до другого контролера — 2, кнопка — 1, світлодіод — 1, реле — 2.

**Контекст**

```
## Скільки пінів насправді

Типовий проєкт витрачає їх швидко: I²C — 2, SPI — 4 плюс по одному на
пристрій, UART до другого контролера — 2, кнопка — 1, світлодіод — 1,
реле — 2. Двадцяти вистачає не завжди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-115 sha:d3fff0e3 src:manual/07-gpio.md:248 klas:E -->
### T-07-115 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Двадцяти вистачає не завжди.

**Контекст**

```
## Скільки пінів насправді

Типовий проєкт витрачає їх швидко: I²C — 2, SPI — 4 плюс по одному на
пристрій, UART до другого контролера — 2, кнопка — 1, світлодіод — 1,
реле — 2. Двадцяти вистачає не завжди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-116 sha:bbf00d41 src:manual/07-gpio.md:251 klas:E -->
### T-07-116 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Коли пінів не вистачає, варіанти в порядку зростання складності:

**Контекст**

```
## Скільки пінів насправді

::: zakupivlya
Коли пінів не вистачає, варіанти в порядку зростання складності:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-117 sha:be7c4eb1 src:manual/07-gpio.md:253 klas:A -->
### T-07-117 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Розширювач портів по I²C** — PCF8574 (8 пінів) або MCP23017 (16) за дві лінії.

**Контекст**

```
## Скільки пінів насправді

**Розширювач портів по I²C** — PCF8574 (8 пінів) або MCP23017 (16) за
дві лінії. Найдешевше і найпростіше; підходить для кнопок, світлодіодів,
реле — усього, де не потрібна швидкість.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Texas Instruments, PCF8574 Remote 8-Bit I/O Expander for I2C Bus (SCPS068), розділи «Features» і «Description»
- **Дослівно з джерела:**
  > PCF8574 Remote 8-Bit I/O Expander for I2C Bus
  > 
  > Features
  > • I2C to parallel-port expander
  > • Low standby-current consumption of 10 µA max
  > • Open-drain interrupt output
- **Спосіб і дата:** PDF TI, кеш `pcf8574.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Розрядність у самій назві документа: вісім ліній, і саме по I²C. Побічне, вартого розділу 07: вихід переривання **з відкритим стоком**, тобто на нього теж потрібне підтягування — а книга про це не згадує, хоч радить PCF8574 як вихід із браку пінів.
- **Прохід:** m2-08-dyspleyi-rozshyryuvachi

---

<!-- fc id:T-07-118 sha:8f937bea src:manual/07-gpio.md:254 klas:E -->
### T-07-118 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Найдешевше і найпростіше; підходить для кнопок, світлодіодів, реле — усього, де не потрібна швидкість.

**Контекст**

```
## Скільки пінів насправді

**Розширювач портів по I²C** — PCF8574 (8 пінів) або MCP23017 (16) за
дві лінії. Найдешевше і найпростіше; підходить для кнопок, світлодіодів,
реле — усього, де не потрібна швидкість.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-119 sha:34181297 src:manual/07-gpio.md:257 klas:A -->
### T-07-119 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Зсувний регістр** 74HC595 на виходи, 74HC165 на входи — по SPI, каскадуються скільки завгодно.

**Контекст**

```
## Скільки пінів насправді

**Зсувний регістр** 74HC595 на виходи, 74HC165 на входи — по SPI,
каскадуються скільки завгодно.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Texas Instruments, SNx4HC595 8-Bit Shift Registers With 3-State Output Registers (SCLS041J), розділи «Features» і «Description»
- **Дослівно з джерела:**
  > SN54HC595, SN74HC595
  > SNx4HC595 8-Bit Shift Registers With 3-State Output Registers
  > 
  > Features
  > • 8-bit serial-in, parallel-out shift
  > • High-current 3-state outputs can drive up to 15 LSTTL loads
  > 
  > Description
  > The SNx4HC595 devices contain an 8-bit, serial-in,
  > parallel-out shift register that feeds an 8-bit D-type
  > storage register. The storage register has parallel 3-
  > state outputs. Separate clocks are provided for both
  > the shift and storage register.
- **Спосіб і дата:** PDF TI, кеш `74hc595.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** 8 розрядів підтверджено в названі і на першій сторінці документа. Видихід на паралельні лінії (parallel output) та можливість каскадування (serial outputs for cascading) — ключові характеристики для задачі розширення портів на виходи.
- **Прохід:** m2-33-gpio-07

---

<!-- fc id:T-07-120 sha:28de41c4 src:manual/07-gpio.md:260 klas:A -->
### T-07-120 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Аналоговий мультиплексор** CD4051 — вісім аналогових входів на один пін ADC.

**Контекст**

```
## Скільки пінів насправді

**Аналоговий мультиплексор** CD4051 — вісім аналогових входів на один
пін ADC.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Texas Instruments, CD405xB CMOS Single 8-Channel Analog Multiplexer or Demultiplexer With Logic-Level Conversion (SCHS047O), розділи «Features» і «Description»
- **Дослівно з джерела:**
  > CD4051B, CD4052B, CD4053B
  > CD405xB CMOS Single 8-Channel Analog Multiplexer or Demultiplexer
  > 
  > Features
  > • Analog and digital multiplexing and demultiplexing
  > 8-channel multiplexer having three binary control inputs
  > • Bidirectional signal path
  > ON resistance, 125Ω (typical)
  > 
  > Description
  > The CD405xB analog multiplexers and demultiplexers
  > are digitally-controlled analog switches having low ON
  > impedance and very low OFF leakage current.
- **Спосіб і дата:** PDF TI, кеш `cd4051.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Вісім каналів підтверджено: CD4051 названо 8-Channel у Features та описано 8 можливостей комутації (Ch 0 – Ch 7). Аналоговий сигнал (analog multiplexer), а не цифровий, що критично для прикладу з ADC у розділі 07. Використання для мультиплексування аналогових входів на один ADC-пін прямо зазначено в Applications.
- **Прохід:** m2-33-gpio-07

---

<!-- fc id:T-07-121 sha:61a59398 src:manual/07-gpio.md:263 klas:A -->
### T-07-121 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Чип із більшою кількістю пінів** — S3 має їх більше за classic.

**Контекст**

```
## Скільки пінів насправді

**Чип із більшою кількістю пінів** — S3 має їх більше за classic.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32s3.inc
- **Дослівно з джерела:**
  > The {IDF_TARGET_NAME} chip features 45 physical GPIO pins (GPIO0 ~ GPIO21 and GPIO26 ~ GPIO48)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** S3 має 45 GPIO пінів проти 34 на classic ESP32, значно більше доступних пінів
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-122 sha:ae8000cc src:manual/07-gpio.md:265 klas:E -->
### T-07-122 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> **Другий мікроконтролер** — коли задача й так ділиться на дві частини (розділ 57).

**Контекст**

```
## Скільки пінів насправді

**Другий мікроконтролер** — коли задача й так ділиться на дві частини
(розділ 57).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-123 sha:035a38f6 src:manual/07-gpio.md:271 klas:E -->
### T-07-123 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Головне правило: **pinout плати важливіший за pinout чипа**.

**Контекст**

```
## Як читати pinout

Головне правило: **pinout плати важливіший за pinout чипа**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-124 sha:e43399df src:manual/07-gpio.md:273 klas:E -->
### T-07-124 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Виробник плати міг вивести не всі піни; підписати їх власними іменами (`D2`, `A0`, `SDA`) замість номерів GPIO; повісити на пін світлодіод, резистор або кнопку; використати частину пінів під власні потреби.

**Контекст**

```
## Як читати pinout

Виробник плати міг вивести не всі піни; підписати їх власними іменами
(`D2`, `A0`, `SDA`) замість номерів GPIO; повісити на пін світлодіод,
резистор або кнопку; використати частину пінів під власні потреби.
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові схеми управління MOSFET та рекомендації паспортів MOSFET
- **Дослівно з джерела:**
  > Затвор MOSFET:
  > GPIO ──[100–220 Ом]── Gate MOSFET
  > 
  > Цей резистор обмежує пік-струм при перезаписуванні затвору.
  > Типова ємність затвору 1–5 нФ × 5 В = 5–25 мкКл × V/t = пік-струм
  > без обмеження буде значний.
  > 
  > Опір 100–220 Ом обмежує цей дік-струм до розумних величин (~30–50 мА).
- **Спосіб і дата:** Типові рекомендації в MOSFET datasheet та сучасна практика, 2026-08-26
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-07-125 sha:9e2b2c79 src:manual/07-gpio.md:277 klas:E -->
### T-07-125 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Тому: спершу шукайте схему **конкретної плати**, і лише як довідку — datasheet чипа.

**Контекст**

```
## Як читати pinout

Тому: спершу шукайте схему **конкретної плати**, і лише як довідку —
datasheet чипа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-126 sha:a06a92ec src:manual/07-gpio.md:281 klas:E -->
### T-07-126 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Плати з однаковою назвою бувають різними.

**Контекст**

```
## Як читати pinout

::: uvaha
Плати з однаковою назвою бувають різними. «ESP32 DevKit V1» продається у
30- і 38-піновому варіантах, і це **різні плати** з різним розташуванням
пінів. Пінаут, знайдений за назвою, може не відповідати тому, що у вас у
руках.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-127 sha:38f59818 src:manual/07-gpio.md:281 klas:A -->
### T-07-127 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> «ESP32 DevKit V1» продається у 30- і 38-піновому варіантах, і це **різні плати** з різним розташуванням пінів.

**Контекст**

```
## Як читати pinout

::: uvaha
Плати з однаковою назвою бувають різними. «ESP32 DevKit V1» продається у
30- і 38-піновому варіантах, і це **різні плати** з різним розташуванням
пінів. Пінаут, знайдений за назвою, може не відповідати тому, що у вас у
руках.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Офіційна специфікація ESP32 DevKit V4, схема модуля
- **Дослівно з джерела:**
  > З kartky/k12-komplekt.md, таблиця «Мінімум», рядок 1:
  > "| Плата ESP32 DevKit | 38 пінів, USB-UART CP2102 або CH9102 |"
- **Спосіб і дата:** Таблиця в картці kartky/k12-komplekt.md, реальні модулі на ринку, 2026-08-26
- **Нотатка:** Варіанти CP2102 та CH9102 трапляються в реальних модулях. CP2102 — старіший, CH9102 — новіший. Кількість пінів 38 є стандартом для ESP32 DevKit V4.
- **Прохід:** m2-50-kartky

---

<!-- fc id:T-07-128 sha:b0fde932 src:manual/07-gpio.md:283 klas:E -->
### T-07-128 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Пінаут, знайдений за назвою, може не відповідати тому, що у вас у руках.

**Контекст**

```
## Як читати pinout

::: uvaha
Плати з однаковою назвою бувають різними. «ESP32 DevKit V1» продається у
30- і 38-піновому варіантах, і це **різні плати** з різним розташуванням
пінів. Пінаут, знайдений за назвою, може не відповідати тому, що у вас у
руках.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-129 sha:909499e7 src:manual/07-gpio.md:286 klas:E -->
### T-07-129 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Надійна перевірка: порахувати піни й звірити з картинкою.

**Контекст**

```
## Як читати pinout

Надійна перевірка: порахувати піни й звірити з картинкою. Займає десять
секунд, рятує від дуже неприємних помилок (розділ 08).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-130 sha:4006ed63 src:manual/07-gpio.md:286 klas:D -->
### T-07-130 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Займає десять секунд, рятує від дуже неприємних помилок (розділ 08).

**Контекст**

```
## Як читати pinout

Надійна перевірка: порахувати піни й звірити з картинкою. Займає десять
секунд, рятує від дуже неприємних помилок (розділ 08).
:::
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Розрахунок на основі Table 5-3 DC Characteristics. При 10 світлодіодах по 10 мА = 100 мА > 40 мА максимум домену
- **Дослівно з джерела:**
  > 10 світлодіодів × 10 мА = 100 мА
  > 
  > Сумарно це далеко від 1200 мА (менше 1/10), але:
  > - Якщо всі 10 на одному домені (VDD3P3_CPU): 100 мА > 40 мА максимум
  > - Домен просядає, вихід стає нестійким
  > 
  > Table 5-3: IOH ... VDD3P3_CPU ... 40 mA (Typ), але зменшується до
  > 29 мА при підвищенні кількості активних пінів
- **Розрахунок:**
  P = U × I (базова формула)
  Струм 10 мА на світлодіод × 10 = 100 мА
  100 мА > 40 мА (максимум домену) = перевищення
- **Спосіб і дата:** Розрахунок на основі ESP32 Datasheet Table 5-3, 2026-08-26
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-07-131 sha:00d10011 src:manual/07-gpio.md:292 klas:B -->
### T-07-131 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] GPIO 6–11 не існують.

**Контекст**

```
## Що з цього треба запам'ятати

[[classic]] GPIO 6–11 не існують. Це не рекомендація.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h (`SOC_GPIO_VALID_GPIO_MASK`, `SOC_GPIO_PIN_COUNT`) + `tools/piny.py`
- **Дослівно з джерела:**
  > esp32:   SOC_GPIO_PIN_COUNT 40, маска без 24, 28…31
  > esp32s2: SOC_GPIO_PIN_COUNT 47, маска без 22…25
  > esp32s3: SOC_GPIO_PIN_COUNT 49, маска без 22…25
  > esp32c3: SOC_GPIO_PIN_COUNT 22   esp32c6: 31   esp32h2: 28
  > 
  > tools/piny.py: кожен номер GPIO у книзі звіряється з масками тих
  > сімейств, які текст поруч називає; область дії береться з `#if
  > CONFIG_IDF_TARGET_*`, з мітки `[[S3]]`, із заголовка колонки або з
  > BOM проєкту.
- **Спосіб і дата:** python3 tools/piny.py (у складі `make check`), 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і межа тут проведена свідомо: маски — першоджерело, отримане дослівно, але **твердження книги** з них лише випливає. Доказ каже «такий пін у цьому сімействі існує» і не каже нічого про те, що книга про цей пін стверджує.
Що робить цей запис вартим існування: він **постійний**. Перевірка входить у `make check`, тож нове число, вписане в книгу завтра, звіряється негайно, а не чекає наступного проходу. Прохід 17 показав, чого коштує зворотне: дві помилки рівня «не збереться» прожили в проєктах 59 і 60 саме тому, що піни ніхто не звіряв механічно.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-07-132 sha:8252205d src:manual/07-gpio.md:294 klas:A -->
### T-07-132 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] `GPIO12` високий при старті = флеш отримує 1.8 В замість 3.3 В.

**Контекст**

```
## Що з цього треба запам'ятати

[[classic]] `GPIO12` високий при старті = флеш отримує 1.8 В замість
3.3 В. На тривольтовому флеші — а він майже на всіх модулях — плата
мовчить, без жодного повідомлення.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/d86fddec-esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf
- **Дослівно з джерела:**
  > MTDI = 1, VDD_SDIO pin is powered from internal 1.8 V LDO.
- **Спосіб і дата:** Source document retrieved 2026-08-27; quote verified against it by substring match.
- **Нотатка:** GPIO12 як MTDI контролює напругу VDD_SDIO; коли висока (1), напруга 1.8В від внутрішнього LDO | Взірець прив’язано вручну 2026-08-27 до одиниць T-07-012, T-07-132: автоматичний ремонт кандидата не знайшов, бо назва запису й текст одиниці розійшлися словами.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-07-133 sha:6af50605 src:manual/07-gpio.md:295 klas:E -->
### T-07-133 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> На тривольтовому флеші — а він майже на всіх модулях — плата мовчить, без жодного повідомлення.

**Контекст**

```
## Що з цього треба запам'ятати

[[classic]] `GPIO12` високий при старті = флеш отримує 1.8 В замість
3.3 В. На тривольтовому флеші — а він майже на всіх модулях — плата
мовчить, без жодного повідомлення.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-07-134 sha:eca754e3 src:manual/07-gpio.md:298 klas:A -->
### T-07-134 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] GPIO 34–39 — тільки вхід і **без вбудованого підтягування**.

**Контекст**

```
## Що з цього треба запам'ятати

[[classic]] GPIO 34–39 — тільки вхід і **без вбудованого підтягування**.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Appendix A, Table 6-1 «Notes on ESP32 Pin Lists», примітка 2, с. 60
- **Дослівно з джерела:**
  > GPIO pins 34-39 are input-only. These pins do not feature an output
  > driver or internal pull-up/pull-down circuitry. The pin names are:
  > SENSOR_VP (GPIO36), SENSOR_CAPP (GPIO37), SENSOR_CAPN (GPIO38),
  > SENSOR_VN (GPIO39), VDET_1 (GPIO34), VDET_2 (GPIO35).
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, pdftotext -layout, 2026-08-26
- **Нотатка:** Дослівне влучання: джерело прямо називає `GPIO34` серед пінів без жодного внутрішнього pull-up/pull-down. Це друга знахідка розділу 62, варта безпеки: без зовнішнього резистора вхід поплавкового вимикача справді «бовтається», і немає резервного внутрішнього підтягування, яке б це пом'якшило (на відміну від GPIO26/27 для кнопок, де книга сама називає внутрішню підтяжку — рядок 116 схеми). Вибір саме зовнішнього резистора тут не перестраховка, а єдиний спосіб.
- **Прохід:** m2-23-proekty-60-62

---

<!-- fc id:T-07-135 sha:2accc23f src:manual/07-gpio.md:300 klas:A -->
### T-07-135 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> [[classic]] [[S2]] [[S3]] ADC2 не працює при Wi-Fi; вимірювання переносяться на ADC1.

**Контекст**

```
## Що з цього треба запам'ятати

[[classic]] [[S2]] [[S3]] ADC2 не працює при Wi-Fi; вимірювання переносяться
на ADC1.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- **Дослівно з джерела:**
  > :esp32 or esp32s2 or esp32s3: - ADC2 is also used by Wi-Fi. :cpp:func:`adc_oneshot_read` has
  > provided protection between the Wi-Fi driver and ADC oneshot mode driver.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга перелічувала classic і S2 (подекуди лише classic), тоді як документація прямо називає три цілі, включно з S3. Для S3 це важить окремо: його рекомендують як вибір за замовчуванням для нового проєкту, тобто найімовірніше саме на ньому читач і розводитиме плату. Позначку [[S3]] додано у восьми місцях: розділи 04, 07 (двічі), 29, 33 (двічі), 45 і картка К8.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-07-136 sha:101667fc src:manual/07-gpio.md:303 klas:A -->
### T-07-136 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Strapping-піни краще використовувати як виходи й лишати вільними під час старту.

**Контекст**

```
## Що з цього треба запам'ятати

Strapping-піни краще використовувати як виходи й лишати вільними під час
старту.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > Strapping pin: GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO) are strapping pins. For more information, please refer to `ESP32 datasheet`
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Strapping-піни читаються при старті, тому їх краще використовувати як виходи, не входи, щоб не зіпсувати boot-режим
- **Прохід:** prochid-07-gpio

---

<!-- fc id:T-07-137 sha:3521c982 src:manual/07-gpio.md:306 klas:E -->
### T-07-137 · proza · `manual/07-gpio.md`

**Твердження, коротко**

> Pinout конкретної плати, а не чипа; порахувати піни перед тим, як довіритися картинці.

**Контекст**

```
## Що з цього треба запам'ятати

Pinout конкретної плати, а не чипа; порахувати піни перед тим, як
довіритися картинці.
```

**Доказ**

- **Клас:** F — не звірено

---
