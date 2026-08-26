# Фактчекінг: `dodatky/d-panik.md`

Одиниць твердження: **169**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-D-001 sha:12851aa7 src:dodatky/d-panik.md:3 klas:F -->
### T-D-001 · proza · рядок 3

**Книга каже, дослівно:**

> Розгорнута версія карток [К6](#k-bootlog) і [К7](#k-panika).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-002 sha:c9f6a4e2 src:dodatky/d-panik.md:3 klas:F -->
### T-D-002 · proza · рядок 3

**Книга каже, дослівно:**

> Пояснення — розділи 16 і 26.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-003 sha:fa25e155 src:dodatky/d-panik.md:8 klas:F -->
### T-D-003 · proza · рядок 8

**Книга каже, дослівно:**

> Числові коди з ROM-заголовка ESP-IDF (enum `RESET_REASON`), [[classic]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-004 sha:1b3814f6 src:dodatky/d-panik.md:10 klas:F -->
### T-D-004 · tablycya-shapka · рядок 10

**Книга каже, дослівно:**

> | Код | Назва | Що сталося | Що робити |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-005 sha:508894ad src:dodatky/d-panik.md:11 klas:A -->
### T-D-005 · komirka · рядок 11

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

<!-- fc id:T-D-006 sha:d090e5b8 src:dodatky/d-panik.md:11 klas:F -->
### T-D-006 · komirka · рядок 11

**Книга каже, дослівно:**

> `0x1` · Що сталося → подано живлення або `EN`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-007 sha:7431c283 src:dodatky/d-panik.md:11 klas:F -->
### T-D-007 · komirka · рядок 11

**Книга каже, дослівно:**

> `0x1` · Що робити → норма

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-008 sha:1baef394 src:dodatky/d-panik.md:12 klas:F -->
### T-D-008 · komirka · рядок 12

**Книга каже, дослівно:**

> `0x3` · Назва → SW_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-009 sha:16e24570 src:dodatky/d-panik.md:12 klas:A -->
### T-D-009 · komirka · рядок 12

**Книга каже, дослівно:**

> `0x3` · Що сталося → `esp_restart()` з коду

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

<!-- fc id:T-D-010 sha:03a89bab src:dodatky/d-panik.md:12 klas:F -->
### T-D-010 · komirka · рядок 12

**Книга каже, дослівно:**

> `0x3` · Що робити → норма, якщо ваша

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-011 sha:7add9e17 src:dodatky/d-panik.md:13 klas:F -->
### T-D-011 · komirka · рядок 13

**Книга каже, дослівно:**

> `0x4` · Назва → OWDT_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-012 sha:3ae2fadd src:dodatky/d-panik.md:13 klas:F -->
### T-D-012 · komirka · рядок 13

**Книга каже, дослівно:**

> `0x4` · Що сталося → застарілий watchdog

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-013 sha:b04df11d src:dodatky/d-panik.md:13 klas:F -->
### T-D-013 · komirka · рядок 13

**Книга каже, дослівно:**

> `0x4` · Що робити → рідко

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-014 sha:60cc5d87 src:dodatky/d-panik.md:14 klas:F -->
### T-D-014 · komirka · рядок 14

**Книга каже, дослівно:**

> `0x5` · Назва → DEEPSLEEP_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-015 sha:d01aac01 src:dodatky/d-panik.md:14 klas:F -->
### T-D-015 · komirka · рядок 14

**Книга каже, дослівно:**

> `0x5` · Що сталося → прокинувся з deep sleep

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-016 sha:0f8056b3 src:dodatky/d-panik.md:14 klas:F -->
### T-D-016 · komirka · рядок 14

**Книга каже, дослівно:**

> `0x5` · Що робити → норма

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-017 sha:6624efb1 src:dodatky/d-panik.md:15 klas:F -->
### T-D-017 · komirka · рядок 15

**Книга каже, дослівно:**

> `0x6` · Назва → SDIO_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-018 sha:8a61920f src:dodatky/d-panik.md:15 klas:F -->
### T-D-018 · komirka · рядок 15

**Книга каже, дослівно:**

> `0x6` · Що сталося → скидання модулем SLC

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-019 sha:31ae5bdb src:dodatky/d-panik.md:15 klas:F -->
### T-D-019 · komirka · рядок 15

**Книга каже, дослівно:**

> `0x6` · Що робити → рідко

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-020 sha:b13c24c5 src:dodatky/d-panik.md:16 klas:A -->
### T-D-020 · komirka · рядок 16

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

<!-- fc id:T-D-021 sha:3f69134f src:dodatky/d-panik.md:16 klas:F -->
### T-D-021 · komirka · рядок 16

**Книга каже, дослівно:**

> `0x7` · Що сталося → watchdog таймера 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-022 sha:64d8d101 src:dodatky/d-panik.md:16 klas:F -->
### T-D-022 · komirka · рядок 16

**Книга каже, дослівно:**

> `0x7` · Що робити → розділ 32

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-023 sha:a4c80ac9 src:dodatky/d-panik.md:17 klas:F -->
### T-D-023 · komirka · рядок 17

**Книга каже, дослівно:**

> `0x8` · Назва → TG1WDT_SYS_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-024 sha:3253c52a src:dodatky/d-panik.md:17 klas:F -->
### T-D-024 · komirka · рядок 17

**Книга каже, дослівно:**

> `0x8` · Що сталося → watchdog таймера 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-025 sha:67e1a886 src:dodatky/d-panik.md:17 klas:F -->
### T-D-025 · komirka · рядок 17

**Книга каже, дослівно:**

> `0x8` · Що робити → розділ 32

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-026 sha:61c76aaf src:dodatky/d-panik.md:18 klas:F -->
### T-D-026 · komirka · рядок 18

**Книга каже, дослівно:**

> `0x9` · Назва → RTCWDT_SYS_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-027 sha:9b884225 src:dodatky/d-panik.md:18 klas:F -->
### T-D-027 · komirka · рядок 18

**Книга каже, дослівно:**

> `0x9` · Що сталося → RTC watchdog

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-028 sha:abc8094d src:dodatky/d-panik.md:18 klas:F -->
### T-D-028 · komirka · рядок 18

**Книга каже, дослівно:**

> `0x9` · Що робити → розділ 32

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-029 sha:3c9dd369 src:dodatky/d-panik.md:19 klas:F -->
### T-D-029 · komirka · рядок 19

**Книга каже, дослівно:**

> `0xa` · Назва → INTRUSION_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-030 sha:47e8e5d3 src:dodatky/d-panik.md:19 klas:F -->
### T-D-030 · komirka · рядок 19

**Книга каже, дослівно:**

> `0xa` · Що сталося → детектор втручання

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-031 sha:9064117d src:dodatky/d-panik.md:19 klas:F -->
### T-D-031 · komirka · рядок 19

**Книга каже, дослівно:**

> `0xa` · Що робити → рідко

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-032 sha:b1aea164 src:dodatky/d-panik.md:20 klas:F -->
### T-D-032 · komirka · рядок 20

**Книга каже, дослівно:**

> `0xb` · Назва → TGWDT_CPU_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-033 sha:ffe03c46 src:dodatky/d-panik.md:20 klas:F -->
### T-D-033 · komirka · рядок 20

**Книга каже, дослівно:**

> `0xb` · Що сталося → watchdog скинув ядро

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-034 sha:4184159d src:dodatky/d-panik.md:20 klas:F -->
### T-D-034 · komirka · рядок 20

**Книга каже, дослівно:**

> `0xb` · Що робити → розділ 32

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-035 sha:9b73d7e0 src:dodatky/d-panik.md:21 klas:A -->
### T-D-035 · komirka · рядок 21

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

<!-- fc id:T-D-036 sha:382d166f src:dodatky/d-panik.md:21 klas:F -->
### T-D-036 · komirka · рядок 21

**Книга каже, дослівно:**

> `0xc` · Що сталося → програмне скидання ядра

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-037 sha:63b241b6 src:dodatky/d-panik.md:21 klas:F -->
### T-D-037 · komirka · рядок 21

**Книга каже, дослівно:**

> `0xc` · Що робити → **типово після паніки**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-038 sha:b265b468 src:dodatky/d-panik.md:22 klas:F -->
### T-D-038 · komirka · рядок 22

**Книга каже, дослівно:**

> `0xd` · Назва → RTCWDT_CPU_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-039 sha:e72beb66 src:dodatky/d-panik.md:22 klas:F -->
### T-D-039 · komirka · рядок 22

**Книга каже, дослівно:**

> `0xd` · Що сталося → RTC watchdog скинув ядро

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-040 sha:cc29d27d src:dodatky/d-panik.md:22 klas:F -->
### T-D-040 · komirka · рядок 22

**Книга каже, дослівно:**

> `0xd` · Що робити → розділ 32

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-041 sha:5964cff8 src:dodatky/d-panik.md:23 klas:F -->
### T-D-041 · komirka · рядок 23

**Книга каже, дослівно:**

> `0xe` · Назва → EXT_CPU_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-042 sha:111c70cc src:dodatky/d-panik.md:23 klas:F -->
### T-D-042 · komirka · рядок 23

**Книга каже, дослівно:**

> `0xe` · Що сталося → APP CPU скинутий PRO CPU

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-043 sha:47b3fdc0 src:dodatky/d-panik.md:23 klas:F -->
### T-D-043 · komirka · рядок 23

**Книга каже, дослівно:**

> `0xe` · Що робити → норма

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-044 sha:4f167746 src:dodatky/d-panik.md:24 klas:A -->
### T-D-044 · komirka · рядок 24

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

<!-- fc id:T-D-045 sha:00c236fb src:dodatky/d-panik.md:24 klas:F -->
### T-D-045 · komirka · рядок 24

**Книга каже, дослівно:**

> `0xf` · Що сталося → **просіло живлення**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-046 sha:3323a02f src:dodatky/d-panik.md:24 klas:F -->
### T-D-046 · komirka · рядок 24

**Книга каже, дослівно:**

> `0xf` · Що робити → ⚡ розділ 06

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-047 sha:9338f26b src:dodatky/d-panik.md:25 klas:F -->
### T-D-047 · komirka · рядок 25

**Книга каже, дослівно:**

> `0x10` · Назва → RTCWDT_RTC_RESET

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-048 sha:6938bd06 src:dodatky/d-panik.md:25 klas:F -->
### T-D-048 · komirka · рядок 25

**Книга каже, дослівно:**

> `0x10` · Що сталося → RTC watchdog скинув усе

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-049 sha:1e2b3315 src:dodatky/d-panik.md:25 klas:F -->
### T-D-049 · komirka · рядок 25

**Книга каже, дослівно:**

> `0x10` · Що робити → розділ 32

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-050 sha:14e3db2f src:dodatky/d-panik.md:28 klas:F -->
### T-D-050 · proza · рядок 28

**Книга каже, дослівно:**

> Три, що трапляються постійно: `0x1` (норма), `0xc` (після паніки), `0xf` (живлення).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-051 sha:95099304 src:dodatky/d-panik.md:32 klas:F -->
### T-D-051 · proza · рядок 32

**Книга каже, дослівно:**

> `rst:0xf` — це **живлення**, не помилка в коді.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-052 sha:0517766f src:dodatky/d-panik.md:32 klas:F -->
### T-D-052 · proza · рядок 32

**Книга каже, дослівно:**

> Скільки б ви не читали код, причина в джерелі, кабелі або конденсаторах (картка К13).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-053 sha:6f6a5a2e src:dodatky/d-panik.md:36 klas:A -->
### T-D-053 · proza · рядок 36

**Книга каже, дослівно:**

> З коду: `esp_reset_reason()`.

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

<!-- fc id:T-D-054 sha:a826fb3a src:dodatky/d-panik.md:36 klas:F -->
### T-D-054 · proza · рядок 36

**Книга каже, дослівно:**

> Логувати першим рядком `app_main`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-055 sha:9789ed83 src:dodatky/d-panik.md:40 klas:F -->
### T-D-055 · tablycya · рядок 40

**Книга каже, дослівно:**

> | Значення | Що це |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-056 sha:8e00aaa2 src:dodatky/d-panik.md:42 klas:F -->
### T-D-056 · tablycya · рядок 42

**Книга каже, дослівно:**

> | `SPI_FAST_FLASH_BOOT` | звичайний старт із флешу |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-057 sha:bb0d0fd7 src:dodatky/d-panik.md:43 klas:F -->
### T-D-057 · tablycya · рядок 43

**Книга каже, дослівно:**

> | `DOWNLOAD_BOOT(UART0/UART1/...)` | download mode, `GPIO0` низький |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-058 sha:37e0f86d src:dodatky/d-panik.md:47 klas:E -->
### T-D-058 · proza · рядок 47

**Книга каже, дослівно:**

> Найнедооціненіший рядок усього boot-логу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-059 sha:757a0843 src:dodatky/d-panik.md:47 klas:A -->
### T-D-059 · proza · рядок 47

**Книга каже, дослівно:**

> Число після `boot:` — не код режиму, а **бітова маска регістра `GPIO_STRAP`**: рівні, які чип зафіксував на strapping-пінах у момент відпускання скидання.

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

<!-- fc id:T-D-060 sha:7c7d8833 src:dodatky/d-panik.md:51 klas:F -->
### T-D-060 · proza · рядок 51

**Книга каже, дослівно:**

> [[classic]] Для ESP32 classic біти такі:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-061 sha:7431ff81 src:dodatky/d-panik.md:53 klas:F -->
### T-D-061 · tablycya · рядок 53

**Книга каже, дослівно:**

> | Біт | Пін |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-062 sha:714c2e09 src:dodatky/d-panik.md:55 klas:F -->
### T-D-062 · tablycya · рядок 55

**Книга каже, дослівно:**

> | `0x01` | `GPIO5` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-063 sha:681a141a src:dodatky/d-panik.md:56 klas:F -->
### T-D-063 · tablycya · рядок 56

**Книга каже, дослівно:**

> | `0x02` | `GPIO15` (MTDO) |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-064 sha:932a0e72 src:dodatky/d-panik.md:57 klas:F -->
### T-D-064 · tablycya · рядок 57

**Книга каже, дослівно:**

> | `0x04` | `GPIO4` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-065 sha:ad51eef3 src:dodatky/d-panik.md:58 klas:F -->
### T-D-065 · tablycya · рядок 58

**Книга каже, дослівно:**

> | `0x08` | `GPIO2` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-066 sha:64f2d662 src:dodatky/d-panik.md:59 klas:F -->
### T-D-066 · tablycya · рядок 59

**Книга каже, дослівно:**

> | `0x10` | `GPIO0` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-067 sha:4456ba75 src:dodatky/d-panik.md:60 klas:A -->
### T-D-067 · tablycya · рядок 60

**Книга каже, дослівно:**

> | `0x20` | `GPIO12` (MTDI) |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild
- **Дослівно з джерела:**
  > choice BOOTLOADER_VDDSDIO_BOOST
  >     bool "VDDSDIO LDO voltage"
  >     default BOOTLOADER_VDDSDIO_BOOST_1_9V
  >     depends on SOC_CONFIGURABLE_VDDSDIO_SUPPORTED
  >     help
  >         If this option is enabled, and VDDSDIO LDO is set to 1.8V (using eFuse
  >         or MTDI bootstrapping pin), bootloader will change LDO settings to
  >         output 1.9V instead. This helps prevent flash chip from browning out
  >         during flash programming operations.
  > 
  >         This option has no effect if VDDSDIO is set to 3.3V, or if the internal
  >         VDDSDIO regulator is disabled via eFuse.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу — уточнення механізму. Книга писала, що GPIO12 «задає напругу, яку стабілізатор подає на мікросхему флешу», і на цьому зупинялася. Kconfig називає і сам стабілізатор (`VDDSDIO`), і обидва значення: високий рівень MTDI дає **1.8 В**, низький — 3.3 В.
З цього випливає те, чого в книзі не було і що змінює діагностику: плата мовчить не тому, що «пін злий», а тому, що на більшості модулів флеш тривольтовий і від 1.8 В не запускається. На модулі з 1.8-вольтовим флешем той самий рівень — правильний. Тобто «у сусіда працює» тут не доводить нічого. Додано в розділ 07.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-D-068 sha:b26aad81 src:dodatky/d-panik.md:62 klas:E -->
### T-D-068 · proza · рядок 62

**Книга каже, дослівно:**

> Звідси читаються два найчастіші значення:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-069 sha:91d5ab98 src:dodatky/d-panik.md:64 klas:F -->
### T-D-069 · proza · рядок 64

**Книга каже, дослівно:**

> `boot:0x13` = `0x01` + `0x02` + `0x10` — `GPIO5`, `GPIO15` і `GPIO0` високі, решта низькі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-070 sha:b8b5cfd0 src:dodatky/d-panik.md:67 klas:F -->
### T-D-070 · proza · рядок 67

**Книга каже, дослівно:**

> `boot:0x3` = `0x01` + `0x02` — те саме, але **`GPIO0` низький**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-071 sha:bbfc62c6 src:dodatky/d-panik.md:71 klas:E -->
### T-D-071 · proza · рядок 71

**Книга каже, дослівно:**

> Це перетворює здогадки на вимірювання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-072 sha:fcc6bd37 src:dodatky/d-panik.md:71 klas:F -->
### T-D-072 · proza · рядок 71

**Книга каже, дослівно:**

> Уся книга повторює, що зовнішня обв'язка на strapping-піні дає загадкові збої (розділи 07, 16) — а перевірити це можна прямо з логу, не беручи осцилографа.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-073 sha:16e19586 src:dodatky/d-panik.md:75 klas:C -->
### T-D-073 · proza · рядок 75

**Книга каже, дослівно:**

> Найцінніший біт — `0x20`.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-D-074 sha:babcdf0b src:dodatky/d-panik.md:75 klas:F -->
### T-D-074 · proza · рядок 75

**Книга каже, дослівно:**

> Якщо він виставлений, `GPIO12` при старті був високим, а отже флеш отримав 1.8 В замість 3.3 В.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-075 sha:7e109f92 src:dodatky/d-panik.md:75 klas:F -->
### T-D-075 · proza · рядок 75

**Книга каже, дослівно:**

> На більшості модулів це і є причина мовчазної плати (розділ 07).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-076 sha:82e1a535 src:dodatky/d-panik.md:79 klas:F -->
### T-D-076 · proza · рядок 79

**Книга каже, дослівно:**

> Другий за цінністю — `0x04`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-077 sha:f52ac6ce src:dodatky/d-panik.md:79 klas:F -->
### T-D-077 · proza · рядок 79

**Книга каже, дослівно:**

> `GPIO4` не керує режимом завантаження й у переліку strapping-пінів не значиться, але його рівень чип фіксує теж, і в масці він видимий.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-078 sha:75285290 src:dodatky/d-panik.md:79 klas:E -->
### T-D-078 · proza · рядок 79

**Книга каже, дослівно:**

> Для діагностики це безкоштовний зайвий канал спостереження.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-079 sha:d39312ec src:dodatky/d-panik.md:87 klas:K -->
### T-D-079 · kod · рядок 87

**Книга каже, дослівно:**

> ```
> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
> configsip: 0, SPIWP:0xee
> mode:DIO, clock div:2
> load:0x3fff0030,len:1344
> entry 0x400805e4
> I (29) boot: ESP-IDF v6.0.2 2nd stage bootloader
> I (33) boot.esp32: SPI Flash Size : 4MB
> I (52) boot: Partition Table:
> I (56) boot: ## Label            Usage      Type ST Offset   Length
> I (63) boot:  0 nvs              WiFi data    01 02 00009000 00006000
> I (70) boot:  1 phy_init         RF data      01 01 0000f000 00001000
> I (78) boot:  2 factory          factory app  00 00 00010000 00100000
> I (xxx) cpu_start: Pro cpu up.
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

<!-- fc id:T-D-080 sha:490ee98b src:dodatky/d-panik.md:88 klas:A -->
### T-D-080 · kod-ryadok · рядок 88

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

<!-- fc id:T-D-081 sha:825633b5 src:dodatky/d-panik.md:103 klas:F -->
### T-D-081 · proza · рядок 103

**Книга каже, дослівно:**

> Звідси безкоштовно читається: **версія ESP-IDF**, **обсяг флешу очима бутлоадера** і **вся таблиця розділів з адресами** — готова відповідь на «що всередині чужого пристрою» (розділ 24).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-082 sha:0ebdcddf src:dodatky/d-panik.md:107 klas:E -->
### T-D-082 · proza · рядок 107

**Книга каже, дослівно:**

> Число в дужках — мілісекунди від старту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-083 sha:3d92627f src:dodatky/d-panik.md:107 klas:E -->
### T-D-083 · proza · рядок 107

**Книга каже, дослівно:**

> Стрибок показує, де прошивка задумалася.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-084 sha:0590c64d src:dodatky/d-panik.md:112 klas:F -->
### T-D-084 · proza · рядок 112

**Книга каже, дослівно:**

> Рядки нижче — дослівні з ESP-IDF; `%d`, `0x%x` і адреси підставляються.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-085 sha:fbdc8285 src:dodatky/d-panik.md:114 klas:F -->
### T-D-085 · tablycya-shapka · рядок 114

**Книга каже, дослівно:**

> | Повідомлення | Причина | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-086 sha:a63a39c2 src:dodatky/d-panik.md:115 klas:A -->
### T-D-086 · komirka · рядок 115

**Книга каже, дослівно:**

> `image at 0x… has invalid magic byte (nothing flashed here?)` · Причина → за адресою застосунку не образ

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-087 sha:ad4c17ec src:dodatky/d-panik.md:115 klas:A -->
### T-D-087 · komirka · рядок 115

**Книга каже, дослівно:**

> `image at 0x… has invalid magic byte (nothing flashed here?)` · Розділ → 18

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-088 sha:0164e3bb src:dodatky/d-panik.md:116 klas:A -->
### T-D-088 · komirka · рядок 116

**Книга каже, дослівно:**

> `Factory app partition is not bootable` · Причина → застосунку немає

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-089 sha:2d07f5b7 src:dodatky/d-panik.md:116 klas:A -->
### T-D-089 · komirka · рядок 116

**Книга каже, дослівно:**

> `Factory app partition is not bootable` · Розділ → К5

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-090 sha:2bc6cd2b src:dodatky/d-panik.md:117 klas:A -->
### T-D-090 · komirka · рядок 117

**Книга каже, дослівно:**

> `partition N invalid magic number 0x…` · Причина → немає таблиці розділів

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-091 sha:b805a263 src:dodatky/d-panik.md:117 klas:A -->
### T-D-091 · komirka · рядок 117

**Книга каже, дослівно:**

> `partition N invalid magic number 0x…` · Розділ → 18

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-092 sha:47044db6 src:dodatky/d-panik.md:118 klas:A -->
### T-D-092 · komirka · рядок 118

**Книга каже, дослівно:**

> `Failed to verify partition table` · Причина → те саме

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-093 sha:6a21db9c src:dodatky/d-panik.md:118 klas:A -->
### T-D-093 · komirka · рядок 118

**Книга каже, дослівно:**

> `Failed to verify partition table` · Розділ → 18

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-094 sha:168149c9 src:dodatky/d-panik.md:119 klas:A -->
### T-D-094 · komirka · рядок 119

**Книга каже, дослівно:**

> `ota data partition invalid, falling back to factory` · Причина → зіпсований `otadata`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-095 sha:e514eca1 src:dodatky/d-panik.md:119 klas:A -->
### T-D-095 · komirka · рядок 119

**Книга каже, дослівно:**

> `ota data partition invalid, falling back to factory` · Розділ → 19

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-096 sha:2f309750 src:dodatky/d-panik.md:120 klas:A -->
### T-D-096 · komirka · рядок 120

**Книга каже, дослівно:**

> `Image hash failed - image is corrupt` · Причина → образ пошкоджений

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-097 sha:e82565ff src:dodatky/d-panik.md:120 klas:A -->
### T-D-097 · komirka · рядок 120

**Книга каже, дослівно:**

> `Image hash failed - image is corrupt` · Розділ → 17

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-098 sha:c946c98e src:dodatky/d-panik.md:121 klas:A -->
### T-D-098 · komirka · рядок 121

**Книга каже, дослівно:**

> `Detected size(…k) smaller than the size in the binary image header(…k). Probe failed.` · Причина → конфігурація > реальний флеш

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/spi_flash/esp_flash_spi_init.c
- **Дослівно з джерела:**
  > ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the binary image "
  >                     "header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chip_size/1024);
  > ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the binary image "
  >                     "header(%dk). Using the size in the binary image header.", …);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга друкувала `Flash chip size mismatch` — рядка з такою назвою в ESP-IDF немає ніде.
Справжні рядки не лише інші, а ще й **два**, з протилежними наслідками. Реальний флеш менший за налаштований — фатально, проба зупиняється (`ESP_LOGE`). Більший — лише попередження (`ESP_LOGW`), система працює, надлишок не використовується.
Друге — типова доля клонів, що продаються як 16 МБ. Книга подавала обидва випадки одним рядком і одним наслідком; тепер вони розділені.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-099 sha:4adb2806 src:dodatky/d-panik.md:121 klas:A -->
### T-D-099 · komirka · рядок 121

**Книга каже, дослівно:**

> `Detected size(…k) smaller than the size in the binary image header(…k). Probe failed.` · Розділ → 08

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/spi_flash/esp_flash_spi_init.c
- **Дослівно з джерела:**
  > ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the binary image "
  >                     "header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chip_size/1024);
  > ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the binary image "
  >                     "header(%dk). Using the size in the binary image header.", …);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга друкувала `Flash chip size mismatch` — рядка з такою назвою в ESP-IDF немає ніде.
Справжні рядки не лише інші, а ще й **два**, з протилежними наслідками. Реальний флеш менший за налаштований — фатально, проба зупиняється (`ESP_LOGE`). Більший — лише попередження (`ESP_LOGW`), система працює, надлишок не використовується.
Друге — типова доля клонів, що продаються як 16 МБ. Книга подавала обидва випадки одним рядком і одним наслідком; тепер вони розділені.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-100 sha:45fbc80e src:dodatky/d-panik.md:122 klas:A -->
### T-D-100 · komirka · рядок 122

**Книга каже, дослівно:**

> `Detected size(…k) larger than … Using the size in the binary image header.` · Причина → конфігурація < реальний флеш; лише попередження

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/spi_flash/esp_flash_spi_init.c
- **Дослівно з джерела:**
  > ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the binary image "
  >                     "header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chip_size/1024);
  > ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the binary image "
  >                     "header(%dk). Using the size in the binary image header.", …);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга друкувала `Flash chip size mismatch` — рядка з такою назвою в ESP-IDF немає ніде.
Справжні рядки не лише інші, а ще й **два**, з протилежними наслідками. Реальний флеш менший за налаштований — фатально, проба зупиняється (`ESP_LOGE`). Більший — лише попередження (`ESP_LOGW`), система працює, надлишок не використовується.
Друге — типова доля клонів, що продаються як 16 МБ. Книга подавала обидва випадки одним рядком і одним наслідком; тепер вони розділені.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-101 sha:f25a0f20 src:dodatky/d-panik.md:122 klas:A -->
### T-D-101 · komirka · рядок 122

**Книга каже, дослівно:**

> `Detected size(…k) larger than … Using the size in the binary image header.` · Розділ → 08

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/spi_flash/esp_flash_spi_init.c
- **Дослівно з джерела:**
  > ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the binary image "
  >                     "header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chip_size/1024);
  > ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the binary image "
  >                     "header(%dk). Using the size in the binary image header.", …);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга друкувала `Flash chip size mismatch` — рядка з такою назвою в ESP-IDF немає ніде.
Справжні рядки не лише інші, а ще й **два**, з протилежними наслідками. Реальний флеш менший за налаштований — фатально, проба зупиняється (`ESP_LOGE`). Більший — лише попередження (`ESP_LOGW`), система працює, надлишок не використовується.
Друге — типова доля клонів, що продаються як 16 МБ. Книга подавала обидва випадки одним рядком і одним наслідком; тепер вони розділені.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-102 sha:930379a1 src:dodatky/d-panik.md:126 klas:E -->
### T-D-102 · proza · рядок 126

**Книга каже, дослівно:**

> Розбіжність обсягу флешу дає **два різні рядки, і наслідки різні**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-103 sha:6a177d47 src:dodatky/d-panik.md:128 klas:A -->
### T-D-103 · proza · рядок 128

**Книга каже, дослівно:**

> Реальний флеш **менший** за налаштований — фатально: бутлоадер зупиняє пробу, бо частина розділів фізично не існує.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/spi_flash/esp_flash_spi_init.c
- **Дослівно з джерела:**
  > ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the binary image "
  >                     "header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chip_size/1024);
  > ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the binary image "
  >                     "header(%dk). Using the size in the binary image header.", …);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга друкувала `Flash chip size mismatch` — рядка з такою назвою в ESP-IDF немає ніде.
Справжні рядки не лише інші, а ще й **два**, з протилежними наслідками. Реальний флеш менший за налаштований — фатально, проба зупиняється (`ESP_LOGE`). Більший — лише попередження (`ESP_LOGW`), система працює, надлишок не використовується.
Друге — типова доля клонів, що продаються як 16 МБ. Книга подавала обидва випадки одним рядком і одним наслідком; тепер вони розділені.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-104 sha:3a4f06b3 src:dodatky/d-panik.md:131 klas:E -->
### T-D-104 · proza · рядок 131

**Книга каже, дослівно:**

> Реальний флеш **більший** — лише попередження: система працює, просто надлишок не використовується.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-105 sha:898ac6ac src:dodatky/d-panik.md:131 klas:F -->
### T-D-105 · proza · рядок 131

**Книга каже, дослівно:**

> Саме цей випадок трапляється з клонами, що продаються як 16 МБ, а стають 4 МБ у конфігурації.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-106 sha:ea9dc162 src:dodatky/d-panik.md:138 klas:F -->
### T-D-106 · tablycya-shapka · рядок 138

**Книга каже, дослівно:**

> | Причина | Що заборонено | Що шукати |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-107 sha:3f7f05f2 src:dodatky/d-panik.md:139 klas:A -->
### T-D-107 · komirka · рядок 139

**Книга каже, дослівно:**

> `LoadProhibited` · Що заборонено → читання з недійсної адреси

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-108 sha:e1369196 src:dodatky/d-panik.md:139 klas:A -->
### T-D-108 · komirka · рядок 139

**Книга каже, дослівно:**

> `LoadProhibited` · Що шукати → `NULL` або звільнений покажчик

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-109 sha:8bc4f39c src:dodatky/d-panik.md:140 klas:A -->
### T-D-109 · komirka · рядок 140

**Книга каже, дослівно:**

> `StoreProhibited` · Що заборонено → запис за недійсною адресою

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-110 sha:28cc86f2 src:dodatky/d-panik.md:140 klas:A -->
### T-D-110 · komirka · рядок 140

**Книга каже, дослівно:**

> `StoreProhibited` · Що шукати → те саме, на запис

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-111 sha:65e5b66a src:dodatky/d-panik.md:141 klas:A -->
### T-D-111 · komirka · рядок 141

**Книга каже, дослівно:**

> `InstrFetchProhibited` · Що заборонено → перехід на недійсну адресу

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-112 sha:89d4b0ed src:dodatky/d-panik.md:141 klas:A -->
### T-D-112 · komirka · рядок 141

**Книга каже, дослівно:**

> `InstrFetchProhibited` · Що шукати → зіпсований покажчик на функцію

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-113 sha:0e5b84a2 src:dodatky/d-panik.md:142 klas:A -->
### T-D-113 · komirka · рядок 142

**Книга каже, дослівно:**

> `IllegalInstruction` · Що заборонено → виконання не-коду

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-114 sha:b8918b59 src:dodatky/d-panik.md:142 klas:A -->
### T-D-114 · komirka · рядок 142

**Книга каже, дослівно:**

> `IllegalInstruction` · Що шукати → переповнення стека

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-115 sha:c4d149ff src:dodatky/d-panik.md:143 klas:A -->
### T-D-115 · komirka · рядок 143

**Книга каже, дослівно:**

> `LoadStoreAlignment` · Що заборонено → невирівняний доступ

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-116 sha:46508737 src:dodatky/d-panik.md:143 klas:A -->
### T-D-116 · komirka · рядок 143

**Книга каже, дослівно:**

> `LoadStoreAlignment` · Що шукати → 32 біти з непарної адреси

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-117 sha:d96111a7 src:dodatky/d-panik.md:144 klas:A -->
### T-D-117 · komirka · рядок 144

**Книга каже, дослівно:**

> `IntegerDivideByZero` · Що заборонено → ділення на нуль

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-118 sha:439a9b98 src:dodatky/d-panik.md:144 klas:A -->
### T-D-118 · komirka · рядок 144

**Книга каже, дослівно:**

> `IntegerDivideByZero` · Що шукати → дільник із датчика без перевірки

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-119 sha:7c359228 src:dodatky/d-panik.md:145 klas:F -->
### T-D-119 · komirka · рядок 145

**Книга каже, дослівно:**

> `Interrupt wdt timeout` · Що заборонено → переривання заблоковані задовго

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-120 sha:4c606b3e src:dodatky/d-panik.md:145 klas:F -->
### T-D-120 · komirka · рядок 145

**Книга каже, дослівно:**

> `Interrupt wdt timeout` · Що шукати → довгий ISR, критична секція

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-121 sha:8712f714 src:dodatky/d-panik.md:146 klas:A -->
### T-D-121 · komirka · рядок 146

**Книга каже, дослівно:**

> `Cache disabled but cached memory region accessed` · Що заборонено → доступ до флешу при вимкненому кеші

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-122 sha:4e40193e src:dodatky/d-panik.md:146 klas:A -->
### T-D-122 · komirka · рядок 146

**Книга каже, дослівно:**

> `Cache disabled but cached memory region accessed` · Що шукати → немає `IRAM_ATTR`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/FreeRTOS-Kernel/include/freertos/{task,queue,semphr,event_groups,timers}.h та components/esp_common/include/esp_attr.h
- **Дослівно з джерела:**
  > Усі 15 викликів FreeRTOS, що вживає книга, знайдено в заголовках ядра.
  > Макроси:
  >   #define IRAM_ATTR _SECTION_ATTR_IMPL(".iram1", __COUNTER__)
  >   #define RTC_DATA_ATTR _SECTION_ATTR_IMPL(".rtc.data", __COUNTER__)
  >   #define configMAX_PRIORITIES ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** `RTC_DATA_ATTR` кладе змінну в секцію `.rtc.data` — це і є механічне підтвердження того, чому вона переживає deep sleep, тоді як звичайна змінна не переживає. `IRAM_ATTR` кладе функцію в `.iram1`, звідки вона виконується при вимкненому кеші флешу.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-D-123 sha:a66ac160 src:dodatky/d-panik.md:151 klas:F -->
### T-D-123 · tablycya · рядок 151

**Книга каже, дослівно:**

> | Поле | Що означає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-124 sha:9e0b8e4a src:dodatky/d-panik.md:153 klas:F -->
### T-D-124 · tablycya · рядок 153

**Книга каже, дослівно:**

> | `PC` | адреса інструкції, на якій упало — **де** |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-125 sha:f82d7189 src:dodatky/d-panik.md:154 klas:F -->
### T-D-125 · tablycya · рядок 154

**Книга каже, дослівно:**

> | `EXCVADDR` | адреса, за якою зверталися — **куди** |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-126 sha:74974165 src:dodatky/d-panik.md:155 klas:F -->
### T-D-126 · tablycya · рядок 155

**Книга каже, дослівно:**

> | `A1` | вказівник стека |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-127 sha:b89ae2bf src:dodatky/d-panik.md:156 klas:F -->
### T-D-127 · tablycya · рядок 156

**Книга каже, дослівно:**

> | `Backtrace` | ланцюжок `адреса:стек`, читати знизу вгору |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-128 sha:6ef4b75c src:dodatky/d-panik.md:159 klas:F -->
### T-D-128 · proza · рядок 159

**Книга каже, дослівно:**

> **`EXCVADDR` — найшвидша підказка.**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-129 sha:f710df6f src:dodatky/d-panik.md:161 klas:C -->
### T-D-129 · proza · рядок 161

**Книга каже, дослівно:**

> Близько нуля (`0x0`–`0x40`) → розіменування `NULL` зі зсувом поля структури.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-D-130 sha:4c0a3cc5 src:dodatky/d-panik.md:161 klas:A -->
### T-D-130 · proza · рядок 161

**Книга каже, дослівно:**

> Це покриває більшість `LoadProhibited` на практиці.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-131 sha:7ff566f8 src:dodatky/d-panik.md:164 klas:E -->
### T-D-131 · proza · рядок 164

**Книга каже, дослівно:**

> Схожа на осмислену адресу, але доступ заборонено → покажчик на вже звільнену пам'ять.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-132 sha:d09dfd9d src:dodatky/d-panik.md:170 klas:E -->
### T-D-132 · proza · рядок 170

**Книга каже, дослівно:**

> **Task WDT** — задача не віддає керування:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-133 sha:655ff0e7 src:dodatky/d-panik.md:172 klas:K -->
### T-D-133 · kod · рядок 172

**Книга каже, дослівно:**

> ```
> E (5234) task_wdt: Task watchdog got triggered. The following tasks/users
> did not reset the watchdog in time:
> E (5234) task_wdt:  - IDLE0 (CPU 0)
> E (5234) task_wdt: Tasks currently running:
> E (5234) task_wdt: CPU 0: my_task
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-134 sha:a1afa6b3 src:dodatky/d-panik.md:175 klas:F -->
### T-D-134 · kod-ryadok · рядок 175

**Книга каже, дослівно:**

> E (5234) task_wdt:  - IDLE0 (CPU 0)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-135 sha:b8253fd9 src:dodatky/d-panik.md:180 klas:A -->
### T-D-135 · proza · рядок 180

**Книга каже, дослівно:**

> Переліків тут **два, і вони різні**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-136 sha:d413fc69 src:dodatky/d-panik.md:180 klas:A -->
### T-D-136 · proza · рядок 180

**Книга каже, дослівно:**

> Після першого рядка — ті, хто не встиг погодувати watchdog (`IDLE0` — потерпілий).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-137 sha:15a9044c src:dodatky/d-panik.md:180 klas:A -->
### T-D-137 · proza · рядок 180

**Книга каже, дослівно:**

> Після `Tasks currently running:` — те, що виконувалося в цю мить, і саме там винуватець: `my_task`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-138 sha:12db62c5 src:dodatky/d-panik.md:185 klas:E -->
### T-D-138 · proza · рядок 185

**Книга каже, дослівно:**

> Це діагностика, а не смерть системи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-139 sha:77e4f2d7 src:dodatky/d-panik.md:187 klas:E -->
### T-D-139 · proza · рядок 187

**Книга каже, дослівно:**

> **Interrupt WDT** — переривання заблоковані:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-140 sha:113645cd src:dodatky/d-panik.md:189 klas:K -->
### T-D-140 · kod · рядок 189

**Книга каже, дослівно:**

> ```
> Guru Meditation Error: Core 0 panic'ed (Interrupt wdt timeout on CPU0)
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-141 sha:61ffbc10 src:dodatky/d-panik.md:193 klas:F -->
### T-D-141 · proza · рядок 193

**Книга каже, дослівно:**

> Причини: важкий код в ISR, довга критична секція, виклик забороненого в ISR (розділ 31).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-142 sha:ef04690f src:dodatky/d-panik.md:198 klas:F -->
### T-D-142 · tablycya · рядок 198

**Книга каже, дослівно:**

> | Повідомлення | Причина |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-143 sha:200e947a src:dodatky/d-panik.md:200 klas:A -->
### T-D-143 · tablycya · рядок 200

**Книга каже, дослівно:**

> | `***ERROR*** A stack overflow in task X has been detected.` | замалий стек задачі |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-144 sha:6747d938 src:dodatky/d-panik.md:201 klas:A -->
### T-D-144 · tablycya · рядок 201

**Книга каже, дослівно:**

> | `CORRUPT HEAP: Bad tail at 0x… Expected 0x… got 0x…` | запис **за** кінець блоку |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-145 sha:0e926220 src:dodatky/d-panik.md:202 klas:A -->
### T-D-145 · tablycya · рядок 202

**Книга каже, дослівно:**

> | `CORRUPT HEAP: Bad head at 0x…` | запис **перед** початком блоку |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-146 sha:c629c9be src:dodatky/d-panik.md:203 klas:A -->
### T-D-146 · tablycya · рядок 203

**Книга каже, дослівно:**

> | `Guru Meditation ... IllegalInstruction` | часто теж переповнення стека |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-147 sha:69aa2c68 src:dodatky/d-panik.md:204 klas:F -->
### T-D-147 · tablycya · рядок 204

**Книга каже, дослівно:**

> | `assert failed: ...` | порушено внутрішній інваріант |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-148 sha:4dc00872 src:dodatky/d-panik.md:205 klas:A -->
### T-D-148 · tablycya · рядок 205

**Книга каже, дослівно:**

> | `heap_caps_malloc failed` | немає пам'яті або немає блоку потрібного розміру |

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

<!-- fc id:T-D-149 sha:1e8945f3 src:dodatky/d-panik.md:208 klas:A -->
### T-D-149 · proza · рядок 208

**Книга каже, дослівно:**

> `Bad head` і `Bad tail` — не однакові повідомлення.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-150 sha:7076a5df src:dodatky/d-panik.md:208 klas:A -->
### T-D-150 · proza · рядок 208

**Книга каже, дослівно:**

> Купа тримає навколо кожного блоку контрольні слова-канарки, і зіпсована каже, з якого боку писали повз.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-151 sha:dbf57f9c src:dodatky/d-panik.md:212 klas:A -->
### T-D-151 · proza · рядок 212

**Книга каже, дослівно:**

> `Bad tail` — типове переповнення буфера: писали далі, ніж виділили.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-152 sha:68e01a8c src:dodatky/d-panik.md:212 klas:F -->
### T-D-152 · proza · рядок 212

**Книга каже, дослівно:**

> Шукати `memcpy`, `sprintf`, цикл із `<=` замість `<`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-153 sha:123d0b6e src:dodatky/d-panik.md:215 klas:A -->
### T-D-153 · proza · рядок 215

**Книга каже, дослівно:**

> `Bad head` — писали **до** початку блоку: від'ємний індекс, зсув покажчика назад, звільнення чужої адреси.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-154 sha:290e2e50 src:dodatky/d-panik.md:215 klas:E -->
### T-D-154 · proza · рядок 215

**Книга каже, дослівно:**

> Трапляється рідше й майже завжди означає помилку в арифметиці покажчиків.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-155 sha:0140364c src:dodatky/d-panik.md:219 klas:A -->
### T-D-155 · proza · рядок 219

**Книга каже, дослівно:**

> Адреса в повідомленні — це адреса канарки, тобто край самого блоку.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- **Дослівно з джерела:**
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad head at %p. Expected 0x%08x got 0x%08x\n", …);
  > MULTI_HEAP_STDERR_PRINTF("CORRUPT HEAP: Bad tail at %p. Expected 0x%08x got 0x%08x\n", …);
  > 
  > #define ERR_STR1 "***ERROR*** A stack overflow in task "
  > #define ERR_STR2 " has been detected."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і практично корисне. Книга мала один рядок `CORRUPT HEAP`, тоді як купа каже, **з якого боку** писали повз: `Bad tail` — за кінець блоку (класичне переповнення буфера), `Bad head` — перед початком (від'ємний індекс, арифметика покажчиків).
Це звужує пошук удвічі й не коштує нічого. Додано в додаток D блоком уваги разом із поясненням, що адреса в рядку — це адреса канарки, тобто край блоку.
Рядок про переповнення стека доповнено до повного: `… has been detected.`
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-D-156 sha:a135e9c8 src:dodatky/d-panik.md:219 klas:F -->
### T-D-156 · proza · рядок 219

**Книга каже, дослівно:**

> Її можна порівняти з тим, що повернув `malloc`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-157 sha:760e202b src:dodatky/d-panik.md:223 klas:A -->
### T-D-157 · proza · рядок 223

**Книга каже, дослівно:**

> Діагностика — розділ 30: `uxTaskGetStackHighWaterMark`, `heap_caps_get_largest_free_block`.

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

<!-- fc id:T-D-158 sha:cbdc8d7f src:dodatky/d-panik.md:228 klas:F -->
### T-D-158 · proza · рядок 228

**Книга каже, дослівно:**

> **`rst:` у першому рядку.** Живлення, watchdog чи паніка — три різні шляхи. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-159 sha:61db3e19 src:dodatky/d-panik.md:228 klas:F -->
### T-D-159 · proza · рядок 228

**Книга каже, дослівно:**

> **Причина паніки і `EXCVADDR`.** Часто відповідь уже тут. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-160 sha:8d7da41f src:dodatky/d-panik.md:228 klas:F -->
### T-D-160 · proza · рядок 228

**Книга каже, дослівно:**

> **Backtrace через `.elf`** того самого збирання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-161 sha:223bf487 src:dodatky/d-panik.md:228 klas:F -->
### T-D-161 · proza · рядок 228

**Книга каже, дослівно:**

> **Відтворити.** Збій, який не відтворюється, не полагоджений. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-162 sha:6a7c80ec src:dodatky/d-panik.md:228 klas:E -->
### T-D-162 · proza · рядок 228

**Книга каже, дослівно:**

> Не відтворюється → coredump і логування переходів станів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-163 sha:4304fde6 src:dodatky/d-panik.md:236 klas:F -->
### T-D-163 · proza · рядок 236

**Книга каже, дослівно:**

> Без `.elf` **того самого збирання** backtrace нерозшифровний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-164 sha:91a1f9a6 src:dodatky/d-panik.md:236 klas:E -->
### T-D-164 · proza · рядок 236

**Книга каже, дослівно:**

> Перезібраний «такий самий» проєкт не підходить: адреси зсуваються від будь-якої зміни тулчейну чи бібліотеки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-165 sha:00df861d src:dodatky/d-panik.md:240 klas:F -->
### T-D-165 · proza · рядок 240

**Книга каже, дослівно:**

> `.elf` зберігається разом із кожним образом, що поїхав (розділ 21).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-166 sha:9a6f1773 src:dodatky/d-panik.md:245 klas:E -->
### T-D-166 · proza · рядок 245

**Книга каже, дослівно:**

> Дивитися **найперший** дамп після подачі живлення: відкрити монітор, **потім** подати живлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-167 sha:c50282dd src:dodatky/d-panik.md:245 klas:E -->
### T-D-167 · proza · рядок 245

**Книга каже, дослівно:**

> У першому — причина, в решті — наслідки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-168 sha:71f2dcf5 src:dodatky/d-panik.md:248 klas:F -->
### T-D-168 · proza · рядок 248

**Книга каже, дослівно:**

> Швидке відсікання: залити свідомо справний мінімальний образ (`hello_world`).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-D-169 sha:d8b5c935 src:dodatky/d-panik.md:248 klas:F -->
### T-D-169 · proza · рядок 248

**Книга каже, дослівно:**

> Працює — справа в прошивці; ні — у залізі чи живленні (розділ 20).

**Доказ**

- **Клас:** F — не звірено

---
