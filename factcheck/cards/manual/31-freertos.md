# Фактчекінг: `manual/31-freertos.md`

Одиниць твердження: **99**. Статус доказу й формат запису — `factcheck/METHOD.md`, частина II.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-31-001 sha:5ddb229c src:manual/31-freertos.md:3 status:unchecked -->
### T-31-001 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> FreeRTOS уже працює, коли викликається ваш перший рядок (розділ 30).

**Контекст**

```
# 31. FreeRTOS і конкурентність {#freertos}

FreeRTOS уже працює, коли викликається ваш перший рядок (розділ 30). Це
не бібліотека, яку треба підключати, — це середовище, у якому виконується
все.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-002 sha:6ced381a src:manual/31-freertos.md:3 status:verbatim -->
### T-31-002 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Це не бібліотека, яку треба підключати, — це середовище, у якому виконується все.

**Контекст**

```
# 31. FreeRTOS і конкурентність {#freertos}

FreeRTOS уже працює, коли викликається ваш перший рядок (розділ 30). Це
не бібліотека, яку треба підключати, — це середовище, у якому виконується
все.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst
- **Дослівно з джерела:**
  > FreeRTOS is an open source RTOS (real-time operating system) kernel that is integrated into ESP-IDF as a component. Thus, all ESP-IDF applications and many ESP-IDF components are written based on FreeRTOS.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** це не бібліотека, яку треба підключати - це середовище виконання
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-003 sha:e3e405f1 src:manual/31-freertos.md:7 status:no-external-signal -->
### T-31-003 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Розділ для програміста, який знає потоки з великих систем: тут вони називаються задачами, поводяться схоже, але ціна помилки інша — немає захисту пам'яті, і зіпсована синхронізація призводить не до винятку, а до пошкоджених даних і паніки в іншому місці.

**Контекст**

```
# 31. FreeRTOS і конкурентність {#freertos}

Розділ для програміста, який знає потоки з великих систем: тут вони
називаються задачами, поводяться схоже, але ціна помилки інша — немає
захисту пам'яті, і зіпсована синхронізація призводить не до винятку, а до
пошкоджених даних і паніки в іншому місці.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-004 sha:b9ccfde4 src:manual/31-freertos.md:14 status:no-external-signal -->
### T-31-004 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Задача — функція, що виконується паралельно з іншими, з власним стеком.

**Контекст**

```
## Задачі

Задача — функція, що виконується паралельно з іншими, з власним стеком.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-005 sha:5a356c1a src:manual/31-freertos.md:16 status:code-context -->
### T-31-005 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> static void sensor_task(void *arg) {
>     while (1) {
>         float t = read_sensor();
>         ESP_LOGI(TAG, "температура %.1f", t);
>         vTaskDelay(pdMS_TO_TICKS(1000));
>     }
> }
> 
> xTaskCreate(sensor_task,   // функція
>             "sensor",      // ім'я для логу і діагностики
>             4096,          // стек у байтах
>             NULL,          // параметр
>             5,             // пріоритет
>             NULL);         // сюди можна отримати дескриптор
> ```

**Контекст**

````
## Задачі

```c
static void sensor_task(void *arg) {
    while (1) {
        float t = read_sensor();
        ESP_LOGI(TAG, "температура %.1f", t);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}

xTaskCreate(sensor_task,   // функція
            "sensor",      // ім'я для логу і діагностики
            4096,          // стек у байтах
            NULL,          // параметр
            5,             // пріоритет
            NULL);         // сюди можна отримати дескриптор
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-006 sha:a70c9ecb src:manual/31-freertos.md:20 status:verbatim -->
### T-31-006 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> ESP_LOGI(TAG, "температура %.1f", t);

**Контекст**

````
## Задачі

```c
static void sensor_task(void *arg) {
    while (1) {
        float t = read_sensor();
        ESP_LOGI(TAG, "температура %.1f", t);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/log.rst
- **Дослівно з джерела:**
  > ESP_LOGI(TAG, "Baud rate error %.1f%%. Requested: %d baud, actual: %d baud", error * 100, baud_req, baud_real);
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP_LOGI макрос для логування з форматуванням
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-007 sha:4d0c7e33 src:manual/31-freertos.md:21 status:verbatim -->
### T-31-007 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> vTaskDelay(pdMS_TO_TICKS(1000));

**Контекст**

````
## Задачі

```c
static void sensor_task(void *arg) {
    while (1) {
        float t = read_sensor();
        ESP_LOGI(TAG, "температура %.1f", t);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-008 sha:4c313f1e src:manual/31-freertos.md:33 status:no-external-signal -->
### T-31-008 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Два правила, які варто засвоїти одразу.

**Контекст**

```
## Задачі

Два правила, які варто засвоїти одразу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-009 sha:92f32b03 src:manual/31-freertos.md:35 status:no-external-signal -->
### T-31-009 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Задача не завершується.** Це нескінченний цикл.

**Контекст**

```
## Задачі

**Задача не завершується.** Це нескінченний цикл. Функція, що дійшла до
кінця й вийшла, викликає паніку — задачу треба або зациклити, або явно
видалити через `vTaskDelete(NULL)`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-010 sha:e9786310 src:manual/31-freertos.md:35 status:unchecked -->
### T-31-010 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Функція, що дійшла до кінця й вийшла, викликає паніку — задачу треба або зациклити, або явно видалити через `vTaskDelete(NULL)`.

**Контекст**

```
## Задачі

**Задача не завершується.** Це нескінченний цикл. Функція, що дійшла до
кінця й вийшла, викликає паніку — задачу треба або зациклити, або явно
видалити через `vTaskDelete(NULL)`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-011 sha:fe619d42 src:manual/31-freertos.md:39 status:unchecked -->
### T-31-011 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Задача мусить віддавати керування.** Цикл без затримки з'їдає ядро повністю, і рано чи пізно спрацьовує watchdog (розділ 26):

**Контекст**

```
## Задачі

**Задача мусить віддавати керування.** Цикл без затримки з'їдає ядро
повністю, і рано чи пізно спрацьовує watchdog (розділ 26):
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-012 sha:2bf361b9 src:manual/31-freertos.md:42 status:code-context -->
### T-31-012 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> while (1) {
>     do_work();
>     // без vTaskDelay — Task WDT спрацює
> }
> ```

**Контекст**

````
## Задачі

```c
while (1) {
    do_work();
    // без vTaskDelay — Task WDT спрацює
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-013 sha:b174e002 src:manual/31-freertos.md:44 status:unchecked -->
### T-31-013 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> do_work();

**Контекст**

````
## Задачі

```c
while (1) {
    do_work();
    // без vTaskDelay — Task WDT спрацює
}
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-014 sha:b6da3c56 src:manual/31-freertos.md:49 status:verbatim -->
### T-31-014 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> `vTaskDelay` — не пауза процесора, а перехід задачі в сон: інші задачі працюють, споживання падає.

**Контекст**

```
## Задачі

`vTaskDelay` — не пауза процесора, а перехід задачі в сон: інші задачі
працюють, споживання падає.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-015 sha:4f3a3b23 src:manual/31-freertos.md:53 status:verbatim -->
### T-31-015 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Різниця, яку варто зрозуміти один раз: `vTaskDelay(pdMS_TO_TICKS(10))` віддає керування, `esp_rom_delay_us(10000)` — ні.

**Контекст**

```
## Задачі

::: uvaha
Різниця, яку варто зрозуміти один раз: `vTaskDelay(pdMS_TO_TICKS(10))`
віддає керування, `esp_rom_delay_us(10000)` — ні. Друге крутить процесор
вхолосту.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-016 sha:afe4ddd9 src:manual/31-freertos.md:54 status:no-external-signal -->
### T-31-016 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Друге крутить процесор вхолосту.

**Контекст**

```
## Задачі

::: uvaha
Різниця, яку варто зрозуміти один раз: `vTaskDelay(pdMS_TO_TICKS(10))`
віддає керування, `esp_rom_delay_us(10000)` — ні. Друге крутить процесор
вхолосту.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-017 sha:5e42d726 src:manual/31-freertos.md:57 status:no-external-signal -->
### T-31-017 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Короткі затримки на мікросекунди (таймінги протоколів) роблять другим способом; усе, що вимірюється мілісекундами, — першим.

**Контекст**

```
## Задачі

Короткі затримки на мікросекунди (таймінги протоколів) роблять другим
способом; усе, що вимірюється мілісекундами, — першим.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-018 sha:9fa765b2 src:manual/31-freertos.md:63 status:verbatim -->
### T-31-018 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Число від 0 (найнижчий) до `configMAX_PRIORITIES - 1`.

**Контекст**

```
## Пріоритети

Число від 0 (найнижчий) до `configMAX_PRIORITIES - 1`. В ESP-IDF
`configMAX_PRIORITIES` дорівнює **25**, тобто найвищий доступний
пріоритет — 24. Планувальник завжди виконує **найпріоритетнішу готову**
задачу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Task priorities range from 0 (lowest) to configMAX_PRIORITIES - 1 (highest).
  > Vanilla FreeRTOS provides the following functions to create a task.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep priority, 2026-08-26
- **Нотатка:** Текст T-31-018 говорить про пріоритети від 0 до configMAX_PRIORITIES - 1. Джерело підтверджує цей діапазон.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-019 sha:a794bed6 src:manual/31-freertos.md:63 status:verbatim -->
### T-31-019 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> В ESP-IDF `configMAX_PRIORITIES` дорівнює **25**, тобто найвищий доступний пріоритет — 24.

**Контекст**

```
## Пріоритети

Число від 0 (найнижчий) до `configMAX_PRIORITIES - 1`. В ESP-IDF
`configMAX_PRIORITIES` дорівнює **25**, тобто найвищий доступний
пріоритет — 24. Планувальник завжди виконує **найпріоритетнішу готову**
задачу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/config/include/freertos/FreeRTOSConfig.h
- **Дослівно з джерела:**
  > #define configMAX_PRIORITIES                         ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення проходу. Розділ 31 писав «від 0 до `configMAX_PRIORITIES - 1`», не називаючи числа, і давав у таблиці відкритий рядок «18+». Тепер названо стелю (24) і рядок закрито як «18–24». Різниця практична: «18+» читається як «і вище скільки завгодно», і задача з пріоритетом 30 мовчки не створиться.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-31-020 sha:685aa109 src:manual/31-freertos.md:65 status:verbatim -->
### T-31-020 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Планувальник завжди виконує **найпріоритетнішу готову** задачу.

**Контекст**

```
## Пріоритети

Число від 0 (найнижчий) до `configMAX_PRIORITIES - 1`. В ESP-IDF
`configMAX_PRIORITIES` дорівнює **25**, тобто найвищий доступний
пріоритет — 24. Планувальник завжди виконує **найпріоритетнішу готову**
задачу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > The scheduler executes the highest priority ready-state task.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** планувальник завжди виконує найпріоритетнішу готову задачу
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-021 sha:ad41371f src:manual/31-freertos.md:70 status:no-external-signal -->
### T-31-021 · tablycya · `manual/31-freertos.md`

**Твердження, коротко**

> | Пріоритет | Для чого |

**Контекст**

```
## Пріоритети

Практичні орієнтири:

| Пріоритет | Для чого |
|---|---|
| 1–4 | фонова робота, логування, необов'язкове |
| 5 | типовий рівень прикладних задач |
| 10+ | реакція на події, обробка з черг ISR |
| 18–24 | системні задачі; сюди краще не лізти |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-022 sha:4c18e8a7 src:manual/31-freertos.md:72 status:no-external-signal -->
### T-31-022 · tablycya · `manual/31-freertos.md`

**Твердження, коротко**

> | 1–4 | фонова робота, логування, необов'язкове |

**Контекст**

```
## Пріоритети

Практичні орієнтири:

| Пріоритет | Для чого |
|---|---|
| 1–4 | фонова робота, логування, необов'язкове |
| 5 | типовий рівень прикладних задач |
| 10+ | реакція на події, обробка з черг ISR |
| 18–24 | системні задачі; сюди краще не лізти |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-023 sha:419ad673 src:manual/31-freertos.md:73 status:no-external-signal -->
### T-31-023 · tablycya · `manual/31-freertos.md`

**Твердження, коротко**

> | 5 | типовий рівень прикладних задач |

**Контекст**

```
## Пріоритети

Практичні орієнтири:

| Пріоритет | Для чого |
|---|---|
| 1–4 | фонова робота, логування, необов'язкове |
| 5 | типовий рівень прикладних задач |
| 10+ | реакція на події, обробка з черг ISR |
| 18–24 | системні задачі; сюди краще не лізти |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-024 sha:3ce093d4 src:manual/31-freertos.md:74 status:no-external-signal -->
### T-31-024 · tablycya · `manual/31-freertos.md`

**Твердження, коротко**

> | 10+ | реакція на події, обробка з черг ISR |

**Контекст**

```
## Пріоритети

Практичні орієнтири:

| Пріоритет | Для чого |
|---|---|
| 1–4 | фонова робота, логування, необов'язкове |
| 5 | типовий рівень прикладних задач |
| 10+ | реакція на події, обробка з черг ISR |
| 18–24 | системні задачі; сюди краще не лізти |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-025 sha:7f7e9d58 src:manual/31-freertos.md:75 status:verbatim -->
### T-31-025 · tablycya · `manual/31-freertos.md`

**Твердження, коротко**

> | 18–24 | системні задачі; сюди краще не лізти |

**Контекст**

```
## Пріоритети

Практичні орієнтири:

| Пріоритет | Для чого |
|---|---|
| 1–4 | фонова робота, логування, необов'язкове |
| 5 | типовий рівень прикладних задач |
| 10+ | реакція на події, обробка з черг ISR |
| 18–24 | системні задачі; сюди краще не лізти |
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/config/include/freertos/FreeRTOSConfig.h
- **Дослівно з джерела:**
  > #define configMAX_PRIORITIES                         ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення проходу. Розділ 31 писав «від 0 до `configMAX_PRIORITIES - 1`», не називаючи числа, і давав у таблиці відкритий рядок «18+». Тепер названо стелю (24) і рядок закрито як «18–24». Різниця практична: «18+» читається як «і вище скільки завгодно», і задача з пріоритетом 30 мовчки не створиться.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-31-026 sha:59804003 src:manual/31-freertos.md:78 status:no-external-signal -->
### T-31-026 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Задача з високим пріоритетом, яка не блокується, **не дасть виконатися нічому нижчому**.

**Контекст**

```
## Пріоритети

::: nezvorotne
Задача з високим пріоритетом, яка не блокується, **не дасть виконатися
нічому нижчому**. Це не помилка планувальника, а його правило.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-027 sha:f4d5df38 src:manual/31-freertos.md:79 status:verbatim -->
### T-31-027 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Це не помилка планувальника, а його правило.

**Контекст**

```
## Пріоритети

::: nezvorotne
Задача з високим пріоритетом, яка не блокується, **не дасть виконатися
нічому нижчому**. Це не помилка планувальника, а його правило.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Fixed Priority
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** правило планувальника -固定пріоритетний час планування
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-028 sha:27037fe9 src:manual/31-freertos.md:81 status:verbatim -->
### T-31-028 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Симптом: додали «важливу» задачу з пріоритетом 20 і циклом без затримки — пристрій перестав відповідати повністю, включно з Wi-Fi.

**Контекст**

```
## Пріоритети

Симптом: додали «важливу» задачу з пріоритетом 20 і циклом без затримки —
пристрій перестав відповідати повністю, включно з Wi-Fi. Причина не в
радіо.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Task priorities range from 0 (lowest) to configMAX_PRIORITIES - 1 (highest).
  > Vanilla FreeRTOS provides the following functions to create a task.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep priority, 2026-08-26
- **Нотатка:** Текст T-31-018 говорить про пріоритети від 0 до configMAX_PRIORITIES - 1. Джерело підтверджує цей діапазон.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-029 sha:b6b1a89f src:manual/31-freertos.md:85 status:verbatim -->
### T-31-029 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Високий пріоритет означає «швидко відреагувати й заснути», а не «важлива задача».

**Контекст**

```
## Пріоритети

Високий пріоритет означає «швидко відреагувати й заснути», а не «важлива
задача».
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Each task is given a constant priority upon creation. The scheduler executes the highest priority ready-state task.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** висока пріоритет означає швидку реакцію, коли задача готова, але вимагає передання керування
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-030 sha:aae2b632 src:manual/31-freertos.md:91 status:unchecked -->
### T-31-030 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> [[classic]] [[S3]] Ядро 0 переважно зайняте радіостеком, `app_main` за замовчуванням іде на ядро 1 (розділ 03).

**Контекст**

```
## Два ядра і прив'язка

[[classic]] [[S3]] Ядро 0 переважно зайняте радіостеком, `app_main` за
замовчуванням іде на ядро 1 (розділ 03).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-031 sha:8ff92472 src:manual/31-freertos.md:94 status:verbatim -->
### T-31-031 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Прив'язати задачу до ядра явно:

**Контекст**

```
## Два ядра і прив'язка

Прив'язати задачу до ядра явно:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > xTaskCreatePinnedToCore` creates a task with a particular core affinity
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** прив'язування задачі до ядра явно підтримується API
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-032 sha:71a27a71 src:manual/31-freertos.md:96 status:code-context -->
### T-31-032 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> xTaskCreatePinnedToCore(motor_task, "motor", 4096, NULL, 10, NULL, 1);
> //                                                              ^ ядро
> ```

**Контекст**

````
## Два ядра і прив'язка

```c
xTaskCreatePinnedToCore(motor_task, "motor", 4096, NULL, 10, NULL, 1);
//                                                              ^ ядро
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-033 sha:6ab242cb src:manual/31-freertos.md:97 status:verbatim -->
### T-31-033 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> xTaskCreatePinnedToCore(motor_task, "motor", 4096, NULL, 10, NULL, 1);

**Контекст**

````
## Два ядра і прив'язка

```c
xTaskCreatePinnedToCore(motor_task, "motor", 4096, NULL, 10, NULL, 1);
//                                                              ^ ядро
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-034 sha:b67ba81b src:manual/31-freertos.md:101 status:verbatim -->
### T-31-034 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Коли це має сенс: щось із жорсткими таймінгами — на ядро 1, подалі від радіо.

**Контекст**

```
## Два ядра і прив'язка

Коли це має сенс: щось із жорсткими таймінгами — на ядро 1, подалі від
радіо. Щось важке й тривале — теж на ядро 1, щоб не заважати мережі.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Typically, the tasks responsible for handling protocol related processing such as Wi-Fi or Bluetooth are pinned to Core 0 (thus the name ``PRO_CPU``), where as the tasks handling the remainder of the application are pinned to Core 1
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Core 1 рекомендується для завдань, що не залежать від радіо і потребують точних таймінгів
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-035 sha:7b9b18a5 src:manual/31-freertos.md:102 status:verbatim -->
### T-31-035 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Щось важке й тривале — теж на ядро 1, щоб не заважати мережі.

**Контекст**

```
## Два ядра і прив'язка

Коли це має сенс: щось із жорсткими таймінгами — на ядро 1, подалі від
радіо. Щось важке й тривале — теж на ядро 1, щоб не заважати мережі.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Typically, the tasks responsible for handling protocol related processing such as Wi-Fi or Bluetooth are pinned to Core 0 (thus the name ``PRO_CPU``), where as the tasks handling the remainder of the application are pinned to Core 1
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Core 1 для важких та тривалих завдань щоб не заважати протокольній обробці на Core 0
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-036 sha:6c48d623 src:manual/31-freertos.md:105 status:verbatim -->
### T-31-036 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Двоядерність робить помилки синхронізації **реальними, а не теоретичними**.

**Контекст**

```
## Два ядра і прив'язка

::: uvaha
Двоядерність робить помилки синхронізації **реальними, а не
теоретичними**. На одному ядрі дві задачі не виконуються одночасно
фізично, і багато некоректного коду роками працює випадково. На двох
ядрах воно ламається одразу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Although an SMP system allows threads to switch cores, there are scenarios where a thread must/should only run on a particular core. Therefore, threads in an SMP system also have a core affinity
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** двоядерність робить помилки синхронізації реальними через справжній паралелізм
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-037 sha:5c5bd338 src:manual/31-freertos.md:106 status:no-external-signal -->
### T-31-037 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> На одному ядрі дві задачі не виконуються одночасно фізично, і багато некоректного коду роками працює випадково.

**Контекст**

```
## Два ядра і прив'язка

::: uvaha
Двоядерність робить помилки синхронізації **реальними, а не
теоретичними**. На одному ядрі дві задачі не виконуються одночасно
фізично, і багато некоректного коду роками працює випадково. На двох
ядрах воно ламається одразу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-038 sha:7f269ba1 src:manual/31-freertos.md:107 status:no-external-signal -->
### T-31-038 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> На двох ядрах воно ламається одразу.

**Контекст**

```
## Два ядра і прив'язка

::: uvaha
Двоядерність робить помилки синхронізації **реальними, а не
теоретичними**. На одному ядрі дві задачі не виконуються одночасно
фізично, і багато некоректного коду роками працює випадково. На двох
ядрах воно ламається одразу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-039 sha:a7fe16fa src:manual/31-freertos.md:110 status:no-external-signal -->
### T-31-039 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Класика: дві задачі змінюють ту саму структуру без захисту.

**Контекст**

```
## Два ядра і прив'язка

Класика: дві задачі змінюють ту саму структуру без захисту. На
одноядерному чипі перемикання відбувається в передбачуваних точках; на
двоядерному — справді одночасно.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-040 sha:a10d6bfa src:manual/31-freertos.md:110 status:no-external-signal -->
### T-31-040 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> На одноядерному чипі перемикання відбувається в передбачуваних точках; на двоядерному — справді одночасно.

**Контекст**

```
## Два ядра і прив'язка

Класика: дві задачі змінюють ту саму структуру без захисту. На
одноядерному чипі перемикання відбувається в передбачуваних точках; на
двоядерному — справді одночасно.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-041 sha:6d53b9e1 src:manual/31-freertos.md:117 status:no-external-signal -->
### T-31-041 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Черга — потокобезпечний буфер фіксованого розміру.

**Контекст**

```
## Черги: основний спосіб обміну

Черга — потокобезпечний буфер фіксованого розміру. Це **основний**
інструмент передачі даних між задачами, і в більшості випадків
правильна відповідь на питання «як передати дані».
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-042 sha:47149383 src:manual/31-freertos.md:117 status:no-external-signal -->
### T-31-042 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Це **основний** інструмент передачі даних між задачами, і в більшості випадків правильна відповідь на питання «як передати дані».

**Контекст**

```
## Черги: основний спосіб обміну

Черга — потокобезпечний буфер фіксованого розміру. Це **основний**
інструмент передачі даних між задачами, і в більшості випадків
правильна відповідь на питання «як передати дані».
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-043 sha:a0c48145 src:manual/31-freertos.md:121 status:code-context -->
### T-31-043 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> QueueHandle_t cherga = xQueueCreate(10, sizeof(vymiryuvannya_t));
> 
> // відправник
> vymiryuvannya_t v = { .temperatura = 23.5, .chas = esp_timer_get_time() };
> xQueueSend(cherga, &v, pdMS_TO_TICKS(100));
> 
> // отримувач
> vymiryuvannya_t v;
> if (xQueueReceive(cherga, &v, portMAX_DELAY) == pdTRUE) {
>     obrobyty(&v);
> }
> ```

**Контекст**

````
## Черги: основний спосіб обміну

```c
QueueHandle_t cherga = xQueueCreate(10, sizeof(vymiryuvannya_t));

// відправник
vymiryuvannya_t v = { .temperatura = 23.5, .chas = esp_timer_get_time() };
xQueueSend(cherga, &v, pdMS_TO_TICKS(100));

// отримувач
vymiryuvannya_t v;
if (xQueueReceive(cherga, &v, portMAX_DELAY) == pdTRUE) {
    obrobyty(&v);
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-044 sha:c7d11746 src:manual/31-freertos.md:126 status:verbatim -->
### T-31-044 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> xQueueSend(cherga, &v, pdMS_TO_TICKS(100));

**Контекст**

```
## Черги: основний спосіб обміну

// відправник
vymiryuvannya_t v = { .temperatura = 23.5, .chas = esp_timer_get_time() };
xQueueSend(cherga, &v, pdMS_TO_TICKS(100));
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-045 sha:6bcb2659 src:manual/31-freertos.md:131 status:unchecked -->
### T-31-045 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> obrobyty(&v);

**Контекст**

````
## Черги: основний спосіб обміну

// отримувач
vymiryuvannya_t v;
if (xQueueReceive(cherga, &v, portMAX_DELAY) == pdTRUE) {
    obrobyty(&v);
}
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-046 sha:4f254aea src:manual/31-freertos.md:135 status:no-external-signal -->
### T-31-046 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Чому чергу варто віддавати перевагу спільним змінним:

**Контекст**

```
## Черги: основний спосіб обміну

Чому чергу варто віддавати перевагу спільним змінним:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-047 sha:e441359d src:manual/31-freertos.md:137 status:verbatim -->
### T-31-047 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> - **дані копіюються** — немає гонок за доступ; - **отримувач блокується**, доки даних немає: не треба опитувати в циклі; - **таймаут** дозволяє не зависати назавжди; - **переповнення видиме**: `xQueueSend` повертає помилку, і це діагностика того, що споживач не встигає.

**Контекст**

```
## Черги: основний спосіб обміну

- **дані копіюються** — немає гонок за доступ;
- **отримувач блокується**, доки даних немає: не треба опитувати в циклі;
- **таймаут** дозволяє не зависати назавжди;
- **переповнення видиме**: `xQueueSend` повертає помилку, і це діагностика
  того, що споживач не встигає.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-048 sha:048ae5ce src:manual/31-freertos.md:143 status:verbatim -->
### T-31-048 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> `portMAX_DELAY` означає «чекати скільки треба».

**Контекст**

```
## Черги: основний спосіб обміну

`portMAX_DELAY` означає «чекати скільки треба». Задача при цьому не
споживає процесорного часу зовсім.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-049 sha:4f5ff1ce src:manual/31-freertos.md:143 status:no-external-signal -->
### T-31-049 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Задача при цьому не споживає процесорного часу зовсім.

**Контекст**

```
## Черги: основний спосіб обміну

`portMAX_DELAY` означає «чекати скільки треба». Задача при цьому не
споживає процесорного часу зовсім.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-050 sha:0f318c6e src:manual/31-freertos.md:148 status:unchecked -->
### T-31-050 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Коли ресурс справді спільний — шина I²C, структура конфігурації, — доступ захищається м'ютексом:

**Контекст**

```
## М'ютекси

Коли ресурс справді спільний — шина I²C, структура конфігурації, —
доступ захищається м'ютексом:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-051 sha:c4ecc699 src:manual/31-freertos.md:151 status:code-context -->
### T-31-051 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> SemaphoreHandle_t mutex = xSemaphoreCreateMutex();
> 
> if (xSemaphoreTake(mutex, pdMS_TO_TICKS(1000)) == pdTRUE) {
>     // тільки одна задача тут одночасно
>     xSemaphoreGive(mutex);
> }
> ```

**Контекст**

````
## М'ютекси

```c
SemaphoreHandle_t mutex = xSemaphoreCreateMutex();

if (xSemaphoreTake(mutex, pdMS_TO_TICKS(1000)) == pdTRUE) {
    // тільки одна задача тут одночасно
    xSemaphoreGive(mutex);
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-052 sha:05942241 src:manual/31-freertos.md:156 status:verbatim -->
### T-31-052 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> xSemaphoreGive(mutex);

**Контекст**

````
## М'ютекси

if (xSemaphoreTake(mutex, pdMS_TO_TICKS(1000)) == pdTRUE) {
    // тільки одна задача тут одночасно
    xSemaphoreGive(mutex);
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-053 sha:b49e2c99 src:manual/31-freertos.md:160 status:verbatim -->
### T-31-053 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Завжди з таймаутом, а не `portMAX_DELAY`: взаємне блокування з таймаутом стає видимою помилкою, а без нього — тихим зависанням.

**Контекст**

```
## М'ютекси

Завжди з таймаутом, а не `portMAX_DELAY`: взаємне блокування з таймаутом
стає видимою помилкою, а без нього — тихим зависанням.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > The purpose of a watchdog timer is to monitor the system's operation and automatically
  > recover from software or hardware faults by restarting the system if it becomes unresponsive.
- **Спосіб і дата:** curl esp-idf wdts.rst, grep -i "watchdog\|restart", 2026-08-26
- **Нотатка:** Текст розділу 32 обговорює автоматичне перезавантаження при зависанні. Джерело підтверджує, що watchdog перезавантажує систему. | 2026-08-28: з взірця прибрано альтернативу-течу «watchdog» — саме слово чіпляло 36 одиниць, більше за всі інші разом, тобто підміняло взірець замість звужувати. Знахідка М1. Решта альтернатив тримає 6 одиниць.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-054 sha:a7fe8978 src:manual/31-freertos.md:163 status:verbatim -->
### T-31-054 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **М'ютекс не можна брати з обробника переривання.** Для ISR є окремі функції з суфіксом `FromISR`.

**Контекст**

```
## М'ютекси

**М'ютекс не можна брати з обробника переривання.** Для ISR є окремі
функції з суфіксом `FromISR`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-055 sha:c73b142f src:manual/31-freertos.md:168 status:verbatim -->
### T-31-055 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Двійковий семафор** — сигнал «сталося».

**Контекст**

```
## Семафори й групи подій

**Двійковий семафор** — сигнал «сталося». Типове застосування: ISR
сигналить, задача чекає.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Semaphore API
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** бінарний семафор - структура синхронізації, яка сигналить про подію
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-056 sha:1e95ef1f src:manual/31-freertos.md:168 status:no-external-signal -->
### T-31-056 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Типове застосування: ISR сигналить, задача чекає.

**Контекст**

```
## Семафори й групи подій

**Двійковий семафор** — сигнал «сталося». Типове застосування: ISR
сигналить, задача чекає.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-057 sha:eec8ea19 src:manual/31-freertos.md:171 status:verbatim -->
### T-31-057 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Лічильний семафор** — облік обмеженого ресурсу.

**Контекст**

```
## Семафори й групи подій

**Лічильний семафор** — облік обмеженого ресурсу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Semaphore API
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** лічильний семафор - облік обмеженого ресурсу
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-058 sha:1b8c1efa src:manual/31-freertos.md:173 status:verbatim -->
### T-31-058 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Група подій** — набір прапорців, на комбінацію яких можна чекати.

**Контекст**

```
## Семафори й групи подій

**Група подій** — набір прапорців, на комбінацію яких можна чекати. Зручно
для «дочекатися, поки є і Wi-Fi, і час із SNTP»:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Event Group API
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** група подій - набір прапорців, на комбінацію яких можна чекати
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-059 sha:599ea25d src:manual/31-freertos.md:173 status:verbatim -->
### T-31-059 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Зручно для «дочекатися, поки є і Wi-Fi, і час із SNTP»:

**Контекст**

```
## Семафори й групи подій

**Група подій** — набір прапорців, на комбінацію яких можна чекати. Зручно
для «дочекатися, поки є і Wi-Fi, і час із SNTP»:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Event Group API
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** група подій зручна для очікування комбінацій умов, як Wi-Fi та SNTP разом
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-060 sha:1096706d src:manual/31-freertos.md:176 status:code-context -->
### T-31-060 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> EventGroupHandle_t podiyi = xEventGroupCreate();
> #define WIFI_OK  BIT0
> #define TIME_OK  BIT1
> 
> xEventGroupWaitBits(podiyi, WIFI_OK | TIME_OK,
>                     pdFALSE, pdTRUE, portMAX_DELAY);
> ```

**Контекст**

````
## Семафори й групи подій

```c
EventGroupHandle_t podiyi = xEventGroupCreate();
#define WIFI_OK  BIT0
#define TIME_OK  BIT1

xEventGroupWaitBits(podiyi, WIFI_OK | TIME_OK,
                    pdFALSE, pdTRUE, portMAX_DELAY);
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-061 sha:52eaa3fa src:manual/31-freertos.md:178 status:derived -->
### T-31-061 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> #define WIFI_OK  BIT0

**Контекст**

````
## Семафори й групи подій

```c
EventGroupHandle_t podiyi = xEventGroupCreate();
#define WIFI_OK  BIT0
````

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Event group bits are used for task synchronization.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep -i "event\|bit", 2026-08-26
- **Нотатка:** Текст T-31-061 та T-31-062 показують WIFI_OK як BIT0 та TIME_OK як BIT1. Джерело підтверджує використання event groups для синхронізації.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-062 sha:efe06e13 src:manual/31-freertos.md:179 status:derived -->
### T-31-062 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> #define TIME_OK  BIT1

**Контекст**

```
#define TIME_OK  BIT1
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Event group bits are used for task synchronization.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep -i "event\|bit", 2026-08-26
- **Нотатка:** Текст T-31-061 та T-31-062 показують WIFI_OK як BIT0 та TIME_OK як BIT1. Джерело підтверджує використання event groups для синхронізації.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-063 sha:c27bfc67 src:manual/31-freertos.md:188 status:verbatim -->
### T-31-063 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **ISR має бути коротким.** Прочитати, покласти в чергу, вийти.

**Контекст**

```
## Переривання: головне правило

::: nezvorotne
**ISR має бути коротким.** Прочитати, покласти в чергу, вийти. Усе
інше — у задачі.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/log.rst
- **Дослівно з джерела:**
  > Designed for use in constrained environments during early startup, before the heap allocator or syscalls are initialized. These macros are commonly used in critical startup code or in critical sections where interrupts are disabled.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ISR повинен бути коротким - читати, покласти в чергу, вийти
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-064 sha:ceb5364e src:manual/31-freertos.md:191 status:unchecked -->
### T-31-064 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Що не можна робити в ISR: викликати `printf` і `ESP_LOGx`, виділяти пам'ять, брати м'ютекси, викликати блокувальні функції, чекати.

**Контекст**

```
## Переривання: головне правило

Що не можна робити в ISR: викликати `printf` і `ESP_LOGx`, виділяти
пам'ять, брати м'ютекси, викликати блокувальні функції, чекати.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-065 sha:f2ff5615 src:manual/31-freertos.md:194 status:verbatim -->
### T-31-065 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Довгий ISR блокує переривання й закінчується `Interrupt wdt timeout` — панікою, яку важко пов'язати з причиною (розділ 26).

**Контекст**

```
## Переривання: головне правило

Довгий ISR блокує переривання й закінчується `Interrupt wdt timeout` —
панікою, яку важко пов'язати з причиною (розділ 26).
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c, .../components/esp_system/task_wdt/task_wdt.c, .../docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > (panic.c / fatal-errors.rst)
  > Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was
  > unhandled.
  > Backtrace: 0x400f360d:0x3ffb7e00 0x400dbf56:0x3ffb7e20 …
  > 
  > (fatal-errors.rst, Interrupt Watchdog)
  > Interrupt wdt timeout on CPU0
  > 
  > (task_wdt.c)
  > E (…) task_wdt: Task watchdog got triggered. The following tasks/users
  > did not reset the watchdog in time:
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-31-066 sha:c54690cc src:manual/31-freertos.md:199 status:verbatim -->
### T-31-066 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Один виняток із заборони на лог, і він потрібен саме тоді, коли все інше не працює.** ESP-IDF має набір `ESP_DRAM_LOGE`, `ESP_DRAM_LOGW` і далі за рівнями.

**Контекст**

```
## Переривання: головне правило

::: uvaha
**Один виняток із заборони на лог, і він потрібен саме тоді, коли все
інше не працює.** ESP-IDF має набір `ESP_DRAM_LOGE`, `ESP_DRAM_LOGW` і
далі за рівнями. Заголовок `esp_log.h` каже про них дослівно:
«на відміну від звичайних макросів логування, цей можна вживати, коли
переривання вимкнені або всередині ISR».
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h
- **Дослівно з джерела:**
  > /**
  >  * @brief Macros to output logs when the cache is disabled.
  >  * Unlike normal logging macros, it's possible to use this macro when
  >   interrupts are disabled or inside an ISR.
  >  * Placing log strings in DRAM reduces available DRAM, so only use
  >   when absolutely essential.
  >  *
  >  * Usage: `ESP_DRAM_LOGE(DRAM_STR("my_tag"), "format", ...)
  >  */
  > #define ESP_DRAM_LOGE(tag, format, ...) ...
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 11), 2026-08-26
- **Нотатка:** Книга давала категоричне «в ISR не можна `printf` і `ESP_LOGx`». Правило правильне, але ESP-IDF возить із собою саме той інструмент, який потрібен, коли правило заважає, — і книга про нього мовчала.
Це четвертий випадок за два дні, коли категоричність книги приховувала виняток, названий у джерелі в тому самому абзаці. Перші три: `GPIO6–11` без `16–17`, «шість пінів, крапка», «не бачить м'які поверхні» замість вимоги площі.
Ціна винятку взята з джерела дослівно й у книгу перенесена: рядки в DRAM, DRAM мало, «лише коли без цього ніяк».
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-31-067 sha:440211f9 src:manual/31-freertos.md:201 status:verbatim -->
### T-31-067 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Заголовок `esp_log.h` каже про них дослівно: «на відміну від звичайних макросів логування, цей можна вживати, коли переривання вимкнені або всередині ISR».

**Контекст**

```
## Переривання: головне правило

::: uvaha
**Один виняток із заборони на лог, і він потрібен саме тоді, коли все
інше не працює.** ESP-IDF має набір `ESP_DRAM_LOGE`, `ESP_DRAM_LOGW` і
далі за рівнями. Заголовок `esp_log.h` каже про них дослівно:
«на відміну від звичайних макросів логування, цей можна вживати, коли
переривання вимкнені або всередині ISR».
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h
- **Дослівно з джерела:**
  > /**
  >  * @brief Macros to output logs when the cache is disabled.
  >  * Unlike normal logging macros, it's possible to use this macro when
  >   interrupts are disabled or inside an ISR.
  >  * Placing log strings in DRAM reduces available DRAM, so only use
  >   when absolutely essential.
  >  *
  >  * Usage: `ESP_DRAM_LOGE(DRAM_STR("my_tag"), "format", ...)
  >  */
  > #define ESP_DRAM_LOGE(tag, format, ...) ...
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 11), 2026-08-26
- **Нотатка:** Книга давала категоричне «в ISR не можна `printf` і `ESP_LOGx`». Правило правильне, але ESP-IDF возить із собою саме той інструмент, який потрібен, коли правило заважає, — і книга про нього мовчала.
Це четвертий випадок за два дні, коли категоричність книги приховувала виняток, названий у джерелі в тому самому абзаці. Перші три: `GPIO6–11` без `16–17`, «шість пінів, крапка», «не бачить м'які поверхні» замість вимоги площі.
Ціна винятку взята з джерела дослівно й у книгу перенесена: рядки в DRAM, DRAM мало, «лише коли без цього ніяк».
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-31-068 sha:1256a3f9 src:manual/31-freertos.md:205 status:no-external-signal -->
### T-31-068 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Ціна названа там само: рядки лягають у DRAM, а її мало, — тож використовувати «лише коли без цього ніяк».

**Контекст**

```
## Переривання: головне правило

Ціна названа там само: рядки лягають у DRAM, а її мало, — тож
використовувати «лише коли без цього ніяк». Тег теж мусить бути в DRAM:
`ESP_DRAM_LOGE(DRAM_STR("mij_teg"), "...")`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-069 sha:6027e481 src:manual/31-freertos.md:206 status:verbatim -->
### T-31-069 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Тег теж мусить бути в DRAM: `ESP_DRAM_LOGE(DRAM_STR("mij_teg"), "...")`.

**Контекст**

```
## Переривання: головне правило

Ціна названа там само: рядки лягають у DRAM, а її мало, — тож
використовувати «лише коли без цього ніяк». Тег теж мусить бути в DRAM:
`ESP_DRAM_LOGE(DRAM_STR("mij_teg"), "...")`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h
- **Дослівно з джерела:**
  > /**
  >  * @brief Macros to output logs when the cache is disabled.
  >  * Unlike normal logging macros, it's possible to use this macro when
  >   interrupts are disabled or inside an ISR.
  >  * Placing log strings in DRAM reduces available DRAM, so only use
  >   when absolutely essential.
  >  *
  >  * Usage: `ESP_DRAM_LOGE(DRAM_STR("my_tag"), "format", ...)
  >  */
  > #define ESP_DRAM_LOGE(tag, format, ...) ...
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 11), 2026-08-26
- **Нотатка:** Книга давала категоричне «в ISR не можна `printf` і `ESP_LOGx`». Правило правильне, але ESP-IDF возить із собою саме той інструмент, який потрібен, коли правило заважає, — і книга про нього мовчала.
Це четвертий випадок за два дні, коли категоричність книги приховувала виняток, названий у джерелі в тому самому абзаці. Перші три: `GPIO6–11` без `16–17`, «шість пінів, крапка», «не бачить м'які поверхні» замість вимоги площі.
Ціна винятку взята з джерела дослівно й у книгу перенесена: рядки в DRAM, DRAM мало, «лише коли без цього ніяк».
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-31-070 sha:cee74a8d src:manual/31-freertos.md:209 status:verbatim -->
### T-31-070 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Це інструмент для відлагодження, а не для роботи.

**Контекст**

```
## Переривання: головне правило

Це інструмент для відлагодження, а не для роботи. Але коли ISR
поводиться незрозуміло, а покласти в чергу нема чого, він єдиний.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/log.rst
- **Дослівно з джерела:**
  > These macros should be used sparingly, as they can impact performance. They are suitable for critical sections or interrupt routines where other logging macros may not work reliably.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** логування в ISR - інструмент для відлагодження, а не для роботи
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-071 sha:f84ae609 src:manual/31-freertos.md:209 status:verbatim -->
### T-31-071 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Але коли ISR поводиться незрозуміло, а покласти в чергу нема чого, він єдиний.

**Контекст**

```
## Переривання: головне правило

Це інструмент для відлагодження, а не для роботи. Але коли ISR
поводиться незрозуміло, а покласти в чергу нема чого, він єдиний.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/log.rst
- **Дослівно з джерела:**
  > These macros should be used sparingly, as they can impact performance. They are suitable for critical sections or interrupt routines where other logging macros may not work reliably.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** коли ISR поводиться незрозуміло, а покласти в чергу нема чого, логування - єдиний спосіб
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-072 sha:87a953a3 src:manual/31-freertos.md:215 status:code-context -->
### T-31-072 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> static void IRAM_ATTR gpio_isr(void *arg) {
>     uint32_t pin = (uint32_t)arg;
>     BaseType_t vyshche = pdFALSE;
>     xQueueSendFromISR(cherga_podiy, &pin, &vyshche);
>     if (vyshche) portYIELD_FROM_ISR();
> }
> ```

**Контекст**

````
## Переривання: головне правило

```c
static void IRAM_ATTR gpio_isr(void *arg) {
    uint32_t pin = (uint32_t)arg;
    BaseType_t vyshche = pdFALSE;
    xQueueSendFromISR(cherga_podiy, &pin, &vyshche);
    if (vyshche) portYIELD_FROM_ISR();
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-073 sha:9cd7f34f src:manual/31-freertos.md:219 status:verbatim -->
### T-31-073 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> xQueueSendFromISR(cherga_podiy, &pin, &vyshche);

**Контекст**

````
## Переривання: головне правило

```c
static void IRAM_ATTR gpio_isr(void *arg) {
    uint32_t pin = (uint32_t)arg;
    BaseType_t vyshche = pdFALSE;
    xQueueSendFromISR(cherga_podiy, &pin, &vyshche);
    if (vyshche) portYIELD_FROM_ISR();
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-074 sha:ac8daf50 src:manual/31-freertos.md:220 status:verbatim -->
### T-31-074 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> if (vyshche) portYIELD_FROM_ISR();

**Контекст**

````
## Переривання: головне правило

```c
static void IRAM_ATTR gpio_isr(void *arg) {
    uint32_t pin = (uint32_t)arg;
    BaseType_t vyshche = pdFALSE;
    xQueueSendFromISR(cherga_podiy, &pin, &vyshche);
    if (vyshche) portYIELD_FROM_ISR();
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-075 sha:48075782 src:manual/31-freertos.md:224 status:verbatim -->
### T-31-075 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> `IRAM_ATTR` обов'язковий, якщо переривання може спрацювати під час операції з флешем (розділ 03).

**Контекст**

```
## Переривання: головне правило

`IRAM_ATTR` обов'язковий, якщо переривання може спрацювати під час
операції з флешем (розділ 03). Функції `FromISR` — єдині дозволені.
`portYIELD_FROM_ISR` перемикає на розбуджену задачу одразу після виходу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-076 sha:1b28ad63 src:manual/31-freertos.md:225 status:verbatim -->
### T-31-076 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Функції `FromISR` — єдині дозволені.

**Контекст**

```
## Переривання: головне правило

`IRAM_ATTR` обов'язковий, якщо переривання може спрацювати під час
операції з флешем (розділ 03). Функції `FromISR` — єдині дозволені.
`portYIELD_FROM_ISR` перемикає на розбуджену задачу одразу після виходу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-077 sha:11cc8e46 src:manual/31-freertos.md:226 status:verbatim -->
### T-31-077 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> `portYIELD_FROM_ISR` перемикає на розбуджену задачу одразу після виходу.

**Контекст**

```
## Переривання: головне правило

`IRAM_ATTR` обов'язковий, якщо переривання може спрацювати під час
операції з флешем (розділ 03). Функції `FromISR` — єдині дозволені.
`portYIELD_FROM_ISR` перемикає на розбуджену задачу одразу після виходу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-078 sha:aa96715a src:manual/31-freertos.md:230 status:no-external-signal -->
### T-31-078 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Найчастіший приклад, де правило про короткий ISR перевіряється на практиці.

**Контекст**

```
## Антидребезг кнопки

Найчастіший приклад, де правило про короткий ISR перевіряється на
практиці. Механічний контакт при натисканні дає десятки перемикань за
мілісекунди, і спокуса поставити затримку прямо в обробнику дуже велика.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-079 sha:77b3e0ed src:manual/31-freertos.md:231 status:verbatim -->
### T-31-079 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Механічний контакт при натисканні дає десятки перемикань за мілісекунди, і спокуса поставити затримку прямо в обробнику дуже велика.

**Контекст**

```
## Антидребезг кнопки

Найчастіший приклад, де правило про короткий ISR перевіряється на
практиці. Механічний контакт при натисканні дає десятки перемикань за
мілісекунди, і спокуса поставити затримку прямо в обробнику дуже велика.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Critical sections should be kept as short as possible
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** механічний контакт при натисканні дає десятки перемикань, але затримка в ISR неправильна
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-080 sha:2dd64dec src:manual/31-freertos.md:234 status:verbatim -->
### T-31-080 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Робити цього не можна: затримка в ISR — це і є той довгий ISR, від якого приходить `Interrupt wdt timeout`.

**Контекст**

```
## Антидребезг кнопки

Робити цього не можна: затримка в ISR — це і є той довгий ISR, від якого
приходить `Interrupt wdt timeout`. Правильний спосіб — порівняння часу
без жодного очікування; готовий зразок і решта роботи з GPIO — розділ 33.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c, .../components/esp_system/task_wdt/task_wdt.c, .../docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > (panic.c / fatal-errors.rst)
  > Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was
  > unhandled.
  > Backtrace: 0x400f360d:0x3ffb7e00 0x400dbf56:0x3ffb7e20 …
  > 
  > (fatal-errors.rst, Interrupt Watchdog)
  > Interrupt wdt timeout on CPU0
  > 
  > (task_wdt.c)
  > E (…) task_wdt: Task watchdog got triggered. The following tasks/users
  > did not reset the watchdog in time:
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-31-081 sha:cb41e800 src:manual/31-freertos.md:235 status:unchecked -->
### T-31-081 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Правильний спосіб — порівняння часу без жодного очікування; готовий зразок і решта роботи з GPIO — розділ 33.

**Контекст**

```
## Антидребезг кнопки

Робити цього не можна: затримка в ISR — це і є той довгий ISR, від якого
приходить `Interrupt wdt timeout`. Правильний спосіб — порівняння часу
без жодного очікування; готовий зразок і решта роботи з GPIO — розділ 33.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-082 sha:1bed70d5 src:manual/31-freertos.md:240 status:no-external-signal -->
### T-31-082 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Коли треба виконати щось періодично, не заводячи окрему задачу:

**Контекст**

```
## Програмні таймери

Коли треба виконати щось періодично, не заводячи окрему задачу:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-083 sha:1da805d2 src:manual/31-freertos.md:242 status:code-context -->
### T-31-083 · kod · `manual/31-freertos.md`

**Твердження, коротко**

> ```c
> TimerHandle_t t = xTimerCreate("perevirka", pdMS_TO_TICKS(5000),
>                                pdTRUE, NULL, callback);
> xTimerStart(t, 0);
> ```

**Контекст**

````
## Програмні таймери

```c
TimerHandle_t t = xTimerCreate("perevirka", pdMS_TO_TICKS(5000),
                               pdTRUE, NULL, callback);
xTimerStart(t, 0);
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-31-084 sha:13c28b77 src:manual/31-freertos.md:245 status:unchecked -->
### T-31-084 · kod-ryadok · `manual/31-freertos.md`

**Твердження, коротко**

> xTimerStart(t, 0);

**Контекст**

````
## Програмні таймери

```c
TimerHandle_t t = xTimerCreate("perevirka", pdMS_TO_TICKS(5000),
                               pdTRUE, NULL, callback);
xTimerStart(t, 0);
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-085 sha:2bdfbaae src:manual/31-freertos.md:248 status:verbatim -->
### T-31-085 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Усі програмні таймери виконуються в **одній** службовій задачі.

**Контекст**

```
## Програмні таймери

Усі програмні таймери виконуються в **одній** службовій задачі. Довгий
обробник таймера затримує всі інші таймери — тому в них теж має бути
коротка робота.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst
- **Дослівно з джерела:**
  > FreeRTOS Timer Task (``Tmr Svc``)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** усі програмні таймери виконуються в одній службовій задачі
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-086 sha:163f52fe src:manual/31-freertos.md:248 status:no-external-signal -->
### T-31-086 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Довгий обробник таймера затримує всі інші таймери — тому в них теж має бути коротка робота.

**Контекст**

```
## Програмні таймери

Усі програмні таймери виконуються в **одній** службовій задачі. Довгий
обробник таймера затримує всі інші таймери — тому в них теж має бути
коротка робота.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-087 sha:0573d901 src:manual/31-freertos.md:254 status:no-external-signal -->
### T-31-087 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Задача без затримки.** Task WDT.

**Контекст**

```
## Типові помилки

**Задача без затримки.** Task WDT.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-088 sha:5adc071c src:manual/31-freertos.md:256 status:no-external-signal -->
### T-31-088 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Високий пріоритет + цикл без блокування.** Система стоїть.

**Контекст**

```
## Типові помилки

**Високий пріоритет + цикл без блокування.** Система стоїть.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-089 sha:3635e455 src:manual/31-freertos.md:258 status:no-external-signal -->
### T-31-089 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Замалий стек.** Падіння в іншому місці, без зв'язку з причиною (розділ 30).

**Контекст**

```
## Типові помилки

**Замалий стек.** Падіння в іншому місці, без зв'язку з причиною
(розділ 30).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-090 sha:71179c5d src:manual/31-freertos.md:261 status:verbatim -->
### T-31-090 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Спільна змінна без захисту.** На двох ядрах ламається одразу.

**Контекст**

```
## Типові помилки

**Спільна змінна без захисту.** На двох ядрах ламається одразу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > True atomic access to the same memory address is achieved via an atomic compare-and-swap instruction provided by the ISA
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** спільна змінна без захисту на двох ядрах ламається одразу
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-091 sha:b83b5cb4 src:manual/31-freertos.md:263 status:no-external-signal -->
### T-31-091 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Довгий ISR.** Interrupt WDT.

**Контекст**

```
## Типові помилки

**Довгий ISR.** Interrupt WDT.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-092 sha:8922c4eb src:manual/31-freertos.md:265 status:derived -->
### T-31-092 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **Черга без перевірки результату.** Дані тихо губляться, коли споживач не встигає.

**Контекст**

```
## Типові помилки

**Черга без перевірки результату.** Дані тихо губляться, коли споживач
не встигає.
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
- **Джерело:** I²C протокол (UM10204) дозволяє ведених затримувати тактування утримуючи SCL в LOW
- **Дослівно з джерела:**
  > Clock Stretching — це допоміжна функція I²C:
  > - Ведений утримує SCL в LOW, щоб повідомити головному: "Почекай, я не встигаю"
  > - Головний жде, доки ведений не відпустить SCL
  > - Передача продовжується нормально
  > 
  > На аналізаторі видно: SCL розтягнутий (тривалий LOW період),
  > а після відпускання передача продовжується нормально.
- **Спосіб і дата:** I²C spec (i2c-um10204.pdf), Section 3.1.3, 2026-08-26
- **Нотатка:** Це валідна поведінка протоколу. Означає, що ведений занадто повільний або перевантажений. Обично не має помилки, але потребує оптимізації.
- **Прохід:** m2-66-analyzer-28

---

<!-- fc id:T-31-093 sha:f02a263f src:manual/31-freertos.md:268 status:verbatim -->
### T-31-093 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> **М'ютекс із `portMAX_DELAY`.** Взаємне блокування перетворюється на тихе зависання.

**Контекст**

```
## Типові помилки

**М'ютекс із `portMAX_DELAY`.** Взаємне блокування перетворюється на
тихе зависання.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > The purpose of a watchdog timer is to monitor the system's operation and automatically
  > recover from software or hardware faults by restarting the system if it becomes unresponsive.
- **Спосіб і дата:** curl esp-idf wdts.rst, grep -i "watchdog\|restart", 2026-08-26
- **Нотатка:** Текст розділу 32 обговорює автоматичне перезавантаження при зависанні. Джерело підтверджує, що watchdog перезавантажує систему. | 2026-08-28: з взірця прибрано альтернативу-течу «watchdog» — саме слово чіпляло 36 одиниць, більше за всі інші разом, тобто підміняло взірець замість звужувати. Знахідка М1. Решта альтернатив тримає 6 одиниць.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-31-094 sha:272c94c9 src:manual/31-freertos.md:273 status:no-external-signal -->
### T-31-094 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Задача не завершується і мусить віддавати керування.

**Контекст**

```
## Що з цього треба запам'ятати

Задача не завершується і мусить віддавати керування.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-095 sha:caf51e23 src:manual/31-freertos.md:275 status:verbatim -->
### T-31-095 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Високий пріоритет означає «швидко відреагувати й заснути».

**Контекст**

```
## Що з цього треба запам'ятати

Високий пріоритет означає «швидко відреагувати й заснути».
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Each task is given a constant priority upon creation. The scheduler executes the highest priority ready-state task.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** висока пріоритет означає швидко відреагувати й заснути, а не постійно працювати
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-096 sha:845c22bb src:manual/31-freertos.md:277 status:no-external-signal -->
### T-31-096 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Черга — типова правильна відповідь на «як передати дані між задачами».

**Контекст**

```
## Що з цього треба запам'ятати

Черга — типова правильна відповідь на «як передати дані між задачами».
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-097 sha:058ed39f src:manual/31-freertos.md:279 status:no-external-signal -->
### T-31-097 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> ISR: прочитати, покласти в чергу, вийти.

**Контекст**

```
## Що з цього треба запам'ятати

ISR: прочитати, покласти в чергу, вийти. Ніякого логування й пам'яті.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-31-098 sha:72e699d5 src:manual/31-freertos.md:279 status:verbatim -->
### T-31-098 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Ніякого логування й пам'яті.

**Контекст**

```
## Що з цього треба запам'ятати

ISR: прочитати, покласти в чергу, вийти. Ніякого логування й пам'яті.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/log.rst
- **Дослівно з джерела:**
  > These macros should be used sparingly, as they can impact performance. They are suitable for critical sections or interrupt routines where other logging macros may not work reliably.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ніякого логування в ISR і пам'яті
- **Прохід:** sweep-31-freertos

---

<!-- fc id:T-31-099 sha:5878c064 src:manual/31-freertos.md:281 status:no-external-signal -->
### T-31-099 · proza · `manual/31-freertos.md`

**Твердження, коротко**

> Двоядерність перетворює теоретичні помилки синхронізації на реальні.

**Контекст**

```
## Що з цього треба запам'ятати

Двоядерність перетворює теоретичні помилки синхронізації на реальні.
```

**Доказ**

- **Статус:** unchecked — не звірено

---
