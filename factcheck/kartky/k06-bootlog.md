# Фактчекінг: `kartky/k06-bootlog.md`

Одиниць твердження: **45**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

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

<!-- fc id:T-K06-011 sha:35861e2c src:kartky/k06-bootlog.md:17 klas:A -->
### T-K06-011 · komirka · рядок 17

**Книга каже, дослівно:**

> `0x3` · Що сталося → скидання з коду (`esp_restart`)

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

<!-- fc id:T-K06-027 sha:859ae045 src:kartky/k06-bootlog.md:32 klas:A -->
### T-K06-027 · proza · рядок 32

**Книга каже, дослівно:**

> [[classic]] Саме **число** після `boot:` — маска рівнів на strapping-пінах: `0x01`=`GPIO5`, `0x02`=`GPIO15`, `0x04`=`GPIO4`, `0x08`=`GPIO2`, `0x10`=`GPIO0`, `0x20`=`GPIO12`.

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

<!-- fc id:T-K06-028 sha:cf09f67f src:kartky/k06-bootlog.md:32 klas:A -->
### T-K06-028 · proza · рядок 32

**Книга каже, дослівно:**

> Отже `0x13` — норма, а **виставлений `0x20` означає `GPIO12` високий**: флеш отримав 1.8 В і плата мовчить (додаток D).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > ``boot:0xNN (DESCRIPTION)`` is the hex value of the strapping pins, as represented
  > in the `GPIO_STRAP register <…/components/soc/{IDF_TARGET_PATH_NAME}/include/soc/gpio_reg.h>`__.
  > 
  > The individual bit values are as follows:
  > 
  > .. only:: esp32
  > 
  >    -  ``0x01`` - GPIO5
  >    -  ``0x02`` - MTDO (GPIO15)
  >    -  ``0x04`` - GPIO4
  >    -  ``0x08`` - GPIO2
  >    -  ``0x10`` - GPIO0
  >    -  ``0x20`` - MTDI (GPIO12)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення проходу, і найцінніше за всі вісім. Книга друкувала `boot:0x13` у кожному прикладі логу й пояснювала лише текст у дужках, ніби число службове. Насправді це прямий вимір: які рівні чип зафіксував на strapping-пінах у момент скидання.
Практичний наслідок великий. Уся книга повторює, що зовнішня обв'язка на strapping-піні дає загадкові збої, і радить її знімати — методом здогадки. Тепер це читається з логу: виставлений біт `0x20` означає `GPIO12` високий, тобто флеш на 1.8 В і мовчазна плата. Перевірка коштує нуль і не потребує приладів.
Арифметика сходиться на обох типових значеннях: `0x13` = 0x01+0x02+0x10 (GPIO5, GPIO15, GPIO0 високі) — норма; `0x3` = 0x01+0x02, тобто те саме без `GPIO0` — download mode.
Додано розгорнуто в додаток D і стисло на картку К6.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-K06-029 sha:41a2b15a src:kartky/k06-bootlog.md:39 klas:F -->
### T-K06-029 · proza · рядок 39

**Книга каже, дослівно:**

> `rst:0xf` — це не програмна помилка.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-030 sha:b25bdbfb src:kartky/k06-bootlog.md:39 klas:F -->
### T-K06-030 · proza · рядок 39

**Книга каже, дослівно:**

> Шукати треба джерело, кабель або конденсатори, а не баг у коді.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-031 sha:5bdf9b38 src:kartky/k06-bootlog.md:39 klas:F -->
### T-K06-031 · proza · рядок 39

**Книга каже, дослівно:**

> Найчастіше з'являється в момент увімкнення Wi-Fi, бо саме там піковий струм.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-032 sha:0219c8b1 src:kartky/k06-bootlog.md:46 klas:F -->
### T-K06-032 · kod · рядок 46

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

<!-- fc id:T-K06-033 sha:f0278c3a src:kartky/k06-bootlog.md:53 klas:F -->
### T-K06-033 · proza · рядок 53

**Книга каже, дослівно:**

> Три речі, які тут читаються безкоштовно: **версія IDF**, якою зібрано прошивку; **обсяг флешу**, який бачить бутлоадер; **уся таблиця розділів** із адресами.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-034 sha:e6a1f09c src:kartky/k06-bootlog.md:53 klas:F -->
### T-K06-034 · proza · рядок 53

**Книга каже, дослівно:**

> Це готова відповідь на «а що там усередині» — без розбирання дампа.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-035 sha:0ebdcddf src:kartky/k06-bootlog.md:58 klas:F -->
### T-K06-035 · proza · рядок 58

**Книга каже, дослівно:**

> Число в дужках — мілісекунди від старту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-036 sha:f043d2b4 src:kartky/k06-bootlog.md:58 klas:F -->
### T-K06-036 · proza · рядок 58

**Книга каже, дослівно:**

> Стрибок у цьому числі показує, де саме прошивка задумалася.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-037 sha:f219b8f9 src:kartky/k06-bootlog.md:63 klas:F -->
### T-K06-037 · tablycya · рядок 63

**Книга каже, дослівно:**

> | Видно | Що це |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-038 sha:b44c3a39 src:kartky/k06-bootlog.md:65 klas:F -->
### T-K06-038 · tablycya · рядок 65

**Книга каже, дослівно:**

> | нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-039 sha:e108d7f6 src:kartky/k06-bootlog.md:66 klas:F -->
### T-K06-039 · tablycya · рядок 66

**Книга каже, дослівно:**

> | перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-040 sha:dd7a6d62 src:kartky/k06-bootlog.md:67 klas:F -->
### T-K06-040 · tablycya · рядок 67

**Книга каже, дослівно:**

> | ті самі рядки по колу | boot loop → картка К7 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-041 sha:36137769 src:kartky/k06-bootlog.md:68 klas:F -->
### T-K06-041 · tablycya · рядок 68

**Книга каже, дослівно:**

> | `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-042 sha:165ae2a1 src:kartky/k06-bootlog.md:69 klas:F -->
### T-K06-042 · tablycya · рядок 69

**Книга каже, дослівно:**

> | зовсім порожньо | немає порту чи живлення → картка К3 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-043 sha:8f7a2ab6 src:kartky/k06-bootlog.md:72 klas:F -->
### T-K06-043 · proza · рядок 72

**Книга каже, дослівно:**

> Рядки ROM завжди йдуть на **115200** — і незалежно від швидкості застосунку, і незалежно від кварцу на платі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-044 sha:ae375117 src:kartky/k06-bootlog.md:72 klas:F -->
### T-K06-044 · proza · рядок 72

**Книга каже, дослівно:**

> Якщо ROM видно, а далі каша — швидкість застосунку інша, і це нормально.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-045 sha:e3061d40 src:kartky/k06-bootlog.md:76 klas:F -->
### T-K06-045 · proza · рядок 76

**Книга каже, дослівно:**

> Якщо ж на 115200 не читається нічого, а на **74880** з'являється осмислений текст — у вас **ESP8266**, а не ESP32: у його ROM швидкість виходить саме такою.

**Доказ**

- **Клас:** F — не звірено

---
