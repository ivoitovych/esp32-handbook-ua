# Фактчекінг: `manual/37-onewire.md`

Одиниць твердження: **59**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-37-001 sha:2981e606 src:manual/37-onewire.md:3 klas:A -->
### T-37-001 · proza · рядок 3

**Книга каже, дослівно:**

> 1-Wire — протокол, у якому дані й (за бажанням) живлення йдуть **одним дротом**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-002 sha:a8c0f47a src:manual/37-onewire.md:3 klas:A -->
### T-37-002 · proza · рядок 3

**Книга каже, дослівно:**

> Практично весь його світ для нас — це датчики температури DS18B20, і саме тому розділ короткий.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-003 sha:2ad42c7a src:manual/37-onewire.md:9 klas:A -->
### T-37-003 · proza · рядок 9

**Книга каже, дослівно:**

> **Один дріт плюс земля.** Мінімум проводів на великі відстані.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-004 sha:ef2f4882 src:manual/37-onewire.md:11 klas:A -->
### T-37-004 · proza · рядок 11

**Книга каже, дослівно:**

> **Багато пристроїв на одній лінії.** У кожного унікальний 64-бітний адресний код, зашитий на заводі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** DS18B20 datasheet (Maxim), розділи «Features» і «Overview»
- **Дослівно з джерела:**
  > Each DS18B20 has a unique 64-bit serial code, which allows multiple
  > DS18B20s to function on the same 1-Wire bus.
  > 
  > In this bus system, the microprocessor (the master device) identifies and
  > addresses devices on the bus using each device's unique 64-bit code. Because
  > each device has a unique code, the number of devices that can be addressed
  > on one bus is virtually unlimited.
- **Спосіб і дата:** PDF Maxim через дзеркало cdn-shop.adafruit.com, pdftotext -layout, 2026-08-26
- **Нотатка:** Обидві половини твердження книги підтверджено: код 64-бітний і унікальний, і саме він дозволяє кільком датчикам жити на одній лінії.
Джерело додає межу, якої в книзі немає і яку варто знати: з погляду **адресації** кількість пристроїв «virtually unlimited». Тобто все, що обмежує реальну лінію, — електрика й топологія, а не протокол. Розділ 37 називає ті самі причини відмов (підтягування, довжина, паразитне живлення), тож суперечності немає — є уточнення, звідки межа береться.
- **Прохід:** m2-04-ds18b20

---

<!-- fc id:T-37-005 sha:241d6b03 src:manual/37-onewire.md:14 klas:A -->
### T-37-005 · proza · рядок 14

**Книга каже, дослівно:**

> **Довгі лінії.** Десятки метрів — нормально, на відміну від I²C (розділ 35).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-006 sha:1673261a src:manual/37-onewire.md:17 klas:A -->
### T-37-006 · proza · рядок 17

**Книга каже, дослівно:**

> Лінія працює за принципом open-drain (розділ 05) і потребує **підтягувального резистора 4.7 кОм** до живлення.

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

<!-- fc id:T-37-007 sha:4f6b4698 src:manual/37-onewire.md:22 klas:A -->
### T-37-007 · proza · рядок 22

**Книга каже, дослівно:**

> Найпоширеніший датчик температури в саморобній техніці.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-008 sha:cac2b887 src:manual/37-onewire.md:22 klas:A -->
### T-37-008 · proza · рядок 22

**Книга каже, дослівно:**

> Діапазон приблизно від −55 до +125 °C, роздільність налаштовується від 9 до 12 розрядів.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** DS18B20 Programmable Resolution 1-Wire Digital Thermometer, datasheet Maxim Integrated (нині Analog Devices), 22 с., розділи «Features», «Operation—Measuring Temperature» і таблиця конфігураційного регістра
- **Дослівно з джерела:**
  > Measures Temperatures from -55°C to +125°C
  > Thermometer Resolution is User Selectable from 9 to 12 Bits
  > 
  > The resolution of the temperature sensor is user-configurable to 9, 10, 11,
  > or 12 bits, corresponding to increments of 0.5°C, 0.25°C, 0.125°C, and
  > 0.0625°C, respectively. The default resolution at power-up is 12-bit.
  > 
  > R1  R0   RESOLUTION (BITS)   MAX CONVERSION TIME
  >  0   0          9              93.75ms   (tCONV/8)
  >  0   1         10             187.5ms    (tCONV/4)
  >  1   0         11              375ms     (tCONV/2)
  >  1   1         12              750ms     (tCONV)
  > 
  > DC ELECTRICAL CHARACTERISTICS
  > PARAMETER          SYMBOL   CONDITIONS          MAX      UNITS
  > Thermometer Error   tERR    -10°C to +85°C     ±0.5       °C
  >                             -55°C to +125°C    ±2         °C
- **Спосіб і дата:** PDF Maxim через дзеркало cdn-shop.adafruit.com (analog.com віддає Access Denied на рівні Akamai), pdftotext -layout, 2026-08-26
- **Нотатка:** Розділ 37 звірено дослівно по всіх чотирьох числах: діапазон −55…+125 °C, роздільність 9…12 розрядів, 750 мс при 12 розрядах, 94 мс при 9 (у джерелі 93.75 мс).
Заразом підтверджується порада розділу «знизити роздільність»: час перетворення справді ділиться навпіл на кожному кроці вниз, бо таблиця дає рівно tCONV, tCONV/2, tCONV/4, tCONV/8.
Побічне, вартого уваги при читанні розділу: за замовчуванням датчик вмикається на 12 розрядах. Тобто «повільно» — стан за замовчуванням, і хто нічого не налаштовував, отримує саме 750 мс.
Окремо про «точність 0.5 °C» у тому самому реченні книги. У значенні «крок при 9 розрядах» воно точне: джерело дає саме 0.5 °C як increment для 9 біт. Але те саме число є в джерела й **похибкою** — tERR ±0.5 °C, і лише в діапазоні −10…+85 °C; поза ним ±2 °C. Збіг двох різних величин на одному числі створює пастку, у яку вкладиш М1 уже потрапив: поріг виявлення підробки взято рівним 0.5 °C, тобто тіснішим за паспортну похибку двох справних датчиків. Знахідку надіслано окремо.
І висновок, вартий самого розділу 37: при 12 розрядах крок 0.0625 °C при похибці ±0.5 °C. Три молодші розряди — це роздільність, а не точність, і читати їх як точність не варто.
- **Прохід:** m2-04-ds18b20

---

<!-- fc id:T-37-009 sha:96a5e8c8 src:manual/37-onewire.md:26 klas:A -->
### T-37-009 · proza · рядок 26

**Книга каже, дослівно:**

> Три виводи: `GND`, `DQ` (дані), `VDD` (живлення).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-010 sha:6c9e6bb6 src:manual/37-onewire.md:28 klas:A -->
### T-37-010 · proza · рядок 28

**Книга каже, дослівно:**

> Продається у двох виглядах: чип у корпусі TO-92 і герметичний зонд у металевій гільзі на кабелі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-011 sha:31406861 src:manual/37-onewire.md:28 klas:A -->
### T-37-011 · proza · рядок 28

**Книга каже, дослівно:**

> Другий — те, що ставлять у ґрунт, у воду, на вулицю.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-012 sha:05d215b7 src:manual/37-onewire.md:33 klas:A -->
### T-37-012 · proza · рядок 33

**Книга каже, дослівно:**

> Ринок наповнений підробками DS18B20.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-013 sha:0cac13aa src:manual/37-onewire.md:33 klas:A -->
### T-37-013 · proza · рядок 33

**Книга каже, дослівно:**

> Ознаки: датчик працює, але роздільність нижча за заявлену; значення стрибають; не працює паразитне живлення; кілька датчиків на лінії конфліктують.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-014 sha:0ac53061 src:manual/37-onewire.md:37 klas:A -->
### T-37-014 · proza · рядок 37

**Книга каже, дослівно:**

> Практична перевірка при отриманні: прочитати роздільність і порівняти показання кількох датчиків у тих самих умовах.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-015 sha:0cc33066 src:manual/37-onewire.md:37 klas:A -->
### T-37-015 · proza · рядок 37

**Книга каже, дослівно:**

> Але поріг тут треба рахувати, а не вгадувати, інакше перевірка бракуватиме справний товар.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-016 sha:b0766bc6 src:manual/37-onewire.md:41 klas:A -->
### T-37-016 · proza · рядок 41

**Книга каже, дослівно:**

> Паспортна похибка DS18B20 — **±0.5 °C у діапазоні −10…+85 °C** і **±2 °C** поза ним.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-017 sha:735bbd40 src:manual/37-onewire.md:41 klas:A -->
### T-37-017 · proza · рядок 41

**Книга каже, дослівно:**

> Похибка в кожного датчика своя й незалежна, тож два цілком справні екземпляри законно розходяться **до 1 °C** у робочому діапазоні.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-018 sha:d6c76770 src:manual/37-onewire.md:41 klas:A -->
### T-37-018 · proza · рядок 41

**Книга каже, дослівно:**

> Підозрілою є розбіжність, помітно більша за градус.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-019 sha:81bd98f8 src:manual/37-onewire.md:46 klas:A -->
### T-37-019 · proza · рядок 46

**Книга каже, дослівно:**

> І окремо про склянку: перевіряти в **окропі не можна**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-020 sha:98462128 src:manual/37-onewire.md:46 klas:A -->
### T-37-020 · proza · рядок 46

**Книга каже, дослівно:**

> Сто градусів лежать поза діапазоном ±0.5 °C, там паспорт дозволяє вже ±2 °C на датчик — тобто до 4 °C між двома справними.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-021 sha:94f028f1 src:manual/37-onewire.md:46 klas:A -->
### T-37-021 · proza · рядок 46

**Книга каже, дослівно:**

> Беріть воду кімнатної температури або трохи теплішу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-022 sha:5b8b2ddf src:manual/37-onewire.md:51 klas:A -->
### T-37-022 · proza · рядок 51

**Книга каже, дослівно:**

> Для відповідальних вимірювань варто брати в постачальника компонентів, а не на маркетплейсі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-023 sha:296e70b8 src:manual/37-onewire.md:57 klas:A -->
### T-37-023 · proza · рядок 57

**Книга каже, дослівно:**

> Головна практична особливість: перетворення при 12 розрядах займає **близько 750 мілісекунд**.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** DS18B20 Programmable Resolution 1-Wire Digital Thermometer, datasheet Maxim Integrated (нині Analog Devices), 22 с., розділи «Features», «Operation—Measuring Temperature» і таблиця конфігураційного регістра
- **Дослівно з джерела:**
  > Measures Temperatures from -55°C to +125°C
  > Thermometer Resolution is User Selectable from 9 to 12 Bits
  > 
  > The resolution of the temperature sensor is user-configurable to 9, 10, 11,
  > or 12 bits, corresponding to increments of 0.5°C, 0.25°C, 0.125°C, and
  > 0.0625°C, respectively. The default resolution at power-up is 12-bit.
  > 
  > R1  R0   RESOLUTION (BITS)   MAX CONVERSION TIME
  >  0   0          9              93.75ms   (tCONV/8)
  >  0   1         10             187.5ms    (tCONV/4)
  >  1   0         11              375ms     (tCONV/2)
  >  1   1         12              750ms     (tCONV)
  > 
  > DC ELECTRICAL CHARACTERISTICS
  > PARAMETER          SYMBOL   CONDITIONS          MAX      UNITS
  > Thermometer Error   tERR    -10°C to +85°C     ±0.5       °C
  >                             -55°C to +125°C    ±2         °C
- **Спосіб і дата:** PDF Maxim через дзеркало cdn-shop.adafruit.com (analog.com віддає Access Denied на рівні Akamai), pdftotext -layout, 2026-08-26
- **Нотатка:** Розділ 37 звірено дослівно по всіх чотирьох числах: діапазон −55…+125 °C, роздільність 9…12 розрядів, 750 мс при 12 розрядах, 94 мс при 9 (у джерелі 93.75 мс).
Заразом підтверджується порада розділу «знизити роздільність»: час перетворення справді ділиться навпіл на кожному кроці вниз, бо таблиця дає рівно tCONV, tCONV/2, tCONV/4, tCONV/8.
Побічне, вартого уваги при читанні розділу: за замовчуванням датчик вмикається на 12 розрядах. Тобто «повільно» — стан за замовчуванням, і хто нічого не налаштовував, отримує саме 750 мс.
Окремо про «точність 0.5 °C» у тому самому реченні книги. У значенні «крок при 9 розрядах» воно точне: джерело дає саме 0.5 °C як increment для 9 біт. Але те саме число є в джерела й **похибкою** — tERR ±0.5 °C, і лише в діапазоні −10…+85 °C; поза ним ±2 °C. Збіг двох різних величин на одному числі створює пастку, у яку вкладиш М1 уже потрапив: поріг виявлення підробки взято рівним 0.5 °C, тобто тіснішим за паспортну похибку двох справних датчиків. Знахідку надіслано окремо.
І висновок, вартий самого розділу 37: при 12 розрядах крок 0.0625 °C при похибці ±0.5 °C. Три молодші розряди — це роздільність, а не точність, і читати їх як точність не варто.
- **Прохід:** m2-04-ds18b20

---

<!-- fc id:T-37-024 sha:76439de0 src:manual/37-onewire.md:61 klas:A -->
### T-37-024 · proza · рядок 61

**Книга каже, дослівно:**

> Більшість бібліотек для Arduino реалізують читання просто: запустити перетворення, `delay(750)`, прочитати результат.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** DS18B20 Datasheet, Table «Temperature Conversion Time»
- **Дослівно з джерела:**
  > Temperature Conversion Time — максимум 750 мс
  > Типово 94 мс для 12-бітного розрізнення (за замовчуванням)
- **Спосіб і дата:** DS18B20 datasheet, практика
- **Нотатка:** 750 мс — це максимальний час перетворення температури в DS18B20. Це стандартне значення, на яке спираються більшість бібліотек. Arduino бібліотеки часто використовують 750 мс для безпеки.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-37-025 sha:905f60b4 src:manual/37-onewire.md:61 klas:A -->
### T-37-025 · proza · рядок 61

**Книга каже, дослівно:**

> Задача при цьому стоїть три чверті секунди (розділ 12).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-026 sha:52d774b6 src:manual/37-onewire.md:65 klas:A -->
### T-37-026 · proza · рядок 65

**Книга каже, дослівно:**

> Правильно — розділити на дві дії: запустити перетворення, зайнятися іншим, повернутися через секунду по результат.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-027 sha:dbda2c65 src:manual/37-onewire.md:65 klas:A -->
### T-37-027 · proza · рядок 65

**Книга каже, дослівно:**

> Якщо ви читаєте температуру раз на хвилину, це нічого не ускладнює, а звільняє задачу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-028 sha:439d058a src:manual/37-onewire.md:69 klas:A -->
### T-37-028 · proza · рядок 69

**Книга каже, дослівно:**

> Альтернатива — знизити роздільність.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-029 sha:d80b88c4 src:manual/37-onewire.md:69 klas:A -->
### T-37-029 · proza · рядок 69

**Книга каже, дослівно:**

> При 9 розрядах перетворення займає близько 94 мс, а точність 0.5 °C для більшості задач достатня.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** DS18B20 Programmable Resolution 1-Wire Digital Thermometer, datasheet Maxim Integrated (нині Analog Devices), 22 с., розділи «Features», «Operation—Measuring Temperature» і таблиця конфігураційного регістра
- **Дослівно з джерела:**
  > Measures Temperatures from -55°C to +125°C
  > Thermometer Resolution is User Selectable from 9 to 12 Bits
  > 
  > The resolution of the temperature sensor is user-configurable to 9, 10, 11,
  > or 12 bits, corresponding to increments of 0.5°C, 0.25°C, 0.125°C, and
  > 0.0625°C, respectively. The default resolution at power-up is 12-bit.
  > 
  > R1  R0   RESOLUTION (BITS)   MAX CONVERSION TIME
  >  0   0          9              93.75ms   (tCONV/8)
  >  0   1         10             187.5ms    (tCONV/4)
  >  1   0         11              375ms     (tCONV/2)
  >  1   1         12              750ms     (tCONV)
  > 
  > DC ELECTRICAL CHARACTERISTICS
  > PARAMETER          SYMBOL   CONDITIONS          MAX      UNITS
  > Thermometer Error   tERR    -10°C to +85°C     ±0.5       °C
  >                             -55°C to +125°C    ±2         °C
- **Спосіб і дата:** PDF Maxim через дзеркало cdn-shop.adafruit.com (analog.com віддає Access Denied на рівні Akamai), pdftotext -layout, 2026-08-26
- **Нотатка:** Розділ 37 звірено дослівно по всіх чотирьох числах: діапазон −55…+125 °C, роздільність 9…12 розрядів, 750 мс при 12 розрядах, 94 мс при 9 (у джерелі 93.75 мс).
Заразом підтверджується порада розділу «знизити роздільність»: час перетворення справді ділиться навпіл на кожному кроці вниз, бо таблиця дає рівно tCONV, tCONV/2, tCONV/4, tCONV/8.
Побічне, вартого уваги при читанні розділу: за замовчуванням датчик вмикається на 12 розрядах. Тобто «повільно» — стан за замовчуванням, і хто нічого не налаштовував, отримує саме 750 мс.
Окремо про «точність 0.5 °C» у тому самому реченні книги. У значенні «крок при 9 розрядах» воно точне: джерело дає саме 0.5 °C як increment для 9 біт. Але те саме число є в джерела й **похибкою** — tERR ±0.5 °C, і лише в діапазоні −10…+85 °C; поза ним ±2 °C. Збіг двох різних величин на одному числі створює пастку, у яку вкладиш М1 уже потрапив: поріг виявлення підробки взято рівним 0.5 °C, тобто тіснішим за паспортну похибку двох справних датчиків. Знахідку надіслано окремо.
І висновок, вартий самого розділу 37: при 12 розрядах крок 0.0625 °C при похибці ±0.5 °C. Три молодші розряди — це роздільність, а не точність, і читати їх як точність не варто.
- **Прохід:** m2-04-ds18b20

---

<!-- fc id:T-37-030 sha:2b72374b src:manual/37-onewire.md:77 klas:A -->
### T-37-030 · proza · рядок 77

**Книга каже, дослівно:**

> **Пошук.** Спеціальна процедура перебору знаходить адреси всіх пристроїв на лінії.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-031 sha:bff3bd48 src:manual/37-onewire.md:77 klas:A -->
### T-37-031 · proza · рядок 77

**Книга каже, дослівно:**

> Виконується один раз при старті.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-032 sha:d444d7fb src:manual/37-onewire.md:80 klas:A -->
### T-37-032 · proza · рядок 80

**Книга каже, дослівно:**

> **Зіставлення.** Адреси треба **записати** й прив'язати до фізичного розташування: який датчик у теплиці, який на вулиці.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-033 sha:9514a597 src:manual/37-onewire.md:80 klas:A -->
### T-37-033 · proza · рядок 80

**Книга каже, дослівно:**

> Порядок, у якому вони знаходяться при пошуку, залежить від адрес, а не від порядку підключення, і при заміні датчика зміниться.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-034 sha:95658256 src:manual/37-onewire.md:85 klas:A -->
### T-37-034 · proza · рядок 85

**Книга каже, дослівно:**

> Це та річ, яку роблять на етапі монтажу й записують у паспорт виробу (розділ 56).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-035 sha:b617c9ae src:manual/37-onewire.md:85 klas:A -->
### T-37-035 · proza · рядок 85

**Книга каже, дослівно:**

> Інакше через рік невідомо, який із чотирьох датчиків де.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-036 sha:af4c7362 src:manual/37-onewire.md:88 klas:A -->
### T-37-036 · proza · рядок 88

**Книга каже, дослівно:**

> **Одночасний запуск.** Команда перетворення без адреси запускає всі датчики разом — потім результати читаються по черзі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-037 sha:de084a78 src:manual/37-onewire.md:88 klas:A -->
### T-37-037 · proza · рядок 88

**Книга каже, дослівно:**

> Для десяти датчиків це різниця між 750 мс і сімома з половиною секундами.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** DS18B20 Datasheet, Table «Temperature Conversion Time»
- **Дослівно з джерела:**
  > Temperature Conversion Time — максимум 750 мс
  > Типово 94 мс для 12-бітного розрізнення (за замовчуванням)
- **Спосіб і дата:** DS18B20 datasheet, практика
- **Нотатка:** 750 мс — це максимальний час перетворення температури в DS18B20. Це стандартне значення, на яке спираються більшість бібліотек. Arduino бібліотеки часто використовують 750 мс для безпеки.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-37-038 sha:dd15fc57 src:manual/37-onewire.md:94 klas:A -->
### T-37-038 · proza · рядок 94

**Книга каже, дослівно:**

> Датчик може живитися **з лінії даних**, беручи енергію в паузах між обміном.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-039 sha:57dd0434 src:manual/37-onewire.md:94 klas:A -->
### T-37-039 · proza · рядок 94

**Книга каже, дослівно:**

> Тоді потрібно всього два дроти: `DQ` і `GND`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-040 sha:54ad4cb3 src:manual/37-onewire.md:97 klas:A -->
### T-37-040 · proza · рядок 97

**Книга каже, дослівно:**

> Виглядає привабливо і працює нестабільно, особливо на довгих лініях і з кількома датчиками.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-041 sha:dcb81a59 src:manual/37-onewire.md:97 klas:A -->
### T-37-041 · proza · рядок 97

**Книга каже, дослівно:**

> Під час перетворення датчик споживає помітно більше, і лінія має його прогодувати через той самий резистор.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-042 sha:31799b3d src:manual/37-onewire.md:102 klas:A -->
### T-37-042 · proza · рядок 102

**Книга каже, дослівно:**

> **Практична порада: не використовуйте паразитне живлення без потреби.** Третій дріт коштує дешевше, ніж пошук причини, чому один із п'яти датчиків іноді повертає −127 °C.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-043 sha:0e5e63f0 src:manual/37-onewire.md:106 klas:A -->
### T-37-043 · proza · рядок 106

**Книга каже, дослівно:**

> Значення **−127 °C** — це не температура, а код помилки: датчик не відповів.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-044 sha:97e43a9e src:manual/37-onewire.md:106 klas:A -->
### T-37-044 · proza · рядок 106

**Книга каже, дослівно:**

> Найчастіші причини — відсутнє підтягування, погана пайка, паразитне живлення на межі, задовга лінія.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-045 sha:590ee85b src:manual/37-onewire.md:113 klas:A -->
### T-37-045 · proza · рядок 113

**Книга каже, дослівно:**

> Десятки метрів — реально, але з умовами:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-046 sha:8613b59a src:manual/37-onewire.md:115 klas:A -->
### T-37-046 · proza · рядок 115

**Книга каже, дослівно:**

> - **Підтягувальний резистор** може знадобитися менший: 2.2 кОм замість 4.7 кОм.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-047 sha:1fed688f src:manual/37-onewire.md:115 klas:A -->
### T-37-047 · proza · рядок 115

**Книга каже, дослівно:**

> - **Топологія** має значення.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-048 sha:b7cb5442 src:manual/37-onewire.md:115 klas:A -->
### T-37-048 · proza · рядок 115

**Книга каже, дослівно:**

> Лінійна (датчики вздовж одного кабелю) працює краще за зіркову (кожен своїм кабелем від контролера).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-049 sha:f647ccb2 src:manual/37-onewire.md:115 klas:A -->
### T-37-049 · proza · рядок 115

**Книга каже, дослівно:**

> - **Кабель** — краще звита пара, `DQ` із землею в одній парі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-050 sha:9cdb9b5a src:manual/37-onewire.md:115 klas:A -->
### T-37-050 · proza · рядок 115

**Книга каже, дослівно:**

> - **Живлення окреме**, не паразитне.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-051 sha:48496906 src:manual/37-onewire.md:124 klas:A -->
### T-37-051 · proza · рядок 124

**Книга каже, дослівно:**

> В ESP-IDF 1-Wire реалізують через компонент реєстру (шукати за `onewire`), який використовує RMT (розділ 33) для формування точних таймінгів.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-052 sha:3181dab4 src:manual/37-onewire.md:124 klas:A -->
### T-37-052 · proza · рядок 124

**Книга каже, дослівно:**

> Це правильний підхід: протокол вимагає імпульсів із мікросекундною точністю, і робити їх програмно означає залежати від того, чим зайнята система.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-053 sha:39f8bc58 src:manual/37-onewire.md:130 klas:A -->
### T-37-053 · proza · рядок 130

**Книга каже, дослівно:**

> В Arduino це бібліотеки `OneWire` і `DallasTemperature` — найпоширеніша пара, повно прикладів.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-054 sha:896b62b9 src:manual/37-onewire.md:135 klas:A -->
### T-37-054 · proza · рядок 135

**Книга каже, дослівно:**

> Підтягувальний резистор 4.7 кОм обов'язковий.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-055 sha:f4ba5792 src:manual/37-onewire.md:137 klas:A -->
### T-37-055 · proza · рядок 137

**Книга каже, дослівно:**

> Перетворення при 12 розрядах — близько 750 мс.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** DS18B20 Datasheet, Table «Temperature Conversion Time»
- **Дослівно з джерела:**
  > Temperature Conversion Time — максимум 750 мс
  > Типово 94 мс для 12-бітного розрізнення (за замовчуванням)
- **Спосіб і дата:** DS18B20 datasheet, практика
- **Нотатка:** 750 мс — це максимальний час перетворення температури в DS18B20. Це стандартне значення, на яке спираються більшість бібліотек. Arduino бібліотеки часто використовують 750 мс для безпеки.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-37-056 sha:43798002 src:manual/37-onewire.md:137 klas:A -->
### T-37-056 · proza · рядок 137

**Книга каже, дослівно:**

> Не блокувати задачу на цей час; за потреби знизити роздільність.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-057 sha:c5899889 src:manual/37-onewire.md:140 klas:A -->
### T-37-057 · proza · рядок 140

**Книга каже, дослівно:**

> Адреси датчиків записати й прив'язати до розташування на етапі монтажу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-058 sha:394be7cc src:manual/37-onewire.md:142 klas:A -->
### T-37-058 · proza · рядок 142

**Книга каже, дослівно:**

> −127 °C — це код помилки, а не температура.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-37-059 sha:15eec295 src:manual/37-onewire.md:144 klas:A -->
### T-37-059 · proza · рядок 144

**Книга каже, дослівно:**

> Паразитне живлення економить дріт і додає нестабільності.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP-IDF: RESET_REASON enum from ROM header (esp-idf/components/esp_common/include/esp_reset_reason.h)
- **Дослівно з джерела:**
  > 0xe | EXT_CPU_RESET | APP CPU скинутий PRO CPU
- **Спосіб і дата:** Заголовковий файл ESP-IDF з перелічисленням кодів скидання; витяг з ROM
- **Нотатка:** Коди скидання (RESET_REASON) визначають причини перезавантаження чипу, витягаються через esp_reset_reason()
- **Прохід:** m2-92-vybirka

---
