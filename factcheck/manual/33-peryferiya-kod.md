# Фактчекінг: `manual/33-peryferiya-kod.md`

Одиниць твердження: **121**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-33-001 sha:6801c405 src:manual/33-peryferiya-kod.md:3 klas:F -->
### T-33-001 · proza · рядок 3

**Книга каже, дослівно:**

> Практична робота з блоками, описаними оглядово в розділі 04.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-002 sha:47541b2b src:manual/33-peryferiya-kod.md:3 klas:F -->
### T-33-002 · proza · рядок 3

**Книга каже, дослівно:**

> Головна ідея розділу: **більшість того, що виглядає як задача для коду, робиться апаратно** — і саме тому працює надійно незалежно від завантаження системи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-003 sha:6723d0bf src:manual/33-peryferiya-kod.md:10 klas:F -->
### T-33-003 · kod · рядок 10

**Книга каже, дослівно:**

> ```c
> gpio_config_t cfg = {
>     .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
>     .mode = GPIO_MODE_OUTPUT,
>     .pull_up_en = GPIO_PULLUP_DISABLE,
>     .pull_down_en = GPIO_PULLDOWN_DISABLE,
>     .intr_type = GPIO_INTR_DISABLE,
> };
> gpio_config(&cfg);
> gpio_set_level(GPIO_NUM_2, 1);
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-004 sha:3fad3578 src:manual/33-peryferiya-kod.md:12 klas:F -->
### T-33-004 · kod-ryadok · рядок 12

**Книга каже, дослівно:**

> .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-005 sha:4ea85d9b src:manual/33-peryferiya-kod.md:13 klas:F -->
### T-33-005 · kod-ryadok · рядок 13

**Книга каже, дослівно:**

> .mode = GPIO_MODE_OUTPUT,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-006 sha:6bd988a2 src:manual/33-peryferiya-kod.md:14 klas:F -->
### T-33-006 · kod-ryadok · рядок 14

**Книга каже, дослівно:**

> .pull_up_en = GPIO_PULLUP_DISABLE,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-007 sha:8c43cf59 src:manual/33-peryferiya-kod.md:15 klas:F -->
### T-33-007 · kod-ryadok · рядок 15

**Книга каже, дослівно:**

> .pull_down_en = GPIO_PULLDOWN_DISABLE,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-008 sha:c0246957 src:manual/33-peryferiya-kod.md:16 klas:F -->
### T-33-008 · kod-ryadok · рядок 16

**Книга каже, дослівно:**

> .intr_type = GPIO_INTR_DISABLE,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-009 sha:514324cb src:manual/33-peryferiya-kod.md:18 klas:F -->
### T-33-009 · kod-ryadok · рядок 18

**Книга каже, дослівно:**

> gpio_config(&cfg);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-010 sha:6602551b src:manual/33-peryferiya-kod.md:19 klas:F -->
### T-33-010 · kod-ryadok · рядок 19

**Книга каже, дослівно:**

> gpio_set_level(GPIO_NUM_2, 1);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-011 sha:bedbcc3c src:manual/33-peryferiya-kod.md:22 klas:F -->
### T-33-011 · proza · рядок 22

**Книга каже, дослівно:**

> `pin_bit_mask` — бітова маска, тому кілька пінів налаштовуються однією дією.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-012 sha:0cfd0d0f src:manual/33-peryferiya-kod.md:22 klas:F -->
### T-33-012 · proza · рядок 22

**Книга каже, дослівно:**

> `1ULL` обов'язково: на пінах вище 31 звичайний `1` переповниться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-013 sha:fbcbf58d src:manual/33-peryferiya-kod.md:27 klas:F -->
### T-33-013 · kod · рядок 27

**Книга каже, дослівно:**

> ```c
> gpio_config_t in = {
>     .pin_bit_mask = (1ULL << GPIO_NUM_5),
>     .mode = GPIO_MODE_INPUT,
>     .pull_up_en = GPIO_PULLUP_ENABLE,
>     .intr_type = GPIO_INTR_NEGEDGE,
> };
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-014 sha:f96f77cb src:manual/33-peryferiya-kod.md:29 klas:F -->
### T-33-014 · kod-ryadok · рядок 29

**Книга каже, дослівно:**

> .pin_bit_mask = (1ULL << GPIO_NUM_5),

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-015 sha:99e0f537 src:manual/33-peryferiya-kod.md:30 klas:F -->
### T-33-015 · kod-ryadok · рядок 30

**Книга каже, дослівно:**

> .mode = GPIO_MODE_INPUT,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-016 sha:5502b7f2 src:manual/33-peryferiya-kod.md:31 klas:F -->
### T-33-016 · kod-ryadok · рядок 31

**Книга каже, дослівно:**

> .pull_up_en = GPIO_PULLUP_ENABLE,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-017 sha:aa23725a src:manual/33-peryferiya-kod.md:32 klas:F -->
### T-33-017 · kod-ryadok · рядок 32

**Книга каже, дослівно:**

> .intr_type = GPIO_INTR_NEGEDGE,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-018 sha:be4ac34e src:manual/33-peryferiya-kod.md:36 klas:F -->
### T-33-018 · proza · рядок 36

**Книга каже, дослівно:**

> Перед вибором піна — картка [К9](#k-pinouty): strapping, тільки-вхідні, зайняті флешем (розділ 07).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-019 sha:e26a0015 src:manual/33-peryferiya-kod.md:41 klas:F -->
### T-33-019 · proza · рядок 41

**Книга каже, дослівно:**

> Обробник має бути коротким: покласти в чергу й вийти (розділ 31).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-020 sha:e35f117f src:manual/33-peryferiya-kod.md:43 klas:F -->
### T-33-020 · kod · рядок 43

**Книга каже, дослівно:**

> ```c
> static void IRAM_ATTR isr(void *arg) {
>     uint32_t pin = (uint32_t)arg;
>     xQueueSendFromISR(cherga, &pin, NULL);
> }
> 
> gpio_install_isr_service(0);
> gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5);
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-021 sha:f9e24be5 src:manual/33-peryferiya-kod.md:46 klas:F -->
### T-33-021 · kod-ryadok · рядок 46

**Книга каже, дослівно:**

> xQueueSendFromISR(cherga, &pin, NULL);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-022 sha:90827293 src:manual/33-peryferiya-kod.md:49 klas:F -->
### T-33-022 · kod-ryadok · рядок 49

**Книга каже, дослівно:**

> gpio_install_isr_service(0);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-023 sha:77ee66f9 src:manual/33-peryferiya-kod.md:50 klas:F -->
### T-33-023 · kod-ryadok · рядок 50

**Книга каже, дослівно:**

> gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-024 sha:154027ff src:manual/33-peryferiya-kod.md:53 klas:F -->
### T-33-024 · proza · рядок 53

**Книга каже, дослівно:**

> Механічна кнопка дає десятки перемикань за мілісекунди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-025 sha:c3f1cea7 src:manual/33-peryferiya-kod.md:53 klas:F -->
### T-33-025 · proza · рядок 53

**Книга каже, дослівно:**

> Антидребезг робиться **не затримкою в ISR** (це прямий шлях до `Interrupt wdt timeout`), а порівнянням часу:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-026 sha:7196915f src:manual/33-peryferiya-kod.md:57 klas:F -->
### T-33-026 · kod · рядок 57

**Книга каже, дослівно:**

> ```c
> static int64_t ostannya;
> 
> static void IRAM_ATTR isr(void *arg) {
>     int64_t teper = esp_timer_get_time();      // мікросекунди
>     if (teper - ostannya < 50000) return;      // 50 мс — ігнорувати
>     ostannya = teper;
>     xQueueSendFromISR(cherga, &teper, NULL);
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-027 sha:2bfd44f4 src:manual/33-peryferiya-kod.md:64 klas:F -->
### T-33-027 · kod-ryadok · рядок 64

**Книга каже, дослівно:**

> xQueueSendFromISR(cherga, &teper, NULL);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-028 sha:ad224fe1 src:manual/33-peryferiya-kod.md:70 klas:F -->
### T-33-028 · proza · рядок 70

**Книга каже, дослівно:**

> **`esp_timer`** — програмні таймери з мікросекундною роздільною здатністю.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-029 sha:61f1d984 src:manual/33-peryferiya-kod.md:70 klas:F -->
### T-33-029 · proza · рядок 70

**Книга каже, дослівно:**

> Для більшості періодичних задач цього досить:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-030 sha:3915b0a4 src:manual/33-peryferiya-kod.md:73 klas:F -->
### T-33-030 · kod · рядок 73

**Книга каже, дослівно:**

> ```c
> static void callback(void *arg) { /* коротко */ }
> 
> esp_timer_create_args_t args = { .callback = callback, .name = "opyt" };
> esp_timer_handle_t t;
> esp_timer_create(&args, &t);
> esp_timer_start_periodic(t, 1000000);   // раз на секунду
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-031 sha:8319cb06 src:manual/33-peryferiya-kod.md:78 klas:F -->
### T-33-031 · kod-ryadok · рядок 78

**Книга каже, дослівно:**

> esp_timer_create(&args, &t);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-032 sha:92cb7370 src:manual/33-peryferiya-kod.md:82 klas:F -->
### T-33-032 · proza · рядок 82

**Книга каже, дослівно:**

> Обробники всіх `esp_timer` виконуються в одній задачі — довгий обробник затримує решту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-033 sha:eb045fe4 src:manual/33-peryferiya-kod.md:85 klas:F -->
### T-33-033 · proza · рядок 85

**Книга каже, дослівно:**

> **`esp_timer_get_time()`** повертає мікросекунди від старту у 64-бітному числі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-034 sha:360af588 src:manual/33-peryferiya-kod.md:85 klas:F -->
### T-33-034 · proza · рядок 85

**Книга каже, дослівно:**

> Це основний спосіб міряти час: переповнення не станеться за час життя пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-035 sha:1525c224 src:manual/33-peryferiya-kod.md:89 klas:F -->
### T-33-035 · proza · рядок 89

**Книга каже, дослівно:**

> **Апаратні таймери** потрібні там, де важлива точність незалежно від завантаження системи, — переривання формується апаратно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-036 sha:abc3c580 src:manual/33-peryferiya-kod.md:94 klas:F -->
### T-33-036 · kod · рядок 94

**Книга каже, дослівно:**

> ```c
> ledc_timer_config_t tcfg = {
>     .speed_mode = LEDC_LOW_SPEED_MODE,
>     .duty_resolution = LEDC_TIMER_13_BIT,
>     .timer_num = LEDC_TIMER_0,
>     .freq_hz = 5000,
> };
> ledc_timer_config(&tcfg);
> 
> ledc_channel_config_t ccfg = {
>     .gpio_num = GPIO_NUM_2,
>     .speed_mode = LEDC_LOW_SPEED_MODE,
>     .channel = LEDC_CHANNEL_0,
>     .timer_sel = LEDC_TIMER_0,
>     .duty = 4096,
> };
> ledc_channel_config(&ccfg);
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-037 sha:105bb277 src:manual/33-peryferiya-kod.md:96 klas:F -->
### T-33-037 · kod-ryadok · рядок 96

**Книга каже, дослівно:**

> .speed_mode = LEDC_LOW_SPEED_MODE,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-038 sha:f0c21116 src:manual/33-peryferiya-kod.md:97 klas:F -->
### T-33-038 · kod-ryadok · рядок 97

**Книга каже, дослівно:**

> .duty_resolution = LEDC_TIMER_13_BIT,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-039 sha:44a45b93 src:manual/33-peryferiya-kod.md:98 klas:F -->
### T-33-039 · kod-ryadok · рядок 98

**Книга каже, дослівно:**

> .timer_num = LEDC_TIMER_0,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-040 sha:99171f13 src:manual/33-peryferiya-kod.md:99 klas:F -->
### T-33-040 · kod-ryadok · рядок 99

**Книга каже, дослівно:**

> .freq_hz = 5000,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-041 sha:d8b6e80c src:manual/33-peryferiya-kod.md:101 klas:F -->
### T-33-041 · kod-ryadok · рядок 101

**Книга каже, дослівно:**

> ledc_timer_config(&tcfg);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-042 sha:80dd0543 src:manual/33-peryferiya-kod.md:104 klas:F -->
### T-33-042 · kod-ryadok · рядок 104

**Книга каже, дослівно:**

> .gpio_num = GPIO_NUM_2,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-043 sha:105bb277 src:manual/33-peryferiya-kod.md:105 klas:F -->
### T-33-043 · kod-ryadok · рядок 105

**Книга каже, дослівно:**

> .speed_mode = LEDC_LOW_SPEED_MODE,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-044 sha:e4df9707 src:manual/33-peryferiya-kod.md:106 klas:F -->
### T-33-044 · kod-ryadok · рядок 106

**Книга каже, дослівно:**

> .channel = LEDC_CHANNEL_0,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-045 sha:b9fc8ae0 src:manual/33-peryferiya-kod.md:107 klas:F -->
### T-33-045 · kod-ryadok · рядок 107

**Книга каже, дослівно:**

> .timer_sel = LEDC_TIMER_0,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-046 sha:d3cd0e78 src:manual/33-peryferiya-kod.md:108 klas:F -->
### T-33-046 · kod-ryadok · рядок 108

**Книга каже, дослівно:**

> .duty = 4096,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-047 sha:6dde17f4 src:manual/33-peryferiya-kod.md:110 klas:F -->
### T-33-047 · kod-ryadok · рядок 110

**Книга каже, дослівно:**

> ledc_channel_config(&ccfg);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-048 sha:6a437dd9 src:manual/33-peryferiya-kod.md:113 klas:A -->
### T-33-048 · proza · рядок 113

**Книга каже, дослівно:**

> Частота і розрядність пов'язані: що вища частота, то менше розрядів доступно. 5 кГц із 13 розрядами — робоче поєднання для світлодіодів.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/ledc.rst
- **Дослівно з джерела:**
  > The frequency and the duty resolution are interdependent. The higher the PWM frequency,
  > the lower the duty resolution which is available, and vice versa.
  > …
  > The LEDC driver offers a helper function :cpp:func:`ledc_find_suitable_duty_resolution`
  > to find the maximum possible resolution for the timer, given the source clock frequency
  > and the desired PWM signal frequency.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Дослівно підтверджує формулювання розділу 33. Друге речення — кандидат на доповнення в наступному проході: у драйвері є готова функція, яка рахує максимальну роздільність, і книга про неї мовчить.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-33-049 sha:1c6e3022 src:manual/33-peryferiya-kod.md:117 klas:F -->
### T-33-049 · proza · рядок 117

**Книга каже, дослівно:**

> Яскравість світлодіода **не лінійна** щодо коефіцієнта заповнення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-050 sha:462e36b5 src:manual/33-peryferiya-kod.md:117 klas:F -->
### T-33-050 · proza · рядок 117

**Книга каже, дослівно:**

> Око сприймає яскравість логарифмічно: перехід від 10 % до 20 % видно, від 80 % до 90 % — майже ні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-051 sha:e20d58db src:manual/33-peryferiya-kod.md:121 klas:F -->
### T-33-051 · proza · рядок 121

**Книга каже, дослівно:**

> Плавне згасання, зроблене лінійно, виглядає як різкий стрибок наприкінці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-052 sha:e3516a73 src:manual/33-peryferiya-kod.md:121 klas:F -->
### T-33-052 · proza · рядок 121

**Книга каже, дослівно:**

> Лікується таблицею або квадратичною залежністю.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-053 sha:bdfa3b50 src:manual/33-peryferiya-kod.md:125 klas:F -->
### T-33-053 · proza · рядок 125

**Книга каже, дослівно:**

> **Серво** керується імпульсами 50 Гц: приблизно 1 мс — один край, 2 мс — інший, 1.5 мс — середина.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-054 sha:1a68cfd1 src:manual/33-peryferiya-kod.md:125 klas:F -->
### T-33-054 · proza · рядок 125

**Книга каже, дослівно:**

> Період при 50 Гц — 20 мс, тому значення `duty` рахується як `2^розрядність × тривалість / 20 мс`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-055 sha:9b0e16fa src:manual/33-peryferiya-kod.md:125 klas:F -->
### T-33-055 · proza · рядок 125

**Книга каже, дослівно:**

> Для 16-розрядної роздільності це приблизно 3277 (1 мс), 4915 (1.5 мс) і 6554 (2 мс).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-056 sha:3aa25745 src:manual/33-peryferiya-kod.md:132 klas:F -->
### T-33-056 · proza · рядок 132

**Книга каже, дослівно:**

> Серво живиться **окремо**, не від піна 3V3 плати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-057 sha:2d20f028 src:manual/33-peryferiya-kod.md:132 klas:F -->
### T-33-057 · proza · рядок 132

**Книга каже, дослівно:**

> Навіть невелике серво в момент рушання бере сотні міліампер, і бортовий стабілізатор цього не витримує: пристрій перезавантажується по brownout саме тоді, коли механізм починає рух (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-058 sha:b1601e7b src:manual/33-peryferiya-kod.md:137 klas:F -->
### T-33-058 · proza · рядок 137

**Книга каже, дослівно:**

> Спільна земля обов'язкова (розділ 48).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-059 sha:681bc71a src:manual/33-peryferiya-kod.md:142 klas:F -->
### T-33-059 · proza · рядок 142

**Книга каже, дослівно:**

> [[classic]] [[S3]] MCPWM зроблений для силової електроніки й уміє те, чого LEDC не вміє:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-060 sha:4b935177 src:manual/33-peryferiya-kod.md:145 klas:F -->
### T-33-060 · proza · рядок 145

**Книга каже, дослівно:**

> - **мертвий час** між верхнім і нижнім плечем моста — без нього обидва ключі на мить відкриті одночасно, і це наскрізний струм; - **апаратне аварійне вимкнення** за зовнішнім сигналом — швидше за будь-яку реакцію коду; - **синхронізація каналів**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-061 sha:db2ade05 src:manual/33-peryferiya-kod.md:151 klas:F -->
### T-33-061 · proza · рядок 151

**Книга каже, дослівно:**

> Для керування двигуном через мостовий драйвер це не зручність, а захист силового каскаду (розділ 48).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-062 sha:9bc36e29 src:manual/33-peryferiya-kod.md:156 klas:F -->
### T-33-062 · proza · рядок 156

**Книга каже, дослівно:**

> RMT задумувався для інфрачервоних пультів, а виявився універсальним формувачем імпульсних послідовностей із наносекундною точністю.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-063 sha:2cf260ec src:manual/33-peryferiya-kod.md:159 klas:F -->
### T-33-063 · proza · рядок 159

**Книга каже, дослівно:**

> Головне застосування — **адресні світлодіоди WS2812**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-064 sha:f25f29ea src:manual/33-peryferiya-kod.md:159 klas:F -->
### T-33-064 · proza · рядок 159

**Книга каже, дослівно:**

> Їхній протокол кодує біти тривалістю імпульсів у сотні наносекунд.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-065 sha:1f2196d8 src:manual/33-peryferiya-kod.md:159 klas:F -->
### T-33-065 · proza · рядок 159

**Книга каже, дослівно:**

> Робити це в коді означає заборонити переривання на весь час передачі — і все одно отримати збої, коли втрутиться радіо.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-066 sha:3f89b4eb src:manual/33-peryferiya-kod.md:164 klas:F -->
### T-33-066 · proza · рядок 164

**Книга каже, дослівно:**

> RMT формує послідовність апаратно: процесор віддає дані й вільний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-067 sha:aeef17bd src:manual/33-peryferiya-kod.md:166 klas:F -->
### T-33-067 · kod · рядок 166

**Книга каже, дослівно:**

> ```c
> led_strip_handle_t strip;
> led_strip_config_t scfg = { .strip_gpio_num = 18, .max_leds = 30 };
> led_strip_rmt_config_t rcfg = { .resolution_hz = 10 * 1000 * 1000 };
> led_strip_new_rmt_device(&scfg, &rcfg, &strip);
> 
> led_strip_set_pixel(strip, 0, 255, 0, 0);
> led_strip_refresh(strip);
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-068 sha:0aeeb7f3 src:manual/33-peryferiya-kod.md:170 klas:F -->
### T-33-068 · kod-ryadok · рядок 170

**Книга каже, дослівно:**

> led_strip_new_rmt_device(&scfg, &rcfg, &strip);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-069 sha:3ceebab0 src:manual/33-peryferiya-kod.md:172 klas:F -->
### T-33-069 · kod-ryadok · рядок 172

**Книга каже, дослівно:**

> led_strip_set_pixel(strip, 0, 255, 0, 0);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-070 sha:b2a1e46a src:manual/33-peryferiya-kod.md:173 klas:F -->
### T-33-070 · kod-ryadok · рядок 173

**Книга каже, дослівно:**

> led_strip_refresh(strip);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-071 sha:0a072e63 src:manual/33-peryferiya-kod.md:176 klas:F -->
### T-33-071 · proza · рядок 176

**Книга каже, дослівно:**

> Номер піна в прикладі довільний — беріть свій за карткою [К9](#k-pinouty).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-072 sha:3eebc84f src:manual/33-peryferiya-kod.md:176 klas:A -->
### T-33-072 · proza · рядок 176

**Книга каже, дослівно:**

> На платах розробки з бортовим адресним світлодіодом він у кожної свій: [[C3]] на C3-DevKitM це `GPIO8`, [[S3]] на S3-DevKitC — `GPIO48`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/arduino-esp32/master/variants/{esp32,esp32s3,esp32c3}/pins_arduino.h
- **Дослівно з джерела:**
  > variants/esp32/pins_arduino.h     static const uint8_t SDA = 21;  static const uint8_t SCL = 22;
  > variants/esp32s3/pins_arduino.h   static const uint8_t SDA = 8;   static const uint8_t SCL = 9;   #define PIN_RGB_LED 48
  > variants/esp32c3/pins_arduino.h   static const uint8_t SDA = 8;   static const uint8_t SCL = 9;   #define PIN_RGB_LED 8
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Джерело правки додатка A в сесії рецензування 06: для C3 стояло 5/6, таких значень немає в жодному варіанті. Те саме джерело підтверджує номери бортових світлодіодів, ужиті в розділі 33.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-33-073 sha:c630370e src:manual/33-peryferiya-kod.md:176 klas:F -->
### T-33-073 · proza · рядок 176

**Книга каже, дослівно:**

> [[classic]] На classic `GPIO8` брати не можна взагалі: там флеш (розділ 07).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-074 sha:be56e056 src:manual/33-peryferiya-kod.md:182 klas:F -->
### T-33-074 · proza · рядок 182

**Книга каже, дослівно:**

> RMT уміє й приймати — вимірювати тривалість вхідних імпульсів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-075 sha:ee324ede src:manual/33-peryferiya-kod.md:182 klas:F -->
### T-33-075 · proza · рядок 182

**Книга каже, дослівно:**

> Це правильний спосіб читати ІЧ-пульти й датчики з імпульсним виходом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-076 sha:48ff1940 src:manual/33-peryferiya-kod.md:187 klas:F -->
### T-33-076 · proza · рядок 187

**Книга каже, дослівно:**

> Апаратний лічильник імпульсів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-077 sha:cb13812b src:manual/33-peryferiya-kod.md:187 klas:F -->
### T-33-077 · proza · рядок 187

**Книга каже, дослівно:**

> Енкодер, витратомір, лічильник обертів — усе це не потребує переривання на кожен імпульс: процесор читає накопичене, коли йому зручно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-078 sha:089f6d9c src:manual/33-peryferiya-kod.md:191 klas:F -->
### T-33-078 · proza · рядок 191

**Книга каже, дослівно:**

> Перевага критична на високих частотах: десять тисяч імпульсів на секунду через переривання з'їдять помітну частину ядра; PCNT не з'їсть нічого.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-079 sha:a75f68d2 src:manual/33-peryferiya-kod.md:194 klas:F -->
### T-33-079 · proza · рядок 194

**Книга каже, дослівно:**

> PCNT уміє й апаратний фільтр коротких сплесків — антидребезг без коду.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-080 sha:81a8f41e src:manual/33-peryferiya-kod.md:198 klas:F -->
### T-33-080 · kod · рядок 198

**Книга каже, дослівно:**

> ```c
> adc_oneshot_unit_handle_t adc;
> adc_oneshot_unit_init_cfg_t ucfg = { .unit_id = ADC_UNIT_1 };
> adc_oneshot_new_unit(&ucfg, &adc);
> 
> adc_oneshot_chan_cfg_t ccfg = {
>     .bitwidth = ADC_BITWIDTH_DEFAULT,
>     .atten = ADC_ATTEN_DB_12,
> };
> adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);
> 
> int raw;
> adc_oneshot_read(adc, ADC_CHANNEL_6, &raw);
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-081 sha:9778c836 src:manual/33-peryferiya-kod.md:201 klas:F -->
### T-33-081 · kod-ryadok · рядок 201

**Книга каже, дослівно:**

> adc_oneshot_new_unit(&ucfg, &adc);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-082 sha:1c285707 src:manual/33-peryferiya-kod.md:204 klas:F -->
### T-33-082 · kod-ryadok · рядок 204

**Книга каже, дослівно:**

> .bitwidth = ADC_BITWIDTH_DEFAULT,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-083 sha:f277858a src:manual/33-peryferiya-kod.md:205 klas:F -->
### T-33-083 · kod-ryadok · рядок 205

**Книга каже, дослівно:**

> .atten = ADC_ATTEN_DB_12,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-084 sha:ba3dde5d src:manual/33-peryferiya-kod.md:207 klas:F -->
### T-33-084 · kod-ryadok · рядок 207

**Книга каже, дослівно:**

> adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-085 sha:eb26138c src:manual/33-peryferiya-kod.md:210 klas:F -->
### T-33-085 · kod-ryadok · рядок 210

**Книга каже, дослівно:**

> adc_oneshot_read(adc, ADC_CHANNEL_6, &raw);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-086 sha:6dd00f50 src:manual/33-peryferiya-kod.md:214 klas:A -->
### T-33-086 · proza · рядок 214

**Книга каже, дослівно:**

> [[classic]] [[S2]] [[S3]] **ADC2 не працює при увімкненому Wi-Fi** (розділ 07).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- **Дослівно з джерела:**
  > :esp32 or esp32s2 or esp32s3: - ADC2 is also used by Wi-Fi. :cpp:func:`adc_oneshot_read` has
  > provided protection between the Wi-Fi driver and ADC oneshot mode driver.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга перелічувала classic і S2 (подекуди лише classic), тоді як документація прямо називає три цілі, включно з S3. Для S3 це важить окремо: його рекомендують як вибір за замовчуванням для нового проєкту, тобто найімовірніше саме на ньому читач і розводитиме плату. Позначку [[S3]] додано у восьми місцях: розділи 04, 07 (двічі), 29, 33 (двічі), 45 і картка К8.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-33-087 sha:f41a8143 src:manual/33-peryferiya-kod.md:214 klas:F -->
### T-33-087 · proza · рядок 214

**Книга каже, дослівно:**

> Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-088 sha:20d78c08 src:manual/33-peryferiya-kod.md:214 klas:F -->
### T-33-088 · proza · рядок 214

**Книга каже, дослівно:**

> Вимірювання переносяться на ADC1.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-089 sha:c19c555e src:manual/33-peryferiya-kod.md:219 klas:F -->
### T-33-089 · proza · рядок 219

**Книга каже, дослівно:**

> **Затухання (attenuation)** задає діапазон вхідної напруги.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-090 sha:b512ca80 src:manual/33-peryferiya-kod.md:219 klas:F -->
### T-33-090 · proza · рядок 219

**Книга каже, дослівно:**

> Без нього ADC міряє лише невелику частину діапазону; з максимальним затуханням доступний майже весь до 3.3 В.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-091 sha:34c873e7 src:manual/33-peryferiya-kod.md:219 klas:F -->
### T-33-091 · proza · рядок 219

**Книга каже, дослівно:**

> Пам'ятайте: вхід не толерантний до перевищення — понад живлення подавати не можна.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-092 sha:79580945 src:manual/33-peryferiya-kod.md:224 klas:F -->
### T-33-092 · proza · рядок 224

**Книга каже, дослівно:**

> **Точність.** ADC ESP32 нелінійний, і сирі відліки не переводяться в вольти простим множенням.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-093 sha:faa9bead src:manual/33-peryferiya-kod.md:224 klas:F -->
### T-33-093 · proza · рядок 224

**Книга каже, дослівно:**

> Штатний шлях — калібрування:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-094 sha:0bfeb273 src:manual/33-peryferiya-kod.md:227 klas:F -->
### T-33-094 · kod · рядок 227

**Книга каже, дослівно:**

> ```c
> adc_cali_handle_t cali;
> adc_cali_curve_fitting_config_t cfg = {
>     .unit_id = ADC_UNIT_1,
>     .atten = ADC_ATTEN_DB_12,
>     .bitwidth = ADC_BITWIDTH_DEFAULT,
> };
> adc_cali_create_scheme_curve_fitting(&cfg, &cali);
> 
> int mv;
> adc_cali_raw_to_voltage(cali, raw, &mv);
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-095 sha:24960961 src:manual/33-peryferiya-kod.md:230 klas:F -->
### T-33-095 · kod-ryadok · рядок 230

**Книга каже, дослівно:**

> .unit_id = ADC_UNIT_1,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-096 sha:f277858a src:manual/33-peryferiya-kod.md:231 klas:F -->
### T-33-096 · kod-ryadok · рядок 231

**Книга каже, дослівно:**

> .atten = ADC_ATTEN_DB_12,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-097 sha:1c285707 src:manual/33-peryferiya-kod.md:232 klas:F -->
### T-33-097 · kod-ryadok · рядок 232

**Книга каже, дослівно:**

> .bitwidth = ADC_BITWIDTH_DEFAULT,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-098 sha:8f9ffc26 src:manual/33-peryferiya-kod.md:234 klas:F -->
### T-33-098 · kod-ryadok · рядок 234

**Книга каже, дослівно:**

> adc_cali_create_scheme_curve_fitting(&cfg, &cali);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-099 sha:2a32eb67 src:manual/33-peryferiya-kod.md:237 klas:F -->
### T-33-099 · kod-ryadok · рядок 237

**Книга каже, дослівно:**

> adc_cali_raw_to_voltage(cali, raw, &mv);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-100 sha:b338b2c7 src:manual/33-peryferiya-kod.md:240 klas:F -->
### T-33-100 · proza · рядок 240

**Книга каже, дослівно:**

> Калібрувальні коефіцієнти зашиті в eFuse кожного чипа на заводі — ця функція їх використовує.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-101 sha:94e81fbb src:manual/33-peryferiya-kod.md:243 klas:F -->
### T-33-101 · proza · рядок 243

**Книга каже, дослівно:**

> **Боротьба з шумом**, у порядку дієвості:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-102 sha:d9cb78d8 src:manual/33-peryferiya-kod.md:245 klas:F -->
### T-33-102 · proza · рядок 245

**Книга каже, дослівно:**

> **Усереднення** 16–64 відліків.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-103 sha:836b0a38 src:manual/33-peryferiya-kod.md:245 klas:F -->
### T-33-103 · proza · рядок 245

**Книга каже, дослівно:**

> Найдешевше і найдієвіше. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-104 sha:7d1e31c2 src:manual/33-peryferiya-kod.md:245 klas:F -->
### T-33-104 · proza · рядок 245

**Книга каже, дослівно:**

> **Конденсатор** 100 нФ від входу до землі. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-105 sha:f3f157b6 src:manual/33-peryferiya-kod.md:245 klas:F -->
### T-33-105 · proza · рядок 245

**Книга каже, дослівно:**

> **Тихе живлення** аналогової частини (розділ 53). 4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-106 sha:0ad8b2a1 src:manual/33-peryferiya-kod.md:245 klas:F -->
### T-33-106 · proza · рядок 245

**Книга каже, дослівно:**

> **Коротші проводи** до джерела сигналу. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-107 sha:7f1a82b2 src:manual/33-peryferiya-kod.md:245 klas:F -->
### T-33-107 · proza · рядок 245

**Книга каже, дослівно:**

> **Зовнішній ADC** по SPI — коли потрібна справжня точність.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-108 sha:fa721a1e src:manual/33-peryferiya-kod.md:252 klas:F -->
### T-33-108 · proza · рядок 252

**Книга каже, дослівно:**

> Вимірювання напруги акумулятора через дільник — класична задача, у якій дільник **сам розряджає акумулятор**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-109 sha:a29a68e8 src:manual/33-peryferiya-kod.md:252 klas:C -->
### T-33-109 · proza · рядок 252

**Книга каже, дослівно:**

> Два резистори по 100 кОм — це 200 кОм між плюсом і землею: при 3.7 В вони постійно беруть 18 мкА.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-33-110 sha:d584a342 src:manual/33-peryferiya-kod.md:252 klas:F -->
### T-33-110 · proza · рядок 252

**Книга каже, дослівно:**

> Для пристрою, що споживає уві сні одиниці мікроампер, дільник стає головним джерелом розряду — більшим за сам чип.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-111 sha:227a685f src:manual/33-peryferiya-kod.md:258 klas:F -->
### T-33-111 · proza · рядок 258

**Книга каже, дослівно:**

> Лікується вмиканням дільника транзистором лише на час вимірювання (розділ 53).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-112 sha:a7c26dcb src:manual/33-peryferiya-kod.md:264 klas:F -->
### T-33-112 · proza · рядок 264

**Книга каже, дослівно:**

> [[classic]] [[S2]] Справжній аналоговий вихід, 8 розрядів, на `GPIO25` і `GPIO26`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-113 sha:a73f83e1 src:manual/33-peryferiya-kod.md:264 klas:F -->
### T-33-113 · proza · рядок 264

**Книга каже, дослівно:**

> Більше ніде в лінійці його немає (розділ 04).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-114 sha:c7206801 src:manual/33-peryferiya-kod.md:264 klas:F -->
### T-33-114 · proza · рядок 264

**Книга каже, дослівно:**

> Де потрібен на інших чипах — зовнішній ЦАП по I²C або згладжений PWM.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-115 sha:89f289a2 src:manual/33-peryferiya-kod.md:270 klas:F -->
### T-33-115 · proza · рядок 270

**Книга каже, дослівно:**

> Антидребезг — порівнянням часу, ніколи не затримкою в ISR.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-116 sha:3b0d82f6 src:manual/33-peryferiya-kod.md:272 klas:F -->
### T-33-116 · proza · рядок 272

**Книга каже, дослівно:**

> Яскравість світлодіода нелінійна щодо коефіцієнта заповнення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-117 sha:d229616c src:manual/33-peryferiya-kod.md:274 klas:F -->
### T-33-117 · proza · рядок 274

**Книга каже, дослівно:**

> Серво живиться окремо; спільна земля обов'язкова.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-118 sha:c9c22960 src:manual/33-peryferiya-kod.md:276 klas:F -->
### T-33-118 · proza · рядок 276

**Книга каже, дослівно:**

> WS2812 керуються через RMT апаратно — у коді це робити не варто.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-119 sha:93141a0c src:manual/33-peryferiya-kod.md:278 klas:F -->
### T-33-119 · proza · рядок 278

**Книга каже, дослівно:**

> PCNT рахує імпульси без переривань і має апаратний антидребезг.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-120 sha:171ad095 src:manual/33-peryferiya-kod.md:280 klas:A -->
### T-33-120 · proza · рядок 280

**Книга каже, дослівно:**

> [[classic]] [[S2]] [[S3]] ADC2 не працює при Wi-Fi; ADC потребує калібрування й усереднення.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- **Дослівно з джерела:**
  > :esp32 or esp32s2 or esp32s3: - ADC2 is also used by Wi-Fi. :cpp:func:`adc_oneshot_read` has
  > provided protection between the Wi-Fi driver and ADC oneshot mode driver.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга перелічувала classic і S2 (подекуди лише classic), тоді як документація прямо називає три цілі, включно з S3. Для S3 це важить окремо: його рекомендують як вибір за замовчуванням для нового проєкту, тобто найімовірніше саме на ньому читач і розводитиме плату. Позначку [[S3]] додано у восьми місцях: розділи 04, 07 (двічі), 29, 33 (двічі), 45 і картка К8.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-33-121 sha:679df6b2 src:manual/33-peryferiya-kod.md:283 klas:F -->
### T-33-121 · proza · рядок 283

**Книга каже, дослівно:**

> Дільник для вимірювання акумулятора розряджає акумулятор.

**Доказ**

- **Клас:** F — не звірено

---
