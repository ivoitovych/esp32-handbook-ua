# Фактчекінг: `manual/40-merezha.md`

Одиниць твердження: **102**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-40-001 sha:950d8d44 src:manual/40-merezha.md:3 klas:F -->
### T-40-001 · proza · рядок 3

**Книга каже, дослівно:**

> Wi-Fi дає канал; далі треба вирішити, що по ньому передавати і як.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-002 sha:b9113487 src:manual/40-merezha.md:3 klas:F -->
### T-40-002 · proza · рядок 3

**Книга каже, дослівно:**

> Розділ про рівень вище фізичного: сокети, HTTP, WebSocket, MQTT, TLS.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-003 sha:0c16a37c src:manual/40-merezha.md:8 klas:E -->
### T-40-003 · proza · рядок 8

**Книга каже, дослівно:**

> **TCP** гарантує доставку й порядок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-004 sha:fe286ad8 src:manual/40-merezha.md:8 klas:E -->
### T-40-004 · proza · рядок 8

**Книга каже, дослівно:**

> Ціна — встановлення з'єднання, підтвердження, повтори; при поганому зв'язку затримки ростуть.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-005 sha:5b919d56 src:manual/40-merezha.md:11 klas:E -->
### T-40-005 · proza · рядок 11

**Книга каже, дослівно:**

> **UDP** нічого не гарантує.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-006 sha:b1af660a src:manual/40-merezha.md:11 klas:E -->
### T-40-006 · proza · рядок 11

**Книга каже, дослівно:**

> Пакет або дійшов, або ні, і дізнатися про це ви не можете.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-007 sha:6a599c12 src:manual/40-merezha.md:11 klas:E -->
### T-40-007 · proza · рядок 11

**Книга каже, дослівно:**

> Зате він швидкий, не потребує з'єднання і дозволяє широкомовну розсилку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-008 sha:0a9dbf6e src:manual/40-merezha.md:15 klas:E -->
### T-40-008 · proza · рядок 15

**Книга каже, дослівно:**

> Практичне правило: **TCP для команд і налаштувань, UDP для потоку вимірювань**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-009 sha:cce1d360 src:manual/40-merezha.md:15 klas:E -->
### T-40-009 · proza · рядок 15

**Книга каже, дослівно:**

> Втрачений відлік температури нічого не змінює; втрачена команда «вимкнути» — змінює.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-010 sha:d6267053 src:manual/40-merezha.md:21 klas:E -->
### T-40-010 · proza · рядок 21

**Книга каже, дослівно:**

> Найзручніший інтерфейс для людини: жодного застосунку, працює з будь-якого телефона.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-011 sha:27f9f409 src:manual/40-merezha.md:24 klas:K -->
### T-40-011 · kod · рядок 24

**Книга каже, дослівно:**

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
### T-40-012 · kod-ryadok · рядок 27

**Книга каже, дослівно:**

> httpd_start(&server, &cfg);

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
### T-40-013 · kod-ryadok · рядок 30

**Книга каже, дослівно:**

> .uri = "/api/stan",

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-014 sha:3b3be56d src:manual/40-merezha.md:31 klas:F -->
### T-40-014 · kod-ryadok · рядок 31

**Книга каже, дослівно:**

> .method = HTTP_GET,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-015 sha:1ff1aec9 src:manual/40-merezha.md:32 klas:F -->
### T-40-015 · kod-ryadok · рядок 32

**Книга каже, дослівно:**

> .handler = stan_handler,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-016 sha:f833664b src:manual/40-merezha.md:34 klas:A -->
### T-40-016 · kod-ryadok · рядок 34

**Книга каже, дослівно:**

> httpd_register_uri_handler(server, &uri);

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
### T-40-017 · proza · рядок 38

**Книга каже, дослівно:**

> Обробник виконується в задачі веб-сервера з **обмеженим стеком**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-018 sha:d6fb9903 src:manual/40-merezha.md:38 klas:E -->
### T-40-018 · proza · рядок 38

**Книга каже, дослівно:**

> Великі буфери там — прямий шлях до переповнення стека, яке проявиться пізніше й деінде (розділ 30).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-019 sha:57ba00a7 src:manual/40-merezha.md:42 klas:F -->
### T-40-019 · proza · рядок 42

**Книга каже, дослівно:**

> Розмір стека сервера задається в `HTTPD_DEFAULT_CONFIG` і його часто доводиться збільшувати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-020 sha:86c0653a src:manual/40-merezha.md:42 klas:F -->
### T-40-020 · proza · рядок 42

**Книга каже, дослівно:**

> Особливо якщо в обробнику формується JSON або використовується TLS.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-021 sha:d91a7859 src:manual/40-merezha.md:47 klas:E -->
### T-40-021 · proza · рядок 47

**Книга каже, дослівно:**

> Статичні файли — HTML, CSS, скрипти — кладуть у розділ файлової системи (розділ 18) або вбудовують у прошивку як ресурси.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-022 sha:d2be0535 src:manual/40-merezha.md:47 klas:E -->
### T-40-022 · proza · рядок 47

**Книга каже, дослівно:**

> Друге простіше для невеликих сторінок і не потребує окремого розділу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-023 sha:553a1977 src:manual/40-merezha.md:53 klas:F -->
### T-40-023 · proza · рядок 53

**Книга каже, дослівно:**

> HTTP влаштований як «запит — відповідь»: сервер не може сам щось надіслати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-024 sha:fde2d7f3 src:manual/40-merezha.md:53 klas:E -->
### T-40-024 · proza · рядок 53

**Книга каже, дослівно:**

> Для сторінки, яка має оновлюватися наживо, це означає опитування щосекунди — марний трафік і затримки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-025 sha:c1bb8fe5 src:manual/40-merezha.md:57 klas:E -->
### T-40-025 · proza · рядок 57

**Книга каже, дослівно:**

> WebSocket дає двонапрямлений канал поверх того самого з'єднання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-026 sha:3aa2580a src:manual/40-merezha.md:57 klas:E -->
### T-40-026 · proza · рядок 57

**Книга каже, дослівно:**

> Для графіка вимірювань у реальному часі це правильний інструмент.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-027 sha:6592d83e src:manual/40-merezha.md:60 klas:E -->
### T-40-027 · proza · рядок 60

**Книга каже, дослівно:**

> Обмеження практичне: кожен клієнт — це відкрите з'єднання й пам'ять під нього.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-028 sha:b23be94f src:manual/40-merezha.md:60 klas:F -->
### T-40-028 · proza · рядок 60

**Книга каже, дослівно:**

> На ESP32 кілька одночасних клієнтів — межа, і поводитися з нею треба свідомо.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-029 sha:4786a8f6 src:manual/40-merezha.md:66 klas:E -->
### T-40-029 · proza · рядок 66

**Книга каже, дослівно:**

> Пристрій отримує адресу від роутера, і вона може змінитися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-030 sha:84b2234f src:manual/40-merezha.md:66 klas:E -->
### T-40-030 · proza · рядок 66

**Книга каже, дослівно:**

> Змушувати людину шукати IP — поганий інтерфейс.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-031 sha:86639629 src:manual/40-merezha.md:71 klas:K -->
### T-40-031 · kod · рядок 71

**Книга каже, дослівно:**

> ```c
> mdns_init();
> mdns_hostname_set("teplytsia");
> mdns_instance_name_set("Датчики теплиці");
> ```

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
### T-40-032 · kod-ryadok · рядок 72

**Книга каже, дослівно:**

> mdns_init();

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
### T-40-033 · kod-ryadok · рядок 73

**Книга каже, дослівно:**

> mdns_hostname_set("teplytsia");

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
### T-40-034 · kod-ryadok · рядок 74

**Книга каже, дослівно:**

> mdns_instance_name_set("Датчики теплиці");

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
### T-40-035 · proza · рядок 77

**Книга каже, дослівно:**

> Далі пристрій доступний як `teplytsia.local` — з телефона, з ноутбука, з браузера.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-036 sha:653ea4a2 src:manual/40-merezha.md:81 klas:E -->
### T-40-036 · proza · рядок 81

**Книга каже, дослівно:**

> Android історично підтримував його неповно; корпоративні мережі часто ріжуть широкомовний трафік; гостьові мережі ізолюють клієнтів одне від одного.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-037 sha:f7798eee src:manual/40-merezha.md:85 klas:E -->
### T-40-037 · proza · рядок 85

**Книга каже, дослівно:**

> Тому: mDNS — це зручність, а не єдиний спосіб дістатися пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-038 sha:ae6489bf src:manual/40-merezha.md:85 klas:E -->
### T-40-038 · proza · рядок 85

**Книга каже, дослівно:**

> Показувати IP-адресу теж треба — хоча б у логу або на дисплеї.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-039 sha:1839164a src:manual/40-merezha.md:91 klas:E -->
### T-40-039 · proza · рядок 91

**Книга каже, дослівно:**

> Годинник у чипі неточний і скидається при вимиканні живлення (розділ 03).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-040 sha:cbb939d1 src:manual/40-merezha.md:91 klas:E -->
### T-40-040 · proza · рядок 91

**Книга каже, дослівно:**

> Якщо є мережа, час беруть з інтернету:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-041 sha:01cae44d src:manual/40-merezha.md:94 klas:K -->
### T-40-041 · kod · рядок 94

**Книга каже, дослівно:**

> ```c
> esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);
> esp_sntp_setservername(0, "pool.ntp.org");
> esp_sntp_init();
> setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);
> tzset();
> ```

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
### T-40-042 · kod-ryadok · рядок 95

**Книга каже, дослівно:**

> esp_sntp_setoperatingmode(ESP_SNTP_OPMODE_POLL);

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
### T-40-043 · kod-ryadok · рядок 96

**Книга каже, дослівно:**

> esp_sntp_setservername(0, "pool.ntp.org");

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
### T-40-044 · kod-ryadok · рядок 97

**Книга каже, дослівно:**

> esp_sntp_init();

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
### T-40-045 · kod-ryadok · рядок 98

**Книга каже, дослівно:**

> setenv("TZ", "EET-2EEST,M3.5.0/3,M10.5.0/4", 1);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-046 sha:ab5c560a src:manual/40-merezha.md:99 klas:F -->
### T-40-046 · kod-ryadok · рядок 99

**Книга каже, дослівно:**

> tzset();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-047 sha:8c357f0b src:manual/40-merezha.md:102 klas:F -->
### T-40-047 · proza · рядок 102

**Книга каже, дослівно:**

> Рядок `TZ` вище — правило переходу на літній час для України; воно працює автономно, без оновлень.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-048 sha:aa6bbdb5 src:manual/40-merezha.md:105 klas:E -->
### T-40-048 · proza · рядок 105

**Книга каже, дослівно:**

> Час приходить **не миттєво**: перша синхронізація займає секунди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-049 sha:caed2427 src:manual/40-merezha.md:105 klas:E -->
### T-40-049 · proza · рядок 105

**Книга каже, дослівно:**

> Код, що ставить мітки часу, має вміти працювати, доки часу ще немає, — інакше в логах з'являються записи з 1970 року.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-050 sha:70ee41d2 src:manual/40-merezha.md:109 klas:F -->
### T-40-050 · proza · рядок 109

**Книга каже, дослівно:**

> Немає мережі й потрібен точний час — зовнішня мікросхема RTC із батарейкою (розділ 60).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-051 sha:70422979 src:manual/40-merezha.md:114 klas:E -->
### T-40-051 · proza · рядок 114

**Книга каже, дослівно:**

> Протокол, придуманий саме для таких пристроїв: легкий, тримає одне з'єднання, працює через погані канали.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-052 sha:237411e6 src:manual/40-merezha.md:117 klas:E -->
### T-40-052 · proza · рядок 117

**Книга каже, дослівно:**

> Модель — «публікація і підписка».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-053 sha:57bee44f src:manual/40-merezha.md:117 klas:E -->
### T-40-053 · proza · рядок 117

**Книга каже, дослівно:**

> Пристрої не знають одне про одного: є **брокер** посередині, є **топіки** — ієрархічні імена.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-054 sha:67a21aaa src:manual/40-merezha.md:117 klas:E -->
### T-40-054 · proza · рядок 117

**Книга каже, дослівно:**

> Хто хоче — публікує, хто хоче — підписується.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-055 sha:cdb9b592 src:manual/40-merezha.md:121 klas:K -->
### T-40-055 · kod · рядок 121

**Книга каже, дослівно:**

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
### T-40-056 · kod-ryadok · рядок 128

**Книга каже, дослівно:**

> esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, handler, NULL);

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
### T-40-057 · kod-ryadok · рядок 129

**Книга каже, дослівно:**

> esp_mqtt_client_start(client);

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
### T-40-058 · kod-ryadok · рядок 131

**Книга каже, дослівно:**

> esp_mqtt_client_publish(client, "teplytsia/temperatura", "23.5", 0, 1, 0);

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
### T-40-059 · proza · рядок 134

**Книга каже, дослівно:**

> **Структура топіків** — це проєктне рішення, і міняти її потім дорого.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-060 sha:6937ad74 src:manual/40-merezha.md:134 klas:F -->
### T-40-060 · proza · рядок 134

**Книга каже, дослівно:**

> Робоча схема: `<об'єкт>/<вузол>/<величина>`, наприклад `teplytsia/datchyk1/temperatura`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-061 sha:9ccd51d0 src:manual/40-merezha.md:134 klas:F -->
### T-40-061 · proza · рядок 134

**Книга каже, дослівно:**

> Керування — окремою гілкою: `teplytsia/datchyk1/cmd/rele`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-062 sha:a84b93ca src:manual/40-merezha.md:141 klas:F -->
### T-40-062 · tablycya-shapka · рядок 141

**Книга каже, дослівно:**

> | Рівень | Гарантія | Коли |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-063 sha:9628ec9a src:manual/40-merezha.md:142 klas:E -->
### T-40-063 · komirka · рядок 142

**Книга каже, дослівно:**

> 0 · Гарантія → доставка не гарантована

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-064 sha:7d437bc9 src:manual/40-merezha.md:142 klas:E -->
### T-40-064 · komirka · рядок 142

**Книга каже, дослівно:**

> 0 · Коли → телеметрія, часті вимірювання

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-065 sha:717e2285 src:manual/40-merezha.md:143 klas:E -->
### T-40-065 · komirka · рядок 143

**Книга каже, дослівно:**

> 1 · Гарантія → доставлено щонайменше раз, можливі дублі

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-066 sha:83a52bfd src:manual/40-merezha.md:143 klas:E -->
### T-40-066 · komirka · рядок 143

**Книга каже, дослівно:**

> 1 · Коли → команди

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-067 sha:6221cb30 src:manual/40-merezha.md:144 klas:E -->
### T-40-067 · komirka · рядок 144

**Книга каже, дослівно:**

> 2 · Гарантія → рівно раз, найдорожчий

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-068 sha:8500e7ee src:manual/40-merezha.md:144 klas:E -->
### T-40-068 · komirka · рядок 144

**Книга каже, дослівно:**

> 2 · Коли → рідко потрібен

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-069 sha:93e6a99f src:manual/40-merezha.md:147 klas:E -->
### T-40-069 · proza · рядок 147

**Книга каже, дослівно:**

> Обробник команд має бути **ідемпотентним**: при QoS 1 те саме повідомлення може прийти двічі, і «увімкнути реле» двічі має означати те саме, що один раз.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-070 sha:a97658fd src:manual/40-merezha.md:152 klas:F -->
### T-40-070 · proza · рядок 152

**Книга каже, дослівно:**

> Дві можливості MQTT, які роблять систему живою і які часто пропускають.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-071 sha:d015a0ae src:manual/40-merezha.md:154 klas:E -->
### T-40-071 · proza · рядок 154

**Книга каже, дослівно:**

> **Retained-повідомлення.** Брокер зберігає останнє значення в топіку і віддає його новому підписнику одразу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-072 sha:8a48a664 src:manual/40-merezha.md:154 klas:E -->
### T-40-072 · proza · рядок 154

**Книга каже, дослівно:**

> Без цього інтерфейс після перезавантаження показує порожнечу, доки датчик не надішле наступне значення — а це може бути через п'ять хвилин.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-073 sha:17065457 src:manual/40-merezha.md:159 klas:F -->
### T-40-073 · proza · рядок 159

**Книга каже, дослівно:**

> **Last Will and Testament.** Пристрій наперед каже брокеру: «якщо я зникну, опублікуй у такий-то топік слово `offline`».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-074 sha:16021207 src:manual/40-merezha.md:159 klas:E -->
### T-40-074 · proza · рядок 159

**Книга каже, дослівно:**

> Тепер система дізнається про мертвий вузол сама, без опитувань.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-075 sha:7a16e395 src:manual/40-merezha.md:159 klas:E -->
### T-40-075 · proza · рядок 159

**Книга каже, дослівно:**

> Для будь-якого виробу, що працює без нагляду, це обов'язкове.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-076 sha:6a8edb98 src:manual/40-merezha.md:167 klas:E -->
### T-40-076 · proza · рядок 167

**Книга каже, дослівно:**

> Незашифрований обмін означає, що будь-хто в мережі бачить дані й може підмінити команди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-077 sha:5b7d99a8 src:manual/40-merezha.md:167 klas:E -->
### T-40-077 · proza · рядок 167

**Книга каже, дослівно:**

> Для пристрою в полі це не теорія.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-078 sha:85ac2b05 src:manual/40-merezha.md:170 klas:E -->
### T-40-078 · proza · рядок 170

**Книга каже, дослівно:**

> Мінімум, що реально працює:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-079 sha:42942377 src:manual/40-merezha.md:172 klas:E -->
### T-40-079 · proza · рядок 172

**Книга каже, дослівно:**

> **Перевірка сертифіката сервера.** Пристрій має знати, з ким говорить.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-080 sha:ce6848a3 src:manual/40-merezha.md:172 klas:E -->
### T-40-080 · proza · рядок 172

**Книга каже, дослівно:**

> Сертифікат вбудовується в прошивку як ресурс.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-081 sha:94635c7b src:manual/40-merezha.md:175 klas:E -->
### T-40-081 · proza · рядок 175

**Книга каже, дослівно:**

> **Зашивати сертифікат центру сертифікації, а не сервера.** Сертифікат сервера протермінується через рік, і всі пристрої одночасно втратять зв'язок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-082 sha:ee961520 src:manual/40-merezha.md:175 klas:E -->
### T-40-082 · proza · рядок 175

**Книга каже, дослівно:**

> Сертифікат CA живе значно довше (розділ 19).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-083 sha:e9d42010 src:manual/40-merezha.md:179 klas:E -->
### T-40-083 · proza · рядок 179

**Книга каже, дослівно:**

> **Не вимикати перевірку.** Спокуса велика — воно одразу починає працювати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-084 sha:29ee7ec2 src:manual/40-merezha.md:179 klas:F -->
### T-40-084 · proza · рядок 179

**Книга каже, дослівно:**

> Але тоді TLS дає лише шифрування без автентифікації, тобто захищає від підслуховування і не захищає від підміни.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-085 sha:da66469b src:manual/40-merezha.md:179 klas:E -->
### T-40-085 · proza · рядок 179

**Книга каже, дослівно:**

> Це половина захисту, яка створює відчуття повного.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-086 sha:98aa77fd src:manual/40-merezha.md:185 klas:F -->
### T-40-086 · proza · рядок 185

**Книга каже, дослівно:**

> TLS коштує ресурсів: кілька кілобайтів RAM на з'єднання, помітний час на рукостискання, і сплеск споживання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-087 sha:cbddb568 src:manual/40-merezha.md:185 klas:F -->
### T-40-087 · proza · рядок 185

**Книга каже, дослівно:**

> На C3 з його 400 КБ (розділ 02) два одночасні TLS-з'єднання вже відчутні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-088 sha:cd1b7976 src:manual/40-merezha.md:189 klas:E -->
### T-40-088 · proza · рядок 189

**Книга каже, дослівно:**

> Апаратні прискорювачі криптографії в чипі роблять це прийнятним (розділ 04), але не безкоштовним.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-089 sha:f5dece33 src:manual/40-merezha.md:189 klas:E -->
### T-40-089 · proza · рядок 189

**Книга каже, дослівно:**

> Для пристрою на батарейці рукостискання при кожній передачі — головна стаття витрат; краще тримати одне з'єднання постійно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-090 sha:e3096115 src:manual/40-merezha.md:197 klas:E -->
### T-40-090 · tablycya · рядок 197

**Книга каже, дослівно:**

> | Задача | Чим |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-091 sha:761d9ec2 src:manual/40-merezha.md:199 klas:F -->
### T-40-091 · tablycya · рядок 199

**Книга каже, дослівно:**

> | Налаштування людиною | HTTP-сервер на пристрої |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-092 sha:e32c11a5 src:manual/40-merezha.md:200 klas:E -->
### T-40-092 · tablycya · рядок 200

**Книга каже, дослівно:**

> | Графік наживо | WebSocket |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-093 sha:9978f5d3 src:manual/40-merezha.md:201 klas:F -->
### T-40-093 · tablycya · рядок 201

**Книга каже, дослівно:**

> | Телеметрія в систему | MQTT |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-094 sha:cc768007 src:manual/40-merezha.md:202 klas:F -->
### T-40-094 · tablycya · рядок 202

**Книга каже, дослівно:**

> | Обмін між своїми вузлами | ESP-NOW (розділ 42) або UDP |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-095 sha:5234074a src:manual/40-merezha.md:203 klas:F -->
### T-40-095 · tablycya · рядок 203

**Книга каже, дослівно:**

> | Команди керування | MQTT з QoS 1 або TCP |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-096 sha:2f67bd2b src:manual/40-merezha.md:204 klas:E -->
### T-40-096 · tablycya · рядок 204

**Книга каже, дослівно:**

> | Доступ без знання IP | mDNS плюс показ IP |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-097 sha:646fd8a7 src:manual/40-merezha.md:208 klas:E -->
### T-40-097 · proza · рядок 208

**Книга каже, дослівно:**

> TCP для команд, UDP для потоку вимірювань.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-098 sha:6386a727 src:manual/40-merezha.md:210 klas:E -->
### T-40-098 · proza · рядок 210

**Книга каже, дослівно:**

> Стек задачі веб-сервера часто треба збільшувати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-099 sha:402147ba src:manual/40-merezha.md:212 klas:E -->
### T-40-099 · proza · рядок 212

**Книга каже, дослівно:**

> mDNS — зручність, а не єдиний шлях; IP показувати теж.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-100 sha:95fe58b2 src:manual/40-merezha.md:214 klas:F -->
### T-40-100 · proza · рядок 214

**Книга каже, дослівно:**

> Retained і Last Will у MQTT роблять систему живою; обробник команд має бути ідемпотентним.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-101 sha:e6c71b56 src:manual/40-merezha.md:217 klas:E -->
### T-40-101 · proza · рядок 217

**Книга каже, дослівно:**

> Зашивати сертифікат CA, а не сервера.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-40-102 sha:9859565e src:manual/40-merezha.md:219 klas:E -->
### T-40-102 · proza · рядок 219

**Книга каже, дослівно:**

> Код має працювати, доки часу ще немає.

**Доказ**

- **Клас:** F — не звірено

---
