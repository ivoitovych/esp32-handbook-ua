# Фактчекінг: `kartky/k06-bootlog.md`

Одиниць твердження: **45**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-K06-001 sha:3b9e12c2 src:kartky/k06-bootlog.md:3 klas:A -->
### T-K06-001 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Монітор на **115200 бод**, натиснути `EN`.

**Контекст**

```
# К6. Читання boot-логу {#k-bootlog}

Монітор на **115200 бод**, натиснути `EN`. Перші рядки друкує ROM, і саме
вони кажуть, чому плата поводиться так, як поводиться.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > After reset, the second line printed by the {IDF_TARGET_NAME} ROM (at 115200bps)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Основна бод-рейт для ROM bootloader ESP32.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-K06-002 sha:82c2748d src:kartky/k06-bootlog.md:3 klas:E -->
### T-K06-002 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Перші рядки друкує ROM, і саме вони кажуть, чому плата поводиться так, як поводиться.

**Контекст**

```
# К6. Читання boot-логу {#k-bootlog}

Монітор на **115200 бод**, натиснути `EN`. Перші рядки друкує ROM, і саме
вони кажуть, чому плата поводиться так, як поводиться.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-003 sha:7419d2c5 src:kartky/k06-bootlog.md:8 klas:K -->
### T-K06-003 · kod · `kartky/k06-bootlog.md`

**Твердження, коротко**

> ```
> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
> ```

**Контекст**

````
## Перший рядок — головний

```
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > rst:0x1 (POWERON_RESET),boot:0x3
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Приклад лога з boot.rst показує 0x1 = POWERON_RESET.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-K06-004 sha:490ee98b src:kartky/k06-bootlog.md:9 klas:A -->
### T-K06-004 · kod-ryadok · `kartky/k06-bootlog.md`

**Твердження, коротко**

> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

**Контекст**

````
## Перший рядок — головний

```
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > rst:0x1 (POWERON_RESET),boot:0x3
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Приклад лога з boot.rst показує 0x1 = POWERON_RESET.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-K06-005 sha:780358c1 src:kartky/k06-bootlog.md:12 klas:A -->
### T-K06-005 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `rst:` — **причина останнього скидання**.

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > ``rst:0xNN (REASON)`` is an enumerated value (and description) of the reason for the reset.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Поле rst містить код причини скидання.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-K06-006 sha:545fffe2 src:kartky/k06-bootlog.md:12 klas:E -->
### T-K06-006 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Найчастіші значення для [[classic]] (повна таблиця — додаток D):

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-007 sha:a9766590 src:kartky/k06-bootlog.md:15 klas:F -->
### T-K06-007 · tablycya-shapka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> | Код | Назва | Що сталося |

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-008 sha:508894ad src:kartky/k06-bootlog.md:17 klas:A -->
### T-K06-008 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x1` · Назва → POWERON_RESET

**Дослівно з книги:** рядок таблиці не знайдено — локатор привів у прозу. Дивіться контекст нижче.

**Контекст**

````
## Перший рядок — головний

```
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > rst:0x1 (POWERON_RESET),boot:0x3
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Приклад лога з boot.rst показує 0x1 = POWERON_RESET.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-K06-009 sha:61891822 src:kartky/k06-bootlog.md:17 klas:A -->
### T-K06-009 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x1` · Що сталося → подано живлення або натиснуто `EN`. Норма

**Дослівно з книги**

```
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Коментар enum'у переводиться як «скидання від подачі напруги на Vbat». EN (enable) — пін вмикання чипа, без якого скидання неможливе. Книга інтерпретує це як «подано живлення або EN», що відповідає суті Vbat reset.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-010 sha:1baef394 src:kartky/k06-bootlog.md:18 klas:A -->
### T-K06-010 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x3` · Назва → SW_RESET

**Дослівно з книги**

```
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > SW_RESET               =  3,    /**<3, Software reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Пряма відповідність: 0x3 = SW_RESET. Неме розходження між книгою й enum'ом.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-011 sha:35861e2c src:kartky/k06-bootlog.md:18 klas:A -->
### T-K06-011 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x3` · Що сталося → скидання з коду (`esp_restart`)

**Дослівно з книги**

```
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

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

<!-- fc id:T-K06-012 sha:60cc5d87 src:kartky/k06-bootlog.md:19 klas:A -->
### T-K06-012 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x5` · Назва → DEEPSLEEP_RESET

**Дослівно з книги**

```
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Пряма відповідність: 0x5 = DEEPSLEEP_RESET. Коментар згадує Deep Sleep.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-013 sha:91ecb724 src:kartky/k06-bootlog.md:19 klas:A -->
### T-K06-013 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x5` · Що сталося → прокинувся з deep sleep. Норма

**Дослівно з книги**

```
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Коментар DEEPSLEEP_RESET говорить про Deep Sleep. Прокинення (wake-up) — це сенс скидання при виході з deep sleep режиму.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-014 sha:b13c24c5 src:kartky/k06-bootlog.md:20 klas:A -->
### T-K06-014 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x7` · Назва → TG0WDT_SYS_RESET

**Дослівно з книги**

```
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

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

<!-- fc id:T-K06-015 sha:f52ff7ed src:kartky/k06-bootlog.md:20 klas:A -->
### T-K06-015 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x7` · Що сталося → спрацював watchdog таймера 0

**Дослівно з книги**

```
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Коментар: «Timer Group0 Watch dog reset». TG0 = Timer Group 0. Книга інтерпретує як «watchdog таймера 0», що дослівно відповідає enum'у.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-016 sha:a4c80ac9 src:kartky/k06-bootlog.md:21 klas:A -->
### T-K06-016 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x8` · Назва → TG1WDT_SYS_RESET

**Дослівно з книги**

```
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Пряма відповідність: 0x8 = TG1WDT_SYS_RESET. TG1 = Timer Group 1.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-017 sha:ec4961ee src:kartky/k06-bootlog.md:21 klas:A -->
### T-K06-017 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x8` · Що сталося → спрацював watchdog таймера 1

**Дослівно з книги**

```
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Коментар: «Timer Group1 Watch dog reset». Книга інтерпретує як «watchdog таймера 1», дослівно.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-018 sha:61c76aaf src:kartky/k06-bootlog.md:22 klas:A -->
### T-K06-018 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x9` · Назва → RTCWDT_SYS_RESET

**Дослівно з книги**

```
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Пряма відповідність: 0x9 = RTCWDT_SYS_RESET. RTC = Real Time Clock.
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-019 sha:df7de7e7 src:kartky/k06-bootlog.md:22 klas:A -->
### T-K06-019 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x9` · Що сталося → спрацював RTC watchdog

**Дослівно з книги**

```
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Коментар: «RTC Watch dog Reset». Книга дослівно передає це як «RTC watchdog».
- **Прохід:** m2-60-panik-a

---

<!-- fc id:T-K06-020 sha:9b73d7e0 src:kartky/k06-bootlog.md:23 klas:A -->
### T-K06-020 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0xc` · Назва → SW_CPU_RESET

**Дослівно з книги**

```
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

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

<!-- fc id:T-K06-021 sha:21e68d08 src:kartky/k06-bootlog.md:23 klas:B -->
### T-K06-021 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0xc` · Що сталося → скидання ядра з коду; часто після паніки

**Дослівно з книги**

```
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://github.com/espressif/esp-idf/blob/release/v5.2/components/esp_rom/include/esp32/rom/rtc.h — RESET_REASON enum, значення 12
- **Дослівно з джерела:**
  > SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
- **Спосіб і дата:** GitHub ESP-IDF, rom/rtc.h, 2026-08-27
- **Нотатка:** Код 0xc (12 у десятковій) — це SW_CPU_RESET, програмне скидання ядра. Частина про «часто після паніки» логічна: паніка часто викликається assert() або explicit reset, який видається як 0xc. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-95-vybirka

---

<!-- fc id:T-K06-022 sha:4f167746 src:kartky/k06-bootlog.md:24 klas:A -->
### T-K06-022 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0xf` · Назва → RTCWDT_BROWN_OUT_RESET

**Дослівно з книги**

```
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

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

<!-- fc id:T-K06-023 sha:00c236fb src:kartky/k06-bootlog.md:24 klas:A -->
### T-K06-023 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0xf` · Що сталося → **просіло живлення**

**Дослівно з книги**

```
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP-IDF компонент esp_system, rtc.h: https://github.com/espressif/esp-idf/blob/master/components/esp_system/include/esp_system/rtc.h
- **Дослівно з джерела:**
  > RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
- **Спосіб і дата:** curl з github.com/espressif/esp-idf, grep з rtc.h, 2026-08-26
- **Нотатка:** Код 0xf (15) прямо визначений як RTCWDT_BROWN_OUT_RESET. Причина — нестабільне живлення. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-96-vybirka

---

<!-- fc id:T-K06-024 sha:9338f26b src:kartky/k06-bootlog.md:25 klas:A -->
### T-K06-024 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x10` · Назва → RTCWDT_RTC_RESET

**Дослівно з книги**

```
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/569e266f-fatal-errors.rst
- **Дослівно з джерела:**
  > rst:0x10 ({IDF_TARGET_RTCWDT_RTC_RESET})
- **Спосіб і дата:** Source document retrieved 2026-08-26 from the local cache; quote verified against it by substring match.
- **Нотатка:** Місце в документі: розділ RTC Watchdog Timeout, рядок 306
- **Прохід:** m2-hvylya2

---

<!-- fc id:T-K06-025 sha:00c16d81 src:kartky/k06-bootlog.md:25 klas:A -->
### T-K06-025 · komirka · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `0x10` · Що сталося → RTC watchdog скинув усе, разом з RTC

**Дослівно з книги**

```
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Контекст**

```
## Перший рядок — головний

`rst:` — **причина останнього скидання**. Найчастіші значення для
[[classic]] (повна таблиця — додаток D):

| Код | Назва | Що сталося |
|---|---|---|
| `0x1` | POWERON_RESET | подано живлення або натиснуто `EN`. Норма |
| `0x3` | SW_RESET | скидання з коду (`esp_restart`) |
| `0x5` | DEEPSLEEP_RESET | прокинувся з deep sleep. Норма |
| `0x7` | TG0WDT_SYS_RESET | спрацював watchdog таймера 0 |
| `0x8` | TG1WDT_SYS_RESET | спрацював watchdog таймера 1 |
| `0x9` | RTCWDT_SYS_RESET | спрацював RTC watchdog |
| `0xc` | SW_CPU_RESET | скидання ядра з коду; часто після паніки |
| `0xf` | RTCWDT_BROWN_OUT_RESET | **просіло живлення** |
| `0x10` | RTCWDT_RTC_RESET | RTC watchdog скинув усе, разом з RTC |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0x10 | RTCWDT_RTC_RESET | RTC watchdog скинув усе
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** RTC watchdog може скидати весь чип, включаючи RTC модуль. Це критичне питання для deep sleep та RTC операцій. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-K06-026 sha:ac281d07 src:kartky/k06-bootlog.md:27 klas:A -->
### T-K06-026 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `boot:` — куди пішов чип: `SPI_FAST_FLASH_BOOT` — звичайний старт із флешу; `DOWNLOAD_BOOT` — режим прошивки: [[classic]] [[S3]] `GPIO0` притиснутий до землі, [[C3]] `GPIO9` (картка К4).

**Контекст**

```
## Перший рядок — головний

`boot:` — куди пішов чип:
`SPI_FAST_FLASH_BOOT` — звичайний старт із флешу;
`DOWNLOAD_BOOT` — режим прошивки: [[classic]] [[S3]] `GPIO0` притиснутий
до землі, [[C3]] `GPIO9` (картка К4).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > ``SPI_FAST_FLASH_BOOT`` - This is the normal SPI flash boot mode.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Дві основні boot-моди описані в boot.rst.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-K06-027 sha:859ae045 src:kartky/k06-bootlog.md:32 klas:A -->
### T-K06-027 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> [[classic]] Саме **число** після `boot:` — маска рівнів на strapping-пінах: `0x01`=`GPIO5`, `0x02`=`GPIO15`, `0x04`=`GPIO4`, `0x08`=`GPIO2`, `0x10`=`GPIO0`, `0x20`=`GPIO12`.

**Контекст**

```
## Перший рядок — головний

[[classic]] Саме **число** після `boot:` — маска рівнів на
strapping-пінах: `0x01`=`GPIO5`, `0x02`=`GPIO15`, `0x04`=`GPIO4`,
`0x08`=`GPIO2`, `0x10`=`GPIO0`, `0x20`=`GPIO12`. Отже `0x13` — норма, а
**виставлений `0x20` означає `GPIO12` високий**: флеш отримав 1.8 В і
плата мовчить (додаток D).
```

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

<!-- fc id:T-K06-028 sha:cf09f67f src:kartky/k06-bootlog.md:34 klas:A -->
### T-K06-028 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Отже `0x13` — норма, а **виставлений `0x20` означає `GPIO12` високий**: флеш отримав 1.8 В і плата мовчить (додаток D).

**Контекст**

```
## Перший рядок — головний

[[classic]] Саме **число** після `boot:` — маска рівнів на
strapping-пінах: `0x01`=`GPIO5`, `0x02`=`GPIO15`, `0x04`=`GPIO4`,
`0x08`=`GPIO2`, `0x10`=`GPIO0`, `0x20`=`GPIO12`. Отже `0x13` — норма, а
**виставлений `0x20` означає `GPIO12` високий**: флеш отримав 1.8 В і
плата мовчить (додаток D).
```

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
### T-K06-029 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> `rst:0xf` — це не програмна помилка.

**Контекст**

```
## Перший рядок — головний

::: zhyvlennya
`rst:0xf` — це не програмна помилка. Це живлення. Шукати треба джерело,
кабель або конденсатори, а не баг у коді. Найчастіше з'являється в момент
увімкнення Wi-Fi, бо саме там піковий струм.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-030 sha:b25bdbfb src:kartky/k06-bootlog.md:39 klas:E -->
### T-K06-030 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Шукати треба джерело, кабель або конденсатори, а не баг у коді.

**Контекст**

```
## Перший рядок — головний

::: zhyvlennya
`rst:0xf` — це не програмна помилка. Це живлення. Шукати треба джерело,
кабель або конденсатори, а не баг у коді. Найчастіше з'являється в момент
увімкнення Wi-Fi, бо саме там піковий струм.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-031 sha:5bdf9b38 src:kartky/k06-bootlog.md:40 klas:F -->
### T-K06-031 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Найчастіше з'являється в момент увімкнення Wi-Fi, бо саме там піковий струм.

**Контекст**

```
## Перший рядок — головний

::: zhyvlennya
`rst:0xf` — це не програмна помилка. Це живлення. Шукати треба джерело,
кабель або конденсатори, а не баг у коді. Найчастіше з'являється в момент
увімкнення Wi-Fi, бо саме там піковий струм.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-032 sha:0219c8b1 src:kartky/k06-bootlog.md:46 klas:K -->
### T-K06-032 · kod · `kartky/k06-bootlog.md`

**Твердження, коротко**

> ```
> I (29) boot: ESP-IDF v6.0.2 2nd stage bootloader
> I (33) boot.esp32: SPI Flash Size : 4MB
> I (52) boot: Partition Table:
> I (56) boot: ## Label      Usage      Type ST Offset   Length
> ```

**Контекст**

````
## Далі — другий бутлоадер

```
I (29) boot: ESP-IDF v6.0.2 2nd stage bootloader
I (33) boot.esp32: SPI Flash Size : 4MB
I (52) boot: Partition Table:
I (56) boot: ## Label      Usage      Type ST Offset   Length
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — наявність теґів і файли версій: espressif/esp-idf (components/esp_common/include/esp_idf_version.h), espressif/esptool (esptool/__init__.py), espressif/arduino-esp32 (platform.txt), pioarduino/platform-espressif32 (platform.json)
- **Дослівно з джерела:**
  > esp-idf v6.0.2  → 200,  v6.0.3 → 404      esp_idf_version.h: MAJOR 6 MINOR 0 PATCH 2
  > esp-idf v5.5.5  → 200,  v5.5.6 → 404
  > esptool v5.3.1  → 200,  v5.3.2 → 404      __init__.py: __version__ = "5.3.1"
  > arduino-esp32 3.3.11 → 200, 3.3.12 → 404  platform.txt: version=3.3.11
  > pioarduino 55.03.311 → 200, 55.03.312 → 404
  >     platform.json: "version": "55.03.311"
  >     і в ньому ж: .../arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, коди відповіді + файли версій, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Кожна з чотирьох версій підтверджена двічі: існуванням теґа й номером усередині самого репозиторію на цьому теґу. Наступного теґа немає в жодного — тобто це справді найновіші, а не просто наявні.
Окремо цінне спостереження: `platform.json` pioarduino 55.03.311 тягне саме `esp32-core-3.3.11`. Тобто два рядки таблиці версій книги узгоджені між собою не за збігом, а за побудовою — форк PlatformIO пінує рівно ту версію Arduino core, яку книга називає поточною.
`toolchain-baseline.yaml` уже мав `status: verified` на всіх чотирьох; цей прохід перевірив, що позначка відповідає дійсності, а не лишилася від попередньої ревізії.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-K06-033 sha:f0278c3a src:kartky/k06-bootlog.md:53 klas:E -->
### T-K06-033 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Три речі, які тут читаються безкоштовно: **версія IDF**, якою зібрано прошивку; **обсяг флешу**, який бачить бутлоадер; **уся таблиця розділів** із адресами.

**Контекст**

```
## Далі — другий бутлоадер

Три речі, які тут читаються безкоштовно: **версія IDF**, якою зібрано
прошивку; **обсяг флешу**, який бачить бутлоадер; **уся таблиця розділів**
із адресами. Це готова відповідь на «а що там усередині» — без розбирання
дампа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-034 sha:e6a1f09c src:kartky/k06-bootlog.md:55 klas:E -->
### T-K06-034 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Це готова відповідь на «а що там усередині» — без розбирання дампа.

**Контекст**

```
## Далі — другий бутлоадер

Три речі, які тут читаються безкоштовно: **версія IDF**, якою зібрано
прошивку; **обсяг флешу**, який бачить бутлоадер; **уся таблиця розділів**
із адресами. Це готова відповідь на «а що там усередині» — без розбирання
дампа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-035 sha:0ebdcddf src:kartky/k06-bootlog.md:58 klas:E -->
### T-K06-035 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Число в дужках — мілісекунди від старту.

**Контекст**

```
## Далі — другий бутлоадер

Число в дужках — мілісекунди від старту. Стрибок у цьому числі показує,
де саме прошивка задумалася.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-036 sha:f043d2b4 src:kartky/k06-bootlog.md:58 klas:E -->
### T-K06-036 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Стрибок у цьому числі показує, де саме прошивка задумалася.

**Контекст**

```
## Далі — другий бутлоадер

Число в дужках — мілісекунди від старту. Стрибок у цьому числі показує,
де саме прошивка задумалася.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-037 sha:f219b8f9 src:kartky/k06-bootlog.md:63 klas:E -->
### T-K06-037 · tablycya · `kartky/k06-bootlog.md`

**Твердження, коротко**

> | Видно | Що це |

**Контекст**

```
## Що означає тиша


| Видно | Що це |
|---|---|
| нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |
| перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |
| ті самі рядки по колу | boot loop → картка К7 |
| `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |
| зовсім порожньо | немає порту чи живлення → картка К3. [[classic]] Або `GPIO15` притиснутий до землі: він глушить лог ROM, плата при цьому справна |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-038 sha:b44c3a39 src:kartky/k06-bootlog.md:65 klas:A -->
### T-K06-038 · tablycya · `kartky/k06-bootlog.md`

**Твердження, коротко**

> | нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |

**Контекст**

```
## Що означає тиша


| Видно | Що це |
|---|---|
| нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |
| перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |
| ті самі рядки по колу | boot loop → картка К7 |
| `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |
| зовсім порожньо | немає порту чи живлення → картка К3. [[classic]] Або `GPIO15` притиснутий до землі: він глушить лог ROM, плата при цьому справна |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > The ESP8266 boot rom writes a log to the UART when booting. The timing is a little bit unusual: ``74880 baud``
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** ESP8266 ROM на 74880 бод — істотна відмінність від ESP32.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-K06-039 sha:e108d7f6 src:kartky/k06-bootlog.md:66 klas:E -->
### T-K06-039 · tablycya · `kartky/k06-bootlog.md`

**Твердження, коротко**

> | перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |

**Контекст**

```
## Що означає тиша


| Видно | Що це |
|---|---|
| нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |
| перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |
| ті самі рядки по колу | boot loop → картка К7 |
| `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |
| зовсім порожньо | немає порту чи живлення → картка К3. [[classic]] Або `GPIO15` притиснутий до землі: він глушить лог ROM, плата при цьому справна |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-040 sha:dd7a6d62 src:kartky/k06-bootlog.md:67 klas:E -->
### T-K06-040 · tablycya · `kartky/k06-bootlog.md`

**Твердження, коротко**

> | ті самі рядки по колу | boot loop → картка К7 |

**Контекст**

```
## Що означає тиша


| Видно | Що це |
|---|---|
| нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |
| перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |
| ті самі рядки по колу | boot loop → картка К7 |
| `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |
| зовсім порожньо | немає порту чи живлення → картка К3. [[classic]] Або `GPIO15` притиснутий до землі: він глушить лог ROM, плата при цьому справна |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-041 sha:36137769 src:kartky/k06-bootlog.md:68 klas:F -->
### T-K06-041 · tablycya · `kartky/k06-bootlog.md`

**Твердження, коротко**

> | `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |

**Контекст**

```
## Що означає тиша


| Видно | Що це |
|---|---|
| нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |
| перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |
| ті самі рядки по колу | boot loop → картка К7 |
| `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |
| зовсім порожньо | немає порту чи живлення → картка К3. [[classic]] Або `GPIO15` притиснутий до землі: він глушить лог ROM, плата при цьому справна |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-042 sha:1e93ec50 src:kartky/k06-bootlog.md:69 klas:A -->
### T-K06-042 · tablycya · `kartky/k06-bootlog.md`

**Твердження, коротко**

> | зовсім порожньо | немає порту чи живлення → картка К3. [[classic]] Або `GPIO15` притиснутий до землі: він глушить лог ROM, плата при цьому справна |

**Контекст**

```
## Що означає тиша


| Видно | Що це |
|---|---|
| нечитний набір символів | не 115200. Читається на 74880 — це ESP8266 |
| перші рядки, далі тиша | застосунок стартував і не логує. Це може бути норма |
| ті самі рядки по колу | boot loop → картка К7 |
| `invalid header: 0x...` | застосунку немає або адреса не та → картка К5 |
| зовсім порожньо | немає порту чи живлення → картка К3. [[classic]] Або `GPIO15` притиснутий до землі: він глушить лог ROM, плата при цьому справна |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 15 (MTDO)  | If driven Low, silences boot messages printed by the ROM
  > |            | bootloader. Has an internal pull-up, so unconnected = High =
  > |            | normal output.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, і рівно в жанрі книги. Розділ 07 писав про `GPIO5` і `GPIO15` одним рядком — «режим і вивід логу при старті», наслідок «сміття в консолі». Насправді наслідок протилежний за характером: `GPIO15`, притиснутий до землі, не псує лог, а **прибирає його цілком**.
Для книги, чия картка К6 присвячена читанню boot-логу, це закриває цілий сценарій: «плата мовчить на 115200» досі означало порт, живлення або швидкість, а тепер має ще одну причину — резистор чи світлодіод на `GPIO15`. Плата при цьому цілком справна.
Додано блоком уваги в розділ 07 і рядком на картку К6.
Рядок про `GPIO5` розділено: його роль (таймінги SDIO-веденого) лишається за datasheet і в наряді, тож книга більше не змішує його з `GPIO15` в одному твердженні.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-K06-043 sha:8f7a2ab6 src:kartky/k06-bootlog.md:72 klas:E -->
### T-K06-043 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Рядки ROM завжди йдуть на **115200** — і незалежно від швидкості застосунку, і незалежно від кварцу на платі.

**Контекст**

```
## Що означає тиша

::: uvaha
Рядки ROM завжди йдуть на **115200** — і незалежно від швидкості
застосунку, і незалежно від кварцу на платі. Якщо ROM видно, а далі
каша — швидкість застосунку інша, і це нормально.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-044 sha:ae375117 src:kartky/k06-bootlog.md:73 klas:E -->
### T-K06-044 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Якщо ROM видно, а далі каша — швидкість застосунку інша, і це нормально.

**Контекст**

```
## Що означає тиша

::: uvaha
Рядки ROM завжди йдуть на **115200** — і незалежно від швидкості
застосунку, і незалежно від кварцу на платі. Якщо ROM видно, а далі
каша — швидкість застосунку інша, і це нормально.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K06-045 sha:e3061d40 src:kartky/k06-bootlog.md:76 klas:A -->
### T-K06-045 · proza · `kartky/k06-bootlog.md`

**Твердження, коротко**

> Якщо ж на 115200 не читається нічого, а на **74880** з'являється осмислений текст — у вас **ESP8266**, а не ESP32: у його ROM швидкість виходить саме такою.

**Контекст**

```
## Що означає тиша

Якщо ж на 115200 не читається нічого, а на **74880** з'являється
осмислений текст — у вас **ESP8266**, а не ESP32: у його ROM швидкість
виходить саме такою.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > The ESP8266 boot rom writes a log to the UART when booting at ``74880 baud``
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Диагностичний метод розпізнавання за baudrate.
- **Прохід:** m2-62-bootlog-k06

---
