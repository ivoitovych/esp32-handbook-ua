# Фактчекінг: `kartky/k11-nikoly.md`

Одиниць твердження: **27**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K11-001 sha:9236f6d0 src:kartky/k11-nikoly.md:3 klas:E -->
### T-K11-001 · proza · рядок 3

**Книга каже, дослівно:**

> Кожен пункт нижче — незворотний або майже незворотний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-002 sha:02a70226 src:kartky/k11-nikoly.md:3 klas:E -->
### T-K11-002 · proza · рядок 3

**Книга каже, дослівно:**

> Прочитати до, а не після.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-003 sha:5e9b040f src:kartky/k11-nikoly.md:7 klas:A -->
### T-K11-003 · proza · рядок 7

**Книга каже, дослівно:**

> **Не палити eFuse наосліп.** `espefuse` записує біти лише в один бік — з 0 у 1, назад ніколи.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/espefuse/index.rst
- **Дослівно з джерела:**
  > ``espefuse`` is a tool for communicating with Espressif chips for the
  > purpose of reading/writing ("burning") the one-time-programmable
  > eFuses. Burning occurs only in one direction from 0 to 1 (never
  > cleared 1->0).
  > 
  > .. warning::
  >     Because eFuse is one-time-programmable, it is possible to
  >     permanently damage or "brick" your {IDF_TARGET_NAME} using this
  >     tool. Use it with great care.
  > 
  > - ``--do-not-confirm`` - Do not pause for confirmation before
  >   permanently writing eFuses. Use with caution. If this option is not
  >   used, a manual confirmation step is required, you need to enter the
  >   word ``BURN`` to continue burning.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Твердження картки К11 звірено, і формулювання уточнено за джерелом: не просто «не скидаються назад», а «лише в один бік, з 0 у 1» — так видно механізм, а не лише наслідок.
Доповнення, якого не було ніде: **остання перепона — набрати слово `BURN`**. Це важливо у двох напрямках. Читач, що злякався картки, знає, що випадковим натисканням нічого не спалить. І він же знає, що `--do-not-confirm` у чужому скрипті означає плату, яка згорить без питання, — а саме чужі скрипти в цій книзі розбираються окремо.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K11-004 sha:0a6903d1 src:kartky/k11-nikoly.md:7 klas:F -->
### T-K11-004 · proza · рядок 7

**Книга каже, дослівно:**

> Помилковий біт може назавжди відібрати JTAG, download mode або можливість перепрошивки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-005 sha:cbb6779a src:kartky/k11-nikoly.md:7 klas:A -->
### T-K11-005 · proza · рядок 7

**Книга каже, дослівно:**

> Не запускати `espefuse burn-*`, поки не зрозуміло дослівно, що робить кожен її аргумент.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/espefuse/index.rst
- **Дослівно з джерела:**
  > ``espefuse`` is a tool for communicating with Espressif chips for the
  > purpose of reading/writing ("burning") the one-time-programmable
  > eFuses. Burning occurs only in one direction from 0 to 1 (never
  > cleared 1->0).
  > 
  > .. warning::
  >     Because eFuse is one-time-programmable, it is possible to
  >     permanently damage or "brick" your {IDF_TARGET_NAME} using this
  >     tool. Use it with great care.
  > 
  > - ``--do-not-confirm`` - Do not pause for confirmation before
  >   permanently writing eFuses. Use with caution. If this option is not
  >   used, a manual confirmation step is required, you need to enter the
  >   word ``BURN`` to continue burning.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Твердження картки К11 звірено, і формулювання уточнено за джерелом: не просто «не скидаються назад», а «лише в один бік, з 0 у 1» — так видно механізм, а не лише наслідок.
Доповнення, якого не було ніде: **остання перепона — набрати слово `BURN`**. Це важливо у двох напрямках. Читач, що злякався картки, знає, що випадковим натисканням нічого не спалить. І він же знає, що `--do-not-confirm` у чужому скрипті означає плату, яка згорить без питання, — а саме чужі скрипти в цій книзі розбираються окремо.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K11-006 sha:6096b254 src:kartky/k11-nikoly.md:12 klas:A -->
### T-K11-006 · proza · рядок 12

**Книга каже, дослівно:**

> Остання перепона — набрати слово `BURN` у відповідь на запит.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/espefuse/index.rst
- **Дослівно з джерела:**
  > ``espefuse`` is a tool for communicating with Espressif chips for the
  > purpose of reading/writing ("burning") the one-time-programmable
  > eFuses. Burning occurs only in one direction from 0 to 1 (never
  > cleared 1->0).
  > 
  > .. warning::
  >     Because eFuse is one-time-programmable, it is possible to
  >     permanently damage or "brick" your {IDF_TARGET_NAME} using this
  >     tool. Use it with great care.
  > 
  > - ``--do-not-confirm`` - Do not pause for confirmation before
  >   permanently writing eFuses. Use with caution. If this option is not
  >   used, a manual confirmation step is required, you need to enter the
  >   word ``BURN`` to continue burning.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Твердження картки К11 звірено, і формулювання уточнено за джерелом: не просто «не скидаються назад», а «лише в один бік, з 0 у 1» — так видно механізм, а не лише наслідок.
Доповнення, якого не було ніде: **остання перепона — набрати слово `BURN`**. Це важливо у двох напрямках. Читач, що злякався картки, знає, що випадковим натисканням нічого не спалить. І він же знає, що `--do-not-confirm` у чужому скрипті означає плату, яка згорить без питання, — а саме чужі скрипти в цій книзі розбираються окремо.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K11-007 sha:c07ac4c6 src:kartky/k11-nikoly.md:12 klas:A -->
### T-K11-007 · proza · рядок 12

**Книга каже, дослівно:**

> Прапорець `--do-not-confirm` її знімає; у чужому скрипті він означає, що плата згорить без питання.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/espefuse/index.rst
- **Дослівно з джерела:**
  > ``espefuse`` is a tool for communicating with Espressif chips for the
  > purpose of reading/writing ("burning") the one-time-programmable
  > eFuses. Burning occurs only in one direction from 0 to 1 (never
  > cleared 1->0).
  > 
  > .. warning::
  >     Because eFuse is one-time-programmable, it is possible to
  >     permanently damage or "brick" your {IDF_TARGET_NAME} using this
  >     tool. Use it with great care.
  > 
  > - ``--do-not-confirm`` - Do not pause for confirmation before
  >   permanently writing eFuses. Use with caution. If this option is not
  >   used, a manual confirmation step is required, you need to enter the
  >   word ``BURN`` to continue burning.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Твердження картки К11 звірено, і формулювання уточнено за джерелом: не просто «не скидаються назад», а «лише в один бік, з 0 у 1» — так видно механізм, а не лише наслідок.
Доповнення, якого не було ніде: **остання перепона — набрати слово `BURN`**. Це важливо у двох напрямках. Читач, що злякався картки, знає, що випадковим натисканням нічого не спалить. І він же знає, що `--do-not-confirm` у чужому скрипті означає плату, яка згорить без питання, — а саме чужі скрипти в цій книзі розбираються окремо.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K11-008 sha:410af712 src:kartky/k11-nikoly.md:18 klas:E -->
### T-K11-008 · proza · рядок 18

**Книга каже, дослівно:**

> **Не вмикати Flash Encryption і Secure Boot «щоб подивитися».** В release-режимі це односторонні двері: чип перестає приймати непідписані прошивки, а флеш стає нечитним поза цим конкретним чипом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-009 sha:27686b7b src:kartky/k11-nikoly.md:18 klas:E -->
### T-K11-009 · proza · рядок 18

**Книга каже, дослівно:**

> Дамп, знятий до цього, ще можна залити; знятий після — ні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-010 sha:4dcbf84d src:kartky/k11-nikoly.md:18 klas:E -->
### T-K11-010 · proza · рядок 18

**Книга каже, дослівно:**

> Пробувати тільки на платі, яку не шкода.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-011 sha:13a6c845 src:kartky/k11-nikoly.md:26 klas:A -->
### T-K11-011 · proza · рядок 26

**Книга каже, дослівно:**

> **Не стирати флеш без дампа.** `erase-flash` знищує NVS разом із калібруванням радіо, збереженими креденшелами і конфігурацією конкретного пристрою.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > Erase Flash: ``erase-flash`` & ``erase-region``
  > 
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  > 
  >     esptool erase-flash
  > 
  > To erase a region of the flash, starting at address 0x20000 with
  > length 16 kB (0x4000 bytes):
  > 
  >     esptool erase-region 0x20000 0x4000
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** «Весь чип, усе замінюється на `0xFF`» — цього досить, щоб твердження книги випливало однозначно: NVS, `phy_init` і таблиця розділів лежать у тому самому флеші, отже зникають разом з усім.
Звідси ж і симптом розділу 16 «за адресою `0x8000` порожньо після `erase-flash` без наступної повної прошивки»: `0xFF` — це і є порожньо, і бутлоадер не знаходить таблиці.
Розширення досяжності на картки К2, К8, К11, К15 і розділ 20, де те саме твердження живе в різних формах.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K11-012 sha:34e89cce src:kartky/k11-nikoly.md:26 klas:E -->
### T-K11-012 · proza · рядок 26

**Книга каже, дослівно:**

> Це не завжди відновлюється перезбиранням прошивки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-013 sha:6d6b390e src:kartky/k11-nikoly.md:33 klas:F -->
### T-K11-013 · proza · рядок 33

**Книга каже, дослівно:**

> **Не подавати 5 В на GPIO.** Логіка ESP32 — 3.3 В.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-014 sha:415c2703 src:kartky/k11-nikoly.md:33 klas:E -->
### T-K11-014 · proza · рядок 33

**Книга каже, дослівно:**

> П'ять вольтів вбивають пін, іноді весь порт, іноді чип.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-015 sha:a8ece2fd src:kartky/k11-nikoly.md:33 klas:F -->
### T-K11-015 · proza · рядок 33

**Книга каже, дослівно:**

> Найчастіші джерела: HC-SR04 (вихід `ECHO`), релейні модулі з `VCC` 5 В, «сумісні з Arduino» датчики.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-016 sha:94045e56 src:kartky/k11-nikoly.md:33 klas:E -->
### T-K11-016 · proza · рядок 33

**Книга каже, дослівно:**

> Дільник або конвертер рівнів — обов'язково.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-017 sha:bcf47c92 src:kartky/k11-nikoly.md:38 klas:F -->
### T-K11-017 · proza · рядок 38

**Книга каже, дослівно:**

> Виняток єдиний: пін `5V`/`VIN` — це вхід стабілізатора, туди 5 В можна.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-018 sha:9e743b56 src:kartky/k11-nikoly.md:42 klas:A -->
### T-K11-018 · proza · рядок 42

**Книга каже, дослівно:**

> [[classic]] **Не чіпати GPIO 6, 7, 8, 9, 10, 11.** Вони з'єднані з мікросхемою флешу на самому модулі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32/include/soc/spi_pins.h, .../components/soc/esp32/include/soc/adc_channel.h, .../components/soc/esp32/include/soc/soc_caps.h, .../docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > (spi_pins.h — піни, якими чип говорить із флешем)
  > MSPI_IOMUX_PIN_NUM_CLK   6      MSPI_IOMUX_PIN_NUM_MISO  7
  > MSPI_IOMUX_PIN_NUM_MOSI  8      MSPI_IOMUX_PIN_NUM_HD    9
  > MSPI_IOMUX_PIN_NUM_WP   10      MSPI_IOMUX_PIN_NUM_CS0  11
  > 
  > (adc_channel.h — ADC1)
  > ADC1_GPIO36_CHANNEL 0 … ADC1_GPIO32_CHANNEL 4, ADC1_GPIO33_CHANNEL 5,
  > ADC1_GPIO34_CHANNEL 6, ADC1_GPIO35_CHANNEL 7
  > 
  > (gpio.rst)
  > GPIO34-39 … can only be set as input mode and do not have software
  > pullup or pulldown functions.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, проходи 12 і 25), 2026-08-26
- **Нотатка:** Три найважливіші пінові правила classic, звірені кожне зі свого джерела, а не з переказу.
«6–11 зайняті флешем» — не рекомендація, а перелік `MSPI_IOMUX_*`: саме цими шістьма чип розмовляє з мікросхемою флешу, і збіг із книгою точний.
«34–39 тільки вхід і без підтягування» — дослівно з `gpio.rst`, разом із другою половиною, на якій наполягає книга: **немає програмного** підтягування, тобто кнопка без зовнішнього резистора не працює.
«ADC1 у classic — це саме GPIO 32–39» — вісім каналів `adc_channel.h` дають рівно цей діапазон, без пропусків.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K11-019 sha:44b30bed src:kartky/k11-nikoly.md:42 klas:E -->
### T-K11-019 · proza · рядок 42

**Книга каже, дослівно:**

> Будь-яка спроба їх використати підвішує чип або псує вміст флешу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-020 sha:925d49ec src:kartky/k11-nikoly.md:42 klas:E -->
### T-K11-020 · proza · рядок 42

**Книга каже, дослівно:**

> На пінауті вони часто виведені — це не означає, що вони вільні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-021 sha:db52595d src:kartky/k11-nikoly.md:50 klas:E -->
### T-K11-021 · proza · рядок 50

**Книга каже, дослівно:**

> **Не паяти під живленням.** На жалі незаземленого паяльника може бути наведений потенціал відносно землі плати, і цього досить, щоб пробити вхід.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-022 sha:8399e47f src:kartky/k11-nikoly.md:50 klas:E -->
### T-K11-022 · proza · рядок 50

**Книга каже, дослівно:**

> Живлення від'єднується завжди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-023 sha:649513c1 src:kartky/k11-nikoly.md:54 klas:E -->
### T-K11-023 · proza · рядок 54

**Книга каже, дослівно:**

> **Не під'єднувати земляний щуп осцилографа абиде.** У приладах із мережевим живленням земля щупа — це земля розетки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-024 sha:e3a0462c src:kartky/k11-nikoly.md:54 klas:E -->
### T-K11-024 · proza · рядок 54

**Книга каже, дослівно:**

> Одне невдале дотикання коротить живлення схеми через прилад.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K11-025 sha:ed255616 src:kartky/k11-nikoly.md:58 klas:A -->
### T-K11-025 · proza · рядок 58

**Книга каже, дослівно:**

> **Не тримати strapping-піни навантаженими під час старту.** [[classic]] `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

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

<!-- fc id:T-K11-026 sha:15310ad7 src:kartky/k11-nikoly.md:58 klas:A -->
### T-K11-026 · proza · рядок 58

**Книга каже, дослівно:**

> Підтягнутий не в той бік `GPIO12` перемикає флеш на 1.8 В, і тривольтовий флеш — а він майже скрізь — не стартує зовсім.

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

<!-- fc id:T-K11-027 sha:f44cff79 src:kartky/k11-nikoly.md:63 klas:E -->
### T-K11-027 · proza · рядок 63

**Книга каже, дослівно:**

> **Не міняти дві речі одночасно.** Не незворотно, але з'їдає більше часу, ніж усе перелічене вище разом.

**Доказ**

- **Клас:** F — не звірено

---
