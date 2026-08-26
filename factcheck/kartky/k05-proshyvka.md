# Фактчекінг: `kartky/k05-proshyvka.md`

Одиниць твердження: **26**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K05-001 sha:91a0e481 src:kartky/k05-proshyvka.md:3 klas:F -->
### T-K05-001 · proza · рядок 3

**Книга каже, дослівно:**

> Прошити зібраний кимось образ, не збираючи проєкт.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-002 sha:2e1573f8 src:kartky/k05-proshyvka.md:7 klas:F -->
### T-K05-002 · proza · рядок 7

**Книга каже, дослівно:**

> Повна прошивка ESP-IDF — це три файли, кожен на своїй адресі:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-003 sha:ad965e81 src:kartky/k05-proshyvka.md:9 klas:F -->
### T-K05-003 · tablycya · рядок 9

**Книга каже, дослівно:**

> | Файл | Що це | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-004 sha:6d834a4f src:kartky/k05-proshyvka.md:11 klas:F -->
### T-K05-004 · tablycya · рядок 11

**Книга каже, дослівно:**

> | `bootloader.bin` | другий бутлоадер | `0x1000` | `0x0` | `0x2000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-005 sha:14c45987 src:kartky/k05-proshyvka.md:12 klas:A -->
### T-K05-005 · tablycya · рядок 12

**Книга каже, дослівно:**

> | `partition-table.bin` | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |

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

<!-- fc id:T-K05-006 sha:7ed729e8 src:kartky/k05-proshyvka.md:13 klas:F -->
### T-K05-006 · tablycya · рядок 13

**Книга каже, дослівно:**

> | застосунок `.bin` | сама програма | `0x10000` | `0x10000` | `0x10000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-007 sha:efc6c6df src:kartky/k05-proshyvka.md:16 klas:F -->
### T-K05-007 · proza · рядок 16

**Книга каже, дослівно:**

> Різниця в адресі бутлоадера — найчастіша причина «прошилося без помилок, але плата мовчить».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-008 sha:14934f37 src:kartky/k05-proshyvka.md:16 klas:F -->
### T-K05-008 · proza · рядок 16

**Книга каже, дослівно:**

> Команда з інструкції для ESP32 classic кладе бутлоадер S3 на `0x1000`, тобто не туди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-009 sha:4188b893 src:kartky/k05-proshyvka.md:16 klas:F -->
### T-K05-009 · proza · рядок 16

**Книга каже, дослівно:**

> Спершу визначити чип (картка К1), потім брати адресу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-010 sha:911de04d src:kartky/k05-proshyvka.md:24 klas:F -->
### T-K05-010 · kod · рядок 24

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-011 sha:0e7ce691 src:kartky/k05-proshyvka.md:31 klas:F -->
### T-K05-011 · proza · рядок 31

**Книга каже, дослівно:**

> ⚠ У команді вище стоїть `0x1000` — адреса **classic і S2**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-012 sha:308e3d3b src:kartky/k05-proshyvka.md:31 klas:F -->
### T-K05-012 · proza · рядок 31

**Книга каже, дослівно:**

> Для решти чипів перший рядок інший: див. таблицю вище.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-013 sha:4b49ff3c src:kartky/k05-proshyvka.md:31 klas:A -->
### T-K05-013 · proza · рядок 31

**Книга каже, дослівно:**

> Правила «що новіше, то ближче до нуля» немає — адресу задає ROM чипа.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     hex
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     # the first 2 sectors are reserved for the key manager with AES-XTS (flash encryption) purpose
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Перша редакція давала двовипадкове правило «classic і S2 → 0x1000, S3, C3 і новіші → 0x0». Третій випадок (P4, C5, H4 → 0x2000) робив формулювання «і новіші» хибним, причому саме для тих чипів, які найновіші. Виправлено в розділах 16, 17, 21, 29, картках К5 і К10, додатку C. Довідка Kconfig дала й формулювання для правила: значення визначає ROM, воно не налаштовується.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-K05-014 sha:a5f80c6b src:kartky/k05-proshyvka.md:35 klas:F -->
### T-K05-014 · proza · рядок 35

**Книга каже, дослівно:**

> `-z` вмикає стиснення — швидше і безпечніше для довгих кабелів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-015 sha:ca260535 src:kartky/k05-proshyvka.md:35 klas:F -->
### T-K05-015 · proza · рядок 35

**Книга каже, дослівно:**

> Не з'єднується — знизити до `--baud 115200`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-016 sha:18bb88d3 src:kartky/k05-proshyvka.md:38 klas:F -->
### T-K05-016 · proza · рядок 38

**Книга каже, дослівно:**

> Якщо образ **один** файл (зібраний через `merge-bin`), адреса завжди `0x0`, незалежно від сімейства чипа: зсуви вже всередині файлу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-017 sha:1df68ffb src:kartky/k05-proshyvka.md:41 klas:F -->
### T-K05-017 · kod · рядок 41

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 write-flash 0x0 merged.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-018 sha:953c7797 src:kartky/k05-proshyvka.md:47 klas:F -->
### T-K05-018 · proza · рядок 47

**Книга каже, дослівно:**

> Команди вище — для esptool v5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-019 sha:d4137943 src:kartky/k05-proshyvka.md:47 klas:F -->
### T-K05-019 · proza · рядок 47

**Книга каже, дослівно:**

> Якщо у вас v4 (іде з ESP-IDF 5.x), то замість дефісів підкреслення і потрібен суфікс `.py`:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-020 sha:09ccdb8d src:kartky/k05-proshyvka.md:50 klas:F -->
### T-K05-020 · kod · рядок 50

**Книга каже, дослівно:**

> ```
> esptool.py --port /dev/ttyUSB0 write_flash -z 0x1000 bootloader.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-021 sha:9b34572c src:kartky/k05-proshyvka.md:54 klas:F -->
### T-K05-021 · proza · рядок 54

**Книга каже, дослівно:**

> Перевірити свою версію: `esptool version` або `esptool.py version`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-022 sha:ba1c09bd src:kartky/k05-proshyvka.md:58 klas:F -->
### T-K05-022 · proza · рядок 58

**Книга каже, дослівно:**

> Не «прошилося без помилок», а:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-023 sha:f9a95e16 src:kartky/k05-proshyvka.md:60 klas:F -->
### T-K05-023 · proza · рядок 60

**Книга каже, дослівно:**

> `esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin` — звіряє вміст флешу з файлом; 2. відкрити монітор на 115200 і скинути плату кнопкою `EN`; 3. прочитати boot-лог (картка К6).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-024 sha:ae4eb4e6 src:kartky/k05-proshyvka.md:65 klas:F -->
### T-K05-024 · proza · рядок 65

**Книга каже, дослівно:**

> Прошивка вважається успішною тільки після третього пункту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-025 sha:631e8856 src:kartky/k05-proshyvka.md:68 klas:F -->
### T-K05-025 · proza · рядок 68

**Книга каже, дослівно:**

> Дамп флешу зняти **до** прошивки, не після (картка К2).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K05-026 sha:f5bd92cd src:kartky/k05-proshyvka.md:68 klas:F -->
### T-K05-026 · proza · рядок 68

**Книга каже, дослівно:**

> Після `write-flash` початкового вмісту вже немає.

**Доказ**

- **Клас:** F — не звірено

---
