# Фактчекінг: `dodatky/b-symptomy.md`

Одиниць твердження: **269**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-B-001 sha:567c1904 src:dodatky/b-symptomy.md:3 klas:E -->
### T-B-001 · proza · рядок 3

**Книга каже, дослівно:**

> Картка [К8](#k-symptomy) — польова верхівка з п'ятнадцяти найчастіших; розгорнутий розбір — розділ 29.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-002 sha:018b7421 src:dodatky/b-symptomy.md:8 klas:E -->
### T-B-002 · proza · рядок 8

**Книга каже, дослівно:**

> **Спершу живлення, потім код.** Більшість «плаваючих багів» — просадка напруги (картка К13).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-003 sha:2ba627c3 src:dodatky/b-symptomy.md:11 klas:E -->
### T-B-003 · proza · рядок 11

**Книга каже, дослівно:**

> **Одна зміна за раз.** Дві зміни — і невідомо, яка допомогла.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-004 sha:d4044ec8 src:dodatky/b-symptomy.md:13 klas:E -->
### T-B-004 · proza · рядок 13

**Книга каже, дослівно:**

> **Мінімальний тест окремо.** Незнайомий модуль — на голій платі з трьома дротами (розділ 44).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-005 sha:56ebed13 src:dodatky/b-symptomy.md:18 klas:F -->
### T-B-005 · tablycya-shapka · рядок 18

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-006 sha:c73ff187 src:dodatky/b-symptomy.md:19 klas:D -->
### T-B-006 · komirka · рядок 19

**Книга каже, дослівно:**

> Порт не з'являється · Причина → кабель без жил даних

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-007 sha:4681cae7 src:dodatky/b-symptomy.md:19 klas:D -->
### T-B-007 · komirka · рядок 19

**Книга каже, дослівно:**

> Порт не з'являється · Дія → інший кабель

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-008 sha:1bbbbfcd src:dodatky/b-symptomy.md:19 klas:D -->
### T-B-008 · komirka · рядок 19

**Книга каже, дослівно:**

> Порт не з'являється · Розділ → 09, К3

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-009 sha:8ace063d src:dodatky/b-symptomy.md:20 klas:D -->
### T-B-009 · komirka · рядок 20

**Книга каже, дослівно:**

> Порт не з'являється · Причина → немає драйвера мосту

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-010 sha:b074e1ee src:dodatky/b-symptomy.md:20 klas:D -->
### T-B-010 · komirka · рядок 20

**Книга каже, дослівно:**

> Порт не з'являється · Дія → CP2102/CH340/**CH9102 окремий**

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-011 sha:bf3faad7 src:dodatky/b-symptomy.md:20 klas:D -->
### T-B-011 · komirka · рядок 20

**Книга каже, дослівно:**

> Порт не з'являється · Розділ → 09

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-012 sha:1479b50d src:dodatky/b-symptomy.md:21 klas:D -->
### T-B-012 · komirka · рядок 21

**Книга каже, дослівно:**

> Порт не з'являється · Причина → відірваний USB-роз'єм

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-013 sha:28ac3abe src:dodatky/b-symptomy.md:21 klas:D -->
### T-B-013 · komirka · рядок 21

**Книга каже, дослівно:**

> Порт не з'являється · Дія → ремонт

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-014 sha:d9c4e5d6 src:dodatky/b-symptomy.md:21 klas:D -->
### T-B-014 · komirka · рядок 21

**Книга каже, дослівно:**

> Порт не з'являється · Розділ → 55

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-015 sha:df070e08 src:dodatky/b-symptomy.md:22 klas:A -->
### T-B-015 · komirka · рядок 22

**Книга каже, дослівно:**

> `Permission denied` · Причина → права

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-016 sha:640a6b84 src:dodatky/b-symptomy.md:22 klas:A -->
### T-B-016 · komirka · рядок 22

**Книга каже, дослівно:**

> `Permission denied` · Дія → група `dialout`, **перезайти**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-017 sha:4d4031cd src:dodatky/b-symptomy.md:22 klas:A -->
### T-B-017 · komirka · рядок 22

**Книга каже, дослівно:**

> `Permission denied` · Розділ → 09

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-018 sha:41ee20e3 src:dodatky/b-symptomy.md:23 klas:A -->
### T-B-018 · komirka · рядок 23

**Книга каже, дослівно:**

> `Device or resource busy` · Причина → порт зайнятий монітором

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-019 sha:4d83c909 src:dodatky/b-symptomy.md:23 klas:A -->
### T-B-019 · komirka · рядок 23

**Книга каже, дослівно:**

> `Device or resource busy` · Дія → закрити монітор

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-020 sha:21296bed src:dodatky/b-symptomy.md:23 klas:A -->
### T-B-020 · komirka · рядок 23

**Книга каже, дослівно:**

> `Device or resource busy` · Розділ → 09

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-021 sha:950686c2 src:dodatky/b-symptomy.md:24 klas:A -->
### T-B-021 · komirka · рядок 24

**Книга каже, дослівно:**

> `Failed to connect` · Причина → не в download mode

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-022 sha:f2c78481 src:dodatky/b-symptomy.md:24 klas:A -->
### T-B-022 · komirka · рядок 24

**Книга каже, дослівно:**

> `Failed to connect` · Дія → `BOOT`+`EN` вручну

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-023 sha:004c9f40 src:dodatky/b-symptomy.md:24 klas:A -->
### T-B-023 · komirka · рядок 24

**Книга каже, дослівно:**

> `Failed to connect` · Розділ → К4

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-024 sha:a97754cc src:dodatky/b-symptomy.md:25 klas:A -->
### T-B-024 · komirka · рядок 25

**Книга каже, дослівно:**

> `Failed to connect` · Причина → зависока швидкість

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-025 sha:00a459db src:dodatky/b-symptomy.md:25 klas:A -->
### T-B-025 · komirka · рядок 25

**Книга каже, дослівно:**

> `Failed to connect` · Дія → `--baud 115200`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-026 sha:270f3bea src:dodatky/b-symptomy.md:25 klas:A -->
### T-B-026 · komirka · рядок 25

**Книга каже, дослівно:**

> `Failed to connect` · Розділ → 17

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-027 sha:f876739b src:dodatky/b-symptomy.md:26 klas:A -->
### T-B-027 · komirka · рядок 26

**Книга каже, дослівно:**

> `Failed to connect` · Причина → обв'язка на strapping-піні

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-028 sha:cac50c5b src:dodatky/b-symptomy.md:26 klas:A -->
### T-B-028 · komirka · рядок 26

**Книга каже, дослівно:**

> `Failed to connect` · Дія → зняти

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-029 sha:2f75783b src:dodatky/b-symptomy.md:26 klas:A -->
### T-B-029 · komirka · рядок 26

**Книга каже, дослівно:**

> `Failed to connect` · Розділ → 16

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-030 sha:997a6b63 src:dodatky/b-symptomy.md:27 klas:A -->
### T-B-030 · komirka · рядок 27

**Книга каже, дослівно:**

> `MD5 of file does not match` · Причина → просадка живлення, кабель

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-031 sha:33ae1bd4 src:dodatky/b-symptomy.md:27 klas:A -->
### T-B-031 · komirka · рядок 27

**Книга каже, дослівно:**

> `MD5 of file does not match` · Дія → коротший кабель, `--baud` нижче

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-032 sha:9303c290 src:dodatky/b-symptomy.md:27 klas:A -->
### T-B-032 · komirka · рядок 27

**Книга каже, дослівно:**

> `MD5 of file does not match` · Розділ → 06

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-033 sha:ea00ff27 src:dodatky/b-symptomy.md:28 klas:A -->
### T-B-033 · komirka · рядок 28

**Книга каже, дослівно:**

> `Invalid head of packet` · Причина → застосунок пише в UART

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-034 sha:79f50ca7 src:dodatky/b-symptomy.md:28 klas:A -->
### T-B-034 · komirka · рядок 28

**Книга каже, дослівно:**

> `Invalid head of packet` · Дія → download mode вручну

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-035 sha:d5a5991c src:dodatky/b-symptomy.md:28 klas:A -->
### T-B-035 · komirka · рядок 28

**Книга каже, дослівно:**

> `Invalid head of packet` · Розділ → 17

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-B-036 sha:cf08f94d src:dodatky/b-symptomy.md:29 klas:A -->
### T-B-036 · komirka · рядок 29

**Книга каже, дослівно:**

> `Failed to start stub flasher` · Причина → клон не приймає stub

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-037 sha:e59b86ec src:dodatky/b-symptomy.md:29 klas:A -->
### T-B-037 · komirka · рядок 29

**Книга каже, дослівно:**

> `Failed to start stub flasher` · Дія → `--no-stub`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-038 sha:81a82c66 src:dodatky/b-symptomy.md:29 klas:A -->
### T-B-038 · komirka · рядок 29

**Книга каже, дослівно:**

> `Failed to start stub flasher` · Розділ → 17

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-039 sha:a7028303 src:dodatky/b-symptomy.md:30 klas:F -->
### T-B-039 · komirka · рядок 30

**Книга каже, дослівно:**

> `This chip is X, not Y` · Причина → не той `--chip`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-040 sha:21e13c37 src:dodatky/b-symptomy.md:30 klas:F -->
### T-B-040 · komirka · рядок 30

**Книга каже, дослівно:**

> `This chip is X, not Y` · Дія → прибрати `--chip`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-041 sha:d67ce886 src:dodatky/b-symptomy.md:30 klas:F -->
### T-B-041 · komirka · рядок 30

**Книга каже, дослівно:**

> `This chip is X, not Y` · Розділ → 17

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-042 sha:56ebed13 src:dodatky/b-symptomy.md:35 klas:F -->
### T-B-042 · tablycya-shapka · рядок 35

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-043 sha:d7c330de src:dodatky/b-symptomy.md:36 klas:E -->
### T-B-043 · komirka · рядок 36

**Книга каже, дослівно:**

> Прошилося, плата мовчить · Причина → **адреса бутлоадера не та**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-044 sha:a4b78d54 src:dodatky/b-symptomy.md:36 klas:A -->
### T-B-044 · komirka · рядок 36

**Книга каже, дослівно:**

> Прошилося, плата мовчить · Дія → `0x1000` classic / `0x0` S3

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  > 
  > (partition-tables.rst)
  > * At a 0x10000 (64 KB) offset in the flash is the app labelled
  >   "factory". The bootloader runs this app by default.
  > nvs,      data, nvs,     0x9000,  0x6000,
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-B-045 sha:895a3335 src:dodatky/b-symptomy.md:36 klas:E -->
### T-B-045 · komirka · рядок 36

**Книга каже, дослівно:**

> Прошилося, плата мовчить · Розділ → 16, К5

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-046 sha:47271d6c src:dodatky/b-symptomy.md:37 klas:F -->
### T-B-046 · komirka · рядок 37

**Книга каже, дослівно:**

> `invalid magic byte` · Причина → застосунку немає або не там

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-047 sha:cbe3b2f8 src:dodatky/b-symptomy.md:37 klas:F -->
### T-B-047 · komirka · рядок 37

**Книга каже, дослівно:**

> `invalid magic byte` · Дія → залити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-048 sha:d2308cd8 src:dodatky/b-symptomy.md:37 klas:F -->
### T-B-048 · komirka · рядок 37

**Книга каже, дослівно:**

> `invalid magic byte` · Розділ → 18

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-049 sha:efbec25c src:dodatky/b-symptomy.md:38 klas:A -->
### T-B-049 · komirka · рядок 38

**Книга каже, дослівно:**

> `Failed to verify partition table` · Причина → немає таблиці розділів

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-050 sha:6ce91a07 src:dodatky/b-symptomy.md:38 klas:A -->
### T-B-050 · komirka · рядок 38

**Книга каже, дослівно:**

> `Failed to verify partition table` · Дія → повна прошивка

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-051 sha:6a21db9c src:dodatky/b-symptomy.md:38 klas:A -->
### T-B-051 · komirka · рядок 38

**Книга каже, дослівно:**

> `Failed to verify partition table` · Розділ → 18

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c
- **Дослівно з джерела:**
  > FAIL_LOAD("image at 0x%"PRIx32" has invalid magic byte (nothing flashed here?)", src_addr);
  > ESP_LOGE(TAG, "Image hash failed - image is corrupt");
  > ESP_LOGE(TAG, "Factory app partition%s", not_bootable);   // " is not bootable"
  > ESP_LOGE(TAG, "partition %d invalid magic number 0x%x", num_parts, part->magic);
  > ESP_LOGE(TAG, "Failed to verify partition table");
  > ESP_LOGE(TAG, "ota data partition invalid, falling back to factory");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. П'ять із шести рядків книга подавала правильно, шостий — `image has invalid SHA256` — не існує взагалі. Насправді ESP-IDF друкує `Image hash failed - image is corrupt`.
Це саме той випадок, заради якого прохід і робився: читач із пошкодженим образом шукав у логу рядок, якого там ніколи не буде.
Заразом рядки в таблиці додатка D доповнено до повного вигляду — з `(nothing flashed here?)` і `falling back to factory`, — бо саме хвіст рядка каже, що бутлоадер зробив далі.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-052 sha:7b0e4404 src:dodatky/b-symptomy.md:39 klas:D -->
### T-B-052 · komirka · рядок 39

**Книга каже, дослівно:**

> Плата не стартує взагалі · Причина → [[classic]] `GPIO12` високий при старті

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-053 sha:636f69c5 src:dodatky/b-symptomy.md:39 klas:D -->
### T-B-053 · komirka · рядок 39

**Книга каже, дослівно:**

> Плата не стартує взагалі · Дія → зняти обв'язку

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-054 sha:8fccc1e7 src:dodatky/b-symptomy.md:39 klas:D -->
### T-B-054 · komirka · рядок 39

**Книга каже, дослівно:**

> Плата не стартує взагалі · Розділ → 07

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-055 sha:78a90252 src:dodatky/b-symptomy.md:40 klas:D -->
### T-B-055 · komirka · рядок 40

**Книга каже, дослівно:**

> Каша в моніторі · Причина → не та швидкість

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-056 sha:c97da9c8 src:dodatky/b-symptomy.md:40 klas:D -->
### T-B-056 · komirka · рядок 40

**Книга каже, дослівно:**

> Каша в моніторі · Дія → ROM ESP32 завжди 115200

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-057 sha:a2f3ba72 src:dodatky/b-symptomy.md:40 klas:D -->
### T-B-057 · komirka · рядок 40

**Книга каже, дослівно:**

> Каша в моніторі · Розділ → 25

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-058 sha:debc906e src:dodatky/b-symptomy.md:41 klas:F -->
### T-B-058 · komirka · рядок 41

**Книга каже, дослівно:**

> Лог читається на 74880 · Причина → це **ESP8266**, не ESP32

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-059 sha:c212a182 src:dodatky/b-symptomy.md:41 klas:E -->
### T-B-059 · komirka · рядок 41

**Книга каже, дослівно:**

> Лог читається на 74880 · Дія → звірити маркування

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-060 sha:d8990451 src:dodatky/b-symptomy.md:41 klas:E -->
### T-B-060 · komirka · рядок 41

**Книга каже, дослівно:**

> Лог читається на 74880 · Розділ → 23

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-061 sha:533acea2 src:dodatky/b-symptomy.md:42 klas:E -->
### T-B-061 · komirka · рядок 42

**Книга каже, дослівно:**

> Boot loop · Причина → паніка

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-062 sha:0729da19 src:dodatky/b-symptomy.md:42 klas:E -->
### T-B-062 · komirka · рядок 42

**Книга каже, дослівно:**

> Boot loop · Дія → перший дамп після живлення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-063 sha:7ee6b4ec src:dodatky/b-symptomy.md:42 klas:E -->
### T-B-063 · komirka · рядок 42

**Книга каже, дослівно:**

> Boot loop · Розділ → 26, К7

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-064 sha:aa64f6e7 src:dodatky/b-symptomy.md:43 klas:F -->
### T-B-064 · komirka · рядок 43

**Книга каже, дослівно:**

> Boot loop · Причина → brownout

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-065 sha:728bc926 src:dodatky/b-symptomy.md:43 klas:E -->
### T-B-065 · komirka · рядок 43

**Книга каже, дослівно:**

> Boot loop · Дія → живлення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-066 sha:a8cbcc9e src:dodatky/b-symptomy.md:43 klas:E -->
### T-B-066 · komirka · рядок 43

**Книга каже, дослівно:**

> Boot loop · Розділ → 06, К13

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-067 sha:b41d5996 src:dodatky/b-symptomy.md:44 klas:E -->
### T-B-067 · komirka · рядок 44

**Книга каже, дослівно:**

> Порожньо в моніторі · Причина → немає порту чи живлення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-068 sha:65bb1cb8 src:dodatky/b-symptomy.md:44 klas:E -->
### T-B-068 · komirka · рядок 44

**Книга каже, дослівно:**

> Порожньо в моніторі · Дія → К3

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-069 sha:bc0ceaeb src:dodatky/b-symptomy.md:44 klas:E -->
### T-B-069 · komirka · рядок 44

**Книга каже, дослівно:**

> Порожньо в моніторі · Розділ → 09

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-070 sha:56ebed13 src:dodatky/b-symptomy.md:49 klas:F -->
### T-B-070 · tablycya-shapka · рядок 49

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-071 sha:f20f6420 src:dodatky/b-symptomy.md:50 klas:F -->
### T-B-071 · komirka · рядок 50

**Книга каже, дослівно:**

> `rst:0xf` · Причина → **просіло живлення**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-072 sha:120f74dd src:dodatky/b-symptomy.md:50 klas:F -->
### T-B-072 · komirka · рядок 50

**Книга каже, дослівно:**

> `rst:0xf` · Дія → кабель, конденсатор, джерело 1 А

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-073 sha:029caf71 src:dodatky/b-symptomy.md:50 klas:F -->
### T-B-073 · komirka · рядок 50

**Книга каже, дослівно:**

> `rst:0xf` · Розділ → 06, К13

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-074 sha:3e808c86 src:dodatky/b-symptomy.md:51 klas:F -->
### T-B-074 · komirka · рядок 51

**Книга каже, дослівно:**

> Перезавантаження при Wi-Fi · Причина → джерело не тягне піків

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-075 sha:bc48f448 src:dodatky/b-symptomy.md:51 klas:F -->
### T-B-075 · komirka · рядок 51

**Книга каже, дослівно:**

> Перезавантаження при Wi-Fi · Дія → джерело від 1 А, 470 мкФ

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-076 sha:ded18b6d src:dodatky/b-symptomy.md:51 klas:F -->
### T-B-076 · komirka · рядок 51

**Книга каже, дослівно:**

> Перезавантаження при Wi-Fi · Розділ → 06

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-077 sha:3da42b98 src:dodatky/b-symptomy.md:52 klas:E -->
### T-B-077 · komirka · рядок 52

**Книга каже, дослівно:**

> Перезавантаження при двигуні · Причина → немає окремого живлення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-078 sha:a4c8b43e src:dodatky/b-symptomy.md:52 klas:E -->
### T-B-078 · komirka · рядок 52

**Книга каже, дослівно:**

> Перезавантаження при двигуні · Дія → окреме джерело, спільна земля

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-079 sha:b3b3593b src:dodatky/b-symptomy.md:52 klas:E -->
### T-B-079 · komirka · рядок 52

**Книга каже, дослівно:**

> Перезавантаження при двигуні · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-080 sha:0ca6156d src:dodatky/b-symptomy.md:53 klas:F -->
### T-B-080 · komirka · рядок 53

**Книга каже, дослівно:**

> Працює від USB, не від БЖ · Причина → немає спільної землі

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-081 sha:ffe63102 src:dodatky/b-symptomy.md:53 klas:F -->
### T-B-081 · komirka · рядок 53

**Книга каже, дослівно:**

> Працює від USB, не від БЖ · Дія → з'єднати `GND`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-082 sha:cb3a0097 src:dodatky/b-symptomy.md:53 klas:F -->
### T-B-082 · komirka · рядок 53

**Книга каже, дослівно:**

> Працює від USB, не від БЖ · Розділ → 05

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-083 sha:0963bdc4 src:dodatky/b-symptomy.md:54 klas:E -->
### T-B-083 · komirka · рядок 54

**Книга каже, дослівно:**

> Стабілізатор гарячий · Причина → перевантаження або слабкий клон

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-084 sha:e7d83ae9 src:dodatky/b-symptomy.md:54 klas:F -->
### T-B-084 · komirka · рядок 54

**Книга каже, дослівно:**

> Стабілізатор гарячий · Дія → зовнішні 3.3 В

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-085 sha:4d555332 src:dodatky/b-symptomy.md:54 klas:E -->
### T-B-085 · komirka · рядок 54

**Книга каже, дослівно:**

> Стабілізатор гарячий · Розділ → 06

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-086 sha:10565047 src:dodatky/b-symptomy.md:55 klas:C -->
### T-B-086 · komirka · рядок 55

**Книга каже, дослівно:**

> Сон 20 мА замість 20 мкА · Причина → плата розробки, не чип

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.espressif.com/en/support/documents/technical-documents (ESP32 Series Datasheet)
- **Що шукати в джерелі:** розділ «Recommended Operating Conditions»: гранично допустимий струм на пін (40 мА) і типова сила драйвера за замовчуванням; робочий діапазон температур; таблиця споживання за режимами (deep sleep, light sleep, modem sleep, активний, пік передачі Wi-Fi).
- **Нотатка:** Найважливіша недосяжна група після BME280: на цих числах стоять розділи 05, 06 і 47, тобто вся частина про живлення. Частина закривається обхідним шляхом — `gpio_set_drive_capability` у ESP-IDF описує рівні сили драйвера, — і це завдання наступного проходу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-B-087 sha:96d04963 src:dodatky/b-symptomy.md:55 klas:C -->
### T-B-087 · komirka · рядок 55

**Книга каже, дослівно:**

> Сон 20 мА замість 20 мкА · Дія → власний монтаж

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.espressif.com/en/support/documents/technical-documents (ESP32 Series Datasheet)
- **Що шукати в джерелі:** розділ «Recommended Operating Conditions»: гранично допустимий струм на пін (40 мА) і типова сила драйвера за замовчуванням; робочий діапазон температур; таблиця споживання за режимами (deep sleep, light sleep, modem sleep, активний, пік передачі Wi-Fi).
- **Нотатка:** Найважливіша недосяжна група після BME280: на цих числах стоять розділи 05, 06 і 47, тобто вся частина про живлення. Частина закривається обхідним шляхом — `gpio_set_drive_capability` у ESP-IDF описує рівні сили драйвера, — і це завдання наступного проходу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-B-088 sha:12d4a879 src:dodatky/b-symptomy.md:55 klas:C -->
### T-B-088 · komirka · рядок 55

**Книга каже, дослівно:**

> Сон 20 мА замість 20 мкА · Розділ → 06, 53

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.espressif.com/en/support/documents/technical-documents (ESP32 Series Datasheet)
- **Що шукати в джерелі:** розділ «Recommended Operating Conditions»: гранично допустимий струм на пін (40 мА) і типова сила драйвера за замовчуванням; робочий діапазон температур; таблиця споживання за режимами (deep sleep, light sleep, modem sleep, активний, пік передачі Wi-Fi).
- **Нотатка:** Найважливіша недосяжна група після BME280: на цих числах стоять розділи 05, 06 і 47, тобто вся частина про живлення. Частина закривається обхідним шляхом — `gpio_set_drive_capability` у ESP-IDF описує рівні сили драйвера, — і це завдання наступного проходу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-B-089 sha:5f9bba1f src:dodatky/b-symptomy.md:56 klas:E -->
### T-B-089 · komirka · рядок 56

**Книга каже, дослівно:**

> Акумулятор сідає за тижні · Причина → дільник вимірювання напруги

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-090 sha:f66a44b6 src:dodatky/b-symptomy.md:56 klas:E -->
### T-B-090 · komirka · рядок 56

**Книга каже, дослівно:**

> Акумулятор сідає за тижні · Дія → ключ на дільник

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-091 sha:b8a0c318 src:dodatky/b-symptomy.md:56 klas:E -->
### T-B-091 · komirka · рядок 56

**Книга каже, дослівно:**

> Акумулятор сідає за тижні · Розділ → 53

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-092 sha:56ebed13 src:dodatky/b-symptomy.md:61 klas:F -->
### T-B-092 · tablycya-shapka · рядок 61

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-093 sha:26d701cf src:dodatky/b-symptomy.md:62 klas:F -->
### T-B-093 · komirka · рядок 62

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Причина → **немає підтягування**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-094 sha:cb23a282 src:dodatky/b-symptomy.md:62 klas:F -->
### T-B-094 · komirka · рядок 62

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Дія → 4.7 кОм на `SDA` і `SCL`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-095 sha:077e3943 src:dodatky/b-symptomy.md:62 klas:F -->
### T-B-095 · komirka · рядок 62

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Розділ → 35

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-096 sha:40eeeaf1 src:dodatky/b-symptomy.md:63 klas:F -->
### T-B-096 · komirka · рядок 63

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Причина → немає спільної землі

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-097 sha:aa27eb03 src:dodatky/b-symptomy.md:63 klas:F -->
### T-B-097 · komirka · рядок 63

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Дія → прозвонити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-098 sha:077e3943 src:dodatky/b-symptomy.md:63 klas:F -->
### T-B-098 · komirka · рядок 63

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Розділ → 35

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-099 sha:21f32a19 src:dodatky/b-symptomy.md:64 klas:F -->
### T-B-099 · komirka · рядок 64

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Причина → не та адреса

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-100 sha:7f3770fe src:dodatky/b-symptomy.md:64 klas:F -->
### T-B-100 · komirka · рядок 64

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Дія → сканер

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-101 sha:077e3943 src:dodatky/b-symptomy.md:64 klas:F -->
### T-B-101 · komirka · рядок 64

**Книга каже, дослівно:**

> I²C не знаходить пристрій · Розділ → 35

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-102 sha:fcce0126 src:dodatky/b-symptomy.md:65 klas:F -->
### T-B-102 · komirka · рядок 65

**Книга каже, дослівно:**

> I²C з помилками · Причина → задовгі проводи, ємність

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-103 sha:f9a93533 src:dodatky/b-symptomy.md:65 klas:F -->
### T-B-103 · komirka · рядок 65

**Книга каже, дослівно:**

> I²C з помилками · Дія → 100 кГц, коротші дроти

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-104 sha:4b8a0f52 src:dodatky/b-symptomy.md:65 klas:F -->
### T-B-104 · komirka · рядок 65

**Книга каже, дослівно:**

> I²C з помилками · Розділ → 35

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-105 sha:d8a4219a src:dodatky/b-symptomy.md:66 klas:F -->
### T-B-105 · komirka · рядок 66

**Книга каже, дослівно:**

> I²C таймаути через раз · Причина → clock stretching

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-106 sha:07489a2a src:dodatky/b-symptomy.md:66 klas:F -->
### T-B-106 · komirka · рядок 66

**Книга каже, дослівно:**

> I²C таймаути через раз · Дія → знизити частоту

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-107 sha:59fbaeca src:dodatky/b-symptomy.md:66 klas:F -->
### T-B-107 · komirka · рядок 66

**Книга каже, дослівно:**

> I²C таймаути через раз · Розділ → 35

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-108 sha:78d360bb src:dodatky/b-symptomy.md:67 klas:F -->
### T-B-108 · komirka · рядок 67

**Книга каже, дослівно:**

> Кілька модулів I²C — не працює · Причина → завелике сумарне підтягування

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-109 sha:7781c2e4 src:dodatky/b-symptomy.md:67 klas:F -->
### T-B-109 · komirka · рядок 67

**Книга каже, дослівно:**

> Кілька модулів I²C — не працює · Дія → лишити один комплект

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-110 sha:a1b52ef4 src:dodatky/b-symptomy.md:67 klas:F -->
### T-B-110 · komirka · рядок 67

**Книга каже, дослівно:**

> Кілька модулів I²C — не працює · Розділ → 35

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-111 sha:1d39d249 src:dodatky/b-symptomy.md:68 klas:F -->
### T-B-111 · komirka · рядок 68

**Книга каже, дослівно:**

> SPI повертає нулі · Причина → **не той режим CPOL/CPHA**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-112 sha:b64cfad9 src:dodatky/b-symptomy.md:68 klas:F -->
### T-B-112 · komirka · рядок 68

**Книга каже, дослівно:**

> SPI повертає нулі · Дія → перебрати чотири

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-113 sha:23a14f4b src:dodatky/b-symptomy.md:68 klas:F -->
### T-B-113 · komirka · рядок 68

**Книга каже, дослівно:**

> SPI повертає нулі · Розділ → 36

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-114 sha:fef84253 src:dodatky/b-symptomy.md:69 klas:F -->
### T-B-114 · komirka · рядок 69

**Книга каже, дослівно:**

> SPI: два разом не працюють · Причина → ведений не відпускає `MISO`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-115 sha:501ce3a6 src:dodatky/b-symptomy.md:69 klas:F -->
### T-B-115 · komirka · рядок 69

**Книга каже, дослівно:**

> SPI: два разом не працюють · Дія → розділити шини

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-116 sha:bfe38995 src:dodatky/b-symptomy.md:69 klas:F -->
### T-B-116 · komirka · рядок 69

**Книга каже, дослівно:**

> SPI: два разом не працюють · Розділ → 36

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-117 sha:3e402858 src:dodatky/b-symptomy.md:70 klas:F -->
### T-B-117 · komirka · рядок 70

**Книга каже, дослівно:**

> SPI: DMA не передає · Причина → буфер не для DMA

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-118 sha:24d6421b src:dodatky/b-symptomy.md:70 klas:A -->
### T-B-118 · komirka · рядок 70

**Книга каже, дослівно:**

> SPI: DMA не передає · Дія → `heap_caps_malloc(MALLOC_CAP_DMA)`

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

<!-- fc id:T-B-119 sha:f8075fb7 src:dodatky/b-symptomy.md:70 klas:F -->
### T-B-119 · komirka · рядок 70

**Книга каже, дослівно:**

> SPI: DMA не передає · Розділ → 36

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-120 sha:b38d79e1 src:dodatky/b-symptomy.md:71 klas:F -->
### T-B-120 · komirka · рядок 71

**Книга каже, дослівно:**

> UART: сміття · Причина → не та швидкість

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-121 sha:3f497c9d src:dodatky/b-symptomy.md:71 klas:F -->
### T-B-121 · komirka · рядок 71

**Книга каже, дослівно:**

> UART: сміття · Дія → перебрати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-122 sha:1cf1a138 src:dodatky/b-symptomy.md:71 klas:F -->
### T-B-122 · komirka · рядок 71

**Книга каже, дослівно:**

> UART: сміття · Розділ → 34

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-123 sha:0703012b src:dodatky/b-symptomy.md:72 klas:F -->
### T-B-123 · komirka · рядок 72

**Книга каже, дослівно:**

> UART: нічого · Причина → переплутані TX/RX

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-124 sha:39da77cd src:dodatky/b-symptomy.md:72 klas:F -->
### T-B-124 · komirka · рядок 72

**Книга каже, дослівно:**

> UART: нічого · Дія → перехресно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-125 sha:c1462df2 src:dodatky/b-symptomy.md:72 klas:F -->
### T-B-125 · komirka · рядок 72

**Книга каже, дослівно:**

> UART: нічого · Розділ → 34

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-126 sha:e7697029 src:dodatky/b-symptomy.md:73 klas:A -->
### T-B-126 · komirka · рядок 73

**Книга каже, дослівно:**

> RS-485: губляться відповіді · Причина → **немає `uart_wait_tx_done`**

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

<!-- fc id:T-B-127 sha:b7f5a9a0 src:dodatky/b-symptomy.md:73 klas:F -->
### T-B-127 · komirka · рядок 73

**Книга каже, дослівно:**

> RS-485: губляться відповіді · Дія → додати перед перемиканням

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-128 sha:4b1c3403 src:dodatky/b-symptomy.md:73 klas:F -->
### T-B-128 · komirka · рядок 73

**Книга каже, дослівно:**

> RS-485: губляться відповіді · Розділ → 34

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-129 sha:0fb1cdd6 src:dodatky/b-symptomy.md:74 klas:F -->
### T-B-129 · komirka · рядок 74

**Книга каже, дослівно:**

> RS-485: помилки на довгій лінії · Причина → термінатори

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-130 sha:84c06d6d src:dodatky/b-symptomy.md:74 klas:F -->
### T-B-130 · komirka · рядок 74

**Книга каже, дослівно:**

> RS-485: помилки на довгій лінії · Дія → 120 Ом лише на кінцях

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-131 sha:40d5f951 src:dodatky/b-symptomy.md:74 klas:F -->
### T-B-131 · komirka · рядок 74

**Книга каже, дослівно:**

> RS-485: помилки на довгій лінії · Розділ → 34

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-132 sha:4ac391fd src:dodatky/b-symptomy.md:75 klas:F -->
### T-B-132 · komirka · рядок 75

**Книга каже, дослівно:**

> CAN: лічильник помилок росте · Причина → один вузол на шині

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-133 sha:f4eaae04 src:dodatky/b-symptomy.md:75 klas:F -->
### T-B-133 · komirka · рядок 75

**Книга каже, дослівно:**

> CAN: лічильник помилок росте · Дія → потрібні двоє

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-134 sha:2f72b877 src:dodatky/b-symptomy.md:75 klas:F -->
### T-B-134 · komirka · рядок 75

**Книга каже, дослівно:**

> CAN: лічильник помилок росте · Розділ → 38

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-135 sha:d285a217 src:dodatky/b-symptomy.md:76 klas:F -->
### T-B-135 · komirka · рядок 76

**Книга каже, дослівно:**

> CAN: не працює · Причина → не та швидкість у вузла

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-136 sha:db57d297 src:dodatky/b-symptomy.md:76 klas:F -->
### T-B-136 · komirka · рядок 76

**Книга каже, дослівно:**

> CAN: не працює · Дія → однакова всюди

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-137 sha:1334b1b5 src:dodatky/b-symptomy.md:76 klas:F -->
### T-B-137 · komirka · рядок 76

**Книга каже, дослівно:**

> CAN: не працює · Розділ → 38

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-138 sha:4a524de8 src:dodatky/b-symptomy.md:77 klas:A -->
### T-B-138 · komirka · рядок 77

**Книга каже, дослівно:**

> DS18B20: −127 °C · Причина → немає підтягування, погана лінія

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

<!-- fc id:T-B-139 sha:99eaf204 src:dodatky/b-symptomy.md:77 klas:A -->
### T-B-139 · komirka · рядок 77

**Книга каже, дослівно:**

> DS18B20: −127 °C · Дія → 4.7 кОм, окреме живлення

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

<!-- fc id:T-B-140 sha:861d1432 src:dodatky/b-symptomy.md:77 klas:A -->
### T-B-140 · komirka · рядок 77

**Книга каже, дослівно:**

> DS18B20: −127 °C · Розділ → 37

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

<!-- fc id:T-B-141 sha:56ebed13 src:dodatky/b-symptomy.md:82 klas:F -->
### T-B-141 · tablycya-shapka · рядок 82

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-142 sha:556f1db3 src:dodatky/b-symptomy.md:83 klas:F -->
### T-B-142 · komirka · рядок 83

**Книга каже, дослівно:**

> ADC читає дурницю · Причина → [[classic]] ADC2 при Wi-Fi

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-143 sha:cf5c1d93 src:dodatky/b-symptomy.md:83 klas:F -->
### T-B-143 · komirka · рядок 83

**Книга каже, дослівно:**

> ADC читає дурницю · Дія → перенести на ADC1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-144 sha:92bb30b0 src:dodatky/b-symptomy.md:83 klas:F -->
### T-B-144 · komirka · рядок 83

**Книга каже, дослівно:**

> ADC читає дурницю · Розділ → 07, 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-145 sha:c32ba837 src:dodatky/b-symptomy.md:84 klas:F -->
### T-B-145 · komirka · рядок 84

**Книга каже, дослівно:**

> ADC нелінійний · Причина → немає калібрування

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-146 sha:20558b51 src:dodatky/b-symptomy.md:84 klas:A -->
### T-B-146 · komirka · рядок 84

**Книга каже, дослівно:**

> ADC нелінійний · Дія → `adc_cali_*`

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

<!-- fc id:T-B-147 sha:93816ae9 src:dodatky/b-symptomy.md:84 klas:F -->
### T-B-147 · komirka · рядок 84

**Книга каже, дослівно:**

> ADC нелінійний · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-148 sha:731640c6 src:dodatky/b-symptomy.md:85 klas:F -->
### T-B-148 · komirka · рядок 85

**Книга каже, дослівно:**

> ADC шумить · Причина → немає усереднення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-149 sha:ce27a167 src:dodatky/b-symptomy.md:85 klas:F -->
### T-B-149 · komirka · рядок 85

**Книга каже, дослівно:**

> ADC шумить · Дія → 16–64 відліки

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-150 sha:c0938288 src:dodatky/b-symptomy.md:85 klas:F -->
### T-B-150 · komirka · рядок 85

**Книга каже, дослівно:**

> ADC шумить · Розділ → 33

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-151 sha:32b98c46 src:dodatky/b-symptomy.md:86 klas:F -->
### T-B-151 · komirka · рядок 86

**Книга каже, дослівно:**

> GPIO дивно при старті · Причина → strapping-пін

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-152 sha:29fc68a1 src:dodatky/b-symptomy.md:86 klas:F -->
### T-B-152 · komirka · рядок 86

**Книга каже, дослівно:**

> GPIO дивно при старті · Дія → інший пін

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-153 sha:d3183725 src:dodatky/b-symptomy.md:86 klas:F -->
### T-B-153 · komirka · рядок 86

**Книга каже, дослівно:**

> GPIO дивно при старті · Розділ → 07

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-154 sha:f3db0ec1 src:dodatky/b-symptomy.md:87 klas:A -->
### T-B-154 · komirka · рядок 87

**Книга каже, дослівно:**

> [[classic]] GPIO 6–11 не працюють · Причина → зайняті флешем

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

<!-- fc id:T-B-155 sha:04299502 src:dodatky/b-symptomy.md:87 klas:A -->
### T-B-155 · komirka · рядок 87

**Книга каже, дослівно:**

> [[classic]] GPIO 6–11 не працюють · Дія → не використовувати

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

<!-- fc id:T-B-156 sha:d4620841 src:dodatky/b-symptomy.md:87 klas:A -->
### T-B-156 · komirka · рядок 87

**Книга каже, дослівно:**

> [[classic]] GPIO 6–11 не працюють · Розділ → 07

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

<!-- fc id:T-B-157 sha:971f6ca7 src:dodatky/b-symptomy.md:88 klas:A -->
### T-B-157 · komirka · рядок 88

**Книга каже, дослівно:**

> Кнопка на GPIO34 не працює · Причина → немає вбудованого підтягування

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

<!-- fc id:T-B-158 sha:61500638 src:dodatky/b-symptomy.md:88 klas:A -->
### T-B-158 · komirka · рядок 88

**Книга каже, дослівно:**

> Кнопка на GPIO34 не працює · Дія → зовнішній резистор

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

<!-- fc id:T-B-159 sha:c492b81b src:dodatky/b-symptomy.md:88 klas:A -->
### T-B-159 · komirka · рядок 88

**Книга каже, дослівно:**

> Кнопка на GPIO34 не працює · Розділ → 07

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

<!-- fc id:T-B-160 sha:60900874 src:dodatky/b-symptomy.md:89 klas:E -->
### T-B-160 · komirka · рядок 89

**Книга каже, дослівно:**

> Реле вмикається при старті · Причина → вхід ключа висить при завантаженні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-161 sha:1d957fca src:dodatky/b-symptomy.md:89 klas:F -->
### T-B-161 · komirka · рядок 89

**Книга каже, дослівно:**

> Реле вмикається при старті · Дія → 10 кОм у бік «вимкнено»

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-162 sha:b03c98f2 src:dodatky/b-symptomy.md:89 klas:E -->
### T-B-162 · komirka · рядок 89

**Книга каже, дослівно:**

> Реле вмикається при старті · Розділ → 47, 62

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-163 sha:6930c5e7 src:dodatky/b-symptomy.md:90 klas:F -->
### T-B-163 · komirka · рядок 90

**Книга каже, дослівно:**

> Реле не спрацьовує · Причина → модуль на 5 В

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-164 sha:fb2de766 src:dodatky/b-symptomy.md:90 klas:F -->
### T-B-164 · komirka · рядок 90

**Книга каже, дослівно:**

> Реле не спрацьовує · Дія → живити 5 В

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-165 sha:c436aab7 src:dodatky/b-symptomy.md:90 klas:E -->
### T-B-165 · komirka · рядок 90

**Книга каже, дослівно:**

> Реле не спрацьовує · Розділ → 47

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-166 sha:9e5a021d src:dodatky/b-symptomy.md:91 klas:E -->
### T-B-166 · komirka · рядок 91

**Книга каже, дослівно:**

> Серво смикається, плата падає · Причина → немає окремого живлення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-167 sha:c55732e1 src:dodatky/b-symptomy.md:91 klas:E -->
### T-B-167 · komirka · рядок 91

**Книга каже, дослівно:**

> Серво смикається, плата падає · Дія → окреме джерело

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-168 sha:04d6097b src:dodatky/b-symptomy.md:91 klas:E -->
### T-B-168 · komirka · рядок 91

**Книга каже, дослівно:**

> Серво смикається, плата падає · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-169 sha:ad2804fa src:dodatky/b-symptomy.md:92 klas:E -->
### T-B-169 · komirka · рядок 92

**Книга каже, дослівно:**

> Кроковий гріється · Причина → не виставлено обмеження струму

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-170 sha:35d7d17e src:dodatky/b-symptomy.md:92 klas:E -->
### T-B-170 · komirka · рядок 92

**Книга каже, дослівно:**

> Кроковий гріється · Дія → налаштувати до запуску

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-171 sha:9ed2bd2c src:dodatky/b-symptomy.md:92 klas:E -->
### T-B-171 · komirka · рядок 92

**Книга каже, дослівно:**

> Кроковий гріється · Розділ → 48

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-172 sha:9711c4e4 src:dodatky/b-symptomy.md:93 klas:A -->
### T-B-172 · komirka · рядок 93

**Книга каже, дослівно:**

> Дисплей зсунутий на 2 пікселі · Причина → це SH1106, не SSD1306

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

<!-- fc id:T-B-173 sha:522f4b8b src:dodatky/b-symptomy.md:93 klas:E -->
### T-B-173 · komirka · рядок 93

**Книга каже, дослівно:**

> Дисплей зсунутий на 2 пікселі · Дія → режим у бібліотеці

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-174 sha:77a543d6 src:dodatky/b-symptomy.md:93 klas:E -->
### T-B-174 · komirka · рядок 93

**Книга каже, дослівно:**

> Дисплей зсунутий на 2 пікселі · Розділ → 46

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-175 sha:ce426656 src:dodatky/b-symptomy.md:94 klas:E -->
### T-B-175 · komirka · рядок 94

**Книга каже, дослівно:**

> Кирилиця — прямокутники · Причина → шрифт без кирилиці

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-176 sha:5c1a88db src:dodatky/b-symptomy.md:94 klas:E -->
### T-B-176 · komirka · рядок 94

**Книга каже, дослівно:**

> Кирилиця — прямокутники · Дія → інший шрифт

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-177 sha:ebfecd76 src:dodatky/b-symptomy.md:94 klas:E -->
### T-B-177 · komirka · рядок 94

**Книга каже, дослівно:**

> Кирилиця — прямокутники · Розділ → 46

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-178 sha:752f79c0 src:dodatky/b-symptomy.md:95 klas:A -->
### T-B-178 · komirka · рядок 95

**Книга каже, дослівно:**

> Датчик гріється, значення пливуть · Причина → подано 5 В на 3.3 В

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf — ESP32 Series Datasheet v5.3, Table 5-1 «Absolute Maximum Ratings» і Table 5-3 «DC Characteristics», с. 51
- **Дослівно з джерела:**
  > Table 5-1. Absolute Maximum Ratings
  > Parameter                                    Description              Min    Max   Unit
  > VDDA, VDD3P3, VDD3P3_RTC,
  > VDD3P3_CPU, VDD_SDIO                  Allowed input voltage          –0.3    3.6    V
  > 
  > Stresses above those listed in Table 5-1 Absolute Maximum Ratings may cause
  > permanent damage to the device.
  > 
  > Table 5-3. DC Characteristics (3.3 V, 25 °C)
  > VIH   High-level input voltage    0.75 × VDD   —   VDD + 0.3   V
  > VIL   Low-level input voltage           –0.3   —   0.25 × VDD  V
  > 
  > [2] Maximum VIH = VDD(max) + 0.5 V or 5.5 V, which ever is lower.
- **Спосіб і дата:** PDF Espressif, кеш `esp32-datasheet.pdf`, реєстр `factcheck/DZHERELA-m2.md`, pdftotext -layout, 2026-08-26
- **Нотатка:** Попередження книги дістає нарешті числову підставу, і вона сильніша за «логіка 3.3 В». Джерело нормує **абсолютний максимум** входу як 3.6 В і прямо каже, що вище — `permanent damage`. П'ять вольтів це перевищення на 1.4 В, тобто не «поза рекомендованим», а поза гранично допустимим.
Друга половина, потрібна для картки К14: поріг високого рівня — `0.75 × VDD`, тобто близько 2.5 В при 3.3 В живлення. Тому п'ятивольтовий вихід читається як логічна одиниця й «начебто працює» — доки пін не деградує. Це пояснює найпідступніше в цій несправності: вона не миттєва.
- **Прохід:** m2-06-napruga-mezhi

---

<!-- fc id:T-B-179 sha:b9e08822 src:dodatky/b-symptomy.md:95 klas:E -->
### T-B-179 · komirka · рядок 95

**Книга каже, дослівно:**

> Датчик гріється, значення пливуть · Дія → конвертер рівнів

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-180 sha:0c75375e src:dodatky/b-symptomy.md:95 klas:E -->
### T-B-180 · komirka · рядок 95

**Книга каже, дослівно:**

> Датчик гріється, значення пливуть · Розділ → 44, К14

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-181 sha:fe46043f src:dodatky/b-symptomy.md:96 klas:E -->
### T-B-181 · komirka · рядок 96

**Книга каже, дослівно:**

> Датчик міряє не те · Причина → стоїть біля нагрітого

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-182 sha:fb5ef80c src:dodatky/b-symptomy.md:96 klas:E -->
### T-B-182 · komirka · рядок 96

**Книга каже, дослівно:**

> Датчик міряє не те · Дія → винести

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-183 sha:da576685 src:dodatky/b-symptomy.md:96 klas:E -->
### T-B-183 · komirka · рядок 96

**Книга каже, дослівно:**

> Датчик міряє не те · Розділ → 45

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-184 sha:cdbf2b21 src:dodatky/b-symptomy.md:97 klas:A -->
### T-B-184 · komirka · рядок 97

**Книга каже, дослівно:**

> `Camera probe failed` · Причина → живлення

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp32-camera/master/driver/esp_camera.c
- **Дослівно з джерела:**
  > ESP_LOGE(TAG, "Camera probe failed with error 0x%x(%s)", err, esp_err_to_name(err));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Без виправлення: те, що друкує книга, — точний початок справжнього рядка, тож пошук у логу спрацює. Зафіксовано повний вигляд, бо код помилки в хвості рядка часто й називає причину.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-185 sha:20942e97 src:dodatky/b-symptomy.md:97 klas:A -->
### T-B-185 · komirka · рядок 97

**Книга каже, дослівно:**

> `Camera probe failed` · Дія → окреме джерело 5 В

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp32-camera/master/driver/esp_camera.c
- **Дослівно з джерела:**
  > ESP_LOGE(TAG, "Camera probe failed with error 0x%x(%s)", err, esp_err_to_name(err));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Без виправлення: те, що друкує книга, — точний початок справжнього рядка, тож пошук у логу спрацює. Зафіксовано повний вигляд, бо код помилки в хвості рядка часто й називає причину.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-186 sha:1e765843 src:dodatky/b-symptomy.md:97 klas:A -->
### T-B-186 · komirka · рядок 97

**Книга каже, дослівно:**

> `Camera probe failed` · Розділ → 49

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp32-camera/master/driver/esp_camera.c
- **Дослівно з джерела:**
  > ESP_LOGE(TAG, "Camera probe failed with error 0x%x(%s)", err, esp_err_to_name(err));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Без виправлення: те, що друкує книга, — точний початок справжнього рядка, тож пошук у логу спрацює. Зафіксовано повний вигляд, бо код помилки в хвості рядка часто й називає причину.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-B-187 sha:56ebed13 src:dodatky/b-symptomy.md:102 klas:F -->
### T-B-187 · tablycya-shapka · рядок 102

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-188 sha:b3c47737 src:dodatky/b-symptomy.md:103 klas:E -->
### T-B-188 · komirka · рядок 103

**Книга каже, дослівно:**

> Мережі немає в списку · Причина → **5 ГГц**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-189 sha:3ee6716b src:dodatky/b-symptomy.md:103 klas:F -->
### T-B-189 · komirka · рядок 103

**Книга каже, дослівно:**

> Мережі немає в списку · Дія → ESP32 бачить лише 2.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-190 sha:56140876 src:dodatky/b-symptomy.md:103 klas:E -->
### T-B-190 · komirka · рядок 103

**Книга каже, дослівно:**

> Мережі немає в списку · Розділ → 39

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-191 sha:2c7a819f src:dodatky/b-symptomy.md:104 klas:F -->
### T-B-191 · komirka · рядок 104

**Книга каже, дослівно:**

> Не під'єднується · Причина → пароль, канал 12–13, WPA3

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-192 sha:ffa97f65 src:dodatky/b-symptomy.md:104 klas:E -->
### T-B-192 · komirka · рядок 104

**Книга каже, дослівно:**

> Не під'єднується · Дія → звірити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-193 sha:6f861a1d src:dodatky/b-symptomy.md:104 klas:E -->
### T-B-193 · komirka · рядок 104

**Книга каже, дослівно:**

> Не під'єднується · Розділ → 39

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-194 sha:1890e8b0 src:dodatky/b-symptomy.md:105 klas:E -->
### T-B-194 · komirka · рядок 105

**Книга каже, дослівно:**

> Під'єднується й відвалюється · Причина → живлення або слабкий сигнал

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-195 sha:6ff78fce src:dodatky/b-symptomy.md:105 klas:E -->
### T-B-195 · komirka · рядок 105

**Книга каже, дослівно:**

> Під'єднується й відвалюється · Дія → RSSI, джерело

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-196 sha:153e04ac src:dodatky/b-symptomy.md:105 klas:E -->
### T-B-196 · komirka · рядок 105

**Книга каже, дослівно:**

> Під'єднується й відвалюється · Розділ → 39

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-197 sha:125d73f0 src:dodatky/b-symptomy.md:106 klas:F -->
### T-B-197 · komirka · рядок 106

**Книга каже, дослівно:**

> Пінги ходять, OTA не проходить · Причина → межа покриття

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-198 sha:7e376d4c src:dodatky/b-symptomy.md:106 klas:F -->
### T-B-198 · komirka · рядок 106

**Книга каже, дослівно:**

> Пінги ходять, OTA не проходить · Дія → RSSI гірше −80

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-199 sha:39a01c38 src:dodatky/b-symptomy.md:106 klas:F -->
### T-B-199 · komirka · рядок 106

**Книга каже, дослівно:**

> Пінги ходять, OTA не проходить · Розділ → 19, 39

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-200 sha:ee2e0a0d src:dodatky/b-symptomy.md:107 klas:A -->
### T-B-200 · komirka · рядок 107

**Книга каже, дослівно:**

> Перезавантажується без мережі · Причина → `ESP_ERROR_CHECK` навколо connect

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 7), 2026-08-26
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-B-201 sha:1f885b10 src:dodatky/b-symptomy.md:107 klas:E -->
### T-B-201 · komirka · рядок 107

**Книга каже, дослівно:**

> Перезавантажується без мережі · Дія → явна обробка

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-202 sha:0e6d6dc2 src:dodatky/b-symptomy.md:107 klas:E -->
### T-B-202 · komirka · рядок 107

**Книга каже, дослівно:**

> Перезавантажується без мережі · Розділ → 32, 39

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-203 sha:bf20564d src:dodatky/b-symptomy.md:108 klas:E -->
### T-B-203 · komirka · рядок 108

**Книга каже, дослівно:**

> Гріється, батарея сідає · Причина → перепід'єднання без паузи

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-204 sha:844e5b3c src:dodatky/b-symptomy.md:108 klas:E -->
### T-B-204 · komirka · рядок 108

**Книга каже, дослівно:**

> Гріється, батарея сідає · Дія → зростаюча пауза

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-205 sha:e56a94c5 src:dodatky/b-symptomy.md:108 klas:E -->
### T-B-205 · komirka · рядок 108

**Книга каже, дослівно:**

> Гріється, батарея сідає · Розділ → 39

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-206 sha:62d52d5f src:dodatky/b-symptomy.md:109 klas:F -->
### T-B-206 · komirka · рядок 109

**Книга каже, дослівно:**

> ESP-NOW: працювало на столі · Причина → роутер змінив канал

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-207 sha:f5a18158 src:dodatky/b-symptomy.md:109 klas:F -->
### T-B-207 · komirka · рядок 109

**Книга каже, дослівно:**

> ESP-NOW: працювало на столі · Дія → фіксувати канал

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-208 sha:3ea91924 src:dodatky/b-symptomy.md:109 klas:F -->
### T-B-208 · komirka · рядок 109

**Книга каже, дослівно:**

> ESP-NOW: працювало на столі · Розділ → 42

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-209 sha:bcba5e79 src:dodatky/b-symptomy.md:110 klas:F -->
### T-B-209 · komirka · рядок 110

**Книга каже, дослівно:**

> BLE: не вміщається · Причина → Bluedroid замість NimBLE

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-210 sha:49025361 src:dodatky/b-symptomy.md:110 klas:F -->
### T-B-210 · komirka · рядок 110

**Книга каже, дослівно:**

> BLE: не вміщається · Дія → перемкнути

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-211 sha:6a99030f src:dodatky/b-symptomy.md:110 klas:F -->
### T-B-211 · komirka · рядок 110

**Книга каже, дослівно:**

> BLE: не вміщається · Розділ → 41

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-212 sha:1e8a7978 src:dodatky/b-symptomy.md:111 klas:F -->
### T-B-212 · komirka · рядок 111

**Книга каже, дослівно:**

> BLE: iOS бачить старі сервіси · Причина → кеш GATT

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-213 sha:37ed6eba src:dodatky/b-symptomy.md:111 klas:F -->
### T-B-213 · komirka · рядок 111

**Книга каже, дослівно:**

> BLE: iOS бачить старі сервіси · Дія → забути пристрій

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-214 sha:cd07deb3 src:dodatky/b-symptomy.md:111 klas:F -->
### T-B-214 · komirka · рядок 111

**Книга каже, дослівно:**

> BLE: iOS бачить старі сервіси · Розділ → 41

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-215 sha:8ac015f9 src:dodatky/b-symptomy.md:112 klas:D -->
### T-B-215 · komirka · рядок 112

**Книга каже, дослівно:**

> SPP не працює на S3/C3 · Причина → Classic є лише в classic

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-216 sha:98e7ec7d src:dodatky/b-symptomy.md:112 klas:D -->
### T-B-216 · komirka · рядок 112

**Книга каже, дослівно:**

> SPP не працює на S3/C3 · Дія → переписати на BLE

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-217 sha:ad3c5a79 src:dodatky/b-symptomy.md:112 klas:D -->
### T-B-217 · komirka · рядок 112

**Книга каже, дослівно:**

> SPP не працює на S3/C3 · Розділ → 41

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-218 sha:e667e32e src:dodatky/b-symptomy.md:113 klas:F -->
### T-B-218 · komirka · рядок 113

**Книга каже, дослівно:**

> LoRa: нічого не чути · Причина → різні параметри в боків

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-219 sha:a488d47d src:dodatky/b-symptomy.md:113 klas:F -->
### T-B-219 · komirka · рядок 113

**Книга каже, дослівно:**

> LoRa: нічого не чути · Дія → однакові SF/BW/CR

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-220 sha:10843ab0 src:dodatky/b-symptomy.md:113 klas:F -->
### T-B-220 · komirka · рядок 113

**Книга каже, дослівно:**

> LoRa: нічого не чути · Розділ → 43

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-221 sha:384e9fbc src:dodatky/b-symptomy.md:114 klas:F -->
### T-B-221 · komirka · рядок 114

**Книга каже, дослівно:**

> LoRa: модуль згорів · Причина → увімкнули без антени

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-222 sha:06dc0149 src:dodatky/b-symptomy.md:114 klas:F -->
### T-B-222 · komirka · рядок 114

**Книга каже, дослівно:**

> LoRa: модуль згорів · Дія → ⛔ незворотно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-223 sha:e89cf009 src:dodatky/b-symptomy.md:114 klas:F -->
### T-B-223 · komirka · рядок 114

**Книга каже, дослівно:**

> LoRa: модуль згорів · Розділ → 43

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-224 sha:56ebed13 src:dodatky/b-symptomy.md:119 klas:F -->
### T-B-224 · tablycya-shapka · рядок 119

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-225 sha:56b88433 src:dodatky/b-symptomy.md:120 klas:E -->
### T-B-225 · komirka · рядок 120

**Книга каже, дослівно:**

> Падає через дні роботи · Причина → фрагментація купи

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-226 sha:e3d6d102 src:dodatky/b-symptomy.md:120 klas:E -->
### T-B-226 · komirka · рядок 120

**Книга каже, дослівно:**

> Падає через дні роботи · Дія → не виділяти в циклі

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-227 sha:d8a49a7b src:dodatky/b-symptomy.md:120 klas:E -->
### T-B-227 · komirka · рядок 120

**Книга каже, дослівно:**

> Падає через дні роботи · Розділ → 30

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-228 sha:962ab34d src:dodatky/b-symptomy.md:121 klas:E -->
### T-B-228 · komirka · рядок 121

**Книга каже, дослівно:**

> Падає в випадковому місці · Причина → переповнення стека задачі

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-229 sha:4aa7bc42 src:dodatky/b-symptomy.md:121 klas:E -->
### T-B-229 · komirka · рядок 121

**Книга каже, дослівно:**

> Падає в випадковому місці · Дія → збільшити стек

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-230 sha:345141ce src:dodatky/b-symptomy.md:121 klas:E -->
### T-B-230 · komirka · рядок 121

**Книга каже, дослівно:**

> Падає в випадковому місці · Розділ → 30

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-231 sha:4bb18d8f src:dodatky/b-symptomy.md:122 klas:F -->
### T-B-231 · komirka · рядок 122

**Книга каже, дослівно:**

> `malloc` = `NULL`, пам'ять є · Причина → немає суцільного блоку

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-232 sha:df6cd31c src:dodatky/b-symptomy.md:122 klas:F -->
### T-B-232 · komirka · рядок 122

**Книга каже, дослівно:**

> `malloc` = `NULL`, пам'ять є · Дія → `largest_free_block`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-233 sha:161267f9 src:dodatky/b-symptomy.md:122 klas:F -->
### T-B-233 · komirka · рядок 122

**Книга каже, дослівно:**

> `malloc` = `NULL`, пам'ять є · Розділ → 30

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-234 sha:4264d262 src:dodatky/b-symptomy.md:123 klas:A -->
### T-B-234 · komirka · рядок 123

**Книга каже, дослівно:**

> `LoadProhibited`, `EXCVADDR` ~0 · Причина → розіменування `NULL`

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

<!-- fc id:T-B-235 sha:962e23f9 src:dodatky/b-symptomy.md:123 klas:A -->
### T-B-235 · komirka · рядок 123

**Книга каже, дослівно:**

> `LoadProhibited`, `EXCVADDR` ~0 · Дія → перевіряти `malloc`

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

<!-- fc id:T-B-236 sha:65aff682 src:dodatky/b-symptomy.md:123 klas:A -->
### T-B-236 · komirka · рядок 123

**Книга каже, дослівно:**

> `LoadProhibited`, `EXCVADDR` ~0 · Розділ → 26

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

<!-- fc id:T-B-237 sha:6d0abcdc src:dodatky/b-symptomy.md:124 klas:E -->
### T-B-237 · komirka · рядок 124

**Книга каже, дослівно:**

> Task WDT · Причина → цикл без затримки

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-238 sha:200b2107 src:dodatky/b-symptomy.md:124 klas:A -->
### T-B-238 · komirka · рядок 124

**Книга каже, дослівно:**

> Task WDT · Дія → `vTaskDelay`

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

<!-- fc id:T-B-239 sha:13104249 src:dodatky/b-symptomy.md:124 klas:E -->
### T-B-239 · komirka · рядок 124

**Книга каже, дослівно:**

> Task WDT · Розділ → 31

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-240 sha:b9f68376 src:dodatky/b-symptomy.md:125 klas:E -->
### T-B-240 · komirka · рядок 125

**Книга каже, дослівно:**

> Interrupt WDT · Причина → довгий ISR

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-241 sha:fc0e937d src:dodatky/b-symptomy.md:125 klas:E -->
### T-B-241 · komirka · рядок 125

**Книга каже, дослівно:**

> Interrupt WDT · Дія → коротко: у чергу і вийти

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-242 sha:54b06376 src:dodatky/b-symptomy.md:125 klas:E -->
### T-B-242 · komirka · рядок 125

**Книга каже, дослівно:**

> Interrupt WDT · Розділ → 31

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-243 sha:735bca0f src:dodatky/b-symptomy.md:126 klas:E -->
### T-B-243 · komirka · рядок 126

**Книга каже, дослівно:**

> Система стоїть · Причина → висока пріоритетна задача без блокування

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-244 sha:2cc14ea6 src:dodatky/b-symptomy.md:126 klas:E -->
### T-B-244 · komirka · рядок 126

**Книга каже, дослівно:**

> Система стоїть · Дія → знизити або блокувати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-245 sha:0e15746b src:dodatky/b-symptomy.md:126 klas:E -->
### T-B-245 · komirka · рядок 126

**Книга каже, дослівно:**

> Система стоїть · Розділ → 31

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-246 sha:5464bc24 src:dodatky/b-symptomy.md:127 klas:E -->
### T-B-246 · komirka · рядок 127

**Книга каже, дослівно:**

> Дані псуються випадково · Причина → спільна змінна без захисту

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-247 sha:051322d4 src:dodatky/b-symptomy.md:127 klas:E -->
### T-B-247 · komirka · рядок 127

**Книга каже, дослівно:**

> Дані псуються випадково · Дія → черга або м'ютекс

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-248 sha:9416c78b src:dodatky/b-symptomy.md:127 klas:E -->
### T-B-248 · komirka · рядок 127

**Книга каже, дослівно:**

> Дані псуються випадково · Розділ → 31

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-249 sha:56ebed13 src:dodatky/b-symptomy.md:132 klas:F -->
### T-B-249 · tablycya-shapka · рядок 132

**Книга каже, дослівно:**

> | Симптом | Причина | Дія | Розділ |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-250 sha:668b2f3a src:dodatky/b-symptomy.md:133 klas:E -->
### T-B-250 · komirka · рядок 133

**Книга каже, дослівно:**

> На столі працює, у корпусі ні · Причина → перегрів

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-251 sha:484b056e src:dodatky/b-symptomy.md:133 klas:E -->
### T-B-251 · komirka · рядок 133

**Книга каже, дослівно:**

> На столі працює, у корпусі ні · Дія → вентиляція, менша потужність

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-252 sha:1dbefcae src:dodatky/b-symptomy.md:133 klas:E -->
### T-B-252 · komirka · рядок 133

**Книга каже, дослівно:**

> На столі працює, у корпусі ні · Розділ → 54

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-253 sha:d5dba67b src:dodatky/b-symptomy.md:134 klas:E -->
### T-B-253 · komirka · рядок 134

**Книга каже, дослівно:**

> Немає зв'язку в корпусі · Причина → **метал екранує**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-254 sha:ee489cf0 src:dodatky/b-symptomy.md:134 klas:E -->
### T-B-254 · komirka · рядок 134

**Книга каже, дослівно:**

> Немає зв'язку в корпусі · Дія → пластик або зовнішня антена

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-255 sha:b987e276 src:dodatky/b-symptomy.md:134 klas:E -->
### T-B-255 · komirka · рядок 134

**Книга каже, дослівно:**

> Немає зв'язку в корпусі · Розділ → 39, 54

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-256 sha:806f210b src:dodatky/b-symptomy.md:135 klas:E -->
### T-B-256 · komirka · рядок 135

**Книга каже, дослівно:**

> Через місяці корозія · Причина → конденсат

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-257 sha:76b833a9 src:dodatky/b-symptomy.md:135 klas:E -->
### T-B-257 · komirka · рядок 135

**Книга каже, дослівно:**

> Через місяці корозія · Дія → силікагель, мембрана, лак

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-258 sha:53c80222 src:dodatky/b-symptomy.md:135 klas:E -->
### T-B-258 · komirka · рядок 135

**Книга каже, дослівно:**

> Через місяці корозія · Розділ → 54

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-259 sha:6889ccbc src:dodatky/b-symptomy.md:136 klas:E -->
### T-B-259 · komirka · рядок 136

**Книга каже, дослівно:**

> Обрив після перевезення · Причина → вібрація, немає strain relief

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-260 sha:a99802d5 src:dodatky/b-symptomy.md:136 klas:E -->
### T-B-260 · komirka · рядок 136

**Книга каже, дослівно:**

> Обрив після перевезення · Дія → закріпити кабель

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-261 sha:4b549068 src:dodatky/b-symptomy.md:136 klas:E -->
### T-B-261 · komirka · рядок 136

**Книга каже, дослівно:**

> Обрив після перевезення · Розділ → 54

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-262 sha:1116848e src:dodatky/b-symptomy.md:137 klas:D -->
### T-B-262 · komirka · рядок 137

**Книга каже, дослівно:**

> Дроти вискочили · Причина → Dupont під вібрацією

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-263 sha:0b4670aa src:dodatky/b-symptomy.md:137 klas:D -->
### T-B-263 · komirka · рядок 137

**Книга каже, дослівно:**

> Дроти вискочили · Дія → постійний монтаж

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-264 sha:8b297e2e src:dodatky/b-symptomy.md:137 klas:D -->
### T-B-264 · komirka · рядок 137

**Книга каже, дослівно:**

> Дроти вискочили · Розділ → 52

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** dodatky/b-symptomy.md проти заголовків manual/*.md
- **Дослівно з джерела:**
  > Звірено всі 70 рядків таблиці симптомів із назвами розділів, куди
  > вони відсилають. Вибірка:
  > 
  >   Порт не з'являється            → 09. Підключення до комп'ютера
  >   `Failed to connect`            → 17. esptool / 16. Як завантажується
  >   `MD5 of file does not match`   → 06. Живлення і струмоспоживання
  >   Плата не стартує взагалі       → 07. Розпіновка й обмеження GPIO
  >   Лог читається на 74880         → 23. Тріаж невідомої плати
  >   DS18B20: −127 °C               → 37. 1-Wire
  >   SPP не працює на S3/C3         → 41. Bluetooth і BLE
  >   `Camera probe failed`          → 49. Карти пам'яті, камери, звук
  >   Через місяці корозія           → 54. Корпус і захист середовища
- **Спосіб і дата:** зіставлення номерів із заголовками розділів, 2026-08-26
- **Нотатка:** Додаток B — найщільніша навігаційна таблиця книги і головна точка входу для того, хто прийшов із симптомом. Помилка в номері тут коштує найдорожче: людина з несправною платою потрапляє не в той розділ і робить висновок, що довідник їй не допоміг.
Розбіжностей немає в жодному з 70 рядків. Кілька рядків свідомо ведуть у два розділи (наприклад, `Failed to connect` → 17 і 16), і обидва доречні: один про інструмент, другий про причину.
Перевірка тематичної доречності — не механічна, тож клас `D` тут означає «перевірено зіставленням у межах книги», а не «обчислено».
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-B-265 sha:b76bf4b9 src:dodatky/b-symptomy.md:142 klas:E -->
### T-B-265 · proza · рядок 142

**Книга каже, дослівно:**

> Майже ніколи не програмний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-266 sha:488aeda0 src:dodatky/b-symptomy.md:142 klas:E -->
### T-B-266 · proza · рядок 142

**Книга каже, дослівно:**

> Порядок підозр **строго**:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-267 sha:68afb39c src:dodatky/b-symptomy.md:144 klas:E -->
### T-B-267 · proza · рядок 144

**Книга каже, дослівно:**

> **живлення → пайка → земля → логічні рівні → таймінги → і лише потім код**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-268 sha:ec2b3a25 src:dodatky/b-symptomy.md:147 klas:E -->
### T-B-268 · proza · рядок 147

**Книга каже, дослівно:**

> Збій, що зник після зміни, але не відтворювався стабільно до неї, — **не полагоджений**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-B-269 sha:9b7591b2 src:dodatky/b-symptomy.md:150 klas:E -->
### T-B-269 · proza · рядок 150

**Книга каже, дослівно:**

> Перш ніж закрити питання, треба вміти викликати збій за бажанням (розділи 29, 58).

**Доказ**

- **Клас:** F — не звірено

---
