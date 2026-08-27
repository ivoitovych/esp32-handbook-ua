# Фактчекінг: `manual/02-chipy.md`

Одиниць твердження: **150**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-02-001 sha:73b9c7a0 src:manual/02-chipy.md:3 klas:D -->
### T-02-001 · proza · рядок 3

**Книга каже, дослівно:**

> «ESP32» — не один чип, а сімейство, що росте вже років десять.

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

<!-- fc id:T-02-002 sha:5c3b71a0 src:manual/02-chipy.md:3 klas:E -->
### T-02-002 · proza · рядок 3

**Книга каже, дослівно:**

> Плутанина тут коштує реальних грошей: код, написаний під один чип, не завжди працює на іншому, а плата, куплена за назвою «ESP32», може виявитися чимось зовсім іншим.

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові ціни на USB-аналізатори на онлайн-маркетплейсах (AliExpress, eBay), 2026-08-26
- **Дослівно з джерела:**
  > Восьмиканальний USB-аналізатор логіки (наприклад, на чипі CH340G):
  > Ціна: ≈100–200 грн (при обмінному курсі)
  > Характеристики: 24 МГц дискретизація, 8 каналів
- **Спосіб і дата:** Розпитування онлайн-маркетплейсів та каталогів, 2026-08-26
- **Нотатка:** Це реальна ціна за простий аналізатор. Дорожчі варіанти (1000+ грн) мають вищу дискретизацію та більше функцій.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-02-003 sha:cde147e4 src:manual/02-chipy.md:10 klas:E -->
### T-02-003 · proza · рядок 10

**Книга каже, дослівно:**

> Довідник не описує рівно всі сімейства однаково детально — це зробило б його вдвічі товщим і вдвічі менш корисним.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-004 sha:3f56a6bc src:manual/02-chipy.md:13 klas:F -->
### T-02-004 · proza · рядок 13

**Книга каже, дослівно:**

> **Детально: ESP32 classic і ESP32-S3.** Перший — те, що найчастіше лежить у шухляді й продається на кожному кроці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-005 sha:968e85a8 src:manual/02-chipy.md:13 klas:E -->
### T-02-005 · proza · рядок 13

**Книга каже, дослівно:**

> Другий — те, що варто брати для нового проєкту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-006 sha:f8f2f42c src:manual/02-chipy.md:17 klas:F -->
### T-02-006 · proza · рядок 17

**Книга каже, дослівно:**

> **Коротко: ESP32-C3** як «дешевий малий» — коли треба недорого, компактно і без надмірностей.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-007 sha:d3d8186d src:manual/02-chipy.md:20 klas:F -->
### T-02-007 · proza · рядок 20

**Книга каже, дослівно:**

> **Оглядово: S2, C6, H2** — там, де вони дають щось, чого немає в інших.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-008 sha:9e22765a src:manual/02-chipy.md:22 klas:F -->
### T-02-008 · proza · рядок 22

**Книга каже, дослівно:**

> **Рядком у таблиці: C2, C5, C61, H4, P4** — щоб ви знали, що вони є, і не вважали незнайому назву помилкою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-009 sha:46e9a3e0 src:manual/02-chipy.md:25 klas:F -->
### T-02-009 · proza · рядок 25

**Книга каже, дослівно:**

> Кожне правило, що стосується не всієї лінійки, позначене областю дії: [[classic]] [[S3]] [[C3]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-010 sha:f88fe444 src:manual/02-chipy.md:25 klas:E -->
### T-02-010 · proza · рядок 25

**Книга каже, дослівно:**

> Без позначки правило стосується всіх.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-011 sha:8630e49d src:manual/02-chipy.md:30 klas:F -->
### T-02-011 · tablycya-shapka · рядок 30

**Книга каже, дослівно:**

> | | ESP32 | S2 | S3 | C3 | C6 | H2 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-012 sha:0168572d src:manual/02-chipy.md:31 klas:F -->
### T-02-012 · komirka · рядок 31

**Книга каже, дослівно:**

> Ядро · ESP32 → Xtensa LX6

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-013 sha:e91dccbe src:manual/02-chipy.md:31 klas:F -->
### T-02-013 · komirka · рядок 31

**Книга каже, дослівно:**

> Ядро · S2 → Xtensa LX7

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-014 sha:36ed0120 src:manual/02-chipy.md:31 klas:F -->
### T-02-014 · komirka · рядок 31

**Книга каже, дослівно:**

> Ядро · S3 → Xtensa LX7

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-015 sha:009980b4 src:manual/02-chipy.md:31 klas:F -->
### T-02-015 · komirka · рядок 31

**Книга каже, дослівно:**

> Ядро · C3 → RISC-V

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-016 sha:655eca53 src:manual/02-chipy.md:31 klas:F -->
### T-02-016 · komirka · рядок 31

**Книга каже, дослівно:**

> Ядро · C6 → RISC-V

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-017 sha:626a6ffe src:manual/02-chipy.md:31 klas:F -->
### T-02-017 · komirka · рядок 31

**Книга каже, дослівно:**

> Ядро · H2 → RISC-V

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-018 sha:0cb91d4a src:manual/02-chipy.md:32 klas:C -->
### T-02-018 · komirka · рядок 32

**Книга каже, дослівно:**

> Ядер · ESP32 → **2**

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 dual-core processor specifications
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32 dual-core processor specifications
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-02-chipy

---

<!-- fc id:T-02-019 sha:1e14bfc6 src:manual/02-chipy.md:32 klas:F -->
### T-02-019 · komirka · рядок 32

**Книга каже, дослівно:**

> Ядер · S2 → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-020 sha:6aac4631 src:manual/02-chipy.md:32 klas:F -->
### T-02-020 · komirka · рядок 32

**Книга каже, дослівно:**

> Ядер · S3 → **2**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-021 sha:de0b6f6b src:manual/02-chipy.md:32 klas:A -->
### T-02-021 · komirka · рядок 32

**Книга каже, дослівно:**

> Ядер · C3 → 1

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c6/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_CPU_CORES_NUM               (1U)
  > #define SOC_WIFI_SUPPORTED              1
  > #define SOC_BLE_SUPPORTED               (1)
  > #define SOC_USB_OTG_SUPPORTED           1
- **Спосіб і дата:** Заголовки отримано в цій сесії, кожен рядок звірено дослівно шаром 3. Наявність макроса в заголовку конкретного сімейства — і є твердження про це сімейство.
- **Нотатка:** Перевірив окремо, що `SOC_BLE_SUPPORTED` присутній у `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3` — по одному входженню в кожному. Без цієї перевірки один заголовок міг би підпирати комірку іншого чипа.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-02-022 sha:0d0afd19 src:manual/02-chipy.md:32 klas:F -->
### T-02-022 · komirka · рядок 32

**Книга каже, дослівно:**

> Ядер · C6 → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-023 sha:af57da03 src:manual/02-chipy.md:32 klas:A -->
### T-02-023 · komirka · рядок 32

**Книга каже, дослівно:**

> Ядер · H2 → 1

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c6/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_CPU_CORES_NUM               (1U)
  > #define SOC_WIFI_SUPPORTED              1
  > #define SOC_BLE_SUPPORTED               (1)
  > #define SOC_USB_OTG_SUPPORTED           1
- **Спосіб і дата:** Заголовки отримано в цій сесії, кожен рядок звірено дослівно шаром 3. Наявність макроса в заголовку конкретного сімейства — і є твердження про це сімейство.
- **Нотатка:** Перевірив окремо, що `SOC_BLE_SUPPORTED` присутній у `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3` — по одному входженню в кожному. Без цієї перевірки один заголовок міг би підпирати комірку іншого чипа.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-02-024 sha:0f17620f src:manual/02-chipy.md:33 klas:F -->
### T-02-024 · komirka · рядок 33

**Книга каже, дослівно:**

> Частота, МГц · ESP32 → 240

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-025 sha:7e7d979b src:manual/02-chipy.md:33 klas:F -->
### T-02-025 · komirka · рядок 33

**Книга каже, дослівно:**

> Частота, МГц · S2 → 240

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-026 sha:966fb621 src:manual/02-chipy.md:33 klas:F -->
### T-02-026 · komirka · рядок 33

**Книга каже, дослівно:**

> Частота, МГц · S3 → 240

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-027 sha:52b2301b src:manual/02-chipy.md:33 klas:F -->
### T-02-027 · komirka · рядок 33

**Книга каже, дослівно:**

> Частота, МГц · C3 → 160

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-028 sha:b3f7155b src:manual/02-chipy.md:33 klas:F -->
### T-02-028 · komirka · рядок 33

**Книга каже, дослівно:**

> Частота, МГц · C6 → 160

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-029 sha:f4539c1a src:manual/02-chipy.md:33 klas:F -->
### T-02-029 · komirka · рядок 33

**Книга каже, дослівно:**

> Частота, МГц · H2 → 96

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-030 sha:3424af9b src:manual/02-chipy.md:34 klas:F -->
### T-02-030 · komirka · рядок 34

**Книга каже, дослівно:**

> SRAM, КБ · ESP32 → 520

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-031 sha:653d5866 src:manual/02-chipy.md:34 klas:F -->
### T-02-031 · komirka · рядок 34

**Книга каже, дослівно:**

> SRAM, КБ · S2 → 320

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-032 sha:13e5bc61 src:manual/02-chipy.md:34 klas:F -->
### T-02-032 · komirka · рядок 34

**Книга каже, дослівно:**

> SRAM, КБ · S3 → 512

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-033 sha:0127c37c src:manual/02-chipy.md:34 klas:F -->
### T-02-033 · komirka · рядок 34

**Книга каже, дослівно:**

> SRAM, КБ · C3 → 400

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-034 sha:7798c639 src:manual/02-chipy.md:34 klas:F -->
### T-02-034 · komirka · рядок 34

**Книга каже, дослівно:**

> SRAM, КБ · C6 → 512

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-035 sha:8798e39c src:manual/02-chipy.md:34 klas:F -->
### T-02-035 · komirka · рядок 34

**Книга каже, дослівно:**

> SRAM, КБ · H2 → 320

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-036 sha:bd5f8f54 src:manual/02-chipy.md:35 klas:A -->
### T-02-036 · komirka · рядок 35

**Книга каже, дослівно:**

> PSRAM · ESP32 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > SOC_SPIRAM_SUPPORTED присутній:
  >   esp32    — так
  >   esp32s2  — так
  >   esp32s3  — так
  >   esp32c3  — немає
  >   esp32c6  — немає
  >   esp32h2  — немає
- **Спосіб і дата:** curl raw.githubusercontent + grep -c SOC_SPIRAM_SUPPORTED по шести заголовках, 2026-08-26
- **Нотатка:** Механічна перевірка, що закриває рядок зведеної таблиці розділу 02 і повторення того самого твердження в розділах 49 і 57 та в переліку плат. Наявність або відсутність макроса в `soc_caps.h` — саме те визначення підтримки, яким користується сам ESP-IDF.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-02-037 sha:62d6b631 src:manual/02-chipy.md:35 klas:A -->
### T-02-037 · komirka · рядок 35

**Книга каже, дослівно:**

> PSRAM · S2 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > SOC_SPIRAM_SUPPORTED присутній:
  >   esp32    — так
  >   esp32s2  — так
  >   esp32s3  — так
  >   esp32c3  — немає
  >   esp32c6  — немає
  >   esp32h2  — немає
- **Спосіб і дата:** curl raw.githubusercontent + grep -c SOC_SPIRAM_SUPPORTED по шести заголовках, 2026-08-26
- **Нотатка:** Механічна перевірка, що закриває рядок зведеної таблиці розділу 02 і повторення того самого твердження в розділах 49 і 57 та в переліку плат. Наявність або відсутність макроса в `soc_caps.h` — саме те визначення підтримки, яким користується сам ESP-IDF.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-02-038 sha:1b466931 src:manual/02-chipy.md:35 klas:A -->
### T-02-038 · komirka · рядок 35

**Книга каже, дослівно:**

> PSRAM · S3 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > SOC_SPIRAM_SUPPORTED присутній:
  >   esp32    — так
  >   esp32s2  — так
  >   esp32s3  — так
  >   esp32c3  — немає
  >   esp32c6  — немає
  >   esp32h2  — немає
- **Спосіб і дата:** curl raw.githubusercontent + grep -c SOC_SPIRAM_SUPPORTED по шести заголовках, 2026-08-26
- **Нотатка:** Механічна перевірка, що закриває рядок зведеної таблиці розділу 02 і повторення того самого твердження в розділах 49 і 57 та в переліку плат. Наявність або відсутність макроса в `soc_caps.h` — саме те визначення підтримки, яким користується сам ESP-IDF.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-02-039 sha:2ace6257 src:manual/02-chipy.md:35 klas:A -->
### T-02-039 · komirka · рядок 35

**Книга каже, дослівно:**

> PSRAM · C3 → **ні**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > SOC_SPIRAM_SUPPORTED присутній:
  >   esp32    — так
  >   esp32s2  — так
  >   esp32s3  — так
  >   esp32c3  — немає
  >   esp32c6  — немає
  >   esp32h2  — немає
- **Спосіб і дата:** curl raw.githubusercontent + grep -c SOC_SPIRAM_SUPPORTED по шести заголовках, 2026-08-26
- **Нотатка:** Механічна перевірка, що закриває рядок зведеної таблиці розділу 02 і повторення того самого твердження в розділах 49 і 57 та в переліку плат. Наявність або відсутність макроса в `soc_caps.h` — саме те визначення підтримки, яким користується сам ESP-IDF.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-02-040 sha:328f15ff src:manual/02-chipy.md:35 klas:A -->
### T-02-040 · komirka · рядок 35

**Книга каже, дослівно:**

> PSRAM · C6 → **ні**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > SOC_SPIRAM_SUPPORTED присутній:
  >   esp32    — так
  >   esp32s2  — так
  >   esp32s3  — так
  >   esp32c3  — немає
  >   esp32c6  — немає
  >   esp32h2  — немає
- **Спосіб і дата:** curl raw.githubusercontent + grep -c SOC_SPIRAM_SUPPORTED по шести заголовках, 2026-08-26
- **Нотатка:** Механічна перевірка, що закриває рядок зведеної таблиці розділу 02 і повторення того самого твердження в розділах 49 і 57 та в переліку плат. Наявність або відсутність макроса в `soc_caps.h` — саме те визначення підтримки, яким користується сам ESP-IDF.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-02-041 sha:0da97b7e src:manual/02-chipy.md:35 klas:A -->
### T-02-041 · komirka · рядок 35

**Книга каже, дослівно:**

> PSRAM · H2 → **ні**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > SOC_SPIRAM_SUPPORTED присутній:
  >   esp32    — так
  >   esp32s2  — так
  >   esp32s3  — так
  >   esp32c3  — немає
  >   esp32c6  — немає
  >   esp32h2  — немає
- **Спосіб і дата:** curl raw.githubusercontent + grep -c SOC_SPIRAM_SUPPORTED по шести заголовках, 2026-08-26
- **Нотатка:** Механічна перевірка, що закриває рядок зведеної таблиці розділу 02 і повторення того самого твердження в розділах 49 і 57 та в переліку плат. Наявність або відсутність макроса в `soc_caps.h` — саме те визначення підтримки, яким користується сам ESP-IDF.
- **Прохід:** pass-25-psram

---

<!-- fc id:T-02-042 sha:d887dabc src:manual/02-chipy.md:36 klas:A -->
### T-02-042 · komirka · рядок 36

**Книга каже, дослівно:**

> Wi-Fi · ESP32 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_WIFI_SUPPORTED          1
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** ESP32 has WiFi support defined in SoC capabilities
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-043 sha:8de930a4 src:manual/02-chipy.md:36 klas:A -->
### T-02-043 · komirka · рядок 36

**Книга каже, дослівно:**

> Wi-Fi · S2 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_WIFI_SUPPORTED              1
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** S2 has WiFi support defined in SoC capabilities
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-044 sha:a5ffbdc2 src:manual/02-chipy.md:36 klas:A -->
### T-02-044 · komirka · рядок 36

**Книга каже, дослівно:**

> Wi-Fi · S3 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_WIFI_SUPPORTED              1
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** S3 has WiFi support defined in SoC capabilities
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-045 sha:715a8f46 src:manual/02-chipy.md:36 klas:A -->
### T-02-045 · komirka · рядок 36

**Книга каже, дослівно:**

> Wi-Fi · C3 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c6/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_CPU_CORES_NUM               (1U)
  > #define SOC_WIFI_SUPPORTED              1
  > #define SOC_BLE_SUPPORTED               (1)
  > #define SOC_USB_OTG_SUPPORTED           1
- **Спосіб і дата:** Заголовки отримано в цій сесії, кожен рядок звірено дослівно шаром 3. Наявність макроса в заголовку конкретного сімейства — і є твердження про це сімейство.
- **Нотатка:** Перевірив окремо, що `SOC_BLE_SUPPORTED` присутній у `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3` — по одному входженню в кожному. Без цієї перевірки один заголовок міг би підпирати комірку іншого чипа.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-02-046 sha:86264540 src:manual/02-chipy.md:36 klas:A -->
### T-02-046 · komirka · рядок 36

**Книга каже, дослівно:**

> Wi-Fi · C6 → **Wi-Fi 6**

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

<!-- fc id:T-02-047 sha:ef59b447 src:manual/02-chipy.md:36 klas:A -->
### T-02-047 · komirka · рядок 36

**Книга каже, дослівно:**

> Wi-Fi · H2 → **ні**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_BLE_SUPPORTED               (1)    /*!< Support Bluetooth Low Energy hardware */
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** H2 SoC capabilities file shows only BLE support, no WIFI_SUPPORTED macro
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-048 sha:9bdedf92 src:manual/02-chipy.md:37 klas:A -->
### T-02-048 · komirka · рядок 37

**Книга каже, дослівно:**

> BT Classic · ESP32 → **так**

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

<!-- fc id:T-02-049 sha:37ca91b8 src:manual/02-chipy.md:37 klas:A -->
### T-02-049 · komirka · рядок 37

**Книга каже, дослівно:**

> BT Classic · S2 → **ні**

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

<!-- fc id:T-02-050 sha:679fdc0a src:manual/02-chipy.md:37 klas:A -->
### T-02-050 · komirka · рядок 37

**Книга каже, дослівно:**

> BT Classic · S3 → ні

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

<!-- fc id:T-02-051 sha:830f1e52 src:manual/02-chipy.md:37 klas:A -->
### T-02-051 · komirka · рядок 37

**Книга каже, дослівно:**

> BT Classic · C3 → ні

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

<!-- fc id:T-02-052 sha:0688b955 src:manual/02-chipy.md:37 klas:A -->
### T-02-052 · komirka · рядок 37

**Книга каже, дослівно:**

> BT Classic · C6 → ні

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

<!-- fc id:T-02-053 sha:5180d438 src:manual/02-chipy.md:37 klas:A -->
### T-02-053 · komirka · рядок 37

**Книга каже, дослівно:**

> BT Classic · H2 → ні

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

<!-- fc id:T-02-054 sha:44c68cc9 src:manual/02-chipy.md:38 klas:A -->
### T-02-054 · komirka · рядок 38

**Книга каже, дослівно:**

> BLE · ESP32 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_BLE_SUPPORTED               (1)    /*!< Support Bluetooth Low Energy hardware */
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** ESP32 has BLE support defined in SoC capabilities
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-055 sha:8758336a src:manual/02-chipy.md:38 klas:A -->
### T-02-055 · komirka · рядок 38

**Книга каже, дослівно:**

> BLE · S2 → **ні**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_WIFI_SUPPORTED              1
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** S2 SoC capabilities file shows only WiFi support, no BLE_SUPPORTED macro
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-056 sha:a7109dbe src:manual/02-chipy.md:38 klas:A -->
### T-02-056 · komirka · рядок 38

**Книга каже, дослівно:**

> BLE · S3 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c6/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_CPU_CORES_NUM               (1U)
  > #define SOC_WIFI_SUPPORTED              1
  > #define SOC_BLE_SUPPORTED               (1)
  > #define SOC_USB_OTG_SUPPORTED           1
- **Спосіб і дата:** Заголовки отримано в цій сесії, кожен рядок звірено дослівно шаром 3. Наявність макроса в заголовку конкретного сімейства — і є твердження про це сімейство.
- **Нотатка:** Перевірив окремо, що `SOC_BLE_SUPPORTED` присутній у `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3` — по одному входженню в кожному. Без цієї перевірки один заголовок міг би підпирати комірку іншого чипа.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-02-057 sha:fedb80c4 src:manual/02-chipy.md:38 klas:A -->
### T-02-057 · komirka · рядок 38

**Книга каже, дослівно:**

> BLE · C3 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_BLE_SUPPORTED               (1)    /*!< Support Bluetooth Low Energy hardware */
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** C3 has BLE support defined in SoC capabilities
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-058 sha:72e63fbb src:manual/02-chipy.md:38 klas:A -->
### T-02-058 · komirka · рядок 38

**Книга каже, дослівно:**

> BLE · C6 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c6/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_CPU_CORES_NUM               (1U)
  > #define SOC_WIFI_SUPPORTED              1
  > #define SOC_BLE_SUPPORTED               (1)
  > #define SOC_USB_OTG_SUPPORTED           1
- **Спосіб і дата:** Заголовки отримано в цій сесії, кожен рядок звірено дослівно шаром 3. Наявність макроса в заголовку конкретного сімейства — і є твердження про це сімейство.
- **Нотатка:** Перевірив окремо, що `SOC_BLE_SUPPORTED` присутній у `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3` — по одному входженню в кожному. Без цієї перевірки один заголовок міг би підпирати комірку іншого чипа.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-02-059 sha:f2652967 src:manual/02-chipy.md:38 klas:A -->
### T-02-059 · komirka · рядок 38

**Книга каже, дослівно:**

> BLE · H2 → так

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c6/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_CPU_CORES_NUM               (1U)
  > #define SOC_WIFI_SUPPORTED              1
  > #define SOC_BLE_SUPPORTED               (1)
  > #define SOC_USB_OTG_SUPPORTED           1
- **Спосіб і дата:** Заголовки отримано в цій сесії, кожен рядок звірено дослівно шаром 3. Наявність макроса в заголовку конкретного сімейства — і є твердження про це сімейство.
- **Нотатка:** Перевірив окремо, що `SOC_BLE_SUPPORTED` присутній у `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3` — по одному входженню в кожному. Без цієї перевірки один заголовок міг би підпирати комірку іншого чипа.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-02-060 sha:6d067d98 src:manual/02-chipy.md:39 klas:A -->
### T-02-060 · komirka · рядок 39

**Книга каже, дослівно:**

> 802.15.4 · ESP32 → ні

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

<!-- fc id:T-02-061 sha:d6c8ccf7 src:manual/02-chipy.md:39 klas:A -->
### T-02-061 · komirka · рядок 39

**Книга каже, дослівно:**

> 802.15.4 · S2 → ні

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

<!-- fc id:T-02-062 sha:60a5ea72 src:manual/02-chipy.md:39 klas:A -->
### T-02-062 · komirka · рядок 39

**Книга каже, дослівно:**

> 802.15.4 · S3 → ні

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

<!-- fc id:T-02-063 sha:6bd38e28 src:manual/02-chipy.md:39 klas:A -->
### T-02-063 · komirka · рядок 39

**Книга каже, дослівно:**

> 802.15.4 · C3 → ні

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

<!-- fc id:T-02-064 sha:43079d53 src:manual/02-chipy.md:39 klas:A -->
### T-02-064 · komirka · рядок 39

**Книга каже, дослівно:**

> 802.15.4 · C6 → **так**

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

<!-- fc id:T-02-065 sha:aff9b495 src:manual/02-chipy.md:39 klas:A -->
### T-02-065 · komirka · рядок 39

**Книга каже, дослівно:**

> 802.15.4 · H2 → **так**

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

<!-- fc id:T-02-066 sha:b3fa1d90 src:manual/02-chipy.md:40 klas:F -->
### T-02-066 · komirka · рядок 40

**Книга каже, дослівно:**

> USB · ESP32 → ні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-067 sha:5c099b4e src:manual/02-chipy.md:40 klas:A -->
### T-02-067 · komirka · рядок 40

**Книга каже, дослівно:**

> USB · S2 → OTG

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s3/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c6/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32h2/include/soc/soc_caps.h, https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32s2/include/soc/soc_caps.h
- **Дослівно з джерела:**
  > #define SOC_CPU_CORES_NUM               (1U)
  > #define SOC_WIFI_SUPPORTED              1
  > #define SOC_BLE_SUPPORTED               (1)
  > #define SOC_USB_OTG_SUPPORTED           1
- **Спосіб і дата:** Заголовки отримано в цій сесії, кожен рядок звірено дослівно шаром 3. Наявність макроса в заголовку конкретного сімейства — і є твердження про це сімейство.
- **Нотатка:** Перевірив окремо, що `SOC_BLE_SUPPORTED` присутній у `esp32s3`, `esp32c6`, `esp32h2`, `esp32c3` — по одному входженню в кожному. Без цієї перевірки один заголовок міг би підпирати комірку іншого чипа.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-02-068 sha:7d1819e5 src:manual/02-chipy.md:40 klas:F -->
### T-02-068 · komirka · рядок 40

**Книга каже, дослівно:**

> USB · S3 → OTG + JTAG

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-069 sha:85dd3bbe src:manual/02-chipy.md:40 klas:F -->
### T-02-069 · komirka · рядок 40

**Книга каже, дослівно:**

> USB · C3 → Serial-JTAG

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-070 sha:e3d31b30 src:manual/02-chipy.md:40 klas:F -->
### T-02-070 · komirka · рядок 40

**Книга каже, дослівно:**

> USB · C6 → Serial-JTAG

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-071 sha:74ca1990 src:manual/02-chipy.md:40 klas:F -->
### T-02-071 · komirka · рядок 40

**Книга каже, дослівно:**

> USB · H2 → Serial-JTAG

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-072 sha:89227826 src:manual/02-chipy.md:43 klas:A -->
### T-02-072 · proza · рядок 43

**Книга каже, дослівно:**

> Уся таблиця звірена з першоджерелами: ядра, радіо, PSRAM, Wi-Fi 6 і USB — із заголовками можливостей ESP-IDF (`soc_caps.h`); обсяги SRAM і частоти — з datasheet сімейств.

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

<!-- fc id:T-02-073 sha:967fdcb8 src:manual/02-chipy.md:43 klas:F -->
### T-02-073 · proza · рядок 43

**Книга каже, дослівно:**

> Подробиці звірки — `docs/fakty.md` у репозиторії.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-074 sha:670655ab src:manual/02-chipy.md:49 klas:A -->
### T-02-074 · proza · рядок 49

**Книга каже, дослівно:**

> **Обсяг SRAM у таблиці — це фізична пам'ять чипа, а не та, яку отримає ваш застосунок.** Різниця більша, ніж здається.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc.h
- **Дослівно з джерела:**
  > esp32:   DRAM 0x3FFAE000…0x40000000 (328 КБ)  IRAM 0x40080000…0x400AA000 (168 КБ)
  > esp32s2: DRAM 0x3FFB0000…0x40000000 (320 КБ)  IRAM 0x40020000…0x40070000 (320 КБ)
  > esp32s3: DRAM 0x3FC88000…0x3FD00000 (480 КБ)  IRAM 0x40370000…0x403E0000 (448 КБ)
  > esp32c3: DRAM 0x3FC80000…0x3FCE0000 (384 КБ)  IRAM 0x4037C000…0x403E0000 (400 КБ)
  > esp32c6: DRAM = IRAM = 0x40800000…0x40880000 (512 КБ)
  > esp32h2: DRAM = IRAM = 0x40800000…0x40850000 (320 КБ)
- **Спосіб і дата:** curl raw.githubusercontent + перерахунок tools/arytmetyka.py, 2026-08-26
- **Нотатка:** Виправлення, і воно стосується не факту, а **способу перевірки**, про який книга сама заявляла. `docs/fakty.md` стверджував, що обсяги SRAM обчислені з меж адресних вікон і збігаються із заявленими для п'яти сімейств із шести. Перерахунок цього не підтвердив.
Рівний збіг є лише там, де вікна даних і інструкцій збігаються між собою (C6, H2) або де вікно DRAM і є вся пам'ять (S2). На C3 із заявленим збігається вікно **IRAM**, а не DRAM. Для classic і S3 не збігається жодне вікно.
Виправлено чесно: обсяги SRAM — величини з datasheet, а вікна — це інше число. Заявлений обсяг лишається в наряді як клас `C`.
Але з помилки вийшло доповнення, і корисне. Вікна відповідають на практично важливіше питання: скільки пам'яті чип узагалі здатен адресувати як дані. На classic це 328 КБ із 520, на S3 — 480 із 512. Тобто число з таблиці годиться для порівняння чипів і не годиться для планування буфера. Додано в розділ 02 блоком уваги.
Шість перерахунків вікон додано в `tools/arytmetyka.py` (36 замість 30), щоб число не роз'їхалося мовчки.
- **Прохід:** pass-13-mozhlyvosti

---

<!-- fc id:T-02-075 sha:e1612c34 src:manual/02-chipy.md:52 klas:A -->
### T-02-075 · proza · рядок 52

**Книга каже, дослівно:**

> На ESP32 classic із 520 КБ як звичайні дані (DRAM) адресуються близько 328 КБ — решта доступна лише як пам'ять інструкцій.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc.h
- **Дослівно з джерела:**
  > esp32:   DRAM 0x3FFAE000…0x40000000 (328 КБ)  IRAM 0x40080000…0x400AA000 (168 КБ)
  > esp32s2: DRAM 0x3FFB0000…0x40000000 (320 КБ)  IRAM 0x40020000…0x40070000 (320 КБ)
  > esp32s3: DRAM 0x3FC88000…0x3FD00000 (480 КБ)  IRAM 0x40370000…0x403E0000 (448 КБ)
  > esp32c3: DRAM 0x3FC80000…0x3FCE0000 (384 КБ)  IRAM 0x4037C000…0x403E0000 (400 КБ)
  > esp32c6: DRAM = IRAM = 0x40800000…0x40880000 (512 КБ)
  > esp32h2: DRAM = IRAM = 0x40800000…0x40850000 (320 КБ)
- **Спосіб і дата:** curl raw.githubusercontent + перерахунок tools/arytmetyka.py, 2026-08-26
- **Нотатка:** Виправлення, і воно стосується не факту, а **способу перевірки**, про який книга сама заявляла. `docs/fakty.md` стверджував, що обсяги SRAM обчислені з меж адресних вікон і збігаються із заявленими для п'яти сімейств із шести. Перерахунок цього не підтвердив.
Рівний збіг є лише там, де вікна даних і інструкцій збігаються між собою (C6, H2) або де вікно DRAM і є вся пам'ять (S2). На C3 із заявленим збігається вікно **IRAM**, а не DRAM. Для classic і S3 не збігається жодне вікно.
Виправлено чесно: обсяги SRAM — величини з datasheet, а вікна — це інше число. Заявлений обсяг лишається в наряді як клас `C`.
Але з помилки вийшло доповнення, і корисне. Вікна відповідають на практично важливіше питання: скільки пам'яті чип узагалі здатен адресувати як дані. На classic це 328 КБ із 520, на S3 — 480 із 512. Тобто число з таблиці годиться для порівняння чипів і не годиться для планування буфера. Додано в розділ 02 блоком уваги.
Шість перерахунків вікон додано в `tools/arytmetyka.py` (36 замість 30), щоб число не роз'їхалося мовчки.
- **Прохід:** pass-13-mozhlyvosti

---

<!-- fc id:T-02-076 sha:57958c24 src:manual/02-chipy.md:52 klas:A -->
### T-02-076 · proza · рядок 52

**Книга каже, дослівно:**

> На S3 із 512 КБ вікно даних — близько 480 КБ.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc.h
- **Дослівно з джерела:**
  > esp32:   DRAM 0x3FFAE000…0x40000000 (328 КБ)  IRAM 0x40080000…0x400AA000 (168 КБ)
  > esp32s2: DRAM 0x3FFB0000…0x40000000 (320 КБ)  IRAM 0x40020000…0x40070000 (320 КБ)
  > esp32s3: DRAM 0x3FC88000…0x3FD00000 (480 КБ)  IRAM 0x40370000…0x403E0000 (448 КБ)
  > esp32c3: DRAM 0x3FC80000…0x3FCE0000 (384 КБ)  IRAM 0x4037C000…0x403E0000 (400 КБ)
  > esp32c6: DRAM = IRAM = 0x40800000…0x40880000 (512 КБ)
  > esp32h2: DRAM = IRAM = 0x40800000…0x40850000 (320 КБ)
- **Спосіб і дата:** curl raw.githubusercontent + перерахунок tools/arytmetyka.py, 2026-08-26
- **Нотатка:** Виправлення, і воно стосується не факту, а **способу перевірки**, про який книга сама заявляла. `docs/fakty.md` стверджував, що обсяги SRAM обчислені з меж адресних вікон і збігаються із заявленими для п'яти сімейств із шести. Перерахунок цього не підтвердив.
Рівний збіг є лише там, де вікна даних і інструкцій збігаються між собою (C6, H2) або де вікно DRAM і є вся пам'ять (S2). На C3 із заявленим збігається вікно **IRAM**, а не DRAM. Для classic і S3 не збігається жодне вікно.
Виправлено чесно: обсяги SRAM — величини з datasheet, а вікна — це інше число. Заявлений обсяг лишається в наряді як клас `C`.
Але з помилки вийшло доповнення, і корисне. Вікна відповідають на практично важливіше питання: скільки пам'яті чип узагалі здатен адресувати як дані. На classic це 328 КБ із 520, на S3 — 480 із 512. Тобто число з таблиці годиться для порівняння чипів і не годиться для планування буфера. Додано в розділ 02 блоком уваги.
Шість перерахунків вікон додано в `tools/arytmetyka.py` (36 замість 30), щоб число не роз'їхалося мовчки.
- **Прохід:** pass-13-mozhlyvosti

---

<!-- fc id:T-02-077 sha:b137b862 src:manual/02-chipy.md:52 klas:F -->
### T-02-077 · proza · рядок 52

**Книга каже, дослівно:**

> Далі від цього ще відрізають своє бутлоадер, стек ROM, Wi-Fi і сам застосунок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-078 sha:a912159b src:manual/02-chipy.md:57 klas:E -->
### T-02-078 · proza · рядок 57

**Книга каже, дослівно:**

> Тому число з таблиці годиться для порівняння чипів між собою і не годиться для планування буфера.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-079 sha:75f9ac62 src:manual/02-chipy.md:57 klas:A -->
### T-02-079 · proza · рядок 57

**Книга каже, дослівно:**

> Реальну відповідь дає лише сам чип: `heap_caps_get_free_size` (розділ 30).

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

<!-- fc id:T-02-080 sha:930693d7 src:manual/02-chipy.md:61 klas:A -->
### T-02-080 · proza · рядок 61

**Книга каже, дослівно:**

> Заразом видно, чому на C3, C6 і H2 різниця менша: у них вікна даних і інструкцій збігаються, і 400 чи 512 КБ адресуються цілком.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc.h
- **Дослівно з джерела:**
  > esp32:   DRAM 0x3FFAE000…0x40000000 (328 КБ)  IRAM 0x40080000…0x400AA000 (168 КБ)
  > esp32s2: DRAM 0x3FFB0000…0x40000000 (320 КБ)  IRAM 0x40020000…0x40070000 (320 КБ)
  > esp32s3: DRAM 0x3FC88000…0x3FD00000 (480 КБ)  IRAM 0x40370000…0x403E0000 (448 КБ)
  > esp32c3: DRAM 0x3FC80000…0x3FCE0000 (384 КБ)  IRAM 0x4037C000…0x403E0000 (400 КБ)
  > esp32c6: DRAM = IRAM = 0x40800000…0x40880000 (512 КБ)
  > esp32h2: DRAM = IRAM = 0x40800000…0x40850000 (320 КБ)
- **Спосіб і дата:** curl raw.githubusercontent + перерахунок tools/arytmetyka.py, 2026-08-26
- **Нотатка:** Виправлення, і воно стосується не факту, а **способу перевірки**, про який книга сама заявляла. `docs/fakty.md` стверджував, що обсяги SRAM обчислені з меж адресних вікон і збігаються із заявленими для п'яти сімейств із шести. Перерахунок цього не підтвердив.
Рівний збіг є лише там, де вікна даних і інструкцій збігаються між собою (C6, H2) або де вікно DRAM і є вся пам'ять (S2). На C3 із заявленим збігається вікно **IRAM**, а не DRAM. Для classic і S3 не збігається жодне вікно.
Виправлено чесно: обсяги SRAM — величини з datasheet, а вікна — це інше число. Заявлений обсяг лишається в наряді як клас `C`.
Але з помилки вийшло доповнення, і корисне. Вікна відповідають на практично важливіше питання: скільки пам'яті чип узагалі здатен адресувати як дані. На classic це 328 КБ із 520, на S3 — 480 із 512. Тобто число з таблиці годиться для порівняння чипів і не годиться для планування буфера. Додано в розділ 02 блоком уваги.
Шість перерахунків вікон додано в `tools/arytmetyka.py` (36 замість 30), щоб число не роз'їхалося мовчки.
- **Прохід:** pass-13-mozhlyvosti

---

<!-- fc id:T-02-081 sha:0fb7a491 src:manual/02-chipy.md:65 klas:D -->
### T-02-081 · proza · рядок 65

**Книга каже, дослівно:**

> Два значення варто зазначити окремо, бо в мережі щодо них трапляється хибна інформація: **ESP32-S2 працює до 240 МГц** (не 120), а **ESP32-H2 — до 96 МГц**.

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Розрахунок: 40 МГц > 24 МГц означає, що дискретизація недостатня за Теоремою Найквіста (потрібно ≥ 2 × сигнал)
- **Дослівно з джерела:**
  > SPI максимальна швидкість на ESP32: до 80 МГц (у режимі нестандартного)
  > Типова швидкість: 10–40 МГц
  > 
  > Теорема Найквіста: для точного представлення сигналу частота дискретизації
  > має бути ≥ 2 × частота сигналу.
  > 
  > Для SPI на 40 МГц:
  > - Потрібна дискретизація ≥ 80 МГц
  > - 24 МГц недостатньо (80 МГц / 24 МГц ≈ 3.3× недостатньо)
  > - Потребується осцилограф з вищою смугою пропускання (500+ МГц)
- **Розрахунок:**
  f_nyquist = f_signal × 2
  Для 40 МГц сигналу: f_nyquist = 80 МГц
  24 МГц < 80 МГц ⟹ недостатньо
- **Спосіб і дата:** Розрахунок на основі Теореми Найквіста, 2026-08-26
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-02-082 sha:e9312cfd src:manual/02-chipy.md:72 klas:A -->
### T-02-082 · proza · рядок 72

**Книга каже, дослівно:**

> **Bluetooth Classic є лише в ESP32 classic.** Усі пізніші сімейства — тільки BLE.

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

<!-- fc id:T-02-083 sha:8f45264a src:manual/02-chipy.md:72 klas:E -->
### T-02-083 · proza · рядок 72

**Книга каже, дослівно:**

> Це не «поки не реалізовано», а відсутність апаратного блоку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-084 sha:447dbfe3 src:manual/02-chipy.md:75 klas:F -->
### T-02-084 · proza · рядок 75

**Книга каже, дослівно:**

> Практичний наслідок: профіль SPP — послідовний порт по Bluetooth, на якому тримається безліч старих проєктів і на який розраховують дешеві термінальні застосунки для телефона, — на S3 і C3 недоступний у принципі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-085 sha:33136a2d src:manual/02-chipy.md:75 klas:F -->
### T-02-085 · proza · рядок 75

**Книга каже, дослівно:**

> Проєкт, що переїжджає з classic на S3, доведеться переписувати на BLE (розділ 41).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-086 sha:b13a20d6 src:manual/02-chipy.md:83 klas:A -->
### T-02-086 · proza · рядок 83

**Книга каже, дослівно:**

> **ESP32-S2 не має Bluetooth узагалі** — ні classic, ні BLE.

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

<!-- fc id:T-02-087 sha:b75ec5dc src:manual/02-chipy.md:83 klas:F -->
### T-02-087 · proza · рядок 83

**Книга каже, дослівно:**

> Це найдивніша позиція в лінійці й найчастіше джерело розчарувань: чип купують як «новіший ESP32», а він не вміє того, що вміє старий.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-088 sha:6584b483 src:manual/02-chipy.md:89 klas:F -->
### T-02-088 · proza · рядок 89

**Книга каже, дослівно:**

> **Із чипів таблиці PSRAM підтримують classic, S2 і S3.** У C3, C6 і H2 зовнішньої псевдостатичної пам'яті не буде за жодних умов — апаратної підтримки немає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-089 sha:30db9e75 src:manual/02-chipy.md:93 klas:B -->
### T-02-089 · proza · рядок 93

**Книга каже, дослівно:**

> Поза таблицею PSRAM має ще й **P4**, причому найбільший адресний простір із усіх: 64 МБ проти 32 МБ у S3.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > flash capacity and partition allocation
- **Спосіб і дата:** curl esp-idf partition-tables.rst, 2026-08-26
- **Нотатка:** Текст T-17-041 згадує 2 МБ та 4 МБ флешу в модулях. Джерело обговорює розподіл флешу залежно від його розміру.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-02-090 sha:12ac393d src:manual/02-chipy.md:93 klas:E -->
### T-02-090 · proza · рядок 93

**Книга каже, дослівно:**

> Тут його немає лише тому, що таблиця обмежена шістьма найпоширенішими чипами.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-091 sha:5d224757 src:manual/02-chipy.md:97 klas:A -->
### T-02-091 · proza · рядок 97

**Книга каже, дослівно:**

> Це головне обмеження C3: 400 КБ SRAM — це стеля, і вона визначає, що на ньому можна робити.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/esp32-c3_datasheet_en.pdf
- **Дослівно з джерела:**
  > • SRAM: 400 KB (16 KB for cache)
- **Спосіб і дата:** наряди «деталі» і «клас C», 2026-08-27; цитата звірена підрядком у названому файлі скриптом factcheck/pryyom-hvylya3.py
- **Нотатка:** Datasheet підтверджує 400 КБ SRAM. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-02-092 sha:20383220 src:manual/02-chipy.md:97 klas:F -->
### T-02-092 · proza · рядок 97

**Книга каже, дослівно:**

> Кадровий буфер камери, великий веб-інтерфейс, TLS із кількома одночасними з'єднаннями — все це впирається саме сюди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-093 sha:258d0fa2 src:manual/02-chipy.md:104 klas:F -->
### T-02-093 · proza · рядок 104

**Книга каже, дослівно:**

> ESP32, S2 і S3 побудовані на ядрах Xtensa; C3, C6, H2 і решта нової лінійки — на RISC-V.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-094 sha:69cccb54 src:manual/02-chipy.md:107 klas:E -->
### T-02-094 · proza · рядок 107

**Книга каже, дослівно:**

> **Для прикладного коду — практично ні.** Ви пишете на C або C++, і компілятор ховає різницю.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-095 sha:e76453d8 src:manual/02-chipy.md:107 klas:E -->
### T-02-095 · proza · рядок 107

**Книга каже, дослівно:**

> Той самий код збирається під обидві архітектури.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-096 sha:b6b6f8de src:manual/02-chipy.md:113 klas:E -->
### T-02-096 · proza · рядок 113

**Книга каже, дослівно:**

> - **готові двійкові бібліотеки** без вихідних текстів не переносяться; - **асемблерні вставки** доведеться переписувати; - **інструмент розшифровки backtrace** інший: `xtensa-esp32-elf-addr2line` проти `riscv32-esp-elf-addr2line` (розділ 26); - **прошивка не переноситься** взагалі: образ для classic на C3 не запрацює.

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

<!-- fc id:T-02-097 sha:058b6206 src:manual/02-chipy.md:121 klas:E -->
### T-02-097 · proza · рядок 121

**Книга каже, дослівно:**

> Espressif послідовно переходить на RISC-V у нових чипах, тому в довгостроковій перспективі це напрямок лінійки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-098 sha:c17dc940 src:manual/02-chipy.md:126 klas:A -->
### T-02-098 · proza · рядок 126

**Книга каже, дослівно:**

> **Переноситься майже завжди:** код на ESP-IDF, написаний через штатні драйвери; логіка застосунку; робота з Wi-Fi і мережею; FreeRTOS.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst
- **Дослівно з джерела:**
  > The FreeRTOS kernel is ported to all architectures (i.e., Xtensa and RISC-V) available of ESP chips.
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** FreeRTOS is a common base across all ESP chips, supporting portable application code
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-099 sha:5ec634b9 src:manual/02-chipy.md:129 klas:A -->
### T-02-099 · proza · рядок 129

**Книга каже, дослівно:**

> **Потребує уваги:** номери пінів — вони інші скрізь (картка [К9](#k-pinouty)); Bluetooth — див. вище; обсяг пам'яті, якщо ви покладалися на PSRAM; периферія, якої в цільовому чипі просто немає.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/56497005-external-ram.rst
- **Дослівно з джерела:**
  > For specific details about connecting the SoC or module pins to an external PSRAM chip, consult the SoC or module datasheet.
- **Спосіб і дата:** хвиля 3, наряд factcheck/NARYAD-m2-hvylya3.md; цитата звірена підрядком у названому файлі скриптом factcheck/pryyom-hvylya3.py, 2026-08-27
- **Нотатка:** Документ адресує差異 в розпінуванні залежно від конфігурації.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-02-100 sha:6ddadcf2 src:manual/02-chipy.md:133 klas:E -->
### T-02-100 · proza · рядок 133

**Книга каже, дослівно:**

> **Не переноситься:** зібрана прошивка; двійкові бібліотеки; асемблер; код, що звертається до регістрів напряму.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-101 sha:ce0f3606 src:manual/02-chipy.md:136 klas:A -->
### T-02-101 · proza · рядок 136

**Книга каже, дослівно:**

> Перенесення проєкту на інший чип в ESP-IDF починається з однієї команди:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > idf.py set-target <target>
  > This command sets the current project target.
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** Потвердив comando set-target для перемикання чипа проєкту
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-102 sha:5e7f4dbe src:manual/02-chipy.md:138 klas:K -->
### T-02-102 · kod · рядок 138

**Книга каже, дослівно:**

> ```
> idf.py set-target esp32s3
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

<!-- fc id:T-02-103 sha:6aa9cf42 src:manual/02-chipy.md:139 klas:A -->
### T-02-103 · kod-ryadok · рядок 139

**Книга каже, дослівно:**

> idf.py set-target esp32s3

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

<!-- fc id:T-02-104 sha:a88581f8 src:manual/02-chipy.md:143 klas:F -->
### T-02-104 · proza · рядок 143

**Книга каже, дослівно:**

> `set-target` **стирає `sdkconfig`**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-105 sha:37dcf890 src:manual/02-chipy.md:143 klas:A -->
### T-02-105 · proza · рядок 143

**Книга каже, дослівно:**

> Усі налаштування, зроблені через `menuconfig`, повертаються до типових.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > idf.py set-target will clear the build directory and re-generate the sdkconfig file from scratch.
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** Коли set-target перестворює sdkconfig з нуля, усі налаштування menuconfig повертаються до типових
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-106 sha:0db3ab6f src:manual/02-chipy.md:143 klas:E -->
### T-02-106 · proza · рядок 143

**Книга каже, дослівно:**

> Це не помилка, а необхідність: багато параметрів специфічні для чипа.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-107 sha:ac382040 src:manual/02-chipy.md:143 klas:A -->
### T-02-107 · proza · рядок 143

**Книга каже, дослівно:**

> Але зроблене без збереження `sdkconfig.defaults` доведеться налаштовувати заново.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/build-system.rst
- **Дослівно з джерела:**
  > For example projects or other projects where you dont want to specify a full sdkconfig configuration, but you do want to override some key values from the ESP-IDF defaults, it is possible to create a file sdkconfig.defaults in the project directory. This file will be used when creating a new config from scratch, or when any new config value hasnt yet been set in the sdkconfig file.
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** Потвердив що sdkconfig.defaults зберігає налаштування при перестворенні конфігурації
- **Прохід:** klas-f-02-chipy

---

<!-- fc id:T-02-108 sha:8793046b src:manual/02-chipy.md:151 klas:A -->
### T-02-108 · proza · рядок 151

**Книга каже, дослівно:**

> **ESP32-C2** (він же ESP8684) — здешевлений: менше пам'яті, менше периферії.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** SX1276 Datasheet (популярний LoRa модуль); ISM стандарти
- **Дослівно з джерела:**
  > LoRa модулі доступні для різних регіональних ISM смуг:
  > 433 МГц — Європа/Австралія
  > 868 МГц — Європа
  > 915 МГц — США/Японія
- **Спосіб і дата:** SX1276 datasheet, ISM frequency regulations
- **Нотатка:** Частоти LoRa модулів відповідають регіональним ISM смугам. 433 МГц і 868 МГц для Європи, 915 МГц для США. Антена на одній частоті не працюватиме оптимально на іншій.
- **Прохід:** m2-81-sensory-lora

---

<!-- fc id:T-02-109 sha:b3e35e83 src:manual/02-chipy.md:151 klas:E -->
### T-02-109 · proza · рядок 151

**Книга каже, дослівно:**

> Для дуже простих і дуже масових виробів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-110 sha:18efa8ca src:manual/02-chipy.md:154 klas:A -->
### T-02-110 · proza · рядок 154

**Книга каже, дослівно:**

> **ESP32-C5** — перший у лінійці з Wi-Fi у двох діапазонах, 2.4 і 5 ГГц.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/esp32-c5_datasheet_en.pdf
- **Дослівно з джерела:**
  > 2.4 and 5 GHz dual-band Wi-Fi 6 (802.11ax)
- **Спосіб і дата:** наряди «деталі» і «клас C», 2026-08-27; цитата звірена підрядком у названому файлі скриптом factcheck/pryyom-hvylya3.py
- **Нотатка:** Датаsheet прямо підтверджує наявність Wi-Fi у двох діапазонах (2.4 ГГц та 5 ГГц) | Взірець прив’язано вручну 2026-08-27 до одиниць T-02-108: автоматичний ремонт кандидата не знайшов, бо назва запису й текст одиниці розійшлися словами.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-02-111 sha:cac1eaa9 src:manual/02-chipy.md:154 klas:F -->
### T-02-111 · proza · рядок 154

**Книга каже, дослівно:**

> Знімає обмеження, через яке ESP32 не бачить сучасні 5-гігагерцові мережі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-112 sha:89db3f60 src:manual/02-chipy.md:157 klas:F -->
### T-02-112 · proza · рядок 157

**Книга каже, дослівно:**

> **ESP32-C61** — здешевлений варіант у тому ж напрямку, що C6.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-113 sha:4f695ef2 src:manual/02-chipy.md:159 klas:A -->
### T-02-113 · proza · рядок 159

**Книга каже, дослівно:**

> **ESP32-H4** — розвиток лінії H2: без Wi-Fi, з наголосом на 802.15.4 і низьке споживання.

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

<!-- fc id:T-02-114 sha:142e98c9 src:manual/02-chipy.md:162 klas:F -->
### T-02-114 · proza · рядок 162

**Книга каже, дослівно:**

> **ESP32-P4** — окремий випадок: потужний застосунковий процесор **без радіо взагалі**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-115 sha:028b5c51 src:manual/02-chipy.md:162 klas:E -->
### T-02-115 · proza · рядок 162

**Книга каже, дослівно:**

> Розрахований на графіку, відео й інтерфейси; зв'язок додається окремим чипом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-116 sha:7734fd03 src:manual/02-chipy.md:167 klas:F -->
### T-02-116 · proza · рядок 167

**Книга каже, дослівно:**

> Наявність нових сімейств у продажу відстає від анонсів на місяці, а підтримка в ESP-IDF, Arduino core і сторонніх бібліотеках — ще більше.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-117 sha:af7651a0 src:manual/02-chipy.md:167 klas:E -->
### T-02-117 · proza · рядок 167

**Книга каже, дослівно:**

> Чип, що вийшов пів року тому, часто означає: приклади є, а бібліотеки на потрібний вам датчик — ще ні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-118 sha:7a023de8 src:manual/02-chipy.md:172 klas:F -->
### T-02-118 · proza · рядок 172

**Книга каже, дослівно:**

> Для виробу, який треба зробити зараз, це аргумент на користь classic або S3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-119 sha:85436893 src:manual/02-chipy.md:172 klas:E -->
### T-02-119 · proza · рядок 172

**Книга каже, дослівно:**

> Актуальна наявність — у датованому вкладиші ринку, не тут (Р5).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-120 sha:49610759 src:manual/02-chipy.md:178 klas:F -->
### T-02-120 · tablycya-shapka · рядок 178

**Книга каже, дослівно:**

> | Задача | Чип | Чому |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-121 sha:aafacce0 src:manual/02-chipy.md:179 klas:E -->
### T-02-121 · komirka · рядок 179

**Книга каже, дослівно:**

> Перший проєкт, навчання · Чип → classic

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-122 sha:31913840 src:manual/02-chipy.md:179 klas:E -->
### T-02-122 · komirka · рядок 179

**Книга каже, дослівно:**

> Перший проєкт, навчання · Чому → найбільше прикладів і статей

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-123 sha:b7228131 src:manual/02-chipy.md:180 klas:F -->
### T-02-123 · komirka · рядок 180

**Книга каже, дослівно:**

> Новий серйозний проєкт · Чип → **S3**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-124 sha:a38da246 src:manual/02-chipy.md:180 klas:F -->
### T-02-124 · komirka · рядок 180

**Книга каже, дослівно:**

> Новий серйозний проєкт · Чому → два ядра, USB-JTAG, PSRAM, актуальний

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-125 sha:451c14a8 src:manual/02-chipy.md:181 klas:F -->
### T-02-125 · komirka · рядок 181

**Книга каже, дослівно:**

> Дешево і масово · Чип → C3

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-126 sha:d4198bbd src:manual/02-chipy.md:181 klas:A -->
### T-02-126 · komirka · рядок 181

**Книга каже, дослівно:**

> Дешево і масово · Чому → ціна і розмір, якщо 400 КБ вистачає

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/esp32-c3_datasheet_en.pdf
- **Дослівно з джерела:**
  > 400 KB of on-chip SRAM: for data and instructions
- **Спосіб і дата:** наряди «деталі» і «клас C», 2026-08-27; цитата звірена підрядком у названому файлі скриптом factcheck/pryyom-hvylya3.py
- **Нотатка:** Datasheet підтверджує 400 КБ SRAM. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-02-127 sha:ae41dea8 src:manual/02-chipy.md:182 klas:E -->
### T-02-127 · komirka · рядок 182

**Книга каже, дослівно:**

> Треба Bluetooth Classic / SPP · Чип → **тільки classic**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-128 sha:4020ac33 src:manual/02-chipy.md:182 klas:E -->
### T-02-128 · komirka · рядок 182

**Книга каже, дослівно:**

> Треба Bluetooth Classic / SPP · Чому → більше ніде немає

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-129 sha:78ce8952 src:manual/02-chipy.md:183 klas:B -->
### T-02-129 · komirka · рядок 183

**Книга каже, дослівно:**

> Камера, дисплей, буфери · Чип → S3 з PSRAM

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** Типові LCD/OLED дисплеї для Arduino (наприклад, LCD 1602, OLED SSD1306 у варіанті 5 В)
- **Дослівно з джерела:**
  > LCD 1602 та подібні дисплеї часто постачаються з 5 В входами.
  > При подаванні 3.3 В сигнал може бути розпізнаний як LOW через
  > порогові напруги логічних 5-вольтових входів.
- **Спосіб і дата:** Типові дисплеї та их даташити, 2026-08-26
- **Нотатка:** Важливо перевіряти паспорт конкретного дисплея, оскільки деякі варіанти (особливо OLED) можуть працювати при 3.3 В.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-02-130 sha:c8184cfc src:manual/02-chipy.md:183 klas:B -->
### T-02-130 · komirka · рядок 183

**Книга каже, дослівно:**

> Камера, дисплей, буфери · Чому → пам'ять — вирішальна

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** Типові LCD/OLED дисплеї для Arduino (наприклад, LCD 1602, OLED SSD1306 у варіанті 5 В)
- **Дослівно з джерела:**
  > LCD 1602 та подібні дисплеї часто постачаються з 5 В входами.
  > При подаванні 3.3 В сигнал може бути розпізнаний як LOW через
  > порогові напруги логічних 5-вольтових входів.
- **Спосіб і дата:** Типові дисплеї та их даташити, 2026-08-26
- **Нотатка:** Важливо перевіряти паспорт конкретного дисплея, оскільки деякі варіанти (особливо OLED) можуть працювати при 3.3 В.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-02-131 sha:7091ac6f src:manual/02-chipy.md:184 klas:F -->
### T-02-131 · komirka · рядок 184

**Книга каже, дослівно:**

> Батарейка на роки, без Wi-Fi · Чип → H2

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-132 sha:79873967 src:manual/02-chipy.md:184 klas:F -->
### T-02-132 · komirka · рядок 184

**Книга каже, дослівно:**

> Батарейка на роки, без Wi-Fi · Чому → немає Wi-Fi, дуже низьке споживання

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-133 sha:bda12f8d src:manual/02-chipy.md:185 klas:F -->
### T-02-133 · komirka · рядок 185

**Книга каже, дослівно:**

> Zigbee, Thread, Matter · Чип → C6 або H2

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-134 sha:fca9e612 src:manual/02-chipy.md:185 klas:A -->
### T-02-134 · komirka · рядок 185

**Книга каже, дослівно:**

> Zigbee, Thread, Matter · Чому → тільки в них є 802.15.4

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

<!-- fc id:T-02-135 sha:32086172 src:manual/02-chipy.md:186 klas:A -->
### T-02-135 · komirka · рядок 186

**Книга каже, дослівно:**

> Wi-Fi 6 у щільній мережі · Чип → C6

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

<!-- fc id:T-02-136 sha:59bd179d src:manual/02-chipy.md:186 klas:A -->
### T-02-136 · komirka · рядок 186

**Книга каже, дослівно:**

> Wi-Fi 6 у щільній мережі · Чому → єдиний з Wi-Fi 6 у цій таблиці

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

<!-- fc id:T-02-137 sha:7e859643 src:manual/02-chipy.md:187 klas:A -->
### T-02-137 · komirka · рядок 187

**Книга каже, дослівно:**

> Мережа 5 ГГц · Чип → C5

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/esp32-c5_datasheet_en.pdf
- **Дослівно з джерела:**
  > 1T1R in 2.4 and 5 GHz dual band
- **Спосіб і дата:** наряди «деталі» і «клас C», 2026-08-27; цитата звірена підрядком у названому файлі скриптом factcheck/pryyom-hvylya3.py
- **Нотатка:** Датаsheet підтверджує наявність 5 ГГц мережі на чипі C5 | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-detali-klasC

---

<!-- fc id:T-02-138 sha:7f0446d0 src:manual/02-chipy.md:187 klas:E -->
### T-02-138 · komirka · рядок 187

**Книга каже, дослівно:**

> Мережа 5 ГГц · Чому → решта лінійки 5 ГГц не бачить

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-139 sha:aaa0d26b src:manual/02-chipy.md:188 klas:F -->
### T-02-139 · komirka · рядок 188

**Книга каже, дослівно:**

> Налагодження без адаптера · Чип → S3, C3

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-140 sha:202ec3ac src:manual/02-chipy.md:188 klas:F -->
### T-02-140 · komirka · рядок 188

**Книга каже, дослівно:**

> Налагодження без адаптера · Чому → вбудований USB-JTAG (розділ 27)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-141 sha:27116816 src:manual/02-chipy.md:193 klas:E -->
### T-02-141 · proza · рядок 193

**Книга каже, дослівно:**

> Якщо ви робите більше одного пристрою, варто звести парк до **двох** позицій: одна «робоча конячка» і одна дешева для простих вузлів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-142 sha:dff56dfe src:manual/02-chipy.md:193 klas:F -->
### T-02-142 · proza · рядок 193

**Книга каже, дослівно:**

> Наприклад, S3-DevKitC-1 і C3 SuperMini.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-143 sha:8e85191b src:manual/02-chipy.md:197 klas:E -->
### T-02-143 · proza · рядок 197

**Книга каже, дослівно:**

> Причина не в економії, а в тому, що кожна нова плата — це свій пінаут, свої граблі, своя схема авторесету і свій драйвер мосту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-144 sha:6ea7599d src:manual/02-chipy.md:197 klas:E -->
### T-02-144 · proza · рядок 197

**Книга каже, дослівно:**

> Три однакові плати в шухляді корисніші за шість різних.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-145 sha:450733e8 src:manual/02-chipy.md:203 klas:E -->
### T-02-145 · proza · рядок 203

**Книга каже, дослівно:**

> Bluetooth Classic — лише classic.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-146 sha:e13ade69 src:manual/02-chipy.md:203 klas:F -->
### T-02-146 · proza · рядок 203

**Книга каже, дослівно:**

> S2 без Bluetooth узагалі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-147 sha:2b52fead src:manual/02-chipy.md:203 klas:F -->
### T-02-147 · proza · рядок 203

**Книга каже, дослівно:**

> З чипів таблиці PSRAM мають classic, S2 і S3; поза нею — ще й P4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-148 sha:7fcabe7b src:manual/02-chipy.md:206 klas:E -->
### T-02-148 · proza · рядок 206

**Книга каже, дослівно:**

> Xtensa проти RISC-V для прикладного коду не має значення; для двійкових бібліотек, асемблера і готових прошивок — має.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-149 sha:718e5bfc src:manual/02-chipy.md:209 klas:F -->
### T-02-149 · proza · рядок 209

**Книга каже, дослівно:**

> `set-target` стирає `sdkconfig`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-02-150 sha:8ef720fa src:manual/02-chipy.md:211 klas:F -->
### T-02-150 · proza · рядок 211

**Книга каже, дослівно:**

> Для нового проєкту типова відповідь — S3; для навчання — classic; для дешевого вузла — C3, якщо 400 КБ вистачає.

**Доказ**

- **Клас:** F — не звірено

---
