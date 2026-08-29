# Фактчекінг: `kartky/k04-boot.md`

Одиниць твердження: **25**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-K04-001 sha:d392369e src:kartky/k04-boot.md:3 klas:E -->
### T-K04-001 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Плата не переходить у режим прошивки сама.

**Контекст**

```
# К4. Download mode вручну (BOOT + EN) {#k-boot}

Плата не переходить у режим прошивки сама. Це нормальна ситуація для
частини плат, а не ознака несправності.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-002 sha:8324cf6d src:kartky/k04-boot.md:3 klas:E -->
### T-K04-002 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Це нормальна ситуація для частини плат, а не ознака несправності.

**Контекст**

```
# К4. Download mode вручну (BOOT + EN) {#k-boot}

Плата не переходить у режим прошивки сама. Це нормальна ситуація для
частини плат, а не ознака несправності.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-003 sha:957a85b7 src:kartky/k04-boot.md:8 klas:E -->
### T-K04-003 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Щоб прийняти прошивку, чип має стартувати не в застосунок, а в ROM-бутлоадер.

**Контекст**

```
## Що таке download mode

Щоб прийняти прошивку, чип має стартувати не в застосунок, а в
ROM-бутлоадер. Вибір робиться **в момент скидання** за станом
strapping-піна.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-004 sha:3285d7ba src:kartky/k04-boot.md:9 klas:F -->
### T-K04-004 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Вибір робиться **в момент скидання** за станом strapping-піна.

**Контекст**

```
## Що таке download mode

Щоб прийняти прошивку, чип має стартувати не в застосунок, а в
ROM-бутлоадер. Вибір робиться **в момент скидання** за станом
strapping-піна.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-005 sha:7fb043c1 src:kartky/k04-boot.md:12 klas:B -->
### T-K04-005 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> [[classic]] [[S3]] Вирішує `GPIO0`:

**Контекст**

```
## Що таке download mode

[[classic]] [[S3]] Вирішує `GPIO0`:
```

**Доказ**

- **Статус:** derived — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst (Select Bootloader Mode, Automatic Bootloader)
- **Дослівно з джерела:**
  > The {chip} will enter the serial bootloader when {STRAP_BOOT_GPIO} is
  > held low on reset. Otherwise it will run the program in flash.
  > 
  > {STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left
  > unconnected then it will pull high.
  > 
  > Many boards use a button marked "Flash" (or "BOOT" on some Espressif
  > development boards) that pulls {STRAP_BOOT_GPIO} low when pressed.
  > 
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-006 sha:0c221230 src:kartky/k04-boot.md:14 klas:B -->
### T-K04-006 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> - `GPIO0` вільний (підтягнутий вгору) → звичайний старт застосунку; - `GPIO0` притиснутий до землі → download mode.

**Контекст**

```
## Що таке download mode

- `GPIO0` вільний (підтягнутий вгору) → звичайний старт застосунку;
- `GPIO0` притиснутий до землі → download mode.
```

**Доказ**

- **Статус:** derived — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > 0x10  - GPIO0
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep GPIO0, 2026-08-26
- **Нотатка:** Текст називає GPIO0 ключовим для режиму завантаження. Джерело показує GPIO0 з кодом 0x10. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flash

---

<!-- fc id:T-K04-007 sha:fcc462fe src:kartky/k04-boot.md:17 klas:A -->
### T-K04-007 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> [[C3]] Вирішує пара пінів: до землі притискається `GPIO9`, а `GPIO8` при цьому має лишатися високим.

**Контекст**

```
## Що таке download mode

[[C3]] Вирішує пара пінів: до землі притискається `GPIO9`, а `GPIO8` при
цьому має лишатися високим. Кнопка `BOOT` на платах C3 діє саме на
`GPIO9`, тому послідовність нижче не змінюється.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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

<!-- fc id:T-K04-008 sha:a007b94b src:kartky/k04-boot.md:18 klas:B -->
### T-K04-008 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Кнопка `BOOT` на платах C3 діє саме на `GPIO9`, тому послідовність нижче не змінюється.

**Контекст**

```
## Що таке download mode

[[C3]] Вирішує пара пінів: до землі притискається `GPIO9`, а `GPIO8` при
цьому має лишатися високим. Кнопка `BOOT` на платах C3 діє саме на
`GPIO9`, тому послідовність нижче не змінюється.
```

**Доказ**

- **Статус:** derived — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst (Select Bootloader Mode, Automatic Bootloader)
- **Дослівно з джерела:**
  > The {chip} will enter the serial bootloader when {STRAP_BOOT_GPIO} is
  > held low on reset. Otherwise it will run the program in flash.
  > 
  > {STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left
  > unconnected then it will pull high.
  > 
  > Many boards use a button marked "Flash" (or "BOOT" on some Espressif
  > development boards) that pulls {STRAP_BOOT_GPIO} low when pressed.
  > 
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-009 sha:055ab3de src:kartky/k04-boot.md:21 klas:B -->
### T-K04-009 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Кнопка `BOOT` (іноді `IO0`, `FLASH`) саме притискає `GPIO0` до землі.

**Контекст**

```
## Що таке download mode

Кнопка `BOOT` (іноді `IO0`, `FLASH`) саме притискає `GPIO0` до землі.
Кнопка `EN` (іноді `RST`, `RESET`) — скидання.
```

**Доказ**

- **Статус:** derived — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst (Select Bootloader Mode, Automatic Bootloader)
- **Дослівно з джерела:**
  > The {chip} will enter the serial bootloader when {STRAP_BOOT_GPIO} is
  > held low on reset. Otherwise it will run the program in flash.
  > 
  > {STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left
  > unconnected then it will pull high.
  > 
  > Many boards use a button marked "Flash" (or "BOOT" on some Espressif
  > development boards) that pulls {STRAP_BOOT_GPIO} low when pressed.
  > 
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-010 sha:d5503eea src:kartky/k04-boot.md:22 klas:F -->
### T-K04-010 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Кнопка `EN` (іноді `RST`, `RESET`) — скидання.

**Контекст**

```
## Що таке download mode

Кнопка `BOOT` (іноді `IO0`, `FLASH`) саме притискає `GPIO0` до землі.
Кнопка `EN` (іноді `RST`, `RESET`) — скидання.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-011 sha:f44d03d0 src:kartky/k04-boot.md:26 klas:B -->
### T-K04-011 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Порядок обов'язковий: стан `GPIO0` читається один раз, у момент відпускання скидання.

**Контекст**

```
## Послідовність

Порядок обов'язковий: стан `GPIO0` читається один раз, у момент відпускання
скидання.
```

**Доказ**

- **Статус:** derived — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst (Select Bootloader Mode, Automatic Bootloader)
- **Дослівно з джерела:**
  > The {chip} will enter the serial bootloader when {STRAP_BOOT_GPIO} is
  > held low on reset. Otherwise it will run the program in flash.
  > 
  > {STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left
  > unconnected then it will pull high.
  > 
  > Many boards use a button marked "Flash" (or "BOOT" on some Espressif
  > development boards) that pulls {STRAP_BOOT_GPIO} low when pressed.
  > 
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-012 sha:620a701f src:kartky/k04-boot.md:29 klas:F -->
### T-K04-012 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Натиснути і **тримати** `BOOT`. 2.

**Контекст**

```
## Послідовність

1. Натиснути і **тримати** `BOOT`.
2. Не відпускаючи `BOOT`, коротко натиснути й відпустити `EN`.
3. Зачекати півсекунди.
4. Відпустити `BOOT`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-013 sha:1b439fce src:kartky/k04-boot.md:30 klas:F -->
### T-K04-013 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Не відпускаючи `BOOT`, коротко натиснути й відпустити `EN`. 3.

**Контекст**

```
## Послідовність

1. Натиснути і **тримати** `BOOT`.
2. Не відпускаючи `BOOT`, коротко натиснути й відпустити `EN`.
3. Зачекати півсекунди.
4. Відпустити `BOOT`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-014 sha:83417cd4 src:kartky/k04-boot.md:34 klas:F -->
### T-K04-014 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Ознака успіху — у моніторі порту рядок виду `waiting for download`.

**Контекст**

```
## Послідовність

Ознака успіху — у моніторі порту рядок виду
`waiting for download`. Якщо монітор закритий, просто запустити прошивку:
вона має початися без «Failed to connect».
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-015 sha:b14933d1 src:kartky/k04-boot.md:35 klas:E -->
### T-K04-015 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Якщо монітор закритий, просто запустити прошивку: вона має початися без «Failed to connect».

**Контекст**

```
## Послідовність

Ознака успіху — у моніторі порту рядок виду
`waiting for download`. Якщо монітор закритий, просто запустити прошивку:
вона має початися без «Failed to connect».
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-016 sha:689b217f src:kartky/k04-boot.md:40 klas:A -->
### T-K04-016 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> На платі є схема, що смикає `GPIO0` і `EN` сигналами `DTR`/`RTS` USB-мосту.

**Контекст**

```
## Чому авторесет не спрацював

На платі є схема, що смикає `GPIO0` і `EN` сигналами `DTR`/`RTS` USB-мосту.
Вона не універсальна і не працює, коли:
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > esptool is not able to reset your hardware automatically in the
  > following cases:
  > - Your hardware does not have the ``DTR`` and ``RTS`` lines connected
  >   to ``{IDF_TARGET_STRAP_BOOT_GPIO}`` and ``EN`` (``CHIP_PU``)
  > - The ``DTR`` and ``RTS`` lines are configured differently
  > - There are no such serial control lines at all
  > 
  > (troubleshooting.rst)
  > If you have connected other devices to GPIO pins, try removing them
  > and see if esptool starts working.
  > Check the chip is receiving 3.3V from a stable power source.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Чотири з п'яти причин книги підтверджено дослівно. **П'ята — ні**, і це варте запису: «драйвер мосту не керує `DTR`/`RTS` (трапляється на CH9102 у Windows)».
Агент шукав `CH9102` у `troubleshooting.rst`, `boot-mode-selection.rst` і `reset.py` — немає ніде. Твердження не спростоване, воно **непідтверджене**: поведінка драйвера під Windows у документації esptool не описана й описана бути не може.
Лишаю в книзі як є, але позначаю тут: якщо колись знадобиться клас `A` на цей рядок, джерелом буде не esptool, а сам драйвер WCH або відтворення на живій машині. Це не наряд для М2 — це чесна межа того, що взагалі можна процитувати.
Побічно варте уваги: `troubleshooting.rst` радить те саме, що книга, у двох інших рядках — зняти сторонні пристрої з GPIO і перевірити стабільність 3.3 В. Тобто перелік книги не лише правильний, а й впорядкований так само, як у джерелі.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-K04-017 sha:e439e3fc src:kartky/k04-boot.md:41 klas:E -->
### T-K04-017 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Вона не універсальна і не працює, коли:

**Контекст**

```
## Чому авторесет не спрацював

На платі є схема, що смикає `GPIO0` і `EN` сигналами `DTR`/`RTS` USB-мосту.
Вона не універсальна і не працює, коли:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-018 sha:73f5ce2b src:kartky/k04-boot.md:43 klas:A -->
### T-K04-018 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> - на `GPIO0` або `GPIO2` навішано зовнішню обв'язку, яка їх утримує; - плата без такої схеми взагалі (голі модулі, частина клонів); - живлення просідає під час скидання — конденсатори не встигають; - драйвер мосту не керує `DTR`/`RTS` (трапляється на CH9102 у Windows).

**Контекст**

```
## Чому авторесет не спрацював

- на `GPIO0` або `GPIO2` навішано зовнішню обв'язку, яка їх утримує;
- плата без такої схеми взагалі (голі модулі, частина клонів);
- живлення просідає під час скидання — конденсатори не встигають;
- драйвер мосту не керує `DTR`/`RTS` (трапляється на CH9102 у Windows).
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > esptool is not able to reset your hardware automatically in the
  > following cases:
  > - Your hardware does not have the ``DTR`` and ``RTS`` lines connected
  >   to ``{IDF_TARGET_STRAP_BOOT_GPIO}`` and ``EN`` (``CHIP_PU``)
  > - The ``DTR`` and ``RTS`` lines are configured differently
  > - There are no such serial control lines at all
  > 
  > (troubleshooting.rst)
  > If you have connected other devices to GPIO pins, try removing them
  > and see if esptool starts working.
  > Check the chip is receiving 3.3V from a stable power source.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Чотири з п'яти причин книги підтверджено дослівно. **П'ята — ні**, і це варте запису: «драйвер мосту не керує `DTR`/`RTS` (трапляється на CH9102 у Windows)».
Агент шукав `CH9102` у `troubleshooting.rst`, `boot-mode-selection.rst` і `reset.py` — немає ніде. Твердження не спростоване, воно **непідтверджене**: поведінка драйвера під Windows у документації esptool не описана й описана бути не може.
Лишаю в книзі як є, але позначаю тут: якщо колись знадобиться клас `A` на цей рядок, джерелом буде не esptool, а сам драйвер WCH або відтворення на живій машині. Це не наряд для М2 — це чесна межа того, що взагалі можна процитувати.
Побічно варте уваги: `troubleshooting.rst` радить те саме, що книга, у двох інших рядках — зняти сторонні пристрої з GPIO і перевірити стабільність 3.3 В. Тобто перелік книги не лише правильний, а й впорядкований так само, як у джерелі.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-K04-019 sha:af13e196 src:kartky/k04-boot.md:50 klas:B -->
### T-K04-019 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Голий модуль або плата без кнопок: перемичкою або пінцетом замкнути `GPIO0` на `GND`, потім коротко замкнути `EN` на `GND` і відпустити, далі прибрати перемичку з `GPIO0`.

**Контекст**

```
## Плати без кнопок

Голий модуль або плата без кнопок: перемичкою або пінцетом замкнути
`GPIO0` на `GND`, потім коротко замкнути `EN` на `GND` і відпустити,
далі прибрати перемичку з `GPIO0`. Послідовність та сама.
```

**Доказ**

- **Статус:** derived — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst (Select Bootloader Mode, Automatic Bootloader)
- **Дослівно з джерела:**
  > The {chip} will enter the serial bootloader when {STRAP_BOOT_GPIO} is
  > held low on reset. Otherwise it will run the program in flash.
  > 
  > {STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left
  > unconnected then it will pull high.
  > 
  > Many boards use a button marked "Flash" (or "BOOT" on some Espressif
  > development boards) that pulls {STRAP_BOOT_GPIO} low when pressed.
  > 
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-020 sha:f2b0c52e src:kartky/k04-boot.md:55 klas:F -->
### T-K04-020 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> [[classic]] На платах ESP32-CAM кнопки `BOOT` немає взагалі: `GPIO0` з'єднується з `GND` перемичкою на самій платі.

**Контекст**

```
## Плати без кнопок

::: uvaha
[[classic]] На платах ESP32-CAM кнопки `BOOT` немає взагалі: `GPIO0`
з'єднується з `GND` перемичкою на самій платі. Після прошивки перемичку
обов'язково зняти, інакше плата так і лишиться в download mode.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-021 sha:3535f9d1 src:kartky/k04-boot.md:56 klas:E -->
### T-K04-021 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Після прошивки перемичку обов'язково зняти, інакше плата так і лишиться в download mode.

**Контекст**

```
## Плати без кнопок

::: uvaha
[[classic]] На платах ESP32-CAM кнопки `BOOT` немає взагалі: `GPIO0`
з'єднується з `GND` перемичкою на самій платі. Після прошивки перемичку
обов'язково зняти, інакше плата так і лишиться в download mode.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-022 sha:c8450f0a src:kartky/k04-boot.md:62 klas:F -->
### T-K04-022 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Понизити швидкість: `--baud 115200`.

**Контекст**

```
## Якщо не допомогло

Понизити швидкість: `--baud 115200`. Спробувати інший USB-порт напряму,
без хаба. Зняти всі дроти зі strapping-пінів — під час старту вони мають бути
вільні. [[classic]] Це `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`;
[[S3]] `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`; [[C3]] `GPIO2`, `GPIO8`,
`GPIO9` (картка К9).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-023 sha:93250c1f src:kartky/k04-boot.md:62 klas:F -->
### T-K04-023 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Спробувати інший USB-порт напряму, без хаба.

**Контекст**

```
## Якщо не допомогло

Понизити швидкість: `--baud 115200`. Спробувати інший USB-порт напряму,
без хаба. Зняти всі дроти зі strapping-пінів — під час старту вони мають бути
вільні. [[classic]] Це `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`;
[[S3]] `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`; [[C3]] `GPIO2`, `GPIO8`,
`GPIO9` (картка К9).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-024 sha:58a20250 src:kartky/k04-boot.md:63 klas:F -->
### T-K04-024 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> Зняти всі дроти зі strapping-пінів — під час старту вони мають бути вільні.

**Контекст**

```
## Якщо не допомогло

Понизити швидкість: `--baud 115200`. Спробувати інший USB-порт напряму,
без хаба. Зняти всі дроти зі strapping-пінів — під час старту вони мають бути
вільні. [[classic]] Це `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`;
[[S3]] `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`; [[C3]] `GPIO2`, `GPIO8`,
`GPIO9` (картка К9).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K04-025 sha:95310ffc src:kartky/k04-boot.md:64 klas:A -->
### T-K04-025 · proza · `kartky/k04-boot.md`

**Твердження, коротко**

> [[classic]] Це `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`; [[S3]] `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`; [[C3]] `GPIO2`, `GPIO8`, `GPIO9` (картка К9).

**Контекст**

```
## Якщо не допомогло

Понизити швидкість: `--baud 115200`. Спробувати інший USB-порт напряму,
без хаба. Зняти всі дроти зі strapping-пінів — під час старту вони мають бути
вільні. [[classic]] Це `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`;
[[S3]] `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`; [[C3]] `GPIO2`, `GPIO8`,
`GPIO9` (картка К9).
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Pin Definitions Table, с. 50
- **Дослівно з джерела:**
  > GPIO5 — VDD_SDIO (Voltage selection for SDIO Slave)
  > Input only during boot; selects 1.8 V or 3.3 V mode for in-package SDIO
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, розділ Pin Definitions, 2026-08-26
- **Нотатка:** GPIO5 в chip має спеціальну функцію VDD_SDIO select, тому його вплив переважно обмежений SDIO функціональністю.
- **Прохід:** m2-63-gpio-07

---
