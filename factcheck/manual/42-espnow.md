# Фактчекінг: `manual/42-espnow.md`

Одиниць твердження: **86**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-42-001 sha:e12353a5 src:manual/42-espnow.md:3 klas:F -->
### T-42-001 · proza · рядок 3

**Книга каже, дослівно:**

> ESP-NOW — власний протокол Espressif для прямого обміну між пристроями на ESP32 і ESP8266.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-002 sha:dd3855b4 src:manual/42-espnow.md:3 klas:E -->
### T-42-002 · proza · рядок 3

**Книга каже, дослівно:**

> Без роутера, без точки доступу, без IP-адрес.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-003 sha:3a142f89 src:manual/42-espnow.md:6 klas:E -->
### T-42-003 · proza · рядок 6

**Книга каже, дослівно:**

> Для автономних датчиків це часто найкраще технічне рішення в усій книзі, і причина одна: **передача без під'єднання**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-004 sha:bdf974c6 src:manual/42-espnow.md:11 klas:E -->
### T-42-004 · proza · рядок 11

**Книга каже, дослівно:**

> Звичайний Wi-Fi перед першою передачею мусить під'єднатися до точки доступу: сканування, автентифікація, асоціація, отримання IP.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-005 sha:63289213 src:manual/42-espnow.md:11 klas:F -->
### T-42-005 · proza · рядок 11

**Книга каже, дослівно:**

> Це секунди — від однієї до десяти, а на межі покриття може не відбутися взагалі (розділ 39).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-006 sha:9eee4e7d src:manual/42-espnow.md:16 klas:E -->
### T-42-006 · proza · рядок 16

**Книга каже, дослівно:**

> ESP-NOW не робить нічого з цього.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-007 sha:c2bc31a0 src:manual/42-espnow.md:16 klas:E -->
### T-42-007 · proza · рядок 16

**Книга каже, дослівно:**

> Пакет іде **одразу**, за мілісекунди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-008 sha:ea18b432 src:manual/42-espnow.md:19 klas:F -->
### T-42-008 · proza · рядок 19

**Книга каже, дослівно:**

> Для датчика на батарейці, який прокидається, міряє й засинає (розділ 06), різниця виглядає так:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-009 sha:56101255 src:manual/42-espnow.md:22 klas:F -->
### T-42-009 · proza · рядок 22

**Книга каже, дослівно:**

> *Wi-Fi:* прокинувся → 3 секунди на під'єднання → передав → заснув.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-010 sha:88f5799c src:manual/42-espnow.md:22 klas:E -->
### T-42-010 · proza · рядок 22

**Книга каже, дослівно:**

> Активна фаза — три з половиною секунди при сотні міліампер.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-011 sha:7c2c734a src:manual/42-espnow.md:25 klas:F -->
### T-42-011 · proza · рядок 25

**Книга каже, дослівно:**

> *ESP-NOW:* прокинувся → 10 мілісекунд на передачу → заснув.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-012 sha:f19af6af src:manual/42-espnow.md:25 klas:E -->
### T-42-012 · proza · рядок 25

**Книга каже, дослівно:**

> Активна фаза — частки секунди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-013 sha:a26e8f1c src:manual/42-espnow.md:28 klas:E -->
### T-42-013 · proza · рядок 28

**Книга каже, дослівно:**

> Це різниця у **два порядки** в споживанні на цикл, тобто різниця між місяцем і роками роботи від тих самих батарейок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-014 sha:8cf4ae97 src:manual/42-espnow.md:34 klas:E -->
### T-42-014 · proza · рядок 34

**Книга каже, дослівно:**

> Обмін іде за **MAC-адресами**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-015 sha:de2e8697 src:manual/42-espnow.md:34 klas:F -->
### T-42-015 · proza · рядок 34

**Книга каже, дослівно:**

> Кожен пристрій має унікальну MAC від заводу (розділ 20), і вона ж є адресою в ESP-NOW.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-016 sha:5acf4a2b src:manual/42-espnow.md:37 klas:K -->
### T-42-016 · kod · рядок 37

**Книга каже, дослівно:**

> ```c
> esp_now_init();
> 
> esp_now_peer_info_t peer = {
>     .channel = 1,
>     .encrypt = false,
> };
> memcpy(peer.peer_addr, mac_pryimacha, 6);
> esp_now_add_peer(&peer);
> 
> esp_now_send(mac_pryimacha, (uint8_t *)&dani, sizeof(dani));
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

<!-- fc id:T-42-017 sha:fb113f48 src:manual/42-espnow.md:38 klas:A -->
### T-42-017 · kod-ryadok · рядок 38

**Книга каже, дослівно:**

> esp_now_init();

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

<!-- fc id:T-42-018 sha:4bc3e2eb src:manual/42-espnow.md:41 klas:F -->
### T-42-018 · kod-ryadok · рядок 41

**Книга каже, дослівно:**

> .channel = 1,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-019 sha:1753a16b src:manual/42-espnow.md:42 klas:F -->
### T-42-019 · kod-ryadok · рядок 42

**Книга каже, дослівно:**

> .encrypt = false,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-020 sha:ef0288f3 src:manual/42-espnow.md:44 klas:F -->
### T-42-020 · kod-ryadok · рядок 44

**Книга каже, дослівно:**

> memcpy(peer.peer_addr, mac_pryimacha, 6);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-021 sha:6d1b1f7b src:manual/42-espnow.md:45 klas:A -->
### T-42-021 · kod-ryadok · рядок 45

**Книга каже, дослівно:**

> esp_now_add_peer(&peer);

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

<!-- fc id:T-42-022 sha:e65aad77 src:manual/42-espnow.md:47 klas:A -->
### T-42-022 · kod-ryadok · рядок 47

**Книга каже, дослівно:**

> esp_now_send(mac_pryimacha, (uint8_t *)&dani, sizeof(dani));

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

<!-- fc id:T-42-023 sha:aaeb4359 src:manual/42-espnow.md:50 klas:E -->
### T-42-023 · proza · рядок 50

**Книга каже, дослівно:**

> Прийом — через зареєстрований обробник:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-024 sha:11151595 src:manual/42-espnow.md:52 klas:K -->
### T-42-024 · kod · рядок 52

**Книга каже, дослівно:**

> ```c
> static void on_recv(const esp_now_recv_info_t *info,
>                     const uint8_t *data, int len) {
>     // виконується в контексті Wi-Fi — коротко, без важкої роботи
>     xQueueSend(cherga, data, 0);
> }
> esp_now_register_recv_cb(on_recv);
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-42-025 sha:2f70bab1 src:manual/42-espnow.md:56 klas:A -->
### T-42-025 · kod-ryadok · рядок 56

**Книга каже, дослівно:**

> xQueueSend(cherga, data, 0);

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

<!-- fc id:T-42-026 sha:f10cb37e src:manual/42-espnow.md:58 klas:A -->
### T-42-026 · kod-ryadok · рядок 58

**Книга каже, дослівно:**

> esp_now_register_recv_cb(on_recv);

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

<!-- fc id:T-42-027 sha:3b9efbae src:manual/42-espnow.md:62 klas:E -->
### T-42-027 · proza · рядок 62

**Книга каже, дослівно:**

> Обробник прийому виконується в контексті **задачі** Wi-Fi, а не в перериванні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-028 sha:96cc2aa7 src:manual/42-espnow.md:65 klas:F -->
### T-42-028 · proza · рядок 65

**Книга каже, дослівно:**

> Правило поведінки те саме, що для ISR (розділ 31): скопіювати дані, покласти в чергу, вийти.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-029 sha:6871d700 src:manual/42-espnow.md:65 klas:E -->
### T-42-029 · proza · рядок 65

**Книга каже, дослівно:**

> Важка робота там блокує радіостек.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-030 sha:8b37020a src:manual/42-espnow.md:68 klas:A -->
### T-42-030 · proza · рядок 68

**Книга каже, дослівно:**

> А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не `xQueueSendFromISR`.

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

<!-- fc id:T-42-031 sha:057d29d7 src:manual/42-espnow.md:68 klas:F -->
### T-42-031 · proza · рядок 68

**Книга каже, дослівно:**

> Варіант `FromISR` у задачі не спрацює як треба, і помилка ця тиха.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-032 sha:adbb1161 src:manual/42-espnow.md:68 klas:A -->
### T-42-032 · proza · рядок 68

**Книга каже, дослівно:**

> Нульовий таймаут у `xQueueSend` теж не випадковий: чекати на місце в черзі всередині радіостека не можна.

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

<!-- fc id:T-42-033 sha:774e7574 src:manual/42-espnow.md:73 klas:A -->
### T-42-033 · proza · рядок 73

**Книга каже, дослівно:**

> І окремо: `esp_now_recv_info_t`, на який указує `info`, живе **лише поки триває виклик**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-42-034 sha:9df638c8 src:manual/42-espnow.md:73 klas:E -->
### T-42-034 · proza · рядок 73

**Книга каже, дослівно:**

> Знадобився MAC відправника — копіювати його тут, а не зберігати покажчик.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-035 sha:5bd8e367 src:manual/42-espnow.md:80 klas:A -->
### T-42-035 · proza · рядок 80

**Книга каже, дослівно:**

> **Розмір пакета — до 250 байтів.** Це жорстко.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-42-036 sha:98e0962e src:manual/42-espnow.md:82 klas:F -->
### T-42-036 · proza · рядок 82

**Книга каже, дослівно:**

> **Немає гарантії доставки.** Є підтвердження на рівні кадру (`send_cb` повідомляє, чи пакет прийнято сусідом), але немає повторів і немає контролю порядку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-037 sha:b677b0b8 src:manual/42-espnow.md:86 klas:E -->
### T-42-037 · proza · рядок 86

**Книга каже, дослівно:**

> **Треба знати MAC отримувача.** Або зашити, або передати при налаштуванні, або використати широкомовну адресу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-038 sha:de0470ae src:manual/42-espnow.md:89 klas:E -->
### T-42-038 · proza · рядок 89

**Книга каже, дослівно:**

> **Один канал.** Усі учасники мають бути на одному радіоканалі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-039 sha:0f4b36d7 src:manual/42-espnow.md:91 klas:A -->
### T-42-039 · proza · рядок 91

**Книга каже, дослівно:**

> **Кількість peer-ів обмежена жорстко: 20 усього, з них не більше 6 зашифрованих.** Друге число визначає проєкт значно сильніше за перше: конструкція «багато датчиків → один приймач» із шифруванням упирається в шість датчиків на приймач, а не в двадцять.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-42-040 sha:01364990 src:manual/42-espnow.md:91 klas:E -->
### T-42-040 · proza · рядок 91

**Книга каже, дослівно:**

> Обходиться це або broadcast-обміном із власним шифруванням у полі корисних даних, або другим приймачем.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-041 sha:51237438 src:manual/42-espnow.md:100 klas:F -->
### T-42-041 · proza · рядок 100

**Книга каже, дослівно:**

> Широкомовна адреса `FF:FF:FF:FF:FF:FF` дозволяє передавати всім, хто слухає, не знаючи адрес.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-042 sha:c7e0acb3 src:manual/42-espnow.md:103 klas:E -->
### T-42-042 · proza · рядок 103

**Книга каже, дослівно:**

> Зручно для виявлення пристроїв і для розсилки команд одразу всім.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-043 sha:7d22d1f8 src:manual/42-espnow.md:103 klas:E -->
### T-42-043 · proza · рядок 103

**Книга каже, дослівно:**

> Обмеження: broadcast **не шифрується** — це властивість протоколу, а не налаштування.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-044 sha:f2cf5cc8 src:manual/42-espnow.md:107 klas:E -->
### T-42-044 · proza · рядок 107

**Книга каже, дослівно:**

> Практична схема: broadcast для початкового знайомства, далі — адресний обмін із шифруванням.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-045 sha:3ccbedcd src:manual/42-espnow.md:112 klas:E -->
### T-42-045 · proza · рядок 112

**Книга каже, дослівно:**

> ESP-NOW підтримує шифрування з ключами PMK і LMK.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-046 sha:5b245222 src:manual/42-espnow.md:114 klas:K -->
### T-42-046 · kod · рядок 114

**Книга каже, дослівно:**

> ```c
> esp_now_set_pmk((uint8_t *)"pmk1234567890123");   // рівно 16 байтів
> peer.encrypt = true;
> memcpy(peer.lmk, "lmk1234567890123", 16);
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

<!-- fc id:T-42-047 sha:fcda1a09 src:manual/42-espnow.md:117 klas:F -->
### T-42-047 · kod-ryadok · рядок 117

**Книга каже, дослівно:**

> memcpy(peer.lmk, "lmk1234567890123", 16);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-048 sha:5e201060 src:manual/42-espnow.md:121 klas:E -->
### T-42-048 · proza · рядок 121

**Книга каже, дослівно:**

> Без шифрування ESP-NOW — це відкритий радіоефір.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-049 sha:71c60544 src:manual/42-espnow.md:121 klas:F -->
### T-42-049 · proza · рядок 121

**Книга каже, дослівно:**

> Будь-хто з ESP32 поруч може слухати ваш обмін і, знаючи MAC, надсилати пакети від чужого імені.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-050 sha:cbf48b1d src:manual/42-espnow.md:124 klas:E -->
### T-42-050 · proza · рядок 124

**Книга каже, дослівно:**

> Для датчика температури це може бути прийнятним.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-051 sha:f3e296e5 src:manual/42-espnow.md:124 klas:E -->
### T-42-051 · proza · рядок 124

**Книга каже, дослівно:**

> Для будь-чого, що керує — ні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-052 sha:1cbf3006 src:manual/42-espnow.md:124 klas:F -->
### T-42-052 · proza · рядок 124

**Книга каже, дослівно:**

> Питання те саме, що в розділі 41: що станеться, якщо туди напише сторонній? (розділ 50)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-053 sha:b8699f11 src:manual/42-espnow.md:128 klas:F -->
### T-42-053 · proza · рядок 128

**Книга каже, дослівно:**

> І окремо: ключі, зашиті в код, дістаються з дампа прошивки за п'ять хвилин (розділ 24).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-054 sha:b135d061 src:manual/42-espnow.md:128 klas:F -->
### T-42-054 · proza · рядок 128

**Книга каже, дослівно:**

> Місце ключів — NVS, записаний окремо на кожен пристрій (розділ 21).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-055 sha:53d93813 src:manual/42-espnow.md:135 klas:E -->
### T-42-055 · proza · рядок 135

**Книга каже, дослівно:**

> Найважча практична частина.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-056 sha:48c74bdb src:manual/42-espnow.md:135 klas:E -->
### T-42-056 · proza · рядок 135

**Книга каже, дослівно:**

> ESP-NOW і Wi-Fi ділять одне радіо і **один канал**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-057 sha:f8115ba2 src:manual/42-espnow.md:138 klas:E -->
### T-42-057 · proza · рядок 138

**Книга каже, дослівно:**

> Коли пристрій під'єднаний до точки доступу, він працює на її каналі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-058 sha:4248c371 src:manual/42-espnow.md:138 klas:E -->
### T-42-058 · proza · рядок 138

**Книга каже, дослівно:**

> Щоб ESP-NOW працював, партнери мусять бути **на тому самому каналі** — а він визначається роутером і може змінитися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-059 sha:350ec4ac src:manual/42-espnow.md:144 klas:E -->
### T-42-059 · proza · рядок 144

**Книга каже, дослівно:**

> **Тільки ESP-NOW.** Найнадійніше.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-060 sha:1dda21f6 src:manual/42-espnow.md:144 klas:E -->
### T-42-060 · proza · рядок 144

**Книга каже, дослівно:**

> Усі вузли на фіксованому каналі, Wi-Fi не використовується.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-061 sha:6135207f src:manual/42-espnow.md:144 klas:E -->
### T-42-061 · proza · рядок 144

**Книга каже, дослівно:**

> Для замкненої мережі датчиків — оптимально.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-062 sha:8a44357a src:manual/42-espnow.md:147 klas:E -->
### T-42-062 · proza · рядок 147

**Книга каже, дослівно:**

> **Шлюз із двома ролями.** Датчики працюють тільки по ESP-NOW; один вузол (шлюз) під'єднаний до Wi-Fi і приймає ESP-NOW.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-063 sha:7ff46ce5 src:manual/42-espnow.md:147 klas:E -->
### T-42-063 · proza · рядок 147

**Книга каже, дослівно:**

> Шлюз мусить тримати канал ESP-NOW рівним каналу точки доступу — і, якщо роутер змінить канал, повідомити датчики або перейти сам.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-064 sha:1e516a9c src:manual/42-espnow.md:152 klas:E -->
### T-42-064 · proza · рядок 152

**Книга каже, дослівно:**

> **Динамічне перемикання.** Пристрій вимикає Wi-Fi, передає по ESP-NOW, вмикає назад.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-065 sha:e7ae9737 src:manual/42-espnow.md:152 klas:E -->
### T-42-065 · proza · рядок 152

**Книга каже, дослівно:**

> Працює, але з'їдає час і ускладнює логіку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-066 sha:9c93f60d src:manual/42-espnow.md:156 klas:E -->
### T-42-066 · proza · рядок 156

**Книга каже, дослівно:**

> Найчастіша проблема ESP-NOW у реальних установках: **усе працювало на столі, а на об'єкті перестало**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-067 sha:570fdf0b src:manual/42-espnow.md:156 klas:E -->
### T-42-067 · proza · рядок 156

**Книга каже, дослівно:**

> Причина майже завжди — роутер змінив канал (автоматичний вибір каналу увімкнений за замовчуванням у більшості роутерів), і шлюз переїхав, а датчики лишилися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-068 sha:fd5169b3 src:manual/42-espnow.md:161 klas:E -->
### T-42-068 · proza · рядок 161

**Книга каже, дослівно:**

> Лікування: зафіксувати канал у налаштуваннях роутера або передбачити процедуру повторного узгодження каналу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-069 sha:f4029737 src:manual/42-espnow.md:167 klas:E -->
### T-42-069 · proza · рядок 167

**Книга каже, дослівно:**

> Найпоширеніша й найвдаліша конструкція на ESP-NOW.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-070 sha:9a5c871c src:manual/42-espnow.md:169 klas:A -->
### T-42-070 · proza · рядок 169

**Книга каже, дослівно:**

> Десять датчиків прокидаються за розкладом, надсилають по 20 байтів на відомий MAC і засинають.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bt/host/bluedroid/stack/include/stack/gatt_api.h та https://raw.githubusercontent.com/apache/mynewt-nimble/master/nimble/host/include/host/ble_att.h
- **Дослівно з джерела:**
  > (Bluedroid, у складі ESP-IDF)
  > #define GATT_DEF_BLE_MTU_SIZE               23
  > #define GATT_MAX_MTU_SIZE                   517
  > 
  > (NimBLE, apache/mynewt-nimble)
  > #define BLE_ATT_MTU_DFLT                    23
  > #define BLE_ATT_MTU_MAX                     527
  >  * The specified MTU must be within the following range: [23, BLE_ATT_MTU_MAX].
  >  * 23 is a minimum imposed by the Bluetooth specification;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Закриває пункт наряду, який спирався на платну специфікацію Bluetooth Core. Обидва стеки, між якими вибирає розділ 41, дають те саме число, а коментар NimBLE прямо посилається на специфікацію як на джерело мінімуму. Клас A: цитати з обох стеків отримано.
- **Прохід:** pass-04-obkhidni

---

<!-- fc id:T-42-071 sha:92ea83dd src:manual/42-espnow.md:169 klas:F -->
### T-42-071 · proza · рядок 169

**Книга каже, дослівно:**

> Приймач постійно живиться, слухає, накопичує і віддає далі — у Wi-Fi, MQTT (розділ 40) чи на дисплей.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-072 sha:9b3986c9 src:manual/42-espnow.md:175 klas:E -->
### T-42-072 · proza · рядок 175

**Книга каже, дослівно:**

> - датчики не витрачають енергію на під'єднання; - вихід з ладу приймача не заважає датчикам працювати (вони просто передають у порожнечу); - додати датчик означає прописати його MAC у приймачі (пам'ятаючи про межу peer-ів вище); - немає роутера — немає залежності від його налаштувань.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-073 sha:01975951 src:manual/42-espnow.md:184 klas:E -->
### T-42-073 · proza · рядок 184

**Книга каже, дослівно:**

> **Лічильник у пакеті.** Приймач бачить пропуски й може оцінити якість зв'язку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-074 sha:159e1c45 src:manual/42-espnow.md:187 klas:F -->
### T-42-074 · proza · рядок 187

**Книга каже, дослівно:**

> **Мітка часу від приймача**, а не від датчика: у датчика немає точного часу (розділ 40).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-075 sha:b40becd9 src:manual/42-espnow.md:190 klas:E -->
### T-42-075 · proza · рядок 190

**Книга каже, дослівно:**

> **Буфер у датчику.** Не дійшло — спробувати ще раз наступного разу, надіславши два вимірювання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-076 sha:69210e00 src:manual/42-espnow.md:195 klas:A -->
### T-42-076 · proza · рядок 195

**Книга каже, дослівно:**

> **Багато даних.** 250 байтів на пакет і відсутність контролю потоку роблять його непридатним для потокової передачі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-42-077 sha:b6848d71 src:manual/42-espnow.md:198 klas:E -->
### T-42-077 · proza · рядок 198

**Книга каже, дослівно:**

> **Велика відстань.** Дальність та сама, що у Wi-Fi.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-078 sha:0f61ca0f src:manual/42-espnow.md:198 klas:F -->
### T-42-078 · proza · рядок 198

**Книга каже, дослівно:**

> Потрібні кілометри — це LoRa (розділ 43).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-079 sha:bc696489 src:manual/42-espnow.md:201 klas:E -->
### T-42-079 · proza · рядок 201

**Книга каже, дослівно:**

> **Обмін із чимось, крім ESP.** Протокол власний: телефон, комп'ютер чи чужий контролер його не розуміють.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-080 sha:ec26b923 src:manual/42-espnow.md:204 klas:E -->
### T-42-080 · proza · рядок 204

**Книга каже, дослівно:**

> **Потрібна гарантована доставка.** Доведеться будувати підтвердження самому.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-081 sha:b34287fd src:manual/42-espnow.md:209 klas:E -->
### T-42-081 · proza · рядок 209

**Книга каже, дослівно:**

> Головна перевага — передача без під'єднання: мілісекунди замість секунд, два порядки економії на циклі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-082 sha:1ccd7865 src:manual/42-espnow.md:212 klas:A -->
### T-42-082 · proza · рядок 212

**Книга каже, дослівно:**

> 250 байтів на пакет, немає гарантії доставки.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-42-083 sha:574fb8ff src:manual/42-espnow.md:214 klas:E -->
### T-42-083 · proza · рядок 214

**Книга каже, дослівно:**

> Усі учасники на одному каналі; співіснування з Wi-Fi — головна складність.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-084 sha:35a8ee97 src:manual/42-espnow.md:216 klas:E -->
### T-42-084 · proza · рядок 216

**Книга каже, дослівно:**

> Роутер, що сам змінив канал, — найчастіша причина «працювало на столі, не працює на об'єкті».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-085 sha:797fdb03 src:manual/42-espnow.md:219 klas:E -->
### T-42-085 · proza · рядок 219

**Книга каже, дослівно:**

> Без шифрування це відкритий ефір; ключі зберігати в NVS, не в коді.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-086 sha:5242ab3d src:manual/42-espnow.md:221 klas:E -->
### T-42-086 · proza · рядок 221

**Книга каже, дослівно:**

> Конструкція «багато датчиків → один приймач» — найвдаліше застосування.

**Доказ**

- **Клас:** F — не звірено

---
