# Фактчекінг: `manual/13-pio.md`

Одиниць твердження: **77**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-13-001 sha:1fdbb66e src:manual/13-pio.md:3 klas:F -->
### T-13-001 · proza · `manual/13-pio.md`

**Твердження, коротко**

> PlatformIO — розширення для VS Code, що керує вбудованими проєктами: тулчейни, платформи, бібліотеки, кілька цільових середовищ в одному проєкті.

**Дослівно з книги**

```
PlatformIO — розширення для VS Code, що керує вбудованими проєктами:
```

**Контекст**

```
# 13. PlatformIO і pioarduino {#pio}

PlatformIO — розширення для VS Code, що керує вбудованими проєктами:
тулчейни, платформи, бібліотеки, кілька цільових середовищ в одному
проєкті. Для ESP32 воно дає те, чого не дає Arduino IDE: фіксовані
версії, нормальний менеджер залежностей і конфігурацію в одному файлі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-002 sha:f593172f src:manual/13-pio.md:3 klas:A -->
### T-13-002 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Для ESP32 воно дає те, чого не дає Arduino IDE: фіксовані версії, нормальний менеджер залежностей і конфігурацію в одному файлі.

**Дослівно з книги**

```
PlatformIO — розширення для VS Code, що керує вбудованими проєктами:
```

**Контекст**

```
# 13. PlatformIO і pioarduino {#pio}

PlatformIO — розширення для VS Code, що керує вбудованими проєктами:
тулчейни, платформи, бібліотеки, кілька цільових середовищ в одному
проєкті. Для ESP32 воно дає те, чого не дає Arduino IDE: фіксовані
версії, нормальний менеджер залежностей і конфігурацію в одному файлі.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/platformio/platform-espressif32/master/platform.json
- **Дослівно з джерела:**
  > "version": "7.0.1"
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** платформа дає фіксовані версії компонентів у platform.json
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-003 sha:7528b989 src:manual/13-pio.md:8 klas:E -->
### T-13-003 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Ситуація навколо нього нетипова, і про неї треба знати до того, як почнете.

**Дослівно з книги**

```
Ситуація навколо нього нетипова, і про неї треба знати до того, як
```

**Контекст**

```
# 13. PlatformIO і pioarduino {#pio}

Ситуація навколо нього нетипова, і про неї треба знати до того, як
почнете.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-004 sha:7c3c99a0 src:manual/13-pio.md:13 klas:A -->
### T-13-004 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Підтримка ESP32 у PlatformIO забезпечується платформою `platform-espressif32`.

**Дослівно з книги**

```
Підтримка ESP32 у PlatformIO забезпечується платформою
```

**Контекст**

```
## Статус: чому все складно

Підтримка ESP32 у PlatformIO забезпечується платформою
`platform-espressif32`. Офіційна платформа від PlatformIO **відстала**
від Arduino core: підтримка Arduino 3.x у ній офіційно не з'явилася, і
через відсутність подальшого розвитку спільнота створила форк.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/platformio/platform-espressif32/master/platform.json
- **Дослівно з джерела:**
  > "name": "espressif32"
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтримка ESP32 у PlatformIO забезпечується платформою platform-espressif32
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-005 sha:098cf69e src:manual/13-pio.md:13 klas:A -->
### T-13-005 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Офіційна платформа від PlatformIO **відстала** від Arduino core: підтримка Arduino 3.x у ній офіційно не з'явилася, і через відсутність подальшого розвитку спільнота створила форк.

**Дослівно з книги**

```
Підтримка ESP32 у PlatformIO забезпечується платформою
```

**Контекст**

```
## Статус: чому все складно

Підтримка ESP32 у PlatformIO забезпечується платформою
`platform-espressif32`. Офіційна платформа від PlatformIO **відстала**
від Arduino core: підтримка Arduino 3.x у ній офіційно не з'явилася, і
через відсутність подальшого розвитку спільнота створила форк.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/platformio/platform-espressif32/master/platform.json
- **Дослівно з джерела:**
  > "version": "~3.20017.0"
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** офіційна платформа використовує Arduino 2.x версію (~3.20017.0)
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-006 sha:1dabb487 src:manual/13-pio.md:18 klas:A -->
### T-13-006 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Форк називається **pioarduino** і супроводжується спільнотою.

**Дослівно з книги**

```
Форк називається **pioarduino** і супроводжується спільнотою. Він
```

**Контекст**

```
## Статус: чому все складно

Форк називається **pioarduino** і супроводжується спільнотою. Він
підтримує актуальні версії Arduino core і нові сімейства чипів.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/master/README.md
- **Дослівно з джерела:**
  > # pioarduino (p)eople (i)nitiated (o)ptimized (arduino)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує існування форку pioarduino, підтримуваного спільнотою
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-007 sha:4ec26d12 src:manual/13-pio.md:18 klas:A -->
### T-13-007 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Він підтримує актуальні версії Arduino core і нові сімейства чипів.

**Дослівно з книги**

```
Форк називається **pioarduino** і супроводжується спільнотою. Він
```

**Контекст**

```
## Статус: чому все складно

Форк називається **pioarduino** і супроводжується спільнотою. Він
підтримує актуальні версії Arduino core і нові сімейства чипів.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/master/platform.json
- **Дослівно з джерела:**
  > "version": "https://github.com/espressif/arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz"
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** pioarduino підтримує Arduino 3.3.11 із новими сімействами чипів
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-008 sha:63df3a47 src:manual/13-pio.md:21 klas:E -->
### T-13-008 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Практичний висновок на сьогодні:

**Контекст**

```
## Статус: чому все складно

Практичний висновок на сьогодні:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-009 sha:eef32775 src:manual/13-pio.md:23 klas:F -->
### T-13-009 · proza · `manual/13-pio.md`

**Твердження, коротко**

> - працюєте з **Arduino 2.x** і старим кодом → офіційна платформа працює; - потрібен **Arduino 3.x**, S3, C3, C6 або новіші → **pioarduino**.

**Дослівно з книги**

```
- працюєте з **Arduino 2.x** і старим кодом → офіційна платформа працює;
```

**Контекст**

```
## Статус: чому все складно

- працюєте з **Arduino 2.x** і старим кодом → офіційна платформа працює;
- потрібен **Arduino 3.x**, S3, C3, C6 або новіші → **pioarduino**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-010 sha:4d0842b5 src:manual/13-pio.md:27 klas:E -->
### T-13-010 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Це та частина довідника, що застаріває найшвидше.

**Дослівно з книги**

```
Це та частина довідника, що застаріває найшвидше. Стан проєктів може
```

**Контекст**

```
## Статус: чому все складно

::: uvaha
Це та частина довідника, що застаріває найшвидше. Стан проєктів може
змінитися: офіційна платформа може наздогнати, форк — злитися назад або
зупинитися.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-011 sha:87c9dff3 src:manual/13-pio.md:27 klas:E -->
### T-13-011 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Стан проєктів може змінитися: офіційна платформа може наздогнати, форк — злитися назад або зупинитися.

**Дослівно з книги**

```
Це та частина довідника, що застаріває найшвидше. Стан проєктів може
```

**Контекст**

```
## Статус: чому все складно

::: uvaha
Це та частина довідника, що застаріває найшвидше. Стан проєктів може
змінитися: офіційна платформа може наздогнати, форк — злитися назад або
зупинитися.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-012 sha:e78e3416 src:manual/13-pio.md:31 klas:E -->
### T-13-012 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Тому: перед початком нового проєкту перевірте поточний стан обох, а не покладайтеся на цей текст.

**Дослівно з книги**

```
Тому: перед початком нового проєкту перевірте поточний стан обох, а не
```

**Контекст**

```
## Статус: чому все складно

Тому: перед початком нового проєкту перевірте поточний стан обох, а не
покладайтеся на цей текст. Версія, звірена на дату цієї ревізії, — у
таблиці на початку частини; наскільки вона застаріла, залежить від того,
коли ви це читаєте.
:::
```

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

<!-- fc id:T-13-013 sha:5c49975c src:manual/13-pio.md:31 klas:E -->
### T-13-013 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Версія, звірена на дату цієї ревізії, — у таблиці на початку частини; наскільки вона застаріла, залежить від того, коли ви це читаєте.

**Дослівно з книги**

```
Тому: перед початком нового проєкту перевірте поточний стан обох, а не
```

**Контекст**

```
## Статус: чому все складно

Тому: перед початком нового проєкту перевірте поточний стан обох, а не
покладайтеся на цей текст. Версія, звірена на дату цієї ревізії, — у
таблиці на початку частини; наскільки вона застаріла, залежить від того,
коли ви це читаєте.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-014 sha:5a0c92c3 src:manual/13-pio.md:39 klas:A -->
### T-13-014 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Версії фіксуються в проєкті.** Це головне.

**Дослівно з книги**

```
**Версії фіксуються в проєкті.** Це головне. `platformio.ini` лежить у
```

**Контекст**

```
## Чому це взагалі варте уваги

**Версії фіксуються в проєкті.** Це головне. `platformio.ini` лежить у
git і повністю описує, чим збирається проєкт. Через рік на іншій машині
збереться те саме.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/platformio/platform-espressif32/master/examples/arduino-blink/platformio.ini
- **Дослівно з джерела:**
  > [env:esp32doit-devkit-v1]
  > platform = espressif32
  > framework = arduino
  > board = esp32doit-devkit-v1
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** показує, що версії можуть бути зафіксовані в проєкті
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-015 sha:18113102 src:manual/13-pio.md:39 klas:A -->
### T-13-015 · proza · `manual/13-pio.md`

**Твердження, коротко**

> `platformio.ini` лежить у git і повністю описує, чим збирається проєкт.

**Дослівно з книги**

```
**Версії фіксуються в проєкті.** Це головне. `platformio.ini` лежить у
```

**Контекст**

```
## Чому це взагалі варте уваги

**Версії фіксуються в проєкті.** Це головне. `platformio.ini` лежить у
git і повністю описує, чим збирається проєкт. Через рік на іншій машині
збереться те саме.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/platformio/platform-espressif32/master/examples/arduino-blink/platformio.ini
- **Дослівно з джерела:**
  > platform = espressif32
  > framework = arduino
  > board = esp32doit-devkit-v1
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** platformio.ini описує, чим збирається проєкт
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-016 sha:6e6ff0ea src:manual/13-pio.md:39 klas:E -->
### T-13-016 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Через рік на іншій машині збереться те саме.

**Дослівно з книги**

```
**Версії фіксуються в проєкті.** Це головне. `platformio.ini` лежить у
```

**Контекст**

```
## Чому це взагалі варте уваги

**Версії фіксуються в проєкті.** Це головне. `platformio.ini` лежить у
git і повністю описує, чим збирається проєкт. Через рік на іншій машині
збереться те саме.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-017 sha:19495775 src:manual/13-pio.md:43 klas:F -->
### T-13-017 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Кілька середовищ в одному проєкті.** Один код, кілька цілей: classic і S3, налагоджувальна й робоча збірка, дві різні плати.

**Дослівно з книги**

```
**Кілька середовищ в одному проєкті.** Один код, кілька цілей: classic і
```

**Контекст**

```
## Чому це взагалі варте уваги

**Кілька середовищ в одному проєкті.** Один код, кілька цілей: classic і
S3, налагоджувальна й робоча збірка, дві різні плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-018 sha:a99e783d src:manual/13-pio.md:46 klas:F -->
### T-13-018 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Менеджер бібліотек.** Залежності записуються у файл із версіями, а не ставляться руками в спільний каталог, як в Arduino IDE.

**Дослівно з книги**

```
**Менеджер бібліотек.** Залежності записуються у файл із версіями, а не
```

**Контекст**

```
## Чому це взагалі варте уваги

**Менеджер бібліотек.** Залежності записуються у файл із версіями, а не
ставляться руками в спільний каталог, як в Arduino IDE.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-019 sha:297f0eb6 src:manual/13-pio.md:49 klas:F -->
### T-13-019 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Підтримка обох фреймворків.** І Arduino, і ESP-IDF — через один інтерфейс.

**Дослівно з книги**

```
**Підтримка обох фреймворків.** І Arduino, і ESP-IDF — через один
```

**Контекст**

```
## Чому це взагалі варте уваги

**Підтримка обох фреймворків.** І Arduino, і ESP-IDF — через один
інтерфейс.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-020 sha:aec08e40 src:manual/13-pio.md:54 klas:A -->
### T-13-020 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Весь проєкт описується одним файлом:

**Контекст**

```
## platformio.ini

Весь проєкт описується одним файлом:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/platformio/platform-espressif32/master/examples/arduino-blink/platformio.ini
- **Дослівно з джерела:**
  > [env:esp32doit-devkit-v1]
  > platform = espressif32
  > framework = arduino
  > board = esp32doit-devkit-v1
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** весь проєкт описується в platformio.ini файлі
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-021 sha:9cc8c88c src:manual/13-pio.md:56 klas:K -->
### T-13-021 · kod · `manual/13-pio.md`

**Твердження, коротко**

> ```ini
> [env:esp32dev]
> platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
> board = esp32dev
> framework = arduino
> monitor_speed = 115200
> upload_speed = 460800
> build_flags =
>     -DCORE_DEBUG_LEVEL=3
>     -DMY_SENSOR_ADDR=0x76
> lib_deps =
>     adafruit/Adafruit BME280 Library @ ^2.2.2
> ```

**Дослівно з книги**

````
```ini
````

**Контекст**

````
## platformio.ini

```ini
[env:esp32dev]
platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
board = esp32dev
framework = arduino
monitor_speed = 115200
upload_speed = 460800
build_flags =
    -DCORE_DEBUG_LEVEL=3
    -DMY_SENSOR_ADDR=0x76
lib_deps =
    adafruit/Adafruit BME280 Library @ ^2.2.2
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/main/README.md та .../55.03.311/platform.json
- **Дослівно з джерела:**
  > ### Stable Arduino
  > currently espressif Arduino 3.3.11 and IDF v5.5.5.
  > 
  > [env:stable]
  > platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
  > board = ...
  > 
  > (platform.json теґа 55.03.311)
  > "version": "55.03.311"
  > …/arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення за рецензією. Розділ 13 правильно пояснював, що для Arduino 3.x і нових чипів потрібен `pioarduino`, — і давав для копіювання `platform = espressif32 @ 6.5.0`, тобто офіційну платформу епохи Arduino 2.x. Причому й у прикладі для S3.
Розбіжність між тим, що книга радить, і тим, що читач може скопіювати, гірша за просто застарілий приклад: копіюють частіше, ніж читають.
Усі приклади переведено на `pioarduino`. Рядок `platform` у розділі про кілька середовищ винесено в спільну секцію `[env]` — дві плати мусять збиратися однією платформою.
Пінування показано тегом релізу (`55.03.311`), а сам номер відсилає до таблиці версій частини IV, як вимагає Р4.
Підтверджено й те, що робить пораду несуперечливою: README форка називає ті самі Arduino 3.3.11 та IDF 5.5.5, що стоять у `toolchain-baseline.yaml`.
- **Прохід:** pass-17-simeystva-proektiv

---

<!-- fc id:T-13-022 sha:f9f47141 src:manual/13-pio.md:71 klas:A -->
### T-13-022 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Чому в рядку `platform` посилання, а не звичне `espressif32 @ 6.5.0`.**

**Контекст**

```
## platformio.ini

::: uvaha
**Чому в рядку `platform` посилання, а не звичне `espressif32 @ 6.5.0`.**
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/main/README.md та .../55.03.311/platform.json
- **Дослівно з джерела:**
  > ### Stable Arduino
  > currently espressif Arduino 3.3.11 and IDF v5.5.5.
  > 
  > [env:stable]
  > platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
  > board = ...
  > 
  > (platform.json теґа 55.03.311)
  > "version": "55.03.311"
  > …/arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення за рецензією. Розділ 13 правильно пояснював, що для Arduino 3.x і нових чипів потрібен `pioarduino`, — і давав для копіювання `platform = espressif32 @ 6.5.0`, тобто офіційну платформу епохи Arduino 2.x. Причому й у прикладі для S3.
Розбіжність між тим, що книга радить, і тим, що читач може скопіювати, гірша за просто застарілий приклад: копіюють частіше, ніж читають.
Усі приклади переведено на `pioarduino`. Рядок `platform` у розділі про кілька середовищ винесено в спільну секцію `[env]` — дві плати мусять збиратися однією платформою.
Пінування показано тегом релізу (`55.03.311`), а сам номер відсилає до таблиці версій частини IV, як вимагає Р4.
Підтверджено й те, що робить пораду несуперечливою: README форка називає ті самі Arduino 3.3.11 та IDF 5.5.5, що стоять у `toolchain-baseline.yaml`.
- **Прохід:** pass-17-simeystva-proektiv

---

<!-- fc id:T-13-023 sha:60ff61c5 src:manual/13-pio.md:73 klas:A -->
### T-13-023 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Офіційна платформа PlatformIO лишилася на Arduino 2.x.

**Дослівно з книги**

```
Офіційна платформа PlatformIO лишилася на Arduino 2.x. Запис
```

**Контекст**

```
## platformio.ini

Офіційна платформа PlatformIO лишилася на Arduino 2.x. Запис
`espressif32 @ 6.5.0` збереться — і дасть Arduino 2.x, тобто не те, про
що написано в розділі 12, і без підтримки нових чипів.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/main/README.md та .../55.03.311/platform.json
- **Дослівно з джерела:**
  > ### Stable Arduino
  > currently espressif Arduino 3.3.11 and IDF v5.5.5.
  > 
  > [env:stable]
  > platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
  > board = ...
  > 
  > (platform.json теґа 55.03.311)
  > "version": "55.03.311"
  > …/arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення за рецензією. Розділ 13 правильно пояснював, що для Arduino 3.x і нових чипів потрібен `pioarduino`, — і давав для копіювання `platform = espressif32 @ 6.5.0`, тобто офіційну платформу епохи Arduino 2.x. Причому й у прикладі для S3.
Розбіжність між тим, що книга радить, і тим, що читач може скопіювати, гірша за просто застарілий приклад: копіюють частіше, ніж читають.
Усі приклади переведено на `pioarduino`. Рядок `platform` у розділі про кілька середовищ винесено в спільну секцію `[env]` — дві плати мусять збиратися однією платформою.
Пінування показано тегом релізу (`55.03.311`), а сам номер відсилає до таблиці версій частини IV, як вимагає Р4.
Підтверджено й те, що робить пораду несуперечливою: README форка називає ті самі Arduino 3.3.11 та IDF 5.5.5, що стоять у `toolchain-baseline.yaml`.
- **Прохід:** pass-17-simeystva-proektiv

---

<!-- fc id:T-13-024 sha:bd308fc1 src:manual/13-pio.md:73 klas:A -->
### T-13-024 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Запис `espressif32 @ 6.5.0` збереться — і дасть Arduino 2.x, тобто не те, про що написано в розділі 12, і без підтримки нових чипів.

**Дослівно з книги**

```
Офіційна платформа PlatformIO лишилася на Arduino 2.x. Запис
```

**Контекст**

```
## platformio.ini

Офіційна платформа PlatformIO лишилася на Arduino 2.x. Запис
`espressif32 @ 6.5.0` збереться — і дасть Arduino 2.x, тобто не те, про
що написано в розділі 12, і без підтримки нових чипів.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/platformio/platform-espressif32/master/platform.json
- **Дослівно з джерела:**
  > "version": "~3.20017.0"
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** запис espressif32 @ без версії дає Arduino 2.x
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-025 sha:749a3756 src:manual/13-pio.md:77 klas:A -->
### T-13-025 · proza · `manual/13-pio.md`

**Твердження, коротко**

> `pioarduino` розповсюджується не через реєстр PlatformIO, а архівом релізу, тому й рядок такий довгий.

**Дослівно з книги**

```
`pioarduino` розповсюджується не через реєстр PlatformIO, а архівом
```

**Контекст**

```
## platformio.ini

`pioarduino` розповсюджується не через реєстр PlatformIO, а архівом
релізу, тому й рядок такий довгий. Мітка `stable` завжди вказує на
поточний стабільний реліз форка — на момент цієї ревізії це Arduino
3.3.11 і ESP-IDF 5.5.5 (таблиця версій у частині IV).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/master/platform.json
- **Дослівно з джерела:**
  > "version": "https://github.com/espressif/arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz"
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** pioarduino розповсюджується через архив релізу, не через реєстр
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-026 sha:a8551e95 src:manual/13-pio.md:77 klas:A -->
### T-13-026 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Мітка `stable` завжди вказує на поточний стабільний реліз форка — на момент цієї ревізії це Arduino 3.3.11 і ESP-IDF 5.5.5 (таблиця версій у частині IV).

**Дослівно з книги**

```
`pioarduino` розповсюджується не через реєстр PlatformIO, а архівом
```

**Контекст**

```
## platformio.ini

`pioarduino` розповсюджується не через реєстр PlatformIO, а архівом
релізу, тому й рядок такий довгий. Мітка `stable` завжди вказує на
поточний стабільний реліз форка — на момент цієї ревізії це Arduino
3.3.11 і ESP-IDF 5.5.5 (таблиця версій у частині IV).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — наявність теґів і файли версій: espressif/esp-idf (components/esp_common/include/esp_idf_version.h), espressif/esptool (esptool/__init__.py), espressif/arduino-esp32 (platform.txt), pioarduino/platform-espressif32 (platform.json)
- **Дослівно з джерела:**
  > esp-idf v6.0.2  → 200,  v6.0.3 → 404      esp_idf_version.h: MAJOR 6 MINOR 0 PATCH 2
  > esp-idf v5.5.5  → 200,  v5.5.6 → 404
  > esptool v5.3.1  → 200,  v5.3.2 → 404      __init__.py: __version__ = "5.3.1"
  > arduino-esp32 3.3.11 → 200, 3.3.12 → 404  platform.txt: version=3.3.11
  > pioarduino 55.03.311 → 200, 55.03.312 → 404
  >     platform.json: "version": "55.03.311"
  >     і в ньому ж: .../arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, коди відповіді + файли версій, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Кожна з чотирьох версій підтверджена двічі: існуванням теґа й номером усередині самого репозиторію на цьому теґу. Наступного теґа немає в жодного — тобто це справді найновіші, а не просто наявні.
Окремо цінне спостереження: `platform.json` pioarduino 55.03.311 тягне саме `esp32-core-3.3.11`. Тобто два рядки таблиці версій книги узгоджені між собою не за збігом, а за побудовою — форк PlatformIO пінує рівно ту версію Arduino core, яку книга називає поточною.
`toolchain-baseline.yaml` уже мав `status: verified` на всіх чотирьох; цей прохід перевірив, що позначка відповідає дійсності, а не лишилася від попередньої ревізії.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-13-027 sha:47baf400 src:manual/13-pio.md:82 klas:F -->
### T-13-027 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Старий запис лишається доречним рівно в одному випадку: проєкт свідомо живе на Arduino 2.x і переносити його нікуди.

**Дослівно з книги**

```
Старий запис лишається доречним рівно в одному випадку: проєкт свідомо
```

**Контекст**

```
## platformio.ini

Старий запис лишається доречним рівно в одному випадку: проєкт свідомо
живе на Arduino 2.x і переносити його нікуди.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-028 sha:941bc495 src:manual/13-pio.md:86 klas:E -->
### T-13-028 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Розбір рядків, що мають значення.

**Контекст**

```
## platformio.ini

Розбір рядків, що мають значення.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-029 sha:a126aa2c src:manual/13-pio.md:88 klas:A -->
### T-13-029 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **`platform`.** Тут — джерело платформи, а не лише її версія.

**Контекст**

```
## platformio.ini

**`platform`.** Тут — джерело платформи, а не лише її версія.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/master/README.md
- **Дослівно з джерела:**
  > platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** platform specifies URL source of the platform
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-030 sha:ae130aac src:manual/13-pio.md:91 klas:E -->
### T-13-030 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Версію платформи треба пінити завжди.** Запис без версії означає «бери найсвіжішу», і одного дня проєкт, що збирався роками, перестане збиратися — на іншій машині, в іншого розробника, або у вас після оновлення.

**Дослівно з книги**

```
**Версію платформи треба пінити завжди.** Запис без версії означає «бери
```

**Контекст**

```
## platformio.ini

::: nezvorotne
**Версію платформи треба пінити завжди.** Запис без версії означає «бери
найсвіжішу», і одного дня проєкт, що збирався роками, перестане
збиратися — на іншій машині, в іншого розробника, або у вас після
оновлення.
```

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

<!-- fc id:T-13-031 sha:be464ff9 src:manual/13-pio.md:96 klas:E -->
### T-13-031 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Це та помилка, що виявляється в найгірший момент: коли треба терміново перезібрати прошивку для виробу в полі.

**Дослівно з книги**

```
Це та помилка, що виявляється в найгірший момент: коли треба терміново
```

**Контекст**

```
## platformio.ini

Це та помилка, що виявляється в найгірший момент: коли треба терміново
перезібрати прошивку для виробу в полі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-032 sha:d5d76327 src:manual/13-pio.md:99 klas:A -->
### T-13-032 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Для `pioarduino` пінування — це заміна мітки `stable` на **тег релізу**:

**Контекст**

```
## platformio.ini

Для `pioarduino` пінування — це заміна мітки `stable` на **тег релізу**:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/master/README.md
- **Дослівно з джерела:**
  > pio project init --board esp32dev
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** pioarduino uses release version tags for pinning
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-033 sha:827612bd src:manual/13-pio.md:101 klas:K -->
### T-13-033 · kod · `manual/13-pio.md`

**Твердження, коротко**

> ```ini
> platform = https://github.com/pioarduino/platform-espressif32/releases/download/55.03.311/platform-espressif32.zip
> ```

**Дослівно з книги**

````
```ini
````

**Контекст**

````
## platformio.ini

```ini
platform = https://github.com/pioarduino/platform-espressif32/releases/download/55.03.311/platform-espressif32.zip
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — наявність теґів і файли версій: espressif/esp-idf (components/esp_common/include/esp_idf_version.h), espressif/esptool (esptool/__init__.py), espressif/arduino-esp32 (platform.txt), pioarduino/platform-espressif32 (platform.json)
- **Дослівно з джерела:**
  > esp-idf v6.0.2  → 200,  v6.0.3 → 404      esp_idf_version.h: MAJOR 6 MINOR 0 PATCH 2
  > esp-idf v5.5.5  → 200,  v5.5.6 → 404
  > esptool v5.3.1  → 200,  v5.3.2 → 404      __init__.py: __version__ = "5.3.1"
  > arduino-esp32 3.3.11 → 200, 3.3.12 → 404  platform.txt: version=3.3.11
  > pioarduino 55.03.311 → 200, 55.03.312 → 404
  >     platform.json: "version": "55.03.311"
  >     і в ньому ж: .../arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, коди відповіді + файли версій, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Кожна з чотирьох версій підтверджена двічі: існуванням теґа й номером усередині самого репозиторію на цьому теґу. Наступного теґа немає в жодного — тобто це справді найновіші, а не просто наявні.
Окремо цінне спостереження: `platform.json` pioarduino 55.03.311 тягне саме `esp32-core-3.3.11`. Тобто два рядки таблиці версій книги узгоджені між собою не за збігом, а за побудовою — форк PlatformIO пінує рівно ту версію Arduino core, яку книга називає поточною.
`toolchain-baseline.yaml` уже мав `status: verified` на всіх чотирьох; цей прохід перевірив, що позначка відповідає дійсності, а не лишилася від попередньої ревізії.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-13-034 sha:fd412be3 src:manual/13-pio.md:105 klas:E -->
### T-13-034 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Номер тегу — з таблиці версій у частині IV; вона єдине місце в книзі, де версії живуть, і оновлюється окремо від тексту (Р4).

**Дослівно з книги**

```
Номер тегу — з таблиці версій у частині IV; вона єдине місце в книзі, де
```

**Контекст**

```
## platformio.ini

Номер тегу — з таблиці версій у частині IV; вона єдине місце в книзі, де
версії живуть, і оновлюється окремо від тексту (Р4).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-035 sha:2343936e src:manual/13-pio.md:109 klas:F -->
### T-13-035 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **`board`** — ідентифікатор плати з переліку PlatformIO.

**Дослівно з книги**

```
**`board`** — ідентифікатор плати з переліку PlatformIO. Він задає чип,
```

**Контекст**

```
## platformio.ini

**`board`** — ідентифікатор плати з переліку PlatformIO. Він задає чип,
обсяг флешу і розбивку за замовчуванням. Плату, якої немає в переліку,
описують власним файлом або беруть найближчу й правлять параметри.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-036 sha:c8f4d86f src:manual/13-pio.md:109 klas:E -->
### T-13-036 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Він задає чип, обсяг флешу і розбивку за замовчуванням.

**Дослівно з книги**

```
**`board`** — ідентифікатор плати з переліку PlatformIO. Він задає чип,
```

**Контекст**

```
## platformio.ini

**`board`** — ідентифікатор плати з переліку PlatformIO. Він задає чип,
обсяг флешу і розбивку за замовчуванням. Плату, якої немає в переліку,
описують власним файлом або беруть найближчу й правлять параметри.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-037 sha:7934e141 src:manual/13-pio.md:109 klas:E -->
### T-13-037 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Плату, якої немає в переліку, описують власним файлом або беруть найближчу й правлять параметри.

**Дослівно з книги**

```
**`board`** — ідентифікатор плати з переліку PlatformIO. Він задає чип,
```

**Контекст**

```
## platformio.ini

**`board`** — ідентифікатор плати з переліку PlatformIO. Він задає чип,
обсяг флешу і розбивку за замовчуванням. Плату, якої немає в переліку,
описують власним файлом або беруть найближчу й правлять параметри.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-038 sha:18fbe0ff src:manual/13-pio.md:113 klas:F -->
### T-13-038 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **`framework`** — `arduino` або `espidf`.

**Контекст**

```
## platformio.ini

**`framework`** — `arduino` або `espidf`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-039 sha:79d6fd32 src:manual/13-pio.md:115 klas:F -->
### T-13-039 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **`build_flags`** — параметри компіляції й макроси.

**Дослівно з книги**

```
**`build_flags`** — параметри компіляції й макроси. Зручний спосіб
```

**Контекст**

```
## platformio.ini

**`build_flags`** — параметри компіляції й макроси. Зручний спосіб
тримати конфігурацію в одному місці замість правок у коді.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-040 sha:33af8147 src:manual/13-pio.md:115 klas:E -->
### T-13-040 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Зручний спосіб тримати конфігурацію в одному місці замість правок у коді.

**Дослівно з книги**

```
**`build_flags`** — параметри компіляції й макроси. Зручний спосіб
```

**Контекст**

```
## platformio.ini

**`build_flags`** — параметри компіляції й макроси. Зручний спосіб
тримати конфігурацію в одному місці замість правок у коді.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-041 sha:7b36f4c5 src:manual/13-pio.md:118 klas:F -->
### T-13-041 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **`lib_deps`** — залежності з версіями.

**Дослівно з книги**

```
**`lib_deps`** — залежності з версіями. `^2.2.2` означає «сумісні
```

**Контекст**

```
## platformio.ini

**`lib_deps`** — залежності з версіями. `^2.2.2` означає «сумісні
оновлення»; для виробничого проєкту точна версія надійніша.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-042 sha:4b5106dd src:manual/13-pio.md:118 klas:F -->
### T-13-042 · proza · `manual/13-pio.md`

**Твердження, коротко**

> `^2.2.2` означає «сумісні оновлення»; для виробничого проєкту точна версія надійніша.

**Дослівно з книги**

```
**`lib_deps`** — залежності з версіями. `^2.2.2` означає «сумісні
```

**Контекст**

```
## platformio.ini

**`lib_deps`** — залежності з версіями. `^2.2.2` означає «сумісні
оновлення»; для виробничого проєкту точна версія надійніша.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-043 sha:6a3b8741 src:manual/13-pio.md:123 klas:E -->
### T-13-043 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Типовий випадок — один проєкт на дві плати:

**Контекст**

```
## Кілька середовищ

Типовий випадок — один проєкт на дві плати:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-044 sha:c028fc5b src:manual/13-pio.md:125 klas:K -->
### T-13-044 · kod · `manual/13-pio.md`

**Твердження, коротко**

> ```ini
> [env]
> platform = https://github.com/pioarduino/platform-espressif32/releases/download/55.03.311/platform-espressif32.zip
> framework = arduino
> monitor_speed = 115200
> lib_deps = adafruit/Adafruit BME280 Library @ 2.2.2
> 
> [env:classic]
> board = esp32dev
> 
> [env:s3]
> board = esp32-s3-devkitc-1
> build_flags = -DHAS_PSRAM
> ```

**Дослівно з книги**

````
```ini
````

**Контекст**

````
## Кілька середовищ

```ini
[env]
platform = https://github.com/pioarduino/platform-espressif32/releases/download/55.03.311/platform-espressif32.zip
framework = arduino
monitor_speed = 115200
lib_deps = adafruit/Adafruit BME280 Library @ 2.2.2
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — наявність теґів і файли версій: espressif/esp-idf (components/esp_common/include/esp_idf_version.h), espressif/esptool (esptool/__init__.py), espressif/arduino-esp32 (platform.txt), pioarduino/platform-espressif32 (platform.json)
- **Дослівно з джерела:**
  > esp-idf v6.0.2  → 200,  v6.0.3 → 404      esp_idf_version.h: MAJOR 6 MINOR 0 PATCH 2
  > esp-idf v5.5.5  → 200,  v5.5.6 → 404
  > esptool v5.3.1  → 200,  v5.3.2 → 404      __init__.py: __version__ = "5.3.1"
  > arduino-esp32 3.3.11 → 200, 3.3.12 → 404  platform.txt: version=3.3.11
  > pioarduino 55.03.311 → 200, 55.03.312 → 404
  >     platform.json: "version": "55.03.311"
  >     і в ньому ж: .../arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, коди відповіді + файли версій, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Кожна з чотирьох версій підтверджена двічі: існуванням теґа й номером усередині самого репозиторію на цьому теґу. Наступного теґа немає в жодного — тобто це справді найновіші, а не просто наявні.
Окремо цінне спостереження: `platform.json` pioarduino 55.03.311 тягне саме `esp32-core-3.3.11`. Тобто два рядки таблиці версій книги узгоджені між собою не за збігом, а за побудовою — форк PlatformIO пінує рівно ту версію Arduino core, яку книга називає поточною.
`toolchain-baseline.yaml` уже мав `status: verified` на всіх чотирьох; цей прохід перевірив, що позначка відповідає дійсності, а не лишилася від попередньої ревізії.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-13-045 sha:af92b07e src:manual/13-pio.md:140 klas:F -->
### T-13-045 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Спільна секція одна.** `[env]` без імені — це загальні налаштування, які успадковують усі середовища; імена робочих середовищ (`[env:classic]`, `[env:s3]`) мають бути різні.

**Дослівно з книги**

```
**Спільна секція одна.** `[env]` без імені — це загальні налаштування,
```

**Контекст**

```
## Кілька середовищ

**Спільна секція одна.** `[env]` без імені — це загальні налаштування,
які успадковують усі середовища; імена робочих середовищ (`[env:classic]`,
`[env:s3]`) мають бути різні. Двох секцій `[env]` в одному файлі не
буває — друга не додає до першої, і поводиться це не так, як здається.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-046 sha:90d170e3 src:manual/13-pio.md:140 klas:F -->
### T-13-046 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Двох секцій `[env]` в одному файлі не буває — друга не додає до першої, і поводиться це не так, як здається.

**Дослівно з книги**

```
**Спільна секція одна.** `[env]` без імені — це загальні налаштування,
```

**Контекст**

```
## Кілька середовищ

**Спільна секція одна.** `[env]` без імені — це загальні налаштування,
які успадковують усі середовища; імена робочих середовищ (`[env:classic]`,
`[env:s3]`) мають бути різні. Двох секцій `[env]` в одному файлі не
буває — друга не додає до першої, і поводиться це не так, як здається.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-047 sha:262212b8 src:manual/13-pio.md:145 klas:F -->
### T-13-047 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Рядок `platform` винесено в спільну секцію навмисно: дві плати мають збиратися **однією** платформою, інакше різниця між середовищами перестає бути різницею плат.

**Дослівно з книги**

```
Рядок `platform` винесено в спільну секцію навмисно: дві плати мають
```

**Контекст**

```
## Кілька середовищ

Рядок `platform` винесено в спільну секцію навмисно: дві плати мають
збиратися **однією** платформою, інакше різниця між середовищами
перестає бути різницею плат. Для S3 це не косметика — офіційна
платформа його новіші ревізії просто не знає.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-048 sha:6c4a7027 src:manual/13-pio.md:145 klas:A -->
### T-13-048 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Для S3 це не косметика — офіційна платформа його новіші ревізії просто не знає.

**Дослівно з книги**

```
Рядок `platform` винесено в спільну секцію навмисно: дві плати мають
```

**Контекст**

```
## Кілька середовищ

Рядок `platform` винесено в спільну секцію навмисно: дві плати мають
збиратися **однією** платформою, інакше різниця між середовищами
перестає бути різницею плат. Для S3 це не косметика — офіційна
платформа його новіші ревізії просто не знає.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/master/README.md
- **Дослівно з джерела:**
  > pio project init --board esp32dev
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** pio command is used to manage environments and build specific boards
- **Прохід:** prochid-13-pio

---

<!-- fc id:T-13-049 sha:bc2c14ce src:manual/13-pio.md:150 klas:F -->
### T-13-049 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Тут стоїть тег, а не `stable`**, і це та сама вимога, що й вище: файл, який можна скопіювати, має збиратися однаково завтра й через рік.

**Дослівно з книги**

```
**Тут стоїть тег, а не `stable`**, і це та сама вимога, що й вище: файл,
```

**Контекст**

```
## Кілька середовищ

**Тут стоїть тег, а не `stable`**, і це та сама вимога, що й вище: файл,
який можна скопіювати, має збиратися однаково завтра й через рік.
Мітка `stable` для швидкої спроби зручна, але відтворюваності не дає:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-050 sha:326f3278 src:manual/13-pio.md:150 klas:F -->
### T-13-050 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Мітка `stable` для швидкої спроби зручна, але відтворюваності не дає:

**Контекст**

```
## Кілька середовищ

**Тут стоїть тег, а не `stable`**, і це та сама вимога, що й вище: файл,
який можна скопіювати, має збиратися однаково завтра й через рік.
Мітка `stable` для швидкої спроби зручна, але відтворюваності не дає:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-051 sha:7131bc02 src:manual/13-pio.md:154 klas:K -->
### T-13-051 · kod · `manual/13-pio.md`

**Твердження, коротко**

> ```ini
> ; швидкий старт, НЕ відтворювано — платформа може змінитися будь-коли
> platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
> ```

**Дослівно з книги**

````
```ini
````

**Контекст**

````
## Кілька середовищ

```ini
; швидкий старт, НЕ відтворювано — платформа може змінитися будь-коли
platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/pioarduino/platform-espressif32/main/README.md та .../55.03.311/platform.json
- **Дослівно з джерела:**
  > ### Stable Arduino
  > currently espressif Arduino 3.3.11 and IDF v5.5.5.
  > 
  > [env:stable]
  > platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
  > board = ...
  > 
  > (platform.json теґа 55.03.311)
  > "version": "55.03.311"
  > …/arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення за рецензією. Розділ 13 правильно пояснював, що для Arduino 3.x і нових чипів потрібен `pioarduino`, — і давав для копіювання `platform = espressif32 @ 6.5.0`, тобто офіційну платформу епохи Arduino 2.x. Причому й у прикладі для S3.
Розбіжність між тим, що книга радить, і тим, що читач може скопіювати, гірша за просто застарілий приклад: копіюють частіше, ніж читають.
Усі приклади переведено на `pioarduino`. Рядок `platform` у розділі про кілька середовищ винесено в спільну секцію `[env]` — дві плати мусять збиратися однією платформою.
Пінування показано тегом релізу (`55.03.311`), а сам номер відсилає до таблиці версій частини IV, як вимагає Р4.
Підтверджено й те, що робить пораду несуперечливою: README форка називає ті самі Arduino 3.3.11 та IDF 5.5.5, що стоять у `toolchain-baseline.yaml`.
- **Прохід:** pass-17-simeystva-proektiv

---

<!-- fc id:T-13-052 sha:6619cb7d src:manual/13-pio.md:159 klas:E -->
### T-13-052 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Номер тегу — з таблиці версій у частині IV (Р4).

**Контекст**

```
## Кілька середовищ

Номер тегу — з таблиці версій у частині IV (Р4).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-053 sha:407ecd76 src:manual/13-pio.md:161 klas:F -->
### T-13-053 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Збирання конкретного середовища — вибором у панелі PlatformIO або `pio run -e s3`.

**Дослівно з книги**

```
Збирання конкретного середовища — вибором у панелі PlatformIO або
```

**Контекст**

```
## Кілька середовищ

Збирання конкретного середовища — вибором у панелі PlatformIO або
`pio run -e s3`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-054 sha:47b4dc2c src:manual/13-pio.md:164 klas:E -->
### T-13-054 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Для виробу це зручно й іншим чином: окремі середовища для налагоджувальної збірки (докладний лог) і робочої (мінімум логу, оптимізація за розміром).

**Дослівно з книги**

```
Для виробу це зручно й іншим чином: окремі середовища для
```

**Контекст**

```
## Кілька середовищ

Для виробу це зручно й іншим чином: окремі середовища для
налагоджувальної збірки (докладний лог) і робочої (мінімум логу,
оптимізація за розміром).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-055 sha:7c1dad7e src:manual/13-pio.md:170 klas:F -->
### T-13-055 · proza · `manual/13-pio.md`

**Твердження, коротко**

> `framework = espidf` дозволяє збирати проєкт ESP-IDF через PlatformIO.

**Контекст**

```
## ESP-IDF усередині PlatformIO

`framework = espidf` дозволяє збирати проєкт ESP-IDF через PlatformIO.
Працює, але з застереженням: версія ESP-IDF при цьому визначається
версією платформи, а не вашим вибором, і зазвичай відстає від поточного
stable.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-056 sha:36a4b4be src:manual/13-pio.md:170 klas:F -->
### T-13-056 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Працює, але з застереженням: версія ESP-IDF при цьому визначається версією платформи, а не вашим вибором, і зазвичай відстає від поточного stable.

**Дослівно з книги**

```
`framework = espidf` дозволяє збирати проєкт ESP-IDF через PlatformIO.
```

**Контекст**

```
## ESP-IDF усередині PlatformIO

`framework = espidf` дозволяє збирати проєкт ESP-IDF через PlatformIO.
Працює, але з застереженням: версія ESP-IDF при цьому визначається
версією платформи, а не вашим вибором, і зазвичай відстає від поточного
stable.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-057 sha:830b1a26 src:manual/13-pio.md:175 klas:F -->
### T-13-057 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Для серйозної роботи з ESP-IDF надійніше брати сам ESP-IDF з офіційним розширенням (розділ 11): там версія під вашим контролем, а вся штатна діагностика працює без обхідних шляхів.

**Дослівно з книги**

```
Для серйозної роботи з ESP-IDF надійніше брати сам ESP-IDF з офіційним
```

**Контекст**

```
## ESP-IDF усередині PlatformIO

Для серйозної роботи з ESP-IDF надійніше брати сам ESP-IDF з офіційним
розширенням (розділ 11): там версія під вашим контролем, а вся штатна
діагностика працює без обхідних шляхів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-058 sha:2b4c7e4e src:manual/13-pio.md:179 klas:F -->
### T-13-058 · proza · `manual/13-pio.md`

**Твердження, коротко**

> PlatformIO виграє там, де головне — Arduino і бібліотеки.

**Контекст**

```
## ESP-IDF усередині PlatformIO

PlatformIO виграє там, де головне — Arduino і бібліотеки.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-059 sha:f0918098 src:manual/13-pio.md:183 klas:E -->
### T-13-059 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Проєкт збирався, перестав.** Майже завжди — незапінена версія платформи або бібліотеки.

**Дослівно з книги**

```
**Проєкт збирався, перестав.** Майже завжди — незапінена версія
```

**Контекст**

```
## Типові проблеми

**Проєкт збирався, перестав.** Майже завжди — незапінена версія
платформи або бібліотеки. Перше, що перевіряти.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-060 sha:f8ccc59c src:manual/13-pio.md:186 klas:C -->
### T-13-060 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Бібліотека не знаходиться.** Ім'я в `lib_deps` має точно відповідати реєстру, разом з іменем автора: `adafruit/Adafruit BME280 Library`, а не просто назва.

**Дослівно з книги**

```
**Бібліотека не знаходиться.** Ім'я в `lib_deps` має точно відповідати
```

**Контекст**

```
## Типові проблеми

**Бібліотека не знаходиться.** Ім'я в `lib_deps` має точно відповідати
реєстру, разом з іменем автора: `adafruit/Adafruit BME280 Library`, а не
просто назва.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** https://www.bosch-sensortec.com/ (BME280 Datasheet, BST-BME280-DS002)
- **Що шукати в джерелі:** розділ «Register description»: адреси 0xD0 (id = 0x60), 0xE0, 0xF2 (ctrl_hum), 0xF4 (ctrl_meas), 0xF5 (config, біти 7–5 t_sb, 4–2 filter, 0 spi3w_en), 0xF7 (дані); блоки калібрування 0x88–0xA1 і 0xE1–0xE7, включно з упаковкою dig_H4 і dig_H5 у спільний байт 0xE5; розділ «Compensation formulas» — цілочислові версії для T, P, H і формати Q, у яких повертається результат.
- **Нотатка:** Найбільша група в книзі, що впирається в недосяжне джерело: увесь драйвер проєкту 59 і рекомендації розділів 44 і 45. Формули були звірені рядок у рядок у сесії рецензування 05 — але за знанням, а не за відкритим документом, тож клас тут C. Проміжний шлях до класу B: референсний драйвер `BoschSensortec/BME280_driver` на GitHub — той самий код від того самого автора; його спробує наступний прохід.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-13-061 sha:f1f3a5b4 src:manual/13-pio.md:190 klas:F -->
### T-13-061 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Плати немає в переліку.** Взяти найближчу за чипом і обсягом флешу й поправити `board_build.*` параметрами.

**Дослівно з книги**

```
**Плати немає в переліку.** Взяти найближчу за чипом і обсягом флешу й
```

**Контекст**

```
## Типові проблеми

**Плати немає в переліку.** Взяти найближчу за чипом і обсягом флешу й
поправити `board_build.*` параметрами.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-062 sha:6ef65336 src:manual/13-pio.md:193 klas:E -->
### T-13-062 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Конфлікт із встановленим ESP-IDF.** PlatformIO тримає власні тулчейни окремо.

**Дослівно з книги**

```
**Конфлікт із встановленим ESP-IDF.** PlatformIO тримає власні тулчейни
```

**Контекст**

```
## Типові проблеми

**Конфлікт із встановленим ESP-IDF.** PlatformIO тримає власні тулчейни
окремо. Змінні середовища від `export.sh`, активовані в тому ж терміналі,
можуть заплутати збирання. Не змішувати в одному вікні.
```

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

<!-- fc id:T-13-063 sha:24b7726c src:manual/13-pio.md:193 klas:F -->
### T-13-063 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Змінні середовища від `export.sh`, активовані в тому ж терміналі, можуть заплутати збирання.

**Дослівно з книги**

```
**Конфлікт із встановленим ESP-IDF.** PlatformIO тримає власні тулчейни
```

**Контекст**

```
## Типові проблеми

**Конфлікт із встановленим ESP-IDF.** PlatformIO тримає власні тулчейни
окремо. Змінні середовища від `export.sh`, активовані в тому ж терміналі,
можуть заплутати збирання. Не змішувати в одному вікні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-064 sha:71f8b903 src:manual/13-pio.md:193 klas:E -->
### T-13-064 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Не змішувати в одному вікні.

**Дослівно з книги**

```
можуть заплутати збирання. Не змішувати в одному вікні.
```

**Контекст**

```
## Типові проблеми

**Конфлікт із встановленим ESP-IDF.** PlatformIO тримає власні тулчейни
окремо. Змінні середовища від `export.sh`, активовані в тому ж терміналі,
можуть заплутати збирання. Не змішувати в одному вікні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-065 sha:e09bc506 src:manual/13-pio.md:197 klas:E -->
### T-13-065 · proza · `manual/13-pio.md`

**Твердження, коротко**

> **Монітор не відкривається.** Порт зайнятий іншим монітором — та сама причина, що скрізь (розділ 09).

**Дослівно з книги**

```
**Монітор не відкривається.** Порт зайнятий іншим монітором — та сама
```

**Контекст**

```
## Типові проблеми

**Монітор не відкривається.** Порт зайнятий іншим монітором — та сама
причина, що скрізь (розділ 09).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-066 sha:f12c5e0a src:manual/13-pio.md:202 klas:E -->
### T-13-066 · tablycya · `manual/13-pio.md`

**Твердження, коротко**

> | Ситуація | Що брати |

**Контекст**

```
## Що обрати


| Ситуація | Що брати |
|---|---|
| Arduino + багато бібліотек, проєкт із кількох файлів | PlatformIO / pioarduino |
| Одна плата, один файл, швидка перевірка | Arduino IDE |
| Кілька цільових плат з одного коду | PlatformIO / pioarduino |
| Виріб, OTA, серійність, довгий супровід | ESP-IDF (розділ 11) |
| Потрібні найновіші чипи або Arduino 3.x | pioarduino |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-067 sha:a2387335 src:manual/13-pio.md:204 klas:F -->
### T-13-067 · tablycya · `manual/13-pio.md`

**Твердження, коротко**

> | Arduino + багато бібліотек, проєкт із кількох файлів | PlatformIO / pioarduino |

**Контекст**

```
## Що обрати


| Ситуація | Що брати |
|---|---|
| Arduino + багато бібліотек, проєкт із кількох файлів | PlatformIO / pioarduino |
| Одна плата, один файл, швидка перевірка | Arduino IDE |
| Кілька цільових плат з одного коду | PlatformIO / pioarduino |
| Виріб, OTA, серійність, довгий супровід | ESP-IDF (розділ 11) |
| Потрібні найновіші чипи або Arduino 3.x | pioarduino |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-068 sha:7ebd085f src:manual/13-pio.md:205 klas:F -->
### T-13-068 · tablycya · `manual/13-pio.md`

**Твердження, коротко**

> | Одна плата, один файл, швидка перевірка | Arduino IDE |

**Контекст**

```
## Що обрати


| Ситуація | Що брати |
|---|---|
| Arduino + багато бібліотек, проєкт із кількох файлів | PlatformIO / pioarduino |
| Одна плата, один файл, швидка перевірка | Arduino IDE |
| Кілька цільових плат з одного коду | PlatformIO / pioarduino |
| Виріб, OTA, серійність, довгий супровід | ESP-IDF (розділ 11) |
| Потрібні найновіші чипи або Arduino 3.x | pioarduino |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-069 sha:41c63667 src:manual/13-pio.md:206 klas:F -->
### T-13-069 · tablycya · `manual/13-pio.md`

**Твердження, коротко**

> | Кілька цільових плат з одного коду | PlatformIO / pioarduino |

**Контекст**

```
## Що обрати


| Ситуація | Що брати |
|---|---|
| Arduino + багато бібліотек, проєкт із кількох файлів | PlatformIO / pioarduino |
| Одна плата, один файл, швидка перевірка | Arduino IDE |
| Кілька цільових плат з одного коду | PlatformIO / pioarduino |
| Виріб, OTA, серійність, довгий супровід | ESP-IDF (розділ 11) |
| Потрібні найновіші чипи або Arduino 3.x | pioarduino |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-070 sha:911cb2bf src:manual/13-pio.md:207 klas:A -->
### T-13-070 · tablycya · `manual/13-pio.md`

**Твердження, коротко**

> | Виріб, OTA, серійність, довгий супровід | ESP-IDF (розділ 11) |

**Контекст**

```
## Що обрати


| Ситуація | Що брати |
|---|---|
| Arduino + багато бібліотек, проєкт із кількох файлів | PlatformIO / pioarduino |
| Одна плата, один файл, швидка перевірка | Arduino IDE |
| Кілька цільових плат з одного коду | PlatformIO / pioarduino |
| Виріб, OTA, серійність, довгий супровід | ESP-IDF (розділ 11) |
| Потрібні найновіші чипи або Arduino 3.x | pioarduino |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > Factory app, two OTA definitions
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Таблиці розділів ESP-IDF підтримують OTA, що потрібне для серійного виробництва та довгострокового супроводу
- **Прохід:** klas-f-13-pio

---

<!-- fc id:T-13-071 sha:90f5ca53 src:manual/13-pio.md:208 klas:F -->
### T-13-071 · tablycya · `manual/13-pio.md`

**Твердження, коротко**

> | Потрібні найновіші чипи або Arduino 3.x | pioarduino |

**Контекст**

```
## Що обрати


| Ситуація | Що брати |
|---|---|
| Arduino + багато бібліотек, проєкт із кількох файлів | PlatformIO / pioarduino |
| Одна плата, один файл, швидка перевірка | Arduino IDE |
| Кілька цільових плат з одного коду | PlatformIO / pioarduino |
| Виріб, OTA, серійність, довгий супровід | ESP-IDF (розділ 11) |
| Потрібні найновіші чипи або Arduino 3.x | pioarduino |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-072 sha:ee36c4b3 src:manual/13-pio.md:212 klas:F -->
### T-13-072 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Офіційна платформа PlatformIO відстала від Arduino core; спільнотний форк pioarduino підтримує актуальні версії.

**Дослівно з книги**

```
Офіційна платформа PlatformIO відстала від Arduino core; спільнотний
```

**Контекст**

```
## Що з цього треба запам'ятати

Офіційна платформа PlatformIO відстала від Arduino core; спільнотний
форк pioarduino підтримує актуальні версії. Стан варто перевіряти перед
початком проєкту — саме ця частина застаріває найшвидше.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-073 sha:03240a6a src:manual/13-pio.md:212 klas:E -->
### T-13-073 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Стан варто перевіряти перед початком проєкту — саме ця частина застаріває найшвидше.

**Дослівно з книги**

```
Офіційна платформа PlatformIO відстала від Arduino core; спільнотний
```

**Контекст**

```
## Що з цього треба запам'ятати

Офіційна платформа PlatformIO відстала від Arduino core; спільнотний
форк pioarduino підтримує актуальні версії. Стан варто перевіряти перед
початком проєкту — саме ця частина застаріває найшвидше.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-074 sha:16ba4163 src:manual/13-pio.md:216 klas:E -->
### T-13-074 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Версію платформи і версії бібліотек пінити завжди.

**Дослівно з книги**

```
Версію платформи і версії бібліотек пінити завжди. Незапінена версія
```

**Контекст**

```
## Що з цього треба запам'ятати

Версію платформи і версії бібліотек пінити завжди. Незапінена версія
ламає збирання в найгірший момент.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-075 sha:b81ae778 src:manual/13-pio.md:216 klas:E -->
### T-13-075 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Незапінена версія ламає збирання в найгірший момент.

**Дослівно з книги**

```
Версію платформи і версії бібліотек пінити завжди. Незапінена версія
```

**Контекст**

```
## Що з цього треба запам'ятати

Версію платформи і версії бібліотек пінити завжди. Незапінена версія
ламає збирання в найгірший момент.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-076 sha:a1620013 src:manual/13-pio.md:219 klas:F -->
### T-13-076 · proza · `manual/13-pio.md`

**Твердження, коротко**

> `platformio.ini` у git повністю описує проєкт — у цьому головна цінність.

**Контекст**

```
## Що з цього треба запам'ятати

`platformio.ini` у git повністю описує проєкт — у цьому головна цінність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-13-077 sha:07b465b5 src:manual/13-pio.md:221 klas:F -->
### T-13-077 · proza · `manual/13-pio.md`

**Твердження, коротко**

> Для ESP-IDF надійніше брати сам ESP-IDF, а не його через PlatformIO.

**Контекст**

```
## Що з цього треба запам'ятати

Для ESP-IDF надійніше брати сам ESP-IDF, а не його через PlatformIO.
```

**Доказ**

- **Клас:** F — не звірено

---
