# Фактчекінг: `kartky/k04-boot.md`

Одиниць твердження: **25**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K04-001 sha:d392369e src:kartky/k04-boot.md:3 klas:E -->
### T-K04-001 · proza · рядок 3

**Книга каже, дослівно:**

> Плата не переходить у режим прошивки сама.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-002 sha:8324cf6d src:kartky/k04-boot.md:3 klas:E -->
### T-K04-002 · proza · рядок 3

**Книга каже, дослівно:**

> Це нормальна ситуація для частини плат, а не ознака несправності.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-003 sha:957a85b7 src:kartky/k04-boot.md:8 klas:E -->
### T-K04-003 · proza · рядок 8

**Книга каже, дослівно:**

> Щоб прийняти прошивку, чип має стартувати не в застосунок, а в ROM-бутлоадер.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-004 sha:3285d7ba src:kartky/k04-boot.md:8 klas:F -->
### T-K04-004 · proza · рядок 8

**Книга каже, дослівно:**

> Вибір робиться **в момент скидання** за станом strapping-піна.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-005 sha:7fb043c1 src:kartky/k04-boot.md:12 klas:B -->
### T-K04-005 · proza · рядок 12

**Книга каже, дослівно:**

> [[classic]] [[S3]] Вирішує `GPIO0`:

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 26), 2026-08-26
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-006 sha:0c221230 src:kartky/k04-boot.md:14 klas:B -->
### T-K04-006 · proza · рядок 14

**Книга каже, дослівно:**

> - `GPIO0` вільний (підтягнутий вгору) → звичайний старт застосунку; - `GPIO0` притиснутий до землі → download mode.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 26), 2026-08-26
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-007 sha:fcc462fe src:kartky/k04-boot.md:17 klas:A -->
### T-K04-007 · proza · рядок 17

**Книга каже, дослівно:**

> [[C3]] Вирішує пара пінів: до землі притискається `GPIO9`, а `GPIO8` при цьому має лишатися високим.

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

<!-- fc id:T-K04-008 sha:a007b94b src:kartky/k04-boot.md:17 klas:B -->
### T-K04-008 · proza · рядок 17

**Книга каже, дослівно:**

> Кнопка `BOOT` на платах C3 діє саме на `GPIO9`, тому послідовність нижче не змінюється.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 26), 2026-08-26
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-009 sha:055ab3de src:kartky/k04-boot.md:21 klas:B -->
### T-K04-009 · proza · рядок 21

**Книга каже, дослівно:**

> Кнопка `BOOT` (іноді `IO0`, `FLASH`) саме притискає `GPIO0` до землі.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 26), 2026-08-26
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-010 sha:d5503eea src:kartky/k04-boot.md:21 klas:F -->
### T-K04-010 · proza · рядок 21

**Книга каже, дослівно:**

> Кнопка `EN` (іноді `RST`, `RESET`) — скидання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-011 sha:f44d03d0 src:kartky/k04-boot.md:26 klas:B -->
### T-K04-011 · proza · рядок 26

**Книга каже, дослівно:**

> Порядок обов'язковий: стан `GPIO0` читається один раз, у момент відпускання скидання.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 26), 2026-08-26
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-012 sha:620a701f src:kartky/k04-boot.md:29 klas:F -->
### T-K04-012 · proza · рядок 29

**Книга каже, дослівно:**

> Натиснути і **тримати** `BOOT`. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-013 sha:1b439fce src:kartky/k04-boot.md:29 klas:F -->
### T-K04-013 · proza · рядок 29

**Книга каже, дослівно:**

> Не відпускаючи `BOOT`, коротко натиснути й відпустити `EN`. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-014 sha:83417cd4 src:kartky/k04-boot.md:34 klas:F -->
### T-K04-014 · proza · рядок 34

**Книга каже, дослівно:**

> Ознака успіху — у моніторі порту рядок виду `waiting for download`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-015 sha:b14933d1 src:kartky/k04-boot.md:34 klas:E -->
### T-K04-015 · proza · рядок 34

**Книга каже, дослівно:**

> Якщо монітор закритий, просто запустити прошивку: вона має початися без «Failed to connect».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-016 sha:689b217f src:kartky/k04-boot.md:40 klas:B -->
### T-K04-016 · proza · рядок 40

**Книга каже, дослівно:**

> На платі є схема, що смикає `GPIO0` і `EN` сигналами `DTR`/`RTS` USB-мосту.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 26), 2026-08-26
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-017 sha:e439e3fc src:kartky/k04-boot.md:40 klas:E -->
### T-K04-017 · proza · рядок 40

**Книга каже, дослівно:**

> Вона не універсальна і не працює, коли:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-018 sha:73f5ce2b src:kartky/k04-boot.md:43 klas:F -->
### T-K04-018 · proza · рядок 43

**Книга каже, дослівно:**

> - на `GPIO0` або `GPIO2` навішано зовнішню обв'язку, яка їх утримує; - плата без такої схеми взагалі (голі модулі, частина клонів); - живлення просідає під час скидання — конденсатори не встигають; - драйвер мосту не керує `DTR`/`RTS` (трапляється на CH9102 у Windows).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-019 sha:af13e196 src:kartky/k04-boot.md:50 klas:B -->
### T-K04-019 · proza · рядок 50

**Книга каже, дослівно:**

> Голий модуль або плата без кнопок: перемичкою або пінцетом замкнути `GPIO0` на `GND`, потім коротко замкнути `EN` на `GND` і відпустити, далі прибрати перемичку з `GPIO0`.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 26), 2026-08-26
- **Нотатка:** Клас `B`. Джерело дає механізм повністю — рівень при скиданні, внутрішнє підтягування, кнопка, автоскидання через `DTR`/`RTS`. Порядок «тримати BOOT → натиснути EN → відпустити BOOT» із нього випливає однозначно, але дослівно так ніде не написаний.
Ставити тут `A` було б тим самим, чим був би `A` для JTAG-пінів у проході 20: твердження безсумнівне, але не процитоване. Картка К4 — інструкція, і чесний клас для інструкції, зібраної з фактів, — `B`.
Окремо звірено, що на C3 кнопка діє на `GPIO9`: це головний strapping-пін сімейства за підстановкою `STRAP_BOOT_GPIO`.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K04-020 sha:f2b0c52e src:kartky/k04-boot.md:55 klas:F -->
### T-K04-020 · proza · рядок 55

**Книга каже, дослівно:**

> [[classic]] На платах ESP32-CAM кнопки `BOOT` немає взагалі: `GPIO0` з'єднується з `GND` перемичкою на самій платі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-021 sha:3535f9d1 src:kartky/k04-boot.md:55 klas:E -->
### T-K04-021 · proza · рядок 55

**Книга каже, дослівно:**

> Після прошивки перемичку обов'язково зняти, інакше плата так і лишиться в download mode.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-022 sha:c8450f0a src:kartky/k04-boot.md:62 klas:F -->
### T-K04-022 · proza · рядок 62

**Книга каже, дослівно:**

> Понизити швидкість: `--baud 115200`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-023 sha:93250c1f src:kartky/k04-boot.md:62 klas:F -->
### T-K04-023 · proza · рядок 62

**Книга каже, дослівно:**

> Спробувати інший USB-порт напряму, без хаба.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-024 sha:58a20250 src:kartky/k04-boot.md:62 klas:F -->
### T-K04-024 · proza · рядок 62

**Книга каже, дослівно:**

> Зняти всі дроти зі strapping-пінів — під час старту вони мають бути вільні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K04-025 sha:95310ffc src:kartky/k04-boot.md:62 klas:A -->
### T-K04-025 · proza · рядок 62

**Книга каже, дослівно:**

> [[classic]] Це `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`; [[S3]] `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`; [[C3]] `GPIO2`, `GPIO8`, `GPIO9` (картка К9).

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
