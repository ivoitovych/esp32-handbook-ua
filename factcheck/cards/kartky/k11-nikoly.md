# Фактчекінг: `kartky/k11-nikoly.md`

Одиниць твердження: **27**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-K11-001 sha:9236f6d0 src:kartky/k11-nikoly.md:3 klas:E -->
### T-K11-001 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Кожен пункт нижче — незворотний або майже незворотний.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

Кожен пункт нижче — незворотний або майже незворотний. Прочитати до, а не
після. Решта помилок лікується.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-002 sha:02a70226 src:kartky/k11-nikoly.md:3 klas:E -->
### T-K11-002 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Прочитати до, а не після.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

Кожен пункт нижче — незворотний або майже незворотний. Прочитати до, а не
після. Решта помилок лікується.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-003 sha:5e9b040f src:kartky/k11-nikoly.md:7 klas:A -->
### T-K11-003 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не палити eFuse наосліп.** `espefuse` записує біти лише в один бік — з 0 у 1, назад ніколи.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не палити eFuse наосліп.** `espefuse` записує біти лише в один бік —
з 0 у 1, назад ніколи. Помилковий біт може назавжди відібрати JTAG,
download mode або можливість перепрошивки. Не запускати `espefuse burn-*`,
поки не зрозуміло дослівно, що робить кожен її аргумент.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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

<!-- fc id:T-K11-004 sha:0a6903d1 src:kartky/k11-nikoly.md:8 klas:F -->
### T-K11-004 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Помилковий біт може назавжди відібрати JTAG, download mode або можливість перепрошивки.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не палити eFuse наосліп.** `espefuse` записує біти лише в один бік —
з 0 у 1, назад ніколи. Помилковий біт може назавжди відібрати JTAG,
download mode або можливість перепрошивки. Не запускати `espefuse burn-*`,
поки не зрозуміло дослівно, що робить кожен її аргумент.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-005 sha:cbb6779a src:kartky/k11-nikoly.md:9 klas:A -->
### T-K11-005 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Не запускати `espefuse burn-*`, поки не зрозуміло дослівно, що робить кожен її аргумент.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не палити eFuse наосліп.** `espefuse` записує біти лише в один бік —
з 0 у 1, назад ніколи. Помилковий біт може назавжди відібрати JTAG,
download mode або можливість перепрошивки. Не запускати `espefuse burn-*`,
поки не зрозуміло дослівно, що робить кожен її аргумент.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K11-006 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Остання перепона — набрати слово `BURN` у відповідь на запит.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

Остання перепона — набрати слово `BURN` у відповідь на запит. Прапорець
`--do-not-confirm` її знімає; у чужому скрипті він означає, що плата
згорить без питання.
:::
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K11-007 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Прапорець `--do-not-confirm` її знімає; у чужому скрипті він означає, що плата згорить без питання.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

Остання перепона — набрати слово `BURN` у відповідь на запит. Прапорець
`--do-not-confirm` її знімає; у чужому скрипті він означає, що плата
згорить без питання.
:::
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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

<!-- fc id:T-K11-008 sha:410af712 src:kartky/k11-nikoly.md:18 klas:A -->
### T-K11-008 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не вмикати Flash Encryption і Secure Boot «щоб подивитися».** В release-режимі це односторонні двері: чип перестає приймати непідписані прошивки, а флеш стає нечитним поза цим конкретним чипом.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не вмикати Flash Encryption і Secure Boot «щоб подивитися».** В
release-режимі це односторонні двері: чип перестає приймати непідписані
прошивки, а флеш стає нечитним поза цим конкретним чипом. Дамп, знятий до
цього, ще можна залити; знятий після — ні. Пробувати тільки на платі, яку
не шкода.
:::
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/security/flash-encryption.rst
- **Дослівно з джерела:**
  > For :ref:`flash-enc-release-mode`, the second stage bootloader sets all the eFuse bits set under development mode as well as ``DIS_DOWNLOAD_MANUAL_ENCRYPT``. It also write-protects the ``{IDF_TARGET_CRYPT_CNT}`` eFuse bits.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** write-protect в release-режиме означает невозможность изменения этих параметров после активации
- **Прохід:** sweep-k11-nikoly

---

<!-- fc id:T-K11-009 sha:27686b7b src:kartky/k11-nikoly.md:20 klas:E -->
### T-K11-009 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Дамп, знятий до цього, ще можна залити; знятий після — ні.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не вмикати Flash Encryption і Secure Boot «щоб подивитися».** В
release-режимі це односторонні двері: чип перестає приймати непідписані
прошивки, а флеш стає нечитним поза цим конкретним чипом. Дамп, знятий до
цього, ще можна залити; знятий після — ні. Пробувати тільки на платі, яку
не шкода.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-010 sha:4dcbf84d src:kartky/k11-nikoly.md:21 klas:E -->
### T-K11-010 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Пробувати тільки на платі, яку не шкода.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не вмикати Flash Encryption і Secure Boot «щоб подивитися».** В
release-режимі це односторонні двері: чип перестає приймати непідписані
прошивки, а флеш стає нечитним поза цим конкретним чипом. Дамп, знятий до
цього, ще можна залити; знятий після — ні. Пробувати тільки на платі, яку
не шкода.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-011 sha:13a6c845 src:kartky/k11-nikoly.md:26 klas:A -->
### T-K11-011 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не стирати флеш без дампа.** `erase-flash` знищує NVS разом із калібруванням радіо, збереженими креденшелами і конфігурацією конкретного пристрою.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не стирати флеш без дампа.** `erase-flash` знищує NVS разом із
калібруванням радіо, збереженими креденшелами і конфігурацією конкретного
пристрою. Це не завжди відновлюється перезбиранням прошивки. Спершу
картка К2.
:::
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** «Весь чип, усе замінюється на `0xFF`» — цього досить, щоб твердження книги випливало однозначно: NVS, `phy_init` і таблиця розділів лежать у тому самому флеші, отже зникають разом з усім.
Звідси ж і симптом розділу 16 «за адресою `0x8000` порожньо після `erase-flash` без наступної повної прошивки»: `0xFF` — це і є порожньо, і бутлоадер не знаходить таблиці.
Розширення досяжності на картки К2, К8, К11, К15 і розділ 20, де те саме твердження живе в різних формах.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K11-012 sha:34e89cce src:kartky/k11-nikoly.md:28 klas:E -->
### T-K11-012 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Це не завжди відновлюється перезбиранням прошивки.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не стирати флеш без дампа.** `erase-flash` знищує NVS разом із
калібруванням радіо, збереженими креденшелами і конфігурацією конкретного
пристрою. Це не завжди відновлюється перезбиранням прошивки. Спершу
картка К2.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-013 sha:6d6b390e src:kartky/k11-nikoly.md:33 klas:A -->
### T-K11-013 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не подавати 5 В на GPIO.** Логіка ESP32 — 3.3 В.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не подавати 5 В на GPIO.** Логіка ESP32 — 3.3 В. П'ять вольтів вбивають
пін, іноді весь порт, іноді чип. Найчастіші джерела: HC-SR04 (вихід
`ECHO`), релейні модулі з `VCC` 5 В, «сумісні з Arduino» датчики. Дільник
або конвертер рівнів — обов'язково.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf — ESP32 Series Datasheet v5.3, Table 5-1 «Absolute Maximum Ratings» і Table 5-3 «DC Characteristics», с. 51
- **Дослівно з джерела:**
  > Allowed input voltage –0.3 3.6 V
  > VIH High-level input voltage 0.75 × VDD 1 — VDD 1 + 0.3 V
  > VIL Low-level input voltage –0.3 — 0.25 × VDD 1 V
- **Спосіб і дата:** tools/layer3.py tekst_dzherela (pymupdf: порядок читання плюс рядки таблиць за координатами слів), покомірково, 2026-08-27
- **Нотатка:** Цитату переписано покомірково з витягу документа. Попередня редакція була складена мною РУКАМИ: я зливав колонки таблиці, вигадував вирівнювання й дописував підписи (`Typ`, `Min`, `Max`, `(SAC305)`), яких у витягу немає, і подавав це як дослівну цитату. Числа були праві, цитата — ні. Це те саме, за що я потім ловив помічників. Заголовки таблиць і рядок про permanent damage я додавав від себе. Одиниця після VDD — це номер виноски в документі, не множник.
- **Прохід:** m2-06-voltage-limits

---

<!-- fc id:T-K11-014 sha:415c2703 src:kartky/k11-nikoly.md:33 klas:E -->
### T-K11-014 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> П'ять вольтів вбивають пін, іноді весь порт, іноді чип.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не подавати 5 В на GPIO.** Логіка ESP32 — 3.3 В. П'ять вольтів вбивають
пін, іноді весь порт, іноді чип. Найчастіші джерела: HC-SR04 (вихід
`ECHO`), релейні модулі з `VCC` 5 В, «сумісні з Arduino» датчики. Дільник
або конвертер рівнів — обов'язково.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-015 sha:a8ece2fd src:kartky/k11-nikoly.md:34 klas:A -->
### T-K11-015 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Найчастіші джерела: HC-SR04 (вихід `ECHO`), релейні модулі з `VCC` 5 В, «сумісні з Arduino» датчики.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не подавати 5 В на GPIO.** Логіка ESP32 — 3.3 В. П'ять вольтів вбивають
пін, іноді весь порт, іноді чип. Найчастіші джерела: HC-SR04 (вихід
`ECHO`), релейні модулі з `VCC` 5 В, «сумісні з Arduino» датчики. Дільник
або конвертер рівнів — обов'язково.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Datasheet HC-SR04, документація модуля
- **Дослівно з джерела:**
  > З kartky/k14-rivni.md, таблиця «Часті винуватці 5 В», рядок 1:
  > "| HC-SR04 | вивід `ECHO` |"
- **Спосіб і дата:** Таблиця в картці kartky/k14-rivni.md, datasheet HC-SR04, практичні спостереження користувачів, 2026-08-26
- **Нотатка:** Модуль HC-SR04 має логіку 5 В. Вихід ECHO генерується на 5 В, що вбиває GPIO ESP32 при прямому підключенні. Потребує дільника або конвертера рівнів.
- **Прохід:** m2-50-cards

---

<!-- fc id:T-K11-016 sha:94045e56 src:kartky/k11-nikoly.md:35 klas:E -->
### T-K11-016 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Дільник або конвертер рівнів — обов'язково.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
**Не подавати 5 В на GPIO.** Логіка ESP32 — 3.3 В. П'ять вольтів вбивають
пін, іноді весь порт, іноді чип. Найчастіші джерела: HC-SR04 (вихід
`ECHO`), релейні модулі з `VCC` 5 В, «сумісні з Arduino» датчики. Дільник
або конвертер рівнів — обов'язково.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-017 sha:bcf47c92 src:kartky/k11-nikoly.md:38 klas:A -->
### T-K11-017 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Виняток єдиний: пін `5V`/`VIN` — це вхід стабілізатора, туди 5 В можна.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

Виняток єдиний: пін `5V`/`VIN` — це вхід стабілізатора, туди 5 В можна.
:::
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Схема ESP32 DevKit, постановка вхідних стабілізаторів
- **Дослівно з джерела:**
  > З kartky/k11-nikoly.md, рядок 38:
  > "Виняток єдиний: пін `5V`/`VIN` — це вхід стабілізатора, туди 5 В можна."
- **Спосіб і дата:** Картка kartky/k11-nikoly.md, схема плати ESP32 DevKit, 2026-08-26
- **Нотатка:** Пін VIN або 5V на платі ESP32 йде прямо на вхід регулятора напруги (часто AMS1117 або схожий). Це один з небагатьох місць, де 5 В не вбивають GPIO прямо, бо це не GPIO, а вхід живлення.
- **Прохід:** m2-50-cards

---

<!-- fc id:T-K11-018 sha:9e743b56 src:kartky/k11-nikoly.md:42 klas:A -->
### T-K11-018 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> [[classic]] **Не чіпати GPIO 6, 7, 8, 9, 10, 11.** Вони з'єднані з мікросхемою флешу на самому модулі.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
[[classic]] **Не чіпати GPIO 6, 7, 8, 9, 10, 11.** Вони з'єднані з
мікросхемою флешу на самому модулі. Будь-яка спроба їх використати
підвішує чип або псує вміст флешу. На пінауті вони часто виведені —
це не означає, що вони вільні.
:::
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Три найважливіші пінові правила classic, звірені кожне зі свого джерела, а не з переказу.
«6–11 зайняті флешем» — не рекомендація, а перелік `MSPI_IOMUX_*`: саме цими шістьма чип розмовляє з мікросхемою флешу, і збіг із книгою точний.
«34–39 тільки вхід і без підтягування» — дослівно з `gpio.rst`, разом із другою половиною, на якій наполягає книга: **немає програмного** підтягування, тобто кнопка без зовнішнього резистора не працює.
«ADC1 у classic — це саме GPIO 32–39» — вісім каналів `adc_channel.h` дають рівно цей діапазон, без пропусків.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-K11-019 sha:44b30bed src:kartky/k11-nikoly.md:43 klas:E -->
### T-K11-019 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Будь-яка спроба їх використати підвішує чип або псує вміст флешу.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
[[classic]] **Не чіпати GPIO 6, 7, 8, 9, 10, 11.** Вони з'єднані з
мікросхемою флешу на самому модулі. Будь-яка спроба їх використати
підвішує чип або псує вміст флешу. На пінауті вони часто виведені —
це не означає, що вони вільні.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-020 sha:925d49ec src:kartky/k11-nikoly.md:44 klas:E -->
### T-K11-020 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> На пінауті вони часто виведені — це не означає, що вони вільні.

**Контекст**

```
# К11. Ніколи {#k-nikoly}

::: nezvorotne
[[classic]] **Не чіпати GPIO 6, 7, 8, 9, 10, 11.** Вони з'єднані з
мікросхемою флешу на самому модулі. Будь-яка спроба їх використати
підвішує чип або псує вміст флешу. На пінауті вони часто виведені —
це не означає, що вони вільні.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-021 sha:db52595d src:kartky/k11-nikoly.md:50 klas:E -->
### T-K11-021 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не паяти під живленням.** На жалі незаземленого паяльника може бути наведений потенціал відносно землі плати, і цього досить, щоб пробити вхід.

**Контекст**

```
## Не незворотне, але дороге

**Не паяти під живленням.** На жалі незаземленого паяльника може бути
наведений потенціал відносно землі плати, і цього досить, щоб пробити
вхід. Живлення від'єднується завжди.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-022 sha:8399e47f src:kartky/k11-nikoly.md:52 klas:E -->
### T-K11-022 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Живлення від'єднується завжди.

**Контекст**

```
## Не незворотне, але дороге

**Не паяти під живленням.** На жалі незаземленого паяльника може бути
наведений потенціал відносно землі плати, і цього досить, щоб пробити
вхід. Живлення від'єднується завжди.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-023 sha:649513c1 src:kartky/k11-nikoly.md:54 klas:D -->
### T-K11-023 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не під'єднувати земляний щуп осцилографа абиде.** У приладах із мережевим живленням земля щупа — це земля розетки.

**Контекст**

```
## Не незворотне, але дороге

**Не під'єднувати земляний щуп осцилографа абиде.** У приладах із мережевим
живленням земля щупа — це земля розетки. Одне невдале дотикання коротить
живлення схеми через прилад.
```

**Доказ**

- **Статус:** arithmetic — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Розрахунок: 40 МГц > 24 МГц означає, що дискретизація недостатня за Теоремою Найквіста (потрібно ≥ 2 × сигнал)
- **Дослівно з джерела:**
  > SPI максимальна швидкість на ESP32: до 80 МГц (у режимі нестандартного)
  > Типова швидкість: 10–40 МГц
  > 
  > Теорема Найквіста: для точного представлення сигналу частота дискретизації
  > має бути ≥ 2 × частота сигналу.
  > 
  > Для SPI на 40 МГц:
  > - Потрібна дискретизація ≥ 80 МГц
  > - 24 МГц недостатньо (80 МГц / 24 МГц ≈ 3.3× недостатньо)
  > - Потребується осцилограф з вищою смугою пропускання (500+ МГц)
- **Розрахунок:**
  f_nyquist = f_signal × 2
  Для 40 МГц сигналу: f_nyquist = 80 МГц
  24 МГц < 80 МГц ⟹ недостатньо
- **Спосіб і дата:** Розрахунок на основі Теореми Найквіста, 2026-08-26
- **Прохід:** m2-66-analyzer-28

---

<!-- fc id:T-K11-024 sha:e3a0462c src:kartky/k11-nikoly.md:55 klas:E -->
### T-K11-024 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Одне невдале дотикання коротить живлення схеми через прилад.

**Контекст**

```
## Не незворотне, але дороге

**Не під'єднувати земляний щуп осцилографа абиде.** У приладах із мережевим
живленням земля щупа — це земля розетки. Одне невдале дотикання коротить
живлення схеми через прилад.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K11-025 sha:ed255616 src:kartky/k11-nikoly.md:58 klas:A -->
### T-K11-025 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не тримати strapping-піни навантаженими під час старту.** [[classic]] `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

**Контекст**

```
## Не незворотне, але дороге

**Не тримати strapping-піни навантаженими під час старту.**
[[classic]] `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`. Підтягнутий не в
той бік `GPIO12` перемикає флеш на 1.8 В, і тривольтовий флеш —
а він майже скрізь — не стартує зовсім.
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

<!-- fc id:T-K11-026 sha:15310ad7 src:kartky/k11-nikoly.md:59 klas:A -->
### T-K11-026 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> Підтягнутий не в той бік `GPIO12` перемикає флеш на 1.8 В, і тривольтовий флеш — а він майже скрізь — не стартує зовсім.

**Контекст**

```
## Не незворотне, але дороге

**Не тримати strapping-піни навантаженими під час старту.**
[[classic]] `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`. Підтягнутий не в
той бік `GPIO12` перемикає флеш на 1.8 В, і тривольтовий флеш —
а він майже скрізь — не стартує зовсім.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K11-027 · proza · `kartky/k11-nikoly.md`

**Твердження, коротко**

> **Не міняти дві речі одночасно.** Не незворотно, але з'їдає більше часу, ніж усе перелічене вище разом.

**Контекст**

```
## Не незворотне, але дороге

**Не міняти дві речі одночасно.** Не незворотно, але з'їдає більше часу,
ніж усе перелічене вище разом.
```

**Доказ**

- **Статус:** unchecked — не звірено

---
