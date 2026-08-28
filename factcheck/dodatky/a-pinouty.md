# Фактчекінг: `dodatky/a-pinouty.md`

Одиниць твердження: **123**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-A-001 sha:7be6df09 src:dodatky/a-pinouty.md:3 klas:D -->
### T-A-001 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Розгорнута версія картки [К9](#k-pinouty).

**Контекст**

```
# Додаток A. Повні пінаут-таблиці {#dod-pinouty}

Розгорнута версія картки [К9](#k-pinouty). Обмеження пояснені в
розділі 07; тут — повні таблиці для звірки.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/cross_refs.py — перевірка проти дерева файлів репозиторію
- **Розрахунок:**
  posylannya: згадок 689, адресатів 79, помилок 0
  
  Перевірено:
    «розділ NN»  → існує manual/NN-*.md, і це не той самий розділ
    «картка КN»  → існує kartky/kNN-*.md
    «додаток X»  → існує dodatky/x-*.md (з переведенням кириличної
                   букви в латинську назву файлу)
- **Спосіб і дата:** python3 tools/cross_refs.py, 2026-08-26
- **Нотатка:** Нуль помилок із 689 згадок. Це другий вимір після арифметики й API, де прохід не дав жодного виправлення.
Клас `D`, а не `A`: зовнішнє джерело тут не потрібне й не буває — перевіряється твердження книги про саму себе, і перевіряється механічно.
Головне тут не результат, а те, що перевірка тепер постійна: `tools/cross_refs.py` стоїть у `make check`. Досі номер розділу можна було зсунути, і жоден інструмент цього б не помітив — текст лишається зв'язним, а читач іде не туди.
Одне самопосилання цей інструмент уже спіймав раніше, у проході 9 (розділ 17 відсилав сам на себе); тоді його знайшов `review.py` на клікабельному посиланні. Тепер такий самий контроль поширено на прозу.
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-A-002 sha:3a0c7d75 src:dodatky/a-pinouty.md:3 klas:E -->
### T-A-002 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Обмеження пояснені в розділі 07; тут — повні таблиці для звірки.

**Контекст**

```
# Додаток A. Повні пінаут-таблиці {#dod-pinouty}

Розгорнута версія картки [К9](#k-pinouty). Обмеження пояснені в
розділі 07; тут — повні таблиці для звірки.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-003 sha:20376379 src:dodatky/a-pinouty.md:7 klas:E -->
### T-A-003 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> **Pinout плати важливіший за pinout чипа.** Виробник міг вивести не всі піни, підписати їх власними іменами, повісити світлодіод чи резистор.

**Контекст**

```
# Додаток A. Повні пінаут-таблиці {#dod-pinouty}

::: uvaha
**Pinout плати важливіший за pinout чипа.** Виробник міг вивести не всі
піни, підписати їх власними іменами, повісити світлодіод чи резистор.
Таблиці нижче описують **чип**; конкретну плату звіряйте з її схемою
(розділ 08).
:::
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

<!-- fc id:T-A-004 sha:2015cd18 src:dodatky/a-pinouty.md:9 klas:E -->
### T-A-004 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Таблиці нижче описують **чип**; конкретну плату звіряйте з її схемою (розділ 08).

**Контекст**

```
# Додаток A. Повні пінаут-таблиці {#dod-pinouty}

::: uvaha
**Pinout плати важливіший за pinout чипа.** Виробник міг вивести не всі
піни, підписати їх власними іменами, повісити світлодіод чи резистор.
Таблиці нижче описують **чип**; конкретну плату звіряйте з її схемою
(розділ 08).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-005 sha:388a34df src:dodatky/a-pinouty.md:15 klas:F -->
### T-A-005 · tablycya-shapka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> | GPIO | Обмеження | ADC | Touch | Примітка |

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-006 sha:5000c0ba src:dodatky/a-pinouty.md:16 klas:F -->
### T-A-006 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 0 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-007 sha:e947fae0 src:dodatky/a-pinouty.md:16 klas:A -->
### T-A-007 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 0 · ADC → ADC2_1

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/adc_channel.h та .../esp32/include/soc/touch_sensor_channel.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)
  > ADC1: CH0→36 CH1→37 CH2→38 CH3→39 CH4→32 CH5→33 CH6→34 CH7→35
  > ADC2: CH0→4 CH1→0 CH2→2 CH3→15 CH4→13 CH5→12 CH6→14 CH7→27 CH8→25 CH9→26
  > 
  > (esp32/touch_sensor_channel.h)
  > T0→4 T1→0 T2→2 T3→15 T4→13 T5→12 T6→14 T7→27 T8→33 T9→32
  > 
  > (esp32s3) ADC1: 1…10   ADC2: 11…20
  > (esp32c3) ADC1: 0…4    ADC2: 5
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у найдрібнішому місці книги. Звірено **кожну** комірку таблиці classic: усі десять номерів каналів ADC2, усі вісім ADC1, усі десять сенсорів touch.
Окремо звернімо увагу на рядок `32, 33 | ADC1_4/5 | T9/T8`: тут порядок навмисно різний, бо `GPIO32` — це `T9`, а `GPIO33` — `T8`. Легко було б поставити «T8/T9» і помилитися; у книзі стоїть правильно.
Списки «ADC1 працює завжди: 32–39» і «ADC2 не працює при Wi-Fi: 0, 2, 4, 12–15, 25–27» збігаються з заголовком повністю.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-008 sha:092e56b9 src:dodatky/a-pinouty.md:16 klas:E -->
### T-A-008 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 0 · Touch → T1

**Дослівно з книги**

```
|---|---|---|---|---|
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-009 sha:a8d9831a src:dodatky/a-pinouty.md:16 klas:A -->
### T-A-009 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 0 · Примітка → `BOOT`; низький = download mode

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/uart_pins.h
- **Дослівно з джерела:**
  > #define U0RXD_GPIO_NUM  (3)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 0 - strapping пін BOOT; низький = download mode
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-010 sha:4985f051 src:dodatky/a-pinouty.md:17 klas:A -->
### T-A-010 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 1 · Обмеження → UART0 TX

**Дослівно з книги**

```
| 1 | UART0 TX | — | — | консоль |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/uart_pins.h
- **Дослівно з джерела:**
  > #define U0TXD_GPIO_NUM  (1)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 1 - апаратний пін UART0 TX на ESP32 classic
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-011 sha:b06bf589 src:dodatky/a-pinouty.md:17 klas:A -->
### T-A-011 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 1 · Примітка → консоль

**Дослівно з книги**

```
| 1 | UART0 TX | — | — | консоль |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/uart_pins.h
- **Дослівно з джерела:**
  > #define U0RXD_GPIO_NUM  (3)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 3 - апаратний пін UART0 RX на ESP32 classic, консоль
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-012 sha:e5de6037 src:dodatky/a-pinouty.md:18 klas:F -->
### T-A-012 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 2 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-013 sha:8c4af79f src:dodatky/a-pinouty.md:18 klas:F -->
### T-A-013 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 2 · ADC → ADC2_2

**Дослівно з книги**

```
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-014 sha:9b9041b5 src:dodatky/a-pinouty.md:18 klas:E -->
### T-A-014 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 2 · Touch → T2

**Дослівно з книги**

```
| 1 | UART0 TX | — | — | консоль |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-015 sha:cf70cbf0 src:dodatky/a-pinouty.md:18 klas:E -->
### T-A-015 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 2 · Примітка → часто вбудований світлодіод

**Дослівно з книги**

```
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-016 sha:876f7496 src:dodatky/a-pinouty.md:19 klas:A -->
### T-A-016 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 3 · Обмеження → UART0 RX

**Дослівно з книги**

```
| 3 | UART0 RX | — | — | консоль |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/uart_pins.h
- **Дослівно з джерела:**
  > #define U0RXD_GPIO_NUM  (3)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 3 - UART0 RX на ESP32 classic
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-017 sha:ed43aba0 src:dodatky/a-pinouty.md:19 klas:A -->
### T-A-017 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 3 · Примітка → консоль

**Дослівно з книги**

```
| 1 | UART0 TX | — | — | консоль |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/uart_pins.h
- **Дослівно з джерела:**
  > #define U0RXD_GPIO_NUM  (3)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 3 - UART0 RX, консоль
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-018 sha:ed03bfea src:dodatky/a-pinouty.md:20 klas:F -->
### T-A-018 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 4 · ADC → ADC2_0

**Дослівно з книги**

```
| 4 | — | ADC2_0 | T0 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-019 sha:05bb8e87 src:dodatky/a-pinouty.md:20 klas:E -->
### T-A-019 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 4 · Touch → T0

**Дослівно з книги**

```
| 3 | UART0 RX | — | — | консоль |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-020 sha:4d0bd90a src:dodatky/a-pinouty.md:20 klas:E -->
### T-A-020 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 4 · Примітка → вільний

**Дослівно з книги**

```
| 4 | — | ADC2_0 | T0 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-021 sha:72e7b29e src:dodatky/a-pinouty.md:21 klas:F -->
### T-A-021 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 5 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-022 sha:b215d5b9 src:dodatky/a-pinouty.md:21 klas:E -->
### T-A-022 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 5 · Примітка → типовий SPI CS

**Дослівно з книги**

```
| 5 | **strapping** | — | — | типовий SPI CS |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

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

<!-- fc id:T-A-023 sha:c20d762c src:dodatky/a-pinouty.md:22 klas:E -->
### T-A-023 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 6–11 · Обмеження → **флеш — не чіпати**

**Дослівно з книги**

```
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-024 sha:87ce2d39 src:dodatky/a-pinouty.md:22 klas:E -->
### T-A-024 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 6–11 · Примітка → ⛔ ніколи

**Дослівно з книги**

```
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-025 sha:18d879e2 src:dodatky/a-pinouty.md:23 klas:A -->
### T-A-025 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 12 · Обмеження → **strapping (MTDI)**

**Дослівно з книги**

```
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild
- **Дослівно з джерела:**
  > choice BOOTLOADER_VDDSDIO_BOOST
  >     bool "VDDSDIO LDO voltage"
  >     default BOOTLOADER_VDDSDIO_BOOST_1_9V
  >     depends on SOC_CONFIGURABLE_VDDSDIO_SUPPORTED
  >     help
  >         If this option is enabled, and VDDSDIO LDO is set to 1.8V (using eFuse
  >         or MTDI bootstrapping pin), bootloader will change LDO settings to
  >         output 1.9V instead. This helps prevent flash chip from browning out
  >         during flash programming operations.
  > 
  >         This option has no effect if VDDSDIO is set to 3.3V, or if the internal
  >         VDDSDIO regulator is disabled via eFuse.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу — уточнення механізму. Книга писала, що GPIO12 «задає напругу, яку стабілізатор подає на мікросхему флешу», і на цьому зупинялася. Kconfig називає і сам стабілізатор (`VDDSDIO`), і обидва значення: високий рівень MTDI дає **1.8 В**, низький — 3.3 В.
З цього випливає те, чого в книзі не було і що змінює діагностику: плата мовчить не тому, що «пін злий», а тому, що на більшості модулів флеш тривольтовий і від 1.8 В не запускається. На модулі з 1.8-вольтовим флешем той самий рівень — правильний. Тобто «у сусіда працює» тут не доводить нічого. Додано в розділ 07.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-A-026 sha:abe0de18 src:dodatky/a-pinouty.md:23 klas:F -->
### T-A-026 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 12 · ADC → ADC2_5

**Дослівно з книги**

```
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-027 sha:3ec06bb0 src:dodatky/a-pinouty.md:23 klas:E -->
### T-A-027 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 12 · Touch → T5

**Дослівно з книги**

```
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-028 sha:a4683015 src:dodatky/a-pinouty.md:23 klas:E -->
### T-A-028 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 12 · Примітка → ⛔ високий при старті = не стартує

**Дослівно з книги**

```
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-029 sha:63e35bc2 src:dodatky/a-pinouty.md:24 klas:F -->
### T-A-029 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 13 · Обмеження → JTAG TCK

**Дослівно з книги**

```
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-030 sha:9e3f89fa src:dodatky/a-pinouty.md:24 klas:F -->
### T-A-030 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 13 · ADC → ADC2_4

**Дослівно з книги**

```
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-031 sha:fdd88742 src:dodatky/a-pinouty.md:24 klas:E -->
### T-A-031 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 13 · Touch → T4

**Дослівно з книги**

```
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-032 sha:82afe384 src:dodatky/a-pinouty.md:24 klas:E -->
### T-A-032 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 13 · Примітка → вільний

**Дослівно з книги**

```
| 4 | — | ADC2_0 | T0 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-033 sha:ce47eb55 src:dodatky/a-pinouty.md:25 klas:F -->
### T-A-033 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 14 · Обмеження → JTAG TMS

**Дослівно з книги**

```
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-034 sha:87f25f3b src:dodatky/a-pinouty.md:25 klas:F -->
### T-A-034 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 14 · ADC → ADC2_6

**Дослівно з книги**

```
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-035 sha:590ac959 src:dodatky/a-pinouty.md:25 klas:E -->
### T-A-035 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 14 · Touch → T6

**Дослівно з книги**

```
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-036 sha:cba43828 src:dodatky/a-pinouty.md:25 klas:E -->
### T-A-036 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 14 · Примітка → вільний

**Дослівно з книги**

```
| 4 | — | ADC2_0 | T0 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-037 sha:4ad5886e src:dodatky/a-pinouty.md:26 klas:A -->
### T-A-037 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 15 · Обмеження → **strapping (MTDO)**

**Дослівно з книги**

```
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 12 (MTDI)   | If driven High, flash voltage (VDD_SDIO) is 1.8V not default 3.3V…
  > | 15 (MTDO)   | If driven Low, silences boot messages printed by the ROM bootloader…
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Половина таблиці JTAG розділу 27 закривається дослівно, і закривається джерелом із зовсім іншої теми: документація esptool називає `GPIO12` саме як `MTDI`, а `GPIO15` — як `MTDO`.
Це водночас підтверджує головне попередження розділу 27: обидва піни JTAG на classic — strapping-піни. `MTDI` високий при старті означає флеш на 1.8 В, а `MTDO` низький глушить boot-лог. Тобто під'єднаний адаптер може і не дати платі стартувати, і забрати лог, яким це діагностують.
- **Прохід:** pass-20-jtag-obvyazka

---

<!-- fc id:T-A-038 sha:59ca81f5 src:dodatky/a-pinouty.md:26 klas:F -->
### T-A-038 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 15 · ADC → ADC2_3

**Дослівно з книги**

```
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-039 sha:edc7c97b src:dodatky/a-pinouty.md:26 klas:E -->
### T-A-039 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 15 · Touch → T3

**Дослівно з книги**

```
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-040 sha:ca9296f3 src:dodatky/a-pinouty.md:26 klas:E -->
### T-A-040 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 15 · Примітка → вільний з обережністю

**Дослівно з книги**

```
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-041 sha:080598b8 src:dodatky/a-pinouty.md:27 klas:F -->
### T-A-041 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 16, 17 · Примітка → вільні; зайняті на WROVER (PSRAM)

**Дослівно з книги**

```
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-042 sha:8d087270 src:dodatky/a-pinouty.md:28 klas:E -->
### T-A-042 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 18, 19 · Примітка → типові SPI SCK, MISO

**Дослівно з книги**

```
| 18, 19 | — | — | — | типові SPI SCK, MISO |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

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

<!-- fc id:T-A-043 sha:6ec98572 src:dodatky/a-pinouty.md:29 klas:F -->
### T-A-043 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 21, 22 · Примітка → типові I²C SDA, SCL

**Дослівно з книги**

```
| 21, 22 | — | — | — | типові I²C SDA, SCL |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-044 sha:cefe078e src:dodatky/a-pinouty.md:30 klas:E -->
### T-A-044 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 23 · Примітка → типовий SPI MOSI

**Дослівно з книги**

```
| 23 | — | — | — | типовий SPI MOSI |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

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

<!-- fc id:T-A-045 sha:64083f4c src:dodatky/a-pinouty.md:31 klas:A -->
### T-A-045 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 25 · Обмеження → **DAC1**

**Дослівно з книги**

```
| 25 | **DAC1** | ADC2_8 | — | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/dac_channel.h
- **Дослівно з джерела:**
  > DAC_GPIO25_CHANNEL      DAC_CHAN_0
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 25 is DAC channel 0 (DAC1)
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-046 sha:7d926829 src:dodatky/a-pinouty.md:31 klas:A -->
### T-A-046 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 25 · ADC → ADC2_8

**Дослівно з книги**

```
| 25 | **DAC1** | ADC2_8 | — | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > ADC2_GPIO25_CHANNEL     8
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 25 corresponds to ADC2 channel 8
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-047 sha:04ee97cb src:dodatky/a-pinouty.md:32 klas:A -->
### T-A-047 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 26 · Обмеження → **DAC2**

**Дослівно з книги**

```
| 26 | **DAC2** | ADC2_9 | — | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/dac_channel.h
- **Дослівно з джерела:**
  > DAC_GPIO26_CHANNEL      DAC_CHAN_1
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 26 is DAC channel 1 (DAC2)
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-048 sha:7ea69553 src:dodatky/a-pinouty.md:32 klas:A -->
### T-A-048 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 26 · ADC → ADC2_9

**Дослівно з книги**

```
| 26 | **DAC2** | ADC2_9 | — | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/adc_channel.h та .../esp32/include/soc/touch_sensor_channel.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)
  > ADC1: CH0→36 CH1→37 CH2→38 CH3→39 CH4→32 CH5→33 CH6→34 CH7→35
  > ADC2: CH0→4 CH1→0 CH2→2 CH3→15 CH4→13 CH5→12 CH6→14 CH7→27 CH8→25 CH9→26
  > 
  > (esp32/touch_sensor_channel.h)
  > T0→4 T1→0 T2→2 T3→15 T4→13 T5→12 T6→14 T7→27 T8→33 T9→32
  > 
  > (esp32s3) ADC1: 1…10   ADC2: 11…20
  > (esp32c3) ADC1: 0…4    ADC2: 5
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у найдрібнішому місці книги. Звірено **кожну** комірку таблиці classic: усі десять номерів каналів ADC2, усі вісім ADC1, усі десять сенсорів touch.
Окремо звернімо увагу на рядок `32, 33 | ADC1_4/5 | T9/T8`: тут порядок навмисно різний, бо `GPIO32` — це `T9`, а `GPIO33` — `T8`. Легко було б поставити «T8/T9» і помилитися; у книзі стоїть правильно.
Списки «ADC1 працює завжди: 32–39» і «ADC2 не працює при Wi-Fi: 0, 2, 4, 12–15, 25–27» збігаються з заголовком повністю.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-049 sha:c7c1cbc2 src:dodatky/a-pinouty.md:33 klas:A -->
### T-A-049 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 27 · ADC → ADC2_7

**Дослівно з книги**

```
| 27 | — | ADC2_7 | T7 | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > ADC2_GPIO27_CHANNEL     7
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 27 corresponds to ADC2 channel 7
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-050 sha:60266760 src:dodatky/a-pinouty.md:33 klas:E -->
### T-A-050 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 27 · Touch → T7

**Дослівно з книги**

```
| 26 | **DAC2** | ADC2_9 | — | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-051 sha:ab6a85b6 src:dodatky/a-pinouty.md:34 klas:A -->
### T-A-051 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 32, 33 · ADC → ADC1_4/5

**Дослівно з книги**

```
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/adc_channel.h та .../esp32/include/soc/touch_sensor_channel.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)
  > ADC1: CH0→36 CH1→37 CH2→38 CH3→39 CH4→32 CH5→33 CH6→34 CH7→35
  > ADC2: CH0→4 CH1→0 CH2→2 CH3→15 CH4→13 CH5→12 CH6→14 CH7→27 CH8→25 CH9→26
  > 
  > (esp32/touch_sensor_channel.h)
  > T0→4 T1→0 T2→2 T3→15 T4→13 T5→12 T6→14 T7→27 T8→33 T9→32
  > 
  > (esp32s3) ADC1: 1…10   ADC2: 11…20
  > (esp32c3) ADC1: 0…4    ADC2: 5
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у найдрібнішому місці книги. Звірено **кожну** комірку таблиці classic: усі десять номерів каналів ADC2, усі вісім ADC1, усі десять сенсорів touch.
Окремо звернімо увагу на рядок `32, 33 | ADC1_4/5 | T9/T8`: тут порядок навмисно різний, бо `GPIO32` — це `T9`, а `GPIO33` — `T8`. Легко було б поставити «T8/T9» і помилитися; у книзі стоїть правильно.
Списки «ADC1 працює завжди: 32–39» і «ADC2 не працює при Wi-Fi: 0, 2, 4, 12–15, 25–27» збігаються з заголовком повністю.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-052 sha:45814a6b src:dodatky/a-pinouty.md:34 klas:A -->
### T-A-052 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 32, 33 · Touch → T9/T8

**Дослівно з книги**

```
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/adc_channel.h та .../esp32/include/soc/touch_sensor_channel.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)
  > ADC1: CH0→36 CH1→37 CH2→38 CH3→39 CH4→32 CH5→33 CH6→34 CH7→35
  > ADC2: CH0→4 CH1→0 CH2→2 CH3→15 CH4→13 CH5→12 CH6→14 CH7→27 CH8→25 CH9→26
  > 
  > (esp32/touch_sensor_channel.h)
  > T0→4 T1→0 T2→2 T3→15 T4→13 T5→12 T6→14 T7→27 T8→33 T9→32
  > 
  > (esp32s3) ADC1: 1…10   ADC2: 11…20
  > (esp32c3) ADC1: 0…4    ADC2: 5
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у найдрібнішому місці книги. Звірено **кожну** комірку таблиці classic: усі десять номерів каналів ADC2, усі вісім ADC1, усі десять сенсорів touch.
Окремо звернімо увагу на рядок `32, 33 | ADC1_4/5 | T9/T8`: тут порядок навмисно різний, бо `GPIO32` — це `T9`, а `GPIO33` — `T8`. Легко було б поставити «T8/T9» і помилитися; у книзі стоїть правильно.
Списки «ADC1 працює завжди: 32–39» і «ADC2 не працює при Wi-Fi: 0, 2, 4, 12–15, 25–27» збігаються з заголовком повністю.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-053 sha:f2882492 src:dodatky/a-pinouty.md:34 klas:F -->
### T-A-053 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 32, 33 · Примітка → **ADC1 — працює при Wi-Fi**

**Дослівно з книги**

```
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-054 sha:486e3929 src:dodatky/a-pinouty.md:35 klas:E -->
### T-A-054 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 34–39 · Обмеження → **тільки вхід, без підтягування**

**Дослівно з книги**

```
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-055 sha:892263e2 src:dodatky/a-pinouty.md:35 klas:F -->
### T-A-055 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 34–39 · ADC → ADC1

**Дослівно з книги**

```
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-056 sha:b5b763e8 src:dodatky/a-pinouty.md:38 klas:E -->
### T-A-056 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> **Вільні без застережень:** 4, 13, 14, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 32, 33.

**Контекст**

```
## ESP32 classic (WROOM-32)

**Вільні без застережень:** 4, 13, 14, 16, 17, 18, 19, 21, 22, 23, 25,
26, 27, 32, 33.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-057 sha:4c059759 src:dodatky/a-pinouty.md:41 klas:A -->
### T-A-057 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> **ADC1** (працює завжди): 32, 33, 34, 35, 36, 37, 38, 39.

**Контекст**

```
## ESP32 classic (WROOM-32)

**ADC1** (працює завжди): 32, 33, 34, 35, 36, 37, 38, 39.
**ADC2** (не працює при Wi-Fi): 0, 2, 4, 12, 13, 14, 15, 25, 26, 27.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/adc_channel.h та .../esp32/include/soc/touch_sensor_channel.h
- **Дослівно з джерела:**
  > (esp32/adc_channel.h)
  > ADC1: CH0→36 CH1→37 CH2→38 CH3→39 CH4→32 CH5→33 CH6→34 CH7→35
  > ADC2: CH0→4 CH1→0 CH2→2 CH3→15 CH4→13 CH5→12 CH6→14 CH7→27 CH8→25 CH9→26
  > 
  > (esp32/touch_sensor_channel.h)
  > T0→4 T1→0 T2→2 T3→15 T4→13 T5→12 T6→14 T7→27 T8→33 T9→32
  > 
  > (esp32s3) ADC1: 1…10   ADC2: 11…20
  > (esp32c3) ADC1: 0…4    ADC2: 5
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей у найдрібнішому місці книги. Звірено **кожну** комірку таблиці classic: усі десять номерів каналів ADC2, усі вісім ADC1, усі десять сенсорів touch.
Окремо звернімо увагу на рядок `32, 33 | ADC1_4/5 | T9/T8`: тут порядок навмисно різний, бо `GPIO32` — це `T9`, а `GPIO33` — `T8`. Легко було б поставити «T8/T9» і помилитися; у книзі стоїть правильно.
Списки «ADC1 працює завжди: 32–39» і «ADC2 не працює при Wi-Fi: 0, 2, 4, 12–15, 25–27» збігаються з заголовком повністю.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-058 sha:577c3369 src:dodatky/a-pinouty.md:42 klas:F -->
### T-A-058 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> **ADC2** (не працює при Wi-Fi): 0, 2, 4, 12, 13, 14, 15, 25, 26, 27.

**Контекст**

```
## ESP32 classic (WROOM-32)

**ADC1** (працює завжди): 32, 33, 34, 35, 36, 37, 38, 39.
**ADC2** (не працює при Wi-Fi): 0, 2, 4, 12, 13, 14, 15, 25, 26, 27.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-059 sha:c143225d src:dodatky/a-pinouty.md:46 klas:F -->
### T-A-059 · tablycya-shapka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> | GPIO | Обмеження | Примітка |

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-060 sha:5000c0ba src:dodatky/a-pinouty.md:47 klas:F -->
### T-A-060 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 0 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-061 sha:5fb9bafa src:dodatky/a-pinouty.md:47 klas:F -->
### T-A-061 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 0 · Примітка → `BOOT`

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-062 sha:ffb2b847 src:dodatky/a-pinouty.md:48 klas:F -->
### T-A-062 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 3 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-063 sha:8d001f58 src:dodatky/a-pinouty.md:49 klas:A -->
### T-A-063 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 19, 20 · Обмеження → **native USB** D−, D+

**Дослівно з книги**

```
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

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

<!-- fc id:T-A-064 sha:72fbec74 src:dodatky/a-pinouty.md:49 klas:E -->
### T-A-064 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 19, 20 · Примітка → втрачаються при перевизначенні

**Дослівно з книги**

```
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-065 sha:8d8d045c src:dodatky/a-pinouty.md:50 klas:A -->
### T-A-065 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 26–32 · Обмеження → **флеш і PSRAM**

**Дослівно з книги**

```
| 26–32 | **флеш і PSRAM** | не чіпати |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/56497005-external-ram.rst
- **Дослівно з джерела:**
  > The external memory is incorporated in the memory map and, with certain restrictions, is usable in the same way as internal data RAM.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ згадує обмеження для флеш/PSRAM.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-A-066 sha:cbb51688 src:dodatky/a-pinouty.md:50 klas:E -->
### T-A-066 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 26–32 · Примітка → не чіпати

**Дослівно з книги**

```
| 26–32 | **флеш і PSRAM** | не чіпати |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-067 sha:5ead256e src:dodatky/a-pinouty.md:51 klas:A -->
### T-A-067 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 33–37 · Обмеження → флеш/PSRAM на Octal-модулях

**Дослівно з книги**

```
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/56497005-external-ram.rst
- **Дослівно з джерела:**
  > PSRAM access speed may be faster than flash access, so the overall application performance may be better. For example, if the PSRAM is an Octal mode (8-line PSRAM) and is configured to 80 MHz, then it is faster than a Quad flash (4-line flash) which is configured to 80 MHz.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ згадує octal PSRAM на цих чипах.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-A-068 sha:c329711f src:dodatky/a-pinouty.md:51 klas:F -->
### T-A-068 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 33–37 · Примітка → `N16R8` і подібні

**Дослівно з книги**

```
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-069 sha:69ff4be4 src:dodatky/a-pinouty.md:52 klas:F -->
### T-A-069 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 45, 46 · Обмеження → **strapping**

**Дослівно з книги**

```
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-070 sha:c1435f95 src:dodatky/a-pinouty.md:52 klas:A -->
### T-A-070 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 45, 46 · Примітка → ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний

**Дослівно з книги**

```
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > .. only:: esp32 or esp32s2 or esp32s3
  > 
  >    {IDF_TARGET_STRAP_BOOT_2_GPIO} must also be either left unconnected/floating,
  >    or driven Low, in order to enter the serial bootloader.
  > 
  > .. only:: esp32c3 or esp32c2 or esp32h2 or esp32c6 or esp32p4 or esp32c5 or esp32c61 …
  > 
  >    {IDF_TARGET_STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  >    serial bootloader reliably. The strapping combination of {…STRAP_BOOT_2_GPIO} = 0
  >    and {…STRAP_BOOT_GPIO} = 0 is invalid and will trigger unexpected behavior.
  > 
  > In normal boot mode ({…STRAP_BOOT_GPIO} high), {…STRAP_BOOT_2_GPIO} is ignored.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення, і воно дороге. Книга у трьох місцях писала, що на S3 «комбінація `GPIO46` = 1 разом із `GPIO0` = 0 недійсна». Це правило з **C3**, механічно перенесене на S3 — разом із переверненим рівнем.
Правда протилежна: на classic, S2 і S3 другий пін мусить бути **низьким або вільним**, щоб увійти в бутлоадер. Поняття «недійсна комбінація» існує тільки в RISC-V сімействах, де другий пін навпаки має бути високим.
Ціна помилки — саме та, заради якої пінаути й друкують: розробник плати на S3, читаючи книгу, підтягне `GPIO46` угору «щоб уникнути недійсної комбінації» — і зробить download mode недосяжним на всій партії.
Виправлено в розділі 07, на картці К9 і в додатку A; у розділ 07 додано таблицю на три сімейства, бо саме перенесення плати з чипа на чип і породжує цю помилку.
Заразом зафіксовано правило, якого книга не називала: у звичайному режимі (головний пін високий) другий пін ігнорується взагалі.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-071 sha:6ab0e3c0 src:dodatky/a-pinouty.md:53 klas:F -->
### T-A-071 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 1–10 · Обмеження → ADC1

**Дослівно з книги**

```
| 1–10 | ADC1 | працює при Wi-Fi |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-072 sha:c57bbbac src:dodatky/a-pinouty.md:53 klas:F -->
### T-A-072 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 1–10 · Примітка → працює при Wi-Fi

**Дослівно з книги**

```
| 1–10 | ADC1 | працює при Wi-Fi |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-073 sha:a632ce30 src:dodatky/a-pinouty.md:54 klas:F -->
### T-A-073 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 11–20 · Обмеження → ADC2

**Дослівно з книги**

```
| 11–20 | ADC2 | |
```

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-074 sha:ce399c4d src:dodatky/a-pinouty.md:57 klas:E -->
### T-A-074 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Тільки-вхідних пінів немає — усі повнофункціональні.

**Контекст**

```
## ESP32-S3 (WROOM-1)

Тільки-вхідних пінів немає — усі повнофункціональні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-075 sha:f7b36f07 src:dodatky/a-pinouty.md:60 klas:A -->
### T-A-075 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> [[S3]] Модулі `N8` і `N16R8` мають **різну** кількість доступних пінів: Octal PSRAM з'їдає GPIO 33–37.

**Контекст**

```
## ESP32-S3 (WROOM-1)

::: uvaha
[[S3]] Модулі `N8` і `N16R8` мають **різну** кількість доступних пінів:
Octal PSRAM з'їдає GPIO 33–37. Перед розводкою плати треба точно знати,
який модуль стоїть (розділ 07).
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32s3/include/soc/spi_pins.h та .../components/soc/esp32s3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define MSPI_IOMUX_PIN_NUM_CS1      26
  > #define MSPI_IOMUX_PIN_NUM_HD       27
  > #define MSPI_IOMUX_PIN_NUM_WP       28
  > #define MSPI_IOMUX_PIN_NUM_CS0      29
  > #define MSPI_IOMUX_PIN_NUM_CLK      30
  > #define MSPI_IOMUX_PIN_NUM_MISO     31
  > #define MSPI_IOMUX_PIN_NUM_MOSI     32
  > #define MSPI_IOMUX_PIN_NUM_D4       33
  > #define MSPI_IOMUX_PIN_NUM_D5       34
  > #define MSPI_IOMUX_PIN_NUM_D6       35
  > #define MSPI_IOMUX_PIN_NUM_D7       36
  > #define MSPI_IOMUX_PIN_NUM_DQS      37
  > 
  > (soc_caps.h)
  > #define SOC_GPIO_PIN_COUNT                 49
  > #define SOC_SPIRAM_SUPPORTED            1
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Звірено без розбіжностей, і збіг тут точніший, ніж очікувалося: сім пінів MSPI — це рівно `GPIO26`–`GPIO32`, як пише книга, а чотири лінії даних `D4`–`D7` плюс `DQS` — рівно `GPIO33`–`GPIO37`.
Підтвердилося й число: «октальна PSRAM з'їдає **п'ять** додаткових пінів» — 33, 34, 35, 36, 37, тобто п'ять і є.
Твердження живе в чотирьох місцях (розділи 07 і 23, додаток A, картка К9) і скрізь однакове — рідкісний випадок, коли пропагація спрацювала сама.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-A-076 sha:1f79377a src:dodatky/a-pinouty.md:61 klas:E -->
### T-A-076 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Перед розводкою плати треба точно знати, який модуль стоїть (розділ 07).

**Контекст**

```
## ESP32-S3 (WROOM-1)

::: uvaha
[[S3]] Модулі `N8` і `N16R8` мають **різну** кількість доступних пінів:
Octal PSRAM з'їдає GPIO 33–37. Перед розводкою плати треба точно знати,
який модуль стоїть (розділ 07).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-077 sha:c143225d src:dodatky/a-pinouty.md:67 klas:F -->
### T-A-077 · tablycya-shapka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> | GPIO | Обмеження | Примітка |

**Контекст**

```
## ESP32-S3 (WROOM-1)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 0 | **strapping** | `BOOT` |
| 3 | **strapping** | |
| 19, 20 | **native USB** D−, D+ | втрачаються при перевизначенні |
| 26–32 | **флеш і PSRAM** | не чіпати |
| 33–37 | флеш/PSRAM на Octal-модулях | `N16R8` і подібні |
| 45, 46 | **strapping** | ⛔ `46` мусить бути низьким або вільним, інакше download mode недосяжний |
| 1–10 | ADC1 | працює при Wi-Fi |
| 11–20 | ADC2 | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-078 sha:e5de6037 src:dodatky/a-pinouty.md:68 klas:F -->
### T-A-078 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 2 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-079 sha:199390fa src:dodatky/a-pinouty.md:69 klas:F -->
### T-A-079 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 8 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-080 sha:93f4a490 src:dodatky/a-pinouty.md:69 klas:E -->
### T-A-080 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 8 · Примітка → має бути високим для download mode

**Дослівно з книги**

```
| 8 | **strapping** | має бути високим для download mode |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-081 sha:633261ce src:dodatky/a-pinouty.md:70 klas:F -->
### T-A-081 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 9 · Обмеження → **strapping**

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-082 sha:354711b9 src:dodatky/a-pinouty.md:70 klas:E -->
### T-A-082 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 9 · Примітка → низький при скиданні = download mode

**Дослівно з книги**

```
| 9 | **strapping** | низький при скиданні = download mode |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-083 sha:decb25b1 src:dodatky/a-pinouty.md:71 klas:E -->
### T-A-083 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 12–17 · Обмеження → **флеш**

**Дослівно з книги**

```
| 12–17 | **флеш** | не чіпати |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-084 sha:d87ed22f src:dodatky/a-pinouty.md:71 klas:E -->
### T-A-084 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 12–17 · Примітка → не чіпати

**Дослівно з книги**

```
| 12–17 | **флеш** | не чіпати |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-085 sha:2c8c2e8f src:dodatky/a-pinouty.md:72 klas:A -->
### T-A-085 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 18, 19 · Обмеження → **USB-Serial-JTAG**

**Дослівно з книги**

```
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

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

<!-- fc id:T-A-086 sha:2fcf634e src:dodatky/a-pinouty.md:72 klas:E -->
### T-A-086 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 18, 19 · Примітка → втрачається налагодження

**Дослівно з книги**

```
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-087 sha:3e05c152 src:dodatky/a-pinouty.md:73 klas:F -->
### T-A-087 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 0–4 · Обмеження → ADC1

**Дослівно з книги**

```
| 0–4 | ADC1 | |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-088 sha:6fd20726 src:dodatky/a-pinouty.md:74 klas:A -->
### T-A-088 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 5 · Обмеження → ADC2

**Дослівно з книги**

```
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
```

**Контекст**

```
## ESP32 classic (WROOM-32)


| GPIO | Обмеження | ADC | Touch | Примітка |
|---|---|---|---|---|
| 0 | **strapping** | ADC2_1 | T1 | `BOOT`; низький = download mode |
| 1 | UART0 TX | — | — | консоль |
| 2 | **strapping** | ADC2_2 | T2 | часто вбудований світлодіод |
| 3 | UART0 RX | — | — | консоль |
| 4 | — | ADC2_0 | T0 | вільний |
| 5 | **strapping** | — | — | типовий SPI CS |
| 6–11 | **флеш — не чіпати** | — | — | ⛔ ніколи |
| 12 | **strapping (MTDI)** | ADC2_5 | T5 | ⛔ високий при старті = не стартує |
| 13 | JTAG TCK | ADC2_4 | T4 | вільний |
| 14 | JTAG TMS | ADC2_6 | T6 | вільний |
| 15 | **strapping (MTDO)** | ADC2_3 | T3 | вільний з обережністю |
| 16, 17 | — | — | — | вільні; зайняті на WROVER (PSRAM) |
| 18, 19 | — | — | — | типові SPI SCK, MISO |
| 21, 22 | — | — | — | типові I²C SDA, SCL |
| 23 | — | — | — | типовий SPI MOSI |
| 25 | **DAC1** | ADC2_8 | — | |
| 26 | **DAC2** | ADC2_9 | — | |
| 27 | — | ADC2_7 | T7 | |
| 32, 33 | — | ADC1_4/5 | T9/T8 | **ADC1 — працює при Wi-Fi** |
| 34–39 | **тільки вхід, без підтягування** | ADC1 | — | |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > ADC2_GPIO5_CHANNEL      0
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** GPIO 5 is ADC2 channel 0 on ESP32-C3
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-089 sha:9b2d4e43 src:dodatky/a-pinouty.md:74 klas:A -->
### T-A-089 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> 5 · Примітка → ⛔ разовий режим не підтримується, див. нижче

**Дослівно з книги**

```
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)


| GPIO | Обмеження | Примітка |
|---|---|---|
| 2 | **strapping** | |
| 8 | **strapping** | має бути високим для download mode |
| 9 | **strapping** | низький при скиданні = download mode |
| 12–17 | **флеш** | не чіпати |
| 18, 19 | **USB-Serial-JTAG** | втрачається налагодження |
| 0–4 | ADC1 | |
| 5 | ADC2 | ⛔ разовий режим не підтримується, див. нижче |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- **Дослівно з джерела:**
  > :esp32c3: - ADC2 oneshot mode is no longer supported, due to hardware limitations.
  > The results are not stable. This issue can be found in `ESP32-C3 Series SoC Errata`.
  > For compatibility, you can enable :ref:`CONFIG_ADC_ONESHOT_FORCE_USE_ADC2_ON_C3` to force use ADC2.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу, і серйозніша за попередню. Картка К9 і додаток A подавали `GPIO5` на C3 як звичайний аналоговий вхід. Насправді разовий режим ADC2 на C3 в ESP-IDF вимкнено через ваду кремнію, і ввімкнути його можна лише примусовим перемикачем. Читач, який заклав цей пін в аналогову частину плати, отримав би нестабільні показання без жодного повідомлення. Виправлено в картці К9 і додатку A, де тепер сказано прямо: на C3 аналоговий вхід — це GPIO0–GPIO4.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-A-090 sha:9fd74c06 src:dodatky/a-pinouty.md:77 klas:A -->
### T-A-090 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> ⛔ Комбінація `GPIO8`=0 і `GPIO9`=0 недійсна.

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)

⛔ Комбінація `GPIO8`=0 і `GPIO9`=0 недійсна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../esp-idf/components/soc/esp32c3/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > {STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  > serial bootloader reliably. The strapping combination of
  > {STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and will
  > trigger unexpected behavior.
  > (для esp32c3: STRAP_BOOT_2_GPIO = GPIO8, STRAP_BOOT_GPIO = GPIO9)
  > 
  > (esp32c3/adc_channel.h)
  > ADC1_GPIO0_CHANNEL 0   ADC1_GPIO1_CHANNEL 1   ADC1_GPIO2_CHANNEL 2
  > ADC1_GPIO3_CHANNEL 3   ADC1_GPIO4_CHANNEL 4
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Додаток A робить із двох звірених фактів висновок, і висновок правильний у неочевидний бік: типова обв'язка I²C на C3 завантаженню **не заважає**. Підтяжки тягнуть обидві лінії вгору, а потрібно саме `GPIO8` високий; `GPIO9` високий означає звичайний старт.
Друга половина — застереження, і воно точне: ведений, що притискає `SDA` до землі в момент скидання, дає `GPIO8` = 0. Разом із `GPIO9` = 0 (натиснута кнопка `BOOT`) це та сама недійсна комбінація.
«На C3 аналоговий вхід — це `GPIO0`–`GPIO4`, і більше нічого» — п'ять каналів `adc_channel.h`, рівно цей діапазон.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-A-091 sha:02d9e968 src:dodatky/a-pinouty.md:80 klas:A -->
### T-A-091 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> [[C3]] **ADC2 на C3 непридатний для звичайних вимірювань.** Це не конфлікт із Wi-Fi, як на classic, S2 і S3, а апаратна вада самого чипа: разовий режим (oneshot) на ADC2 в ESP-IDF **вимкнено**, бо результати нестабільні.

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)

::: nezvorotne
[[C3]] **ADC2 на C3 непридатний для звичайних вимірювань.** Це не
конфлікт із Wi-Fi, як на classic, S2 і S3, а апаратна вада самого чипа:
разовий режим (oneshot) на ADC2 в ESP-IDF **вимкнено**, бо результати
нестабільні. Драйвер має примусовий перемикач, щоб увімкнути його назад,
і вмикати його немає підстав.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- **Дослівно з джерела:**
  > :esp32c3: - ADC2 oneshot mode is no longer supported, due to hardware limitations.
  > The results are not stable. This issue can be found in `ESP32-C3 Series SoC Errata`.
  > For compatibility, you can enable :ref:`CONFIG_ADC_ONESHOT_FORCE_USE_ADC2_ON_C3` to force use ADC2.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу, і серйозніша за попередню. Картка К9 і додаток A подавали `GPIO5` на C3 як звичайний аналоговий вхід. Насправді разовий режим ADC2 на C3 в ESP-IDF вимкнено через ваду кремнію, і ввімкнути його можна лише примусовим перемикачем. Читач, який заклав цей пін в аналогову частину плати, отримав би нестабільні показання без жодного повідомлення. Виправлено в картці К9 і додатку A, де тепер сказано прямо: на C3 аналоговий вхід — це GPIO0–GPIO4.
- **Прохід:** pass-02-povedinka

---

<!-- fc id:T-A-092 sha:4afef0e1 src:dodatky/a-pinouty.md:83 klas:E -->
### T-A-092 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Драйвер має примусовий перемикач, щоб увімкнути його назад, і вмикати його немає підстав.

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)

::: nezvorotne
[[C3]] **ADC2 на C3 непридатний для звичайних вимірювань.** Це не
конфлікт із Wi-Fi, як на classic, S2 і S3, а апаратна вада самого чипа:
разовий режим (oneshot) на ADC2 в ESP-IDF **вимкнено**, бо результати
нестабільні. Драйвер має примусовий перемикач, щоб увімкнути його назад,
і вмикати його немає підстав.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-093 sha:32636b98 src:dodatky/a-pinouty.md:86 klas:A -->
### T-A-093 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Практичний наслідок для розводки плати: на C3 аналоговий вхід — це `GPIO0`–`GPIO4`, і більше нічого.

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)

Практичний наслідок для розводки плати: на C3 аналоговий вхід — це
`GPIO0`–`GPIO4`, і більше нічого. П'ятий пін як аналоговий закладати не
можна.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../esp-idf/components/soc/esp32c3/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > {STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  > serial bootloader reliably. The strapping combination of
  > {STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and will
  > trigger unexpected behavior.
  > (для esp32c3: STRAP_BOOT_2_GPIO = GPIO8, STRAP_BOOT_GPIO = GPIO9)
  > 
  > (esp32c3/adc_channel.h)
  > ADC1_GPIO0_CHANNEL 0   ADC1_GPIO1_CHANNEL 1   ADC1_GPIO2_CHANNEL 2
  > ADC1_GPIO3_CHANNEL 3   ADC1_GPIO4_CHANNEL 4
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Додаток A робить із двох звірених фактів висновок, і висновок правильний у неочевидний бік: типова обв'язка I²C на C3 завантаженню **не заважає**. Підтяжки тягнуть обидві лінії вгору, а потрібно саме `GPIO8` високий; `GPIO9` високий означає звичайний старт.
Друга половина — застереження, і воно точне: ведений, що притискає `SDA` до землі в момент скидання, дає `GPIO8` = 0. Разом із `GPIO9` = 0 (натиснута кнопка `BOOT`) це та сама недійсна комбінація.
«На C3 аналоговий вхід — це `GPIO0`–`GPIO4`, і більше нічого» — п'ять каналів `adc_channel.h`, рівно цей діапазон.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-A-094 sha:8e250d60 src:dodatky/a-pinouty.md:87 klas:E -->
### T-A-094 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> П'ятий пін як аналоговий закладати не можна.

**Контекст**

```
## ESP32-C3 (MINI-1, SuperMini)

Практичний наслідок для розводки плати: на C3 аналоговий вхід — це
`GPIO0`–`GPIO4`, і більше нічого. П'ятий пін як аналоговий закладати не
можна.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-095 sha:40ed1cdb src:dodatky/a-pinouty.md:95 klas:E -->
### T-A-095 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Тут змішано дві різні речі, і плутати їх дорого.

**Контекст**

```
## Піни за замовчуванням

Тут змішано дві різні речі, і плутати їх дорого.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-096 sha:0e48669e src:dodatky/a-pinouty.md:97 klas:A -->
### T-A-096 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> **Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості без проходу через матрицю.

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/<ціль>/include/soc/{uart_pins,spi_pins}.h
- **Дослівно з джерела:**
  > esp32/uart_pins.h    U0RXD_GPIO_NUM 3    U0TXD_GPIO_NUM 1
  > esp32s3/uart_pins.h  U0RXD_GPIO_NUM 44   U0TXD_GPIO_NUM 43
  > esp32c3/uart_pins.h  U0RXD_GPIO_NUM 20   U0TXD_GPIO_NUM 21
  > esp32/spi_pins.h     SPI2 (HSPI) MOSI 13 MISO 12 CLK 14 CS 15;  SPI3 (VSPI) MOSI 23 MISO 19 CLK 18 CS 5
  > esp32s3/spi_pins.h   SPI2 MOSI 11 MISO 13 CLK 12 CS 10
  > esp32c3/spi_pins.h   SPI2 MOSI 7  MISO 2  CLK 6  CS 10
- **Спосіб і дата:** curl raw.githubusercontent для трьох цілей, 2026-08-26
- **Нотатка:** Покриває таблицю апаратних пінів у додатку A. Помилку в пінах SPI для C3 (було 6/2/4/7) виправлено за цим джерелом ще на етапі написання; тут зафіксовано доказ.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-A-097 sha:a10d9d2f src:dodatky/a-pinouty.md:98 klas:A -->
### T-A-097 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Значення нижче звірені з ESP-IDF (`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/<ціль>/include/soc/{uart_pins,spi_pins}.h
- **Дослівно з джерела:**
  > esp32/uart_pins.h    U0RXD_GPIO_NUM 3    U0TXD_GPIO_NUM 1
  > esp32s3/uart_pins.h  U0RXD_GPIO_NUM 44   U0TXD_GPIO_NUM 43
  > esp32c3/uart_pins.h  U0RXD_GPIO_NUM 20   U0TXD_GPIO_NUM 21
  > esp32/spi_pins.h     SPI2 (HSPI) MOSI 13 MISO 12 CLK 14 CS 15;  SPI3 (VSPI) MOSI 23 MISO 19 CLK 18 CS 5
  > esp32s3/spi_pins.h   SPI2 MOSI 11 MISO 13 CLK 12 CS 10
  > esp32c3/spi_pins.h   SPI2 MOSI 7  MISO 2  CLK 6  CS 10
- **Спосіб і дата:** curl raw.githubusercontent для трьох цілей, 2026-08-26
- **Нотатка:** Покриває таблицю апаратних пінів у додатку A. Помилку в пінах SPI для C3 (було 6/2/4/7) виправлено за цим джерелом ще на етапі написання; тут зафіксовано доказ.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-A-098 sha:0e12c8c4 src:dodatky/a-pinouty.md:101 klas:F -->
### T-A-098 · tablycya-shapka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> | Функція | [[classic]] | [[S3]] | [[C3]] |

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-099 sha:090b0b6b src:dodatky/a-pinouty.md:102 klas:A -->
### T-A-099 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> UART0 TX / RX · [[classic]] → 1 / 3

**Дослівно з книги**

```
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
```

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/uart_pins.h
- **Дослівно з джерела:**
  > #define U0TXD_GPIO_NUM  (1)
  > #define U0RXD_GPIO_NUM  (3)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** UART0 TX/RX на GPIO 1/3 для ESP32 classic
- **Прохід:** prochid-a-pinouty

---

<!-- fc id:T-A-100 sha:56d23897 src:dodatky/a-pinouty.md:102 klas:F -->
### T-A-100 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> UART0 TX / RX · [[S3]] → 43 / 44

**Дослівно з книги**

```
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
```

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-101 sha:ab72153b src:dodatky/a-pinouty.md:102 klas:F -->
### T-A-101 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> UART0 TX / RX · [[C3]] → 21 / 20

**Дослівно з книги**

```
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
```

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-102 sha:4700ea2d src:dodatky/a-pinouty.md:103 klas:A -->
### T-A-102 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> SPI2 MOSI / MISO / CLK / CS · [[classic]] → 13/12/14/15

**Дослівно з книги**

```
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
```

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/{uart_pins.h,spi_pins.h}
- **Дослівно з джерела:**
  > esp32:   U0TXD 1, U0RXD 3
  >          HSPI(=SPI2) MOSI 13 MISO 12 CLK 14 CS 15
  >          VSPI(=SPI3) MOSI 23 MISO 19 CLK 18 CS 5
  >          MSPI (флеш) CLK 6 MISO 7 MOSI 8 HD 9 WP 10 CS0 11
  > esp32s3: U0TXD 43, U0RXD 44
  >          SPI2 MOSI 11 MISO 13 CLK 12 CS 10
  >          MSPI CS1 26 HD 27 WP 28 CS0 29 CLK 30 MISO 31 MOSI 32
  >               D4 33 D5 34 D6 35 D7 36 DQS 37
  > esp32c3: U0TXD 21, U0RXD 20
  >          SPI2 MOSI 7 MISO 2 CLK 6 CS 10
  >          MSPI HD 12 WP 13 CS0 14 CLK 15 MOSI 16 MISO 17
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Усі дванадцять чисел таблиці IOMUX збігаються, і ототожнення `SPI2 = HSPI`, `SPI3 = VSPI` теж стоїть у заголовку дослівно (`#define SPI2_FUNC_NUM HSPI_FUNC_NUM`).
Заразом підтверджено діапазони пінів флешу, які книга забороняє чіпати: classic 6–11, C3 12–17, S3 26–32 плюс 33–37 на модулях з Octal PSRAM. Останнє видно прямо: `MSPI_IOMUX_PIN_NUM_D4…DQS` — це саме 33…37.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-103 sha:390631d1 src:dodatky/a-pinouty.md:103 klas:A -->
### T-A-103 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> SPI2 MOSI / MISO / CLK / CS · [[S3]] → 11/13/12/10

**Дослівно з книги**

```
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
```

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/{uart_pins.h,spi_pins.h}
- **Дослівно з джерела:**
  > esp32:   U0TXD 1, U0RXD 3
  >          HSPI(=SPI2) MOSI 13 MISO 12 CLK 14 CS 15
  >          VSPI(=SPI3) MOSI 23 MISO 19 CLK 18 CS 5
  >          MSPI (флеш) CLK 6 MISO 7 MOSI 8 HD 9 WP 10 CS0 11
  > esp32s3: U0TXD 43, U0RXD 44
  >          SPI2 MOSI 11 MISO 13 CLK 12 CS 10
  >          MSPI CS1 26 HD 27 WP 28 CS0 29 CLK 30 MISO 31 MOSI 32
  >               D4 33 D5 34 D6 35 D7 36 DQS 37
  > esp32c3: U0TXD 21, U0RXD 20
  >          SPI2 MOSI 7 MISO 2 CLK 6 CS 10
  >          MSPI HD 12 WP 13 CS0 14 CLK 15 MOSI 16 MISO 17
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Усі дванадцять чисел таблиці IOMUX збігаються, і ототожнення `SPI2 = HSPI`, `SPI3 = VSPI` теж стоїть у заголовку дослівно (`#define SPI2_FUNC_NUM HSPI_FUNC_NUM`).
Заразом підтверджено діапазони пінів флешу, які книга забороняє чіпати: classic 6–11, C3 12–17, S3 26–32 плюс 33–37 на модулях з Octal PSRAM. Останнє видно прямо: `MSPI_IOMUX_PIN_NUM_D4…DQS` — це саме 33…37.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-104 sha:f41f46f7 src:dodatky/a-pinouty.md:103 klas:A -->
### T-A-104 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> SPI2 MOSI / MISO / CLK / CS · [[C3]] → 7/2/6/10

**Дослівно з книги**

```
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
```

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/{uart_pins.h,spi_pins.h}
- **Дослівно з джерела:**
  > esp32:   U0TXD 1, U0RXD 3
  >          HSPI(=SPI2) MOSI 13 MISO 12 CLK 14 CS 15
  >          VSPI(=SPI3) MOSI 23 MISO 19 CLK 18 CS 5
  >          MSPI (флеш) CLK 6 MISO 7 MOSI 8 HD 9 WP 10 CS0 11
  > esp32s3: U0TXD 43, U0RXD 44
  >          SPI2 MOSI 11 MISO 13 CLK 12 CS 10
  >          MSPI CS1 26 HD 27 WP 28 CS0 29 CLK 30 MISO 31 MOSI 32
  >               D4 33 D5 34 D6 35 D7 36 DQS 37
  > esp32c3: U0TXD 21, U0RXD 20
  >          SPI2 MOSI 7 MISO 2 CLK 6 CS 10
  >          MSPI HD 12 WP 13 CS0 14 CLK 15 MOSI 16 MISO 17
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Усі дванадцять чисел таблиці IOMUX збігаються, і ототожнення `SPI2 = HSPI`, `SPI3 = VSPI` теж стоїть у заголовку дослівно (`#define SPI2_FUNC_NUM HSPI_FUNC_NUM`).
Заразом підтверджено діапазони пінів флешу, які книга забороняє чіпати: classic 6–11, C3 12–17, S3 26–32 плюс 33–37 на модулях з Octal PSRAM. Останнє видно прямо: `MSPI_IOMUX_PIN_NUM_D4…DQS` — це саме 33…37.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-105 sha:b5c533a3 src:dodatky/a-pinouty.md:104 klas:A -->
### T-A-105 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> SPI3 MOSI / MISO / CLK / CS · [[classic]] → 23/19/18/5

**Дослівно з книги**

```
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Контекст**

```
## Піни за замовчуванням

**Апаратні піни (IOMUX)** — ті, на яких блок працює на повній швидкості
без проходу через матрицю. Значення нижче звірені з ESP-IDF
(`soc/<чип>/include/soc/uart_pins.h` і `spi_pins.h`).

| Функція | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| UART0 TX / RX | 1 / 3 | 43 / 44 | 21 / 20 |
| SPI2 MOSI / MISO / CLK / CS | 13/12/14/15 | 11/13/12/10 | 7/2/6/10 |
| SPI3 MOSI / MISO / CLK / CS | 23/19/18/5 | — | — |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/{uart_pins.h,spi_pins.h}
- **Дослівно з джерела:**
  > esp32:   U0TXD 1, U0RXD 3
  >          HSPI(=SPI2) MOSI 13 MISO 12 CLK 14 CS 15
  >          VSPI(=SPI3) MOSI 23 MISO 19 CLK 18 CS 5
  >          MSPI (флеш) CLK 6 MISO 7 MOSI 8 HD 9 WP 10 CS0 11
  > esp32s3: U0TXD 43, U0RXD 44
  >          SPI2 MOSI 11 MISO 13 CLK 12 CS 10
  >          MSPI CS1 26 HD 27 WP 28 CS0 29 CLK 30 MISO 31 MOSI 32
  >               D4 33 D5 34 D6 35 D7 36 DQS 37
  > esp32c3: U0TXD 21, U0RXD 20
  >          SPI2 MOSI 7 MISO 2 CLK 6 CS 10
  >          MSPI HD 12 WP 13 CS0 14 CLK 15 MOSI 16 MISO 17
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Усі дванадцять чисел таблиці IOMUX збігаються, і ототожнення `SPI2 = HSPI`, `SPI3 = VSPI` теж стоїть у заголовку дослівно (`#define SPI2_FUNC_NUM HSPI_FUNC_NUM`).
Заразом підтверджено діапазони пінів флешу, які книга забороняє чіпати: classic 6–11, C3 12–17, S3 26–32 плюс 33–37 на модулях з Octal PSRAM. Останнє видно прямо: `MSPI_IOMUX_PIN_NUM_D4…DQS` — це саме 33…37.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-106 sha:071a0c5f src:dodatky/a-pinouty.md:107 klas:A -->
### T-A-106 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> [[classic]] SPI2 і SPI3 у classic історично звуться **HSPI** і **VSPI**; у прикладах і бібліотеках частіше трапляється саме VSPI (23/19/18/5).

**Контекст**

```
## Піни за замовчуванням

[[classic]] SPI2 і SPI3 у classic історично звуться **HSPI** і **VSPI**;
у прикладах і бібліотеках частіше трапляється саме VSPI (23/19/18/5).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/{uart_pins.h,spi_pins.h}
- **Дослівно з джерела:**
  > esp32:   U0TXD 1, U0RXD 3
  >          HSPI(=SPI2) MOSI 13 MISO 12 CLK 14 CS 15
  >          VSPI(=SPI3) MOSI 23 MISO 19 CLK 18 CS 5
  >          MSPI (флеш) CLK 6 MISO 7 MOSI 8 HD 9 WP 10 CS0 11
  > esp32s3: U0TXD 43, U0RXD 44
  >          SPI2 MOSI 11 MISO 13 CLK 12 CS 10
  >          MSPI CS1 26 HD 27 WP 28 CS0 29 CLK 30 MISO 31 MOSI 32
  >               D4 33 D5 34 D6 35 D7 36 DQS 37
  > esp32c3: U0TXD 21, U0RXD 20
  >          SPI2 MOSI 7 MISO 2 CLK 6 CS 10
  >          MSPI HD 12 WP 13 CS0 14 CLK 15 MOSI 16 MISO 17
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Усі дванадцять чисел таблиці IOMUX збігаються, і ототожнення `SPI2 = HSPI`, `SPI3 = VSPI` теж стоїть у заголовку дослівно (`#define SPI2_FUNC_NUM HSPI_FUNC_NUM`).
Заразом підтверджено діапазони пінів флешу, які книга забороняє чіпати: classic 6–11, C3 12–17, S3 26–32 плюс 33–37 на модулях з Octal PSRAM. Останнє видно прямо: `MSPI_IOMUX_PIN_NUM_D4…DQS` — це саме 33…37.
- **Прохід:** pass-12-piny

---

<!-- fc id:T-A-107 sha:2dfd20e4 src:dodatky/a-pinouty.md:110 klas:F -->
### T-A-107 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> **Домовленість, а не апаратна прив'язка.** Для I²C апаратних піни за замовчуванням у ESP-IDF **немає взагалі** — їх задають у проєкті.

**Контекст**

```
## Піни за замовчуванням

**Домовленість, а не апаратна прив'язка.** Для I²C апаратних піни за
замовчуванням у ESP-IDF **немає взагалі** — їх задають у проєкті. Числа
нижче — те, що прийнято в прикладах і в Arduino, не більше:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-108 sha:4b8831ab src:dodatky/a-pinouty.md:111 klas:F -->
### T-A-108 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Числа нижче — те, що прийнято в прикладах і в Arduino, не більше:

**Контекст**

```
## Піни за замовчуванням

**Домовленість, а не апаратна прив'язка.** Для I²C апаратних піни за
замовчуванням у ESP-IDF **немає взагалі** — їх задають у проєкті. Числа
нижче — те, що прийнято в прикладах і в Arduino, не більше:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-109 sha:7d05e143 src:dodatky/a-pinouty.md:114 klas:F -->
### T-A-109 · tablycya-shapka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> | | [[classic]] | [[S3]] | [[C3]] |

**Контекст**

```
## Піни за замовчуванням

**Домовленість, а не апаратна прив'язка.** Для I²C апаратних піни за
замовчуванням у ESP-IDF **немає взагалі** — їх задають у проєкті. Числа
нижче — те, що прийнято в прикладах і в Arduino, не більше:

| | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| I²C SDA / SCL | 21 / 22 | 8 / 9 | 8 / 9 |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-110 sha:fce9954a src:dodatky/a-pinouty.md:115 klas:F -->
### T-A-110 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> I²C SDA / SCL · [[classic]] → 21 / 22

**Дослівно з книги**

```
| I²C SDA / SCL | 21 / 22 | 8 / 9 | 8 / 9 |
```

**Контекст**

```
## Піни за замовчуванням

**Домовленість, а не апаратна прив'язка.** Для I²C апаратних піни за
замовчуванням у ESP-IDF **немає взагалі** — їх задають у проєкті. Числа
нижче — те, що прийнято в прикладах і в Arduino, не більше:

| | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| I²C SDA / SCL | 21 / 22 | 8 / 9 | 8 / 9 |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-111 sha:c3291e0e src:dodatky/a-pinouty.md:115 klas:F -->
### T-A-111 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> I²C SDA / SCL · [[S3]] → 8 / 9

**Дослівно з книги**

```
| I²C SDA / SCL | 21 / 22 | 8 / 9 | 8 / 9 |
```

**Контекст**

```
## Піни за замовчуванням

**Домовленість, а не апаратна прив'язка.** Для I²C апаратних піни за
замовчуванням у ESP-IDF **немає взагалі** — їх задають у проєкті. Числа
нижче — те, що прийнято в прикладах і в Arduino, не більше:

| | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| I²C SDA / SCL | 21 / 22 | 8 / 9 | 8 / 9 |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-112 sha:d575518e src:dodatky/a-pinouty.md:115 klas:F -->
### T-A-112 · komirka · `dodatky/a-pinouty.md`

**Твердження, коротко**

> I²C SDA / SCL · [[C3]] → 8 / 9

**Дослівно з книги**

```
| I²C SDA / SCL | 21 / 22 | 8 / 9 | 8 / 9 |
```

**Контекст**

```
## Піни за замовчуванням

**Домовленість, а не апаратна прив'язка.** Для I²C апаратних піни за
замовчуванням у ESP-IDF **немає взагалі** — їх задають у проєкті. Числа
нижче — те, що прийнято в прикладах і в Arduino, не більше:

| | [[classic]] | [[S3]] | [[C3]] |
|---|---|---|---|
| I²C SDA / SCL | 21 / 22 | 8 / 9 | 8 / 9 |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-113 sha:02f2aa4a src:dodatky/a-pinouty.md:119 klas:A -->
### T-A-113 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> [[C3]] Зверніть увагу на C3: типові для Arduino `SDA` = `GPIO8` і `SCL` = `GPIO9` — це **обидва strapping-піни** (таблиця вище).

**Контекст**

```
## Піни за замовчуванням

::: uvaha
[[C3]] Зверніть увагу на C3: типові для Arduino `SDA` = `GPIO8` і
`SCL` = `GPIO9` — це **обидва strapping-піни** (таблиця вище).
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

<!-- fc id:T-A-114 sha:6fd3a16a src:dodatky/a-pinouty.md:122 klas:E -->
### T-A-114 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Практично це означає дві речі.

**Контекст**

```
## Піни за замовчуванням

Практично це означає дві речі. Перше: зовнішні підтягувальні резистори
I²C тягнуть обидві лінії вгору, а `GPIO8` при старті **має** бути
високим, і `GPIO9` високий означає звичайний старт, — тобто типова
обв'язка I²C не заважає завантаженню, а навпаки збігається з потрібними
рівнями. Друге, і гірше: ведений, що притискає `SDA` до землі в момент
скидання, дає `GPIO8` = 0 — недійсну комбінацію.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-115 sha:409b4ced src:dodatky/a-pinouty.md:122 klas:A -->
### T-A-115 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Перше: зовнішні підтягувальні резистори I²C тягнуть обидві лінії вгору, а `GPIO8` при старті **має** бути високим, і `GPIO9` високий означає звичайний старт, — тобто типова обв'язка I²C не заважає завантаженню, а навпаки збігається з потрібними рівнями.

**Контекст**

```
## Піни за замовчуванням

Практично це означає дві речі. Перше: зовнішні підтягувальні резистори
I²C тягнуть обидві лінії вгору, а `GPIO8` при старті **має** бути
високим, і `GPIO9` високий означає звичайний старт, — тобто типова
обв'язка I²C не заважає завантаженню, а навпаки збігається з потрібними
рівнями. Друге, і гірше: ведений, що притискає `SDA` до землі в момент
скидання, дає `GPIO8` = 0 — недійсну комбінацію.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../esp-idf/components/soc/esp32c3/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > {STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  > serial bootloader reliably. The strapping combination of
  > {STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and will
  > trigger unexpected behavior.
  > (для esp32c3: STRAP_BOOT_2_GPIO = GPIO8, STRAP_BOOT_GPIO = GPIO9)
  > 
  > (esp32c3/adc_channel.h)
  > ADC1_GPIO0_CHANNEL 0   ADC1_GPIO1_CHANNEL 1   ADC1_GPIO2_CHANNEL 2
  > ADC1_GPIO3_CHANNEL 3   ADC1_GPIO4_CHANNEL 4
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Додаток A робить із двох звірених фактів висновок, і висновок правильний у неочевидний бік: типова обв'язка I²C на C3 завантаженню **не заважає**. Підтяжки тягнуть обидві лінії вгору, а потрібно саме `GPIO8` високий; `GPIO9` високий означає звичайний старт.
Друга половина — застереження, і воно точне: ведений, що притискає `SDA` до землі в момент скидання, дає `GPIO8` = 0. Разом із `GPIO9` = 0 (натиснута кнопка `BOOT`) це та сама недійсна комбінація.
«На C3 аналоговий вхід — це `GPIO0`–`GPIO4`, і більше нічого» — п'ять каналів `adc_channel.h`, рівно цей діапазон.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-A-116 sha:8325baa5 src:dodatky/a-pinouty.md:126 klas:A -->
### T-A-116 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Друге, і гірше: ведений, що притискає `SDA` до землі в момент скидання, дає `GPIO8` = 0 — недійсну комбінацію.

**Контекст**

```
## Піни за замовчуванням

Практично це означає дві речі. Перше: зовнішні підтягувальні резистори
I²C тягнуть обидві лінії вгору, а `GPIO8` при старті **має** бути
високим, і `GPIO9` високий означає звичайний старт, — тобто типова
обв'язка I²C не заважає завантаженню, а навпаки збігається з потрібними
рівнями. Друге, і гірше: ведений, що притискає `SDA` до землі в момент
скидання, дає `GPIO8` = 0 — недійсну комбінацію.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../esp-idf/components/soc/esp32c3/include/soc/adc_channel.h
- **Дослівно з джерела:**
  > {STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the
  > serial bootloader reliably. The strapping combination of
  > {STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and will
  > trigger unexpected behavior.
  > (для esp32c3: STRAP_BOOT_2_GPIO = GPIO8, STRAP_BOOT_GPIO = GPIO9)
  > 
  > (esp32c3/adc_channel.h)
  > ADC1_GPIO0_CHANNEL 0   ADC1_GPIO1_CHANNEL 1   ADC1_GPIO2_CHANNEL 2
  > ADC1_GPIO3_CHANNEL 3   ADC1_GPIO4_CHANNEL 4
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Додаток A робить із двох звірених фактів висновок, і висновок правильний у неочевидний бік: типова обв'язка I²C на C3 завантаженню **не заважає**. Підтяжки тягнуть обидві лінії вгору, а потрібно саме `GPIO8` високий; `GPIO9` високий означає звичайний старт.
Друга половина — застереження, і воно точне: ведений, що притискає `SDA` до землі в момент скидання, дає `GPIO8` = 0. Разом із `GPIO9` = 0 (натиснута кнопка `BOOT`) це та сама недійсна комбінація.
«На C3 аналоговий вхід — це `GPIO0`–`GPIO4`, і більше нічого» — п'ять каналів `adc_channel.h`, рівно цей діапазон.
- **Прохід:** pass-30-piny-suciljno

---

<!-- fc id:T-A-117 sha:2d8ff849 src:dodatky/a-pinouty.md:129 klas:E -->
### T-A-117 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Симптом — плата, яка стартує через раз і лише коли датчик від'єднаний.

**Контекст**

```
## Піни за замовчуванням

Симптом — плата, яка стартує через раз і лише коли датчик від'єднаний.
Якщо пінів вистачає, I²C на C3 варто перенести на будь-яку іншу пару
(розділ 04): матриця GPIO це дозволяє, а швидкість I²C від маршруту
через матрицю не страждає.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-118 sha:df609ca6 src:dodatky/a-pinouty.md:130 klas:D -->
### T-A-118 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Якщо пінів вистачає, I²C на C3 варто перенести на будь-яку іншу пару (розділ 04): матриця GPIO це дозволяє, а швидкість I²C від маршруту через матрицю не страждає.

**Контекст**

```
## Піни за замовчуванням

Симптом — плата, яка стартує через раз і лише коли датчик від'єднаний.
Якщо пінів вистачає, I²C на C3 варто перенести на будь-яку іншу пару
(розділ 04): матриця GPIO це дозволяє, а швидкість I²C від маршруту
через матрицю не страждає.
:::
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/cross_refs.py — перевірка проти дерева файлів репозиторію
- **Розрахунок:**
  posylannya: згадок 689, адресатів 79, помилок 0
  
  Перевірено:
    «розділ NN»  → існує manual/NN-*.md, і це не той самий розділ
    «картка КN»  → існує kartky/kNN-*.md
    «додаток X»  → існує dodatky/x-*.md (з переведенням кириличної
                   букви в латинську назву файлу)
- **Спосіб і дата:** python3 tools/cross_refs.py, 2026-08-26
- **Нотатка:** Нуль помилок із 689 згадок. Це другий вимір після арифметики й API, де прохід не дав жодного виправлення.
Клас `D`, а не `A`: зовнішнє джерело тут не потрібне й не буває — перевіряється твердження книги про саму себе, і перевіряється механічно.
Головне тут не результат, а те, що перевірка тепер постійна: `tools/cross_refs.py` стоїть у `make check`. Досі номер розділу можна було зсунути, і жоден інструмент цього б не помітив — текст лишається зв'язним, а читач іде не туди.
Одне самопосилання цей інструмент уже спіймав раніше, у проході 9 (розділ 17 відсилав сам на себе); тоді його знайшов `review.py` на клікабельному посиланні. Тепер такий самий контроль поширено на прозу.
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-A-119 sha:a5597ef2 src:dodatky/a-pinouty.md:136 klas:F -->
### T-A-119 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Завдяки матриці GPIO будь-який із цих сигналів переноситься на інший пін (розділ 04).

**Контекст**

```
## Піни за замовчуванням

::: uvaha
Завдяки матриці GPIO будь-який із цих сигналів переноситься на інший пін
(розділ 04). Ціна перенесення SPI з апаратного піна — нижча гранична
частота: маршрут через матрицю додає затримку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-120 sha:1b60f222 src:dodatky/a-pinouty.md:137 klas:D -->
### T-A-120 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Ціна перенесення SPI з апаратного піна — нижча гранична частота: маршрут через матрицю додає затримку.

**Контекст**

```
## Піни за замовчуванням

::: uvaha
Завдяки матриці GPIO будь-який із цих сигналів переноситься на інший пін
(розділ 04). Ціна перенесення SPI з апаратного піна — нижча гранична
частота: маршрут через матрицю додає затримку.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/cross_refs.py — перевірка проти дерева файлів репозиторію
- **Розрахунок:**
  posylannya: згадок 689, адресатів 79, помилок 0
  
  Перевірено:
    «розділ NN»  → існує manual/NN-*.md, і це не той самий розділ
    «картка КN»  → існує kartky/kNN-*.md
    «додаток X»  → існує dodatky/x-*.md (з переведенням кириличної
                   букви в латинську назву файлу)
- **Спосіб і дата:** python3 tools/cross_refs.py, 2026-08-26
- **Нотатка:** Нуль помилок із 689 згадок. Це другий вимір після арифметики й API, де прохід не дав жодного виправлення.
Клас `D`, а не `A`: зовнішнє джерело тут не потрібне й не буває — перевіряється твердження книги про саму себе, і перевіряється механічно.
Головне тут не результат, а те, що перевірка тепер постійна: `tools/cross_refs.py` стоїть у `make check`. Досі номер розділу можна було зсунути, і жоден інструмент цього б не помітив — текст лишається зв'язним, а читач іде не туди.
Одне самопосилання цей інструмент уже спіймав раніше, у проході 9 (розділ 17 відсилав сам на себе); тоді його знайшов `review.py` на клікабельному посиланні. Тепер такий самий контроль поширено на прозу.
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-A-121 sha:6d13423d src:dodatky/a-pinouty.md:140 klas:F -->
### T-A-121 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Для I²C і UART це не має значення; для SPI на десятках мегагерц — має.

**Контекст**

```
## Піни за замовчуванням

Для I²C і UART це не має значення; для SPI на десятках мегагерц —
має.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-A-122 sha:e4453418 src:dodatky/a-pinouty.md:146 klas:A -->
### T-A-122 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> [[classic]] 38-пінова плата: з ~34 GPIO відкидаємо 6 пінів флешу, 2 піни консолі й 6 тільки-вхідних → близько **20 повноцінних**, із яких 5 — strapping.

**Контекст**

```
## Скільки пінів насправді

[[classic]] 38-пінова плата: з ~34 GPIO відкидаємо 6 пінів флешу,
2 піни консолі й 6 тільки-вхідних → близько **20 повноцінних**, із яких
5 — strapping.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP32 Series Datasheet v5.3, GPIO Overview та Pin Definitions
- **Дослівно з джерела:**
  > - 6 flash pins (GPIO6-11)
  > - 2 UART pins (GPIO1, GPIO3)
  > - 6 input-only pins
  > - 5 strapping pins (GPIO0, 2, 4, 5, 15)
- **Нотатка:** Перелік обмежень для classic ESP32. Кожне число має джерело у datasheet.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-A-123 sha:3846a274 src:dodatky/a-pinouty.md:150 klas:A -->
### T-A-123 · proza · `dodatky/a-pinouty.md`

**Твердження, коротко**

> Коли не вистачає: розширювач по I²C (PCF8574, MCP23017), зсувний регістр (74HC595/165), аналоговий мультиплексор (CD4051), чип із більшою кількістю пінів, або другий мікроконтролер (розділ 07).

**Контекст**

```
## Скільки пінів насправді

Коли не вистачає: розширювач по I²C (PCF8574, MCP23017), зсувний
регістр (74HC595/165), аналоговий мультиплексор (CD4051), чип із більшою
кількістю пінів, або другий мікроконтролер (розділ 07).
```

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
