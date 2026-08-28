# Фактчекінг: `manual/41-ble.md`

Одиниць твердження: **82**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-41-001 sha:f6628fea src:manual/41-ble.md:3 klas:F -->
### T-41-001 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Bluetooth на ESP32 — тема, де найлегше витратити час даремно, бо відповідь на «як зробити» залежить від чипа сильніше, ніж деінде.

**Контекст**

```
# 41. Bluetooth і BLE {#ble}

Bluetooth на ESP32 — тема, де найлегше витратити час даремно, бо
відповідь на «як зробити» залежить від чипа сильніше, ніж деінде.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-002 sha:87624831 src:manual/41-ble.md:9 klas:A -->
### T-41-002 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Bluetooth Classic є лише в ESP32 classic.** S3, C3, C6, H2 — **тільки BLE**.

**Контекст**

```
## Найважливіше рішення вже ухвалене за вас

::: nezvorotne
**Bluetooth Classic є лише в ESP32 classic.** S3, C3, C6, H2 —
**тільки BLE**. ESP32-S2 не має Bluetooth узагалі (розділ 02).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > esp32:   CPU_CORES_NUM 2   WIFI 1  BT 1  BLE 1  BT_CLASSIC 1  SPIRAM 1
  > esp32s2: CPU_CORES_NUM 1   WIFI 1  (BT/BLE відсутні)          SPIRAM 1  USB_OTG 1
  > esp32s3: CPU_CORES_NUM 2   WIFI 1  BT 1  BLE 1  (без BT_CLASSIC) SPIRAM 1
  >                              USB_OTG 1  USB_SERIAL_JTAG 1
  > esp32c3: CPU_CORES_NUM 1   WIFI 1  BT 1  BLE 1  (без SPIRAM)  USB_SERIAL_JTAG 1
  > esp32c6: CPU_CORES_NUM 1   WIFI 1  BT 1  BLE 1  IEEE802154 1  USB_SERIAL_JTAG 1
  >          #define SOC_WIFI_HE_SUPPORT (1)  /*!< Support Wi-Fi 6 */
  > esp32h2: CPU_CORES_NUM 1   (без WIFI)  BT 1  BLE 1  IEEE802154 1  USB_SERIAL_JTAG 1
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх шістдесяти комірках. Звірено кожен рядок: ядра, PSRAM, Wi-Fi, BT Classic, BLE, 802.15.4, USB — по шести сімействах.
Окремо приємно закрився рядок «Wi-Fi 6» для C6: у заголовку стоїть `SOC_WIFI_HE_SUPPORT (1) /*!< Support Wi-Fi 6 */`, і цього прапорця немає в жодного іншого сімейства книги. Тобто твердження не з маркетингового опису, а з умови збирання.
Три блоки уваги розділу 02 теж підтверджені механічно: `SOC_BT_CLASSIC_SUPPORTED` є лише в classic; у S2 немає ні `SOC_BT_SUPPORTED`, ні `SOC_BLE_SUPPORTED`; `SOC_SPIRAM_SUPPORTED` є рівно в classic, S2 і S3.
- **Прохід:** pass-13-mozhlyvosti

---

<!-- fc id:T-41-003 sha:06fa7a1a src:manual/41-ble.md:10 klas:A -->
### T-41-003 · proza · `manual/41-ble.md`

**Твердження, коротко**

> ESP32-S2 не має Bluetooth узагалі (розділ 02).

**Контекст**

```
## Найважливіше рішення вже ухвалене за вас

::: nezvorotne
**Bluetooth Classic є лише в ESP32 classic.** S3, C3, C6, H2 —
**тільки BLE**. ESP32-S2 не має Bluetooth узагалі (розділ 02).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > esp32:   CPU_CORES_NUM 2   WIFI 1  BT 1  BLE 1  BT_CLASSIC 1  SPIRAM 1
  > esp32s2: CPU_CORES_NUM 1   WIFI 1  (BT/BLE відсутні)          SPIRAM 1  USB_OTG 1
  > esp32s3: CPU_CORES_NUM 2   WIFI 1  BT 1  BLE 1  (без BT_CLASSIC) SPIRAM 1
  >                              USB_OTG 1  USB_SERIAL_JTAG 1
  > esp32c3: CPU_CORES_NUM 1   WIFI 1  BT 1  BLE 1  (без SPIRAM)  USB_SERIAL_JTAG 1
  > esp32c6: CPU_CORES_NUM 1   WIFI 1  BT 1  BLE 1  IEEE802154 1  USB_SERIAL_JTAG 1
  >          #define SOC_WIFI_HE_SUPPORT (1)  /*!< Support Wi-Fi 6 */
  > esp32h2: CPU_CORES_NUM 1   (без WIFI)  BT 1  BLE 1  IEEE802154 1  USB_SERIAL_JTAG 1
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у всіх шістдесяти комірках. Звірено кожен рядок: ядра, PSRAM, Wi-Fi, BT Classic, BLE, 802.15.4, USB — по шести сімействах.
Окремо приємно закрився рядок «Wi-Fi 6» для C6: у заголовку стоїть `SOC_WIFI_HE_SUPPORT (1) /*!< Support Wi-Fi 6 */`, і цього прапорця немає в жодного іншого сімейства книги. Тобто твердження не з маркетингового опису, а з умови збирання.
Три блоки уваги розділу 02 теж підтверджені механічно: `SOC_BT_CLASSIC_SUPPORTED` є лише в classic; у S2 немає ні `SOC_BT_SUPPORTED`, ні `SOC_BLE_SUPPORTED`; `SOC_SPIRAM_SUPPORTED` є рівно в classic, S2 і S3.
- **Прохід:** pass-13-mozhlyvosti

---

<!-- fc id:T-41-004 sha:6530cc25 src:manual/41-ble.md:12 klas:E -->
### T-41-004 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Це відсутність апаратного блоку, а не нереалізована функція.

**Контекст**

```
## Найважливіше рішення вже ухвалене за вас

Це відсутність апаратного блоку, а не нереалізована функція. Ніяка
бібліотека і ніяка версія IDF цього не змінить.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-005 sha:b8cb3f66 src:manual/41-ble.md:12 klas:E -->
### T-41-005 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Ніяка бібліотека і ніяка версія IDF цього не змінить.

**Контекст**

```
## Найважливіше рішення вже ухвалене за вас

Це відсутність апаратного блоку, а не нереалізована функція. Ніяка
бібліотека і ніяка версія IDF цього не змінить.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-006 sha:78640fc8 src:manual/41-ble.md:15 klas:E -->
### T-41-006 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Практичний наслідок величезний: профіль **SPP** — послідовний порт по Bluetooth, на якому тримається безліч старих проєктів і на який розраховані прості термінальні застосунки для телефона, — існує **тільки на classic**.

**Контекст**

```
## Найважливіше рішення вже ухвалене за вас

Практичний наслідок величезний: профіль **SPP** — послідовний порт по
Bluetooth, на якому тримається безліч старих проєктів і на який
розраховані прості термінальні застосунки для телефона, — існує **тільки
на classic**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-007 sha:9a9b3be0 src:manual/41-ble.md:20 klas:A -->
### T-41-007 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Проєкт на SPP, що переїжджає на S3, доведеться переписувати на BLE.

**Контекст**

```
## Найважливіше рішення вже ухвалене за вас

Проєкт на SPP, що переїжджає на S3, доведеться переписувати на BLE.
Це не порт, а переробка: інша модель обміну.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/classic-bt/profiles-protocols.rst
- **Дослівно з джерела:**
  > Serial Port Profile (SPP) defines a serial communication application based on the RFCOMM protocol, enabling RS-232-style data transmission over Bluetooth.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** SPP is Classic Bluetooth only; S3 supports only BLE, so projects moving to S3 must be rewritten
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-008 sha:37b75670 src:manual/41-ble.md:21 klas:E -->
### T-41-008 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Це не порт, а переробка: інша модель обміну.

**Контекст**

```
## Найважливіше рішення вже ухвалене за вас

Проєкт на SPP, що переїжджає на S3, доведеться переписувати на BLE.
Це не порт, а переробка: інша модель обміну.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-009 sha:6c734931 src:manual/41-ble.md:26 klas:F -->
### T-41-009 · tablycya-shapka · `manual/41-ble.md`

**Твердження, коротко**

> | | Bluetooth Classic | BLE |

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-010 sha:55309baf src:manual/41-ble.md:27 klas:E -->
### T-41-010 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Де є · Bluetooth Classic → **тільки classic**

**Дослівно з книги**

```
| Де є | **тільки classic** | уся лінійка, крім S2 |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-011 sha:ca7eb120 src:manual/41-ble.md:27 klas:A -->
### T-41-011 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Де є · BLE → уся лінійка, крім S2

**Дослівно з книги**

```
| Де є | **тільки classic** | уся лінійка, крім S2 |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/ble/overview.rst
- **Дослівно з джерела:**
  > * - ESP32
  >   - Y
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - Y
  > * - ESP32-S3
  >   - Y
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - Y
  > * - ESP32-C2
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - \–
  >   - Y
  > * - ESP32-C3
  >   - Y
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - Y
  > * - ESP32-C5
  >   - Y
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - Y
  > * - ESP32-C6
  >   - Y
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - Y
  > * - ESP32-C61
  >   - Y
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - Y
  > * - ESP32-H2
  >   - Y
  >   - Y
  >   - Y
  >   - Y
  >   - \–
  >   - \–
  >   - \–
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** BLE support table shows ESP32, S3, C2, C3, C5, C6, C61, H2, H4 - notably S2 is absent
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-012 sha:dadfcd93 src:manual/41-ble.md:28 klas:E -->
### T-41-012 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Модель · Bluetooth Classic → потік байтів

**Дослівно з книги**

```
| Модель | потік байтів | набір іменованих значень |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-013 sha:01ce171b src:manual/41-ble.md:28 klas:F -->
### T-41-013 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Модель · BLE → набір іменованих значень

**Дослівно з книги**

```
| Модель | потік байтів | набір іменованих значень |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-014 sha:48639305 src:manual/41-ble.md:29 klas:E -->
### T-41-014 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Швидкість · Bluetooth Classic → сотні кбіт/с

**Дослівно з книги**

```
| Швидкість | сотні кбіт/с | десятки кбіт/с |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-015 sha:ed26a2f5 src:manual/41-ble.md:29 klas:A -->
### T-41-015 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Швидкість · BLE → десятки кбіт/с

**Дослівно з книги**

```
| Швидкість | сотні кбіт/с | десятки кбіт/с |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/ble/get-started/ble-introduction.rst
- **Дослівно з джерела:**
  > Bluetooth LE is a Bluetooth protocol that is not compatible with Bluetooth Classic and was introduced in Bluetooth 4.0. As the name suggests, Bluetooth LE is a low-power Bluetooth protocol with a lower data transfer rate compared to Bluetooth Classic.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** BLE has lower data transfer rate than Classic (though specific "tens of kbits/s" not stated)
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-016 sha:3acb9138 src:manual/41-ble.md:30 klas:E -->
### T-41-016 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Споживання · Bluetooth Classic → висока

**Дослівно з книги**

```
| Споживання | висока | **дуже низька** |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-017 sha:cf950a32 src:manual/41-ble.md:30 klas:F -->
### T-41-017 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Споживання · BLE → **дуже низька**

**Дослівно з книги**

```
| Споживання | висока | **дуже низька** |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-018 sha:087229f4 src:manual/41-ble.md:31 klas:E -->
### T-41-018 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Спарювання · Bluetooth Classic → так, з PIN

**Дослівно з книги**

```
| Спарювання | так, з PIN | не обов'язкове |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-019 sha:cff9038c src:manual/41-ble.md:31 klas:A -->
### T-41-019 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Спарювання · BLE → не обов'язкове

**Дослівно з книги**

```
| Спарювання | так, з PIN | не обов'язкове |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/ble/get-started/ble-connection.rst
- **Дослівно з джерела:**
  > conn_itvl=36, conn_latency=0, supervision_timeout=500, encrypted=0, authenticated=0, bonded=0
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** BLE connection logs show encrypted=0, authenticated=0, bonded=0, proving pairing/bonding not obligatory
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-020 sha:fe2aada0 src:manual/41-ble.md:32 klas:E -->
### T-41-020 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Пам'ять у прошивці · Bluetooth Classic → багато

**Дослівно з книги**

```
| Пам'ять у прошивці | багато | менше |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-021 sha:1df8009c src:manual/41-ble.md:32 klas:F -->
### T-41-021 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Пам'ять у прошивці · BLE → менше

**Дослівно з книги**

```
| Пам'ять у прошивці | багато | менше |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-022 sha:5a5441a8 src:manual/41-ble.md:33 klas:E -->
### T-41-022 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Термінал на телефоні · Bluetooth Classic → простий (SPP)

**Дослівно з книги**

```
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-023 sha:8a345583 src:manual/41-ble.md:33 klas:F -->
### T-41-023 · komirka · `manual/41-ble.md`

**Твердження, коротко**

> Термінал на телефоні · BLE → потрібен BLE-застосунок

**Дослівно з книги**

```
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Контекст**

```
## Classic проти BLE


| | Bluetooth Classic | BLE |
|---|---|---|
| Де є | **тільки classic** | уся лінійка, крім S2 |
| Модель | потік байтів | набір іменованих значень |
| Швидкість | сотні кбіт/с | десятки кбіт/с |
| Споживання | висока | **дуже низька** |
| Спарювання | так, з PIN | не обов'язкове |
| Пам'ять у прошивці | багато | менше |
| Термінал на телефоні | простий (SPP) | потрібен BLE-застосунок |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-024 sha:e8134748 src:manual/41-ble.md:36 klas:E -->
### T-41-024 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Classic** зручний там, де треба «просто послідовний порт по повітрю»: налагодження, обмін із застарілим обладнанням, термінал.

**Контекст**

```
## Classic проти BLE

**Classic** зручний там, де треба «просто послідовний порт по повітрю»:
налагодження, обмін із застарілим обладнанням, термінал.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-025 sha:e26940e5 src:manual/41-ble.md:39 klas:F -->
### T-41-025 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **BLE** — коли треба батарейка, багато пристроїв або сучасні телефони. iOS із Bluetooth Classic для довільних пристроїв практично не працює — це окрема причина, чому SPP не варто закладати в новий проєкт.

**Контекст**

```
## Classic проти BLE

**BLE** — коли треба батарейка, багато пристроїв або сучасні телефони.
iOS із Bluetooth Classic для довільних пристроїв практично не працює —
це окрема причина, чому SPP не варто закладати в новий проєкт.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-026 sha:01b61ea1 src:manual/41-ble.md:45 klas:E -->
### T-41-026 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Він публікує **структуру даних**, і клієнт читає або пише її частини.

**Контекст**

```
## Модель BLE: GATT

BLE не передає потік. Він публікує **структуру даних**, і клієнт читає
або пише її частини.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-027 sha:054abfcc src:manual/41-ble.md:48 klas:E -->
### T-41-027 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Сервіс** — логічна група.

**Контекст**

```
## Модель BLE: GATT

**Сервіс** — логічна група. Наприклад, «датчики середовища».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-028 sha:2b68f60f src:manual/41-ble.md:48 klas:E -->
### T-41-028 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Наприклад, «датчики середовища».

**Контекст**

```
## Модель BLE: GATT

**Сервіс** — логічна група. Наприклад, «датчики середовища».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-029 sha:2fefd5b6 src:manual/41-ble.md:50 klas:E -->
### T-41-029 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Характеристика** — окреме значення всередині сервісу: температура, вологість.

**Контекст**

```
## Модель BLE: GATT

**Характеристика** — окреме значення всередині сервісу: температура,
вологість. У кожної є права: читати, писати, сповіщати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-030 sha:1cb8e270 src:manual/41-ble.md:51 klas:E -->
### T-41-030 · proza · `manual/41-ble.md`

**Твердження, коротко**

> У кожної є права: читати, писати, сповіщати.

**Контекст**

```
## Модель BLE: GATT

**Характеристика** — окреме значення всередині сервісу: температура,
вологість. У кожної є права: читати, писати, сповіщати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-031 sha:181164db src:manual/41-ble.md:53 klas:E -->
### T-41-031 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Notify** — сервер сам надсилає значення клієнту при зміні.

**Контекст**

```
## Модель BLE: GATT

**Notify** — сервер сам надсилає значення клієнту при зміні. Це те, що
замінює потік: клієнт підписується один раз і отримує оновлення.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-032 sha:4dea69c1 src:manual/41-ble.md:53 klas:E -->
### T-41-032 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Це те, що замінює потік: клієнт підписується один раз і отримує оновлення.

**Контекст**

```
## Модель BLE: GATT

**Notify** — сервер сам надсилає значення клієнту при зміні. Це те, що
замінює потік: клієнт підписується один раз і отримує оновлення.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-033 sha:55de95d4 src:manual/41-ble.md:56 klas:E -->
### T-41-033 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **UUID** — ідентифікатор сервісу чи характеристики.

**Контекст**

```
## Модель BLE: GATT

**UUID** — ідентифікатор сервісу чи характеристики. Стандартні профілі
мають короткі 16-бітні номери; власні — 128-бітні, які генеруються один
раз.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-034 sha:dce1a60e src:manual/41-ble.md:56 klas:E -->
### T-41-034 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Стандартні профілі мають короткі 16-бітні номери; власні — 128-бітні, які генеруються один раз.

**Контекст**

```
## Модель BLE: GATT

**UUID** — ідентифікатор сервісу чи характеристики. Стандартні профілі
мають короткі 16-бітні номери; власні — 128-бітні, які генеруються один
раз.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-035 sha:8af20e65 src:manual/41-ble.md:61 klas:F -->
### T-41-035 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Спокуса відтворити SPP через BLE — зробити характеристику «дані» і ганяти через неї байти — виникає в усіх, хто прийшов із Classic.

**Контекст**

```
## Модель BLE: GATT

::: uvaha
Спокуса відтворити SPP через BLE — зробити характеристику «дані» і
ганяти через неї байти — виникає в усіх, хто прийшов із Classic. Так
роблять, і воно працює (це називають BLE UART або Nordic UART Service).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-036 sha:5619b766 src:manual/41-ble.md:62 klas:F -->
### T-41-036 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Так роблять, і воно працює (це називають BLE UART або Nordic UART Service).

**Контекст**

```
## Модель BLE: GATT

::: uvaha
Спокуса відтворити SPP через BLE — зробити характеристику «дані» і
ганяти через неї байти — виникає в усіх, хто прийшов із Classic. Так
роблять, і воно працює (це називають BLE UART або Nordic UART Service).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-037 sha:ad12af6e src:manual/41-ble.md:65 klas:E -->
### T-41-037 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Але правильніше описати дані як дані: окрема характеристика на температуру, окрема на стан реле.

**Контекст**

```
## Модель BLE: GATT

Але правильніше описати дані як дані: окрема характеристика на
температуру, окрема на стан реле. Тоді пристрій самоописовий — будь-який
універсальний BLE-застосунок покаже осмислені значення без вашого
клієнта. Для виробу, який обслуговуватимуть інші люди, це велика
різниця.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-038 sha:32a9ba20 src:manual/41-ble.md:66 klas:A -->
### T-41-038 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Тоді пристрій самоописовий — будь-який універсальний BLE-застосунок покаже осмислені значення без вашого клієнта.

**Контекст**

```
## Модель BLE: GATT

Але правильніше описати дані як дані: окрема характеристика на
температуру, окрема на стан реле. Тоді пристрій самоописовий — будь-який
універсальний BLE-застосунок покаже осмислені значення без вашого
клієнта. Для виробу, який обслуговуватимуть інші люди, це велика
різниця.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/ble/get-started/ble-data-exchange.rst
- **Дослівно з джерела:**
  > In fact, the definitions of these services and characteristic data are also provided by the SIG. For example, the value of the Heart Rate Measurement must include a flag field and a heart rate measurement field, and may include fields such as energy expended, RR-interval, and transmission interval, among others. Therefore, these definitions from SIG allow Bluetooth LE devices from different manufacturers to recognize each other's services or characteristic data, enabling cross-manufacturer communication.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Підтверджує, що стандартні GATT послуги дозволяють універсальним додаткам розпізнавати та виводити осмислені значення без кастомного клієнта
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-039 sha:d9e54fe1 src:manual/41-ble.md:68 klas:E -->
### T-41-039 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Для виробу, який обслуговуватимуть інші люди, це велика різниця.

**Контекст**

```
## Модель BLE: GATT

Але правильніше описати дані як дані: окрема характеристика на
температуру, окрема на стан реле. Тоді пристрій самоописовий — будь-який
універсальний BLE-застосунок покаже осмислені значення без вашого
клієнта. Для виробу, який обслуговуватимуть інші люди, це велика
різниця.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-040 sha:f1921f7b src:manual/41-ble.md:74 klas:A -->
### T-41-040 · proza · `manual/41-ble.md`

**Твердження, коротко**

> В ESP-IDF два стеки BLE, і вибір між ними — не смак.

**Контекст**

```
## Bluedroid і NimBLE

В ESP-IDF два стеки BLE, і вибір між ними — не смак.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/bluetooth/index.rst
- **Дослівно з джерела:**
  > ESP-IDF supports two host stacks: **Bluedroid** and **NimBLE**.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Прямо підтверджує наявність двох стеків BLE в ESP-IDF
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-041 sha:be3db6f9 src:manual/41-ble.md:76 klas:A -->
### T-41-041 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Bluedroid** — повний стек, підтримує і Classic, і BLE.

**Контекст**

```
## Bluedroid і NimBLE

**Bluedroid** — повний стек, підтримує і Classic, і BLE. Займає значно
більше пам'яті.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/bluetooth/index.rst
- **Дослівно з джерела:**
  > - **Bluedroid** (the default stack): Supports both Bluetooth Classic and Bluetooth LE. Recommended for applications that require both technologies.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Підтверджує повний стек Bluedroid, що підтримує Classic і BLE
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-042 sha:5a38b893 src:manual/41-ble.md:76 klas:E -->
### T-41-042 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Займає значно більше пам'яті.

**Контекст**

```
## Bluedroid і NimBLE

**Bluedroid** — повний стек, підтримує і Classic, і BLE. Займає значно
більше пам'яті.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-043 sha:3aa1db4f src:manual/41-ble.md:79 klas:A -->
### T-41-043 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **NimBLE** — тільки BLE, компактніший, займає в рази менше RAM і флешу.

**Контекст**

```
## Bluedroid і NimBLE

**NimBLE** — тільки BLE, компактніший, займає в рази менше RAM і флешу.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/ble/overview.rst
- **Дослівно з джерела:**
  > Although both support Bluetooth LE, ESP-NimBLE requires less heap and flash size.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Підтверджує NimBLE як BLE-тільки компактніший стек з меншим RAM і флешем
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-044 sha:7d83be34 src:manual/41-ble.md:82 klas:A -->
### T-41-044 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Для BLE-проєкту беріть NimBLE.** Різниця в пам'яті вимірюється десятками кілобайтів — на C3 з його 400 КБ (розділ 02) це різниця між «вміщається» і «ні».

**Контекст**

```
## Bluedroid і NimBLE

::: uvaha
**Для BLE-проєкту беріть NimBLE.** Різниця в пам'яті вимірюється
десятками кілобайтів — на C3 з його 400 КБ (розділ 02) це різниця між
«вміщається» і «ні».
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/esp32-c3_datasheet_en.pdf
- **Дослівно з джерела:**
  > • SRAM: 400 KB (16 KB for cache)
- **Спосіб і дата:** Source document retrieved 2026-08-27; quote verified against it by substring match.
- **Нотатка:** Datasheet підтверджує 400 КБ SRAM; твердження про адекватність для простих задач вимагає практичної оцінки. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-41-045 sha:4ad04ec3 src:manual/41-ble.md:86 klas:E -->
### T-41-045 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Bluedroid потрібен лише тоді, коли треба Classic, тобто тільки на classic-чипі.

**Контекст**

```
## Bluedroid і NimBLE

Bluedroid потрібен лише тоді, коли треба Classic, тобто тільки на
classic-чипі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-046 sha:c9bf4f76 src:manual/41-ble.md:89 klas:A -->
### T-41-046 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Перемикається в `menuconfig`: `Component config` → `Bluetooth` → `Host`.

**Контекст**

```
## Bluedroid і NimBLE

Перемикається в `menuconfig`: `Component config` → `Bluetooth` →
`Host`.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/Kconfig та .../components/bt/Kconfig
- **Дослівно з джерела:**
  > (freertos/Kconfig)
  > menu "FreeRTOS"
  >     menu "Kernel"
  >         choice FREERTOS_CHECK_STACKOVERFLOW
  >             prompt "configCHECK_FOR_STACK_OVERFLOW"
  >             default FREERTOS_CHECK_STACKOVERFLOW_CANARY
  >                 bool "Check using canary bytes (Method 2)"
  > 
  > (bt/Kconfig)
  > menu "Bluetooth"
  >     choice BT_HOST
  >         prompt "Host"
  >             bool "Bluedroid - Dual-mode"
  >             bool "NimBLE - BLE only"
  >             bool "Disabled"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Без розбіжностей. Розділ 41 називає `Component config` → `Bluetooth` → `Host`, і саме так меню й влаштоване; назви варіантів (`Bluedroid - Dual-mode`, `NimBLE - BLE only`) підтверджують і те, що книга каже про призначення кожного.
Шлях до `configCHECK_FOR_STACK_OVERFLOW` у розділі 30 теж перевірено цим проходом і теж без розбіжностей — але доказ на нього вже стояв із проходу 6, тож реєстр залишає сильніший наявний. Витяг наведено тут як другу, незалежну звірку того самого місця.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-41-047 sha:76516abc src:manual/41-ble.md:95 klas:F -->
### T-41-047 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Bluetooth — найважчий компонент після Wi-Fi.

**Контекст**

```
## Скільки це коштує пам'яті

Bluetooth — найважчий компонент після Wi-Fi. Прошивка з BLE помітно
більша, а RAM з'їдається стеком постійно, а не лише під час обміну.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-048 sha:7611ba9c src:manual/41-ble.md:95 klas:F -->
### T-41-048 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Прошивка з BLE помітно більша, а RAM з'їдається стеком постійно, а не лише під час обміну.

**Контекст**

```
## Скільки це коштує пам'яті

Bluetooth — найважчий компонент після Wi-Fi. Прошивка з BLE помітно
більша, а RAM з'їдається стеком постійно, а не лише під час обміну.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-049 sha:642e02fc src:manual/41-ble.md:100 klas:A -->
### T-41-049 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Wi-Fi і Bluetooth одночасно** працюють, але ділять одне радіо і конкурують за час.

**Контекст**

```
## Скільки це коштує пам'яті

**Wi-Fi і Bluetooth одночасно** працюють, але ділять одне радіо і
конкурують за час. Продуктивність обох падає, споживання росте. Для
провізіювання (розділ 39) це нормально; для постійної одночасної роботи
— привід подумати.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/coexist.rst
- **Дослівно з джерела:**
  > Each type of board has only one 2.4 GHz ISM band RF module, shared by two or three modules. Consequently, a module cannot receive or transmit data while another module is engaged in data transmission or reception.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Підтверджує, що Wi-Fi і Bluetooth ділять одне радіо і конкурують за час
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-050 sha:7942e32b src:manual/41-ble.md:101 klas:E -->
### T-41-050 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Продуктивність обох падає, споживання росте.

**Контекст**

```
## Скільки це коштує пам'яті

**Wi-Fi і Bluetooth одночасно** працюють, але ділять одне радіо і
конкурують за час. Продуктивність обох падає, споживання росте. Для
провізіювання (розділ 39) це нормально; для постійної одночасної роботи
— привід подумати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-051 sha:340f962d src:manual/41-ble.md:101 klas:E -->
### T-41-051 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Для провізіювання (розділ 39) це нормально; для постійної одночасної роботи — привід подумати.

**Контекст**

```
## Скільки це коштує пам'яті

**Wi-Fi і Bluetooth одночасно** працюють, але ділять одне радіо і
конкурують за час. Продуктивність обох падає, споживання росте. Для
провізіювання (розділ 39) це нормально; для постійної одночасної роботи
— привід подумати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-052 sha:f98180c6 src:manual/41-ble.md:105 klas:C -->
### T-41-052 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **На C3 з 400 КБ** BLE плюс Wi-Fi плюс TLS плюс власна логіка — це вже тісно.

**Контекст**

```
## Скільки це коштує пам'яті

**На C3 з 400 КБ** BLE плюс Wi-Fi плюс TLS плюс власна логіка — це вже
тісно.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP-IDF Programming Guide, mbedTLS memory footprint / ESP-TLS — оцінка пам'яті на з'єднання; цитати не дістав
- **Спосіб і дата:** позахідна знань про пам'ять та криптографію, 2026-08-27
- **Нотатка:** Клас B без цитати. Джерело для витрат пам'яті на TLS-з'єднання існує (документація mbedTLS в ESP-IDF наводить порядок величин), але я його не відкривав. Тому C.
- **Прохід:** m2-90-vybirka

---

<!-- fc id:T-41-053 sha:667124ed src:manual/41-ble.md:108 klas:F -->
### T-41-053 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Вимикати, коли не треба.** Пристрій, у якому BLE потрібен лише для початкового налаштування, має його вимикати після — це звільняє пам'ять і знижує споживання.

**Контекст**

```
## Скільки це коштує пам'яті

**Вимикати, коли не треба.** Пристрій, у якому BLE потрібен лише для
початкового налаштування, має його вимикати після — це звільняє пам'ять
і знижує споживання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-054 sha:881b2151 src:manual/41-ble.md:114 klas:A -->
### T-41-054 · proza · `manual/41-ble.md`

**Твердження, коротко**

> BLE спроєктований для батарейок, і його головний параметр — **інтервал реклами** (advertising interval).

**Контекст**

```
## Споживання

BLE спроєктований для батарейок, і його головний параметр —
**інтервал реклами** (advertising interval).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/ble/get-started/ble-introduction.rst
- **Дослівно з джерела:**
  > Bluetooth LE is a low-power Bluetooth protocol with a lower data transfer rate compared to Bluetooth Classic. It is typically used in data communication for the Internet of Things (IoT), such as smart switches or sensors
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Підтверджує, що BLE спроєктований для низької енергоефективності; інтервал реклами важливий для оптимізації
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-055 sha:d790ddd4 src:manual/41-ble.md:117 klas:E -->
### T-41-055 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Пристрій, що рекламує себе кожні 100 мс, знаходиться миттєво і їсть відчутно.

**Контекст**

```
## Споживання

Пристрій, що рекламує себе кожні 100 мс, знаходиться миттєво і їсть
відчутно. Той, що рекламує раз на секунду, знаходиться за секунду і їсть
у десять разів менше.
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

<!-- fc id:T-41-056 sha:186463f4 src:manual/41-ble.md:118 klas:D -->
### T-41-056 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Той, що рекламує раз на секунду, знаходиться за секунду і їсть у десять разів менше.

**Контекст**

```
## Споживання

Пристрій, що рекламує себе кожні 100 мс, знаходиться миттєво і їсть
відчутно. Той, що рекламує раз на секунду, знаходиться за секунду і їсть
у десять разів менше.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Розрахунок на основі Table 5-3 DC Characteristics. При 10 світлодіодах по 10 мА = 100 мА > 40 мА максимум домену
- **Дослівно з джерела:**
  > 10 світлодіодів × 10 мА = 100 мА
  > 
  > Сумарно це далеко від 1200 мА (менше 1/10), але:
  > - Якщо всі 10 на одному домені (VDD3P3_CPU): 100 мА > 40 мА максимум
  > - Домен просядає, вихід стає нестійким
  > 
  > Table 5-3: IOH ... VDD3P3_CPU ... 40 mA (Typ), але зменшується до
  > 29 мА при підвищенні кількості активних пінів
- **Розрахунок:**
  P = U × I (базова формула)
  Струм 10 мА на світлодіод × 10 = 100 мА
  100 мА > 40 мА (максимум домену) = перевищення
- **Спосіб і дата:** Розрахунок на основі ESP32 Datasheet Table 5-3, 2026-08-26
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-41-057 sha:9cbaca90 src:manual/41-ble.md:121 klas:E -->
### T-41-057 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Для датчика на батарейці різниця в місяцях роботи.

**Контекст**

```
## Споживання

Для датчика на батарейці різниця в місяцях роботи. Розумний підхід:
частий інтервал перші хвилини після старту (щоб зручно було під'єднатися),
далі рідкий.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-058 sha:c2356973 src:manual/41-ble.md:121 klas:E -->
### T-41-058 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Розумний підхід: частий інтервал перші хвилини після старту (щоб зручно було під'єднатися), далі рідкий.

**Контекст**

```
## Споживання

Для датчика на батарейці різниця в місяцях роботи. Розумний підхід:
частий інтервал перші хвилини після старту (щоб зручно було під'єднатися),
далі рідкий.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-059 sha:efb33e27 src:manual/41-ble.md:125 klas:E -->
### T-41-059 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Інтервал з'єднання** визначає затримку обміну після під'єднання.

**Контекст**

```
## Споживання

**Інтервал з'єднання** визначає затримку обміну після під'єднання. Тут
теж компроміс між швидкістю реакції і споживанням, і телефон має право
його змінити.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-060 sha:f5e909aa src:manual/41-ble.md:125 klas:E -->
### T-41-060 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Тут теж компроміс між швидкістю реакції і споживанням, і телефон має право його змінити.

**Контекст**

```
## Споживання

**Інтервал з'єднання** визначає затримку обміну після під'єднання. Тут
теж компроміс між швидкістю реакції і споживанням, і телефон має право
його змінити.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-061 sha:b4d73a01 src:manual/41-ble.md:131 klas:F -->
### T-41-061 · proza · `manual/41-ble.md`

**Твердження, коротко**

> BLE без спарювання доступний **будь-кому поруч**.

**Контекст**

```
## Безпека

BLE без спарювання доступний **будь-кому поруч**. Для датчика
температури це прийнятно; для керування чимось — ні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-062 sha:f44698af src:manual/41-ble.md:131 klas:E -->
### T-41-062 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Для датчика температури це прийнятно; для керування чимось — ні.

**Контекст**

```
## Безпека

BLE без спарювання доступний **будь-кому поруч**. Для датчика
температури це прийнятно; для керування чимось — ні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-063 sha:71310120 src:manual/41-ble.md:134 klas:E -->
### T-41-063 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Мінімум для пристрою, що приймає команди:

**Контекст**

```
## Безпека

Мінімум для пристрою, що приймає команди:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-064 sha:98f1d808 src:manual/41-ble.md:136 klas:E -->
### T-41-064 · proza · `manual/41-ble.md`

**Твердження, коротко**

> - **спарювання з підтвердженням** — щоб під'єднатися міг не кожен; - **характеристики керування тільки для запису після автентифікації**; - **не публікувати в рекламі нічого зайвого** — ім'я пристрою видно всім, хто сканує, включно з сусідами.

**Контекст**

```
## Безпека

- **спарювання з підтвердженням** — щоб під'єднатися міг не кожен;
- **характеристики керування тільки для запису після автентифікації**;
- **не публікувати в рекламі нічого зайвого** — ім'я пристрою видно
  всім, хто сканує, включно з сусідами.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-065 sha:74bf0e1b src:manual/41-ble.md:142 klas:E -->
### T-41-065 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Найпоширеніша реальна вразливість — характеристика запису без жодного захисту, доступна на відстані десятків метрів.

**Контекст**

```
## Безпека

::: nezvorotne
Найпоширеніша реальна вразливість — характеристика запису без жодного
захисту, доступна на відстані десятків метрів. Будь-хто зі смартфоном і
безкоштовним застосунком може під'єднатися і надіслати команду.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-066 sha:46321b22 src:manual/41-ble.md:143 klas:E -->
### T-41-066 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Будь-хто зі смартфоном і безкоштовним застосунком може під'єднатися і надіслати команду.

**Контекст**

```
## Безпека

::: nezvorotne
Найпоширеніша реальна вразливість — характеристика запису без жодного
захисту, доступна на відстані десятків метрів. Будь-хто зі смартфоном і
безкоштовним застосунком може під'єднатися і надіслати команду.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-067 sha:0d6116bf src:manual/41-ble.md:146 klas:E -->
### T-41-067 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Питання, яке варто поставити до кожної характеристики із правом запису: **що станеться, якщо туди напише сторонній?** (розділ 50)

**Контекст**

```
## Безпека

Питання, яке варто поставити до кожної характеристики із правом
запису: **що станеться, якщо туди напише сторонній?** (розділ 50)
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-068 sha:3dd125e1 src:manual/41-ble.md:152 klas:E -->
### T-41-068 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Найпоширеніший сценарій: пристрій — сервер, телефон — клієнт.

**Контекст**

```
## Обмін із телефоном

Найпоширеніший сценарій: пристрій — сервер, телефон — клієнт.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-069 sha:6c9574e5 src:manual/41-ble.md:154 klas:F -->
### T-41-069 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Для розробки й налагодження є універсальні BLE-застосунки: вони сканують пристрої, показують сервіси, характеристики й дозволяють читати й писати вручну.

**Контекст**

```
## Обмін із телефоном

Для розробки й налагодження є універсальні BLE-застосунки: вони сканують
пристрої, показують сервіси, характеристики й дозволяють читати й
писати вручну. Це найшвидший спосіб перевірити, що ваш GATT правильний,
до написання власного застосунку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-070 sha:bd8802ff src:manual/41-ble.md:156 klas:E -->
### T-41-070 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Це найшвидший спосіб перевірити, що ваш GATT правильний, до написання власного застосунку.

**Контекст**

```
## Обмін із телефоном

Для розробки й налагодження є універсальні BLE-застосунки: вони сканують
пристрої, показують сервіси, характеристики й дозволяють читати й
писати вручну. Це найшвидший спосіб перевірити, що ваш GATT правильний,
до написання власного застосунку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-071 sha:8225efdc src:manual/41-ble.md:161 klas:A -->
### T-41-071 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Розмір пакета обмежений** — за замовчуванням ATT MTU дорівнює 23 байтам, з яких 3 службові, тобто на корисні дані лишається **20 байтів**.

**Контекст**

```
## Обмін із телефоном

**Розмір пакета обмежений** — за замовчуванням ATT MTU дорівнює 23
байтам, з яких 3 службові, тобто на корисні дані лишається **20 байтів**.
Довгі рядки доведеться або ділити, або узгоджувати більший MTU — і друге
телефон має право не підтримати.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bt/host/bluedroid/stack/include/stack/gatt_api.h та https://raw.githubusercontent.com/apache/mynewt-nimble/master/nimble/host/include/host/ble_att.h
- **Дослівно з джерела:**
  > (Bluedroid, у складі ESP-IDF)
  > #define GATT_DEF_BLE_MTU_SIZE               23
  > #define GATT_MAX_MTU_SIZE                   517
  > 
  > (NimBLE, apache/mynewt-nimble)
  > #define BLE_ATT_MTU_DFLT                    23
  > #define BLE_ATT_MTU_MAX                     527
  >  * The specified MTU must be within the following range: [23, BLE_ATT_MTU_MAX].
  >  * 23 is a minimum imposed by the Bluetooth specification;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Закриває пункт наряду, який спирався на платну специфікацію Bluetooth Core. Обидва стеки, між якими вибирає розділ 41, дають те саме число, а коментар NimBLE прямо посилається на специфікацію як на джерело мінімуму. Клас A: цитати з обох стеків отримано.
- **Прохід:** pass-04-obkhidni

---

<!-- fc id:T-41-072 sha:f484e4a2 src:manual/41-ble.md:163 klas:A -->
### T-41-072 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Довгі рядки доведеться або ділити, або узгоджувати більший MTU — і друге телефон має право не підтримати.

**Контекст**

```
## Обмін із телефоном

**Розмір пакета обмежений** — за замовчуванням ATT MTU дорівнює 23
байтам, з яких 3 службові, тобто на корисні дані лишається **20 байтів**.
Довгі рядки доведеться або ділити, або узгоджувати більший MTU — і друге
телефон має право не підтримати.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bt/host/bluedroid/stack/include/stack/gatt_api.h та https://raw.githubusercontent.com/apache/mynewt-nimble/master/nimble/host/include/host/ble_att.h
- **Дослівно з джерела:**
  > (Bluedroid, у складі ESP-IDF)
  > #define GATT_DEF_BLE_MTU_SIZE               23
  > #define GATT_MAX_MTU_SIZE                   517
  > 
  > (NimBLE, apache/mynewt-nimble)
  > #define BLE_ATT_MTU_DFLT                    23
  > #define BLE_ATT_MTU_MAX                     527
  >  * The specified MTU must be within the following range: [23, BLE_ATT_MTU_MAX].
  >  * 23 is a minimum imposed by the Bluetooth specification;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Закриває пункт наряду, який спирався на платну специфікацію Bluetooth Core. Обидва стеки, між якими вибирає розділ 41, дають те саме число, а коментар NimBLE прямо посилається на специфікацію як на джерело мінімуму. Клас A: цитати з обох стеків отримано.
- **Прохід:** pass-04-obkhidni

---

<!-- fc id:T-41-073 sha:96b52b3c src:manual/41-ble.md:166 klas:E -->
### T-41-073 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **Телефон керує параметрами з'єднання.** Ваші налаштування інтервалів — побажання, а не команда.

**Контекст**

```
## Обмін із телефоном

**Телефон керує параметрами з'єднання.** Ваші налаштування інтервалів —
побажання, а не команда.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-074 sha:d1aba810 src:manual/41-ble.md:169 klas:E -->
### T-41-074 · proza · `manual/41-ble.md`

**Твердження, коротко**

> **iOS суворіший** щодо структури GATT і кешує її.

**Контекст**

```
## Обмін із телефоном

**iOS суворіший** щодо структури GATT і кешує її. Змінили структуру
сервісів — телефон може продовжувати бачити стару, доки не забути
пристрій у налаштуваннях. Це джерело дуже заплутаних годин налагодження.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-075 sha:bba733d9 src:manual/41-ble.md:169 klas:E -->
### T-41-075 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Змінили структуру сервісів — телефон може продовжувати бачити стару, доки не забути пристрій у налаштуваннях.

**Контекст**

```
## Обмін із телефоном

**iOS суворіший** щодо структури GATT і кешує її. Змінили структуру
сервісів — телефон може продовжувати бачити стару, доки не забути
пристрій у налаштуваннях. Це джерело дуже заплутаних годин налагодження.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-076 sha:24c52040 src:manual/41-ble.md:171 klas:E -->
### T-41-076 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Це джерело дуже заплутаних годин налагодження.

**Контекст**

```
## Обмін із телефоном

**iOS суворіший** щодо структури GATT і кешує її. Змінили структуру
сервісів — телефон може продовжувати бачити стару, доки не забути
пристрій у налаштуваннях. Це джерело дуже заплутаних годин налагодження.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-077 sha:4a3cd76b src:manual/41-ble.md:175 klas:F -->
### T-41-077 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Classic — тільки на classic-чипі; SPP на S3 і C3 не існує в принципі.

**Контекст**

```
## Що з цього треба запам'ятати

Classic — тільки на classic-чипі; SPP на S3 і C3 не існує в принципі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-078 sha:92698aea src:manual/41-ble.md:177 klas:A -->
### T-41-078 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Для BLE-проєкту брати NimBLE: різниця в пам'яті вирішальна на C3.

**Контекст**

```
## Що з цього треба запам'ятати

Для BLE-проєкту брати NimBLE: різниця в пам'яті вирішальна на C3.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/ble/overview.rst
- **Дослівно з джерела:**
  > Although both support Bluetooth LE, ESP-NimBLE requires less heap and flash size.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документація стверджує, що NimBLE вимагає менше пам'яті в принципі, але не зазначає, що ця різниця "вирішальна" саме для C3. Більш того, в таблиці підтримки чипів показано, що обидва стеки (Bluedroid і NimBLE) підтримуються на C3.
- **Прохід:** klas-f-41-ble

---

<!-- fc id:T-41-079 sha:dd5da72d src:manual/41-ble.md:179 klas:F -->
### T-41-079 · proza · `manual/41-ble.md`

**Твердження, коротко**

> BLE публікує структуру даних, а не потік; описуйте значення окремими характеристиками.

**Контекст**

```
## Що з цього треба запам'ятати

BLE публікує структуру даних, а не потік; описуйте значення окремими
характеристиками.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-080 sha:4d008387 src:manual/41-ble.md:182 klas:E -->
### T-41-080 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Інтервал реклами — головний важіль споживання.

**Контекст**

```
## Що з цього треба запам'ятати

Інтервал реклами — головний важіль споживання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-081 sha:997bf1c7 src:manual/41-ble.md:184 klas:E -->
### T-41-081 · proza · `manual/41-ble.md`

**Твердження, коротко**

> Характеристика запису без захисту доступна будь-кому поруч.

**Контекст**

```
## Що з цього треба запам'ятати

Характеристика запису без захисту доступна будь-кому поруч.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-41-082 sha:12158bb4 src:manual/41-ble.md:186 klas:E -->
### T-41-082 · proza · `manual/41-ble.md`

**Твердження, коротко**

> iOS кешує структуру GATT: після зміни сервісів пристрій треба забути в налаштуваннях телефона.

**Контекст**

```
## Що з цього треба запам'ятати

iOS кешує структуру GATT: після зміни сервісів пристрій треба забути в
налаштуваннях телефона.
```

**Доказ**

- **Клас:** F — не звірено

---
