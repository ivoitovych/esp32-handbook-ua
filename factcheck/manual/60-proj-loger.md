# Фактчекінг: `manual/60-proj-loger.md`

Одиниць твердження: **102**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-60-001 sha:c6bb5de4 src:manual/60-proj-loger.md:3 klas:F -->
### T-60-001 · proza · рядок 3

**Книга каже, дослівно:**

> Пристрій прокидається за розкладом, міряє, записує на картку й засинає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-002 sha:533db87a src:manual/60-proj-loger.md:3 klas:F -->
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

<!-- fc id:T-60-005 sha:918c6132 src:manual/60-proj-loger.md:13 klas:F -->
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

<!-- fc id:T-60-030 sha:29ab3854 src:manual/60-proj-loger.md:42 klas:C -->
### T-60-030 · kod · рядок 42

**Книга каже, дослівно:**

> ```
> 18650 ──[захист]──[TP4056]──┬── buck-boost 3.3 В ── ESP32 + периферія
>                             │
>                             └──[MOSFET]──[100к]──┬── ADC (GPIO34)
>                                           [100к]─┘
>                                             GND
> 
> I²C  (GPIO21/22): BME280 + DS3231, спільні підтяжки 4.7 кОм
> 1-Wire (GPIO4):  DS18B20 + підтяжка 4.7 кОм
> SPI  (18/19/23): microSD, CS на GPIO5
> ```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-031 sha:3d5502e9 src:manual/60-proj-loger.md:55 klas:F -->
### T-60-031 · proza · рядок 55

**Книга каже, дослівно:**

> **Buck-boost, а не LDO** — головне рішення проєкту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-032 sha:259eae72 src:manual/60-proj-loger.md:55 klas:F -->
### T-60-032 · proza · рядок 55

**Книга каже, дослівно:**

> Звичайний LDO перестає давати 3.3 В, коли акумулятор просів до 3.8 В, і відсікає приблизно половину ємності.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-033 sha:a503da18 src:manual/60-proj-loger.md:55 klas:F -->
### T-60-033 · proza · рядок 55

**Книга каже, дослівно:**

> Buck-boost працює до 3.0 В.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-034 sha:9eb66891 src:manual/60-proj-loger.md:59 klas:F -->
### T-60-034 · proza · рядок 59

**Книга каже, дослівно:**

> Різниця — вдвічі за часом роботи, і вона більша за будь-яку оптимізацію коду (розділ 53).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-035 sha:99a575e7 src:manual/60-proj-loger.md:64 klas:F -->
### T-60-035 · proza · рядок 64

**Книга каже, дослівно:**

> **Дільник вимірювання напруги вмикається транзистором.** Постійно під'єднаний дільник із двох резисторів по 100 кОм бере на порядок більше, ніж чип уві сні (числа — розділ 33), тобто стає головним споживачем усього пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-036 sha:195b9722 src:manual/60-proj-loger.md:69 klas:F -->
### T-60-036 · proza · рядок 69

**Книга каже, дослівно:**

> Без ключа розрахунок на три місяці перетворюється на три тижні (розділ 53).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-037 sha:5b607b9b src:manual/60-proj-loger.md:75 klas:F -->
### T-60-037 · proza · рядок 75

**Книга каже, дослівно:**

> Deep sleep — це перезавантаження: RAM втрачається, `app_main` починається спочатку (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-038 sha:077ad9d7 src:manual/60-proj-loger.md:75 klas:A -->
### T-60-038 · proza · рядок 75

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

<!-- fc id:T-60-039 sha:047a7bc6 src:manual/60-proj-loger.md:78 klas:A -->
### T-60-039 · kod · рядок 78

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

<!-- fc id:T-60-040 sha:84ff3f5f src:manual/60-proj-loger.md:85 klas:A -->
### T-60-040 · proza · рядок 85

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

<!-- fc id:T-60-041 sha:60e50665 src:manual/60-proj-loger.md:85 klas:F -->
### T-60-041 · proza · рядок 85

**Книга каже, дослівно:**

> Буфер на 20–30 записів у неї вміщається; більше — ні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-042 sha:33b09b68 src:manual/60-proj-loger.md:90 klas:A -->
### T-60-042 · kod · рядок 90

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

<!-- fc id:T-60-043 sha:36e9dc05 src:manual/60-proj-loger.md:98 klas:F -->
### T-60-043 · kod-ryadok · рядок 98

**Книга каже, дослівно:**

> ESP_LOGE(TAG, "акумулятор %.2f В — засинаємо назавжди", napruga);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-044 sha:96e47c3f src:manual/60-proj-loger.md:109 klas:F -->
### T-60-044 · kod-ryadok · рядок 109

**Книга каже, дослівно:**

> ESP_LOGW(TAG, "картка недоступна, у буфері %u", u_buferi);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-045 sha:11e7a3b4 src:manual/60-proj-loger.md:114 klas:F -->
### T-60-045 · kod-ryadok · рядок 114

**Книга каже, дослівно:**

> zasnuty(15 * 60);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-046 sha:86c1b4b6 src:manual/60-proj-loger.md:119 klas:F -->
### T-60-046 · proza · рядок 119

**Книга каже, дослівно:**

> Перевірка напруги стоїть **першою**, до будь-якої роботи з карткою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-047 sha:d34c43c3 src:manual/60-proj-loger.md:121 klas:F -->
### T-60-047 · proza · рядок 121

**Книга каже, дослівно:**

> Причина: запис у картку при просілому живленні — найнадійніший спосіб пошкодити файлову систему FAT так, що втрачається не останній файл, а картка цілком (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-048 sha:c226a03c src:manual/60-proj-loger.md:125 klas:F -->
### T-60-048 · proza · рядок 125

**Книга каже, дослівно:**

> Розряджений акумулятор має призводити до чистого засинання, а не до спроби записати ще один рядок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-049 sha:f0958dca src:manual/60-proj-loger.md:131 klas:A -->
### T-60-049 · kod · рядок 131

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

<!-- fc id:T-60-050 sha:e249c82c src:manual/60-proj-loger.md:133 klas:F -->
### T-60-050 · kod-ryadok · рядок 133

**Книга каже, дослівно:**

> gpio_set_level(PIN_DILNYK_EN, 1);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-051 sha:fa5319b8 src:manual/60-proj-loger.md:139 klas:A -->
### T-60-051 · kod-ryadok · рядок 139

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

<!-- fc id:T-60-052 sha:ad6f9b2c src:manual/60-proj-loger.md:145 klas:A -->
### T-60-052 · kod-ryadok · рядок 145

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

<!-- fc id:T-60-053 sha:4b6bd1c9 src:manual/60-proj-loger.md:152 klas:F -->
### T-60-053 · kod · рядок 152

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

<!-- fc id:T-60-054 sha:f0c8956e src:manual/60-proj-loger.md:163 klas:F -->
### T-60-054 · kod-ryadok · рядок 163

**Книга каже, дослівно:**

> fflush(f);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-055 sha:17341195 src:manual/60-proj-loger.md:165 klas:F -->
### T-60-055 · kod-ryadok · рядок 165

**Книга каже, дослівно:**

> fclose(f);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-056 sha:d99dbbfc src:manual/60-proj-loger.md:172 klas:F -->
### T-60-056 · proza · рядок 172

**Книга каже, дослівно:**

> Чотири дії наприкінці — `fflush`, `fsync`, `fclose`, `sd_unmount` — виглядають надмірними і не є ними.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-057 sha:a161b206 src:manual/60-proj-loger.md:175 klas:F -->
### T-60-057 · proza · рядок 175

**Книга каже, дослівно:**

> Файл, залишений відкритим, означає, що дані лежать у буфері в RAM.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-058 sha:b0cfdae4 src:manual/60-proj-loger.md:175 klas:F -->
### T-60-058 · proza · рядок 175

**Книга каже, дослівно:**

> Зникнення живлення — тим більше.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-059 sha:5619cd9a src:manual/60-proj-loger.md:178 klas:F -->
### T-60-059 · proza · рядок 178

**Книга каже, дослівно:**

> Правило логера: **відкрив, дописав рядок, закрив, розмонтував**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-060 sha:1ee7e676 src:manual/60-proj-loger.md:178 klas:F -->
### T-60-060 · proza · рядок 178

**Книга каже, дослівно:**

> Ніколи не тримати файл відкритим між циклами (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-061 sha:69c60ed0 src:manual/60-proj-loger.md:184 klas:A -->
### T-60-061 · kod · рядок 184

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

<!-- fc id:T-60-062 sha:08a000e8 src:manual/60-proj-loger.md:187 klas:F -->
### T-60-062 · kod-ryadok · рядок 187

**Книга каже, дослівно:**

> sd_unmount();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-063 sha:ab40e8e7 src:manual/60-proj-loger.md:188 klas:F -->
### T-60-063 · kod-ryadok · рядок 188

**Книга каже, дослівно:**

> gpio_set_level(PIN_DILNYK_EN, 0);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-064 sha:3fd6a686 src:manual/60-proj-loger.md:191 klas:A -->
### T-60-064 · kod-ryadok · рядок 191

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

<!-- fc id:T-60-065 sha:34ad95d5 src:manual/60-proj-loger.md:192 klas:F -->
### T-60-065 · kod-ryadok · рядок 192

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "засинаємо на %lu с", sekund);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-066 sha:c5771474 src:manual/60-proj-loger.md:193 klas:F -->
### T-60-066 · kod-ryadok · рядок 193

**Книга каже, дослівно:**

> esp_deep_sleep_start();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-067 sha:ad07f2d7 src:manual/60-proj-loger.md:198 klas:C -->
### T-60-067 · proza · рядок 198

**Книга каже, дослівно:**

> **Живлення периферії вмикається ключем.** Модуль microSD, BME280 і RTC споживають уві сні — разом це можуть бути мілі-, а не мікроампери.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-068 sha:fac610a6 src:manual/60-proj-loger.md:201 klas:F -->
### T-60-068 · proza · рядок 201

**Книга каже, дослівно:**

> Один MOSFET, що знімає живлення з усієї периферії на час сну, часто економить більше, ніж усі налаштування сну разом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-069 sha:b4495bba src:manual/60-proj-loger.md:204 klas:F -->
### T-60-069 · proza · рядок 204

**Книга каже, дослівно:**

> Виняток — RTC DS3231: він має власну батарейку й лишається живим сам.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-070 sha:83a8e3da src:manual/60-proj-loger.md:209 klas:F -->
### T-60-070 · proza · рядок 209

**Книга каже, дослівно:**

> Розрахунок для циклу раз на 15 хвилин:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-071 sha:6f45d6d6 src:manual/60-proj-loger.md:211 klas:F -->
### T-60-071 · tablycya-shapka · рядок 211

**Книга каже, дослівно:**

> | Фаза | Час | Струм | Заряд |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-072 sha:a6f4ae9a src:manual/60-proj-loger.md:212 klas:F -->
### T-60-072 · komirka · рядок 212

**Книга каже, дослівно:**

> Пробудження й ініціалізація · Час → 300 мс

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-073 sha:17288f9c src:manual/60-proj-loger.md:212 klas:C -->
### T-60-073 · komirka · рядок 212

**Книга каже, дослівно:**

> Пробудження й ініціалізація · Струм → 40 мА

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.espressif.com/en/support/documents/technical-documents (ESP32 Series Datasheet)
- **Що шукати в джерелі:** розділ «Recommended Operating Conditions»: гранично допустимий струм на пін (40 мА) і типова сила драйвера за замовчуванням; робочий діапазон температур; таблиця споживання за режимами (deep sleep, light sleep, modem sleep, активний, пік передачі Wi-Fi).
- **Нотатка:** Найважливіша недосяжна група після BME280: на цих числах стоять розділи 05, 06 і 47, тобто вся частина про живлення. Частина закривається обхідним шляхом — `gpio_set_drive_capability` у ESP-IDF описує рівні сили драйвера, — і це завдання наступного проходу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-074 sha:2d0a41b2 src:manual/60-proj-loger.md:212 klas:F -->
### T-60-074 · komirka · рядок 212

**Книга каже, дослівно:**

> Пробудження й ініціалізація · Заряд → 12 мА·с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-075 sha:b201f1de src:manual/60-proj-loger.md:213 klas:A -->
### T-60-075 · komirka · рядок 213

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

<!-- fc id:T-60-076 sha:68da1621 src:manual/60-proj-loger.md:213 klas:A -->
### T-60-076 · komirka · рядок 213

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

<!-- fc id:T-60-077 sha:7bf88644 src:manual/60-proj-loger.md:213 klas:A -->
### T-60-077 · komirka · рядок 213

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

<!-- fc id:T-60-078 sha:772fb917 src:manual/60-proj-loger.md:214 klas:F -->
### T-60-078 · komirka · рядок 214

**Книга каже, дослівно:**

> Запис на картку · Час → 400 мс

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-079 sha:ef81a4da src:manual/60-proj-loger.md:214 klas:F -->
### T-60-079 · komirka · рядок 214

**Книга каже, дослівно:**

> Запис на картку · Струм → 80 мА

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-080 sha:386c98cf src:manual/60-proj-loger.md:214 klas:F -->
### T-60-080 · komirka · рядок 214

**Книга каже, дослівно:**

> Запис на картку · Заряд → 32 мА·с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-081 sha:9084f4d4 src:manual/60-proj-loger.md:215 klas:F -->
### T-60-081 · komirka · рядок 215

**Книга каже, дослівно:**

> Сон · Час → 899 с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-082 sha:d5314759 src:manual/60-proj-loger.md:215 klas:F -->
### T-60-082 · komirka · рядок 215

**Книга каже, дослівно:**

> Сон · Струм → 30 мкА

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-083 sha:4b86eaef src:manual/60-proj-loger.md:215 klas:F -->
### T-60-083 · komirka · рядок 215

**Книга каже, дослівно:**

> Сон · Заряд → 27 мА·с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-084 sha:7ebdd2fb src:manual/60-proj-loger.md:216 klas:F -->
### T-60-084 · komirka · рядок 216

**Книга каже, дослівно:**

> **Разом за цикл** · Час → 900 с

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-085 sha:fa15cd97 src:manual/60-proj-loger.md:216 klas:D -->
### T-60-085 · komirka · рядок 216

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

<!-- fc id:T-60-086 sha:3a61fcae src:manual/60-proj-loger.md:219 klas:D -->
### T-60-086 · proza · рядок 219

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

<!-- fc id:T-60-087 sha:f90b83e5 src:manual/60-proj-loger.md:221 klas:D -->
### T-60-087 · proza · рядок 221

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

<!-- fc id:T-60-088 sha:c426e030 src:manual/60-proj-loger.md:225 klas:F -->
### T-60-088 · proza · рядок 225

**Книга каже, дослівно:**

> Розрахунок дає **понад рік**, і саме тому його треба перевірити вимірюванням (розділ 58).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-089 sha:45833f6d src:manual/60-proj-loger.md:228 klas:F -->
### T-60-089 · proza · рядок 228

**Книга каже, дослівно:**

> Практика зазвичай дає менше, і причини завжди ті самі: струм сну вищий за очікуваний (плата розробки!), холод з'їдає ємність, картка споживає більше при записі, ніж у datasheet.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-090 sha:30cc6798 src:manual/60-proj-loger.md:232 klas:F -->
### T-60-090 · proza · рядок 232

**Книга каже, дослівно:**

> Ціль «три місяці» в постановці — свідомо занижена.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-091 sha:e71331a3 src:manual/60-proj-loger.md:232 klas:F -->
### T-60-091 · proza · рядок 232

**Книга каже, дослівно:**

> Розрахунок на рік із запасом утричі означає, що три місяці ви отримаєте навіть при неприємних сюрпризах.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-092 sha:cfdb4c7e src:manual/60-proj-loger.md:237 klas:C -->
### T-60-092 · proza · рядок 237

**Книга каже, дослівно:**

> **Плата розробки для фінальної версії не годиться**: USB-міст, стабілізатор і світлодіод споживають уві сні на порядки більше за чип. 20 мА замість 30 мкА перетворює рік на добу (розділ 06).

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.espressif.com/en/support/documents/technical-documents (ESP32 Series Datasheet)
- **Що шукати в джерелі:** розділ «Recommended Operating Conditions»: гранично допустимий струм на пін (40 мА) і типова сила драйвера за замовчуванням; робочий діапазон температур; таблиця споживання за режимами (deep sleep, light sleep, modem sleep, активний, пік передачі Wi-Fi).
- **Нотатка:** Найважливіша недосяжна група після BME280: на цих числах стоять розділи 05, 06 і 47, тобто вся частина про живлення. Частина закривається обхідним шляхом — `gpio_set_drive_capability` у ESP-IDF описує рівні сили драйвера, — і це завдання наступного проходу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-60-093 sha:20a65322 src:manual/60-proj-loger.md:243 klas:F -->
### T-60-093 · proza · рядок 243

**Книга каже, дослівно:**

> Кілька циклів на столі з логом: значення осмислені, рядки в CSV з'являються. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-094 sha:6d2dba14 src:manual/60-proj-loger.md:243 klas:F -->
### T-60-094 · proza · рядок 243

**Книга каже, дослівно:**

> **Виміряти струм сну** USB-тестером або, краще, шунтом і осцилографом (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-095 sha:195b951b src:manual/60-proj-loger.md:243 klas:F -->
### T-60-095 · proza · рядок 243

**Книга каже, дослівно:**

> Це головна перевірка проєкту. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-096 sha:126b1d9d src:manual/60-proj-loger.md:243 klas:F -->
### T-60-096 · proza · рядок 243

**Книга каже, дослівно:**

> Вийняти картку на ходу — пристрій продовжує, накопичує в буфер. 4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-097 sha:3b7a50dc src:manual/60-proj-loger.md:243 klas:F -->
### T-60-097 · proza · рядок 243

**Книга каже, дослівно:**

> Вставити назад — накопичене дописується. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-098 sha:58500cd8 src:manual/60-proj-loger.md:243 klas:F -->
### T-60-098 · proza · рядок 243

**Книга каже, дослівно:**

> Знизити напругу живлення лабораторним джерелом до 3.1 В — пристрій має заснути назавжди, не пошкодивши картку. 6.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-099 sha:7f1d478f src:manual/60-proj-loger.md:243 klas:F -->
### T-60-099 · proza · рядок 243

**Книга каже, дослівно:**

> Вимикати живлення грубо, багато разів, зокрема під час запису (розділ 58).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-100 sha:47cb735d src:manual/60-proj-loger.md:243 klas:F -->
### T-60-100 · proza · рядок 243

**Книга каже, дослівно:**

> Картка має лишатися читабельною. 7.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-101 sha:7fa10fa1 src:manual/60-proj-loger.md:243 klas:F -->
### T-60-101 · proza · рядок 243

**Книга каже, дослівно:**

> Тиждень безперервної роботи з реальним акумулятором; порівняти реальне падіння напруги з розрахунком.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-60-102 sha:985bc47c src:manual/60-proj-loger.md:258 klas:F -->
### T-60-102 · proza · рядок 258

**Книга каже, дослівно:**

> - **ESP-NOW** замість картки: передавати на приймач замість запису (розділ 42, проєкт 61) — прибирає картку й додає надійності; - **e-paper** для показу останнього значення без витрат енергії (розділ 46); - **сонячна панель** із контролером заряду; - **ULP-співпроцесор** для пробудження за подією, а не за розкладом (розділ 03).

**Доказ**

- **Клас:** F — не звірено

---
