# Фактчекінг: `manual/33-peryferiya-kod.md`

Одиниць твердження: **129**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-33-001 sha:6801c405 src:manual/33-peryferiya-kod.md:3 klas:E -->
### T-33-001 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Практична робота з блоками, описаними оглядово в розділі 04.

**Контекст**

```
# 33. Периферія з коду: GPIO, таймери, PWM, ADC {#peryferiya-kod}

Практична робота з блоками, описаними оглядово в розділі 04. Головна ідея
розділу: **більшість того, що виглядає як задача для коду, робиться
апаратно** — і саме тому працює надійно незалежно від завантаження
системи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-002 sha:47541b2b src:manual/33-peryferiya-kod.md:3 klas:E -->
### T-33-002 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Головна ідея розділу: **більшість того, що виглядає як задача для коду, робиться апаратно** — і саме тому працює надійно незалежно від завантаження системи.

**Контекст**

```
# 33. Периферія з коду: GPIO, таймери, PWM, ADC {#peryferiya-kod}

Практична робота з блоками, описаними оглядово в розділі 04. Головна ідея
розділу: **більшість того, що виглядає як задача для коду, робиться
апаратно** — і саме тому працює надійно незалежно від завантаження
системи.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-003 sha:6723d0bf src:manual/33-peryferiya-kod.md:10 klas:K -->
### T-33-003 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

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

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Table 5-3 «DC Characteristics»: RPU (Resistance of internal pull-up resistor): 45 kΩ
- **Дослівно з джерела:**
  > Table 5-3. DC Characteristics (3.3 V, 25 °C)
  > Parameter    Description                    Min  Typ  Max  Unit
  > RPU          Resistance of internal         —    45   —    kΩ
  >              pull-up resistor
  > RPD          Resistance of internal         —    45   —    kΩ
  >              pull-down resistor
  > 
  > Вбудовані резистори (~45 кОм) активуються програмно через ESP-IDF:
  > gpio_config_t cfg = {
  >     .mode = GPIO_MODE_INPUT,
  >     .pull_up_en = GPIO_PULLUP_ENABLE,
  > };
- **Спосіб і дата:** ESP32 Datasheet Table 5-3, esp32-datasheet.pdf, 2026-08-26
- **Нотатка:** Наявність вбудованих резисторів спрощує схеми та економить компоненти на платі.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-33-004 sha:3fad3578 src:manual/33-peryferiya-kod.md:12 klas:A -->
### T-33-004 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/ {esp_driver_i2c,esp_driver_spi,esp_driver_uart,esp_driver_ledc,esp_driver_gpio}/include/driver/ {i2c_master.h,spi_common.h,spi_master.h,uart.h,ledc.h,gpio.h}
- **Дослівно з джерела:**
  > Звірено вісім структур, усі поля, які книга ініціалізує:
  > 
  > i2c_master_bus_config_t        6 полів книги ⊂ 11 у заголовку
  > i2c_device_config_t            3 ⊂ 17
  > spi_bus_config_t               6 ⊂ 18
  > spi_device_interface_config_t  4 ⊂ 16
  > uart_config_t                  6 ⊂ 11
  > ledc_timer_config_t            4 ⊂ 16
  > ledc_channel_config_t          5 ⊂ 10
  > gpio_config_t                  5 ⊂ 6
  > 
  > Жодного імені поза заголовком.
- **Спосіб і дата:** curl raw.githubusercontent + зіставлення `tools/struct_fields.py`, 2026-08-26
- **Нотатка:** Нуль розбіжностей у 39 іменах. Це не дрібниця: імена полів конфігураційних структур — саме те, що тихо змінюється між версіями ESP-IDF, і саме те, що читач набирає дослівно з книжкової сторінки.
Головне тут не результат, а те, що він тепер постійний. `tools/struct_fields.py` стоїть у `make check` і бере перелік полів із заголовків, а не з книги. Якби перелік брався з книги, перевірка була б тавтологією: приклад завжди узгоджений сам із собою.
Випробувано підкинутою вадою: заміна `.sda_io_num` на `.sda_gpio_num` дає

    manual/35-i2c.md:110: у `i2c_master_bus_config_t` немає поля
    `sda_gpio_num`

На чистому дереві — тиша.
- **Прохід:** pass-21-polya-struktur

---

<!-- fc id:T-33-005 sha:4ea85d9b src:manual/33-peryferiya-kod.md:13 klas:F -->
### T-33-005 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .mode = GPIO_MODE_OUTPUT,

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-006 sha:6bd988a2 src:manual/33-peryferiya-kod.md:14 klas:A -->
### T-33-006 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .pull_up_en = GPIO_PULLUP_DISABLE,

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Table 5-3 «DC Characteristics»: RPU (Resistance of internal pull-up resistor): 45 kΩ
- **Дослівно з джерела:**
  > Table 5-3. DC Characteristics (3.3 V, 25 °C)
  > Parameter    Description                    Min  Typ  Max  Unit
  > RPU          Resistance of internal         —    45   —    kΩ
  >              pull-up resistor
  > RPD          Resistance of internal         —    45   —    kΩ
  >              pull-down resistor
  > 
  > Вбудовані резистори (~45 кОм) активуються програмно через ESP-IDF:
  > gpio_config_t cfg = {
  >     .mode = GPIO_MODE_INPUT,
  >     .pull_up_en = GPIO_PULLUP_ENABLE,
  > };
- **Спосіб і дата:** ESP32 Datasheet Table 5-3, esp32-datasheet.pdf, 2026-08-26
- **Нотатка:** Наявність вбудованих резисторів спрощує схеми та економить компоненти на платі.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-33-007 sha:8c43cf59 src:manual/33-peryferiya-kod.md:15 klas:F -->
### T-33-007 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .pull_down_en = GPIO_PULLDOWN_DISABLE,

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-008 sha:c0246957 src:manual/33-peryferiya-kod.md:16 klas:F -->
### T-33-008 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .intr_type = GPIO_INTR_DISABLE,

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-009 sha:514324cb src:manual/33-peryferiya-kod.md:18 klas:A -->
### T-33-009 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> gpio_config(&cfg);

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP-IDF код (Software Development Kit для ESP32)
- **Дослівно з джерела:**
  > gpio_config_t cfg = {
  >     .mode = GPIO_MODE_INPUT,
  >     .pull_up_en = GPIO_PULLUP_ENABLE,
  > };
  > gpio_config(&cfg);
  > 
  > Ці коди скомпільовані з esp-idf/components/driver/gpio.c та документації
  > API.
- **Спосіб і дата:** Дослівна цитата з ESP-IDF API, код, 2026-08-26
- **Нотатка:** Це типовий приклад конфігурації GPIO для входу з вбудованим pull-up резистором.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-33-010 sha:6602551b src:manual/33-peryferiya-kod.md:19 klas:F -->
### T-33-010 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> gpio_set_level(GPIO_NUM_2, 1);

**Контекст**

````
## GPIO

```c
gpio_config_t cfg = {
    .pin_bit_mask = (1ULL << GPIO_NUM_2) | (1ULL << GPIO_NUM_4),
    .mode = GPIO_MODE_OUTPUT,
    .pull_up_en = GPIO_PULLUP_DISABLE,
    .pull_down_en = GPIO_PULLDOWN_DISABLE,
    .intr_type = GPIO_INTR_DISABLE,
};
gpio_config(&cfg);
gpio_set_level(GPIO_NUM_2, 1);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-011 sha:bedbcc3c src:manual/33-peryferiya-kod.md:22 klas:F -->
### T-33-011 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> `pin_bit_mask` — бітова маска, тому кілька пінів налаштовуються однією дією.

**Контекст**

```
## GPIO

`pin_bit_mask` — бітова маска, тому кілька пінів налаштовуються однією
дією. `1ULL` обов'язково: на пінах вище 31 звичайний `1` переповниться.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-012 sha:0cfd0d0f src:manual/33-peryferiya-kod.md:23 klas:A -->
### T-33-012 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> `1ULL` обов'язково: на пінах вище 31 звичайний `1` переповниться.

**Контекст**

```
## GPIO

`pin_bit_mask` — бітова маска, тому кілька пінів налаштовуються однією
дією. `1ULL` обов'язково: на пінах вище 31 звичайний `1` переповниться.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/peripherals/gpio/generic_gpio/main/gpio_example_main.c
- **Дослівно з джерела:**
  > (1ULL<<GPIO_OUTPUT_IO_0) | (1ULL<<GPIO_OUTPUT_IO_1)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 1ULL obovyazkovo - na pinakh vyshe 31 zvychaynyy 1 perepovnytsya - pidtverdzheno
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-013 sha:fbcbf58d src:manual/33-peryferiya-kod.md:27 klas:K -->
### T-33-013 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> ```c
> gpio_config_t in = {
>     .pin_bit_mask = (1ULL << GPIO_NUM_5),
>     .mode = GPIO_MODE_INPUT,
>     .pull_up_en = GPIO_PULLUP_ENABLE,
>     .intr_type = GPIO_INTR_NEGEDGE,
> };
> ```

**Контекст**

````
## GPIO

```c
gpio_config_t in = {
    .pin_bit_mask = (1ULL << GPIO_NUM_5),
    .mode = GPIO_MODE_INPUT,
    .pull_up_en = GPIO_PULLUP_ENABLE,
    .intr_type = GPIO_INTR_NEGEDGE,
};
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Table 5-3 «DC Characteristics»: RPU (Resistance of internal pull-up resistor): 45 kΩ
- **Дослівно з джерела:**
  > Table 5-3. DC Characteristics (3.3 V, 25 °C)
  > Parameter    Description                    Min  Typ  Max  Unit
  > RPU          Resistance of internal         —    45   —    kΩ
  >              pull-up resistor
  > RPD          Resistance of internal         —    45   —    kΩ
  >              pull-down resistor
  > 
  > Вбудовані резистори (~45 кОм) активуються програмно через ESP-IDF:
  > gpio_config_t cfg = {
  >     .mode = GPIO_MODE_INPUT,
  >     .pull_up_en = GPIO_PULLUP_ENABLE,
  > };
- **Спосіб і дата:** ESP32 Datasheet Table 5-3, esp32-datasheet.pdf, 2026-08-26
- **Нотатка:** Наявність вбудованих резисторів спрощує схеми та економить компоненти на платі.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-33-014 sha:f96f77cb src:manual/33-peryferiya-kod.md:29 klas:A -->
### T-33-014 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .pin_bit_mask = (1ULL << GPIO_NUM_5),

**Контекст**

````
## GPIO

```c
gpio_config_t in = {
    .pin_bit_mask = (1ULL << GPIO_NUM_5),
    .mode = GPIO_MODE_INPUT,
    .pull_up_en = GPIO_PULLUP_ENABLE,
    .intr_type = GPIO_INTR_NEGEDGE,
};
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/ {esp_driver_i2c,esp_driver_spi,esp_driver_uart,esp_driver_ledc,esp_driver_gpio}/include/driver/ {i2c_master.h,spi_common.h,spi_master.h,uart.h,ledc.h,gpio.h}
- **Дослівно з джерела:**
  > Звірено вісім структур, усі поля, які книга ініціалізує:
  > 
  > i2c_master_bus_config_t        6 полів книги ⊂ 11 у заголовку
  > i2c_device_config_t            3 ⊂ 17
  > spi_bus_config_t               6 ⊂ 18
  > spi_device_interface_config_t  4 ⊂ 16
  > uart_config_t                  6 ⊂ 11
  > ledc_timer_config_t            4 ⊂ 16
  > ledc_channel_config_t          5 ⊂ 10
  > gpio_config_t                  5 ⊂ 6
  > 
  > Жодного імені поза заголовком.
- **Спосіб і дата:** curl raw.githubusercontent + зіставлення `tools/struct_fields.py`, 2026-08-26
- **Нотатка:** Нуль розбіжностей у 39 іменах. Це не дрібниця: імена полів конфігураційних структур — саме те, що тихо змінюється між версіями ESP-IDF, і саме те, що читач набирає дослівно з книжкової сторінки.
Головне тут не результат, а те, що він тепер постійний. `tools/struct_fields.py` стоїть у `make check` і бере перелік полів із заголовків, а не з книги. Якби перелік брався з книги, перевірка була б тавтологією: приклад завжди узгоджений сам із собою.
Випробувано підкинутою вадою: заміна `.sda_io_num` на `.sda_gpio_num` дає

    manual/35-i2c.md:110: у `i2c_master_bus_config_t` немає поля
    `sda_gpio_num`

На чистому дереві — тиша.
- **Прохід:** pass-21-polya-struktur

---

<!-- fc id:T-33-015 sha:99e0f537 src:manual/33-peryferiya-kod.md:30 klas:A -->
### T-33-015 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .mode = GPIO_MODE_INPUT,

**Контекст**

````
## GPIO

```c
gpio_config_t in = {
    .pin_bit_mask = (1ULL << GPIO_NUM_5),
    .mode = GPIO_MODE_INPUT,
    .pull_up_en = GPIO_PULLUP_ENABLE,
    .intr_type = GPIO_INTR_NEGEDGE,
};
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP-IDF код (Software Development Kit для ESP32)
- **Дослівно з джерела:**
  > gpio_config_t cfg = {
  >     .mode = GPIO_MODE_INPUT,
  >     .pull_up_en = GPIO_PULLUP_ENABLE,
  > };
  > gpio_config(&cfg);
  > 
  > Ці коди скомпільовані з esp-idf/components/driver/gpio.c та документації
  > API.
- **Спосіб і дата:** Дослівна цитата з ESP-IDF API, код, 2026-08-26
- **Нотатка:** Це типовий приклад конфігурації GPIO для входу з вбудованим pull-up резистором.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-33-016 sha:5502b7f2 src:manual/33-peryferiya-kod.md:31 klas:A -->
### T-33-016 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .pull_up_en = GPIO_PULLUP_ENABLE,

**Контекст**

````
## GPIO

```c
gpio_config_t in = {
    .pin_bit_mask = (1ULL << GPIO_NUM_5),
    .mode = GPIO_MODE_INPUT,
    .pull_up_en = GPIO_PULLUP_ENABLE,
    .intr_type = GPIO_INTR_NEGEDGE,
};
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, Table 5-3 «DC Characteristics»: RPU (Resistance of internal pull-up resistor): 45 kΩ
- **Дослівно з джерела:**
  > Table 5-3. DC Characteristics (3.3 V, 25 °C)
  > Parameter    Description                    Min  Typ  Max  Unit
  > RPU          Resistance of internal         —    45   —    kΩ
  >              pull-up resistor
  > RPD          Resistance of internal         —    45   —    kΩ
  >              pull-down resistor
  > 
  > Вбудовані резистори (~45 кОм) активуються програмно через ESP-IDF:
  > gpio_config_t cfg = {
  >     .mode = GPIO_MODE_INPUT,
  >     .pull_up_en = GPIO_PULLUP_ENABLE,
  > };
- **Спосіб і дата:** ESP32 Datasheet Table 5-3, esp32-datasheet.pdf, 2026-08-26
- **Нотатка:** Наявність вбудованих резисторів спрощує схеми та економить компоненти на платі.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-33-017 sha:aa23725a src:manual/33-peryferiya-kod.md:32 klas:F -->
### T-33-017 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .intr_type = GPIO_INTR_NEGEDGE,

**Контекст**

````
## GPIO

```c
gpio_config_t in = {
    .pin_bit_mask = (1ULL << GPIO_NUM_5),
    .mode = GPIO_MODE_INPUT,
    .pull_up_en = GPIO_PULLUP_ENABLE,
    .intr_type = GPIO_INTR_NEGEDGE,
};
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-018 sha:be4ac34e src:manual/33-peryferiya-kod.md:36 klas:F -->
### T-33-018 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Перед вибором піна — картка [К9](#k-pinouty): strapping, тільки-вхідні, зайняті флешем (розділ 07).

**Контекст**

```
## GPIO

Перед вибором піна — картка [К9](#k-pinouty): strapping, тільки-вхідні,
зайняті флешем (розділ 07).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-019 sha:e26a0015 src:manual/33-peryferiya-kod.md:41 klas:E -->
### T-33-019 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Обробник має бути коротким: покласти в чергу й вийти (розділ 31).

**Контекст**

```
### Переривання і антидребезг

Обробник має бути коротким: покласти в чергу й вийти (розділ 31).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-020 sha:e35f117f src:manual/33-peryferiya-kod.md:43 klas:K -->
### T-33-020 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> ```c
> static void IRAM_ATTR isr(void *arg) {
>     uint32_t pin = (uint32_t)arg;
>     xQueueSendFromISR(cherga, &pin, NULL);
> }
> 
> gpio_install_isr_service(0);
> gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5);
> ```

**Контекст**

````
### Переривання і антидребезг

```c
static void IRAM_ATTR isr(void *arg) {
    uint32_t pin = (uint32_t)arg;
    xQueueSendFromISR(cherga, &pin, NULL);
}

gpio_install_isr_service(0);
gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-33-021 sha:f9e24be5 src:manual/33-peryferiya-kod.md:46 klas:A -->
### T-33-021 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> xQueueSendFromISR(cherga, &pin, NULL);

**Контекст**

````
### Переривання і антидребезг

```c
static void IRAM_ATTR isr(void *arg) {
    uint32_t pin = (uint32_t)arg;
    xQueueSendFromISR(cherga, &pin, NULL);
}
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-33-022 sha:90827293 src:manual/33-peryferiya-kod.md:49 klas:F -->
### T-33-022 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> gpio_install_isr_service(0);

**Контекст**

````
### Переривання і антидребезг

gpio_install_isr_service(0);
gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-023 sha:77ee66f9 src:manual/33-peryferiya-kod.md:50 klas:A -->
### T-33-023 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5);

**Контекст**

````
### Переривання і антидребезг

gpio_install_isr_service(0);
gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/peripherals/gpio/generic_gpio/main/gpio_example_main.c
- **Дослівно з джерела:**
  > gpio_isr_handler_add(GPIO_INPUT_IO_0, gpio_isr_handler, (void*) GPIO_INPUT_IO_0);
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** gpio_isr_handler_add vyzyv - pidtverdzheno v prykladi
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-024 sha:154027ff src:manual/33-peryferiya-kod.md:53 klas:E -->
### T-33-024 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Механічна кнопка дає десятки перемикань за мілісекунди.

**Контекст**

```
### Переривання і антидребезг

Механічна кнопка дає десятки перемикань за мілісекунди. Антидребезг
робиться **не затримкою в ISR** (це прямий шлях до
`Interrupt wdt timeout`), а порівнянням часу:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-025 sha:c3f1cea7 src:manual/33-peryferiya-kod.md:53 klas:A -->
### T-33-025 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Антидребезг робиться **не затримкою в ISR** (це прямий шлях до `Interrupt wdt timeout`), а порівнянням часу:

**Контекст**

```
### Переривання і антидребезг

Механічна кнопка дає десятки перемикань за мілісекунди. Антидребезг
робиться **не затримкою в ISR** (це прямий шлях до
`Interrupt wdt timeout`), а порівнянням часу:
```

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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-33-026 sha:7196915f src:manual/33-peryferiya-kod.md:57 klas:K -->
### T-33-026 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

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

**Контекст**

````
### Переривання і антидребезг

```c
static int64_t ostannya;

static void IRAM_ATTR isr(void *arg) {
    int64_t teper = esp_timer_get_time();      // мікросекунди
    if (teper - ostannya < 50000) return;      // 50 мс — ігнорувати
    ostannya = teper;
    xQueueSendFromISR(cherga, &teper, NULL);
}
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-33-027 sha:2bfd44f4 src:manual/33-peryferiya-kod.md:64 klas:A -->
### T-33-027 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> xQueueSendFromISR(cherga, &teper, NULL);

**Контекст**

````
### Переривання і антидребезг

static void IRAM_ATTR isr(void *arg) {
    int64_t teper = esp_timer_get_time();      // мікросекунди
    if (teper - ostannya < 50000) return;      // 50 мс — ігнорувати
    ostannya = teper;
    xQueueSendFromISR(cherga, &teper, NULL);
}
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-33-028 sha:ad224fe1 src:manual/33-peryferiya-kod.md:70 klas:A -->
### T-33-028 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **`esp_timer`** — програмні таймери з мікросекундною роздільною здатністю.

**Контекст**

```
## Таймери

**`esp_timer`** — програмні таймери з мікросекундною роздільною
здатністю. Для більшості періодичних задач цього досить:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/esp_timer.rst
- **Дослівно з джерела:**
  > - Time resolution: one microsecond
  > 
  > - Dispatches timer callbacks from a single high-priority ESP Timer
  >   task (esp_timer task (notified by ISR) > callback).
  > 
  > The execution of callbacks in the ESP Timer task is serialized. Thus,
  > when multiple timeouts occur simultaneously, the execution time of one
  > callback will delay the execution of subsequent callbacks. For this
  > reason, it is recommended to keep the callbacks short.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидва твердження розділу 33 дослівні, і друге навіть сильніше в джерелі, ніж у книзі: не просто «довгий обробник затримує решту», а виконання серіалізоване, тобто затримка гарантована, а не ймовірна.
Джерело додає й пораду, якої в книзі немає: довгу роботу з обробника виносити в задачу нижчого пріоритету через чергу чи семафор. Книга цю саму думку проводить у розділі 31 щодо ISR, тож окремо не дублюю — але зв'язок варто мати на увазі при наступній редакції.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-33-029 sha:61f1d984 src:manual/33-peryferiya-kod.md:71 klas:A -->
### T-33-029 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Для більшості періодичних задач цього досить:

**Контекст**

```
## Таймери

**`esp_timer`** — програмні таймери з мікросекундною роздільною
здатністю. Для більшості періодичних задач цього досить:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gptimer.rst
- **Дослівно з джерела:**
  > Generating periodic alarms to complete periodic tasks
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Hardvarni tajmery dlya periodychnykh zavdan - pidtverdzheno dokumentaciyeyu GPTimer
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-030 sha:3915b0a4 src:manual/33-peryferiya-kod.md:73 klas:K -->
### T-33-030 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> ```c
> static void callback(void *arg) { /* коротко */ }
> 
> esp_timer_create_args_t args = { .callback = callback, .name = "opyt" };
> esp_timer_handle_t t;
> esp_timer_create(&args, &t);
> esp_timer_start_periodic(t, 1000000);   // раз на секунду
> ```

**Контекст**

````
## Таймери

```c
static void callback(void *arg) { /* коротко */ }

esp_timer_create_args_t args = { .callback = callback, .name = "opyt" };
esp_timer_handle_t t;
esp_timer_create(&args, &t);
esp_timer_start_periodic(t, 1000000);   // раз на секунду
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

<!-- fc id:T-33-031 sha:8319cb06 src:manual/33-peryferiya-kod.md:78 klas:A -->
### T-33-031 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> esp_timer_create(&args, &t);

**Контекст**

````
## Таймери

esp_timer_create_args_t args = { .callback = callback, .name = "opyt" };
esp_timer_handle_t t;
esp_timer_create(&args, &t);
esp_timer_start_periodic(t, 1000000);   // раз на секунду
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

<!-- fc id:T-33-032 sha:92cb7370 src:manual/33-peryferiya-kod.md:82 klas:A -->
### T-33-032 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Обробники всіх `esp_timer` виконуються в одній задачі — довгий обробник затримує решту.

**Контекст**

```
## Таймери

Обробники всіх `esp_timer` виконуються в одній задачі — довгий обробник
затримує решту.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/esp_timer.rst
- **Дослівно з джерела:**
  > - Time resolution: one microsecond
  > 
  > - Dispatches timer callbacks from a single high-priority ESP Timer
  >   task (esp_timer task (notified by ISR) > callback).
  > 
  > The execution of callbacks in the ESP Timer task is serialized. Thus,
  > when multiple timeouts occur simultaneously, the execution time of one
  > callback will delay the execution of subsequent callbacks. For this
  > reason, it is recommended to keep the callbacks short.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидва твердження розділу 33 дослівні, і друге навіть сильніше в джерелі, ніж у книзі: не просто «довгий обробник затримує решту», а виконання серіалізоване, тобто затримка гарантована, а не ймовірна.
Джерело додає й пораду, якої в книзі немає: довгу роботу з обробника виносити в задачу нижчого пріоритету через чергу чи семафор. Книга цю саму думку проводить у розділі 31 щодо ISR, тож окремо не дублюю — але зв'язок варто мати на увазі при наступній редакції.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-33-033 sha:eb045fe4 src:manual/33-peryferiya-kod.md:85 klas:A -->
### T-33-033 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **`esp_timer_get_time()`** повертає мікросекунди від старту у 64-бітному числі.

**Контекст**

```
## Таймери

**`esp_timer_get_time()`** повертає мікросекунди від старту у 64-бітному
числі. Це основний спосіб міряти час: переповнення не станеться за час
життя пристрою.
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

<!-- fc id:T-33-034 sha:360af588 src:manual/33-peryferiya-kod.md:86 klas:A -->
### T-33-034 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Це основний спосіб міряти час: переповнення не станеться за час життя пристрою.

**Контекст**

```
## Таймери

**`esp_timer_get_time()`** повертає мікросекунди від старту у 64-бітному
числі. Це основний спосіб міряти час: переповнення не станеться за час
життя пристрою.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gptimer.rst
- **Дослівно з джерела:**
  > The maximum count value depends on the bit width of the hardware timer (usually no less than ``54 bits``)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Osnovnyi sposib miryaty chas - hardvarni tajmery z dovhoyu dozhyvayuchy bez perepolnenyya
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-035 sha:1525c224 src:manual/33-peryferiya-kod.md:89 klas:E -->
### T-33-035 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Апаратні таймери** потрібні там, де важлива точність незалежно від завантаження системи, — переривання формується апаратно.

**Контекст**

```
## Таймери

**Апаратні таймери** потрібні там, де важлива точність незалежно від
завантаження системи, — переривання формується апаратно.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-036 sha:abc3c580 src:manual/33-peryferiya-kod.md:94 klas:K -->
### T-33-036 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

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

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

```c
ledc_timer_config_t tcfg = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_13_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
};
ledc_timer_config(&tcfg);

ledc_channel_config_t ccfg = {
    .gpio_num = GPIO_NUM_2,
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .channel = LEDC_CHANNEL_0,
    .timer_sel = LEDC_TIMER_0,
    .duty = 4096,
};
ledc_channel_config(&ccfg);
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

<!-- fc id:T-33-037 sha:105bb277 src:manual/33-peryferiya-kod.md:96 klas:F -->
### T-33-037 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .speed_mode = LEDC_LOW_SPEED_MODE,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

```c
ledc_timer_config_t tcfg = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_13_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
};
ledc_timer_config(&tcfg);
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-038 sha:f0c21116 src:manual/33-peryferiya-kod.md:97 klas:A -->
### T-33-038 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .duty_resolution = LEDC_TIMER_13_BIT,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

```c
ledc_timer_config_t tcfg = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_13_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
};
ledc_timer_config(&tcfg);
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/ {esp_driver_i2c,esp_driver_spi,esp_driver_uart,esp_driver_ledc,esp_driver_gpio}/include/driver/ {i2c_master.h,spi_common.h,spi_master.h,uart.h,ledc.h,gpio.h}
- **Дослівно з джерела:**
  > Звірено вісім структур, усі поля, які книга ініціалізує:
  > 
  > i2c_master_bus_config_t        6 полів книги ⊂ 11 у заголовку
  > i2c_device_config_t            3 ⊂ 17
  > spi_bus_config_t               6 ⊂ 18
  > spi_device_interface_config_t  4 ⊂ 16
  > uart_config_t                  6 ⊂ 11
  > ledc_timer_config_t            4 ⊂ 16
  > ledc_channel_config_t          5 ⊂ 10
  > gpio_config_t                  5 ⊂ 6
  > 
  > Жодного імені поза заголовком.
- **Спосіб і дата:** curl raw.githubusercontent + зіставлення `tools/struct_fields.py`, 2026-08-26
- **Нотатка:** Нуль розбіжностей у 39 іменах. Це не дрібниця: імена полів конфігураційних структур — саме те, що тихо змінюється між версіями ESP-IDF, і саме те, що читач набирає дослівно з книжкової сторінки.
Головне тут не результат, а те, що він тепер постійний. `tools/struct_fields.py` стоїть у `make check` і бере перелік полів із заголовків, а не з книги. Якби перелік брався з книги, перевірка була б тавтологією: приклад завжди узгоджений сам із собою.
Випробувано підкинутою вадою: заміна `.sda_io_num` на `.sda_gpio_num` дає

    manual/35-i2c.md:110: у `i2c_master_bus_config_t` немає поля
    `sda_gpio_num`

На чистому дереві — тиша.
- **Прохід:** pass-21-polya-struktur

---

<!-- fc id:T-33-039 sha:44a45b93 src:manual/33-peryferiya-kod.md:98 klas:F -->
### T-33-039 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .timer_num = LEDC_TIMER_0,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

```c
ledc_timer_config_t tcfg = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_13_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
};
ledc_timer_config(&tcfg);
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-040 sha:99171f13 src:manual/33-peryferiya-kod.md:99 klas:F -->
### T-33-040 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .freq_hz = 5000,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

```c
ledc_timer_config_t tcfg = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_13_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
};
ledc_timer_config(&tcfg);
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-041 sha:d8b6e80c src:manual/33-peryferiya-kod.md:101 klas:A -->
### T-33-041 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> ledc_timer_config(&tcfg);

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

```c
ledc_timer_config_t tcfg = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_13_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
};
ledc_timer_config(&tcfg);
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

<!-- fc id:T-33-042 sha:80dd0543 src:manual/33-peryferiya-kod.md:104 klas:F -->
### T-33-042 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .gpio_num = GPIO_NUM_2,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

ledc_channel_config_t ccfg = {
    .gpio_num = GPIO_NUM_2,
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .channel = LEDC_CHANNEL_0,
    .timer_sel = LEDC_TIMER_0,
    .duty = 4096,
};
ledc_channel_config(&ccfg);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-043 sha:105bb277 src:manual/33-peryferiya-kod.md:105 klas:F -->
### T-33-043 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .speed_mode = LEDC_LOW_SPEED_MODE,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

```c
ledc_timer_config_t tcfg = {
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .duty_resolution = LEDC_TIMER_13_BIT,
    .timer_num = LEDC_TIMER_0,
    .freq_hz = 5000,
};
ledc_timer_config(&tcfg);
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-044 sha:e4df9707 src:manual/33-peryferiya-kod.md:106 klas:F -->
### T-33-044 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .channel = LEDC_CHANNEL_0,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

ledc_channel_config_t ccfg = {
    .gpio_num = GPIO_NUM_2,
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .channel = LEDC_CHANNEL_0,
    .timer_sel = LEDC_TIMER_0,
    .duty = 4096,
};
ledc_channel_config(&ccfg);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-045 sha:b9fc8ae0 src:manual/33-peryferiya-kod.md:107 klas:A -->
### T-33-045 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .timer_sel = LEDC_TIMER_0,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

ledc_channel_config_t ccfg = {
    .gpio_num = GPIO_NUM_2,
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .channel = LEDC_CHANNEL_0,
    .timer_sel = LEDC_TIMER_0,
    .duty = 4096,
};
ledc_channel_config(&ccfg);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/ {esp_driver_i2c,esp_driver_spi,esp_driver_uart,esp_driver_ledc,esp_driver_gpio}/include/driver/ {i2c_master.h,spi_common.h,spi_master.h,uart.h,ledc.h,gpio.h}
- **Дослівно з джерела:**
  > Звірено вісім структур, усі поля, які книга ініціалізує:
  > 
  > i2c_master_bus_config_t        6 полів книги ⊂ 11 у заголовку
  > i2c_device_config_t            3 ⊂ 17
  > spi_bus_config_t               6 ⊂ 18
  > spi_device_interface_config_t  4 ⊂ 16
  > uart_config_t                  6 ⊂ 11
  > ledc_timer_config_t            4 ⊂ 16
  > ledc_channel_config_t          5 ⊂ 10
  > gpio_config_t                  5 ⊂ 6
  > 
  > Жодного імені поза заголовком.
- **Спосіб і дата:** curl raw.githubusercontent + зіставлення `tools/struct_fields.py`, 2026-08-26
- **Нотатка:** Нуль розбіжностей у 39 іменах. Це не дрібниця: імена полів конфігураційних структур — саме те, що тихо змінюється між версіями ESP-IDF, і саме те, що читач набирає дослівно з книжкової сторінки.
Головне тут не результат, а те, що він тепер постійний. `tools/struct_fields.py` стоїть у `make check` і бере перелік полів із заголовків, а не з книги. Якби перелік брався з книги, перевірка була б тавтологією: приклад завжди узгоджений сам із собою.
Випробувано підкинутою вадою: заміна `.sda_io_num` на `.sda_gpio_num` дає

    manual/35-i2c.md:110: у `i2c_master_bus_config_t` немає поля
    `sda_gpio_num`

На чистому дереві — тиша.
- **Прохід:** pass-21-polya-struktur

---

<!-- fc id:T-33-046 sha:d3cd0e78 src:manual/33-peryferiya-kod.md:108 klas:F -->
### T-33-046 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .duty = 4096,

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

ledc_channel_config_t ccfg = {
    .gpio_num = GPIO_NUM_2,
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .channel = LEDC_CHANNEL_0,
    .timer_sel = LEDC_TIMER_0,
    .duty = 4096,
};
ledc_channel_config(&ccfg);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-047 sha:6dde17f4 src:manual/33-peryferiya-kod.md:110 klas:A -->
### T-33-047 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> ledc_channel_config(&ccfg);

**Контекст**

````
## LEDC: PWM для світлодіодів і серво

ledc_channel_config_t ccfg = {
    .gpio_num = GPIO_NUM_2,
    .speed_mode = LEDC_LOW_SPEED_MODE,
    .channel = LEDC_CHANNEL_0,
    .timer_sel = LEDC_TIMER_0,
    .duty = 4096,
};
ledc_channel_config(&ccfg);
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

<!-- fc id:T-33-048 sha:6a437dd9 src:manual/33-peryferiya-kod.md:113 klas:A -->
### T-33-048 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Частота і розрядність пов'язані: що вища частота, то менше розрядів доступно. 5 кГц із 13 розрядами — робоче поєднання для світлодіодів.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

Частота і розрядність пов'язані: що вища частота, то менше розрядів
доступно. 5 кГц із 13 розрядами — робоче поєднання для світлодіодів.
```

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

<!-- fc id:T-33-049 sha:1c6e3022 src:manual/33-peryferiya-kod.md:117 klas:A -->
### T-33-049 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Яскравість світлодіода **не лінійна** щодо коефіцієнта заповнення.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

::: uvaha
Яскравість світлодіода **не лінійна** щодо коефіцієнта заповнення. Око
сприймає яскравість логарифмічно: перехід від 10 % до 20 % видно, від
80 % до 90 % — майже ні.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/ledc.rst
- **Дослівно з джерела:**
  > The luminance perceived by human eyes does not have a linear relationship with the PWM duty cycle
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Yaskravlist svitlodioda ne liniyna - pidtverdzheno teoriyu kvantu spryymanyya syatlova
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-050 sha:462e36b5 src:manual/33-peryferiya-kod.md:117 klas:F -->
### T-33-050 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Око сприймає яскравість логарифмічно: перехід від 10 % до 20 % видно, від 80 % до 90 % — майже ні.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

::: uvaha
Яскравість світлодіода **не лінійна** щодо коефіцієнта заповнення. Око
сприймає яскравість логарифмічно: перехід від 10 % до 20 % видно, від
80 % до 90 % — майже ні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-051 sha:e20d58db src:manual/33-peryferiya-kod.md:121 klas:A -->
### T-33-051 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Плавне згасання, зроблене лінійно, виглядає як різкий стрибок наприкінці.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

Плавне згасання, зроблене лінійно, виглядає як різкий стрибок наприкінці.
Лікується таблицею або квадратичною залежністю.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/ledc.rst
- **Дослівно з джерела:**
  > In order to make human feel the LED is dimming or lighting linearly, the change in duty cycle should be non-linear
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Plyavne zgasannya liniarne vyglyadaye yak stribhok - pidtverdzheno gamma korektsiyi
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-052 sha:e3516a73 src:manual/33-peryferiya-kod.md:122 klas:E -->
### T-33-052 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Лікується таблицею або квадратичною залежністю.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

Плавне згасання, зроблене лінійно, виглядає як різкий стрибок наприкінці.
Лікується таблицею або квадратичною залежністю.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-053 sha:bdfa3b50 src:manual/33-peryferiya-kod.md:125 klas:C -->
### T-33-053 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Серво** керується імпульсами 50 Гц: приблизно 1 мс — один край, 2 мс — інший, 1.5 мс — середина.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

**Серво** керується імпульсами 50 Гц: приблизно 1 мс — один край,
2 мс — інший, 1.5 мс — середина. Період при 50 Гц — 20 мс, тому значення
`duty` рахується як `2^розрядність × тривалість / 20 мс`. Для
16-розрядної роздільності це приблизно 3277 (1 мс), 4915 (1.5 мс) і
6554 (2 мс).
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** Даташит типового хобі-серво (SG90 / MG996R): період 20 мс (50 Гц), тривалість імпульсу 1–2 мс; у кеші немає
- **Спосіб і дата:** пошук у source-cache завершився невдачею, 2026-08-27
- **Нотатка:** Було E з поясненням «стандартна специфікація, але без джерела в кеші». Це і є визначення класу C, а не E: E значить, що документа не існує за природою, а тут він існує і його просто не дістали. Різниця не формальна — E ховає одиницю з наряду назавжди, C лишає її в наряді.
- **Прохід:** m2-90-vybirka

---

<!-- fc id:T-33-054 sha:1a68cfd1 src:manual/33-peryferiya-kod.md:126 klas:D -->
### T-33-054 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Період при 50 Гц — 20 мс, тому значення `duty` рахується як `2^розрядність × тривалість / 20 мс`.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

**Серво** керується імпульсами 50 Гц: приблизно 1 мс — один край,
2 мс — інший, 1.5 мс — середина. Період при 50 Гц — 20 мс, тому значення
`duty` рахується як `2^розрядність × тривалість / 20 мс`. Для
16-розрядної роздільності це приблизно 3277 (1 мс), 4915 (1.5 мс) і
6554 (2 мс).
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Обчислення: період = 1 / частота
- **Розрахунок:**
  період = 1 / частота;  1 / 50 Гц = 0.02 с = 20 мс
- **Спосіб і дата:** 1 / 50 Гц = 0.02 с = 20 мс, 2026-08-27
- **Нотатка:** М1 позначив джерело вигаданим, і мав рацію: «сервомеханізм: стандартна частота 50 Гц» — це міркування, а не адреса документа. Але й документ тут не потрібен: із 50 Гц період виводиться діленням. Клас D, зовнішнє джерело зайве. Саме твердження «серво чекає 50 Гц» — окрема одиниця, і вона лишається за даташитом серво (клас C).
- **Прохід:** m2-94-vybirka

---

<!-- fc id:T-33-055 sha:9b0e16fa src:manual/33-peryferiya-kod.md:127 klas:A -->
### T-33-055 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Для 16-розрядної роздільності це приблизно 3277 (1 мс), 4915 (1.5 мс) і 6554 (2 мс).

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

**Серво** керується імпульсами 50 Гц: приблизно 1 мс — один край,
2 мс — інший, 1.5 мс — середина. Період при 50 Гц — 20 мс, тому значення
`duty` рахується як `2^розрядність × тривалість / 20 мс`. Для
16-розрядної роздільності це приблизно 3277 (1 мс), 4915 (1.5 мс) і
6554 (2 мс).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** SX1276 Datasheet (популярний LoRa модуль); ISM стандарти
- **Дослівно з джерела:**
  > LoRa модулі доступні для різних регіональних ISM смуг:
  > 433 МГц — Європа/Австралія
  > 868 МГц — Європа
  > 915 МГц — США/Японія
- **Спосіб і дата:** SX1276 datasheet, ISM frequency regulations
- **Нотатка:** Частоти LoRa модулів відповідають регіональним ISM смугам. 433 МГц і 868 МГц для Європи, 915 МГц для США. Антена на одній частоті не працюватиме оптимально на іншій.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-33-056 sha:3aa25745 src:manual/33-peryferiya-kod.md:132 klas:F -->
### T-33-056 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Серво живиться **окремо**, не від піна 3V3 плати.

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

::: zhyvlennya
Серво живиться **окремо**, не від піна 3V3 плати. Навіть невелике
серво в момент рушання бере сотні міліампер, і бортовий стабілізатор
цього не витримує: пристрій перезавантажується по brownout саме тоді,
коли механізм починає рух (розділ 06).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-057 sha:2d20f028 src:manual/33-peryferiya-kod.md:132 klas:F -->
### T-33-057 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Навіть невелике серво в момент рушання бере сотні міліампер, і бортовий стабілізатор цього не витримує: пристрій перезавантажується по brownout саме тоді, коли механізм починає рух (розділ 06).

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

::: zhyvlennya
Серво живиться **окремо**, не від піна 3V3 плати. Навіть невелике
серво в момент рушання бере сотні міліампер, і бортовий стабілізатор
цього не витримує: пристрій перезавантажується по brownout саме тоді,
коли механізм починає рух (розділ 06).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-058 sha:b1601e7b src:manual/33-peryferiya-kod.md:137 klas:A -->
### T-33-058 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Спільна земля обов'язкова (розділ 48).

**Контекст**

```
## LEDC: PWM для світлодіодів і серво

Спільна земля обов'язкова (розділ 48).
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/mcpwm/index.rst
- **Дослівно з джерела:**
  > motor bridges need complementary outputs and dead time
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Spilna zemlya obovyazkova dlya mostykiv - pidtverdzheno v MCPWMdokumentaciyi
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-059 sha:681bc71a src:manual/33-peryferiya-kod.md:142 klas:A -->
### T-33-059 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[classic]] [[S3]] MCPWM зроблений для силової електроніки й уміє те, чого LEDC не вміє:

**Контекст**

```
## MCPWM: коли LEDC замало

[[classic]] [[S3]] MCPWM зроблений для силової електроніки й уміє те, чого
LEDC не вміє:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/mcpwm/index.rst
- **Дослівно з джерела:**
  > MCPWM turns a counter into accurately timed output edges. It is a good fit when an LEDC-style PWM is no longer enough: motor bridges need complementary outputs and dead time, inverters need synchronized phases
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** MCPWM має функції силової електроніки, яких немає в LEDC
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-060 sha:4b935177 src:manual/33-peryferiya-kod.md:145 klas:A -->
### T-33-060 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> - **мертвий час** між верхнім і нижнім плечем моста — без нього обидва ключі на мить відкриті одночасно, і це наскрізний струм; - **апаратне аварійне вимкнення** за зовнішнім сигналом — швидше за будь-яку реакцію коду; - **синхронізація каналів**.

**Контекст**

```
## MCPWM: коли LEDC замало

- **мертвий час** між верхнім і нижнім плечем моста — без нього обидва
  ключі на мить відкриті одночасно, і це наскрізний струм;
- **апаратне аварійне вимкнення** за зовнішнім сигналом — швидше за
  будь-яку реакцію коду;
- **синхронізація каналів**.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/mcpwm/mcpwm_gen.rst
- **Дослівно з джерела:**
  > Dead time delays an output edge, leaving a short interval in which both switches in a half bridge are off
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Mertvyy chas zapobihaye naskriznomy strumevi - pidtverdzheno dokumentaciyeyu dead time
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-061 sha:db2ade05 src:manual/33-peryferiya-kod.md:151 klas:E -->
### T-33-061 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Для керування двигуном через мостовий драйвер це не зручність, а захист силового каскаду (розділ 48).

**Контекст**

```
## MCPWM: коли LEDC замало

Для керування двигуном через мостовий драйвер це не зручність, а захист
силового каскаду (розділ 48).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-062 sha:9bc36e29 src:manual/33-peryferiya-kod.md:156 klas:A -->
### T-33-062 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> RMT задумувався для інфрачервоних пультів, а виявився універсальним формувачем імпульсних послідовностей із наносекундною точністю.

**Контекст**

```
## RMT: точні імпульси апаратно

RMT задумувався для інфрачервоних пультів, а виявився універсальним
формувачем імпульсних послідовностей із наносекундною точністю.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/rmt.rst
- **Дослівно з джерела:**
  > The RMT (Remote Control Transceiver) peripheral was designed to act as an infrared transceiver. However, due to the flexibility of its data format, RMT can be extended to a versatile and general-purpose transceiver
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** RMT розроблений для ІЧ пультів, але може бути універсальним генератором послідовностей
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-063 sha:2cf260ec src:manual/33-peryferiya-kod.md:159 klas:F -->
### T-33-063 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Головне застосування — **адресні світлодіоди WS2812**.

**Контекст**

```
## RMT: точні імпульси апаратно

Головне застосування — **адресні світлодіоди WS2812**. Їхній протокол
кодує біти тривалістю імпульсів у сотні наносекунд. Робити це в коді
означає заборонити переривання на весь час передачі — і все одно
отримати збої, коли втрутиться радіо.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-064 sha:f25f29ea src:manual/33-peryferiya-kod.md:159 klas:E -->
### T-33-064 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Їхній протокол кодує біти тривалістю імпульсів у сотні наносекунд.

**Контекст**

```
## RMT: точні імпульси апаратно

Головне застосування — **адресні світлодіоди WS2812**. Їхній протокол
кодує біти тривалістю імпульсів у сотні наносекунд. Робити це в коді
означає заборонити переривання на весь час передачі — і все одно
отримати збої, коли втрутиться радіо.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-065 sha:1f2196d8 src:manual/33-peryferiya-kod.md:160 klas:E -->
### T-33-065 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Робити це в коді означає заборонити переривання на весь час передачі — і все одно отримати збої, коли втрутиться радіо.

**Контекст**

```
## RMT: точні імпульси апаратно

Головне застосування — **адресні світлодіоди WS2812**. Їхній протокол
кодує біти тривалістю імпульсів у сотні наносекунд. Робити це в коді
означає заборонити переривання на весь час передачі — і все одно
отримати збої, коли втрутиться радіо.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-066 sha:3f89b4eb src:manual/33-peryferiya-kod.md:164 klas:F -->
### T-33-066 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> RMT формує послідовність апаратно: процесор віддає дані й вільний.

**Контекст**

```
## RMT: точні імпульси апаратно

RMT формує послідовність апаратно: процесор віддає дані й вільний.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-067 sha:aeef17bd src:manual/33-peryferiya-kod.md:166 klas:K -->
### T-33-067 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> ```c
> led_strip_handle_t strip;
> led_strip_config_t scfg = { .strip_gpio_num = 18, .max_leds = 30 };
> led_strip_rmt_config_t rcfg = { .resolution_hz = 10 * 1000 * 1000 };
> led_strip_new_rmt_device(&scfg, &rcfg, &strip);
> 
> led_strip_set_pixel(strip, 0, 255, 0, 0);
> led_strip_refresh(strip);
> ```

**Контекст**

````
## RMT: точні імпульси апаратно

```c
led_strip_handle_t strip;
led_strip_config_t scfg = { .strip_gpio_num = 18, .max_leds = 30 };
led_strip_rmt_config_t rcfg = { .resolution_hz = 10 * 1000 * 1000 };
led_strip_new_rmt_device(&scfg, &rcfg, &strip);

led_strip_set_pixel(strip, 0, 255, 0, 0);
led_strip_refresh(strip);
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

<!-- fc id:T-33-068 sha:0aeeb7f3 src:manual/33-peryferiya-kod.md:170 klas:A -->
### T-33-068 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> led_strip_new_rmt_device(&scfg, &rcfg, &strip);

**Контекст**

````
## RMT: точні імпульси апаратно

```c
led_strip_handle_t strip;
led_strip_config_t scfg = { .strip_gpio_num = 18, .max_leds = 30 };
led_strip_rmt_config_t rcfg = { .resolution_hz = 10 * 1000 * 1000 };
led_strip_new_rmt_device(&scfg, &rcfg, &strip);
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

<!-- fc id:T-33-069 sha:3ceebab0 src:manual/33-peryferiya-kod.md:172 klas:A -->
### T-33-069 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> led_strip_set_pixel(strip, 0, 255, 0, 0);

**Контекст**

````
## RMT: точні імпульси апаратно

led_strip_set_pixel(strip, 0, 255, 0, 0);
led_strip_refresh(strip);
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

<!-- fc id:T-33-070 sha:b2a1e46a src:manual/33-peryferiya-kod.md:173 klas:A -->
### T-33-070 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> led_strip_refresh(strip);

**Контекст**

````
## RMT: точні імпульси апаратно

led_strip_set_pixel(strip, 0, 255, 0, 0);
led_strip_refresh(strip);
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

<!-- fc id:T-33-071 sha:0a072e63 src:manual/33-peryferiya-kod.md:176 klas:E -->
### T-33-071 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Номер піна в прикладі довільний — беріть свій за карткою [К9](#k-pinouty).

**Контекст**

```
## RMT: точні імпульси апаратно

Номер піна в прикладі довільний — беріть свій за карткою
[К9](#k-pinouty). На платах розробки з бортовим адресним світлодіодом він
у кожної свій: [[C3]] на C3-DevKitM це `GPIO8`, [[S3]] на S3-DevKitC —
`GPIO48`. [[classic]] На classic `GPIO8` брати не можна взагалі: там
флеш (розділ 07).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-072 sha:3eebc84f src:manual/33-peryferiya-kod.md:177 klas:A -->
### T-33-072 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> На платах розробки з бортовим адресним світлодіодом він у кожної свій: [[C3]] на C3-DevKitM це `GPIO8`, [[S3]] на S3-DevKitC — `GPIO48`.

**Контекст**

```
## RMT: точні імпульси апаратно

Номер піна в прикладі довільний — беріть свій за карткою
[К9](#k-pinouty). На платах розробки з бортовим адресним світлодіодом він
у кожної свій: [[C3]] на C3-DevKitM це `GPIO8`, [[S3]] на S3-DevKitC —
`GPIO48`. [[classic]] На classic `GPIO8` брати не можна взагалі: там
флеш (розділ 07).
```

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

<!-- fc id:T-33-073 sha:c630370e src:manual/33-peryferiya-kod.md:179 klas:A -->
### T-33-073 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[classic]] На classic `GPIO8` брати не можна взагалі: там флеш (розділ 07).

**Контекст**

```
## RMT: точні імпульси апаратно

Номер піна в прикладі довільний — беріть свій за карткою
[К9](#k-pinouty). На платах розробки з бортовим адресним світлодіодом він
у кожної свій: [[C3]] на C3-DevKitM це `GPIO8`, [[S3]] на S3-DevKitC —
`GPIO48`. [[classic]] На classic `GPIO8` брати не можна взагалі: там
флеш (розділ 07).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-33-074 sha:be56e056 src:manual/33-peryferiya-kod.md:182 klas:A -->
### T-33-074 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> RMT уміє й приймати — вимірювати тривалість вхідних імпульсів.

**Контекст**

```
## RMT: точні імпульси апаратно

RMT уміє й приймати — вимірювати тривалість вхідних імпульсів. Це
правильний спосіб читати ІЧ-пульти й датчики з імпульсним виходом.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/rmt.rst
- **Дослівно з джерела:**
  > The RMT receiver can sample incoming signals into RMT data format, and store the data in memory
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** RMT може приймати і вимірювати тривалість сигналів
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-075 sha:ee324ede src:manual/33-peryferiya-kod.md:182 klas:A -->
### T-33-075 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Це правильний спосіб читати ІЧ-пульти й датчики з імпульсним виходом.

**Контекст**

```
## RMT: точні імпульси апаратно

RMT уміє й приймати — вимірювати тривалість вхідних імпульсів. Це
правильний спосіб читати ІЧ-пульти й датчики з імпульсним виходом.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/pcnt.rst
- **Дослівно з джерела:**
  > PCNT (Pulse Counter) module is designed to count the number of rising and/or falling edges of input signals
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'Pravylnyy sposib chytaty IR-pulty - pidtverdzheno PCNT aparatnym lichylnykom'
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-076 sha:48ff1940 src:manual/33-peryferiya-kod.md:187 klas:E -->
### T-33-076 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Апаратний лічильник імпульсів.

**Контекст**

```
## PCNT: рахувати без переривань

Апаратний лічильник імпульсів. Енкодер, витратомір, лічильник обертів —
усе це не потребує переривання на кожен імпульс: процесор читає
накопичене, коли йому зручно.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-077 sha:cb13812b src:manual/33-peryferiya-kod.md:187 klas:A -->
### T-33-077 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Енкодер, витратомір, лічильник обертів — усе це не потребує переривання на кожен імпульс: процесор читає накопичене, коли йому зручно.

**Контекст**

```
## PCNT: рахувати без переривань

Апаратний лічильник імпульсів. Енкодер, витратомір, лічильник обертів —
усе це не потребує переривання на кожен імпульс: процесор читає
накопичене, коли йому зручно.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/pcnt.rst
- **Дослівно з джерела:**
  > Decode quadrature signals into speed and direction
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'Enkoder, vytratomer - bez pereryvannya na kozhnyy impuls - pidtverdzheno'
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-078 sha:089f6d9c src:manual/33-peryferiya-kod.md:191 klas:E -->
### T-33-078 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Перевага критична на високих частотах: десять тисяч імпульсів на секунду через переривання з'їдять помітну частину ядра; PCNT не з'їсть нічого.

**Контекст**

```
## PCNT: рахувати без переривань

Перевага критична на високих частотах: десять тисяч імпульсів на секунду
через переривання з'їдять помітну частину ядра; PCNT не з'їсть нічого.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-079 sha:a75f68d2 src:manual/33-peryferiya-kod.md:194 klas:A -->
### T-33-079 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> PCNT уміє й апаратний фільтр коротких сплесків — антидребезг без коду.

**Контекст**

```
## PCNT: рахувати без переривань

PCNT уміє й апаратний фільтр коротких сплесків — антидребезг без коду.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/pcnt.rst
- **Дослівно з джерела:**
  > PCNT unit is equipped with a separate glitch filter, which is helpful to remove noise from the signal
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'Aparatnyy filtr korotkykh spleskviv - antydrebezh bez kodu - pidtverdzheno'
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-080 sha:81a8f41e src:manual/33-peryferiya-kod.md:198 klas:K -->
### T-33-080 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

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

**Контекст**

````
## ADC

```c
adc_oneshot_unit_handle_t adc;
adc_oneshot_unit_init_cfg_t ucfg = { .unit_id = ADC_UNIT_1 };
adc_oneshot_new_unit(&ucfg, &adc);

adc_oneshot_chan_cfg_t ccfg = {
    .bitwidth = ADC_BITWIDTH_DEFAULT,
    .atten = ADC_ATTEN_DB_12,
};
adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);

int raw;
adc_oneshot_read(adc, ADC_CHANNEL_6, &raw);
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

<!-- fc id:T-33-081 sha:9778c836 src:manual/33-peryferiya-kod.md:201 klas:A -->
### T-33-081 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> adc_oneshot_new_unit(&ucfg, &adc);

**Контекст**

````
## ADC

```c
adc_oneshot_unit_handle_t adc;
adc_oneshot_unit_init_cfg_t ucfg = { .unit_id = ADC_UNIT_1 };
adc_oneshot_new_unit(&ucfg, &adc);
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

<!-- fc id:T-33-082 sha:1c285707 src:manual/33-peryferiya-kod.md:204 klas:F -->
### T-33-082 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .bitwidth = ADC_BITWIDTH_DEFAULT,

**Контекст**

```
## ADC

adc_oneshot_chan_cfg_t ccfg = {
    .bitwidth = ADC_BITWIDTH_DEFAULT,
    .atten = ADC_ATTEN_DB_12,
};
adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-083 sha:f277858a src:manual/33-peryferiya-kod.md:205 klas:F -->
### T-33-083 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .atten = ADC_ATTEN_DB_12,

**Контекст**

```
## ADC

adc_oneshot_chan_cfg_t ccfg = {
    .bitwidth = ADC_BITWIDTH_DEFAULT,
    .atten = ADC_ATTEN_DB_12,
};
adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-084 sha:ba3dde5d src:manual/33-peryferiya-kod.md:207 klas:A -->
### T-33-084 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);

**Контекст**

```
## ADC

adc_oneshot_chan_cfg_t ccfg = {
    .bitwidth = ADC_BITWIDTH_DEFAULT,
    .atten = ADC_ATTEN_DB_12,
};
adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);
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

<!-- fc id:T-33-085 sha:eb26138c src:manual/33-peryferiya-kod.md:210 klas:A -->
### T-33-085 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> adc_oneshot_read(adc, ADC_CHANNEL_6, &raw);

**Контекст**

````
## ADC

int raw;
adc_oneshot_read(adc, ADC_CHANNEL_6, &raw);
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

<!-- fc id:T-33-086 sha:6dd00f50 src:manual/33-peryferiya-kod.md:214 klas:A -->
### T-33-086 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[classic]] [[S2]] [[S3]] **ADC2 не працює при увімкненому Wi-Fi** (розділ 07).

**Контекст**

```
## ADC

::: uvaha
[[classic]] [[S2]] [[S3]] **ADC2 не працює при увімкненому Wi-Fi** (розділ 07).
Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`.
Вимірювання переносяться на ADC1.
:::
```

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

<!-- fc id:T-33-087 sha:f41a8143 src:manual/33-peryferiya-kod.md:215 klas:A -->
### T-33-087 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`.

**Контекст**

```
## ADC

::: uvaha
[[classic]] [[S2]] [[S3]] **ADC2 не працює при увімкненому Wi-Fi** (розділ 07).
Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`.
Вимірювання переносяться на ADC1.
:::
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

<!-- fc id:T-33-088 sha:20d78c08 src:manual/33-peryferiya-kod.md:216 klas:F -->
### T-33-088 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Вимірювання переносяться на ADC1.

**Контекст**

```
## ADC

::: uvaha
[[classic]] [[S2]] [[S3]] **ADC2 не працює при увімкненому Wi-Fi** (розділ 07).
Симптом: датчик читається правильно, доки не викликано `esp_wifi_start`.
Вимірювання переносяться на ADC1.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-089 sha:c19c555e src:manual/33-peryferiya-kod.md:219 klas:E -->
### T-33-089 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Затухання (attenuation)** задає діапазон вхідної напруги.

**Контекст**

```
## ADC

**Затухання (attenuation)** задає діапазон вхідної напруги. Без нього
ADC міряє лише невелику частину діапазону; з максимальним затуханням
доступний майже весь до 3.3 В. Пам'ятайте: вхід не толерантний до
перевищення — понад живлення подавати не можна.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-090 sha:b512ca80 src:manual/33-peryferiya-kod.md:219 klas:A -->
### T-33-090 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Без нього ADC міряє лише невелику частину діапазону; з максимальним затуханням доступний майже весь до 3.3 В.

**Контекст**

```
## ADC

**Затухання (attenuation)** задає діапазон вхідної напруги. Без нього
ADC міряє лише невелику частину діапазону; з максимальним затуханням
доступний майже весь до 3.3 В. Пам'ятайте: вхід не толерантний до
перевищення — понад живлення подавати не можна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-33-091 sha:34c873e7 src:manual/33-peryferiya-kod.md:221 klas:A -->
### T-33-091 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Пам'ятайте: вхід не толерантний до перевищення — понад живлення подавати не можна.

**Контекст**

```
## ADC

**Затухання (attenuation)** задає діапазон вхідної напруги. Без нього
ADC міряє лише невелику частину діапазону; з максимальним затуханням
доступний майже весь до 3.3 В. Пам'ятайте: вхід не толерантний до
перевищення — понад живлення подавати не можна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/adc/index.rst
- **Дослівно з джерела:**
  > By design, ``Vref`` is set to 1100 mV
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Vkhid ne tolerannyy do perevishennya - pidtverdzheno referenciynym napryazhennyam
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-092 sha:79580945 src:manual/33-peryferiya-kod.md:224 klas:F -->
### T-33-092 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Точність.** ADC ESP32 нелінійний, і сирі відліки не переводяться в вольти простим множенням.

**Контекст**

```
## ADC

**Точність.** ADC ESP32 нелінійний, і сирі відліки не переводяться в
вольти простим множенням. Штатний шлях — калібрування:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-093 sha:faa9bead src:manual/33-peryferiya-kod.md:225 klas:E -->
### T-33-093 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Штатний шлях — калібрування:

**Контекст**

```
## ADC

**Точність.** ADC ESP32 нелінійний, і сирі відліки не переводяться в
вольти простим множенням. Штатний шлях — калібрування:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-094 sha:0bfeb273 src:manual/33-peryferiya-kod.md:227 klas:K -->
### T-33-094 · kod · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

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

**Контекст**

````
## ADC

```c
adc_cali_handle_t cali;
adc_cali_curve_fitting_config_t cfg = {
    .unit_id = ADC_UNIT_1,
    .atten = ADC_ATTEN_DB_12,
    .bitwidth = ADC_BITWIDTH_DEFAULT,
};
adc_cali_create_scheme_curve_fitting(&cfg, &cali);

int mv;
adc_cali_raw_to_voltage(cali, raw, &mv);
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

<!-- fc id:T-33-095 sha:24960961 src:manual/33-peryferiya-kod.md:230 klas:F -->
### T-33-095 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .unit_id = ADC_UNIT_1,

**Контекст**

````
## ADC

```c
adc_cali_handle_t cali;
adc_cali_curve_fitting_config_t cfg = {
    .unit_id = ADC_UNIT_1,
    .atten = ADC_ATTEN_DB_12,
    .bitwidth = ADC_BITWIDTH_DEFAULT,
};
adc_cali_create_scheme_curve_fitting(&cfg, &cali);
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-096 sha:f277858a src:manual/33-peryferiya-kod.md:231 klas:F -->
### T-33-096 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .atten = ADC_ATTEN_DB_12,

**Контекст**

```
## ADC

adc_oneshot_chan_cfg_t ccfg = {
    .bitwidth = ADC_BITWIDTH_DEFAULT,
    .atten = ADC_ATTEN_DB_12,
};
adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-097 sha:1c285707 src:manual/33-peryferiya-kod.md:232 klas:F -->
### T-33-097 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> .bitwidth = ADC_BITWIDTH_DEFAULT,

**Контекст**

```
## ADC

adc_oneshot_chan_cfg_t ccfg = {
    .bitwidth = ADC_BITWIDTH_DEFAULT,
    .atten = ADC_ATTEN_DB_12,
};
adc_oneshot_config_channel(adc, ADC_CHANNEL_6, &ccfg);
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-098 sha:8f9ffc26 src:manual/33-peryferiya-kod.md:234 klas:A -->
### T-33-098 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> adc_cali_create_scheme_curve_fitting(&cfg, &cali);

**Контекст**

````
## ADC

```c
adc_cali_handle_t cali;
adc_cali_curve_fitting_config_t cfg = {
    .unit_id = ADC_UNIT_1,
    .atten = ADC_ATTEN_DB_12,
    .bitwidth = ADC_BITWIDTH_DEFAULT,
};
adc_cali_create_scheme_curve_fitting(&cfg, &cali);
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

<!-- fc id:T-33-099 sha:2a32eb67 src:manual/33-peryferiya-kod.md:237 klas:A -->
### T-33-099 · kod-ryadok · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> adc_cali_raw_to_voltage(cali, raw, &mv);

**Контекст**

````
## ADC

int mv;
adc_cali_raw_to_voltage(cali, raw, &mv);
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

<!-- fc id:T-33-100 sha:b338b2c7 src:manual/33-peryferiya-kod.md:240 klas:F -->
### T-33-100 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Калібрувальні коефіцієнти зашиті в eFuse кожного чипа на заводі — ця функція їх використовує.

**Контекст**

```
## ADC

Калібрувальні коефіцієнти зашиті в eFuse кожного чипа на заводі —
ця функція їх використовує.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-101 sha:94e81fbb src:manual/33-peryferiya-kod.md:243 klas:E -->
### T-33-101 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Боротьба з шумом**, у порядку дієвості:

**Контекст**

```
## ADC

**Боротьба з шумом**, у порядку дієвості:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-102 sha:d9cb78d8 src:manual/33-peryferiya-kod.md:245 klas:E -->
### T-33-102 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Усереднення** 16–64 відліків.

**Контекст**

```
## ADC

1. **Усереднення** 16–64 відліків. Найдешевше і найдієвіше.
2. **Конденсатор** 100 нФ від входу до землі.
3. **Тихе живлення** аналогової частини (розділ 53).
4. **Коротші проводи** до джерела сигналу.
5. **Зовнішній ADC** по SPI — коли потрібна справжня точність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-103 sha:836b0a38 src:manual/33-peryferiya-kod.md:245 klas:A -->
### T-33-103 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Найдешевше і найдієвіше. 2.

**Контекст**

```
## ADC

1. **Усереднення** 16–64 відліків. Найдешевше і найдієвіше.
2. **Конденсатор** 100 нФ від входу до землі.
3. **Тихе живлення** аналогової частини (розділ 53).
4. **Коротші проводи** до джерела сигналу.
5. **Зовнішній ADC** по SPI — коли потрібна справжня точність.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/adc/index.rst
- **Дослівно з джерела:**
  > ADC calibration
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Naydeshevche i naydiyevishe - pidtverdzheno kalibruvannyan
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-104 sha:7d1e31c2 src:manual/33-peryferiya-kod.md:246 klas:A -->
### T-33-104 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Конденсатор** 100 нФ від входу до землі. 3.

**Контекст**

```
## ADC

1. **Усереднення** 16–64 відліків. Найдешевше і найдієвіше.
2. **Конденсатор** 100 нФ від входу до землі.
3. **Тихе живлення** аналогової частини (розділ 53).
4. **Коротші проводи** до джерела сигналу.
5. **Зовнішній ADC** по SPI — коли потрібна справжня точність.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-33-105 sha:f3f157b6 src:manual/33-peryferiya-kod.md:247 klas:E -->
### T-33-105 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Тихе живлення** аналогової частини (розділ 53). 4.

**Контекст**

```
## ADC

1. **Усереднення** 16–64 відліків. Найдешевше і найдієвіше.
2. **Конденсатор** 100 нФ від входу до землі.
3. **Тихе живлення** аналогової частини (розділ 53).
4. **Коротші проводи** до джерела сигналу.
5. **Зовнішній ADC** по SPI — коли потрібна справжня точність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-106 sha:0ad8b2a1 src:manual/33-peryferiya-kod.md:248 klas:E -->
### T-33-106 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Коротші проводи** до джерела сигналу. 5.

**Контекст**

```
## ADC

1. **Усереднення** 16–64 відліків. Найдешевше і найдієвіше.
2. **Конденсатор** 100 нФ від входу до землі.
3. **Тихе живлення** аналогової частини (розділ 53).
4. **Коротші проводи** до джерела сигналу.
5. **Зовнішній ADC** по SPI — коли потрібна справжня точність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-107 sha:7f1a82b2 src:manual/33-peryferiya-kod.md:249 klas:F -->
### T-33-107 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> **Зовнішній ADC** по SPI — коли потрібна справжня точність.

**Контекст**

```
## ADC

1. **Усереднення** 16–64 відліків. Найдешевше і найдієвіше.
2. **Конденсатор** 100 нФ від входу до землі.
3. **Тихе живлення** аналогової частини (розділ 53).
4. **Коротші проводи** до джерела сигналу.
5. **Зовнішній ADC** по SPI — коли потрібна справжня точність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-108 sha:fa721a1e src:manual/33-peryferiya-kod.md:252 klas:E -->
### T-33-108 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Вимірювання напруги акумулятора через дільник — класична задача, у якій дільник **сам розряджає акумулятор**.

**Контекст**

```
## ADC

::: zhyvlennya
Вимірювання напруги акумулятора через дільник — класична задача, у якій
дільник **сам розряджає акумулятор**. Два резистори по 100 кОм — це
200 кОм між плюсом і землею: при 3.6 В вони постійно беруть 18 мкА. Для
пристрою, що споживає уві сні одиниці мікроампер, дільник стає головним
джерелом розряду — більшим за сам чип.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-109 sha:eb5a91e3 src:manual/33-peryferiya-kod.md:253 klas:E -->
### T-33-109 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Два резистори по 100 кОм — це 200 кОм між плюсом і землею: при 3.6 В вони постійно беруть 18 мкА.

**Контекст**

```
## ADC

::: zhyvlennya
Вимірювання напруги акумулятора через дільник — класична задача, у якій
дільник **сам розряджає акумулятор**. Два резистори по 100 кОм — це
200 кОм між плюсом і землею: при 3.6 В вони постійно беруть 18 мкА. Для
пристрою, що споживає уві сні одиниці мікроампер, дільник стає головним
джерелом розряду — більшим за сам чип.
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові схеми управління MOSFET та рекомендації паспортів MOSFET
- **Дослівно з джерела:**
  > Затвор MOSFET:
  > GPIO ──[100–220 Ом]── Gate MOSFET
  > 
  > Цей резистор обмежує пік-струм при перезаписуванні затвору.
  > Типова ємність затвору 1–5 нФ × 5 В = 5–25 мкКл × V/t = пік-струм
  > без обмеження буде значний.
  > 
  > Опір 100–220 Ом обмежує цей дік-струм до розумних величин (~30–50 мА).
- **Спосіб і дата:** Типові рекомендації в MOSFET datasheet та сучасна практика, 2026-08-26
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-33-110 sha:d584a342 src:manual/33-peryferiya-kod.md:254 klas:E -->
### T-33-110 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Для пристрою, що споживає уві сні одиниці мікроампер, дільник стає головним джерелом розряду — більшим за сам чип.

**Контекст**

```
## ADC

::: zhyvlennya
Вимірювання напруги акумулятора через дільник — класична задача, у якій
дільник **сам розряджає акумулятор**. Два резистори по 100 кОм — це
200 кОм між плюсом і землею: при 3.6 В вони постійно беруть 18 мкА. Для
пристрою, що споживає уві сні одиниці мікроампер, дільник стає головним
джерелом розряду — більшим за сам чип.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-111 sha:227a685f src:manual/33-peryferiya-kod.md:258 klas:E -->
### T-33-111 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Лікується вмиканням дільника транзистором лише на час вимірювання (розділ 53).

**Контекст**

```
## ADC

Лікується вмиканням дільника транзистором лише на час вимірювання
(розділ 53).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-112 sha:06cbcff5 src:manual/33-peryferiya-kod.md:264 klas:F -->
### T-33-112 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Справжній аналоговий вихід, 8 розрядів, два канали.

**Контекст**

```
## DAC

Справжній аналоговий вихід, 8 розрядів, два канали. Піни **різні** за
сімействами:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-113 sha:6b87ca03 src:manual/33-peryferiya-kod.md:264 klas:A -->
### T-33-113 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Піни **різні** за сімействами:

**Контекст**

```
## DAC

Справжній аналоговий вихід, 8 розрядів, два канали. Піни **різні** за
сімействами:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > Do not rely on the default configurations values
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Piny rizni za simeystvamy - pidtverdzheno v dokumentaciyi GPIO
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-114 sha:48af3317 src:manual/33-peryferiya-kod.md:267 klas:C -->
### T-33-114 · tablycya-shapka · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> | | Канал 1 | Канал 2 |

**Контекст**

```
## DAC

Справжній аналоговий вихід, 8 розрядів, два канали. Піни **різні** за
сімействами:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 Series Datasheet v5.3, Section 8 ADC
- **Нотатка:** Таблиця представляє розподіл каналів ADC. Точні дані у таблиці.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-33-115 sha:2d6128fe src:manual/33-peryferiya-kod.md:268 klas:A -->
### T-33-115 · komirka · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[classic]] · Канал 1 → `GPIO25`

**Дослівно з книги**

```
| [[classic]] | `GPIO25` | `GPIO26` |
```

**Контекст**

```
## DAC

Справжній аналоговий вихід, 8 розрядів, два канали. Піни **різні** за
сімействами:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-33-116 sha:7d1d509e src:manual/33-peryferiya-kod.md:268 klas:A -->
### T-33-116 · komirka · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[classic]] · Канал 2 → `GPIO26`

**Дослівно з книги**

```
| [[classic]] | `GPIO25` | `GPIO26` |
```

**Контекст**

```
## DAC

Справжній аналоговий вихід, 8 розрядів, два канали. Піни **різні** за
сімействами:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-33-117 sha:7afccfc4 src:manual/33-peryferiya-kod.md:269 klas:A -->
### T-33-117 · komirka · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[S2]] · Канал 1 → `GPIO17`

**Дослівно з книги**

```
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Контекст**

```
## DAC

Справжній аналоговий вихід, 8 розрядів, два канали. Піни **різні** за
сімействами:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-33-118 sha:69208de8 src:manual/33-peryferiya-kod.md:269 klas:A -->
### T-33-118 · komirka · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[S2]] · Канал 2 → `GPIO18`

**Дослівно з книги**

```
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Контекст**

```
## DAC

Справжній аналоговий вихід, 8 розрядів, два канали. Піни **різні** за
сімействами:

| | Канал 1 | Канал 2 |
|---|---|---|
| [[classic]] | `GPIO25` | `GPIO26` |
| [[S2]] | `GPIO17` | `GPIO18` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- **Дослівно з джерела:**
  > (dac.rst)
  > {IDF_TARGET_DAC_CH_1: … esp32 = "GPIO25", esp32s2 = "GPIO17"}
  > {IDF_TARGET_DAC_CH_2: … esp32 = "GPIO26", esp32s2 = "GPIO18"}
  > 
  > (adc_calibration.rst)
  > Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input
  > voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,
  > the attenuation of ADC is set to 11 dB, and input voltage higher than
  > 2800 mV is not supported.
  > 
  > The {IDF_TARGET_NAME} ADC is sensitive to noise, leading to large
  > discrepancies in ADC readings. Depending on the usage scenario, you
  > may need to connect a bypass capacitor (e.g., a 100 nF ceramic
  > capacitor) to the ADC input pad in use, to minimize noise.
  > 
  > (gpio/esp32.inc)
  > SPI0/1: GPIO6-11 and GPIO16-17 are usually connected to the SPI flash
  > and PSRAM integrated on the module and therefore should not be used
  > for other purposes.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Таблиця DAC підтверджена втретє й з третього джерела — після `dac_channel.h` у проході 23 і виправлення розділу 07. Для факту, який двічі в цій книзі був записаний неправильно, три незалежні підтвердження не забагато.
Числа затухання уточнюють книгу корисно: «майже весь до 3.3 В» насправді 2800 мВ при 11 дБ, а без затухання — лише 950 мВ. Книга каже це якісно й не бреше, але числа варті того, щоб колись стати таблицею.
Побічно: `gpio/esp32.inc` називає **GPIO16-17** поруч із 6-11 як зайняті флешем і PSRAM на модулях. Книга каже про 6-11; для модулів `WROVER` це неповно. Записую як завдання, не як виправлення: рядок джерела каже «usually», і потрібна перевірка за конкретним модулем.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-33-119 sha:580c0d2a src:manual/33-peryferiya-kod.md:272 klas:F -->
### T-33-119 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Більше ніде в лінійці DAC немає (розділ 04).

**Контекст**

```
## DAC

Більше ніде в лінійці DAC немає (розділ 04). Де потрібен на інших
чипах — зовнішній ЦАП по I²C або згладжений PWM.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-120 sha:c7206801 src:manual/33-peryferiya-kod.md:272 klas:F -->
### T-33-120 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Де потрібен на інших чипах — зовнішній ЦАП по I²C або згладжений PWM.

**Контекст**

```
## DAC

Більше ніде в лінійці DAC немає (розділ 04). Де потрібен на інших
чипах — зовнішній ЦАП по I²C або згладжений PWM.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-121 sha:d7aa1bdc src:manual/33-peryferiya-kod.md:276 klas:A -->
### T-33-121 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> `GPIO25` і `GPIO26` на S2 **не існують узагалі**: у нього немає пінів 22–25.

**Контекст**

```
## DAC

::: uvaha
`GPIO25` і `GPIO26` на S2 **не існують узагалі**: у нього немає пінів
22–25. Тобто помилитися тут не «майже те саме», а неробочий код і
`ESP_ERR_INVALID_ARG` при налаштуванні.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2}/include/soc/dac_channel.h
- **Дослівно з джерела:**
  > (esp32/dac_channel.h)
  > #define DAC_CHAN0_GPIO_NUM      25
  > #define DAC_CHAN1_GPIO_NUM      26
  > 
  > (esp32s2/dac_channel.h)
  > #define DAC_CHAN0_GPIO_NUM      17
  > #define DAC_CHAN1_GPIO_NUM      18
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка не рецензента, а нового інструмента `tools/pins.py`, який зробили за його зауваженням. Перший же запуск позначив рядок розділу 33: «[[classic]] [[S2]] … на `GPIO25` і `GPIO26`».
Для classic це правда, для S2 — ні двічі: DAC там на `GPIO17`/`GPIO18`, а `GPIO25` у S2 взагалі не існує (маска вирізає 22–25).
Показово, що ця помилка тієї самої природи, що знайдені рецензентом: твердження про два сімейства, вірне для одного. Тобто інструмент ловить саме клас, а не окремий випадок.
- **Прохід:** pass-17-simeystva-proektiv

---

<!-- fc id:T-33-122 sha:fb9fa4e3 src:manual/33-peryferiya-kod.md:277 klas:A -->
### T-33-122 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Тобто помилитися тут не «майже те саме», а неробочий код і `ESP_ERR_INVALID_ARG` при налаштуванні.

**Контекст**

```
## DAC

::: uvaha
`GPIO25` і `GPIO26` на S2 **не існують узагалі**: у нього немає пінів
22–25. Тобто помилитися тут не «майже те саме», а неробочий код і
`ESP_ERR_INVALID_ARG` при налаштуванні.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/app_update/include/esp_ota_ops.h, .../components/esp_common/include/esp_err.h, .../docs/en/api-reference/storage/{wear-levelling,fatfs}.rst
- **Дослівно з джерела:**
  > (esp_ota_ops.h)
  > #define ESP_ERR_OTA_BASE                         0x1500                     /*!< Base error code for ota_ops api */
  > #define ESP_ERR_OTA_PARTITION_CONFLICT           (ESP_ERR_OTA_BASE + 0x01)  /*!< Error if request was to write or erase the current running partition */
  > #define ESP_ERR_OTA_VALIDATE_FAILED              (ESP_ERR_OTA_BASE + 0x03)  /*!< Error if OTA app image is invalid */
  > 
  > (esp_err.h)
  > #define ESP_ERR_INVALID_ARG         0x102
  > 
  > (wear-levelling.rst)
  > The wear levelling component … distributes wear across the whole
  > partition, and is used together with the FAT filesystem via
  > esp_vfs_fat_spiflash_mount_rw_wl.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Усі названі книгою константи існують дослівно. Прохід 7 звіряв виклики; ці — коди повернення, і вони живуть у тих самих заголовках.
Твердження розділу 18 про `wear_levelling` підтверджується від протилежного: у документації FAT монтується через `esp_vfs_fat_spiflash_mount_rw_wl`, тобто саме через шар вирівнювання зносу, — отже сама FAT його не робить, як книга й пише.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-33-123 sha:89f289a2 src:manual/33-peryferiya-kod.md:283 klas:E -->
### T-33-123 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Антидребезг — порівнянням часу, ніколи не затримкою в ISR.

**Контекст**

```
## Що з цього треба запам'ятати

Антидребезг — порівнянням часу, ніколи не затримкою в ISR.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-124 sha:3b0d82f6 src:manual/33-peryferiya-kod.md:285 klas:A -->
### T-33-124 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Яскравість світлодіода нелінійна щодо коефіцієнта заповнення.

**Контекст**

```
## Що з цього треба запам'ятати

Яскравість світлодіода нелінійна щодо коефіцієнта заповнення.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/ledc.rst
- **Дослівно з джерела:**
  > The luminance perceived by human eyes does not have a linear relationship with the PWM duty cycle
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Yaskravlist svitlodioda neliniyna - pidtverdzheno
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-125 sha:d229616c src:manual/33-peryferiya-kod.md:287 klas:E -->
### T-33-125 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Серво живиться окремо; спільна земля обов'язкова.

**Контекст**

```
## Що з цього треба запам'ятати

Серво живиться окремо; спільна земля обов'язкова.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-126 sha:c9c22960 src:manual/33-peryferiya-kod.md:289 klas:F -->
### T-33-126 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> WS2812 керуються через RMT апаратно — у коді це робити не варто.

**Контекст**

```
## Що з цього треба запам'ятати

WS2812 керуються через RMT апаратно — у коді це робити не варто.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-33-127 sha:93141a0c src:manual/33-peryferiya-kod.md:291 klas:A -->
### T-33-127 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> PCNT рахує імпульси без переривань і має апаратний антидребезг.

**Контекст**

```
## Що з цього треба запам'ятати

PCNT рахує імпульси без переривань і має апаратний антидребезг.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/pcnt.rst
- **Дослівно з джерела:**
  > PCNT unit is equipped with a separate glitch filter
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** PCNT rakhuje impulsyuz bez pereryvanny - pidtverdzheno
- **Прохід:** prochid-33-peryferiya-kod

---

<!-- fc id:T-33-128 sha:171ad095 src:manual/33-peryferiya-kod.md:293 klas:A -->
### T-33-128 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> [[classic]] [[S2]] [[S3]] ADC2 не працює при Wi-Fi; ADC потребує калібрування й усереднення.

**Контекст**

```
## Що з цього треба запам'ятати

[[classic]] [[S2]] [[S3]] ADC2 не працює при Wi-Fi; ADC потребує калібрування й
усереднення.
```

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

<!-- fc id:T-33-129 sha:679df6b2 src:manual/33-peryferiya-kod.md:296 klas:E -->
### T-33-129 · proza · `manual/33-peryferiya-kod.md`

**Твердження, коротко**

> Дільник для вимірювання акумулятора розряджає акумулятор.

**Контекст**

```
## Що з цього треба запам'ятати

Дільник для вимірювання акумулятора розряджає акумулятор.
```

**Доказ**

- **Клас:** F — не звірено

---
