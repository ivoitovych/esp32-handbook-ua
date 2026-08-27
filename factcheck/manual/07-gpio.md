# Фактчекінг: `manual/07-gpio.md`

Одиниць твердження: **137**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-07-001 sha:a7df30f3 src:manual/07-gpio.md:3 klas:A -->
### T-07-001 · proza · рядок 3

**Книга каже, дослівно:**

> Матриця GPIO робить більшість пінів взаємозамінними (розділ 04) — і саме через це легко забути, що взаємозамінні **не всі**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-002 sha:65b80860 src:manual/07-gpio.md:3 klas:A -->
### T-07-002 · proza · рядок 3

**Книга каже, дослівно:**

> Піни-винятки не позначені на платі жодним чином, поводяться дивно і псують нерви довше, ніж будь-яка інша дрібниця.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-003 sha:0dcae029 src:manual/07-gpio.md:8 klas:A -->
### T-07-003 · proza · рядок 8

**Книга каже, дослівно:**

> Швидка довідка — картка [К9](#k-pinouty).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-004 sha:497cb464 src:manual/07-gpio.md:8 klas:A -->
### T-07-004 · proza · рядок 8

**Книга каже, дослівно:**

> Тут — чому кожне обмеження існує, бо зрозуміле обмеження запам'ятовується, а список — ні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-005 sha:cc3571ac src:manual/07-gpio.md:13 klas:A -->
### T-07-005 · proza · рядок 13

**Книга каже, дослівно:**

> При скиданні ROM-бутлоадер має вирішити, звідки завантажуватися.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-006 sha:0c44d42d src:manual/07-gpio.md:13 klas:A -->
### T-07-006 · proza · рядок 13

**Книга каже, дослівно:**

> Джерелом рішення служать кілька звичайних GPIO, стан яких читається **один раз**, у момент відпускання скидання (розділ 16).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-007 sha:2d4ea1d4 src:manual/07-gpio.md:13 klas:A -->
### T-07-007 · proza · рядок 13

**Книга каже, дослівно:**

> Далі ці піни працюють як звичайні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-008 sha:44ec0959 src:manual/07-gpio.md:18 klas:A -->
### T-07-008 · proza · рядок 18

**Книга каже, дослівно:**

> [[classic]] ESP32 classic: `GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`.

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

<!-- fc id:T-07-009 sha:9145afd8 src:manual/07-gpio.md:20 klas:A -->
### T-07-009 · tablycya-shapka · рядок 20

**Книга каже, дослівно:**

> | Пін | Що задає | Наслідок помилки |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-010 sha:1f80fd22 src:manual/07-gpio.md:21 klas:A -->
### T-07-010 · komirka · рядок 21

**Книга каже, дослівно:**

> `GPIO0` · Що задає → звичайний старт або download mode

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-011 sha:40fa9dc7 src:manual/07-gpio.md:21 klas:A -->
### T-07-011 · komirka · рядок 21

**Книга каже, дослівно:**

> `GPIO0` · Наслідок помилки → плата не стартує в застосунок

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-012 sha:ce485f20 src:manual/07-gpio.md:22 klas:A -->
### T-07-012 · komirka · рядок 22

**Книга каже, дослівно:**

> `GPIO12` · Що задає → напругу живлення флешу: високий = 1.8 В

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-013 sha:e1c33c77 src:manual/07-gpio.md:22 klas:A -->
### T-07-013 · komirka · рядок 22

**Книга каже, дослівно:**

> `GPIO12` · Наслідок помилки → **тривольтовий флеш не стартує**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-014 sha:4c5651fc src:manual/07-gpio.md:23 klas:A -->
### T-07-014 · komirka · рядок 23

**Книга каже, дослівно:**

> `GPIO2` · Що задає → разом із `GPIO0`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-015 sha:526ab509 src:manual/07-gpio.md:23 klas:A -->
### T-07-015 · komirka · рядок 23

**Книга каже, дослівно:**

> `GPIO2` · Наслідок помилки → заважає входу в download mode

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-016 sha:fa0a392e src:manual/07-gpio.md:24 klas:A -->
### T-07-016 · komirka · рядок 24

**Книга каже, дослівно:**

> `GPIO15` · Що задає → чи друкує ROM boot-лог

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-017 sha:ba3c0447 src:manual/07-gpio.md:24 klas:A -->
### T-07-017 · komirka · рядок 24

**Книга каже, дослівно:**

> `GPIO15` · Наслідок помилки → **лог зникає повністю**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-018 sha:a47a5658 src:manual/07-gpio.md:25 klas:A -->
### T-07-018 · komirka · рядок 25

**Книга каже, дослівно:**

> `GPIO5` · Що задає → таймінги SDIO-веденого

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
### T-07-019 · komirka · рядок 25

**Книга каже, дослівно:**

> `GPIO5` · Наслідок помилки → рідко помітно поза SDIO

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
### T-07-020 · proza · рядок 29

**Книга каже, дослівно:**

> [[classic]] **`GPIO15`, притиснутий до землі, вимикає boot-лог ROM.**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-021 sha:448ca622 src:manual/07-gpio.md:31 klas:A -->
### T-07-021 · proza · рядок 31

**Книга каже, дослівно:**

> У джерела формулювання пряме: `MTDO`, поданий низьким, глушить повідомлення, які друкує ROM-бутлоадер.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-022 sha:13378f7b src:manual/07-gpio.md:31 klas:A -->
### T-07-022 · proza · рядок 31

**Книга каже, дослівно:**

> Пін має внутрішнє підтягування вгору, тому не під'єднаний = високий = звичайний вивід.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-023 sha:f88217d7 src:manual/07-gpio.md:35 klas:A -->
### T-07-023 · proza · рядок 35

**Книга каже, дослівно:**

> Наслідок для діагностики важливий і неочевидний.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-024 sha:3cc299dc src:manual/07-gpio.md:35 klas:A -->
### T-07-024 · proza · рядок 35

**Книга каже, дослівно:**

> «Плата мовчить на 115200» звично означає порт, живлення чи швидкість (картка К6) — але на classic це може означати просто резистор або світлодіод на `GPIO15`.

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

<!-- fc id:T-07-025 sha:4c72b57c src:manual/07-gpio.md:35 klas:A -->
### T-07-025 · proza · рядок 35

**Книга каже, дослівно:**

> Плата при цьому працює нормально, вона лише мовчить.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-026 sha:2088d8d8 src:manual/07-gpio.md:40 klas:A -->
### T-07-026 · proza · рядок 40

**Книга каже, дослівно:**

> Перевірка коштує нуль: зняти обв'язку з `GPIO15` і скинути.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-027 sha:08517ba3 src:manual/07-gpio.md:44 klas:A -->
### T-07-027 · proza · рядок 44

**Книга каже, дослівно:**

> [[classic]] `GPIO12` (MTDI) — найзліший пін у всій лінійці.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-028 sha:e7afa480 src:manual/07-gpio.md:44 klas:A -->
### T-07-028 · proza · рядок 44

**Книга каже, дослівно:**

> Він задає напругу внутрішнього стабілізатора `VDDSDIO`, від якого живиться мікросхема флешу: високий рівень при старті означає **1.8 В**, низький — 3.3 В.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-029 sha:e461769b src:manual/07-gpio.md:49 klas:A -->
### T-07-029 · proza · рядок 49

**Книга каже, дослівно:**

> Уся зловісність — у тому, що на переважній більшості модулів (`WROOM-32` і подібних) флеш **тривольтовий**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-030 sha:1cf32b5b src:manual/07-gpio.md:49 klas:A -->
### T-07-030 · proza · рядок 49

**Книга каже, дослівно:**

> Він отримує 1.8 В, не запускається, і плата не подає ознак життя: ні логу, ні реакції, ні повідомлення про помилку.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-031 sha:126e9170 src:manual/07-gpio.md:54 klas:A -->
### T-07-031 · proza · рядок 54

**Книга каже, дослівно:**

> Звідси й друга половина пастки: на модулях, де флеш справді на 1.8 В, той самий високий рівень — правильне налаштування.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-032 sha:f1f40880 src:manual/07-gpio.md:54 klas:A -->
### T-07-032 · proza · рядок 54

**Книга каже, дослівно:**

> Тобто поведінка залежить від модуля, а не лише від піна, і «у сусіда працює» тут нічого не доводить.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-033 sha:9c7ac3ac src:manual/07-gpio.md:59 klas:A -->
### T-07-033 · proza · рядок 59

**Книга каже, дослівно:**

> Втішна половина: **сам пін має внутрішнє підтягування вниз**, тож ні до чого не під'єднаний `GPIO12` = низький = 3.3 В = правильно.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-034 sha:6f66ba9c src:manual/07-gpio.md:59 klas:A -->
### T-07-034 · proza · рядок 59

**Книга каже, дослівно:**

> Тобто чип безпечний за замовчуванням, і високим його робить **тільки те, що причепили ззовні**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-035 sha:c9a973d7 src:manual/07-gpio.md:64 klas:A -->
### T-07-035 · proza · рядок 64

**Книга каже, дослівно:**

> Саме тому діагностика проста, а плати все одно викидають, вважаючи їх мертвими.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-036 sha:0eefa260 src:manual/07-gpio.md:64 klas:A -->
### T-07-036 · proza · рядок 64

**Книга каже, дослівно:**

> Достатньо зняти те, що тримає `GPIO12` високим.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-037 sha:bb7e589a src:manual/07-gpio.md:67 klas:A -->
### T-07-037 · proza · рядок 67

**Книга каже, дослівно:**

> Найчастіші винуватці: підтягувальний резистор, поставлений «про всяк випадок»; світлодіод із резистором на живлення; JTAG-адаптер (розділ 27); довгий вільний дріт, що ловить наводку.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-038 sha:18fd55d6 src:manual/07-gpio.md:72 klas:A -->
### T-07-038 · proza · рядок 72

**Книга каже, дослівно:**

> [[S3]] S3: `GPIO0`, `GPIO3`, `GPIO45`, `GPIO46`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-039 sha:ddcca7e9 src:manual/07-gpio.md:72 klas:A -->
### T-07-039 · proza · рядок 72

**Книга каже, дослівно:**

> Вхід у бутлоадер — `GPIO0` притиснутий до землі, а `GPIO46` при цьому **низький або вільний**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-040 sha:646aea48 src:manual/07-gpio.md:72 klas:A -->
### T-07-040 · proza · рядок 72

**Книга каже, дослівно:**

> Підтягнутий угору `GPIO46` не дає ввійти в download mode.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-041 sha:13e25920 src:manual/07-gpio.md:76 klas:A -->
### T-07-041 · proza · рядок 76

**Книга каже, дослівно:**

> [[C3]] C3: `GPIO2`, `GPIO8`, `GPIO9`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-042 sha:ea35d47e src:manual/07-gpio.md:76 klas:A -->
### T-07-042 · proza · рядок 76

**Книга каже, дослівно:**

> Вхід у бутлоадер — `GPIO9` притиснутий до землі, `GPIO8` при цьому високий.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-043 sha:4b043722 src:manual/07-gpio.md:76 klas:A -->
### T-07-043 · proza · рядок 76

**Книга каже, дослівно:**

> Комбінація `GPIO8` = 0 і `GPIO9` = 0 недійсна.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-044 sha:25dddc72 src:manual/07-gpio.md:81 klas:A -->
### T-07-044 · proza · рядок 81

**Книга каже, дослівно:**

> **Другий strapping-пін працює на S3 і C3 у протилежні боки.** Це джерело помилок при перенесенні плати з одного чипа на інший.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-045 sha:738e4c61 src:manual/07-gpio.md:84 klas:A -->
### T-07-045 · tablycya-shapka · рядок 84

**Книга каже, дослівно:**

> | | Головний пін | Другий пін для входу в бутлоадер |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-046 sha:a23fd859 src:manual/07-gpio.md:85 klas:A -->
### T-07-046 · komirka · рядок 85

**Книга каже, дослівно:**

> [[classic]] · Головний пін → `GPIO0` = 0

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-047 sha:3e79ba6b src:manual/07-gpio.md:85 klas:A -->
### T-07-047 · komirka · рядок 85

**Книга каже, дослівно:**

> [[classic]] · Другий пін для входу в бутлоадер → `GPIO2` низький або вільний

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-048 sha:4e3150be src:manual/07-gpio.md:86 klas:A -->
### T-07-048 · komirka · рядок 86

**Книга каже, дослівно:**

> [[S3]] · Головний пін → `GPIO0` = 0

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-049 sha:2d751064 src:manual/07-gpio.md:86 klas:A -->
### T-07-049 · komirka · рядок 86

**Книга каже, дослівно:**

> [[S3]] · Другий пін для входу в бутлоадер → `GPIO46` низький або вільний

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-050 sha:197dffaa src:manual/07-gpio.md:87 klas:A -->
### T-07-050 · komirka · рядок 87

**Книга каже, дослівно:**

> [[C3]] · Головний пін → `GPIO9` = 0

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-051 sha:2e5908b5 src:manual/07-gpio.md:87 klas:A -->
### T-07-051 · komirka · рядок 87

**Книга каже, дослівно:**

> [[C3]] · Другий пін для входу в бутлоадер → `GPIO8` **високий**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-052 sha:cd5ba6b2 src:manual/07-gpio.md:90 klas:A -->
### T-07-052 · proza · рядок 90

**Книга каже, дослівно:**

> І поняття «недійсна комбінація» існує лише в правому стовпці для C3 (і решти RISC-V): там `GPIO8` = 0 разом із `GPIO9` = 0 дає непередбачувану поведінку.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-053 sha:7070a25b src:manual/07-gpio.md:90 klas:A -->
### T-07-053 · proza · рядок 90

**Книга каже, дослівно:**

> На classic і S3 такої комбінації немає — там неправильний рівень другого піна просто не пускає в download mode.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-054 sha:d28dc959 src:manual/07-gpio.md:95 klas:A -->
### T-07-054 · proza · рядок 95

**Книга каже, дослівно:**

> У звичайному режимі (головний пін високий) другий пін ігнорується взагалі — на всіх сімействах.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-055 sha:8fc6eaa5 src:manual/07-gpio.md:99 klas:A -->
### T-07-055 · proza · рядок 99

**Книга каже, дослівно:**

> **Практичне правило:** strapping-піни можна використовувати, але як **виходи**, і бажано ті, що ні до чого не під'єднані під час старту.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-056 sha:8dc5f04a src:manual/07-gpio.md:99 klas:A -->
### T-07-056 · proza · рядок 99

**Книга каже, дослівно:**

> Вхід, кнопка чи датчик на strapping-піні — джерело збоїв, які проявляються раз на десять увімкнень.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-057 sha:05e05b1d src:manual/07-gpio.md:105 klas:A -->
### T-07-057 · proza · рядок 105

**Книга каже, дослівно:**

> **Внутрішнє підтягування тут — 45 кОм, і цього мало для кнопки.**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-058 sha:d06a1e95 src:manual/07-gpio.md:107 klas:A -->
### T-07-058 · proza · рядок 107

**Книга каже, дослівно:**

> Кожен strapping-пін має внутрішній резистор саме такого номіналу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-059 sha:dbf37389 src:manual/07-gpio.md:107 klas:A -->
### T-07-059 · proza · рядок 107

**Книга каже, дослівно:**

> Він задає стан за замовчуванням, коли до піна нічого не під'єднано, — і саме тому вільний пін поводиться передбачувано.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-060 sha:1eb06e75 src:manual/07-gpio.md:111 klas:A -->
### T-07-060 · proza · рядок 111

**Книга каже, дослівно:**

> Кнопка `BOOT` на власній платі, зроблена «просто перемикачем на землю», конкурує з внутрішнім підтягуванням і на довгих доріжках або при наводці може не пересилити його надійно.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-061 sha:393f05ea src:manual/07-gpio.md:115 klas:A -->
### T-07-061 · proza · рядок 115

**Книга каже, дослівно:**

> Правильно: **сильна підтяжка вниз, 10 кОм на землю**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-062 sha:87c3d715 src:manual/07-gpio.md:115 klas:A -->
### T-07-062 · proza · рядок 115

**Книга каже, дослівно:**

> Це рекомендація самої документації esptool, а не запас «про всяк випадок».

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-063 sha:c3ef5d6f src:manual/07-gpio.md:121 klas:A -->
### T-07-063 · proza · рядок 121

**Книга каже, дослівно:**

> [[classic]] `GPIO6`, `GPIO7`, `GPIO8`, `GPIO9`, `GPIO10`, `GPIO11` з'єднані з мікросхемою флешу всередині модуля.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-064 sha:d8a73a0f src:manual/07-gpio.md:124 klas:A -->
### T-07-064 · proza · рядок 124

**Книга каже, дослівно:**

> Вони **виведені на гребінку** більшості плат, підписані як звичайні GPIO — і це чиста пастка.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-065 sha:6964fc01 src:manual/07-gpio.md:124 klas:A -->
### T-07-065 · proza · рядок 124

**Книга каже, дослівно:**

> Спроба їх використати підвішує чип або псує вміст флешу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-066 sha:30b73e47 src:manual/07-gpio.md:128 klas:A -->
### T-07-066 · proza · рядок 128

**Книга каже, дослівно:**

> Правило категоричне: [[classic]] шість пінів 6–11 не існують.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-067 sha:25039e68 src:manual/07-gpio.md:128 klas:A -->
### T-07-067 · proza · рядок 128

**Книга каже, дослівно:**

> Ніколи, за жодних умов, у жодному проєкті.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-068 sha:ec10e19e src:manual/07-gpio.md:132 klas:A -->
### T-07-068 · proza · рядок 132

**Книга каже, дослівно:**

> [[classic]] **На модулях із PSRAM до цього переліку додаються `GPIO16` і `GPIO17`.** Документація ESP-IDF називає їх в одному рядку з 6–11: «GPIO 6-11 and GPIO16-17 are usually connected to the SPI flash and PSRAM integrated on the module».

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-069 sha:f4840dbc src:manual/07-gpio.md:137 klas:A -->
### T-07-069 · proza · рядок 137

**Книга каже, дослівно:**

> Різниця між шісткою й цією парою — у слові «usually».

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-070 sha:32397664 src:manual/07-gpio.md:137 klas:A -->
### T-07-070 · proza · рядок 137

**Книга каже, дослівно:**

> Піни 6–11 зайняті завжди; 16 і 17 — лише там, де на модулі є PSRAM, тобто на `WROVER` і подібних.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-071 sha:e55b2180 src:manual/07-gpio.md:137 klas:A -->
### T-07-071 · proza · рядок 137

**Книга каже, дослівно:**

> На голому `WROOM-32` вони вільні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-072 sha:11f8e1b0 src:manual/07-gpio.md:141 klas:A -->
### T-07-072 · proza · рядок 141

**Книга каже, дослівно:**

> Практично це означає, що правило «шість пінів» безпечне лише доти, доки ви знаєте, який модуль тримаєте.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-073 sha:cd5972bc src:manual/07-gpio.md:141 klas:A -->
### T-07-073 · proza · рядок 141

**Книга каже, дослівно:**

> Взяли `WROVER` за схемою, накресленою для `WROOM`, — і `GPIO16` уже нічий.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-074 sha:c9a2eeb3 src:manual/07-gpio.md:146 klas:A -->
### T-07-074 · proza · рядок 146

**Книга каже, дослівно:**

> [[S3]] На S3 те саме стосується `GPIO26`–`GPIO32`, а на модулях з Octal PSRAM (`N16R8` і подібні) — додатково `GPIO33`–`GPIO37`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-075 sha:203497bf src:manual/07-gpio.md:149 klas:A -->
### T-07-075 · proza · рядок 149

**Книга каже, дослівно:**

> [[C3]] На C3 — `GPIO12`–`GPIO17`, і окремо `GPIO11`: його майданчик у матриці називається `VDD_SPI`, тобто це вивід живлення самої флеш-пам'яті, а не звичайний пін.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-076 sha:d9afb982 src:manual/07-gpio.md:149 klas:A -->
### T-07-076 · proza · рядок 149

**Книга каже, дослівно:**

> Перевести його в GPIO можна лише пропаленням eFuse `VDD_SPI_AS_GPIO` — незворотним (картка К11), і на модулі з внутрішнім флешем це забирає в флешу живлення.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-077 sha:8b178734 src:manual/07-gpio.md:149 klas:A -->
### T-07-077 · proza · рядок 149

**Книга каже, дослівно:**

> Рахуйте `GPIO11` серед зайнятих.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-078 sha:9a2e525e src:manual/07-gpio.md:156 klas:A -->
### T-07-078 · proza · рядок 156

**Книга каже, дослівно:**

> [[S3]] Це найпоширеніша причина «купив S3 із 16 МБ і 8 МБ PSRAM, а пінів менше, ніж на classic».

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-079 sha:5638f14b src:manual/07-gpio.md:156 klas:A -->
### T-07-079 · proza · рядок 156

**Книга каже, дослівно:**

> Октальна PSRAM з'їдає п'ять додаткових пінів, і на платі вони або не виведені, або виведені й непридатні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-080 sha:f1266858 src:manual/07-gpio.md:160 klas:A -->
### T-07-080 · proza · рядок 160

**Книга каже, дослівно:**

> Перед проєктуванням плати на S3 варто точно знати, який модуль стоїть: `N8` і `N16R8` мають різну кількість доступних пінів.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-081 sha:6a801047 src:manual/07-gpio.md:166 klas:A -->
### T-07-081 · proza · рядок 166

**Книга каже, дослівно:**

> [[classic]] `GPIO34`–`GPIO39` мають лише вхідний буфер.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-082 sha:2b119dd6 src:manual/07-gpio.md:168 klas:A -->
### T-07-082 · proza · рядок 168

**Книга каже, дослівно:**

> - вихідного драйвера — керувати з них нічим не можна; - **вбудованого підтягування** — ні pull-up, ні pull-down.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-083 sha:2dbf225d src:manual/07-gpio.md:171 klas:A -->
### T-07-083 · proza · рядок 171

**Книга каже, дослівно:**

> Друге важливіше, бо менш очевидне.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-084 sha:9b7ec34b src:manual/07-gpio.md:171 klas:A -->
### T-07-084 · proza · рядок 171

**Книга каже, дослівно:**

> Кнопка на `GPIO34` без **зовнішнього** резистора не працює: вхід бовтається і читає випадкове (розділ 05).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-085 sha:1d981589 src:manual/07-gpio.md:171 klas:A -->
### T-07-085 · proza · рядок 171

**Книга каже, дослівно:**

> Виглядає як несправний пін або несправна кнопка.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-086 sha:7997d730 src:manual/07-gpio.md:175 klas:A -->
### T-07-086 · proza · рядок 175

**Книга каже, дослівно:**

> Налаштуванням у коді це не змінюється: апаратної схеми немає.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-087 sha:dc856329 src:manual/07-gpio.md:177 klas:A -->
### T-07-087 · proza · рядок 177

**Книга каже, дослівно:**

> У пізніших сімействах (S3, C3) тільки-вхідних пінів немає — усі повнофункціональні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-088 sha:4d958fd4 src:manual/07-gpio.md:182 klas:A -->
### T-07-088 · proza · рядок 182

**Книга каже, дослівно:**

> **ADC1 і ADC2.** У чипі два аналого-цифрові перетворювачі, і вони не рівноправні.

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
### T-07-089 · proza · рядок 186

**Книга каже, дослівно:**

> [[classic]] [[S2]] [[S3]] **ADC2 ділиться з Wi-Fi, і радіо має пріоритет.** Драйвер це передбачає: `adc_oneshot_read` розводить себе з драйвером Wi-Fi і при зайнятому ADC2 повертає **помилку**, а не зіпсоване число.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-090 sha:0038f55f src:manual/07-gpio.md:190 klas:A -->
### T-07-090 · proza · рядок 190

**Книга каже, дослівно:**

> Тобто зіпсованих даних чекати не варто — варто чекати читання, яке перестало вдаватися.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-091 sha:97c124bb src:manual/07-gpio.md:190 klas:A -->
### T-07-091 · proza · рядок 190

**Книга каже, дослівно:**

> Що гірше для того, хто не перевіряє код повернення: датчик просто «замовкає» на старому значенні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-092 sha:4fe5b2b1 src:manual/07-gpio.md:194 klas:A -->
### T-07-092 · proza · рядок 194

**Книга каже, дослівно:**

> Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`, після чого читання перестає вдаватися.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-093 sha:cf5a8129 src:manual/07-gpio.md:194 klas:A -->
### T-07-093 · proza · рядок 194

**Книга каже, дослівно:**

> Людина шукає помилку в коді вимірювання, а справа в тому, який саме пін обрано.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-094 sha:4abe4c19 src:manual/07-gpio.md:198 klas:A -->
### T-07-094 · proza · рядок 198

**Книга каже, дослівно:**

> Лікування одне: перенести вимірювання на **ADC1** — [[classic]] це `GPIO32`–`GPIO39`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-095 sha:e9ad2932 src:manual/07-gpio.md:202 klas:A -->
### T-07-095 · proza · рядок 202

**Книга каже, дослівно:**

> **DAC.** Справжній аналоговий вихід є лише у двох сімействах, і піни в них **різні**:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-096 sha:48af3317 src:manual/07-gpio.md:205 klas:A -->
### T-07-096 · tablycya-shapka · рядок 205

**Книга каже, дослівно:**

> | | Канал 1 | Канал 2 |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-097 sha:2d6128fe src:manual/07-gpio.md:206 klas:A -->
### T-07-097 · komirka · рядок 206

**Книга каже, дослівно:**

> [[classic]] · Канал 1 → `GPIO25`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-098 sha:7d1d509e src:manual/07-gpio.md:206 klas:A -->
### T-07-098 · komirka · рядок 206

**Книга каже, дослівно:**

> [[classic]] · Канал 2 → `GPIO26`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-099 sha:7afccfc4 src:manual/07-gpio.md:207 klas:A -->
### T-07-099 · komirka · рядок 207

**Книга каже, дослівно:**

> [[S2]] · Канал 1 → `GPIO17`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-100 sha:69208de8 src:manual/07-gpio.md:207 klas:A -->
### T-07-100 · komirka · рядок 207

**Книга каже, дослівно:**

> [[S2]] · Канал 2 → `GPIO18`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-101 sha:8435c691 src:manual/07-gpio.md:210 klas:A -->
### T-07-101 · proza · рядок 210

**Книга каже, дослівно:**

> Більше ніде в лінійці DAC немає (розділи 04 і 33).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-102 sha:21828d34 src:manual/07-gpio.md:212 klas:A -->
### T-07-102 · proza · рядок 212

**Книга каже, дослівно:**

> Плутати їх дорого вдвічі: на S2 `GPIO25` не просто не має DAC — його там не існує взагалі, маска дійсних пінів вирізає 22–25.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-103 sha:4838050a src:manual/07-gpio.md:215 klas:A -->
### T-07-103 · proza · рядок 215

**Книга каже, дослівно:**

> **Touch.** Ємнісні сенсори прив'язані до конкретних пінів і є лише в classic, S2 і S3.

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
### T-07-104 · proza · рядок 218

**Книга каже, дослівно:**

> Для всіх трьох матриця GPIO не діє: це аналогові блоки, фізично з'єднані з конкретними ніжками.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-105 sha:89f377b7 src:manual/07-gpio.md:223 klas:A -->
### T-07-105 · proza · рядок 223

**Книга каже, дослівно:**

> **UART0** [[classic]] `GPIO1` (TX) і `GPIO3` (RX) — це консоль.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-106 sha:08617839 src:manual/07-gpio.md:223 klas:A -->
### T-07-106 · proza · рядок 223

**Книга каже, дослівно:**

> Через них іде boot-лог і прошивка.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-107 sha:99a46388 src:manual/07-gpio.md:223 klas:A -->
### T-07-107 · proza · рядок 223

**Книга каже, дослівно:**

> Використати їх під щось інше можна, але тоді ви втрачаєте і лог, і зручну прошивку — тобто саме те, чим діагностують проблеми.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-108 sha:7af574ff src:manual/07-gpio.md:228 klas:A -->
### T-07-108 · proza · рядок 228

**Книга каже, дослівно:**

> Правило: чіпати UART0 тільки тоді, коли пінів справді не лишилося.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-109 sha:6d5fd871 src:manual/07-gpio.md:230 klas:A -->
### T-07-109 · proza · рядок 230

**Книга каже, дослівно:**

> **USB-JTAG** [[S3]] `GPIO19`, `GPIO20`; [[C3]] `GPIO18`, `GPIO19`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-110 sha:6f074d3a src:manual/07-gpio.md:230 klas:A -->
### T-07-110 · proza · рядок 230

**Книга каже, дослівно:**

> Переналаштувати їх можна, але це вимикає покрокове налагодження (розділ 27).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-111 sha:16fc615f src:manual/07-gpio.md:236 klas:A -->
### T-07-111 · proza · рядок 236

**Книга каже, дослівно:**

> Практичний підрахунок для [[classic]] 38-пінової плати.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-112 sha:1c767126 src:manual/07-gpio.md:239 klas:A -->
### T-07-112 · proza · рядок 239

**Книга каже, дослівно:**

> - 6 пінів флешу (6–11) — не існують; - 2 піни консолі (1, 3) — краще не чіпати; - 6 тільки-вхідних (34–39) — придатні лише під датчики;

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

<!-- fc id:T-07-113 sha:dae5d714 src:manual/07-gpio.md:243 klas:A -->
### T-07-113 · proza · рядок 243

**Книга каже, дослівно:**

> Лишається близько **20 повноцінних** пінів, з яких п'ять — strapping і потребують уваги.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-114 sha:2e6e5ae0 src:manual/07-gpio.md:246 klas:A -->
### T-07-114 · proza · рядок 246

**Книга каже, дослівно:**

> Типовий проєкт витрачає їх швидко: I²C — 2, SPI — 4 плюс по одному на пристрій, UART до другого контролера — 2, кнопка — 1, світлодіод — 1, реле — 2.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-115 sha:d3fff0e3 src:manual/07-gpio.md:246 klas:A -->
### T-07-115 · proza · рядок 246

**Книга каже, дослівно:**

> Двадцяти вистачає не завжди.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-116 sha:bbf00d41 src:manual/07-gpio.md:251 klas:A -->
### T-07-116 · proza · рядок 251

**Книга каже, дослівно:**

> Коли пінів не вистачає, варіанти в порядку зростання складності:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-117 sha:be7c4eb1 src:manual/07-gpio.md:253 klas:A -->
### T-07-117 · proza · рядок 253

**Книга каже, дослівно:**

> **Розширювач портів по I²C** — PCF8574 (8 пінів) або MCP23017 (16) за дві лінії.

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

<!-- fc id:T-07-118 sha:8f937bea src:manual/07-gpio.md:253 klas:A -->
### T-07-118 · proza · рядок 253

**Книга каже, дослівно:**

> Найдешевше і найпростіше; підходить для кнопок, світлодіодів, реле — усього, де не потрібна швидкість.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-119 sha:34181297 src:manual/07-gpio.md:257 klas:A -->
### T-07-119 · proza · рядок 257

**Книга каже, дослівно:**

> **Зсувний регістр** 74HC595 на виходи, 74HC165 на входи — по SPI, каскадуються скільки завгодно.

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
### T-07-120 · proza · рядок 260

**Книга каже, дослівно:**

> **Аналоговий мультиплексор** CD4051 — вісім аналогових входів на один пін ADC.

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
### T-07-121 · proza · рядок 263

**Книга каже, дослівно:**

> **Чип із більшою кількістю пінів** — S3 має їх більше за classic.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-122 sha:ae8000cc src:manual/07-gpio.md:265 klas:A -->
### T-07-122 · proza · рядок 265

**Книга каже, дослівно:**

> **Другий мікроконтролер** — коли задача й так ділиться на дві частини (розділ 57).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-123 sha:035a38f6 src:manual/07-gpio.md:271 klas:A -->
### T-07-123 · proza · рядок 271

**Книга каже, дослівно:**

> Головне правило: **pinout плати важливіший за pinout чипа**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-124 sha:e43399df src:manual/07-gpio.md:273 klas:A -->
### T-07-124 · proza · рядок 273

**Книга каже, дослівно:**

> Виробник плати міг вивести не всі піни; підписати їх власними іменами (`D2`, `A0`, `SDA`) замість номерів GPIO; повісити на пін світлодіод, резистор або кнопку; використати частину пінів під власні потреби.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-125 sha:9e2b2c79 src:manual/07-gpio.md:277 klas:A -->
### T-07-125 · proza · рядок 277

**Книга каже, дослівно:**

> Тому: спершу шукайте схему **конкретної плати**, і лише як довідку — datasheet чипа.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-126 sha:a06a92ec src:manual/07-gpio.md:281 klas:A -->
### T-07-126 · proza · рядок 281

**Книга каже, дослівно:**

> Плати з однаковою назвою бувають різними.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-127 sha:38f59818 src:manual/07-gpio.md:281 klas:A -->
### T-07-127 · proza · рядок 281

**Книга каже, дослівно:**

> «ESP32 DevKit V1» продається у 30- і 38-піновому варіантах, і це **різні плати** з різним розташуванням пінів.

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

<!-- fc id:T-07-128 sha:b0fde932 src:manual/07-gpio.md:281 klas:A -->
### T-07-128 · proza · рядок 281

**Книга каже, дослівно:**

> Пінаут, знайдений за назвою, може не відповідати тому, що у вас у руках.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-129 sha:909499e7 src:manual/07-gpio.md:286 klas:A -->
### T-07-129 · proza · рядок 286

**Книга каже, дослівно:**

> Надійна перевірка: порахувати піни й звірити з картинкою.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-130 sha:4006ed63 src:manual/07-gpio.md:286 klas:A -->
### T-07-130 · proza · рядок 286

**Книга каже, дослівно:**

> Займає десять секунд, рятує від дуже неприємних помилок (розділ 08).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-131 sha:00d10011 src:manual/07-gpio.md:292 klas:A -->
### T-07-131 · proza · рядок 292

**Книга каже, дослівно:**

> [[classic]] GPIO 6–11 не існують.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-132 sha:8252205d src:manual/07-gpio.md:294 klas:A -->
### T-07-132 · proza · рядок 294

**Книга каже, дослівно:**

> [[classic]] `GPIO12` високий при старті = флеш отримує 1.8 В замість 3.3 В.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-133 sha:6af50605 src:manual/07-gpio.md:294 klas:A -->
### T-07-133 · proza · рядок 294

**Книга каже, дослівно:**

> На тривольтовому флеші — а він майже на всіх модулях — плата мовчить, без жодного повідомлення.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-134 sha:eca754e3 src:manual/07-gpio.md:298 klas:A -->
### T-07-134 · proza · рядок 298

**Книга каже, дослівно:**

> [[classic]] GPIO 34–39 — тільки вхід і **без вбудованого підтягування**.

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
### T-07-135 · proza · рядок 300

**Книга каже, дослівно:**

> [[classic]] [[S2]] [[S3]] ADC2 не працює при Wi-Fi; вимірювання переносяться на ADC1.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-136 sha:101667fc src:manual/07-gpio.md:303 klas:A -->
### T-07-136 · proza · рядок 303

**Книга каже, дослівно:**

> Strapping-піни краще використовувати як виходи й лишати вільними під час старту.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-07-137 sha:3521c982 src:manual/07-gpio.md:306 klas:A -->
### T-07-137 · proza · рядок 306

**Книга каже, дослівно:**

> Pinout конкретної плати, а не чипа; порахувати піни перед тим, як довіритися картинці.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---
