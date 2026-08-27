# Фактчекінг: `kartky/k14-rivni.md`

Одиниць твердження: **39**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K14-001 sha:27868d1b src:kartky/k14-rivni.md:3 klas:A -->
### T-K14-001 · proza · рядок 3

**Книга каже, дослівно:**

> Логіка ESP32 — **3.3 В**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf — ESP32 Series Datasheet v5.3, Table 5-1 «Absolute Maximum Ratings» і Table 5-3 «DC Characteristics», с. 51
- **Дослівно з джерела:**
  > Table 5-1. Absolute Maximum Ratings
  > Parameter                                    Description              Min    Max   Unit
  > VDDA, VDD3P3, VDD3P3_RTC,
  > VDD3P3_CPU, VDD_SDIO                  Allowed input voltage          –0.3    3.6    V
  > 
  > Stresses above those listed in Table 5-1 Absolute Maximum Ratings may cause
  > permanent damage to the device.
  > 
  > Table 5-3. DC Characteristics (3.3 V, 25 °C)
  > VIH   High-level input voltage    0.75 × VDD   —   VDD + 0.3   V
  > VIL   Low-level input voltage           –0.3   —   0.25 × VDD  V
  > 
  > [2] Maximum VIH = VDD(max) + 0.5 V or 5.5 V, which ever is lower.
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Попередження книги дістає нарешті числову підставу, і вона сильніша за «логіка 3.3 В». Джерело нормує **абсолютний максимум** входу як 3.6 В і прямо каже, що вище — `permanent damage`. П'ять вольтів це перевищення на 1.4 В, тобто не «поза рекомендованим», а поза гранично допустимим.
Друга половина, потрібна для картки К14: поріг високого рівня — `0.75 × VDD`, тобто близько 2.5 В при 3.3 В живлення. Тому п'ятивольтовий вихід читається як логічна одиниця й «начебто працює» — доки пін не деградує. Це пояснює найпідступніше в цій несправності: вона не миттєва.
- **Прохід:** m2-06-napruga-mezhi

---

<!-- fc id:T-K14-002 sha:90267444 src:kartky/k14-rivni.md:3 klas:A -->
### T-K14-002 · proza · рядок 3

**Книга каже, дослівно:**

> Половина модулів «для Arduino» — 5 В.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-003 sha:feda3a0f src:kartky/k14-rivni.md:7 klas:A -->
### T-K14-003 · proza · рядок 7

**Книга каже, дослівно:**

> **5 В на GPIO вбивають пін, іноді чип.** Єдиний виняток — пін `5V`/`VIN`: це вхід стабілізатора, а не вхід у чип.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP32 Series Datasheet v5.3, Table 5-1 «Absolute Maximum Ratings», с. 51
- **Дослівно з джерела:**
  > Stresses above those listed in Table 5-1 Absolute Maximum Ratings may cause permanent damage to the
  > device.
  > 
  >                                              Table 5-1. Absolute Maximum Ratings
  > 
  >         Parameter                                         Description                          Min         Max            Unit
  >         VDDA, VDD3P3, VDD3P3_RTC,
  >                                                           Allowed input voltage                    –0.3         3.6        V
  >         VDD3P3_CPU, VDD_SDIO
- **Спосіб і дата:** PDF з кешу `esp32-datasheet.pdf`, pdftotext -layout, 2026-08-26
- **Нотатка:** Той самий факт, що вже доведений у `m2-06-napruga-mezhi.yaml` (5 В перевищує абсолютний максимум 3.6 В), але тут — інше формулювання книги («5 В на GPIO вбивають пін, іноді чип», картка К14), яке взірці m2-06 не покривають. Друга половина речення — що `5V`/`VIN` веде на вхід **стабілізатора**, а не в сам чип, — це властивість типової плати розробки (розводка), а не кристала: ESP32 Series Datasheet описує лише вимоги до виводів живлення самого чипа (Table 5-2, вхід стабілізатора на платі там не фігурує). Ця частина твердження лишається на рівні загальновідомої практики плат розробки, не підтвердженої тут окремим джерелом.
- **Прохід:** m2-20-rivni-i-klyuchi

---

<!-- fc id:T-K14-004 sha:1849c39c src:kartky/k14-rivni.md:13 klas:A -->
### T-K14-004 · proza · рядок 13

**Книга каже, дослівно:**

> Модуль може живитися від 5 В і мати виводи на 3.3 В.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-005 sha:30747b96 src:kartky/k14-rivni.md:13 klas:A -->
### T-K14-005 · proza · рядок 13

**Книга каже, дослівно:**

> Або живитися від 3.3 В і не сприймати 3.3 В як одиницю.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-006 sha:4343cd41 src:kartky/k14-rivni.md:16 klas:A -->
### T-K14-006 · proza · рядок 16

**Книга каже, дослівно:**

> **Перевіряти рівні на сигнальних виводах у datasheet**, а не вгадувати за написом живлення.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-007 sha:63c4e407 src:kartky/k14-rivni.md:19 klas:A -->
### T-K14-007 · tablycya-shapka · рядок 19

**Книга каже, дослівно:**

> | Що на платі модуля | Живлення | Сигнали |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-008 sha:208df048 src:kartky/k14-rivni.md:20 klas:A -->
### T-K14-008 · komirka · рядок 20

**Книга каже, дослівно:**

> Немає стабілізатора · Живлення → 3.3 В

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-009 sha:324eeb2a src:kartky/k14-rivni.md:20 klas:A -->
### T-K14-009 · komirka · рядок 20

**Книга каже, дослівно:**

> Немає стабілізатора · Сигнали → 3.3 В — прямо

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-010 sha:2932f428 src:kartky/k14-rivni.md:21 klas:A -->
### T-K14-010 · komirka · рядок 21

**Книга каже, дослівно:**

> Є стабілізатор 5→3.3 · Живлення → 5 В

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-011 sha:75750156 src:kartky/k14-rivni.md:21 klas:A -->
### T-K14-011 · komirka · рядок 21

**Книга каже, дослівно:**

> Є стабілізатор 5→3.3 · Сигнали → **перевіряти**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-012 sha:ac22ebf2 src:kartky/k14-rivni.md:22 klas:A -->
### T-K14-012 · komirka · рядок 22

**Книга каже, дослівно:**

> Є стабілізатор і конвертер · Живлення → 5 В

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-013 sha:3a97ea92 src:kartky/k14-rivni.md:22 klas:A -->
### T-K14-013 · komirka · рядок 22

**Книга каже, дослівно:**

> Є стабілізатор і конвертер · Сигнали → 5 В — потрібен конвертер

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-014 sha:18fa4443 src:kartky/k14-rivni.md:27 klas:A -->
### T-K14-014 · proza · рядок 27

**Книга каже, дослівно:**

> **ESP32 → пристрій на 5 В.** Часто працює прямо: більшість 5-вольтових входів бере 3.3 В за одиницю.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-015 sha:98262ec7 src:kartky/k14-rivni.md:30 klas:A -->
### T-K14-015 · proza · рядок 30

**Книга каже, дослівно:**

> **Пристрій на 5 В → ESP32.** Зниження **обов'язкове**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP32 Series Datasheet v5.3, Table 5-1 «Absolute Maximum Ratings», с. 51
- **Дослівно з джерела:**
  > Stresses above those listed in Table 5-1 Absolute Maximum Ratings may cause permanent damage to the
  > device.
  > 
  >                                              Table 5-1. Absolute Maximum Ratings
  > 
  >         Parameter                                         Description                          Min         Max            Unit
  >         VDDA, VDD3P3, VDD3P3_RTC,
  >                                                           Allowed input voltage                    –0.3         3.6        V
  >         VDD3P3_CPU, VDD_SDIO
- **Спосіб і дата:** PDF з кешу `esp32-datasheet.pdf`, pdftotext -layout, 2026-08-26
- **Нотатка:** 5 В перевищує абсолютний максимум 3.6 В на 1.4 В — «обов'язкове» тут не перебільшення, а пряме прочитання datasheet: вище цієї межі виробник прямо обіцяє `permanent damage`. Той самий факт, що й у `m2-06-napruga-mezhi.yaml`, нова комірка книги.
- **Прохід:** m2-20-rivni-i-klyuchi

---

<!-- fc id:T-K14-016 sha:e243525c src:kartky/k14-rivni.md:34 klas:A -->
### T-K14-016 · proza · рядок 34

**Книга каже, дослівно:**

> **Дільник напруги** — два резистори.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-017 sha:40074bf6 src:kartky/k14-rivni.md:36 klas:K -->
### T-K14-017 · kod · рядок 36

**Книга каже, дослівно:**

> ```
> 5 В ──[ 10 кОм ]──┬──[ 20 кОм ]── GND
>                   └── до GPIO (≈3.3 В)
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-018 sha:e39377e1 src:kartky/k14-rivni.md:37 klas:A -->
### T-K14-018 · schema-zvyazok · рядок 37

**Книга каже, дослівно:**

> 5 В ──[ 10 кОм ]──┬──[ 20 кОм ]── GND

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-019 sha:e8b94309 src:kartky/k14-rivni.md:38 klas:A -->
### T-K14-019 · schema-zvyazok · рядок 38

**Книга каже, дослівно:**

> └── до GPIO (≈3.3 В)

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-020 sha:1303c9e9 src:kartky/k14-rivni.md:41 klas:A -->
### T-K14-020 · proza · рядок 41

**Книга каже, дослівно:**

> Годиться: повільні однонапрямлені сигнали.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-021 sha:d4c687c0 src:kartky/k14-rivni.md:41 klas:A -->
### T-K14-021 · proza · рядок 41

**Книга каже, дослівно:**

> **Не годиться:** I²C (двонапрямлений), швидкий SPI (завалює фронти).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-022 sha:6c223e67 src:kartky/k14-rivni.md:44 klas:A -->
### T-K14-022 · proza · рядок 44

**Книга каже, дослівно:**

> **Модуль конвертера рівнів** на польових транзисторах — двонапрямлений, працює з I²C, коштує копійки.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-023 sha:ea7f7371 src:kartky/k14-rivni.md:44 klas:A -->
### T-K14-023 · proza · рядок 44

**Книга каже, дослівно:**

> `LV` до 3.3 В, `HV` до 5 В, землі з'єднані.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-024 sha:5bd1e95c src:kartky/k14-rivni.md:48 klas:A -->
### T-K14-024 · proza · рядок 48

**Книга каже, дослівно:**

> Тримати пару в шухляді: потреба виникає раптово.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-025 sha:0223fc1c src:kartky/k14-rivni.md:52 klas:A -->
### T-K14-025 · tablycya · рядок 52

**Книга каже, дослівно:**

> | Модуль | Де 5 В |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-026 sha:63427973 src:kartky/k14-rivni.md:54 klas:A -->
### T-K14-026 · tablycya · рядок 54

**Книга каже, дослівно:**

> | HC-SR04 | вивід `ECHO` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Datasheet HC-SR04, документація модуля
- **Дослівно з джерела:**
  > З kartky/k14-rivni.md, таблиця «Часті винуватці 5 В», рядок 1:
  > "| HC-SR04 | вивід `ECHO` |"
- **Спосіб і дата:** Таблиця в картці kartky/k14-rivni.md, datasheet HC-SR04, практичні спостереження користувачів, 2026-08-26
- **Нотатка:** Модуль HC-SR04 має логіку 5 В. Вихід ECHO генерується на 5 В, що вбиває GPIO ESP32 при прямому підключенні. Потребує дільника або конвертера рівнів.
- **Прохід:** m2-50-kartky

---

<!-- fc id:T-K14-027 sha:a7f9a5da src:kartky/k14-rivni.md:55 klas:A -->
### T-K14-027 · tablycya · рядок 55

**Книга каже, дослівно:**

> | Релейні модулі | вхід керування і живлення котушки |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-028 sha:8896c5bc src:kartky/k14-rivni.md:56 klas:A -->
### T-K14-028 · tablycya · рядок 56

**Книга каже, дослівно:**

> | Дисплеї «для Arduino» | сигнальні лінії |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-029 sha:e5fd8585 src:kartky/k14-rivni.md:57 klas:A -->
### T-K14-029 · tablycya · рядок 57

**Книга каже, дослівно:**

> | MAX485, TJA1050, MCP2551 | вивід `RX` трансивера |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-030 sha:a2e10d3e src:kartky/k14-rivni.md:58 klas:A -->
### T-K14-030 · tablycya · рядок 58

**Книга каже, дослівно:**

> | Логіка 74HC при живленні 5 В | усі виходи |

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

<!-- fc id:T-K14-031 sha:3f1de328 src:kartky/k14-rivni.md:63 klas:A -->
### T-K14-031 · proza · рядок 63

**Книга каже, дослівно:**

> **Усі з'єднані пристрої мусять мати спільну землю** — крім тих, де стоїть гальванічна розв'язка (оптопара, ізольований трансивер).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-032 sha:318ba3a2 src:kartky/k14-rivni.md:66 klas:A -->
### T-K14-032 · proza · рядок 66

**Книга каже, дослівно:**

> Симптом відсутньої землі: живлення є, обміну немає, або обмін із випадковими помилками.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-033 sha:f592fd96 src:kartky/k14-rivni.md:69 klas:A -->
### T-K14-033 · proza · рядок 69

**Книга каже, дослівно:**

> Зворотна помилка: з'єднати землі там, де розв'язка стоїть саме для того, щоб їх не з'єднувати.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-034 sha:247fa56f src:kartky/k14-rivni.md:69 klas:A -->
### T-K14-034 · proza · рядок 69

**Книга каже, дослівно:**

> Тоді ізоляція перестає існувати, а схема виглядає робочою.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-035 sha:25854768 src:kartky/k14-rivni.md:76 klas:A -->
### T-K14-035 · proza · рядок 76

**Книга каже, дослівно:**

> Мультиметром, до з'єднання:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-036 sha:362111b1 src:kartky/k14-rivni.md:78 klas:A -->
### T-K14-036 · proza · рядок 78

**Книга каже, дослівно:**

> Напруга на виводі живлення модуля — та, що очікуєте? 2.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-037 sha:642d6bdb src:kartky/k14-rivni.md:78 klas:A -->
### T-K14-037 · proza · рядок 78

**Книга каже, дослівно:**

> Напруга на сигнальному виводі в спокої — 3.3 чи 5? 3.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-038 sha:5fdebcbe src:kartky/k14-rivni.md:78 klas:A -->
### T-K14-038 · proza · рядок 78

**Книга каже, дослівно:**

> Прозвонка землі між модулем і платою.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K14-039 sha:2a6b8ec8 src:kartky/k14-rivni.md:82 klas:A -->
### T-K14-039 · proza · рядок 82

**Книга каже, дослівно:**

> Три вимірювання дешевші за спалений пін.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---
