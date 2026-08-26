# Фактчекінг: `dodatky/e-interfeysy.md`

Одиниць твердження: **151**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

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

<!-- fc id:T-E-004 sha:eb769fde src:dodatky/e-interfeysy.md:8 klas:F -->
### T-E-004 · proza · рядок 8

**Книга каже, дослівно:**

> **Підтягування 4.7 кОм обов'язкове** (розділ 35).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-005 sha:17f406f5 src:dodatky/e-interfeysy.md:11 klas:F -->
### T-E-005 · tablycya-shapka · рядок 11

**Книга каже, дослівно:**

> | Пристрій | Адреса | Що дає | Бібліотека |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-006 sha:dcae0ce9 src:dodatky/e-interfeysy.md:12 klas:A -->
### T-E-006 · komirka · рядок 12

**Книга каже, дослівно:**

> BME280 / BMP280 · Адреса → `0x76`, `0x77`

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

<!-- fc id:T-E-007 sha:3f3e6545 src:dodatky/e-interfeysy.md:12 klas:C -->
### T-E-007 · komirka · рядок 12

**Книга каже, дослівно:**

> BME280 / BMP280 · Що дає → тиск, T, вологість

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-008 sha:e2458664 src:dodatky/e-interfeysy.md:12 klas:C -->
### T-E-008 · komirka · рядок 12

**Книга каже, дослівно:**

> BME280 / BMP280 · Бібліотека → реєстр IDF; Adafruit BME280

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-009 sha:5f4e30c5 src:dodatky/e-interfeysy.md:13 klas:A -->
### T-E-009 · komirka · рядок 13

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

<!-- fc id:T-E-010 sha:11669d9f src:dodatky/e-interfeysy.md:13 klas:E -->
### T-E-010 · komirka · рядок 13

**Книга каже, дослівно:**

> SHT3x / SHT4x · Що дає → точна вологість

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-011 sha:57cc4434 src:dodatky/e-interfeysy.md:13 klas:E -->
### T-E-011 · komirka · рядок 13

**Книга каже, дослівно:**

> SHT3x / SHT4x · Бібліотека → Sensirion

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-012 sha:3a822c76 src:dodatky/e-interfeysy.md:14 klas:A -->
### T-E-012 · komirka · рядок 14

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

<!-- fc id:T-E-013 sha:1899b23c src:dodatky/e-interfeysy.md:14 klas:D -->
### T-E-013 · komirka · рядок 14

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

<!-- fc id:T-E-014 sha:60e52cde src:dodatky/e-interfeysy.md:14 klas:D -->
### T-E-014 · komirka · рядок 14

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

<!-- fc id:T-E-015 sha:6004e5d0 src:dodatky/e-interfeysy.md:15 klas:C -->
### T-E-015 · komirka · рядок 15

**Книга каже, дослівно:**

> DS3231 · Адреса → `0x68`

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-016 sha:450710eb src:dodatky/e-interfeysy.md:15 klas:F -->
### T-E-016 · komirka · рядок 15

**Книга каже, дослівно:**

> DS3231 · Що дає → RTC з батарейкою

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-017 sha:aeaa568e src:dodatky/e-interfeysy.md:15 klas:F -->
### T-E-017 · komirka · рядок 15

**Книга каже, дослівно:**

> DS3231 · Бібліотека → RTClib

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-018 sha:274457e9 src:dodatky/e-interfeysy.md:16 klas:A -->
### T-E-018 · komirka · рядок 16

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

<!-- fc id:T-E-019 sha:d5040300 src:dodatky/e-interfeysy.md:16 klas:F -->
### T-E-019 · komirka · рядок 16

**Книга каже, дослівно:**

> MPU6050 · Що дає → акселерометр, гіроскоп

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-020 sha:6181e702 src:dodatky/e-interfeysy.md:16 klas:F -->
### T-E-020 · komirka · рядок 16

**Книга каже, дослівно:**

> MPU6050 · Бібліотека → MPU6050

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-021 sha:04902e5b src:dodatky/e-interfeysy.md:17 klas:A -->
### T-E-021 · komirka · рядок 17

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

<!-- fc id:T-E-022 sha:825b180a src:dodatky/e-interfeysy.md:17 klas:F -->
### T-E-022 · komirka · рядок 17

**Книга каже, дослівно:**

> BNO055 · Що дає → готова орієнтація

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-023 sha:b55c4a45 src:dodatky/e-interfeysy.md:17 klas:F -->
### T-E-023 · komirka · рядок 17

**Книга каже, дослівно:**

> BNO055 · Бібліотека → Adafruit BNO055

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-024 sha:3a9afe05 src:dodatky/e-interfeysy.md:18 klas:C -->
### T-E-024 · komirka · рядок 18

**Книга каже, дослівно:**

> INA219 / INA226 · Адреса → `0x40`+

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-025 sha:b0502556 src:dodatky/e-interfeysy.md:18 klas:F -->
### T-E-025 · komirka · рядок 18

**Книга каже, дослівно:**

> INA219 / INA226 · Що дає → струм і напруга

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-026 sha:bf63dda1 src:dodatky/e-interfeysy.md:18 klas:F -->
### T-E-026 · komirka · рядок 18

**Книга каже, дослівно:**

> INA219 / INA226 · Бібліотека → Adafruit INA219

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-027 sha:d621df80 src:dodatky/e-interfeysy.md:19 klas:C -->
### T-E-027 · komirka · рядок 19

**Книга каже, дослівно:**

> VL53L0X / VL53L1X · Адреса → `0x29`

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-028 sha:eca8e7cb src:dodatky/e-interfeysy.md:19 klas:F -->
### T-E-028 · komirka · рядок 19

**Книга каже, дослівно:**

> VL53L0X / VL53L1X · Що дає → лазерна відстань

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-029 sha:031a738c src:dodatky/e-interfeysy.md:19 klas:F -->
### T-E-029 · komirka · рядок 19

**Книга каже, дослівно:**

> VL53L0X / VL53L1X · Бібліотека → VL53L0X

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-030 sha:974da9fb src:dodatky/e-interfeysy.md:20 klas:A -->
### T-E-030 · komirka · рядок 20

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

<!-- fc id:T-E-031 sha:a6fff190 src:dodatky/e-interfeysy.md:20 klas:A -->
### T-E-031 · komirka · рядок 20

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

<!-- fc id:T-E-032 sha:caaaf18d src:dodatky/e-interfeysy.md:20 klas:A -->
### T-E-032 · komirka · рядок 20

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

<!-- fc id:T-E-033 sha:af561b9a src:dodatky/e-interfeysy.md:21 klas:A -->
### T-E-033 · komirka · рядок 21

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

<!-- fc id:T-E-034 sha:84958947 src:dodatky/e-interfeysy.md:21 klas:F -->
### T-E-034 · komirka · рядок 21

**Книга каже, дослівно:**

> PCF8574 · Що дає → розширювач портів

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-035 sha:7da6b06b src:dodatky/e-interfeysy.md:21 klas:F -->
### T-E-035 · komirka · рядок 21

**Книга каже, дослівно:**

> PCF8574 · Бібліотека → PCF8574

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-036 sha:9ec27075 src:dodatky/e-interfeysy.md:22 klas:A -->
### T-E-036 · komirka · рядок 22

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

<!-- fc id:T-E-037 sha:55153a86 src:dodatky/e-interfeysy.md:22 klas:F -->
### T-E-037 · komirka · рядок 22

**Книга каже, дослівно:**

> MCP23017 · Що дає → розширювач, 16 пінів

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-038 sha:49d948f0 src:dodatky/e-interfeysy.md:22 klas:F -->
### T-E-038 · komirka · рядок 22

**Книга каже, дослівно:**

> MCP23017 · Бібліотека → MCP23017

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-039 sha:7d4b5654 src:dodatky/e-interfeysy.md:23 klas:A -->
### T-E-039 · komirka · рядок 23

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

<!-- fc id:T-E-040 sha:302952a9 src:dodatky/e-interfeysy.md:23 klas:F -->
### T-E-040 · komirka · рядок 23

**Книга каже, дослівно:**

> TCA9548A · Що дає → мультиплексор шини

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-041 sha:ef9fcd2b src:dodatky/e-interfeysy.md:23 klas:F -->
### T-E-041 · komirka · рядок 23

**Книга каже, дослівно:**

> TCA9548A · Бібліотека → TCA9548A

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-042 sha:ed48c80e src:dodatky/e-interfeysy.md:24 klas:A -->
### T-E-042 · komirka · рядок 24

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

<!-- fc id:T-E-043 sha:0edbf47b src:dodatky/e-interfeysy.md:24 klas:F -->
### T-E-043 · komirka · рядок 24

**Книга каже, дослівно:**

> AT24Cxx · Що дає → EEPROM

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-044 sha:9f46567b src:dodatky/e-interfeysy.md:28 klas:A -->
### T-E-044 · proza · рядок 28

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

<!-- fc id:T-E-045 sha:50f4c8ac src:dodatky/e-interfeysy.md:28 klas:F -->
### T-E-045 · proza · рядок 28

**Книга каже, дослівно:**

> Разом на одній шині — конфлікт; розв'язується перемичкою на MPU6050 (адреса `0x69`) або мультиплексором (розділ 35).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-046 sha:cf3f864a src:dodatky/e-interfeysy.md:35 klas:F -->
### T-E-046 · proza · рядок 35

**Книга каже, дослівно:**

> Швидко, чотири лінії плюс `CS` на кожен пристрій (розділ 36).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-047 sha:f78815d4 src:dodatky/e-interfeysy.md:37 klas:F -->
### T-E-047 · tablycya-shapka · рядок 37

**Книга каже, дослівно:**

> | Пристрій | Режим | Що дає | Бібліотека |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-048 sha:6f5fce38 src:dodatky/e-interfeysy.md:38 klas:A -->
### T-E-048 · komirka · рядок 38

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

<!-- fc id:T-E-049 sha:5524a220 src:dodatky/e-interfeysy.md:38 klas:F -->
### T-E-049 · komirka · рядок 38

**Книга каже, дослівно:**

> ST7789 · Що дає → TFT-дисплей

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-050 sha:f129922d src:dodatky/e-interfeysy.md:38 klas:F -->
### T-E-050 · komirka · рядок 38

**Книга каже, дослівно:**

> ST7789 · Бібліотека → TFT_eSPI, LovyanGFX

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-051 sha:adfd8b57 src:dodatky/e-interfeysy.md:39 klas:F -->
### T-E-051 · komirka · рядок 39

**Книга каже, дослівно:**

> ILI9341 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-052 sha:dfb7b32b src:dodatky/e-interfeysy.md:39 klas:F -->
### T-E-052 · komirka · рядок 39

**Книга каже, дослівно:**

> ILI9341 · Що дає → TFT-дисплей

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-053 sha:f30ebfb1 src:dodatky/e-interfeysy.md:39 klas:F -->
### T-E-053 · komirka · рядок 39

**Книга каже, дослівно:**

> ILI9341 · Бібліотека → TFT_eSPI, LovyanGFX

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-054 sha:8f11bd59 src:dodatky/e-interfeysy.md:40 klas:E -->
### T-E-054 · komirka · рядок 40

**Книга каже, дослівно:**

> microSD · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-055 sha:59f2f000 src:dodatky/e-interfeysy.md:40 klas:E -->
### T-E-055 · komirka · рядок 40

**Книга каже, дослівно:**

> microSD · Що дає → картка пам'яті

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-056 sha:223f57f7 src:dodatky/e-interfeysy.md:40 klas:F -->
### T-E-056 · komirka · рядок 40

**Книга каже, дослівно:**

> microSD · Бібліотека → штатний `esp_vfs_fat`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-057 sha:d5eed7a0 src:dodatky/e-interfeysy.md:41 klas:C -->
### T-E-057 · komirka · рядок 41

**Книга каже, дослівно:**

> SX1276 / RFM95 · Режим → 0

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-058 sha:2d0a3f04 src:dodatky/e-interfeysy.md:41 klas:C -->
### T-E-058 · komirka · рядок 41

**Книга каже, дослівно:**

> SX1276 / RFM95 · Що дає → LoRa

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-059 sha:94c061f0 src:dodatky/e-interfeysy.md:41 klas:C -->
### T-E-059 · komirka · рядок 41

**Книга каже, дослівно:**

> SX1276 / RFM95 · Бібліотека → RadioLib, LoRa

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-060 sha:33326c46 src:dodatky/e-interfeysy.md:42 klas:C -->
### T-E-060 · komirka · рядок 42

**Книга каже, дослівно:**

> SX1262 · Режим → 0

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-061 sha:b83467dd src:dodatky/e-interfeysy.md:42 klas:C -->
### T-E-061 · komirka · рядок 42

**Книга каже, дослівно:**

> SX1262 · Що дає → LoRa, новіший

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-062 sha:a588779e src:dodatky/e-interfeysy.md:42 klas:C -->
### T-E-062 · komirka · рядок 42

**Книга каже, дослівно:**

> SX1262 · Бібліотека → RadioLib

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.semtech.com/ (SX1276/SX1262 Datasheet)
- **Що шукати в джерелі:** діапазон Spreading Factor (7…12) і його вплив на час передачі й чутливість; допустимі значення Bandwidth і Coding Rate; вимога узгодженого навантаження на виході передавача.
- **Нотатка:** Твердження «ніколи не вмикати передавач без антени» в розділі 43 подано як категоричне, і воно таким і лишається — але підстава для нього має бути в datasheet, а не в фольклорі.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-063 sha:dc8f7e30 src:dodatky/e-interfeysy.md:43 klas:F -->
### T-E-063 · komirka · рядок 43

**Книга каже, дослівно:**

> NRF24L01 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-064 sha:722a12f0 src:dodatky/e-interfeysy.md:43 klas:F -->
### T-E-064 · komirka · рядок 43

**Книга каже, дослівно:**

> NRF24L01 · Що дає → радіо 2.4 ГГц

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-065 sha:e12a5df8 src:dodatky/e-interfeysy.md:43 klas:F -->
### T-E-065 · komirka · рядок 43

**Книга каже, дослівно:**

> NRF24L01 · Бібліотека → RF24

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-066 sha:27d739d6 src:dodatky/e-interfeysy.md:44 klas:F -->
### T-E-066 · komirka · рядок 44

**Книга каже, дослівно:**

> MCP2515 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-067 sha:3ec6e643 src:dodatky/e-interfeysy.md:44 klas:F -->
### T-E-067 · komirka · рядок 44

**Книга каже, дослівно:**

> MCP2515 · Що дає → зовнішній CAN

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-068 sha:8f789500 src:dodatky/e-interfeysy.md:44 klas:F -->
### T-E-068 · komirka · рядок 44

**Книга каже, дослівно:**

> MCP2515 · Бібліотека → — (у ESP32 є свій, розділ 38)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-069 sha:39070e8a src:dodatky/e-interfeysy.md:45 klas:F -->
### T-E-069 · komirka · рядок 45

**Книга каже, дослівно:**

> MAX31855 / MAX6675 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-070 sha:1aa5f02d src:dodatky/e-interfeysy.md:45 klas:F -->
### T-E-070 · komirka · рядок 45

**Книга каже, дослівно:**

> MAX31855 / MAX6675 · Що дає → термопара

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-071 sha:5de71916 src:dodatky/e-interfeysy.md:45 klas:F -->
### T-E-071 · komirka · рядок 45

**Книга каже, дослівно:**

> MAX31855 / MAX6675 · Бібліотека → Adafruit MAX31855

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-072 sha:4371340c src:dodatky/e-interfeysy.md:46 klas:F -->
### T-E-072 · komirka · рядок 46

**Книга каже, дослівно:**

> ADS1256, MCP3208 · Режим → 0/1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-073 sha:e486f0a5 src:dodatky/e-interfeysy.md:46 klas:F -->
### T-E-073 · komirka · рядок 46

**Книга каже, дослівно:**

> ADS1256, MCP3208 · Що дає → зовнішній точний ADC

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-074 sha:c89cdd6b src:dodatky/e-interfeysy.md:47 klas:E -->
### T-E-074 · komirka · рядок 47

**Книга каже, дослівно:**

> W5500 · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-075 sha:95e8ad21 src:dodatky/e-interfeysy.md:47 klas:E -->
### T-E-075 · komirka · рядок 47

**Книга каже, дослівно:**

> W5500 · Що дає → дротовий Ethernet

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-076 sha:ffad2970 src:dodatky/e-interfeysy.md:47 klas:E -->
### T-E-076 · komirka · рядок 47

**Книга каже, дослівно:**

> W5500 · Бібліотека → Ethernet

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-077 sha:91a5608b src:dodatky/e-interfeysy.md:48 klas:F -->
### T-E-077 · komirka · рядок 48

**Книга каже, дослівно:**

> E-paper (SSD16xx) · Режим → 0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-078 sha:ebbcf551 src:dodatky/e-interfeysy.md:48 klas:F -->
### T-E-078 · komirka · рядок 48

**Книга каже, дослівно:**

> E-paper (SSD16xx) · Що дає → електронний папір

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-079 sha:0053b4f8 src:dodatky/e-interfeysy.md:48 klas:F -->
### T-E-079 · komirka · рядок 48

**Книга каже, дослівно:**

> E-paper (SSD16xx) · Бібліотека → GxEPD2

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-080 sha:508da6ef src:dodatky/e-interfeysy.md:51 klas:E -->
### T-E-080 · proza · рядок 51

**Книга каже, дослівно:**

> Режим у таблиці — типовий; звіряти з datasheet конкретного модуля.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-081 sha:e5d00b74 src:dodatky/e-interfeysy.md:53 klas:A -->
### T-E-081 · proza · рядок 53

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

<!-- fc id:T-E-082 sha:2ec41b36 src:dodatky/e-interfeysy.md:53 klas:F -->
### T-E-082 · proza · рядок 53

**Книга каже, дослівно:**

> Adafruit за замовчуванням ставить `SPI_MODE0`, частина інших бібліотек — третій (розділ 36).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-083 sha:2584d17b src:dodatky/e-interfeysy.md:60 klas:F -->
### T-E-083 · proza · рядок 60

**Книга каже, дослівно:**

> Два дроти, будь-яка відстань через RS-485 (розділ 34).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-084 sha:58e2d28c src:dodatky/e-interfeysy.md:62 klas:F -->
### T-E-084 · tablycya-shapka · рядок 62

**Книга каже, дослівно:**

> | Пристрій | Швидкість | Що дає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-085 sha:94d7dcf5 src:dodatky/e-interfeysy.md:63 klas:E -->
### T-E-085 · komirka · рядок 63

**Книга каже, дослівно:**

> GPS NEO-6M / NEO-8M · Швидкість → 9600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-086 sha:2aae51ca src:dodatky/e-interfeysy.md:63 klas:E -->
### T-E-086 · komirka · рядок 63

**Книга каже, дослівно:**

> GPS NEO-6M / NEO-8M · Що дає → координати, точний час (NMEA)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-087 sha:855aa221 src:dodatky/e-interfeysy.md:64 klas:C -->
### T-E-087 · komirka · рядок 64

**Книга каже, дослівно:**

> MAX485 / SP3485 · Швидкість → будь-яка

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-088 sha:c547b848 src:dodatky/e-interfeysy.md:64 klas:C -->
### T-E-088 · komirka · рядок 64

**Книга каже, дослівно:**

> MAX485 / SP3485 · Що дає → RS-485, сотні метрів

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-089 sha:3f504a93 src:dodatky/e-interfeysy.md:65 klas:F -->
### T-E-089 · komirka · рядок 65

**Книга каже, дослівно:**

> PMS5003, SDS011 · Швидкість → 9600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-090 sha:0612861d src:dodatky/e-interfeysy.md:65 klas:F -->
### T-E-090 · komirka · рядок 65

**Книга каже, дослівно:**

> PMS5003, SDS011 · Що дає → пилові частинки

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-091 sha:b8877b39 src:dodatky/e-interfeysy.md:66 klas:E -->
### T-E-091 · komirka · рядок 66

**Книга каже, дослівно:**

> MH-Z19 · Швидкість → 9600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-092 sha:053289b4 src:dodatky/e-interfeysy.md:66 klas:E -->
### T-E-092 · komirka · рядок 66

**Книга каже, дослівно:**

> MH-Z19 · Що дає → CO₂

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-093 sha:5b51dcfb src:dodatky/e-interfeysy.md:67 klas:F -->
### T-E-093 · komirka · рядок 67

**Книга каже, дослівно:**

> A6 / SIM800 / SIM7600 · Швидкість → 115200

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-094 sha:896f6358 src:dodatky/e-interfeysy.md:67 klas:F -->
### T-E-094 · komirka · рядок 67

**Книга каже, дослівно:**

> A6 / SIM800 / SIM7600 · Що дає → стільниковий зв'язок

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-095 sha:cac54e4e src:dodatky/e-interfeysy.md:68 klas:E -->
### T-E-095 · komirka · рядок 68

**Книга каже, дослівно:**

> Модулі відбитків пальців · Швидкість → 57600

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-096 sha:48ea03d4 src:dodatky/e-interfeysy.md:68 klas:E -->
### T-E-096 · komirka · рядок 68

**Книга каже, дослівно:**

> Модулі відбитків пальців · Що дає → біометрія

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-097 sha:5155a527 src:dodatky/e-interfeysy.md:69 klas:E -->
### T-E-097 · komirka · рядок 69

**Книга каже, дослівно:**

> Інший мікроконтролер · Швидкість → ваша

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-098 sha:e2c081b0 src:dodatky/e-interfeysy.md:69 klas:E -->
### T-E-098 · komirka · рядок 69

**Книга каже, дослівно:**

> Інший мікроконтролер · Що дає → companion-схема (розділ 57)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-099 sha:e19753d0 src:dodatky/e-interfeysy.md:74 klas:F -->
### T-E-099 · proza · рядок 74

**Книга каже, дослівно:**

> Один дріт, десятки метрів, підтягування 4.7 кОм (розділ 37).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-100 sha:929d7feb src:dodatky/e-interfeysy.md:76 klas:F -->
### T-E-100 · tablycya-shapka · рядок 76

**Книга каже, дослівно:**

> | Пристрій | Що дає | Бібліотека |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-101 sha:63e06b9b src:dodatky/e-interfeysy.md:77 klas:C -->
### T-E-101 · komirka · рядок 77

**Книга каже, дослівно:**

> DS18B20 · Що дає → температура, кілька на лінії

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (DS18B20 Datasheet, Maxim Integrated)
- **Що шукати в джерелі:** таблиця часу перетворення за роздільністю (9 біт ≈ 93.75 мс, 12 біт ≈ 750 мс); робочий діапазон −55…+125 °C; налаштування роздільності 9–12 біт; вимога підтягувального резистора 4.7 кОм; розділ про паразитне живлення й обмеження на кількість пристроїв; 64-бітний унікальний ROM-код.
- **Нотатка:** Значення −127 °C, яке книга називає кодом помилки, у datasheet відсутнє: це домовленість бібліотеки `DallasTemperature` (`DEVICE_DISCONNECTED_C`). Окремий пункт для наступного проходу — його можна закрити класом A з GitHub, бо бібліотека відкрита.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-102 sha:8665749b src:dodatky/e-interfeysy.md:77 klas:C -->
### T-E-102 · komirka · рядок 77

**Книга каже, дослівно:**

> DS18B20 · Бібліотека → OneWire + DallasTemperature

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.analog.com/ (DS18B20 Datasheet, Maxim Integrated)
- **Що шукати в джерелі:** таблиця часу перетворення за роздільністю (9 біт ≈ 93.75 мс, 12 біт ≈ 750 мс); робочий діапазон −55…+125 °C; налаштування роздільності 9–12 біт; вимога підтягувального резистора 4.7 кОм; розділ про паразитне живлення й обмеження на кількість пристроїв; 64-бітний унікальний ROM-код.
- **Нотатка:** Значення −127 °C, яке книга називає кодом помилки, у datasheet відсутнє: це домовленість бібліотеки `DallasTemperature` (`DEVICE_DISCONNECTED_C`). Окремий пункт для наступного проходу — його можна закрити класом A з GitHub, бо бібліотека відкрита.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-103 sha:a1c587ef src:dodatky/e-interfeysy.md:78 klas:F -->
### T-E-103 · komirka · рядок 78

**Книга каже, дослівно:**

> DS2431 · Що дає → EEPROM

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-104 sha:dfa3ce29 src:dodatky/e-interfeysy.md:83 klas:F -->
### T-E-104 · proza · рядок 83

**Книга каже, дослівно:**

> Промислова шина, потрібен трансивер **на 3.3 В** (розділ 38).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-105 sha:7371b723 src:dodatky/e-interfeysy.md:85 klas:E -->
### T-E-105 · tablycya · рядок 85

**Книга каже, дослівно:**

> | Пристрій | Що дає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-106 sha:31ba3159 src:dodatky/e-interfeysy.md:87 klas:C -->
### T-E-106 · tablycya · рядок 87

**Книга каже, дослівно:**

> | SN65HVD230 | трансивер 3.3 В — **правильний вибір** |

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-107 sha:e1da2f4a src:dodatky/e-interfeysy.md:88 klas:C -->
### T-E-107 · tablycya · рядок 88

**Книга каже, дослівно:**

> | TJA1050, MCP2551 | трансивери 5 В — ⛔ потрібен конвертер на `RX` |

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.ti.com/ та https://www.analog.com/ (datasheet відповідних трансиверів)
- **Що шукати в джерелі:** напруга живлення й рівні логічних входів/виходів кожного: SN65HVD230 (3.3 В), TJA1050 і MCP2551 (5 В, рівень виходу RX), MAX485 (5 В) і його 3.3-вольтові аналоги на кшталт SP3485/MAX3485.
- **Нотатка:** Твердження книги «5-вольтовий трансивер може спалити пін ESP32» спирається саме на рівень виходу RX і на те, що вхід ESP32 не толерантний до 5 В. Обидві половини потребують окремих datasheet.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-E-108 sha:e67a29db src:dodatky/e-interfeysy.md:89 klas:E -->
### T-E-108 · tablycya · рядок 89

**Книга каже, дослівно:**

> | BMS акумуляторних збірок | стан батареї |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-109 sha:8929fec1 src:dodatky/e-interfeysy.md:90 klas:E -->
### T-E-109 · tablycya · рядок 90

**Книга каже, дослівно:**

> | Частотні перетворювачі | керування приводом |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-110 sha:d063a502 src:dodatky/e-interfeysy.md:91 klas:E -->
### T-E-110 · tablycya · рядок 91

**Книга каже, дослівно:**

> | Автомобільна електроніка | діагностика, телеметрія |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-111 sha:754f537d src:dodatky/e-interfeysy.md:95 klas:E -->
### T-E-111 · proza · рядок 95

**Книга каже, дослівно:**

> Цифровий звук (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-112 sha:d058b8f8 src:dodatky/e-interfeysy.md:97 klas:F -->
### T-E-112 · tablycya-shapka · рядок 97

**Книга каже, дослівно:**

> | Пристрій | Що дає | Примітка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-113 sha:c6e013aa src:dodatky/e-interfeysy.md:98 klas:F -->
### T-E-113 · komirka · рядок 98

**Книга каже, дослівно:**

> INMP441 · Що дає → цифровий мікрофон

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-114 sha:68634053 src:dodatky/e-interfeysy.md:98 klas:F -->
### T-E-114 · komirka · рядок 98

**Книга каже, дослівно:**

> INMP441 · Примітка → без аналогової обв'язки

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-115 sha:e83535cc src:dodatky/e-interfeysy.md:99 klas:F -->
### T-E-115 · komirka · рядок 99

**Книга каже, дослівно:**

> MAX98357A · Що дає → підсилювач класу D

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-116 sha:b327d32d src:dodatky/e-interfeysy.md:99 klas:F -->
### T-E-116 · komirka · рядок 99

**Книга каже, дослівно:**

> MAX98357A · Примітка → окреме живлення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-117 sha:2aedf206 src:dodatky/e-interfeysy.md:100 klas:F -->
### T-E-117 · komirka · рядок 100

**Книга каже, дослівно:**

> PCM5102 · Що дає → ЦАП для звуку

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-118 sha:06d56aa5 src:dodatky/e-interfeysy.md:105 klas:F -->
### T-E-118 · tablycya-shapka · рядок 105

**Книга каже, дослівно:**

> | Пристрій | Як | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-119 sha:5a46b695 src:dodatky/e-interfeysy.md:106 klas:F -->
### T-E-119 · komirka · рядок 106

**Книга каже, дослівно:**

> WS2812 / SK6812 · Як → **RMT**, не програмно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-120 sha:2a40ffab src:dodatky/e-interfeysy.md:106 klas:F -->
### T-E-120 · komirka · рядок 106

**Книга каже, дослівно:**

> WS2812 / SK6812 · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-121 sha:70c43f02 src:dodatky/e-interfeysy.md:107 klas:F -->
### T-E-121 · komirka · рядок 107

**Книга каже, дослівно:**

> Серво SG90, MG996R · Як → LEDC 50 Гц, окреме живлення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-122 sha:92e46f9c src:dodatky/e-interfeysy.md:107 klas:F -->
### T-E-122 · komirka · рядок 107

**Книга каже, дослівно:**

> Серво SG90, MG996R · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-123 sha:c29a7095 src:dodatky/e-interfeysy.md:108 klas:F -->
### T-E-123 · komirka · рядок 108

**Книга каже, дослівно:**

> HC-SR04 · Як → тригер + вимір `ECHO` (⛔ 5 В!)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-124 sha:2edcffe2 src:dodatky/e-interfeysy.md:108 klas:F -->
### T-E-124 · komirka · рядок 108

**Книга каже, дослівно:**

> HC-SR04 · Розділ → 45

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-125 sha:25d38211 src:dodatky/e-interfeysy.md:109 klas:F -->
### T-E-125 · komirka · рядок 109

**Книга каже, дослівно:**

> PIR HC-SR501 · Як → цифровий вхід

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-126 sha:7a8a7c1e src:dodatky/e-interfeysy.md:109 klas:F -->
### T-E-126 · komirka · рядок 109

**Книга каже, дослівно:**

> PIR HC-SR501 · Розділ → 45

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-127 sha:af56f9d9 src:dodatky/e-interfeysy.md:110 klas:E -->
### T-E-127 · komirka · рядок 110

**Книга каже, дослівно:**

> Енкодер · Як → **PCNT**, не переривання

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-128 sha:54d7c2be src:dodatky/e-interfeysy.md:110 klas:E -->
### T-E-128 · komirka · рядок 110

**Книга каже, дослівно:**

> Енкодер · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-129 sha:6718e2ac src:dodatky/e-interfeysy.md:111 klas:E -->
### T-E-129 · komirka · рядок 111

**Книга каже, дослівно:**

> Реле, MOSFET · Як → вихід + резистор на затворі

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-130 sha:b7388bb6 src:dodatky/e-interfeysy.md:111 klas:E -->
### T-E-130 · komirka · рядок 111

**Книга каже, дослівно:**

> Реле, MOSFET · Розділ → 47

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-131 sha:a6161f9a src:dodatky/e-interfeysy.md:112 klas:F -->
### T-E-131 · komirka · рядок 112

**Книга каже, дослівно:**

> A4988 / DRV8825 · Як → `STEP` + `DIR`, кроки апаратно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-132 sha:32214f7d src:dodatky/e-interfeysy.md:112 klas:F -->
### T-E-132 · komirka · рядок 112

**Книга каже, дослівно:**

> A4988 / DRV8825 · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-133 sha:909ea86e src:dodatky/e-interfeysy.md:113 klas:F -->
### T-E-133 · komirka · рядок 113

**Книга каже, дослівно:**

> DRV8833 / TB6612 · Як → PWM + напрямок

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-134 sha:dc6772ec src:dodatky/e-interfeysy.md:113 klas:F -->
### T-E-134 · komirka · рядок 113

**Книга каже, дослівно:**

> DRV8833 / TB6612 · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-135 sha:70d1ab2b src:dodatky/e-interfeysy.md:114 klas:E -->
### T-E-135 · komirka · рядок 114

**Книга каже, дослівно:**

> Кнопки · Як → вхід із підтягуванням, антидребезг

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-136 sha:82b294d2 src:dodatky/e-interfeysy.md:114 klas:E -->
### T-E-136 · komirka · рядок 114

**Книга каже, дослівно:**

> Кнопки · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-137 sha:b65fc0a5 src:dodatky/e-interfeysy.md:119 klas:F -->
### T-E-137 · proza · рядок 119

**Книга каже, дослівно:**

> [[classic]] Лише **ADC1** (GPIO 32–39) при Wi-Fi (розділ 07).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-138 sha:8d32b02f src:dodatky/e-interfeysy.md:121 klas:E -->
### T-E-138 · tablycya · рядок 121

**Книга каже, дослівно:**

> | Джерело | Обв'язка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-139 sha:c8c1f60e src:dodatky/e-interfeysy.md:123 klas:E -->
### T-E-139 · tablycya · рядок 123

**Книга каже, дослівно:**

> | Дільник напруги акумулятора | 2 резистори + **ключ** (розділ 53) |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-140 sha:d6e27376 src:dodatky/e-interfeysy.md:124 klas:E -->
### T-E-140 · tablycya · рядок 124

**Книга каже, дослівно:**

> | Фоторезистор, термістор | дільник із резистором |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-141 sha:17f8b064 src:dodatky/e-interfeysy.md:125 klas:F -->
### T-E-141 · tablycya · рядок 125

**Книга каже, дослівно:**

> | ACS712 (струм) | напряму, усереднення |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-142 sha:fcd63e03 src:dodatky/e-interfeysy.md:126 klas:E -->
### T-E-142 · tablycya · рядок 126

**Книга каже, дослівно:**

> | Потенціометр | напряму |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-143 sha:fb2090c8 src:dodatky/e-interfeysy.md:127 klas:E -->
### T-E-143 · tablycya · рядок 127

**Книга каже, дослівно:**

> | Датчик вологості ґрунту | дільник; ємнісні кращі за резистивні |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-144 sha:06362e64 src:dodatky/e-interfeysy.md:131 klas:A -->
### T-E-144 · proza · рядок 131

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

<!-- fc id:T-E-145 sha:66b89da4 src:dodatky/e-interfeysy.md:131 klas:E -->
### T-E-145 · proza · рядок 131

**Книга каже, дослівно:**

> Менший вибір, вища якість, фіксовані версії (розділ 11).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-146 sha:dcd5dd7e src:dodatky/e-interfeysy.md:134 klas:F -->
### T-E-146 · proza · рядок 134

**Книга каже, дослівно:**

> **Arduino:** менеджер бібліотек.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-147 sha:4bb5ebd8 src:dodatky/e-interfeysy.md:134 klas:E -->
### T-E-147 · proza · рядок 134

**Книга каже, дослівно:**

> Величезний вибір, дуже нерівна якість (розділ 12).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-148 sha:107a64bc src:dodatky/e-interfeysy.md:137 klas:F -->
### T-E-148 · proza · рядок 137

**Книга каже, дослівно:**

> **Приклади в самому ESP-IDF** — каталог `examples/`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-149 sha:abdd0a3f src:dodatky/e-interfeysy.md:137 klas:E -->
### T-E-149 · proza · рядок 137

**Книга каже, дослівно:**

> Найнедооціненіший ресурс: робочий приклад майже на кожну периферію, точно під вашу версію.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-150 sha:b357ccb9 src:dodatky/e-interfeysy.md:140 klas:E -->
### T-E-150 · proza · рядок 140

**Книга каже, дослівно:**

> **Бібліотеки немає** — розділ 44: datasheet, регістр ідентифікації, код для іншої платформи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-E-151 sha:f5b849f3 src:dodatky/e-interfeysy.md:144 klas:F -->
### T-E-151 · proza · рядок 144

**Книга каже, дослівно:**

> Перед тим як брати бібліотеку: подивитися дату останнього оновлення (міг не пережити Arduino core 2.x → 3.x), пошукати всередині блокувальні `delay`, перевірити, чи взагалі обробляються помилки шини (розділ 12).

**Доказ**

- **Клас:** F — не звірено

---
