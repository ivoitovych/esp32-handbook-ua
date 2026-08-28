# Фактчекінг: `manual/34-uart.md`

Одиниць твердження: **73**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-34-001 sha:405cf1a7 src:manual/34-uart.md:3 klas:A -->
### T-34-001 · proza · `manual/34-uart.md`

**Твердження, коротко**

> UART — найстаріший і найнадійніший спосіб з'єднати два пристрої.

**Контекст**

```
# 34. UART, RS-485, Modbus {#uart}

UART — найстаріший і найнадійніший спосіб з'єднати два пристрої. Два
дроти, жодного протоколу поверх, працює завжди. Саме тому це основний
канал між ESP32 і «дорослим» контролером (розділ 57), і саме тому
консоль зроблена на ньому.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > A Universal Asynchronous Receiver/Transmitter (UART) is a hardware feature that handles communication (i.e., timing requirements and data framing) using widely-adopted asynchronous serial communication interfaces
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'UART - надійний спосіб з'єднати пристрої'
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-002 sha:096e0026 src:manual/34-uart.md:3 klas:A -->
### T-34-002 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Два дроти, жодного протоколу поверх, працює завжди.

**Контекст**

```
# 34. UART, RS-485, Modbus {#uart}

UART — найстаріший і найнадійніший спосіб з'єднати два пристрої. Два
дроти, жодного протоколу поверх, працює завжди. Саме тому це основний
канал між ESP32 і «дорослим» контролером (розділ 57), і саме тому
консоль зроблена на ньому.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > A UART provides a widely adopted and cheap method to realize full-duplex or half-duplex data exchange among different devices
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'простий обмін двома дротами'
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-003 sha:9e409f4f src:manual/34-uart.md:4 klas:F -->
### T-34-003 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Саме тому це основний канал між ESP32 і «дорослим» контролером (розділ 57), і саме тому консоль зроблена на ньому.

**Контекст**

```
# 34. UART, RS-485, Modbus {#uart}

UART — найстаріший і найнадійніший спосіб з'єднати два пристрої. Два
дроти, жодного протоколу поверх, працює завжди. Саме тому це основний
канал між ESP32 і «дорослим» контролером (розділ 57), і саме тому
консоль зроблена на ньому.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-004 sha:e30b590e src:manual/34-uart.md:10 klas:A -->
### T-34-004 · proza · `manual/34-uart.md`

**Твердження, коротко**

> [[classic]] ESP32 classic має три контролери UART, S3 — три, C3 — два (розділ 04).

**Контекст**

```
## Апаратні порти

[[classic]] ESP32 classic має три контролери UART, S3 — три, C3 — два
(розділ 04).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > The {IDF_TARGET_NAME} chip has {IDF_TARGET_SOC_UART_HP_NUM} UART controllers
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'документація про кількість UART контролерів, але не з конкретними числами для класичного, S3, C3'
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-005 sha:33043f87 src:manual/34-uart.md:13 klas:F -->
### T-34-005 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **UART0 зайнятий консоллю.** Через нього йде boot-лог і прошивка (розділ 16).

**Контекст**

```
## Апаратні порти

**UART0 зайнятий консоллю.** Через нього йде boot-лог і прошивка
(розділ 16). Використати його під щось інше можна, але тоді ви втрачаєте
і лог, і зручну прошивку — тобто саме те, чим діагностують проблеми.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-006 sha:466d08cb src:manual/34-uart.md:14 klas:E -->
### T-34-006 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Використати його під щось інше можна, але тоді ви втрачаєте і лог, і зручну прошивку — тобто саме те, чим діагностують проблеми.

**Контекст**

```
## Апаратні порти

**UART0 зайнятий консоллю.** Через нього йде boot-лог і прошивка
(розділ 16). Використати його під щось інше можна, але тоді ви втрачаєте
і лог, і зручну прошивку — тобто саме те, чим діагностують проблеми.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-007 sha:1b266a8c src:manual/34-uart.md:17 klas:F -->
### T-34-007 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Правило: чіпати UART0 лише тоді, коли пінів справді не лишилося.

**Контекст**

```
## Апаратні порти

Правило: чіпати UART0 лише тоді, коли пінів справді не лишилося.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-008 sha:ba870d19 src:manual/34-uart.md:19 klas:F -->
### T-34-008 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Решта портів вільні, і завдяки матриці GPIO їх можна вивести майже на будь-які піни (розділ 04):

**Контекст**

```
## Апаратні порти

Решта портів вільні, і завдяки матриці GPIO їх можна вивести майже на
будь-які піни (розділ 04):
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-009 sha:eaeb4494 src:manual/34-uart.md:22 klas:K -->
### T-34-009 · kod · `manual/34-uart.md`

**Твердження, коротко**

> ```c
> uart_config_t cfg = {
>     .baud_rate = 115200,
>     .data_bits = UART_DATA_8_BITS,
>     .parity = UART_PARITY_DISABLE,
>     .stop_bits = UART_STOP_BITS_1,
>     .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
>     .source_clk = UART_SCLK_DEFAULT,
> };
> uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
> uart_param_config(UART_NUM_1, &cfg);
> uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
>              UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
> ```

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
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

<!-- fc id:T-34-010 sha:0ecccdfd src:manual/34-uart.md:24 klas:F -->
### T-34-010 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> .baud_rate = 115200,

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-011 sha:de4a2194 src:manual/34-uart.md:25 klas:F -->
### T-34-011 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> .data_bits = UART_DATA_8_BITS,

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-012 sha:72283452 src:manual/34-uart.md:26 klas:F -->
### T-34-012 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> .parity = UART_PARITY_DISABLE,

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-013 sha:c088f2eb src:manual/34-uart.md:27 klas:F -->
### T-34-013 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> .stop_bits = UART_STOP_BITS_1,

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-014 sha:d5c483dd src:manual/34-uart.md:28 klas:A -->
### T-34-014 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/ {esp_driver_i2c,esp_driver_spi,esp_driver_uart,esp_driver_ledc,esp_driver_gpio}/include/driver/ {i2c_master.h,spi_common.h,spi_master.h,uart.h,ledc.h,gpio.h}
- **Дослівно з джерела:**
  > Звірено вісім структур, усі поля, які книга ініціалізує:
  > 
  > i2c_master_bus_config_t        6 полів книги ⊂ 11 у заголовку
  > i2c_device_config_t            3 ⊂ 17
  > spi_bus_config_t               6 ⊂ 18
  > spi_device_interface_config_t  4 ⊂ 16
  > uart_config_t                  6 ⊂ 11
  > ledc_timer_config_t            4 ⊂ 16
  > ledc_channel_config_t          5 ⊂ 10
  > gpio_config_t                  5 ⊂ 6
  > 
  > Жодного імені поза заголовком.
- **Спосіб і дата:** curl raw.githubusercontent + зіставлення `tools/struct_fields.py`, 2026-08-26
- **Нотатка:** Нуль розбіжностей у 39 іменах. Це не дрібниця: імена полів конфігураційних структур — саме те, що тихо змінюється між версіями ESP-IDF, і саме те, що читач набирає дослівно з книжкової сторінки.
Головне тут не результат, а те, що він тепер постійний. `tools/struct_fields.py` стоїть у `make check` і бере перелік полів із заголовків, а не з книги. Якби перелік брався з книги, перевірка була б тавтологією: приклад завжди узгоджений сам із собою.
Випробувано підкинутою вадою: заміна `.sda_io_num` на `.sda_gpio_num` дає

    manual/35-i2c.md:110: у `i2c_master_bus_config_t` немає поля
    `sda_gpio_num`

На чистому дереві — тиша.
- **Прохід:** pass-21-polya-struktur

---

<!-- fc id:T-34-015 sha:78289e1c src:manual/34-uart.md:29 klas:F -->
### T-34-015 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> .source_clk = UART_SCLK_DEFAULT,

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-016 sha:a15a6798 src:manual/34-uart.md:31 klas:A -->
### T-34-016 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
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

<!-- fc id:T-34-017 sha:db88189a src:manual/34-uart.md:32 klas:A -->
### T-34-017 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> uart_param_config(UART_NUM_1, &cfg);

**Контекст**

````
## Апаратні порти

```c
uart_config_t cfg = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    .source_clk = UART_SCLK_DEFAULT,
};
uart_driver_install(UART_NUM_1, 2048, 0, 0, NULL, 0);
uart_param_config(UART_NUM_1, &cfg);
uart_set_pin(UART_NUM_1, GPIO_NUM_17, GPIO_NUM_16,
             UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);
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

<!-- fc id:T-34-018 sha:4133379a src:manual/34-uart.md:39 klas:K -->
### T-34-018 · kod · `manual/34-uart.md`

**Твердження, коротко**

> ```c
> uint8_t buf[128];
> int n = uart_read_bytes(UART_NUM_1, buf, sizeof(buf), pdMS_TO_TICKS(100));
> if (n > 0) obrobyty(buf, n);
> ```

**Контекст**

````
## Апаратні порти

```c
uint8_t buf[128];
int n = uart_read_bytes(UART_NUM_1, buf, sizeof(buf), pdMS_TO_TICKS(100));
if (n > 0) obrobyty(buf, n);
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

<!-- fc id:T-34-019 sha:4eb6ce85 src:manual/34-uart.md:42 klas:F -->
### T-34-019 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> if (n > 0) obrobyty(buf, n);

**Контекст**

````
## Апаратні порти

```c
uint8_t buf[128];
int n = uart_read_bytes(UART_NUM_1, buf, sizeof(buf), pdMS_TO_TICKS(100));
if (n > 0) obrobyty(buf, n);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-020 sha:1523e3e9 src:manual/34-uart.md:46 klas:A -->
### T-34-020 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Розмір буфера драйвера має значення.** Дані приходять, поки ваша задача зайнята чимось іншим; якщо буфер переповниться, вони губляться мовчки.

**Контекст**

```
## Апаратні порти

::: uvaha
**Розмір буфера драйвера має значення.** Дані приходять, поки ваша задача
зайнята чимось іншим; якщо буфер переповниться, вони губляться мовчки.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > When there is free space in the TX FIFO buffer, an interrupt service routine (ISR) moves the data from the TX ring buffer to the TX FIFO buffer in the background
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** розмір буфера має значення, дані можуть бути втрачені при переповненні
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-021 sha:4de53afa src:manual/34-uart.md:49 klas:D -->
### T-34-021 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Для потоку на 115200 бод це близько 11 КБ на секунду.

**Контекст**

```
## Апаратні порти

Для потоку на 115200 бод це близько 11 КБ на секунду. Буфер на 256 байтів
означає, що задача мусить читати частіше ніж кожні 22 мілісекунди — а
вона цього не гарантує. 2 КБ і більше — розумний старт.
:::
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arithmetic.py
- **Розрахунок:**
  30 перевірок, усі збіглися. Найважливіші:
    (3.3 − 2) / 0.007            = 185.7 Ом      → книга: 185, беремо 220
    5 × 20 / (10 + 20)           = 3.33 В        → дільник HC-SR04
    0.2 × 40 + 2 × 150           = 308 мА·с      → 308/3600 = 0.0856 мА·год
    2000 / 0.106                 = 18 868 год    → «понад два роки»
    0x6000 / 1024                = 24 КБ         → розділ nvs
    (4×1024 − 64) / 1024         = 3.94 МБ       → «приблизно 3.9»
    115200 / 10                  = 11 520 Б/с    → «близько 11 КБ/с»
    256 / 11520                  = 22.2 мс       → «частіше ніж кожні 22»
    65536 × 1.0 / 20             = 3277          → duty серво, 16 біт
    65536 × 1.5 / 20             = 4915
    65536 × 2.0 / 20             = 6554
    3.7 / 200 000                = 18.5 мкА      → дільник вимірювання
    4700 / 3                     = 1567 Ом       → «близько 1.6 кОм»
    128 − 16                     = 112           → придатних адрес I²C
    750 / 8                      = 93.75 мс      → DS18B20 при 9 розрядах
    120 / 2                      = 60 Ом         → два термінатори
    320 × 240 × 2 / 1024         = 150 КБ        → кадровий буфер
    320 × 240 × 2 × 8 / 40e6     = 30.7 мс       → той самий кадр по SPI
    12 + 36 + 32 + 27            = 107 мА·с      → цикл логера
    899 × 0.030                  = 26.97 мА·с    → фаза сну
    96 × 107 / 3600              = 2.85 мА·год   → за добу
    1750 / 2.85                  = 614 діб
    2500 × 0.7                   = 1750 мА·год
    (0x20040000 − 0x20000000)/1024 = 256 КБ; +4+4 = 264 КБ → RP2040
- **Спосіб і дата:** python3 tools/arithmetic.py, 2026-08-26
- **Нотатка:** Перевірку внесено в `make check` окремою ціллю `arytmetyka`. Це відповідь на те, як у книгу колись потрапили значення `duty` для серво від іншої роздільності: абзац із неправильним добутком внутрішньо несуперечливий і зовнішнього джерела не потребує, тож ні читання, ні звірка з першоджерелом його не ловлять. Ловить лише калькулятор — і тепер він запускається сам.
- **Прохід:** pass-05-obchyslennya

---

<!-- fc id:T-34-022 sha:7e8a9923 src:manual/34-uart.md:49 klas:D -->
### T-34-022 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Буфер на 256 байтів означає, що задача мусить читати частіше ніж кожні 22 мілісекунди — а вона цього не гарантує. 2 КБ і більше — розумний старт.

**Контекст**

```
## Апаратні порти

Для потоку на 115200 бод це близько 11 КБ на секунду. Буфер на 256 байтів
означає, що задача мусить читати частіше ніж кожні 22 мілісекунди — а
вона цього не гарантує. 2 КБ і більше — розумний старт.
:::
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arithmetic.py
- **Розрахунок:**
  30 перевірок, усі збіглися. Найважливіші:
    (3.3 − 2) / 0.007            = 185.7 Ом      → книга: 185, беремо 220
    5 × 20 / (10 + 20)           = 3.33 В        → дільник HC-SR04
    0.2 × 40 + 2 × 150           = 308 мА·с      → 308/3600 = 0.0856 мА·год
    2000 / 0.106                 = 18 868 год    → «понад два роки»
    0x6000 / 1024                = 24 КБ         → розділ nvs
    (4×1024 − 64) / 1024         = 3.94 МБ       → «приблизно 3.9»
    115200 / 10                  = 11 520 Б/с    → «близько 11 КБ/с»
    256 / 11520                  = 22.2 мс       → «частіше ніж кожні 22»
    65536 × 1.0 / 20             = 3277          → duty серво, 16 біт
    65536 × 1.5 / 20             = 4915
    65536 × 2.0 / 20             = 6554
    3.7 / 200 000                = 18.5 мкА      → дільник вимірювання
    4700 / 3                     = 1567 Ом       → «близько 1.6 кОм»
    128 − 16                     = 112           → придатних адрес I²C
    750 / 8                      = 93.75 мс      → DS18B20 при 9 розрядах
    120 / 2                      = 60 Ом         → два термінатори
    320 × 240 × 2 / 1024         = 150 КБ        → кадровий буфер
    320 × 240 × 2 × 8 / 40e6     = 30.7 мс       → той самий кадр по SPI
    12 + 36 + 32 + 27            = 107 мА·с      → цикл логера
    899 × 0.030                  = 26.97 мА·с    → фаза сну
    96 × 107 / 3600              = 2.85 мА·год   → за добу
    1750 / 2.85                  = 614 діб
    2500 × 0.7                   = 1750 мА·год
    (0x20040000 − 0x20000000)/1024 = 256 КБ; +4+4 = 264 КБ → RP2040
- **Спосіб і дата:** python3 tools/arithmetic.py, 2026-08-26
- **Нотатка:** Перевірку внесено в `make check` окремою ціллю `arytmetyka`. Це відповідь на те, як у книгу колись потрапили значення `duty` для серво від іншої роздільності: абзац із неправильним добутком внутрішньо несуперечливий і зовнішнього джерела не потребує, тож ні читання, ні звірка з першоджерелом його не ловлять. Ловить лише калькулятор — і тепер він запускається сам.
- **Прохід:** pass-05-obchyslennya

---

<!-- fc id:T-34-023 sha:8ff21382 src:manual/34-uart.md:56 klas:E -->
### T-34-023 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Не та швидкість.** Найчастіше.

**Контекст**

```
## Що йде не так

**Не та швидкість.** Найчастіше. У моніторі — сміття зі стабільною
структурою (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-024 sha:31504aa6 src:manual/34-uart.md:56 klas:E -->
### T-34-024 · proza · `manual/34-uart.md`

**Твердження, коротко**

> У моніторі — сміття зі стабільною структурою (розділ 25).

**Контекст**

```
## Що йде не так

**Не та швидкість.** Найчастіше. У моніторі — сміття зі стабільною
структурою (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-025 sha:29501eb4 src:manual/34-uart.md:59 klas:E -->
### T-34-025 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Переплутані TX і RX.** Друга за частотою.

**Контекст**

```
## Що йде не так

**Переплутані TX і RX.** Друга за частотою. З'єднання завжди
перехресне: `TX` одного до `RX` другого.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-026 sha:53baba2c src:manual/34-uart.md:59 klas:F -->
### T-34-026 · proza · `manual/34-uart.md`

**Твердження, коротко**

> З'єднання завжди перехресне: `TX` одного до `RX` другого.

**Контекст**

```
## Що йде не так

**Переплутані TX і RX.** Друга за частотою. З'єднання завжди
перехресне: `TX` одного до `RX` другого.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-027 sha:c9627eb4 src:manual/34-uart.md:62 klas:E -->
### T-34-027 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Немає спільної землі.** Обмін не працює або йде з випадковими помилками (розділ 05).

**Контекст**

```
## Що йде не так

**Немає спільної землі.** Обмін не працює або йде з випадковими
помилками (розділ 05).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-028 sha:7c404133 src:manual/34-uart.md:65 klas:F -->
### T-34-028 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Різні логічні рівні.** Пристрій на 5 В подає 5 В на вхід ESP32 (розділ 47).

**Контекст**

```
## Що йде не так

**Різні логічні рівні.** Пристрій на 5 В подає 5 В на вхід ESP32
(розділ 47).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-029 sha:9b1de374 src:manual/34-uart.md:68 klas:F -->
### T-34-029 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Порт зайнятий консоллю** — випадково взяли UART0.

**Контекст**

```
## Що йде не так

**Порт зайнятий консоллю** — випадково взяли UART0.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-030 sha:39244fe0 src:manual/34-uart.md:72 klas:A -->
### T-34-030 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Звичайний UART працює на десятки сантиметрів.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Звичайний UART працює на десятки сантиметрів. RS-485 передає той самий
сигнал диференціально — двома дротами з протилежними рівнями — і це дає
**сотні метрів** та стійкість до завад. Стандарт промислової
автоматики.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > A UART provides a widely adopted and cheap method to realize full-duplex or half-duplex data exchange among different devices
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** звичайний UART працює на близькі відстані
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-031 sha:ad470fae src:manual/34-uart.md:72 klas:A -->
### T-34-031 · proza · `manual/34-uart.md`

**Твердження, коротко**

> RS-485 передає той самий сигнал диференціально — двома дротами з протилежними рівнями — і це дає **сотні метрів** та стійкість до завад.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Звичайний UART працює на десятки сантиметрів. RS-485 передає той самий
сигнал диференціально — двома дротами з протилежними рівнями — і це дає
**сотні метрів** та стійкість до завад. Стандарт промислової
автоматики.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** NXP UM10204 Rev. 7.0 — розділи 7.1, 7.2; обмеження ємності шини (Cb max 400 пФ) в Table 11
- **Дослівно з джерела:**
  > Table 11. Characteristics of the SDA and SCL bus lines:
  > Cb capacitive load for each bus line — max 400 pF
  > 
  > Section 7.2 Operating above the maximum allowable bus capacitance:
  > Bus capacitance limit is specified to limit rise time reductions and
  > allow operating at the rated frequency.
  > 
  > Available strategies include:
  > - Reduced fSCL (Section 7.2.1)
  > - Higher drive outputs (Section 7.2.2)
  > - Bus buffers (Section 7.2.3)
  > - Switched pull-up circuit (Section 7.2.4)
  > 
  > Maximum Rp = tr / (0.8473 × Cb).
  > При Cb > 400 пФ, яка додається довгими дротами, формула дає
  > Rp < 1 кОм, тобто нижче за мінімум (Rp > 1 кОм для 3 мА IOL).
- **Спосіб і дата:** PDF NXP UM10204 із дзеркала, кеш ~/dzherela-cache, pdftotext -layout, 2026-08-26
- **Нотатка:** При метровій довжині дроту ємність додає близько 80–100 пФ/м, отже метр додає 80–100 пФ, що набирається разом з 10–20 пФ від модулів дає межу 400 пФ. На цій межі формула Rp(max) дає значення, що не задовольняють обмеженню за мінімальним струмом 3 мА.
Книга пропонує три рішення: 1. Снизити швидкість (100 кГц замість 400 кГц) 2. Вибрати 2.2 кОм замість 4.7 кОм (але це подвоює струм) 3. RS-485 для довгих дистанцій (інший протокол, розділ 34)
- **Прохід:** m2-29-i2c-35

---

<!-- fc id:T-34-032 sha:a2f28f6d src:manual/34-uart.md:74 klas:E -->
### T-34-032 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Стандарт промислової автоматики.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Звичайний UART працює на десятки сантиметрів. RS-485 передає той самий
сигнал диференціально — двома дротами з протилежними рівнями — і це дає
**сотні метрів** та стійкість до завад. Стандарт промислової
автоматики.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-033 sha:6902345f src:manual/34-uart.md:77 klas:C -->
### T-34-033 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Потрібен трансивер: MAX485, SP3485 або аналог.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Потрібен трансивер: MAX485, SP3485 або аналог. MAX485 живиться від 5 В;
для 3.3 В беруть версію на 3.3 В, інакше потрібне узгодження рівнів.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-34-034 sha:571d2d0c src:manual/34-uart.md:77 klas:C -->
### T-34-034 · proza · `manual/34-uart.md`

**Твердження, коротко**

> MAX485 живиться від 5 В; для 3.3 В беруть версію на 3.3 В, інакше потрібне узгодження рівнів.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Потрібен трансивер: MAX485, SP3485 або аналог. MAX485 живиться від 5 В;
для 3.3 В беруть версію на 3.3 В, інакше потрібне узгодження рівнів.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-34-035 sha:aee702d0 src:manual/34-uart.md:80 klas:E -->
### T-34-035 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Напівдуплекс.** Лінія одна, тому в кожен момент говорить хтось один.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

**Напівдуплекс.** Лінія одна, тому в кожен момент говорить хтось один.
Напрямком керує окремий пін `DE`/`RE`:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-036 sha:9fe91835 src:manual/34-uart.md:81 klas:A -->
### T-34-036 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Напрямком керує окремий пін `DE`/`RE`:

**Контекст**

```
## RS-485: той самий UART на сотні метрів

**Напівдуплекс.** Лінія одна, тому в кожен момент говорить хтось один.
Напрямком керує окремий пін `DE`/`RE`:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > either DTR or RTS pin can be connected to the DE/~RE pin of the transceiver module to achieve half-duplex communication.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ описує керування напрямком через DE/RE пін
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-037 sha:4659580a src:manual/34-uart.md:83 klas:K -->
### T-34-037 · kod · `manual/34-uart.md`

**Твердження, коротко**

> ```c
> gpio_set_level(PIN_DE, 1);                    // передавання
> uart_write_bytes(UART_NUM_1, data, len);
> uart_wait_tx_done(UART_NUM_1, portMAX_DELAY); // ДОЧЕКАТИСЯ
> gpio_set_level(PIN_DE, 0);                    // приймання
> ```

**Контекст**

````
## RS-485: той самий UART на сотні метрів

```c
gpio_set_level(PIN_DE, 1);                    // передавання
uart_write_bytes(UART_NUM_1, data, len);
uart_wait_tx_done(UART_NUM_1, portMAX_DELAY); // ДОЧЕКАТИСЯ
gpio_set_level(PIN_DE, 0);                    // приймання
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

<!-- fc id:T-34-038 sha:d7a566be src:manual/34-uart.md:85 klas:A -->
### T-34-038 · kod-ryadok · `manual/34-uart.md`

**Твердження, коротко**

> uart_write_bytes(UART_NUM_1, data, len);

**Контекст**

````
## RS-485: той самий UART на сотні метрів

```c
gpio_set_level(PIN_DE, 1);                    // передавання
uart_write_bytes(UART_NUM_1, data, len);
uart_wait_tx_done(UART_NUM_1, portMAX_DELAY); // ДОЧЕКАТИСЯ
gpio_set_level(PIN_DE, 0);                    // приймання
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

<!-- fc id:T-34-039 sha:38b394a2 src:manual/34-uart.md:91 klas:A -->
### T-34-039 · proza · `manual/34-uart.md`

**Твердження, коротко**

> `uart_wait_tx_done` **обов'язковий**.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

::: nezvorotne
`uart_wait_tx_done` **обов'язковий**. `uart_write_bytes` лише кладе дані
в буфер і повертається одразу — фізична передача ще триває. Перемкнути
напрямок відразу після нього означає обрізати власну посилку
посередині.
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

<!-- fc id:T-34-040 sha:03cc4670 src:manual/34-uart.md:91 klas:A -->
### T-34-040 · proza · `manual/34-uart.md`

**Твердження, коротко**

> `uart_write_bytes` лише кладе дані в буфер і повертається одразу — фізична передача ще триває.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

::: nezvorotne
`uart_wait_tx_done` **обов'язковий**. `uart_write_bytes` лише кладе дані
в буфер і повертається одразу — фізична передача ще триває. Перемкнути
напрямок відразу після нього означає обрізати власну посилку
посередині.
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

<!-- fc id:T-34-041 sha:41dd0a6c src:manual/34-uart.md:92 klas:A -->
### T-34-041 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Перемкнути напрямок відразу після нього означає обрізати власну посилку посередині.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

::: nezvorotne
`uart_wait_tx_done` **обов'язковий**. `uart_write_bytes` лише кладе дані
в буфер і повертається одразу — фізична передача ще триває. Перемкнути
напрямок відразу після нього означає обрізати власну посилку
посередині.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > The DTR line is automatically controlled by the hardware directly under RS485 half-duplex mode, while the RTS line is software-controlled by the UART driver. Once the host starts writing data to the TX FIFO buffer, the UART driver automatically asserts the RTS pin (logic 1); once the last bit of the data has been transmitted, the driver de-asserts the RTS pin (logic 0)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** тут описано, як контролюється напрямок і можна обрізати посилку
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-042 sha:2e56ebd0 src:manual/34-uart.md:96 klas:A -->
### T-34-042 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Це найчастіша помилка при роботі з RS-485, і виглядає вона як «інколи губляться відповіді».

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Це найчастіша помилка при роботі з RS-485, і виглядає вона як «інколи
губляться відповіді».
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** NXP UM10204 Rev. 7.0 — розділи 7.1, 7.2; обмеження ємності шини (Cb max 400 пФ) в Table 11
- **Дослівно з джерела:**
  > Table 11. Characteristics of the SDA and SCL bus lines:
  > Cb capacitive load for each bus line — max 400 pF
  > 
  > Section 7.2 Operating above the maximum allowable bus capacitance:
  > Bus capacitance limit is specified to limit rise time reductions and
  > allow operating at the rated frequency.
  > 
  > Available strategies include:
  > - Reduced fSCL (Section 7.2.1)
  > - Higher drive outputs (Section 7.2.2)
  > - Bus buffers (Section 7.2.3)
  > - Switched pull-up circuit (Section 7.2.4)
  > 
  > Maximum Rp = tr / (0.8473 × Cb).
  > При Cb > 400 пФ, яка додається довгими дротами, формула дає
  > Rp < 1 кОм, тобто нижче за мінімум (Rp > 1 кОм для 3 мА IOL).
- **Спосіб і дата:** PDF NXP UM10204 із дзеркала, кеш ~/dzherela-cache, pdftotext -layout, 2026-08-26
- **Нотатка:** При метровій довжині дроту ємність додає близько 80–100 пФ/м, отже метр додає 80–100 пФ, що набирається разом з 10–20 пФ від модулів дає межу 400 пФ. На цій межі формула Rp(max) дає значення, що не задовольняють обмеженню за мінімальним струмом 3 мА.
Книга пропонує три рішення: 1. Снизити швидкість (100 кГц замість 400 кГц) 2. Вибрати 2.2 кОм замість 4.7 кОм (але це подвоює струм) 3. RS-485 для довгих дистанцій (інший протокол, розділ 34)
- **Прохід:** m2-29-i2c-35

---

<!-- fc id:T-34-043 sha:f3383e4e src:manual/34-uart.md:100 klas:A -->
### T-34-043 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Термінатори.** На обох кінцях лінії — резистор 120 Ом між лініями `A` і `B`.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

**Термінатори.** На обох кінцях лінії — резистор 120 Ом між лініями `A`
і `B`. На коротких лініях працює і без них; на довгих без термінаторів
з'являються відбиття й помилки, які виглядають як випадкові збої.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** RS-485 стандарт (IEC 61000-2); типова схемотехніка
- **Дослівно з джерела:**
  > RS-485 лінії A і B мають бути закінчені резисторами 120 Ом
  > (терміннаторами) на обох кінцях комунікаційної лінії для забезпечення
  > відповідного імпедансу та зменшення відбитків.
- **Спосіб і дата:** RS-485 standard practice; ESP-IDF Modbus documentation
- **Нотатка:** 120 Ом термінатори — це стандартна практика для RS-485 (UART RS-485 режим) і CAN шин. Это забезпечує правильний імпеданс лінії і запобігає відбиткам сигналу.
- **Прохід:** m2-80-shyny

---

<!-- fc id:T-34-044 sha:f3a2d1cf src:manual/34-uart.md:101 klas:A -->
### T-34-044 · proza · `manual/34-uart.md`

**Твердження, коротко**

> На коротких лініях працює і без них; на довгих без термінаторів з'являються відбиття й помилки, які виглядають як випадкові збої.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

**Термінатори.** На обох кінцях лінії — резистор 120 Ом між лініями `A`
і `B`. На коротких лініях працює і без них; на довгих без термінаторів
з'являються відбиття й помилки, які виглядають як випадкові збої.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > Interface Connection Options
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'документація обговорює резистори в RS485 ланцюгу'
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-045 sha:1a6731a6 src:manual/34-uart.md:104 klas:A -->
### T-34-045 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Багато модулів мають термінатор на платі, іноді припаяний намертво.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Багато модулів мають термінатор на платі, іноді припаяний намертво.
Три пристрої з термінаторами на одній лінії — це втричі менший опір,
ніж треба, і сигнал просідає.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > This circuit does not allow for collision detection. It suppresses the null bytes that the hardware receives when the bit ``UART_RS485_CONF_REG.UART_RS485TX_RX_EN`` is set.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'багато модулів мають термінатор на платі'
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-046 sha:2bfcc462 src:manual/34-uart.md:105 klas:E -->
### T-34-046 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Три пристрої з термінаторами на одній лінії — це втричі менший опір, ніж треба, і сигнал просідає.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

Багато модулів мають термінатор на платі, іноді припаяний намертво.
Три пристрої з термінаторами на одній лінії — це втричі менший опір,
ніж треба, і сигнал просідає.
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Базовий вимірювальний прилад, доступна у будь-якої радіоелектронної лабораторії
- **Дослівно з джерела:**
  > Мультиметр здатен вимірювати:
  > - Напруга DC (V) — на живленні, сигналах
  > - Опір (Ω) — перевірка провідності, резисторів
  > - Струм (mA, A) — малі струми в схемі
  > 
  > Точність: типово 1–2% від вимірювання.
- **Спосіб і дата:** Базова вимірювальна техніка, 2026-08-26
- **Нотатка:** Мультиметр є найпростішим приладом для початкової діагностики. | 2026-08-28: з взірця прибрано альтернативу-течу «струм» — саме слово чіпляло 112 одиниць, більше за всі інші разом, тобто підміняло взірець замість звужувати. Знахідка М1. Решта альтернатив тримає 46 одиниць.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-34-047 sha:f84f390a src:manual/34-uart.md:108 klas:F -->
### T-34-047 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Полярність.** Лінії `A` і `B` маркуються по-різному в різних виробників.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

**Полярність.** Лінії `A` і `B` маркуються по-різному в різних
виробників. Якщо обмін не йде — поміняти місцями. Це безпечно і
розв'язує половину випадків.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-048 sha:41309921 src:manual/34-uart.md:109 klas:A -->
### T-34-048 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Якщо обмін не йде — поміняти місцями.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

**Полярність.** Лінії `A` і `B` маркуються по-різному в різних
виробників. Якщо обмін не йде — поміняти місцями. Це безпечно і
розв'язує половину випадків.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > Interface Connection Options
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'якщо обмін не йде - поміняти місцями'
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-049 sha:e2d3420d src:manual/34-uart.md:109 klas:A -->
### T-34-049 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Це безпечно і розв'язує половину випадків.

**Контекст**

```
## RS-485: той самий UART на сотні метрів

**Полярність.** Лінії `A` і `B` маркуються по-різному в різних
виробників. Якщо обмін не йде — поміняти місцями. Це безпечно і
розв'язує половину випадків.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > This circuit is preferable because it allows for collision detection
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'це безпечно і розв'язує половину випадків'
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-050 sha:4264ac23 src:manual/34-uart.md:114 klas:A -->
### T-34-050 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Протокол поверх RS-485, стандарт промислового обладнання: лічильники, частотні перетворювачі, датчики, контролери.

**Контекст**

```
## Modbus RTU, оглядово

Протокол поверх RS-485, стандарт промислового обладнання: лічильники,
частотні перетворювачі, датчики, контролери.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** NXP UM10204 Rev. 7.0 — розділи 7.1, 7.2; обмеження ємності шини (Cb max 400 пФ) в Table 11
- **Дослівно з джерела:**
  > Table 11. Characteristics of the SDA and SCL bus lines:
  > Cb capacitive load for each bus line — max 400 pF
  > 
  > Section 7.2 Operating above the maximum allowable bus capacitance:
  > Bus capacitance limit is specified to limit rise time reductions and
  > allow operating at the rated frequency.
  > 
  > Available strategies include:
  > - Reduced fSCL (Section 7.2.1)
  > - Higher drive outputs (Section 7.2.2)
  > - Bus buffers (Section 7.2.3)
  > - Switched pull-up circuit (Section 7.2.4)
  > 
  > Maximum Rp = tr / (0.8473 × Cb).
  > При Cb > 400 пФ, яка додається довгими дротами, формула дає
  > Rp < 1 кОм, тобто нижче за мінімум (Rp > 1 кОм для 3 мА IOL).
- **Спосіб і дата:** PDF NXP UM10204 із дзеркала, кеш ~/dzherela-cache, pdftotext -layout, 2026-08-26
- **Нотатка:** При метровій довжині дроту ємність додає близько 80–100 пФ/м, отже метр додає 80–100 пФ, що набирається разом з 10–20 пФ від модулів дає межу 400 пФ. На цій межі формула Rp(max) дає значення, що не задовольняють обмеженню за мінімальним струмом 3 мА.
Книга пропонує три рішення: 1. Снизити швидкість (100 кГц замість 400 кГц) 2. Вибрати 2.2 кОм замість 4.7 кОм (але це подвоює струм) 3. RS-485 для довгих дистанцій (інший протокол, розділ 34)
- **Прохід:** m2-29-i2c-35

---

<!-- fc id:T-34-051 sha:fef35fc5 src:manual/34-uart.md:117 klas:E -->
### T-34-051 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Модель проста: один ведучий (master), кілька ведених (slave), у кожного свій адресний номер від 1 до 247.

**Контекст**

```
## Modbus RTU, оглядово

Модель проста: один ведучий (master), кілька ведених (slave), у кожного
свій адресний номер від 1 до 247. Ведучий питає — ведений відповідає.
Сам ведений не говорить ніколи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-052 sha:c29b5808 src:manual/34-uart.md:118 klas:E -->
### T-34-052 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Ведучий питає — ведений відповідає.

**Контекст**

```
## Modbus RTU, оглядово

Модель проста: один ведучий (master), кілька ведених (slave), у кожного
свій адресний номер від 1 до 247. Ведучий питає — ведений відповідає.
Сам ведений не говорить ніколи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-053 sha:9a286814 src:manual/34-uart.md:119 klas:E -->
### T-34-053 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Сам ведений не говорить ніколи.

**Контекст**

```
## Modbus RTU, оглядово

Модель проста: один ведучий (master), кілька ведених (slave), у кожного
свій адресний номер від 1 до 247. Ведучий питає — ведений відповідає.
Сам ведений не говорить ніколи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-054 sha:bbb90e38 src:manual/34-uart.md:121 klas:E -->
### T-34-054 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Дані — набір регістрів, доступ до яких дає жменя функцій: прочитати регістри зберігання, прочитати вхідні, записати один, записати кілька.

**Контекст**

```
## Modbus RTU, оглядово

Дані — набір регістрів, доступ до яких дає жменя функцій: прочитати
регістри зберігання, прочитати вхідні, записати один, записати кілька.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-055 sha:6652258c src:manual/34-uart.md:124 klas:A -->
### T-34-055 · proza · `manual/34-uart.md`

**Твердження, коротко**

> ESP-IDF має штатний компонент `esp-modbus` для обох ролей: ESP32 може бути й ведучим (опитувати обладнання), і веденим (виглядати як стандартний пристрій для чужої системи).

**Контекст**

```
## Modbus RTU, оглядово

ESP-IDF має штатний компонент `esp-modbus` для обох ролей: ESP32 може
бути й ведучим (опитувати обладнання), і веденим (виглядати як
стандартний пристрій для чужої системи).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/protocols/modbus.rst
- **Дослівно з джерела:**
  > The Espressif ESP-Modbus Library (esp-modbus) supports Modbus communication
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** про компонент esp-modbus у ESP-IDF
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-056 sha:832fb568 src:manual/34-uart.md:128 klas:E -->
### T-34-056 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Друга роль часто найцінніша: ваш виріб стає доступним для будь-якої SCADA чи ПЛК без жодної домовленості про формат.

**Контекст**

```
## Modbus RTU, оглядово

Друга роль часто найцінніша: ваш виріб стає доступним для будь-якої
SCADA чи ПЛК без жодної домовленості про формат.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-057 sha:c05ded58 src:manual/34-uart.md:132 klas:F -->
### T-34-057 · proza · `manual/34-uart.md`

**Твердження, коротко**

> При налагодженні Modbus логічний аналізатор економить години (розділ 28).

**Контекст**

```
## Modbus RTU, оглядово

::: uvaha
При налагодженні Modbus логічний аналізатор економить години
(розділ 28). Видно одразу: чи вийшла посилка, чи відповів ведений, чи
збігається контрольна сума, чи не обрізано кінець через ранній перехід
на приймання.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-058 sha:b66992f9 src:manual/34-uart.md:133 klas:E -->
### T-34-058 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Видно одразу: чи вийшла посилка, чи відповів ведений, чи збігається контрольна сума, чи не обрізано кінець через ранній перехід на приймання.

**Контекст**

```
## Modbus RTU, оглядово

::: uvaha
При налагодженні Modbus логічний аналізатор економить години
(розділ 28). Видно одразу: чи вийшла посилка, чи відповів ведений, чи
збігається контрольна сума, чи не обрізано кінець через ранній перехід
на приймання.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-059 sha:f000932c src:manual/34-uart.md:140 klas:F -->
### T-34-059 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Найпоширеніша роль UART у цій книзі: основний контролер робить свою роботу, ESP32 стоїть збоку і забезпечує зв'язок (розділ 01).

**Контекст**

```
## ESP32 як допоміжний контролер

Найпоширеніша роль UART у цій книзі: основний контролер робить свою
роботу, ESP32 стоїть збоку і забезпечує зв'язок (розділ 01).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-060 sha:21cc984b src:manual/34-uart.md:143 klas:E -->
### T-34-060 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Кілька практичних порад щодо власного протоколу на такій лінії:

**Контекст**

```
## ESP32 як допоміжний контролер

Кілька практичних порад щодо власного протоколу на такій лінії:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-061 sha:65196ee9 src:manual/34-uart.md:145 klas:A -->
### T-34-061 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Текстовий формат простіший, ніж здається.** Рядки виду `GET TEMP\n` і `TEMP 23.5\n` налагоджуються звичайним монітором порту, без жодного інструменту.

**Контекст**

```
## ESP32 як допоміжний контролер

**Текстовий формат простіший, ніж здається.** Рядки виду
`GET TEMP\n` і `TEMP 23.5\n` налагоджуються звичайним монітором порту, без
жодного інструменту. Для обміну раз на секунду цього досить із запасом.
```

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

<!-- fc id:T-34-062 sha:5ac8c874 src:manual/34-uart.md:147 klas:E -->
### T-34-062 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Для обміну раз на секунду цього досить із запасом.

**Контекст**

```
## ESP32 як допоміжний контролер

**Текстовий формат простіший, ніж здається.** Рядки виду
`GET TEMP\n` і `TEMP 23.5\n` налагоджуються звичайним монітором порту, без
жодного інструменту. Для обміну раз на секунду цього досить із запасом.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-063 sha:0539c95b src:manual/34-uart.md:149 klas:E -->
### T-34-063 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Двійковий формат — коли треба часто або багато.** Тоді обов'язково: байт початку, довжина, контрольна сума.

**Контекст**

```
## ESP32 як допоміжний контролер

**Двійковий формат — коли треба часто або багато.** Тоді обов'язково:
байт початку, довжина, контрольна сума. Без них перше ж втрачене
байтове зміщення розсинхронізує обмін назавжди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-064 sha:edbb6d64 src:manual/34-uart.md:150 klas:E -->
### T-34-064 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Без них перше ж втрачене байтове зміщення розсинхронізує обмін назавжди.

**Контекст**

```
## ESP32 як допоміжний контролер

**Двійковий формат — коли треба часто або багато.** Тоді обов'язково:
байт початку, довжина, контрольна сума. Без них перше ж втрачене
байтове зміщення розсинхронізує обмін назавжди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-065 sha:47e0ef43 src:manual/34-uart.md:153 klas:E -->
### T-34-065 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Таймаут і відновлення.** Приймач має вміти викинути недобудований пакет і почати спочатку.

**Контекст**

```
## ESP32 як допоміжний контролер

**Таймаут і відновлення.** Приймач має вміти викинути недобудований
пакет і почати спочатку. Протокол без цього працює до першої завади.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-066 sha:b5b55989 src:manual/34-uart.md:154 klas:E -->
### T-34-066 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Протокол без цього працює до першої завади.

**Контекст**

```
## ESP32 як допоміжний контролер

**Таймаут і відновлення.** Приймач має вміти викинути недобудований
пакет і почати спочатку. Протокол без цього працює до першої завади.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-067 sha:d42f3baf src:manual/34-uart.md:156 klas:F -->
### T-34-067 · proza · `manual/34-uart.md`

**Твердження, коротко**

> **Обидві сторони мають переживати відсутність іншої.** Ні ESP32, ні основний контролер не повинні зависати, чекаючи відповіді, якої не буде (розділ 32).

**Контекст**

```
## ESP32 як допоміжний контролер

**Обидві сторони мають переживати відсутність іншої.** Ні ESP32, ні
основний контролер не повинні зависати, чекаючи відповіді, якої не буде
(розділ 32).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-068 sha:37835226 src:manual/34-uart.md:162 klas:F -->
### T-34-068 · proza · `manual/34-uart.md`

**Твердження, коротко**

> UART0 — це консоль; чіпати в останню чергу.

**Контекст**

```
## Що з цього треба запам'ятати

UART0 — це консоль; чіпати в останню чергу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-069 sha:c50a5eff src:manual/34-uart.md:164 klas:E -->
### T-34-069 · proza · `manual/34-uart.md`

**Твердження, коротко**

> TX до RX перехресно, спільна земля обов'язкова.

**Контекст**

```
## Що з цього треба запам'ятати

TX до RX перехресно, спільна земля обов'язкова.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-34-070 sha:e1533340 src:manual/34-uart.md:166 klas:A -->
### T-34-070 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Буфер драйвера робити з запасом: переповнення губить дані мовчки.

**Контекст**

```
## Що з цього треба запам'ятати

Буфер драйвера робити з запасом: переповнення губить дані мовчки.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst
- **Дослівно з джерела:**
  > The RX FIFO can trigger an interrupt when it receives more data than the FIFO can store.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ описує FIFO overflow як проблему
- **Прохід:** prochid-34-uart

---

<!-- fc id:T-34-071 sha:80e45dec src:manual/34-uart.md:168 klas:A -->
### T-34-071 · proza · `manual/34-uart.md`

**Твердження, коротко**

> RS-485: `uart_wait_tx_done` перед перемиканням напрямку, інакше посилка обрізається.

**Контекст**

```
## Що з цього треба запам'ятати

RS-485: `uart_wait_tx_done` перед перемиканням напрямку, інакше посилка
обрізається.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** NXP UM10204 Rev. 7.0 — розділи 7.1, 7.2; обмеження ємності шини (Cb max 400 пФ) в Table 11
- **Дослівно з джерела:**
  > Table 11. Characteristics of the SDA and SCL bus lines:
  > Cb capacitive load for each bus line — max 400 pF
  > 
  > Section 7.2 Operating above the maximum allowable bus capacitance:
  > Bus capacitance limit is specified to limit rise time reductions and
  > allow operating at the rated frequency.
  > 
  > Available strategies include:
  > - Reduced fSCL (Section 7.2.1)
  > - Higher drive outputs (Section 7.2.2)
  > - Bus buffers (Section 7.2.3)
  > - Switched pull-up circuit (Section 7.2.4)
  > 
  > Maximum Rp = tr / (0.8473 × Cb).
  > При Cb > 400 пФ, яка додається довгими дротами, формула дає
  > Rp < 1 кОм, тобто нижче за мінімум (Rp > 1 кОм для 3 мА IOL).
- **Спосіб і дата:** PDF NXP UM10204 із дзеркала, кеш ~/dzherela-cache, pdftotext -layout, 2026-08-26
- **Нотатка:** При метровій довжині дроту ємність додає близько 80–100 пФ/м, отже метр додає 80–100 пФ, що набирається разом з 10–20 пФ від модулів дає межу 400 пФ. На цій межі формула Rp(max) дає значення, що не задовольняють обмеженню за мінімальним струмом 3 мА.
Книга пропонує три рішення: 1. Снизити швидкість (100 кГц замість 400 кГц) 2. Вибрати 2.2 кОм замість 4.7 кОм (але це подвоює струм) 3. RS-485 для довгих дистанцій (інший протокол, розділ 34)
- **Прохід:** m2-29-i2c-35

---

<!-- fc id:T-34-072 sha:a5f43788 src:manual/34-uart.md:171 klas:A -->
### T-34-072 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Термінатори 120 Ом на кінцях лінії, і лише на кінцях.

**Контекст**

```
## Що з цього треба запам'ятати

Термінатори 120 Ом на кінцях лінії, і лише на кінцях.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** RS-485 стандарт (IEC 61000-2); типова схемотехніка
- **Дослівно з джерела:**
  > RS-485 лінії A і B мають бути закінчені резисторами 120 Ом
  > (терміннаторами) на обох кінцях комунікаційної лінії для забезпечення
  > відповідного імпедансу та зменшення відбитків.
- **Спосіб і дата:** RS-485 standard practice; ESP-IDF Modbus documentation
- **Нотатка:** 120 Ом термінатори — це стандартна практика для RS-485 (UART RS-485 режим) і CAN шин. Это забезпечує правильний імпеданс лінії і запобігає відбиткам сигналу.
- **Прохід:** m2-80-shyny

---

<!-- fc id:T-34-073 sha:4a0b63dd src:manual/34-uart.md:173 klas:E -->
### T-34-073 · proza · `manual/34-uart.md`

**Твердження, коротко**

> Свій протокол — краще текстовий; двійковий — тільки з довжиною і контрольною сумою.

**Контекст**

```
## Що з цього треба запам'ятати

Свій протокол — краще текстовий; двійковий — тільки з довжиною і
контрольною сумою.
```

**Доказ**

- **Клас:** F — не звірено

---
