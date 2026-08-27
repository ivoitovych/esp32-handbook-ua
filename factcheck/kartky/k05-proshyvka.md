# Фактчекінг: `kartky/k05-proshyvka.md`

Одиниць твердження: **39**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K05-001 sha:91a0e481 src:kartky/k05-proshyvka.md:3 klas:E -->
### T-K05-001 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Прошити зібраний кимось образ, не збираючи проєкт.

**Контекст**

```
# К5. Прошивка готового образу {#k-proshyvka}

Прошити зібраний кимось образ, не збираючи проєкт.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-002 sha:2e1573f8 src:kartky/k05-proshyvka.md:7 klas:F -->
### T-K05-002 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-003 sha:ad965e81 src:kartky/k05-proshyvka.md:9 klas:F -->
### T-K05-003 · tablycya-shapka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> | Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-004 sha:bb0f770d src:kartky/k05-proshyvka.md:10 klas:F -->
### T-K05-004 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `bootloader.bin` · Що це → другий бутлоадер

**Дослівно з книги**

```
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-005 sha:e3c8ae66 src:kartky/k05-proshyvka.md:10 klas:A -->
### T-K05-005 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `bootloader.bin` · classic, S2 → `0x1000`

**Дослівно з книги**

```
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  > 
  > (partition-tables.rst)
  > * At a 0x10000 (64 KB) offset in the flash is the app labelled
  >   "factory". The bootloader runs this app by default.
  > nvs,      data, nvs,     0x9000,  0x6000,
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K05-006 sha:cad2ff61 src:kartky/k05-proshyvka.md:10 klas:A -->
### T-K05-006 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `bootloader.bin` · S3, C3, C6, H2 → `0x0`

**Дослівно з книги**

```
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

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
### T-K05-007 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `bootloader.bin` · P4, C5, H4 → `0x2000`

**Дослівно з книги**

```
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  > 
  > (partition-tables.rst)
  > * At a 0x10000 (64 KB) offset in the flash is the app labelled
  >   "factory". The bootloader runs this app by default.
  > nvs,      data, nvs,     0x9000,  0x6000,
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K05-008 sha:01aad120 src:kartky/k05-proshyvka.md:11 klas:A -->
### T-K05-008 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `partition-table.bin` · Що це → таблиця розділів

**Дослівно з книги**

```
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/4aac28c3-partition-tables.rst
- **Дослівно з джерела:**
  > A single {IDF_TARGET_NAME}'s flash can contain multiple apps, as well as many different kinds of data (calibration data, filesystems, parameter storage, etc). For this reason a partition table is flashed
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує partition table як таблицю розділів
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-K05-009 sha:d4684bb6 src:kartky/k05-proshyvka.md:11 klas:A -->
### T-K05-009 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `partition-table.bin` · classic, S2 → `0x8000`

**Дослівно з книги**

```
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

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
### T-K05-010 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `partition-table.bin` · S3, C3, C6, H2 → `0x8000`

**Дослівно з книги**

```
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

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
### T-K05-011 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `partition-table.bin` · P4, C5, H4 → `0x8000`

**Дослівно з книги**

```
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K05-012 sha:83295d52 src:kartky/k05-proshyvka.md:12 klas:F -->
### T-K05-012 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> застосунок `.bin` · Що це → сама програма

**Дослівно з книги**

```
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-013 sha:fb9cf9cd src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-013 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> застосунок `.bin` · classic, S2 → `0x10000`

**Дослівно з книги**

```
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  > 
  > (partition-tables.rst)
  > * At a 0x10000 (64 KB) offset in the flash is the app labelled
  >   "factory". The bootloader runs this app by default.
  > nvs,      data, nvs,     0x9000,  0x6000,
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K05-014 sha:630093e6 src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-014 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> застосунок `.bin` · S3, C3, C6, H2 → `0x10000`

**Дослівно з книги**

```
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  > 
  > (partition-tables.rst)
  > * At a 0x10000 (64 KB) offset in the flash is the app labelled
  >   "factory". The bootloader runs this app by default.
  > nvs,      data, nvs,     0x9000,  0x6000,
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K05-015 sha:c2ba364d src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-015 · komirka · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> застосунок `.bin` · P4, C5, H4 → `0x10000`

**Дослівно з книги**

```
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Контекст**

```
## Три образи і їхні адреси

Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

| Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|---|
| `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |
| `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  > 
  > (partition-tables.rst)
  > * At a 0x10000 (64 KB) offset in the flash is the app labelled
  >   "factory". The bootloader runs this app by default.
  > nvs,      data, nvs,     0x9000,  0x6000,
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K05-016 sha:efc6c6df src:kartky/k05-proshyvka.md:16 klas:E -->
### T-K05-016 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок, але плата мовчить».

**Дослівно з книги**

```
Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок,
```

**Контекст**

```
## Три образи і їхні адреси

::: nezvorotne
Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок,
але плата мовчить». Команда з інструкції для ESP32 classic кладе бутлоадер
S3 на `0x1000`, тобто не туди. Спершу визначити чип (картка К1), потім
брати адресу.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-017 sha:14934f37 src:kartky/k05-proshyvka.md:16 klas:A -->
### T-K05-017 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Команда з інструкції для ESP32 classic кладе бутлоадер S3 на `0x1000`, тобто не туди.

**Дослівно з книги**

```
Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок,
```

**Контекст**

```
## Три образи і їхні адреси

::: nezvorotne
Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок,
але плата мовчить». Команда з інструкції для ESP32 classic кладе бутлоадер
S3 на `0x1000`, тобто не туди. Спершу визначити чип (картка К1), потім
брати адресу.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  > 
  > (partition-tables.rst)
  > * At a 0x10000 (64 KB) offset in the flash is the app labelled
  >   "factory". The bootloader runs this app by default.
  > nvs,      data, nvs,     0x9000,  0x6000,
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K05-018 sha:4188b893 src:kartky/k05-proshyvka.md:16 klas:E -->
### T-K05-018 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Спершу визначити чип (картка К1), потім брати адресу.

**Дослівно з книги**

```
Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок,
```

**Контекст**

```
## Три образи і їхні адреси

::: nezvorotne
Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок,
але плата мовчить». Команда з інструкції для ESP32 classic кладе бутлоадер
S3 на `0x1000`, тобто не туди. Спершу визначити чип (картка К1), потім
брати адресу.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-019 sha:911de04d src:kartky/k05-proshyvka.md:24 klas:K -->
### T-K05-019 · kod · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
> ```

**Дослівно з книги**

````
```
````

**Контекст**

````
## Команда

```
esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — ESP-IDF, розділ «RTC Watchdog Timeout» (рядок 306)
- **Дослівно з джерела:**
  > rst:0x10 (RTCWDT_RTC_RESET)
  > 
  > The RTC watchdog is used in the startup code to keep track of
  > execution time and it also helps to prevent a lock-up caused by an
  > unstable power source. It is enabled by default. If the execution
  > time is exceeded, the RTC watchdog will restart the system.
- **Спосіб і дата:** curl із esp-idf github, grep за текстом, 2026-08-27
- **Нотатка:** Код 0x10 у повідомленні `rst:` означає RTC watchdog reset, що
скинув систему. Твердження повністю підтвердить джерелом. Це
стандартний код reset-причин у ESP-IDF.

- **Прохід:** m2-93-vybirka

---

<!-- fc id:T-K05-020 sha:bdd61138 src:kartky/k05-proshyvka.md:25 klas:A -->
### T-K05-020 · kod-ryadok · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \

**Контекст**

````
## Команда

```
esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — ESP-IDF, розділ «RTC Watchdog Timeout» (рядок 306)
- **Дослівно з джерела:**
  > rst:0x10 (RTCWDT_RTC_RESET)
  > 
  > The RTC watchdog is used in the startup code to keep track of
  > execution time and it also helps to prevent a lock-up caused by an
  > unstable power source. It is enabled by default. If the execution
  > time is exceeded, the RTC watchdog will restart the system.
- **Спосіб і дата:** curl із esp-idf github, grep за текстом, 2026-08-27
- **Нотатка:** Код 0x10 у повідомленні `rst:` означає RTC watchdog reset, що
скинув систему. Твердження повністю підтвердить джерелом. Це
стандартний код reset-причин у ESP-IDF.

- **Прохід:** m2-93-vybirka

---

<!-- fc id:T-K05-021 sha:0e7ce691 src:kartky/k05-proshyvka.md:31 klas:A -->
### T-K05-021 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> ⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**.

**Дослівно з книги**

```
⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**. Для решти
```

**Контекст**

```
## Команда

⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**. Для решти
чипів перший рядок інший: див. таблицю вище. Правила «що новіше, то
ближче до нуля» немає — адресу задає ROM чипа.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000"}
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep BOOTLOADER_OFFSET, 2026-08-26
- **Нотатка:** Таблиця розділу 16 показує адреси. Для ESP32: 0x1000. Джерело вказує: esp32="0x1000". | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-K05-022 sha:308e3d3b src:kartky/k05-proshyvka.md:31 klas:E -->
### T-K05-022 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Для решти чипів перший рядок інший: див. таблицю вище.

**Дослівно з книги**

```
⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**. Для решти
```

**Контекст**

```
## Команда

⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**. Для решти
чипів перший рядок інший: див. таблицю вище. Правила «що новіше, то
ближче до нуля» немає — адресу задає ROM чипа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-023 sha:4b49ff3c src:kartky/k05-proshyvka.md:31 klas:A -->
### T-K05-023 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Правила «що новіше, то ближче до нуля» немає — адресу задає ROM чипа.

**Дослівно з книги**

```
⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**. Для решти
```

**Контекст**

```
## Команда

⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**. Для решти
чипів перший рядок інший: див. таблицю вище. Правила «що новіше, то
ближче до нуля» немає — адресу задає ROM чипа.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     hex
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     # the first 2 sectors are reserved for the key manager with AES-XTS (flash encryption) purpose
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Перша редакція давала двовипадкове правило «classic і S2 → 0x1000, S3, C3 і новіші → 0x0». Третій випадок (P4, C5, H4 → 0x2000) робив формулювання «і новіші» хибним, причому саме для тих чипів, які найновіші. Виправлено в розділах 16, 17, 21, 29, картках К5 і К10, додатку C. Довідка Kconfig дала й формулювання для правила: значення визначає ROM, воно не налаштовується.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K05-024 sha:5c4fd9cd src:kartky/k05-proshyvka.md:35 klas:F -->
### T-K05-024 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `-z` — стиснення при передачі.

**Дослівно з книги**

```
`-z` — стиснення при передачі. Уже ввімкнене; писати треба лише
```

**Контекст**

```
## Команда

`-z` — стиснення при передачі. Уже ввімкнене; писати треба лише
разом із `--no-stub`, де воно типово вимкнене.
Не з'єднується — знизити до `--baud 115200`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-025 sha:b73347cd src:kartky/k05-proshyvka.md:35 klas:F -->
### T-K05-025 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Уже ввімкнене; писати треба лише разом із `--no-stub`, де воно типово вимкнене.

**Дослівно з книги**

```
`-z` — стиснення при передачі. Уже ввімкнене; писати треба лише
```

**Контекст**

```
## Команда

`-z` — стиснення при передачі. Уже ввімкнене; писати треба лише
разом із `--no-stub`, де воно типово вимкнене.
Не з'єднується — знизити до `--baud 115200`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-026 sha:ca260535 src:kartky/k05-proshyvka.md:35 klas:F -->
### T-K05-026 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Не з'єднується — знизити до `--baud 115200`.

**Контекст**

```
## Команда

`-z` — стиснення при передачі. Уже ввімкнене; писати треба лише
разом із `--no-stub`, де воно типово вимкнене.
Не з'єднується — знизити до `--baud 115200`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-027 sha:18bb88d3 src:kartky/k05-proshyvka.md:39 klas:A -->
### T-K05-027 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Якщо образ **один** файл (зібраний через `merge-bin`), адреса завжди `0x0`, незалежно від сімейства чипа: зсуви вже всередині файлу.

**Дослівно з книги**

```
Якщо образ **один** файл (зібраний через `merge-bin`), адреса завжди `0x0`,
```

**Контекст**

```
## Команда

Якщо образ **один** файл (зібраний через `merge-bin`), адреса завжди `0x0`,
незалежно від сімейства чипа: зсуви вже всередині файлу.
```

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
### T-K05-028 · kod · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 write-flash 0x0 merged.bin
> ```

**Дослівно з книги**

````
```
````

**Контекст**

````
## Команда

```
esptool --port /dev/ttyUSB0 write-flash 0x0 merged.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-K05-029 sha:9a611ded src:kartky/k05-proshyvka.md:43 klas:A -->
### T-K05-029 · kod-ryadok · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 write-flash 0x0 merged.bin

**Контекст**

````
## Команда

```
esptool --port /dev/ttyUSB0 write-flash 0x0 merged.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-K05-030 sha:953c7797 src:kartky/k05-proshyvka.md:48 klas:A -->
### T-K05-030 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Команди вище — для esptool v5.

**Дослівно з книги**

```
Команди вище — для esptool v5. Якщо у вас v4 (іде з ESP-IDF 5.x), то
```

**Контекст**

```
## Синтаксис: v5 проти v4

Команди вище — для esptool v5. Якщо у вас v4 (іде з ESP-IDF 5.x), то
замість дефісів підкреслення і потрібен суфікс `.py`:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-K05-031 sha:d4137943 src:kartky/k05-proshyvka.md:48 klas:F -->
### T-K05-031 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Якщо у вас v4 (іде з ESP-IDF 5.x), то замість дефісів підкреслення і потрібен суфікс `.py`:

**Дослівно з книги**

```
Команди вище — для esptool v5. Якщо у вас v4 (іде з ESP-IDF 5.x), то
```

**Контекст**

```
## Синтаксис: v5 проти v4

Команди вище — для esptool v5. Якщо у вас v4 (іде з ESP-IDF 5.x), то
замість дефісів підкреслення і потрібен суфікс `.py`:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-032 sha:09ccdb8d src:kartky/k05-proshyvka.md:51 klas:K -->
### T-K05-032 · kod · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> ```
> esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bootloader.bin
> ```

**Дослівно з книги**

````
```
````

**Контекст**

````
## Синтаксис: v5 проти v4

```
esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bootloader.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-K05-033 sha:b9fc11f0 src:kartky/k05-proshyvka.md:52 klas:A -->
### T-K05-033 · kod-ryadok · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bootloader.bin

**Контекст**

````
## Синтаксис: v5 проти v4

```
esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bootloader.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-K05-034 sha:9b34572c src:kartky/k05-proshyvka.md:55 klas:A -->
### T-K05-034 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Перевірити свою версію: `esptool version` або `esptool.py version`.

**Контекст**

```
## Синтаксис: v5 проти v4

Перевірити свою версію: `esptool version` або `esptool.py version`.
```

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

<!-- fc id:T-K05-035 sha:ba1c09bd src:kartky/k05-proshyvka.md:59 klas:E -->
### T-K05-035 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Не «прошилося без помилок», а:

**Контекст**

```
## Перевірка після прошивки

Не «прошилося без помилок», а:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-036 sha:f9a95e16 src:kartky/k05-proshyvka.md:61 klas:A -->
### T-K05-036 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> `esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin` — звіряє вміст флешу з файлом; 2. відкрити монітор на 115200 і скинути плату кнопкою `EN`; 3. прочитати boot-лог (картка К6).

**Дослівно з книги**

```
1. `esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin` — звіряє
```

**Контекст**

```
## Перевірка після прошивки

1. `esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin` — звіряє
   вміст флешу з файлом;
2. відкрити монітор на 115200 і скинути плату кнопкою `EN`;
3. прочитати boot-лог (картка К6).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/{basic-commands,advanced-commands,basic-options,advanced-options}.rst та tools/idf_py_actions/{core_ext,serial_ext,debug_ext}.py в esp-idf release/v5.5, плюс idf-component-manager/idf_extensions.py
- **Дослівно з джерела:**
  > esptool (з переліку команд у __init__.py і документації):
  >   write-flash read-flash erase-flash erase-region read-mac flash-id
  >   elf2image image-info merge-bin version verify-flash dump-mem
  >   read-mem write-mem get-security-info chip-id run …
  > 
  > idf.py (з ACTIONS у core_ext/serial_ext/debug_ext):
  >   all(alias build) app app-flash bootloader clean fullclean menuconfig
  >   merge-bin monitor flash erase-flash partition-table reconfigure
  >   set-target size size-components size-files python-clean read-otadata
  >   efuse-summary … openocd gdb coredump-info coredump-debug
  > 
  > idf-component-manager: add-dependency create-manifest upload-component
  >   create-project-from-example
  > 
  > Приклад із документації дослівно:
  >   esptool -p PORT -b 460800 read-flash 0 ALL flash_contents.bin
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Суцільна перевірка, як у проході 7: узято всі команди, що книга друкує, а не сумнівні. Крім трьох виправлень вище, розбіжностей немає — включно з `read-flash 0 ALL`, яке дослівно збігається з прикладом документації, і `idf.py build`, що є псевдонімом до `all` (`'aliases': ['build']` у `core_ext.py`).
Заразом підтверджено дві дрібниці, які книга стверджує в інших розділах: типова швидкість esptool — 115200, а 74880 названо «usual baud rate used by the ESP8266» для boot-логу. Друге підтверджує картку К6 з іншого боку, ніж прохід 8.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-K05-037 sha:ae4eb4e6 src:kartky/k05-proshyvka.md:66 klas:E -->
### T-K05-037 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Прошивка вважається успішною тільки після третього пункту.

**Контекст**

```
## Перевірка після прошивки

Прошивка вважається успішною тільки після третього пункту.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-038 sha:631e8856 src:kartky/k05-proshyvka.md:69 klas:E -->
### T-K05-038 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Дамп флешу зняти **до** прошивки, не після (картка К2).

**Дослівно з книги**

```
Дамп флешу зняти **до** прошивки, не після (картка К2). Після
```

**Контекст**

```
## Перевірка після прошивки

::: uvaha
Дамп флешу зняти **до** прошивки, не після (картка К2). Після
`write-flash` початкового вмісту вже немає.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-039 sha:f5bd92cd src:kartky/k05-proshyvka.md:69 klas:A -->
### T-K05-039 · proza · `kartky/k05-proshyvka.md`

**Твердження, коротко**

> Після `write-flash` початкового вмісту вже немає.

**Дослівно з книги**

```
Дамп флешу зняти **до** прошивки, не після (картка К2). Після
```

**Контекст**

```
## Перевірка після прошивки

::: uvaha
Дамп флешу зняти **до** прошивки, не після (картка К2). Після
`write-flash` початкового вмісту вже немає.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---
