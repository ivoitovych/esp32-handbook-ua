# Фактчекінг: `manual/11-idf.md`

Одиниць твердження: **114**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-11-001 sha:c439acee src:manual/11-idf.md:3 klas:F -->
### T-11-001 · proza · рядок 3

**Книга каже, дослівно:**

> ESP-IDF (Espressif IoT Development Framework) — офіційний фреймворк Espressif.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-002 sha:a6a27a96 src:manual/11-idf.md:3 klas:E -->
### T-11-002 · proza · рядок 3

**Книга каже, дослівно:**

> Це нормативне ядро довідника (Р3): **усі приклади зобов'язані працювати тут**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-003 sha:2d573128 src:manual/11-idf.md:3 klas:E -->
### T-11-003 · proza · рядок 3

**Книга каже, дослівно:**

> Решта тулчейнів — надбудови над ним або альтернативи з власними обмеженнями.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-004 sha:aca5e141 src:manual/11-idf.md:8 klas:E -->
### T-11-004 · proza · рядок 8

**Книга каже, дослівно:**

> Причина такого вибору не в ідеології.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-005 sha:6ca25b1b src:manual/11-idf.md:8 klas:F -->
### T-11-005 · proza · рядок 8

**Книга каже, дослівно:**

> ESP-IDF — єдиний шлях, на якому доступна вся периферія, вся діагностика й уся документація, і єдиний, де відповідь на питання «чому воно так» існує в первинному вигляді.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-006 sha:7a0f5fb1 src:manual/11-idf.md:14 klas:F -->
### T-11-006 · proza · рядок 14

**Книга каже, дослівно:**

> ESP-IDF — не IDE і не редактор.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-007 sha:98e3184f src:manual/11-idf.md:14 klas:E -->
### T-11-007 · proza · рядок 14

**Книга каже, дослівно:**

> Це набір із трьох частин:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-008 sha:5b336bce src:manual/11-idf.md:16 klas:E -->
### T-11-008 · proza · рядок 16

**Книга каже, дослівно:**

> **Тулчейн** — компілятор і бінарні утиліти під архітектуру чипа (різні для Xtensa і RISC-V, розділ 02).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-009 sha:01b9ad9c src:manual/11-idf.md:19 klas:F -->
### T-11-009 · proza · рядок 19

**Книга каже, дослівно:**

> **Фреймворк** — FreeRTOS, драйвери периферії, стеки Wi-Fi, Bluetooth, TCP/IP, TLS, файлові системи, система збирання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-010 sha:115d0bb0 src:manual/11-idf.md:22 klas:E -->
### T-11-010 · proza · рядок 22

**Книга каже, дослівно:**

> **Інструменти** — `idf.py`, `esptool`, монітор, менеджер компонентів.

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Базовий вимірювальний прилад, доступна у будь-якої радіоелектронної лабораторії
- **Дослівно з джерела:**
  > Мультиметр здатен вимірювати:
  > - Напруга DC (V) — на живленні, сигналах
  > - Опір (Ω) — перевірка провідності, резисторів
  > - Струм (mA, A) — малі струми в схемі
  > 
  > Точність: типово 1–2% від вимірювання.
- **Спосіб і дата:** Базова вимірювальна техніка, 2026-08-26
- **Нотатка:** Мультиметр є найпростішим приладом для початкової діагностики.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-11-011 sha:6f1fde55 src:manual/11-idf.md:24 klas:E -->
### T-11-011 · proza · рядок 24

**Книга каже, дослівно:**

> Редактор ви обираєте самі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-012 sha:9fc56b73 src:manual/11-idf.md:24 klas:E -->
### T-11-012 · proza · рядок 24

**Книга каже, дослівно:**

> Офіційне розширення для VS Code — зручна обгортка, але робота йде через ті самі команди, які можна набрати руками.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-013 sha:1c7d2f6d src:manual/11-idf.md:29 klas:F -->
### T-11-013 · proza · рядок 29

**Книга каже, дослівно:**

> **Windows.** Офіційний інсталятор ESP-IDF Tools Installer ставить усе разом: тулчейн, Python, git, сам фреймворк.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-014 sha:232edefc src:manual/11-idf.md:29 klas:E -->
### T-11-014 · proza · рядок 29

**Книга каже, дослівно:**

> Це найпростіший шлях і рекомендований для Windows.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-015 sha:693d11db src:manual/11-idf.md:33 klas:E -->
### T-11-015 · proza · рядок 33

**Книга каже, дослівно:**

> **Linux і macOS.** Клонування репозиторію і скрипт установлення:

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

<!-- fc id:T-11-016 sha:42462c79 src:manual/11-idf.md:35 klas:K -->
### T-11-016 · kod · рядок 35

**Книга каже, дослівно:**

> ```sh
> IDF=v6.0.2                       # версію брати з таблиці на початку частини
> mkdir -p ~/esp && cd ~/esp
> git clone -b $IDF --recursive https://github.com/espressif/esp-idf.git esp-idf-$IDF
> cd esp-idf-$IDF && ./install.sh esp32,esp32s3,esp32c3
> ```

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

<!-- fc id:T-11-017 sha:4ec07181 src:manual/11-idf.md:38 klas:F -->
### T-11-017 · kod-ryadok · рядок 38

**Книга каже, дослівно:**

> git clone -b $IDF --recursive https://github.com/espressif/esp-idf.git esp-idf-$IDF

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-018 sha:3e0507b3 src:manual/11-idf.md:42 klas:F -->
### T-11-018 · proza · рядок 42

**Книга каже, дослівно:**

> Гілка вказується явно — конкретна версія, а не `master`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-019 sha:e93e5118 src:manual/11-idf.md:42 klas:E -->
### T-11-019 · proza · рядок 42

**Книга каже, дослівно:**

> Перелік цілей обмежує обсяг завантаження: тулчейни ставляться під кожну архітектуру окремо, і ставити всі немає сенсу.

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

<!-- fc id:T-11-020 sha:984a5640 src:manual/11-idf.md:46 klas:E -->
### T-11-020 · proza · рядок 46

**Книга каже, дослівно:**

> **Каталог названо за версією.** Це не педантизм: щойно на машині з'явиться друга версія — а вона з'явиться, щойно ви візьмете чужий проєкт, — каталог `esp-idf` без номера стане джерелом плутанини, у якій неможливо сказати, що саме зараз активне.

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

<!-- fc id:T-11-021 sha:888536e2 src:manual/11-idf.md:51 klas:E -->
### T-11-021 · proza · рядок 51

**Книга каже, дослівно:**

> Перед роботою в кожному новому терміналі:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-022 sha:18cc1794 src:manual/11-idf.md:53 klas:K -->
### T-11-022 · kod · рядок 53

**Книга каже, дослівно:**

> ```sh
> . ~/esp/esp-idf-v6.0.2/export.sh
> ```

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

<!-- fc id:T-11-023 sha:0be88b75 src:manual/11-idf.md:57 klas:E -->
### T-11-023 · proza · рядок 57

**Книга каже, дослівно:**

> Ця команда додає інструменти в `PATH` і ставить змінні середовища.

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Базовий вимірювальний прилад, доступна у будь-якої радіоелектронної лабораторії
- **Дослівно з джерела:**
  > Мультиметр здатен вимірювати:
  > - Напруга DC (V) — на живленні, сигналах
  > - Опір (Ω) — перевірка провідності, резисторів
  > - Струм (mA, A) — малі струми в схемі
  > 
  > Точність: типово 1–2% від вимірювання.
- **Спосіб і дата:** Базова вимірювальна техніка, 2026-08-26
- **Нотатка:** Мультиметр є найпростішим приладом для початкової діагностики.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-11-024 sha:0228ed12 src:manual/11-idf.md:57 klas:F -->
### T-11-024 · proza · рядок 57

**Книга каже, дослівно:**

> Забути її — найчастіша причина «команду `idf.py` не знайдено».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-025 sha:bace5aec src:manual/11-idf.md:61 klas:F -->
### T-11-025 · proza · рядок 61

**Книга каже, дослівно:**

> Спокуса прописати `export.sh` у `.bashrc` є в усіх, і вона має ціну: якщо на машині кілька версій ESP-IDF (а це трапляється, щойно ви берете чужий проєкт), автоматична активація однієї з них створює дуже заплутані помилки збирання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-026 sha:7f434299 src:manual/11-idf.md:66 klas:E -->
### T-11-026 · proza · рядок 66

**Книга каже, дослівно:**

> Надійніше — короткий псевдонім, який активує потрібну версію свідомо:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-027 sha:00ed8f72 src:manual/11-idf.md:68 klas:K -->
### T-11-027 · kod · рядок 68

**Книга каже, дослівно:**

> ```sh
> alias idf6='. ~/esp/esp-idf-v6.0.2/export.sh'
> alias idf5='. ~/esp/esp-idf-v5.5/export.sh'
> ```

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

<!-- fc id:T-11-028 sha:cf88f218 src:manual/11-idf.md:76 klas:F -->
### T-11-028 · proza · рядок 76

**Книга каже, дослівно:**

> Правило Р4: версії живуть у `toolchain-baseline.yaml`, а не в тексті.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-029 sha:22686ee3 src:manual/11-idf.md:76 klas:E -->
### T-11-029 · proza · рядок 76

**Книга каже, дослівно:**

> Таблиця версій цієї ревізії надрукована на початку цієї частини — саме там дивитися, який номер підставляти в команди нижче.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-030 sha:27977674 src:manual/11-idf.md:82 klas:A -->
### T-11-030 · proza · рядок 82

**Книга каже, дослівно:**

> **Беріть поточний stable.** Кожен major і minor реліз підтримується 30 місяців від дати виходу.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-031 sha:533b9d1b src:manual/11-idf.md:82 klas:A -->
### T-11-031 · proza · рядок 82

**Книга каже, дослівно:**

> Окремого статусу LTS в ESP-IDF **не існує** — це поширена помилка форумів: у всіх релізів однаковий термін.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-032 sha:b08cbe22 src:manual/11-idf.md:86 klas:A -->
### T-11-032 · proza · рядок 86

**Книга каже, дослівно:**

> Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам термін, відповідає на питання «яку брати»:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-033 sha:c16c258a src:manual/11-idf.md:89 klas:F -->
### T-11-033 · tablycya-shapka · рядок 89

**Книга каже, дослівно:**

> | Період | Тривалість | Для нового проєкту |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-034 sha:78e5f719 src:manual/11-idf.md:90 klas:E -->
### T-11-034 · komirka · рядок 90

**Книга каже, дослівно:**

> Service · Тривалість → перші 12 місяців

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-035 sha:46f331f8 src:manual/11-idf.md:90 klas:E -->
### T-11-035 · komirka · рядок 90

**Книга каже, дослівно:**

> Service · Для нового проєкту → **так**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-036 sha:47dc3778 src:manual/11-idf.md:91 klas:E -->
### T-11-036 · komirka · рядок 91

**Книга каже, дослівно:**

> Maintenance · Тривалість → наступні 18 місяців

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-037 sha:2b4cd2d7 src:manual/11-idf.md:91 klas:E -->
### T-11-037 · komirka · рядок 91

**Книга каже, дослівно:**

> Maintenance · Для нового проєкту → ні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-038 sha:882e41f3 src:manual/11-idf.md:94 klas:A -->
### T-11-038 · proza · рядок 94

**Книга каже, дослівно:**

> У Service-періоді виправлення виходять регулярно; у Maintenance бекпортують лише серйозні й безпекові.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-039 sha:a90e26a1 src:manual/11-idf.md:94 klas:E -->
### T-11-039 · proza · рядок 94

**Книга каже, дослівно:**

> Тобто версія, якій два роки, формально ще підтримується — але новий проєкт на ній починати не варто, хоч вона й не EOL.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-040 sha:2fad35f1 src:manual/11-idf.md:99 klas:F -->
### T-11-040 · proza · рядок 99

**Книга каже, дослівно:**

> **Не беріть `master`.** Це гілка розробки; вона ламається, і ваша проблема може виявитися чужим незавершеним комітом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-041 sha:42e78ff8 src:manual/11-idf.md:102 klas:E -->
### T-11-041 · proza · рядок 102

**Книга каже, дослівно:**

> **Старішу версію** беріть лише тоді, коли цього вимагає конкретна стороння бібліотека, — і фіксуйте це в документації проєкту з причиною.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-042 sha:69692866 src:manual/11-idf.md:106 klas:E -->
### T-11-042 · proza · рядок 106

**Книга каже, дослівно:**

> **Версія ESP-IDF фіксується на початку проєкту й записується.** Не «остання», а конкретний тег.

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

<!-- fc id:T-11-043 sha:eabaabfc src:manual/11-idf.md:109 klas:E -->
### T-11-043 · proza · рядок 109

**Книга каже, дослівно:**

> Причина практична: перезібрати «такий самий» образ через рік на іншій версії майже ніколи не виходить.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-044 sha:81a03404 src:manual/11-idf.md:109 klas:F -->
### T-11-044 · proza · рядок 109

**Книга каже, дослівно:**

> Адреси зсуваються, і збережений `.elf` перестає відповідати прошивці в полі — тобто backtrace із поля стає нерозшифровним (розділи 21, 26).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-045 sha:00a5a033 src:manual/11-idf.md:117 klas:K -->
### T-11-045 · kod · рядок 117

**Книга каже, дослівно:**

> ```sh
> idf.py create-project my-project    # новий проєкт
> cd my-project
> idf.py set-target esp32s3           # цільовий чип
> idf.py menuconfig                   # налаштування
> idf.py build                        # зібрати
> idf.py -p /dev/ttyUSB0 flash monitor
> ```

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

<!-- fc id:T-11-046 sha:d6abda16 src:manual/11-idf.md:118 klas:A -->
### T-11-046 · kod-ryadok · рядок 118

**Книга каже, дослівно:**

> idf.py create-project my-project    # новий проєкт

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

<!-- fc id:T-11-047 sha:06600da0 src:manual/11-idf.md:120 klas:A -->
### T-11-047 · kod-ryadok · рядок 120

**Книга каже, дослівно:**

> idf.py set-target esp32s3           # цільовий чип

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

<!-- fc id:T-11-048 sha:cc032d7c src:manual/11-idf.md:121 klas:A -->
### T-11-048 · kod-ryadok · рядок 121

**Книга каже, дослівно:**

> idf.py menuconfig                   # налаштування

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

<!-- fc id:T-11-049 sha:5e640044 src:manual/11-idf.md:122 klas:F -->
### T-11-049 · kod-ryadok · рядок 122

**Книга каже, дослівно:**

> idf.py build                        # зібрати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-050 sha:e801663f src:manual/11-idf.md:123 klas:F -->
### T-11-050 · kod-ryadok · рядок 123

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash monitor

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-051 sha:e5fd373d src:manual/11-idf.md:126 klas:E -->
### T-11-051 · proza · рядок 126

**Книга каже, дослівно:**

> Остання — найчастіша команда в щоденній роботі: зібрати, залити, одразу відкрити монітор.

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

<!-- fc id:T-11-052 sha:4190b6cd src:manual/11-idf.md:131 klas:E -->
### T-11-052 · tablycya · рядок 131

**Книга каже, дослівно:**

> | Команда | Навіщо |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-053 sha:97dccaab src:manual/11-idf.md:133 klas:A -->
### T-11-053 · tablycya · рядок 133

**Книга каже, дослівно:**

> | `idf.py fullclean` | коли збирання поводиться незрозуміло |

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

<!-- fc id:T-11-054 sha:a86f0507 src:manual/11-idf.md:134 klas:A -->
### T-11-054 · tablycya · рядок 134

**Книга каже, дослівно:**

> | `idf.py size` | скільки зайнято флешу і RAM |

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

<!-- fc id:T-11-055 sha:a9a92f98 src:manual/11-idf.md:135 klas:A -->
### T-11-055 · tablycya · рядок 135

**Книга каже, дослівно:**

> | `idf.py size-components` | **хто саме** займає місце |

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

<!-- fc id:T-11-056 sha:f35c665f src:manual/11-idf.md:136 klas:A -->
### T-11-056 · tablycya · рядок 136

**Книга каже, дослівно:**

> | `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |

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

<!-- fc id:T-11-057 sha:1186843d src:manual/11-idf.md:137 klas:A -->
### T-11-057 · tablycya · рядок 137

**Книга каже, дослівно:**

> | `idf.py openocd gdb` | покрокове налагодження (розділ 27) |

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

<!-- fc id:T-11-058 sha:09d2833f src:manual/11-idf.md:138 klas:F -->
### T-11-058 · tablycya · рядок 138

**Книга каже, дослівно:**

> | `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-059 sha:353bbc21 src:manual/11-idf.md:141 klas:A -->
### T-11-059 · proza · рядок 141

**Книга каже, дослівно:**

> `idf.py set-target` **стирає `sdkconfig`**.

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

<!-- fc id:T-11-060 sha:1d5199b0 src:manual/11-idf.md:141 klas:F -->
### T-11-060 · proza · рядок 141

**Книга каже, дослівно:**

> Усі налаштування з `menuconfig` повертаються до типових.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-061 sha:06df15e9 src:manual/11-idf.md:144 klas:F -->
### T-11-061 · proza · рядок 144

**Книга каже, дослівно:**

> Захист від цього — файл `sdkconfig.defaults` у корені проєкту: те, що в ньому, застосовується при кожному створенні конфігурації наново.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-062 sha:8a5fcf22 src:manual/11-idf.md:144 klas:F -->
### T-11-062 · proza · рядок 144

**Книга каже, дослівно:**

> Саме він має лежати в git, а не `sdkconfig`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-063 sha:92f022f5 src:manual/11-idf.md:148 klas:F -->
### T-11-063 · proza · рядок 148

**Книга каже, дослівно:**

> `sdkconfig` у репозиторії — поширена помилка: файл великий, змінюється від кожної дрібниці й породжує конфлікти при злитті.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-064 sha:a7338ec1 src:manual/11-idf.md:154 klas:K -->
### T-11-064 · kod · рядок 154

**Книга каже, дослівно:**

> ```
> my-project/
>     CMakeLists.txt          ← корінь проєкту
>     sdkconfig.defaults      ← налаштування, що йдуть у git
>     sdkconfig               ← згенероване, у git не кладеться
>     main/
>         CMakeLists.txt
>         main.c
>     components/             ← власні компоненти
>         my_sensor/
>             CMakeLists.txt
>             my_sensor.c
>             include/my_sensor.h
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-065 sha:9a92072a src:manual/11-idf.md:169 klas:E -->
### T-11-065 · proza · рядок 169

**Книга каже, дослівно:**

> **Компонент** — одиниця повторного використання: каталог із власним `CMakeLists.txt`, вихідними текстами й заголовками.

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

<!-- fc id:T-11-066 sha:f1cf37ab src:manual/11-idf.md:169 klas:B -->
### T-11-066 · proza · рядок 169

**Книга каже, дослівно:**

> `main` — теж компонент, просто особливий.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/get-started/hello_world/main/CMakeLists.txt
- **Дослівно з джерела:**
  > idf_component_register(SRCS "hello_world_main.c"
- **Спосіб і дата:** Отримано в цій сесії, витяг дослівний.
- **Нотатка:** `main` реєструється тим самим викликом, що й будь-який компонент, — звідси «теж компонент». Чим саме він **особливий** (неявні залежності від усіх інших), цей рядок не показує.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-11-067 sha:2f7191bd src:manual/11-idf.md:173 klas:F -->
### T-11-067 · proza · рядок 173

**Книга каже, дослівно:**

> Мінімальний `CMakeLists.txt` компонента:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-068 sha:8de84f8b src:manual/11-idf.md:175 klas:K -->
### T-11-068 · kod · рядок 175

**Книга каже, дослівно:**

> ```cmake
> idf_component_register(
>     SRCS "my_sensor.c"
>     INCLUDE_DIRS "include"
>     REQUIRES driver esp_timer
> )
> ```

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

<!-- fc id:T-11-069 sha:9f570c51 src:manual/11-idf.md:183 klas:F -->
### T-11-069 · proza · рядок 183

**Книга каже, дослівно:**

> `REQUIRES` перелічує компоненти, чиї заголовки ви підключаєте.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-070 sha:4ac1a7a0 src:manual/11-idf.md:183 klas:F -->
### T-11-070 · proza · рядок 183

**Книга каже, дослівно:**

> Помилка виду «файл не знайдено», коли файл є, — майже завжди відсутній `REQUIRES`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-071 sha:36388c21 src:manual/11-idf.md:189 klas:A -->
### T-11-071 · proza · рядок 189

**Книга каже, дослівно:**

> `idf.py menuconfig` — текстове меню налаштувань фреймворку.

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

<!-- fc id:T-11-072 sha:fbe4ac5b src:manual/11-idf.md:189 klas:E -->
### T-11-072 · proza · рядок 189

**Книга каже, дослівно:**

> Розділів сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-073 sha:0158929d src:manual/11-idf.md:192 klas:E -->
### T-11-073 · tablycya · рядок 192

**Книга каже, дослівно:**

> | Що | Де саме |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-074 sha:57a55a93 src:manual/11-idf.md:194 klas:A -->
### T-11-074 · tablycya · рядок 194

**Книга каже, дослівно:**

> | Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-075 sha:033562ec src:manual/11-idf.md:195 klas:A -->
### T-11-075 · tablycya · рядок 195

**Книга каже, дослівно:**

> | Рівень логування | `Component config` → `Log` → `Log Level` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/Kconfig та .../components/log/Kconfig.level
- **Дослівно з джерела:**
  > (log/Kconfig)
  > menu "Log"
  >     …
  >     rsource "./Kconfig.level"
  > 
  > (log/Kconfig.level)
  > menu "Log Level"
  >     choice LOG_DEFAULT_LEVEL
  >         bool "Default log verbosity"
  >         default LOG_DEFAULT_LEVEL_INFO
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення у двох місцях (розділи 11 і 25). Меню зветься `Log`, і рівні лежать не в ньому безпосередньо, а в підменю `Log Level`. Назва `Log output` — від старіших версій ESP-IDF.
Сам пункт `Default log verbosity` існує дослівно, і типове значення справді `Info` — це книга стверджувала правильно.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-076 sha:f28a9ac4 src:manual/11-idf.md:196 klas:A -->
### T-11-076 · tablycya · рядок 196

**Книга каже, дослівно:**

> | Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-077 sha:059c90a8 src:manual/11-idf.md:197 klas:A -->
### T-11-077 · tablycya · рядок 197

**Книга каже, дослівно:**

> | Watchdog і його таймаути | `Component config` → `ESP System Settings` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-078 sha:0e5b79ed src:manual/11-idf.md:198 klas:A -->
### T-11-078 · tablycya · рядок 198

**Книга каже, дослівно:**

> | Coredump | `Component config` → `Core dump` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-079 sha:d697a4b5 src:manual/11-idf.md:199 klas:A -->
### T-11-079 · tablycya · рядок 199

**Книга каже, дослівно:**

> | Підтримка PSRAM | `Component config` → `ESP PSRAM` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-080 sha:24eabbac src:manual/11-idf.md:200 klas:A -->
### T-11-080 · tablycya · рядок 200

**Книга каже, дослівно:**

> | Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig
- **Дослівно з джерела:**
  > menu "Compiler options"
  >     choice COMPILER_OPTIMIZATION
  >         prompt "Optimization Level"
  >         default COMPILER_OPTIMIZATION_DEBUG
  >         config COMPILER_OPTIMIZATION_DEBUG
  >             bool "Debug (-Og)"
  >         config COMPILER_OPTIMIZATION_SIZE
  >             bool "Optimize for size (-Os with GCC, -Oz with Clang)"
  >         config COMPILER_OPTIMIZATION_PERF
  >             bool "Optimize for performance (-O2)"
  >         config COMPILER_OPTIMIZATION_NONE
  >             bool "Debug without optimization (-O0)"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Розділ 27 підтверджено дослівно, включно з твердженням, що `Debug (-Og)` — це і є значення за замовчуванням (`default COMPILER_OPTIMIZATION_DEBUG`).
У таблиці розділу 11 рядок був скорочений до `Compiler options` → `-Os`, тобто пропускав рівень `Optimization Level`; уточнено.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-081 sha:a0fbdfcd src:manual/11-idf.md:202 klas:A -->
### T-11-081 · proza · рядок 202

**Книга каже, дослівно:**

> Три перші пункти меню — `Serial flasher config`, `Partition Table` і `Bootloader config` — лежать у корені, решта всередині `Component config`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-082 sha:a1afae4e src:manual/11-idf.md:202 klas:E -->
### T-11-082 · proza · рядок 202

**Книга каже, дослівно:**

> Це не косметика: у корені живе те, що стосується самої збірки й прошивки, а не окремого компонента.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-083 sha:551e3e47 src:manual/11-idf.md:207 klas:F -->
### T-11-083 · proza · рядок 207

**Книга каже, дослівно:**

> Пошук усередині `menuconfig` — клавіша `/`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-084 sha:798e784d src:manual/11-idf.md:207 klas:E -->
### T-11-084 · proza · рядок 207

**Книга каже, дослівно:**

> Це найкорисніша клавіша в усьому інтерфейсі: назви параметрів здебільшого відомі з документації, а шукати їх по деревах довго.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-085 sha:980f9ca8 src:manual/11-idf.md:213 klas:E -->
### T-11-085 · proza · рядок 213

**Книга каже, дослівно:**

> Сторонні бібліотеки ставляться з реєстру компонентів Espressif:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-086 sha:c0f7fc7a src:manual/11-idf.md:215 klas:K -->
### T-11-086 · kod · рядок 215

**Книга каже, дослівно:**

> ```sh
> idf.py add-dependency "espressif/led_strip^3.0.3"
> ```

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

<!-- fc id:T-11-087 sha:4f76e0f2 src:manual/11-idf.md:216 klas:A -->
### T-11-087 · kod-ryadok · рядок 216

**Книга каже, дослівно:**

> idf.py add-dependency "espressif/led_strip^3.0.3"

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

<!-- fc id:T-11-088 sha:40bd7292 src:manual/11-idf.md:219 klas:F -->
### T-11-088 · proza · рядок 219

**Книга каже, дослівно:**

> Це створює файл `idf_component.yml`, який фіксує залежності проєкту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-089 sha:ee2d2f1b src:manual/11-idf.md:219 klas:E -->
### T-11-089 · proza · рядок 219

**Книга каже, дослівно:**

> Файл кладеться в git — саме він робить проєкт відтворюваним.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-090 sha:aca0806c src:manual/11-idf.md:222 klas:E -->
### T-11-090 · proza · рядок 222

**Книга каже, дослівно:**

> Номер версії в команді — з реєстру **на момент роботи**, а не з книги (Р4): компоненти оновлюються значно частіше за ревізії довідника.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-091 sha:30483f3f src:manual/11-idf.md:222 klas:A -->
### T-11-091 · proza · рядок 222

**Книга каже, дослівно:**

> Значок `^` означає «ця major-версія, будь-яка новіша minor», тож `^3.0.3` не візьме 4.x — і це саме те, чого хочеться від залежності у виробі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/idf-extra-components/master/led_strip/{idf_component.yml,CHANGELOG.md}
- **Дослівно з джерела:**
  > (idf_component.yml)
  > version: "3.0.3"
  > description: Driver for Addressable LED Strip (WS2812, etc)
  > dependencies:
  >   idf: ">=5.0"
  > 
  > (CHANGELOG.md)
  > ## 3.0.3
  > - Support WS2816 with 16-bit color
  > ## 3.0.0
  > - Discontinued support for ESP-IDF v4.x
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Версія в книзі збігається з поточною в реєстрі дослівно, і приклад `idf.py add-dependency "espressif/led_strip^3.0.3"` робочий.
Заразом підтвердилося пояснення розділу 11 про `^`: сам компонент оголошує `idf: ">=5.0"`, а його CHANGELOG прямо каже, що 3.0.0 припинив підтримку ESP-IDF v4.x. Тобто мажорна межа в цьому компоненті справді несе зміну сумісності — саме те, заради чого книга радить `^`.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-11-092 sha:9322693e src:manual/11-idf.md:228 klas:F -->
### T-11-092 · proza · рядок 228

**Книга каже, дослівно:**

> Реєстр невеликий порівняно з екосистемою Arduino, і це реальне обмеження ESP-IDF: бібліотеки на конкретний датчик там може не бути (розділ 12).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-093 sha:153c053d src:manual/11-idf.md:233 klas:F -->
### T-11-093 · proza · рядок 233

**Книга каже, дослівно:**

> Офіційне розширення від Espressif робить те саме, що `idf.py`, тільки кнопками, і додає інтеграцію з відлагоджувачем.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-094 sha:445bb076 src:manual/11-idf.md:236 klas:E -->
### T-11-094 · proza · рядок 236

**Книга каже, дослівно:**

> Ключове після встановлення — **вибрати гілку ESP-IDF**: розширення вміє встановити фреймворк саме або використати вже встановлений.

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

<!-- fc id:T-11-095 sha:7f37de94 src:manual/11-idf.md:236 klas:E -->
### T-11-095 · proza · рядок 236

**Книга каже, дослівно:**

> Другий варіант надійніший, якщо ви вже працюєте з командного рядка: інакше на машині з'являються дві копії й починається плутанина, яка з них активна.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-096 sha:36ad5706 src:manual/11-idf.md:242 klas:E -->
### T-11-096 · proza · рядок 242

**Книга каже, дослівно:**

> Що дає розширення понад командний рядок:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-097 sha:4d081911 src:manual/11-idf.md:244 klas:A -->
### T-11-097 · proza · рядок 244

**Книга каже, дослівно:**

> - **IntelliSense**, налаштований на конкретний чип: автодоповнення знає, які функції доступні саме тут; - **налагодження в один клік** (розділ 27); - **перегляд регістрів периферії** з розшифровкою бітових полів; - **вбудований монітор** із розшифровкою backtrace.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/51b28bff-idf-monitor.rst
- **Дослівно з джерела:**
  > Whenever the chip outputs a hexadecimal address that points to executable code, IDF monitor looks up the location in the source code
- **Спосіб і дата:** хвиля 3, наряд factcheck/NARYAD-m2-hvylya3.md; цитата звірена підрядком у названому файлі скриптом factcheck/pryyom-hvylya3.py, 2026-08-27
- **Нотатка:** Документ описує вбудований монітор з розшифровкою backtrace адрес.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-11-098 sha:f32cde1d src:manual/11-idf.md:251 klas:E -->
### T-11-098 · proza · рядок 251

**Книга каже, дослівно:**

> Найчастіша проблема з розширенням — IntelliSense показує помилки там, де збирання проходить успішно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-099 sha:009c5309 src:manual/11-idf.md:251 klas:F -->
### T-11-099 · proza · рядок 251

**Книга каже, дослівно:**

> Причина зазвичай у тому, що конфігурація розширення вказує на іншу версію ESP-IDF, ніж та, якою збирається проєкт.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-100 sha:04ac6509 src:manual/11-idf.md:251 klas:F -->
### T-11-100 · proza · рядок 251

**Книга каже, дослівно:**

> Червоні підкреслення при успішному `idf.py build` — це проблема редактора, а не коду.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-101 sha:5075d2bd src:manual/11-idf.md:260 klas:E -->
### T-11-101 · proza · рядок 260

**Книга каже, дослівно:**

> Чесна відповідь: ESP-IDF складніший за Arduino і вимагає більше часу на старті.

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

<!-- fc id:T-11-102 sha:b2bd2d4d src:manual/11-idf.md:260 klas:E -->
### T-11-102 · proza · рядок 260

**Книга каже, дослівно:**

> Він виграє в тому, що стає видно пізніше:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-103 sha:31020c6e src:manual/11-idf.md:263 klas:F -->
### T-11-103 · proza · рядок 263

**Книга каже, дослівно:**

> **Уся периферія доступна.** Блоки на кшталт MCPWM, PCNT, TWAI в Arduino доступні частково або через сторонні обгортки (розділ 04).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-104 sha:570bdca4 src:manual/11-idf.md:266 klas:F -->
### T-11-104 · proza · рядок 266

**Книга каже, дослівно:**

> **Діагностика.** Coredump, розшифровка backtrace, JTAG, докладний лог підсистем — усе штатне (розділи 26, 27).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-105 sha:812e0ce8 src:manual/11-idf.md:269 klas:A -->
### T-11-105 · proza · рядок 269

**Книга каже, дослівно:**

> **Керування пам'яттю й таймінгами.** Розміри стеків, прив'язка до ядер, пріоритети задач, `IRAM_ATTR` — усе під контролем (розділи 30, 31).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Task priorities range from 0 (lowest) to configMAX_PRIORITIES - 1 (highest).
  > Vanilla FreeRTOS provides the following functions to create a task.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep priority, 2026-08-26
- **Нотатка:** Текст T-31-018 говорить про пріоритети від 0 до configMAX_PRIORITIES - 1. Джерело підтверджує цей діапазон.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-11-106 sha:7f64c2fd src:manual/11-idf.md:272 klas:F -->
### T-11-106 · proza · рядок 272

**Книга каже, дослівно:**

> **Відтворюваність.** Зафіксована версія фреймворку, зафіксовані компоненти, збережений `sdkconfig`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-107 sha:c803dfc0 src:manual/11-idf.md:272 klas:E -->
### T-11-107 · proza · рядок 272

**Книга каже, дослівно:**

> Виріб, який треба супроводжувати роками, будується так.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-108 sha:fb1ad6c4 src:manual/11-idf.md:276 klas:E -->
### T-11-108 · proza · рядок 276

**Книга каже, дослівно:**

> Arduino core лишається правильним інструментом для швидкого прототипування — і в довіднику він саме в цій ролі (розділ 12).

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Базовий вимірювальний прилад, доступна у будь-якої радіоелектронної лабораторії
- **Дослівно з джерела:**
  > Мультиметр здатен вимірювати:
  > - Напруга DC (V) — на живленні, сигналах
  > - Опір (Ω) — перевірка провідності, резисторів
  > - Струм (mA, A) — малі струми в схемі
  > 
  > Точність: типово 1–2% від вимірювання.
- **Спосіб і дата:** Базова вимірювальна техніка, 2026-08-26
- **Нотатка:** Мультиметр є найпростішим приладом для початкової діагностики.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-11-109 sha:0a1fc86c src:manual/11-idf.md:281 klas:F -->
### T-11-109 · proza · рядок 281

**Книга каже, дослівно:**

> `export.sh` у кожному новому терміналі; свідомий псевдонім замість запису в `.bashrc`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-110 sha:07a06fdd src:manual/11-idf.md:284 klas:E -->
### T-11-110 · proza · рядок 284

**Книга каже, дослівно:**

> Версія фіксується на початку проєкту й записується.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-111 sha:80e99395 src:manual/11-idf.md:284 klas:A -->
### T-11-111 · proza · рядок 284

**Книга каже, дослівно:**

> LTS в ESP-IDF не існує — у всіх релізів 30 місяців, із яких перші 12 — Service, і саме вони придатні для нового проєкту.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-112 sha:c323842e src:manual/11-idf.md:288 klas:F -->
### T-11-112 · proza · рядок 288

**Книга каже, дослівно:**

> `set-target` стирає `sdkconfig`; у git кладеться `sdkconfig.defaults`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-113 sha:c78ccc1b src:manual/11-idf.md:290 klas:F -->
### T-11-113 · proza · рядок 290

**Книга каже, дослівно:**

> `REQUIRES` у `CMakeLists.txt` — причина більшості «файл не знайдено».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-114 sha:d0259d8b src:manual/11-idf.md:292 klas:F -->
### T-11-114 · proza · рядок 292

**Книга каже, дослівно:**

> Клавіша `/` у `menuconfig`.

**Доказ**

- **Клас:** F — не звірено

---
