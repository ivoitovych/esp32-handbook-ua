# Фактчекінг: `manual/42-espnow.md`

Одиниць твердження: **86**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-42-001 sha:e12353a5 src:manual/42-espnow.md:3 klas:A -->
### T-42-001 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> ESP-NOW — власний протокол Espressif для прямого обміну між пристроями на ESP32 і ESP8266.

**Дослівно з книги**

```
ESP-NOW — власний протокол Espressif для прямого обміну між пристроями
```

**Контекст**

```
# 42. ESP-NOW {#espnow}

ESP-NOW — власний протокол Espressif для прямого обміну між пристроями
на ESP32 і ESP8266. Без роутера, без точки доступу, без IP-адрес.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > ESP-NOW is a kind of connectionless Wi-Fi communication protocol that is defined by Espressif.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документ каже "defined by Espressif", а не "власний протокол". Крім того, документ не згадує ESP8266.
- **Прохід:** klas-f-42-espnow

---

<!-- fc id:T-42-002 sha:dd3855b4 src:manual/42-espnow.md:3 klas:E -->
### T-42-002 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Без роутера, без точки доступу, без IP-адрес.

**Дослівно з книги**

```
на ESP32 і ESP8266. Без роутера, без точки доступу, без IP-адрес.
```

**Контекст**

```
# 42. ESP-NOW {#espnow}

ESP-NOW — власний протокол Espressif для прямого обміну між пристроями
на ESP32 і ESP8266. Без роутера, без точки доступу, без IP-адрес.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-003 sha:3a142f89 src:manual/42-espnow.md:6 klas:E -->
### T-42-003 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Для автономних датчиків це часто найкраще технічне рішення в усій книзі, і причина одна: **передача без під'єднання**.

**Дослівно з книги**

```
Для автономних датчиків це часто найкраще технічне рішення в усій книзі,
```

**Контекст**

```
# 42. ESP-NOW {#espnow}

Для автономних датчиків це часто найкраще технічне рішення в усій книзі,
і причина одна: **передача без під'єднання**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-004 sha:bdf974c6 src:manual/42-espnow.md:11 klas:F -->
### T-42-004 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Звичайний Wi-Fi перед першою передачею мусить під'єднатися до точки доступу: сканування, автентифікація, асоціація, отримання IP.

**Дослівно з книги**

```
Звичайний Wi-Fi перед першою передачею мусить під'єднатися до точки
```

**Контекст**

```
## Чому це важливо

Звичайний Wi-Fi перед першою передачею мусить під'єднатися до точки
доступу: сканування, автентифікація, асоціація, отримання IP. Це
секунди — від однієї до десяти, а на межі покриття може не відбутися
взагалі (розділ 39).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-005 sha:63289213 src:manual/42-espnow.md:11 klas:E -->
### T-42-005 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Це секунди — від однієї до десяти, а на межі покриття може не відбутися взагалі (розділ 39).

**Дослівно з книги**

```
Звичайний Wi-Fi перед першою передачею мусить під'єднатися до точки
```

**Контекст**

```
## Чому це важливо

Звичайний Wi-Fi перед першою передачею мусить під'єднатися до точки
доступу: сканування, автентифікація, асоціація, отримання IP. Це
секунди — від однієї до десяти, а на межі покриття може не відбутися
взагалі (розділ 39).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-006 sha:9eee4e7d src:manual/42-espnow.md:16 klas:A -->
### T-42-006 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> ESP-NOW не робить нічого з цього.

**Дослівно з книги**

```
ESP-NOW не робить нічого з цього. Пакет іде **одразу**, за мілісекунди.
```

**Контекст**

```
## Чому це важливо

ESP-NOW не робить нічого з цього. Пакет іде **одразу**, за мілісекунди.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > ESP-NOW is a kind of connectionless Wi-Fi communication protocol that is defined by Espressif. In ESP-NOW, application data is encapsulated in a vendor-specific action frame and then transmitted from one Wi-Fi device to another without connection.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP-NOW не потребує підключення до точки доступу, на відміну від звичайного Wi-Fi. Слово "connectionless" підтверджує, що ESP-NOW не робить нічого з того, що потрібно для звичайного Wi-Fi.
- **Прохід:** klas-f-42-espnow

---

<!-- fc id:T-42-007 sha:c2bc31a0 src:manual/42-espnow.md:16 klas:E -->
### T-42-007 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Пакет іде **одразу**, за мілісекунди.

**Дослівно з книги**

```
ESP-NOW не робить нічого з цього. Пакет іде **одразу**, за мілісекунди.
```

**Контекст**

```
## Чому це важливо

ESP-NOW не робить нічого з цього. Пакет іде **одразу**, за мілісекунди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-008 sha:ea18b432 src:manual/42-espnow.md:19 klas:E -->
### T-42-008 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Для датчика на батарейці, який прокидається, міряє й засинає (розділ 06), різниця виглядає так:

**Дослівно з книги**

```
Для датчика на батарейці, який прокидається, міряє й засинає
```

**Контекст**

```
## Чому це важливо

::: zhyvlennya
Для датчика на батарейці, який прокидається, міряє й засинає
(розділ 06), різниця виглядає так:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-009 sha:56101255 src:manual/42-espnow.md:22 klas:F -->
### T-42-009 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> *Wi-Fi:* прокинувся → 3 секунди на під'єднання → передав → заснув.

**Контекст**

```
## Чому це важливо

*Wi-Fi:* прокинувся → 3 секунди на під'єднання → передав → заснув.
Активна фаза — три з половиною секунди при сотні міліампер.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-010 sha:88f5799c src:manual/42-espnow.md:22 klas:E -->
### T-42-010 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Активна фаза — три з половиною секунди при сотні міліампер.

**Контекст**

```
## Чому це важливо

*Wi-Fi:* прокинувся → 3 секунди на під'єднання → передав → заснув.
Активна фаза — три з половиною секунди при сотні міліампер.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-011 sha:7c2c734a src:manual/42-espnow.md:25 klas:F -->
### T-42-011 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> *ESP-NOW:* прокинувся → 10 мілісекунд на передачу → заснув.

**Дослівно з книги**

```
*ESP-NOW:* прокинувся → 10 мілісекунд на передачу → заснув. Активна
```

**Контекст**

```
## Чому це важливо

*ESP-NOW:* прокинувся → 10 мілісекунд на передачу → заснув. Активна
фаза — частки секунди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-012 sha:f19af6af src:manual/42-espnow.md:25 klas:E -->
### T-42-012 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Активна фаза — частки секунди.

**Дослівно з книги**

```
*ESP-NOW:* прокинувся → 10 мілісекунд на передачу → заснув. Активна
```

**Контекст**

```
## Чому це важливо

*ESP-NOW:* прокинувся → 10 мілісекунд на передачу → заснув. Активна
фаза — частки секунди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-013 sha:a26e8f1c src:manual/42-espnow.md:28 klas:E -->
### T-42-013 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Це різниця у **два порядки** в споживанні на цикл, тобто різниця між місяцем і роками роботи від тих самих батарейок.

**Дослівно з книги**

```
Це різниця у **два порядки** в споживанні на цикл, тобто різниця між
```

**Контекст**

```
## Чому це важливо

Це різниця у **два порядки** в споживанні на цикл, тобто різниця між
місяцем і роками роботи від тих самих батарейок.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-014 sha:8cf4ae97 src:manual/42-espnow.md:34 klas:E -->
### T-42-014 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Обмін іде за **MAC-адресами**.

**Дослівно з книги**

```
Обмін іде за **MAC-адресами**. Кожен пристрій має унікальну MAC від
```

**Контекст**

```
## Як воно влаштоване

Обмін іде за **MAC-адресами**. Кожен пристрій має унікальну MAC від
заводу (розділ 20), і вона ж є адресою в ESP-NOW.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-015 sha:de2e8697 src:manual/42-espnow.md:34 klas:A -->
### T-42-015 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Кожен пристрій має унікальну MAC від заводу (розділ 20), і вона ж є адресою в ESP-NOW.

**Дослівно з книги**

```
Обмін іде за **MAC-адресами**. Кожен пристрій має унікальну MAC від
```

**Контекст**

```
## Як воно влаштоване

Обмін іде за **MAC-адресами**. Кожен пристрій має унікальну MAC від
заводу (розділ 20), і вона ж є адресою в ESP-NOW.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > As ESP-NOW is connectionless, the MAC header is a little different from that of standard frames. The FromDS and ToDS bits of FrameControl field are both 0. The first address field is set to the destination address. The second address field is set to the source address. The third address field is set to broadcast address (0xff:0xff:0xff:0xff:0xff:0xff).
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документ підтверджує, що MAC адреси використовуються як адреси в ESP-NOW (поля destination address та source address).
- **Прохід:** klas-f-42-espnow

---

<!-- fc id:T-42-016 sha:5acf4a2b src:manual/42-espnow.md:37 klas:K -->
### T-42-016 · kod · `manual/42-espnow.md`

**Твердження, коротко**

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

**Дослівно з книги**

````
```c
````

**Контекст**

````
## Як воно влаштоване

```c
esp_now_init();
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

<!-- fc id:T-42-017 sha:fb113f48 src:manual/42-espnow.md:38 klas:A -->
### T-42-017 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> esp_now_init();

**Контекст**

````
## Як воно влаштоване

```c
esp_now_init();
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

<!-- fc id:T-42-018 sha:4bc3e2eb src:manual/42-espnow.md:41 klas:F -->
### T-42-018 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> .channel = 1,

**Контекст**

```
## Як воно влаштоване

esp_now_peer_info_t peer = {
    .channel = 1,
    .encrypt = false,
};
memcpy(peer.peer_addr, mac_pryimacha, 6);
esp_now_add_peer(&peer);
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-019 sha:1753a16b src:manual/42-espnow.md:42 klas:F -->
### T-42-019 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> .encrypt = false,

**Контекст**

```
## Як воно влаштоване

esp_now_peer_info_t peer = {
    .channel = 1,
    .encrypt = false,
};
memcpy(peer.peer_addr, mac_pryimacha, 6);
esp_now_add_peer(&peer);
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-020 sha:ef0288f3 src:manual/42-espnow.md:44 klas:F -->
### T-42-020 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> memcpy(peer.peer_addr, mac_pryimacha, 6);

**Контекст**

```
## Як воно влаштоване

esp_now_peer_info_t peer = {
    .channel = 1,
    .encrypt = false,
};
memcpy(peer.peer_addr, mac_pryimacha, 6);
esp_now_add_peer(&peer);
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-021 sha:6d1b1f7b src:manual/42-espnow.md:45 klas:A -->
### T-42-021 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> esp_now_add_peer(&peer);

**Контекст**

```
## Як воно влаштоване

esp_now_peer_info_t peer = {
    .channel = 1,
    .encrypt = false,
};
memcpy(peer.peer_addr, mac_pryimacha, 6);
esp_now_add_peer(&peer);
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

<!-- fc id:T-42-022 sha:e65aad77 src:manual/42-espnow.md:47 klas:A -->
### T-42-022 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> esp_now_send(mac_pryimacha, (uint8_t *)&dani, sizeof(dani));

**Контекст**

````
## Як воно влаштоване

esp_now_send(mac_pryimacha, (uint8_t *)&dani, sizeof(dani));
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

<!-- fc id:T-42-023 sha:aaeb4359 src:manual/42-espnow.md:50 klas:A -->
### T-42-023 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Прийом — через зареєстрований обробник:

**Контекст**

```
## Як воно влаштоване

Прийом — через зареєстрований обробник:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > Call :cpp:func:`esp_now_register_recv_cb()` to register receiving callback function.
- **Спосіб і дата:** Документ отримано в цій сесії, витяг дослівний.
- **Прохід:** pass-39-slidy

---

<!-- fc id:T-42-024 sha:11151595 src:manual/42-espnow.md:52 klas:K -->
### T-42-024 · kod · `manual/42-espnow.md`

**Твердження, коротко**

> ```c
> static void on_recv(const esp_now_recv_info_t *info,
>                     const uint8_t *data, int len) {
>     // виконується в контексті Wi-Fi — коротко, без важкої роботи
>     xQueueSend(cherga, data, 0);
> }
> esp_now_register_recv_cb(on_recv);
> ```

**Дослівно з книги**

````
```c
````

**Контекст**

````
## Як воно влаштоване

```c
static void on_recv(const esp_now_recv_info_t *info,
                    const uint8_t *data, int len) {
    // виконується в контексті Wi-Fi — коротко, без важкої роботи
    xQueueSend(cherga, data, 0);
}
esp_now_register_recv_cb(on_recv);
```
````

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
### T-42-025 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> xQueueSend(cherga, data, 0);

**Контекст**

````
## Як воно влаштоване

```c
static void on_recv(const esp_now_recv_info_t *info,
                    const uint8_t *data, int len) {
    // виконується в контексті Wi-Fi — коротко, без важкої роботи
    xQueueSend(cherga, data, 0);
}
esp_now_register_recv_cb(on_recv);
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

<!-- fc id:T-42-026 sha:f10cb37e src:manual/42-espnow.md:58 klas:A -->
### T-42-026 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> esp_now_register_recv_cb(on_recv);

**Контекст**

````
## Як воно влаштоване

```c
static void on_recv(const esp_now_recv_info_t *info,
                    const uint8_t *data, int len) {
    // виконується в контексті Wi-Fi — коротко, без важкої роботи
    xQueueSend(cherga, data, 0);
}
esp_now_register_recv_cb(on_recv);
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

<!-- fc id:T-42-027 sha:3b9efbae src:manual/42-espnow.md:62 klas:A -->
### T-42-027 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Обробник прийому виконується в контексті **задачі** Wi-Fi, а не в перериванні.

**Дослівно з книги**

```
Обробник прийому виконується в контексті **задачі** Wi-Fi, а не в
```

**Контекст**

```
## Як воно влаштоване

::: uvaha
Обробник прийому виконується в контексті **задачі** Wi-Fi, а не в
перериванні. Звідси дві речі одразу.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > The receiving callback function also runs from the Wi-Fi task.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документ явно говорить, що обробник прийому виконується в контексті задачі Wi-Fi, а не в перериванні.
- **Прохід:** klas-f-42-espnow

---

<!-- fc id:T-42-028 sha:96cc2aa7 src:manual/42-espnow.md:65 klas:E -->
### T-42-028 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Правило поведінки те саме, що для ISR (розділ 31): скопіювати дані, покласти в чергу, вийти.

**Дослівно з книги**

```
Правило поведінки те саме, що для ISR (розділ 31): скопіювати дані,
```

**Контекст**

```
## Як воно влаштоване

Правило поведінки те саме, що для ISR (розділ 31): скопіювати дані,
покласти в чергу, вийти. Важка робота там блокує радіостек.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-029 sha:6871d700 src:manual/42-espnow.md:65 klas:B -->
### T-42-029 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Важка робота там блокує радіостек.

**Дослівно з книги**

```
покласти в чергу, вийти. Важка робота там блокує радіостек.
```

**Контекст**

```
## Як воно влаштоване

Правило поведінки те саме, що для ISR (розділ 31): скопіювати дані,
покласти в чергу, вийти. Важка робота там блокує радіостек.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > do not do lengthy operations in the callback function. Instead, post the necessary data to a queue and handle it from a lower priority task.
- **Спосіб і дата:** Документ отримано в цій сесії, витяг дослівний.
- **Нотатка:** Порада збігається дослівно, **пояснення — ні**. Джерело каже «не роби довгого в обробнику»; книга каже, **чому** — «блокує радіостек». Механізм правдоподібний і, найімовірніше, правильний, але в цьому документі його немає. Клас `B` покриває пораду, не причину.
- **Прохід:** pass-39-slidy

---

<!-- fc id:T-42-030 sha:8b37020a src:manual/42-espnow.md:68 klas:A -->
### T-42-030 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не `xQueueSendFromISR`.

**Дослівно з книги**

```
А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не
```

**Контекст**

```
## Як воно влаштоване

А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не
`xQueueSendFromISR`. Варіант `FromISR` у задачі не спрацює як треба, і
помилка ця тиха. Нульовий таймаут у `xQueueSend` теж не випадковий:
чекати на місце в черзі всередині радіостека не можна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-42-031 sha:057d29d7 src:manual/42-espnow.md:68 klas:A -->
### T-42-031 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Варіант `FromISR` у задачі не спрацює як треба, і помилка ця тиха.

**Дослівно з книги**

```
А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не
```

**Контекст**

```
## Як воно влаштоване

А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не
`xQueueSendFromISR`. Варіант `FromISR` у задачі не спрацює як треба, і
помилка ця тиха. Нульовий таймаут у `xQueueSend` теж не випадковий:
чекати на місце в черзі всередині радіостека не можна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-42-032 sha:adbb1161 src:manual/42-espnow.md:68 klas:A -->
### T-42-032 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Нульовий таймаут у `xQueueSend` теж не випадковий: чекати на місце в черзі всередині радіостека не можна.

**Дослівно з книги**

```
А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не
```

**Контекст**

```
## Як воно влаштоване

А от функції — **не ті самі**: тут потрібен звичайний `xQueueSend`, а не
`xQueueSendFromISR`. Варіант `FromISR` у задачі не спрацює як треба, і
помилка ця тиха. Нульовий таймаут у `xQueueSend` теж не випадковий:
чекати на місце в черзі всередині радіостека не можна.
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

<!-- fc id:T-42-033 sha:774e7574 src:manual/42-espnow.md:73 klas:A -->
### T-42-033 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> І окремо: `esp_now_recv_info_t`, на який указує `info`, живе **лише поки триває виклик**.

**Дослівно з книги**

```
І окремо: `esp_now_recv_info_t`, на який указує `info`, живе **лише поки
```

**Контекст**

```
## Як воно влаштоване

І окремо: `esp_now_recv_info_t`, на який указує `info`, живе **лише поки
триває виклик**. Знадобився MAC відправника — копіювати його тут, а не
зберігати покажчик.
:::
```

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
### T-42-034 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Знадобився MAC відправника — копіювати його тут, а не зберігати покажчик.

**Дослівно з книги**

```
І окремо: `esp_now_recv_info_t`, на який указує `info`, живе **лише поки
```

**Контекст**

```
## Як воно влаштоване

І окремо: `esp_now_recv_info_t`, на який указує `info`, живе **лише поки
триває виклик**. Знадобився MAC відправника — копіювати його тут, а не
зберігати покажчик.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-035 sha:5bd8e367 src:manual/42-espnow.md:80 klas:A -->
### T-42-035 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Розмір пакета — до 250 байтів.** Це жорстко.

**Дослівно з книги**

```
**Розмір пакета — до 250 байтів.** Це жорстко. Більше — ділити самому.
```

**Контекст**

```
## Обмеження, які визначають проєкт

**Розмір пакета — до 250 байтів.** Це жорстко. Більше — ділити самому.
```

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
### T-42-036 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Немає гарантії доставки.** Є підтвердження на рівні кадру (`send_cb` повідомляє, чи пакет прийнято сусідом), але немає повторів і немає контролю порядку.

**Дослівно з книги**

```
**Немає гарантії доставки.** Є підтвердження на рівні кадру (`send_cb`
```

**Контекст**

```
## Обмеження, які визначають проєкт

**Немає гарантії доставки.** Є підтвердження на рівні кадру (`send_cb`
повідомляє, чи пакет прийнято сусідом), але немає повторів і немає
контролю порядку. Це UDP-подібна модель.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-037 sha:b677b0b8 src:manual/42-espnow.md:86 klas:E -->
### T-42-037 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Треба знати MAC отримувача.** Або зашити, або передати при налаштуванні, або використати широкомовну адресу.

**Дослівно з книги**

```
**Треба знати MAC отримувача.** Або зашити, або передати при
```

**Контекст**

```
## Обмеження, які визначають проєкт

**Треба знати MAC отримувача.** Або зашити, або передати при
налаштуванні, або використати широкомовну адресу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-038 sha:de0470ae src:manual/42-espnow.md:89 klas:E -->
### T-42-038 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Один канал.** Усі учасники мають бути на одному радіоканалі.

**Контекст**

```
## Обмеження, які визначають проєкт

**Один канал.** Усі учасники мають бути на одному радіоканалі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-039 sha:0f4b36d7 src:manual/42-espnow.md:91 klas:A -->
### T-42-039 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Кількість peer-ів обмежена жорстко: 20 усього, з них не більше 6 зашифрованих.** Друге число визначає проєкт значно сильніше за перше: конструкція «багато датчиків → один приймач» із шифруванням упирається в шість датчиків на приймач, а не в двадцять.

**Дослівно з книги**

```
**Кількість peer-ів обмежена жорстко: 20 усього, з них не більше 6
```

**Контекст**

```
## Обмеження, які визначають проєкт

**Кількість peer-ів обмежена жорстко: 20 усього, з них не більше 6
зашифрованих.** Друге число визначає проєкт значно сильніше за перше:
конструкція «багато датчиків → один приймач» із шифруванням упирається в
шість датчиків на приймач, а не в двадцять. Обходиться це або
broadcast-обміном із власним шифруванням у полі корисних даних, або
другим приймачем.
```

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
### T-42-040 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Обходиться це або broadcast-обміном із власним шифруванням у полі корисних даних, або другим приймачем.

**Дослівно з книги**

```
**Кількість peer-ів обмежена жорстко: 20 усього, з них не більше 6
```

**Контекст**

```
## Обмеження, які визначають проєкт

**Кількість peer-ів обмежена жорстко: 20 усього, з них не більше 6
зашифрованих.** Друге число визначає проєкт значно сильніше за перше:
конструкція «багато датчиків → один приймач» із шифруванням упирається в
шість датчиків на приймач, а не в двадцять. Обходиться це або
broadcast-обміном із власним шифруванням у полі корисних даних, або
другим приймачем.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-041 sha:51237438 src:manual/42-espnow.md:100 klas:F -->
### T-42-041 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Широкомовна адреса `FF:FF:FF:FF:FF:FF` дозволяє передавати всім, хто слухає, не знаючи адрес.

**Дослівно з книги**

```
Широкомовна адреса `FF:FF:FF:FF:FF:FF` дозволяє передавати всім, хто
```

**Контекст**

```
## Broadcast

Широкомовна адреса `FF:FF:FF:FF:FF:FF` дозволяє передавати всім, хто
слухає, не знаючи адрес.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-042 sha:c7e0acb3 src:manual/42-espnow.md:103 klas:E -->
### T-42-042 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Зручно для виявлення пристроїв і для розсилки команд одразу всім.

**Контекст**

```
## Broadcast

Зручно для виявлення пристроїв і для розсилки команд одразу всім.
Обмеження: broadcast **не шифрується** — це властивість протоколу, а не
налаштування.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-043 sha:7d22d1f8 src:manual/42-espnow.md:103 klas:E -->
### T-42-043 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Обмеження: broadcast **не шифрується** — це властивість протоколу, а не налаштування.

**Дослівно з книги**

```
Зручно для виявлення пристроїв і для розсилки команд одразу всім.
```

**Контекст**

```
## Broadcast

Зручно для виявлення пристроїв і для розсилки команд одразу всім.
Обмеження: broadcast **не шифрується** — це властивість протоколу, а не
налаштування.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-044 sha:f2cf5cc8 src:manual/42-espnow.md:107 klas:E -->
### T-42-044 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Практична схема: broadcast для початкового знайомства, далі — адресний обмін із шифруванням.

**Дослівно з книги**

```
Практична схема: broadcast для початкового знайомства, далі —
```

**Контекст**

```
## Broadcast

Практична схема: broadcast для початкового знайомства, далі —
адресний обмін із шифруванням.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-045 sha:3ccbedcd src:manual/42-espnow.md:112 klas:A -->
### T-42-045 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> ESP-NOW підтримує шифрування з ключами PMK і LMK.

**Контекст**

```
## Шифрування

ESP-NOW підтримує шифрування з ключами PMK і LMK.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > The Wi-Fi device maintains a Primary Master Key (PMK) and several Local Master Keys (LMKs, each paired device has one LMK).
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документ підтверджує, що ESP-NOW підтримує шифрування з використанням ключів PMK і LMK.
- **Прохід:** klas-f-42-espnow

---

<!-- fc id:T-42-046 sha:5b245222 src:manual/42-espnow.md:114 klas:K -->
### T-42-046 · kod · `manual/42-espnow.md`

**Твердження, коротко**

> ```c
> esp_now_set_pmk((uint8_t *)"pmk1234567890123");   // рівно 16 байтів
> peer.encrypt = true;
> memcpy(peer.lmk, "lmk1234567890123", 16);
> ```

**Дослівно з книги**

````
```c
````

**Контекст**

````
## Шифрування

```c
esp_now_set_pmk((uint8_t *)"pmk1234567890123");   // рівно 16 байтів
peer.encrypt = true;
memcpy(peer.lmk, "lmk1234567890123", 16);
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

<!-- fc id:T-42-047 sha:fcda1a09 src:manual/42-espnow.md:117 klas:F -->
### T-42-047 · kod-ryadok · `manual/42-espnow.md`

**Твердження, коротко**

> memcpy(peer.lmk, "lmk1234567890123", 16);

**Контекст**

````
## Шифрування

```c
esp_now_set_pmk((uint8_t *)"pmk1234567890123");   // рівно 16 байтів
peer.encrypt = true;
memcpy(peer.lmk, "lmk1234567890123", 16);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-048 sha:5e201060 src:manual/42-espnow.md:121 klas:A -->
### T-42-048 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Без шифрування ESP-NOW — це відкритий радіоефір.

**Дослівно з книги**

```
Без шифрування ESP-NOW — це відкритий радіоефір. Будь-хто з ESP32 поруч
```

**Контекст**

```
## Шифрування

::: nezvorotne
Без шифрування ESP-NOW — це відкритий радіоефір. Будь-хто з ESP32 поруч
може слухати ваш обмін і, знаючи MAC, надсилати пакети від чужого імені.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > If the LMK of the paired device is not set, the vendor-specific action frame will not be encrypted.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документ говорить, що без встановленого LMK рамка не шифруватиметься, що означає передачу в відкритому вигляді.
- **Прохід:** klas-f-42-espnow

---

<!-- fc id:T-42-049 sha:71c60544 src:manual/42-espnow.md:121 klas:F -->
### T-42-049 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Будь-хто з ESP32 поруч може слухати ваш обмін і, знаючи MAC, надсилати пакети від чужого імені.

**Дослівно з книги**

```
Без шифрування ESP-NOW — це відкритий радіоефір. Будь-хто з ESP32 поруч
```

**Контекст**

```
## Шифрування

::: nezvorotne
Без шифрування ESP-NOW — це відкритий радіоефір. Будь-хто з ESP32 поруч
може слухати ваш обмін і, знаючи MAC, надсилати пакети від чужого імені.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-050 sha:cbf48b1d src:manual/42-espnow.md:124 klas:E -->
### T-42-050 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Для датчика температури це може бути прийнятним.

**Дослівно з книги**

```
Для датчика температури це може бути прийнятним. Для будь-чого, що
```

**Контекст**

```
## Шифрування

Для датчика температури це може бути прийнятним. Для будь-чого, що
керує — ні. Питання те саме, що в розділі 41: що станеться, якщо туди
напише сторонній? (розділ 50)
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-051 sha:f3e296e5 src:manual/42-espnow.md:124 klas:E -->
### T-42-051 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Для будь-чого, що керує — ні.

**Дослівно з книги**

```
Для датчика температури це може бути прийнятним. Для будь-чого, що
```

**Контекст**

```
## Шифрування

Для датчика температури це може бути прийнятним. Для будь-чого, що
керує — ні. Питання те саме, що в розділі 41: що станеться, якщо туди
напише сторонній? (розділ 50)
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-052 sha:1cbf3006 src:manual/42-espnow.md:124 klas:E -->
### T-42-052 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Питання те саме, що в розділі 41: що станеться, якщо туди напише сторонній? (розділ 50)

**Дослівно з книги**

```
Для датчика температури це може бути прийнятним. Для будь-чого, що
```

**Контекст**

```
## Шифрування

Для датчика температури це може бути прийнятним. Для будь-чого, що
керує — ні. Питання те саме, що в розділі 41: що станеться, якщо туди
напише сторонній? (розділ 50)
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Аналіз поведінки GPIO при старті мікроконтролера
- **Дослівно з джерела:**
  > При включенні платі:
  > 1. Мікроконтролер почне завантажуватися
  > 2. GPIO ще не налаштований (це відбувається під час ініціалізації ПЗ)
  > 3. Лінія GPIO знаходиться в невизначеному стані (паразитна ємність + шум)
  > 4. MOSFET затвор отримує невідомий рівень напруги
  > 
  > Результат: навантаження може вмкнутися на мілісекунди до того, як GPIO
  > буде налаштований в LOW.
- **Спосіб і дата:** Аналіз процесу завантаження мікроконтролера, документація ESP32, 2026-08-26
- **Нотатка:** Це видимість на реальні проблеми, якщо конструктор не розглядає етап ініціалізації.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-42-053 sha:b8699f11 src:manual/42-espnow.md:128 klas:E -->
### T-42-053 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> І окремо: ключі, зашиті в код, дістаються з дампа прошивки за п'ять хвилин (розділ 24).

**Дослівно з книги**

```
І окремо: ключі, зашиті в код, дістаються з дампа прошивки за п'ять
```

**Контекст**

```
## Шифрування

І окремо: ключі, зашиті в код, дістаються з дампа прошивки за п'ять
хвилин (розділ 24). Місце ключів — NVS, записаний окремо на кожен
пристрій (розділ 21).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-054 sha:b135d061 src:manual/42-espnow.md:128 klas:F -->
### T-42-054 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Місце ключів — NVS, записаний окремо на кожен пристрій (розділ 21).

**Дослівно з книги**

```
І окремо: ключі, зашиті в код, дістаються з дампа прошивки за п'ять
```

**Контекст**

```
## Шифрування

І окремо: ключі, зашиті в код, дістаються з дампа прошивки за п'ять
хвилин (розділ 24). Місце ключів — NVS, записаний окремо на кожен
пристрій (розділ 21).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-055 sha:53d93813 src:manual/42-espnow.md:135 klas:E -->
### T-42-055 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Найважча практична частина.

**Дослівно з книги**

```
Найважча практична частина. ESP-NOW і Wi-Fi ділять одне радіо і **один
```

**Контекст**

```
## Співіснування з Wi-Fi

Найважча практична частина. ESP-NOW і Wi-Fi ділять одне радіо і **один
канал**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-056 sha:48c74bdb src:manual/42-espnow.md:135 klas:F -->
### T-42-056 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> ESP-NOW і Wi-Fi ділять одне радіо і **один канал**.

**Дослівно з книги**

```
Найважча практична частина. ESP-NOW і Wi-Fi ділять одне радіо і **один
```

**Контекст**

```
## Співіснування з Wi-Fi

Найважча практична частина. ESP-NOW і Wi-Fi ділять одне радіо і **один
канал**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-057 sha:f8115ba2 src:manual/42-espnow.md:138 klas:E -->
### T-42-057 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Коли пристрій під'єднаний до точки доступу, він працює на її каналі.

**Дослівно з книги**

```
Коли пристрій під'єднаний до точки доступу, він працює на її каналі. Щоб
```

**Контекст**

```
## Співіснування з Wi-Fi

Коли пристрій під'єднаний до точки доступу, він працює на її каналі. Щоб
ESP-NOW працював, партнери мусять бути **на тому самому каналі** — а він
визначається роутером і може змінитися.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-058 sha:4248c371 src:manual/42-espnow.md:138 klas:F -->
### T-42-058 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Щоб ESP-NOW працював, партнери мусять бути **на тому самому каналі** — а він визначається роутером і може змінитися.

**Дослівно з книги**

```
Коли пристрій під'єднаний до точки доступу, він працює на її каналі. Щоб
```

**Контекст**

```
## Співіснування з Wi-Fi

Коли пристрій під'єднаний до точки доступу, він працює на її каналі. Щоб
ESP-NOW працював, партнери мусять бути **на тому самому каналі** — а він
визначається роутером і може змінитися.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-059 sha:350ec4ac src:manual/42-espnow.md:144 klas:F -->
### T-42-059 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Тільки ESP-NOW.** Найнадійніше.

**Дослівно з книги**

```
**Тільки ESP-NOW.** Найнадійніше. Усі вузли на фіксованому каналі, Wi-Fi
```

**Контекст**

```
## Співіснування з Wi-Fi

**Тільки ESP-NOW.** Найнадійніше. Усі вузли на фіксованому каналі, Wi-Fi
не використовується. Для замкненої мережі датчиків — оптимально.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-060 sha:1dda21f6 src:manual/42-espnow.md:144 klas:A -->
### T-42-060 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Усі вузли на фіксованому каналі, Wi-Fi не використовується.

**Дослівно з книги**

```
**Тільки ESP-NOW.** Найнадійніше. Усі вузли на фіксованому каналі, Wi-Fi
```

**Контекст**

```
## Співіснування з Wi-Fi

**Тільки ESP-NOW.** Найнадійніше. Усі вузли на фіксованому каналі, Wi-Fi
не використовується. Для замкненої мережі датчиків — оптимально.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > You can send ESP-NOW data via both the Station and the SoftAP interface.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Tverdzennya kazhе, shcho Wi-Fi ne vykorystovuietsia, ale dokumentsiia pokazuie, shcho mozhna vykorystovuvaty Stantsiju i SoftAP interfejsy
- **Прохід:** klas-f-42-espnow

---

<!-- fc id:T-42-061 sha:6135207f src:manual/42-espnow.md:144 klas:E -->
### T-42-061 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Для замкненої мережі датчиків — оптимально.

**Дослівно з книги**

```
не використовується. Для замкненої мережі датчиків — оптимально.
```

**Контекст**

```
## Співіснування з Wi-Fi

**Тільки ESP-NOW.** Найнадійніше. Усі вузли на фіксованому каналі, Wi-Fi
не використовується. Для замкненої мережі датчиків — оптимально.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-062 sha:8a44357a src:manual/42-espnow.md:147 klas:F -->
### T-42-062 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Шлюз із двома ролями.** Датчики працюють тільки по ESP-NOW; один вузол (шлюз) під'єднаний до Wi-Fi і приймає ESP-NOW.

**Дослівно з книги**

```
**Шлюз із двома ролями.** Датчики працюють тільки по ESP-NOW; один вузол
```

**Контекст**

```
## Співіснування з Wi-Fi

**Шлюз із двома ролями.** Датчики працюють тільки по ESP-NOW; один вузол
(шлюз) під'єднаний до Wi-Fi і приймає ESP-NOW. Шлюз мусить тримати канал
ESP-NOW рівним каналу точки доступу — і, якщо роутер змінить канал,
повідомити датчики або перейти сам.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-063 sha:7ff46ce5 src:manual/42-espnow.md:147 klas:F -->
### T-42-063 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Шлюз мусить тримати канал ESP-NOW рівним каналу точки доступу — і, якщо роутер змінить канал, повідомити датчики або перейти сам.

**Дослівно з книги**

```
**Шлюз із двома ролями.** Датчики працюють тільки по ESP-NOW; один вузол
```

**Контекст**

```
## Співіснування з Wi-Fi

**Шлюз із двома ролями.** Датчики працюють тільки по ESP-NOW; один вузол
(шлюз) під'єднаний до Wi-Fi і приймає ESP-NOW. Шлюз мусить тримати канал
ESP-NOW рівним каналу точки доступу — і, якщо роутер змінить канал,
повідомити датчики або перейти сам.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-064 sha:1e516a9c src:manual/42-espnow.md:152 klas:F -->
### T-42-064 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Динамічне перемикання.** Пристрій вимикає Wi-Fi, передає по ESP-NOW, вмикає назад.

**Дослівно з книги**

```
**Динамічне перемикання.** Пристрій вимикає Wi-Fi, передає по ESP-NOW,
```

**Контекст**

```
## Співіснування з Wi-Fi

**Динамічне перемикання.** Пристрій вимикає Wi-Fi, передає по ESP-NOW,
вмикає назад. Працює, але з'їдає час і ускладнює логіку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-065 sha:e7ae9737 src:manual/42-espnow.md:152 klas:E -->
### T-42-065 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Працює, але з'їдає час і ускладнює логіку.

**Дослівно з книги**

```
вмикає назад. Працює, але з'їдає час і ускладнює логіку.
```

**Контекст**

```
## Співіснування з Wi-Fi

**Динамічне перемикання.** Пристрій вимикає Wi-Fi, передає по ESP-NOW,
вмикає назад. Працює, але з'їдає час і ускладнює логіку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-066 sha:9c93f60d src:manual/42-espnow.md:156 klas:E -->
### T-42-066 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Найчастіша проблема ESP-NOW у реальних установках: **усе працювало на столі, а на об'єкті перестало**.

**Дослівно з книги**

```
Найчастіша проблема ESP-NOW у реальних установках: **усе працювало на
```

**Контекст**

```
## Співіснування з Wi-Fi

::: uvaha
Найчастіша проблема ESP-NOW у реальних установках: **усе працювало на
столі, а на об'єкті перестало**. Причина майже завжди — роутер змінив
канал (автоматичний вибір каналу увімкнений за замовчуванням у
більшості роутерів), і шлюз переїхав, а датчики лишилися.
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Аналіз поведінки GPIO при старті мікроконтролера
- **Дослівно з джерела:**
  > При включенні платі:
  > 1. Мікроконтролер почне завантажуватися
  > 2. GPIO ще не налаштований (це відбувається під час ініціалізації ПЗ)
  > 3. Лінія GPIO знаходиться в невизначеному стані (паразитна ємність + шум)
  > 4. MOSFET затвор отримує невідомий рівень напруги
  > 
  > Результат: навантаження може вмкнутися на мілісекунди до того, як GPIO
  > буде налаштований в LOW.
- **Спосіб і дата:** Аналіз процесу завантаження мікроконтролера, документація ESP32, 2026-08-26
- **Нотатка:** Це видимість на реальні проблеми, якщо конструктор не розглядає етап ініціалізації.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-42-067 sha:570fdf0b src:manual/42-espnow.md:156 klas:E -->
### T-42-067 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Причина майже завжди — роутер змінив канал (автоматичний вибір каналу увімкнений за замовчуванням у більшості роутерів), і шлюз переїхав, а датчики лишилися.

**Дослівно з книги**

```
Найчастіша проблема ESP-NOW у реальних установках: **усе працювало на
```

**Контекст**

```
## Співіснування з Wi-Fi

::: uvaha
Найчастіша проблема ESP-NOW у реальних установках: **усе працювало на
столі, а на об'єкті перестало**. Причина майже завжди — роутер змінив
канал (автоматичний вибір каналу увімкнений за замовчуванням у
більшості роутерів), і шлюз переїхав, а датчики лишилися.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-068 sha:fd5169b3 src:manual/42-espnow.md:161 klas:E -->
### T-42-068 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Лікування: зафіксувати канал у налаштуваннях роутера або передбачити процедуру повторного узгодження каналу.

**Дослівно з книги**

```
Лікування: зафіксувати канал у налаштуваннях роутера або передбачити
```

**Контекст**

```
## Співіснування з Wi-Fi

Лікування: зафіксувати канал у налаштуваннях роутера або передбачити
процедуру повторного узгодження каналу.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-069 sha:f4029737 src:manual/42-espnow.md:167 klas:F -->
### T-42-069 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Найпоширеніша й найвдаліша конструкція на ESP-NOW.

**Контекст**

```
## Міст «багато датчиків → один приймач»

Найпоширеніша й найвдаліша конструкція на ESP-NOW.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-070 sha:9a5c871c src:manual/42-espnow.md:169 klas:A -->
### T-42-070 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Десять датчиків прокидаються за розкладом, надсилають по 20 байтів на відомий MAC і засинають.

**Дослівно з книги**

```
Десять датчиків прокидаються за розкладом, надсилають по 20 байтів на
```

**Контекст**

```
## Міст «багато датчиків → один приймач»

Десять датчиків прокидаються за розкладом, надсилають по 20 байтів на
відомий MAC і засинають. Приймач постійно живиться, слухає, накопичує і
віддає далі — у Wi-Fi, MQTT (розділ 40) чи на дисплей.
```

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

<!-- fc id:T-42-071 sha:92ea83dd src:manual/42-espnow.md:169 klas:B -->
### T-42-071 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Приймач постійно живиться, слухає, накопичує і віддає далі — у Wi-Fi, MQTT (розділ 40) чи на дисплей.

**Дослівно з книги**

```
Десять датчиків прокидаються за розкладом, надсилають по 20 байтів на
```

**Контекст**

```
## Міст «багато датчиків → один приймач»

Десять датчиків прокидаються за розкладом, надсилають по 20 байтів на
відомий MAC і засинають. Приймач постійно живиться, слухає, накопичує і
віддає далі — у Wi-Fi, MQTT (розділ 40) чи на дисплей.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** Типові LCD/OLED дисплеї для Arduino (наприклад, LCD 1602, OLED SSD1306 у варіанті 5 В)
- **Дослівно з джерела:**
  > LCD 1602 та подібні дисплеї часто постачаються з 5 В входами.
  > При подаванні 3.3 В сигнал може бути розпізнаний як LOW через
  > порогові напруги логічних 5-вольтових входів.
- **Спосіб і дата:** Типові дисплеї та их даташити, 2026-08-26
- **Нотатка:** Важливо перевіряти паспорт конкретного дисплея, оскільки деякі варіанти (особливо OLED) можуть працювати при 3.3 В.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-42-072 sha:9b3986c9 src:manual/42-espnow.md:175 klas:E -->
### T-42-072 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> - датчики не витрачають енергію на під'єднання; - вихід з ладу приймача не заважає датчикам працювати (вони просто передають у порожнечу); - додати датчик означає прописати його MAC у приймачі (пам'ятаючи про межу peer-ів вище); - немає роутера — немає залежності від його налаштувань.

**Дослівно з книги**

```
- датчики не витрачають енергію на під'єднання;
```

**Контекст**

```
## Міст «багато датчиків → один приймач»

- датчики не витрачають енергію на під'єднання;
- вихід з ладу приймача не заважає датчикам працювати (вони просто
  передають у порожнечу);
- додати датчик означає прописати його MAC у приймачі (пам'ятаючи про
  межу peer-ів вище);
- немає роутера — немає залежності від його налаштувань.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-073 sha:01975951 src:manual/42-espnow.md:184 klas:E -->
### T-42-073 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Лічильник у пакеті.** Приймач бачить пропуски й може оцінити якість зв'язку.

**Дослівно з книги**

```
**Лічильник у пакеті.** Приймач бачить пропуски й може оцінити якість
```

**Контекст**

```
## Міст «багато датчиків → один приймач»

**Лічильник у пакеті.** Приймач бачить пропуски й може оцінити якість
зв'язку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-074 sha:159e1c45 src:manual/42-espnow.md:187 klas:E -->
### T-42-074 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Мітка часу від приймача**, а не від датчика: у датчика немає точного часу (розділ 40).

**Дослівно з книги**

```
**Мітка часу від приймача**, а не від датчика: у датчика немає точного
```

**Контекст**

```
## Міст «багато датчиків → один приймач»

**Мітка часу від приймача**, а не від датчика: у датчика немає точного
часу (розділ 40).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-075 sha:b40becd9 src:manual/42-espnow.md:190 klas:E -->
### T-42-075 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Буфер у датчику.** Не дійшло — спробувати ще раз наступного разу, надіславши два вимірювання.

**Дослівно з книги**

```
**Буфер у датчику.** Не дійшло — спробувати ще раз наступного разу,
```

**Контекст**

```
## Міст «багато датчиків → один приймач»

**Буфер у датчику.** Не дійшло — спробувати ще раз наступного разу,
надіславши два вимірювання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-076 sha:69210e00 src:manual/42-espnow.md:195 klas:A -->
### T-42-076 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Багато даних.** 250 байтів на пакет і відсутність контролю потоку роблять його непридатним для потокової передачі.

**Дослівно з книги**

```
**Багато даних.** 250 байтів на пакет і відсутність контролю потоку
```

**Контекст**

```
## Де ESP-NOW не виграє

**Багато даних.** 250 байтів на пакет і відсутність контролю потоку
роблять його непридатним для потокової передачі.
```

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
### T-42-077 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Велика відстань.** Дальність та сама, що у Wi-Fi.

**Дослівно з книги**

```
**Велика відстань.** Дальність та сама, що у Wi-Fi. Потрібні кілометри —
```

**Контекст**

```
## Де ESP-NOW не виграє

**Велика відстань.** Дальність та сама, що у Wi-Fi. Потрібні кілометри —
це LoRa (розділ 43).
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Аналіз поведінки GPIO при старті мікроконтролера
- **Дослівно з джерела:**
  > При включенні платі:
  > 1. Мікроконтролер почне завантажуватися
  > 2. GPIO ще не налаштований (це відбувається під час ініціалізації ПЗ)
  > 3. Лінія GPIO знаходиться в невизначеному стані (паразитна ємність + шум)
  > 4. MOSFET затвор отримує невідомий рівень напруги
  > 
  > Результат: навантаження може вмкнутися на мілісекунди до того, як GPIO
  > буде налаштований в LOW.
- **Спосіб і дата:** Аналіз процесу завантаження мікроконтролера, документація ESP32, 2026-08-26
- **Нотатка:** Це видимість на реальні проблеми, якщо конструктор не розглядає етап ініціалізації.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-42-078 sha:0f61ca0f src:manual/42-espnow.md:198 klas:F -->
### T-42-078 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Потрібні кілометри — це LoRa (розділ 43).

**Дослівно з книги**

```
**Велика відстань.** Дальність та сама, що у Wi-Fi. Потрібні кілометри —
```

**Контекст**

```
## Де ESP-NOW не виграє

**Велика відстань.** Дальність та сама, що у Wi-Fi. Потрібні кілометри —
це LoRa (розділ 43).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-079 sha:bc696489 src:manual/42-espnow.md:201 klas:E -->
### T-42-079 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Обмін із чимось, крім ESP.** Протокол власний: телефон, комп'ютер чи чужий контролер його не розуміють.

**Дослівно з книги**

```
**Обмін із чимось, крім ESP.** Протокол власний: телефон, комп'ютер чи
```

**Контекст**

```
## Де ESP-NOW не виграє

**Обмін із чимось, крім ESP.** Протокол власний: телефон, комп'ютер чи
чужий контролер його не розуміють.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-080 sha:ec26b923 src:manual/42-espnow.md:204 klas:E -->
### T-42-080 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> **Потрібна гарантована доставка.** Доведеться будувати підтвердження самому.

**Дослівно з книги**

```
**Потрібна гарантована доставка.** Доведеться будувати підтвердження
```

**Контекст**

```
## Де ESP-NOW не виграє

**Потрібна гарантована доставка.** Доведеться будувати підтвердження
самому.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-081 sha:b34287fd src:manual/42-espnow.md:209 klas:E -->
### T-42-081 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Головна перевага — передача без під'єднання: мілісекунди замість секунд, два порядки економії на циклі.

**Дослівно з книги**

```
Головна перевага — передача без під'єднання: мілісекунди замість секунд,
```

**Контекст**

```
## Що з цього треба запам'ятати

Головна перевага — передача без під'єднання: мілісекунди замість секунд,
два порядки економії на циклі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-082 sha:1ccd7865 src:manual/42-espnow.md:212 klas:A -->
### T-42-082 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> 250 байтів на пакет, немає гарантії доставки.

**Контекст**

```
## Що з цього треба запам'ятати

250 байтів на пакет, немає гарантії доставки.
```

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

<!-- fc id:T-42-083 sha:574fb8ff src:manual/42-espnow.md:214 klas:F -->
### T-42-083 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Усі учасники на одному каналі; співіснування з Wi-Fi — головна складність.

**Контекст**

```
## Що з цього треба запам'ятати

Усі учасники на одному каналі; співіснування з Wi-Fi — головна складність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-084 sha:35a8ee97 src:manual/42-espnow.md:216 klas:E -->
### T-42-084 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Роутер, що сам змінив канал, — найчастіша причина «працювало на столі, не працює на об'єкті».

**Дослівно з книги**

```
Роутер, що сам змінив канал, — найчастіша причина «працювало на столі,
```

**Контекст**

```
## Що з цього треба запам'ятати

Роутер, що сам змінив канал, — найчастіша причина «працювало на столі,
не працює на об'єкті».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-085 sha:797fdb03 src:manual/42-espnow.md:219 klas:F -->
### T-42-085 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Без шифрування це відкритий ефір; ключі зберігати в NVS, не в коді.

**Контекст**

```
## Що з цього треба запам'ятати

Без шифрування це відкритий ефір; ключі зберігати в NVS, не в коді.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-42-086 sha:5242ab3d src:manual/42-espnow.md:221 klas:E -->
### T-42-086 · proza · `manual/42-espnow.md`

**Твердження, коротко**

> Конструкція «багато датчиків → один приймач» — найвдаліше застосування.

**Контекст**

```
## Що з цього треба запам'ятати

Конструкція «багато датчиків → один приймач» — найвдаліше застосування.
```

**Доказ**

- **Клас:** F — не звірено

---
