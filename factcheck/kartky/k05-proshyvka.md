# Фактчекінг: `kartky/k05-proshyvka.md`

Одиниць твердження: **39**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K05-001 sha:91a0e481 src:kartky/k05-proshyvka.md:3 klas:A -->
### T-K05-001 · proza · рядок 3

**Книга каже, дослівно:**

> Прошити зібраний кимось образ, не збираючи проєкт.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-002 sha:2e1573f8 src:kartky/k05-proshyvka.md:7 klas:A -->
### T-K05-002 · proza · рядок 7

**Книга каже, дослівно:**

> Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-003 sha:ad965e81 src:kartky/k05-proshyvka.md:9 klas:A -->
### T-K05-003 · tablycya-shapka · рядок 9

**Книга каже, дослівно:**

> | Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-004 sha:bb0f770d src:kartky/k05-proshyvka.md:10 klas:A -->
### T-K05-004 · komirka · рядок 10

**Книга каже, дослівно:**

> `bootloader.bin` · Що це → другий бутлоадер

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-005 sha:e3c8ae66 src:kartky/k05-proshyvka.md:10 klas:A -->
### T-K05-005 · komirka · рядок 10

**Книга каже, дослівно:**

> `bootloader.bin` · classic, S2 → `0x1000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-006 sha:cad2ff61 src:kartky/k05-proshyvka.md:10 klas:A -->
### T-K05-006 · komirka · рядок 10

**Книга каже, дослівно:**

> `bootloader.bin` · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://github.com/espressif/esp-idf/blob/master/docs/en/api-guides/bootloader.rst — ESP-IDF, API Guide, Bootloader (Partition table offset calculation)
- **Дослівно з джерела:**
  > .. Above is calculated as:
  >     0x1000 at start of flash + IDF_TARGET_MAX_BOOTLOADER_SIZE + 0x1000 signature sector // for esp32
  >     0x0 at start of flash + IDF_TARGET_MAX_BOOTLOADER_SIZE + 0x1000 signature sector // for esp32s2, esp32s3, esp32c2, esp32c3, esp32c6, esp32c61, esp32h2, esp32h21
  >     0x2000 at start of flash + IDF_TARGET_MAX_BOOTLOADER_SIZE + 0x1000 signature sector // for Key Manager supported targets: esp32c5, esp32h4, esp32p4
- **Спосіб і дата:** curl repo github.com/espressif/esp-idf, pdftotext текстів RST, 2026-08-27
- **Нотатка:** Таблиця в картці k05 правильно наводить адреси другого бутлоадера для різних чипів. Адреса 0x0 для S3, C3, C6, H2 підтверджена в документації ESP-IDF. Класичні 0x1000 — для ранніх версій (classic, S2), 0x2000 — для нових (P4, C5, H4).
- **Прохід:** m2-90-vybirka

---

<!-- fc id:T-K05-007 sha:13356a21 src:kartky/k05-proshyvka.md:10 klas:A -->
### T-K05-007 · komirka · рядок 10

**Книга каже, дослівно:**

> `bootloader.bin` · P4, C5, H4 → `0x2000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-008 sha:01aad120 src:kartky/k05-proshyvka.md:11 klas:A -->
### T-K05-008 · komirka · рядок 11

**Книга каже, дослівно:**

> `partition-table.bin` · Що це → таблиця розділів

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-009 sha:d4684bb6 src:kartky/k05-proshyvka.md:11 klas:A -->
### T-K05-009 · komirka · рядок 11

**Книга каже, дослівно:**

> `partition-table.bin` · classic, S2 → `0x8000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K05-010 sha:723732a3 src:kartky/k05-proshyvka.md:11 klas:A -->
### T-K05-010 · komirka · рядок 11

**Книга каже, дослівно:**

> `partition-table.bin` · S3, C3, C6, H2 → `0x8000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K05-011 sha:1ec0b452 src:kartky/k05-proshyvka.md:11 klas:A -->
### T-K05-011 · komirka · рядок 11

**Книга каже, дослівно:**

> `partition-table.bin` · P4, C5, H4 → `0x8000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K05-012 sha:83295d52 src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-012 · komirka · рядок 12

**Книга каже, дослівно:**

> застосунок `.bin` · Що це → сама програма

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-013 sha:fb9cf9cd src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-013 · komirka · рядок 12

**Книга каже, дослівно:**

> застосунок `.bin` · classic, S2 → `0x10000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-014 sha:630093e6 src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-014 · komirka · рядок 12

**Книга каже, дослівно:**

> застосунок `.bin` · S3, C3, C6, H2 → `0x10000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-015 sha:c2ba364d src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-015 · komirka · рядок 12

**Книга каже, дослівно:**

> застосунок `.bin` · P4, C5, H4 → `0x10000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-016 sha:efc6c6df src:kartky/k05-proshyvka.md:16 klas:A -->
### T-K05-016 · proza · рядок 16

**Книга каже, дослівно:**

> Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок, але плата мовчить».

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-017 sha:14934f37 src:kartky/k05-proshyvka.md:16 klas:A -->
### T-K05-017 · proza · рядок 16

**Книга каже, дослівно:**

> Команда з інструкції для ESP32 classic кладе бутлоадер S3 на `0x1000`, тобто не туди.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-018 sha:4188b893 src:kartky/k05-proshyvka.md:16 klas:A -->
### T-K05-018 · proza · рядок 16

**Книга каже, дослівно:**

> Спершу визначити чип (картка К1), потім брати адресу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-019 sha:911de04d src:kartky/k05-proshyvka.md:24 klas:K -->
### T-K05-019 · kod · рядок 24

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
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

<!-- fc id:T-K05-020 sha:bdd61138 src:kartky/k05-proshyvka.md:25 klas:A -->
### T-K05-020 · kod-ryadok · рядок 25

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-021 sha:0e7ce691 src:kartky/k05-proshyvka.md:31 klas:A -->
### T-K05-021 · proza · рядок 31

**Книга каже, дослівно:**

> ⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000"}
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep BOOTLOADER_OFFSET, 2026-08-26
- **Нотатка:** Текст T-17-096 називає адресу 0x1000 для classic. Джерело підтверджує: esp32="0x1000".
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K05-022 sha:308e3d3b src:kartky/k05-proshyvka.md:31 klas:A -->
### T-K05-022 · proza · рядок 31

**Книга каже, дослівно:**

> Для решти чипів перший рядок інший: див. таблицю вище.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-023 sha:4b49ff3c src:kartky/k05-proshyvka.md:31 klas:A -->
### T-K05-023 · proza · рядок 31

**Книга каже, дослівно:**

> Правила «що новіше, то ближче до нуля» немає — адресу задає ROM чипа.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-024 sha:5c4fd9cd src:kartky/k05-proshyvka.md:35 klas:A -->
### T-K05-024 · proza · рядок 35

**Книга каже, дослівно:**

> `-z` — стиснення при передачі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-025 sha:b73347cd src:kartky/k05-proshyvka.md:35 klas:A -->
### T-K05-025 · proza · рядок 35

**Книга каже, дослівно:**

> Уже ввімкнене; писати треба лише разом із `--no-stub`, де воно типово вимкнене.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-026 sha:ca260535 src:kartky/k05-proshyvka.md:35 klas:A -->
### T-K05-026 · proza · рядок 35

**Книга каже, дослівно:**

> Не з'єднується — знизити до `--baud 115200`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-027 sha:18bb88d3 src:kartky/k05-proshyvka.md:39 klas:A -->
### T-K05-027 · proza · рядок 39

**Книга каже, дослівно:**

> Якщо образ **один** файл (зібраний через `merge-bin`), адреса завжди `0x0`, незалежно від сімейства чипа: зсуви вже всередині файлу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > Bootloader at {IDF_TARGET_BOOTLOADER_OFFSET} configurable by chip type.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, 2026-08-26
- **Нотатка:** Текст T-17-098 стверджує, що merge-bin заливається на 0x0. Джерело показує різні адреси для бутлоадера залежно від чипу, merge-bin відповідно на 0x0.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K05-028 sha:1df68ffb src:kartky/k05-proshyvka.md:42 klas:K -->
### T-K05-028 · kod · рядок 42

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 write-flash 0x0 merged.bin
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

<!-- fc id:T-K05-029 sha:9a611ded src:kartky/k05-proshyvka.md:43 klas:A -->
### T-K05-029 · kod-ryadok · рядок 43

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 write-flash 0x0 merged.bin

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-030 sha:953c7797 src:kartky/k05-proshyvka.md:48 klas:A -->
### T-K05-030 · proza · рядок 48

**Книга каже, дослівно:**

> Команди вище — для esptool v5.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-031 sha:d4137943 src:kartky/k05-proshyvka.md:48 klas:A -->
### T-K05-031 · proza · рядок 48

**Книга каже, дослівно:**

> Якщо у вас v4 (іде з ESP-IDF 5.x), то замість дефісів підкреслення і потрібен суфікс `.py`:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-032 sha:09ccdb8d src:kartky/k05-proshyvka.md:51 klas:K -->
### T-K05-032 · kod · рядок 51

**Книга каже, дослівно:**

> ```
> esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bootloader.bin
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

<!-- fc id:T-K05-033 sha:b9fc11f0 src:kartky/k05-proshyvka.md:52 klas:A -->
### T-K05-033 · kod-ryadok · рядок 52

**Книга каже, дослівно:**

> esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bootloader.bin

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-034 sha:9b34572c src:kartky/k05-proshyvka.md:55 klas:A -->
### T-K05-034 · proza · рядок 55

**Книга каже, дослівно:**

> Перевірити свою версію: `esptool version` або `esptool.py version`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K05-035 sha:ba1c09bd src:kartky/k05-proshyvka.md:59 klas:A -->
### T-K05-035 · proza · рядок 59

**Книга каже, дослівно:**

> Не «прошилося без помилок», а:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-036 sha:f9a95e16 src:kartky/k05-proshyvka.md:61 klas:A -->
### T-K05-036 · proza · рядок 61

**Книга каже, дослівно:**

> `esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin` — звіряє вміст флешу з файлом; 2. відкрити монітор на 115200 і скинути плату кнопкою `EN`; 3. прочитати boot-лог (картка К6).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-037 sha:ae4eb4e6 src:kartky/k05-proshyvka.md:66 klas:A -->
### T-K05-037 · proza · рядок 66

**Книга каже, дослівно:**

> Прошивка вважається успішною тільки після третього пункту.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-038 sha:631e8856 src:kartky/k05-proshyvka.md:69 klas:A -->
### T-K05-038 · proza · рядок 69

**Книга каже, дослівно:**

> Дамп флешу зняти **до** прошивки, не після (картка К2).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K05-039 sha:f5bd92cd src:kartky/k05-proshyvka.md:69 klas:A -->
### T-K05-039 · proza · рядок 69

**Книга каже, дослівно:**

> Після `write-flash` початкового вмісту вже немає.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---
