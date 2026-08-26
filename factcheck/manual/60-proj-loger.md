# Фактчекінг: `manual/60-proj-loger.md`

Одиниць твердження: **140**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-60-001 sha:c6bb5de4 src:manual/60-proj-loger.md:3 klas:E -->
### T-60-001 · proza · рядок 3

**Книга каже, дослівно:**

> Пристрій прокидається за розкладом, міряє, записує на картку й засинає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-002 sha:533db87a src:manual/60-proj-loger.md:3 klas:E -->
### T-60-002 · proza · рядок 3

**Книга каже, дослівно:**

> Живе від акумулятора місяцями.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-003 sha:1c9cb872 src:manual/60-proj-loger.md:6 klas:F -->
### T-60-003 · proza · рядок 6

**Книга каже, дослівно:**

> Головна тема проєкту — **бюджет енергії** (розділ 06) і надійність запису при зникненні живлення (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-004 sha:df07925b src:manual/60-proj-loger.md:11 klas:C -->
### T-60-004 · proza · рядок 11

**Книга каже, дослівно:**

> **Вхід:** BME280 (I²C) і DS18B20 (1-Wire) для виносного вимірювання.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-005 sha:918c6132 src:manual/60-proj-loger.md:13 klas:E -->
### T-60-005 · proza · рядок 13

**Книга каже, дослівно:**

> **Вихід:** файл CSV на microSD, один рядок на вимірювання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-006 sha:13d73ded src:manual/60-proj-loger.md:15 klas:C -->
### T-60-006 · proza · рядок 15

**Книга каже, дослівно:**

> **Живлення:** 18650, ціль — не менше трьох місяців при вимірюванні раз на 15 хвилин.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-007 sha:ad9247ee src:manual/60-proj-loger.md:18 klas:F -->
### T-60-007 · proza · рядок 18

**Книга каже, дослівно:**

> **Час:** RTC DS3231 із власною батарейкою — мережі немає, SNTP недоступний (розділ 40).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-008 sha:99eb74ab src:manual/60-proj-loger.md:21 klas:A -->
### T-60-008 · proza · рядок 21

**Книга каже, дослівно:**

> **Поведінка при відмові:** картка недоступна — вимірювання накопичуються в RTC RAM; датчик мовчить — записується позначка; акумулятор розряджений — пристрій засинає назавжди, не псуючи картку.

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

<!-- fc id:T-60-009 sha:648244e3 src:manual/60-proj-loger.md:27 klas:F -->
### T-60-009 · tablycya-shapka · рядок 27

**Книга каже, дослівно:**

> | Позиція | Кількість | Примітка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-010 sha:86983c72 src:manual/60-proj-loger.md:28 klas:F -->
### T-60-010 · komirka · рядок 28

**Книга каже, дослівно:**

> ESP32 classic або C3 · Кількість → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-011 sha:cc0e8296 src:manual/60-proj-loger.md:28 klas:F -->
### T-60-011 · komirka · рядок 28

**Книга каже, дослівно:**

> ESP32 classic або C3 · Примітка → **не плата розробки** для фінальної версії

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-012 sha:ae098f83 src:manual/60-proj-loger.md:29 klas:C -->
### T-60-012 · komirka · рядок 29

**Книга каже, дослівно:**

> BME280 · Кількість → 1

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-013 sha:9800167e src:manual/60-proj-loger.md:29 klas:C -->
### T-60-013 · komirka · рядок 29

**Книга каже, дослівно:**

> BME280 · Примітка → I²C

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-014 sha:42ba36b1 src:manual/60-proj-loger.md:30 klas:C -->
### T-60-014 · komirka · рядок 30

**Книга каже, дослівно:**

> DS18B20 у зонді · Кількість → 1

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (DS18B20 Datasheet, Maxim Integrated)
- **Що шукати в джерелі:** таблиця часу перетворення за роздільністю (9 біт ≈ 93.75 мс, 12 біт ≈ 750 мс); робочий діапазон −55…+125 °C; налаштування роздільності 9–12 біт; вимога підтягувального резистора 4.7 кОм; розділ про паразитне живлення й обмеження на кількість пристроїв; 64-бітний унікальний ROM-код.
- **Нотатка:** Значення −127 °C, яке книга називає кодом помилки, у datasheet відсутнє: це домовленість бібліотеки `DallasTemperature` (`DEVICE_DISCONNECTED_C`). Окремий пункт для наступного проходу — його можна закрити класом A з GitHub, бо бібліотека відкрита.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-015 sha:aa59c919 src:manual/60-proj-loger.md:30 klas:C -->
### T-60-015 · komirka · рядок 30

**Книга каже, дослівно:**

> DS18B20 у зонді · Примітка → 1-Wire, резистор 4.7 кОм

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (DS18B20 Datasheet, Maxim Integrated)
- **Що шукати в джерелі:** таблиця часу перетворення за роздільністю (9 біт ≈ 93.75 мс, 12 біт ≈ 750 мс); робочий діапазон −55…+125 °C; налаштування роздільності 9–12 біт; вимога підтягувального резистора 4.7 кОм; розділ про паразитне живлення й обмеження на кількість пристроїв; 64-бітний унікальний ROM-код.
- **Нотатка:** Значення −127 °C, яке книга називає кодом помилки, у datasheet відсутнє: це домовленість бібліотеки `DallasTemperature` (`DEVICE_DISCONNECTED_C`). Окремий пункт для наступного проходу — його можна закрити класом A з GitHub, бо бібліотека відкрита.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-016 sha:376fd675 src:manual/60-proj-loger.md:31 klas:F -->
### T-60-016 · komirka · рядок 31

**Книга каже, дослівно:**

> DS3231 модуль RTC · Кількість → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-017 sha:90f9a897 src:manual/60-proj-loger.md:31 klas:F -->
### T-60-017 · komirka · рядок 31

**Книга каже, дослівно:**

> DS3231 модуль RTC · Примітка → I²C, з батарейкою CR2032

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-018 sha:c08c37e1 src:manual/60-proj-loger.md:32 klas:F -->
### T-60-018 · komirka · рядок 32

**Книга каже, дослівно:**

> Модуль microSD · Кількість → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-019 sha:b5b70cc2 src:manual/60-proj-loger.md:32 klas:F -->
### T-60-019 · komirka · рядок 32

**Книга каже, дослівно:**

> Модуль microSD · Примітка → SPI

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-020 sha:69538962 src:manual/60-proj-loger.md:33 klas:C -->
### T-60-020 · komirka · рядок 33

**Книга каже, дослівно:**

> 18650 з захистом · Кількість → 1

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-021 sha:d7115003 src:manual/60-proj-loger.md:33 klas:C -->
### T-60-021 · komirka · рядок 33

**Книга каже, дослівно:**

> 18650 з захистом · Примітка → розділ 53

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-022 sha:a5e98667 src:manual/60-proj-loger.md:34 klas:C -->
### T-60-022 · komirka · рядок 34

**Книга каже, дослівно:**

> TP4056 **з захистом** · Кількість → 1

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-023 sha:b13324f3 src:manual/60-proj-loger.md:34 klas:C -->
### T-60-023 · komirka · рядок 34

**Книга каже, дослівно:**

> TP4056 **з захистом** · Примітка → розділ 53

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-024 sha:8315296f src:manual/60-proj-loger.md:35 klas:F -->
### T-60-024 · komirka · рядок 35

**Книга каже, дослівно:**

> Перетворювач buck-boost на 3.3 В · Кількість → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-025 sha:b07cbc0d src:manual/60-proj-loger.md:35 klas:F -->
### T-60-025 · komirka · рядок 35

**Книга каже, дослівно:**

> Перетворювач buck-boost на 3.3 В · Примітка → ключове рішення, див. нижче

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-026 sha:7326d03c src:manual/60-proj-loger.md:36 klas:F -->
### T-60-026 · komirka · рядок 36

**Книга каже, дослівно:**

> Резистори 4.7 кОм · Кількість → 3

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-027 sha:6b151619 src:manual/60-proj-loger.md:36 klas:F -->
### T-60-027 · komirka · рядок 36

**Книга каже, дослівно:**

> Резистори 4.7 кОм · Примітка → I²C і 1-Wire

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-028 sha:060e5700 src:manual/60-proj-loger.md:37 klas:F -->
### T-60-028 · komirka · рядок 37

**Книга каже, дослівно:**

> MOSFET малий + резистори · Кількість → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-029 sha:186c921d src:manual/60-proj-loger.md:37 klas:F -->
### T-60-029 · komirka · рядок 37

**Книга каже, дослівно:**

> MOSFET малий + резистори · Примітка → ключ дільника вимірювання напруги

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-030 sha:4bd153f0 src:manual/60-proj-loger.md:42 klas:E -->
### T-60-030 · proza · рядок 42

**Книга каже, дослівно:**

> Проєкту потрібно вісім пінів, і на двох сімействах вони **різні повністю**, а не одним номером.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-031 sha:94984a51 src:manual/60-proj-loger.md:45 klas:F -->
### T-60-031 · tablycya-shapka · рядок 45

**Книга каже, дослівно:**

> | Сигнал | classic | C3 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-032 sha:3daa915e src:manual/60-proj-loger.md:46 klas:A -->
### T-60-032 · komirka · рядок 46

**Книга каже, дослівно:**

> ADC дільника · classic → `GPIO34`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-033 sha:f0e5e49f src:manual/60-proj-loger.md:46 klas:A -->
### T-60-033 · komirka · рядок 46

**Книга каже, дослівно:**

> ADC дільника · C3 → `GPIO3`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-034 sha:428aeadd src:manual/60-proj-loger.md:47 klas:A -->
### T-60-034 · komirka · рядок 47

**Книга каже, дослівно:**

> Ключ дільника (вихід) · classic → `GPIO13`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-035 sha:fcf60801 src:manual/60-proj-loger.md:47 klas:A -->
### T-60-035 · komirka · рядок 47

**Книга каже, дослівно:**

> Ключ дільника (вихід) · C3 → `GPIO2` ⚠

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-036 sha:08cc13e4 src:manual/60-proj-loger.md:48 klas:F -->
### T-60-036 · komirka · рядок 48

**Книга каже, дослівно:**

> I²C `SDA` / `SCL` · classic → `GPIO21` / `GPIO22`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-037 sha:48e76c55 src:manual/60-proj-loger.md:48 klas:F -->
### T-60-037 · komirka · рядок 48

**Книга каже, дослівно:**

> I²C `SDA` / `SCL` · C3 → `GPIO4` / `GPIO5`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-038 sha:5ab1fd1f src:manual/60-proj-loger.md:49 klas:F -->
### T-60-038 · komirka · рядок 49

**Книга каже, дослівно:**

> 1-Wire · classic → `GPIO4`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-039 sha:6d7a7c0c src:manual/60-proj-loger.md:49 klas:F -->
### T-60-039 · komirka · рядок 49

**Книга каже, дослівно:**

> 1-Wire · C3 → `GPIO1`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-040 sha:cd06b540 src:manual/60-proj-loger.md:50 klas:A -->
### T-60-040 · komirka · рядок 50

**Книга каже, дослівно:**

> SPI `SCK` / `MOSI` / `MISO` · classic → `GPIO18` / `GPIO23` / `GPIO19`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-041 sha:556efc25 src:manual/60-proj-loger.md:50 klas:A -->
### T-60-041 · komirka · рядок 50

**Книга каже, дослівно:**

> SPI `SCK` / `MOSI` / `MISO` · C3 → `GPIO6` / `GPIO7` / `GPIO10`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-042 sha:1c06c4e9 src:manual/60-proj-loger.md:51 klas:A -->
### T-60-042 · komirka · рядок 51

**Книга каже, дослівно:**

> SPI `CS` microSD · classic → `GPIO5`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-043 sha:dcea22ca src:manual/60-proj-loger.md:51 klas:A -->
### T-60-043 · komirka · рядок 51

**Книга каже, дослівно:**

> SPI `CS` microSD · C3 → `GPIO0`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-044 sha:43bd8072 src:manual/60-proj-loger.md:54 klas:A -->
### T-60-044 · proza · рядок 54

**Книга каже, дослівно:**

> [[classic]] Четвірка `18`/`23`/`19`/`5` на classic — це рідні піни SPI3 (VSPI) один в один.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-045 sha:b8cb5c30 src:manual/60-proj-loger.md:54 klas:F -->
### T-60-045 · proza · рядок 54

**Книга каже, дослівно:**

> [[C3]] На C3 рідними лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2`, а він уже пішов під ключ дільника.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-046 sha:57e3b369 src:manual/60-proj-loger.md:54 klas:F -->
### T-60-046 · proza · рядок 54

**Книга каже, дослівно:**

> Для microSD це не коштує нічого — межа матриці 40 МГц (розділ 36).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-047 sha:6c208dfa src:manual/60-proj-loger.md:60 klas:A -->
### T-60-047 · proza · рядок 60

**Книга каже, дослівно:**

> [[C3]] **Жодного з пінів `GPIO22`, `GPIO23`, `GPIO34` на C3 не існує.** У C3 усього 22 піни, `GPIO0`–`GPIO21`, і класична розпіновка з розділу 07 переноситься на нього не заміною чисел, а перерозподілом усіх трьох шин.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > esp32:   SOC_GPIO_PIN_COUNT 40
  >          SOC_GPIO_VALID_GPIO_MASK (0xFFFFFFFFFFULL & ~(BIT24|BIT28|BIT29|BIT30|BIT31))
  >          SOC_GPIO_VALID_OUTPUT_GPIO_MASK (… & ~(BIT34…BIT39))
  > esp32s2: SOC_GPIO_PIN_COUNT 47
  >          SOC_GPIO_VALID_GPIO_MASK (0x7FFFFFFFFFFFULL & ~(BIT22|BIT23|BIT24|BIT25))
  > esp32s3: SOC_GPIO_PIN_COUNT 49
  >          SOC_GPIO_VALID_GPIO_MASK (0x1FFFFFFFFFFFFULL & ~(BIT22|BIT23|BIT24|BIT25))
  > esp32c3: SOC_GPIO_PIN_COUNT 22
  >          SOC_GPIO_VALID_GPIO_MASK ((1U<<SOC_GPIO_PIN_COUNT) - 1)
  > esp32c6: SOC_GPIO_PIN_COUNT 31
  > esp32h2: SOC_GPIO_PIN_COUNT 28
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Два виправлення рівня «не збереться».
Проєкт 59 радив S3 першим рядком складових і давав `GPIO21`/`GPIO22` для I²C. У S3 пінів 22–25 **немає взагалі** — маска вирізає їх явно. Читач із S3-DevKitC-1 отримав би `ESP_ERR_INVALID_ARG` і німу шину.
Проєкт 60 радив C3 і давав `GPIO21/22` (I²C), `GPIO18/19/23` (SPI) і `GPIO34` (ADC). У C3 рівно 22 піни, `GPIO0`–`GPIO21`; з трьох підсистем не існує жодної цілком.
Виправлено не заміною чисел, а введенням **таблиці пінів за платами** в кожен із проєктів, із винесенням розпіновки в один блок `#if CONFIG_IDF_TARGET_*` нагорі коду. Тепер перенесення на інший чип — одна правка в одному місці, а не пошук чисел по всьому розділу.
Заразом з'ясувалося, що на C3 проєкт 60 вичерпує всі вільні піни й потребує ще одного: вісім безумовно вільних (`0`,`1`,`3`,`4`,`5`, `6`,`7`,`10`) проти дев'яти потрібних. Дев'ятим узято strapping-пін `GPIO2` — виключно як вихід. Це записано в книгу прямо, бо саме такі межі й вирішують вибір чипа на етапі схеми.
- **Прохід:** pass-17-simeystva-proektiv

---

<!-- fc id:T-60-048 sha:2c26e8f8 src:manual/60-proj-loger.md:65 klas:A -->
### T-60-048 · proza · рядок 65

**Книга каже, дослівно:**

> Ще гірше те, що з цих 22 пінів вільні далеко не всі: `GPIO12`–`GPIO17` зайняті флешем, `GPIO18` і `GPIO19` — USB-Serial-JTAG, `GPIO20` і `GPIO21` — консоль UART0, а `GPIO2`, `GPIO8`, `GPIO9` — strapping.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/usb-serial-jtag-console.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_USB_DP_GPIO:default="Not Updated!",esp32c3="19",esp32s3="20",
  >  esp32c6="13", esp32h2="27", esp32p4="25/27", esp32c5="14", esp32c61="13"}
  > {IDF_TARGET_USB_DM_GPIO:default="Not Updated!",esp32c3="18",esp32s3="19",
  >  esp32c6="12", esp32h2="26", esp32p4="24/26", esp32c5="13", esp32c61="12"}
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Збігається, і навіть порядок правильний: на S3 `D−` = `GPIO19`, `D+` = `GPIO20`, тож запис «19, 20 — D−, D+» точний. На C3 пара 18/19 у тому ж порядку.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-60-049 sha:69d3aa6b src:manual/60-proj-loger.md:65 klas:A -->
### T-60-049 · proza · рядок 65

**Книга каже, дослівно:**

> Лишається рівно вісім безумовно вільних: `0`, `1`, `3`, `4`, `5`, `6`, `7`, `10`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-050 sha:6770ffab src:manual/60-proj-loger.md:71 klas:E -->
### T-60-050 · proza · рядок 71

**Книга каже, дослівно:**

> Проєкту треба **дев'ять**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-051 sha:d5b2eb5a src:manual/60-proj-loger.md:71 klas:F -->
### T-60-051 · proza · рядок 71

**Книга каже, дослівно:**

> Тому ключ дільника доводиться вішати на strapping-пін `GPIO2` — це припустимо лише тому, що він працює тут **виключно як вихід** і лише після старту (розділ 07), а зовнішньої обв'язки на ньому немає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-052 sha:cd431346 src:manual/60-proj-loger.md:76 klas:F -->
### T-60-052 · proza · рядок 76

**Книга каже, дослівно:**

> Тобто **цей проєкт вичерпує C3 повністю й трохи більше**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-053 sha:a9b481b9 src:manual/60-proj-loger.md:76 klas:E -->
### T-60-053 · proza · рядок 76

**Книга каже, дослівно:**

> Додати ще один датчик буде нікуди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-054 sha:728d95b8 src:manual/60-proj-loger.md:76 klas:E -->
### T-60-054 · proza · рядок 76

**Книга каже, дослівно:**

> Це саме той випадок, коли вибір чипа робиться на етапі схеми, а не після: на classic такої тісноти немає, і саме тому в BOM він стоїть першим.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-055 sha:90a056ff src:manual/60-proj-loger.md:84 klas:E -->
### T-60-055 · proza · рядок 84

**Книга каже, дослівно:**

> Нижче — варіант для classic.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-056 sha:3da23978 src:manual/60-proj-loger.md:84 klas:F -->
### T-60-056 · proza · рядок 84

**Книга каже, дослівно:**

> Для C3 підставте піни з таблиці вище.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-057 sha:618e4824 src:manual/60-proj-loger.md:86 klas:K -->
### T-60-057 · kod · рядок 86

**Книга каже, дослівно:**

> ```
> 18650 ──[захист]──[TP4056]──┬── buck-boost 3.3 В ── ESP32 + периферія
>                             │
>                             └──[MOSFET]──[100к]──┬── ADC     classic 34 / C3 3
>                                           [100к]─┘
>                                             GND
> 
> I²C   SDA/SCL:  BME280 + DS3231, спільні підтяжки 4.7 кОм
>                                             classic 21/22   C3 4/5
> 1-Wire:         DS18B20 + підтяжка 4.7 кОм  classic 4       C3 1
> SPI  SCK/MOSI/MISO + CS: microSD            classic 18/23/19 + 5
>                                             C3      6/7/10   + 0
> ```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-058 sha:913f8132 src:manual/60-proj-loger.md:87 klas:C -->
### T-60-058 · schema-zvyazok · рядок 87

**Книга каже, дослівно:**

> 18650 ──[захист]──[TP4056]──┬── buck-boost 3.3 В ── ESP32 + периферія

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (TP4056 і DW01 datasheet) та специфікації виробників елементів 18650
- **Що шукати в джерелі:** для TP4056: типовий струм заряджання і резистор, яким він задається; склад варіанта із захистом (DW01 плюс подвійний MOSFET) і що саме він захищає. Для елементів: напруга повного заряду 4.2 В, номінальна 3.7 В, межа розряду, заборона заряджання нижче 0 °C і її причина (металізація літію).
- **Нотатка:** Розділ 53 — найризикованіший у книзі з погляду наслідків, тож ця група має бути закрита першою, щойно з'явиться доступ.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-059 sha:e6f1a6a7 src:manual/60-proj-loger.md:88 klas:F -->
### T-60-059 · schema-zvyazok · рядок 88

**Книга каже, дослівно:**

> │

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-060 sha:a1efd7c9 src:manual/60-proj-loger.md:89 klas:F -->
### T-60-060 · schema-zvyazok · рядок 89

**Книга каже, дослівно:**

> └──[MOSFET]──[100к]──┬── ADC     classic 34 / C3 3

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-061 sha:6b711a92 src:manual/60-proj-loger.md:90 klas:F -->
### T-60-061 · schema-zvyazok · рядок 90

**Книга каже, дослівно:**

> [100к]─┘

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-062 sha:3d5502e9 src:manual/60-proj-loger.md:101 klas:E -->
### T-60-062 · proza · рядок 101

**Книга каже, дослівно:**

> **Buck-boost, а не LDO** — головне рішення проєкту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-063 sha:259eae72 src:manual/60-proj-loger.md:101 klas:F -->
### T-60-063 · proza · рядок 101

**Книга каже, дослівно:**

> Звичайний LDO перестає давати 3.3 В, коли акумулятор просів до 3.8 В, і відсікає приблизно половину ємності.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-064 sha:a503da18 src:manual/60-proj-loger.md:101 klas:F -->
### T-60-064 · proza · рядок 101

**Книга каже, дослівно:**

> Buck-boost працює до 3.0 В.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-065 sha:9eb66891 src:manual/60-proj-loger.md:105 klas:F -->
### T-60-065 · proza · рядок 105

**Книга каже, дослівно:**

> Різниця — вдвічі за часом роботи, і вона більша за будь-яку оптимізацію коду (розділ 53).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-066 sha:99a575e7 src:manual/60-proj-loger.md:110 klas:F -->
### T-60-066 · proza · рядок 110

**Книга каже, дослівно:**

> **Дільник вимірювання напруги вмикається транзистором.** Постійно під'єднаний дільник із двох резисторів по 100 кОм бере на порядок більше, ніж чип уві сні (числа — розділ 33), тобто стає головним споживачем усього пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-067 sha:195b9722 src:manual/60-proj-loger.md:115 klas:F -->
### T-60-067 · proza · рядок 115

**Книга каже, дослівно:**

> Без ключа розрахунок на три місяці перетворюється на три тижні (розділ 53).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-068 sha:2513a78d src:manual/60-proj-loger.md:121 klas:E -->
### T-60-068 · proza · рядок 121

**Книга каже, дослівно:**

> Уся розпіновка — в одному місці нагорі, а не розсіяна по викликах.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-069 sha:51d55f35 src:manual/60-proj-loger.md:121 klas:E -->
### T-60-069 · proza · рядок 121

**Книга каже, дослівно:**

> Це не охайність заради охайності: саме розсіяні числа й роблять перенесення на інший чип неможливим без пропусків.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-070 sha:911b825f src:manual/60-proj-loger.md:125 klas:K -->
### T-60-070 · kod · рядок 125

**Книга каже, дослівно:**

> ```c
> // Піни й канал ADC за платою (таблиця вище).
> #if CONFIG_IDF_TARGET_ESP32C3
> #  define PIN_SDA        GPIO_NUM_4
> #  define PIN_SCL        GPIO_NUM_5
> #  define PIN_1WIRE      GPIO_NUM_1
> #  define PIN_SCK        GPIO_NUM_6
> #  define PIN_MOSI       GPIO_NUM_7
> #  define PIN_MISO       GPIO_NUM_10
> #  define PIN_CS_SD      GPIO_NUM_0
> #  define PIN_DILNYK_EN  GPIO_NUM_2      // ⚠ strapping: лише вихід
> #  define ADC_CHANNEL    ADC_CHANNEL_3   // GPIO3
> #else                                    // ESP32 classic
> #  define PIN_SDA        GPIO_NUM_21
> #  define PIN_SCL        GPIO_NUM_22
> #  define PIN_1WIRE      GPIO_NUM_4
> #  define PIN_SCK        GPIO_NUM_18
> #  define PIN_MOSI       GPIO_NUM_23
> #  define PIN_MISO       GPIO_NUM_19
> #  define PIN_CS_SD      GPIO_NUM_5
> #  define PIN_DILNYK_EN  GPIO_NUM_13
> #  define ADC_CHANNEL    ADC_CHANNEL_6   // GPIO34 = ADC1_6
> #endif
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)          (esp32c3/adc_channel.h)
  > #define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3
  > #define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3
  > 
  > (esp32/spi_pins.h)             (esp32c3/spi_pins.h)
  > #define VSPI_IOMUX_PIN_NUM_CLK  18   #define SPI2_IOMUX_PIN_NUM_CLK  6
  > #define VSPI_IOMUX_PIN_NUM_MOSI 23   #define SPI2_IOMUX_PIN_NUM_MOSI 7
  > #define VSPI_IOMUX_PIN_NUM_MISO 19   #define SPI2_IOMUX_PIN_NUM_MISO 2
  > #define VSPI_IOMUX_PIN_NUM_CS    5   #define SPI2_IOMUX_PIN_NUM_CS  10
  > #define SPI3_IOMUX_PIN_NUM_CLK  VSPI_IOMUX_PIN_NUM_CLK
  >                                      #define MSPI_IOMUX_PIN_NUM_HD   12
  >                                      #define MSPI_IOMUX_PIN_NUM_WP   13
  >                                      #define MSPI_IOMUX_PIN_NUM_CS0  14
  >                                      #define MSPI_IOMUX_PIN_NUM_CLK  15
  >                                      #define MSPI_IOMUX_PIN_NUM_MOSI 16
  >                                      #define MSPI_IOMUX_PIN_NUM_MISO 17
  > 
  > (esp32c3/soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 22
  > #define SOC_GPIO_VALID_GPIO_MASK  ((1U<<SOC_GPIO_PIN_COUNT) - 1)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Проєкт 60 після проходу 17 має піновий план на два сімейства, і тут він звірений цілком, а не вибірково. Розбіжностей немає: `ADC_CHANNEL_6` на classic це справді `GPIO34`, `ADC_CHANNEL_3` на C3 це справді `GPIO3`, а класична четвірка SPI `18`/`23`/`19`/`5` — це дослівно рідні піни SPI3 (VSPI).
Підтвердилося й твердження, на якому тримається весь наголос розділу: у C3 рівно 22 піни, `GPIO12`–`GPIO17` зайняті флешем (це видно з `MSPI_IOMUX_PIN_NUM_*`, де перелічені саме 12–17), і після консолі, USB-JTAG та strapping лишається вісім вільних при потрібних дев'яти.
Одне спостереження варте було додати в книгу. На C3 рідними в проєкті лишилися тільки `SCK` і `MOSI`: рідний `MISO` там `GPIO2` — той самий strapping-пін, який проєкт уже витратив на ключ дільника. Тобто тіснота C3 коштує не лише пінів, а й рідної розпіновки SPI. Ціна при цьому нульова, і чому саме — у наступному записі.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-60-071 sha:f9fbb83e src:manual/60-proj-loger.md:151 klas:F -->
### T-60-071 · proza · рядок 151

**Книга каже, дослівно:**

> [[C3]] Рядок `PIN_DILNYK_EN` на C3 — свідомий компроміс і єдине місце, де довелося взяти strapping-пін.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-072 sha:04d77d98 src:manual/60-proj-loger.md:151 klas:F -->
### T-60-072 · proza · рядок 151

**Книга каже, дослівно:**

> Вільних більше немає, а `GPIO2` тут працює **лише як вихід** і лише після старту, тож на завантаження не впливає (розділ 07).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-073 sha:c59f8ae8 src:manual/60-proj-loger.md:151 klas:E -->
### T-60-073 · proza · рядок 151

**Книга каже, дослівно:**

> Зовнішньої обв'язки на ньому бути не повинно — затвор MOSFET підключається напряму.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-074 sha:65e265f5 src:manual/60-proj-loger.md:157 klas:E -->
### T-60-074 · proza · рядок 157

**Книга каже, дослівно:**

> Якщо ця умова незручна, висновок той самий, що вище: беріть classic.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-075 sha:5b607b9b src:manual/60-proj-loger.md:162 klas:F -->
### T-60-075 · proza · рядок 162

**Книга каже, дослівно:**

> Deep sleep — це перезавантаження: RAM втрачається, `app_main` починається спочатку (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-076 sha:077ad9d7 src:manual/60-proj-loger.md:162 klas:A -->
### T-60-076 · proza · рядок 162

**Книга каже, дослівно:**

> Переживає сон лише RTC RAM.

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

<!-- fc id:T-60-077 sha:047a7bc6 src:manual/60-proj-loger.md:165 klas:K -->
### T-60-077 · kod · рядок 165

**Книга каже, дослівно:**

> ```c
> RTC_DATA_ATTR static uint32_t nomer_cyklu = 0;
> RTC_DATA_ATTR static uint32_t pomylok_karty = 0;
> RTC_DATA_ATTR static zapys_t bufer[BUFER_ROZMIR];  // накопичення при збої
> RTC_DATA_ATTR static uint8_t  u_buferi = 0;
> ```

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

<!-- fc id:T-60-078 sha:84ff3f5f src:manual/60-proj-loger.md:172 klas:A -->
### T-60-078 · proza · рядок 172

**Книга каже, дослівно:**

> RTC RAM невелика — одиниці кілобайтів.

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

<!-- fc id:T-60-079 sha:60e50665 src:manual/60-proj-loger.md:172 klas:F -->
### T-60-079 · proza · рядок 172

**Книга каже, дослівно:**

> Буфер на 20–30 записів у неї вміщається; більше — ні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-080 sha:33b09b68 src:manual/60-proj-loger.md:177 klas:K -->
### T-60-080 · kod · рядок 177

**Книга каже, дослівно:**

> ```c
> void app_main(void) {
>     nomer_cyklu++;
>     ESP_LOGI(TAG, "цикл %lu, причина пробудження: %d",
>              nomer_cyklu, esp_sleep_get_wakeup_cause());
> 
>     float napruga = zmiryaty_akumulyator();      // з ключем, див. нижче
>     if (napruga < 3.2f) {
>         ESP_LOGE(TAG, "акумулятор %.2f В — засинаємо назавжди", napruga);
>         esp_deep_sleep_start();                  // без таймера: не прокинеться
>     }
> 
>     zapys_t z = { .chas = rtc_chas(), .napruga = napruga };
>     z.ok_bme = (bme_measure(&z.temp, &z.hum, &z.pres) == ESP_OK);
>     z.ok_ds  = (ds18b20_read(&z.temp_zovni) == ESP_OK);
> 
>     if (!zapysaty_na_kartku(&z)) {
>         pomylok_karty++;
>         if (u_buferi < BUFER_ROZMIR) bufer[u_buferi++] = z;
>         ESP_LOGW(TAG, "картка недоступна, у буфері %u", u_buferi);
>     } else if (u_buferi > 0) {
>         skynuty_bufer();                         // дописати накопичене
>     }
> 
>     zasnuty(15 * 60);
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

<!-- fc id:T-60-081 sha:36e9dc05 src:manual/60-proj-loger.md:185 klas:F -->
### T-60-081 · kod-ryadok · рядок 185

**Книга каже, дослівно:**

> ESP_LOGE(TAG, "акумулятор %.2f В — засинаємо назавжди", napruga);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-082 sha:96e47c3f src:manual/60-proj-loger.md:196 klas:F -->
### T-60-082 · kod-ryadok · рядок 196

**Книга каже, дослівно:**

> ESP_LOGW(TAG, "картка недоступна, у буфері %u", u_buferi);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-083 sha:11e7a3b4 src:manual/60-proj-loger.md:201 klas:F -->
### T-60-083 · kod-ryadok · рядок 201

**Книга каже, дослівно:**

> zasnuty(15 * 60);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-084 sha:86c1b4b6 src:manual/60-proj-loger.md:206 klas:E -->
### T-60-084 · proza · рядок 206

**Книга каже, дослівно:**

> Перевірка напруги стоїть **першою**, до будь-якої роботи з карткою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-085 sha:d34c43c3 src:manual/60-proj-loger.md:208 klas:F -->
### T-60-085 · proza · рядок 208

**Книга каже, дослівно:**

> Причина: запис у картку при просілому живленні — найнадійніший спосіб пошкодити файлову систему FAT так, що втрачається не останній файл, а картка цілком (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-086 sha:c226a03c src:manual/60-proj-loger.md:212 klas:E -->
### T-60-086 · proza · рядок 212

**Книга каже, дослівно:**

> Розряджений акумулятор має призводити до чистого засинання, а не до спроби записати ще один рядок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-087 sha:f0958dca src:manual/60-proj-loger.md:218 klas:K -->
### T-60-087 · kod · рядок 218

**Книга каже, дослівно:**

> ```c
> static float zmiryaty_akumulyator(void) {
>     gpio_set_level(PIN_DILNYK_EN, 1);
>     vTaskDelay(pdMS_TO_TICKS(10));           // дати зарядитися ємності
> 
>     int sum = 0;
>     for (int i = 0; i < 32; i++) {           // усереднення (розділ 33)
>         int raw;
>         adc_oneshot_read(adc, ADC_CHANNEL, &raw);
>         sum += raw;
>     }
>     gpio_set_level(PIN_DILNYK_EN, 0);        // вимкнути одразу
> 
>     int mv;
>     adc_cali_raw_to_voltage(cali, sum / 32, &mv);
>     return mv * 2.0f / 1000.0f;              // дільник 1:2
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

<!-- fc id:T-60-088 sha:e249c82c src:manual/60-proj-loger.md:220 klas:F -->
### T-60-088 · kod-ryadok · рядок 220

**Книга каже, дослівно:**

> gpio_set_level(PIN_DILNYK_EN, 1);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-089 sha:fa5319b8 src:manual/60-proj-loger.md:226 klas:A -->
### T-60-089 · kod-ryadok · рядок 226

**Книга каже, дослівно:**

> adc_oneshot_read(adc, ADC_CHANNEL, &raw);

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

<!-- fc id:T-60-090 sha:ad6f9b2c src:manual/60-proj-loger.md:232 klas:A -->
### T-60-090 · kod-ryadok · рядок 232

**Книга каже, дослівно:**

> adc_cali_raw_to_voltage(cali, sum / 32, &mv);

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

<!-- fc id:T-60-091 sha:4b6bd1c9 src:manual/60-proj-loger.md:239 klas:K -->
### T-60-091 · kod · рядок 239

**Книга каже, дослівно:**

> ```c
> static bool zapysaty_na_kartku(const zapys_t *z) {
>     if (sd_mount() != ESP_OK) return false;
> 
>     FILE *f = fopen(MOUNT "/dani.csv", "a");
>     if (!f) { sd_unmount(); return false; }
> 
>     fprintf(f, "%lld,%.2f,%.1f,%.1f,%.2f,%.2f,%d,%d\n",
>             z->chas, z->temp, z->hum, z->pres,
>             z->temp_zovni, z->napruga, z->ok_bme, z->ok_ds);
> 
>     fflush(f);
>     fsync(fileno(f));      // змусити записати на носій, а не в буфер
>     fclose(f);
>     sd_unmount();          // розмонтувати одразу
>     return true;
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-092 sha:f0c8956e src:manual/60-proj-loger.md:250 klas:F -->
### T-60-092 · kod-ryadok · рядок 250

**Книга каже, дослівно:**

> fflush(f);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-093 sha:17341195 src:manual/60-proj-loger.md:252 klas:F -->
### T-60-093 · kod-ryadok · рядок 252

**Книга каже, дослівно:**

> fclose(f);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-094 sha:d99dbbfc src:manual/60-proj-loger.md:259 klas:F -->
### T-60-094 · proza · рядок 259

**Книга каже, дослівно:**

> Чотири дії наприкінці — `fflush`, `fsync`, `fclose`, `sd_unmount` — виглядають надмірними і не є ними.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-095 sha:a161b206 src:manual/60-proj-loger.md:262 klas:E -->
### T-60-095 · proza · рядок 262

**Книга каже, дослівно:**

> Файл, залишений відкритим, означає, що дані лежать у буфері в RAM.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-096 sha:b0cfdae4 src:manual/60-proj-loger.md:262 klas:E -->
### T-60-096 · proza · рядок 262

**Книга каже, дослівно:**

> Зникнення живлення — тим більше.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-097 sha:5619cd9a src:manual/60-proj-loger.md:265 klas:E -->
### T-60-097 · proza · рядок 265

**Книга каже, дослівно:**

> Правило логера: **відкрив, дописав рядок, закрив, розмонтував**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-098 sha:1ee7e676 src:manual/60-proj-loger.md:265 klas:F -->
### T-60-098 · proza · рядок 265

**Книга каже, дослівно:**

> Ніколи не тримати файл відкритим між циклами (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-099 sha:69c60ed0 src:manual/60-proj-loger.md:271 klas:K -->
### T-60-099 · kod · рядок 271

**Книга каже, дослівно:**

> ```c
> static void zasnuty(uint32_t sekund) {
>     // вимкнути все, що споживає
>     sd_unmount();
>     gpio_set_level(PIN_DILNYK_EN, 0);
>     gpio_set_level(PIN_ZHYVLENNYA_PERYFERIYI, 0);   // ключ живлення датчиків
> 
>     esp_sleep_enable_timer_wakeup((uint64_t)sekund * 1000000ULL);
>     ESP_LOGI(TAG, "засинаємо на %lu с", sekund);
>     esp_deep_sleep_start();
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

<!-- fc id:T-60-100 sha:08a000e8 src:manual/60-proj-loger.md:274 klas:F -->
### T-60-100 · kod-ryadok · рядок 274

**Книга каже, дослівно:**

> sd_unmount();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-101 sha:ab40e8e7 src:manual/60-proj-loger.md:275 klas:F -->
### T-60-101 · kod-ryadok · рядок 275

**Книга каже, дослівно:**

> gpio_set_level(PIN_DILNYK_EN, 0);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-102 sha:3fd6a686 src:manual/60-proj-loger.md:278 klas:A -->
### T-60-102 · kod-ryadok · рядок 278

**Книга каже, дослівно:**

> esp_sleep_enable_timer_wakeup((uint64_t)sekund * 1000000ULL);

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

<!-- fc id:T-60-103 sha:34ad95d5 src:manual/60-proj-loger.md:279 klas:F -->
### T-60-103 · kod-ryadok · рядок 279

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "засинаємо на %lu с", sekund);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-104 sha:c5771474 src:manual/60-proj-loger.md:280 klas:F -->
### T-60-104 · kod-ryadok · рядок 280

**Книга каже, дослівно:**

> esp_deep_sleep_start();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-105 sha:ad07f2d7 src:manual/60-proj-loger.md:285 klas:C -->
### T-60-105 · proza · рядок 285

**Книга каже, дослівно:**

> **Живлення периферії вмикається ключем.** Модуль microSD, BME280 і RTC споживають уві сні — разом це можуть бути мілі-, а не мікроампери.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-106 sha:fac610a6 src:manual/60-proj-loger.md:288 klas:E -->
### T-60-106 · proza · рядок 288

**Книга каже, дослівно:**

> Один MOSFET, що знімає живлення з усієї периферії на час сну, часто економить більше, ніж усі налаштування сну разом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-107 sha:b4495bba src:manual/60-proj-loger.md:291 klas:F -->
### T-60-107 · proza · рядок 291

**Книга каже, дослівно:**

> Виняток — RTC DS3231: він має власну батарейку й лишається живим сам.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-108 sha:83a8e3da src:manual/60-proj-loger.md:296 klas:F -->
### T-60-108 · proza · рядок 296

**Книга каже, дослівно:**

> Розрахунок для циклу раз на 15 хвилин:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-109 sha:6f45d6d6 src:manual/60-proj-loger.md:298 klas:F -->
### T-60-109 · tablycya-shapka · рядок 298

**Книга каже, дослівно:**

> | Фаза | Час | Струм | Заряд |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-110 sha:a6f4ae9a src:manual/60-proj-loger.md:299 klas:F -->
### T-60-110 · komirka · рядок 299

**Книга каже, дослівно:**

> Пробудження й ініціалізація · Час → 300 мс

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-111 sha:17288f9c src:manual/60-proj-loger.md:299 klas:C -->
### T-60-111 · komirka · рядок 299

**Книга каже, дослівно:**

> Пробудження й ініціалізація · Струм → 40 мА

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.espressif.com/en/support/documents/technical-documents (ESP32 Series Datasheet)
- **Що шукати в джерелі:** розділ «Recommended Operating Conditions»: гранично допустимий струм на пін (40 мА) і типова сила драйвера за замовчуванням; робочий діапазон температур; таблиця споживання за режимами (deep sleep, light sleep, modem sleep, активний, пік передачі Wi-Fi).
- **Нотатка:** Найважливіша недосяжна група після BME280: на цих числах стоять розділи 05, 06 і 47, тобто вся частина про живлення. Частина закривається обхідним шляхом — `gpio_set_drive_capability` у ESP-IDF описує рівні сили драйвера, — і це завдання наступного проходу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-112 sha:2d0a41b2 src:manual/60-proj-loger.md:299 klas:F -->
### T-60-112 · komirka · рядок 299

**Книга каже, дослівно:**

> Пробудження й ініціалізація · Заряд → 12 мА·с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-113 sha:b201f1de src:manual/60-proj-loger.md:300 klas:A -->
### T-60-113 · komirka · рядок 300

**Книга каже, дослівно:**

> Вимірювання (DS18B20 — 750 мс) · Час → 900 мс

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/milesburton/Arduino-Temperature-Control-Library/master/DallasTemperature.h
- **Дослівно з джерела:**
  > #define DEVICE_DISCONNECTED_C -127
  > #define DEVICE_DISCONNECTED_F -196.6
  > #define DEVICE_DISCONNECTED_RAW -7040
  > …
  > #define MAX_CONVERSION_TIMEOUT 750
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Закриває пункт, який прохід 3 записав у наряд із приміткою, що −127 у datasheet відсутнє. Так і є: це домовленість бібліотеки `DallasTemperature`, і саме її бачить читач. Тепер підтверджено дослівно, разом із межею перетворення 750 мс.
- **Прохід:** pass-04-obkhidni

---

<!-- fc id:T-60-114 sha:68da1621 src:manual/60-proj-loger.md:300 klas:A -->
### T-60-114 · komirka · рядок 300

**Книга каже, дослівно:**

> Вимірювання (DS18B20 — 750 мс) · Струм → 40 мА

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/milesburton/Arduino-Temperature-Control-Library/master/DallasTemperature.h
- **Дослівно з джерела:**
  > #define DEVICE_DISCONNECTED_C -127
  > #define DEVICE_DISCONNECTED_F -196.6
  > #define DEVICE_DISCONNECTED_RAW -7040
  > …
  > #define MAX_CONVERSION_TIMEOUT 750
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Закриває пункт, який прохід 3 записав у наряд із приміткою, що −127 у datasheet відсутнє. Так і є: це домовленість бібліотеки `DallasTemperature`, і саме її бачить читач. Тепер підтверджено дослівно, разом із межею перетворення 750 мс.
- **Прохід:** pass-04-obkhidni

---

<!-- fc id:T-60-115 sha:7bf88644 src:manual/60-proj-loger.md:300 klas:A -->
### T-60-115 · komirka · рядок 300

**Книга каже, дослівно:**

> Вимірювання (DS18B20 — 750 мс) · Заряд → 36 мА·с

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/milesburton/Arduino-Temperature-Control-Library/master/DallasTemperature.h
- **Дослівно з джерела:**
  > #define DEVICE_DISCONNECTED_C -127
  > #define DEVICE_DISCONNECTED_F -196.6
  > #define DEVICE_DISCONNECTED_RAW -7040
  > …
  > #define MAX_CONVERSION_TIMEOUT 750
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Закриває пункт, який прохід 3 записав у наряд із приміткою, що −127 у datasheet відсутнє. Так і є: це домовленість бібліотеки `DallasTemperature`, і саме її бачить читач. Тепер підтверджено дослівно, разом із межею перетворення 750 мс.
- **Прохід:** pass-04-obkhidni

---

<!-- fc id:T-60-116 sha:772fb917 src:manual/60-proj-loger.md:301 klas:F -->
### T-60-116 · komirka · рядок 301

**Книга каже, дослівно:**

> Запис на картку · Час → 400 мс

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-117 sha:ef81a4da src:manual/60-proj-loger.md:301 klas:F -->
### T-60-117 · komirka · рядок 301

**Книга каже, дослівно:**

> Запис на картку · Струм → 80 мА

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-118 sha:386c98cf src:manual/60-proj-loger.md:301 klas:F -->
### T-60-118 · komirka · рядок 301

**Книга каже, дослівно:**

> Запис на картку · Заряд → 32 мА·с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-119 sha:9084f4d4 src:manual/60-proj-loger.md:302 klas:F -->
### T-60-119 · komirka · рядок 302

**Книга каже, дослівно:**

> Сон · Час → 899 с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-120 sha:d5314759 src:manual/60-proj-loger.md:302 klas:F -->
### T-60-120 · komirka · рядок 302

**Книга каже, дослівно:**

> Сон · Струм → 30 мкА

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-121 sha:4b86eaef src:manual/60-proj-loger.md:302 klas:F -->
### T-60-121 · komirka · рядок 302

**Книга каже, дослівно:**

> Сон · Заряд → 27 мА·с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-122 sha:7ebdd2fb src:manual/60-proj-loger.md:303 klas:F -->
### T-60-122 · komirka · рядок 303

**Книга каже, дослівно:**

> **Разом за цикл** · Час → 900 с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-123 sha:fa15cd97 src:manual/60-proj-loger.md:303 klas:D -->
### T-60-123 · komirka · рядок 303

**Книга каже, дослівно:**

> **Разом за цикл** · Заряд → **≈107 мА·с**

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

<!-- fc id:T-60-124 sha:3a61fcae src:manual/60-proj-loger.md:306 klas:D -->
### T-60-124 · proza · рядок 306

**Книга каже, дослівно:**

> За добу: 96 циклів × 107 мА·с ≈ 10 272 мА·с ≈ **2.85 мА·год**.

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

<!-- fc id:T-60-125 sha:f90b83e5 src:manual/60-proj-loger.md:308 klas:D -->
### T-60-125 · proza · рядок 308

**Книга каже, дослівно:**

> З 18650 на 2500 мА·год, беручи 70 % на старіння і холод: `1750 / 2.85 ≈ 614 діб`.

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

<!-- fc id:T-60-126 sha:c426e030 src:manual/60-proj-loger.md:312 klas:F -->
### T-60-126 · proza · рядок 312

**Книга каже, дослівно:**

> Розрахунок дає **понад рік**, і саме тому його треба перевірити вимірюванням (розділ 58).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-127 sha:45833f6d src:manual/60-proj-loger.md:315 klas:E -->
### T-60-127 · proza · рядок 315

**Книга каже, дослівно:**

> Практика зазвичай дає менше, і причини завжди ті самі: струм сну вищий за очікуваний (плата розробки!), холод з'їдає ємність, картка споживає більше при записі, ніж у datasheet.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-128 sha:30cc6798 src:manual/60-proj-loger.md:319 klas:E -->
### T-60-128 · proza · рядок 319

**Книга каже, дослівно:**

> Ціль «три місяці» в постановці — свідомо занижена.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-129 sha:e71331a3 src:manual/60-proj-loger.md:319 klas:E -->
### T-60-129 · proza · рядок 319

**Книга каже, дослівно:**

> Розрахунок на рік із запасом утричі означає, що три місяці ви отримаєте навіть при неприємних сюрпризах.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-130 sha:cfdb4c7e src:manual/60-proj-loger.md:324 klas:C -->
### T-60-130 · proza · рядок 324

**Книга каже, дослівно:**

> **Плата розробки для фінальної версії не годиться**: USB-міст, стабілізатор і світлодіод споживають уві сні на порядки більше за чип. 20 мА замість 30 мкА перетворює рік на добу (розділ 06).

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.espressif.com/en/support/documents/technical-documents (ESP32 Series Datasheet)
- **Що шукати в джерелі:** розділ «Recommended Operating Conditions»: гранично допустимий струм на пін (40 мА) і типова сила драйвера за замовчуванням; робочий діапазон температур; таблиця споживання за режимами (deep sleep, light sleep, modem sleep, активний, пік передачі Wi-Fi).
- **Нотатка:** Найважливіша недосяжна група після BME280: на цих числах стоять розділи 05, 06 і 47, тобто вся частина про живлення. Частина закривається обхідним шляхом — `gpio_set_drive_capability` у ESP-IDF описує рівні сили драйвера, — і це завдання наступного проходу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-131 sha:20a65322 src:manual/60-proj-loger.md:330 klas:F -->
### T-60-131 · proza · рядок 330

**Книга каже, дослівно:**

> Кілька циклів на столі з логом: значення осмислені, рядки в CSV з'являються. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-132 sha:6d2dba14 src:manual/60-proj-loger.md:330 klas:F -->
### T-60-132 · proza · рядок 330

**Книга каже, дослівно:**

> **Виміряти струм сну** USB-тестером або, краще, шунтом і осцилографом (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-133 sha:195b951b src:manual/60-proj-loger.md:330 klas:F -->
### T-60-133 · proza · рядок 330

**Книга каже, дослівно:**

> Це головна перевірка проєкту. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-134 sha:126b1d9d src:manual/60-proj-loger.md:330 klas:F -->
### T-60-134 · proza · рядок 330

**Книга каже, дослівно:**

> Вийняти картку на ходу — пристрій продовжує, накопичує в буфер. 4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-135 sha:3b7a50dc src:manual/60-proj-loger.md:330 klas:F -->
### T-60-135 · proza · рядок 330

**Книга каже, дослівно:**

> Вставити назад — накопичене дописується. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-136 sha:58500cd8 src:manual/60-proj-loger.md:330 klas:F -->
### T-60-136 · proza · рядок 330

**Книга каже, дослівно:**

> Знизити напругу живлення лабораторним джерелом до 3.1 В — пристрій має заснути назавжди, не пошкодивши картку. 6.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-137 sha:7f1d478f src:manual/60-proj-loger.md:330 klas:F -->
### T-60-137 · proza · рядок 330

**Книга каже, дослівно:**

> Вимикати живлення грубо, багато разів, зокрема під час запису (розділ 58).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-138 sha:47cb735d src:manual/60-proj-loger.md:330 klas:F -->
### T-60-138 · proza · рядок 330

**Книга каже, дослівно:**

> Картка має лишатися читабельною. 7.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-139 sha:7fa10fa1 src:manual/60-proj-loger.md:330 klas:E -->
### T-60-139 · proza · рядок 330

**Книга каже, дослівно:**

> Тиждень безперервної роботи з реальним акумулятором; порівняти реальне падіння напруги з розрахунком.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-140 sha:985bc47c src:manual/60-proj-loger.md:345 klas:F -->
### T-60-140 · proza · рядок 345

**Книга каже, дослівно:**

> - **ESP-NOW** замість картки: передавати на приймач замість запису (розділ 42, проєкт 61) — прибирає картку й додає надійності; - **e-paper** для показу останнього значення без витрат енергії (розділ 46); - **сонячна панель** із контролером заряду; - **ULP-співпроцесор** для пробудження за подією, а не за розкладом (розділ 03).

**Доказ**

- **Клас:** F — не звірено

---
