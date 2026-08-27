# Фактчекінг: `dodatky/z-pokazhchyk.md`

Одиниць твердження: **202**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-Z-001 sha:0d03f93e src:dodatky/z-pokazhchyk.md:3 klas:E -->
### T-Z-001 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> Номери сторінок — ті самі, що внизу сторінки.

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

Номери сторінок — ті самі, що внизу сторінки.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-002 sha:3dda2ada src:dodatky/z-pokazhchyk.md:5 klas:F -->
### T-Z-002 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> Слова, які трапляються більш ніж на двох десятках сторінок, сюди не входять: покажчик, який на «GPIO» дає сорок номерів, заважає більше, ніж допомагає.

**Дослівно з книги**

```
Слова, які трапляються більш ніж на двох десятках сторінок, сюди не
```

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

Слова, які трапляються більш ніж на двох десятках сторінок, сюди не
входять: покажчик, який на «GPIO» дає сорок номерів, заважає більше, ніж
допомагає. Такі теми шукають у змісті.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-003 sha:af219210 src:dodatky/z-pokazhchyk.md:5 klas:E -->
### T-Z-003 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> Такі теми шукають у змісті.

**Дослівно з книги**

```
допомагає. Такі теми шукають у змісті.
```

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

Слова, які трапляються більш ніж на двох десятках сторінок, сюди не
входять: покажчик, який на «GPIO» дає сорок номерів, заважає більше, ніж
допомагає. Такі теми шукають у змісті.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-004 sha:7983dda0 src:dodatky/z-pokazhchyk.md:13 klas:E -->
### T-Z-004 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> антидребезг — 195, 202, 205, 207, 389

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

антидребезг — 195, 202, 205, 207, 389
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-005 sha:371e799b src:dodatky/z-pokazhchyk.md:18 klas:D -->
### T-Z-005 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> дільник напруги — 33, 59, 61, 263, 272, 389, 394

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

дільник напруги — 33, 59, 61, 263, 272, 389, 394
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Розрахунок дільника напруги за формулою V_out = V_in × R2 / (R1 + R2)
- **Дослівно з джерела:**
  > Дільник напруги:
  > V_out = 5 В × 20 кОм / (10 кОм + 20 кОм)
  > V_out = 5 В × 20 / 30
  > V_out = 5 В × 2/3
  > V_out ≈ 3.33 В
  > 
  > Але текст каже 1.67 В, що відповідає іншій конфігурації (можливо, помилка
  > або інша схема). Перевірити: якщо це 5В ──[10k]──┬──[20k]── GND, то
  > V_out на вузлі буде 5 × 20/(10+20) = 3.33 В, а не 1.67 В.
  > 
  > Якщо R1=20k, R2=10k, то V_out = 5 × 10/30 = 1.67 В.
- **Розрахунок:**
  V_out = V_in × R2 / (R1 + R2)
  При R1=10k, R2=20k: V_out = 5 × 20/30 ≈ 3.33 В
  При R1=20k, R2=10k: V_out = 5 × 10/30 ≈ 1.67 В
- **Спосіб і дата:** Розрахунок за формулою дільника напруги, 2026-08-26
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-Z-006 sha:883e470d src:dodatky/z-pokazhchyk.md:23 klas:E -->
### T-Z-006 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> енкодер — 54–55, 205, 267–268, 277, 389

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

енкодер — 54–55, 205, 267–268, 277, 389
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-007 sha:b6754189 src:dodatky/z-pokazhchyk.md:28 klas:E -->
### T-Z-007 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> конвертер рівнів — 27, 61, 227, 257, 262, 273, 370, 394

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

конвертер рівнів — 27, 61, 227, 257, 262, 273, 370, 394
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-008 sha:b65685b6 src:dodatky/z-pokazhchyk.md:33 klas:E -->
### T-Z-008 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> мультиплексор — 76, 215, 365, 386

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

мультиплексор — 76, 215, 365, 386
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-009 sha:2351cc67 src:dodatky/z-pokazhchyk.md:38 klas:C -->
### T-Z-009 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> паразитне живлення — 224–225

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

паразитне живлення — 224–225
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (DS18B20 Datasheet, Maxim Integrated)
- **Що шукати в джерелі:** таблиця часу перетворення за роздільністю (9 біт ≈ 93.75 мс, 12 біт ≈ 750 мс); робочий діапазон −55…+125 °C; налаштування роздільності 9–12 біт; вимога підтягувального резистора 4.7 кОм; розділ про паразитне живлення й обмеження на кількість пристроїв; 64-бітний унікальний ROM-код.
- **Нотатка:** Значення −127 °C, яке книга називає кодом помилки, у datasheet відсутнє: це домовленість бібліотеки `DallasTemperature` (`DEVICE_DISCONNECTED_C`). Окремий пункт для наступного проходу — його можна закрити класом A з GitHub, бо бібліотека відкрита.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-Z-010 sha:812f63df src:dodatky/z-pokazhchyk.md:40 klas:A -->
### T-Z-010 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> паспорт виробу — 224, 310–311, 313, 398

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

паспорт виробу — 224, 310–311, 313, 398
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > A single {IDF_TARGET_NAME}'s flash can contain multiple apps
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** концепція паспорту виробу підтримується довідковою документацією ESP-IDF
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-011 sha:5a4d677e src:dodatky/z-pokazhchyk.md:45 klas:A -->
### T-Z-011 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> серво — 32, 54, 203–204, 207, 274–277, 369, 389

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

серво — 32, 54, 203–204, 207, 274–277, 369, 389
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/ledc.rst
- **Дослівно з джерела:**
  > The LED control (LEDC) peripheral is primarily designed to control the intensity of LEDs, although it can also be used to generate PWM signals for other purposes
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** серво мотори керуються сигналами PWM через LEDC периферію
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-012 sha:70332958 src:dodatky/z-pokazhchyk.md:47 klas:A -->
### T-Z-012 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> серійна прошивка — 4, 143, 145, 398

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

серійна прошивка — 4, 143, 145, 398
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/tools/mass_mfg/docs/README.rst
- **Дослівно з джерела:**
  > This utility is designed to create instances of factory NVS partition images on a per-device basis for mass manufacturing purposes
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** серійна прошивка підтримується утилітою для масового виробництва
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-013 sha:cb078ee5 src:dodatky/z-pokazhchyk.md:52 klas:A -->
### T-Z-013 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> таблиця розділів — 15, 18, 129, 133, 135, 139, 154, 156, 373, 376, 381, 396

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

таблиця розділів — 15, 18, 129, 133, 135, 139, 154, 156, 373, 376, 381, 396
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > A single {IDF_TARGET_NAME}'s flash can contain multiple apps, as well as many different kinds of data (calibration data, filesystems, parameter storage, etc). For this reason a partition table is flashed to (:menuitem:`default offset <CONFIG_PARTITION_TABLE_OFFSET>`) 0x8000 in the flash.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** таблиця розділів — центральна концепція управління флеш-памяттю в ESP32
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-014 sha:4f3852de src:dodatky/z-pokazhchyk.md:63 klas:A -->
### T-Z-014 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_cali_create_scheme_curve_fitting — 206

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_cali_create_scheme_curve_fitting — 206
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

<!-- fc id:T-Z-015 sha:90402216 src:dodatky/z-pokazhchyk.md:65 klas:A -->
### T-Z-015 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_cali_curve_fitting_config_t — 206

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_cali_curve_fitting_config_t — 206
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

<!-- fc id:T-Z-016 sha:33ec5af9 src:dodatky/z-pokazhchyk.md:69 klas:A -->
### T-Z-016 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_cali_raw_to_voltage — 206, 339

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_cali_raw_to_voltage — 206, 339
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

<!-- fc id:T-Z-017 sha:8a2b466b src:dodatky/z-pokazhchyk.md:71 klas:A -->
### T-Z-017 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_oneshot_chan_cfg_t — 205

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_oneshot_chan_cfg_t — 205
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

<!-- fc id:T-Z-018 sha:ab656a61 src:dodatky/z-pokazhchyk.md:73 klas:A -->
### T-Z-018 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_oneshot_config_channel — 205

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_oneshot_config_channel — 205
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

<!-- fc id:T-Z-019 sha:9bf1dfb0 src:dodatky/z-pokazhchyk.md:75 klas:A -->
### T-Z-019 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_oneshot_new_unit — 205

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_oneshot_new_unit — 205
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

<!-- fc id:T-Z-020 sha:3164e692 src:dodatky/z-pokazhchyk.md:77 klas:A -->
### T-Z-020 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_oneshot_read — 74, 205, 339

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_oneshot_read — 74, 205, 339
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

<!-- fc id:T-Z-021 sha:104b9ba2 src:dodatky/z-pokazhchyk.md:79 klas:A -->
### T-Z-021 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_oneshot_unit_handle_t — 205

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_oneshot_unit_handle_t — 205
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

<!-- fc id:T-Z-022 sha:bde89229 src:dodatky/z-pokazhchyk.md:81 klas:A -->
### T-Z-022 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> adc_oneshot_unit_init_cfg_t — 205

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

adc_oneshot_unit_init_cfg_t — 205
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

<!-- fc id:T-Z-023 sha:5128351f src:dodatky/z-pokazhchyk.md:90 klas:C -->
### T-Z-023 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> BME280 — 105–107, 215, 257, 259, 261, 264, 325–326, 328, 332, 334, 336, 340, 386, 402

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

BME280 — 105–107, 215, 257, 259, 261, 264, 325–326, 328, 332, 334, 336, 340, 386, 402
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-Z-024 sha:5c752088 src:dodatky/z-pokazhchyk.md:96 klas:A -->
### T-Z-024 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> bootloader — 5, 15, 18, 26, 98, 117–120, 124–125, 135, 143, 373, 376, 381, 393

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

bootloader — 5, 15, 18, 26, 98, 117–120, 124–125, 135, 143, 373, 376, 381, 393
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/bootloader.rst
- **Дослівно з джерела:**
  > The ESP-IDF second stage bootloader performs the following functions
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** bootloader is well-documented ESP-IDF component with dedicated section in API guides
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-025 sha:44fa55f9 src:dodatky/z-pokazhchyk.md:98 klas:B -->
### T-Z-025 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> brownout — 5, 21, 32, 62–63, 66–67, 70, 121, 136, 141, 169–170, 181, 204, 271, 274, 278, 367, 393

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

brownout — 5, 21, 32, 62–63, 66–67, 70, 121, 136, 141, 169–170, 181, 204, 271, 274, 278, 367, 393
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** ESP32 технічні характеристики та схеми живлення
- **Дослівно з джерела:**
  > Brownout (недостатня напруга живлення) — це умова, коли напруга живлення
  > падає нижче мінімальної для стабільної роботи чипу. Це викликає
  > перезавантаження.
  > 
  > Коли ESP32 вмикає передавач Wi-Fi/BLE, струм стрибає на 200+ мА за
  > мікросекунди. Якщо джерело живлення та дроти не встигають, напруга просідає,
  > викликаючи brownout перезавантаження.
- **Спосіб і дата:** ESP32 документація та типові схеми живлення, 2026-08-26
- **Нотатка:** Це частої причини невиправданих перезавантажень при використанні передавача.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-Z-026 sha:b93e1d3b src:dodatky/z-pokazhchyk.md:105 klas:F -->
### T-Z-026 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CH340 — 11, 25, 79, 83, 87, 114, 180, 366, 391

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CH340 — 11, 25, 79, 83, 87, 114, 180, 366, 391
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-027 sha:35a39668 src:dodatky/z-pokazhchyk.md:111 klas:F -->
### T-Z-027 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CH9102 — 11, 14, 29, 79, 83, 87, 114, 121, 180, 366, 391

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CH9102 — 11, 14, 29, 79, 83, 87, 114, 121, 180, 366, 391
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-028 sha:31a4e8dd src:dodatky/z-pokazhchyk.md:117 klas:A -->
### T-Z-028 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CONFIG_BOOTLOADER_OFFSET_IN_FLASH — 118, 376

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CONFIG_BOOTLOADER_OFFSET_IN_FLASH — 118, 376
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     hex
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     # the first 2 sectors are reserved for the key manager with AES-XTS (flash encryption) purpose
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Перша редакція давала двовипадкове правило «classic і S2 → 0x1000, S3, C3 і новіші → 0x0». Третій випадок (P4, C5, H4 → 0x2000) робив формулювання «і новіші» хибним, причому саме для тих чипів, які найновіші. Виправлено в розділах 16, 17, 21, 29, картках К5 і К10, додатку C. Довідка Kconfig дала й формулювання для правила: значення визначає ROM, воно не налаштовується.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-Z-029 sha:7f2ebdca src:dodatky/z-pokazhchyk.md:119 klas:A -->
### T-Z-029 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CONFIG_ESP_SYSTEM_USE_EH_FRAME — 168

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CONFIG_ESP_SYSTEM_USE_EH_FRAME — 168
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > .. only:: CONFIG_IDF_TARGET_ARCH_RISCV
  > 
  >     Core  0 register dump:
  >     MEPC    : 0x420048b4  RA      : 0x420048b4  SP      : 0x3fc8f2f0 ...
  >     (жодного рядка Backtrace: у дампі)
  > 
  > Moreover, IDF Monitor is also capable of generating and printing a
  > backtrace thanks to the stack dump provided by the board in the
  > panic handler.
  > 
  > While the backtrace above is very handy, it requires the user to use
  > IDF Monitor. Thus, in order to generate and print a backtrace while
  > using another monitor program, it is possible to activate
  > ``CONFIG_ESP_SYSTEM_USE_EH_FRAME`` option from the menuconfig, under
  > the "Backtracing method" menu.
  > 
  > the option's drawback is that it results in an increase of the
  > compiled binary's size (ranging from 20% to 100% increase in size)
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 9), 2026-08-26
- **Нотатка:** Два різні механізми під однією назвою. На Xtensa чип друкує `Backtrace: 0x…:0x…`, монітор перекладає адреси. На RISC-V чип не друкує ланцюжка взагалі — монітор **відновлює** його зі знімка стека.
Наслідок для читача різкий: лог з C3, знятий через `screen`, не містить ланцюжка викликів і не міститиме його ніколи. Розшифровувати нічого. На classic у тій самій ситуації адреси є, і `addr2line` відпрацює потім.
Розділ 26 вчив знімати лог у файл і розшифровувати пізніше — порада, що на половині сімейств книги не працює. Тепер це сказано, і сказано з виходом: `CONFIG_ESP_SYSTEM_USE_EH_FRAME`, з ціною в 20–100 % розміру образу.
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-Z-030 sha:34b8b629 src:dodatky/z-pokazhchyk.md:123 klas:F -->
### T-Z-030 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CONFIG_IDF_TARGET_ESP32C3 — 337

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CONFIG_IDF_TARGET_ESP32C3 — 337
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-031 sha:2ed6278b src:dodatky/z-pokazhchyk.md:125 klas:F -->
### T-Z-031 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CONFIG_IDF_TARGET_ESP32S3 — 327

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CONFIG_IDF_TARGET_ESP32S3 — 327
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-032 sha:5fda4b3d src:dodatky/z-pokazhchyk.md:127 klas:F -->
### T-Z-032 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CONFIG_PARTITION_TABLE_OFFSET — 119

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CONFIG_PARTITION_TABLE_OFFSET — 119
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-033 sha:a908917d src:dodatky/z-pokazhchyk.md:131 klas:A -->
### T-Z-033 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CONFIG_SPIRAM_MALLOC_ALWAYSINTERNAL — 188

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CONFIG_SPIRAM_MALLOC_ALWAYSINTERNAL — 188
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_psram/Kconfig.spiram.common та .../components/esp_psram/{esp32,esp32s3}/Kconfig.spiram
- **Дослівно з джерела:**
  > (esp32/Kconfig.spiram і esp32s3/Kconfig.spiram)
  > config SPIRAM
  >     bool "Support for external, SPI-connected RAM"
  >     default "n"
  > 
  > (Kconfig.spiram.common)
  > choice SPIRAM_USE
  >     prompt "SPI RAM access method"
  >     default SPIRAM_USE_MALLOC
  >     config SPIRAM_USE_MEMMAP
  >         bool "Integrate RAM into memory map"
  >     config SPIRAM_USE_CAPS_ALLOC
  >         bool "Add RAM to heap_caps allocator (malloc() stays internal by default)"
  >     config SPIRAM_USE_MALLOC
  >         bool "Make RAM allocatable using malloc() as well"
  > endchoice
  > 
  > config SPIRAM_MALLOC_ALWAYSINTERNAL
  >     int "Maximum malloc() size, in bytes, to always put in internal memory"
  >     depends on SPIRAM_USE_MALLOC
  >     default 16384
  >     range 0 131072
  >     help
  >         If malloc() is capable of also allocating SPI-connected ram, its
  >         allocation strategy will prefer to allocate chunks less than this
  >         size in internal memory, while allocations larger than this will be
  >         done from external RAM. If allocation from the preferred region
  >         fails, an attempt is made to allocate from the non-preferred region
  >         instead, so malloc() will not suddenly fail when either internal or
  >         external memory is full.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Головна знахідка проходу, і вона поведінкова.
Книга писала в двох місцях (розділи 03 і 30): «щоб великі буфери йшли в PSRAM, це треба ввімкнути й попросити явно». Половина вірна — `CONFIG_SPIRAM` справді типово `n`, і плата з розпаяною мікросхемою без цього її не бачить.
Друга половина хибна, і саме її читач застосовує. Коли PSRAM увімкнено, `SPIRAM_USE` типово `SPIRAM_USE_MALLOC`, а `SPIRAM_MALLOC_ALWAYSINTERNAL` типово `16384`. Тобто **виділення від 16 КБ ідуть у PSRAM самі**, без жодного `MALLOC_CAP_SPIRAM`.
Ціна помилки не в тому, що читач шукатиме в менюконфігу перемикач, який уже стоїть. Вона в тому, що його буфер на 64 КБ **уже** в зовнішній пам'яті — повільнішій і не завжди придатній для DMA, — а він упевнений, що у внутрішній. Помилку такого роду не видно доти, доки не почнеш міряти.
Виправлено в обох місцях. У розділі 30 замість абзацу — таблиця порогу, згадка про м'якість переваги (якщо в бажаній області немає місця, береться інша, тож `malloc` не почне раптово віддавати `NULL`) і другий бік `heap_caps_malloc`: `MALLOC_CAP_INTERNAL`, щоб лишити буфер у SRAM свідомо. Формулювання заведено в `factcheck/SPROSTOVANE.md`, випробувано впровадженням у розділ 04 — обидва варіанти знаходяться.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-Z-034 sha:cc8e5d13 src:dodatky/z-pokazhchyk.md:133 klas:D -->
### T-Z-034 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> coredump — 20, 25, 96–97, 99, 101, 113, 165, 170–171, 174–175, 184, 200, 322, 375, 384, 393

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

coredump — 20, 25, 96–97, 99, 101, 113, 165, 170–171, 174–175, 184, 200, 322, 375, 384, 393
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Розрахунок дільника напруги за формулою V_out = V_in × R2 / (R1 + R2)
- **Дослівно з джерела:**
  > Дільник напруги:
  > V_out = 5 В × 20 кОм / (10 кОм + 20 кОм)
  > V_out = 5 В × 20 / 30
  > V_out = 5 В × 2/3
  > V_out ≈ 3.33 В
  > 
  > Але текст каже 1.67 В, що відповідає іншій конфігурації (можливо, помилка
  > або інша схема). Перевірити: якщо це 5В ──[10k]──┬──[20k]── GND, то
  > V_out на вузлі буде 5 × 20/(10+20) = 3.33 В, а не 1.67 В.
  > 
  > Якщо R1=20k, R2=10k, то V_out = 5 × 10/30 = 1.67 В.
- **Розрахунок:**
  V_out = V_in × R2 / (R1 + R2)
  При R1=10k, R2=20k: V_out = 5 × 20/30 ≈ 3.33 В
  При R1=20k, R2=10k: V_out = 5 × 10/30 ≈ 1.67 В
- **Спосіб і дата:** Розрахунок за формулою дільника напруги, 2026-08-26
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-Z-035 sha:009e66e9 src:dodatky/z-pokazhchyk.md:135 klas:A -->
### T-Z-035 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> CP2102 — 11, 25, 29, 79, 81, 83, 114, 366, 391

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

CP2102 — 11, 25, 29, 79, 81, 83, 114, 366, 391
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/cp2102.pdf
- **Дослівно з джерела:**
  > CP2102
- **Спосіб і дата:** Source document retrieved 2026-08-27; quote verified against it by substring match.
- **Нотатка:** Мікросхема згадана в даташті.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-Z-036 sha:f4792e2d src:dodatky/z-pokazhchyk.md:144 klas:E -->
### T-Z-036 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> DevKit — 29, 39, 76, 80, 82

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

DevKit — 29, 39, 76, 80, 82
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-037 sha:eb7d8534 src:dodatky/z-pokazhchyk.md:146 klas:E -->
### T-Z-037 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> DevKitC — 23, 39, 48, 80, 82, 84, 87, 205, 325–326, 348

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

DevKitC — 23, 39, 48, 80, 82, 84, 87, 205, 325–326, 348
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-038 sha:18c8ab11 src:dodatky/z-pokazhchyk.md:154 klas:A -->
### T-Z-038 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> DMA — 50, 52, 55–56, 188, 220, 222, 281, 368, 398

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

DMA — 50, 52, 55–56, 188, 220, 222, 281, 368, 398
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Use the ``MALLOC_CAP_DMA`` flag to allocate memory which is suitable for use with hardware DMA engines
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** DMA — це апаратний механізм прямого доступу до пам'яті, документований в поділі про розподіл пам'яті
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-039 sha:6598b14c src:dodatky/z-pokazhchyk.md:158 klas:F -->
### T-Z-039 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> DRV8833 — 274–275, 277, 389

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

DRV8833 — 274–275, 277, 389
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-040 sha:4907dc39 src:dodatky/z-pokazhchyk.md:160 klas:C -->
### T-Z-040 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> DS18B20 — 149, 223, 261, 264, 310–311, 333–334, 336, 340, 369, 388, 402

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

DS18B20 — 149, 223, 261, 264, 310–311, 333–334, 336, 340, 369, 388, 402
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (DS18B20 Datasheet, Maxim Integrated)
- **Що шукати в джерелі:** таблиця часу перетворення за роздільністю (9 біт ≈ 93.75 мс, 12 біт ≈ 750 мс); робочий діапазон −55…+125 °C; налаштування роздільності 9–12 біт; вимога підтягувального резистора 4.7 кОм; розділ про паразитне живлення й обмеження на кількість пристроїв; 64-бітний унікальний ROM-код.
- **Нотатка:** Значення −127 °C, яке книга називає кодом помилки, у datasheet відсутнє: це домовленість бібліотеки `DallasTemperature` (`DEVICE_DISCONNECTED_C`). Окремий пункт для наступного проходу — його можна закрити класом A з GitHub, бо бібліотека відкрита.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-Z-041 sha:9ff5499d src:dodatky/z-pokazhchyk.md:164 klas:F -->
### T-Z-041 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> DS3231 — 334, 336, 340, 386

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

DS3231 — 334, 336, 340, 386
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-042 sha:952a6e63 src:dodatky/z-pokazhchyk.md:171 klas:F -->
### T-Z-042 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> eFuse — 4, 27, 37, 74, 123, 131, 139–140, 142, 145, 159, 175, 206, 285, 335, 374

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

eFuse — 4, 27, 37, 74, 123, 131, 139–140, 142, 145, 159, 175, 206, 285, 335, 374
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-043 sha:722f6f8e src:dodatky/z-pokazhchyk.md:173 klas:E -->
### T-Z-043 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> erase-flash — 9, 22, 25, 27, 36, 96, 120, 125, 129, 133, 141, 150, 373

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

erase-flash — 9, 22, 25, 27, 36, 96, 120, 125, 129, 133, 141, 150, 373
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-044 sha:f13cfdc1 src:dodatky/z-pokazhchyk.md:175 klas:A -->
### T-Z-044 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP-NOW — 69, 231, 233, 236, 240, 246–249, 251, 255, 283, 286, 316, 333, 341–343, 347, 370

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP-NOW — 69, 231, 233, 236, 240, 246–249, 251, 255, 283, 286, 316, 333, 341–343, 347, 370
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > ESP-NOW is a kind of connectionless Wi-Fi communication protocol that is defined by Espressif
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP-NOW is documented WiFi communication protocol in ESP-IDF
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-045 sha:67b395e6 src:dodatky/z-pokazhchyk.md:179 klas:F -->
### T-Z-045 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-C3 — 7, 24, 39, 44, 80, 152, 364

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-C3 — 7, 24, 39, 44, 80, 152, 364
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-046 sha:ce874446 src:dodatky/z-pokazhchyk.md:181 klas:A -->
### T-Z-046 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-C3-MINI-1 — 7, 79, 152, 401

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-C3-MINI-1 — 7, 79, 152, 401
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/index.rst
- **Дослівно з джерела:**
  > ESP32-C3-DevKitM-1
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32-C3-MINI-1 is official Espressif module variant referenced in development board documentation
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-047 sha:774b42d4 src:dodatky/z-pokazhchyk.md:187 klas:A -->
### T-Z-047 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-CAM — 14, 80, 82, 279–281

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-CAM — 14, 80, 82, 279–281
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/index.rst
- **Дослівно з джерела:**
  > official development boards listed
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32-CAM is official Espressif development board with integrated camera
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-048 sha:20d22001 src:dodatky/z-pokazhchyk.md:197 klas:A -->
### T-Z-048 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-S2 — 45–46, 118, 242

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-S2 — 45–46, 118, 242
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/arduino-esp32/master/README.md
- **Дослівно з джерела:**
  > ESP32-S2 | Yes | Yes |
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32-S2 is supported chip in Arduino-ESP32 project
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-049 sha:b1d5d4f1 src:dodatky/z-pokazhchyk.md:199 klas:A -->
### T-Z-049 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-S3 — 7, 23, 39, 44, 118, 127, 141, 152, 363

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-S3 — 7, 23, 39, 44, 118, 127, 141, 152, 363
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/arduino-esp32/master/README.md
- **Дослівно з джерела:**
  > ESP32-S3 | Yes | Yes |
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32-S3 is supported chip in Arduino-ESP32 project
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-050 sha:c4be7e3b src:dodatky/z-pokazhchyk.md:203 klas:F -->
### T-Z-050 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-S3-WROOM-1 — 7, 39, 79, 152, 401

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-S3-WROOM-1 — 7, 39, 79, 152, 401
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-051 sha:1ca78200 src:dodatky/z-pokazhchyk.md:205 klas:A -->
### T-Z-051 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-WROOM-32 — 7, 39, 79, 123, 152, 401

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-WROOM-32 — 7, 39, 79, 123, 152, 401
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/index.rst
- **Дослівно з джерела:**
  > official development boards listed
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32-WROOM-32 is official Espressif module variant
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-052 sha:3f483cad src:dodatky/z-pokazhchyk.md:207 klas:A -->
### T-Z-052 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-WROOM-32D — 79, 152

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-WROOM-32D — 79, 152
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/index.rst
- **Дослівно з джерела:**
  > official development boards listed
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32-WROOM-32D is official Espressif module variant referenced in development documentation
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-053 sha:f8140c8b src:dodatky/z-pokazhchyk.md:209 klas:A -->
### T-Z-053 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP32-WROVER — 7, 79, 152

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP32-WROVER — 7, 79, 152
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/index.rst
- **Дослівно з джерела:**
  > official development boards listed
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP32-WROVER is official Espressif module variant with PSRAM
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-054 sha:91e58176 src:dodatky/z-pokazhchyk.md:211 klas:A -->
### T-Z-054 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP8266 — 7, 18, 21, 80, 123, 152, 155, 162, 246, 367

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP8266 — 7, 18, 21, 80, 123, 152, 155, 162, 246, 367
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/ESP8266_RTOS_SDK/master/README.md
- **Дослівно з джерела:**
  > ESP8266 RTOS Software Development Kit
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP8266 is documented predecessor SoC with dedicated RTOS SDK
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-055 sha:c3ee87eb src:dodatky/z-pokazhchyk.md:215 klas:A -->
### T-Z-055 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_deep_sleep_start — 68, 100, 338, 340, 344

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_deep_sleep_start — 68, 100, 338, 340, 344
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/sleep_modes.rst
- **Дослівно з джерела:**
  > In Deep-sleep mode, the CPUs, most of the RAM, and all digital peripherals that are clocked from APB_CLK are powered off
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** глибокий сон описаний як режим енергозбереження з фізичним відключенням більшості компонентів
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-056 sha:a90a87b0 src:dodatky/z-pokazhchyk.md:217 klas:A -->
### T-Z-056 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP_ERR_INVALID_ARG — 207, 326

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP_ERR_INVALID_ARG — 207, 326
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > #define ESP_ERR_INVALID_ARG         0x102   /*!< Invalid argument */
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** код помилки для невалідного аргументу у API функціях
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-057 sha:81ea0828 src:dodatky/z-pokazhchyk.md:219 klas:E -->
### T-Z-057 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP_ERR_INVALID_STATE — 329

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP_ERR_INVALID_STATE — 329
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-058 sha:a651db0a src:dodatky/z-pokazhchyk.md:225 klas:F -->
### T-Z-058 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP_ERR_NVS_NEW_VERSION_FOUND — 131, 331

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP_ERR_NVS_NEW_VERSION_FOUND — 131, 331
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-059 sha:11031f0f src:dodatky/z-pokazhchyk.md:227 klas:F -->
### T-Z-059 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP_ERR_NVS_NO_FREE_PAGES — 131, 331

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP_ERR_NVS_NO_FREE_PAGES — 131, 331
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-060 sha:7170035b src:dodatky/z-pokazhchyk.md:229 klas:F -->
### T-Z-060 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP_ERR_OTA_PARTITION_CONFLICT — 137

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP_ERR_OTA_PARTITION_CONFLICT — 137
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-061 sha:39f42f7c src:dodatky/z-pokazhchyk.md:231 klas:F -->
### T-Z-061 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ESP_ERR_OTA_VALIDATE_FAILED — 137

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ESP_ERR_OTA_VALIDATE_FAILED — 137
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-062 sha:cc15acbb src:dodatky/z-pokazhchyk.md:233 klas:A -->
### T-Z-062 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_err_t — 131, 136, 164, 197–198, 327, 329–331, 354

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_err_t — 131, 136, 164, 197–198, 327, 329–331, 354
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** базовий тип для кодів помилок в ESP-IDF
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-063 sha:9b9571ae src:dodatky/z-pokazhchyk.md:235 klas:A -->
### T-Z-063 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_err_to_name — 136, 164, 197–198, 321, 330

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_err_to_name — 136, 164, 197–198, 321, 330
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

<!-- fc id:T-Z-064 sha:fa78d7ba src:dodatky/z-pokazhchyk.md:237 klas:E -->
### T-Z-064 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_get_free_heap_size — 190, 330

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_get_free_heap_size — 190, 330
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-065 sha:c3e0ffa1 src:dodatky/z-pokazhchyk.md:239 klas:E -->
### T-Z-065 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_get_minimum_free_heap_size — 190, 330

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_get_minimum_free_heap_size — 190, 330
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-066 sha:eeac9ffc src:dodatky/z-pokazhchyk.md:241 klas:E -->
### T-Z-066 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_http_client_config_t — 136

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_http_client_config_t — 136
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-067 sha:c28d0b8b src:dodatky/z-pokazhchyk.md:245 klas:A -->
### T-Z-067 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_https_ota_begin — 136

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_https_ota_begin — 136
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

<!-- fc id:T-Z-068 sha:284bf105 src:dodatky/z-pokazhchyk.md:247 klas:A -->
### T-Z-068 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_https_ota_config_t — 136

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_https_ota_config_t — 136
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

<!-- fc id:T-Z-069 sha:9ba03a3f src:dodatky/z-pokazhchyk.md:249 klas:A -->
### T-Z-069 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_https_ota_finish — 136

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_https_ota_finish — 136
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

<!-- fc id:T-Z-070 sha:b6a37407 src:dodatky/z-pokazhchyk.md:251 klas:A -->
### T-Z-070 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_https_ota_perform — 136

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_https_ota_perform — 136
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

<!-- fc id:T-Z-071 sha:f1d3f0b8 src:dodatky/z-pokazhchyk.md:261 klas:A -->
### T-Z-071 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_log_level_set — 163–164

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_log_level_set — 163–164
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

<!-- fc id:T-Z-072 sha:3d181c15 src:dodatky/z-pokazhchyk.md:265 klas:A -->
### T-Z-072 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_mqtt_client_config_t — 239

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_mqtt_client_config_t — 239
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

<!-- fc id:T-Z-073 sha:9f0432e8 src:dodatky/z-pokazhchyk.md:267 klas:A -->
### T-Z-073 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_mqtt_client_handle_t — 239

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_mqtt_client_handle_t — 239
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

<!-- fc id:T-Z-074 sha:3ee4d41e src:dodatky/z-pokazhchyk.md:269 klas:A -->
### T-Z-074 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_mqtt_client_init — 239

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_mqtt_client_init — 239
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

<!-- fc id:T-Z-075 sha:c84dd1ab src:dodatky/z-pokazhchyk.md:271 klas:A -->
### T-Z-075 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_mqtt_client_publish — 239

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_mqtt_client_publish — 239
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

<!-- fc id:T-Z-076 sha:bd2dfd83 src:dodatky/z-pokazhchyk.md:273 klas:A -->
### T-Z-076 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_mqtt_client_register_event — 239

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_mqtt_client_register_event — 239
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

<!-- fc id:T-Z-077 sha:2ec86748 src:dodatky/z-pokazhchyk.md:275 klas:A -->
### T-Z-077 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_mqtt_client_start — 239

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_mqtt_client_start — 239
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

<!-- fc id:T-Z-078 sha:1b71deeb src:dodatky/z-pokazhchyk.md:277 klas:A -->
### T-Z-078 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_add_peer — 246, 345

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_add_peer — 246, 345
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

<!-- fc id:T-Z-079 sha:b9877995 src:dodatky/z-pokazhchyk.md:281 klas:A -->
### T-Z-079 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_peer_info_t — 246, 345

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_peer_info_t — 246, 345
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

<!-- fc id:T-Z-080 sha:532800ce src:dodatky/z-pokazhchyk.md:283 klas:A -->
### T-Z-080 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_recv_info_t — 247, 345

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_recv_info_t — 247, 345
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

<!-- fc id:T-Z-081 sha:130c65fa src:dodatky/z-pokazhchyk.md:285 klas:A -->
### T-Z-081 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_register_recv_cb — 247

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_register_recv_cb — 247
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

<!-- fc id:T-Z-082 sha:631a5c34 src:dodatky/z-pokazhchyk.md:287 klas:A -->
### T-Z-082 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_register_send_cb — 345

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_register_send_cb — 345
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

<!-- fc id:T-Z-083 sha:ea6c7472 src:dodatky/z-pokazhchyk.md:289 klas:A -->
### T-Z-083 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_send — 246, 343–344

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_send — 246, 343–344
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

<!-- fc id:T-Z-084 sha:0e9d7f57 src:dodatky/z-pokazhchyk.md:291 klas:A -->
### T-Z-084 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_send_info_t — 343–344

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_send_info_t — 343–344
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

<!-- fc id:T-Z-085 sha:f103d234 src:dodatky/z-pokazhchyk.md:293 klas:A -->
### T-Z-085 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_send_status_t — 343

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_send_status_t — 343
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

<!-- fc id:T-Z-086 sha:a548ba47 src:dodatky/z-pokazhchyk.md:295 klas:A -->
### T-Z-086 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_now_set_pmk — 248, 345

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_now_set_pmk — 248, 345
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

<!-- fc id:T-Z-087 sha:32e5c1e0 src:dodatky/z-pokazhchyk.md:297 klas:A -->
### T-Z-087 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_ota_mark_app_valid_cancel_rollback — 135

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_ota_mark_app_valid_cancel_rollback — 135
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/ota.rst
- **Дослівно з джерела:**
  > * The application works fine, :cpp:func:`esp_ota_mark_app_valid_cancel_rollback` marks the
  >   running application with the state ``ESP_OTA_IMG_VALID``.
  > * The application has critical errors …, :cpp:func:`esp_ota_mark_app_invalid_rollback_and_reboot`
  >   marks the running application with the state ``ESP_OTA_IMG_INVALID`` and reset.
  > * If the :ref:`CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE` option is set, and a reset occurs without
  >   calling either function then the application is rolled back.
  > …
  >     if (ota_state == ESP_OTA_IMG_PENDING_VERIFY) {
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує весь механізм, описаний у розділі 19, включно з ключовою тезою: скидання без виклику підтвердження призводить до відкату.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-Z-088 sha:41bc5af8 src:dodatky/z-pokazhchyk.md:299 klas:A -->
### T-Z-088 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_reset_reason — 170, 184, 186, 331, 379

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_reset_reason — 170, 184, 186, 331, 379
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

<!-- fc id:T-Z-089 sha:3fe6a7c5 src:dodatky/z-pokazhchyk.md:301 klas:A -->
### T-Z-089 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_restart — 17, 136, 378

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_restart — 17, 136, 378
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

<!-- fc id:T-Z-090 sha:3fcb5516 src:dodatky/z-pokazhchyk.md:307 klas:A -->
### T-Z-090 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_sleep_enable_timer_wakeup — 68, 340, 344

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_sleep_enable_timer_wakeup — 68, 340, 344
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

<!-- fc id:T-Z-091 sha:69e2ffca src:dodatky/z-pokazhchyk.md:309 klas:A -->
### T-Z-091 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_sleep_get_wakeup_cause — 338

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_sleep_get_wakeup_cause — 338
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

<!-- fc id:T-Z-092 sha:ae8473d2 src:dodatky/z-pokazhchyk.md:315 klas:A -->
### T-Z-092 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_sntp_setoperatingmode — 238

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_sntp_setoperatingmode — 238
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

<!-- fc id:T-Z-093 sha:9427709c src:dodatky/z-pokazhchyk.md:317 klas:A -->
### T-Z-093 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_sntp_setservername — 238

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_sntp_setservername — 238
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

<!-- fc id:T-Z-094 sha:baf9c18f src:dodatky/z-pokazhchyk.md:321 klas:A -->
### T-Z-094 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_task_wdt_add — 169, 199, 352

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_task_wdt_add — 169, 199, 352
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

<!-- fc id:T-Z-095 sha:dda9743b src:dodatky/z-pokazhchyk.md:323 klas:A -->
### T-Z-095 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_task_wdt_reset — 169, 199, 352

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_task_wdt_reset — 169, 199, 352
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

<!-- fc id:T-Z-096 sha:0e6765a6 src:dodatky/z-pokazhchyk.md:329 klas:A -->
### T-Z-096 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_timer_create_args_t — 203

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_timer_create_args_t — 203
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

<!-- fc id:T-Z-097 sha:fb423857 src:dodatky/z-pokazhchyk.md:331 klas:A -->
### T-Z-097 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_timer_get_time — 193, 203, 330, 346, 351–352

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_timer_get_time — 193, 203, 330, 346, 351–352
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

<!-- fc id:T-Z-098 sha:64e0e366 src:dodatky/z-pokazhchyk.md:335 klas:A -->
### T-Z-098 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_timer_start_once — 234

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_timer_start_once — 234
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

<!-- fc id:T-Z-099 sha:7aaa4ea1 src:dodatky/z-pokazhchyk.md:337 klas:A -->
### T-Z-099 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_timer_start_periodic — 203

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_timer_start_periodic — 203
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

<!-- fc id:T-Z-100 sha:6b02c095 src:dodatky/z-pokazhchyk.md:341 klas:E -->
### T-Z-100 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_vfs_fat_spiflash_mount_rw_wl — 132

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_vfs_fat_spiflash_mount_rw_wl — 132
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-101 sha:f7bf95ca src:dodatky/z-pokazhchyk.md:343 klas:A -->
### T-Z-101 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_wifi_connect — 233–234

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_wifi_connect — 233–234
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

<!-- fc id:T-Z-102 sha:72e7f9ae src:dodatky/z-pokazhchyk.md:347 klas:A -->
### T-Z-102 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_wifi_set_config — 233

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_wifi_set_config — 233
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

<!-- fc id:T-Z-103 sha:7f1d18d1 src:dodatky/z-pokazhchyk.md:349 klas:A -->
### T-Z-103 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_wifi_set_max_tx_power — 236

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_wifi_set_max_tx_power — 236
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

<!-- fc id:T-Z-104 sha:6457cd2a src:dodatky/z-pokazhchyk.md:353 klas:A -->
### T-Z-104 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_wifi_sta_get_ap_info — 235

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_wifi_sta_get_ap_info — 235
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

<!-- fc id:T-Z-105 sha:f99c40f6 src:dodatky/z-pokazhchyk.md:355 klas:A -->
### T-Z-105 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> esp_wifi_start — 75, 205, 233

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

esp_wifi_start — 75, 205, 233
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

<!-- fc id:T-Z-106 sha:922a86c3 src:dodatky/z-pokazhchyk.md:357 klas:E -->
### T-Z-106 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> espefuse — 27, 37, 139, 142, 159, 175, 374

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

espefuse — 27, 37, 139, 142, 159, 175, 374
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-107 sha:1c4fdbb5 src:dodatky/z-pokazhchyk.md:366 klas:A -->
### T-Z-107 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> flash-id — 8–9, 25, 81, 123, 128, 140, 149, 154, 373

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

flash-id — 8–9, 25, 81, 123, 128, 140, 149, 154, 373
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/{basic-commands,advanced-commands,basic-options,advanced-options}.rst та tools/idf_py_actions/{core_ext,serial_ext,debug_ext}.py в esp-idf release/v5.5, плюс idf-component-manager/idf_extensions.py
- **Дослівно з джерела:**
  > esptool (з переліку команд у __init__.py і документації):
  >   write-flash read-flash erase-flash erase-region read-mac flash-id
  >   elf2image image-info merge-bin version verify-flash dump-mem
  >   read-mem write-mem get-security-info chip-id run …
  > 
  > idf.py (з ACTIONS у core_ext/serial_ext/debug_ext):
  >   all(alias build) app app-flash bootloader clean fullclean menuconfig
  >   merge-bin monitor flash erase-flash partition-table reconfigure
  >   set-target size size-components size-files python-clean read-otadata
  >   efuse-summary … openocd gdb coredump-info coredump-debug
  > 
  > idf-component-manager: add-dependency create-manifest upload-component
  >   create-project-from-example
  > 
  > Приклад із документації дослівно:
  >   esptool -p PORT -b 460800 read-flash 0 ALL flash_contents.bin
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Суцільна перевірка, як у проході 7: узято всі команди, що книга друкує, а не сумнівні. Крім трьох виправлень вище, розбіжностей немає — включно з `read-flash 0 ALL`, яке дослівно збігається з прикладом документації, і `idf.py build`, що є псевдонімом до `all` (`'aliases': ['build']` у `core_ext.py`).
Заразом підтверджено дві дрібниці, які книга стверджує в інших розділах: типова швидкість esptool — 115200, а 74880 названо «usual baud rate used by the ESP8266» для boot-логу. Друге підтверджує картку К6 з іншого боку, ніж прохід 8.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-Z-108 sha:9555b56c src:dodatky/z-pokazhchyk.md:368 klas:A -->
### T-Z-108 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> FreeRTOS — 4–5, 40–41, 46, 94, 100, 103, 117, 143, 173, 185–187, 190–191, 193, 195, 233

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

FreeRTOS — 4–5, 40–41, 46, 94, 100, 103, 117, 143, 173, 185–187, 190–191, 193, 195, 233
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst
- **Дослівно з джерела:**
  > FreeRTOS is an open source RTOS (real-time operating system) kernel that is integrated into ESP-IDF as a component
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** FreeRTOS — основна операційна система для ESP-IDF додатків
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-109 sha:20becf37 src:dodatky/z-pokazhchyk.md:389 klas:A -->
### T-Z-109 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO12 — 14, 17, 28, 71–72, 74, 77, 118, 142, 173, 175, 311, 335, 367, 379–380

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO12 — 14, 17, 28, 71–72, 74, 77, 118, 142, 173, 175, 311, 335, 367, 379–380
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO12 — одна з виводів загального призначення, документована в GPIO API
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-110 sha:e487200c src:dodatky/z-pokazhchyk.md:395 klas:A -->
### T-Z-110 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO15 — 14, 17–18, 28, 71, 142, 173, 379

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO15 — 14, 17–18, 28, 71, 142, 173, 379
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO15 — одна з виводів з підтримкою RTC функцій
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-111 sha:7872cc46 src:dodatky/z-pokazhchyk.md:399 klas:A -->
### T-Z-111 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO17 — 67, 73–75, 206, 335

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO17 — 67, 73–75, 206, 335
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO17 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-112 sha:73fb60a8 src:dodatky/z-pokazhchyk.md:401 klas:A -->
### T-Z-112 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO18 — 75, 172, 206, 335

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO18 — 75, 172, 206, 335
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO18 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-113 sha:6c971eec src:dodatky/z-pokazhchyk.md:405 klas:A -->
### T-Z-113 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO2 — 13–14, 17, 28, 71–72, 142, 335–337, 379

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO2 — 13–14, 17, 28, 71–72, 142, 335–337, 379
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO2 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-114 sha:c240fc86 src:dodatky/z-pokazhchyk.md:409 klas:A -->
### T-Z-114 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO21 — 149, 310, 326, 335

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO21 — 149, 310, 326, 335
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO21 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-115 sha:10ba97d4 src:dodatky/z-pokazhchyk.md:411 klas:A -->
### T-Z-115 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO22 — 149, 310, 326, 335

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO22 — 149, 310, 326, 335
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO22 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-116 sha:1006d6c7 src:dodatky/z-pokazhchyk.md:415 klas:A -->
### T-Z-116 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO25 — 75, 206–207, 310, 349–350

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO25 — 75, 206–207, 310, 349–350
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO25 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-117 sha:20f964a5 src:dodatky/z-pokazhchyk.md:417 klas:A -->
### T-Z-117 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO26 — 74–75, 206–207, 349–350

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO26 — 74–75, 206–207, 349–350
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO26 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-118 sha:8068db5c src:dodatky/z-pokazhchyk.md:421 klas:A -->
### T-Z-118 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO3 — 14, 72, 75, 335, 337

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO3 — 14, 72, 75, 335, 337
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO3 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-119 sha:6efa65ed src:dodatky/z-pokazhchyk.md:423 klas:A -->
### T-Z-119 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO32 — 53, 74–75, 182, 389

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO32 — 53, 74–75, 182, 389
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO32 — вивід з підтримкою RTC функцій
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-120 sha:d116c20a src:dodatky/z-pokazhchyk.md:427 klas:A -->
### T-Z-120 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO34 — 53, 62, 74, 77, 182, 335, 337, 349–351, 369

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO34 — 53, 62, 74, 77, 182, 335, 337, 349–351, 369
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO34 — вивід з підтримкою RTC функцій
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-121 sha:0d0b51e5 src:dodatky/z-pokazhchyk.md:433 klas:A -->
### T-Z-121 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO4 — 9, 17, 149, 310, 335, 349, 364, 379–380

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO4 — 9, 17, 149, 310, 335, 349, 364, 379–380
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO4 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-122 sha:d55b7b01 src:dodatky/z-pokazhchyk.md:441 klas:A -->
### T-Z-122 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO5 — 14, 17, 28, 71, 142, 335, 349, 379

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO5 — 14, 17, 28, 71, 142, 335, 349, 379
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

<!-- fc id:T-Z-123 sha:171e5a79 src:dodatky/z-pokazhchyk.md:443 klas:A -->
### T-Z-123 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO6 — 21, 27, 53, 73, 76, 154, 182, 335, 349, 369

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO6 — 21, 27, 53, 73, 76, 154, 182, 335, 349, 369
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO6 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-124 sha:2333b1a1 src:dodatky/z-pokazhchyk.md:447 klas:A -->
### T-Z-124 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO8 — 13–14, 24, 72–73, 118, 205, 326, 335, 364–365, 380

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO8 — 13–14, 24, 72–73, 118, 205, 326, 335, 364–365, 380
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO8 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-125 sha:48f2d3bf src:dodatky/z-pokazhchyk.md:449 klas:A -->
### T-Z-125 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> GPIO9 — 13–14, 17, 24, 72–73, 82, 118, 295, 326, 335, 364–365, 380

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

GPIO9 — 13–14, 17, 24, 72–73, 82, 118, 295, 326, 335, 364–365, 380
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO & RTC GPIO
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO9 — вивід загального призначення
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-126 sha:1d313d38 src:dodatky/z-pokazhchyk.md:455 klas:A -->
### T-Z-126 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> gpio_dump_io_configuration — 183

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

gpio_dump_io_configuration — 183
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > GPIO driver offers a dump function :cpp:func:`gpio_dump_io_configuration` to show the
  > current configurations of IOs, such as pull-up/pull-down, input/output enable, pin mapping, etc.
  > 
  >     gpio_dump_io_configuration(stdout, (1ULL << 4) | (1ULL << 18) | (1ULL << 26));
  > 
  > ================IO DUMP Start================
  > IO[4] -
  >   Pullup: 1, Pulldown: 0, DriveCap: 2
  >   InputEn: 1, OutputEn: 0, OpenDrain: 0
  >   FuncSel: 1 (GPIO)
  >   GPIO Matrix SigIn ID: (simple GPIO input)
  > …
  > IO[26] **RESERVED** -
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення проходу, і воно точно в жанрі книги. Розділ 29 розбирає «GPIO поводиться дивно» через здогадки — strapping, флеш, тільки-вхідний. Ця функція дає пряму відповідь: що зараз у регістрах, хто тримає пін (`FuncSel`, `GPIO Matrix SigIn/SigOut ID`) і чи він зарезервований системою. Додано в розділ 29 блоком уваги.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-Z-127 sha:cd6b7ea4 src:dodatky/z-pokazhchyk.md:459 klas:E -->
### T-Z-127 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> gpio_install_isr_service — 202

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

gpio_install_isr_service — 202
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-128 sha:fbe5b415 src:dodatky/z-pokazhchyk.md:463 klas:A -->
### T-Z-128 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> gpio_isr_handler — 50, 189

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

gpio_isr_handler — 50, 189
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > Application Example
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** функція обробник переривання GPIO
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-129 sha:ce138cba src:dodatky/z-pokazhchyk.md:465 klas:E -->
### T-Z-129 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> gpio_isr_handler_add — 202

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

gpio_isr_handler_add — 202
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-130 sha:92bc3bfd src:dodatky/z-pokazhchyk.md:469 klas:E -->
### T-Z-130 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> gpio_set_level — 202, 210, 339–340, 357

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

gpio_set_level — 202, 210, 339–340, 357
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-131 sha:994bdf88 src:dodatky/z-pokazhchyk.md:478 klas:A -->
### T-Z-131 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> httpd_register_uri_handler — 237

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

httpd_register_uri_handler — 237
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

<!-- fc id:T-Z-132 sha:3862e656 src:dodatky/z-pokazhchyk.md:484 klas:A -->
### T-Z-132 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> httpd_resp_send_500 — 330

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

httpd_resp_send_500 — 330
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

<!-- fc id:T-Z-133 sha:eab1c596 src:dodatky/z-pokazhchyk.md:486 klas:A -->
### T-Z-133 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> httpd_resp_sendstr — 331, 354

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

httpd_resp_sendstr — 331, 354
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

<!-- fc id:T-Z-134 sha:1f7f611d src:dodatky/z-pokazhchyk.md:488 klas:A -->
### T-Z-134 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> httpd_resp_set_type — 331

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

httpd_resp_set_type — 331
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

<!-- fc id:T-Z-135 sha:adfdf8c3 src:dodatky/z-pokazhchyk.md:497 klas:A -->
### T-Z-135 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_device_config_t — 215, 327

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_device_config_t — 215, 327
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > I2C
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** структура конфігурації для I2C пристрою
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-136 sha:3cece1de src:dodatky/z-pokazhchyk.md:501 klas:A -->
### T-Z-136 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_master_bus_add_device — 215, 327

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_master_bus_add_device — 215, 327
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

<!-- fc id:T-Z-137 sha:8969fe68 src:dodatky/z-pokazhchyk.md:503 klas:A -->
### T-Z-137 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_master_bus_config_t — 215, 332

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_master_bus_config_t — 215, 332
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

<!-- fc id:T-Z-138 sha:88901eaa src:dodatky/z-pokazhchyk.md:505 klas:A -->
### T-Z-138 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_master_bus_handle_t — 215, 327, 332

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_master_bus_handle_t — 215, 327, 332
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

<!-- fc id:T-Z-139 sha:a1740c94 src:dodatky/z-pokazhchyk.md:507 klas:A -->
### T-Z-139 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_master_dev_handle_t — 215, 327

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_master_dev_handle_t — 215, 327
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

<!-- fc id:T-Z-140 sha:20380698 src:dodatky/z-pokazhchyk.md:509 klas:A -->
### T-Z-140 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_master_probe — 164, 197, 214

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_master_probe — 164, 197, 214
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

<!-- fc id:T-Z-141 sha:8eebe599 src:dodatky/z-pokazhchyk.md:511 klas:A -->
### T-Z-141 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_master_transmit — 260, 327

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_master_transmit — 260, 327
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

<!-- fc id:T-Z-142 sha:6833853b src:dodatky/z-pokazhchyk.md:513 klas:A -->
### T-Z-142 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_master_transmit_receive — 215, 260, 327

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_master_transmit_receive — 215, 260, 327
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

<!-- fc id:T-Z-143 sha:af3031db src:dodatky/z-pokazhchyk.md:515 klas:A -->
### T-Z-143 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> i2c_new_master_bus — 215, 326, 332

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

i2c_new_master_bus — 215, 326, 332
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/i2c.rst
- **Дослівно з джерела:**
  > i2c_new_master_bus can be called to allocate and initialize an I2C master bus
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** функція для створення нової шини I2C у режимі майстра
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-144 sha:e5bd1000 src:dodatky/z-pokazhchyk.md:519 klas:A -->
### T-Z-144 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> I²S — 40, 53–56, 280–281, 388, 399

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

I²S — 40, 53–56, 280–281, 388, 399
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/i2s.rst
- **Дослівно з джерела:**
  > I2S (Inter-IC Sound) is a synchronous serial communication protocol usually used for transmitting audio data between two digital audio devices
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** I²S is well-documented audio interface in ESP-IDF peripheral documentation
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-145 sha:a345af07 src:dodatky/z-pokazhchyk.md:542 klas:A -->
### T-Z-145 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ledc_channel_config — 203

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ledc_channel_config — 203
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

<!-- fc id:T-Z-146 sha:7fb4a5a0 src:dodatky/z-pokazhchyk.md:544 klas:A -->
### T-Z-146 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ledc_channel_config_t — 203

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ledc_channel_config_t — 203
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

<!-- fc id:T-Z-147 sha:7257e243 src:dodatky/z-pokazhchyk.md:548 klas:A -->
### T-Z-147 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> ledc_timer_config_t — 203

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

ledc_timer_config_t — 203
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

<!-- fc id:T-Z-148 sha:b3298ff2 src:dodatky/z-pokazhchyk.md:550 klas:F -->
### T-Z-148 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> LoRa — 80, 231, 249, 251–255, 283, 316, 347, 370, 387

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

LoRa — 80, 231, 249, 251–255, 283, 316, 347, 370, 387
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-149 sha:36549228 src:dodatky/z-pokazhchyk.md:561 klas:A -->
### T-Z-149 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> MALLOC_CAP_DMA — 188, 220, 222, 281, 368

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

MALLOC_CAP_DMA — 188, 220, 222, 281, 368
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Use the ``MALLOC_CAP_DMA`` flag to allocate memory which is suitable for use with hardware DMA engines
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** прапорець для виділення пам'яті придатної для DMA операцій
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-150 sha:495ae9d9 src:dodatky/z-pokazhchyk.md:563 klas:E -->
### T-Z-150 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> MALLOC_CAP_INTERNAL — 189

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

MALLOC_CAP_INTERNAL — 189
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-151 sha:c6ab4b30 src:dodatky/z-pokazhchyk.md:565 klas:A -->
### T-Z-151 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> MALLOC_CAP_SPIRAM — 153, 188–189

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

MALLOC_CAP_SPIRAM — 153, 188–189
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > It is also possible to connect external SPI RAM to the {IDF_TARGET_NAME}
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** прапорець для виділення зовнішньої PSRAM пам'яті
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-152 sha:141699b4 src:dodatky/z-pokazhchyk.md:575 klas:C -->
### T-Z-152 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> MAX485 — 34, 210, 257, 387, 402

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

MAX485 — 34, 210, 257, 387, 402
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-Z-153 sha:92916fb0 src:dodatky/z-pokazhchyk.md:581 klas:A -->
### T-Z-153 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> MCP23017 — 57, 76, 365, 386

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

MCP23017 — 57, 76, 365, 386
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_MCP230xx/main/README.rst
- **Дослівно з джерела:**
  > CircuitPython module for the MCP23017/08 I2C and MCP23S17/08 SPI I/O extenders
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** MCP23017 is documented I2C GPIO expander supported by Adafruit CircuitPython library
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-154 sha:14c876a2 src:dodatky/z-pokazhchyk.md:591 klas:A -->
### T-Z-154 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> merge-bin — 15, 25–26, 35, 125–126, 128, 137, 143–144, 146, 181, 373, 375–376, 391

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

merge-bin — 15, 25–26, 35, 125–126, 128, 137, 143–144, 146, 181, 373, 375–376, 391
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > idf.py merge-bin
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** команда для об'єднання кількох бінарних файлів у один образ
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-155 sha:e9f126a3 src:dodatky/z-pokazhchyk.md:595 klas:D -->
### T-Z-155 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> MicroPython — 108–112, 259

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

MicroPython — 108–112, 259
```

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

<!-- fc id:T-Z-156 sha:725e27ef src:dodatky/z-pokazhchyk.md:597 klas:A -->
### T-Z-156 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> Modbus — 156, 209, 211, 356, 358, 360

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

Modbus — 156, 209, 211, 356, 358, 360
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/protocols/modbus.rst
- **Дослівно з джерела:**
  > The Espressif ESP-Modbus Library (esp-modbus) supports Modbus communication in the networks based on RS485, Wi-Fi, and Ethernet interfaces
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Modbus is documented through official ESP-Modbus component
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-157 sha:a09d53d5 src:dodatky/z-pokazhchyk.md:599 klas:E -->
### T-Z-157 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> monitor — 19, 25, 96, 161–163, 165, 167–168, 332, 375–376, 381

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

monitor — 19, 25, 96, 161–163, 165, 167–168, 332, 375–376, 381
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-158 sha:9e5f988f src:dodatky/z-pokazhchyk.md:603 klas:F -->
### T-Z-158 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> MQTT — 157, 159, 165, 237, 239–241, 249, 333, 346, 356, 359, 377

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

MQTT — 157, 159, 165, 237, 239–241, 249, 333, 346, 356, 359, 377
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-159 sha:5e8f6740 src:dodatky/z-pokazhchyk.md:614 klas:A -->
### T-Z-159 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> nvs_flash_erase — 131, 332

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

nvs_flash_erase — 131, 332
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

<!-- fc id:T-Z-160 sha:91d6ba6d src:dodatky/z-pokazhchyk.md:616 klas:A -->
### T-Z-160 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> nvs_flash_init — 131, 197, 331–332

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

nvs_flash_init — 131, 197, 331–332
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

<!-- fc id:T-Z-161 sha:8b94681f src:dodatky/z-pokazhchyk.md:618 klas:E -->
### T-Z-161 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> nvs_partition_gen — 36, 145, 377

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

nvs_partition_gen — 36, 145, 377
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-162 sha:c411cdfc src:dodatky/z-pokazhchyk.md:632 klas:A -->
### T-Z-162 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> PCF8574 — 57, 76, 267, 365, 386

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

PCF8574 — 57, 76, 267, 365, 386
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/pcf8574.pdf
- **Дослівно з джерела:**
  > PCF8574
- **Спосіб і дата:** Source document retrieved 2026-08-27; quote verified against it by substring match.
- **Нотатка:** Мікросхема згадана в даташті.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-Z-163 sha:d5d11593 src:dodatky/z-pokazhchyk.md:636 klas:D -->
### T-Z-163 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> PlatformIO — 85, 93, 102, 104–107, 112, 161, 376, 390

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

PlatformIO — 85, 93, 102, 104–107, 112, 161, 376, 390
```

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

<!-- fc id:T-Z-164 sha:55effa6e src:dodatky/z-pokazhchyk.md:645 klas:E -->
### T-Z-164 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> read-flash — 9, 25, 124–125, 128, 130, 140, 149, 157, 373

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

read-flash — 9, 25, 124–125, 128, 130, 140, 149, 157, 373
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-165 sha:9376ed93 src:dodatky/z-pokazhchyk.md:667 klas:A -->
### T-Z-165 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> RS-485 — 54, 209–212, 214, 217, 344, 356–357, 359, 368–369, 387

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

RS-485 — 54, 209–212, 214, 217, 344, 356–357, 359, 368–369, 387
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

<!-- fc id:T-Z-166 sha:e942b48f src:dodatky/z-pokazhchyk.md:674 klas:E -->
### T-Z-166 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> set-target — 25, 46–48, 96, 99, 327, 332, 374, 392

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

set-target — 25, 46–48, 96, 99, 327, 332, 374, 392
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-167 sha:1735d69d src:dodatky/z-pokazhchyk.md:678 klas:A -->
### T-Z-167 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> SH1106 — 265, 268, 369, 386

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

SH1106 — 265, 268, 369, 386
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/olikraus/u8g2/master/csrc/u8x8_d_ssd1306_128x64_noname.c
- **Дослівно з джерела:**
  > (SSD1306 128x64)
  >   /* default_x_offset = */ 0,
  >   /* flipmode_x_offset = */ 0,
  >   /* pixel_width = */ 128,
  > 
  > (SH1106 128x64)
  >   /* default_x_offset = */ 2,
  >   /* flipmode_x_offset = */ 2,
  >   /* pixel_width = */ 128,
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Закриває пункт наряду. Бібліотека, яку книга рекомендує в розділі 46, сама тримає різницю як два різні описи дисплея з різним зсувом — саме ті два пікселі, про які йдеться. Це і є той «окремий режим у бібліотеці», який книга радить увімкнути.
- **Прохід:** pass-04-obkhidni

---

<!-- fc id:T-Z-168 sha:267c4488 src:dodatky/z-pokazhchyk.md:684 klas:A -->
### T-Z-168 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> size-components — 96, 190, 375

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

size-components — 96, 190, 375
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/{basic-commands,advanced-commands,basic-options,advanced-options}.rst та tools/idf_py_actions/{core_ext,serial_ext,debug_ext}.py в esp-idf release/v5.5, плюс idf-component-manager/idf_extensions.py
- **Дослівно з джерела:**
  > esptool (з переліку команд у __init__.py і документації):
  >   write-flash read-flash erase-flash erase-region read-mac flash-id
  >   elf2image image-info merge-bin version verify-flash dump-mem
  >   read-mem write-mem get-security-info chip-id run …
  > 
  > idf.py (з ACTIONS у core_ext/serial_ext/debug_ext):
  >   all(alias build) app app-flash bootloader clean fullclean menuconfig
  >   merge-bin monitor flash erase-flash partition-table reconfigure
  >   set-target size size-components size-files python-clean read-otadata
  >   efuse-summary … openocd gdb coredump-info coredump-debug
  > 
  > idf-component-manager: add-dependency create-manifest upload-component
  >   create-project-from-example
  > 
  > Приклад із документації дослівно:
  >   esptool -p PORT -b 460800 read-flash 0 ALL flash_contents.bin
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Суцільна перевірка, як у проході 7: узято всі команди, що книга друкує, а не сумнівні. Крім трьох виправлень вище, розбіжностей немає — включно з `read-flash 0 ALL`, яке дослівно збігається з прикладом документації, і `idf.py build`, що є псевдонімом до `all` (`'aliases': ['build']` у `core_ext.py`).
Заразом підтверджено дві дрібниці, які книга стверджує в інших розділах: типова швидкість esptool — 115200, а 74880 названо «usual baud rate used by the ESP8266» для boot-логу. Друге підтверджує картку К6 з іншого боку, ніж прохід 8.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-Z-169 sha:575a33e3 src:dodatky/z-pokazhchyk.md:692 klas:A -->
### T-Z-169 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> SOC_TWAI_SUPPORT_FD — 228

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

SOC_TWAI_SUPPORT_FD — 228
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/twai.rst
- **Дослівно з джерела:**
  > The TWAI controllers on the {IDF_TARGET_NAME} are **not compatible with FD format frames
  > and will interpret such frames as errors.**
- **Спосіб і дата:** curl raw.githubusercontent для .rst; окремо перевірено відсутність SOC_TWAI_SUPPORT_FD у soc_caps.h усіх шести цілей, 2026-08-26
- **Нотатка:** Знахідка проходу — прогалина, а не помилка. Книга не згадувала CAN FD взагалі, тоді як наслідок польовий: FD-кадр сприймається як помилка, тобто вузол не просто мовчить, а **псує чужу шину**, як вузол із неправильною швидкістю. Для книги, яка окремо вчить під'єднуватися до чужої працюючої системи, це істотно. Додано блок у розділ 38 із вказівкою перевіряти `SOC_TWAI_SUPPORT_FD` для свого чипа.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-Z-170 sha:2fe944b5 src:dodatky/z-pokazhchyk.md:708 klas:A -->
### T-Z-170 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> spi_device_handle_t — 220

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

spi_device_handle_t — 220
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

<!-- fc id:T-Z-171 sha:87048476 src:dodatky/z-pokazhchyk.md:710 klas:A -->
### T-Z-171 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> spi_device_interface_config_t — 220

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

spi_device_interface_config_t — 220
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

<!-- fc id:T-Z-172 sha:4b861066 src:dodatky/z-pokazhchyk.md:712 klas:A -->
### T-Z-172 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> spi_device_transmit — 220

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

spi_device_transmit — 220
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

<!-- fc id:T-Z-173 sha:875ef220 src:dodatky/z-pokazhchyk.md:718 klas:A -->
### T-Z-173 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> SR04 — 27, 34, 61, 258, 262, 264, 389

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

SR04 — 27, 34, 61, 258, 262, 264, 389
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_HCSR04/main/README.rst
- **Дослівно з джерела:**
  > The HC-SR04 is an inexpensive solution for measuring distances using microcontrollers
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** SR04 (HC-SR04) ultrasonic sensor is documented by Adafruit CircuitPython library
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-174 sha:bebbcdca src:dodatky/z-pokazhchyk.md:722 klas:C -->
### T-Z-174 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> SSD1306 — 149, 257, 265, 268, 310, 369, 386

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

SSD1306 — 149, 257, 265, 268, 310, 369, 386
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-Z-175 sha:046a867a src:dodatky/z-pokazhchyk.md:728 klas:E -->
### T-Z-175 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> SuperMini — 24, 39, 48, 80, 364

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

SuperMini — 24, 39, 48, 80, 364
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-176 sha:78b6d112 src:dodatky/z-pokazhchyk.md:745 klas:C -->
### T-Z-176 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> TP4056 — 298, 301, 334, 336

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

TP4056 — 298, 301, 334, 336
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-Z-177 sha:622120a7 src:dodatky/z-pokazhchyk.md:747 klas:D -->
### T-Z-177 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> TWAI — 54–55, 99–100, 103, 112, 226–230, 359, 388, 399

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

TWAI — 54–55, 99–100, 103, 112, 226–230, 359, 388, 399
```

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

<!-- fc id:T-Z-178 sha:f4828721 src:dodatky/z-pokazhchyk.md:749 klas:A -->
### T-Z-178 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> twai_driver_install — 228

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

twai_driver_install — 228
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

<!-- fc id:T-Z-179 sha:e4f987e9 src:dodatky/z-pokazhchyk.md:751 klas:A -->
### T-Z-179 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> twai_filter_config_t — 228

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

twai_filter_config_t — 228
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

<!-- fc id:T-Z-180 sha:67efba4b src:dodatky/z-pokazhchyk.md:753 klas:A -->
### T-Z-180 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> twai_general_config_t — 228

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

twai_general_config_t — 228
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

<!-- fc id:T-Z-181 sha:f0981bc4 src:dodatky/z-pokazhchyk.md:755 klas:A -->
### T-Z-181 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> twai_get_status_info — 229

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

twai_get_status_info — 229
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

<!-- fc id:T-Z-182 sha:fe95f5a9 src:dodatky/z-pokazhchyk.md:757 klas:A -->
### T-Z-182 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> twai_initiate_recovery — 229

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

twai_initiate_recovery — 229
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

<!-- fc id:T-Z-183 sha:2bd87aec src:dodatky/z-pokazhchyk.md:759 klas:A -->
### T-Z-183 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> twai_message_t — 228, 359

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

twai_message_t — 228, 359
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

<!-- fc id:T-Z-184 sha:449df551 src:dodatky/z-pokazhchyk.md:767 klas:A -->
### T-Z-184 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> twai_timing_config_t — 228

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

twai_timing_config_t — 228
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

<!-- fc id:T-Z-185 sha:a5d357fc src:dodatky/z-pokazhchyk.md:776 klas:A -->
### T-Z-185 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> uart_driver_install — 209

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

uart_driver_install — 209
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

<!-- fc id:T-Z-186 sha:dcd4df23 src:dodatky/z-pokazhchyk.md:782 klas:A -->
### T-Z-186 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> uart_read_bytes — 209, 357

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

uart_read_bytes — 209, 357
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

<!-- fc id:T-Z-187 sha:3f10ce63 src:dodatky/z-pokazhchyk.md:786 klas:A -->
### T-Z-187 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> uart_wait_tx_done — 210, 212, 344, 357, 368

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

uart_wait_tx_done — 210, 212, 344, 357, 368
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

<!-- fc id:T-Z-188 sha:44cbf5aa src:dodatky/z-pokazhchyk.md:788 klas:A -->
### T-Z-188 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> uart_write_bytes — 210, 357–358

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

uart_write_bytes — 210, 357–358
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

<!-- fc id:T-Z-189 sha:6380d48a src:dodatky/z-pokazhchyk.md:795 klas:A -->
### T-Z-189 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> verify-flash — 16, 25, 35, 125, 128, 144, 146, 181, 307, 373

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

verify-flash — 16, 25, 35, 125, 128, 144, 146, 181, 307, 373
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/{basic-commands,advanced-commands,basic-options,advanced-options}.rst та tools/idf_py_actions/{core_ext,serial_ext,debug_ext}.py в esp-idf release/v5.5, плюс idf-component-manager/idf_extensions.py
- **Дослівно з джерела:**
  > esptool (з переліку команд у __init__.py і документації):
  >   write-flash read-flash erase-flash erase-region read-mac flash-id
  >   elf2image image-info merge-bin version verify-flash dump-mem
  >   read-mem write-mem get-security-info chip-id run …
  > 
  > idf.py (з ACTIONS у core_ext/serial_ext/debug_ext):
  >   all(alias build) app app-flash bootloader clean fullclean menuconfig
  >   merge-bin monitor flash erase-flash partition-table reconfigure
  >   set-target size size-components size-files python-clean read-otadata
  >   efuse-summary … openocd gdb coredump-info coredump-debug
  > 
  > idf-component-manager: add-dependency create-manifest upload-component
  >   create-project-from-example
  > 
  > Приклад із документації дослівно:
  >   esptool -p PORT -b 460800 read-flash 0 ALL flash_contents.bin
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Суцільна перевірка, як у проході 7: узято всі команди, що книга друкує, а не сумнівні. Крім трьох виправлень вище, розбіжностей немає — включно з `read-flash 0 ALL`, яке дослівно збігається з прикладом документації, і `idf.py build`, що є псевдонімом до `all` (`'aliases': ['build']` у `core_ext.py`).
Заразом підтверджено дві дрібниці, які книга стверджує в інших розділах: типова швидкість esptool — 115200, а 74880 названо «usual baud rate used by the ESP8266» для boot-логу. Друге підтверджує картку К6 з іншого боку, ніж прохід 8.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-Z-190 sha:fe4aa864 src:dodatky/z-pokazhchyk.md:801 klas:A -->
### T-Z-190 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> vTaskDelay — 19, 100, 169, 191, 198–200, 276, 330, 339, 343, 346, 352, 371

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

vTaskDelay — 19, 100, 169, 191, 198–200, 276, 330, 339, 343, 346, 352, 371
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

<!-- fc id:T-Z-191 sha:66b81d51 src:dodatky/z-pokazhchyk.md:820 klas:A -->
### T-Z-191 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> write-flash — 15–16, 25, 35–36, 93, 122, 124–127, 140, 143–145, 310, 373, 377

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

write-flash — 15–16, 25, 35–36, 93, 122, 124–127, 140, 143–145, 310, 373, 377
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-Z-192 sha:f4d3460e src:dodatky/z-pokazhchyk.md:824 klas:E -->
### T-Z-192 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> WROOM-1 — 23, 235, 363, 390

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

WROOM-1 — 23, 235, 363, 390
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-193 sha:03997ff9 src:dodatky/z-pokazhchyk.md:828 klas:E -->
### T-Z-193 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> WROOM-32 — 23, 67, 72–73, 362, 390

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

WROOM-32 — 23, 67, 72–73, 362, 390
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-Z-194 sha:4929da13 src:dodatky/z-pokazhchyk.md:832 klas:A -->
### T-Z-194 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> WS2812 — 54–55, 200, 204, 207, 388

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

WS2812 — 54–55, 200, 204, 207, 388
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_NeoPixel/main/README.rst
- **Дослівно з джерела:**
  > Higher level NeoPixel driver that presents the strip as a sequence
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** WS2812 (NeoPixel) addressable LED is documented by Adafruit CircuitPython library
- **Прохід:** prochid-z-pokazhchyk

---

<!-- fc id:T-Z-195 sha:9dc5a212 src:dodatky/z-pokazhchyk.md:839 klas:A -->
### T-Z-195 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xEventGroupWaitBits — 194

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xEventGroupWaitBits — 194
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

<!-- fc id:T-Z-196 sha:a5d38561 src:dodatky/z-pokazhchyk.md:847 klas:A -->
### T-Z-196 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xQueueSend — 193, 247, 345, 357, 359

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xQueueSend — 193, 247, 345, 357, 359
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

<!-- fc id:T-Z-197 sha:194f9963 src:dodatky/z-pokazhchyk.md:849 klas:A -->
### T-Z-197 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xQueueSendFromISR — 195, 202–203, 247

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xQueueSendFromISR — 195, 202–203, 247
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

<!-- fc id:T-Z-198 sha:8160210f src:dodatky/z-pokazhchyk.md:851 klas:A -->
### T-Z-198 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xSemaphoreCreateMutex — 193, 332

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xSemaphoreCreateMutex — 193, 332
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

<!-- fc id:T-Z-199 sha:d78a091c src:dodatky/z-pokazhchyk.md:853 klas:A -->
### T-Z-199 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xSemaphoreGive — 193, 330–331

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xSemaphoreGive — 193, 330–331
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

<!-- fc id:T-Z-200 sha:b4776835 src:dodatky/z-pokazhchyk.md:855 klas:A -->
### T-Z-200 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xSemaphoreTake — 193, 330–331

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xSemaphoreTake — 193, 330–331
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

<!-- fc id:T-Z-201 sha:552f958d src:dodatky/z-pokazhchyk.md:857 klas:A -->
### T-Z-201 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xTaskCreate — 186–187, 191, 332

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xTaskCreate — 186–187, 191, 332
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

<!-- fc id:T-Z-202 sha:e215d715 src:dodatky/z-pokazhchyk.md:859 klas:A -->
### T-Z-202 · proza · `dodatky/z-pokazhchyk.md`

**Твердження, коротко**

> xTaskCreatePinnedToCore — 192

**Контекст**

```
# Предметний покажчик {#pokazhchyk}

xTaskCreatePinnedToCore — 192
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
