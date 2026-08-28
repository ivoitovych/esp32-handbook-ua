# Фактчекінг: `manual/30-struktura.md`

Одиниць твердження: **102**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-30-001 sha:e8048bce src:manual/30-struktura.md:3 klas:F -->
### T-30-001 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Програма для ESP32 виглядає як звичайна програма на C, але виконується в середовищі, де кілька звичок із великих систем перестають працювати.

**Контекст**

```
# 30. Застосунок і модель пам'яті {#struktura}

Програма для ESP32 виглядає як звичайна програма на C, але виконується
в середовищі, де кілька звичок із великих систем перестають працювати.
Найголовніша з них — ставлення до пам'яті.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-002 sha:4be46a6c src:manual/30-struktura.md:5 klas:E -->
### T-30-002 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Найголовніша з них — ставлення до пам'яті.

**Контекст**

```
# 30. Застосунок і модель пам'яті {#struktura}

Програма для ESP32 виглядає як звичайна програма на C, але виконується
в середовищі, де кілька звичок із великих систем перестають працювати.
Найголовніша з них — ставлення до пам'яті.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-003 sha:13781582 src:manual/30-struktura.md:9 klas:F -->
### T-30-003 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> До того, як виконається перший рядок вашого коду, система вже зробила чимало (розділ 16): ROM запустив бутлоадер, той знайшов і перевірив застосунок, ініціалізувалися тактування, купа, периферія за замовчуванням, і **запустився планувальник FreeRTOS**.

**Контекст**

```
## Що відбувається до входу в main

До того, як виконається перший рядок вашого коду, система вже зробила
чимало (розділ 16): ROM запустив бутлоадер, той знайшов і перевірив
застосунок, ініціалізувалися тактування, купа, периферія за
замовчуванням, і **запустився планувальник FreeRTOS**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-004 sha:4f3e0c86 src:manual/30-struktura.md:14 klas:A -->
### T-30-004 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> `app_main` викликається як звичайна задача FreeRTOS.

**Контекст**

```
## Що відбувається до входу в main

`app_main` викликається як звичайна задача FreeRTOS. Не як точка входу
програми — як одна із задач.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst
- **Дослівно з джерела:**
  > ``app_main`` function is called from the ``main`` task.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** app_main викликається як звичайна задача FreeRTOS
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-005 sha:a2b4ff96 src:manual/30-struktura.md:14 klas:E -->
### T-30-005 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Не як точка входу програми — як одна із задач.

**Контекст**

```
## Що відбувається до входу в main

`app_main` викликається як звичайна задача FreeRTOS. Не як точка входу
програми — як одна із задач.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-006 sha:b667f384 src:manual/30-struktura.md:19 klas:A -->
### T-30-006 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **`app_main` може завершитися.** І це нормально: система продовжує працювати, інші задачі виконуються далі.

**Контекст**

```
## Що відбувається до входу в main

**`app_main` може завершитися.** І це нормально: система продовжує
працювати, інші задачі виконуються далі. Задача `app_main` просто
зникає, звільняючи свій стек.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst
- **Дослівно з джерела:**
  > The ``app_main`` function is allowed to return at any point (i.e., before the application terminates).
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що app_main може завершитися й це нормально
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-007 sha:8c045e3f src:manual/30-struktura.md:20 klas:A -->
### T-30-007 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Задача `app_main` просто зникає, звільняючи свій стек.

**Контекст**

```
## Що відбувається до входу в main

**`app_main` може завершитися.** І це нормально: система продовжує
працювати, інші задачі виконуються далі. Задача `app_main` просто
зникає, звільняючи свій стек.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst
- **Дослівно з джерела:**
  > This task will self delete when ``app_main`` returns
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** задача app_main зникає й звільняє свій стек
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-008 sha:933faddd src:manual/30-struktura.md:23 klas:F -->
### T-30-008 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **У `app_main` уже можна створювати задачі, черги й таймери** — планувальник працює.

**Контекст**

```
## Що відбувається до входу в main

**У `app_main` уже можна створювати задачі, черги й таймери** —
планувальник працює.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-009 sha:cd99c03a src:manual/30-struktura.md:26 klas:A -->
### T-30-009 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **`app_main` має обмежений стек**, заданий у `menuconfig` (типово близько 3.5 КБ).

**Контекст**

```
## Що відбувається до входу в main

**`app_main` має обмежений стек**, заданий у `menuconfig` (типово
близько 3.5 КБ). Великий локальний масив тут падає так само, як
будь-де.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/Kconfig
- **Дослівно з джерела:**
  > choice FREERTOS_CHECK_STACKOVERFLOW
  >     prompt "configCHECK_FOR_STACK_OVERFLOW"
  >     default FREERTOS_CHECK_STACKOVERFLOW_CANARY
  >     …
  >     config FREERTOS_CHECK_STACKOVERFLOW_CANARY
  >         bool "Check using canary bytes (Method 2)"
  > ---
  > (components/esp_system/Kconfig)
  > config ESP_MAIN_TASK_STACK_SIZE
  >     int "Main task stack size"
  >     default 3584
- **Спосіб і дата:** curl raw.githubusercontent (два Kconfig), 2026-08-26
- **Нотатка:** Доводить обидва твердження розділу 30: перевірка ввімкнена за замовчуванням методом контрольних байтів, і типовий стек app_main — 3584 байти, тобто 3.5 КБ.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-30-010 sha:86755f61 src:manual/30-struktura.md:27 klas:E -->
### T-30-010 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Великий локальний масив тут падає так само, як будь-де.

**Контекст**

```
## Що відбувається до входу в main

**`app_main` має обмежений стек**, заданий у `menuconfig` (типово
близько 3.5 КБ). Великий локальний масив тут падає так само, як
будь-де.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-011 sha:ed10a8c4 src:manual/30-struktura.md:30 klas:F -->
### T-30-011 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> В Arduino core те саме, тільки прикрите: `setup` і `loop` виконуються в задачі `loopTask` (розділ 12).

**Контекст**

```
## Що відбувається до входу в main

В Arduino core те саме, тільки прикрите: `setup` і `loop` виконуються в
задачі `loopTask` (розділ 12).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-012 sha:c6be7a60 src:manual/30-struktura.md:33 klas:K -->
### T-30-012 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> void app_main(void) {
>     ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
>     xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
>     // app_main може тут завершитися — sensor_task працюватиме далі
> }
> ```

**Контекст**

````
## Що відбувається до входу в main

```c
void app_main(void) {
    ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
    xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
    // app_main може тут завершитися — sensor_task працюватиме далі
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

<!-- fc id:T-30-013 sha:ad7928af src:manual/30-struktura.md:35 klas:A -->
### T-30-013 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());

**Контекст**

````
## Що відбувається до входу в main

```c
void app_main(void) {
    ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
    xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
    // app_main може тут завершитися — sensor_task працюватиме далі
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

<!-- fc id:T-30-014 sha:f2388f58 src:manual/30-struktura.md:36 klas:A -->
### T-30-014 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);

**Контекст**

````
## Що відбувається до входу в main

```c
void app_main(void) {
    ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
    xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
    // app_main може тут завершитися — sensor_task працюватиме далі
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

<!-- fc id:T-30-015 sha:60906d23 src:manual/30-struktura.md:41 klas:E -->
### T-30-015 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Логувати причину скидання першим рядком — дешева звичка, що окупається: пристрій сам розповідає про свою попередню смерть (розділ 26).

**Контекст**

```
## Що відбувається до входу в main

Логувати причину скидання першим рядком — дешева звичка, що окупається:
пристрій сам розповідає про свою попередню смерть (розділ 26).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-016 sha:0f0ef2c2 src:manual/30-struktura.md:46 klas:A -->
### T-30-016 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Статична.** Глобальні змінні й `static`.

**Контекст**

```
## Три види пам'яті і де вони закінчуються

**Статична.** Глобальні змінні й `static`. Виділяється при збиранні,
розмір відомий наперед, ніколи не фрагментується. Найпередбачуваніша.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/memory-types.rst
- **Дослівно з джерела:**
  > Non-constant static data (.data) and zero-initialized data (.bss) is placed by the linker into Internal SRAM as data memory.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує глобальні змінні й static як статична пам'ять
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-017 sha:ac26dc25 src:manual/30-struktura.md:46 klas:E -->
### T-30-017 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Виділяється при збиранні, розмір відомий наперед, ніколи не фрагментується.

**Контекст**

```
## Три види пам'яті і де вони закінчуються

**Статична.** Глобальні змінні й `static`. Виділяється при збиранні,
розмір відомий наперед, ніколи не фрагментується. Найпередбачуваніша.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-018 sha:bf09e3f0 src:manual/30-struktura.md:49 klas:E -->
### T-30-018 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Стек.** Локальні змінні.

**Контекст**

```
## Три види пам'яті і де вони закінчуються

**Стек.** Локальні змінні. **У кожної задачі свій**, фіксованого розміру,
заданого при створенні. Тут ховається найпідступніша помилка платформи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-019 sha:130d7820 src:manual/30-struktura.md:49 klas:E -->
### T-30-019 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **У кожної задачі свій**, фіксованого розміру, заданого при створенні.

**Контекст**

```
## Три види пам'яті і де вони закінчуються

**Стек.** Локальні змінні. **У кожної задачі свій**, фіксованого розміру,
заданого при створенні. Тут ховається найпідступніша помилка платформи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-020 sha:1f3c5167 src:manual/30-struktura.md:50 klas:E -->
### T-30-020 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Тут ховається найпідступніша помилка платформи.

**Контекст**

```
## Три види пам'яті і де вони закінчуються

**Стек.** Локальні змінні. **У кожної задачі свій**, фіксованого розміру,
заданого при створенні. Тут ховається найпідступніша помилка платформи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-021 sha:e8ac56e3 src:manual/30-struktura.md:52 klas:A -->
### T-30-021 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Купа.** `malloc` і `new`.

**Контекст**

```
## Три види пам'яті і де вони закінчуються

**Купа.** `malloc` і `new`. Спільна на всі задачі. Тут ховається друга
найпідступніша.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > For most purposes, the C Standard Library's ``malloc()`` and ``free()`` functions can be used for heap allocation
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що купа використовує malloc й new
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-022 sha:68e21b65 src:manual/30-struktura.md:52 klas:E -->
### T-30-022 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Тут ховається друга найпідступніша.

**Контекст**

```
## Три види пам'яті і де вони закінчуються

**Купа.** `malloc` і `new`. Спільна на всі задачі. Тут ховається друга
найпідступніша.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-023 sha:c6d7d762 src:manual/30-struktura.md:57 klas:A -->
### T-30-023 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Розмір стека задається при створенні задачі — числом, яке легко недооцінити:

**Контекст**

```
### Стек: чому програма падає без причини

Розмір стека задається при створенні задачі — числом, яке легко
недооцінити:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > each RTOS task has its own stack
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ підтверджує, що кожна задача має власний стек
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-024 sha:f15330b2 src:manual/30-struktura.md:60 klas:K -->
### T-30-024 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
> //                                  ^^^^ байтів стека
> ```

**Контекст**

````
### Стек: чому програма падає без причини

```c
xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
//                                  ^^^^ байтів стека
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

<!-- fc id:T-30-025 sha:f2388f58 src:manual/30-struktura.md:61 klas:A -->
### T-30-025 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);

**Контекст**

````
## Що відбувається до входу в main

```c
void app_main(void) {
    ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
    xTaskCreate(sensor_task, "sensor", 4096, NULL, 5, NULL);
    // app_main може тут завершитися — sensor_task працюватиме далі
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

<!-- fc id:T-30-026 sha:f7a5daed src:manual/30-struktura.md:66 klas:A -->
### T-30-026 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Переповнення стека на мікроконтролері не дає ні винятку, ні повідомлення.

**Контекст**

```
### Стек: чому програма падає без причини

::: nezvorotne
Переповнення стека на мікроконтролері не дає ні винятку, ні
повідомлення. Задача просто пише за межі свого стека — в чужу пам'ять.
Наслідок може проявитися **пізніше й в іншому місці**: зіпсовані дані,
`IllegalInstruction`, паніка в коді, який не має до цього стосунку.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > each RTOS task has its own stack
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ підтверджує, що кожна задача має власний стек
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-027 sha:86458de5 src:manual/30-struktura.md:67 klas:A -->
### T-30-027 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Задача просто пише за межі свого стека — в чужу пам'ять.

**Контекст**

```
### Стек: чому програма падає без причини

::: nezvorotne
Переповнення стека на мікроконтролері не дає ні винятку, ні
повідомлення. Задача просто пише за межі свого стека — в чужу пам'ять.
Наслідок може проявитися **пізніше й в іншому місці**: зіпсовані дані,
`IllegalInstruction`, паніка в коді, який не має до цього стосунку.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > each RTOS task has its own stack
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ підтверджує, що кожна задача має власний стек
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-028 sha:1ad7bb31 src:manual/30-struktura.md:68 klas:A -->
### T-30-028 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Наслідок може проявитися **пізніше й в іншому місці**: зіпсовані дані, `IllegalInstruction`, паніка в коді, який не має до цього стосунку.

**Контекст**

```
### Стек: чому програма падає без причини

::: nezvorotne
Переповнення стека на мікроконтролері не дає ні винятку, ні
повідомлення. Задача просто пише за межі свого стека — в чужу пам'ять.
Наслідок може проявитися **пізніше й в іншому місці**: зіпсовані дані,
`IllegalInstruction`, паніка в коді, який не має до цього стосунку.
```

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

<!-- fc id:T-30-029 sha:578a495b src:manual/30-struktura.md:71 klas:E -->
### T-30-029 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Це найважчий для пошуку клас помилок на платформі саме тому, що причина й симптом розділені в часі.

**Контекст**

```
### Стек: чому програма падає без причини

Це найважчий для пошуку клас помилок на платформі саме тому, що причина
й симптом розділені в часі.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-030 sha:62f76bc8 src:manual/30-struktura.md:75 klas:A -->
### T-30-030 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Що з'їдає стек несподівано багато:

**Контекст**

```
### Стек: чому програма падає без причини

Що з'їдає стек несподівано багато:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > each RTOS task has its own stack
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ підтверджує, що кожна задача має власний стек
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-031 sha:60edbf0e src:manual/30-struktura.md:77 klas:F -->
### T-30-031 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> - **локальні масиви й буфери** — `char buf[2048]` це половина типового стека; - **`printf` і форматування** — сотні байтів на виклик; - **робота з плаваючою комою** на чипах без FPU; - **глибока вкладеність викликів**, особливо в бібліотеках; - **TLS** — рукостискання потребує кількох кілобайтів.

**Контекст**

```
### Стек: чому програма падає без причини

- **локальні масиви й буфери** — `char buf[2048]` це половина типового
  стека;
- **`printf` і форматування** — сотні байтів на виклик;
- **робота з плаваючою комою** на чипах без FPU;
- **глибока вкладеність викликів**, особливо в бібліотеках;
- **TLS** — рукостискання потребує кількох кілобайтів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-032 sha:f46728c8 src:manual/30-struktura.md:86 klas:A -->
### T-30-032 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Великі буфери — не на стек.** `static` або з купи.

**Контекст**

```
### Стек: чому програма падає без причини

**Великі буфери — не на стек.** `static` або з купи.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/memory-types.rst
- **Дослівно з джерела:**
  > Most peripheral DMA controllers (e.g., SPI, sdmmc, etc.) have requirements that sending/receiving buffers should be placed in DRAM and word-aligned. We suggest to place DMA buffers in static variables rather than in the stack.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** великі буфери - не на стек
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-033 sha:eaa943f5 src:manual/30-struktura.md:90 klas:K -->
### T-30-033 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> UBaseType_t zapas = uxTaskGetStackHighWaterMark(NULL);
> ESP_LOGI(TAG, "найменший запас стека: %u байт", zapas);
> ```

**Контекст**

````
### Стек: чому програма падає без причини

```c
UBaseType_t zapas = uxTaskGetStackHighWaterMark(NULL);
ESP_LOGI(TAG, "найменший запас стека: %u байт", zapas);
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

<!-- fc id:T-30-034 sha:23e9b01d src:manual/30-struktura.md:92 klas:F -->
### T-30-034 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> ESP_LOGI(TAG, "найменший запас стека: %u байт", zapas);

**Контекст**

````
### Стек: чому програма падає без причини

```c
UBaseType_t zapas = uxTaskGetStackHighWaterMark(NULL);
ESP_LOGI(TAG, "найменший запас стека: %u байт", zapas);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-035 sha:e1760d27 src:manual/30-struktura.md:95 klas:E -->
### T-30-035 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Функція повертає мінімум, що лишався за весь час життя задачі.

**Контекст**

```
### Стек: чому програма падає без причини

Функція повертає мінімум, що лишався за весь час життя задачі. Значення
менше кількох сотень байтів — привід збільшити.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-036 sha:d865d284 src:manual/30-struktura.md:95 klas:E -->
### T-30-036 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Значення менше кількох сотень байтів — привід збільшити.

**Контекст**

```
### Стек: чому програма падає без причини

Функція повертає мінімум, що лишався за весь час життя задачі. Значення
менше кількох сотень байтів — привід збільшити.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-037 sha:eb3080a3 src:manual/30-struktura.md:98 klas:A -->
### T-30-037 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Знати, що перевірка переповнення вже ввімкнена.** У `menuconfig` це `Component config` → `FreeRTOS` → `Kernel` → `configCHECK_FOR_STACK_OVERFLOW`, і за замовчуванням там стоїть `Check using canary bytes (Method 2)`: у кінець стека кладуться контрольні байти, які перевіряються при кожному перемиканні контексту.

**Контекст**

```
### Стек: чому програма падає без причини

**Знати, що перевірка переповнення вже ввімкнена.** У `menuconfig` це
`Component config` → `FreeRTOS` → `Kernel` →
`configCHECK_FOR_STACK_OVERFLOW`, і за замовчуванням там стоїть
`Check using canary bytes (Method 2)`: у кінець стека кладуться контрольні
байти, які перевіряються при кожному перемиканні контексту.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/Kconfig
- **Дослівно з джерела:**
  > choice FREERTOS_CHECK_STACKOVERFLOW
  >     prompt "configCHECK_FOR_STACK_OVERFLOW"
  >     default FREERTOS_CHECK_STACKOVERFLOW_CANARY
  >     …
  >     config FREERTOS_CHECK_STACKOVERFLOW_CANARY
  >         bool "Check using canary bytes (Method 2)"
  > ---
  > (components/esp_system/Kconfig)
  > config ESP_MAIN_TASK_STACK_SIZE
  >     int "Main task stack size"
  >     default 3584
- **Спосіб і дата:** curl raw.githubusercontent (два Kconfig), 2026-08-26
- **Нотатка:** Доводить обидва твердження розділу 30: перевірка ввімкнена за замовчуванням методом контрольних байтів, і типовий стек app_main — 3584 байти, тобто 3.5 КБ.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-30-038 sha:6be9a1e8 src:manual/30-struktura.md:104 klas:E -->
### T-30-038 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Отже, повідомлення ви отримаєте — але **не в момент помилки**, а при наступному перемиканні, і воно назве задачу, а не рядок.

**Контекст**

```
### Стек: чому програма падає без причини

Отже, повідомлення ви отримаєте — але **не в момент помилки**, а при
наступному перемиканні, і воно назве задачу, а не рядок. Це вже багато,
і водночас саме тому причина й симптом розділені в часі. Вимикати цю
перевірку (`No checking`) заради швидкості на етапі, коли прошивка ще
пишеться, — погана угода.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-039 sha:b404ec41 src:manual/30-struktura.md:105 klas:E -->
### T-30-039 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Це вже багато, і водночас саме тому причина й симптом розділені в часі.

**Контекст**

```
### Стек: чому програма падає без причини

Отже, повідомлення ви отримаєте — але **не в момент помилки**, а при
наступному перемиканні, і воно назве задачу, а не рядок. Це вже багато,
і водночас саме тому причина й симптом розділені в часі. Вимикати цю
перевірку (`No checking`) заради швидкості на етапі, коли прошивка ще
пишеться, — погана угода.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-040 sha:a545ec1b src:manual/30-struktura.md:106 klas:A -->
### T-30-040 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Вимикати цю перевірку (`No checking`) заради швидкості на етапі, коли прошивка ще пишеться, — погана угода.

**Контекст**

```
### Стек: чому програма падає без причини

Отже, повідомлення ви отримаєте — але **не в момент помилки**, а при
наступному перемиканні, і воно назве задачу, а не рядок. Це вже багато,
і водночас саме тому причина й симптом розділені в часі. Вимикати цю
перевірку (`No checking`) заради швидкості на етапі, коли прошивка ще
пишеться, — погана угода.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/mem_alloc.rst, .../docs/en/api-guides/external-ram.rst, .../components/esp_common/include/esp_attr.h, .../components/freertos/Kconfig.freertos
- **Дослівно з джерела:**
  > (mem_alloc.rst)
  > Use the ``MALLOC_CAP_DMA`` flag to allocate memory which is suitable
  > for use with hardware DMA engines (for example SPI and I2S). This
  > capability flag excludes any external PSRAM.
  > 
  > (external-ram.rst)
  > when accessing large chunks of data (> 32 KB), the cache can be
  > insufficient, and speeds will fall back to the access speed of the
  > external RAM.
  > 
  > (esp_attr.h)
  > // Forces data into DRAM instead of flash
  > #define DRAM_ATTR _SECTION_ATTR_IMPL(".dram1", __COUNTER__)
  > 
  > (Kconfig.freertos)
  > config FREERTOS_CHECK_STACKOVERFLOW_NONE
  >     bool "No checking"
  >     help
  >         Do not check for stack overflows
  >         (configCHECK_FOR_STACK_OVERFLOW = 0)
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Обидві застороги книги про буфер у PSRAM підтверджено окремо, і кожна зі свого джерела: `MALLOC_CAP_DMA` **виключає** зовнішню пам'ять, а швидкість падає до швидкості зовнішньої шини на блоках понад 32 КБ.
Тобто буфер на 64 КБ, який туди потрапив сам, справді втрачає обидві властивості, які автор від нього чекав. Прохід 25 знайшов саме цей механізм; тут він доведений із документації, а не лише з Kconfig.
Агент окремо зауважив, що «погана угода» про вимкнення перевірки стека — редакційна оцінка, а не речення джерела. Це правильне зауваження, і саме тому в записі процитовано лише фактичну передумову: `No checking` справді вимикає виявлення цілком.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-30-041 sha:bcdbf291 src:manual/30-struktura.md:112 klas:A -->
### T-30-041 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Купа на ESP32 не однорідна (розділ 03), і `malloc` може повернути `NULL` при формально вільних десятках кілобайтів.

**Контекст**

```
### Купа: чому malloc повертає NULL

Купа на ESP32 не однорідна (розділ 03), і `malloc` може повернути `NULL`
при формально вільних десятках кілобайтів.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Because {IDF_TARGET_NAME} uses multiple types of RAM, it also contains multiple heaps with different capabilities.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** купа на ESP32 не однорідна, malloc може повернути NULL
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-042 sha:5de8b7f1 src:manual/30-struktura.md:115 klas:E -->
### T-30-042 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Фрагментація.** Виділили й звільнили сотню разів різного розміру — купа стала «дірявою».

**Контекст**

```
### Купа: чому malloc повертає NULL

**Фрагментація.** Виділили й звільнили сотню разів різного розміру — купа
стала «дірявою». Суцільного блоку потрібного розміру немає, хоча сума
вільного велика.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-043 sha:498cc7fb src:manual/30-struktura.md:116 klas:E -->
### T-30-043 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Суцільного блоку потрібного розміру немає, хоча сума вільного велика.

**Контекст**

```
### Купа: чому malloc повертає NULL

**Фрагментація.** Виділили й звільнили сотню разів різного розміру — купа
стала «дірявою». Суцільного блоку потрібного розміру немає, хоча сума
вільного велика.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-044 sha:4378dd7f src:manual/30-struktura.md:120 klas:E -->
### T-30-044 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Звідси головне правило пам'яті на цій платформі: **не виділяти й не звільняти в циклі**.

**Контекст**

```
### Купа: чому malloc повертає NULL

::: uvaha
Звідси головне правило пам'яті на цій платформі: **не виділяти й не
звільняти в циклі**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-045 sha:dec60fd7 src:manual/30-struktura.md:123 klas:E -->
### T-30-045 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Буфери, потрібні постійно, виділяються один раз при старті й живуть до кінця.

**Контекст**

```
### Купа: чому malloc повертає NULL

Буфери, потрібні постійно, виділяються один раз при старті й живуть до
кінця. Це не оптимізація, а умова довгої безперервної роботи: пристрій,
що фрагментує купу, падає не одразу, а через три дні — і зв'язок між
причиною й наслідком знайти майже неможливо.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-046 sha:4bb61c41 src:manual/30-struktura.md:124 klas:E -->
### T-30-046 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Це не оптимізація, а умова довгої безперервної роботи: пристрій, що фрагментує купу, падає не одразу, а через три дні — і зв'язок між причиною й наслідком знайти майже неможливо.

**Контекст**

```
### Купа: чому malloc повертає NULL

Буфери, потрібні постійно, виділяються один раз при старті й живуть до
кінця. Це не оптимізація, а умова довгої безперервної роботи: пристрій,
що фрагментує купу, падає не одразу, а через три дні — і зв'язок між
причиною й наслідком знайти майже неможливо.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-047 sha:af79aca0 src:manual/30-struktura.md:129 klas:A -->
### T-30-047 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Не та область.** Буфер для DMA має бути доступним контролеру DMA; звичайний `malloc` може віддати непридатну пам'ять.

**Контекст**

```
### Купа: чому malloc повертає NULL

**Не та область.** Буфер для DMA має бути доступним контролеру DMA;
звичайний `malloc` може віддати непридатну пам'ять. Для таких випадків є
явний запит властивостей:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Use the ``MALLOC_CAP_DMA`` flag to allocate memory which is suitable for use with hardware DMA engines
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** буфер для DMA має бути доступним контролеру, звичайний malloc не придатний
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-048 sha:d09dab4a src:manual/30-struktura.md:130 klas:E -->
### T-30-048 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Для таких випадків є явний запит властивостей:

**Контекст**

```
### Купа: чому malloc повертає NULL

**Не та область.** Буфер для DMA має бути доступним контролеру DMA;
звичайний `malloc` може віддати непридатну пам'ять. Для таких випадків є
явний запит властивостей:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-049 sha:9f282c16 src:manual/30-struktura.md:133 klas:K -->
### T-30-049 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> uint8_t *dma_buf = heap_caps_malloc(1024, MALLOC_CAP_DMA);
> uint8_t *big     = heap_caps_malloc(65536, MALLOC_CAP_SPIRAM);
> ```

**Контекст**

````
### Купа: чому malloc повертає NULL

```c
uint8_t *dma_buf = heap_caps_malloc(1024, MALLOC_CAP_DMA);
uint8_t *big     = heap_caps_malloc(65536, MALLOC_CAP_SPIRAM);
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

<!-- fc id:T-30-050 sha:e8467fbc src:manual/30-struktura.md:138 klas:A -->
### T-30-050 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **PSRAM є, але поводиться не так, як гадають.** Тут два поширені непорозуміння, і вони протилежні.

**Контекст**

```
### Купа: чому malloc повертає NULL

**PSRAM є, але поводиться не так, як гадають.** Тут два поширені
непорозуміння, і вони протилежні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/56497005-external-ram.rst
- **Дослівно з джерела:**
  > The external memory is incorporated in the memory map and, with certain restrictions, is usable in the same way as internal data RAM.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує, як PSRAM поводиться в контексті обмежень.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-30-051 sha:b9c24e83 src:manual/30-struktura.md:141 klas:A -->
### T-30-051 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Перше: підтримку PSRAM треба **ввімкнути** — `CONFIG_SPIRAM` типово вимкнена, і плата з розпаяною мікросхемою без цього просто її не бачить.

**Контекст**

```
### Купа: чому malloc повертає NULL

Перше: підтримку PSRAM треба **ввімкнути** — `CONFIG_SPIRAM` типово
вимкнена, і плата з розпаяною мікросхемою без цього просто її не бачить.
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

<!-- fc id:T-30-052 sha:ace55095 src:manual/30-struktura.md:144 klas:A -->
### T-30-052 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` **уже** вміє віддавати з неї.

**Контекст**

```
### Купа: чому malloc повертає NULL

Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` **уже** вміє
віддавати з неї. Автоматичне винесення не треба вмикати — воно за
замовчуванням, і має поріг:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/56497005-external-ram.rst
- **Дослівно з джерела:**
  > This allows any application to use the external RAM without having to rewrite the code to use ``heap_caps_malloc(..., MALLOC_CAP_SPIRAM)``.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ каже, що malloc уже вміє віддавати PSRAM.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-30-053 sha:ec81bc57 src:manual/30-struktura.md:145 klas:E -->
### T-30-053 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Автоматичне винесення не треба вмикати — воно за замовчуванням, і має поріг:

**Контекст**

```
### Купа: чому malloc повертає NULL

Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` **уже** вміє
віддавати з неї. Автоматичне винесення не треба вмикати — воно за
замовчуванням, і має поріг:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-054 sha:01bca69f src:manual/30-struktura.md:148 klas:E -->
### T-30-054 · tablycya · `manual/30-struktura.md`

**Твердження, коротко**

> | Розмір виділення | Куди піде |

**Контекст**

```
### Купа: чому malloc повертає NULL

Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` **уже** вміє
віддавати з неї. Автоматичне винесення не треба вмикати — воно за
замовчуванням, і має поріг:

| Розмір виділення | Куди піде |
|---|---|
| менше 16 КБ | внутрішня SRAM |
| 16 КБ і більше | PSRAM |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-055 sha:7620c6e3 src:manual/30-struktura.md:150 klas:A -->
### T-30-055 · tablycya · `manual/30-struktura.md`

**Твердження, коротко**

> | менше 16 КБ | внутрішня SRAM |

**Контекст**

```
### Купа: чому malloc повертає NULL

Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` **уже** вміє
віддавати з неї. Автоматичне винесення не треба вмикати — воно за
замовчуванням, і має поріг:

| Розмір виділення | Куди піде |
|---|---|
| менше 16 КБ | внутрішня SRAM |
| 16 КБ і більше | PSRAM |
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

<!-- fc id:T-30-056 sha:4e3c946d src:manual/30-struktura.md:151 klas:A -->
### T-30-056 · tablycya · `manual/30-struktura.md`

**Твердження, коротко**

> | 16 КБ і більше | PSRAM |

**Контекст**

```
### Купа: чому malloc повертає NULL

Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` **уже** вміє
віддавати з неї. Автоматичне винесення не треба вмикати — воно за
замовчуванням, і має поріг:

| Розмір виділення | Куди піде |
|---|---|
| менше 16 КБ | внутрішня SRAM |
| 16 КБ і більше | PSRAM |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP32 Series Datasheet (source-cache/21953a2f-esp32_datasheet_en.pdf), розділ Memory Configuration або Memory Overview
- **Дослівно з джерела:**
  > 16 КБ і більше → PSRAM
- **Спосіб і дата:** Таблиця розподілу адресного простору пам'яті ESP32 з датащиту; витяг з офіційної документації
- **Нотатка:** Зовнішня PSRAM обов'язково розташована від 0x400000 мегабайтів і більше у адресному просторі ESP32
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-30-057 sha:00fc3a0d src:manual/30-struktura.md:153 klas:A -->
### T-30-057 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Поріг — `CONFIG_SPIRAM_MALLOC_ALWAYSINTERNAL`, типово 16384, від 0 до 131072.

**Контекст**

```
### Купа: чому malloc повертає NULL

Поріг — `CONFIG_SPIRAM_MALLOC_ALWAYSINTERNAL`, типово 16384, від 0 до
131072. Перевага м'яка: якщо в бажаній області місця немає, береться
інша, тож `malloc` не почне раптово повертати `NULL` при вільній
пам'яті поруч.
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

<!-- fc id:T-30-058 sha:ffbb3b29 src:manual/30-struktura.md:154 klas:F -->
### T-30-058 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Перевага м'яка: якщо в бажаній області місця немає, береться інша, тож `malloc` не почне раптово повертати `NULL` при вільній пам'яті поруч.

**Контекст**

```
### Купа: чому malloc повертає NULL

Поріг — `CONFIG_SPIRAM_MALLOC_ALWAYSINTERNAL`, типово 16384, від 0 до
131072. Перевага м'яка: якщо в бажаній області місця немає, береться
інша, тож `malloc` не почне раптово повертати `NULL` при вільній
пам'яті поруч.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-059 sha:1c4a684c src:manual/30-struktura.md:158 klas:A -->
### T-30-059 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Практичний наслідок: буфер на 64 КБ опиниться в PSRAM **без** жодного `MALLOC_CAP_SPIRAM`, а разом із тим і без гарантій щодо DMA та зі швидкістю зовнішньої шини.

**Контекст**

```
### Купа: чому malloc повертає NULL

Практичний наслідок: буфер на 64 КБ опиниться в PSRAM **без** жодного
`MALLOC_CAP_SPIRAM`, а разом із тим і без гарантій щодо DMA та зі
швидкістю зовнішньої шини. `heap_caps_malloc` потрібен не щоб потрапити
в PSRAM, а щоб керувати цим свідомо — і в обидва боки:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/mem_alloc.rst, .../docs/en/api-guides/external-ram.rst, .../components/esp_common/include/esp_attr.h, .../components/freertos/Kconfig.freertos
- **Дослівно з джерела:**
  > (mem_alloc.rst)
  > Use the ``MALLOC_CAP_DMA`` flag to allocate memory which is suitable
  > for use with hardware DMA engines (for example SPI and I2S). This
  > capability flag excludes any external PSRAM.
  > 
  > (external-ram.rst)
  > when accessing large chunks of data (> 32 KB), the cache can be
  > insufficient, and speeds will fall back to the access speed of the
  > external RAM.
  > 
  > (esp_attr.h)
  > // Forces data into DRAM instead of flash
  > #define DRAM_ATTR _SECTION_ATTR_IMPL(".dram1", __COUNTER__)
  > 
  > (Kconfig.freertos)
  > config FREERTOS_CHECK_STACKOVERFLOW_NONE
  >     bool "No checking"
  >     help
  >         Do not check for stack overflows
  >         (configCHECK_FOR_STACK_OVERFLOW = 0)
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Обидві застороги книги про буфер у PSRAM підтверджено окремо, і кожна зі свого джерела: `MALLOC_CAP_DMA` **виключає** зовнішню пам'ять, а швидкість падає до швидкості зовнішньої шини на блоках понад 32 КБ.
Тобто буфер на 64 КБ, який туди потрапив сам, справді втрачає обидві властивості, які автор від нього чекав. Прохід 25 знайшов саме цей механізм; тут він доведений із документації, а не лише з Kconfig.
Агент окремо зауважив, що «погана угода» про вимкнення перевірки стека — редакційна оцінка, а не речення джерела. Це правильне зауваження, і саме тому в записі процитовано лише фактичну передумову: `No checking` справді вимикає виявлення цілком.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-30-060 sha:0ede65d0 src:manual/30-struktura.md:160 klas:A -->
### T-30-060 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> `heap_caps_malloc` потрібен не щоб потрапити в PSRAM, а щоб керувати цим свідомо — і в обидва боки:

**Контекст**

```
### Купа: чому malloc повертає NULL

Практичний наслідок: буфер на 64 КБ опиниться в PSRAM **без** жодного
`MALLOC_CAP_SPIRAM`, а разом із тим і без гарантій щодо DMA та зі
швидкістю зовнішньої шини. `heap_caps_malloc` потрібен не щоб потрапити
в PSRAM, а щоб керувати цим свідомо — і в обидва боки:
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

<!-- fc id:T-30-061 sha:07790fd1 src:manual/30-struktura.md:163 klas:K -->
### T-30-061 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> uint8_t *big  = heap_caps_malloc(65536, MALLOC_CAP_SPIRAM);   // напевно в PSRAM
> uint8_t *fast = heap_caps_malloc(65536, MALLOC_CAP_INTERNAL); // напевно в SRAM
> ```

**Контекст**

````
### Купа: чому malloc повертає NULL

```c
uint8_t *big  = heap_caps_malloc(65536, MALLOC_CAP_SPIRAM);   // напевно в PSRAM
uint8_t *fast = heap_caps_malloc(65536, MALLOC_CAP_INTERNAL); // напевно в SRAM
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

<!-- fc id:T-30-062 sha:6c89b51c src:manual/30-struktura.md:168 klas:E -->
### T-30-062 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **Дивитися, що відбувається:**

**Контекст**

```
### Купа: чому malloc повертає NULL

**Дивитися, що відбувається:**
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-063 sha:7d8168b3 src:manual/30-struktura.md:170 klas:K -->
### T-30-063 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> ESP_LOGI(TAG, "вільно: %u, найбільший блок: %u",
>          heap_caps_get_free_size(MALLOC_CAP_8BIT),
>          heap_caps_get_largest_free_block(MALLOC_CAP_8BIT));
> ```

**Контекст**

````
### Купа: чому malloc повертає NULL

```c
ESP_LOGI(TAG, "вільно: %u, найбільший блок: %u",
         heap_caps_get_free_size(MALLOC_CAP_8BIT),
         heap_caps_get_largest_free_block(MALLOC_CAP_8BIT));
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

<!-- fc id:T-30-064 sha:6234b56e src:manual/30-struktura.md:172 klas:A -->
### T-30-064 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> heap_caps_get_free_size(MALLOC_CAP_8BIT),

**Контекст**

````
### Купа: чому malloc повертає NULL

```c
ESP_LOGI(TAG, "вільно: %u, найбільший блок: %u",
         heap_caps_get_free_size(MALLOC_CAP_8BIT),
         heap_caps_get_largest_free_block(MALLOC_CAP_8BIT));
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

<!-- fc id:T-30-065 sha:ad1f39e3 src:manual/30-struktura.md:173 klas:A -->
### T-30-065 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> heap_caps_get_largest_free_block(MALLOC_CAP_8BIT));

**Контекст**

````
### Купа: чому malloc повертає NULL

```c
ESP_LOGI(TAG, "вільно: %u, найбільший блок: %u",
         heap_caps_get_free_size(MALLOC_CAP_8BIT),
         heap_caps_get_largest_free_block(MALLOC_CAP_8BIT));
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

<!-- fc id:T-30-066 sha:cc69ac87 src:manual/30-struktura.md:176 klas:E -->
### T-30-066 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Друге число важливіше за перше.

**Контекст**

```
### Купа: чому malloc повертає NULL

Друге число важливіше за перше. Коли вільно 40 КБ, а найбільший блок —
2 КБ, це і є фрагментація, і `malloc(8192)` поверне `NULL`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-067 sha:d52f1ea5 src:manual/30-struktura.md:176 klas:A -->
### T-30-067 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Коли вільно 40 КБ, а найбільший блок — 2 КБ, це і є фрагментація, і `malloc(8192)` поверне `NULL`.

**Контекст**

```
### Купа: чому malloc повертає NULL

Друге число важливіше за перше. Коли вільно 40 КБ, а найбільший блок —
2 КБ, це і є фрагментація, і `malloc(8192)` поверне `NULL`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/memory-types.rst
- **Дослівно з джерела:**
  > This memory can be used interchangeably with :ref:`DRAM`
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** фрагментація - коли вільно 40 КБ, а найбільший блок 2 КБ
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-068 sha:83aff946 src:manual/30-struktura.md:179 klas:A -->
### T-30-068 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **І завжди перевіряти результат.** `malloc`, результат якого не перевірили, — найчастіше джерело `LoadProhibited` на практиці (розділ 26):

**Контекст**

```
### Купа: чому malloc повертає NULL

**І завжди перевіряти результат.** `malloc`, результат якого не
перевірили, — найчастіше джерело `LoadProhibited` на практиці
(розділ 26):
```

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

<!-- fc id:T-30-069 sha:54537a63 src:manual/30-struktura.md:183 klas:K -->
### T-30-069 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> uint8_t *buf = malloc(size);
> if (buf == NULL) {
>     ESP_LOGE(TAG, "не вистачило %u байт", size);
>     return ESP_ERR_NO_MEM;
> }
> ```

**Контекст**

````
### Купа: чому malloc повертає NULL

```c
uint8_t *buf = malloc(size);
if (buf == NULL) {
    ESP_LOGE(TAG, "не вистачило %u байт", size);
    return ESP_ERR_NO_MEM;
}
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-070 sha:960e650b src:manual/30-struktura.md:186 klas:F -->
### T-30-070 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> ESP_LOGE(TAG, "не вистачило %u байт", size);

**Контекст**

````
### Купа: чому malloc повертає NULL

```c
uint8_t *buf = malloc(size);
if (buf == NULL) {
    ESP_LOGE(TAG, "не вистачило %u байт", size);
    return ESP_ERR_NO_MEM;
}
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-071 sha:2c139180 src:manual/30-struktura.md:193 klas:E -->
### T-30-071 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Код виконується з флешу через кеш.

**Контекст**

```
## IRAM, DRAM і чому це вилазить

Код виконується з флешу через кеш. Під час операції з флешем (запис у
NVS, стирання сектора) кеш вимикається, і виконання коду з флешу
неможливе (розділ 03).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-072 sha:283e1395 src:manual/30-struktura.md:193 klas:F -->
### T-30-072 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Під час операції з флешем (запис у NVS, стирання сектора) кеш вимикається, і виконання коду з флешу неможливе (розділ 03).

**Контекст**

```
## IRAM, DRAM і чому це вилазить

Код виконується з флешу через кеш. Під час операції з флешем (запис у
NVS, стирання сектора) кеш вимикається, і виконання коду з флешу
неможливе (розділ 03).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-073 sha:a8346dff src:manual/30-struktura.md:197 klas:A -->
### T-30-073 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Функція, яка може спрацювати в цей момент — насамперед обробник переривання, — має лежати в IRAM:

**Контекст**

```
## IRAM, DRAM і чому це вилазить

Функція, яка може спрацювати в цей момент — насамперед обробник
переривання, — має лежати в IRAM:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > IRAM (Instruction RAM) is memory that is connected to the CPU's instruction bus
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ підтверджує наявність IRAM
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-074 sha:e4e95770 src:manual/30-struktura.md:200 klas:K -->
### T-30-074 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> static void IRAM_ATTR gpio_isr_handler(void *arg) { ... }
> ```

**Контекст**

````
## IRAM, DRAM і чому це вилазить

```c
static void IRAM_ATTR gpio_isr_handler(void *arg) { ... }
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

<!-- fc id:T-30-075 sha:bd569017 src:manual/30-struktura.md:204 klas:A -->
### T-30-075 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Дані, до яких така функція звертається, теж мають бути доступні: `DRAM_ATTR`.

**Контекст**

```
## IRAM, DRAM і чому це вилазить

Дані, до яких така функція звертається, теж мають бути доступні:
`DRAM_ATTR`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/mem_alloc.rst, .../docs/en/api-guides/external-ram.rst, .../components/esp_common/include/esp_attr.h, .../components/freertos/Kconfig.freertos
- **Дослівно з джерела:**
  > (mem_alloc.rst)
  > Use the ``MALLOC_CAP_DMA`` flag to allocate memory which is suitable
  > for use with hardware DMA engines (for example SPI and I2S). This
  > capability flag excludes any external PSRAM.
  > 
  > (external-ram.rst)
  > when accessing large chunks of data (> 32 KB), the cache can be
  > insufficient, and speeds will fall back to the access speed of the
  > external RAM.
  > 
  > (esp_attr.h)
  > // Forces data into DRAM instead of flash
  > #define DRAM_ATTR _SECTION_ATTR_IMPL(".dram1", __COUNTER__)
  > 
  > (Kconfig.freertos)
  > config FREERTOS_CHECK_STACKOVERFLOW_NONE
  >     bool "No checking"
  >     help
  >         Do not check for stack overflows
  >         (configCHECK_FOR_STACK_OVERFLOW = 0)
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Обидві застороги книги про буфер у PSRAM підтверджено окремо, і кожна зі свого джерела: `MALLOC_CAP_DMA` **виключає** зовнішню пам'ять, а швидкість падає до швидкості зовнішньої шини на блоках понад 32 КБ.
Тобто буфер на 64 КБ, який туди потрапив сам, справді втрачає обидві властивості, які автор від нього чекав. Прохід 25 знайшов саме цей механізм; тут він доведений із документації, а не лише з Kconfig.
Агент окремо зауважив, що «погана угода» про вимкнення перевірки стека — редакційна оцінка, а не речення джерела. Це правильне зауваження, і саме тому в записі процитовано лише фактичну передумову: `No checking` справді вимикає виявлення цілком.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-30-076 sha:274d7cce src:manual/30-struktura.md:207 klas:A -->
### T-30-076 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> IRAM небагато, і кожна така функція займає її назавжди.

**Контекст**

```
## IRAM, DRAM і чому це вилазить

IRAM небагато, і кожна така функція займає її назавжди. Помилка
`section .iram0.text will not fit` при збиранні означає, що `IRAM_ATTR`
роздали надто щедро.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/memory-types.rst
- **Дослівно з джерела:**
  > As IRAM is limited, most of an application's binary code must be placed into IROM instead.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує обмеженість IRAM
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-077 sha:ef960cbf src:manual/30-struktura.md:207 klas:A -->
### T-30-077 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Помилка `section .iram0.text will not fit` при збиранні означає, що `IRAM_ATTR` роздали надто щедро.

**Контекст**

```
## IRAM, DRAM і чому це вилазить

IRAM небагато, і кожна така функція займає її назавжди. Помилка
`section .iram0.text will not fit` при збиранні означає, що `IRAM_ATTR`
роздали надто щедро.
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

<!-- fc id:T-30-078 sha:3ff21391 src:manual/30-struktura.md:213 klas:F -->
### T-30-078 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **`volatile`** каже компілятору не оптимізувати доступ до змінної.

**Контекст**

```
## volatile, атомарність, регістри

**`volatile`** каже компілятору не оптимізувати доступ до змінної.
Потрібен для змінних, які змінює обробник переривання, і для доступу до
регістрів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-079 sha:53abed90 src:manual/30-struktura.md:214 klas:E -->
### T-30-079 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Потрібен для змінних, які змінює обробник переривання, і для доступу до регістрів.

**Контекст**

```
## volatile, атомарність, регістри

**`volatile`** каже компілятору не оптимізувати доступ до змінної.
Потрібен для змінних, які змінює обробник переривання, і для доступу до
регістрів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-080 sha:61539d28 src:manual/30-struktura.md:217 klas:F -->
### T-30-080 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> `volatile` **не робить операцію атомарною**.

**Контекст**

```
## volatile, атомарність, регістри

`volatile` **не робить операцію атомарною**. Це найпоширеніше
непорозуміння:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-081 sha:30161603 src:manual/30-struktura.md:217 klas:E -->
### T-30-081 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Це найпоширеніше непорозуміння:

**Контекст**

```
## volatile, атомарність, регістри

`volatile` **не робить операцію атомарною**. Це найпоширеніше
непорозуміння:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-082 sha:5503aeaf src:manual/30-struktura.md:220 klas:K -->
### T-30-082 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> volatile int lichylnyk = 0;
> // в ISR:
> lichylnyk++;   // читання + додавання + запис — три дії, не одна
> ```

**Контекст**

````
## volatile, атомарність, регістри

```c
volatile int lichylnyk = 0;
// в ISR:
lichylnyk++;   // читання + додавання + запис — три дії, не одна
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-083 sha:f8388e6b src:manual/30-struktura.md:226 klas:E -->
### T-30-083 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> На двоядерному чипі така операція може перерватися посередині.

**Контекст**

```
## volatile, атомарність, регістри

На двоядерному чипі така операція може перерватися посередині. Для
лічильників, що змінюються з переривання й читаються із задачі,
правильні інструменти — атомарні операції або примітиви FreeRTOS
(розділ 31).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-084 sha:c2dcc926 src:manual/30-struktura.md:226 klas:F -->
### T-30-084 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Для лічильників, що змінюються з переривання й читаються із задачі, правильні інструменти — атомарні операції або примітиви FreeRTOS (розділ 31).

**Контекст**

```
## volatile, атомарність, регістри

На двоядерному чипі така операція може перерватися посередині. Для
лічильників, що змінюються з переривання й читаються із задачі,
правильні інструменти — атомарні операції або примітиви FreeRTOS
(розділ 31).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-085 sha:5bcfe49a src:manual/30-struktura.md:231 klas:A -->
### T-30-085 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> **32-бітне читання й запис вирівняного слова атомарні** апаратно.

**Контекст**

```
## volatile, атомарність, регістри

**32-бітне читання й запис вирівняного слова атомарні** апаратно. Тому
проста передача одного значення (прапорець, ціле число) із ISR у задачу
через `volatile` працює. Складніші структури — ні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Memory allocated with ``MALLOC_CAP_32BIT`` can **only** be accessed via 32-bit reads and writes
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що 32-бітне читання й запис атомарні
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-086 sha:38e10f93 src:manual/30-struktura.md:231 klas:A -->
### T-30-086 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Тому проста передача одного значення (прапорець, ціле число) із ISR у задачу через `volatile` працює.

**Контекст**

```
## volatile, атомарність, регістри

**32-бітне читання й запис вирівняного слова атомарні** апаратно. Тому
проста передача одного значення (прапорець, ціле число) із ISR у задачу
через `volatile` працює. Складніші структури — ні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Memory allocated with ``MALLOC_CAP_32BIT`` can **only** be accessed via 32-bit reads and writes
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** проста передача одного значення через volatile працює
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-087 sha:42e5df0c src:manual/30-struktura.md:233 klas:A -->
### T-30-087 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Складніші структури — ні.

**Контекст**

```
## volatile, атомарність, регістри

**32-бітне читання й запис вирівняного слова атомарні** апаратно. Тому
проста передача одного значення (прапорець, ціле число) із ISR у задачу
через `volatile` працює. Складніші структури — ні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Memory allocated with ``MALLOC_CAP_32BIT`` can **only** be accessed via 32-bit reads and writes, any other type of access will generate a fatal LoadStoreError exception.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що складніші структури не атомарні
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-088 sha:66cbb212 src:manual/30-struktura.md:237 klas:K -->
### T-30-088 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```sh
> idf.py size              # загальна картка: флеш і RAM
> idf.py size-components   # хто саме займає
> ```

**Контекст**

````
## Скільки в мене лишилося

```sh
idf.py size              # загальна картка: флеш і RAM
idf.py size-components   # хто саме займає
```
````

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

<!-- fc id:T-30-089 sha:30366121 src:manual/30-struktura.md:238 klas:A -->
### T-30-089 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> idf.py size              # загальна картка: флеш і RAM

**Контекст**

````
## Скільки в мене лишилося

```sh
idf.py size              # загальна картка: флеш і RAM
idf.py size-components   # хто саме займає
```
````

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

<!-- fc id:T-30-090 sha:6c692b14 src:manual/30-struktura.md:239 klas:A -->
### T-30-090 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> idf.py size-components   # хто саме займає

**Контекст**

````
## Скільки в мене лишилося

```sh
idf.py size              # загальна картка: флеш і RAM
idf.py size-components   # хто саме займає
```
````

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

<!-- fc id:T-30-091 sha:d2a9a595 src:manual/30-struktura.md:242 klas:A -->
### T-30-091 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> `size-components` — найкорисніша команда, коли прошивка перестала вміщатися: одразу видно, що Wi-Fi і TLS з'їли більшість, а власний код — десяту частину (розділ 18).

**Контекст**

```
## Скільки в мене лишилося

`size-components` — найкорисніша команда, коли прошивка перестала
вміщатися: одразу видно, що Wi-Fi і TLS з'їли більшість, а власний код —
десяту частину (розділ 18).
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

<!-- fc id:T-30-092 sha:23020636 src:manual/30-struktura.md:248 klas:K -->
### T-30-092 · kod · `manual/30-struktura.md`

**Твердження, коротко**

> ```c
> ESP_LOGI(TAG, "вільно RAM: %u", esp_get_free_heap_size());
> ESP_LOGI(TAG, "мінімум за весь час: %u", esp_get_minimum_free_heap_size());
> ```

**Контекст**

````
## Скільки в мене лишилося

```c
ESP_LOGI(TAG, "вільно RAM: %u", esp_get_free_heap_size());
ESP_LOGI(TAG, "мінімум за весь час: %u", esp_get_minimum_free_heap_size());
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-093 sha:2e66a826 src:manual/30-struktura.md:249 klas:F -->
### T-30-093 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> ESP_LOGI(TAG, "вільно RAM: %u", esp_get_free_heap_size());

**Контекст**

````
## Скільки в мене лишилося

```c
ESP_LOGI(TAG, "вільно RAM: %u", esp_get_free_heap_size());
ESP_LOGI(TAG, "мінімум за весь час: %u", esp_get_minimum_free_heap_size());
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-094 sha:991d1932 src:manual/30-struktura.md:250 klas:F -->
### T-30-094 · kod-ryadok · `manual/30-struktura.md`

**Твердження, коротко**

> ESP_LOGI(TAG, "мінімум за весь час: %u", esp_get_minimum_free_heap_size());

**Контекст**

````
## Скільки в мене лишилося

```c
ESP_LOGI(TAG, "вільно RAM: %u", esp_get_free_heap_size());
ESP_LOGI(TAG, "мінімум за весь час: %u", esp_get_minimum_free_heap_size());
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-095 sha:ccc7ed3c src:manual/30-struktura.md:253 klas:E -->
### T-30-095 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Друге значення варто логувати періодично: воно виявляє повільний витік пам'яті, який інакше помітний лише через тижні.

**Контекст**

```
## Скільки в мене лишилося

Друге значення варто логувати періодично: воно виявляє повільний витік
пам'яті, який інакше помітний лише через тижні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-096 sha:8b57246a src:manual/30-struktura.md:258 klas:F -->
### T-30-096 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> `app_main` — звичайна задача FreeRTOS; вона може завершитися, і в неї обмежений стек.

**Контекст**

```
## Що з цього треба запам'ятати

`app_main` — звичайна задача FreeRTOS; вона може завершитися, і в неї
обмежений стек.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-097 sha:6d579e42 src:manual/30-struktura.md:261 klas:E -->
### T-30-097 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Переповнення стека не дає повідомлення й проявляється пізніше та в іншому місці.

**Контекст**

```
## Що з цього треба запам'ятати

Переповнення стека не дає повідомлення й проявляється пізніше та в
іншому місці. Великі буфери — не на стек.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-098 sha:d8584f81 src:manual/30-struktura.md:262 klas:E -->
### T-30-098 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Великі буфери — не на стек.

**Контекст**

```
### Стек: чому програма падає без причини

**Великі буфери — не на стек.** `static` або з купи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-099 sha:e8ebea85 src:manual/30-struktura.md:264 klas:E -->
### T-30-099 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Не виділяти й не звільняти пам'ять у циклі: фрагментація вбиває пристрій через дні, а не одразу.

**Контекст**

```
## Що з цього треба запам'ятати

Не виділяти й не звільняти пам'ять у циклі: фрагментація вбиває пристрій
через дні, а не одразу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-100 sha:9243b822 src:manual/30-struktura.md:267 klas:E -->
### T-30-100 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Найбільший вільний блок важливіший за суму вільного.

**Контекст**

```
## Що з цього треба запам'ятати

Найбільший вільний блок важливіший за суму вільного.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-30-101 sha:21874c85 src:manual/30-struktura.md:269 klas:A -->
### T-30-101 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> Результат `malloc` перевіряти завжди.

**Контекст**

```
## Що з цього треба запам'ятати

Результат `malloc` перевіряти завжди.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > For most purposes, the C Standard Library's ``malloc()`` and ``free()`` functions can be used for heap allocation without any special consideration.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** результат malloc треба перевіряти завжди
- **Прохід:** prochid-30-struktura

---

<!-- fc id:T-30-102 sha:b09b18e3 src:manual/30-struktura.md:271 klas:A -->
### T-30-102 · proza · `manual/30-struktura.md`

**Твердження, коротко**

> `volatile` не робить операцію атомарною.

**Контекст**

```
## Що з цього треба запам'ятати

`volatile` не робить операцію атомарною.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst
- **Дослівно з джерела:**
  > Memory allocated with ``MALLOC_CAP_32BIT`` can **only** be accessed via 32-bit reads and writes
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** volatile не робить операцію атомарною
- **Прохід:** prochid-30-struktura

---
