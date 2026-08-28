# Фактчекінг: `manual/18-rozdily-fleshu.md`

Одиниць твердження: **125**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-18-001 sha:81b76c44 src:manual/18-rozdily-fleshu.md:3 klas:A -->
### T-18-001 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Флеш ESP32 — не один суцільний шматок пам'яті, а набір областей із різним призначенням: бутлоадер, таблиця розділів, застосунок, сховище налаштувань, файлова система.

**Контекст**

```
# 18. Розділи флешу {#rozdily-fleshu}

Флеш ESP32 — не один суцільний шматок пам'яті, а набір областей із
різним призначенням: бутлоадер, таблиця розділів, застосунок, сховище
налаштувань, файлова система. Хто де лежить, описано в **таблиці
розділів** (partition table) за адресою `0x8000`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/a4dbe955-bootloader.rst
- **Дослівно з джерела:**
  > Select the application partition to boot, based on the partition table and ota_data (if any);
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ підтверджує, що флеш містить partition table та різні області, хоча явно не описує всі компоненти.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-002 sha:87d0e3e7 src:manual/18-rozdily-fleshu.md:5 klas:A -->
### T-18-002 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Хто де лежить, описано в **таблиці розділів** (partition table) за адресою `0x8000`.

**Контекст**

```
# 18. Розділи флешу {#rozdily-fleshu}

Флеш ESP32 — не один суцільний шматок пам'яті, а набір областей із
різним призначенням: бутлоадер, таблиця розділів, застосунок, сховище
налаштувань, файлова система. Хто де лежить, описано в **таблиці
розділів** (partition table) за адресою `0x8000`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-18-003 sha:ea68963b src:manual/18-rozdily-fleshu.md:8 klas:A -->
### T-18-003 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Це та частина системи, яку більшість не чіпає роками — рівно до дня, коли застосунок перестає вміщатися у відведений розділ або треба додати OTA.

**Контекст**

```
# 18. Розділи флешу {#rozdily-fleshu}

Це та частина системи, яку більшість не чіпає роками — рівно до дня, коли
застосунок перестає вміщатися у відведений розділ або треба додати OTA.
Тоді виявляється, що змінити розбивку неважко, а зламати нею робочий
пристрій — легко.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > Each entry in the partition table has a name (label), type (app, data, or something else), subtype and the offset in flash where the partition is loaded.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що розбивка - це те, що більшість не змінює, поки застосунок не переріс
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-004 sha:9c606f2f src:manual/18-rozdily-fleshu.md:10 klas:E -->
### T-18-004 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Тоді виявляється, що змінити розбивку неважко, а зламати нею робочий пристрій — легко.

**Контекст**

```
# 18. Розділи флешу {#rozdily-fleshu}

Це та частина системи, яку більшість не чіпає роками — рівно до дня, коли
застосунок перестає вміщатися у відведений розділ або треба додати OTA.
Тоді виявляється, що змінити розбивку неважко, а зламати нею робочий
пристрій — легко.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-005 sha:4a659ad6 src:manual/18-rozdily-fleshu.md:15 klas:E -->
### T-18-005 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Це список записів, кожен з яких каже: назва, тип, підтип, адреса початку, розмір.

**Контекст**

```
## Що таке таблиця розділів

Це список записів, кожен з яких каже: назва, тип, підтип, адреса початку,
розмір. Бутлоадер читає цей список при кожному старті (розділ 16) і за
ним знаходить застосунок.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-006 sha:4bb6abfa src:manual/18-rozdily-fleshu.md:16 klas:E -->
### T-18-006 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Бутлоадер читає цей список при кожному старті (розділ 16) і за ним знаходить застосунок.

**Контекст**

```
## Що таке таблиця розділів

Це список записів, кожен з яких каже: назва, тип, підтип, адреса початку,
розмір. Бутлоадер читає цей список при кожному старті (розділ 16) і за
ним знаходить застосунок.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-007 sha:564e9856 src:manual/18-rozdily-fleshu.md:19 klas:A -->
### T-18-007 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Сама таблиця крихітна: `0xC00` байтів, тобто **не більше 95 записів**, плюс контрольна сума MD5 після них.

**Контекст**

```
## Що таке таблиця розділів

Сама таблиця крихітна: `0xC00` байтів, тобто **не більше 95 записів**,
плюс контрольна сума MD5 після них. Займає вона при цьому цілий сектор
флешу — 4 КБ, — бо стирати флеш можна тільки секторами.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst, .../docs/en/api-guides/bootloader.rst, .../components/partition_table/Kconfig.projbuild
- **Дослівно з джерела:**
  > (partition-tables.rst)
  > The partition table length is 0xC00 bytes, as we allow a maximum of 95
  > entries. An MD5 checksum, used for checking the integrity of the
  > partition table at runtime, is appended after the table data. Thus, the
  > partition table occupies an entire flash sector, which size is 0x1000
  > (4 KB). As a result, any partition following it must be at least
  > located at (default offset) + 0x1000.
  > 
  > (Kconfig.projbuild)
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  >     help
  >         The address of partition table (by default 0x8000).
  >         Allows you to move the partition table, it gives more space
  >         for the bootloader.
  > 
  > (bootloader.rst)
  > When using the default CONFIG_PARTITION_TABLE_OFFSET value 0x8000, the
  > size limit is … bytes.
  > If the bootloader binary is too large, then the bootloader build will
  > fail with an error "Bootloader binary size [..] is too large for
  > partition table offset".
  > Options to work around this are:
  > - Set bootloader compiler optimization back to "Size" …
  > - Reduce bootloader log level …
  > - Set CONFIG_PARTITION_TABLE_OFFSET to a higher value than 0x8000 …
  >   no partition has an offset lower than CONFIG_PARTITION_TABLE_OFFSET
  >   + 0x1000.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Друга хибна причина, і цього разу вона мешкала в `docs/fakty.md`: «типовий ліміт розміру самої таблиці — `0x7000` (28 672 байти)».
`0x7000` до таблиці не має стосунку. Це `0x8000 − 0x1000` — простір, який лишається **бутлоадерові** на classic. Власна довжина таблиці — `0xC00`, тобто 95 записів плюс MD5, і навіть вона займає цілий сектор лише тому, що флеш стирається секторами.
Плутанина не безневинна: з неї випливає, ніби в таблицю влізає приблизно 900 розділів, і ніби вправа «зробити більше розділів» — безкоштовна. Насправді ліміт 95, а `0x7000` вичерпується не розділами, а Secure Boot і рівнем логу бутлоадера.
Виправлено; обидва хибні формулювання заведено в реєстр спростованого і випробувано впровадженням у розділ 04 — знаходяться одразу.
Заразом додано в книгу три речі, яких не було ніде: ліміт 95 записів (розділ 18), скінченність простору бутлоадера з дослівним рядком помилки збірання і ліками в порядку дешевизни (розділ 16), і асиметрія «зсув бутлоадера задає ROM, зсув таблиці — звичайний параметр» (розділ 16). Остання практично важлива: саме зсувом таблиці лікують нестачу місця під бутлоадер.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-18-008 sha:f3faaf6a src:manual/18-rozdily-fleshu.md:20 klas:D -->
### T-18-008 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Займає вона при цьому цілий сектор флешу — 4 КБ, — бо стирати флеш можна тільки секторами.

**Контекст**

```
## Що таке таблиця розділів

Сама таблиця крихітна: `0xC00` байтів, тобто **не більше 95 записів**,
плюс контрольна сума MD5 після них. Займає вона при цьому цілий сектор
флешу — 4 КБ, — бо стирати флеш можна тільки секторами.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arithmetic.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
- **Розрахунок:**
  таблиця розділів  0x8000 + 0x1000 (сектор) = 0x9000  → перший розділ
  nvs               0x9000 + 0x6000          = 0xF000
  phy_init          0xF000 + 0x1000          = 0x10000 → застосунок
  0x10000 / 1024                             = 64 КБ
  
  сектор 0x1000 / 1024 = 4 КБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Замикає ланцюжок, який книга досі подавала трьома окремими твердженнями в розділах 16, 18 і 19: чому таблиця розділів займає цілий сектор, чому наступний розділ не може починатися раніше ніж `0x9000`, і звідки береться «близько 64 КБ службових».
Тепер це один перерахунок із п'яти кроків, і кожен крок видимий. Розмір розділів узято з `partitions_singleapp.csv` ESP-IDF (прохід 7), тобто арифметика спирається на звірені числа, а не на самі себе.
Заразом видно, що «4 МБ мінус 64 КБ службових = 3.9 МБ» із розділу 18 — не округлення на око, а точний наслідок цієї ж розкладки.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-18-009 sha:cc195a29 src:manual/18-rozdily-fleshu.md:23 klas:A -->
### T-18-009 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Типова розбивка для пристрою без OTA виглядає так:

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > # ESP-IDF Partition Table # Name,   Type, SubType, Offset,  Size, Flags nvs,      data, nvs,     0x9000,  0x6000, phy_init, data, phy,     0xf000,  0x1000, factory,  app,  factory, 0x10000, 1M,
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** наведено типову розбивку без OTA
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-010 sha:f337b884 src:manual/18-rozdily-fleshu.md:25 klas:A -->
### T-18-010 · tablycya-shapka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> | Назва | Тип | Підтип | Зсув | Розмір |

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > Name,   Type, SubType, Offset,  Size, Flags
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує формат таблиці розділів з колонками Назва, Тип, Підтип, Зсув, Розмір
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-011 sha:606ac6dd src:manual/18-rozdily-fleshu.md:26 klas:A -->
### T-18-011 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `nvs` · Тип → data

**Дослівно з книги**

```
| `nvs` | data | nvs | `0x9000` | `0x6000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/c02027a1-nvs_flash.rst
- **Дослівно з джерела:**
  > The library uses all the partitions with data type and nvs subtype.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ явно стверджує, що NVS використовує розділи з типом data.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-012 sha:f47ce163 src:manual/18-rozdily-fleshu.md:26 klas:A -->
### T-18-012 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `nvs` · Підтип → nvs

**Дослівно з книги**

```
| `nvs` | data | nvs | `0x9000` | `0x6000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/c02027a1-nvs_flash.rst
- **Дослівно з джерела:**
  > The library uses all the partitions with data type and nvs subtype.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ підтверджує, що NVS використовує розділи з типом data та підтипом nvs.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-013 sha:15620348 src:manual/18-rozdily-fleshu.md:26 klas:A -->
### T-18-013 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `nvs` · Зсув → `0x9000`

**Дослівно з книги**

```
| `nvs` | data | nvs | `0x9000` | `0x6000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > nvs,      data, nvs,     0x9000,  0x6000,
  > factory,  app,  factory, 0x10000, 1M,
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep partition, 2026-08-26
- **Нотатка:** Розділ 18 показує типову таблицю розділів. Джерело підтверджує: nvs на 0x9000, factory на 0x10000. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-18-014 sha:8f0dd715 src:manual/18-rozdily-fleshu.md:26 klas:A -->
### T-18-014 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `nvs` · Розмір → `0x6000`

**Дослівно з книги**

```
| `nvs` | data | nvs | `0x9000` | `0x6000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та .../components/bootloader_support/src/bootloader_utility.c
- **Дослівно з джерела:**
  > # ESP-IDF Partition Table
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     0x9000,  0x6000,
  > phy_init, data, phy,     0xf000,  0x1000,
  > factory,  app,  factory, 0x10000, 1M,
  > 
  > In both cases the factory app is flashed at offset 0x10000.
  > 
  > Sizes and offsets can be specified as decimal numbers, hex numbers
  > with the prefix 0x, or size multipliers K or M (1024 and 1024*1024
  > bytes).
  > 
  > (bootloader_utility.c)
  > ESP_LOGI(TAG, "Partition Table:");
  > ESP_LOGI(TAG, "## Label            Usage          Type ST Offset   Length");
  > …
  > ESP_LOGI(TAG, "End of partition table");
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Уся типова розбивка книги збіглася з тією, що друкує сама документація ESP-IDF, — рядок у рядок.
Окремо цінне: агент знайшов **у коді бутлоадера** рядки, якими таблиця друкується в лог. Книга обіцяє читачеві, що розбивку чужого пристрою видно в boot-лозі без жодних інструментів; тепер це підтверджено не документацією, а самою функцією, яка це друкує.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-015 sha:5f9bc8f0 src:manual/18-rozdily-fleshu.md:27 klas:A -->
### T-18-015 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `phy_init` · Тип → data

**Дослівно з книги**

```
| `phy_init` | data | phy | `0xF000` | `0x1000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > phy_init, data, phy,     0xf000,  0x1000,
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** phy_init має тип data у таблиці розділів
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-016 sha:789c88b9 src:manual/18-rozdily-fleshu.md:27 klas:A -->
### T-18-016 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `phy_init` · Підтип → phy

**Дослівно з книги**

```
| `phy_init` | data | phy | `0xF000` | `0x1000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > phy_init, data, phy,     0xf000,  0x1000,
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** phy_init має підтип phy у таблиці розділів
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-017 sha:fc7a2431 src:manual/18-rozdily-fleshu.md:27 klas:A -->
### T-18-017 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `phy_init` · Зсув → `0xF000`

**Дослівно з книги**

```
| `phy_init` | data | phy | `0xF000` | `0x1000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

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

<!-- fc id:T-18-018 sha:d76b708c src:manual/18-rozdily-fleshu.md:27 klas:A -->
### T-18-018 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `phy_init` · Розмір → `0x1000`

**Дослівно з книги**

```
| `phy_init` | data | phy | `0xF000` | `0x1000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та .../components/bootloader_support/src/bootloader_utility.c
- **Дослівно з джерела:**
  > # ESP-IDF Partition Table
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     0x9000,  0x6000,
  > phy_init, data, phy,     0xf000,  0x1000,
  > factory,  app,  factory, 0x10000, 1M,
  > 
  > In both cases the factory app is flashed at offset 0x10000.
  > 
  > Sizes and offsets can be specified as decimal numbers, hex numbers
  > with the prefix 0x, or size multipliers K or M (1024 and 1024*1024
  > bytes).
  > 
  > (bootloader_utility.c)
  > ESP_LOGI(TAG, "Partition Table:");
  > ESP_LOGI(TAG, "## Label            Usage          Type ST Offset   Length");
  > …
  > ESP_LOGI(TAG, "End of partition table");
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Уся типова розбивка книги збіглася з тією, що друкує сама документація ESP-IDF, — рядок у рядок.
Окремо цінне: агент знайшов **у коді бутлоадера** рядки, якими таблиця друкується в лог. Книга обіцяє читачеві, що розбивку чужого пристрою видно в boot-лозі без жодних інструментів; тепер це підтверджено не документацією, а самою функцією, яка це друкує.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-019 sha:94bcae2e src:manual/18-rozdily-fleshu.md:28 klas:A -->
### T-18-019 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `factory` · Тип → app

**Дослівно з книги**

```
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > factory,  app,  factory, 0x10000, 1M,
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** factory має тип app у таблиці розділів
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-020 sha:98e8369f src:manual/18-rozdily-fleshu.md:28 klas:A -->
### T-18-020 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `factory` · Підтип → factory

**Дослівно з книги**

```
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > factory,  app,  factory, 0x10000, 1M,
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** factory має підтип factory у таблиці розділів
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-021 sha:9df43b5f src:manual/18-rozdily-fleshu.md:28 klas:A -->
### T-18-021 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `factory` · Зсув → `0x10000`

**Дослівно з книги**

```
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > nvs,      data, nvs,     0x9000,  0x6000,
  > factory,  app,  factory, 0x10000, 1M,
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep partition, 2026-08-26
- **Нотатка:** Розділ 18 показує типову таблицю розділів. Джерело підтверджує: nvs на 0x9000, factory на 0x10000. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-18-022 sha:59fff70d src:manual/18-rozdily-fleshu.md:28 klas:A -->
### T-18-022 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `factory` · Розмір → `0x100000`

**Дослівно з книги**

```
| `factory` | app | factory | `0x10000` | `0x100000` |
```

**Контекст**

```
## Що таке таблиця розділів

Типова розбивка для пристрою без OTA виглядає так:

| Назва | Тип | Підтип | Зсув | Розмір |
|---|---|---|---|---|
| `nvs` | data | nvs | `0x9000` | `0x6000` |
| `phy_init` | data | phy | `0xF000` | `0x1000` |
| `factory` | app | factory | `0x10000` | `0x100000` |
```

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

<!-- fc id:T-18-023 sha:0923797f src:manual/18-rozdily-fleshu.md:31 klas:E -->
### T-18-023 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Три речі, які варто прочитати з цієї таблиці одразу.

**Контекст**

```
## Що таке таблиця розділів

Три речі, які варто прочитати з цієї таблиці одразу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-024 sha:50b4dd7d src:manual/18-rozdily-fleshu.md:33 klas:A -->
### T-18-024 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **Застосунок починається з `0x10000`** — це не випадкове число, а перша адреса після таблиці розділів і службових областей.

**Контекст**

```
## Що таке таблиця розділів

**Застосунок починається з `0x10000`** — це не випадкове число, а перша
адреса після таблиці розділів і службових областей. Саме тому у всіх
командах прошивки застосунок іде на `0x10000`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > In both cases the factory app is flashed at offset 0x10000
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** прямо підтверджує, що застосунок починається з адреси 0x10000
- **Прохід:** presud-18-rozdily-fleshu

---

<!-- fc id:T-18-025 sha:6ad702cc src:manual/18-rozdily-fleshu.md:34 klas:A -->
### T-18-025 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Саме тому у всіх командах прошивки застосунок іде на `0x10000`.

**Контекст**

```
## Що таке таблиця розділів

**Застосунок починається з `0x10000`** — це не випадкове число, а перша
адреса після таблиці розділів і службових областей. Саме тому у всіх
командах прошивки застосунок іде на `0x10000`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та .../components/bootloader_support/src/bootloader_utility.c
- **Дослівно з джерела:**
  > # ESP-IDF Partition Table
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     0x9000,  0x6000,
  > phy_init, data, phy,     0xf000,  0x1000,
  > factory,  app,  factory, 0x10000, 1M,
  > 
  > In both cases the factory app is flashed at offset 0x10000.
  > 
  > Sizes and offsets can be specified as decimal numbers, hex numbers
  > with the prefix 0x, or size multipliers K or M (1024 and 1024*1024
  > bytes).
  > 
  > (bootloader_utility.c)
  > ESP_LOGI(TAG, "Partition Table:");
  > ESP_LOGI(TAG, "## Label            Usage          Type ST Offset   Length");
  > …
  > ESP_LOGI(TAG, "End of partition table");
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Уся типова розбивка книги збіглася з тією, що друкує сама документація ESP-IDF, — рядок у рядок.
Окремо цінне: агент знайшов **у коді бутлоадера** рядки, якими таблиця друкується в лог. Книга обіцяє читачеві, що розбивку чужого пристрою видно в boot-лозі без жодних інструментів; тепер це підтверджено не документацією, а самою функцією, яка це друкує.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-026 sha:4eca33d4 src:manual/18-rozdily-fleshu.md:37 klas:A -->
### T-18-026 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **`nvs` лежить перед застосунком.** Це сховище пар «ключ — значення»: налаштування, збережені креденшели Wi-Fi, лічильники.

**Контекст**

```
## Що таке таблиця розділів

**`nvs` лежить перед застосунком.** Це сховище пар «ключ — значення»:
налаштування, збережені креденшели Wi-Fi, лічильники. Воно переживає
оновлення прошивки — і саме тому `erase-flash` такий болючий.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/c02027a1-nvs_flash.rst
- **Дослівно з джерела:**
  > Non-volatile storage (NVS) library is designed to store key-value pairs in flash.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ підтверджує, що NVS — сховище пар ключ-значення. Приклади з wifi-намеспейсом і лічильником перезавантажень також знайдені.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-027 sha:20700e13 src:manual/18-rozdily-fleshu.md:38 klas:A -->
### T-18-027 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Воно переживає оновлення прошивки — і саме тому `erase-flash` такий болючий.

**Контекст**

```
## Що таке таблиця розділів

**`nvs` лежить перед застосунком.** Це сховище пар «ключ — значення»:
налаштування, збережені креденшели Wi-Fi, лічильники. Воно переживає
оновлення прошивки — і саме тому `erase-flash` такий болючий.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > (partition-tables.rst)
  > Note that updating the partition table does not erase data that may
  > have been stored according to the old partition table. You can use
  > ``idf.py erase-flash`` (or ``esptool.py erase_flash``) to erase the
  > entire flash contents.
  > 
  > (basic-commands.rst)
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  >     esptool erase-flash
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Порада книги підтверджена з обох боків: документація прямо каже, що зміна таблиці **не стирає** даних за старою розбивкою, а `erase-flash` замінює все на `0xFF`.
Агент чесно позначив, що «незворотний» — висновок книги, а не речення джерела. Погоджуюся й лишаю клас `A`: із «все замінюється на `0xFF`» незворотність випливає однозначно, а не правдоподібно. Межа між `A` і `B` тут саме в цьому — чи є інший можливий висновок. Тут немає.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-028 sha:ded12860 src:manual/18-rozdily-fleshu.md:41 klas:A -->
### T-18-028 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **`phy_init`** зберігає калібрувальні дані радіо.

**Контекст**

```
## Що таке таблиця розділів

**`phy_init`** зберігає калібрувальні дані радіо. Маленький розділ, про
який ніхто не думає, поки не зітре.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > phy`` (1) is for storing PHY initialisation data. This allows PHY to be configured per-device, instead of in firmware.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що phy_init зберігає калібрувальні дані радіо
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-029 sha:76acd34b src:manual/18-rozdily-fleshu.md:41 klas:E -->
### T-18-029 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Маленький розділ, про який ніхто не думає, поки не зітре.

**Контекст**

```
## Що таке таблиця розділів

**`phy_init`** зберігає калібрувальні дані радіо. Маленький розділ, про
який ніхто не думає, поки не зітре.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-030 sha:b16e6cfe src:manual/18-rozdily-fleshu.md:46 klas:E -->
### T-18-030 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Найдешевший спосіб — прочитати boot-лог: другий бутлоадер друкує всю таблицю з адресами при кожному старті (розділ 16).

**Контекст**

```
## Як подивитися розбивку живого пристрою

Найдешевший спосіб — прочитати boot-лог: другий бутлоадер друкує всю
таблицю з адресами при кожному старті (розділ 16). Нічого розбирати не
треба.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-031 sha:f936f28f src:manual/18-rozdily-fleshu.md:47 klas:E -->
### T-18-031 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Нічого розбирати не треба.

**Контекст**

```
## Як подивитися розбивку живого пристрою

Найдешевший спосіб — прочитати boot-лог: другий бутлоадер друкує всю
таблицю з адресами при кожному старті (розділ 16). Нічого розбирати не
треба.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-032 sha:12c0dae9 src:manual/18-rozdily-fleshu.md:50 klas:E -->
### T-18-032 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Якщо логу немає, таблицю можна зняти з флешу і розібрати:

**Контекст**

```
## Як подивитися розбивку живого пристрою

Якщо логу немає, таблицю можна зняти з флешу і розібрати:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-033 sha:2af2e0ef src:manual/18-rozdily-fleshu.md:52 klas:K -->
### T-18-033 · kod · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 read-flash 0x8000 0x1000 pt.bin
> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
> ```

**Контекст**

````
## Як подивитися розбивку живого пристрою

```
esptool --port /dev/ttyUSB0 read-flash 0x8000 0x1000 pt.bin
python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/4aac28c3-partition-tables.rst
- **Дослівно з джерела:**
  > python gen_esp32part.py input_partitions.csv binary_partitions.bin
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує команду gen_esp32part.py
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-034 sha:5793a2bb src:manual/18-rozdily-fleshu.md:53 klas:D -->
### T-18-034 · kod-ryadok · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 read-flash 0x8000 0x1000 pt.bin

**Контекст**

````
## Як подивитися розбивку живого пристрою

```
esptool --port /dev/ttyUSB0 read-flash 0x8000 0x1000 pt.bin
python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
```
````

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arithmetic.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
- **Розрахунок:**
  таблиця розділів  0x8000 + 0x1000 (сектор) = 0x9000  → перший розділ
  nvs               0x9000 + 0x6000          = 0xF000
  phy_init          0xF000 + 0x1000          = 0x10000 → застосунок
  0x10000 / 1024                             = 64 КБ
  
  сектор 0x1000 / 1024 = 4 КБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Замикає ланцюжок, який книга досі подавала трьома окремими твердженнями в розділах 16, 18 і 19: чому таблиця розділів займає цілий сектор, чому наступний розділ не може починатися раніше ніж `0x9000`, і звідки береться «близько 64 КБ службових».
Тепер це один перерахунок із п'яти кроків, і кожен крок видимий. Розмір розділів узято з `partitions_singleapp.csv` ESP-IDF (прохід 7), тобто арифметика спирається на звірені числа, а не на самі себе.
Заразом видно, що «4 МБ мінус 64 КБ службових = 3.9 МБ» із розділу 18 — не округлення на око, а точний наслідок цієї ж розкладки.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-18-035 sha:4438754b src:manual/18-rozdily-fleshu.md:54 klas:A -->
### T-18-035 · kod-ryadok · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin

**Контекст**

````
## Як подивитися розбивку живого пристрою

```
esptool --port /dev/ttyUSB0 read-flash 0x8000 0x1000 pt.bin
python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/4aac28c3-partition-tables.rst
- **Дослівно з джерела:**
  > python gen_esp32part.py input_partitions.csv binary_partitions.bin
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує команду gen_esp32part.py
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-036 sha:9c3fadfd src:manual/18-rozdily-fleshu.md:57 klas:E -->
### T-18-036 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Другий рядок друкує таблицю в тому самому CSV-форматі, у якому її пишуть.

**Контекст**

```
## Як подивитися розбивку живого пристрою

Другий рядок друкує таблицю в тому самому CSV-форматі, у якому її пишуть.
Це один із перших кроків форензики чужої прошивки — розділ 24.
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

<!-- fc id:T-18-037 sha:170e004e src:manual/18-rozdily-fleshu.md:58 klas:E -->
### T-18-037 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Це один із перших кроків форензики чужої прошивки — розділ 24.

**Контекст**

```
## Як подивитися розбивку живого пристрою

Другий рядок друкує таблицю в тому самому CSV-форматі, у якому її пишуть.
Це один із перших кроків форензики чужої прошивки — розділ 24.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-038 sha:efe25d4b src:manual/18-rozdily-fleshu.md:62 klas:A -->
### T-18-038 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> У проєкті ESP-IDF розбивка задається текстовим файлом:

**Контекст**

```
## CSV: як це описується в проєкті

У проєкті ESP-IDF розбивка задається текстовим файлом:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > If you configure the partition table CSV name in the project configuration (``idf.py menuconfig``) and then build the project
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що розбивка задається текстовим CSV файлом
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-039 sha:8348b7b2 src:manual/18-rozdily-fleshu.md:64 klas:K -->
### T-18-039 · kod · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> ```
> # Name,   Type, SubType, Offset,   Size,   Flags
> nvs,      data, nvs,     0x9000,   0x6000,
> phy_init, data, phy,     0xF000,   0x1000,
> factory,  app,  factory, 0x10000,  1M,
> storage,  data, spiffs,  ,         1M,
> ```

**Контекст**

````
## CSV: як це описується в проєкті

```
# Name,   Type, SubType, Offset,   Size,   Flags
nvs,      data, nvs,     0x9000,   0x6000,
phy_init, data, phy,     0xF000,   0x1000,
factory,  app,  factory, 0x10000,  1M,
storage,  data, spiffs,  ,         1M,
```
````

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

<!-- fc id:T-18-040 sha:40c8d5dd src:manual/18-rozdily-fleshu.md:72 klas:F -->
### T-18-040 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Порожній `Offset` означає «одразу після попереднього» — так і треба робити: явні адреси в кожному рядку легко розсинхронізувати при першій же зміні розміру.

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

Порожній `Offset` означає «одразу після попереднього» — так і треба
робити: явні адреси в кожному рядку легко розсинхронізувати при першій же
зміні розміру.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-041 sha:d9cb149f src:manual/18-rozdily-fleshu.md:76 klas:A -->
### T-18-041 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Розмір записується числом (`0x100000`), або з суфіксом (`1M`, `512K`).

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

Розмір записується числом (`0x100000`), або з суфіксом (`1M`, `512K`).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та .../components/bootloader_support/src/bootloader_utility.c
- **Дослівно з джерела:**
  > # ESP-IDF Partition Table
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     0x9000,  0x6000,
  > phy_init, data, phy,     0xf000,  0x1000,
  > factory,  app,  factory, 0x10000, 1M,
  > 
  > In both cases the factory app is flashed at offset 0x10000.
  > 
  > Sizes and offsets can be specified as decimal numbers, hex numbers
  > with the prefix 0x, or size multipliers K or M (1024 and 1024*1024
  > bytes).
  > 
  > (bootloader_utility.c)
  > ESP_LOGI(TAG, "Partition Table:");
  > ESP_LOGI(TAG, "## Label            Usage          Type ST Offset   Length");
  > …
  > ESP_LOGI(TAG, "End of partition table");
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Уся типова розбивка книги збіглася з тією, що друкує сама документація ESP-IDF, — рядок у рядок.
Окремо цінне: агент знайшов **у коді бутлоадера** рядки, якими таблиця друкується в лог. Книга обіцяє читачеві, що розбивку чужого пристрою видно в boot-лозі без жодних інструментів; тепер це підтверджено не документацією, а самою функцією, яка це друкує.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-042 sha:d8851079 src:manual/18-rozdily-fleshu.md:79 klas:A -->
### T-18-042 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **Розділи типу `app` мають бути вирівняні на `0x10000` (64 КБ).** Це вимога апаратного відображення пам'яті, а не примха.

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

::: uvaha
**Розділи типу `app` мають бути вирівняні на `0x10000` (64 КБ).** Це
вимога апаратного відображення пам'яті, а не примха. Розділи типу `data`
вирівнюються на `0x1000` (4 КБ). Якщо збирання скаржиться на вирівнювання
— справа в цьому.
:::
```

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

<!-- fc id:T-18-043 sha:2cfd4562 src:manual/18-rozdily-fleshu.md:80 klas:A -->
### T-18-043 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Розділи типу `data` вирівнюються на `0x1000` (4 КБ).

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

::: uvaha
**Розділи типу `app` мають бути вирівняні на `0x10000` (64 КБ).** Це
вимога апаратного відображення пам'яті, а не примха. Розділи типу `data`
вирівнюються на `0x1000` (4 КБ). Якщо збирання скаржиться на вирівнювання
— справа в цьому.
:::
```

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

<!-- fc id:T-18-044 sha:14b13bf4 src:manual/18-rozdily-fleshu.md:81 klas:E -->
### T-18-044 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Якщо збирання скаржиться на вирівнювання — справа в цьому.

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

::: uvaha
**Розділи типу `app` мають бути вирівняні на `0x10000` (64 КБ).** Це
вимога апаратного відображення пам'яті, а не примха. Розділи типу `data`
вирівнюються на `0x1000` (4 КБ). Якщо збирання скаржиться на вирівнювання
— справа в цьому.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-045 sha:801f2aae src:manual/18-rozdily-fleshu.md:85 klas:A -->
### T-18-045 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Вибір готової розбивки замість власної — `idf.py menuconfig`, розділ `Partition Table`.

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

Вибір готової розбивки замість власної — `idf.py menuconfig`, розділ
`Partition Table`. Там є типові варіанти: одна `factory`, дві OTA-області,
варіанти під різні обсяги флешу. Для більшості задач власний CSV не
потрібен.
```

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

<!-- fc id:T-18-046 sha:16a9ef2e src:manual/18-rozdily-fleshu.md:86 klas:F -->
### T-18-046 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Там є типові варіанти: одна `factory`, дві OTA-області, варіанти під різні обсяги флешу.

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

Вибір готової розбивки замість власної — `idf.py menuconfig`, розділ
`Partition Table`. Там є типові варіанти: одна `factory`, дві OTA-області,
варіанти під різні обсяги флешу. Для більшості задач власний CSV не
потрібен.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-047 sha:d288675c src:manual/18-rozdily-fleshu.md:87 klas:E -->
### T-18-047 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Для більшості задач власний CSV не потрібен.

**Контекст**

```
# Name,   Type, SubType, Offset,   Size,   Flags

Вибір готової розбивки замість власної — `idf.py menuconfig`, розділ
`Partition Table`. Там є типові варіанти: одна `factory`, дві OTA-області,
варіанти під різні обсяги флешу. Для більшості задач власний CSV не
потрібен.
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

<!-- fc id:T-18-048 sha:25ea8296 src:manual/18-rozdily-fleshu.md:92 klas:A -->
### T-18-048 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> NVS (Non-Volatile Storage) — сховище пар «ключ — значення», розкладене по просторах імен.

**Контекст**

```
## NVS: де живуть налаштування

NVS (Non-Volatile Storage) — сховище пар «ключ — значення», розкладене по
просторах імен. Саме тут має лежати все, що конкретне для **цього
екземпляра** пристрою: серійний номер, калібрувальні коефіцієнти, адреса
сервера, креденшели.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/c02027a1-nvs_flash.rst
- **Дослівно з джерела:**
  > Non-volatile storage (NVS) library is designed to store key-value pairs in flash.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ підтверджує, що NVS — сховище пар ключ-значення з підтримкою намеспейсів.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-049 sha:52530cd3 src:manual/18-rozdily-fleshu.md:93 klas:E -->
### T-18-049 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Саме тут має лежати все, що конкретне для **цього екземпляра** пристрою: серійний номер, калібрувальні коефіцієнти, адреса сервера, креденшели.

**Контекст**

```
## NVS: де живуть налаштування

NVS (Non-Volatile Storage) — сховище пар «ключ — значення», розкладене по
просторах імен. Саме тут має лежати все, що конкретне для **цього
екземпляра** пристрою: серійний номер, калібрувальні коефіцієнти, адреса
сервера, креденшели.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-050 sha:4935de88 src:manual/18-rozdily-fleshu.md:97 klas:F -->
### T-18-050 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Чому саме тут, а не в коді: значення в NVS переживає оновлення прошивки.

**Контекст**

```
## NVS: де живуть налаштування

Чому саме тут, а не в коді: значення в NVS переживає оновлення прошивки.
Один образ можна залити на сто плат, а різне для кожної записати в NVS
окремо — основа серійного виробництва (розділ 21).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-051 sha:d7ea3d3a src:manual/18-rozdily-fleshu.md:98 klas:F -->
### T-18-051 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Один образ можна залити на сто плат, а різне для кожної записати в NVS окремо — основа серійного виробництва (розділ 21).

**Контекст**

```
## NVS: де живуть налаштування

Чому саме тут, а не в коді: значення в NVS переживає оновлення прошивки.
Один образ можна залити на сто плат, а різне для кожної записати в NVS
окремо — основа серійного виробництва (розділ 21).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-052 sha:77e191f6 src:manual/18-rozdily-fleshu.md:101 klas:A -->
### T-18-052 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> NVS стійкий до зникнення живлення: запис влаштований так, що обірвана операція не псує вже записане.

**Контекст**

```
## NVS: де живуть налаштування

NVS стійкий до зникнення живлення: запис влаштований так, що обірвана
операція не псує вже записане. Це не означає, що він незнищенний —
переповнений або пошкоджений NVS призводить до помилок при старті, і в
логу це видно явно (`nvs_flash_init failed`).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/c02027a1-nvs_flash.rst
- **Дослівно з джерела:**
  > The library does try to recover from conditions when flash memory is in an inconsistent state. In particular, one should be able to power off the device at any point and time and then power it back on. This should not result in loss of data, except for the new key-value pair if it was being written at the moment of powering off.
- **Спосіб і дата:** Source document retrieved 2026-08-26 from the local cache; quote verified against it by substring match.
- **Нотатка:** Підтверджує стійкість до зникнення живлення.
- **Прохід:** m2-hvylya2

---

<!-- fc id:T-18-053 sha:9eef63be src:manual/18-rozdily-fleshu.md:102 klas:A -->
### T-18-053 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Це не означає, що він незнищенний — переповнений або пошкоджений NVS призводить до помилок при старті, і в логу це видно явно (`nvs_flash_init failed`).

**Контекст**

```
## NVS: де живуть налаштування

NVS стійкий до зникнення живлення: запис влаштований так, що обірвана
операція не псує вже записане. Це не означає, що він незнищенний —
переповнений або пошкоджений NVS призводить до помилок при старті, і в
логу це видно явно (`nvs_flash_init failed`).
```

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

<!-- fc id:T-18-054 sha:7d517b9b src:manual/18-rozdily-fleshu.md:106 klas:F -->
### T-18-054 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Стандартна реакція на пошкоджений NVS — стерти і переініціалізувати.

**Контекст**

```
## NVS: де живуть налаштування

Стандартна реакція на пошкоджений NVS — стерти і переініціалізувати. Це
робиться з коду, і це нормальна практика:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-055 sha:4b78fd12 src:manual/18-rozdily-fleshu.md:106 klas:E -->
### T-18-055 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Це робиться з коду, і це нормальна практика:

**Контекст**

```
## NVS: де живуть налаштування

Стандартна реакція на пошкоджений NVS — стерти і переініціалізувати. Це
робиться з коду, і це нормальна практика:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-056 sha:bdb800c3 src:manual/18-rozdily-fleshu.md:109 klas:K -->
### T-18-056 · kod · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> ```c
> esp_err_t err = nvs_flash_init();
> if (err == ESP_ERR_NVS_NO_FREE_PAGES ||
>     err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
>     ESP_ERROR_CHECK(nvs_flash_erase());
>     err = nvs_flash_init();
> }
> ESP_ERROR_CHECK(err);
> ```

**Контекст**

````
## NVS: де живуть налаштування

```c
esp_err_t err = nvs_flash_init();
if (err == ESP_ERR_NVS_NO_FREE_PAGES ||
    err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
    ESP_ERROR_CHECK(nvs_flash_erase());
    err = nvs_flash_init();
}
ESP_ERROR_CHECK(err);
```
````

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

<!-- fc id:T-18-057 sha:f3349b99 src:manual/18-rozdily-fleshu.md:113 klas:A -->
### T-18-057 · kod-ryadok · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> ESP_ERROR_CHECK(nvs_flash_erase());

**Контекст**

````
## NVS: де живуть налаштування

```c
esp_err_t err = nvs_flash_init();
if (err == ESP_ERR_NVS_NO_FREE_PAGES ||
    err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
    ESP_ERROR_CHECK(nvs_flash_erase());
    err = nvs_flash_init();
}
ESP_ERROR_CHECK(err);
```
````

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

<!-- fc id:T-18-058 sha:601ab80f src:manual/18-rozdily-fleshu.md:116 klas:F -->
### T-18-058 · kod-ryadok · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> ESP_ERROR_CHECK(err);

**Контекст**

````
## NVS: де живуть налаштування

```c
esp_err_t err = nvs_flash_init();
if (err == ESP_ERR_NVS_NO_FREE_PAGES ||
    err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
    ESP_ERROR_CHECK(nvs_flash_erase());
    err = nvs_flash_init();
}
ESP_ERROR_CHECK(err);
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-059 sha:201bdc14 src:manual/18-rozdily-fleshu.md:120 klas:A -->
### T-18-059 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `nvs_flash_erase()` знищує всі налаштування пристрою.

**Контекст**

```
## NVS: де живуть налаштування

::: nezvorotne
`nvs_flash_erase()` знищує всі налаштування пристрою. У прошивці, що йде
в поле, цей код спрацює саме тоді, коли NVS переповнився — тобто
несподівано, у роботі. Якщо серед налаштувань є те, чого не відновити
(серійний номер, калібрування), його місце не в звичайному NVS, а в
окремому розділі `data` тільки для читання, або в eFuse.
:::
```

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

<!-- fc id:T-18-060 sha:e101ea2e src:manual/18-rozdily-fleshu.md:120 klas:F -->
### T-18-060 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> У прошивці, що йде в поле, цей код спрацює саме тоді, коли NVS переповнився — тобто несподівано, у роботі.

**Контекст**

```
## NVS: де живуть налаштування

::: nezvorotne
`nvs_flash_erase()` знищує всі налаштування пристрою. У прошивці, що йде
в поле, цей код спрацює саме тоді, коли NVS переповнився — тобто
несподівано, у роботі. Якщо серед налаштувань є те, чого не відновити
(серійний номер, калібрування), його місце не в звичайному NVS, а в
окремому розділі `data` тільки для читання, або в eFuse.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-061 sha:92317196 src:manual/18-rozdily-fleshu.md:122 klas:A -->
### T-18-061 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Якщо серед налаштувань є те, чого не відновити (серійний номер, калібрування), його місце не в звичайному NVS, а в окремому розділі `data` тільки для читання, або в eFuse.

**Контекст**

```
## NVS: де живуть налаштування

::: nezvorotne
`nvs_flash_erase()` знищує всі налаштування пристрою. У прошивці, що йде
в поле, цей код спрацює саме тоді, коли NVS переповнився — тобто
несподівано, у роботі. Якщо серед налаштувань є те, чого не відновити
(серійний номер, калібрування), його місце не в звичайному NVS, а в
окремому розділі `data` тільки для читання, або в eFuse.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/c02027a1-nvs_flash.rst
- **Дослівно з джерела:**
  > The partition can be used to store data that is not expected to change, such as calibration data or factory settings.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ явно згадує, що калібрування може зберігатися у спеціальному розділі, не очікуючи змін.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-062 sha:b3d9bf8d src:manual/18-rozdily-fleshu.md:129 klas:C -->
### T-18-062 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна файлова система в окремому розділі `data`.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32-IDF partition table specification
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32-IDF partition table specification
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-18-rozdily-fleshu

---

<!-- fc id:T-18-063 sha:5b298442 src:manual/18-rozdily-fleshu.md:132 klas:F -->
### T-18-063 · tablycya-shapka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> | | LittleFS | SPIFFS | FAT |

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-064 sha:e168a5c0 src:manual/18-rozdily-fleshu.md:133 klas:E -->
### T-18-064 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Стійкість до зникнення живлення · LittleFS → так, за задумом

**Дослівно з книги**

```
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-065 sha:34872fc8 src:manual/18-rozdily-fleshu.md:133 klas:F -->
### T-18-065 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Стійкість до зникнення живлення · SPIFFS → ні

**Дослівно з книги**

```
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-066 sha:136b11ff src:manual/18-rozdily-fleshu.md:133 klas:E -->
### T-18-066 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Стійкість до зникнення живлення · FAT → ні

**Дослівно з книги**

```
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-067 sha:e9f3c2f3 src:manual/18-rozdily-fleshu.md:134 klas:E -->
### T-18-067 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Каталоги · LittleFS → так

**Дослівно з книги**

```
| Каталоги | так | ні, плоский простір | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-068 sha:bd591c14 src:manual/18-rozdily-fleshu.md:134 klas:F -->
### T-18-068 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Каталоги · SPIFFS → ні, плоский простір

**Дослівно з книги**

```
| Каталоги | так | ні, плоский простір | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-069 sha:27ed2cb4 src:manual/18-rozdily-fleshu.md:134 klas:E -->
### T-18-069 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Каталоги · FAT → так

**Дослівно з книги**

```
| Каталоги | так | ні, плоский простір | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-070 sha:7c5fc24e src:manual/18-rozdily-fleshu.md:135 klas:E -->
### T-18-070 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Знос флешу · LittleFS → вирівнюється власним механізмом

**Дослівно з книги**

```
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-071 sha:8b7abf4b src:manual/18-rozdily-fleshu.md:135 klas:F -->
### T-18-071 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Знос флешу · SPIFFS → вирівнюється власним механізмом

**Дослівно з книги**

```
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-072 sha:6a505c3a src:manual/18-rozdily-fleshu.md:135 klas:A -->
### T-18-072 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Знос флешу · FAT → лише через окремий шар `wear_levelling`

**Дослівно з книги**

```
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Усі названі книгою константи існують дослівно. Прохід 7 звіряв виклики; ці — коди повернення, і вони живуть у тих самих заголовках.
Твердження розділу 18 про `wear_levelling` підтверджується від протилежного: у документації FAT монтується через `esp_vfs_fat_spiflash_mount_rw_wl`, тобто саме через шар вирівнювання зносу, — отже сама FAT його не робить, як книга й пише.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-18-073 sha:7a364c66 src:manual/18-rozdily-fleshu.md:136 klas:E -->
### T-18-073 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Швидкість при заповненні · LittleFS → не деградує

**Дослівно з книги**

```
| Швидкість при заповненні | не деградує | різко падає | рівна |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-074 sha:34b80b5e src:manual/18-rozdily-fleshu.md:136 klas:A -->
### T-18-074 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Швидкість при заповненні · SPIFFS → різко падає

**Дослівно з книги**

```
| Швидкість при заповненні | не деградує | різко падає | рівна |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/storage/spiffs.rst
- **Дослівно з джерела:**
  > When the filesystem is running out of space, the garbage collector is trying to find free space by scanning the filesystem multiple times, which can take up to several seconds per write function call
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Точне описання падіння швидкості SPIFFS при заповненні
- **Прохід:** cherga-a-18-rozdily-fleshu

---

<!-- fc id:T-18-075 sha:3764ddb1 src:manual/18-rozdily-fleshu.md:136 klas:C -->
### T-18-075 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Швидкість при заповненні · FAT → рівна

**Дослівно з книги**

```
| Швидкість при заповненні | не деградує | різко падає | рівна |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** FAT Specification
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** FAT Specification
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-18-rozdily-fleshu

---

<!-- fc id:T-18-076 sha:c0ee355e src:manual/18-rozdily-fleshu.md:137 klas:E -->
### T-18-076 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Сумісність із ПК · LittleFS → ні

**Дослівно з книги**

```
| Сумісність із ПК | ні | ні | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-077 sha:2d821c96 src:manual/18-rozdily-fleshu.md:137 klas:F -->
### T-18-077 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Сумісність із ПК · SPIFFS → ні

**Дослівно з книги**

```
| Сумісність із ПК | ні | ні | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-078 sha:97b8e259 src:manual/18-rozdily-fleshu.md:137 klas:E -->
### T-18-078 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Сумісність із ПК · FAT → так

**Дослівно з книги**

```
| Сумісність із ПК | ні | ні | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-079 sha:ad08a567 src:manual/18-rozdily-fleshu.md:138 klas:F -->
### T-18-079 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> У складі ESP-IDF · LittleFS → **ні**, окремий компонент

**Дослівно з книги**

```
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-080 sha:0c51c182 src:manual/18-rozdily-fleshu.md:138 klas:A -->
### T-18-080 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> У складі ESP-IDF · SPIFFS → так

**Дослівно з книги**

```
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > spiffs`` (0x82) is for :doc:`/api-reference/storage/spiffs`
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** SPIFFS є частиною ESP-IDF, наведено посилання на внутрішню документацію
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-081 sha:d37a8a60 src:manual/18-rozdily-fleshu.md:138 klas:F -->
### T-18-081 · komirka · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> У складі ESP-IDF · FAT → так

**Дослівно з книги**

```
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, — потрібна
файлова система в окремому розділі `data`.

| | LittleFS | SPIFFS | FAT |
|---|---|---|---|
| Стійкість до зникнення живлення | так, за задумом | ні | ні |
| Каталоги | так | ні, плоский простір | так |
| Знос флешу | вирівнюється власним механізмом | вирівнюється власним механізмом | лише через окремий шар `wear_levelling` |
| Швидкість при заповненні | не деградує | різко падає | рівна |
| Сумісність із ПК | ні | ні | так |
| У складі ESP-IDF | **ні**, окремий компонент | так | так |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-082 sha:b5482ecd src:manual/18-rozdily-fleshu.md:141 klas:F -->
### T-18-082 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **Практичний висновок простий: беріть LittleFS.** SPIFFS вважається застарілим, не має каталогів і починає гальмувати, коли розділ заповнюється більш ніж наполовину.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

**Практичний висновок простий: беріть LittleFS.** SPIFFS вважається
застарілим, не має каталогів і починає гальмувати, коли розділ
заповнюється більш ніж наполовину. Його розумно лишати тільки в чужому
проєкті, який уже на ньому працює.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-083 sha:c6ab43f6 src:manual/18-rozdily-fleshu.md:143 klas:E -->
### T-18-083 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Його розумно лишати тільки в чужому проєкті, який уже на ньому працює.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

**Практичний висновок простий: беріть LittleFS.** SPIFFS вважається
застарілим, не має каталогів і починає гальмувати, коли розділ
заповнюється більш ніж наполовину. Його розумно лишати тільки в чужому
проєкті, який уже на ньому працює.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-084 sha:009fe204 src:manual/18-rozdily-fleshu.md:147 klas:F -->
### T-18-084 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Останній рядок таблиці — це те, на чому спотикаються, шукаючи LittleFS у `menuconfig`.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

::: uvaha
Останній рядок таблиці — це те, на чому спотикаються, шукаючи LittleFS у
`menuconfig`. Його там немає: на відміну від SPIFFS і FAT, LittleFS **не
входить до ESP-IDF** і ставиться з реєстру компонентів:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-085 sha:784039ff src:manual/18-rozdily-fleshu.md:148 klas:F -->
### T-18-085 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Його там немає: на відміну від SPIFFS і FAT, LittleFS **не входить до ESP-IDF** і ставиться з реєстру компонентів:

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

::: uvaha
Останній рядок таблиці — це те, на чому спотикаються, шукаючи LittleFS у
`menuconfig`. Його там немає: на відміну від SPIFFS і FAT, LittleFS **не
входить до ESP-IDF** і ставиться з реєстру компонентів:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-086 sha:8278d069 src:manual/18-rozdily-fleshu.md:151 klas:K -->
### T-18-086 · kod · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> ```sh
> idf.py add-dependency "joltwallet/littlefs^1.22.3"
> ```

**Контекст**

````
## Файлові системи: LittleFS, SPIFFS, FAT

```sh
idf.py add-dependency "joltwallet/littlefs^1.22.3"
```
````

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

<!-- fc id:T-18-087 sha:2568a317 src:manual/18-rozdily-fleshu.md:152 klas:A -->
### T-18-087 · kod-ryadok · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> idf.py add-dependency "joltwallet/littlefs^1.22.3"

**Контекст**

````
## Файлові системи: LittleFS, SPIFFS, FAT

```sh
idf.py add-dependency "joltwallet/littlefs^1.22.3"
```
````

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

<!-- fc id:T-18-088 sha:706a6f2e src:manual/18-rozdily-fleshu.md:155 klas:A -->
### T-18-088 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Після цього розділ у меню з'являється, а тип розділу в CSV пишеться як `littlefs`.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Після цього розділ у меню з'являється, а тип розділу в CSV пишеться як
`littlefs`. Номер версії — з реєстру на момент роботи, він змінюється
частіше за саму книгу.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > littlefs`` (0x83) is for `LittleFS filesystem
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що littlefs є дійсним типом розділу в CSV
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-089 sha:bb45cfb1 src:manual/18-rozdily-fleshu.md:156 klas:E -->
### T-18-089 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Номер версії — з реєстру на момент роботи, він змінюється частіше за саму книгу.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

Після цього розділ у меню з'являється, а тип розділу в CSV пишеться як
`littlefs`. Номер версії — з реєстру на момент роботи, він змінюється
частіше за саму книгу.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-090 sha:62ee5911 src:manual/18-rozdily-fleshu.md:160 klas:E -->
### T-18-090 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> FAT має сенс в одному випадку: коли той самий носій (найчастіше картку microSD) читатиме звичайний комп'ютер.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

FAT має сенс в одному випадку: коли той самий носій (найчастіше картку
microSD) читатиме звичайний комп'ютер. На вбудованому флеші FAT сама по
собі не вирівнює знос — за це відповідає окремий шар `wear_levelling`,
який ESP-IDF підставляє під неї (`esp_vfs_fat_spiflash_mount_rw_wl`).
Працює це чесно, але шар не безкоштовний ні за місцем, ні за швидкістю,
а стійкості до зникнення живлення не додає. На картці — інша розмова
(розділ 49).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-091 sha:2dd189cd src:manual/18-rozdily-fleshu.md:161 klas:A -->
### T-18-091 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> На вбудованому флеші FAT сама по собі не вирівнює знос — за це відповідає окремий шар `wear_levelling`, який ESP-IDF підставляє під неї (`esp_vfs_fat_spiflash_mount_rw_wl`).

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

FAT має сенс в одному випадку: коли той самий носій (найчастіше картку
microSD) читатиме звичайний комп'ютер. На вбудованому флеші FAT сама по
собі не вирівнює знос — за це відповідає окремий шар `wear_levelling`,
який ESP-IDF підставляє під неї (`esp_vfs_fat_spiflash_mount_rw_wl`).
Працює це чесно, але шар не безкоштовний ні за місцем, ні за швидкістю,
а стійкості до зникнення живлення не додає. На картці — інша розмова
(розділ 49).
```

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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Усі названі книгою константи існують дослівно. Прохід 7 звіряв виклики; ці — коди повернення, і вони живуть у тих самих заголовках.
Твердження розділу 18 про `wear_levelling` підтверджується від протилежного: у документації FAT монтується через `esp_vfs_fat_spiflash_mount_rw_wl`, тобто саме через шар вирівнювання зносу, — отже сама FAT його не робить, як книга й пише.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-18-092 sha:3408b516 src:manual/18-rozdily-fleshu.md:164 klas:E -->
### T-18-092 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Працює це чесно, але шар не безкоштовний ні за місцем, ні за швидкістю, а стійкості до зникнення живлення не додає.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

FAT має сенс в одному випадку: коли той самий носій (найчастіше картку
microSD) читатиме звичайний комп'ютер. На вбудованому флеші FAT сама по
собі не вирівнює знос — за це відповідає окремий шар `wear_levelling`,
який ESP-IDF підставляє під неї (`esp_vfs_fat_spiflash_mount_rw_wl`).
Працює це чесно, але шар не безкоштовний ні за місцем, ні за швидкістю,
а стійкості до зникнення живлення не додає. На картці — інша розмова
(розділ 49).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-093 sha:fdd40a10 src:manual/18-rozdily-fleshu.md:165 klas:E -->
### T-18-093 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> На картці — інша розмова (розділ 49).

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

FAT має сенс в одному випадку: коли той самий носій (найчастіше картку
microSD) читатиме звичайний комп'ютер. На вбудованому флеші FAT сама по
собі не вирівнює знос — за це відповідає окремий шар `wear_levelling`,
який ESP-IDF підставляє під неї (`esp_vfs_fat_spiflash_mount_rw_wl`).
Працює це чесно, але шар не безкоштовний ні за місцем, ні за швидкістю,
а стійкості до зникнення живлення не додає. На картці — інша розмова
(розділ 49).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-094 sha:38b96c9d src:manual/18-rozdily-fleshu.md:169 klas:A -->
### T-18-094 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Жодна файлова система на вбудованому флеші не переживе зникнення живлення **посеред запису** так, щоб гарантовано зберегти останній записаний файл.

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

::: zhyvlennya
Жодна файлова система на вбудованому флеші не переживе зникнення
живлення **посеред запису** так, щоб гарантовано зберегти останній
записаний файл. LittleFS гарантує, що ФС лишиться цілою і попередні дані
доступні, — це не те саме, що «нічого не втрачено». Для логера, який
пише постійно, це проєктне обмеження, а не деталь (розділ 60).
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/littlefs-project/littlefs/master/README.md
- **Дослівно з джерела:**
  > file updates are not actually committed to the filesystem until sync or close is called on the file
- **Спосіб і дата:** `curl` на `raw.githubusercontent.com`, гілка `master`, рядок 113. Документ отримано в цій сесії, витяг наведено дослівно — звідси клас `A`.
- **Нотатка:** Підтверджує твердження книги про найобережнішу з поширених ФС: littlefs дає атомарність операцій і відкат до останнього справного стану, але сам незавершений запис не зберігає. Формулювання в книзі лишено без змін.
- **Прохід:** pass-41-littlefs-vtrata-zhyvlennya

---

<!-- fc id:T-18-095 sha:0e9d20cb src:manual/18-rozdily-fleshu.md:171 klas:E -->
### T-18-095 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> LittleFS гарантує, що ФС лишиться цілою і попередні дані доступні, — це не те саме, що «нічого не втрачено».

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

::: zhyvlennya
Жодна файлова система на вбудованому флеші не переживе зникнення
живлення **посеред запису** так, щоб гарантовано зберегти останній
записаний файл. LittleFS гарантує, що ФС лишиться цілою і попередні дані
доступні, — це не те саме, що «нічого не втрачено». Для логера, який
пише постійно, це проєктне обмеження, а не деталь (розділ 60).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-096 sha:b760318d src:manual/18-rozdily-fleshu.md:172 klas:E -->
### T-18-096 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Для логера, який пише постійно, це проєктне обмеження, а не деталь (розділ 60).

**Контекст**

```
## Файлові системи: LittleFS, SPIFFS, FAT

::: zhyvlennya
Жодна файлова система на вбудованому флеші не переживе зникнення
живлення **посеред запису** так, щоб гарантовано зберегти останній
записаний файл. LittleFS гарантує, що ФС лишиться цілою і попередні дані
доступні, — це не те саме, що «нічого не втрачено». Для логера, який
пише постійно, це проєктне обмеження, а не деталь (розділ 60).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-097 sha:f48a238f src:manual/18-rozdily-fleshu.md:178 klas:E -->
### T-18-097 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Найчастіша причина міняти розбивку — застосунок переріс розділ.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

Найчастіша причина міняти розбивку — застосунок переріс розділ. Помилка
при збиранні виглядає прямо:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-098 sha:231194c9 src:manual/18-rozdily-fleshu.md:178 klas:E -->
### T-18-098 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Помилка при збиранні виглядає прямо:

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

Найчастіша причина міняти розбивку — застосунок переріс розділ. Помилка
при збиранні виглядає прямо:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-099 sha:7ab66916 src:manual/18-rozdily-fleshu.md:181 klas:K -->
### T-18-099 · kod · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> ```
> Error: app partition is too small for binary app.bin size 0x123456
> ```

**Контекст**

````
## Як змінити розбивку і не зламати пристрій

```
Error: app partition is too small for binary app.bin size 0x123456
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-100 sha:bc634816 src:manual/18-rozdily-fleshu.md:185 klas:E -->
### T-18-100 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Варіанти дій, у порядку від найдешевшого:

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

Варіанти дій, у порядку від найдешевшого:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-101 sha:a7b51adc src:manual/18-rozdily-fleshu.md:187 klas:F -->
### T-18-101 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **Прибрати зайве з прошивки.** Рівень логування, невикористані компоненти, оптимізація за розміром (`-Os`) у `menuconfig`.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

1. **Прибрати зайве з прошивки.** Рівень логування, невикористані
   компоненти, оптимізація за розміром (`-Os`) у `menuconfig`.
   `idf.py size` показує, хто саме займає місце.
2. **Взяти готову розбивку з більшим розділом застосунку** для вашого
   обсягу флешу.
3. **Написати власний CSV.**
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-102 sha:473a8f0b src:manual/18-rozdily-fleshu.md:189 klas:A -->
### T-18-102 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> `idf.py size` показує, хто саме займає місце. 2.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

1. **Прибрати зайве з прошивки.** Рівень логування, невикористані
   компоненти, оптимізація за розміром (`-Os`) у `menuconfig`.
   `idf.py size` показує, хто саме займає місце.
2. **Взяти готову розбивку з більшим розділом застосунку** для вашого
   обсягу флешу.
3. **Написати власний CSV.**
```

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

<!-- fc id:T-18-103 sha:d95fc6fa src:manual/18-rozdily-fleshu.md:190 klas:A -->
### T-18-103 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **Взяти готову розбивку з більшим розділом застосунку** для вашого обсягу флешу. 3.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

1. **Прибрати зайве з прошивки.** Рівень логування, невикористані
   компоненти, оптимізація за розміром (`-Os`) у `menuconfig`.
   `idf.py size` показує, хто саме займає місце.
2. **Взяти готову розбивку з більшим розділом застосунку** для вашого
   обсягу флешу.
3. **Написати власний CSV.**
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > The simplest way to use the partition table is to open the project configuration menu (``idf.py menuconfig``) and choose one of the simple predefined partition tables
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує наявність готових розбивок різних розмірів
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-104 sha:6364cfd3 src:manual/18-rozdily-fleshu.md:192 klas:E -->
### T-18-104 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **Написати власний CSV.**

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

1. **Прибрати зайве з прошивки.** Рівень логування, невикористані
   компоненти, оптимізація за розміром (`-Os`) у `menuconfig`.
   `idf.py size` показує, хто саме займає місце.
2. **Взяти готову розбивку з більшим розділом застосунку** для вашого
   обсягу флешу.
3. **Написати власний CSV.**
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

<!-- fc id:T-18-105 sha:85fee83d src:manual/18-rozdily-fleshu.md:195 klas:A -->
### T-18-105 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> **Зміна розбивки несумісна з OTA-оновленням.** Пристрій у полі отримує через OTA лише новий образ застосунку — таблиця розділів при цьому не оновлюється.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

::: nezvorotne
**Зміна розбивки несумісна з OTA-оновленням.** Пристрій у полі отримує
через OTA лише новий образ застосунку — таблиця розділів при цьому не
оновлюється. Якщо нова прошивка розрахована на іншу розбивку, вона або не
влізе, або запишеться поверх чужих даних.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/1c119dba-ota.rst
- **Дослівно з джерела:**
  > The OTA operation functions write a new app firmware image to whichever OTA app slot that is currently not selected for booting. Once the image is verified, the OTA Data partition is updated to specify that this image should be used for the next boot.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ підтверджує, що OTA оновлює лише образ застосунку, таблиця розділів не оновлюється.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-18-106 sha:18b9a9fd src:manual/18-rozdily-fleshu.md:197 klas:A -->
### T-18-106 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Якщо нова прошивка розрахована на іншу розбивку, вона або не влізе, або запишеться поверх чужих даних.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

::: nezvorotne
**Зміна розбивки несумісна з OTA-оновленням.** Пристрій у полі отримує
через OTA лише новий образ застосунку — таблиця розділів при цьому не
оновлюється. Якщо нова прошивка розрахована на іншу розбивку, вона або не
влізе, або запишеться поверх чужих даних.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > Note that updating the partition table does not erase data that may have been stored according to the old partition table.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує ризик перезапису даних при зміні розбивки
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-107 sha:9eebc20f src:manual/18-rozdily-fleshu.md:200 klas:A -->
### T-18-107 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Практично це означає: **розбивку треба обирати з запасом на самому початку**, до того, як перший пристрій поїхав до замовника.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

Практично це означає: **розбивку треба обирати з запасом на самому
початку**, до того, як перший пристрій поїхав до замовника. Змінити її
потім можна лише з фізичним доступом і повною перепрошивкою — а це
поїздка до кожного пристрою.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > Note that updating the partition table does not erase data that may have been stored according to the old partition table. You can use ``idf.py erase-flash`` (or ``esptool erase-flash``) to erase the entire flash contents.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує важливість раннього вибору розбивки
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-108 sha:e6335668 src:manual/18-rozdily-fleshu.md:201 klas:A -->
### T-18-108 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Змінити її потім можна лише з фізичним доступом і повною перепрошивкою — а це поїздка до кожного пристрою.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

Практично це означає: **розбивку треба обирати з запасом на самому
початку**, до того, як перший пристрій поїхав до замовника. Змінити її
потім можна лише з фізичним доступом і повною перепрошивкою — а це
поїздка до кожного пристрою.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > If Secure Boot V1 is enabled, then the partition of type ``app`` needs to have size aligned to 0x10000 (64 KB) boundary.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** показує, що зміна розбивки потребує перепрошивки
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-109 sha:40d6c1dc src:manual/18-rozdily-fleshu.md:206 klas:A -->
### T-18-109 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Другий наслідок того самого: якщо ви змінили розбивку, а на платі лишився старий NVS зі старої розбивки за іншою адресою — застосунок побачить сміття.

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

Другий наслідок того самого: якщо ви змінили розбивку, а на платі лишився
старий NVS зі старої розбивки за іншою адресою — застосунок побачить
сміття. Після зміни розбивки повна прошивка робиться з попереднім
`erase-flash` (і, звісно, з дампом до нього — картка [К2](#k-stan)).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > Note that updating the partition table does not erase data that may have been stored according to the old partition table.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує ризик конфлікту даних при зміні розбивки
- **Прохід:** prochid-18-rozdily-fleshu

---

<!-- fc id:T-18-110 sha:9b05e136 src:manual/18-rozdily-fleshu.md:208 klas:A -->
### T-18-110 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Після зміни розбивки повна прошивка робиться з попереднім `erase-flash` (і, звісно, з дампом до нього — картка [К2](#k-stan)).

**Контекст**

```
## Як змінити розбивку і не зламати пристрій

Другий наслідок того самого: якщо ви змінили розбивку, а на платі лишився
старий NVS зі старої розбивки за іншою адресою — застосунок побачить
сміття. Після зміни розбивки повна прошивка робиться з попереднім
`erase-flash` (і, звісно, з дампом до нього — картка [К2](#k-stan)).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > (partition-tables.rst)
  > Note that updating the partition table does not erase data that may
  > have been stored according to the old partition table. You can use
  > ``idf.py erase-flash`` (or ``esptool.py erase_flash``) to erase the
  > entire flash contents.
  > 
  > (basic-commands.rst)
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  >     esptool erase-flash
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Порада книги підтверджена з обох боків: документація прямо каже, що зміна таблиці **не стирає** даних за старою розбивкою, а `erase-flash` замінює все на `0xFF`.
Агент чесно позначив, що «незворотний» — висновок книги, а не речення джерела. Погоджуюся й лишаю клас `A`: із «все замінюється на `0xFF`» незворотність випливає однозначно, а не правдоподібно. Межа між `A` і `B` тут саме в цьому — чи є інший можливий висновок. Тут немає.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-111 sha:56304439 src:manual/18-rozdily-fleshu.md:213 klas:B -->
### T-18-111 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Орієнтири для типового пристрою на 4 МБ флешу:

**Контекст**

```
## Скільки чого відводити

Орієнтири для типового пристрою на 4 МБ флешу:
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > flash capacity and partition allocation
- **Спосіб і дата:** curl esp-idf partition-tables.rst, 2026-08-26
- **Нотатка:** Текст T-17-041 згадує 2 МБ та 4 МБ флешу в модулях. Джерело обговорює розподіл флешу залежно від його розміру.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-18-112 sha:863a7fb3 src:manual/18-rozdily-fleshu.md:215 klas:D -->
### T-18-112 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> - `nvs` — `0x6000` (24 КБ) вистачає, поки ви не складаєте туди масиви.

**Контекст**

```
## Скільки чого відводити

- `nvs` — `0x6000` (24 КБ) вистачає, поки ви не складаєте туди масиви.
- Застосунок з Wi-Fi і TLS — від 1 МБ. З BLE — більше.
- Дві OTA-області означають **подвоєння** місця під застосунок: два по
  1.5 МБ — це 3 МБ із приблизно 3.9 МБ, доступних після службових
  областей. На все інше лишається менш ніж мегабайт.
- Файлова система — те, що лишилося.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arithmetic.py
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
- **Спосіб і дата:** python3 tools/arithmetic.py, 2026-08-26
- **Нотатка:** Перевірку внесено в `make check` окремою ціллю `arytmetyka`. Це відповідь на те, як у книгу колись потрапили значення `duty` для серво від іншої роздільності: абзац із неправильним добутком внутрішньо несуперечливий і зовнішнього джерела не потребує, тож ні читання, ні звірка з першоджерелом його не ловлять. Ловить лише калькулятор — і тепер він запускається сам.
- **Прохід:** pass-05-obchyslennya

---

<!-- fc id:T-18-113 sha:32ebab82 src:manual/18-rozdily-fleshu.md:216 klas:L -->
### T-18-113 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> - Застосунок з Wi-Fi і TLS — від 1 МБ.

**Контекст**

```
## Скільки чого відводити

- `nvs` — `0x6000` (24 КБ) вистачає, поки ви не складаєте туди масиви.
- Застосунок з Wi-Fi і TLS — від 1 МБ. З BLE — більше.
- Дві OTA-області означають **подвоєння** місця під застосунок: два по
  1.5 МБ — це 3 МБ із приблизно 3.9 МБ, доступних після службових
  областей. На все інше лишається менш ніж мегабайт.
- Файлова система — те, що лишилося.
```

**Доказ**

- **Клас:** 🔎 L — дивилися й не знайшли — робота зроблена, джерела не видно
- **Спосіб і дата:** Емпіричне вимірювання або документація про розмір складових IDF
- **Що шукати в джерелі:** Розмір застосунку, Wi-Fi, TLS, флеш пам'ять
- **Нотатка:** Твердження про розмір застосунку. Це може бути емпіричним спостереженням або витягом із документації IDF про розміри компонентів. Джерело не знайшло. | 2026-08-28, §5 аудиту: клас named-unreachable (C) вимагає НАЗВАНОГО документа — у цьому записі його не було, стояла лише тема в look_for. За власним законом: не можеш назвати документ — це не C, а unverified. Тему збережено в look_for як підказку, куди дивитися, але це не наряд.
2026-08-28: клас unverified був хибним — F означає відсутність доказу, тобто доказ про те, що доказу немає. Шукав; що саме відкривав — у looked_at. Клас L лишає одиницю в черзі видимою, на відміну від E, який ховає її назавжди.
- **Прохід:** m2-97-vybirka

---

<!-- fc id:T-18-114 sha:52f12d51 src:manual/18-rozdily-fleshu.md:217 klas:D -->
### T-18-114 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> - Дві OTA-області означають **подвоєння** місця під застосунок: два по 1.5 МБ — це 3 МБ із приблизно 3.9 МБ, доступних після службових областей.

**Контекст**

```
## Скільки чого відводити

- `nvs` — `0x6000` (24 КБ) вистачає, поки ви не складаєте туди масиви.
- Застосунок з Wi-Fi і TLS — від 1 МБ. З BLE — більше.
- Дві OTA-області означають **подвоєння** місця під застосунок: два по
  1.5 МБ — це 3 МБ із приблизно 3.9 МБ, доступних після службових
  областей. На все інше лишається менш ніж мегабайт.
- Файлова система — те, що лишилося.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arithmetic.py
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
- **Спосіб і дата:** python3 tools/arithmetic.py, 2026-08-26
- **Нотатка:** Перевірку внесено в `make check` окремою ціллю `arytmetyka`. Це відповідь на те, як у книгу колись потрапили значення `duty` для серво від іншої роздільності: абзац із неправильним добутком внутрішньо несуперечливий і зовнішнього джерела не потребує, тож ні читання, ні звірка з першоджерелом його не ловлять. Ловить лише калькулятор — і тепер він запускається сам.
- **Прохід:** pass-05-obchyslennya

---

<!-- fc id:T-18-115 sha:5b4060f0 src:manual/18-rozdily-fleshu.md:219 klas:E -->
### T-18-115 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> На все інше лишається менш ніж мегабайт.

**Контекст**

```
## Скільки чого відводити

- `nvs` — `0x6000` (24 КБ) вистачає, поки ви не складаєте туди масиви.
- Застосунок з Wi-Fi і TLS — від 1 МБ. З BLE — більше.
- Дві OTA-області означають **подвоєння** місця під застосунок: два по
  1.5 МБ — це 3 МБ із приблизно 3.9 МБ, доступних після службових
  областей. На все інше лишається менш ніж мегабайт.
- Файлова система — те, що лишилося.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-116 sha:b8548325 src:manual/18-rozdily-fleshu.md:220 klas:E -->
### T-18-116 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> - Файлова система — те, що лишилося.

**Контекст**

```
## Скільки чого відводити

- `nvs` — `0x6000` (24 КБ) вистачає, поки ви не складаєте туди масиви.
- Застосунок з Wi-Fi і TLS — від 1 МБ. З BLE — більше.
- Дві OTA-області означають **подвоєння** місця під застосунок: два по
  1.5 МБ — це 3 МБ із приблизно 3.9 МБ, доступних після службових
  областей. На все інше лишається менш ніж мегабайт.
- Файлова система — те, що лишилося.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-117 sha:535138f3 src:manual/18-rozdily-fleshu.md:223 klas:B -->
### T-18-117 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Плати з 4 МБ флешу — стандарт і найдешевші, і для більшості задач їх вистачає.

**Контекст**

```
## Скільки чого відводити

::: zakupivlya
Плати з 4 МБ флешу — стандарт і найдешевші, і для більшості задач їх
вистачає. Але як тільки в задачі з'являється OTA **разом із** веб-інтерфейсом
або великими ресурсами, 4 МБ стають тісними. Модулі на 8 і 16 МБ коштують
відчутно дорожче за різницю в ціні флешу — а от переробляти виріб під
інший модуль на пізньому етапі дорожче в рази. Це та економія, яку варто
рахувати на початку.
:::
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > flash capacity and partition allocation
- **Спосіб і дата:** curl esp-idf partition-tables.rst, 2026-08-26
- **Нотатка:** Текст T-17-041 згадує 2 МБ та 4 МБ флешу в модулях. Джерело обговорює розподіл флешу залежно від його розміру.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-18-118 sha:255c3b69 src:manual/18-rozdily-fleshu.md:224 klas:B -->
### T-18-118 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Але як тільки в задачі з'являється OTA **разом із** веб-інтерфейсом або великими ресурсами, 4 МБ стають тісними.

**Контекст**

```
## Скільки чого відводити

::: zakupivlya
Плати з 4 МБ флешу — стандарт і найдешевші, і для більшості задач їх
вистачає. Але як тільки в задачі з'являється OTA **разом із** веб-інтерфейсом
або великими ресурсами, 4 МБ стають тісними. Модулі на 8 і 16 МБ коштують
відчутно дорожче за різницю в ціні флешу — а от переробляти виріб під
інший модуль на пізньому етапі дорожче в рази. Це та економія, яку варто
рахувати на початку.
:::
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > flash capacity and partition allocation
- **Спосіб і дата:** curl esp-idf partition-tables.rst, 2026-08-26
- **Нотатка:** Текст T-17-041 згадує 2 МБ та 4 МБ флешу в модулях. Джерело обговорює розподіл флешу залежно від його розміру.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-18-119 sha:e612ab0d src:manual/18-rozdily-fleshu.md:225 klas:E -->
### T-18-119 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Модулі на 8 і 16 МБ коштують відчутно дорожче за різницю в ціні флешу — а от переробляти виріб під інший модуль на пізньому етапі дорожче в рази.

**Контекст**

```
## Скільки чого відводити

::: zakupivlya
Плати з 4 МБ флешу — стандарт і найдешевші, і для більшості задач їх
вистачає. Але як тільки в задачі з'являється OTA **разом із** веб-інтерфейсом
або великими ресурсами, 4 МБ стають тісними. Модулі на 8 і 16 МБ коштують
відчутно дорожче за різницю в ціні флешу — а от переробляти виріб під
інший модуль на пізньому етапі дорожче в рази. Це та економія, яку варто
рахувати на початку.
:::
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Спосіб і дата:** Економічний аналіз ринку модулів ESP32. Спостереження без цифрових джерел.
- **Нотатка:** Твердження описує тенденцію на ринку модулів — що більші флеш-модулі мають вищу вартість на одиницю ємності. Це економічне спостереження, не технічна специфікація. Конкретного документа з цінами не існує (ціни змінюються). Клас E: джерела немає. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-95-vybirka

---

<!-- fc id:T-18-120 sha:a369ddd0 src:manual/18-rozdily-fleshu.md:227 klas:E -->
### T-18-120 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Це та економія, яку варто рахувати на початку.

**Контекст**

```
## Скільки чого відводити

::: zakupivlya
Плати з 4 МБ флешу — стандарт і найдешевші, і для більшості задач їх
вистачає. Але як тільки в задачі з'являється OTA **разом із** веб-інтерфейсом
або великими ресурсами, 4 МБ стають тісними. Модулі на 8 і 16 МБ коштують
відчутно дорожче за різницю в ціні флешу — а от переробляти виріб під
інший модуль на пізньому етапі дорожче в рази. Це та економія, яку варто
рахувати на початку.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-121 sha:11073fc5 src:manual/18-rozdily-fleshu.md:233 klas:A -->
### T-18-121 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Таблиця розділів лежить на `0x8000` і друкується в boot-лозі при кожному старті — найдешевший спосіб дізнатися, що всередині чужого пристрою.

**Контекст**

```
## Що з цього треба запам'ятати

Таблиця розділів лежить на `0x8000` і друкується в boot-лозі при кожному
старті — найдешевший спосіб дізнатися, що всередині чужого пристрою.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та .../components/bootloader_support/src/bootloader_utility.c
- **Дослівно з джерела:**
  > # ESP-IDF Partition Table
  > # Name,   Type, SubType, Offset,  Size, Flags
  > nvs,      data, nvs,     0x9000,  0x6000,
  > phy_init, data, phy,     0xf000,  0x1000,
  > factory,  app,  factory, 0x10000, 1M,
  > 
  > In both cases the factory app is flashed at offset 0x10000.
  > 
  > Sizes and offsets can be specified as decimal numbers, hex numbers
  > with the prefix 0x, or size multipliers K or M (1024 and 1024*1024
  > bytes).
  > 
  > (bootloader_utility.c)
  > ESP_LOGI(TAG, "Partition Table:");
  > ESP_LOGI(TAG, "## Label            Usage          Type ST Offset   Length");
  > …
  > ESP_LOGI(TAG, "End of partition table");
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Уся типова розбивка книги збіглася з тією, що друкує сама документація ESP-IDF, — рядок у рядок.
Окремо цінне: агент знайшов **у коді бутлоадера** рядки, якими таблиця друкується в лог. Книга обіцяє читачеві, що розбивку чужого пристрою видно в boot-лозі без жодних інструментів; тепер це підтверджено не документацією, а самою функцією, яка це друкує.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-122 sha:1a134448 src:manual/18-rozdily-fleshu.md:236 klas:F -->
### T-18-122 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> NVS переживає оновлення прошивки, і саме тому там живе все, що конкретне для екземпляра.

**Контекст**

```
## Що з цього треба запам'ятати

NVS переживає оновлення прошивки, і саме тому там живе все, що конкретне
для екземпляра. І саме тому `erase-flash` без дампа незворотний.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-123 sha:c0b50278 src:manual/18-rozdily-fleshu.md:237 klas:A -->
### T-18-123 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> І саме тому `erase-flash` без дампа незворотний.

**Контекст**

```
## Що з цього треба запам'ятати

NVS переживає оновлення прошивки, і саме тому там живе все, що конкретне
для екземпляра. І саме тому `erase-flash` без дампа незворотний.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > (partition-tables.rst)
  > Note that updating the partition table does not erase data that may
  > have been stored according to the old partition table. You can use
  > ``idf.py erase-flash`` (or ``esptool.py erase_flash``) to erase the
  > entire flash contents.
  > 
  > (basic-commands.rst)
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  >     esptool erase-flash
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 2), 2026-08-26; взірець і клас — М1
- **Нотатка:** Порада книги підтверджена з обох боків: документація прямо каже, що зміна таблиці **не стирає** даних за старою розбивкою, а `erase-flash` замінює все на `0xFF`.
Агент чесно позначив, що «незворотний» — висновок книги, а не речення джерела. Погоджуюся й лишаю клас `A`: із «все замінюється на `0xFF`» незворотність випливає однозначно, а не правдоподібно. Межа між `A` і `B` тут саме в цьому — чи є інший можливий висновок. Тут немає.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-18-124 sha:b3601380 src:manual/18-rozdily-fleshu.md:239 klas:F -->
### T-18-124 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> LittleFS замість SPIFFS у будь-якому новому проєкті.

**Контекст**

```
## Що з цього треба запам'ятати

LittleFS замість SPIFFS у будь-якому новому проєкті.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-18-125 sha:68676e42 src:manual/18-rozdily-fleshu.md:241 klas:F -->
### T-18-125 · proza · `manual/18-rozdily-fleshu.md`

**Твердження, коротко**

> Розбивку обирають один раз, на початку, з запасом: OTA її не оновлює, а зміна потім вимагає фізичного доступу до кожного пристрою.

**Контекст**

```
## Що з цього треба запам'ятати

Розбивку обирають один раз, на початку, з запасом: OTA її не оновлює, а
зміна потім вимагає фізичного доступу до кожного пристрою.
```

**Доказ**

- **Клас:** F — не звірено

---
