# Фактчекінг: `manual/62-proj-keruvannya.md`

Одиниць твердження: **108**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-62-001 sha:89199f03 src:manual/62-proj-keruvannya.md:3 klas:F -->
### T-62-001 · proza · рядок 3

**Книга каже, дослівно:**

> Пристрій вмикає й вимикає щось реальне: насос, клапан, нагрівач, двигун.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-002 sha:2538859d src:manual/62-proj-keruvannya.md:3 klas:F -->
### T-62-002 · proza · рядок 3

**Книга каже, дослівно:**

> Тема проєкту — **безпечна поведінка**, а не функціональність.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-003 sha:12bac0d9 src:manual/62-proj-keruvannya.md:6 klas:F -->
### T-62-003 · proza · рядок 6

**Книга каже, дослівно:**

> Різниця з попередніми проєктами принципова: помилка тут має фізичні наслідки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-004 sha:5ba52005 src:manual/62-proj-keruvannya.md:6 klas:F -->
### T-62-004 · proza · рядок 6

**Книга каже, дослівно:**

> Насос, що не вимкнувся, заливає приміщення; нагрівач — підпалює.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-005 sha:440f9993 src:manual/62-proj-keruvannya.md:12 klas:F -->
### T-62-005 · proza · рядок 12

**Книга каже, дослівно:**

> **Задача:** керувати насосом за розкладом і за датчиком рівня, з можливістю ручного втручання по мережі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-006 sha:a0c4300b src:manual/62-proj-keruvannya.md:15 klas:F -->
### T-62-006 · proza · рядок 15

**Книга каже, дослівно:**

> **Виходи:** реле насоса, індикація стану.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-007 sha:bb0b772d src:manual/62-proj-keruvannya.md:17 klas:F -->
### T-62-007 · proza · рядок 17

**Книга каже, дослівно:**

> **Входи:** датчик рівня (поплавковий вимикач), кнопка «стоп», кнопка ручного пуску.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-008 sha:96c5340a src:manual/62-proj-keruvannya.md:20 klas:F -->
### T-62-008 · proza · рядок 20

**Книга каже, дослівно:**

> **Безпека:** - насос вимкнений при зникненні живлення, при зависанні, при перезавантаженні; - жорсткий ліміт часу безперервної роботи; - захист від сухого ходу; - аварійна зупинка апаратна, не програмна; - втрата зв'язку не змінює стан механізму.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-009 sha:77a45dd4 src:manual/62-proj-keruvannya.md:31 klas:F -->
### T-62-009 · proza · рядок 31

**Книга каже, дослівно:**

> **Питання, з якого починається проєкт: що станеться, якщо чип зникне просто зараз?**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-010 sha:52ffe580 src:manual/62-proj-keruvannya.md:34 klas:F -->
### T-62-010 · proza · рядок 34

**Книга каже, дослівно:**

> Відповідь має бути «насос вимкнеться», і забезпечується вона схемотехнікою, а не програмою (розділи 32, 47).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-011 sha:3df5db21 src:manual/62-proj-keruvannya.md:37 klas:F -->
### T-62-011 · proza · рядок 37

**Книга каже, дослівно:**

> Три речі, які треба зробити на платі:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-012 sha:f384e7dc src:manual/62-proj-keruvannya.md:39 klas:F -->
### T-62-012 · proza · рядок 39

**Книга каже, дослівно:**

> **Резистор 10 кОм, що утримує керувальний вхід у стані «вимкнено».** Під час завантаження GPIO перебуває у високоімпедансному стані — без резистора вхід висить, і реле може ввімкнутися саме в момент старту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-013 sha:24f28a5e src:manual/62-proj-keruvannya.md:39 klas:F -->
### T-62-013 · proza · рядок 39

**Книга каже, дослівно:**

> При boot loop (розділ 20) це означає блимання насосом раз на секунду.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-014 sha:ba1a98ae src:manual/62-proj-keruvannya.md:39 klas:F -->
### T-62-014 · proza · рядок 39

**Книга каже, дослівно:**

> Куди саме йде цей резистор — на землю чи на 3V3 — залежить від того, яким рівнем вмикається ваш модуль; таблиця в наступному підрозділі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-015 sha:99b36b89 src:manual/62-proj-keruvannya.md:46 klas:F -->
### T-62-015 · proza · рядок 46

**Книга каже, дослівно:**

> **Реле з нормально розімкненими контактами.** Знеструмлене реле = вимкнений насос.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-016 sha:42efe84d src:manual/62-proj-keruvannya.md:49 klas:F -->
### T-62-016 · proza · рядок 49

**Книга каже, дослівно:**

> **Апаратний аварійний вимикач у розрив живлення насоса**, не в логіку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-017 sha:dda89b86 src:manual/62-proj-keruvannya.md:49 klas:F -->
### T-62-017 · proza · рядок 49

**Книга каже, дослівно:**

> Кнопка, що подає сигнал на GPIO, не працює, коли чип завис.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-018 sha:efe8ee6b src:manual/62-proj-keruvannya.md:49 klas:F -->
### T-62-018 · proza · рядок 49

**Книга каже, дослівно:**

> Кнопка, що розриває коло, працює завжди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-019 sha:9bf90e1f src:manual/62-proj-keruvannya.md:54 klas:F -->
### T-62-019 · proza · рядок 54

**Книга каже, дослівно:**

> Перевірка цих трьох речей — перший пункт випробувань, і робиться вона до написання логіки: подати живлення, поспостерігати за реле під час завантаження; висмикнути живлення під час роботи насоса.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-020 sha:dbc86f12 src:manual/62-proj-keruvannya.md:60 klas:F -->
### T-62-020 · proza · рядок 60

**Книга каже, дослівно:**

> Силове коло — усе послідовно, і аварійний вимикач у ньому фізично:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-021 sha:b9ff9d58 src:manual/62-proj-keruvannya.md:62 klas:F -->
### T-62-021 · kod · рядок 62

**Книга каже, дослівно:**

> ```
> +12 В ── [насос] ── [реле: контакти NO] ── [аварійний вимикач] ── GND
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-022 sha:2a932c15 src:manual/62-proj-keruvannya.md:66 klas:F -->
### T-62-022 · proza · рядок 66

**Книга каже, дослівно:**

> Коло керування реле — окреме, від 5 В, а не від 3V3:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-023 sha:93c68e4b src:manual/62-proj-keruvannya.md:68 klas:F -->
### T-62-023 · kod · рядок 68

**Книга каже, дослівно:**

> ```
>    5 В ──── VCC модуля реле
>    GND ──── GND модуля  (спільна з ESP32)
> 
> GPIO25 ──┬──[220 Ом]──── IN модуля
>          │
>       [10 кОм]  ← напрямок підтяжки залежить від модуля, див. нижче
>          │
>        GND  або  3V3
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-024 sha:de2eca7d src:manual/62-proj-keruvannya.md:81 klas:F -->
### T-62-024 · kod · рядок 81

**Книга каже, дослівно:**

> ```
> GPIO34 ── поплавковий вимикач ── GND   (+ зовнішня підтяжка 10 кОм до 3V3!)
> GPIO26 ── кнопка «стоп» ── GND         (внутрішня підтяжка)
> GPIO27 ── кнопка «пуск» ── GND
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-025 sha:dec1d5dd src:manual/62-proj-keruvannya.md:88 klas:F -->
### T-62-025 · proza · рядок 88

**Книга каже, дослівно:**

> **Два питання до релейного модуля, які треба закрити до монтажу** (розділ 47).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-026 sha:1027195f src:manual/62-proj-keruvannya.md:91 klas:F -->
### T-62-026 · proza · рядок 91

**Книга каже, дослівно:**

> **Від чого живиться котушка.** Більшість готових модулів розраховані на **5 В**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-027 sha:bba06f58 src:manual/62-proj-keruvannya.md:91 klas:F -->
### T-62-027 · proza · рядок 91

**Книга каже, дослівно:**

> Від 3.3 В реле або не спрацює, або спрацьовуватиме через раз — класичне «іноді вмикається».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-028 sha:c49cada8 src:manual/62-proj-keruvannya.md:91 klas:F -->
### T-62-028 · proza · рядок 91

**Книга каже, дослівно:**

> Тому `VCC` модуля йде на 5 В, а не на 3V3; керувальний вхід при цьому приймає 3.3-вольтову логіку, бо на модулі стоїть оптопара.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-029 sha:f49c43fd src:manual/62-proj-keruvannya.md:97 klas:F -->
### T-62-029 · proza · рядок 97

**Книга каже, дослівно:**

> **Яким рівнем вмикається.** Багато модулів **інверсні**: реле вмикається логічним **нулем**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-030 sha:5e02ec72 src:manual/62-proj-keruvannya.md:97 klas:F -->
### T-62-030 · proza · рядок 97

**Книга каже, дослівно:**

> Від цього залежить напрямок підтяжки, і помилитися тут означає отримати рівно те, від чого весь цей розділ:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-031 sha:70b70869 src:manual/62-proj-keruvannya.md:101 klas:F -->
### T-62-031 · tablycya-shapka · рядок 101

**Книга каже, дослівно:**

> | Модуль вмикається | Підтяжка 10 кОм | Стан під час завантаження |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-032 sha:d08185e1 src:manual/62-proj-keruvannya.md:102 klas:F -->
### T-62-032 · komirka · рядок 102

**Книга каже, дослівно:**

> високим рівнем · Підтяжка 10 кОм → **на GND**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-033 sha:4efee294 src:manual/62-proj-keruvannya.md:102 klas:F -->
### T-62-033 · komirka · рядок 102

**Книга каже, дослівно:**

> високим рівнем · Стан під час завантаження → реле вимкнене

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-034 sha:867a666c src:manual/62-proj-keruvannya.md:103 klas:F -->
### T-62-034 · komirka · рядок 103

**Книга каже, дослівно:**

> низьким рівнем (інверсний) · Підтяжка 10 кОм → **на 3V3**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-035 sha:3061b493 src:manual/62-proj-keruvannya.md:103 klas:F -->
### T-62-035 · komirka · рядок 103

**Книга каже, дослівно:**

> низьким рівнем (інверсний) · Стан під час завантаження → реле вимкнене

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-036 sha:9256213b src:manual/62-proj-keruvannya.md:106 klas:F -->
### T-62-036 · proza · рядок 106

**Книга каже, дослівно:**

> Правило одне і формулюється не через напрямок, а через результат: **резистор утримує вхід у стані «вимкнено», поки GPIO ще не налаштований.** Перевіряється це не за схемою, а дослідом: подати живлення десять разів і подивитися на реле (пункт 1 випробувань нижче).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-037 sha:04f1066f src:manual/62-proj-keruvannya.md:113 klas:F -->
### T-62-037 · proza · рядок 113

**Книга каже, дослівно:**

> [[classic]] `GPIO34` — тільки вхід і **без вбудованого підтягування** (розділ 07).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-038 sha:7ab48ab4 src:manual/62-proj-keruvannya.md:113 klas:F -->
### T-62-038 · proza · рядок 113

**Книга каже, дослівно:**

> Поплавковому вимикачу потрібен зовнішній резистор 10 кОм до 3.3 В, інакше вхід бовтається й насос вмикається від наводок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-039 sha:2f80ddd9 src:manual/62-proj-keruvannya.md:117 klas:F -->
### T-62-039 · proza · рядок 117

**Книга каже, дослівно:**

> Це саме той випадок, коли «датчик іноді спрацьовує сам» — не датчик, а відсутній резистор.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-040 sha:98707e37 src:manual/62-proj-keruvannya.md:123 klas:F -->
### T-62-040 · proza · рядок 123

**Книга каже, дослівно:**

> Логіка керування будується як явний автомат, а не набором прапорців.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-041 sha:b8cd9901 src:manual/62-proj-keruvannya.md:123 klas:F -->
### T-62-041 · proza · рядок 123

**Книга каже, дослівно:**

> Стан завжди один, переходи явні, і кожен переход логується.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-042 sha:05334bcf src:manual/62-proj-keruvannya.md:126 klas:A -->
### T-62-042 · kod · рядок 126

**Книга каже, дослівно:**

> ```c
> typedef enum {
>     STAN_STOP,          // зупинено, чекає команди
>     STAN_ROBOTA,        // насос працює
>     STAN_AVARIYA,       // помилка, потрібне ручне скидання
>     STAN_BLOKUVANNYA,   // пауза після роботи
> } stan_t;
> 
> static stan_t stan = STAN_STOP;
> static int64_t stan_vid;
> 
> static void perejty(stan_t novyy, const char *prychyna) {
>     if (novyy == stan) return;
>     ESP_LOGI(TAG, "%s -> %s: %s", nazva(stan), nazva(novyy), prychyna);
>     stan = novyy;
>     stan_vid = esp_timer_get_time();
>     nasos_keruvaty(novyy == STAN_ROBOTA);
>     onovyty_indykaciyu();
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

<!-- fc id:T-62-043 sha:fb4554b3 src:manual/62-proj-keruvannya.md:139 klas:F -->
### T-62-043 · kod-ryadok · рядок 139

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "%s -> %s: %s", nazva(stan), nazva(novyy), prychyna);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-044 sha:ea4d167e src:manual/62-proj-keruvannya.md:142 klas:F -->
### T-62-044 · kod-ryadok · рядок 142

**Книга каже, дослівно:**

> nasos_keruvaty(novyy == STAN_ROBOTA);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-045 sha:e5aaf78d src:manual/62-proj-keruvannya.md:143 klas:F -->
### T-62-045 · kod-ryadok · рядок 143

**Книга каже, дослівно:**

> onovyty_indykaciyu();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-046 sha:1157a791 src:manual/62-proj-keruvannya.md:147 klas:F -->
### T-62-046 · proza · рядок 147

**Книга каже, дослівно:**

> Логувати перехід із **причиною** — те, що робить лог придатним для розбору через місяць (розділ 25).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-047 sha:4e69dd78 src:manual/62-proj-keruvannya.md:152 klas:A -->
### T-62-047 · kod · рядок 152

**Книга каже, дослівно:**

> ```c
> #define MAX_ROBOTY_S     600      // 10 хвилин безперервно
> #define PAUZA_PISLYA_S   300      // 5 хвилин відпочинку
> #define ZV_YAZOK_TAIMAUT 120      // втрата зв'язку
> 
> static void task_keruvannya(void *arg) {
>     esp_task_wdt_add(NULL);
>     while (1) {
>         esp_task_wdt_reset();
>         int64_t u_stani = (esp_timer_get_time() - stan_vid) / 1000000;
> 
>         // 1. Аварійна кнопка — найвищий пріоритет
>         if (!gpio_get_level(PIN_STOP))
>             perejty(STAN_AVARIYA, "натиснуто СТОП");
> 
>         // 2. Сухий хід: працюємо, а рівня немає
>         if (stan == STAN_ROBOTA && !riven_ye() && u_stani > 10)
>             perejty(STAN_AVARIYA, "сухий хід: немає рівня");
> 
>         // 3. Ліміт часу безперервної роботи
>         if (stan == STAN_ROBOTA && u_stani > MAX_ROBOTY_S)
>             perejty(STAN_BLOKUVANNYA, "перевищено ліміт часу");
> 
>         // 4. Кінець паузи
>         if (stan == STAN_BLOKUVANNYA && u_stani > PAUZA_PISLYA_S)
>             perejty(STAN_STOP, "пауза завершена");
> 
>         vTaskDelay(pdMS_TO_TICKS(100));
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

<!-- fc id:T-62-048 sha:49e09508 src:manual/62-proj-keruvannya.md:153 klas:F -->
### T-62-048 · kod-ryadok · рядок 153

**Книга каже, дослівно:**

> #define MAX_ROBOTY_S     600      // 10 хвилин безперервно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-049 sha:f5124e8d src:manual/62-proj-keruvannya.md:154 klas:F -->
### T-62-049 · kod-ryadok · рядок 154

**Книга каже, дослівно:**

> #define PAUZA_PISLYA_S   300      // 5 хвилин відпочинку

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-050 sha:76745c58 src:manual/62-proj-keruvannya.md:155 klas:F -->
### T-62-050 · kod-ryadok · рядок 155

**Книга каже, дослівно:**

> #define ZV_YAZOK_TAIMAUT 120      // втрата зв'язку

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-051 sha:3041709b src:manual/62-proj-keruvannya.md:158 klas:A -->
### T-62-051 · kod-ryadok · рядок 158

**Книга каже, дослівно:**

> esp_task_wdt_add(NULL);

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

<!-- fc id:T-62-052 sha:61e9dfbd src:manual/62-proj-keruvannya.md:160 klas:A -->
### T-62-052 · kod-ryadok · рядок 160

**Книга каже, дослівно:**

> esp_task_wdt_reset();

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

<!-- fc id:T-62-053 sha:cf06630c src:manual/62-proj-keruvannya.md:164 klas:F -->
### T-62-053 · kod-ryadok · рядок 164

**Книга каже, дослівно:**

> if (!gpio_get_level(PIN_STOP))

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-054 sha:7ed04c13 src:manual/62-proj-keruvannya.md:165 klas:F -->
### T-62-054 · kod-ryadok · рядок 165

**Книга каже, дослівно:**

> perejty(STAN_AVARIYA, "натиснуто СТОП");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-055 sha:cc6ada9c src:manual/62-proj-keruvannya.md:168 klas:F -->
### T-62-055 · kod-ryadok · рядок 168

**Книга каже, дослівно:**

> if (stan == STAN_ROBOTA && !riven_ye() && u_stani > 10)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-056 sha:900722d7 src:manual/62-proj-keruvannya.md:169 klas:F -->
### T-62-056 · kod-ryadok · рядок 169

**Книга каже, дослівно:**

> perejty(STAN_AVARIYA, "сухий хід: немає рівня");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-057 sha:e49bc4d8 src:manual/62-proj-keruvannya.md:172 klas:F -->
### T-62-057 · kod-ryadok · рядок 172

**Книга каже, дослівно:**

> if (stan == STAN_ROBOTA && u_stani > MAX_ROBOTY_S)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-058 sha:3f4ad16a src:manual/62-proj-keruvannya.md:173 klas:F -->
### T-62-058 · kod-ryadok · рядок 173

**Книга каже, дослівно:**

> perejty(STAN_BLOKUVANNYA, "перевищено ліміт часу");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-059 sha:00253454 src:manual/62-proj-keruvannya.md:176 klas:F -->
### T-62-059 · kod-ryadok · рядок 176

**Книга каже, дослівно:**

> if (stan == STAN_BLOKUVANNYA && u_stani > PAUZA_PISLYA_S)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-060 sha:c7e221ff src:manual/62-proj-keruvannya.md:177 klas:F -->
### T-62-060 · kod-ryadok · рядок 177

**Книга каже, дослівно:**

> perejty(STAN_STOP, "пауза завершена");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-061 sha:20132484 src:manual/62-proj-keruvannya.md:179 klas:A -->
### T-62-061 · kod-ryadok · рядок 179

**Книга каже, дослівно:**

> vTaskDelay(pdMS_TO_TICKS(100));

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

<!-- fc id:T-62-062 sha:d42fe36f src:manual/62-proj-keruvannya.md:185 klas:F -->
### T-62-062 · proza · рядок 185

**Книга каже, дослівно:**

> **Ліміт часу безперервної роботи — найважливіший захист у проєкті.**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-063 sha:fc0a2e44 src:manual/62-proj-keruvannya.md:187 klas:F -->
### T-62-063 · proza · рядок 187

**Книга каже, дослівно:**

> Він рятує від усього, чого ви не передбачили: залиплого реле, збрехлого датчика, помилки в логіці, забутої ручної команди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-064 sha:648dae42 src:manual/62-proj-keruvannya.md:187 klas:F -->
### T-62-064 · proza · рядок 187

**Книга каже, дослівно:**

> Насос, що працює десять хвилин замість двох, — незручність; насос, що працює добу, — аварія.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-065 sha:e3a133ac src:manual/62-proj-keruvannya.md:192 klas:F -->
### T-62-065 · proza · рядок 192

**Книга каже, дослівно:**

> Ліміт ставиться завжди, навіть коли «за логікою такого не буває».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-066 sha:9a8b2e5c src:manual/62-proj-keruvannya.md:192 klas:F -->
### T-62-066 · proza · рядок 192

**Книга каже, дослівно:**

> Саме те, чого не буває за логікою, і трапляється.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-067 sha:bd516205 src:manual/62-proj-keruvannya.md:197 klas:F -->
### T-62-067 · proza · рядок 197

**Книга каже, дослівно:**

> **Стан `AVARIYA` не скидається сам.** Вихід із нього — лише ручне втручання: кнопка або команда з мережі, і бажано після того, як людина подивилася, що сталося.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-068 sha:da6f29d5 src:manual/62-proj-keruvannya.md:201 klas:F -->
### T-62-068 · proza · рядок 201

**Книга каже, дослівно:**

> Автоматичне скидання аварії перетворює захист на затримку: пристрій циклічно вмикає насос, ловить сухий хід, чекає, вмикає знову.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-069 sha:9c0f3e88 src:manual/62-proj-keruvannya.md:208 klas:F -->
### T-62-069 · proza · рядок 208

**Книга каже, дослівно:**

> **Втрата зв'язку не змінює стан механізму — це проєктне рішення, і воно має бути свідомим.**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-070 sha:d024ec6b src:manual/62-proj-keruvannya.md:211 klas:F -->
### T-62-070 · proza · рядок 211

**Книга каже, дослівно:**

> Два можливі варіанти, і обирати треба за наслідками:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-071 sha:7da2f6b3 src:manual/62-proj-keruvannya.md:213 klas:F -->
### T-62-071 · proza · рядок 213

**Книга каже, дослівно:**

> **Продовжити за локальною логікою.** Правильно для насоса, що працює за розкладом і датчиком: мережа потрібна для нагляду, а не для роботи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-072 sha:fcef41df src:manual/62-proj-keruvannya.md:216 klas:F -->
### T-62-072 · proza · рядок 216

**Книга каже, дослівно:**

> **Зупинитися.** Правильно для механізму, яким керує лише оператор: без зв'язку немає нагляду, тому рух припиняється.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-073 sha:6a40ae41 src:manual/62-proj-keruvannya.md:219 klas:F -->
### T-62-073 · proza · рядок 219

**Книга каже, дослівно:**

> Найгірший варіант — **не думати про це**: тоді поведінка визначається випадковим місцем у коді, де мережевий виклик заблокувався або `ESP_ERROR_CHECK` викликав перезавантаження (розділ 32).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-074 sha:978546bd src:manual/62-proj-keruvannya.md:224 klas:F -->
### T-62-074 · proza · рядок 224

**Книга каже, дослівно:**

> У цьому проєкті обрано перший варіант, і він записується в паспорт (розділ 56).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-075 sha:f2860393 src:manual/62-proj-keruvannya.md:229 klas:A -->
### T-62-075 · kod · рядок 229

**Книга каже, дослівно:**

> ```c
> static esp_err_t cmd_handler(httpd_req_t *req) {
>     char buf[64];
>     int n = httpd_req_recv(req, buf, sizeof(buf) - 1);
>     if (n <= 0) return ESP_FAIL;
>     buf[n] = 0;
> 
>     if (strcmp(buf, "pusk") == 0) {
>         if (stan == STAN_AVARIYA)
>             httpd_resp_sendstr(req, "avariya: potriben skydannya");
>         else if (!riven_ye())
>             httpd_resp_sendstr(req, "nemaye rivnya");
>         else {
>             perejty(STAN_ROBOTA, "команда з мережі");
>             httpd_resp_sendstr(req, "ok");
>         }
>     } else if (strcmp(buf, "stop") == 0) {
>         perejty(STAN_STOP, "команда з мережі");
>         httpd_resp_sendstr(req, "ok");
>     } else if (strcmp(buf, "skydannya") == 0) {
>         if (stan == STAN_AVARIYA) perejty(STAN_STOP, "ручне скидання");
>         httpd_resp_sendstr(req, "ok");
>     }
>     return ESP_OK;
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

<!-- fc id:T-62-076 sha:bff39e0f src:manual/62-proj-keruvannya.md:237 klas:F -->
### T-62-076 · kod-ryadok · рядок 237

**Книга каже, дослівно:**

> if (stan == STAN_AVARIYA)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-077 sha:a3f2a35d src:manual/62-proj-keruvannya.md:238 klas:A -->
### T-62-077 · kod-ryadok · рядок 238

**Книга каже, дослівно:**

> httpd_resp_sendstr(req, "avariya: potriben skydannya");

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

<!-- fc id:T-62-078 sha:83924cce src:manual/62-proj-keruvannya.md:240 klas:A -->
### T-62-078 · kod-ryadok · рядок 240

**Книга каже, дослівно:**

> httpd_resp_sendstr(req, "nemaye rivnya");

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

<!-- fc id:T-62-079 sha:779ecc0f src:manual/62-proj-keruvannya.md:242 klas:F -->
### T-62-079 · kod-ryadok · рядок 242

**Книга каже, дослівно:**

> perejty(STAN_ROBOTA, "команда з мережі");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-080 sha:a3150d68 src:manual/62-proj-keruvannya.md:243 klas:A -->
### T-62-080 · kod-ryadok · рядок 243

**Книга каже, дослівно:**

> httpd_resp_sendstr(req, "ok");

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

<!-- fc id:T-62-081 sha:a7ed0c57 src:manual/62-proj-keruvannya.md:246 klas:F -->
### T-62-081 · kod-ryadok · рядок 246

**Книга каже, дослівно:**

> perejty(STAN_STOP, "команда з мережі");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-082 sha:a3150d68 src:manual/62-proj-keruvannya.md:247 klas:A -->
### T-62-082 · kod-ryadok · рядок 247

**Книга каже, дослівно:**

> httpd_resp_sendstr(req, "ok");

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

<!-- fc id:T-62-083 sha:f0c3511e src:manual/62-proj-keruvannya.md:249 klas:F -->
### T-62-083 · kod-ryadok · рядок 249

**Книга каже, дослівно:**

> if (stan == STAN_AVARIYA) perejty(STAN_STOP, "ручне скидання");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-084 sha:a3150d68 src:manual/62-proj-keruvannya.md:250 klas:A -->
### T-62-084 · kod-ryadok · рядок 250

**Книга каже, дослівно:**

> httpd_resp_sendstr(req, "ok");

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

<!-- fc id:T-62-085 sha:19f6806c src:manual/62-proj-keruvannya.md:257 klas:F -->
### T-62-085 · proza · рядок 257

**Книга каже, дослівно:**

> Команда **`stop` виконується завжди й без умов**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-086 sha:9bb680b6 src:manual/62-proj-keruvannya.md:257 klas:F -->
### T-62-086 · proza · рядок 257

**Книга каже, дослівно:**

> Це правило для будь-якого керування: зупинка не має перевірок, не має підтверджень і не залежить від поточного стану.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-087 sha:c0cb37d6 src:manual/62-proj-keruvannya.md:261 klas:F -->
### T-62-087 · proza · рядок 261

**Книга каже, дослівно:**

> Усе інше може бути відхилене; зупинка — ніколи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-088 sha:3fa12ad8 src:manual/62-proj-keruvannya.md:264 klas:F -->
### T-62-088 · proza · рядок 264

**Книга каже, дослівно:**

> Обробник ідемпотентний: «стоп» двічі означає те саме, що один раз (розділ 40).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-089 sha:92e5f6bc src:manual/62-proj-keruvannya.md:269 klas:F -->
### T-62-089 · proza · рядок 269

**Книга каже, дослівно:**

> Стан має бути видимим на місці, без мережі:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-090 sha:4a8e99b7 src:manual/62-proj-keruvannya.md:271 klas:F -->
### T-62-090 · tablycya · рядок 271

**Книга каже, дослівно:**

> | Світлодіод | Стан |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-091 sha:51c885d4 src:manual/62-proj-keruvannya.md:273 klas:F -->
### T-62-091 · tablycya · рядок 273

**Книга каже, дослівно:**

> | не горить | STOP |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-092 sha:fdf62190 src:manual/62-proj-keruvannya.md:274 klas:F -->
### T-62-092 · tablycya · рядок 274

**Книга каже, дослівно:**

> | горить рівно | РОБОТА |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-093 sha:825f7619 src:manual/62-proj-keruvannya.md:275 klas:F -->
### T-62-093 · tablycya · рядок 275

**Книга каже, дослівно:**

> | блимає повільно | БЛОКУВАННЯ (пауза) |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-094 sha:06e8e104 src:manual/62-proj-keruvannya.md:276 klas:F -->
### T-62-094 · tablycya · рядок 276

**Книга каже, дослівно:**

> | блимає швидко | **АВАРІЯ** |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-095 sha:3182a8e9 src:manual/62-proj-keruvannya.md:278 klas:F -->
### T-62-095 · proza · рядок 278

**Книга каже, дослівно:**

> Людина біля пристрою мусить розуміти, що відбувається, не відкриваючи браузер (розділ 56).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-096 sha:1f49899c src:manual/62-proj-keruvannya.md:283 klas:F -->
### T-62-096 · proza · рядок 283

**Книга каже, дослівно:**

> Порядок обов'язковий, і перші три пункти — до підключення насоса:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-097 sha:2bba4dc1 src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-097 · proza · рядок 285

**Книга каже, дослівно:**

> **Реле при завантаженні.** Подати живлення десять разів, спостерігати за реле.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-098 sha:dc644d42 src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-098 · proza · рядок 285

**Книга каже, дослівно:**

> Жодного клацання під час старту. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-099 sha:eef3109d src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-099 · proza · рядок 285

**Книга каже, дослівно:**

> **Зникнення живлення.** Висмикнути живлення при ввімкненому реле — реле має відпустити. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-100 sha:681a455a src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-100 · proza · рядок 285

**Книга каже, дослівно:**

> **Аварійний вимикач.** Розриває коло насоса незалежно від стану чипа. 4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-101 sha:8e5546e2 src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-101 · proza · рядок 285

**Книга каже, дослівно:**

> Ліміт часу: запустити, дочекатися десяти хвилин — має перейти в блокування. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-102 sha:3ef4ae03 src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-102 · proza · рядок 285

**Книга каже, дослівно:**

> Сухий хід: запустити й від'єднати датчик рівня — аварія за десять секунд. 6.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-103 sha:9f0d9ebc src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-103 · proza · рядок 285

**Книга каже, дослівно:**

> Аварія не скидається сама: почекати п'ять хвилин, стан лишається. 7.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-104 sha:3ad292e9 src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-104 · proza · рядок 285

**Книга каже, дослівно:**

> Втрата зв'язку: вимкнути роутер під час роботи — поведінка відповідає записаній у паспорті. 8.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-105 sha:55565e34 src:manual/62-proj-keruvannya.md:285 klas:F -->
### T-62-105 · proza · рядок 285

**Книга каже, дослівно:**

> Зависання: викликати штучне зависання задачі — watchdog має перезавантажити чип, реле — відпустити.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-106 sha:92534189 src:manual/62-proj-keruvannya.md:301 klas:F -->
### T-62-106 · proza · рядок 301

**Книга каже, дослівно:**

> Пункти 1–3 виконуються **з від'єднаним насосом**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-107 sha:e6af39f2 src:manual/62-proj-keruvannya.md:301 klas:F -->
### T-62-107 · proza · рядок 301

**Книга каже, дослівно:**

> Перевіряти захисти на працюючому механізмі — це перевіряти їх наслідками.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-62-108 sha:7a37c9e6 src:manual/62-proj-keruvannya.md:307 klas:F -->
### T-62-108 · proza · рядок 307

**Книга каже, дослівно:**

> - **Кілька механізмів** із взаємними блокуваннями; - **Логування подій** у NVS: історія пусків і аварій переживає перезавантаження (розділ 18); - **Companion-схема** (розділ 57): критичну логіку — на окремий контролер, ESP32 лишити зв'язок; - **Датчик струму** (розділ 45) для контролю, що насос справді крутиться, а не просто отримав живлення.

**Доказ**

- **Клас:** F — не звірено

---
