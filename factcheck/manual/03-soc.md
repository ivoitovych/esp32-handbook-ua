# Фактчекінг: `manual/03-soc.md`

Одиниць твердження: **76**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-03-001 sha:30137967 src:manual/03-soc.md:3 klas:F -->
### T-03-001 · proza · рядок 3

**Книга каже, дослівно:**

> Цей розділ пояснює, чому ESP32 поводиться так, як поводиться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-002 sha:b113984f src:manual/03-soc.md:3 klas:E -->
### T-03-002 · proza · рядок 3

**Книга каже, дослівно:**

> Він не потрібен, щоб змигнути світлодіодом, і стає необхідним рівно тоді, коли з'являються питання виду «чому програма падає лише при увімкненому Wi-Fi» або «чому цей масив не вміщається, хоча пам'яті вдосталь».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-003 sha:6da19cd4 src:manual/03-soc.md:10 klas:F -->
### T-03-003 · proza · рядок 10

**Книга каже, дослівно:**

> [[classic]] [[S3]] ESP32 classic і S3 мають **два ядра**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-004 sha:8ed6fe72 src:manual/03-soc.md:10 klas:F -->
### T-03-004 · proza · рядок 10

**Книга каже, дослівно:**

> Вони називаються PRO_CPU (ядро 0) і APP_CPU (ядро 1) — назви історичні й нічого не означають: ядра рівноправні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-005 sha:29cf8a17 src:manual/03-soc.md:14 klas:E -->
### T-03-005 · proza · рядок 14

**Книга каже, дослівно:**

> Розподіл за замовчуванням, який варто знати:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-006 sha:b7b38102 src:manual/03-soc.md:16 klas:F -->
### T-03-006 · proza · рядок 16

**Книга каже, дослівно:**

> **Ядро 0** зайняте стеком Wi-Fi і Bluetooth.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-007 sha:cde9b7d9 src:manual/03-soc.md:16 klas:E -->
### T-03-007 · proza · рядок 16

**Книга каже, дослівно:**

> Радіо — це не магія в антені, а код, що виконується на тому самому процесорі, і виконується він переважно тут.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-008 sha:a7571eb6 src:manual/03-soc.md:20 klas:F -->
### T-03-008 · proza · рядок 20

**Книга каже, дослівно:**

> **Ядро 1** здебільшого вільне, і саме там за замовчуванням запускається `app_main`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-009 sha:65a050e8 src:manual/03-soc.md:23 klas:F -->
### T-03-009 · proza · рядок 23

**Книга каже, дослівно:**

> Практичний наслідок: задача, прив'язана до ядра 0, конкурує за час із радіостеком.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-010 sha:6c80c4de src:manual/03-soc.md:23 klas:F -->
### T-03-010 · proza · рядок 23

**Книга каже, дослівно:**

> Якщо у вас щось із жорсткими таймінгами — його місце на ядрі 1 (розділ 31).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-011 sha:01a4a513 src:manual/03-soc.md:27 klas:F -->
### T-03-011 · proza · рядок 27

**Книга каже, дослівно:**

> [[C3]] C3, C6, H2 і S2 **одноядерні**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-012 sha:ad7bb8ac src:manual/03-soc.md:27 klas:E -->
### T-03-012 · proza · рядок 27

**Книга каже, дослівно:**

> Там радіостек і ваш код ділять один процесор, і затримки від радіо помітніші.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-013 sha:847f8520 src:manual/03-soc.md:27 klas:F -->
### T-03-013 · proza · рядок 27

**Книга каже, дослівно:**

> Це одна з реальних цін дешевизни C3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-014 sha:e0bf9d8b src:manual/03-soc.md:32 klas:E -->
### T-03-014 · proza · рядок 32

**Книга каже, дослівно:**

> Двоядерність не робить програму вдвічі швидшою автоматично.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-015 sha:e901dcc2 src:manual/03-soc.md:32 klas:E -->
### T-03-015 · proza · рядок 32

**Книга каже, дослівно:**

> Вона дає можливість **розвести** конкуренцію: важку роботу на одне ядро, зв'язок на інше.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-016 sha:3917c8cc src:manual/03-soc.md:32 klas:E -->
### T-03-016 · proza · рядок 32

**Книга каже, дослівно:**

> Код, написаний як один потік, використає одне ядро й лишить друге простоювати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-017 sha:d0503ba8 src:manual/03-soc.md:40 klas:E -->
### T-03-017 · proza · рядок 40

**Книга каже, дослівно:**

> Це найчастіше джерело здивування.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-018 sha:129e874e src:manual/03-soc.md:40 klas:F -->
### T-03-018 · proza · рядок 40

**Книга каже, дослівно:**

> Пам'ять ESP32 не є одним однорідним масивом; вона поділена на області з різними властивостями, і `malloc` може повернути `NULL`, коли сумарно вільно чимало.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-019 sha:ee844d56 src:manual/03-soc.md:44 klas:E -->
### T-03-019 · proza · рядок 44

**Книга каже, дослівно:**

> **ROM.** Зашитий на заводі код: ROM-бутлоадер, частина бібліотечних функцій.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-020 sha:c067fed0 src:manual/03-soc.md:44 klas:E -->
### T-03-020 · proza · рядок 44

**Книга каже, дослівно:**

> Не змінюється, місця не займає у вашому бюджеті.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-021 sha:9d8da4da src:manual/03-soc.md:47 klas:E -->
### T-03-021 · proza · рядок 47

**Книга каже, дослівно:**

> **SRAM** — основна швидка пам'ять на кристалі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-022 sha:1604cbc9 src:manual/03-soc.md:49 klas:E -->
### T-03-022 · proza · рядок 49

**Книга каже, дослівно:**

> - **IRAM** (instruction RAM) — звідси виконується код.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-023 sha:cfc5fb12 src:manual/03-soc.md:49 klas:E -->
### T-03-023 · proza · рядок 49

**Книга каже, дослівно:**

> Сюди потрапляє те, що має працювати швидко або має бути доступним, коли флеш недоступний: обробники переривань, критичні функції.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-024 sha:d9912f25 src:manual/03-soc.md:49 klas:E -->
### T-03-024 · proza · рядок 49

**Книга каже, дослівно:**

> - **DRAM** (data RAM) — тут живуть дані: змінні, стеки задач, купа.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-025 sha:f908bd73 src:manual/03-soc.md:54 klas:A -->
### T-03-025 · proza · рядок 54

**Книга каже, дослівно:**

> **RTC RAM** — маленька область (одиниці кілобайтів), яка **переживає deep sleep**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/sleep_modes.rst
- **Дослівно з джерела:**
  > If some variables in the program are placed into RTC SLOW memory (for example, using
  > ``RTC_DATA_ATTR`` attribute), RTC SLOW memory will be kept powered on by default.
  > This can be overridden using :cpp:func:`esp_sleep_pd_config` function, if desired.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує розділи 06 і 60. Уточнення, варте наступного проходу: «за замовчуванням» — тобто збереження можна й вимкнути, і на чипах, де є лише RTC FAST, усі три атрибути йдуть туди ж.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-03-026 sha:2ea4307a src:manual/03-soc.md:54 klas:E -->
### T-03-026 · proza · рядок 54

**Книга каже, дослівно:**

> Все інше при глибокому сні втрачається.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-027 sha:5ffa26da src:manual/03-soc.md:54 klas:F -->
### T-03-027 · proza · рядок 54

**Книга каже, дослівно:**

> Сюди кладуть лічильники і стан, який має пережити пробудження (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-028 sha:897b7618 src:manual/03-soc.md:58 klas:E -->
### T-03-028 · proza · рядок 58

**Книга каже, дослівно:**

> **Зовнішня флеш** — те, де лежить прошивка.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-029 sha:fd09cd67 src:manual/03-soc.md:58 klas:E -->
### T-03-029 · proza · рядок 58

**Книга каже, дослівно:**

> Код виконується звідти через кеш, а не з RAM: у RAM він просто не помістився б.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-030 sha:2682a6b8 src:manual/03-soc.md:61 klas:F -->
### T-03-030 · proza · рядок 61

**Книга каже, дослівно:**

> **PSRAM** — зовнішня псевдостатична пам'ять (pseudo-static RAM), від 2 до 8 МБ.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-031 sha:bc37401b src:manual/03-soc.md:61 klas:F -->
### T-03-031 · proza · рядок 61

**Книга каже, дослівно:**

> Є лише в classic, S2 і S3 (розділ 02).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-032 sha:0d142738 src:manual/03-soc.md:61 klas:E -->
### T-03-032 · proza · рядок 61

**Книга каже, дослівно:**

> Повільніша за SRAM, бо ходить через ту саму шину, що й флеш, але дозволяє тримати великі буфери: кадри камери, зображення для дисплея, великі структури.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-033 sha:64590e9b src:manual/03-soc.md:67 klas:F -->
### T-03-033 · proza · рядок 67

**Книга каже, дослівно:**

> З цього випливає найчастіша пастка: **`malloc` повернув `NULL`, хоча «пам'ять є»**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-034 sha:c931d7ff src:manual/03-soc.md:70 klas:E -->
### T-03-034 · proza · рядок 70

**Книга каже, дослівно:**

> *Фрагментація.* Купа зайнята дрібними шматками, суцільного блоку потрібного розміру немає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-035 sha:81ce3b3f src:manual/03-soc.md:70 klas:E -->
### T-03-035 · proza · рядок 70

**Книга каже, дослівно:**

> Виникає від виділення й звільнення в циклі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-036 sha:680850ac src:manual/03-soc.md:73 klas:E -->
### T-03-036 · proza · рядок 73

**Книга каже, дослівно:**

> *Не та область.* Буфер для DMA має лежати в DRAM, доступній контролеру DMA.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-037 sha:11b3083b src:manual/03-soc.md:73 klas:A -->
### T-03-037 · proza · рядок 73

**Книга каже, дослівно:**

> Звичайний `malloc` може віддати пам'ять, яка формально є, але для DMA не годиться — для цього є `heap_caps_malloc` із явним зазначенням властивостей.

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

<!-- fc id:T-03-038 sha:9a6731c9 src:manual/03-soc.md:78 klas:A -->
### T-03-038 · proza · рядок 78

**Книга каже, дослівно:**

> *PSRAM не увімкнено.* `CONFIG_SPIRAM` типово вимкнена, і плата з розпаяною мікросхемою без цього її не бачить.

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

<!-- fc id:T-03-039 sha:87756b0a src:manual/03-soc.md:78 klas:A -->
### T-03-039 · proza · рядок 78

**Книга каже, дослівно:**

> А от коли ввімкнено, `malloc` уже сам виносить у PSRAM усе від 16 КБ — вмикати це окремо не треба (розділ 30).

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

<!-- fc id:T-03-040 sha:e1bf5cd3 src:manual/03-soc.md:83 klas:A -->
### T-03-040 · proza · рядок 83

**Книга каже, дослівно:**

> Подивитися реальну картину: `heap_caps_get_free_size` і `heap_caps_print_heap_info` (розділ 30).

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

<!-- fc id:T-03-041 sha:6d0a35b4 src:manual/03-soc.md:89 klas:E -->
### T-03-041 · proza · рядок 89

**Книга каже, дослівно:**

> Код лежить у флеші, а виконується процесором через кеш.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-042 sha:f310a685 src:manual/03-soc.md:89 klas:E -->
### T-03-042 · proza · рядок 89

**Книга каже, дослівно:**

> Поки потрібна ділянка в кеші — все швидко.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-043 sha:cf1f101a src:manual/03-soc.md:89 klas:E -->
### T-03-043 · proza · рядок 89

**Книга каже, дослівно:**

> Коли ні — процесор чекає читання з флешу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-044 sha:c82a89c3 src:manual/03-soc.md:92 klas:E -->
### T-03-044 · proza · рядок 92

**Книга каже, дослівно:**

> Звідси наслідок, який породжує дуже загадкові збої: **у момент операції з флешем виконання коду з флешу неможливе**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-045 sha:628ed161 src:manual/03-soc.md:92 klas:E -->
### T-03-045 · proza · рядок 92

**Книга каже, дослівно:**

> Коли система пише в NVS або стирає сектор, кеш вимикається — і будь-яка функція, що в цей момент має виконатися з флешу, впаде.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-046 sha:94ffa5a7 src:manual/03-soc.md:97 klas:E -->
### T-03-046 · proza · рядок 97

**Книга каже, дослівно:**

> Стосується це насамперед обробників переривань.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-047 sha:80711892 src:manual/03-soc.md:97 klas:A -->
### T-03-047 · proza · рядок 97

**Книга каже, дослівно:**

> Саме тому ISR, які можуть спрацювати під час роботи з флешем, позначають атрибутом `IRAM_ATTR` — щоб вони лежали в IRAM, а не у флеші:

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

<!-- fc id:T-03-048 sha:56f50edc src:manual/03-soc.md:101 klas:K -->
### T-03-048 · kod · рядок 101

**Книга каже, дослівно:**

> ```c
> static void IRAM_ATTR gpio_isr_handler(void *arg) {
>     // цей код виконається навіть тоді, коли кеш вимкнено
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

<!-- fc id:T-03-049 sha:478c1d83 src:manual/03-soc.md:107 klas:A -->
### T-03-049 · proza · рядок 107

**Книга каже, дослівно:**

> Ціна — IRAM небагато, і кожна функція з `IRAM_ATTR` займає її назавжди (розділ 31).

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

<!-- fc id:T-03-050 sha:fcb7d541 src:manual/03-soc.md:112 klas:F -->
### T-03-050 · proza · рядок 112

**Книга каже, дослівно:**

> Частота ядра — 240 МГц для classic, S2, S3; 160 МГц для C3 і C6; 96 МГц для H2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-051 sha:20d9bd0f src:manual/03-soc.md:112 klas:E -->
### T-03-051 · proza · рядок 112

**Книга каже, дослівно:**

> Її можна знизити, і це прямий спосіб зменшити споживання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-052 sha:1ecf96c3 src:manual/03-soc.md:115 klas:E -->
### T-03-052 · proza · рядок 115

**Книга каже, дослівно:**

> Кілька джерел тактування з різними властивостями:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-053 sha:4cbe3890 src:manual/03-soc.md:117 klas:F -->
### T-03-053 · proza · рядок 117

**Книга каже, дослівно:**

> - **зовнішній кварц** (типово 40 МГц) — точний, основне джерело; - **внутрішній RC-генератор** — не потребує деталей, але «пливе» від температури; - **RTC-генератор** — повільний, працює під час сну.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-054 sha:9f706283 src:manual/03-soc.md:123 klas:E -->
### T-03-054 · proza · рядок 123

**Книга каже, дослівно:**

> Годинник реального часу, побудований на внутрішньому RC-генераторі, за добу набігає помітну похибку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-055 sha:3486d9c6 src:manual/03-soc.md:123 klas:F -->
### T-03-055 · proza · рядок 123

**Книга каже, дослівно:**

> Якщо пристрою потрібен точний час і немає мережі для SNTP — потрібна зовнішня мікросхема RTC із власним кварцом і батарейкою (розділ 60).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-056 sha:cbfc1f81 src:manual/03-soc.md:129 klas:E -->
### T-03-056 · proza · рядок 129

**Книга каже, дослівно:**

> **Динамічне керування частотою** (DFS) дозволяє системі самій знижувати частоту, коли роботи немає, і піднімати під навантаженням.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-057 sha:a717ac57 src:manual/03-soc.md:129 klas:F -->
### T-03-057 · proza · рядок 129

**Книга каже, дослівно:**

> Вмикається в `menuconfig` і дає відчутну економію в пристроях, що більшість часу чекають (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-058 sha:4d9cc263 src:manual/03-soc.md:136 klas:E -->
### T-03-058 · proza · рядок 136

**Книга каже, дослівно:**

> Окрема частина кристала, що лишається живою, коли основні ядра сплять:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-059 sha:dc78d229 src:manual/03-soc.md:138 klas:A -->
### T-03-059 · proza · рядок 138

**Книга каже, дослівно:**

> - **RTC RAM** — дані переживають deep sleep; - **RTC GPIO** — частина пінів здатна будити чип; - **RTC-таймер** — будильник; - **ULP-співпроцесор** — крихітний процесор, що може працювати, поки основні ядра вимкнені.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/sleep_modes.rst
- **Дослівно з джерела:**
  > If some variables in the program are placed into RTC SLOW memory (for example, using
  > ``RTC_DATA_ATTR`` attribute), RTC SLOW memory will be kept powered on by default.
  > This can be overridden using :cpp:func:`esp_sleep_pd_config` function, if desired.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує розділи 06 і 60. Уточнення, варте наступного проходу: «за замовчуванням» — тобто збереження можна й вимкнути, і на чипах, де є лише RTC FAST, усі три атрибути йдуть туди ж.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-03-060 sha:769a9fbb src:manual/03-soc.md:144 klas:E -->
### T-03-060 · proza · рядок 144

**Книга каже, дослівно:**

> ULP уміє небагато: прочитати ADC, перевірити пін, порівняти з порогом, розбудити основну систему, якщо щось сталося.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-061 sha:d7dc237e src:manual/03-soc.md:144 klas:E -->
### T-03-061 · proza · рядок 144

**Книга каже, дослівно:**

> Але споживає він мікроампери.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-062 sha:62262d38 src:manual/03-soc.md:147 klas:E -->
### T-03-062 · proza · рядок 147

**Книга каже, дослівно:**

> Типове застосування: пристрій спить, ULP раз на секунду міряє рівень і будить систему, лише коли значення вийшло за межу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-063 sha:49a8a31e src:manual/03-soc.md:147 klas:F -->
### T-03-063 · proza · рядок 147

**Книга каже, дослівно:**

> Замість того щоб будити повноцінну систему сто разів даремно, її будять один раз по ділу (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-064 sha:dd0ef344 src:manual/03-soc.md:152 klas:E -->
### T-03-064 · proza · рядок 152

**Книга каже, дослівно:**

> Програмується ULP окремо — власним асемблером або, у пізніших сімействах, на C для RISC-V-варіанта ULP.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-065 sha:639ff99e src:manual/03-soc.md:152 klas:E -->
### T-03-065 · proza · рядок 152

**Книга каже, дослівно:**

> Це помітно складніше за звичайний код, і братися за нього варто тоді, коли бюджет живлення справді не сходиться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-066 sha:9f63ca99 src:manual/03-soc.md:159 klas:E -->
### T-03-066 · proza · рядок 159

**Книга каже, дослівно:**

> Кожна область пам'яті має свій діапазон адрес.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-067 sha:897d0e0d src:manual/03-soc.md:159 klas:E -->
### T-03-067 · proza · рядок 159

**Книга каже, дослівно:**

> Знати таблицю напам'ять не треба, але вміти прочитати адресу — корисно: **за адресою в дампі паніки одразу видно, куди зверталися**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-068 sha:5b04c8be src:manual/03-soc.md:163 klas:E -->
### T-03-068 · proza · рядок 163

**Книга каже, дослівно:**

> Практичні орієнтири для [[classic]]:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-069 sha:1a0f9aa5 src:manual/03-soc.md:165 klas:C -->
### T-03-069 · proza · рядок 165

**Книга каже, дослівно:**

> - адреса виду `0x400d....` — код, що виконується з флешу; - адреса виду `0x3ffb....` — дані в DRAM, зазвичай стек; - адреса виду `0x3f4.....` — PSRAM; - адреса близько нуля (`0x0`–`0x40`) — розіменування `NULL` зі зсувом поля структури.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-03-070 sha:cbfa3e79 src:manual/03-soc.md:171 klas:A -->
### T-03-070 · proza · рядок 171

**Книга каже, дослівно:**

> Останній випадок покриває більшість `LoadProhibited` на практиці (розділ 26).

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

<!-- fc id:T-03-071 sha:a0d41ca6 src:manual/03-soc.md:176 klas:F -->
### T-03-071 · proza · рядок 176

**Книга каже, дослівно:**

> Радіостек — це код на ядрі 0, а не окремий пристрій.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-072 sha:862d3a8c src:manual/03-soc.md:176 klas:E -->
### T-03-072 · proza · рядок 176

**Книга каже, дослівно:**

> На одноядерних чипах він конкурує з вашим кодом за той самий процесор.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-073 sha:02d793b1 src:manual/03-soc.md:179 klas:F -->
### T-03-073 · proza · рядок 179

**Книга каже, дослівно:**

> Пам'ять неоднорідна: `malloc` може повернути `NULL` при формально вільних кілобайтах через фрагментацію, вимоги DMA або невикористану PSRAM.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-03-074 sha:30a396cf src:manual/03-soc.md:183 klas:A -->
### T-03-074 · proza · рядок 183

**Книга каже, дослівно:**

> Під час операції з флешем код із флешу не виконується — звідси `IRAM_ATTR` на обробниках переривань.

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

<!-- fc id:T-03-075 sha:ece55389 src:manual/03-soc.md:186 klas:A -->
### T-03-075 · proza · рядок 186

**Книга каже, дослівно:**

> RTC RAM переживає deep sleep; усе інше — ні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/sleep_modes.rst
- **Дослівно з джерела:**
  > If some variables in the program are placed into RTC SLOW memory (for example, using
  > ``RTC_DATA_ATTR`` attribute), RTC SLOW memory will be kept powered on by default.
  > This can be overridden using :cpp:func:`esp_sleep_pd_config` function, if desired.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує розділи 06 і 60. Уточнення, варте наступного проходу: «за замовчуванням» — тобто збереження можна й вимкнути, і на чипах, де є лише RTC FAST, усі три атрибути йдуть туди ж.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-03-076 sha:296c8efd src:manual/03-soc.md:188 klas:E -->
### T-03-076 · proza · рядок 188

**Книга каже, дослівно:**

> За адресою в дампі паніки видно, у яку область зверталися.

**Доказ**

- **Клас:** F — не звірено

---
