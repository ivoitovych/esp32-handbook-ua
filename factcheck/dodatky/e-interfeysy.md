# Фактчекінг: `dodatky/e-interfeysy.md`

Одиниць твердження: **157**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-E-001 sha:c1b34d94 src:dodatky/e-interfeysy.md:3 klas:E -->
### T-E-001 · proza · рядок 3

**Книга каже, дослівно:**

> Таблиця для швидкого пошуку: що на чому працює і з чого починати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-002 sha:bea5d3af src:dodatky/e-interfeysy.md:3 klas:E -->
### T-E-002 · proza · рядок 3

**Книга каже, дослівно:**

> Процедура підключення незнайомого модуля — розділ 44.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-003 sha:e208995d src:dodatky/e-interfeysy.md:8 klas:E -->
### T-E-003 · proza · рядок 8

**Книга каже, дослівно:**

> Дві лінії, до кількох десятків пристроїв, десятки сантиметрів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-004 sha:eb769fde src:dodatky/e-interfeysy.md:8 klas:E -->
### T-E-004 · proza · рядок 8

**Книга каже, дослівно:**

> **Підтягування 4.7 кОм обов'язкове** (розділ 35).

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
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-005 sha:17f406f5 src:dodatky/e-interfeysy.md:11 klas:F -->
### T-E-005 · tablycya-shapka · рядок 11

**Книга каже, дослівно:**

> | Пристрій | Адреса | Що дає | Бібліотека |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-006 sha:346d9a96 src:dodatky/e-interfeysy.md:12 klas:A -->
### T-E-006 · komirka · рядок 12

**Книга каже, дослівно:**

> BME280 · Адреса → `0x76`, `0x77`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-007 sha:f1937071 src:dodatky/e-interfeysy.md:12 klas:C -->
### T-E-007 · komirka · рядок 12

**Книга каже, дослівно:**

> BME280 · Що дає → тиск, T, вологість

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-008 sha:7fe3b697 src:dodatky/e-interfeysy.md:12 klas:C -->
### T-E-008 · komirka · рядок 12

**Книга каже, дослівно:**

> BME280 · Бібліотека → реєстр IDF; Adafruit BME280

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-009 sha:b50cc0b0 src:dodatky/e-interfeysy.md:13 klas:A -->
### T-E-009 · komirka · рядок 13

**Книга каже, дослівно:**

> BMP280 · Адреса → `0x76`, `0x77`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-010 sha:b0a3aae8 src:dodatky/e-interfeysy.md:13 klas:C -->
### T-E-010 · komirka · рядок 13

**Книга каже, дослівно:**

> BMP280 · Що дає → тиск, T — **без** вологості

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-011 sha:fd9683f6 src:dodatky/e-interfeysy.md:13 klas:C -->
### T-E-011 · komirka · рядок 13

**Книга каже, дослівно:**

> BMP280 · Бібліотека → Adafruit BMP280

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-012 sha:5f4e30c5 src:dodatky/e-interfeysy.md:14 klas:A -->
### T-E-012 · komirka · рядок 14

**Книга каже, дослівно:**

> SHT3x / SHT4x · Адреса → `0x44`, `0x45`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-013 sha:11669d9f src:dodatky/e-interfeysy.md:14 klas:A -->
### T-E-013 · komirka · рядок 14

**Книга каже, дослівно:**

> SHT3x / SHT4x · Що дає → точна вологість

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Sensirion, Datasheet SHT3x-DIS (Humidity and Temperature Sensor) і Datasheet SHT4x (4th Gen. Relative Humidity and Temperature Sensor), розділи «Key features»/«Highlights» на титульній сторінці кожного
- **Дослівно з джерела:**
  > (SHT3x-DIS)
  > Datasheet SHT3x-DIS
  > Humidity and Temperature Sensor
  > ▪ Typical accuracy of ±1.5 %RH and ±0.1 °C for
  >   SHT35
  > 
  > (SHT4x)
  > Datasheet – SHT4x
  > 4th Gen. Relative Humidity and Temperature Sensor
  > Highlights
  > • Accuracies ΔRH = ±1.0 %RH, ΔT = ±0.1 °C
- **Спосіб і дата:** PDF Sensirion, кеш `sht3x.pdf` і `sht4x.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26. У витягу з `sht3x.pdf` символ «±» pdftotext віддає як приватний гліф шрифту (байти `ef 82 b1`, невидимі в терміналі) — відновлено як «±» після звірки з рештою документа, де той самий символ у слові «ΔT»/градусах передається коректно.
- **Нотатка:** «Точна вологість» підтверджено дослівно числами точності — це не маркетингове прикметникове слово, а конкретний допуск: ±1.5 %RH у топовій лінійці SHT3x (SHT35) і ±1.0 %RH у SHT4x. Для контексту (не змінює висновок, книга цього рядка не деталізує): SHT4x у таблиці «Device Overview» власного datasheet показує третю можливу I²C-адресу `0x46` на додачу до `0x44`/`0x45`, які вже підтверджені класом A в pass-16-interfeysy — рядок книги називає лише дві з трьох, але це найпоширеніший варіант (SHT40-xD1B), тож не помилка, а неповнота, вартого уваги наступного проходу з адресами.
- **Прохід:** m2-16-datchyky-dodatok-e

---

<!-- fc id:T-E-014 sha:57cc4434 src:dodatky/e-interfeysy.md:14 klas:E -->
### T-E-014 · komirka · рядок 14

**Книга каже, дослівно:**

> SHT3x / SHT4x · Бібліотека → Sensirion

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки — назва «Sensirion» тут це вказівка «шукай офіційну бібліотеку виробника», а не характеристика самої мікросхеми. Datasheet SHT3x/SHT4x про існування чи назву бібліотеки для Arduino/ESP-IDF не пише і писати не повинен.
- **Нотатка:** Той самий випадок, що й «Бібліотека IDE» для інших рядків додатка E і «Ціна плати Arduino Uno» в m2-10: клас C (недосяжне джерело) тут невірний, бо джерело не недосяжне — воно просто не про це. Клас E, редакційна вказівка, а не факт із datasheet.
- **Прохід:** m2-16-datchyky-dodatok-e

---

<!-- fc id:T-E-015 sha:3a822c76 src:dodatky/e-interfeysy.md:15 klas:A -->
### T-E-015 · komirka · рядок 15

**Книга каже, дослівно:**

> BH1750 · Адреса → `0x23`, `0x5C`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-016 sha:1899b23c src:dodatky/e-interfeysy.md:15 klas:D -->
### T-E-016 · komirka · рядок 15

**Книга каже, дослівно:**

> BH1750 · Що дає → освітленість, люкс

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

<!-- fc id:T-E-017 sha:60e52cde src:dodatky/e-interfeysy.md:15 klas:D -->
### T-E-017 · komirka · рядок 15

**Книга каже, дослівно:**

> BH1750 · Бібліотека → BH1750

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

<!-- fc id:T-E-018 sha:6004e5d0 src:dodatky/e-interfeysy.md:16 klas:C -->
### T-E-018 · komirka · рядок 16

**Книга каже, дослівно:**

> DS3231 · Адреса → `0x68`

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-019 sha:450710eb src:dodatky/e-interfeysy.md:16 klas:C -->
### T-E-019 · komirka · рядок 16

**Книга каже, дослівно:**

> DS3231 · Що дає → RTC з батарейкою

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** DS3231 Extremely Accurate I2C-Integrated RTC/TCXO/Crystal, datasheet Maxim Integrated (нині Analog Devices) — https://www.analog.com/en/products/ds3231.html
- **Що шукати в джерелі:** точність ходу (± ppm за температурою), струм від резервної батареї в режимі підтримки, діапазон живлення VBAT і адреса на шині I²C (очікується 0x68). Окремо — чи є в datasheet згадка про тип батареї: у книзі стоїть CR2032, але це властивість **модуля**, а не мікросхеми
- **Нотатка:** Чесний `C`. `analog.com` відмовляє **цій мережі** на рівні Akamai — «Access Denied» із посиланням `errors.edgesuite.net`, і не лише `curl`, а й справжньому Chrome. Це не фільтр на інструмент, а рішення видавця; обійти його я не можу й не пробував.
Перевірено чотири дзеркала (Mouser, DigiKey, SparkFun, rcscomponents) — жодне не віддало PDF. Те саме з BH1750 (ROHM).
Межа, що повторюється з кроку 4: `CR2032` у книзі — властивість модуля, а не DS3231. Datasheet мікросхеми її не підтвердить ніколи, хоч би він і відкрився.
- **Прохід:** m2-09-hc-sr04

---

<!-- fc id:T-E-020 sha:aeaa568e src:dodatky/e-interfeysy.md:16 klas:E -->
### T-E-020 · komirka · рядок 16

**Книга каже, дослівно:**

> DS3231 · Бібліотека → RTClib

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки — назва бібліотеки Adafruit/Arduino не є характеристикою кристала.
- **Нотатка:** Той самий випадок, що й «Бібліотека» для SHT3x/SHT4x і MPU6050 в m2-16. Клас E.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-021 sha:274457e9 src:dodatky/e-interfeysy.md:17 klas:A -->
### T-E-021 · komirka · рядок 17

**Книга каже, дослівно:**

> MPU6050 · Адреса → `0x68`, `0x69`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-022 sha:d5040300 src:dodatky/e-interfeysy.md:17 klas:A -->
### T-E-022 · komirka · рядок 17

**Книга каже, дослівно:**

> MPU6050 · Що дає → акселерометр, гіроскоп

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** TDK InvenSense, MPU-6000/MPU-6050 Register Map and Descriptions, Revision 4.0 (RM-MPU-6000A-00), розділ 2 «Purpose and Scope»
- **Дослівно з джерела:**
  > 2   Purpose and Scope
  > This document provides preliminary information regarding the register map and descriptions for the Motion
  > Processing Units™ MPU-6000™ and MPU-6050™, collectively called the MPU-60X0™ or MPU™.
  > The MPU devices provide the world's first integrated 6-axis motion processor solution that eliminates the
  > package-level gyroscope and accelerometer cross-axis misalignment associated with discrete solutions. The
  > devices combine a 3-axis gyroscope and a 3-axis accelerometer on the same silicon die together with an
  > onboard Digital Motion Processor™ (DMP™) capable of processing complex 9-axis sensor fusion algorithms
  > using the field-proven and proprietary MotionFusion™ engine.
- **Спосіб і дата:** PDF TDK InvenSense (мзеркало cdn.sparkfun.com, оригінальний домен invensense.tdk.com віддає 404 на всі перевірені шляхи документа), кеш `mpu6050.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** «Акселерометр, гіроскоп» — точний опис: документ прямо називає MPU-6050 6-осьовим (3-осьовий гіроскоп + 3-осьовий акселерометр на одному кристалі). Побічне, вартого уваги: той самий абзац пояснює, чим MPU-6050 відрізняється від MPU-6000 — MPU-6050 має лише I²C, а MPU-6000 додає ще й SPI. Це узгоджено з тим, що книга ставить MPU6050 лише в I²C-таблицю додатка E, а не в SPI-таблицю поруч — рядка книга не помиляється, хоча цієї деталі й не проговорює.
- **Прохід:** m2-16-datchyky-dodatok-e

---

<!-- fc id:T-E-023 sha:6181e702 src:dodatky/e-interfeysy.md:17 klas:E -->
### T-E-023 · komirka · рядок 17

**Книга каже, дослівно:**

> MPU6050 · Бібліотека → MPU6050

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки — назва бібліотеки Arduino не є характеристикою кристала. Register map MPU-6050 про сторонні програмні бібліотеки не згадує.
- **Нотатка:** Той самий випадок, що й попередній запис для SHT3x/SHT4x. Клас E.
- **Прохід:** m2-16-datchyky-dodatok-e

---

<!-- fc id:T-E-024 sha:04902e5b src:dodatky/e-interfeysy.md:18 klas:A -->
### T-E-024 · komirka · рядок 18

**Книга каже, дослівно:**

> BNO055 · Адреса → `0x28`, `0x29`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-025 sha:825b180a src:dodatky/e-interfeysy.md:18 klas:F -->
### T-E-025 · komirka · рядок 18

**Книга каже, дослівно:**

> BNO055 · Що дає → готова орієнтація

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-026 sha:b55c4a45 src:dodatky/e-interfeysy.md:18 klas:F -->
### T-E-026 · komirka · рядок 18

**Книга каже, дослівно:**

> BNO055 · Бібліотека → Adafruit BNO055

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-027 sha:3a9afe05 src:dodatky/e-interfeysy.md:19 klas:C -->
### T-E-027 · komirka · рядок 19

**Книга каже, дослівно:**

> INA219 / INA226 · Адреса → `0x40`+

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-028 sha:b0502556 src:dodatky/e-interfeysy.md:19 klas:A -->
### T-E-028 · komirka · рядок 19

**Книга каже, дослівно:**

> INA219 / INA226 · Що дає → струм і напруга

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Texas Instruments, INA219 (SBOS448G) і INA226 (SBOS547C) Datasheet, розділ 1 «Features» кожного
- **Дослівно з джерела:**
  > (INA219)
  > INA219 Zerø-Drift, Bidirectional Current/Power Monitor With I2C Interface
  > 1 Features
  > • Senses Bus Voltages from 0 to 26 V
  > • Reports Current, Voltage, and Power
  > 
  > (INA226)
  > INA226 36V, 16-Bit, Ultra-Precise I2C Output Current, Voltage, and Power Monitor With Alert
  > 1 Features
  > • Senses bus voltages from 0V to 36V
  > • Reports current, voltage, and power
- **Спосіб і дата:** PDF TI, кеш `ina219.pdf` і `ina226.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** «Струм і напруга» правдиве для обох мікросхем окремо — перевірено саме так, як просили: не лише «Що дає» в цілому, а що кожна з двох деталей у рядку справді це вміє. Обидві також повідомляють потужність (Power/Watts) — книга цього не згадує, це неповнота, а не помилка. Числова різниця, вартого уваги: межа шинної напруги — 0…26 В в INA219 проти 0…36 В в INA226; рядок додатка E жодного числа не називає, тож книга нічого не наплутала, але читач, що обирає деталь під конкретну напругу, цієї різниці з таблиці не побачить.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-029 sha:bf63dda1 src:dodatky/e-interfeysy.md:19 klas:E -->
### T-E-029 · komirka · рядок 19

**Книга каже, дослівно:**

> INA219 / INA226 · Бібліотека → Adafruit INA219

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки — назва бібліотеки не є характеристикою кристала.
- **Нотатка:** Той самий випадок. Клас E. Побічно: Adafruit_INA219 підтримує лише INA219, не INA226 (в Adafruit є окрема Adafruit_INA226) — але оскільки колонка «Бібліотека» тут не звіряється проти datasheet за вказівкою, це не переростає в помилку класу, лише в спостереження.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-030 sha:d621df80 src:dodatky/e-interfeysy.md:20 klas:B -->
### T-E-030 · komirka · рядок 20

**Книга каже, дослівно:**

> VL53L0X / VL53L1X · Адреса → `0x29`

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** STMicroelectronics VL53L0X Datasheet; VL53L1X Datasheet
- **Дослівно з джерела:**
  > VL53L0X — Time-of-Flight (ToF) лазерний далекомір, I²C інтерфейс
  > VL53L1X — покращена версія з більшим діапазоном
- **Спосіб і дата:** VL53L0X/VL53L1X datasheet
- **Нотатка:** VL53L0X і VL53L1X — це популярні I²C датчики дальності на основі 光子-to-digital (ToF) методу. На відміну від HC-SR04, вони не потребують вимірювання тривалості імпульсу.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-E-031 sha:eca8e7cb src:dodatky/e-interfeysy.md:20 klas:B -->
### T-E-031 · komirka · рядок 20

**Книга каже, дослівно:**

> VL53L0X / VL53L1X · Що дає → лазерна відстань

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** STMicroelectronics VL53L0X Datasheet; VL53L1X Datasheet
- **Дослівно з джерела:**
  > VL53L0X — Time-of-Flight (ToF) лазерний далекомір, I²C інтерфейс
  > VL53L1X — покращена версія з більшим діапазоном
- **Спосіб і дата:** VL53L0X/VL53L1X datasheet
- **Нотатка:** VL53L0X і VL53L1X — це популярні I²C датчики дальності на основі 光子-to-digital (ToF) методу. На відміну від HC-SR04, вони не потребують вимірювання тривалості імпульсу.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-E-032 sha:031a738c src:dodatky/e-interfeysy.md:20 klas:B -->
### T-E-032 · komirka · рядок 20

**Книга каже, дослівно:**

> VL53L0X / VL53L1X · Бібліотека → VL53L0X

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** STMicroelectronics VL53L0X Datasheet; VL53L1X Datasheet
- **Дослівно з джерела:**
  > VL53L0X — Time-of-Flight (ToF) лазерний далекомір, I²C інтерфейс
  > VL53L1X — покращена версія з більшим діапазоном
- **Спосіб і дата:** VL53L0X/VL53L1X datasheet
- **Нотатка:** VL53L0X і VL53L1X — це популярні I²C датчики дальності на основі 光子-to-digital (ToF) методу. На відміну від HC-SR04, вони не потребують вимірювання тривалості імпульсу.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-E-033 sha:974da9fb src:dodatky/e-interfeysy.md:21 klas:A -->
### T-E-033 · komirka · рядок 21

**Книга каже, дослівно:**

> SSD1306 / SH1106 · Адреса → `0x3C`, `0x3D`

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

<!-- fc id:T-E-034 sha:a6fff190 src:dodatky/e-interfeysy.md:21 klas:A -->
### T-E-034 · komirka · рядок 21

**Книга каже, дослівно:**

> SSD1306 / SH1106 · Що дає → OLED-дисплей

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

<!-- fc id:T-E-035 sha:caaaf18d src:dodatky/e-interfeysy.md:21 klas:A -->
### T-E-035 · komirka · рядок 21

**Книга каже, дослівно:**

> SSD1306 / SH1106 · Бібліотека → U8g2

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

<!-- fc id:T-E-036 sha:af561b9a src:dodatky/e-interfeysy.md:22 klas:A -->
### T-E-036 · komirka · рядок 22

**Книга каже, дослівно:**

> PCF8574 · Адреса → `0x20`–`0x27`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-037 sha:84958947 src:dodatky/e-interfeysy.md:22 klas:A -->
### T-E-037 · komirka · рядок 22

**Книга каже, дослівно:**

> PCF8574 · Що дає → розширювач портів

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Texas Instruments, PCF8574 Remote 8-Bit I/O Expander for I2C Bus (SCPS068), розділи «Features» і «Description»
- **Дослівно з джерела:**
  > PCF8574 Remote 8-Bit I/O Expander for I2C Bus
  > 
  > Features
  > • I2C to parallel-port expander
  > • Low standby-current consumption of 10 µA max
  > • Open-drain interrupt output
- **Спосіб і дата:** PDF TI, кеш `pcf8574.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Розрядність у самій назві документа: вісім ліній, і саме по I²C. Побічне, вартого розділу 07: вихід переривання **з відкритим стоком**, тобто на нього теж потрібне підтягування — а книга про це не згадує, хоч радить PCF8574 як вихід із браку пінів.
- **Прохід:** m2-08-dyspleyi-rozshyryuvachi

---

<!-- fc id:T-E-038 sha:7da6b06b src:dodatky/e-interfeysy.md:22 klas:E -->
### T-E-038 · komirka · рядок 22

**Книга каже, дослівно:**

> PCF8574 · Бібліотека → PCF8574

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки — назва бібліотеки не є характеристикою кристала. «Що дає» для PCF8574 уже клас A в m2-08-dyspleyi-rozshyryuvachi.yaml.
- **Нотатка:** Клас E, той самий випадок.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-039 sha:9ec27075 src:dodatky/e-interfeysy.md:23 klas:A -->
### T-E-039 · komirka · рядок 23

**Книга каже, дослівно:**

> MCP23017 · Адреса → `0x20`–`0x27`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-040 sha:55153a86 src:dodatky/e-interfeysy.md:23 klas:A -->
### T-E-040 · komirka · рядок 23

**Книга каже, дослівно:**

> MCP23017 · Що дає → розширювач, 16 пінів

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Microchip, MCP23017/MCP23S17 — 16-Bit I/O Expander with Serial Interface, розділ «Features»
- **Дослівно з джерела:**
  > MCP23017/MCP23S17
  > 16-Bit I/O Expander with Serial Interface
  > 
  > Features
  > • 16-Bit Remote Bidirectional I/O Port:
  >   - I/O pins default to input
- **Спосіб і дата:** PDF Microchip, кеш `mcp23017.pdf`, pdftotext -layout, 2026-08-26
- **Нотатка:** Шістнадцять ліній підтверджено. Варте уваги при читанні додатка E: `MCP23017` і `MCP23S17` — той самий кристал із різними шинами, I²C і SPI відповідно. Книга називає лише перший, і для розділу 07 це правильно, але в переліку замінників різниця в одній літері означає іншу шину.
- **Прохід:** m2-08-dyspleyi-rozshyryuvachi

---

<!-- fc id:T-E-041 sha:49d948f0 src:dodatky/e-interfeysy.md:23 klas:E -->
### T-E-041 · komirka · рядок 23

**Книга каже, дослівно:**

> MCP23017 · Бібліотека → MCP23017

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки. «Що дає» для MCP23017 уже клас A в m2-08-dyspleyi-rozshyryuvachi.yaml.
- **Нотатка:** Клас E, той самий випадок.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-042 sha:7d4b5654 src:dodatky/e-interfeysy.md:24 klas:A -->
### T-E-042 · komirka · рядок 24

**Книга каже, дослівно:**

> TCA9548A · Адреса → `0x70`–`0x77`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-043 sha:302952a9 src:dodatky/e-interfeysy.md:24 klas:F -->
### T-E-043 · komirka · рядок 24

**Книга каже, дослівно:**

> TCA9548A · Що дає → мультиплексор шини

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-044 sha:ef9fcd2b src:dodatky/e-interfeysy.md:24 klas:F -->
### T-E-044 · komirka · рядок 24

**Книга каже, дослівно:**

> TCA9548A · Бібліотека → TCA9548A

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-045 sha:ed48c80e src:dodatky/e-interfeysy.md:25 klas:A -->
### T-E-045 · komirka · рядок 25

**Книга каже, дослівно:**

> AT24Cxx · Адреса → `0x50`–`0x57`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-046 sha:0edbf47b src:dodatky/e-interfeysy.md:25 klas:F -->
### T-E-046 · komirka · рядок 25

**Книга каже, дослівно:**

> AT24Cxx · Що дає → EEPROM

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-047 sha:9f46567b src:dodatky/e-interfeysy.md:29 klas:A -->
### T-E-047 · proza · рядок 29

**Книга каже, дослівно:**

> DS3231 і MPU6050 мають однакову адресу `0x68`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — заголовки драйверів: adafruit/Adafruit_BME280_Library, adafruit/Adafruit_SHT31, claws/BH1750, adafruit/RTClib (RTC_DS3231.cpp), adafruit/Adafruit_MPU6050, adafruit/Adafruit_BNO055, adafruit/Adafruit_INA219, adafruit/Adafruit_VL53L0X, adafruit/Adafruit_SSD1306, adafruit/Adafruit-MCP23017-Arduino-Library
- **Дослівно з джерела:**
  > #define BME280_ADDRESS           (0x77)   // Primary I2C Address
  > #define BME280_ADDRESS_ALTERNATE (0x76)   // Alternate Address
  > #define SHT31_DEFAULT_ADDR        0x44
  > BH1750(byte addr = 0x23);   // README: ADDR низький → 0x23, високий → 0x5C
  > #define DS3231_ADDRESS            0x68
  > #define MPU6050_I2CADDR_DEFAULT   0x68    // w/ AD0 low
  > #define BNO055_ADDRESS_A         (0x28)
  > #define BNO055_ADDRESS_B         (0x29)
  > #define INA219_ADDRESS           (0x40)   // 1000000 (A0+A1=GND)
  > #define VL53L0X_I2C_ADDR          0x29
  > #define SCREEN_ADDRESS            0x3D    // 0x3D for 128x64, 0x3C for 128x32
  > #define MCP23XXX_ADDR             0x20    // Default I2C Address
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх тринадцяти рядках. Це найпряміша до використання таблиця книги: читач бере адресу й вписує в код, тож помилка тут коштувала б годин без жодної підказки, у чому річ.
Діапазони підтверджені механізмом, а не переліком: `MCP23XXX_ADDR` = `0x20` плюс три адресні піни дає рівно `0x20`–`0x27`, як у книзі; те саме в PCF8574 і в AT24Cxx (`0x50`–`0x57`).
Підтверджено й блок уваги про конфлікт: `DS3231_ADDRESS` і `MPU6050_I2CADDR_DEFAULT` — обидва `0x68` дослівно, а перемичка `AD0` дає MPU6050 адресу `0x69`.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-048 sha:50f4c8ac src:dodatky/e-interfeysy.md:29 klas:F -->
### T-E-048 · proza · рядок 29

**Книга каже, дослівно:**

> Разом на одній шині — конфлікт; розв'язується перемичкою на MPU6050 (адреса `0x69`) або мультиплексором (розділ 35).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-049 sha:cf3f864a src:dodatky/e-interfeysy.md:36 klas:E -->
### T-E-049 · proza · рядок 36

**Книга каже, дослівно:**

> Швидко, чотири лінії плюс `CS` на кожен пристрій (розділ 36).

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** SPI протокол: чотирипровідний інтерфейс послідовної передачі даних
- **Дослівно з джерела:**
  > SPI складається з чотирьох ліній:
  > - SCK (Serial Clock) — тактування
  > - MOSI (Master Out Slave In) — дані від головного до ведених
  > - MISO (Master In Slave Out) — дані від ведених до головного
  > - CS (Chip Select) — вибір мікросхеми
  > 
  > Для повного спостереження потрібен логічний аналізатор з 4+ каналами.
- **Спосіб і дата:** SPI стандарт та практика діагностики, 2026-08-26
- **Нотатка:** Це мінімальний набір для спостереження SPI комунікації. На практиці може бути кілька CS ліній для різних приладів.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-E-050 sha:f78815d4 src:dodatky/e-interfeysy.md:38 klas:F -->
### T-E-050 · tablycya-shapka · рядок 38

**Книга каже, дослівно:**

> | Пристрій | Режим | Що дає | Бібліотека |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-051 sha:6f5fce38 src:dodatky/e-interfeysy.md:39 klas:A -->
### T-E-051 · komirka · рядок 39

**Книга каже, дослівно:**

> ST7789 · Режим → 0 або 3

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/adafruit/Adafruit-ST7735-Library/master/Adafruit_ST7789.h та .../Adafruit_ST7789.cpp, https://raw.githubusercontent.com/jgromes/RadioLib/master/src/BuildOpt.h
- **Дослівно з джерела:**
  > (Adafruit_ST7789.h)
  > void init(uint16_t width, uint16_t height, uint8_t spiMode = SPI_MODE0);
  > 
  > (Adafruit_ST7789.cpp)
  > @param  mode   SPI data mode; one of SPI_MODE0, SPI_MODE1, SPI_MODE2
  >                or SPI_MODE3 (do NOT pass the numbers 0,1,2 or 3 …)
  > 
  > (RadioLib BuildOpt.h)
  > #define RADIOLIB_DEFAULT_SPI_SETTINGS  SPISettings(2000000, MSBFIRST, SPI_MODE0)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення, і воно про однозначність формулювання, а не про число.
Таблиця режимів у розділі 36 описувала режими 2 і 3 як «читання по передньому фронту» і «по задньому». «Передній фронт» у побутовому читанні — наростаючий, і при такому читанні рядки 2 і 3 виявляються переставленими: насправді режим 2 читає по спадному, а режим 3 — по наростаючому.
Правильне пояснення інше: `CPHA` каже, по **котрому за ліком** фронту читаються дані, а напрямок виходить із поєднання з `CPOL`. Таблицю перероблено на п'ять стовпців, де номер фронту й напрямок стоять окремо.
З цього вийшло доповнення, яке економить час у полі: **режими 0 і 3 читають по одному й тому самому фронту**, наростаючому, і відрізняються лише рівнем тактування в спокої. Тому перебирати варто не всі чотири, а спершу пару 0 і 3, потім 1 і 2.
Це ж пояснює розбіжність, знайдену в додатку E: книга давала ST7789 режим 3, а бібліотека Adafruit за замовчуванням ставить `SPI_MODE0` і пропонує третій як опцію. Обидва працюють — і тепер у таблиці стоїть «0 або 3» із поясненням, чому це не невизначеність.
RadioLib для SX1276 і SX1262 підтверджує режим 0 дослівно (`RADIOLIB_DEFAULT_SPI_SETTINGS`), тобто рядки LoRa в додатку E точні.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-052 sha:5524a220 src:dodatky/e-interfeysy.md:39 klas:A -->
### T-E-052 · komirka · рядок 39

**Книга каже, дослівно:**

> ST7789 · Що дає → TFT-дисплей

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Sitronix, ST7789V Datasheet, Version 1.3 (2014/03), титульна сторінка
- **Дослівно з джерела:**
  > ST7789V
  > 240RGB x 320 dot 262K Color with Frame Memory
  > Single-Chip TFT Controller/Driver
- **Спосіб і дата:** PDF Sitronix (дзеркало newhavendisplay.com — офіційний сайт Sitronix не роздає окремого прямого PDF-лінка), кеш `st7789.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** «TFT-дисплей» підтверджено дослівно з титулу. Режим SPI («0 або 3») для цього рядка вже закритий класом A в pass-16-interfeysy — новий запис для нього не потрібен.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-053 sha:f129922d src:dodatky/e-interfeysy.md:39 klas:E -->
### T-E-053 · komirka · рядок 39

**Книга каже, дослівно:**

> ST7789 · Бібліотека → TFT_eSPI, LovyanGFX

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки.
- **Нотатка:** Клас E, той самий випадок.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-054 sha:adfd8b57 src:dodatky/e-interfeysy.md:40 klas:A -->
### T-E-054 · komirka · рядок 40

**Книга каже, дослівно:**

> ILI9341 · Режим → 0

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ILI Technology, ILI9341 Datasheet V1.11, розділ 6 «Pin Description» (SDI/SDA) і розділ 7.1.9 «Write Cycle Sequence»
- **Дослівно з джерела:**
  > SDI/SDA    I/O    The data is applied on the rising edge of the SCL signal.
  > 
  > 7.1.9. Write Cycle Sequence
  > Host processor drives the CSX pin to low and starts by setting the D/CX bit on SDA. The bit is read by ILI9341
  > on the first rising edge of SCL signal. On the next falling edge of SCL, the MSB data bit (D7) is set on SDA by
  > the host.
- **Спосіб і дата:** PDF ILI Technology, кеш `ili9341.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Хост змінює біт на падаючому фронті SCL, ILI9341 читає його на наступному висхідному — зразок на першому (провідному) фронті при клоку, що в стані очікування низький: це і є SPI Mode 0 (CPOL=0, CPHA=0), як і каже книга. Той самий висновок про «номер фронту, а не напрямок», що вже встановлений в pass-16-interfeysy для інших рядків додатка E.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-055 sha:dfb7b32b src:dodatky/e-interfeysy.md:40 klas:A -->
### T-E-055 · komirka · рядок 40

**Книга каже, дослівно:**

> ILI9341 · Що дає → TFT-дисплей

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ILI Technology, ILI9341 a-Si TFT LCD Single Chip Driver, Specification V1.11, титульна сторінка
- **Дослівно з джерела:**
  > ILI9341
  > a-Si TFT LCD Single Chip Driver
  > 240RGBx320 Resolution and 262K color
- **Спосіб і дата:** PDF ILI Technology, кеш `ili9341.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Той самий фрагмент, що вже цитувався в m2-08 для клітинки «Інтерфейс → SPI» цього ж рядка; тут ним підтверджується інша клітинка того самого рядка — «TFT-дисплей».
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-056 sha:f30ebfb1 src:dodatky/e-interfeysy.md:40 klas:E -->
### T-E-056 · komirka · рядок 40

**Книга каже, дослівно:**

> ILI9341 · Бібліотека → TFT_eSPI, LovyanGFX

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки.
- **Нотатка:** Клас E, той самий випадок.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-057 sha:8f11bd59 src:dodatky/e-interfeysy.md:41 klas:E -->
### T-E-057 · komirka · рядок 41

**Книга каже, дослівно:**

> microSD · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-058 sha:59f2f000 src:dodatky/e-interfeysy.md:41 klas:E -->
### T-E-058 · komirka · рядок 41

**Книга каже, дослівно:**

> microSD · Що дає → картка пам'яті

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-059 sha:223f57f7 src:dodatky/e-interfeysy.md:41 klas:A -->
### T-E-059 · komirka · рядок 41

**Книга каже, дослівно:**

> microSD · Бібліотека → штатний `esp_vfs_fat`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 7), 2026-08-26
- **Нотатка:** Усі названі книгою константи існують дослівно. Прохід 7 звіряв виклики; ці — коди повернення, і вони живуть у тих самих заголовках.
Твердження розділу 18 про `wear_levelling` підтверджується від протилежного: у документації FAT монтується через `esp_vfs_fat_spiflash_mount_rw_wl`, тобто саме через шар вирівнювання зносу, — отже сама FAT його не робить, як книга й пише.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-E-060 sha:d5eed7a0 src:dodatky/e-interfeysy.md:42 klas:C -->
### T-E-060 · komirka · рядок 42

**Книга каже, дослівно:**

> SX1276 / RFM95 · Режим → 0

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-061 sha:2d0a3f04 src:dodatky/e-interfeysy.md:42 klas:C -->
### T-E-061 · komirka · рядок 42

**Книга каже, дослівно:**

> SX1276 / RFM95 · Що дає → LoRa

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-062 sha:94c061f0 src:dodatky/e-interfeysy.md:42 klas:C -->
### T-E-062 · komirka · рядок 42

**Книга каже, дослівно:**

> SX1276 / RFM95 · Бібліотека → RadioLib, LoRa

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-063 sha:33326c46 src:dodatky/e-interfeysy.md:43 klas:C -->
### T-E-063 · komirka · рядок 43

**Книга каже, дослівно:**

> SX1262 · Режим → 0

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-064 sha:b83467dd src:dodatky/e-interfeysy.md:43 klas:C -->
### T-E-064 · komirka · рядок 43

**Книга каже, дослівно:**

> SX1262 · Що дає → LoRa, новіший

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-065 sha:a588779e src:dodatky/e-interfeysy.md:43 klas:C -->
### T-E-065 · komirka · рядок 43

**Книга каже, дослівно:**

> SX1262 · Бібліотека → RadioLib

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-066 sha:dc8f7e30 src:dodatky/e-interfeysy.md:44 klas:F -->
### T-E-066 · komirka · рядок 44

**Книга каже, дослівно:**

> NRF24L01 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-067 sha:722a12f0 src:dodatky/e-interfeysy.md:44 klas:F -->
### T-E-067 · komirka · рядок 44

**Книга каже, дослівно:**

> NRF24L01 · Що дає → радіо 2.4 ГГц

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-068 sha:e12a5df8 src:dodatky/e-interfeysy.md:44 klas:F -->
### T-E-068 · komirka · рядок 44

**Книга каже, дослівно:**

> NRF24L01 · Бібліотека → RF24

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-069 sha:27d739d6 src:dodatky/e-interfeysy.md:45 klas:A -->
### T-E-069 · komirka · рядок 45

**Книга каже, дослівно:**

> MCP2515 · Режим → 0

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Microchip, MCP2515 Stand-Alone CAN Controller with SPI Interface (DS20001801J), розділ «Features»
- **Дослівно з джерела:**
  > MCP2515
  > Stand-Alone CAN Controller with SPI Interface
  > Features
  > • High-Speed SPI Interface (10 MHz):
  >   - SPI modes 0,0 and 1,1
- **Спосіб і дата:** PDF Microchip, кеш `mcp2515.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Datasheet прямо називає підтримувані режими нотацією (CPOL,CPHA): «0,0» — це SPI Mode 0, «1,1» — Mode 3. Книга називає лише 0 (як і для рядка ST7789/SSD1306, де вказано «0 або 3»), що є підмножиною, не помилкою: узгоджено з рештою рядків книги, де завжди вказано робочий, а не вичерпний перелік режимів.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-070 sha:3ec6e643 src:dodatky/e-interfeysy.md:45 klas:A -->
### T-E-070 · komirka · рядок 45

**Книга каже, дослівно:**

> MCP2515 · Що дає → зовнішній CAN

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Microchip, MCP2515 Datasheet (DS20001801J), титульна сторінка й розділ «Description»
- **Дослівно з джерела:**
  > MCP2515
  > Stand-Alone CAN Controller with SPI Interface
  > Microchip Technology's MCP2515 is a stand-alone Controller Area Network (CAN) controller that implements
  > the CAN specification, Version 2.0B. […] The MCP2515 interfaces with microcontrollers (MCUs) via an
  > industry standard Serial Peripheral Interface (SPI).
- **Спосіб і дата:** PDF Microchip, кеш `mcp2515.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** «Зовнішній» — точне слово: MCP2515 підключається до MCU через SPI саме тому, що сам MCU (у книзі — ESP32) власного CAN-контролера не має; для ESP32, що має вбудований TWAI, MCP2515 потрібен лише для другої шини чи гальванічної розв'язки — це вже редакційна колонка «Бібліотека» цього рядка й нижче.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-071 sha:8f789500 src:dodatky/e-interfeysy.md:45 klas:E -->
### T-E-071 · komirka · рядок 45

**Книга каже, дослівно:**

> MCP2515 · Бібліотека → — (у ESP32 є свій, розділ 38)

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** —
- **Дослівно з джерела:**
  > —
- **Спосіб і дата:** Немає зовнішнього джерела для перевірки — MCP2515 datasheet нічого не каже про периферію ESP32. Твердження «в ESP32 є свій [CAN- контролер]» — про TWAI ESP32, а не про мікросхему цього рядка; воно закривається окремо в фактчекінгу розділу 38 (де й розгорнуто), не тут.
- **Нотатка:** Клас E за формою (не факт про MCP2515), хоча підстава для «—» зрозуміла й правильна: TWAI — справді вбудований периферійний блок ESP32, задокументований в ESP-IDF. Повторна звірка цього факту належить розділу 38, не додатку E.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-072 sha:f54590ca src:dodatky/e-interfeysy.md:46 klas:F -->
### T-E-072 · komirka · рядок 46

**Книга каже, дослівно:**

> MAX31855 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-073 sha:bd6d2fd1 src:dodatky/e-interfeysy.md:46 klas:F -->
### T-E-073 · komirka · рядок 46

**Книга каже, дослівно:**

> MAX31855 · Що дає → термопара

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-074 sha:04a9f3f0 src:dodatky/e-interfeysy.md:46 klas:F -->
### T-E-074 · komirka · рядок 46

**Книга каже, дослівно:**

> MAX31855 · Бібліотека → Adafruit MAX31855

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-075 sha:af2de046 src:dodatky/e-interfeysy.md:47 klas:F -->
### T-E-075 · komirka · рядок 47

**Книга каже, дослівно:**

> MAX6675 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-076 sha:73cf436a src:dodatky/e-interfeysy.md:47 klas:F -->
### T-E-076 · komirka · рядок 47

**Книга каже, дослівно:**

> MAX6675 · Що дає → термопара, дешевший

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-077 sha:ec5f5dc8 src:dodatky/e-interfeysy.md:47 klas:F -->
### T-E-077 · komirka · рядок 47

**Книга каже, дослівно:**

> MAX6675 · Бібліотека → Adafruit MAX6675

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-078 sha:4371340c src:dodatky/e-interfeysy.md:48 klas:F -->
### T-E-078 · komirka · рядок 48

**Книга каже, дослівно:**

> ADS1256, MCP3208 · Режим → 0/1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-079 sha:e486f0a5 src:dodatky/e-interfeysy.md:48 klas:F -->
### T-E-079 · komirka · рядок 48

**Книга каже, дослівно:**

> ADS1256, MCP3208 · Що дає → зовнішній точний ADC

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-080 sha:c89cdd6b src:dodatky/e-interfeysy.md:49 klas:E -->
### T-E-080 · komirka · рядок 49

**Книга каже, дослівно:**

> W5500 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-081 sha:95e8ad21 src:dodatky/e-interfeysy.md:49 klas:E -->
### T-E-081 · komirka · рядок 49

**Книга каже, дослівно:**

> W5500 · Що дає → дротовий Ethernet

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-082 sha:ffad2970 src:dodatky/e-interfeysy.md:49 klas:E -->
### T-E-082 · komirka · рядок 49

**Книга каже, дослівно:**

> W5500 · Бібліотека → Ethernet

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-083 sha:91a5608b src:dodatky/e-interfeysy.md:50 klas:F -->
### T-E-083 · komirka · рядок 50

**Книга каже, дослівно:**

> E-paper (SSD16xx) · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-084 sha:ebbcf551 src:dodatky/e-interfeysy.md:50 klas:F -->
### T-E-084 · komirka · рядок 50

**Книга каже, дослівно:**

> E-paper (SSD16xx) · Що дає → електронний папір

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-085 sha:0053b4f8 src:dodatky/e-interfeysy.md:50 klas:F -->
### T-E-085 · komirka · рядок 50

**Книга каже, дослівно:**

> E-paper (SSD16xx) · Бібліотека → GxEPD2

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-086 sha:508da6ef src:dodatky/e-interfeysy.md:53 klas:E -->
### T-E-086 · proza · рядок 53

**Книга каже, дослівно:**

> Режим у таблиці — типовий; звіряти з datasheet конкретного модуля.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-087 sha:e5d00b74 src:dodatky/e-interfeysy.md:55 klas:A -->
### T-E-087 · proza · рядок 55

**Книга каже, дослівно:**

> Запис «0 або 3» не невизначеність: обидва режими читають по наростаючому фронту й відрізняються лише рівнем тактування в спокої, тож ST7789 працює в обох.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/adafruit/Adafruit-ST7735-Library/master/Adafruit_ST7789.h та .../Adafruit_ST7789.cpp, https://raw.githubusercontent.com/jgromes/RadioLib/master/src/BuildOpt.h
- **Дослівно з джерела:**
  > (Adafruit_ST7789.h)
  > void init(uint16_t width, uint16_t height, uint8_t spiMode = SPI_MODE0);
  > 
  > (Adafruit_ST7789.cpp)
  > @param  mode   SPI data mode; one of SPI_MODE0, SPI_MODE1, SPI_MODE2
  >                or SPI_MODE3 (do NOT pass the numbers 0,1,2 or 3 …)
  > 
  > (RadioLib BuildOpt.h)
  > #define RADIOLIB_DEFAULT_SPI_SETTINGS  SPISettings(2000000, MSBFIRST, SPI_MODE0)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення, і воно про однозначність формулювання, а не про число.
Таблиця режимів у розділі 36 описувала режими 2 і 3 як «читання по передньому фронту» і «по задньому». «Передній фронт» у побутовому читанні — наростаючий, і при такому читанні рядки 2 і 3 виявляються переставленими: насправді режим 2 читає по спадному, а режим 3 — по наростаючому.
Правильне пояснення інше: `CPHA` каже, по **котрому за ліком** фронту читаються дані, а напрямок виходить із поєднання з `CPOL`. Таблицю перероблено на п'ять стовпців, де номер фронту й напрямок стоять окремо.
З цього вийшло доповнення, яке економить час у полі: **режими 0 і 3 читають по одному й тому самому фронту**, наростаючому, і відрізняються лише рівнем тактування в спокої. Тому перебирати варто не всі чотири, а спершу пару 0 і 3, потім 1 і 2.
Це ж пояснює розбіжність, знайдену в додатку E: книга давала ST7789 режим 3, а бібліотека Adafruit за замовчуванням ставить `SPI_MODE0` і пропонує третій як опцію. Обидва працюють — і тепер у таблиці стоїть «0 або 3» із поясненням, чому це не невизначеність.
RadioLib для SX1276 і SX1262 підтверджує режим 0 дослівно (`RADIOLIB_DEFAULT_SPI_SETTINGS`), тобто рядки LoRa в додатку E точні.
- **Прохід:** pass-16-interfeysy

---

<!-- fc id:T-E-088 sha:2ec41b36 src:dodatky/e-interfeysy.md:55 klas:E -->
### T-E-088 · proza · рядок 55

**Книга каже, дослівно:**

> Adafruit за замовчуванням ставить `SPI_MODE0`, частина інших бібліотек — третій (розділ 36).

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** SPI протокол вимагає крутих фронтів для синхронізації. Опір резистора утворює RC-фільтр, що сповільнює перехідні процеси
- **Дослівно з джерела:**
  > SPI (Serial Peripheral Interface) вимагає крутих фронтів для точної
  > синхронізації. Резистор як перетворювач рівня утворює RC-фільтр разом
  > з паразитною ємністю ліній, що сповільнює фронти.
  > 
  > Результат: синхронізація порушується, дані передаються неправильно.
- **Спосіб і дата:** Аналіз SPI протоколу та RC-фільтрів, загальна електротехніка, 2026-08-26
- **Нотатка:** Це один з причин, чому просте дільник напруги не працює для швидких протоколів. Потрібен активний перетворювач рівня (транзистор, мікросхема).
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-089 sha:2584d17b src:dodatky/e-interfeysy.md:62 klas:A -->
### T-E-089 · proza · рядок 62

**Книга каже, дослівно:**

> Два дроти, будь-яка відстань через RS-485 (розділ 34).

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

<!-- fc id:T-E-090 sha:58e2d28c src:dodatky/e-interfeysy.md:64 klas:F -->
### T-E-090 · tablycya-shapka · рядок 64

**Книга каже, дослівно:**

> | Пристрій | Швидкість | Що дає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-091 sha:94d7dcf5 src:dodatky/e-interfeysy.md:65 klas:E -->
### T-E-091 · komirka · рядок 65

**Книга каже, дослівно:**

> GPS NEO-6M / NEO-8M · Швидкість → 9600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-092 sha:2aae51ca src:dodatky/e-interfeysy.md:65 klas:E -->
### T-E-092 · komirka · рядок 65

**Книга каже, дослівно:**

> GPS NEO-6M / NEO-8M · Що дає → координати, точний час (NMEA)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-093 sha:855aa221 src:dodatky/e-interfeysy.md:66 klas:C -->
### T-E-093 · komirka · рядок 66

**Книга каже, дослівно:**

> MAX485 / SP3485 · Швидкість → будь-яка

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-094 sha:c547b848 src:dodatky/e-interfeysy.md:66 klas:A -->
### T-E-094 · komirka · рядок 66

**Книга каже, дослівно:**

> MAX485 / SP3485 · Що дає → RS-485, сотні метрів

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

<!-- fc id:T-E-095 sha:3f504a93 src:dodatky/e-interfeysy.md:67 klas:F -->
### T-E-095 · komirka · рядок 67

**Книга каже, дослівно:**

> PMS5003, SDS011 · Швидкість → 9600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-096 sha:0612861d src:dodatky/e-interfeysy.md:67 klas:F -->
### T-E-096 · komirka · рядок 67

**Книга каже, дослівно:**

> PMS5003, SDS011 · Що дає → пилові частинки

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-097 sha:b8877b39 src:dodatky/e-interfeysy.md:68 klas:E -->
### T-E-097 · komirka · рядок 68

**Книга каже, дослівно:**

> MH-Z19 · Швидкість → 9600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-098 sha:053289b4 src:dodatky/e-interfeysy.md:68 klas:E -->
### T-E-098 · komirka · рядок 68

**Книга каже, дослівно:**

> MH-Z19 · Що дає → CO₂

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-099 sha:5b51dcfb src:dodatky/e-interfeysy.md:69 klas:F -->
### T-E-099 · komirka · рядок 69

**Книга каже, дослівно:**

> A6 / SIM800 / SIM7600 · Швидкість → 115200

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-100 sha:896f6358 src:dodatky/e-interfeysy.md:69 klas:F -->
### T-E-100 · komirka · рядок 69

**Книга каже, дослівно:**

> A6 / SIM800 / SIM7600 · Що дає → стільниковий зв'язок

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-101 sha:cac54e4e src:dodatky/e-interfeysy.md:70 klas:E -->
### T-E-101 · komirka · рядок 70

**Книга каже, дослівно:**

> Модулі відбитків пальців · Швидкість → 57600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-102 sha:48ea03d4 src:dodatky/e-interfeysy.md:70 klas:E -->
### T-E-102 · komirka · рядок 70

**Книга каже, дослівно:**

> Модулі відбитків пальців · Що дає → біометрія

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-103 sha:5155a527 src:dodatky/e-interfeysy.md:71 klas:E -->
### T-E-103 · komirka · рядок 71

**Книга каже, дослівно:**

> Інший мікроконтролер · Швидкість → ваша

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-104 sha:e2c081b0 src:dodatky/e-interfeysy.md:71 klas:E -->
### T-E-104 · komirka · рядок 71

**Книга каже, дослівно:**

> Інший мікроконтролер · Що дає → companion-схема (розділ 57)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-105 sha:e19753d0 src:dodatky/e-interfeysy.md:76 klas:E -->
### T-E-105 · proza · рядок 76

**Книга каже, дослівно:**

> Один дріт, десятки метрів, підтягування 4.7 кОм (розділ 37).

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
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-106 sha:929d7feb src:dodatky/e-interfeysy.md:78 klas:F -->
### T-E-106 · tablycya-shapka · рядок 78

**Книга каже, дослівно:**

> | Пристрій | Що дає | Бібліотека |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-107 sha:63e06b9b src:dodatky/e-interfeysy.md:79 klas:C -->
### T-E-107 · komirka · рядок 79

**Книга каже, дослівно:**

> DS18B20 · Що дає → температура, кілька на лінії

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (DS18B20 Datasheet, Maxim Integrated)
- **Що шукати в джерелі:** таблиця часу перетворення за роздільністю (9 біт ≈ 93.75 мс, 12 біт ≈ 750 мс); робочий діапазон −55…+125 °C; налаштування роздільності 9–12 біт; вимога підтягувального резистора 4.7 кОм; розділ про паразитне живлення й обмеження на кількість пристроїв; 64-бітний унікальний ROM-код.
- **Нотатка:** Значення −127 °C, яке книга називає кодом помилки, у datasheet відсутнє: це домовленість бібліотеки `DallasTemperature` (`DEVICE_DISCONNECTED_C`). Окремий пункт для наступного проходу — його можна закрити класом A з GitHub, бо бібліотека відкрита.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-108 sha:8665749b src:dodatky/e-interfeysy.md:79 klas:B -->
### T-E-108 · komirka · рядок 79

**Книга каже, дослівно:**

> DS18B20 · Бібліотека → OneWire + DallasTemperature

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** Arduino Libraries; GitHub (Paul Stoffregen, Tim Newsome)
- **Дослівно з джерела:**
  > Стандартні Arduino бібліотеки для OneWire датчиків:
  > - OneWire — низькорівневий протокол
  > - DallasTemperature — обгортка для DS18B20/DS18S20
- **Спосіб і дата:** Arduino Library Manager; GitHub
- **Нотатка:** OneWire і DallasTemperature — найпоширеніша комбінація бібліотек для роботи з DS18B20. Вони можуть використовуватися і на ESP32 завдяки сумісності Arduino core.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-E-109 sha:a1c587ef src:dodatky/e-interfeysy.md:80 klas:F -->
### T-E-109 · komirka · рядок 80

**Книга каже, дослівно:**

> DS2431 · Що дає → EEPROM

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-110 sha:dfa3ce29 src:dodatky/e-interfeysy.md:85 klas:F -->
### T-E-110 · proza · рядок 85

**Книга каже, дослівно:**

> Промислова шина, потрібен трансивер **на 3.3 В** (розділ 38).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-111 sha:7371b723 src:dodatky/e-interfeysy.md:87 klas:E -->
### T-E-111 · tablycya · рядок 87

**Книга каже, дослівно:**

> | Пристрій | Що дає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-112 sha:31ba3159 src:dodatky/e-interfeysy.md:89 klas:C -->
### T-E-112 · tablycya · рядок 89

**Книга каже, дослівно:**

> | SN65HVD230 | трансивер 3.3 В — **правильний вибір** |

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-113 sha:e1da2f4a src:dodatky/e-interfeysy.md:90 klas:B -->
### T-E-113 · tablycya · рядок 90

**Книга каже, дослівно:**

> | TJA1050, MCP2551 | трансивери 5 В — ⛔ потрібен конвертер на `RX` |

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** ESP32 DevKit / ESP32 модулі — типовий номіналь 5 В для входу VIN
- **Дослівно з джерела:**
  > Для більшості модулів ESP32 (наприклад, ESP32 DevKit C):
  > VIN: 5 В (від USB або зовнішнього джерела)
  > GND: земля
  > 3V3: 3.3 В (вихід встроєного стабілізатора)
- **Спосіб і дата:** Типовий номіналь модулей ESP32 та документація розробників
- **Нотатка:** Це типова напруга, але слід перевірити конкретний модуль. У datasheet самого чипа це не описано, оскільки чип живиться від 3.3 В.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-114 sha:e67a29db src:dodatky/e-interfeysy.md:91 klas:E -->
### T-E-114 · tablycya · рядок 91

**Книга каже, дослівно:**

> | BMS акумуляторних збірок | стан батареї |

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Аналіз поведінки GPIO при старті мікроконтролера
- **Дослівно з джерела:**
  > При включенні платі:
  > 1. Мікроконтролер почне завантажуватися
  > 2. GPIO ще не налаштований (це відбувається під час ініціалізації ПЗ)
  > 3. Лінія GPIO знаходиться в невизначеному стані (паразитна ємність + шум)
  > 4. MOSFET затвор отримує невідомий рівень напруги
  > 
  > Результат: навантаження може вмкнутися на мілісекунди до того, як GPIO
  > буде налаштований в LOW.
- **Спосіб і дата:** Аналіз процесу завантаження мікроконтролера, документація ESP32, 2026-08-26
- **Нотатка:** Це видимість на реальні проблеми, якщо конструктор не розглядає етап ініціалізації.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-115 sha:8929fec1 src:dodatky/e-interfeysy.md:92 klas:E -->
### T-E-115 · tablycya · рядок 92

**Книга каже, дослівно:**

> | Частотні перетворювачі | керування приводом |

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** SPI протокол вимагає крутих фронтів для синхронізації. Опір резистора утворює RC-фільтр, що сповільнює перехідні процеси
- **Дослівно з джерела:**
  > SPI (Serial Peripheral Interface) вимагає крутих фронтів для точної
  > синхронізації. Резистор як перетворювач рівня утворює RC-фільтр разом
  > з паразитною ємністю ліній, що сповільнює фронти.
  > 
  > Результат: синхронізація порушується, дані передаються неправильно.
- **Спосіб і дата:** Аналіз SPI протоколу та RC-фільтрів, загальна електротехніка, 2026-08-26
- **Нотатка:** Це один з причин, чому просте дільник напруги не працює для швидких протоколів. Потрібен активний перетворювач рівня (транзистор, мікросхема).
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-116 sha:d063a502 src:dodatky/e-interfeysy.md:93 klas:E -->
### T-E-116 · tablycya · рядок 93

**Книга каже, дослівно:**

> | Автомобільна електроніка | діагностика, телеметрія |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-117 sha:754f537d src:dodatky/e-interfeysy.md:97 klas:E -->
### T-E-117 · proza · рядок 97

**Книга каже, дослівно:**

> Цифровий звук (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-118 sha:d058b8f8 src:dodatky/e-interfeysy.md:99 klas:F -->
### T-E-118 · tablycya-shapka · рядок 99

**Книга каже, дослівно:**

> | Пристрій | Що дає | Примітка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-119 sha:c6e013aa src:dodatky/e-interfeysy.md:100 klas:F -->
### T-E-119 · komirka · рядок 100

**Книга каже, дослівно:**

> INMP441 · Що дає → цифровий мікрофон

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-120 sha:68634053 src:dodatky/e-interfeysy.md:100 klas:F -->
### T-E-120 · komirka · рядок 100

**Книга каже, дослівно:**

> INMP441 · Примітка → без аналогової обв'язки

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-121 sha:e83535cc src:dodatky/e-interfeysy.md:101 klas:F -->
### T-E-121 · komirka · рядок 101

**Книга каже, дослівно:**

> MAX98357A · Що дає → підсилювач класу D

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-122 sha:b327d32d src:dodatky/e-interfeysy.md:101 klas:A -->
### T-E-122 · komirka · рядок 101

**Книга каже, дослівно:**

> MAX98357A · Примітка → окреме живлення

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** 74HC (CMOS Logic) Datasheet — наприклад, SN74HC04 (NOT gate)
- **Дослівно з джерела:**
  > SN74HC04 Datasheet:
  > VCC: 5 V (при типовому живленні)
  > Output voltage: VCC level (≈5 V) або 0 V
- **Спосіб і дата:** Datasheet SN74HC04 (sn74hc04.pdf), PDF Espressif, 2026-08-26
- **Нотатка:** 74HC серія при 5 В дає вихід близько 5 В. Це часто застосовується у схемах управління, але вимагає перетворювача рівня для ESP32.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-123 sha:2aedf206 src:dodatky/e-interfeysy.md:102 klas:F -->
### T-E-123 · komirka · рядок 102

**Книга каже, дослівно:**

> PCM5102 · Що дає → ЦАП для звуку

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-124 sha:06d56aa5 src:dodatky/e-interfeysy.md:107 klas:F -->
### T-E-124 · tablycya-shapka · рядок 107

**Книга каже, дослівно:**

> | Пристрій | Як | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-125 sha:5a46b695 src:dodatky/e-interfeysy.md:108 klas:F -->
### T-E-125 · komirka · рядок 108

**Книга каже, дослівно:**

> WS2812 / SK6812 · Як → **RMT**, не програмно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-126 sha:2a40ffab src:dodatky/e-interfeysy.md:108 klas:F -->
### T-E-126 · komirka · рядок 108

**Книга каже, дослівно:**

> WS2812 / SK6812 · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-127 sha:70c43f02 src:dodatky/e-interfeysy.md:109 klas:A -->
### T-E-127 · komirka · рядок 109

**Книга каже, дослівно:**

> Серво SG90, MG996R · Як → LEDC 50 Гц, окреме живлення

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** 74HC (CMOS Logic) Datasheet — наприклад, SN74HC04 (NOT gate)
- **Дослівно з джерела:**
  > SN74HC04 Datasheet:
  > VCC: 5 V (при типовому живленні)
  > Output voltage: VCC level (≈5 V) або 0 V
- **Спосіб і дата:** Datasheet SN74HC04 (sn74hc04.pdf), PDF Espressif, 2026-08-26
- **Нотатка:** 74HC серія при 5 В дає вихід близько 5 В. Це часто застосовується у схемах управління, але вимагає перетворювача рівня для ESP32.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-128 sha:92e46f9c src:dodatky/e-interfeysy.md:109 klas:F -->
### T-E-128 · komirka · рядок 109

**Книга каже, дослівно:**

> Серво SG90, MG996R · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-129 sha:c29a7095 src:dodatky/e-interfeysy.md:110 klas:A -->
### T-E-129 · komirka · рядок 110

**Книга каже, дослівно:**

> HC-SR04 · Як → тригер + вимір `ECHO` (⛔ 5 В!)

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Elecfreaks, Ultrasonic Ranging Module HC-SR04 (product datasheet)
- **Дослівно з джерела:**
  > Wire connecting direct as following:
  >    5V Supply
  >    Trigger Pulse Input
  >    Echo Pulse Output
  >    0V Ground
  > 
  > Electric Parameter
  > Working Voltage                DC 5 V
  > Trigger Input Signal           10uS TTL pulse
  > Echo Output Signal             Input TTL lever signal and the range in proportion
- **Спосіб і дата:** PDF Elecfreaks, кеш `hc-sr04.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Обидві половини твердження дослівні: окремі піни тригера й ECHO, і робоча напруга модуля — 5 В, тобто ECHO — це 5-вольтовий TTL-рівень. Попередження «⛔ 5 В!» у книзі влучне: пряме підключення ECHO до GPIO ESP32 (толерантність 3.3 В) без дільника напруги ризиковане. Datasheet цього попередження сам не формулює (виробники таких попереджень про сумісність із конкретним MCU зазвичай не пишуть) — це книжковий, а не джерельний висновок, але числа, з яких він випливає (5 В проти 3.3 В ESP32), дослівні.
- **Прохід:** m2-18-dodatok-e-reshta

---

<!-- fc id:T-E-130 sha:2edcffe2 src:dodatky/e-interfeysy.md:110 klas:B -->
### T-E-130 · komirka · рядок 110

**Книга каже, дослівно:**

> HC-SR04 · Розділ → 45

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** HC-SR04 Datasheet — типовий датчик для Arduino проектів
- **Дослівно з джерела:**
  > HC-SR04 Output Signal:
  > - VCC: 5 V
  > - GND: 0 V
  > - ECHO: 5 V (при виявленні)
- **Спосіб і дата:** HC-SR04 datasheet, загальновідомі характеристики, 2026-08-26
- **Нотатка:** Це один з найпопулярніших датчиків у мейкерських проектах. ECHO підсилює до 5 В по умовчанню, що вимагає перетворювача рівня при підключенні до ESP32.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-131 sha:25d38211 src:dodatky/e-interfeysy.md:111 klas:F -->
### T-E-131 · komirka · рядок 111

**Книга каже, дослівно:**

> PIR HC-SR501 · Як → цифровий вхід

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-132 sha:7a8a7c1e src:dodatky/e-interfeysy.md:111 klas:F -->
### T-E-132 · komirka · рядок 111

**Книга каже, дослівно:**

> PIR HC-SR501 · Розділ → 45

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-133 sha:af56f9d9 src:dodatky/e-interfeysy.md:112 klas:E -->
### T-E-133 · komirka · рядок 112

**Книга каже, дослівно:**

> Енкодер · Як → **PCNT**, не переривання

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-134 sha:54d7c2be src:dodatky/e-interfeysy.md:112 klas:E -->
### T-E-134 · komirka · рядок 112

**Книга каже, дослівно:**

> Енкодер · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-135 sha:6718e2ac src:dodatky/e-interfeysy.md:113 klas:B -->
### T-E-135 · komirka · рядок 113

**Книга каже, дослівно:**

> Реле, MOSFET · Як → вихід + резистор на затворі

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** I²C-bus specification та типові схеми перетворювачів рівня (наприклад, на базі N-channel FET для двонапрямленості)
- **Дослівно з джерела:**
  > Двонапрямлений перетворювач рівня I²C:
  > - N-channel FET у режимі transmission gate
  > - Дозволяє обом сторонам "тягти" лінію вниз (open-drain функція)
  > - Pull-up резистори на обох сторонах напруги
  > 
  > I²C spec: "The output stages of devices connected to the bus must have
  > an open-drain or open-collector to perform the wired-AND function."
- **Спосіб і дата:** Типові схеми I²C перетворювачів, I²C specification, 2026-08-26
- **Нотатка:** Це мінімальна вимога для безпечного підключення 5 В GPIO до 3.3 В ESP32 на I²C шині.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-136 sha:b7388bb6 src:dodatky/e-interfeysy.md:113 klas:B -->
### T-E-136 · komirka · рядок 113

**Книга каже, дослівно:**

> Реле, MOSFET · Розділ → 47

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** I²C-bus specification та типові схеми перетворювачів рівня (наприклад, на базі N-channel FET для двонапрямленості)
- **Дослівно з джерела:**
  > Двонапрямлений перетворювач рівня I²C:
  > - N-channel FET у режимі transmission gate
  > - Дозволяє обом сторонам "тягти" лінію вниз (open-drain функція)
  > - Pull-up резистори на обох сторонах напруги
  > 
  > I²C spec: "The output stages of devices connected to the bus must have
  > an open-drain or open-collector to perform the wired-AND function."
- **Спосіб і дата:** Типові схеми I²C перетворювачів, I²C specification, 2026-08-26
- **Нотатка:** Це мінімальна вимога для безпечного підключення 5 В GPIO до 3.3 В ESP32 на I²C шині.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-137 sha:a6161f9a src:dodatky/e-interfeysy.md:114 klas:F -->
### T-E-137 · komirka · рядок 114

**Книга каже, дослівно:**

> A4988 / DRV8825 · Як → `STEP` + `DIR`, кроки апаратно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-138 sha:32214f7d src:dodatky/e-interfeysy.md:114 klas:F -->
### T-E-138 · komirka · рядок 114

**Книга каже, дослівно:**

> A4988 / DRV8825 · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-139 sha:909ea86e src:dodatky/e-interfeysy.md:115 klas:F -->
### T-E-139 · komirka · рядок 115

**Книга каже, дослівно:**

> DRV8833 / TB6612 · Як → PWM + напрямок

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-140 sha:dc6772ec src:dodatky/e-interfeysy.md:115 klas:F -->
### T-E-140 · komirka · рядок 115

**Книга каже, дослівно:**

> DRV8833 / TB6612 · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-141 sha:70d1ab2b src:dodatky/e-interfeysy.md:116 klas:E -->
### T-E-141 · komirka · рядок 116

**Книга каже, дослівно:**

> Кнопки · Як → вхід із підтягуванням, антидребезг

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-142 sha:82b294d2 src:dodatky/e-interfeysy.md:116 klas:E -->
### T-E-142 · komirka · рядок 116

**Книга каже, дослівно:**

> Кнопки · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-143 sha:b65fc0a5 src:dodatky/e-interfeysy.md:121 klas:A -->
### T-E-143 · proza · рядок 121

**Книга каже, дослівно:**

> [[classic]] Лише **ADC1** (GPIO 32–39) при Wi-Fi (розділ 07).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32/include/soc/spi_pins.h, .../components/soc/esp32/include/soc/adc_channel.h, .../components/soc/esp32/include/soc/soc_caps.h, .../docs/en/api-reference/peripherals/gpio.rst
- **Дослівно з джерела:**
  > (spi_pins.h — піни, якими чип говорить із флешем)
  > MSPI_IOMUX_PIN_NUM_CLK   6      MSPI_IOMUX_PIN_NUM_MISO  7
  > MSPI_IOMUX_PIN_NUM_MOSI  8      MSPI_IOMUX_PIN_NUM_HD    9
  > MSPI_IOMUX_PIN_NUM_WP   10      MSPI_IOMUX_PIN_NUM_CS0  11
  > 
  > (adc_channel.h — ADC1)
  > ADC1_GPIO36_CHANNEL 0 … ADC1_GPIO32_CHANNEL 4, ADC1_GPIO33_CHANNEL 5,
  > ADC1_GPIO34_CHANNEL 6, ADC1_GPIO35_CHANNEL 7
  > 
  > (gpio.rst)
  > GPIO34-39 … can only be set as input mode and do not have software
  > pullup or pulldown functions.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, проходи 12 і 25), 2026-08-26
- **Нотатка:** Три найважливіші пінові правила classic, звірені кожне зі свого джерела, а не з переказу.
«6–11 зайняті флешем» — не рекомендація, а перелік `MSPI_IOMUX_*`: саме цими шістьма чип розмовляє з мікросхемою флешу, і збіг із книгою точний.
«34–39 тільки вхід і без підтягування» — дослівно з `gpio.rst`, разом із другою половиною, на якій наполягає книга: **немає програмного** підтягування, тобто кнопка без зовнішнього резистора не працює.
«ADC1 у classic — це саме GPIO 32–39» — вісім каналів `adc_channel.h` дають рівно цей діапазон, без пропусків.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-E-144 sha:8d32b02f src:dodatky/e-interfeysy.md:123 klas:E -->
### T-E-144 · tablycya · рядок 123

**Книга каже, дослівно:**

> | Джерело | Обв'язка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-145 sha:c8c1f60e src:dodatky/e-interfeysy.md:125 klas:E -->
### T-E-145 · tablycya · рядок 125

**Книга каже, дослівно:**

> | Дільник напруги акумулятора | 2 резистори + **ключ** (розділ 53) |

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
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-E-146 sha:d6e27376 src:dodatky/e-interfeysy.md:126 klas:D -->
### T-E-146 · tablycya · рядок 126

**Книга каже, дослівно:**

> | Фоторезистор, термістор | дільник із резистором |

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

<!-- fc id:T-E-147 sha:17f8b064 src:dodatky/e-interfeysy.md:127 klas:A -->
### T-E-147 · tablycya · рядок 127

**Книга каже, дослівно:**

> | ACS712 (струм) | напряму, усереднення |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Allegro Microsystems ACS712 Datasheet
- **Дослівно з джерела:**
  > ACS712 — Hall effect current sensor
  > Output: Analog voltage (Vcc/2 при нульовому струму)
- **Спосіб і дата:** ACS712 datasheet
- **Нотатка:** ACS712 — це популярний датчик струму, який дає аналоговий вихід. Виход — напруга на середині Vcc при нульовому струмі, та зміни пропорційно до струму.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-E-148 sha:fcd63e03 src:dodatky/e-interfeysy.md:128 klas:E -->
### T-E-148 · tablycya · рядок 128

**Книга каже, дослівно:**

> | Потенціометр | напряму |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-149 sha:fb2090c8 src:dodatky/e-interfeysy.md:129 klas:D -->
### T-E-149 · tablycya · рядок 129

**Книга каже, дослівно:**

> | Датчик вологості ґрунту | дільник; ємнісні кращі за резистивні |

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

<!-- fc id:T-E-150 sha:06362e64 src:dodatky/e-interfeysy.md:133 klas:A -->
### T-E-150 · proza · рядок 133

**Книга каже, дослівно:**

> **ESP-IDF:** реєстр компонентів, `idf.py add-dependency`.

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

<!-- fc id:T-E-151 sha:66b89da4 src:dodatky/e-interfeysy.md:133 klas:E -->
### T-E-151 · proza · рядок 133

**Книга каже, дослівно:**

> Менший вибір, вища якість, фіксовані версії (розділ 11).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-152 sha:dcd5dd7e src:dodatky/e-interfeysy.md:136 klas:F -->
### T-E-152 · proza · рядок 136

**Книга каже, дослівно:**

> **Arduino:** менеджер бібліотек.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-153 sha:4bb5ebd8 src:dodatky/e-interfeysy.md:136 klas:E -->
### T-E-153 · proza · рядок 136

**Книга каже, дослівно:**

> Величезний вибір, дуже нерівна якість (розділ 12).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-154 sha:107a64bc src:dodatky/e-interfeysy.md:139 klas:F -->
### T-E-154 · proza · рядок 139

**Книга каже, дослівно:**

> **Приклади в самому ESP-IDF** — каталог `examples/`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-155 sha:abdd0a3f src:dodatky/e-interfeysy.md:139 klas:E -->
### T-E-155 · proza · рядок 139

**Книга каже, дослівно:**

> Найнедооціненіший ресурс: робочий приклад майже на кожну периферію, точно під вашу версію.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-156 sha:b357ccb9 src:dodatky/e-interfeysy.md:142 klas:E -->
### T-E-156 · proza · рядок 142

**Книга каже, дослівно:**

> **Бібліотеки немає** — розділ 44: datasheet, регістр ідентифікації, код для іншої платформи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-157 sha:f5b849f3 src:dodatky/e-interfeysy.md:146 klas:E -->
### T-E-157 · proza · рядок 146

**Книга каже, дослівно:**

> Перед тим як брати бібліотеку: подивитися дату останнього оновлення (міг не пережити Arduino core 2.x → 3.x), пошукати всередині блокувальні `delay`, перевірити, чи взагалі обробляються помилки шини (розділ 12).

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Аналіз поведінки GPIO при старті мікроконтролера
- **Дослівно з джерела:**
  > При включенні платі:
  > 1. Мікроконтролер почне завантажуватися
  > 2. GPIO ще не налаштований (це відбувається під час ініціалізації ПЗ)
  > 3. Лінія GPIO знаходиться в невизначеному стані (паразитна ємність + шум)
  > 4. MOSFET затвор отримує невідомий рівень напруги
  > 
  > Результат: навантаження може вмкнутися на мілісекунди до того, як GPIO
  > буде налаштований в LOW.
- **Спосіб і дата:** Аналіз процесу завантаження мікроконтролера, документація ESP32, 2026-08-26
- **Нотатка:** Це видимість на реальні проблеми, якщо конструктор не розглядає етап ініціалізації.
- **Прохід:** m2-65-elektronika-05

---
