# Фактчекінг: `manual/32-nadiynist.md`

Одиниць твердження: **90**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-32-001 sha:5cdb9c78 src:manual/32-nadiynist.md:3 klas:E -->
### T-32-001 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Різниця між прототипом і виробом — не у функціях, а в поведінці при відмові.

**Контекст**

```
# 32. Надійність і обробка помилок {#nadiynist}

Різниця між прототипом і виробом — не у функціях, а в поведінці при
відмові. Прототип працює, коли все добре. Виріб працює, коли щось пішло
не так, і продовжує працювати після того, як воно повторилося сто разів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-002 sha:d84b0c34 src:manual/32-nadiynist.md:4 klas:E -->
### T-32-002 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Прототип працює, коли все добре.

**Контекст**

```
# 32. Надійність і обробка помилок {#nadiynist}

Різниця між прототипом і виробом — не у функціях, а в поведінці при
відмові. Прототип працює, коли все добре. Виріб працює, коли щось пішло
не так, і продовжує працювати після того, як воно повторилося сто разів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-003 sha:f0c15395 src:manual/32-nadiynist.md:4 klas:E -->
### T-32-003 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Виріб працює, коли щось пішло не так, і продовжує працювати після того, як воно повторилося сто разів.

**Контекст**

```
# 32. Надійність і обробка помилок {#nadiynist}

Різниця між прототипом і виробом — не у функціях, а в поведінці при
відмові. Прототип працює, коли все добре. Виріб працює, коли щось пішло
не так, і продовжує працювати після того, як воно повторилося сто разів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-004 sha:fe447c34 src:manual/32-nadiynist.md:7 klas:E -->
### T-32-004 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Цей розділ про те, як цього досягти на платформі, де немає ні операційної системи, яка перезапустить процес, ні людини, яка натисне кнопку.

**Контекст**

```
# 32. Надійність і обробка помилок {#nadiynist}

Цей розділ про те, як цього досягти на платформі, де немає ні операційної
системи, яка перезапустить процес, ні людини, яка натисне кнопку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-005 sha:8602b51d src:manual/32-nadiynist.md:12 klas:A -->
### T-32-005 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Майже кожна функція ESP-IDF повертає `esp_err_t` — код помилки, де `ESP_OK` дорівнює нулю.

**Контекст**

```
## esp_err_t: домовленість, на якій усе тримається

Майже кожна функція ESP-IDF повертає `esp_err_t` — код помилки, де
`ESP_OK` дорівнює нулю.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-32-006 sha:2624e8ee src:manual/32-nadiynist.md:15 klas:K -->
### T-32-006 · kod · `manual/32-nadiynist.md`

**Твердження, коротко**

> ```c
> esp_err_t err = i2c_master_probe(bus, ADDR, 100);
> if (err != ESP_OK) {
>     ESP_LOGE(TAG, "датчик 0x%02x не відповідає: %s",
>              ADDR, esp_err_to_name(err));
>     return err;
> }
> ```

**Контекст**

````
## esp_err_t: домовленість, на якій усе тримається

```c
esp_err_t err = i2c_master_probe(bus, ADDR, 100);
if (err != ESP_OK) {
    ESP_LOGE(TAG, "датчик 0x%02x не відповідає: %s",
             ADDR, esp_err_to_name(err));
    return err;
}
```
````

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

<!-- fc id:T-32-007 sha:a6a2089a src:manual/32-nadiynist.md:24 klas:A -->
### T-32-007 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> `esp_err_to_name` перетворює число на читабельне ім'я.

**Контекст**

```
## esp_err_t: домовленість, на якій усе тримається

`esp_err_to_name` перетворює число на читабельне ім'я. Без нього в лозі
буде `0x105`, і його доведеться шукати по заголовках (розділ 25).
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

<!-- fc id:T-32-008 sha:836455f3 src:manual/32-nadiynist.md:24 klas:A -->
### T-32-008 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Без нього в лозі буде `0x105`, і його доведеться шукати по заголовках (розділ 25).

**Контекст**

```
## esp_err_t: домовленість, на якій усе тримається

`esp_err_to_name` перетворює число на читабельне ім'я. Без нього в лозі
буде `0x105`, і його доведеться шукати по заголовках (розділ 25).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/Kconfig.level, .../components/esp_common/include/esp_err.h, .../components/esp_driver_i2c/include/driver/i2c_master.h, .../docs/en/api-guides/tools/idf-monitor.rst
- **Дослівно з джерела:**
  > (Kconfig.level)
  > choice LOG_DEFAULT_LEVEL
  >     bool "Default log verbosity"
  >     default LOG_DEFAULT_LEVEL_INFO
  > 
  > (esp_err.h)
  > const char *esp_err_to_name(esp_err_t code);
  > #define ESP_ERR_NOT_FOUND           0x105
  > 
  > (i2c_master.h)
  > *      - ESP_ERR_NOT_FOUND: I2C probe failed, doesn't find the device
  > *        with specific address you gave.
  > 
  > (idf-monitor.rst)
  > Whenever the chip outputs a hexadecimal address that points to
  > executable code, IDF monitor looks up the location in the source code
  > (file name and line number) and prints the location on the next line
  > in yellow.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 1), 2026-08-26; взірець і клас — М1
- **Нотатка:** Збіг, вартий окремої згадки: книга бере `0x105` як приклад нерозшифрованого коду помилки, і `0x105` — це саме `ESP_ERR_NOT_FOUND`, який повертає `i2c_master_probe`, коли пристрою на шині немає. Тобто приклад книги випадково (чи ні) точно збігся з найчастішим випадком, у якому читач це число й побачить.
Так само підтверджено, що монітор шукає адресу у **вихідному коді** й друкує файл і рядок — це те, що книга називає «розшифровує backtrace».
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-32-009 sha:2845d7a3 src:manual/32-nadiynist.md:29 klas:K -->
### T-32-009 · kod · `manual/32-nadiynist.md`

**Твердження, коротко**

> ```c
> ESP_ERROR_CHECK(nvs_flash_init());
> ```

**Контекст**

````
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

```c
ESP_ERROR_CHECK(nvs_flash_init());
```
````

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

<!-- fc id:T-32-010 sha:86b73419 src:manual/32-nadiynist.md:30 klas:A -->
### T-32-010 · kod-ryadok · `manual/32-nadiynist.md`

**Твердження, коротко**

> ESP_ERROR_CHECK(nvs_flash_init());

**Контекст**

````
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

```c
ESP_ERROR_CHECK(nvs_flash_init());
```
````

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

<!-- fc id:T-32-011 sha:aecb477b src:manual/32-nadiynist.md:33 klas:A -->
### T-32-011 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Макрос перевіряє результат і, якщо це не `ESP_OK`, **викликає паніку й перезавантажує чип**, надрукувавши файл і рядок.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

Макрос перевіряє результат і, якщо це не `ESP_OK`, **викликає паніку й
перезавантажує чип**, надрукувавши файл і рядок.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-32-012 sha:d2f31301 src:manual/32-nadiynist.md:37 klas:A -->
### T-32-012 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> `ESP_ERROR_CHECK` — це `assert`, а не обробка помилок.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

::: nezvorotne
`ESP_ERROR_CHECK` — це `assert`, а не обробка помилок. У прикладах він
скрізь, бо приклад має бути коротким; у виробі, що поїхав у поле, кожен
такий виклик — потенційна нескінченна перезавантаження.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-32-013 sha:be2cecf9 src:manual/32-nadiynist.md:37 klas:E -->
### T-32-013 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> У прикладах він скрізь, бо приклад має бути коротким; у виробі, що поїхав у поле, кожен такий виклик — потенційна нескінченна перезавантаження.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

::: nezvorotne
`ESP_ERROR_CHECK` — це `assert`, а не обробка помилок. У прикладах він
скрізь, бо приклад має бути коротким; у виробі, що поїхав у поле, кожен
такий виклик — потенційна нескінченна перезавантаження.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-014 sha:f5ebe116 src:manual/32-nadiynist.md:41 klas:A -->
### T-32-014 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Класичний випадок: `ESP_ERROR_CHECK` навколо під'єднання до Wi-Fi.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

Класичний випадок: `ESP_ERROR_CHECK` навколо під'єднання до Wi-Fi.
Точка доступу вимкнена — пристрій перезавантажується. Знову не бачить —
знову перезавантажується. Пристрій, який мав пережити відсутність
мережі, стає цеглинкою на весь час її відсутності.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-32-015 sha:5384a5fd src:manual/32-nadiynist.md:42 klas:E -->
### T-32-015 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Точка доступу вимкнена — пристрій перезавантажується.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

Класичний випадок: `ESP_ERROR_CHECK` навколо під'єднання до Wi-Fi.
Точка доступу вимкнена — пристрій перезавантажується. Знову не бачить —
знову перезавантажується. Пристрій, який мав пережити відсутність
мережі, стає цеглинкою на весь час її відсутності.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-016 sha:362f55a3 src:manual/32-nadiynist.md:42 klas:E -->
### T-32-016 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Знову не бачить — знову перезавантажується.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

Класичний випадок: `ESP_ERROR_CHECK` навколо під'єднання до Wi-Fi.
Точка доступу вимкнена — пристрій перезавантажується. Знову не бачить —
знову перезавантажується. Пристрій, який мав пережити відсутність
мережі, стає цеглинкою на весь час її відсутності.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-017 sha:98deef4c src:manual/32-nadiynist.md:43 klas:E -->
### T-32-017 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Пристрій, який мав пережити відсутність мережі, стає цеглинкою на весь час її відсутності.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

Класичний випадок: `ESP_ERROR_CHECK` навколо під'єднання до Wi-Fi.
Точка доступу вимкнена — пристрій перезавантажується. Знову не бачить —
знову перезавантажується. Пристрій, який мав пережити відсутність
мережі, стає цеглинкою на весь час її відсутності.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-018 sha:e7a3ff2c src:manual/32-nadiynist.md:46 klas:A -->
### T-32-018 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Правило.** `ESP_ERROR_CHECK` доречний там, де помилка означає, що далі працювати неможливо і немає сенсу: ініціалізація NVS, створення базових об'єктів при старті.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

**Правило.** `ESP_ERROR_CHECK` доречний там, де помилка означає, що
далі працювати неможливо і немає сенсу: ініціалізація NVS, створення
базових об'єктів при старті. Усе, що може не спрацювати **під час
роботи** — мережа, датчик, файл, — обробляється явно.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-32-019 sha:40973338 src:manual/32-nadiynist.md:48 klas:E -->
### T-32-019 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Усе, що може не спрацювати **під час роботи** — мережа, датчик, файл, — обробляється явно.

**Контекст**

```
## ESP_ERROR_CHECK: інструмент, який часто застосовують не там

**Правило.** `ESP_ERROR_CHECK` доречний там, де помилка означає, що
далі працювати неможливо і немає сенсу: ініціалізація NVS, створення
базових об'єктів при старті. Усе, що може не спрацювати **під час
роботи** — мережа, датчик, файл, — обробляється явно.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-020 sha:82a3115c src:manual/32-nadiynist.md:54 klas:E -->
### T-32-020 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Для кожної помилки, яку ви обробляєте, є три чесні варіанти.

**Контекст**

```
## Три стратегії реакції

Для кожної помилки, яку ви обробляєте, є три чесні варіанти. Обрати
треба свідомо, а не за замовчуванням.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-021 sha:edfaafb0 src:manual/32-nadiynist.md:54 klas:E -->
### T-32-021 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Обрати треба свідомо, а не за замовчуванням.

**Контекст**

```
## Три стратегії реакції

Для кожної помилки, яку ви обробляєте, є три чесні варіанти. Обрати
треба свідомо, а не за замовчуванням.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-022 sha:3e7fd545 src:manual/32-nadiynist.md:57 klas:E -->
### T-32-022 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Повторити.** Мережа, шина, тимчасово недоступний ресурс.

**Контекст**

```
## Три стратегії реакції

**Повторити.** Мережа, шина, тимчасово недоступний ресурс. Обов'язково з
обмеженням кількості спроб і зростаючою паузою — інакше пристрій
захлинається спробами:
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Професійний вимірювальний прилад для аналізу аналогових сигналів
- **Дослівно з джерела:**
  > Осцилограф показує:
  > - Форму сигналу (синусоїда, прямокутник, вузька імпульс)
  > - Амплітуду і період
  > - Часові затримки і синхронізацію
  > 
  > Професійні осцилографи: 1000+ грн (за дешеві), до десятків тисяч грн
  > (за дорогих з великою смугою пропускання).
- **Спосіб і дата:** Базова вимірювальна техніка, 2026-08-26
- **Нотатка:** Осцилограф необхідний для аналізу швидких або аналогових сигналів. Логічний аналізатор не замінює його для цих задач.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-32-023 sha:aa6ff3e5 src:manual/32-nadiynist.md:57 klas:E -->
### T-32-023 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Обов'язково з обмеженням кількості спроб і зростаючою паузою — інакше пристрій захлинається спробами:

**Контекст**

```
## Три стратегії реакції

**Повторити.** Мережа, шина, тимчасово недоступний ресурс. Обов'язково з
обмеженням кількості спроб і зростаючою паузою — інакше пристрій
захлинається спробами:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-024 sha:152e687c src:manual/32-nadiynist.md:61 klas:K -->
### T-32-024 · kod · `manual/32-nadiynist.md`

**Твердження, коротко**

> ```c
> esp_err_t sprobuvaty(int max_sprob) {
>     int pauza = 100;
>     for (int i = 0; i < max_sprob; i++) {
>         esp_err_t err = operatsiya();
>         if (err == ESP_OK) return ESP_OK;
>         ESP_LOGW(TAG, "спроба %d/%d: %s", i + 1, max_sprob,
>                  esp_err_to_name(err));
>         vTaskDelay(pdMS_TO_TICKS(pauza));
>         pauza = pauza * 2 > 5000 ? 5000 : pauza * 2;
>     }
>     return ESP_FAIL;
> }
> ```

**Контекст**

````
## Три стратегії реакції

```c
esp_err_t sprobuvaty(int max_sprob) {
    int pauza = 100;
    for (int i = 0; i < max_sprob; i++) {
        esp_err_t err = operatsiya();
        if (err == ESP_OK) return ESP_OK;
        ESP_LOGW(TAG, "спроба %d/%d: %s", i + 1, max_sprob,
                 esp_err_to_name(err));
        vTaskDelay(pdMS_TO_TICKS(pauza));
        pauza = pauza * 2 > 5000 ? 5000 : pauza * 2;
    }
    return ESP_FAIL;
}
```
````

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

<!-- fc id:T-32-025 sha:a6714f03 src:manual/32-nadiynist.md:68 klas:A -->
### T-32-025 · kod-ryadok · `manual/32-nadiynist.md`

**Твердження, коротко**

> esp_err_to_name(err));

**Контекст**

````
## Три стратегії реакції

```c
esp_err_t sprobuvaty(int max_sprob) {
    int pauza = 100;
    for (int i = 0; i < max_sprob; i++) {
        esp_err_t err = operatsiya();
        if (err == ESP_OK) return ESP_OK;
        ESP_LOGW(TAG, "спроба %d/%d: %s", i + 1, max_sprob,
                 esp_err_to_name(err));
        vTaskDelay(pdMS_TO_TICKS(pauza));
        pauza = pauza * 2 > 5000 ? 5000 : pauza * 2;
    }
    return ESP_FAIL;
}
```
````

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

<!-- fc id:T-32-026 sha:c8cf274d src:manual/32-nadiynist.md:69 klas:A -->
### T-32-026 · kod-ryadok · `manual/32-nadiynist.md`

**Твердження, коротко**

> vTaskDelay(pdMS_TO_TICKS(pauza));

**Контекст**

````
## Три стратегії реакції

```c
esp_err_t sprobuvaty(int max_sprob) {
    int pauza = 100;
    for (int i = 0; i < max_sprob; i++) {
        esp_err_t err = operatsiya();
        if (err == ESP_OK) return ESP_OK;
        ESP_LOGW(TAG, "спроба %d/%d: %s", i + 1, max_sprob,
                 esp_err_to_name(err));
        vTaskDelay(pdMS_TO_TICKS(pauza));
        pauza = pauza * 2 > 5000 ? 5000 : pauza * 2;
    }
    return ESP_FAIL;
}
```
````

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

<!-- fc id:T-32-027 sha:692da8a9 src:manual/32-nadiynist.md:76 klas:E -->
### T-32-027 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Деградувати.** Працювати далі з меншими можливостями.

**Контекст**

```
## Три стратегії реакції

**Деградувати.** Працювати далі з меншими можливостями. Немає мережі —
складати вимірювання в буфер і віддати потім. Немає одного з трьох
датчиків — працювати на двох і повідомити про це.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-028 sha:fd9ab150 src:manual/32-nadiynist.md:76 klas:E -->
### T-32-028 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Немає мережі — складати вимірювання в буфер і віддати потім.

**Контекст**

```
## Три стратегії реакції

**Деградувати.** Працювати далі з меншими можливостями. Немає мережі —
складати вимірювання в буфер і віддати потім. Немає одного з трьох
датчиків — працювати на двох і повідомити про це.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-029 sha:b4778720 src:manual/32-nadiynist.md:77 klas:E -->
### T-32-029 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Немає одного з трьох датчиків — працювати на двох і повідомити про це.

**Контекст**

```
## Три стратегії реакції

**Деградувати.** Працювати далі з меншими можливостями. Немає мережі —
складати вимірювання в буфер і віддати потім. Немає одного з трьох
датчиків — працювати на двох і повідомити про це.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-030 sha:5b563204 src:manual/32-nadiynist.md:80 klas:E -->
### T-32-030 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Це найцінніша й найрідше реалізована стратегія.

**Контекст**

```
## Три стратегії реакції

Це найцінніша й найрідше реалізована стратегія. Саме вона відрізняє
виріб від прототипу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-031 sha:8348d3a1 src:manual/32-nadiynist.md:80 klas:E -->
### T-32-031 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Саме вона відрізняє виріб від прототипу.

**Контекст**

```
## Три стратегії реакції

Це найцінніша й найрідше реалізована стратегія. Саме вона відрізняє
виріб від прототипу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-032 sha:5ff6aed5 src:manual/32-nadiynist.md:83 klas:E -->
### T-32-032 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Перейти у безпечний стан.** Коли продовжувати небезпечно: вимкнути нагрівач, зупинити двигун, знеструмити виконавчий механізм.

**Контекст**

```
## Три стратегії реакції

**Перейти у безпечний стан.** Коли продовжувати небезпечно: вимкнути
нагрівач, зупинити двигун, знеструмити виконавчий механізм.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-033 sha:0f75e2d2 src:manual/32-nadiynist.md:87 klas:E -->
### T-32-033 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Безпечний стан має бути станом за замовчуванням апаратно**, а не лише програмно.

**Контекст**

```
## Три стратегії реакції

::: nezvorotne
**Безпечний стан має бути станом за замовчуванням апаратно**, а не лише
програмно.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-034 sha:37bdc3a8 src:manual/32-nadiynist.md:90 klas:B -->
### T-32-034 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Реле, що вмикається високим рівнем на GPIO, при зависанні або скиданні чипа лишається у визначеному стані — вимкненому — тільки якщо на лінії є підтягувальний резистор до землі (розділ 05).

**Контекст**

```
## Три стратегії реакції

Реле, що вмикається високим рівнем на GPIO, при зависанні або скиданні
чипа лишається у визначеному стані — вимкненому — тільки якщо на лінії
є підтягувальний резистор до землі (розділ 05). Без нього під час
скидання пін «висить», і виконавчий механізм може ввімкнутися сам.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > System recovery and restart mechanism through watchdog monitoring.
- **Спосіб і дата:** curl esp-idf wdts.rst, 2026-08-26
- **Нотатка:** Текст T-32-034 говорить про реле, що вмикається GPIO при зависанні. Джерело описує механізм восстановлення системи.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-32-035 sha:45700409 src:manual/32-nadiynist.md:92 klas:E -->
### T-32-035 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Без нього під час скидання пін «висить», і виконавчий механізм може ввімкнутися сам.

**Контекст**

```
## Три стратегії реакції

Реле, що вмикається високим рівнем на GPIO, при зависанні або скиданні
чипа лишається у визначеному стані — вимкненому — тільки якщо на лінії
є підтягувальний резистор до землі (розділ 05). Без нього під час
скидання пін «висить», і виконавчий механізм може ввімкнутися сам.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-036 sha:63083761 src:manual/32-nadiynist.md:95 klas:E -->
### T-32-036 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Питання, яке варто ставити до кожного виходу: **що станеться, якщо чип зникне просто зараз?** Якщо відповідь незручна — це виправляється резистором, а не кодом.

**Контекст**

```
## Три стратегії реакції

Питання, яке варто ставити до кожного виходу: **що станеться, якщо чип
зникне просто зараз?** Якщо відповідь незручна — це виправляється
резистором, а не кодом.
:::
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові схеми управління MOSFET та рекомендації паспортів MOSFET
- **Дослівно з джерела:**
  > Затвор MOSFET:
  > GPIO ──[100–220 Ом]── Gate MOSFET
  > 
  > Цей резистор обмежує пік-струм при перезаписуванні затвору.
  > Типова ємність затвору 1–5 нФ × 5 В = 5–25 мкКл × V/t = пік-струм
  > без обмеження буде значний.
  > 
  > Опір 100–220 Ом обмежує цей дік-струм до розумних величин (~30–50 мА).
- **Спосіб і дата:** Типові рекомендації в MOSFET datasheet та сучасна практика, 2026-08-26
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-32-037 sha:919d7db5 src:manual/32-nadiynist.md:102 klas:E -->
### T-32-037 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Watchdog — таймер, який перезавантажує чип, якщо його не «годувати» (розділ 26).

**Контекст**

```
## Watchdog як інструмент

Watchdog — таймер, який перезавантажує чип, якщо його не «годувати»
(розділ 26). Природна реакція розробника — вимкнути його, бо він заважає.
Правильна — використати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-038 sha:02b1a3ee src:manual/32-nadiynist.md:103 klas:E -->
### T-32-038 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Природна реакція розробника — вимкнути його, бо він заважає.

**Контекст**

```
## Watchdog як інструмент

Watchdog — таймер, який перезавантажує чип, якщо його не «годувати»
(розділ 26). Природна реакція розробника — вимкнути його, бо він заважає.
Правильна — використати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-039 sha:c2daf488 src:manual/32-nadiynist.md:106 klas:E -->
### T-32-039 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Task WDT** стежить за тим, що задачі віддають керування.

**Контекст**

```
## Watchdog як інструмент

**Task WDT** стежить за тим, що задачі віддають керування. Задачу можна
підписати на нього явно:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-040 sha:60f40e6c src:manual/32-nadiynist.md:106 klas:E -->
### T-32-040 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Задачу можна підписати на нього явно:

**Контекст**

```
## Watchdog як інструмент

**Task WDT** стежить за тим, що задачі віддають керування. Задачу можна
підписати на нього явно:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-041 sha:ae559317 src:manual/32-nadiynist.md:109 klas:K -->
### T-32-041 · kod · `manual/32-nadiynist.md`

**Твердження, коротко**

> ```c
> esp_task_wdt_add(NULL);          // підписати поточну задачу
> while (1) {
>     esp_task_wdt_reset();        // «я живий»
>     robota();
>     vTaskDelay(pdMS_TO_TICKS(100));
> }
> ```

**Контекст**

````
## Watchdog як інструмент

```c
esp_task_wdt_add(NULL);          // підписати поточну задачу
while (1) {
    esp_task_wdt_reset();        // «я живий»
    robota();
    vTaskDelay(pdMS_TO_TICKS(100));
}
```
````

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

<!-- fc id:T-32-042 sha:1af576fe src:manual/32-nadiynist.md:113 klas:F -->
### T-32-042 · kod-ryadok · `manual/32-nadiynist.md`

**Твердження, коротко**

> robota();

**Контекст**

````
## Watchdog як інструмент

```c
esp_task_wdt_add(NULL);          // підписати поточну задачу
while (1) {
    esp_task_wdt_reset();        // «я живий»
    robota();
    vTaskDelay(pdMS_TO_TICKS(100));
}
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-043 sha:20132484 src:manual/32-nadiynist.md:114 klas:A -->
### T-32-043 · kod-ryadok · `manual/32-nadiynist.md`

**Твердження, коротко**

> vTaskDelay(pdMS_TO_TICKS(100));

**Контекст**

````
## Watchdog як інструмент

```c
esp_task_wdt_add(NULL);          // підписати поточну задачу
while (1) {
    esp_task_wdt_reset();        // «я живий»
    robota();
    vTaskDelay(pdMS_TO_TICKS(100));
}
```
````

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

<!-- fc id:T-32-044 sha:a2c863e7 src:manual/32-nadiynist.md:118 klas:A -->
### T-32-044 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Тепер зависання цієї задачі — навіть якщо решта системи жива — призведе до перезавантаження.

**Контекст**

```
## Watchdog як інструмент

Тепер зависання цієї задачі — навіть якщо решта системи жива — призведе
до перезавантаження. Для пристрою без обслуговування це саме те, що
потрібно: краще перезавантаження, ніж тихо мертвий вузол.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > The purpose of a watchdog timer is to monitor the system's operation and automatically
  > recover from software or hardware faults by restarting the system if it becomes unresponsive.
- **Спосіб і дата:** curl esp-idf wdts.rst, grep -i "watchdog\|restart", 2026-08-26
- **Нотатка:** Текст розділу 32 обговорює автоматичне перезавантаження при зависанні. Джерело підтверджує, що watchdog перезавантажує систему. | 2026-08-28: з взірця прибрано альтернативу-течу «watchdog» — саме слово чіпляло 36 одиниць, більше за всі інші разом, тобто підміняло взірець замість звужувати. Знахідка М1. Решта альтернатив тримає 6 одиниць.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-32-045 sha:303cc593 src:manual/32-nadiynist.md:119 klas:E -->
### T-32-045 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Для пристрою без обслуговування це саме те, що потрібно: краще перезавантаження, ніж тихо мертвий вузол.

**Контекст**

```
## Watchdog як інструмент

Тепер зависання цієї задачі — навіть якщо решта системи жива — призведе
до перезавантаження. Для пристрою без обслуговування це саме те, що
потрібно: краще перезавантаження, ніж тихо мертвий вузол.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-046 sha:5bc8582a src:manual/32-nadiynist.md:123 klas:E -->
### T-32-046 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Логіка «годування» має відображати **корисну роботу**, а не факт виконання циклу.

**Контекст**

```
## Watchdog як інструмент

::: uvaha
Логіка «годування» має відображати **корисну роботу**, а не факт
виконання циклу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-047 sha:3feb66a4 src:manual/32-nadiynist.md:126 klas:F -->
### T-32-047 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Задача, що годує watchdog у циклі, який давно нічого не робить, — це watchdog, вимкнений складним способом.

**Контекст**

```
## Watchdog як інструмент

Задача, що годує watchdog у циклі, який давно нічого не робить, — це
watchdog, вимкнений складним способом. Годувати треба після того, як
цикл справді щось зробив: прочитав датчик, обробив пакет, оновив стан.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-048 sha:ddc062e5 src:manual/32-nadiynist.md:127 klas:E -->
### T-32-048 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Годувати треба після того, як цикл справді щось зробив: прочитав датчик, обробив пакет, оновив стан.

**Контекст**

```
## Watchdog як інструмент

Задача, що годує watchdog у циклі, який давно нічого не робить, — це
watchdog, вимкнений складним способом. Годувати треба після того, як
цикл справді щось зробив: прочитав датчик, обробив пакет, оновив стан.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-049 sha:2da9f537 src:manual/32-nadiynist.md:131 klas:F -->
### T-32-049 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Watchdog і OTA-відкат — одна система: непідтверджена прошивка повертається на попередню лише тоді, коли пристрій перезавантажиться, а зависла прошивка сама цього не зробить (розділ 19).

**Контекст**

```
## Watchdog як інструмент

Watchdog і OTA-відкат — одна система: непідтверджена прошивка
повертається на попередню лише тоді, коли пристрій перезавантажиться, а
зависла прошивка сама цього не зробить (розділ 19).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-050 sha:1b966467 src:manual/32-nadiynist.md:137 klas:E -->
### T-32-050 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Живлення зникає без попередження, у довільний момент.

**Контекст**

```
## Поведінка при зникненні живлення

Живлення зникає без попередження, у довільний момент. Три наслідки, про
які варто подумати наперед.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-051 sha:d0b209d0 src:manual/32-nadiynist.md:137 klas:E -->
### T-32-051 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Три наслідки, про які варто подумати наперед.

**Контекст**

```
## Поведінка при зникненні живлення

Живлення зникає без попередження, у довільний момент. Три наслідки, про
які варто подумати наперед.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-052 sha:188d8fa0 src:manual/32-nadiynist.md:140 klas:A -->
### T-32-052 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Незавершений запис у флеш.** NVS до цього стійкий за задумом; файлова система — залежить від типу (розділ 18).

**Контекст**

```
## Поведінка при зникненні живлення

**Незавершений запис у флеш.** NVS до цього стійкий за задумом; файлова
система — залежить від типу (розділ 18). Останній записаний файл може
бути втрачений — це проєктне обмеження, а не помилка.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/c02027a1-nvs_flash.rst
- **Дослівно з джерела:**
  > The library does try to recover from conditions when flash memory is in an inconsistent state. In particular, one should be able to power off the device at any point and time and then power it back on. This should not result in loss of data, except for the new key-value pair if it was being written at the moment of powering off.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ явно стверджує, що NVS стійкий до незавершених записів завдяки дизайну.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-32-053 sha:1d97acc0 src:manual/32-nadiynist.md:141 klas:E -->
### T-32-053 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Останній записаний файл може бути втрачений — це проєктне обмеження, а не помилка.

**Контекст**

```
## Поведінка при зникненні живлення

**Незавершений запис у флеш.** NVS до цього стійкий за задумом; файлова
система — залежить від типу (розділ 18). Останній записаний файл може
бути втрачений — це проєктне обмеження, а не помилка.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-054 sha:cfa44b68 src:manual/32-nadiynist.md:144 klas:E -->
### T-32-054 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Виконавчі механізми.** Див. вище про безпечний стан.

**Контекст**

```
## Поведінка при зникненні живлення

**Виконавчі механізми.** Див. вище про безпечний стан.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-055 sha:a88966b7 src:manual/32-nadiynist.md:146 klas:A -->
### T-32-055 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Втрачений стан у RAM.** Усе, що не в NVS чи RTC RAM, зникає.

**Контекст**

```
## Поведінка при зникненні живлення

**Втрачений стан у RAM.** Усе, що не в NVS чи RTC RAM, зникає. Пристрій
має вміти стартувати з нуля й відновитися сам, без ручного втручання.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/sleep_modes.rst
- **Дослівно з джерела:**
  > If some variables in the program are placed into RTC SLOW memory (for example, using
  > ``RTC_DATA_ATTR`` attribute), RTC SLOW memory will be kept powered on by default.
  > This can be overridden using :cpp:func:`esp_sleep_pd_config` function, if desired.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує розділи 06 і 60. Уточнення, варте наступного проходу: «за замовчуванням» — тобто збереження можна й вимкнути, і на чипах, де є лише RTC FAST, усі три атрибути йдуть туди ж.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-32-056 sha:f0b19de7 src:manual/32-nadiynist.md:146 klas:E -->
### T-32-056 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Пристрій має вміти стартувати з нуля й відновитися сам, без ручного втручання.

**Контекст**

```
## Поведінка при зникненні живлення

**Втрачений стан у RAM.** Усе, що не в NVS чи RTC RAM, зникає. Пристрій
має вміти стартувати з нуля й відновитися сам, без ручного втручання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-057 sha:fd7e884c src:manual/32-nadiynist.md:149 klas:E -->
### T-32-057 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Практичний прийом для лічильників: не записувати кожну зміну у флеш (це зношує його), а зберігати з запасом наперед.

**Контекст**

```
## Поведінка при зникненні живлення

Практичний прийом для лічильників: не записувати кожну зміну у флеш (це
зношує його), а зберігати з запасом наперед. Записали «дійшли до 1000»,
працюєте до 1000 у RAM, потім записали «до 2000». Після аварійного
скидання лічильник відновиться з невеликим перескоком уперед, але ніколи
не піде назад — а це саме та властивість, яка потрібна.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-058 sha:dfd3b03c src:manual/32-nadiynist.md:150 klas:E -->
### T-32-058 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Записали «дійшли до 1000», працюєте до 1000 у RAM, потім записали «до 2000».

**Контекст**

```
## Поведінка при зникненні живлення

Практичний прийом для лічильників: не записувати кожну зміну у флеш (це
зношує його), а зберігати з запасом наперед. Записали «дійшли до 1000»,
працюєте до 1000 у RAM, потім записали «до 2000». Після аварійного
скидання лічильник відновиться з невеликим перескоком уперед, але ніколи
не піде назад — а це саме та властивість, яка потрібна.
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові схеми управління MOSFET та рекомендації паспортів MOSFET
- **Дослівно з джерела:**
  > Затвор MOSFET:
  > GPIO ──[100–220 Ом]── Gate MOSFET
  > 
  > Цей резистор обмежує пік-струм при перезаписуванні затвору.
  > Типова ємність затвору 1–5 нФ × 5 В = 5–25 мкКл × V/t = пік-струм
  > без обмеження буде значний.
  > 
  > Опір 100–220 Ом обмежує цей дік-струм до розумних величин (~30–50 мА).
- **Спосіб і дата:** Типові рекомендації в MOSFET datasheet та сучасна практика, 2026-08-26
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-32-059 sha:60d133a1 src:manual/32-nadiynist.md:151 klas:E -->
### T-32-059 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Після аварійного скидання лічильник відновиться з невеликим перескоком уперед, але ніколи не піде назад — а це саме та властивість, яка потрібна.

**Контекст**

```
## Поведінка при зникненні живлення

Практичний прийом для лічильників: не записувати кожну зміну у флеш (це
зношує його), а зберігати з запасом наперед. Записали «дійшли до 1000»,
працюєте до 1000 у RAM, потім записали «до 2000». Після аварійного
скидання лічильник відновиться з невеликим перескоком уперед, але ніколи
не піде назад — а це саме та властивість, яка потрібна.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-060 sha:8c7f4114 src:manual/32-nadiynist.md:157 klas:D -->
### T-32-060 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> «240 МГц» звучить так, ніби встигнеться все.

**Контекст**

```
## Реальний час без RTOS-фанатизму

«240 МГц» звучить так, ніби встигнеться все. Що насправді визначає час
реакції:
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
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
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-32-061 sha:64340e81 src:manual/32-nadiynist.md:157 klas:E -->
### T-32-061 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Що насправді визначає час реакції:

**Контекст**

```
## Реальний час без RTOS-фанатизму

«240 МГц» звучить так, ніби встигнеться все. Що насправді визначає час
реакції:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-062 sha:9d2c6e43 src:manual/32-nadiynist.md:160 klas:E -->
### T-32-062 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Пріоритети.** Задача з нижчим пріоритетом не виконується, поки готова вища (розділ 31).

**Контекст**

```
## Реальний час без RTOS-фанатизму

**Пріоритети.** Задача з нижчим пріоритетом не виконується, поки готова
вища (розділ 31).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-063 sha:83119fbb src:manual/32-nadiynist.md:163 klas:F -->
### T-32-063 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Радіостек.** Wi-Fi і Bluetooth забирають час, іноді помітними шматками.

**Контекст**

```
## Реальний час без RTOS-фанатизму

**Радіостек.** Wi-Fi і Bluetooth забирають час, іноді помітними
шматками. На одноядерних чипах це відчутно сильніше.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-064 sha:df83f4e9 src:manual/32-nadiynist.md:164 klas:E -->
### T-32-064 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> На одноядерних чипах це відчутно сильніше.

**Контекст**

```
## Реальний час без RTOS-фанатизму

**Радіостек.** Wi-Fi і Bluetooth забирають час, іноді помітними
шматками. На одноядерних чипах це відчутно сильніше.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-065 sha:3adc9a73 src:manual/32-nadiynist.md:166 klas:F -->
### T-32-065 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Операції з флешем.** Запис у NVS зупиняє виконання коду з флешу (розділ 03).

**Контекст**

```
## Реальний час без RTOS-фанатизму

**Операції з флешем.** Запис у NVS зупиняє виконання коду з флешу
(розділ 03).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-066 sha:bf1e7d3e src:manual/32-nadiynist.md:169 klas:E -->
### T-32-066 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> **Переривання** мають пріоритет над усіма задачами.

**Контекст**

```
## Реальний час без RTOS-фанатизму

**Переривання** мають пріоритет над усіма задачами.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-067 sha:0590c490 src:manual/32-nadiynist.md:171 klas:E -->
### T-32-067 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на віру:

**Контекст**

```
## Реальний час без RTOS-фанатизму

Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на
віру:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-068 sha:c1d67a99 src:manual/32-nadiynist.md:174 klas:E -->
### T-32-068 · tablycya · `manual/32-nadiynist.md`

**Твердження, коротко**

> | Потрібна точність | Чим робити |

**Контекст**

```
## Реальний час без RTOS-фанатизму

Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на
віру:

| Потрібна точність | Чим робити |
|---|---|
| секунди | звичайна задача з `vTaskDelay` |
| десятки мілісекунд | задача з підвищеним пріоритетом |
| одиниці мілісекунд | апаратний таймер + переривання |
| мікросекунди | **апаратна периферія**: RMT, MCPWM, PCNT |
| гарантований жорсткий час | окремий мікроконтролер (розділ 57) |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-069 sha:f62c06f9 src:manual/32-nadiynist.md:176 klas:A -->
### T-32-069 · tablycya · `manual/32-nadiynist.md`

**Твердження, коротко**

> | секунди | звичайна задача з `vTaskDelay` |

**Контекст**

```
## Реальний час без RTOS-фанатизму

Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на
віру:

| Потрібна точність | Чим робити |
|---|---|
| секунди | звичайна задача з `vTaskDelay` |
| десятки мілісекунд | задача з підвищеним пріоритетом |
| одиниці мілісекунд | апаратний таймер + переривання |
| мікросекунди | **апаратна периферія**: RMT, MCPWM, PCNT |
| гарантований жорсткий час | окремий мікроконтролер (розділ 57) |
```

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

<!-- fc id:T-32-070 sha:2fe46684 src:manual/32-nadiynist.md:177 klas:E -->
### T-32-070 · tablycya · `manual/32-nadiynist.md`

**Твердження, коротко**

> | десятки мілісекунд | задача з підвищеним пріоритетом |

**Контекст**

```
## Реальний час без RTOS-фанатизму

Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на
віру:

| Потрібна точність | Чим робити |
|---|---|
| секунди | звичайна задача з `vTaskDelay` |
| десятки мілісекунд | задача з підвищеним пріоритетом |
| одиниці мілісекунд | апаратний таймер + переривання |
| мікросекунди | **апаратна периферія**: RMT, MCPWM, PCNT |
| гарантований жорсткий час | окремий мікроконтролер (розділ 57) |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-071 sha:a28eac67 src:manual/32-nadiynist.md:178 klas:E -->
### T-32-071 · tablycya · `manual/32-nadiynist.md`

**Твердження, коротко**

> | одиниці мілісекунд | апаратний таймер + переривання |

**Контекст**

```
## Реальний час без RTOS-фанатизму

Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на
віру:

| Потрібна точність | Чим робити |
|---|---|
| секунди | звичайна задача з `vTaskDelay` |
| десятки мілісекунд | задача з підвищеним пріоритетом |
| одиниці мілісекунд | апаратний таймер + переривання |
| мікросекунди | **апаратна периферія**: RMT, MCPWM, PCNT |
| гарантований жорсткий час | окремий мікроконтролер (розділ 57) |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-072 sha:f752de15 src:manual/32-nadiynist.md:179 klas:F -->
### T-32-072 · tablycya · `manual/32-nadiynist.md`

**Твердження, коротко**

> | мікросекунди | **апаратна периферія**: RMT, MCPWM, PCNT |

**Контекст**

```
## Реальний час без RTOS-фанатизму

Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на
віру:

| Потрібна точність | Чим робити |
|---|---|
| секунди | звичайна задача з `vTaskDelay` |
| десятки мілісекунд | задача з підвищеним пріоритетом |
| одиниці мілісекунд | апаратний таймер + переривання |
| мікросекунди | **апаратна периферія**: RMT, MCPWM, PCNT |
| гарантований жорсткий час | окремий мікроконтролер (розділ 57) |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-073 sha:5dee921d src:manual/32-nadiynist.md:180 klas:E -->
### T-32-073 · tablycya · `manual/32-nadiynist.md`

**Твердження, коротко**

> | гарантований жорсткий час | окремий мікроконтролер (розділ 57) |

**Контекст**

```
## Реальний час без RTOS-фанатизму

Практичні орієнтири, які варто перевіряти вимірюванням, а не приймати на
віру:

| Потрібна точність | Чим робити |
|---|---|
| секунди | звичайна задача з `vTaskDelay` |
| десятки мілісекунд | задача з підвищеним пріоритетом |
| одиниці мілісекунд | апаратний таймер + переривання |
| мікросекунди | **апаратна периферія**: RMT, MCPWM, PCNT |
| гарантований жорсткий час | окремий мікроконтролер (розділ 57) |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-074 sha:20692047 src:manual/32-nadiynist.md:183 klas:E -->
### T-32-074 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Останній рядок — не поразка, а нормальне інженерне рішення.

**Контекст**

```
## Реальний час без RTOS-фанатизму

::: uvaha
Останній рядок — не поразка, а нормальне інженерне рішення. ESP32
чудовий у зв'язку й посередній у гарантованих таймінгах. Задача, де
потрібне й те, й те, природно ділиться між двома чипами: STM32 тримає
таймінги, ESP32 стоїть збоку і забезпечує зв'язок (розділ 01).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-075 sha:c1e1655b src:manual/32-nadiynist.md:183 klas:F -->
### T-32-075 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> ESP32 чудовий у зв'язку й посередній у гарантованих таймінгах.

**Контекст**

```
## Реальний час без RTOS-фанатизму

::: uvaha
Останній рядок — не поразка, а нормальне інженерне рішення. ESP32
чудовий у зв'язку й посередній у гарантованих таймінгах. Задача, де
потрібне й те, й те, природно ділиться між двома чипами: STM32 тримає
таймінги, ESP32 стоїть збоку і забезпечує зв'язок (розділ 01).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-076 sha:0c8c57fb src:manual/32-nadiynist.md:184 klas:F -->
### T-32-076 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Задача, де потрібне й те, й те, природно ділиться між двома чипами: STM32 тримає таймінги, ESP32 стоїть збоку і забезпечує зв'язок (розділ 01).

**Контекст**

```
## Реальний час без RTOS-фанатизму

::: uvaha
Останній рядок — не поразка, а нормальне інженерне рішення. ESP32
чудовий у зв'язку й посередній у гарантованих таймінгах. Задача, де
потрібне й те, й те, природно ділиться між двома чипами: STM32 тримає
таймінги, ESP32 стоїть збоку і забезпечує зв'язок (розділ 01).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-077 sha:b2c1ae60 src:manual/32-nadiynist.md:189 klas:E -->
### T-32-077 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Там, де таймінги критичні, найкраще рішення — **не робити їх у коді взагалі**.

**Контекст**

```
## Реальний час без RTOS-фанатизму

Там, де таймінги критичні, найкраще рішення — **не робити їх у коді
взагалі**. RMT формує імпульси WS2812 апаратно; MCPWM тримає мертвий час;
PCNT рахує імпульси. Периферія не залежить від того, чим зайнятий
процесор (розділ 33).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-078 sha:46ad545a src:manual/32-nadiynist.md:190 klas:F -->
### T-32-078 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> RMT формує імпульси WS2812 апаратно; MCPWM тримає мертвий час; PCNT рахує імпульси.

**Контекст**

```
## Реальний час без RTOS-фанатизму

Там, де таймінги критичні, найкраще рішення — **не робити їх у коді
взагалі**. RMT формує імпульси WS2812 апаратно; MCPWM тримає мертвий час;
PCNT рахує імпульси. Периферія не залежить від того, чим зайнятий
процесор (розділ 33).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-079 sha:a9f0f3fc src:manual/32-nadiynist.md:191 klas:E -->
### T-32-079 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Периферія не залежить від того, чим зайнятий процесор (розділ 33).

**Контекст**

```
## Реальний час без RTOS-фанатизму

Там, де таймінги критичні, найкраще рішення — **не робити їх у коді
взагалі**. RMT формує імпульси WS2812 апаратно; MCPWM тримає мертвий час;
PCNT рахує імпульси. Периферія не залежить від того, чим зайнятий
процесор (розділ 33).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-080 sha:0f4691b1 src:manual/32-nadiynist.md:196 klas:E -->
### T-32-080 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Те, що варто мати в кожній прошивці, яка їде в поле:

**Контекст**

```
## Мінімальний набір для виробу

Те, що варто мати в кожній прошивці, яка їде в поле:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-081 sha:ae4a96a9 src:manual/32-nadiynist.md:198 klas:A -->
### T-32-081 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> - логування причини скидання першим рядком `app_main` (розділ 26); - Task WDT, підписаний на головні робочі задачі; - обмежені повтори зі зростаючою паузою для всього мережевого; - деградація замість зупинки, де це можливо; - безпечний стан виконавчих механізмів, забезпечений апаратно; - періодичне логування мінімуму вільної пам'яті — виявляє витік (розділ 30); - coredump у флеші (розділ 26); - OTA з відкатом, якщо пристрій має оновлюватися (розділ 19).

**Контекст**

```
## Мінімальний набір для виробу

- логування причини скидання першим рядком `app_main` (розділ 26);
- Task WDT, підписаний на головні робочі задачі;
- обмежені повтори зі зростаючою паузою для всього мережевого;
- деградація замість зупинки, де це можливо;
- безпечний стан виконавчих механізмів, забезпечений апаратно;
- періодичне логування мінімуму вільної пам'яті — виявляє витік
  (розділ 30);
- coredump у флеші (розділ 26);
- OTA з відкатом, якщо пристрій має оновлюватися (розділ 19).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/esp32-c3_datasheet_en.pdf
- **Дослівно з джерела:**
  > • SRAM: 400 KB (16 KB for cache)
- **Спосіб і дата:** Source document retrieved 2026-08-27; quote verified against it by substring match.
- **Нотатка:** Datasheet підтверджує 400 КБ SRAM; твердження про адекватність для простих задач вимагає практичної оцінки. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-32-082 sha:9e04f85e src:manual/32-nadiynist.md:208 klas:E -->
### T-32-082 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Це перелік, який відрізняє пристрій, що працює місяцями без уваги, від пристрою, до якого треба їздити.

**Контекст**

```
## Мінімальний набір для виробу

Це перелік, який відрізняє пристрій, що працює місяцями без уваги, від
пристрою, до якого треба їздити.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-083 sha:fac227b0 src:manual/32-nadiynist.md:213 klas:A -->
### T-32-083 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> `ESP_ERROR_CHECK` — це `assert`.

**Контекст**

```
## Що з цього треба запам'ятати

`ESP_ERROR_CHECK` — це `assert`. У виробі він доречний лише там, де
помилка робить подальшу роботу безглуздою.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-32-084 sha:e0150223 src:manual/32-nadiynist.md:213 klas:E -->
### T-32-084 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> У виробі він доречний лише там, де помилка робить подальшу роботу безглуздою.

**Контекст**

```
## Що з цього треба запам'ятати

`ESP_ERROR_CHECK` — це `assert`. У виробі він доречний лише там, де
помилка робить подальшу роботу безглуздою.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-085 sha:62924b7e src:manual/32-nadiynist.md:216 klas:E -->
### T-32-085 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Три чесні стратегії: повторити з обмеженням, деградувати, перейти в безпечний стан.

**Контекст**

```
## Що з цього треба запам'ятати

Три чесні стратегії: повторити з обмеженням, деградувати, перейти в
безпечний стан. Деградація — найцінніша й найрідше реалізована.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-086 sha:10555fe8 src:manual/32-nadiynist.md:217 klas:E -->
### T-32-086 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Деградація — найцінніша й найрідше реалізована.

**Контекст**

```
## Що з цього треба запам'ятати

Три чесні стратегії: повторити з обмеженням, деградувати, перейти в
безпечний стан. Деградація — найцінніша й найрідше реалізована.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-087 sha:322756f4 src:manual/32-nadiynist.md:219 klas:E -->
### T-32-087 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Безпечний стан забезпечується резистором, а не кодом.

**Контекст**

```
## Що з цього треба запам'ятати

Безпечний стан забезпечується резистором, а не кодом. Питання до кожного
виходу: що станеться, якщо чип зникне зараз?
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові схеми управління MOSFET та рекомендації паспортів MOSFET
- **Дослівно з джерела:**
  > Затвор MOSFET:
  > GPIO ──[100–220 Ом]── Gate MOSFET
  > 
  > Цей резистор обмежує пік-струм при перезаписуванні затвору.
  > Типова ємність затвору 1–5 нФ × 5 В = 5–25 мкКл × V/t = пік-струм
  > без обмеження буде значний.
  > 
  > Опір 100–220 Ом обмежує цей дік-струм до розумних величин (~30–50 мА).
- **Спосіб і дата:** Типові рекомендації в MOSFET datasheet та сучасна практика, 2026-08-26
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-32-088 sha:105ed1b7 src:manual/32-nadiynist.md:219 klas:E -->
### T-32-088 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Питання до кожного виходу: що станеться, якщо чип зникне зараз?

**Контекст**

```
## Що з цього треба запам'ятати

Безпечний стан забезпечується резистором, а не кодом. Питання до кожного
виходу: що станеться, якщо чип зникне зараз?
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-089 sha:d9826450 src:manual/32-nadiynist.md:222 klas:E -->
### T-32-089 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Watchdog — інструмент, а не перешкода; годувати його треба після корисної роботи, а не в порожньому циклі.

**Контекст**

```
## Що з цього треба запам'ятати

Watchdog — інструмент, а не перешкода; годувати його треба після
корисної роботи, а не в порожньому циклі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-32-090 sha:a4a80472 src:manual/32-nadiynist.md:225 klas:E -->
### T-32-090 · proza · `manual/32-nadiynist.md`

**Твердження, коротко**

> Критичні таймінги віддають апаратній периферії або окремому чипу.

**Контекст**

```
## Що з цього треба запам'ятати

Критичні таймінги віддають апаратній периферії або окремому чипу.
```

**Доказ**

- **Клас:** F — не звірено

---
