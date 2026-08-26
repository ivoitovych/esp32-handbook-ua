# Фактчекінг: `manual/63-proj-mist.md`

Одиниць твердження: **80**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-63-001 sha:fedd4339 src:manual/63-proj-mist.md:3 klas:F -->
### T-63-001 · proza · рядок 3

**Книга каже, дослівно:**

> Пристрій, що з'єднує дві сторони, які не розмовляють одна з одною: обладнання з послідовним портом і мережу, RS-485 і Wi-Fi, CAN і MQTT.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-002 sha:59fe3663 src:manual/63-proj-mist.md:6 klas:F -->
### T-63-002 · proza · рядок 6

**Книга каже, дослівно:**

> Це найпоширеніша реальна роль ESP32 у чужій системі (розділ 57), і проєкт зібраний як каркас, що налаштовується під конкретний випадок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-003 sha:9d3eb30c src:manual/63-proj-mist.md:11 klas:F -->
### T-63-003 · proza · рядок 11

**Книга каже, дослівно:**

> **Задача:** прозоро передавати дані між послідовним інтерфейсом і мережею, у обидва боки, з логуванням і можливістю налаштувати параметри без перепрошивки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-004 sha:03f842f5 src:manual/63-proj-mist.md:15 klas:F -->
### T-63-004 · proza · рядок 15

**Книга каже, дослівно:**

> **Варіанти, які покриває один каркас:**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-005 sha:a460c66e src:manual/63-proj-mist.md:17 klas:F -->
### T-63-005 · tablycya-shapka · рядок 17

**Книга каже, дослівно:**

> | Міст | Один бік | Другий бік |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-006 sha:ad923067 src:manual/63-proj-mist.md:18 klas:F -->
### T-63-006 · komirka · рядок 18

**Книга каже, дослівно:**

> Термінал по мережі · Один бік → UART

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-007 sha:a82ae55f src:manual/63-proj-mist.md:18 klas:F -->
### T-63-007 · komirka · рядок 18

**Книга каже, дослівно:**

> Термінал по мережі · Другий бік → TCP-сервер

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-008 sha:5e51e79b src:manual/63-proj-mist.md:19 klas:F -->
### T-63-008 · komirka · рядок 19

**Книга каже, дослівно:**

> Modbus TCP → RTU · Один бік → RS-485

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-009 sha:ffcf0fd3 src:manual/63-proj-mist.md:19 klas:F -->
### T-63-009 · komirka · рядок 19

**Книга каже, дослівно:**

> Modbus TCP → RTU · Другий бік → TCP-сервер

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-010 sha:d770730c src:manual/63-proj-mist.md:20 klas:F -->
### T-63-010 · komirka · рядок 20

**Книга каже, дослівно:**

> Телеметрія · Один бік → UART або CAN

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-011 sha:8eb44ead src:manual/63-proj-mist.md:20 klas:F -->
### T-63-011 · komirka · рядок 20

**Книга каже, дослівно:**

> Телеметрія · Другий бік → MQTT

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-012 sha:b5bf5fd8 src:manual/63-proj-mist.md:21 klas:F -->
### T-63-012 · komirka · рядок 21

**Книга каже, дослівно:**

> Шлюз шини · Один бік → CAN

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-013 sha:2c46ea77 src:manual/63-proj-mist.md:21 klas:F -->
### T-63-013 · komirka · рядок 21

**Книга каже, дослівно:**

> Шлюз шини · Другий бік → Wi-Fi + MQTT

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-014 sha:e9aec07f src:manual/63-proj-mist.md:24 klas:F -->
### T-63-014 · proza · рядок 24

**Книга каже, дослівно:**

> **Поведінка при відмові:** зникла мережа — дані з послідовного боку буферизуються; зник послідовний бік — мережевий клієнт отримує повідомлення, а не тишу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-015 sha:6adf159f src:manual/63-proj-mist.md:30 klas:F -->
### T-63-015 · proza · рядок 30

**Книга каже, дослівно:**

> Два незалежні напрямки, кожен зі своєю задачею і чергою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-016 sha:fd256b9b src:manual/63-proj-mist.md:30 klas:F -->
### T-63-016 · proza · рядок 30

**Книга каже, дослівно:**

> Це ключове рішення: жодна сторона не має блокувати іншу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-017 sha:a37df5ab src:manual/63-proj-mist.md:33 klas:K -->
### T-63-017 · kod · рядок 33

**Книга каже, дослівно:**

> ```
>    UART/RS-485/CAN                          мережа
>         │                                      │
>    [task_rx_serial] ──> cherga_do_merezhi ──> [task_tx_net]
>                                               
>    [task_tx_serial] <── cherga_do_serial  <── [task_rx_net]
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-018 sha:2e4d5ee9 src:manual/63-proj-mist.md:35 klas:F -->
### T-63-018 · schema-zvyazok · рядок 35

**Книга каже, дослівно:**

> │                                      │

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-019 sha:a6c093a3 src:manual/63-proj-mist.md:36 klas:F -->
### T-63-019 · schema-zvyazok · рядок 36

**Книга каже, дослівно:**

> [task_rx_serial] ──> cherga_do_merezhi ──> [task_tx_net]

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-020 sha:12977693 src:manual/63-proj-mist.md:38 klas:F -->
### T-63-020 · schema-zvyazok · рядок 38

**Книга каже, дослівно:**

> [task_tx_serial] <── cherga_do_serial  <── [task_rx_net]

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-021 sha:ccb7e5b3 src:manual/63-proj-mist.md:41 klas:K -->
### T-63-021 · kod · рядок 41

**Книга каже, дослівно:**

> ```c
> typedef struct {
>     uint16_t dovzhyna;
>     uint8_t  dani[512];
> } blok_t;
> 
> static QueueHandle_t do_merezhi;   // від послідовного боку в мережу
> static QueueHandle_t do_serial;    // з мережі в послідовний бік
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-022 sha:f5dcbd4f src:manual/63-proj-mist.md:52 klas:F -->
### T-63-022 · proza · рядок 52

**Книга каже, дослівно:**

> Черги фіксованого розміру — це і буфер, і **захист від перевантаження**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-023 sha:2597f20d src:manual/63-proj-mist.md:52 klas:A -->
### T-63-023 · proza · рядок 52

**Книга каже, дослівно:**

> Коли одна сторона швидша за іншу, черга заповнюється, і `xQueueSend` повертає помилку — тобто ви **дізнаєтеся** про перевантаження замість того, щоб мовчки з'їсти пам'ять.

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

<!-- fc id:T-63-024 sha:bd1cc93c src:manual/63-proj-mist.md:57 klas:F -->
### T-63-024 · proza · рядок 57

**Книга каже, дослівно:**

> Міст без обмеження буфера при відсутній мережі з'їдає всю купу за хвилини й падає (розділ 30).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-025 sha:e18e6e3b src:manual/63-proj-mist.md:63 klas:K -->
### T-63-025 · kod · рядок 63

**Книга каже, дослівно:**

> ```c
> static void task_rx_serial(void *arg) {
>     blok_t b;
>     while (1) {
>         int n = uart_read_bytes(UART_PORT, b.dani, sizeof(b.dani),
>                                 pdMS_TO_TICKS(20));
>         if (n <= 0) continue;
>         b.dovzhyna = n;
>         if (xQueueSend(do_merezhi, &b, 0) != pdTRUE) {
>             vtracheno_do_merezhi += n;
>             ESP_LOGW(TAG, "черга в мережу повна, втрачено %d Б", n);
>         }
>     }
> }
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

<!-- fc id:T-63-026 sha:15e56919 src:manual/63-proj-mist.md:68 klas:A -->
### T-63-026 · kod-ryadok · рядок 68

**Книга каже, дослівно:**

> pdMS_TO_TICKS(20));

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

<!-- fc id:T-63-027 sha:2bec772f src:manual/63-proj-mist.md:73 klas:F -->
### T-63-027 · kod-ryadok · рядок 73

**Книга каже, дослівно:**

> ESP_LOGW(TAG, "черга в мережу повна, втрачено %d Б", n);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-028 sha:bb7614e8 src:manual/63-proj-mist.md:79 klas:F -->
### T-63-028 · proza · рядок 79

**Книга каже, дослівно:**

> Читання з коротким таймаутом, а не порція фіксованого розміру: дані з послідовного порту приходять довільними шматками, і чекати повного буфера означає додавати затримку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-029 sha:d4feea6b src:manual/63-proj-mist.md:83 klas:D -->
### T-63-029 · proza · рядок 83

**Книга каже, дослівно:**

> **Розмір буфера драйвера** беруть із запасом: на 115200 бод це близько 11 КБ на секунду, і 256 байтів переповнюються за 22 мілісекунди (розділ 34).

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py
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
- **Спосіб і дата:** python3 tools/arytmetyka.py, 2026-08-26
- **Нотатка:** Перевірку внесено в `make check` окремою ціллю `arytmetyka`. Це відповідь на те, як у книгу колись потрапили значення `duty` для серво від іншої роздільності: абзац із неправильним добутком внутрішньо несуперечливий і зовнішнього джерела не потребує, тож ні читання, ні звірка з першоджерелом його не ловлять. Ловить лише калькулятор — і тепер він запускається сам.
- **Прохід:** pass-05-obchyslennya

---

<!-- fc id:T-63-030 sha:99e6c971 src:manual/63-proj-mist.md:89 klas:K -->
### T-63-030 · kod · рядок 89

**Книга каже, дослівно:**

> ```c
> static void nadislaty_serial(const blok_t *b) {
> #if REZHYM_RS485
>     gpio_set_level(PIN_DE, 1);
> #endif
>     uart_write_bytes(UART_PORT, b->dani, b->dovzhyna);
> #if REZHYM_RS485
>     uart_wait_tx_done(UART_PORT, portMAX_DELAY);   // ОБОВ'ЯЗКОВО
>     gpio_set_level(PIN_DE, 0);
> #endif
> }
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

<!-- fc id:T-63-031 sha:0c32211a src:manual/63-proj-mist.md:92 klas:F -->
### T-63-031 · kod-ryadok · рядок 92

**Книга каже, дослівно:**

> gpio_set_level(PIN_DE, 1);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-032 sha:9c41187b src:manual/63-proj-mist.md:94 klas:A -->
### T-63-032 · kod-ryadok · рядок 94

**Книга каже, дослівно:**

> uart_write_bytes(UART_PORT, b->dani, b->dovzhyna);

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

<!-- fc id:T-63-033 sha:82ed161b src:manual/63-proj-mist.md:97 klas:F -->
### T-63-033 · kod-ryadok · рядок 97

**Книга каже, дослівно:**

> gpio_set_level(PIN_DE, 0);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-034 sha:6fe4bed6 src:manual/63-proj-mist.md:103 klas:A -->
### T-63-034 · proza · рядок 103

**Книга каже, дослівно:**

> `uart_wait_tx_done` перед перемиканням напрямку — найчастіша помилка роботи з RS-485 (розділ 34).

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

<!-- fc id:T-63-035 sha:c3a7d066 src:manual/63-proj-mist.md:106 klas:A -->
### T-63-035 · proza · рядок 106

**Книга каже, дослівно:**

> `uart_write_bytes` лише кладе дані в буфер і повертається одразу.

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

<!-- fc id:T-63-036 sha:24664874 src:manual/63-proj-mist.md:106 klas:F -->
### T-63-036 · proza · рядок 106

**Книга каже, дослівно:**

> Перемкнути напрямок відразу після нього означає обрізати власну посилку посередині — і виглядає це як «інколи губляться відповіді», що збиває з пантелику надовго.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-037 sha:66e8b36e src:manual/63-proj-mist.md:114 klas:K -->
### T-63-037 · kod · рядок 114

**Книга каже, дослівно:**

> ```c
> static void task_tcp(void *arg) {
>     int listen_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
>     struct sockaddr_in addr = {
>         .sin_family = AF_INET,
>         .sin_addr.s_addr = htonl(INADDR_ANY),
>         .sin_port = htons(PORT),
>     };
>     bind(listen_sock, (struct sockaddr *)&addr, sizeof(addr));
>     listen(listen_sock, 1);
> 
>     while (1) {
>         struct sockaddr_in klient;
>         socklen_t len = sizeof(klient);
>         int sock = accept(listen_sock, (struct sockaddr *)&klient, &len);
>         if (sock < 0) continue;
> 
>         ESP_LOGI(TAG, "клієнт під'єднався");
>         // очистити чергу: клієнт не має отримати те, що накопичилося
>         xQueueReset(do_merezhi);
> 
>         obsluhovuvaty(sock);          // до розриву з'єднання
>         close(sock);
>         ESP_LOGI(TAG, "клієнт від'єднався");
>     }
> }
> ```

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

<!-- fc id:T-63-038 sha:2a61cebc src:manual/63-proj-mist.md:118 klas:F -->
### T-63-038 · kod-ryadok · рядок 118

**Книга каже, дослівно:**

> .sin_family = AF_INET,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-039 sha:c18a302b src:manual/63-proj-mist.md:120 klas:F -->
### T-63-039 · kod-ryadok · рядок 120

**Книга каже, дослівно:**

> .sin_port = htons(PORT),

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-040 sha:d4572ea9 src:manual/63-proj-mist.md:122 klas:F -->
### T-63-040 · kod-ryadok · рядок 122

**Книга каже, дослівно:**

> bind(listen_sock, (struct sockaddr *)&addr, sizeof(addr));

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-041 sha:7fdee34f src:manual/63-proj-mist.md:123 klas:F -->
### T-63-041 · kod-ryadok · рядок 123

**Книга каже, дослівно:**

> listen(listen_sock, 1);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-042 sha:69390e31 src:manual/63-proj-mist.md:131 klas:F -->
### T-63-042 · kod-ryadok · рядок 131

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "клієнт під'єднався");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-043 sha:2c701669 src:manual/63-proj-mist.md:133 klas:A -->
### T-63-043 · kod-ryadok · рядок 133

**Книга каже, дослівно:**

> xQueueReset(do_merezhi);

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

<!-- fc id:T-63-044 sha:0d388178 src:manual/63-proj-mist.md:136 klas:F -->
### T-63-044 · kod-ryadok · рядок 136

**Книга каже, дослівно:**

> close(sock);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-045 sha:c6873381 src:manual/63-proj-mist.md:137 klas:F -->
### T-63-045 · kod-ryadok · рядок 137

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "клієнт від'єднався");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-046 sha:8d130e38 src:manual/63-proj-mist.md:143 klas:A -->
### T-63-046 · proza · рядок 143

**Книга каже, дослівно:**

> `xQueueReset` при під'єднанні нового клієнта — важлива дрібниця.

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

<!-- fc id:T-63-047 sha:4dd09020 src:manual/63-proj-mist.md:143 klas:F -->
### T-63-047 · proza · рядок 143

**Книга каже, дослівно:**

> Без неї клієнт одразу отримує все, що накопичилося за час, поки ніхто не слухав: для термінала це сотні рядків старих даних.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-048 sha:e867d143 src:manual/63-proj-mist.md:147 klas:F -->
### T-63-048 · proza · рядок 147

**Книга каже, дослівно:**

> Виняток — міст, де дані не можна втрачати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-049 sha:392d6692 src:manual/63-proj-mist.md:147 klas:F -->
### T-63-049 · proza · рядок 147

**Книга каже, дослівно:**

> Тоді, навпаки, накопичене треба віддати, і черга має бути більшою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-050 sha:b5609df0 src:manual/63-proj-mist.md:151 klas:F -->
### T-63-050 · proza · рядок 151

**Книга каже, дослівно:**

> **Один клієнт одночасно** — свідоме обмеження.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-051 sha:201a16b4 src:manual/63-proj-mist.md:151 klas:F -->
### T-63-051 · proza · рядок 151

**Книга каже, дослівно:**

> Кілька клієнтів на одному послідовному порту означають перемішані відповіді: обладнання не знає, кому воно відповідає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-052 sha:be351eec src:manual/63-proj-mist.md:151 klas:F -->
### T-63-052 · proza · рядок 151

**Книга каже, дослівно:**

> Для Modbus це прямий шлях до хаосу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-053 sha:12f1694d src:manual/63-proj-mist.md:157 klas:F -->
### T-63-053 · proza · рядок 157

**Книга каже, дослівно:**

> Міст, у якого швидкість зашита в код, доводиться перепрошивати при кожній зміні обладнання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-054 sha:1985092e src:manual/63-proj-mist.md:157 klas:F -->
### T-63-054 · proza · рядок 157

**Книга каже, дослівно:**

> Параметри йдуть у NVS (розділ 18):

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-055 sha:529f3b27 src:manual/63-proj-mist.md:160 klas:K -->
### T-63-055 · kod · рядок 160

**Книга каже, дослівно:**

> ```c
> typedef struct {
>     uint32_t baud;
>     uint8_t  data_bits, parity, stop_bits;
>     uint8_t  rezhym;          // UART, RS-485, CAN
>     uint16_t tcp_port;
>     char     mqtt_uri[128];
>     char     mqtt_topic[64];
> } nalashtuvannya_t;
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-056 sha:f0f5135a src:manual/63-proj-mist.md:171 klas:F -->
### T-63-056 · proza · рядок 171

**Книга каже, дослівно:**

> Задаються через веб-форму (розділ 40), зберігаються в NVS, читаються при старті.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-057 sha:a87c2640 src:manual/63-proj-mist.md:171 klas:F -->
### T-63-057 · proza · рядок 171

**Книга каже, дослівно:**

> Скидання на заводські — довгим натисканням кнопки (розділ 39).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-058 sha:09283dc8 src:manual/63-proj-mist.md:176 klas:K -->
### T-63-058 · kod · рядок 176

**Книга каже, дослівно:**

> ```c
> static void task_rx_can(void *arg) {
>     twai_message_t msg;
>     while (1) {
>         if (twai_receive(&msg, pdMS_TO_TICKS(100)) != ESP_OK) continue;
> 
>         blok_t b;
>         b.dovzhyna = snprintf((char *)b.dani, sizeof(b.dani),
>                               "%03lx:%d:", msg.identifier,
>                               msg.data_length_code);
>         for (int i = 0; i < msg.data_length_code; i++)
>             b.dovzhyna += snprintf((char *)b.dani + b.dovzhyna,
>                                    sizeof(b.dani) - b.dovzhyna,
>                                    "%02x", msg.data[i]);
>         b.dani[b.dovzhyna++] = '\n';
>         xQueueSend(do_merezhi, &b, 0);
>     }
> }
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

<!-- fc id:T-63-059 sha:fdd16bb3 src:manual/63-proj-mist.md:191 klas:A -->
### T-63-059 · kod-ryadok · рядок 191

**Книга каже, дослівно:**

> xQueueSend(do_merezhi, &b, 0);

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

<!-- fc id:T-63-060 sha:582d7e98 src:manual/63-proj-mist.md:196 klas:F -->
### T-63-060 · proza · рядок 196

**Книга каже, дослівно:**

> Текстове представлення обрано свідомо: такий потік читається людиною в терміналі й розбирається будь-яким скриптом без домовленостей про двійковий формат.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-061 sha:05909696 src:manual/63-proj-mist.md:201 klas:F -->
### T-63-061 · proza · рядок 201

**Книга каже, дослівно:**

> Міст на CAN за замовчуванням має працювати в режимі **`LISTEN_ONLY`** (розділ 38).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-062 sha:cba16aff src:manual/63-proj-mist.md:204 klas:F -->
### T-63-062 · proza · рядок 204

**Книга каже, дослівно:**

> Передача в чужу працюючу шину — дія з наслідками: пакет із чужим ідентифікатором може бути сприйнятий як команда керування.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-063 sha:631e3a04 src:manual/63-proj-mist.md:204 klas:F -->
### T-63-063 · proza · рядок 204

**Книга каже, дослівно:**

> У техніці, що рухається або гріє, це не формальність.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-064 sha:a4aa8b3c src:manual/63-proj-mist.md:208 klas:F -->
### T-63-064 · proza · рядок 208

**Книга каже, дослівно:**

> Передача вмикається окремим свідомим налаштуванням, і за замовчуванням вона вимкнена.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-065 sha:72c8c00f src:manual/63-proj-mist.md:214 klas:F -->
### T-63-065 · proza · рядок 214

**Книга каже, дослівно:**

> Міст, який мовчки не працює, — найгірший варіант.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-066 sha:9018335a src:manual/63-proj-mist.md:214 klas:F -->
### T-63-066 · proza · рядок 214

**Книга каже, дослівно:**

> Мінімум лічильників, доступних через веб:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-067 sha:88a71994 src:manual/63-proj-mist.md:217 klas:K -->
### T-63-067 · kod · рядок 217

**Книга каже, дослівно:**

> ```c
> static struct {
>     uint32_t serial_rx, serial_tx;
>     uint32_t net_rx, net_tx;
>     uint32_t vtracheno_do_merezhi, vtracheno_do_serial;
>     uint32_t pomylok_serial;
>     int64_t  ostannya_aktyvnist;
> } statystyka;
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-068 sha:c5ba6a52 src:manual/63-proj-mist.md:227 klas:F -->
### T-63-068 · proza · рядок 227

**Книга каже, дослівно:**

> Ці сім чисел відповідають на головне питання діагностики: **на якому боці зупинилося**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-069 sha:af328f59 src:manual/63-proj-mist.md:227 klas:F -->
### T-63-069 · proza · рядок 227

**Книга каже, дослівно:**

> Дані йдуть із послідовного, але не йдуть у мережу — проблема в мережі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-070 sha:8a0f6cc7 src:manual/63-proj-mist.md:227 klas:F -->
### T-63-070 · proza · рядок 227

**Книга каже, дослівно:**

> Не йдуть із послідовного — проблема на тому боці або в налаштуваннях порту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-071 sha:3aa19ebb src:manual/63-proj-mist.md:232 klas:F -->
### T-63-071 · proza · рядок 232

**Книга каже, дослівно:**

> Без цих лічильників те саме з'ясовується логічним аналізатором і годинами (розділ 28).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-072 sha:b2417e1d src:manual/63-proj-mist.md:237 klas:F -->
### T-63-072 · proza · рядок 237

**Книга каже, дослівно:**

> **Заглушка:** з'єднати `TX` і `RX` між собою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-073 sha:477e1cf2 src:manual/63-proj-mist.md:237 klas:F -->
### T-63-073 · proza · рядок 237

**Книга каже, дослівно:**

> Усе, що надіслано з мережі, має повернутися. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-074 sha:ffa0be4a src:manual/63-proj-mist.md:237 klas:F -->
### T-63-074 · proza · рядок 237

**Книга каже, дослівно:**

> **Реальне обладнання:** підключити, звірити швидкість і формат. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-075 sha:cb1d1c36 src:manual/63-proj-mist.md:237 klas:F -->
### T-63-075 · proza · рядок 237

**Книга каже, дослівно:**

> **Обрив мережі** під час обміну: лічильник втрат росте, пристрій живий, після відновлення все працює. 4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-076 sha:ba43020f src:manual/63-proj-mist.md:237 klas:F -->
### T-63-076 · proza · рядок 237

**Книга каже, дослівно:**

> **Обрив послідовного боку:** мережевий клієнт отримує повідомлення про це. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-077 sha:eb7a0411 src:manual/63-proj-mist.md:237 klas:F -->
### T-63-077 · proza · рядок 237

**Книга каже, дослівно:**

> **Перевантаження:** подати потік швидший, ніж може прийняти другий бік.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-078 sha:9dc32c61 src:manual/63-proj-mist.md:237 klas:F -->
### T-63-078 · proza · рядок 237

**Книга каже, дослівно:**

> Черга має переповнитися **з логом**, а не з'їсти пам'ять. 6.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-079 sha:9afcee63 src:manual/63-proj-mist.md:237 klas:F -->
### T-63-079 · proza · рядок 237

**Книга каже, дослівно:**

> **Доба роботи** з реальним трафіком: мінімум вільної пам'яті не зменшується (розділ 58).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-63-080 sha:20ab681f src:manual/63-proj-mist.md:251 klas:F -->
### T-63-080 · proza · рядок 251

**Книга каже, дослівно:**

> - **Modbus RTU ↔ TCP** зі штатним компонентом `esp-modbus` замість прозорого мосту (розділ 34); - **Кілька послідовних портів** одночасно; - **Фільтрація** на боці CAN — приймати лише потрібні ідентифікатори, не турбуючи процесор рештою; - **Буферизація у флеш** для мостів, де втрата даних неприйнятна; - **Companion-роль** (розділ 57): міст як постійна частина великої системи, з паспортом і версіонуванням (розділ 56).

**Доказ**

- **Клас:** F — не звірено

---
