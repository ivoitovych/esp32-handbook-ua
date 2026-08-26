# Фактчекінг: `manual/18-rozdily-fleshu.md`

Одиниць твердження: **123**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-18-001 sha:81b76c44 src:manual/18-rozdily-fleshu.md:3 klas:F -->
### T-18-001 · proza · рядок 3

**Книга каже, дослівно:**

> Флеш ESP32 — не один суцільний шматок пам'яті, а набір областей із різним призначенням: бутлоадер, таблиця розділів, застосунок, сховище налаштувань, файлова система.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-002 sha:87d0e3e7 src:manual/18-rozdily-fleshu.md:3 klas:A -->
### T-18-002 · proza · рядок 3

**Книга каже, дослівно:**

> Хто де лежить, описано в **таблиці розділів** (partition table) за адресою `0x8000`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > For this reason a partition table is flashed to
  > (:ref:`default offset <CONFIG_PARTITION_TABLE_OFFSET>`) 0x8000 in the flash.
  > …
  > In both cases the factory app is flashed at offset 0x10000.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Вихідний .rst документації ESP-IDF — те, з чого зроблено docs.espressif.com, який із цього середовища не дістається.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-18-003 sha:ea68963b src:manual/18-rozdily-fleshu.md:8 klas:E -->
### T-18-003 · proza · рядок 8

**Книга каже, дослівно:**

> Це та частина системи, яку більшість не чіпає роками — рівно до дня, коли застосунок перестає вміщатися у відведений розділ або треба додати OTA.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-004 sha:9c606f2f src:manual/18-rozdily-fleshu.md:8 klas:E -->
### T-18-004 · proza · рядок 8

**Книга каже, дослівно:**

> Тоді виявляється, що змінити розбивку неважко, а зламати нею робочий пристрій — легко.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-005 sha:4a659ad6 src:manual/18-rozdily-fleshu.md:15 klas:E -->
### T-18-005 · proza · рядок 15

**Книга каже, дослівно:**

> Це список записів, кожен з яких каже: назва, тип, підтип, адреса початку, розмір.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-006 sha:4bb6abfa src:manual/18-rozdily-fleshu.md:15 klas:F -->
### T-18-006 · proza · рядок 15

**Книга каже, дослівно:**

> Бутлоадер читає цей список при кожному старті (розділ 16) і за ним знаходить застосунок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-007 sha:cc195a29 src:manual/18-rozdily-fleshu.md:19 klas:E -->
### T-18-007 · proza · рядок 19

**Книга каже, дослівно:**

> Типова розбивка для пристрою без OTA виглядає так:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-008 sha:f337b884 src:manual/18-rozdily-fleshu.md:21 klas:F -->
### T-18-008 · tablycya-shapka · рядок 21

**Книга каже, дослівно:**

> | Назва | Тип | Підтип | Зсув | Розмір |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-009 sha:606ac6dd src:manual/18-rozdily-fleshu.md:22 klas:F -->
### T-18-009 · komirka · рядок 22

**Книга каже, дослівно:**

> `nvs` · Тип → data

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-010 sha:f47ce163 src:manual/18-rozdily-fleshu.md:22 klas:F -->
### T-18-010 · komirka · рядок 22

**Книга каже, дослівно:**

> `nvs` · Підтип → nvs

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-011 sha:15620348 src:manual/18-rozdily-fleshu.md:22 klas:F -->
### T-18-011 · komirka · рядок 22

**Книга каже, дослівно:**

> `nvs` · Зсув → `0x9000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-012 sha:8f0dd715 src:manual/18-rozdily-fleshu.md:22 klas:F -->
### T-18-012 · komirka · рядок 22

**Книга каже, дослівно:**

> `nvs` · Розмір → `0x6000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-013 sha:5f9bc8f0 src:manual/18-rozdily-fleshu.md:23 klas:F -->
### T-18-013 · komirka · рядок 23

**Книга каже, дослівно:**

> `phy_init` · Тип → data

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-014 sha:789c88b9 src:manual/18-rozdily-fleshu.md:23 klas:F -->
### T-18-014 · komirka · рядок 23

**Книга каже, дослівно:**

> `phy_init` · Підтип → phy

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-015 sha:fc7a2431 src:manual/18-rozdily-fleshu.md:23 klas:A -->
### T-18-015 · komirka · рядок 23

**Книга каже, дослівно:**

> `phy_init` · Зсув → `0xF000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/partition_table/partitions_singleapp.csv та .../components/partition_table/gen_esp32part.py
- **Дослівно з джерела:**
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     ,        0x6000,
  > phy_init, data, phy,     ,        0x1000,
  > factory,  app,  factory, ,        1M,
  > 
  > (gen_esp32part.py)
  > ALIGNMENT = {
  >     APP_TYPE: 0x10000,
  >     DATA_TYPE: 0x1000,
  >     BOOTLOADER_TYPE: 0x1000,
  >     PARTITION_TABLE_TYPE: 0x1000,
  > }
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує таблицю розділу 18 повністю: `nvs` розміром `0x6000`, `phy_init` розміром `0x1000`, `factory` 1 МБ — і, головне, вирівнювання: розділи типу `app` на 64 КБ, типу `data` на 4 КБ. Саме ці два числа книга називає вимогою апаратного відображення пам'яті.
Окремо зафіксовано для наступних ревізій: у розбивці з OTA (`partitions_two_ota.csv`) `nvs` уже `0x4000`, і додається `otadata` розміром `0x2000`. Книга цієї розбивки таблицею не подає, тож розбіжності немає, але сума службових областей до `0x10000` сходиться саме так — і це підтверджує «близько 64 КБ» у розділі 19.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-18-016 sha:d76b708c src:manual/18-rozdily-fleshu.md:23 klas:F -->
### T-18-016 · komirka · рядок 23

**Книга каже, дослівно:**

> `phy_init` · Розмір → `0x1000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-017 sha:94bcae2e src:manual/18-rozdily-fleshu.md:24 klas:F -->
### T-18-017 · komirka · рядок 24

**Книга каже, дослівно:**

> `factory` · Тип → app

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-018 sha:98e8369f src:manual/18-rozdily-fleshu.md:24 klas:F -->
### T-18-018 · komirka · рядок 24

**Книга каже, дослівно:**

> `factory` · Підтип → factory

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-019 sha:9df43b5f src:manual/18-rozdily-fleshu.md:24 klas:A -->
### T-18-019 · komirka · рядок 24

**Книга каже, дослівно:**

> `factory` · Зсув → `0x10000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/partition_table/partitions_singleapp.csv та .../components/partition_table/gen_esp32part.py
- **Дослівно з джерела:**
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     ,        0x6000,
  > phy_init, data, phy,     ,        0x1000,
  > factory,  app,  factory, ,        1M,
  > 
  > (gen_esp32part.py)
  > ALIGNMENT = {
  >     APP_TYPE: 0x10000,
  >     DATA_TYPE: 0x1000,
  >     BOOTLOADER_TYPE: 0x1000,
  >     PARTITION_TABLE_TYPE: 0x1000,
  > }
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує таблицю розділу 18 повністю: `nvs` розміром `0x6000`, `phy_init` розміром `0x1000`, `factory` 1 МБ — і, головне, вирівнювання: розділи типу `app` на 64 КБ, типу `data` на 4 КБ. Саме ці два числа книга називає вимогою апаратного відображення пам'яті.
Окремо зафіксовано для наступних ревізій: у розбивці з OTA (`partitions_two_ota.csv`) `nvs` уже `0x4000`, і додається `otadata` розміром `0x2000`. Книга цієї розбивки таблицею не подає, тож розбіжності немає, але сума службових областей до `0x10000` сходиться саме так — і це підтверджує «близько 64 КБ» у розділі 19.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-18-020 sha:59fff70d src:manual/18-rozdily-fleshu.md:24 klas:A -->
### T-18-020 · komirka · рядок 24

**Книга каже, дослівно:**

> `factory` · Розмір → `0x100000`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/partition_table/partitions_singleapp.csv та .../components/partition_table/gen_esp32part.py
- **Дослівно з джерела:**
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     ,        0x6000,
  > phy_init, data, phy,     ,        0x1000,
  > factory,  app,  factory, ,        1M,
  > 
  > (gen_esp32part.py)
  > ALIGNMENT = {
  >     APP_TYPE: 0x10000,
  >     DATA_TYPE: 0x1000,
  >     BOOTLOADER_TYPE: 0x1000,
  >     PARTITION_TABLE_TYPE: 0x1000,
  > }
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує таблицю розділу 18 повністю: `nvs` розміром `0x6000`, `phy_init` розміром `0x1000`, `factory` 1 МБ — і, головне, вирівнювання: розділи типу `app` на 64 КБ, типу `data` на 4 КБ. Саме ці два числа книга називає вимогою апаратного відображення пам'яті.
Окремо зафіксовано для наступних ревізій: у розбивці з OTA (`partitions_two_ota.csv`) `nvs` уже `0x4000`, і додається `otadata` розміром `0x2000`. Книга цієї розбивки таблицею не подає, тож розбіжності немає, але сума службових областей до `0x10000` сходиться саме так — і це підтверджує «близько 64 КБ» у розділі 19.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-18-021 sha:0923797f src:manual/18-rozdily-fleshu.md:27 klas:E -->
### T-18-021 · proza · рядок 27

**Книга каже, дослівно:**

> Три речі, які варто прочитати з цієї таблиці одразу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-022 sha:50b4dd7d src:manual/18-rozdily-fleshu.md:29 klas:D -->
### T-18-022 · proza · рядок 29

**Книга каже, дослівно:**

> **Застосунок починається з `0x10000`** — це не випадкове число, а перша адреса після таблиці розділів і службових областей.

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
- **Дослівно з джерела:**
  > таблиця розділів  0x8000 + 0x1000 (сектор) = 0x9000  → перший розділ
  > nvs               0x9000 + 0x6000          = 0xF000
  > phy_init          0xF000 + 0x1000          = 0x10000 → застосунок
  > 0x10000 / 1024                             = 64 КБ
  > 
  > сектор 0x1000 / 1024 = 4 КБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Замикає ланцюжок, який книга досі подавала трьома окремими твердженнями в розділах 16, 18 і 19: чому таблиця розділів займає цілий сектор, чому наступний розділ не може починатися раніше ніж `0x9000`, і звідки береться «близько 64 КБ службових».
Тепер це один перерахунок із п'яти кроків, і кожен крок видимий. Розмір розділів узято з `partitions_singleapp.csv` ESP-IDF (прохід 7), тобто арифметика спирається на звірені числа, а не на самі себе.
Заразом видно, що «4 МБ мінус 64 КБ службових = 3.9 МБ» із розділу 18 — не округлення на око, а точний наслідок цієї ж розкладки.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-18-023 sha:6ad702cc src:manual/18-rozdily-fleshu.md:29 klas:F -->
### T-18-023 · proza · рядок 29

**Книга каже, дослівно:**

> Саме тому у всіх командах прошивки застосунок іде на `0x10000`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-024 sha:4eca33d4 src:manual/18-rozdily-fleshu.md:33 klas:F -->
### T-18-024 · proza · рядок 33

**Книга каже, дослівно:**

> **`nvs` лежить перед застосунком.** Це сховище пар «ключ — значення»: налаштування, збережені креденшели Wi-Fi, лічильники.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-025 sha:20700e13 src:manual/18-rozdily-fleshu.md:33 klas:F -->
### T-18-025 · proza · рядок 33

**Книга каже, дослівно:**

> Воно переживає оновлення прошивки — і саме тому `erase-flash` такий болючий.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-026 sha:ded12860 src:manual/18-rozdily-fleshu.md:37 klas:F -->
### T-18-026 · proza · рядок 37

**Книга каже, дослівно:**

> **`phy_init`** зберігає калібрувальні дані радіо.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-027 sha:76acd34b src:manual/18-rozdily-fleshu.md:37 klas:E -->
### T-18-027 · proza · рядок 37

**Книга каже, дослівно:**

> Маленький розділ, про який ніхто не думає, поки не зітре.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-028 sha:b16e6cfe src:manual/18-rozdily-fleshu.md:42 klas:F -->
### T-18-028 · proza · рядок 42

**Книга каже, дослівно:**

> Найдешевший спосіб — прочитати boot-лог: другий бутлоадер друкує всю таблицю з адресами при кожному старті (розділ 16).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-029 sha:f936f28f src:manual/18-rozdily-fleshu.md:42 klas:E -->
### T-18-029 · proza · рядок 42

**Книга каже, дослівно:**

> Нічого розбирати не треба.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-030 sha:12c0dae9 src:manual/18-rozdily-fleshu.md:46 klas:E -->
### T-18-030 · proza · рядок 46

**Книга каже, дослівно:**

> Якщо логу немає, таблицю можна зняти з флешу і розібрати:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-031 sha:2af2e0ef src:manual/18-rozdily-fleshu.md:48 klas:K -->
### T-18-031 · kod · рядок 48

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 read-flash 0x8000 0x1000 pt.bin
> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
> ```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
- **Дослівно з джерела:**
  > таблиця розділів  0x8000 + 0x1000 (сектор) = 0x9000  → перший розділ
  > nvs               0x9000 + 0x6000          = 0xF000
  > phy_init          0xF000 + 0x1000          = 0x10000 → застосунок
  > 0x10000 / 1024                             = 64 КБ
  > 
  > сектор 0x1000 / 1024 = 4 КБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Замикає ланцюжок, який книга досі подавала трьома окремими твердженнями в розділах 16, 18 і 19: чому таблиця розділів займає цілий сектор, чому наступний розділ не може починатися раніше ніж `0x9000`, і звідки береться «близько 64 КБ службових».
Тепер це один перерахунок із п'яти кроків, і кожен крок видимий. Розмір розділів узято з `partitions_singleapp.csv` ESP-IDF (прохід 7), тобто арифметика спирається на звірені числа, а не на самі себе.
Заразом видно, що «4 МБ мінус 64 КБ службових = 3.9 МБ» із розділу 18 — не округлення на око, а точний наслідок цієї ж розкладки.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-18-032 sha:5793a2bb src:manual/18-rozdily-fleshu.md:49 klas:D -->
### T-18-032 · kod-ryadok · рядок 49

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 read-flash 0x8000 0x1000 pt.bin

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
- **Дослівно з джерела:**
  > таблиця розділів  0x8000 + 0x1000 (сектор) = 0x9000  → перший розділ
  > nvs               0x9000 + 0x6000          = 0xF000
  > phy_init          0xF000 + 0x1000          = 0x10000 → застосунок
  > 0x10000 / 1024                             = 64 КБ
  > 
  > сектор 0x1000 / 1024 = 4 КБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Замикає ланцюжок, який книга досі подавала трьома окремими твердженнями в розділах 16, 18 і 19: чому таблиця розділів займає цілий сектор, чому наступний розділ не може починатися раніше ніж `0x9000`, і звідки береться «близько 64 КБ службових».
Тепер це один перерахунок із п'яти кроків, і кожен крок видимий. Розмір розділів узято з `partitions_singleapp.csv` ESP-IDF (прохід 7), тобто арифметика спирається на звірені числа, а не на самі себе.
Заразом видно, що «4 МБ мінус 64 КБ службових = 3.9 МБ» із розділу 18 — не округлення на око, а точний наслідок цієї ж розкладки.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-18-033 sha:4438754b src:manual/18-rozdily-fleshu.md:50 klas:F -->
### T-18-033 · kod-ryadok · рядок 50

**Книга каже, дослівно:**

> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-034 sha:9c3fadfd src:manual/18-rozdily-fleshu.md:53 klas:E -->
### T-18-034 · proza · рядок 53

**Книга каже, дослівно:**

> Другий рядок друкує таблицю в тому самому CSV-форматі, у якому її пишуть.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-035 sha:170e004e src:manual/18-rozdily-fleshu.md:53 klas:F -->
### T-18-035 · proza · рядок 53

**Книга каже, дослівно:**

> Це один із перших кроків форензики чужої прошивки — розділ 24.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-036 sha:efe25d4b src:manual/18-rozdily-fleshu.md:58 klas:E -->
### T-18-036 · proza · рядок 58

**Книга каже, дослівно:**

> У проєкті ESP-IDF розбивка задається текстовим файлом:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-037 sha:8348b7b2 src:manual/18-rozdily-fleshu.md:60 klas:K -->
### T-18-037 · kod · рядок 60

**Книга каже, дослівно:**

> ```
> # Name,   Type, SubType, Offset,   Size,   Flags
> nvs,      data, nvs,     0x9000,   0x6000,
> phy_init, data, phy,     0xF000,   0x1000,
> factory,  app,  factory, 0x10000,  1M,
> storage,  data, spiffs,  ,         1M,
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/partition_table/partitions_singleapp.csv та .../components/partition_table/gen_esp32part.py
- **Дослівно з джерела:**
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     ,        0x6000,
  > phy_init, data, phy,     ,        0x1000,
  > factory,  app,  factory, ,        1M,
  > 
  > (gen_esp32part.py)
  > ALIGNMENT = {
  >     APP_TYPE: 0x10000,
  >     DATA_TYPE: 0x1000,
  >     BOOTLOADER_TYPE: 0x1000,
  >     PARTITION_TABLE_TYPE: 0x1000,
  > }
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує таблицю розділу 18 повністю: `nvs` розміром `0x6000`, `phy_init` розміром `0x1000`, `factory` 1 МБ — і, головне, вирівнювання: розділи типу `app` на 64 КБ, типу `data` на 4 КБ. Саме ці два числа книга називає вимогою апаратного відображення пам'яті.
Окремо зафіксовано для наступних ревізій: у розбивці з OTA (`partitions_two_ota.csv`) `nvs` уже `0x4000`, і додається `otadata` розміром `0x2000`. Книга цієї розбивки таблицею не подає, тож розбіжності немає, але сума службових областей до `0x10000` сходиться саме так — і це підтверджує «близько 64 КБ» у розділі 19.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-18-038 sha:40c8d5dd src:manual/18-rozdily-fleshu.md:68 klas:F -->
### T-18-038 · proza · рядок 68

**Книга каже, дослівно:**

> Порожній `Offset` означає «одразу після попереднього» — так і треба робити: явні адреси в кожному рядку легко розсинхронізувати при першій же зміні розміру.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-039 sha:d9cb149f src:manual/18-rozdily-fleshu.md:72 klas:F -->
### T-18-039 · proza · рядок 72

**Книга каже, дослівно:**

> Розмір записується числом (`0x100000`), або з суфіксом (`1M`, `512K`).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-040 sha:d8851079 src:manual/18-rozdily-fleshu.md:75 klas:A -->
### T-18-040 · proza · рядок 75

**Книга каже, дослівно:**

> **Розділи типу `app` мають бути вирівняні на `0x10000` (64 КБ).** Це вимога апаратного відображення пам'яті, а не примха.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/partition_table/partitions_singleapp.csv та .../components/partition_table/gen_esp32part.py
- **Дослівно з джерела:**
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     ,        0x6000,
  > phy_init, data, phy,     ,        0x1000,
  > factory,  app,  factory, ,        1M,
  > 
  > (gen_esp32part.py)
  > ALIGNMENT = {
  >     APP_TYPE: 0x10000,
  >     DATA_TYPE: 0x1000,
  >     BOOTLOADER_TYPE: 0x1000,
  >     PARTITION_TABLE_TYPE: 0x1000,
  > }
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує таблицю розділу 18 повністю: `nvs` розміром `0x6000`, `phy_init` розміром `0x1000`, `factory` 1 МБ — і, головне, вирівнювання: розділи типу `app` на 64 КБ, типу `data` на 4 КБ. Саме ці два числа книга називає вимогою апаратного відображення пам'яті.
Окремо зафіксовано для наступних ревізій: у розбивці з OTA (`partitions_two_ota.csv`) `nvs` уже `0x4000`, і додається `otadata` розміром `0x2000`. Книга цієї розбивки таблицею не подає, тож розбіжності немає, але сума службових областей до `0x10000` сходиться саме так — і це підтверджує «близько 64 КБ» у розділі 19.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-18-041 sha:2cfd4562 src:manual/18-rozdily-fleshu.md:75 klas:A -->
### T-18-041 · proza · рядок 75

**Книга каже, дослівно:**

> Розділи типу `data` вирівнюються на `0x1000` (4 КБ).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/partition_table/partitions_singleapp.csv та .../components/partition_table/gen_esp32part.py
- **Дослівно з джерела:**
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     ,        0x6000,
  > phy_init, data, phy,     ,        0x1000,
  > factory,  app,  factory, ,        1M,
  > 
  > (gen_esp32part.py)
  > ALIGNMENT = {
  >     APP_TYPE: 0x10000,
  >     DATA_TYPE: 0x1000,
  >     BOOTLOADER_TYPE: 0x1000,
  >     PARTITION_TABLE_TYPE: 0x1000,
  > }
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує таблицю розділу 18 повністю: `nvs` розміром `0x6000`, `phy_init` розміром `0x1000`, `factory` 1 МБ — і, головне, вирівнювання: розділи типу `app` на 64 КБ, типу `data` на 4 КБ. Саме ці два числа книга називає вимогою апаратного відображення пам'яті.
Окремо зафіксовано для наступних ревізій: у розбивці з OTA (`partitions_two_ota.csv`) `nvs` уже `0x4000`, і додається `otadata` розміром `0x2000`. Книга цієї розбивки таблицею не подає, тож розбіжності немає, але сума службових областей до `0x10000` сходиться саме так — і це підтверджує «близько 64 КБ» у розділі 19.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-18-042 sha:14b13bf4 src:manual/18-rozdily-fleshu.md:75 klas:E -->
### T-18-042 · proza · рядок 75

**Книга каже, дослівно:**

> Якщо збирання скаржиться на вирівнювання — справа в цьому.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-043 sha:801f2aae src:manual/18-rozdily-fleshu.md:81 klas:A -->
### T-18-043 · proza · рядок 81

**Книга каже, дослівно:**

> Вибір готової розбивки замість власної — `idf.py menuconfig`, розділ `Partition Table`.

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

<!-- fc id:T-18-044 sha:16a9ef2e src:manual/18-rozdily-fleshu.md:81 klas:F -->
### T-18-044 · proza · рядок 81

**Книга каже, дослівно:**

> Там є типові варіанти: одна `factory`, дві OTA-області, варіанти під різні обсяги флешу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-045 sha:d288675c src:manual/18-rozdily-fleshu.md:81 klas:E -->
### T-18-045 · proza · рядок 81

**Книга каже, дослівно:**

> Для більшості задач власний CSV не потрібен.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-046 sha:25ea8296 src:manual/18-rozdily-fleshu.md:88 klas:E -->
### T-18-046 · proza · рядок 88

**Книга каже, дослівно:**

> NVS (Non-Volatile Storage) — сховище пар «ключ — значення», розкладене по просторах імен.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-047 sha:52530cd3 src:manual/18-rozdily-fleshu.md:88 klas:E -->
### T-18-047 · proza · рядок 88

**Книга каже, дослівно:**

> Саме тут має лежати все, що конкретне для **цього екземпляра** пристрою: серійний номер, калібрувальні коефіцієнти, адреса сервера, креденшели.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-048 sha:4935de88 src:manual/18-rozdily-fleshu.md:93 klas:E -->
### T-18-048 · proza · рядок 93

**Книга каже, дослівно:**

> Чому саме тут, а не в коді: значення в NVS переживає оновлення прошивки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-049 sha:d7ea3d3a src:manual/18-rozdily-fleshu.md:93 klas:F -->
### T-18-049 · proza · рядок 93

**Книга каже, дослівно:**

> Один образ можна залити на сто плат, а різне для кожної записати в NVS окремо — основа серійного виробництва (розділ 21).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-050 sha:77e191f6 src:manual/18-rozdily-fleshu.md:97 klas:E -->
### T-18-050 · proza · рядок 97

**Книга каже, дослівно:**

> NVS стійкий до зникнення живлення: запис влаштований так, що обірвана операція не псує вже записане.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-051 sha:9eef63be src:manual/18-rozdily-fleshu.md:97 klas:A -->
### T-18-051 · proza · рядок 97

**Книга каже, дослівно:**

> Це не означає, що він незнищенний — переповнений або пошкоджений NVS призводить до помилок при старті, і в логу це видно явно (`nvs_flash_init failed`).

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

<!-- fc id:T-18-052 sha:7d517b9b src:manual/18-rozdily-fleshu.md:102 klas:E -->
### T-18-052 · proza · рядок 102

**Книга каже, дослівно:**

> Стандартна реакція на пошкоджений NVS — стерти і переініціалізувати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-053 sha:4b78fd12 src:manual/18-rozdily-fleshu.md:102 klas:E -->
### T-18-053 · proza · рядок 102

**Книга каже, дослівно:**

> Це робиться з коду, і це нормальна практика:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-054 sha:bdb800c3 src:manual/18-rozdily-fleshu.md:105 klas:K -->
### T-18-054 · kod · рядок 105

**Книга каже, дослівно:**

> ```c
> esp_err_t err = nvs_flash_init();
> if (err == ESP_ERR_NVS_NO_FREE_PAGES ||
>     err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
>     ESP_ERROR_CHECK(nvs_flash_erase());
>     err = nvs_flash_init();
> }
> ESP_ERROR_CHECK(err);
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

<!-- fc id:T-18-055 sha:f3349b99 src:manual/18-rozdily-fleshu.md:109 klas:A -->
### T-18-055 · kod-ryadok · рядок 109

**Книга каже, дослівно:**

> ESP_ERROR_CHECK(nvs_flash_erase());

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

<!-- fc id:T-18-056 sha:601ab80f src:manual/18-rozdily-fleshu.md:112 klas:F -->
### T-18-056 · kod-ryadok · рядок 112

**Книга каже, дослівно:**

> ESP_ERROR_CHECK(err);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-057 sha:201bdc14 src:manual/18-rozdily-fleshu.md:116 klas:A -->
### T-18-057 · proza · рядок 116

**Книга каже, дослівно:**

> `nvs_flash_erase()` знищує всі налаштування пристрою.

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

<!-- fc id:T-18-058 sha:e101ea2e src:manual/18-rozdily-fleshu.md:116 klas:E -->
### T-18-058 · proza · рядок 116

**Книга каже, дослівно:**

> У прошивці, що йде в поле, цей код спрацює саме тоді, коли NVS переповнився — тобто несподівано, у роботі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-059 sha:92317196 src:manual/18-rozdily-fleshu.md:116 klas:F -->
### T-18-059 · proza · рядок 116

**Книга каже, дослівно:**

> Якщо серед налаштувань є те, чого не відновити (серійний номер, калібрування), його місце не в звичайному NVS, а в окремому розділі `data` тільки для читання, або в eFuse.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-060 sha:b3d9bf8d src:manual/18-rozdily-fleshu.md:125 klas:F -->
### T-18-060 · proza · рядок 125

**Книга каже, дослівно:**

> Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна файлова система в окремому розділі `data`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-061 sha:5b298442 src:manual/18-rozdily-fleshu.md:128 klas:F -->
### T-18-061 · tablycya-shapka · рядок 128

**Книга каже, дослівно:**

> | | LittleFS | SPIFFS | FAT |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-062 sha:e168a5c0 src:manual/18-rozdily-fleshu.md:129 klas:F -->
### T-18-062 · komirka · рядок 129

**Книга каже, дослівно:**

> Стійкість до зникнення живлення · LittleFS → так, за задумом

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-063 sha:34872fc8 src:manual/18-rozdily-fleshu.md:129 klas:F -->
### T-18-063 · komirka · рядок 129

**Книга каже, дослівно:**

> Стійкість до зникнення живлення · SPIFFS → ні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-064 sha:136b11ff src:manual/18-rozdily-fleshu.md:129 klas:F -->
### T-18-064 · komirka · рядок 129

**Книга каже, дослівно:**

> Стійкість до зникнення живлення · FAT → ні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-065 sha:e9f3c2f3 src:manual/18-rozdily-fleshu.md:130 klas:F -->
### T-18-065 · komirka · рядок 130

**Книга каже, дослівно:**

> Каталоги · LittleFS → так

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-066 sha:bd591c14 src:manual/18-rozdily-fleshu.md:130 klas:F -->
### T-18-066 · komirka · рядок 130

**Книга каже, дослівно:**

> Каталоги · SPIFFS → ні, плоский простір

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-067 sha:27ed2cb4 src:manual/18-rozdily-fleshu.md:130 klas:F -->
### T-18-067 · komirka · рядок 130

**Книга каже, дослівно:**

> Каталоги · FAT → так

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-068 sha:7c5fc24e src:manual/18-rozdily-fleshu.md:131 klas:F -->
### T-18-068 · komirka · рядок 131

**Книга каже, дослівно:**

> Знос флешу · LittleFS → вирівнюється власним механізмом

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-069 sha:8b7abf4b src:manual/18-rozdily-fleshu.md:131 klas:F -->
### T-18-069 · komirka · рядок 131

**Книга каже, дослівно:**

> Знос флешу · SPIFFS → вирівнюється власним механізмом

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-070 sha:6a505c3a src:manual/18-rozdily-fleshu.md:131 klas:F -->
### T-18-070 · komirka · рядок 131

**Книга каже, дослівно:**

> Знос флешу · FAT → лише через окремий шар `wear_levelling`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-071 sha:7a364c66 src:manual/18-rozdily-fleshu.md:132 klas:F -->
### T-18-071 · komirka · рядок 132

**Книга каже, дослівно:**

> Швидкість при заповненні · LittleFS → не деградує

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-072 sha:34b80b5e src:manual/18-rozdily-fleshu.md:132 klas:F -->
### T-18-072 · komirka · рядок 132

**Книга каже, дослівно:**

> Швидкість при заповненні · SPIFFS → різко падає

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-073 sha:3764ddb1 src:manual/18-rozdily-fleshu.md:132 klas:F -->
### T-18-073 · komirka · рядок 132

**Книга каже, дослівно:**

> Швидкість при заповненні · FAT → рівна

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-074 sha:c0ee355e src:manual/18-rozdily-fleshu.md:133 klas:F -->
### T-18-074 · komirka · рядок 133

**Книга каже, дослівно:**

> Сумісність із ПК · LittleFS → ні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-075 sha:2d821c96 src:manual/18-rozdily-fleshu.md:133 klas:F -->
### T-18-075 · komirka · рядок 133

**Книга каже, дослівно:**

> Сумісність із ПК · SPIFFS → ні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-076 sha:97b8e259 src:manual/18-rozdily-fleshu.md:133 klas:F -->
### T-18-076 · komirka · рядок 133

**Книга каже, дослівно:**

> Сумісність із ПК · FAT → так

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-077 sha:ad08a567 src:manual/18-rozdily-fleshu.md:134 klas:F -->
### T-18-077 · komirka · рядок 134

**Книга каже, дослівно:**

> У складі ESP-IDF · LittleFS → **ні**, окремий компонент

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-078 sha:0c51c182 src:manual/18-rozdily-fleshu.md:134 klas:F -->
### T-18-078 · komirka · рядок 134

**Книга каже, дослівно:**

> У складі ESP-IDF · SPIFFS → так

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-079 sha:d37a8a60 src:manual/18-rozdily-fleshu.md:134 klas:F -->
### T-18-079 · komirka · рядок 134

**Книга каже, дослівно:**

> У складі ESP-IDF · FAT → так

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-080 sha:b5482ecd src:manual/18-rozdily-fleshu.md:137 klas:E -->
### T-18-080 · proza · рядок 137

**Книга каже, дослівно:**

> **Практичний висновок простий: беріть LittleFS.** SPIFFS вважається застарілим, не має каталогів і починає гальмувати, коли розділ заповнюється більш ніж наполовину.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-081 sha:c6ab43f6 src:manual/18-rozdily-fleshu.md:137 klas:E -->
### T-18-081 · proza · рядок 137

**Книга каже, дослівно:**

> Його розумно лишати тільки в чужому проєкті, який уже на ньому працює.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-082 sha:009fe204 src:manual/18-rozdily-fleshu.md:143 klas:F -->
### T-18-082 · proza · рядок 143

**Книга каже, дослівно:**

> Останній рядок таблиці — це те, на чому спотикаються, шукаючи LittleFS у `menuconfig`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-083 sha:784039ff src:manual/18-rozdily-fleshu.md:143 klas:E -->
### T-18-083 · proza · рядок 143

**Книга каже, дослівно:**

> Його там немає: на відміну від SPIFFS і FAT, LittleFS **не входить до ESP-IDF** і ставиться з реєстру компонентів:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-084 sha:8278d069 src:manual/18-rozdily-fleshu.md:147 klas:K -->
### T-18-084 · kod · рядок 147

**Книга каже, дослівно:**

> ```sh
> idf.py add-dependency "joltwallet/littlefs^1.22.3"
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

<!-- fc id:T-18-085 sha:2568a317 src:manual/18-rozdily-fleshu.md:148 klas:A -->
### T-18-085 · kod-ryadok · рядок 148

**Книга каже, дослівно:**

> idf.py add-dependency "joltwallet/littlefs^1.22.3"

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

<!-- fc id:T-18-086 sha:706a6f2e src:manual/18-rozdily-fleshu.md:151 klas:F -->
### T-18-086 · proza · рядок 151

**Книга каже, дослівно:**

> Після цього розділ у меню з'являється, а тип розділу в CSV пишеться як `littlefs`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-087 sha:bb45cfb1 src:manual/18-rozdily-fleshu.md:151 klas:E -->
### T-18-087 · proza · рядок 151

**Книга каже, дослівно:**

> Номер версії — з реєстру на момент роботи, він змінюється частіше за саму книгу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-088 sha:62ee5911 src:manual/18-rozdily-fleshu.md:156 klas:E -->
### T-18-088 · proza · рядок 156

**Книга каже, дослівно:**

> FAT має сенс в одному випадку: коли той самий носій (найчастіше картку microSD) читатиме звичайний комп'ютер.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-089 sha:2dd189cd src:manual/18-rozdily-fleshu.md:156 klas:F -->
### T-18-089 · proza · рядок 156

**Книга каже, дослівно:**

> На вбудованому флеші FAT сама по собі не вирівнює знос — за це відповідає окремий шар `wear_levelling`, який ESP-IDF підставляє під неї (`esp_vfs_fat_spiflash_mount_rw_wl`).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-090 sha:3408b516 src:manual/18-rozdily-fleshu.md:156 klas:E -->
### T-18-090 · proza · рядок 156

**Книга каже, дослівно:**

> Працює це чесно, але шар не безкоштовний ні за місцем, ні за швидкістю, а стійкості до зникнення живлення не додає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-091 sha:fdd40a10 src:manual/18-rozdily-fleshu.md:156 klas:F -->
### T-18-091 · proza · рядок 156

**Книга каже, дослівно:**

> На картці — інша розмова (розділ 49).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-092 sha:38b96c9d src:manual/18-rozdily-fleshu.md:165 klas:E -->
### T-18-092 · proza · рядок 165

**Книга каже, дослівно:**

> Жодна файлова система на вбудованому флеші не переживе зникнення живлення **посеред запису** так, щоб гарантовано зберегти останній записаний файл.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-093 sha:0e9d20cb src:manual/18-rozdily-fleshu.md:165 klas:E -->
### T-18-093 · proza · рядок 165

**Книга каже, дослівно:**

> LittleFS гарантує, що ФС лишиться цілою і попередні дані доступні, — це не те саме, що «нічого не втрачено».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-094 sha:b760318d src:manual/18-rozdily-fleshu.md:165 klas:F -->
### T-18-094 · proza · рядок 165

**Книга каже, дослівно:**

> Для логера, який пише постійно, це проєктне обмеження, а не деталь (розділ 60).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-095 sha:f48a238f src:manual/18-rozdily-fleshu.md:174 klas:E -->
### T-18-095 · proza · рядок 174

**Книга каже, дослівно:**

> Найчастіша причина міняти розбивку — застосунок переріс розділ.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-096 sha:231194c9 src:manual/18-rozdily-fleshu.md:174 klas:E -->
### T-18-096 · proza · рядок 174

**Книга каже, дослівно:**

> Помилка при збиранні виглядає прямо:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-097 sha:7ab66916 src:manual/18-rozdily-fleshu.md:177 klas:K -->
### T-18-097 · kod · рядок 177

**Книга каже, дослівно:**

> ```
> Error: app partition is too small for binary app.bin size 0x123456
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-098 sha:bc634816 src:manual/18-rozdily-fleshu.md:181 klas:E -->
### T-18-098 · proza · рядок 181

**Книга каже, дослівно:**

> Варіанти дій, у порядку від найдешевшого:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-099 sha:a7b51adc src:manual/18-rozdily-fleshu.md:183 klas:F -->
### T-18-099 · proza · рядок 183

**Книга каже, дослівно:**

> **Прибрати зайве з прошивки.** Рівень логування, невикористані компоненти, оптимізація за розміром (`-Os`) у `menuconfig`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-100 sha:473a8f0b src:manual/18-rozdily-fleshu.md:183 klas:F -->
### T-18-100 · proza · рядок 183

**Книга каже, дослівно:**

> `idf.py size` показує, хто саме займає місце. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-101 sha:d95fc6fa src:manual/18-rozdily-fleshu.md:183 klas:F -->
### T-18-101 · proza · рядок 183

**Книга каже, дослівно:**

> **Взяти готову розбивку з більшим розділом застосунку** для вашого обсягу флешу. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-102 sha:6364cfd3 src:manual/18-rozdily-fleshu.md:183 klas:E -->
### T-18-102 · proza · рядок 183

**Книга каже, дослівно:**

> **Написати власний CSV.**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-103 sha:85fee83d src:manual/18-rozdily-fleshu.md:191 klas:E -->
### T-18-103 · proza · рядок 191

**Книга каже, дослівно:**

> **Зміна розбивки несумісна з OTA-оновленням.** Пристрій у полі отримує через OTA лише новий образ застосунку — таблиця розділів при цьому не оновлюється.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-104 sha:18b9a9fd src:manual/18-rozdily-fleshu.md:191 klas:E -->
### T-18-104 · proza · рядок 191

**Книга каже, дослівно:**

> Якщо нова прошивка розрахована на іншу розбивку, вона або не влізе, або запишеться поверх чужих даних.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-105 sha:9eebc20f src:manual/18-rozdily-fleshu.md:196 klas:E -->
### T-18-105 · proza · рядок 196

**Книга каже, дослівно:**

> Практично це означає: **розбивку треба обирати з запасом на самому початку**, до того, як перший пристрій поїхав до замовника.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-106 sha:e6335668 src:manual/18-rozdily-fleshu.md:196 klas:E -->
### T-18-106 · proza · рядок 196

**Книга каже, дослівно:**

> Змінити її потім можна лише з фізичним доступом і повною перепрошивкою — а це поїздка до кожного пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-107 sha:40d6c1dc src:manual/18-rozdily-fleshu.md:202 klas:E -->
### T-18-107 · proza · рядок 202

**Книга каже, дослівно:**

> Другий наслідок того самого: якщо ви змінили розбивку, а на платі лишився старий NVS зі старої розбивки за іншою адресою — застосунок побачить сміття.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-108 sha:9b05e136 src:manual/18-rozdily-fleshu.md:202 klas:F -->
### T-18-108 · proza · рядок 202

**Книга каже, дослівно:**

> Після зміни розбивки повна прошивка робиться з попереднім `erase-flash` (і, звісно, з дампом до нього — картка [К2](#k-stan)).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-109 sha:56304439 src:manual/18-rozdily-fleshu.md:209 klas:F -->
### T-18-109 · proza · рядок 209

**Книга каже, дослівно:**

> Орієнтири для типового пристрою на 4 МБ флешу:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-110 sha:863a7fb3 src:manual/18-rozdily-fleshu.md:211 klas:D -->
### T-18-110 · proza · рядок 211

**Книга каже, дослівно:**

> - `nvs` — `0x6000` (24 КБ) вистачає, поки ви не складаєте туди масиви.

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

<!-- fc id:T-18-111 sha:32ebab82 src:manual/18-rozdily-fleshu.md:211 klas:F -->
### T-18-111 · proza · рядок 211

**Книга каже, дослівно:**

> - Застосунок з Wi-Fi і TLS — від 1 МБ.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-112 sha:52f12d51 src:manual/18-rozdily-fleshu.md:211 klas:D -->
### T-18-112 · proza · рядок 211

**Книга каже, дослівно:**

> - Дві OTA-області означають **подвоєння** місця під застосунок: два по 1.5 МБ — це 3 МБ із приблизно 3.9 МБ, доступних після службових областей.

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

<!-- fc id:T-18-113 sha:5b4060f0 src:manual/18-rozdily-fleshu.md:211 klas:E -->
### T-18-113 · proza · рядок 211

**Книга каже, дослівно:**

> На все інше лишається менш ніж мегабайт.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-114 sha:b8548325 src:manual/18-rozdily-fleshu.md:211 klas:E -->
### T-18-114 · proza · рядок 211

**Книга каже, дослівно:**

> - Файлова система — те, що лишилося.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-115 sha:535138f3 src:manual/18-rozdily-fleshu.md:219 klas:F -->
### T-18-115 · proza · рядок 219

**Книга каже, дослівно:**

> Плати з 4 МБ флешу — стандарт і найдешевші, і для більшості задач їх вистачає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-116 sha:255c3b69 src:manual/18-rozdily-fleshu.md:219 klas:F -->
### T-18-116 · proza · рядок 219

**Книга каже, дослівно:**

> Але як тільки в задачі з'являється OTA **разом із** веб-інтерфейсом або великими ресурсами, 4 МБ стають тісними.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-117 sha:e612ab0d src:manual/18-rozdily-fleshu.md:219 klas:F -->
### T-18-117 · proza · рядок 219

**Книга каже, дослівно:**

> Модулі на 8 і 16 МБ коштують відчутно дорожче за різницю в ціні флешу — а от переробляти виріб під інший модуль на пізньому етапі дорожче в рази.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-118 sha:a369ddd0 src:manual/18-rozdily-fleshu.md:219 klas:E -->
### T-18-118 · proza · рядок 219

**Книга каже, дослівно:**

> Це та економія, яку варто рахувати на початку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-119 sha:11073fc5 src:manual/18-rozdily-fleshu.md:229 klas:F -->
### T-18-119 · proza · рядок 229

**Книга каже, дослівно:**

> Таблиця розділів лежить на `0x8000` і друкується в boot-лозі при кожному старті — найдешевший спосіб дізнатися, що всередині чужого пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-120 sha:1a134448 src:manual/18-rozdily-fleshu.md:232 klas:E -->
### T-18-120 · proza · рядок 232

**Книга каже, дослівно:**

> NVS переживає оновлення прошивки, і саме тому там живе все, що конкретне для екземпляра.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-121 sha:c0b50278 src:manual/18-rozdily-fleshu.md:232 klas:F -->
### T-18-121 · proza · рядок 232

**Книга каже, дослівно:**

> І саме тому `erase-flash` без дампа незворотний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-122 sha:b3601380 src:manual/18-rozdily-fleshu.md:235 klas:E -->
### T-18-122 · proza · рядок 235

**Книга каже, дослівно:**

> LittleFS замість SPIFFS у будь-якому новому проєкті.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-123 sha:68676e42 src:manual/18-rozdily-fleshu.md:237 klas:E -->
### T-18-123 · proza · рядок 237

**Книга каже, дослівно:**

> Розбивку обирають один раз, на початку, з запасом: OTA її не оновлює, а зміна потім вимагає фізичного доступу до кожного пристрою.

**Доказ**

- **Клас:** F — не звірено

---
