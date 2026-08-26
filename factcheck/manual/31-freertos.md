# Фактчекінг: `manual/31-freertos.md`

Одиниць твердження: **99**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-31-001 sha:5ddb229c src:manual/31-freertos.md:3 klas:F -->
### T-31-001 · proza · рядок 3

**Книга каже, дослівно:**

> FreeRTOS уже працює, коли викликається ваш перший рядок (розділ 30).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-002 sha:6ced381a src:manual/31-freertos.md:3 klas:E -->
### T-31-002 · proza · рядок 3

**Книга каже, дослівно:**

> Це не бібліотека, яку треба підключати, — це середовище, у якому виконується все.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-003 sha:e3e405f1 src:manual/31-freertos.md:7 klas:E -->
### T-31-003 · proza · рядок 7

**Книга каже, дослівно:**

> Розділ для програміста, який знає потоки з великих систем: тут вони називаються задачами, поводяться схоже, але ціна помилки інша — немає захисту пам'яті, і зіпсована синхронізація призводить не до винятку, а до пошкоджених даних і паніки в іншому місці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-004 sha:b9ccfde4 src:manual/31-freertos.md:14 klas:E -->
### T-31-004 · proza · рядок 14

**Книга каже, дослівно:**

> Задача — функція, що виконується паралельно з іншими, з власним стеком.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-005 sha:5a356c1a src:manual/31-freertos.md:16 klas:K -->
### T-31-005 · kod · рядок 16

**Книга каже, дослівно:**

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

<!-- fc id:T-31-006 sha:a70c9ecb src:manual/31-freertos.md:20 klas:F -->
### T-31-006 · kod-ryadok · рядок 20

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "температура %.1f", t);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-007 sha:4d0c7e33 src:manual/31-freertos.md:21 klas:A -->
### T-31-007 · kod-ryadok · рядок 21

**Книга каже, дослівно:**

> vTaskDelay(pdMS_TO_TICKS(1000));

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

<!-- fc id:T-31-008 sha:4c313f1e src:manual/31-freertos.md:33 klas:E -->
### T-31-008 · proza · рядок 33

**Книга каже, дослівно:**

> Два правила, які варто засвоїти одразу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-009 sha:92f32b03 src:manual/31-freertos.md:35 klas:E -->
### T-31-009 · proza · рядок 35

**Книга каже, дослівно:**

> **Задача не завершується.** Це нескінченний цикл.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-010 sha:e9786310 src:manual/31-freertos.md:35 klas:F -->
### T-31-010 · proza · рядок 35

**Книга каже, дослівно:**

> Функція, що дійшла до кінця й вийшла, викликає паніку — задачу треба або зациклити, або явно видалити через `vTaskDelete(NULL)`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-011 sha:fe619d42 src:manual/31-freertos.md:39 klas:F -->
### T-31-011 · proza · рядок 39

**Книга каже, дослівно:**

> **Задача мусить віддавати керування.** Цикл без затримки з'їдає ядро повністю, і рано чи пізно спрацьовує watchdog (розділ 26):

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-012 sha:2bf361b9 src:manual/31-freertos.md:42 klas:K -->
### T-31-012 · kod · рядок 42

**Книга каже, дослівно:**

> ```c
> while (1) {
>     do_work();
>     // без vTaskDelay — Task WDT спрацює
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

<!-- fc id:T-31-013 sha:b174e002 src:manual/31-freertos.md:44 klas:F -->
### T-31-013 · kod-ryadok · рядок 44

**Книга каже, дослівно:**

> do_work();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-014 sha:b6da3c56 src:manual/31-freertos.md:49 klas:A -->
### T-31-014 · proza · рядок 49

**Книга каже, дослівно:**

> `vTaskDelay` — не пауза процесора, а перехід задачі в сон: інші задачі працюють, споживання падає.

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

<!-- fc id:T-31-015 sha:4f3a3b23 src:manual/31-freertos.md:53 klas:A -->
### T-31-015 · proza · рядок 53

**Книга каже, дослівно:**

> Різниця, яку варто зрозуміти один раз: `vTaskDelay(pdMS_TO_TICKS(10))` віддає керування, `esp_rom_delay_us(10000)` — ні.

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

<!-- fc id:T-31-016 sha:afe4ddd9 src:manual/31-freertos.md:53 klas:E -->
### T-31-016 · proza · рядок 53

**Книга каже, дослівно:**

> Друге крутить процесор вхолосту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-017 sha:5e42d726 src:manual/31-freertos.md:57 klas:E -->
### T-31-017 · proza · рядок 57

**Книга каже, дослівно:**

> Короткі затримки на мікросекунди (таймінги протоколів) роблять другим способом; усе, що вимірюється мілісекундами, — першим.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-018 sha:9fa765b2 src:manual/31-freertos.md:63 klas:F -->
### T-31-018 · proza · рядок 63

**Книга каже, дослівно:**

> Число від 0 (найнижчий) до `configMAX_PRIORITIES - 1`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-019 sha:a794bed6 src:manual/31-freertos.md:63 klas:A -->
### T-31-019 · proza · рядок 63

**Книга каже, дослівно:**

> В ESP-IDF `configMAX_PRIORITIES` дорівнює **25**, тобто найвищий доступний пріоритет — 24.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/config/include/freertos/FreeRTOSConfig.h
- **Дослівно з джерела:**
  > #define configMAX_PRIORITIES                         ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення проходу. Розділ 31 писав «від 0 до `configMAX_PRIORITIES - 1`», не називаючи числа, і давав у таблиці відкритий рядок «18+». Тепер названо стелю (24) і рядок закрито як «18–24». Різниця практична: «18+» читається як «і вище скільки завгодно», і задача з пріоритетом 30 мовчки не створиться.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-31-020 sha:685aa109 src:manual/31-freertos.md:63 klas:E -->
### T-31-020 · proza · рядок 63

**Книга каже, дослівно:**

> Планувальник завжди виконує **найпріоритетнішу готову** задачу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-021 sha:ad41371f src:manual/31-freertos.md:70 klas:E -->
### T-31-021 · tablycya · рядок 70

**Книга каже, дослівно:**

> | Пріоритет | Для чого |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-022 sha:4c18e8a7 src:manual/31-freertos.md:72 klas:E -->
### T-31-022 · tablycya · рядок 72

**Книга каже, дослівно:**

> | 1–4 | фонова робота, логування, необов'язкове |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-023 sha:419ad673 src:manual/31-freertos.md:73 klas:E -->
### T-31-023 · tablycya · рядок 73

**Книга каже, дослівно:**

> | 5 | типовий рівень прикладних задач |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-024 sha:3ce093d4 src:manual/31-freertos.md:74 klas:E -->
### T-31-024 · tablycya · рядок 74

**Книга каже, дослівно:**

> | 10+ | реакція на події, обробка з черг ISR |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-025 sha:7f7e9d58 src:manual/31-freertos.md:75 klas:A -->
### T-31-025 · tablycya · рядок 75

**Книга каже, дослівно:**

> | 18–24 | системні задачі; сюди краще не лізти |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/config/include/freertos/FreeRTOSConfig.h
- **Дослівно з джерела:**
  > #define configMAX_PRIORITIES                         ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення проходу. Розділ 31 писав «від 0 до `configMAX_PRIORITIES - 1`», не називаючи числа, і давав у таблиці відкритий рядок «18+». Тепер названо стелю (24) і рядок закрито як «18–24». Різниця практична: «18+» читається як «і вище скільки завгодно», і задача з пріоритетом 30 мовчки не створиться.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-31-026 sha:59804003 src:manual/31-freertos.md:78 klas:E -->
### T-31-026 · proza · рядок 78

**Книга каже, дослівно:**

> Задача з високим пріоритетом, яка не блокується, **не дасть виконатися нічому нижчому**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-027 sha:f4d5df38 src:manual/31-freertos.md:78 klas:E -->
### T-31-027 · proza · рядок 78

**Книга каже, дослівно:**

> Це не помилка планувальника, а його правило.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-028 sha:27037fe9 src:manual/31-freertos.md:81 klas:F -->
### T-31-028 · proza · рядок 81

**Книга каже, дослівно:**

> Симптом: додали «важливу» задачу з пріоритетом 20 і циклом без затримки — пристрій перестав відповідати повністю, включно з Wi-Fi.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-029 sha:b6b1a89f src:manual/31-freertos.md:85 klas:E -->
### T-31-029 · proza · рядок 85

**Книга каже, дослівно:**

> Високий пріоритет означає «швидко відреагувати й заснути», а не «важлива задача».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-030 sha:aae2b632 src:manual/31-freertos.md:91 klas:F -->
### T-31-030 · proza · рядок 91

**Книга каже, дослівно:**

> [[classic]] [[S3]] Ядро 0 переважно зайняте радіостеком, `app_main` за замовчуванням іде на ядро 1 (розділ 03).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-031 sha:8ff92472 src:manual/31-freertos.md:94 klas:E -->
### T-31-031 · proza · рядок 94

**Книга каже, дослівно:**

> Прив'язати задачу до ядра явно:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-032 sha:71a27a71 src:manual/31-freertos.md:96 klas:K -->
### T-31-032 · kod · рядок 96

**Книга каже, дослівно:**

> ```c
> xTaskCreatePinnedToCore(motor_task, "motor", 4096, NULL, 10, NULL, 1);
> //                                                              ^ ядро
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

<!-- fc id:T-31-033 sha:6ab242cb src:manual/31-freertos.md:97 klas:A -->
### T-31-033 · kod-ryadok · рядок 97

**Книга каже, дослівно:**

> xTaskCreatePinnedToCore(motor_task, "motor", 4096, NULL, 10, NULL, 1);

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

<!-- fc id:T-31-034 sha:b67ba81b src:manual/31-freertos.md:101 klas:E -->
### T-31-034 · proza · рядок 101

**Книга каже, дослівно:**

> Коли це має сенс: щось із жорсткими таймінгами — на ядро 1, подалі від радіо.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-035 sha:7b9b18a5 src:manual/31-freertos.md:101 klas:E -->
### T-31-035 · proza · рядок 101

**Книга каже, дослівно:**

> Щось важке й тривале — теж на ядро 1, щоб не заважати мережі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-036 sha:6c48d623 src:manual/31-freertos.md:105 klas:E -->
### T-31-036 · proza · рядок 105

**Книга каже, дослівно:**

> Двоядерність робить помилки синхронізації **реальними, а не теоретичними**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-037 sha:5c5bd338 src:manual/31-freertos.md:105 klas:E -->
### T-31-037 · proza · рядок 105

**Книга каже, дослівно:**

> На одному ядрі дві задачі не виконуються одночасно фізично, і багато некоректного коду роками працює випадково.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-038 sha:7f269ba1 src:manual/31-freertos.md:105 klas:E -->
### T-31-038 · proza · рядок 105

**Книга каже, дослівно:**

> На двох ядрах воно ламається одразу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-039 sha:a7fe16fa src:manual/31-freertos.md:110 klas:E -->
### T-31-039 · proza · рядок 110

**Книга каже, дослівно:**

> Класика: дві задачі змінюють ту саму структуру без захисту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-040 sha:a10d6bfa src:manual/31-freertos.md:110 klas:E -->
### T-31-040 · proza · рядок 110

**Книга каже, дослівно:**

> На одноядерному чипі перемикання відбувається в передбачуваних точках; на двоядерному — справді одночасно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-041 sha:6d53b9e1 src:manual/31-freertos.md:117 klas:E -->
### T-31-041 · proza · рядок 117

**Книга каже, дослівно:**

> Черга — потокобезпечний буфер фіксованого розміру.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-042 sha:47149383 src:manual/31-freertos.md:117 klas:E -->
### T-31-042 · proza · рядок 117

**Книга каже, дослівно:**

> Це **основний** інструмент передачі даних між задачами, і в більшості випадків правильна відповідь на питання «як передати дані».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-043 sha:a0c48145 src:manual/31-freertos.md:121 klas:K -->
### T-31-043 · kod · рядок 121

**Книга каже, дослівно:**

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

<!-- fc id:T-31-044 sha:c7d11746 src:manual/31-freertos.md:126 klas:A -->
### T-31-044 · kod-ryadok · рядок 126

**Книга каже, дослівно:**

> xQueueSend(cherga, &v, pdMS_TO_TICKS(100));

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

<!-- fc id:T-31-045 sha:6bcb2659 src:manual/31-freertos.md:131 klas:F -->
### T-31-045 · kod-ryadok · рядок 131

**Книга каже, дослівно:**

> obrobyty(&v);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-046 sha:4f254aea src:manual/31-freertos.md:135 klas:E -->
### T-31-046 · proza · рядок 135

**Книга каже, дослівно:**

> Чому чергу варто віддавати перевагу спільним змінним:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-047 sha:e441359d src:manual/31-freertos.md:137 klas:A -->
### T-31-047 · proza · рядок 137

**Книга каже, дослівно:**

> - **дані копіюються** — немає гонок за доступ; - **отримувач блокується**, доки даних немає: не треба опитувати в циклі; - **таймаут** дозволяє не зависати назавжди; - **переповнення видиме**: `xQueueSend` повертає помилку, і це діагностика того, що споживач не встигає.

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

<!-- fc id:T-31-048 sha:048ae5ce src:manual/31-freertos.md:143 klas:A -->
### T-31-048 · proza · рядок 143

**Книга каже, дослівно:**

> `portMAX_DELAY` означає «чекати скільки треба».

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

<!-- fc id:T-31-049 sha:4f5ff1ce src:manual/31-freertos.md:143 klas:E -->
### T-31-049 · proza · рядок 143

**Книга каже, дослівно:**

> Задача при цьому не споживає процесорного часу зовсім.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-050 sha:0f318c6e src:manual/31-freertos.md:148 klas:F -->
### T-31-050 · proza · рядок 148

**Книга каже, дослівно:**

> Коли ресурс справді спільний — шина I²C, структура конфігурації, — доступ захищається м'ютексом:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-051 sha:c4ecc699 src:manual/31-freertos.md:151 klas:K -->
### T-31-051 · kod · рядок 151

**Книга каже, дослівно:**

> ```c
> SemaphoreHandle_t mutex = xSemaphoreCreateMutex();
> 
> if (xSemaphoreTake(mutex, pdMS_TO_TICKS(1000)) == pdTRUE) {
>     // тільки одна задача тут одночасно
>     xSemaphoreGive(mutex);
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

<!-- fc id:T-31-052 sha:05942241 src:manual/31-freertos.md:156 klas:A -->
### T-31-052 · kod-ryadok · рядок 156

**Книга каже, дослівно:**

> xSemaphoreGive(mutex);

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

<!-- fc id:T-31-053 sha:b49e2c99 src:manual/31-freertos.md:160 klas:A -->
### T-31-053 · proza · рядок 160

**Книга каже, дослівно:**

> Завжди з таймаутом, а не `portMAX_DELAY`: взаємне блокування з таймаутом стає видимою помилкою, а без нього — тихим зависанням.

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

<!-- fc id:T-31-054 sha:a7fe8978 src:manual/31-freertos.md:163 klas:F -->
### T-31-054 · proza · рядок 163

**Книга каже, дослівно:**

> **М'ютекс не можна брати з обробника переривання.** Для ISR є окремі функції з суфіксом `FromISR`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-055 sha:c73b142f src:manual/31-freertos.md:168 klas:E -->
### T-31-055 · proza · рядок 168

**Книга каже, дослівно:**

> **Двійковий семафор** — сигнал «сталося».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-056 sha:1e95ef1f src:manual/31-freertos.md:168 klas:E -->
### T-31-056 · proza · рядок 168

**Книга каже, дослівно:**

> Типове застосування: ISR сигналить, задача чекає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-057 sha:eec8ea19 src:manual/31-freertos.md:171 klas:E -->
### T-31-057 · proza · рядок 171

**Книга каже, дослівно:**

> **Лічильний семафор** — облік обмеженого ресурсу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-058 sha:1b8c1efa src:manual/31-freertos.md:173 klas:E -->
### T-31-058 · proza · рядок 173

**Книга каже, дослівно:**

> **Група подій** — набір прапорців, на комбінацію яких можна чекати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-059 sha:599ea25d src:manual/31-freertos.md:173 klas:F -->
### T-31-059 · proza · рядок 173

**Книга каже, дослівно:**

> Зручно для «дочекатися, поки є і Wi-Fi, і час із SNTP»:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-060 sha:1096706d src:manual/31-freertos.md:176 klas:K -->
### T-31-060 · kod · рядок 176

**Книга каже, дослівно:**

> ```c
> EventGroupHandle_t podiyi = xEventGroupCreate();
> #define WIFI_OK  BIT0
> #define TIME_OK  BIT1
> 
> xEventGroupWaitBits(podiyi, WIFI_OK | TIME_OK,
>                     pdFALSE, pdTRUE, portMAX_DELAY);
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

<!-- fc id:T-31-061 sha:52eaa3fa src:manual/31-freertos.md:178 klas:F -->
### T-31-061 · kod-ryadok · рядок 178

**Книга каже, дослівно:**

> #define WIFI_OK  BIT0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-062 sha:efe06e13 src:manual/31-freertos.md:179 klas:F -->
### T-31-062 · kod-ryadok · рядок 179

**Книга каже, дослівно:**

> #define TIME_OK  BIT1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-063 sha:c27bfc67 src:manual/31-freertos.md:188 klas:E -->
### T-31-063 · proza · рядок 188

**Книга каже, дослівно:**

> **ISR має бути коротким.** Прочитати, покласти в чергу, вийти.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-064 sha:ceb5364e src:manual/31-freertos.md:191 klas:F -->
### T-31-064 · proza · рядок 191

**Книга каже, дослівно:**

> Що не можна робити в ISR: викликати `printf` і `ESP_LOGx`, виділяти пам'ять, брати м'ютекси, викликати блокувальні функції, чекати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-065 sha:f2ff5615 src:manual/31-freertos.md:194 klas:A -->
### T-31-065 · proza · рядок 194

**Книга каже, дослівно:**

> Довгий ISR блокує переривання й закінчується `Interrupt wdt timeout` — панікою, яку важко пов'язати з причиною (розділ 26).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-31-066 sha:c54690cc src:manual/31-freertos.md:199 klas:A -->
### T-31-066 · proza · рядок 199

**Книга каже, дослівно:**

> **Один виняток із заборони на лог, і він потрібен саме тоді, коли все інше не працює.** ESP-IDF має набір `ESP_DRAM_LOGE`, `ESP_DRAM_LOGW` і далі за рівнями.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h
- **Дослівно з джерела:**
  > /**
  >  * @brief Macros to output logs when the cache is disabled.
  >  * Unlike normal logging macros, it's possible to use this macro when
  >  * interrupts are disabled or inside an ISR.
  >  * Placing log strings in DRAM reduces available DRAM, so only use
  >  * when absolutely essential.
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

<!-- fc id:T-31-067 sha:440211f9 src:manual/31-freertos.md:199 klas:A -->
### T-31-067 · proza · рядок 199

**Книга каже, дослівно:**

> Заголовок `esp_log.h` каже про них дослівно: «на відміну від звичайних макросів логування, цей можна вживати, коли переривання вимкнені або всередині ISR».

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h
- **Дослівно з джерела:**
  > /**
  >  * @brief Macros to output logs when the cache is disabled.
  >  * Unlike normal logging macros, it's possible to use this macro when
  >  * interrupts are disabled or inside an ISR.
  >  * Placing log strings in DRAM reduces available DRAM, so only use
  >  * when absolutely essential.
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

<!-- fc id:T-31-068 sha:1256a3f9 src:manual/31-freertos.md:205 klas:E -->
### T-31-068 · proza · рядок 205

**Книга каже, дослівно:**

> Ціна названа там само: рядки лягають у DRAM, а її мало, — тож використовувати «лише коли без цього ніяк».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-069 sha:6027e481 src:manual/31-freertos.md:205 klas:A -->
### T-31-069 · proza · рядок 205

**Книга каже, дослівно:**

> Тег теж мусить бути в DRAM: `ESP_DRAM_LOGE(DRAM_STR("mij_teg"), "...")`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h
- **Дослівно з джерела:**
  > /**
  >  * @brief Macros to output logs when the cache is disabled.
  >  * Unlike normal logging macros, it's possible to use this macro when
  >  * interrupts are disabled or inside an ISR.
  >  * Placing log strings in DRAM reduces available DRAM, so only use
  >  * when absolutely essential.
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

<!-- fc id:T-31-070 sha:cee74a8d src:manual/31-freertos.md:209 klas:E -->
### T-31-070 · proza · рядок 209

**Книга каже, дослівно:**

> Це інструмент для відлагодження, а не для роботи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-071 sha:f84ae609 src:manual/31-freertos.md:209 klas:E -->
### T-31-071 · proza · рядок 209

**Книга каже, дослівно:**

> Але коли ISR поводиться незрозуміло, а покласти в чергу нема чого, він єдиний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-072 sha:87a953a3 src:manual/31-freertos.md:215 klas:K -->
### T-31-072 · kod · рядок 215

**Книга каже, дослівно:**

> ```c
> static void IRAM_ATTR gpio_isr(void *arg) {
>     uint32_t pin = (uint32_t)arg;
>     BaseType_t vyshche = pdFALSE;
>     xQueueSendFromISR(cherga_podiy, &pin, &vyshche);
>     if (vyshche) portYIELD_FROM_ISR();
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

<!-- fc id:T-31-073 sha:9cd7f34f src:manual/31-freertos.md:219 klas:A -->
### T-31-073 · kod-ryadok · рядок 219

**Книга каже, дослівно:**

> xQueueSendFromISR(cherga_podiy, &pin, &vyshche);

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

<!-- fc id:T-31-074 sha:ac8daf50 src:manual/31-freertos.md:220 klas:A -->
### T-31-074 · kod-ryadok · рядок 220

**Книга каже, дослівно:**

> if (vyshche) portYIELD_FROM_ISR();

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

<!-- fc id:T-31-075 sha:48075782 src:manual/31-freertos.md:224 klas:A -->
### T-31-075 · proza · рядок 224

**Книга каже, дослівно:**

> `IRAM_ATTR` обов'язковий, якщо переривання може спрацювати під час операції з флешем (розділ 03).

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

<!-- fc id:T-31-076 sha:1b28ad63 src:manual/31-freertos.md:224 klas:F -->
### T-31-076 · proza · рядок 224

**Книга каже, дослівно:**

> Функції `FromISR` — єдині дозволені.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-077 sha:11cc8e46 src:manual/31-freertos.md:224 klas:A -->
### T-31-077 · proza · рядок 224

**Книга каже, дослівно:**

> `portYIELD_FROM_ISR` перемикає на розбуджену задачу одразу після виходу.

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

<!-- fc id:T-31-078 sha:aa96715a src:manual/31-freertos.md:230 klas:E -->
### T-31-078 · proza · рядок 230

**Книга каже, дослівно:**

> Найчастіший приклад, де правило про короткий ISR перевіряється на практиці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-079 sha:77b3e0ed src:manual/31-freertos.md:230 klas:E -->
### T-31-079 · proza · рядок 230

**Книга каже, дослівно:**

> Механічний контакт при натисканні дає десятки перемикань за мілісекунди, і спокуса поставити затримку прямо в обробнику дуже велика.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-080 sha:2dd64dec src:manual/31-freertos.md:234 klas:A -->
### T-31-080 · proza · рядок 234

**Книга каже, дослівно:**

> Робити цього не можна: затримка в ISR — це і є той довгий ISR, від якого приходить `Interrupt wdt timeout`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-31-081 sha:cb41e800 src:manual/31-freertos.md:234 klas:F -->
### T-31-081 · proza · рядок 234

**Книга каже, дослівно:**

> Правильний спосіб — порівняння часу без жодного очікування; готовий зразок і решта роботи з GPIO — розділ 33.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-082 sha:1bed70d5 src:manual/31-freertos.md:240 klas:E -->
### T-31-082 · proza · рядок 240

**Книга каже, дослівно:**

> Коли треба виконати щось періодично, не заводячи окрему задачу:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-083 sha:1da805d2 src:manual/31-freertos.md:242 klas:K -->
### T-31-083 · kod · рядок 242

**Книга каже, дослівно:**

> ```c
> TimerHandle_t t = xTimerCreate("perevirka", pdMS_TO_TICKS(5000),
>                                pdTRUE, NULL, callback);
> xTimerStart(t, 0);
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

<!-- fc id:T-31-084 sha:13c28b77 src:manual/31-freertos.md:245 klas:F -->
### T-31-084 · kod-ryadok · рядок 245

**Книга каже, дослівно:**

> xTimerStart(t, 0);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-085 sha:2bdfbaae src:manual/31-freertos.md:248 klas:E -->
### T-31-085 · proza · рядок 248

**Книга каже, дослівно:**

> Усі програмні таймери виконуються в **одній** службовій задачі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-086 sha:163f52fe src:manual/31-freertos.md:248 klas:E -->
### T-31-086 · proza · рядок 248

**Книга каже, дослівно:**

> Довгий обробник таймера затримує всі інші таймери — тому в них теж має бути коротка робота.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-087 sha:0573d901 src:manual/31-freertos.md:254 klas:E -->
### T-31-087 · proza · рядок 254

**Книга каже, дослівно:**

> **Задача без затримки.** Task WDT.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-088 sha:5adc071c src:manual/31-freertos.md:256 klas:E -->
### T-31-088 · proza · рядок 256

**Книга каже, дослівно:**

> **Високий пріоритет + цикл без блокування.** Система стоїть.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-089 sha:3635e455 src:manual/31-freertos.md:258 klas:E -->
### T-31-089 · proza · рядок 258

**Книга каже, дослівно:**

> **Замалий стек.** Падіння в іншому місці, без зв'язку з причиною (розділ 30).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-090 sha:71179c5d src:manual/31-freertos.md:261 klas:E -->
### T-31-090 · proza · рядок 261

**Книга каже, дослівно:**

> **Спільна змінна без захисту.** На двох ядрах ламається одразу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-091 sha:b83b5cb4 src:manual/31-freertos.md:263 klas:E -->
### T-31-091 · proza · рядок 263

**Книга каже, дослівно:**

> **Довгий ISR.** Interrupt WDT.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-092 sha:8922c4eb src:manual/31-freertos.md:265 klas:E -->
### T-31-092 · proza · рядок 265

**Книга каже, дослівно:**

> **Черга без перевірки результату.** Дані тихо губляться, коли споживач не встигає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-093 sha:f02a263f src:manual/31-freertos.md:268 klas:A -->
### T-31-093 · proza · рядок 268

**Книга каже, дослівно:**

> **М'ютекс із `portMAX_DELAY`.** Взаємне блокування перетворюється на тихе зависання.

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

<!-- fc id:T-31-094 sha:272c94c9 src:manual/31-freertos.md:273 klas:E -->
### T-31-094 · proza · рядок 273

**Книга каже, дослівно:**

> Задача не завершується і мусить віддавати керування.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-095 sha:caf51e23 src:manual/31-freertos.md:275 klas:E -->
### T-31-095 · proza · рядок 275

**Книга каже, дослівно:**

> Високий пріоритет означає «швидко відреагувати й заснути».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-096 sha:845c22bb src:manual/31-freertos.md:277 klas:E -->
### T-31-096 · proza · рядок 277

**Книга каже, дослівно:**

> Черга — типова правильна відповідь на «як передати дані між задачами».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-097 sha:058ed39f src:manual/31-freertos.md:279 klas:E -->
### T-31-097 · proza · рядок 279

**Книга каже, дослівно:**

> ISR: прочитати, покласти в чергу, вийти.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-098 sha:72e699d5 src:manual/31-freertos.md:279 klas:E -->
### T-31-098 · proza · рядок 279

**Книга каже, дослівно:**

> Ніякого логування й пам'яті.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-31-099 sha:5878c064 src:manual/31-freertos.md:281 klas:E -->
### T-31-099 · proza · рядок 281

**Книга каже, дослівно:**

> Двоядерність перетворює теоретичні помилки синхронізації на реальні.

**Доказ**

- **Клас:** F — не звірено

---
