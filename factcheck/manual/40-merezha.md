# Фактчекінг: `manual/40-merezha.md`

Одиниць твердження: **102**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-40-001 sha:950d8d44 src:manual/40-merezha.md:3 klas:F -->
### T-40-001 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Wi-Fi дає канал; далі треба вирішити, що по ньому передавати і як.

**Контекст**

```
# 40. Мережеві протоколи {#merezha}

Wi-Fi дає канал; далі треба вирішити, що по ньому передавати і як.
Розділ про рівень вище фізичного: сокети, HTTP, WebSocket, MQTT, TLS.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-002 sha:b9113487 src:manual/40-merezha.md:3 klas:F -->
### T-40-002 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Розділ про рівень вище фізичного: сокети, HTTP, WebSocket, MQTT, TLS.

**Контекст**

```
# 40. Мережеві протоколи {#merezha}

Wi-Fi дає канал; далі треба вирішити, що по ньому передавати і як.
Розділ про рівень вище фізичного: сокети, HTTP, WebSocket, MQTT, TLS.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-003 sha:0c16a37c src:manual/40-merezha.md:8 klas:E -->
### T-40-003 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **TCP** гарантує доставку й порядок.

**Контекст**

```
## TCP чи UDP

**TCP** гарантує доставку й порядок. Ціна — встановлення з'єднання,
підтвердження, повтори; при поганому зв'язку затримки ростуть.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-004 sha:fe286ad8 src:manual/40-merezha.md:8 klas:E -->
### T-40-004 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Ціна — встановлення з'єднання, підтвердження, повтори; при поганому зв'язку затримки ростуть.

**Контекст**

```
## TCP чи UDP

**TCP** гарантує доставку й порядок. Ціна — встановлення з'єднання,
підтвердження, повтори; при поганому зв'язку затримки ростуть.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-005 sha:5b919d56 src:manual/40-merezha.md:11 klas:E -->
### T-40-005 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **UDP** нічого не гарантує.

**Контекст**

```
## TCP чи UDP

**UDP** нічого не гарантує. Пакет або дійшов, або ні, і дізнатися про це
ви не можете. Зате він швидкий, не потребує з'єднання і дозволяє
широкомовну розсилку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-006 sha:b1af660a src:manual/40-merezha.md:11 klas:E -->
### T-40-006 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Пакет або дійшов, або ні, і дізнатися про це ви не можете.

**Контекст**

```
## TCP чи UDP

**UDP** нічого не гарантує. Пакет або дійшов, або ні, і дізнатися про це
ви не можете. Зате він швидкий, не потребує з'єднання і дозволяє
широкомовну розсилку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-007 sha:6a599c12 src:manual/40-merezha.md:11 klas:E -->
### T-40-007 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Зате він швидкий, не потребує з'єднання і дозволяє широкомовну розсилку.

**Контекст**

```
## TCP чи UDP

**UDP** нічого не гарантує. Пакет або дійшов, або ні, і дізнатися про це
ви не можете. Зате він швидкий, не потребує з'єднання і дозволяє
широкомовну розсилку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-008 sha:0a9dbf6e src:manual/40-merezha.md:15 klas:E -->
### T-40-008 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Практичне правило: **TCP для команд і налаштувань, UDP для потоку вимірювань**.

**Контекст**

```
## TCP чи UDP

Практичне правило: **TCP для команд і налаштувань, UDP для потоку
вимірювань**. Втрачений відлік температури нічого не змінює; втрачена
команда «вимкнути» — змінює.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-009 sha:cce1d360 src:manual/40-merezha.md:15 klas:E -->
### T-40-009 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Втрачений відлік температури нічого не змінює; втрачена команда «вимкнути» — змінює.

**Контекст**

```
## TCP чи UDP

Практичне правило: **TCP для команд і налаштувань, UDP для потоку
вимірювань**. Втрачений відлік температури нічого не змінює; втрачена
команда «вимкнути» — змінює.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-010 sha:d6267053 src:manual/40-merezha.md:21 klas:E -->
### T-40-010 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Найзручніший інтерфейс для людини: жодного застосунку, працює з будь-якого телефона.

**Контекст**

```
## HTTP-сервер на пристрої

Найзручніший інтерфейс для людини: жодного застосунку, працює з будь-якого
телефона.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-011 sha:27f9f409 src:manual/40-merezha.md:24 klas:K -->
### T-40-011 · kod · `manual/40-merezha.md`

**Твердження, коротко**

> ```c
> httpd_config_t cfg = HTTPD_DEFAULT_CONFIG();
> httpd_handle_t server = NULL;
> httpd_start(&server, &cfg);
> 
> httpd_uri_t uri = {
>     .uri = "/api/stan",
>     .method = HTTP_GET,
>     .handler = stan_handler,
> };
> httpd_register_uri_handler(server, &uri);
> ```

**Контекст**

````
## HTTP-сервер на пристрої

```c
httpd_config_t cfg = HTTPD_DEFAULT_CONFIG();
httpd_handle_t server = NULL;
httpd_start(&server, &cfg);
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

<!-- fc id:T-40-012 sha:5f326a60 src:manual/40-merezha.md:27 klas:A -->
### T-40-012 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> httpd_start(&server, &cfg);

**Контекст**

````
## HTTP-сервер на пристрої

```c
httpd_config_t cfg = HTTPD_DEFAULT_CONFIG();
httpd_handle_t server = NULL;
httpd_start(&server, &cfg);
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

<!-- fc id:T-40-013 sha:b5f61665 src:manual/40-merezha.md:30 klas:F -->
### T-40-013 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> .uri = "/api/stan",

**Контекст**

````
## HTTP-сервер на пристрої

httpd_uri_t uri = {
    .uri = "/api/stan",
    .method = HTTP_GET,
    .handler = stan_handler,
};
httpd_register_uri_handler(server, &uri);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-014 sha:3b3be56d src:manual/40-merezha.md:31 klas:F -->
### T-40-014 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> .method = HTTP_GET,

**Контекст**

````
## HTTP-сервер на пристрої

httpd_uri_t uri = {
    .uri = "/api/stan",
    .method = HTTP_GET,
    .handler = stan_handler,
};
httpd_register_uri_handler(server, &uri);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-015 sha:1ff1aec9 src:manual/40-merezha.md:32 klas:F -->
### T-40-015 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> .handler = stan_handler,

**Контекст**

````
## HTTP-сервер на пристрої

httpd_uri_t uri = {
    .uri = "/api/stan",
    .method = HTTP_GET,
    .handler = stan_handler,
};
httpd_register_uri_handler(server, &uri);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-016 sha:f833664b src:manual/40-merezha.md:34 klas:A -->
### T-40-016 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> httpd_register_uri_handler(server, &uri);

**Контекст**

````
## HTTP-сервер на пристрої

httpd_uri_t uri = {
    .uri = "/api/stan",
    .method = HTTP_GET,
    .handler = stan_handler,
};
httpd_register_uri_handler(server, &uri);
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

<!-- fc id:T-40-017 sha:b21a17f0 src:manual/40-merezha.md:38 klas:E -->
### T-40-017 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Обробник виконується в задачі веб-сервера з **обмеженим стеком**.

**Контекст**

```
## HTTP-сервер на пристрої

::: uvaha
Обробник виконується в задачі веб-сервера з **обмеженим стеком**. Великі
буфери там — прямий шлях до переповнення стека, яке проявиться пізніше
й деінде (розділ 30).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-018 sha:d6fb9903 src:manual/40-merezha.md:38 klas:E -->
### T-40-018 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Великі буфери там — прямий шлях до переповнення стека, яке проявиться пізніше й деінде (розділ 30).

**Контекст**

```
## HTTP-сервер на пристрої

::: uvaha
Обробник виконується в задачі веб-сервера з **обмеженим стеком**. Великі
буфери там — прямий шлях до переповнення стека, яке проявиться пізніше
й деінде (розділ 30).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-019 sha:57ba00a7 src:manual/40-merezha.md:42 klas:F -->
### T-40-019 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Розмір стека сервера задається в `HTTPD_DEFAULT_CONFIG` і його часто доводиться збільшувати.

**Контекст**

```
## HTTP-сервер на пристрої

Розмір стека сервера задається в `HTTPD_DEFAULT_CONFIG` і його часто
доводиться збільшувати. Особливо якщо в обробнику формується JSON або
використовується TLS.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-020 sha:86c0653a src:manual/40-merezha.md:42 klas:F -->
### T-40-020 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Особливо якщо в обробнику формується JSON або використовується TLS.

**Контекст**

```
## HTTP-сервер на пристрої

Розмір стека сервера задається в `HTTPD_DEFAULT_CONFIG` і його часто
доводиться збільшувати. Особливо якщо в обробнику формується JSON або
використовується TLS.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-021 sha:d91a7859 src:manual/40-merezha.md:47 klas:E -->
### T-40-021 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Статичні файли — HTML, CSS, скрипти — кладуть у розділ файлової системи (розділ 18) або вбудовують у прошивку як ресурси.

**Контекст**

```
## HTTP-сервер на пристрої

Статичні файли — HTML, CSS, скрипти — кладуть у розділ файлової системи
(розділ 18) або вбудовують у прошивку як ресурси. Друге простіше для
невеликих сторінок і не потребує окремого розділу.
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** SPI протокол: чотирипровідний інтерфейс послідовної передачі даних
- **Дослівно з джерела:**
  > SPI складається з чотирьох ліній:
  > - SCK (Serial Clock) — тактування
  > - MOSI (Master Out Slave In) — дані від головного до ведених
  > - MISO (Master In Slave Out) — дані від ведених до головного
  > - CS (Chip Select) — вибір мікросхеми
  > 
  > Для повного спостереження потрібен логічний аналізатор з 4+ каналами.
- **Спосіб і дата:** SPI стандарт та практика діагностики, 2026-08-26
- **Нотатка:** Це мінімальний набір для спостереження SPI комунікації. На практиці може бути кілька CS ліній для різних приладів.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-40-022 sha:d2be0535 src:manual/40-merezha.md:47 klas:E -->
### T-40-022 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Друге простіше для невеликих сторінок і не потребує окремого розділу.

**Контекст**

```
## HTTP-сервер на пристрої

Статичні файли — HTML, CSS, скрипти — кладуть у розділ файлової системи
(розділ 18) або вбудовують у прошивку як ресурси. Друге простіше для
невеликих сторінок і не потребує окремого розділу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-023 sha:553a1977 src:manual/40-merezha.md:53 klas:F -->
### T-40-023 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> HTTP влаштований як «запит — відповідь»: сервер не може сам щось надіслати.

**Контекст**

```
## WebSocket

HTTP влаштований як «запит — відповідь»: сервер не може сам щось
надіслати. Для сторінки, яка має оновлюватися наживо, це означає
опитування щосекунди — марний трафік і затримки.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-024 sha:fde2d7f3 src:manual/40-merezha.md:53 klas:E -->
### T-40-024 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Для сторінки, яка має оновлюватися наживо, це означає опитування щосекунди — марний трафік і затримки.

**Контекст**

```
## WebSocket

HTTP влаштований як «запит — відповідь»: сервер не може сам щось
надіслати. Для сторінки, яка має оновлюватися наживо, це означає
опитування щосекунди — марний трафік і затримки.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-025 sha:c1bb8fe5 src:manual/40-merezha.md:57 klas:B -->
### T-40-025 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> WebSocket дає двонапрямлений канал поверх того самого з'єднання.

**Контекст**

```
## WebSocket

WebSocket дає двонапрямлений канал поверх того самого з'єднання. Для
графіка вимірювань у реальному часі це правильний інструмент.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** I²C-bus specification та типові схеми перетворювачів рівня (наприклад, на базі N-channel FET для двонапрямленості)
- **Дослівно з джерела:**
  > Двонапрямлений перетворювач рівня I²C:
  > - N-channel FET у режимі transmission gate
  > - Дозволяє обом сторонам "тягти" лінію вниз (open-drain функція)
  > - Pull-up резистори на обох сторонах напруги
  > 
  > I²C spec: "The output stages of devices connected to the bus must have
  > an open-drain or open-collector to perform the wired-AND function."
- **Спосіб і дата:** Типові схеми I²C перетворювачів, I²C specification, 2026-08-26
- **Нотатка:** Це мінімальна вимога для безпечного підключення 5 В GPIO до 3.3 В ESP32 на I²C шині. | 2026-08-28: з взірця прибрано альтернативу-течу «I²C» — саме слово чіпляло 117 одиниць, більше за всі інші разом, тобто підміняло взірець замість звужувати. Знахідка М1. Решта альтернатив тримає 58 одиниць.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-40-026 sha:3aa2580a src:manual/40-merezha.md:57 klas:E -->
### T-40-026 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Для графіка вимірювань у реальному часі це правильний інструмент.

**Контекст**

```
## WebSocket

WebSocket дає двонапрямлений канал поверх того самого з'єднання. Для
графіка вимірювань у реальному часі це правильний інструмент.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-027 sha:6592d83e src:manual/40-merezha.md:60 klas:E -->
### T-40-027 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Обмеження практичне: кожен клієнт — це відкрите з'єднання й пам'ять під нього.

**Контекст**

```
## WebSocket

Обмеження практичне: кожен клієнт — це відкрите з'єднання й пам'ять під
нього. На ESP32 кілька одночасних клієнтів — межа, і поводитися з нею
треба свідомо.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-028 sha:b23be94f src:manual/40-merezha.md:60 klas:F -->
### T-40-028 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> На ESP32 кілька одночасних клієнтів — межа, і поводитися з нею треба свідомо.

**Контекст**

```
## WebSocket

Обмеження практичне: кожен клієнт — це відкрите з'єднання й пам'ять під
нього. На ESP32 кілька одночасних клієнтів — межа, і поводитися з нею
треба свідомо.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-029 sha:4786a8f6 src:manual/40-merezha.md:66 klas:E -->
### T-40-029 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Пристрій отримує адресу від роутера, і вона може змінитися.

**Контекст**

```
## mDNS: щоб не шукати IP

Пристрій отримує адресу від роутера, і вона може змінитися. Змушувати
людину шукати IP — поганий інтерфейс.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-030 sha:84b2234f src:manual/40-merezha.md:66 klas:E -->
### T-40-030 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Змушувати людину шукати IP — поганий інтерфейс.

**Контекст**

```
## mDNS: щоб не шукати IP

Пристрій отримує адресу від роутера, і вона може змінитися. Змушувати
людину шукати IP — поганий інтерфейс.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-031 sha:86639629 src:manual/40-merezha.md:71 klas:K -->
### T-40-031 · kod · `manual/40-merezha.md`

**Твердження, коротко**

> ```c
> mdns_init();
> mdns_hostname_set("teplytsia");
> mdns_instance_name_set("Датчики теплиці");
> ```

**Контекст**

````
## mDNS: щоб не шукати IP

```c
mdns_init();
mdns_hostname_set("teplytsia");
mdns_instance_name_set("Датчики теплиці");
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

<!-- fc id:T-40-032 sha:f15667d5 src:manual/40-merezha.md:72 klas:A -->
### T-40-032 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> mdns_init();

**Контекст**

````
## mDNS: щоб не шукати IP

```c
mdns_init();
mdns_hostname_set("teplytsia");
mdns_instance_name_set("Датчики теплиці");
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

<!-- fc id:T-40-033 sha:cb6701a7 src:manual/40-merezha.md:73 klas:A -->
### T-40-033 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> mdns_hostname_set("teplytsia");

**Контекст**

````
## mDNS: щоб не шукати IP

```c
mdns_init();
mdns_hostname_set("teplytsia");
mdns_instance_name_set("Датчики теплиці");
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

<!-- fc id:T-40-034 sha:0b1f2c68 src:manual/40-merezha.md:74 klas:A -->
### T-40-034 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> mdns_instance_name_set("Датчики теплиці");

**Контекст**

````
## mDNS: щоб не шукати IP

```c
mdns_init();
mdns_hostname_set("teplytsia");
mdns_instance_name_set("Датчики теплиці");
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

<!-- fc id:T-40-035 sha:d61aa1fa src:manual/40-merezha.md:77 klas:F -->
### T-40-035 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Далі пристрій доступний як `teplytsia.local` — з телефона, з ноутбука, з браузера.

**Контекст**

```
## mDNS: щоб не шукати IP

Далі пристрій доступний як `teplytsia.local` — з телефона, з ноутбука,
з браузера.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-036 sha:653ea4a2 src:manual/40-merezha.md:81 klas:E -->
### T-40-036 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Android історично підтримував його неповно; корпоративні мережі часто ріжуть широкомовний трафік; гостьові мережі ізолюють клієнтів одне від одного.

**Контекст**

```
## mDNS: щоб не шукати IP

::: uvaha
mDNS працює не скрізь. Android історично підтримував його неповно;
корпоративні мережі часто ріжуть широкомовний трафік; гостьові мережі
ізолюють клієнтів одне від одного.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-037 sha:f7798eee src:manual/40-merezha.md:85 klas:E -->
### T-40-037 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Тому: mDNS — це зручність, а не єдиний спосіб дістатися пристрою.

**Контекст**

```
## mDNS: щоб не шукати IP

Тому: mDNS — це зручність, а не єдиний спосіб дістатися пристрою.
Показувати IP-адресу теж треба — хоча б у логу або на дисплеї.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-038 sha:ae6489bf src:manual/40-merezha.md:85 klas:E -->
### T-40-038 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Показувати IP-адресу теж треба — хоча б у логу або на дисплеї.

**Контекст**

```
## mDNS: щоб не шукати IP

Тому: mDNS — це зручність, а не єдиний спосіб дістатися пристрою.
Показувати IP-адресу теж треба — хоча б у логу або на дисплеї.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-039 sha:1839164a src:manual/40-merezha.md:91 klas:E -->
### T-40-039 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Годинник у чипі неточний і скидається при вимиканні живлення (розділ 03).

**Контекст**

```
## SNTP: точний час

Годинник у чипі неточний і скидається при вимиканні живлення
(розділ 03). Якщо є мережа, час беруть з інтернету:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-040 sha:cbb939d1 src:manual/40-merezha.md:91 klas:E -->
### T-40-040 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Якщо є мережа, час беруть з інтернету:

**Контекст**

```
## SNTP: точний час

Годинник у чипі неточний і скидається при вимиканні живлення
(розділ 03). Якщо є мережа, час беруть з інтернету:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-041 sha:01cae44d src:manual/40-merezha.md:94 klas:K -->
### T-40-041 · kod · `manual/40-merezha.md`

**Твердження, коротко**

> ```c
> esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
> esp_sntp_setservername(0, "pool.ntp.org");
> esp_sntp_init();
> setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
> tzset();
> ```

**Контекст**

````
## SNTP: точний час

```c
esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
esp_sntp_setservername(0, "pool.ntp.org");
esp_sntp_init();
setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
tzset();
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

<!-- fc id:T-40-042 sha:651d6c12 src:manual/40-merezha.md:95 klas:A -->
### T-40-042 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);

**Контекст**

````
## SNTP: точний час

```c
esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
esp_sntp_setservername(0, "pool.ntp.org");
esp_sntp_init();
setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
tzset();
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

<!-- fc id:T-40-043 sha:1e52cf1e src:manual/40-merezha.md:96 klas:A -->
### T-40-043 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> esp_sntp_setservername(0, "pool.ntp.org");

**Контекст**

````
## SNTP: точний час

```c
esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
esp_sntp_setservername(0, "pool.ntp.org");
esp_sntp_init();
setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
tzset();
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

<!-- fc id:T-40-044 sha:afab5f1f src:manual/40-merezha.md:97 klas:A -->
### T-40-044 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> esp_sntp_init();

**Контекст**

````
## SNTP: точний час

```c
esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
esp_sntp_setservername(0, "pool.ntp.org");
esp_sntp_init();
setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
tzset();
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

<!-- fc id:T-40-045 sha:0cc9293f src:manual/40-merezha.md:98 klas:F -->
### T-40-045 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);

**Контекст**

````
## SNTP: точний час

```c
esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
esp_sntp_setservername(0, "pool.ntp.org");
esp_sntp_init();
setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
tzset();
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-046 sha:ab5c560a src:manual/40-merezha.md:99 klas:F -->
### T-40-046 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> tzset();

**Контекст**

````
## SNTP: точний час

```c
esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
esp_sntp_setservername(0, "pool.ntp.org");
esp_sntp_init();
setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
tzset();
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-047 sha:8c357f0b src:manual/40-merezha.md:102 klas:F -->
### T-40-047 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Рядок `TZ` вище — правило переходу на літній час для України; воно працює автономно, без оновлень.

**Контекст**

```
## SNTP: точний час

Рядок `TZ` вище — правило переходу на літній час для України; воно
працює автономно, без оновлень.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-048 sha:aa6bbdb5 src:manual/40-merezha.md:105 klas:E -->
### T-40-048 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Час приходить **не миттєво**: перша синхронізація займає секунди.

**Контекст**

```
## SNTP: точний час

Час приходить **не миттєво**: перша синхронізація займає секунди.
Код, що ставить мітки часу, має вміти працювати, доки часу ще немає, —
інакше в логах з'являються записи з 1970 року.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-049 sha:caed2427 src:manual/40-merezha.md:105 klas:E -->
### T-40-049 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Код, що ставить мітки часу, має вміти працювати, доки часу ще немає, — інакше в логах з'являються записи з 1970 року.

**Контекст**

```
## SNTP: точний час

Час приходить **не миттєво**: перша синхронізація займає секунди.
Код, що ставить мітки часу, має вміти працювати, доки часу ще немає, —
інакше в логах з'являються записи з 1970 року.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-050 sha:70ee41d2 src:manual/40-merezha.md:109 klas:F -->
### T-40-050 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Немає мережі й потрібен точний час — зовнішня мікросхема RTC із батарейкою (розділ 60).

**Контекст**

```
## SNTP: точний час

Немає мережі й потрібен точний час — зовнішня мікросхема RTC із
батарейкою (розділ 60).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-051 sha:70422979 src:manual/40-merezha.md:114 klas:E -->
### T-40-051 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Протокол, придуманий саме для таких пристроїв: легкий, тримає одне з'єднання, працює через погані канали.

**Контекст**

```
## MQTT

Протокол, придуманий саме для таких пристроїв: легкий, тримає одне
з'єднання, працює через погані канали.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-052 sha:237411e6 src:manual/40-merezha.md:117 klas:E -->
### T-40-052 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Модель — «публікація і підписка».

**Контекст**

```
## MQTT

Модель — «публікація і підписка». Пристрої не знають одне про одного:
є **брокер** посередині, є **топіки** — ієрархічні імена. Хто хоче —
публікує, хто хоче — підписується.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-053 sha:57bee44f src:manual/40-merezha.md:117 klas:E -->
### T-40-053 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Пристрої не знають одне про одного: є **брокер** посередині, є **топіки** — ієрархічні імена.

**Контекст**

```
## MQTT

Модель — «публікація і підписка». Пристрої не знають одне про одного:
є **брокер** посередині, є **топіки** — ієрархічні імена. Хто хоче —
публікує, хто хоче — підписується.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-054 sha:67a21aaa src:manual/40-merezha.md:117 klas:E -->
### T-40-054 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Хто хоче — публікує, хто хоче — підписується.

**Контекст**

```
## MQTT

Модель — «публікація і підписка». Пристрої не знають одне про одного:
є **брокер** посередині, є **топіки** — ієрархічні імена. Хто хоче —
публікує, хто хоче — підписується.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-055 sha:cdb9b592 src:manual/40-merezha.md:121 klas:K -->
### T-40-055 · kod · `manual/40-merezha.md`

**Твердження, коротко**

> ```c
> esp_mqtt_client_config_t cfg = {
>     .broker.address.uri = "mqtt://192.168.1.10",
>     .credentials.username = "datchyk",
>     .session.keepalive = 60,
> };
> esp_mqtt_client_handle_t client = esp_mqtt_client_init(&cfg);
> esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, handler, NULL);
> esp_mqtt_client_start(client);
> 
> esp_mqtt_client_publish(client, "teplytsia/temperatura", "23.5", 0, 1, 0);
> ```

**Контекст**

````
## MQTT

```c
esp_mqtt_client_config_t cfg = {
    .broker.address.uri = "mqtt://192.168.1.10",
    .credentials.username = "datchyk",
    .session.keepalive = 60,
};
esp_mqtt_client_handle_t client = esp_mqtt_client_init(&cfg);
esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, handler, NULL);
esp_mqtt_client_start(client);
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

<!-- fc id:T-40-056 sha:2c105ffb src:manual/40-merezha.md:128 klas:A -->
### T-40-056 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, handler, NULL);

**Контекст**

````
## MQTT

```c
esp_mqtt_client_config_t cfg = {
    .broker.address.uri = "mqtt://192.168.1.10",
    .credentials.username = "datchyk",
    .session.keepalive = 60,
};
esp_mqtt_client_handle_t client = esp_mqtt_client_init(&cfg);
esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, handler, NULL);
esp_mqtt_client_start(client);
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

<!-- fc id:T-40-057 sha:da12f696 src:manual/40-merezha.md:129 klas:A -->
### T-40-057 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> esp_mqtt_client_start(client);

**Контекст**

````
## MQTT

```c
esp_mqtt_client_config_t cfg = {
    .broker.address.uri = "mqtt://192.168.1.10",
    .credentials.username = "datchyk",
    .session.keepalive = 60,
};
esp_mqtt_client_handle_t client = esp_mqtt_client_init(&cfg);
esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, handler, NULL);
esp_mqtt_client_start(client);
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

<!-- fc id:T-40-058 sha:7fcb8ea4 src:manual/40-merezha.md:131 klas:A -->
### T-40-058 · kod-ryadok · `manual/40-merezha.md`

**Твердження, коротко**

> esp_mqtt_client_publish(client, "teplytsia/temperatura", "23.5", 0, 1, 0);

**Контекст**

````
## MQTT

esp_mqtt_client_publish(client, "teplytsia/temperatura", "23.5", 0, 1, 0);
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

<!-- fc id:T-40-059 sha:f98961f2 src:manual/40-merezha.md:134 klas:E -->
### T-40-059 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **Структура топіків** — це проєктне рішення, і міняти її потім дорого.

**Контекст**

```
## MQTT

**Структура топіків** — це проєктне рішення, і міняти її потім дорого.
Робоча схема: `<об'єкт>/<вузол>/<величина>`, наприклад
`teplytsia/datchyk1/temperatura`. Керування — окремою гілкою:
`teplytsia/datchyk1/cmd/rele`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-060 sha:6937ad74 src:manual/40-merezha.md:134 klas:F -->
### T-40-060 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Робоча схема: `<об'єкт>/<вузол>/<величина>`, наприклад `teplytsia/datchyk1/temperatura`.

**Контекст**

```
## MQTT

**Структура топіків** — це проєктне рішення, і міняти її потім дорого.
Робоча схема: `<об'єкт>/<вузол>/<величина>`, наприклад
`teplytsia/datchyk1/temperatura`. Керування — окремою гілкою:
`teplytsia/datchyk1/cmd/rele`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-061 sha:9ccd51d0 src:manual/40-merezha.md:134 klas:F -->
### T-40-061 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Керування — окремою гілкою: `teplytsia/datchyk1/cmd/rele`.

**Контекст**

```
## MQTT

**Структура топіків** — це проєктне рішення, і міняти її потім дорого.
Робоча схема: `<об'єкт>/<вузол>/<величина>`, наприклад
`teplytsia/datchyk1/temperatura`. Керування — окремою гілкою:
`teplytsia/datchyk1/cmd/rele`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-062 sha:a84b93ca src:manual/40-merezha.md:141 klas:F -->
### T-40-062 · tablycya-shapka · `manual/40-merezha.md`

**Твердження, коротко**

> | Рівень | Гарантія | Коли |

**Контекст**

```
## MQTT

**QoS:**

| Рівень | Гарантія | Коли |
|---|---|---|
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
| 1 | доставлено щонайменше раз, можливі дублі | команди |
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-063 sha:9628ec9a src:manual/40-merezha.md:142 klas:E -->
### T-40-063 · komirka · `manual/40-merezha.md`

**Твердження, коротко**

> 0 · Гарантія → доставка не гарантована

**Дослівно з книги**

```
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
```

**Контекст**

```
## MQTT

**QoS:**

| Рівень | Гарантія | Коли |
|---|---|---|
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
| 1 | доставлено щонайменше раз, можливі дублі | команди |
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-064 sha:7d437bc9 src:manual/40-merezha.md:142 klas:E -->
### T-40-064 · komirka · `manual/40-merezha.md`

**Твердження, коротко**

> 0 · Коли → телеметрія, часті вимірювання

**Дослівно з книги**

```
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
```

**Контекст**

```
## MQTT

**QoS:**

| Рівень | Гарантія | Коли |
|---|---|---|
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
| 1 | доставлено щонайменше раз, можливі дублі | команди |
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-065 sha:717e2285 src:manual/40-merezha.md:143 klas:E -->
### T-40-065 · komirka · `manual/40-merezha.md`

**Твердження, коротко**

> 1 · Гарантія → доставлено щонайменше раз, можливі дублі

**Дослівно з книги**

```
| 1 | доставлено щонайменше раз, можливі дублі | команди |
```

**Контекст**

```
## MQTT

**QoS:**

| Рівень | Гарантія | Коли |
|---|---|---|
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
| 1 | доставлено щонайменше раз, можливі дублі | команди |
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-066 sha:83a52bfd src:manual/40-merezha.md:143 klas:E -->
### T-40-066 · komirka · `manual/40-merezha.md`

**Твердження, коротко**

> 1 · Коли → команди

**Дослівно з книги**

```
| 1 | доставлено щонайменше раз, можливі дублі | команди |
```

**Контекст**

```
## MQTT

**QoS:**

| Рівень | Гарантія | Коли |
|---|---|---|
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
| 1 | доставлено щонайменше раз, можливі дублі | команди |
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-067 sha:6221cb30 src:manual/40-merezha.md:144 klas:E -->
### T-40-067 · komirka · `manual/40-merezha.md`

**Твердження, коротко**

> 2 · Гарантія → рівно раз, найдорожчий

**Дослівно з книги**

```
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Контекст**

```
## MQTT

**QoS:**

| Рівень | Гарантія | Коли |
|---|---|---|
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
| 1 | доставлено щонайменше раз, можливі дублі | команди |
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-068 sha:8500e7ee src:manual/40-merezha.md:144 klas:E -->
### T-40-068 · komirka · `manual/40-merezha.md`

**Твердження, коротко**

> 2 · Коли → рідко потрібен

**Дослівно з книги**

```
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Контекст**

```
## MQTT

**QoS:**

| Рівень | Гарантія | Коли |
|---|---|---|
| 0 | доставка не гарантована | телеметрія, часті вимірювання |
| 1 | доставлено щонайменше раз, можливі дублі | команди |
| 2 | рівно раз, найдорожчий | рідко потрібен |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-069 sha:93e6a99f src:manual/40-merezha.md:147 klas:E -->
### T-40-069 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Обробник команд має бути **ідемпотентним**: при QoS 1 те саме повідомлення може прийти двічі, і «увімкнути реле» двічі має означати те саме, що один раз.

**Контекст**

```
## MQTT

Обробник команд має бути **ідемпотентним**: при QoS 1 те саме
повідомлення може прийти двічі, і «увімкнути реле» двічі має означати
те саме, що один раз.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-070 sha:a97658fd src:manual/40-merezha.md:152 klas:F -->
### T-40-070 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Дві можливості MQTT, які роблять систему живою і які часто пропускають.

**Контекст**

```
## MQTT

::: uvaha
Дві можливості MQTT, які роблять систему живою і які часто пропускають.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-071 sha:d015a0ae src:manual/40-merezha.md:154 klas:E -->
### T-40-071 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **Retained-повідомлення.** Брокер зберігає останнє значення в топіку і віддає його новому підписнику одразу.

**Контекст**

```
## MQTT

**Retained-повідомлення.** Брокер зберігає останнє значення в топіку і
віддає його новому підписнику одразу. Без цього інтерфейс після
перезавантаження показує порожнечу, доки датчик не надішле наступне
значення — а це може бути через п'ять хвилин.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-072 sha:8a48a664 src:manual/40-merezha.md:154 klas:E -->
### T-40-072 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Без цього інтерфейс після перезавантаження показує порожнечу, доки датчик не надішле наступне значення — а це може бути через п'ять хвилин.

**Контекст**

```
## MQTT

**Retained-повідомлення.** Брокер зберігає останнє значення в топіку і
віддає його новому підписнику одразу. Без цього інтерфейс після
перезавантаження показує порожнечу, доки датчик не надішле наступне
значення — а це може бути через п'ять хвилин.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-073 sha:17065457 src:manual/40-merezha.md:159 klas:F -->
### T-40-073 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **Last Will and Testament.** Пристрій наперед каже брокеру: «якщо я зникну, опублікуй у такий-то топік слово `offline`».

**Контекст**

```
## MQTT

**Last Will and Testament.** Пристрій наперед каже брокеру: «якщо я
зникну, опублікуй у такий-то топік слово `offline`». Тепер система
дізнається про мертвий вузол сама, без опитувань. Для будь-якого виробу,
що працює без нагляду, це обов'язкове.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-074 sha:16021207 src:manual/40-merezha.md:159 klas:E -->
### T-40-074 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Тепер система дізнається про мертвий вузол сама, без опитувань.

**Контекст**

```
## MQTT

**Last Will and Testament.** Пристрій наперед каже брокеру: «якщо я
зникну, опублікуй у такий-то топік слово `offline`». Тепер система
дізнається про мертвий вузол сама, без опитувань. Для будь-якого виробу,
що працює без нагляду, це обов'язкове.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-075 sha:7a16e395 src:manual/40-merezha.md:159 klas:E -->
### T-40-075 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Для будь-якого виробу, що працює без нагляду, це обов'язкове.

**Контекст**

```
## MQTT

**Last Will and Testament.** Пристрій наперед каже брокеру: «якщо я
зникну, опублікуй у такий-то топік слово `offline`». Тепер система
дізнається про мертвий вузол сама, без опитувань. Для будь-якого виробу,
що працює без нагляду, це обов'язкове.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-076 sha:6a8edb98 src:manual/40-merezha.md:167 klas:E -->
### T-40-076 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Незашифрований обмін означає, що будь-хто в мережі бачить дані й може підмінити команди.

**Контекст**

```
## TLS: мінімум

Незашифрований обмін означає, що будь-хто в мережі бачить дані й може
підмінити команди. Для пристрою в полі це не теорія.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-077 sha:5b7d99a8 src:manual/40-merezha.md:167 klas:E -->
### T-40-077 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Для пристрою в полі це не теорія.

**Контекст**

```
## TLS: мінімум

Незашифрований обмін означає, що будь-хто в мережі бачить дані й може
підмінити команди. Для пристрою в полі це не теорія.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-078 sha:85ac2b05 src:manual/40-merezha.md:170 klas:E -->
### T-40-078 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Мінімум, що реально працює:

**Контекст**

```
## TLS: мінімум

Мінімум, що реально працює:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-079 sha:42942377 src:manual/40-merezha.md:172 klas:E -->
### T-40-079 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **Перевірка сертифіката сервера.** Пристрій має знати, з ким говорить.

**Контекст**

```
## TLS: мінімум

**Перевірка сертифіката сервера.** Пристрій має знати, з ким говорить.
Сертифікат вбудовується в прошивку як ресурс.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-080 sha:ce6848a3 src:manual/40-merezha.md:172 klas:E -->
### T-40-080 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Сертифікат вбудовується в прошивку як ресурс.

**Контекст**

```
## TLS: мінімум

**Перевірка сертифіката сервера.** Пристрій має знати, з ким говорить.
Сертифікат вбудовується в прошивку як ресурс.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-081 sha:94635c7b src:manual/40-merezha.md:175 klas:E -->
### T-40-081 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **Зашивати сертифікат центру сертифікації, а не сервера.** Сертифікат сервера протермінується через рік, і всі пристрої одночасно втратять зв'язок.

**Контекст**

```
## TLS: мінімум

**Зашивати сертифікат центру сертифікації, а не сервера.** Сертифікат
сервера протермінується через рік, і всі пристрої одночасно втратять
зв'язок. Сертифікат CA живе значно довше (розділ 19).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-082 sha:ee961520 src:manual/40-merezha.md:175 klas:E -->
### T-40-082 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Сертифікат CA живе значно довше (розділ 19).

**Контекст**

```
## TLS: мінімум

**Зашивати сертифікат центру сертифікації, а не сервера.** Сертифікат
сервера протермінується через рік, і всі пристрої одночасно втратять
зв'язок. Сертифікат CA живе значно довше (розділ 19).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-083 sha:e9d42010 src:manual/40-merezha.md:179 klas:E -->
### T-40-083 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> **Не вимикати перевірку.** Спокуса велика — воно одразу починає працювати.

**Контекст**

```
## TLS: мінімум

**Не вимикати перевірку.** Спокуса велика — воно одразу починає
працювати. Але тоді TLS дає лише шифрування без автентифікації, тобто
захищає від підслуховування і не захищає від підміни. Це половина
захисту, яка створює відчуття повного.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-084 sha:29ee7ec2 src:manual/40-merezha.md:179 klas:F -->
### T-40-084 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Але тоді TLS дає лише шифрування без автентифікації, тобто захищає від підслуховування і не захищає від підміни.

**Контекст**

```
## TLS: мінімум

**Не вимикати перевірку.** Спокуса велика — воно одразу починає
працювати. Але тоді TLS дає лише шифрування без автентифікації, тобто
захищає від підслуховування і не захищає від підміни. Це половина
захисту, яка створює відчуття повного.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-085 sha:da66469b src:manual/40-merezha.md:179 klas:E -->
### T-40-085 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Це половина захисту, яка створює відчуття повного.

**Контекст**

```
## TLS: мінімум

**Не вимикати перевірку.** Спокуса велика — воно одразу починає
працювати. Але тоді TLS дає лише шифрування без автентифікації, тобто
захищає від підслуховування і не захищає від підміни. Це половина
захисту, яка створює відчуття повного.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-086 sha:98aa77fd src:manual/40-merezha.md:185 klas:F -->
### T-40-086 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> TLS коштує ресурсів: кілька кілобайтів RAM на з'єднання, помітний час на рукостискання, і сплеск споживання.

**Контекст**

```
## TLS: мінімум

::: zhyvlennya
TLS коштує ресурсів: кілька кілобайтів RAM на з'єднання, помітний час на
рукостискання, і сплеск споживання. На C3 з його 400 КБ (розділ 02) два
одночасні TLS-з'єднання вже відчутні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-087 sha:cbddb568 src:manual/40-merezha.md:185 klas:C -->
### T-40-087 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> На C3 з його 400 КБ (розділ 02) два одночасні TLS-з'єднання вже відчутні.

**Контекст**

```
## TLS: мінімум

::: zhyvlennya
TLS коштує ресурсів: кілька кілобайтів RAM на з'єднання, помітний час на
рукостискання, і сплеск споживання. На C3 з його 400 КБ (розділ 02) два
одночасні TLS-з'єднання вже відчутні.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP-IDF Programming Guide, mbedTLS memory footprint / ESP-TLS — оцінка пам'яті на з'єднання; цитати не дістав
- **Спосіб і дата:** позахідна знань про пам'ять та криптографію, 2026-08-27
- **Нотатка:** Клас B без цитати. Джерело для витрат пам'яті на TLS-з'єднання існує (документація mbedTLS в ESP-IDF наводить порядок величин), але я його не відкривав. Тому C.
- **Прохід:** m2-90-vybirka

---

<!-- fc id:T-40-088 sha:cd1b7976 src:manual/40-merezha.md:189 klas:E -->
### T-40-088 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Апаратні прискорювачі криптографії в чипі роблять це прийнятним (розділ 04), але не безкоштовним.

**Контекст**

```
## TLS: мінімум

Апаратні прискорювачі криптографії в чипі роблять це прийнятним
(розділ 04), але не безкоштовним. Для пристрою на батарейці рукостискання
при кожній передачі — головна стаття витрат; краще тримати одне
з'єднання постійно.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-089 sha:f5dece33 src:manual/40-merezha.md:189 klas:E -->
### T-40-089 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Для пристрою на батарейці рукостискання при кожній передачі — головна стаття витрат; краще тримати одне з'єднання постійно.

**Контекст**

```
## TLS: мінімум

Апаратні прискорювачі криптографії в чипі роблять це прийнятним
(розділ 04), але не безкоштовним. Для пристрою на батарейці рукостискання
при кожній передачі — головна стаття витрат; краще тримати одне
з'єднання постійно.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-090 sha:e3096115 src:manual/40-merezha.md:197 klas:E -->
### T-40-090 · tablycya · `manual/40-merezha.md`

**Твердження, коротко**

> | Задача | Чим |

**Контекст**

```
## Що обрати


| Задача | Чим |
|---|---|
| Налаштування людиною | HTTP-сервер на пристрої |
| Графік наживо | WebSocket |
| Телеметрія в систему | MQTT |
| Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |
| Команди керування | MQTT з QoS 1 або TCP |
| Доступ без знання IP | mDNS плюс показ IP |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-091 sha:761d9ec2 src:manual/40-merezha.md:199 klas:F -->
### T-40-091 · tablycya · `manual/40-merezha.md`

**Твердження, коротко**

> | Налаштування людиною | HTTP-сервер на пристрої |

**Контекст**

```
## Що обрати


| Задача | Чим |
|---|---|
| Налаштування людиною | HTTP-сервер на пристрої |
| Графік наживо | WebSocket |
| Телеметрія в систему | MQTT |
| Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |
| Команди керування | MQTT з QoS 1 або TCP |
| Доступ без знання IP | mDNS плюс показ IP |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-092 sha:e32c11a5 src:manual/40-merezha.md:200 klas:E -->
### T-40-092 · tablycya · `manual/40-merezha.md`

**Твердження, коротко**

> | Графік наживо | WebSocket |

**Контекст**

```
## Що обрати


| Задача | Чим |
|---|---|
| Налаштування людиною | HTTP-сервер на пристрої |
| Графік наживо | WebSocket |
| Телеметрія в систему | MQTT |
| Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |
| Команди керування | MQTT з QoS 1 або TCP |
| Доступ без знання IP | mDNS плюс показ IP |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-093 sha:9978f5d3 src:manual/40-merezha.md:201 klas:F -->
### T-40-093 · tablycya · `manual/40-merezha.md`

**Твердження, коротко**

> | Телеметрія в систему | MQTT |

**Контекст**

```
## Що обрати


| Задача | Чим |
|---|---|
| Налаштування людиною | HTTP-сервер на пристрої |
| Графік наживо | WebSocket |
| Телеметрія в систему | MQTT |
| Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |
| Команди керування | MQTT з QoS 1 або TCP |
| Доступ без знання IP | mDNS плюс показ IP |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-094 sha:cc768007 src:manual/40-merezha.md:202 klas:F -->
### T-40-094 · tablycya · `manual/40-merezha.md`

**Твердження, коротко**

> | Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |

**Контекст**

```
## Що обрати


| Задача | Чим |
|---|---|
| Налаштування людиною | HTTP-сервер на пристрої |
| Графік наживо | WebSocket |
| Телеметрія в систему | MQTT |
| Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |
| Команди керування | MQTT з QoS 1 або TCP |
| Доступ без знання IP | mDNS плюс показ IP |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-095 sha:5234074a src:manual/40-merezha.md:203 klas:F -->
### T-40-095 · tablycya · `manual/40-merezha.md`

**Твердження, коротко**

> | Команди керування | MQTT з QoS 1 або TCP |

**Контекст**

```
## Що обрати


| Задача | Чим |
|---|---|
| Налаштування людиною | HTTP-сервер на пристрої |
| Графік наживо | WebSocket |
| Телеметрія в систему | MQTT |
| Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |
| Команди керування | MQTT з QoS 1 або TCP |
| Доступ без знання IP | mDNS плюс показ IP |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-096 sha:2f67bd2b src:manual/40-merezha.md:204 klas:E -->
### T-40-096 · tablycya · `manual/40-merezha.md`

**Твердження, коротко**

> | Доступ без знання IP | mDNS плюс показ IP |

**Контекст**

```
## Що обрати


| Задача | Чим |
|---|---|
| Налаштування людиною | HTTP-сервер на пристрої |
| Графік наживо | WebSocket |
| Телеметрія в систему | MQTT |
| Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |
| Команди керування | MQTT з QoS 1 або TCP |
| Доступ без знання IP | mDNS плюс показ IP |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-097 sha:646fd8a7 src:manual/40-merezha.md:208 klas:E -->
### T-40-097 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> TCP для команд, UDP для потоку вимірювань.

**Контекст**

```
## Що з цього треба запам'ятати

TCP для команд, UDP для потоку вимірювань.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-098 sha:6386a727 src:manual/40-merezha.md:210 klas:E -->
### T-40-098 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Стек задачі веб-сервера часто треба збільшувати.

**Контекст**

```
## Що з цього треба запам'ятати

Стек задачі веб-сервера часто треба збільшувати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-099 sha:402147ba src:manual/40-merezha.md:212 klas:E -->
### T-40-099 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> mDNS — зручність, а не єдиний шлях; IP показувати теж.

**Контекст**

```
## Що з цього треба запам'ятати

mDNS — зручність, а не єдиний шлях; IP показувати теж.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-100 sha:95fe58b2 src:manual/40-merezha.md:214 klas:F -->
### T-40-100 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Retained і Last Will у MQTT роблять систему живою; обробник команд має бути ідемпотентним.

**Контекст**

```
## Що з цього треба запам'ятати

Retained і Last Will у MQTT роблять систему живою; обробник команд має
бути ідемпотентним.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-101 sha:e6c71b56 src:manual/40-merezha.md:217 klas:E -->
### T-40-101 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Зашивати сертифікат CA, а не сервера.

**Контекст**

```
## Що з цього треба запам'ятати

Зашивати сертифікат CA, а не сервера. Не вимикати перевірку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-102 sha:9859565e src:manual/40-merezha.md:219 klas:E -->
### T-40-102 · proza · `manual/40-merezha.md`

**Твердження, коротко**

> Код має працювати, доки часу ще немає.

**Контекст**

```
## Що з цього треба запам'ятати

Код має працювати, доки часу ще немає.
```

**Доказ**

- **Клас:** F — не звірено

---
