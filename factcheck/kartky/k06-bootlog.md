# Фактчекінг: `kartky/k06-bootlog.md`

Одиниць твердження: **43**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K06-001 sha:3b9e12c2 src:kartky/k06-bootlog.md:3 klas:F -->
### T-K06-001 · proza · рядок 3

**Книга каже, дослівно:**

> Монітор на **115200 бод**, натиснути `EN`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-002 sha:82c2748d src:kartky/k06-bootlog.md:3 klas:F -->
### T-K06-002 · proza · рядок 3

**Книга каже, дослівно:**

> Перші рядки друкує ROM, і саме вони кажуть, чому плата поводиться так, як поводиться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-003 sha:7419d2c5 src:kartky/k06-bootlog.md:8 klas:A -->
### T-K06-003 · kod · рядок 8

**Книга каже, дослівно:**

> ```
> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K06-004 sha:490ee98b src:kartky/k06-bootlog.md:9 klas:A -->
### T-K06-004 · kod-ryadok · рядок 9

**Книга каже, дослівно:**

> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K06-005 sha:780358c1 src:kartky/k06-bootlog.md:12 klas:F -->
### T-K06-005 · proza · рядок 12

**Книга каже, дослівно:**

> `rst:` — **причина останнього скидання**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-006 sha:545fffe2 src:kartky/k06-bootlog.md:12 klas:F -->
### T-K06-006 · proza · рядок 12

**Книга каже, дослівно:**

> Найчастіші значення для [[classic]] (повна таблиця — додаток D):

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-007 sha:a9766590 src:kartky/k06-bootlog.md:15 klas:F -->
### T-K06-007 · tablycya-shapka · рядок 15

**Книга каже, дослівно:**

> | Код | Назва | Що сталося |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-008 sha:508894ad src:kartky/k06-bootlog.md:16 klas:A -->
### T-K06-008 · komirka · рядок 16

**Книга каже, дослівно:**

> `0x1` · Назва → POWERON_RESET

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K06-009 sha:61891822 src:kartky/k06-bootlog.md:16 klas:F -->
### T-K06-009 · komirka · рядок 16

**Книга каже, дослівно:**

> `0x1` · Що сталося → подано живлення або натиснуто `EN`. Норма

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-010 sha:1baef394 src:kartky/k06-bootlog.md:17 klas:F -->
### T-K06-010 · komirka · рядок 17

**Книга каже, дослівно:**

> `0x3` · Назва → SW_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-011 sha:35861e2c src:kartky/k06-bootlog.md:17 klas:F -->
### T-K06-011 · komirka · рядок 17

**Книга каже, дослівно:**

> `0x3` · Що сталося → скидання з коду (`esp_restart`)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-012 sha:60cc5d87 src:kartky/k06-bootlog.md:18 klas:F -->
### T-K06-012 · komirka · рядок 18

**Книга каже, дослівно:**

> `0x5` · Назва → DEEPSLEEP_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-013 sha:91ecb724 src:kartky/k06-bootlog.md:18 klas:F -->
### T-K06-013 · komirka · рядок 18

**Книга каже, дослівно:**

> `0x5` · Що сталося → прокинувся з deep sleep. Норма

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-014 sha:b13c24c5 src:kartky/k06-bootlog.md:19 klas:A -->
### T-K06-014 · komirka · рядок 19

**Книга каже, дослівно:**

> `0x7` · Назва → TG0WDT_SYS_RESET

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K06-015 sha:f52ff7ed src:kartky/k06-bootlog.md:19 klas:F -->
### T-K06-015 · komirka · рядок 19

**Книга каже, дослівно:**

> `0x7` · Що сталося → спрацював watchdog таймера 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-016 sha:a4c80ac9 src:kartky/k06-bootlog.md:20 klas:F -->
### T-K06-016 · komirka · рядок 20

**Книга каже, дослівно:**

> `0x8` · Назва → TG1WDT_SYS_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-017 sha:ec4961ee src:kartky/k06-bootlog.md:20 klas:F -->
### T-K06-017 · komirka · рядок 20

**Книга каже, дослівно:**

> `0x8` · Що сталося → спрацював watchdog таймера 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-018 sha:61c76aaf src:kartky/k06-bootlog.md:21 klas:F -->
### T-K06-018 · komirka · рядок 21

**Книга каже, дослівно:**

> `0x9` · Назва → RTCWDT_SYS_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-019 sha:df7de7e7 src:kartky/k06-bootlog.md:21 klas:F -->
### T-K06-019 · komirka · рядок 21

**Книга каже, дослівно:**

> `0x9` · Що сталося → спрацював RTC watchdog

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-020 sha:9b73d7e0 src:kartky/k06-bootlog.md:22 klas:A -->
### T-K06-020 · komirka · рядок 22

**Книга каже, дослівно:**

> `0xc` · Назва → SW_CPU_RESET

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K06-021 sha:21e68d08 src:kartky/k06-bootlog.md:22 klas:F -->
### T-K06-021 · komirka · рядок 22

**Книга каже, дослівно:**

> `0xc` · Що сталося → скидання ядра з коду; часто після паніки

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-022 sha:4f167746 src:kartky/k06-bootlog.md:23 klas:A -->
### T-K06-022 · komirka · рядок 23

**Книга каже, дослівно:**

> `0xf` · Назва → RTCWDT_BROWN_OUT_RESET

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K06-023 sha:00c236fb src:kartky/k06-bootlog.md:23 klas:F -->
### T-K06-023 · komirka · рядок 23

**Книга каже, дослівно:**

> `0xf` · Що сталося → **просіло живлення**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-024 sha:9338f26b src:kartky/k06-bootlog.md:24 klas:F -->
### T-K06-024 · komirka · рядок 24

**Книга каже, дослівно:**

> `0x10` · Назва → RTCWDT_RTC_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-025 sha:00c16d81 src:kartky/k06-bootlog.md:24 klas:F -->
### T-K06-025 · komirka · рядок 24

**Книга каже, дослівно:**

> `0x10` · Що сталося → RTC watchdog скинув усе, разом з RTC

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-026 sha:ac281d07 src:kartky/k06-bootlog.md:27 klas:F -->
### T-K06-026 · proza · рядок 27

**Книга каже, дослівно:**

> `boot:` — куди пішов чип: `SPI_FAST_FLASH_BOOT` — звичайний старт із флешу; `DOWNLOAD_BOOT` — режим прошивки: [[classic]] [[S3]] `GPIO0` притиснутий до землі, [[C3]] `GPIO9` (картка К4).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-027 sha:41a2b15a src:kartky/k06-bootlog.md:33 klas:F -->
### T-K06-027 · proza · рядок 33

**Книга каже, дослівно:**

> `rst:0xf` — це не програмна помилка.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-028 sha:b25bdbfb src:kartky/k06-bootlog.md:33 klas:F -->
### T-K06-028 · proza · рядок 33

**Книга каже, дослівно:**

> Шукати треба джерело, кабель або конденсатори, а не баг у коді.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-029 sha:5bdf9b38 src:kartky/k06-bootlog.md:33 klas:F -->
### T-K06-029 · proza · рядок 33

**Книга каже, дослівно:**

> Найчастіше з'являється в момент увімкнення Wi-Fi, бо саме там піковий струм.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-030 sha:0219c8b1 src:kartky/k06-bootlog.md:40 klas:F -->
### T-K06-030 · kod · рядок 40

**Книга каже, дослівно:**

> ```
> I (29) boot: ESP-IDF v6.0.2 2nd stage bootloader
> I (33) boot.esp32: SPI Flash Size : 4MB
> I (52) boot: Partition Table:
> I (56) boot: ## Label      Usage      Type ST Offset   Length
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-031 sha:f0278c3a src:kartky/k06-bootlog.md:47 klas:F -->
### T-K06-031 · proza · рядок 47

**Книга каже, дослівно:**

> Три речі, які тут читаються безкоштовно: **версія IDF**, якою зібрано прошивку; **обсяг флешу**, який бачить бутлоадер; **уся таблиця розділів** із адресами.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-032 sha:e6a1f09c src:kartky/k06-bootlog.md:47 klas:F -->
### T-K06-032 · proza · рядок 47

**Книга каже, дослівно:**

> Це готова відповідь на «а що там усередині» — без розбирання дампа.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-033 sha:0ebdcddf src:kartky/k06-bootlog.md:52 klas:F -->
### T-K06-033 · proza · рядок 52

**Книга каже, дослівно:**

> Число в дужках — мілісекунди від старту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-034 sha:f043d2b4 src:kartky/k06-bootlog.md:52 klas:F -->
### T-K06-034 · proza · рядок 52

**Книга каже, дослівно:**

> Стрибок у цьому числі показує, де саме прошивка задумалася.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-035 sha:f219b8f9 src:kartky/k06-bootlog.md:57 klas:F -->
### T-K06-035 · tablycya · рядок 57

**Книга каже, дослівно:**

> | Видно | Що це |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-036 sha:b44c3a39 src:kartky/k06-bootlog.md:59 klas:F -->
### T-K06-036 · tablycya · рядок 59

**Книга каже, дослівно:**

> | нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-037 sha:e108d7f6 src:kartky/k06-bootlog.md:60 klas:F -->
### T-K06-037 · tablycya · рядок 60

**Книга каже, дослівно:**

> | перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-038 sha:dd7a6d62 src:kartky/k06-bootlog.md:61 klas:F -->
### T-K06-038 · tablycya · рядок 61

**Книга каже, дослівно:**

> | ті самі рядки по колу | boot loop → картка К7 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-039 sha:36137769 src:kartky/k06-bootlog.md:62 klas:F -->
### T-K06-039 · tablycya · рядок 62

**Книга каже, дослівно:**

> | `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-040 sha:165ae2a1 src:kartky/k06-bootlog.md:63 klas:F -->
### T-K06-040 · tablycya · рядок 63

**Книга каже, дослівно:**

> | зовсім порожньо | немає порту чи живлення → картка К3 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-041 sha:8f7a2ab6 src:kartky/k06-bootlog.md:66 klas:F -->
### T-K06-041 · proza · рядок 66

**Книга каже, дослівно:**

> Рядки ROM завжди йдуть на **115200** — і незалежно від швидкості застосунку, і незалежно від кварцу на платі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-042 sha:ae375117 src:kartky/k06-bootlog.md:66 klas:F -->
### T-K06-042 · proza · рядок 66

**Книга каже, дослівно:**

> Якщо ROM видно, а далі каша — швидкість застосунку інша, і це нормально.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-043 sha:e3061d40 src:kartky/k06-bootlog.md:70 klas:F -->
### T-K06-043 · proza · рядок 70

**Книга каже, дослівно:**

> Якщо ж на 115200 не читається нічого, а на **74880** з'являється осмислений текст — у вас **ESP8266**, а не ESP32: у його ROM швидкість виходить саме такою.

**Доказ**

- **Клас:** F — не звірено

---
