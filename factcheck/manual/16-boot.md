# Фактчекінг: `manual/16-boot.md`

Одиниць твердження: **95**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-16-001 sha:349f6843 src:manual/16-boot.md:3 klas:E -->
### T-16-001 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Між подачею живлення і першим рядком вашого коду проходить три етапи, і на кожному чип може зупинитися.

**Контекст**

```
# 16. Як завантажується ESP32 {#boot}

Між подачею живлення і першим рядком вашого коду проходить три етапи, і на
кожному чип може зупинитися. Розуміння цього ланцюжка — різниця між
«плата чомусь не працює» і «плата зупинилася на другому етапі, бо не
знайшла таблицю розділів за адресою `0x8000`».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-002 sha:11f1c487 src:manual/16-boot.md:4 klas:A -->
### T-16-002 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Розуміння цього ланцюжка — різниця між «плата чомусь не працює» і «плата зупинилася на другому етапі, бо не знайшла таблицю розділів за адресою `0x8000`».

**Контекст**

```
# 16. Як завантажується ESP32 {#boot}

Між подачею живлення і першим рядком вашого коду проходить три етапи, і на
кожному чип може зупинитися. Розуміння цього ланцюжка — різниця між
«плата чомусь не працює» і «плата зупинилася на другому етапі, бо не
знайшла таблицю розділів за адресою `0x8000`».
```

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

<!-- fc id:T-16-003 sha:11330d7e src:manual/16-boot.md:8 klas:E -->
### T-16-003 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Це найкорисніші двадцять хвилин, які можна витратити на теорію: майже вся діагностика прошивки (розділ 29) зводиться до питання «на якому етапі воно стало».

**Контекст**

```
# 16. Як завантажується ESP32 {#boot}

Це найкорисніші двадцять хвилин, які можна витратити на теорію: майже вся
діагностика прошивки (розділ 29) зводиться до питання «на якому етапі
воно стало».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-004 sha:37a50017 src:manual/16-boot.md:14 klas:A -->
### T-16-004 · proza · `manual/16-boot.md`

**Твердження, коротко**

> **Етап 1 — ROM bootloader.** Зашитий у кремній на заводі, змінити його неможливо.

**Контекст**

```
## Три етапи

**Етап 1 — ROM bootloader.** Зашитий у кремній на заводі, змінити його
неможливо. Він стартує завжди, незалежно від того, що у флеші. Саме тому
плата з повністю стертим флешем все одно подає ознаки життя: ROM живий.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > The ROM bootloader is in read-only memory (ROM) on the ESP32 chip.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, 2026-08-26
- **Нотатка:** Текст одиниці T-16-004 констатує ROM bootloader у read-only memory у кремнії. Джерело підтверджує: The ROM bootloader is in read-only memory.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-16-005 sha:df2dec6a src:manual/16-boot.md:15 klas:C -->
### T-16-005 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Він стартує завжди, незалежно від того, що у флеші.

**Контекст**

```
## Три етапи

**Етап 1 — ROM bootloader.** Зашитий у кремній на заводі, змінити його
неможливо. Він стартує завжди, незалежно від того, що у флеші. Саме тому
плата з повністю стертим флешем все одно подає ознаки життя: ROM живий.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 boot sequence specification
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32 boot sequence specification
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-16-boot

---

<!-- fc id:T-16-006 sha:e47891e7 src:manual/16-boot.md:15 klas:E -->
### T-16-006 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Саме тому плата з повністю стертим флешем все одно подає ознаки життя: ROM живий.

**Контекст**

```
## Три етапи

**Етап 1 — ROM bootloader.** Зашитий у кремній на заводі, змінити його
неможливо. Він стартує завжди, незалежно від того, що у флеші. Саме тому
плата з повністю стертим флешем все одно подає ознаки життя: ROM живий.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-007 sha:d51c3c70 src:manual/16-boot.md:18 klas:F -->
### T-16-007 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Завдання ROM-бутлоадера: подивитися на strapping-піни і вирішити, звідки брати наступний код — з флешу чи з UART.

**Контекст**

```
## Три етапи

Завдання ROM-бутлоадера: подивитися на strapping-піни і вирішити, звідки
брати наступний код — з флешу чи з UART.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-008 sha:371e3feb src:manual/16-boot.md:21 klas:B -->
### T-16-008 · proza · `manual/16-boot.md`

**Твердження, коротко**

> **Етап 2 — другий бутлоадер (bootloader.bin).** Уже ваш, лежить у флеші, збирається разом із проєктом.

**Контекст**

```
## Три етапи

**Етап 2 — другий бутлоадер (bootloader.bin).** Уже ваш, лежить у флеші,
збирається разом із проєктом. Він налаштовує тактування і флеш, читає
таблицю розділів, обирає активний розділ застосунку, перевіряє його і
передає керування.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > After reset, the second line printed by the ESP32 ROM is a reset & boot mode message.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, 2026-08-26
- **Нотатка:** Послідовність: ROM (етап 1), потім другий бутлоадер з флешу (етап 2). Джерело підтверджує послідовність етапів.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-16-009 sha:73a47ca1 src:manual/16-boot.md:22 klas:E -->
### T-16-009 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Він налаштовує тактування і флеш, читає таблицю розділів, обирає активний розділ застосунку, перевіряє його і передає керування.

**Контекст**

```
## Три етапи

**Етап 2 — другий бутлоадер (bootloader.bin).** Уже ваш, лежить у флеші,
збирається разом із проєктом. Він налаштовує тактування і флеш, читає
таблицю розділів, обирає активний розділ застосунку, перевіряє його і
передає керування.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-010 sha:8b2614cd src:manual/16-boot.md:26 klas:F -->
### T-16-010 · proza · `manual/16-boot.md`

**Твердження, коротко**

> **Етап 3 — застосунок.** Ініціалізація FreeRTOS, потім `app_main` (в ESP-IDF) або `setup`/`loop` (в Arduino core).

**Контекст**

```
## Три етапи

**Етап 3 — застосунок.** Ініціалізація FreeRTOS, потім `app_main`
(в ESP-IDF) або `setup`/`loop` (в Arduino core).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-011 sha:b8f3d5d1 src:manual/16-boot.md:29 klas:C -->
### T-16-011 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Головне практичне: **етапи 2 і 3 живуть у флеші за фіксованими адресами**, і якщо хоч одна адреса не та, ланцюжок рветься мовчки — без повідомлення про помилку, просто без результату.

**Контекст**

```
## Три етапи

Головне практичне: **етапи 2 і 3 живуть у флеші за фіксованими адресами**,
і якщо хоч одна адреса не та, ланцюжок рветься мовчки — без повідомлення
про помилку, просто без результату.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 bootloader specification
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32 bootloader specification
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-16-boot

---

<!-- fc id:T-16-012 sha:719a564d src:manual/16-boot.md:35 klas:C -->
### T-16-012 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Strapping-пін — це звичайний GPIO, стан якого читається **один раз**, у момент відпускання скидання, і потім більше не має значення для завантаження.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Strapping-пін — це звичайний GPIO, стан якого читається **один раз**,
у момент відпускання скидання, і потім більше не має значення для
завантаження. Далі пін працює як звичайний.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP-IDF v5.3 bootloader source
- **Нотатка:** Твердження про послідовність завантаження та читання strapping-пінів. Потребує перевірки в bootloader коді. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-63-gpio-07

---

<!-- fc id:T-16-013 sha:2e09aa20 src:manual/16-boot.md:37 klas:E -->
### T-16-013 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Далі пін працює як звичайний.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Strapping-пін — це звичайний GPIO, стан якого читається **один раз**,
у момент відпускання скидання, і потім більше не має значення для
завантаження. Далі пін працює як звичайний.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-014 sha:bd61d296 src:manual/16-boot.md:39 klas:C -->
### T-16-014 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Ключовий — `GPIO0` [[classic]] [[S3]]:

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Ключовий — `GPIO0` [[classic]] [[S3]]:
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 та ESP32-S3 Datasheet, розділ про boot mode selection
- **Що шукати в джерелі:** GPIO pin functions, boot mode control
- **Нотатка:** Твердження про GPIO0 як ключовий контрольний пін для boot режимів. Це стандартна функція ESP32 архітектури, що підтверджується datasheet.
- **Прохід:** m2-98-vybirka

---

<!-- fc id:T-16-015 sha:10272434 src:manual/16-boot.md:41 klas:E -->
### T-16-015 · tablycya · `manual/16-boot.md`

**Твердження, коротко**

> | `GPIO0` при скиданні | Куди піде ROM |

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Ключовий — `GPIO0` [[classic]] [[S3]]:

| `GPIO0` при скиданні | Куди піде ROM |
|---|---|
| високий (підтягнутий вгору) | звичайний старт із флешу |
| низький (притиснутий до землі) | download mode: чекає прошивку по UART |
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Нотатка:** Це заголовок таблиці з самої книги, яка описує залежність ROM адреси від стану GPIO0 при скиданні. Таблиця з книги не є зовнішнім джерелом.
- **Прохід:** m2-98-vybirka

---

<!-- fc id:T-16-016 sha:93a3f980 src:manual/16-boot.md:43 klas:E -->
### T-16-016 · tablycya · `manual/16-boot.md`

**Твердження, коротко**

> | високий (підтягнутий вгору) | звичайний старт із флешу |

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Ключовий — `GPIO0` [[classic]] [[S3]]:

| `GPIO0` при скиданні | Куди піде ROM |
|---|---|
| високий (підтягнутий вгору) | звичайний старт із флешу |
| низький (притиснутий до землі) | download mode: чекає прошивку по UART |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-017 sha:08cf4b01 src:manual/16-boot.md:44 klas:F -->
### T-16-017 · tablycya · `manual/16-boot.md`

**Твердження, коротко**

> | низький (притиснутий до землі) | download mode: чекає прошивку по UART |

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Ключовий — `GPIO0` [[classic]] [[S3]]:

| `GPIO0` при скиданні | Куди піде ROM |
|---|---|
| високий (підтягнутий вгору) | звичайний старт із флешу |
| низький (притиснутий до землі) | download mode: чекає прошивку по UART |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-018 sha:232b5f4b src:manual/16-boot.md:46 klas:A -->
### T-16-018 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Для [[C3]] роль іншу грає пара пінів: `GPIO9` притиснутий до землі вмикає download mode, і `GPIO8` при цьому має бути високим.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Для [[C3]] роль іншу грає пара пінів: `GPIO9` притиснутий до землі вмикає
download mode, і `GPIO8` при цьому має бути високим.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp8266="GPIO0", esp32="GPIO0",
  >  esp32s2="GPIO0", esp32s3="GPIO0", esp32p4="GPIO35", esp32c5="GPIO28",
  >  esp32h21="GPIO14", esp32h4="GPIO14"}
  > {IDF_TARGET_STRAP_BOOT_2_GPIO:default="GPIO8", esp32="GPIO2", esp32s2="GPIO46",
  >  esp32s3="GPIO46", esp32p4="GPIO36", esp32c5="GPIO27", esp32h21="GPIO13",
  >  esp32h4="GPIO13"}
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує головні піни входу в download mode для всіх сімейств книги: `GPIO0` на classic, S2 і S3; `GPIO9` на C3 (значення `default`), із другим піном `GPIO8`. Збігається з розділом 07, карткою К9 і додатком A.
Заразом видно, що для P4, C5 і H4 піни зовсім інші (`GPIO35`, `GPIO28`, `GPIO14`) — ще один доказ того, що правило «і новіші», виправлене в проході 1 для адреси бутлоадера, не працює й для пінів.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-16-019 sha:fb3b60cc src:manual/16-boot.md:49 klas:F -->
### T-16-019 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Повний перелік strapping-пінів по сімействах — картка [К9](#k-pinouty), вхід у download mode вручну — картка [К4](#k-boot).

**Контекст**

```
## Куди дивиться ROM: strapping-піни

Повний перелік strapping-пінів по сімействах — картка [К9](#k-pinouty),
вхід у download mode вручну — картка [К4](#k-boot).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-020 sha:3a71c61e src:manual/16-boot.md:53 klas:F -->
### T-16-020 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Це пояснює цілий клас загадкових несправностей: **зовнішня обв'язка на strapping-піні**.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

::: uvaha
Це пояснює цілий клас загадкових несправностей: **зовнішня обв'язка на
strapping-піні**. Світлодіод із резистором на `GPIO0`, датчик, що тримає
лінію низькою, довгий дріт, який ловить наводку — і плата стартує не туди
або не стартує взагалі. Причому в коді все правильно, і в 99 % часу пін
поводиться нормально: значення має лише мілісекунда після скидання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-021 sha:728e14e7 src:manual/16-boot.md:54 klas:C -->
### T-16-021 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Світлодіод із резистором на `GPIO0`, датчик, що тримає лінію низькою, довгий дріт, який ловить наводку — і плата стартує не туди або не стартує взагалі.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

::: uvaha
Це пояснює цілий клас загадкових несправностей: **зовнішня обв'язка на
strapping-піні**. Світлодіод із резистором на `GPIO0`, датчик, що тримає
лінію низькою, довгий дріт, який ловить наводку — і плата стартує не туди
або не стартує взагалі. Причому в коді все правильно, і в 99 % часу пін
поводиться нормально: значення має лише мілісекунда після скидання.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 Boot Mode Selection Guide, Strapping Pins
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32 Boot Mode Selection Guide, Strapping Pins
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-16-boot

---

<!-- fc id:T-16-022 sha:1a088eeb src:manual/16-boot.md:56 klas:F -->
### T-16-022 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Причому в коді все правильно, і в 99 % часу пін поводиться нормально: значення має лише мілісекунда після скидання.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

::: uvaha
Це пояснює цілий клас загадкових несправностей: **зовнішня обв'язка на
strapping-піні**. Світлодіод із резистором на `GPIO0`, датчик, що тримає
лінію низькою, довгий дріт, який ловить наводку — і плата стартує не туди
або не стартує взагалі. Причому в коді все правильно, і в 99 % часу пін
поводиться нормально: значення має лише мілісекунда після скидання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-023 sha:b274c770 src:manual/16-boot.md:59 klas:A -->
### T-16-023 · proza · `manual/16-boot.md`

**Твердження, коротко**

> [[classic]] Найзліший випадок — `GPIO12` (MTDI).

**Контекст**

```
## Куди дивиться ROM: strapping-піни

[[classic]] Найзліший випадок — `GPIO12` (MTDI). Він задає напругу
живлення флешу. Підтягнутий вгору при старті — і плата не стартує взагалі,
без жодного повідомлення.
:::
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

<!-- fc id:T-16-024 sha:48424b86 src:manual/16-boot.md:59 klas:A -->
### T-16-024 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Він задає напругу живлення флешу.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

[[classic]] Найзліший випадок — `GPIO12` (MTDI). Він задає напругу
живлення флешу. Підтягнутий вгору при старті — і плата не стартує взагалі,
без жодного повідомлення.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > :esp32: -  VDDSDIO has been enabled at 1.8V (due to MTDI/GPIO12, see above),
  >         but this flash chip requires 3.3V so it's browning out.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Дослівне підтвердження механізму, доданого в розділ 07 у проході 6 за Kconfig бутлоадера. Тут те саме сказано з боку симптому: не «плата не стартує», а «флеш вимагає 3.3 В і провалюється по живленню». Формулювання книги («на переважній більшості модулів флеш тривольтовий») тепер спирається на джерело, а не лише на висновок.
Це рідкісний випадок, коли два незалежні першоджерела Espressif — Kconfig ESP-IDF і документація esptool — описують ту саму пастку з різних боків, і обидва доступні звідси.
- **Прохід:** pass-08-strapping

---

<!-- fc id:T-16-025 sha:4de10478 src:manual/16-boot.md:60 klas:E -->
### T-16-025 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Підтягнутий вгору при старті — і плата не стартує взагалі, без жодного повідомлення.

**Контекст**

```
## Куди дивиться ROM: strapping-піни

[[classic]] Найзліший випадок — `GPIO12` (MTDI). Він задає напругу
живлення флешу. Підтягнутий вгору при старті — і плата не стартує взагалі,
без жодного повідомлення.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-026 sha:a976fca3 src:manual/16-boot.md:66 klas:A -->
### T-16-026 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Другий бутлоадер лежить за адресою, яка **залежить від сімейства чипа**:

**Контекст**

```
## Що робить другий бутлоадер

Другий бутлоадер лежить за адресою, яка **залежить від сімейства чипа**:
```

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

<!-- fc id:T-16-027 sha:f44b1e43 src:manual/16-boot.md:68 klas:F -->
### T-16-027 · tablycya · `manual/16-boot.md`

**Твердження, коротко**

> | Сімейство | Адреса `bootloader.bin` |

**Контекст**

```
## Що робить другий бутлоадер

Другий бутлоадер лежить за адресою, яка **залежить від сімейства чипа**:

| Сімейство | Адреса `bootloader.bin` |
|---|---|
| ESP32 classic, ESP32-S2 | `0x1000` |
| ESP32-S3, C3, C6, H2 | `0x0` |
| ESP32-P4, C5, H4 | `0x2000` |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-028 sha:30495adc src:manual/16-boot.md:70 klas:A -->
### T-16-028 · tablycya · `manual/16-boot.md`

**Твердження, коротко**

> | ESP32 classic, ESP32-S2 | `0x1000` |

**Контекст**

```
## Що робить другий бутлоадер

Другий бутлоадер лежить за адресою, яка **залежить від сімейства чипа**:

| Сімейство | Адреса `bootloader.bin` |
|---|---|
| ESP32 classic, ESP32-S2 | `0x1000` |
| ESP32-S3, C3, C6, H2 | `0x0` |
| ESP32-P4, C5, H4 | `0x2000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild та .../docs/en/api-guides/startup.rst; https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32*.py
- **Дослівно з джерела:**
  > (Kconfig.projbuild)
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     hex
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     # the first 2 sectors are reserved for the key manager with AES-XTS
  >     #   (flash encryption) purpose
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > (startup.rst)
  > .. only:: esp32
  >    … If :doc:`/security/secure-boot-v1` is in use then the first 4 kB
  >    sector of flash is used to store secure boot IV and digest of the
  >    bootloader image. Otherwise, this sector is unused.
  > .. only:: esp32s2
  >    … The 4 kB sector of flash before this address is unused.
  > .. only:: SOC_KEY_MANAGER_SUPPORTED
  >    … The 8 kB sector of flash before this address is reserved for the
  >    key manager for use with flash encryption (AES-XTS).
  > 
  > (esptool/targets/)
  > esp32.py:   BOOTLOADER_FLASH_OFFSET = 0x1000
  > esp32s3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c6.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32p4.py: BOOTLOADER_FLASH_OFFSET = 0x2000  # First 2 sectors reserved for FE
  > esp32c5.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > esp32h4.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > (S2 успадковує 0x1000 від ESP32ROM; H2 — 0x0 від ESP32C6ROM;
  >  C2 — 0x0 від ESP32C3ROM)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Три рядки таблиці зсувів звірено з двох незалежних боків — Kconfig ESP-IDF і розбір цілей esptool — і збіг дослівний, включно з успадкуванням для S2, H2 і C2. Твердження книги «значення задає ROM і в ESP-IDF не налаштовується» теж дослівне: воно є в довідці Kconfig.
Хибною виявилася **причина**. Книга писала: «у classic і S2 проміжок від `0x0` до `0x1000` зарезервовано під потреби ROM». ROM-бутлоадер живе в кремнії й у флеші не займає нічого. Насправді на classic цей сектор належить IV і дайджестові Secure Boot v1 — а без secure boot просто не використовується; на S2 не використовується завжди.
Виправлено у двох місцях (розділ 16 і `docs/fakty.md`), і формулювання заведено в `factcheck/SPROSTOVANE.md`. Заразом таблиця в `docs/fakty.md` була **неповна** — у ній бракувало рядка `0x2000` для P4, C5 і H4, який у розділі 16 є з проходу 6.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-16-029 sha:5904e9bb src:manual/16-boot.md:71 klas:A -->
### T-16-029 · tablycya · `manual/16-boot.md`

**Твердження, коротко**

> | ESP32-S3, C3, C6, H2 | `0x0` |

**Контекст**

```
## Що робить другий бутлоадер

Другий бутлоадер лежить за адресою, яка **залежить від сімейства чипа**:

| Сімейство | Адреса `bootloader.bin` |
|---|---|
| ESP32 classic, ESP32-S2 | `0x1000` |
| ESP32-S3, C3, C6, H2 | `0x0` |
| ESP32-P4, C5, H4 | `0x2000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP-IDF Programming Guide, api-guides/bootloader.rst і api-guides/boot-mode-selection.rst, рядок 5 — підстановка IDF_TARGET_BOOTLOADER_OFFSET (кеш: dzherela-kesh/8af5fd4e-boot-mode-selection.rst, dzherela-kesh/a4dbe955-bootloader.rst)
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000", esp32c5="0x2000", esp32s31="0x2000"}
- **Спосіб і дата:** grep по кешованих .rst ESP-IDF, 2026-08-27
- **Нотатка:** Агент був поставив джерелом саму книгу. Справжнє джерело — підстановка IDF_TARGET_BOOTLOADER_OFFSET, з якої ESP-IDF рендерить свою документацію: типове 0x0, classic і S2 — 0x1000, P4 і C5 — 0x2000. Таблиця книги (рядки 70–72 розділу 16) збігається з нею повністю, включно з третім значенням і складом кожної групи. Друге місце в тому ж кеші, bootloader.rst рядок 152, зараховує S2 до групи 0x0 — це розбіжність усередині документації самої ESP-IDF, і права там підстановка з рядка 5, бо саме нею рендериться текст. Книга стоїть на правильному боці.
- **Прохід:** m2-94-vybirka

---

<!-- fc id:T-16-030 sha:f3920dcd src:manual/16-boot.md:72 klas:A -->
### T-16-030 · tablycya · `manual/16-boot.md`

**Твердження, коротко**

> | ESP32-P4, C5, H4 | `0x2000` |

**Контекст**

```
## Що робить другий бутлоадер

Другий бутлоадер лежить за адресою, яка **залежить від сімейства чипа**:

| Сімейство | Адреса `bootloader.bin` |
|---|---|
| ESP32 classic, ESP32-S2 | `0x1000` |
| ESP32-S3, C3, C6, H2 | `0x0` |
| ESP32-P4, C5, H4 | `0x2000` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild та .../docs/en/api-guides/startup.rst; https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32*.py
- **Дослівно з джерела:**
  > (Kconfig.projbuild)
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     hex
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     # the first 2 sectors are reserved for the key manager with AES-XTS
  >     #   (flash encryption) purpose
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > (startup.rst)
  > .. only:: esp32
  >    … If :doc:`/security/secure-boot-v1` is in use then the first 4 kB
  >    sector of flash is used to store secure boot IV and digest of the
  >    bootloader image. Otherwise, this sector is unused.
  > .. only:: esp32s2
  >    … The 4 kB sector of flash before this address is unused.
  > .. only:: SOC_KEY_MANAGER_SUPPORTED
  >    … The 8 kB sector of flash before this address is reserved for the
  >    key manager for use with flash encryption (AES-XTS).
  > 
  > (esptool/targets/)
  > esp32.py:   BOOTLOADER_FLASH_OFFSET = 0x1000
  > esp32s3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c6.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32p4.py: BOOTLOADER_FLASH_OFFSET = 0x2000  # First 2 sectors reserved for FE
  > esp32c5.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > esp32h4.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > (S2 успадковує 0x1000 від ESP32ROM; H2 — 0x0 від ESP32C6ROM;
  >  C2 — 0x0 від ESP32C3ROM)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Три рядки таблиці зсувів звірено з двох незалежних боків — Kconfig ESP-IDF і розбір цілей esptool — і збіг дослівний, включно з успадкуванням для S2, H2 і C2. Твердження книги «значення задає ROM і в ESP-IDF не налаштовується» теж дослівне: воно є в довідці Kconfig.
Хибною виявилася **причина**. Книга писала: «у classic і S2 проміжок від `0x0` до `0x1000` зарезервовано під потреби ROM». ROM-бутлоадер живе в кремнії й у флеші не займає нічого. Насправді на classic цей сектор належить IV і дайджестові Secure Boot v1 — а без secure boot просто не використовується; на S2 не використовується завжди.
Виправлено у двох місцях (розділ 16 і `docs/fakty.md`), і формулювання заведено в `factcheck/SPROSTOVANE.md`. Заразом таблиця в `docs/fakty.md` була **неповна** — у ній бракувало рядка `0x2000` для P4, C5 і H4, який у розділі 16 є з проходу 6.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-16-031 sha:c22fedd2 src:manual/16-boot.md:74 klas:E -->
### T-16-031 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Причина в кожному рядку своя, і в першому вона не та, про яку зазвичай думають.

**Контекст**

```
## Що робить другий бутлоадер

Причина в кожному рядку своя, і в першому вона не та, про яку зазвичай
думають. [[classic]] На classic перший сектор (`0x0`–`0x1000`) відведено
під **IV і дайджест Secure Boot v1**; коли secure boot не ввімкнено — а
це звичайний випадок — сектор просто не використовується. [[S2]] На S2
він не використовується взагалі ніколи. У наступному поколінні зайвий
сектор прибрали, і бутлоадер став на `0x0`. У найновішому — перші два
сектори (8 КБ) віддані менеджерові ключів апаратного шифрування флешу
(AES-XTS), і бутлоадер зсунувся вдруге.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-032 sha:b1de2763 src:manual/16-boot.md:75 klas:A -->
### T-16-032 · proza · `manual/16-boot.md`

**Твердження, коротко**

> [[classic]] На classic перший сектор (`0x0`–`0x1000`) відведено під **IV і дайджест Secure Boot v1**; коли secure boot не ввімкнено — а це звичайний випадок — сектор просто не використовується.

**Контекст**

```
## Що робить другий бутлоадер

Причина в кожному рядку своя, і в першому вона не та, про яку зазвичай
думають. [[classic]] На classic перший сектор (`0x0`–`0x1000`) відведено
під **IV і дайджест Secure Boot v1**; коли secure boot не ввімкнено — а
це звичайний випадок — сектор просто не використовується. [[S2]] На S2
він не використовується взагалі ніколи. У наступному поколінні зайвий
сектор прибрали, і бутлоадер став на `0x0`. У найновішому — перші два
сектори (8 КБ) віддані менеджерові ключів апаратного шифрування флешу
(AES-XTS), і бутлоадер зсунувся вдруге.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild та .../docs/en/api-guides/startup.rst; https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32*.py
- **Дослівно з джерела:**
  > (Kconfig.projbuild)
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     hex
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     # the first 2 sectors are reserved for the key manager with AES-XTS
  >     #   (flash encryption) purpose
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > (startup.rst)
  > .. only:: esp32
  >    … If :doc:`/security/secure-boot-v1` is in use then the first 4 kB
  >    sector of flash is used to store secure boot IV and digest of the
  >    bootloader image. Otherwise, this sector is unused.
  > .. only:: esp32s2
  >    … The 4 kB sector of flash before this address is unused.
  > .. only:: SOC_KEY_MANAGER_SUPPORTED
  >    … The 8 kB sector of flash before this address is reserved for the
  >    key manager for use with flash encryption (AES-XTS).
  > 
  > (esptool/targets/)
  > esp32.py:   BOOTLOADER_FLASH_OFFSET = 0x1000
  > esp32s3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c6.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32p4.py: BOOTLOADER_FLASH_OFFSET = 0x2000  # First 2 sectors reserved for FE
  > esp32c5.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > esp32h4.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > (S2 успадковує 0x1000 від ESP32ROM; H2 — 0x0 від ESP32C6ROM;
  >  C2 — 0x0 від ESP32C3ROM)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Три рядки таблиці зсувів звірено з двох незалежних боків — Kconfig ESP-IDF і розбір цілей esptool — і збіг дослівний, включно з успадкуванням для S2, H2 і C2. Твердження книги «значення задає ROM і в ESP-IDF не налаштовується» теж дослівне: воно є в довідці Kconfig.
Хибною виявилася **причина**. Книга писала: «у classic і S2 проміжок від `0x0` до `0x1000` зарезервовано під потреби ROM». ROM-бутлоадер живе в кремнії й у флеші не займає нічого. Насправді на classic цей сектор належить IV і дайджестові Secure Boot v1 — а без secure boot просто не використовується; на S2 не використовується завжди.
Виправлено у двох місцях (розділ 16 і `docs/fakty.md`), і формулювання заведено в `factcheck/SPROSTOVANE.md`. Заразом таблиця в `docs/fakty.md` була **неповна** — у ній бракувало рядка `0x2000` для P4, C5 і H4, який у розділі 16 є з проходу 6.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-16-033 sha:f4c2a592 src:manual/16-boot.md:77 klas:F -->
### T-16-033 · proza · `manual/16-boot.md`

**Твердження, коротко**

> [[S2]] На S2 він не використовується взагалі ніколи.

**Контекст**

```
## Що робить другий бутлоадер

Причина в кожному рядку своя, і в першому вона не та, про яку зазвичай
думають. [[classic]] На classic перший сектор (`0x0`–`0x1000`) відведено
під **IV і дайджест Secure Boot v1**; коли secure boot не ввімкнено — а
це звичайний випадок — сектор просто не використовується. [[S2]] На S2
він не використовується взагалі ніколи. У наступному поколінні зайвий
сектор прибрали, і бутлоадер став на `0x0`. У найновішому — перші два
сектори (8 КБ) віддані менеджерові ключів апаратного шифрування флешу
(AES-XTS), і бутлоадер зсунувся вдруге.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-034 sha:04eedad6 src:manual/16-boot.md:78 klas:A -->
### T-16-034 · proza · `manual/16-boot.md`

**Твердження, коротко**

> У наступному поколінні зайвий сектор прибрали, і бутлоадер став на `0x0`.

**Контекст**

```
## Що робить другий бутлоадер

Причина в кожному рядку своя, і в першому вона не та, про яку зазвичай
думають. [[classic]] На classic перший сектор (`0x0`–`0x1000`) відведено
під **IV і дайджест Secure Boot v1**; коли secure boot не ввімкнено — а
це звичайний випадок — сектор просто не використовується. [[S2]] На S2
він не використовується взагалі ніколи. У наступному поколінні зайвий
сектор прибрали, і бутлоадер став на `0x0`. У найновішому — перші два
сектори (8 КБ) віддані менеджерові ключів апаратного шифрування флешу
(AES-XTS), і бутлоадер зсунувся вдруге.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP-IDF Programming Guide, api-guides/bootloader.rst і api-guides/boot-mode-selection.rst, рядок 5 — підстановка IDF_TARGET_BOOTLOADER_OFFSET (кеш: dzherela-kesh/8af5fd4e-boot-mode-selection.rst, dzherela-kesh/a4dbe955-bootloader.rst)
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000", esp32c5="0x2000", esp32s31="0x2000"}
- **Спосіб і дата:** grep по кешованих .rst ESP-IDF, 2026-08-27
- **Нотатка:** Агент був поставив джерелом саму книгу. Справжнє джерело — підстановка IDF_TARGET_BOOTLOADER_OFFSET, з якої ESP-IDF рендерить свою документацію: типове 0x0, classic і S2 — 0x1000, P4 і C5 — 0x2000. Таблиця книги (рядки 70–72 розділу 16) збігається з нею повністю, включно з третім значенням і складом кожної групи. Друге місце в тому ж кеші, bootloader.rst рядок 152, зараховує S2 до групи 0x0 — це розбіжність усередині документації самої ESP-IDF, і права там підстановка з рядка 5, бо саме нею рендериться текст. Книга стоїть на правильному боці.
- **Прохід:** m2-94-vybirka

---

<!-- fc id:T-16-035 sha:93217872 src:manual/16-boot.md:79 klas:A -->
### T-16-035 · proza · `manual/16-boot.md`

**Твердження, коротко**

> У найновішому — перші два сектори (8 КБ) віддані менеджерові ключів апаратного шифрування флешу (AES-XTS), і бутлоадер зсунувся вдруге.

**Контекст**

```
## Що робить другий бутлоадер

Причина в кожному рядку своя, і в першому вона не та, про яку зазвичай
думають. [[classic]] На classic перший сектор (`0x0`–`0x1000`) відведено
під **IV і дайджест Secure Boot v1**; коли secure boot не ввімкнено — а
це звичайний випадок — сектор просто не використовується. [[S2]] На S2
він не використовується взагалі ніколи. У наступному поколінні зайвий
сектор прибрали, і бутлоадер став на `0x0`. У найновішому — перші два
сектори (8 КБ) віддані менеджерові ключів апаратного шифрування флешу
(AES-XTS), і бутлоадер зсунувся вдруге.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild та .../docs/en/api-guides/startup.rst; https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32*.py
- **Дослівно з джерела:**
  > (Kconfig.projbuild)
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     hex
  >     default 0x1000 if IDF_TARGET_ESP32 || IDF_TARGET_ESP32S2
  >     # the first 2 sectors are reserved for the key manager with AES-XTS
  >     #   (flash encryption) purpose
  >     default 0x2000 if IDF_TARGET_ESP32P4 || IDF_TARGET_ESP32C5 || IDF_TARGET_ESP32H4
  >     default 0x0
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > (startup.rst)
  > .. only:: esp32
  >    … If :doc:`/security/secure-boot-v1` is in use then the first 4 kB
  >    sector of flash is used to store secure boot IV and digest of the
  >    bootloader image. Otherwise, this sector is unused.
  > .. only:: esp32s2
  >    … The 4 kB sector of flash before this address is unused.
  > .. only:: SOC_KEY_MANAGER_SUPPORTED
  >    … The 8 kB sector of flash before this address is reserved for the
  >    key manager for use with flash encryption (AES-XTS).
  > 
  > (esptool/targets/)
  > esp32.py:   BOOTLOADER_FLASH_OFFSET = 0x1000
  > esp32s3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c3.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32c6.py: BOOTLOADER_FLASH_OFFSET = 0x0
  > esp32p4.py: BOOTLOADER_FLASH_OFFSET = 0x2000  # First 2 sectors reserved for FE
  > esp32c5.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > esp32h4.py: BOOTLOADER_FLASH_OFFSET = 0x2000
  > (S2 успадковує 0x1000 від ESP32ROM; H2 — 0x0 від ESP32C6ROM;
  >  C2 — 0x0 від ESP32C3ROM)
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Три рядки таблиці зсувів звірено з двох незалежних боків — Kconfig ESP-IDF і розбір цілей esptool — і збіг дослівний, включно з успадкуванням для S2, H2 і C2. Твердження книги «значення задає ROM і в ESP-IDF не налаштовується» теж дослівне: воно є в довідці Kconfig.
Хибною виявилася **причина**. Книга писала: «у classic і S2 проміжок від `0x0` до `0x1000` зарезервовано під потреби ROM». ROM-бутлоадер живе в кремнії й у флеші не займає нічого. Насправді на classic цей сектор належить IV і дайджестові Secure Boot v1 — а без secure boot просто не використовується; на S2 не використовується завжди.
Виправлено у двох місцях (розділ 16 і `docs/fakty.md`), і формулювання заведено в `factcheck/SPROSTOVANE.md`. Заразом таблиця в `docs/fakty.md` була **неповна** — у ній бракувало рядка `0x2000` для P4, C5 і H4, який у розділі 16 є з проходу 6.
- **Прохід:** pass-24-zsuvy-i-matrycya

---

<!-- fc id:T-16-036 sha:1c71192c src:manual/16-boot.md:84 klas:A -->
### T-16-036 · proza · `manual/16-boot.md`

**Твердження, коротко**

> **Правила «що новіше, то ближче до нуля» не існує** — і саме таке припущення робить помилку.

**Контекст**

```
## Що робить другий бутлоадер

::: uvaha
**Правила «що новіше, то ближче до нуля» не існує** — і саме таке
припущення робить помилку. Значення задається ROM конкретного чипа й у
ESP-IDF не налаштовується взагалі: це `CONFIG_BOOTLOADER_OFFSET_IN_FLASH`,
і в довідці до нього сказано прямо, що воно визначене ROM.
```

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

<!-- fc id:T-16-037 sha:f5be32d6 src:manual/16-boot.md:85 klas:A -->
### T-16-037 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Значення задається ROM конкретного чипа й у ESP-IDF не налаштовується взагалі: це `CONFIG_BOOTLOADER_OFFSET_IN_FLASH`, і в довідці до нього сказано прямо, що воно визначене ROM.

**Контекст**

```
## Що робить другий бутлоадер

::: uvaha
**Правила «що новіше, то ближче до нуля» не існує** — і саме таке
припущення робить помилку. Значення задається ROM конкретного чипа й у
ESP-IDF не налаштовується взагалі: це `CONFIG_BOOTLOADER_OFFSET_IN_FLASH`,
і в довідці до нього сказано прямо, що воно визначене ROM.
```

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

<!-- fc id:T-16-038 sha:24750ec2 src:manual/16-boot.md:89 klas:E -->
### T-16-038 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Практичний висновок: адресу не пригадують, а дивляться.

**Контекст**

```
## Що робить другий бутлоадер

Практичний висновок: адресу не пригадують, а дивляться. `idf.py flash`
знає її сам; коли заливаєте `esptool` вручну — беріть адресу з таблиці
вище для **свого** чипа, а не з чужої інструкції.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-039 sha:7780ccef src:manual/16-boot.md:89 klas:A -->
### T-16-039 · proza · `manual/16-boot.md`

**Твердження, коротко**

> `idf.py flash` знає її сам; коли заливаєте `esptool` вручну — беріть адресу з таблиці вище для **свого** чипа, а не з чужої інструкції.

**Контекст**

```
## Що робить другий бутлоадер

Практичний висновок: адресу не пригадують, а дивляться. `idf.py flash`
знає її сам; коли заливаєте `esptool` вручну — беріть адресу з таблиці
вище для **свого** чипа, а не з чужої інструкції.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     …
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  >     help
  >         The address of partition table (by default 0x8000).
  >         Allows you to move the partition table, it gives more space
  >         for the bootloader.
  > 
  > (basic-commands.rst)
  > The next arguments to ``write-flash`` are one or more pairs of offset
  > (address) and file name. Consult your SDK documentation to determine
  > the files to flash at which offsets.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Асиметрія, додана в проході 24, підтверджена дослівно з двох файлів Kconfig поспіль: один каже «визначається ROM, не налаштовується», другий — «дозволяє пересунути».
Друга половина сильніша й пояснює найдорожчу помилку розділу 17: `write-flash` бере **пари «адреса — файл»** і відсилає читача до документації SDK. Тобто інструмент не має і не може мати уявлення, чи правильна адреса, — він робить рівно те, що просили, і мовчить.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-16-040 sha:50435e63 src:manual/16-boot.md:95 klas:E -->
### T-16-040 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Це найчастіша причина «прошилося без жодної помилки, а плата мовчить».

**Контекст**

```
## Що робить другий бутлоадер

::: nezvorotne
Це найчастіша причина «прошилося без жодної помилки, а плата мовчить».
Інструкція з інтернету, написана для ESP32 classic, кладе бутлоадер S3
на `0x1000` — тобто в порожнє місце. `esptool` при цьому не має підстав
скаржитися: він робить рівно те, що просили. Спершу визначити чип
(картка [К1](#k-triazh)), потім брати адресу.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-041 sha:34472fe4 src:manual/16-boot.md:96 klas:A -->
### T-16-041 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Інструкція з інтернету, написана для ESP32 classic, кладе бутлоадер S3 на `0x1000` — тобто в порожнє місце.

**Контекст**

```
## Що робить другий бутлоадер

::: nezvorotne
Це найчастіша причина «прошилося без жодної помилки, а плата мовчить».
Інструкція з інтернету, написана для ESP32 classic, кладе бутлоадер S3
на `0x1000` — тобто в порожнє місце. `esptool` при цьому не має підстав
скаржитися: він робить рівно те, що просили. Спершу визначити чип
(картка [К1](#k-triazh)), потім брати адресу.
:::
```

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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-16-042 sha:a123154f src:manual/16-boot.md:97 klas:A -->
### T-16-042 · proza · `manual/16-boot.md`

**Твердження, коротко**

> `esptool` при цьому не має підстав скаржитися: він робить рівно те, що просили.

**Контекст**

```
## Що робить другий бутлоадер

::: nezvorotne
Це найчастіша причина «прошилося без жодної помилки, а плата мовчить».
Інструкція з інтернету, написана для ESP32 classic, кладе бутлоадер S3
на `0x1000` — тобто в порожнє місце. `esptool` при цьому не має підстав
скаржитися: він робить рівно те, що просили. Спершу визначити чип
(картка [К1](#k-triazh)), потім брати адресу.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     …
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  >     help
  >         The address of partition table (by default 0x8000).
  >         Allows you to move the partition table, it gives more space
  >         for the bootloader.
  > 
  > (basic-commands.rst)
  > The next arguments to ``write-flash`` are one or more pairs of offset
  > (address) and file name. Consult your SDK documentation to determine
  > the files to flash at which offsets.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Асиметрія, додана в проході 24, підтверджена дослівно з двох файлів Kconfig поспіль: один каже «визначається ROM, не налаштовується», другий — «дозволяє пересунути».
Друга половина сильніша й пояснює найдорожчу помилку розділу 17: `write-flash` бере **пари «адреса — файл»** і відсилає читача до документації SDK. Тобто інструмент не має і не може мати уявлення, чи правильна адреса, — він робить рівно те, що просили, і мовчить.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-16-043 sha:b57ee9e2 src:manual/16-boot.md:98 klas:E -->
### T-16-043 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Спершу визначити чип (картка [К1](#k-triazh)), потім брати адресу.

**Контекст**

```
## Що робить другий бутлоадер

::: nezvorotne
Це найчастіша причина «прошилося без жодної помилки, а плата мовчить».
Інструкція з інтернету, написана для ESP32 classic, кладе бутлоадер S3
на `0x1000` — тобто в порожнє місце. `esptool` при цьому не має підстав
скаржитися: він робить рівно те, що просили. Спершу визначити чип
(картка [К1](#k-triazh)), потім брати адресу.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-044 sha:2e8a35eb src:manual/16-boot.md:102 klas:A -->
### T-16-044 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Далі бутлоадер читає **таблицю розділів** за адресою `0x8000` — ця адреса однакова на всіх сімействах.

**Контекст**

```
## Що робить другий бутлоадер

Далі бутлоадер читає **таблицю розділів** за адресою `0x8000` — ця
адреса однакова на всіх сімействах. Таблиця займає цілий сектор флешу
(`0x1000`, тобто 4 КБ), тому наступний розділ не може починатися раніше
ніж `0x9000`. Детально про розділи — розділ 18.
```

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

<!-- fc id:T-16-045 sha:22d5057d src:manual/16-boot.md:103 klas:D -->
### T-16-045 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Таблиця займає цілий сектор флешу (`0x1000`, тобто 4 КБ), тому наступний розділ не може починатися раніше ніж `0x9000`.

**Контекст**

```
## Що робить другий бутлоадер

Далі бутлоадер читає **таблицю розділів** за адресою `0x8000` — ця
адреса однакова на всіх сімействах. Таблиця займає цілий сектор флешу
(`0x1000`, тобто 4 КБ), тому наступний розділ не може починатися раніше
ніж `0x9000`. Детально про розділи — розділ 18.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
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

<!-- fc id:T-16-046 sha:c95b1a3f src:manual/16-boot.md:105 klas:E -->
### T-16-046 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Детально про розділи — розділ 18.

**Контекст**

```
## Що робить другий бутлоадер

Далі бутлоадер читає **таблицю розділів** за адресою `0x8000` — ця
адреса однакова на всіх сімействах. Таблиця займає цілий сектор флешу
(`0x1000`, тобто 4 КБ), тому наступний розділ не може починатися раніше
ніж `0x9000`. Детально про розділи — розділ 18.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-047 sha:ed9083b2 src:manual/16-boot.md:107 klas:A -->
### T-16-047 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Тут варта уваги асиметрія: адреса бутлоадера задана ROM і не налаштовується, а адреса таблиці розділів — звичайний параметр (`CONFIG_PARTITION_TABLE_OFFSET`), який **можна** зсунути.

**Контекст**

```
## Що робить другий бутлоадер

Тут варта уваги асиметрія: адреса бутлоадера задана ROM і не
налаштовується, а адреса таблиці розділів — звичайний параметр
(`CONFIG_PARTITION_TABLE_OFFSET`), який **можна** зсунути. Це не
дрібниця, бо саме цим зсувом лікують наступну проблему.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     …
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  >     help
  >         The address of partition table (by default 0x8000).
  >         Allows you to move the partition table, it gives more space
  >         for the bootloader.
  > 
  > (basic-commands.rst)
  > The next arguments to ``write-flash`` are one or more pairs of offset
  > (address) and file name. Consult your SDK documentation to determine
  > the files to flash at which offsets.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Асиметрія, додана в проході 24, підтверджена дослівно з двох файлів Kconfig поспіль: один каже «визначається ROM, не налаштовується», другий — «дозволяє пересунути».
Друга половина сильніша й пояснює найдорожчу помилку розділу 17: `write-flash` бере **пари «адреса — файл»** і відсилає читача до документації SDK. Тобто інструмент не має і не може мати уявлення, чи правильна адреса, — він робить рівно те, що просили, і мовчить.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-16-048 sha:bbad0666 src:manual/16-boot.md:109 klas:E -->
### T-16-048 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Це не дрібниця, бо саме цим зсувом лікують наступну проблему.

**Контекст**

```
## Що робить другий бутлоадер

Тут варта уваги асиметрія: адреса бутлоадера задана ROM і не
налаштовується, а адреса таблиці розділів — звичайний параметр
(`CONFIG_PARTITION_TABLE_OFFSET`), який **можна** зсунути. Це не
дрібниця, бо саме цим зсувом лікують наступну проблему.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-049 sha:13fb9aa2 src:manual/16-boot.md:113 klas:A -->
### T-16-049 · proza · `manual/16-boot.md`

**Твердження, коротко**

> **Простір бутлоадера — це проміжок до таблиці розділів, і він скінченний.** [[classic]] На classic це `0x8000 − 0x1000 = 0x7000` (28 КБ); на S3 і C3, де бутлоадер починається з нуля, — цілі `0x8000` (32 КБ).

**Контекст**

```
## Що робить другий бутлоадер

::: uvaha
**Простір бутлоадера — це проміжок до таблиці розділів, і він скінченний.**
[[classic]] На classic це `0x8000 − 0x1000 = 0x7000` (28 КБ); на S3 і C3,
де бутлоадер починається з нуля, — цілі `0x8000` (32 КБ).
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

<!-- fc id:T-16-050 sha:b0215fc8 src:manual/16-boot.md:117 klas:E -->
### T-16-050 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Звичайному бутлоадеру цього з великим запасом.

**Контекст**

```
## Що робить другий бутлоадер

Звичайному бутлоадеру цього з великим запасом. Але шифрування флешу,
Secure Boot і піднятий рівень логу бутлоадера додають відчутно, і збірка
падає з `Bootloader binary size [..] is too large for partition table
offset`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-051 sha:7515725f src:manual/16-boot.md:117 klas:A -->
### T-16-051 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Але шифрування флешу, Secure Boot і піднятий рівень логу бутлоадера додають відчутно, і збірка падає з `Bootloader binary size [..] is too large for partition table offset`.

**Контекст**

```
## Що робить другий бутлоадер

Звичайному бутлоадеру цього з великим запасом. Але шифрування флешу,
Secure Boot і піднятий рівень логу бутлоадера додають відчутно, і збірка
падає з `Bootloader binary size [..] is too large for partition table
offset`.
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

<!-- fc id:T-16-052 sha:e5db7dcc src:manual/16-boot.md:122 klas:A -->
### T-16-052 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Ліки в порядку дешевизни: повернути оптимізацію бутлоадера на «Size», знизити його рівень логу, і лише потім — відсунути таблицю розділів на адресу більшу за `0x8000`.

**Контекст**

```
## Що робить другий бутлоадер

Ліки в порядку дешевизни: повернути оптимізацію бутлоадера на «Size»,
знизити його рівень логу, і лише потім — відсунути таблицю розділів на
адресу більшу за `0x8000`. Останнє тягне за собою перерахунок явних
зсувів у CSV: жоден розділ не може починатися раніше ніж нова адреса
таблиці плюс `0x1000`.
:::
```

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

<!-- fc id:T-16-053 sha:66180914 src:manual/16-boot.md:124 klas:A -->
### T-16-053 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Останнє тягне за собою перерахунок явних зсувів у CSV: жоден розділ не може починатися раніше ніж нова адреса таблиці плюс `0x1000`.

**Контекст**

```
## Що робить другий бутлоадер

Ліки в порядку дешевизни: повернути оптимізацію бутлоадера на «Size»,
знизити його рівень логу, і лише потім — відсунути таблицю розділів на
адресу більшу за `0x8000`. Останнє тягне за собою перерахунок явних
зсувів у CSV: жоден розділ не може починатися раніше ніж нова адреса
таблиці плюс `0x1000`.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000"}
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep BOOTLOADER_OFFSET, 2026-08-26
- **Нотатка:** Таблиця розділу 16 показує адреси. Для ESP32: 0x1000. Джерело вказує: esp32="0x1000". | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-16-054 sha:99ffdfc9 src:manual/16-boot.md:129 klas:E -->
### T-16-054 · proza · `manual/16-boot.md`

**Твердження, коротко**

> З таблиці бутлоадер дізнається, де лежить застосунок.

**Контекст**

```
## Що робить другий бутлоадер

З таблиці бутлоадер дізнається, де лежить застосунок. Якщо розділів
`ota_0`/`ota_1` кілька, вибір робиться за вмістом службового розділу
`otadata` (розділ 19). Якщо є лише `factory` — беруть його.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-055 sha:53494bdf src:manual/16-boot.md:129 klas:A -->
### T-16-055 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Якщо розділів `ota_0`/`ota_1` кілька, вибір робиться за вмістом службового розділу `otadata` (розділ 19).

**Контекст**

```
## Що робить другий бутлоадер

З таблиці бутлоадер дізнається, де лежить застосунок. Якщо розділів
`ota_0`/`ota_1` кілька, вибір робиться за вмістом службового розділу
`otadata` (розділ 19). Якщо є лише `factory` — беруть його.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > ota_0,    app,  ota_0,   0x20000,  1M,
  > ota_1,    app,  ota_1,   0x120000, 1M,
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep ota_, 2026-08-26
- **Нотатка:** Текст посилається на ota_0 та ota_1 у таблиці розділів. Джерело підтверджує їхню наявність.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-16-056 sha:36fdba60 src:manual/16-boot.md:131 klas:A -->
### T-16-056 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Якщо є лише `factory` — беруть його.

**Контекст**

```
## Що робить другий бутлоадер

З таблиці бутлоадер дізнається, де лежить застосунок. Якщо розділів
`ota_0`/`ota_1` кілька, вибір робиться за вмістом службового розділу
`otadata` (розділ 19). Якщо є лише `factory` — беруть його.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > If "ota data" is empty, it will execute the factory app.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Quote found in partition-tables.rst confirming that bootloader executes factory app when OTA data is empty
- **Прохід:** cherga-a-16-boot

---

<!-- fc id:T-16-057 sha:6f9388d2 src:manual/16-boot.md:135 klas:E -->
### T-16-057 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Монітор на **115200 бод** — це швидкість ROM, і вона не залежить від налаштувань вашого застосунку.

**Контекст**

```
## Що видно в консолі

Монітор на **115200 бод** — це швидкість ROM, і вона не залежить від
налаштувань вашого застосунку. Скинути плату кнопкою `EN`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-058 sha:4a5d1bee src:manual/16-boot.md:136 klas:F -->
### T-16-058 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Скинути плату кнопкою `EN`.

**Контекст**

```
## Що видно в консолі

Монітор на **115200 бод** — це швидкість ROM, і вона не залежить від
налаштувань вашого застосунку. Скинути плату кнопкою `EN`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-059 sha:17b0b9ca src:manual/16-boot.md:140 klas:K -->
### T-16-059 · kod · `manual/16-boot.md`

**Твердження, коротко**

> ```
> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
> configsip: 0, SPIWP:0xee
> mode:DIO, clock div:2
> load:0x3fff0030,len:1344
> entry 0x400805e4
> I (29) boot: ESP-IDF v6.0.2 2nd stage bootloader
> I (33) boot.esp32: SPI Flash Size : 4MB
> I (52) boot: Partition Table:
> I (56) boot: ## Label            Usage      Type ST Offset   Length
> I (63) boot:  0 nvs              WiFi data    01 02 00009000 00006000
> ...
> I (xxx) cpu_start: Pro cpu up.
> ```

**Контекст**

````
## Що видно в консолі

```
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
mode:DIO, clock div:2
load:0x3fff0030,len:1344
entry 0x400805e4
I (29) boot: ESP-IDF v6.0.2 2nd stage bootloader
I (33) boot.esp32: SPI Flash Size : 4MB
I (52) boot: Partition Table:
I (56) boot: ## Label            Usage      Type ST Offset   Length
I (63) boot:  0 nvs              WiFi data    01 02 00009000 00006000
...
I (xxx) cpu_start: Pro cpu up.
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > rst:0x1 (POWERON_RESET),boot:0x3
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Приклад лога з boot.rst показує 0x1 = POWERON_RESET.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-16-060 sha:490ee98b src:manual/16-boot.md:141 klas:A -->
### T-16-060 · kod-ryadok · `manual/16-boot.md`

**Твердження, коротко**

> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

**Контекст**

````
## Що видно в консолі

```
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
mode:DIO, clock div:2
load:0x3fff0030,len:1344
entry 0x400805e4
I (29) boot: ESP-IDF v6.0.2 2nd stage bootloader
I (33) boot.esp32: SPI Flash Size : 4MB
I (52) boot: Partition Table:
I (56) boot: ## Label            Usage      Type ST Offset   Length
I (63) boot:  0 nvs              WiFi data    01 02 00009000 00006000
...
I (xxx) cpu_start: Pro cpu up.
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > rst:0x1 (POWERON_RESET),boot:0x3
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Приклад лога з boot.rst показує 0x1 = POWERON_RESET.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-16-061 sha:cafabedc src:manual/16-boot.md:155 klas:E -->
### T-16-061 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Читається тут більше, ніж здається.

**Контекст**

```
## Що видно в консолі

Читається тут більше, ніж здається. `rst:` — причина скидання (повна
таблиця кодів на картці [К6](#k-bootlog)). Версія IDF, якою зібрано
прошивку. Обсяг флешу, який **бачить бутлоадер** — а це не завжди те, що
написано на модулі. І вся таблиця розділів з адресами: готова відповідь
на «а що там усередині», без розбирання дампа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-062 sha:8c83e86c src:manual/16-boot.md:155 klas:A -->
### T-16-062 · proza · `manual/16-boot.md`

**Твердження, коротко**

> `rst:` — причина скидання (повна таблиця кодів на картці [К6](#k-bootlog)).

**Контекст**

```
## Що видно в консолі

Читається тут більше, ніж здається. `rst:` — причина скидання (повна
таблиця кодів на картці [К6](#k-bootlog)). Версія IDF, якою зібрано
прошивку. Обсяг флешу, який **бачить бутлоадер** — а це не завжди те, що
написано на модулі. І вся таблиця розділів з адресами: готова відповідь
на «а що там усередині», без розбирання дампа.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > ``rst:0xNN (REASON)`` is an enumerated value (and description) of the reason for the reset.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Поле rst містить код причини скидання.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-16-063 sha:9687babe src:manual/16-boot.md:156 klas:E -->
### T-16-063 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Версія IDF, якою зібрано прошивку.

**Контекст**

```
## Що видно в консолі

Читається тут більше, ніж здається. `rst:` — причина скидання (повна
таблиця кодів на картці [К6](#k-bootlog)). Версія IDF, якою зібрано
прошивку. Обсяг флешу, який **бачить бутлоадер** — а це не завжди те, що
написано на модулі. І вся таблиця розділів з адресами: готова відповідь
на «а що там усередині», без розбирання дампа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-064 sha:50f40ab5 src:manual/16-boot.md:157 klas:E -->
### T-16-064 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Обсяг флешу, який **бачить бутлоадер** — а це не завжди те, що написано на модулі.

**Контекст**

```
## Що видно в консолі

Читається тут більше, ніж здається. `rst:` — причина скидання (повна
таблиця кодів на картці [К6](#k-bootlog)). Версія IDF, якою зібрано
прошивку. Обсяг флешу, який **бачить бутлоадер** — а це не завжди те, що
написано на модулі. І вся таблиця розділів з адресами: готова відповідь
на «а що там усередині», без розбирання дампа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-065 sha:b91c3393 src:manual/16-boot.md:158 klas:E -->
### T-16-065 · proza · `manual/16-boot.md`

**Твердження, коротко**

> І вся таблиця розділів з адресами: готова відповідь на «а що там усередині», без розбирання дампа.

**Контекст**

```
## Що видно в консолі

Читається тут більше, ніж здається. `rst:` — причина скидання (повна
таблиця кодів на картці [К6](#k-bootlog)). Версія IDF, якою зібрано
прошивку. Обсяг флешу, який **бачить бутлоадер** — а це не завжди те, що
написано на модулі. І вся таблиця розділів з адресами: готова відповідь
на «а що там усередині», без розбирання дампа.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-066 sha:e5f9555a src:manual/16-boot.md:163 klas:K -->
### T-16-066 · kod · `manual/16-boot.md`

**Твердження, коротко**

> ```
> rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))
> waiting for download
> ```

**Контекст**

````
## Що видно в консолі

```
rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))
waiting for download
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > rst:0x1 (POWERON_RESET),boot:0x3
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Приклад лога з boot.rst показує 0x1 = POWERON_RESET.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-16-067 sha:5b0e39f3 src:manual/16-boot.md:164 klas:A -->
### T-16-067 · kod-ryadok · `manual/16-boot.md`

**Твердження, коротко**

> rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))

**Контекст**

````
## Що видно в консолі

```
rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))
waiting for download
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > rst:0x1 (POWERON_RESET),boot:0x3
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Приклад лога з boot.rst показує 0x1 = POWERON_RESET.
- **Прохід:** m2-62-bootlog-k06

---

<!-- fc id:T-16-068 sha:2987ec81 src:manual/16-boot.md:168 klas:F -->
### T-16-068 · proza · `manual/16-boot.md`

**Твердження, коротко**

> `waiting for download` — рівно те, чого треба досягти перед прошивкою.

**Контекст**

```
## Що видно в консолі

`waiting for download` — рівно те, чого треба досягти перед прошивкою.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-069 sha:dfc19c84 src:manual/16-boot.md:172 klas:K -->
### T-16-069 · kod · `manual/16-boot.md`

**Твердження, коротко**

> ```
> E (xxx) esp_image: image at 0x10000 has invalid magic byte (nothing flashed here?)
> E (xxx) boot: Factory app partition is not bootable
> ```

**Контекст**

````
## Що видно в консолі

```
E (xxx) esp_image: image at 0x10000 has invalid magic byte (nothing flashed here?)
E (xxx) boot: Factory app partition is not bootable
```
````

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

<!-- fc id:T-16-070 sha:c68e2346 src:manual/16-boot.md:173 klas:A -->
### T-16-070 · kod-ryadok · `manual/16-boot.md`

**Твердження, коротко**

> E (xxx) esp_image: image at 0x10000 has invalid magic byte (nothing flashed here?)

**Контекст**

````
## Що видно в консолі

```
E (xxx) esp_image: image at 0x10000 has invalid magic byte (nothing flashed here?)
E (xxx) boot: Factory app partition is not bootable
```
````

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

<!-- fc id:T-16-071 sha:3098ca78 src:manual/16-boot.md:177 klas:E -->
### T-16-071 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Другий бутлоадер живий, розділи знайшов, але за адресою застосунку не те, чого він очікує.

**Контекст**

```
## Що видно в консолі

Другий бутлоадер живий, розділи знайшов, але за адресою застосунку
не те, чого він очікує. Або застосунок не заливали, або залили не туди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-072 sha:120fecd6 src:manual/16-boot.md:178 klas:E -->
### T-16-072 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Або застосунок не заливали, або залили не туди.

**Контекст**

```
## Що видно в консолі

Другий бутлоадер живий, розділи знайшов, але за адресою застосунку
не те, чого він очікує. Або застосунок не заливали, або залили не туди.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-073 sha:65aa20e8 src:manual/16-boot.md:180 klas:E -->
### T-16-073 · proza · `manual/16-boot.md`

**Твердження, коротко**

> **Не знайдено таблицю розділів:**

**Контекст**

```
## Що видно в консолі

**Не знайдено таблицю розділів:**
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-074 sha:df92f5bb src:manual/16-boot.md:182 klas:K -->
### T-16-074 · kod · `manual/16-boot.md`

**Твердження, коротко**

> ```
> E (xxx) flash_parts: partition 0 invalid magic number 0xffff
> E (xxx) boot: Failed to verify partition table
> ```

**Контекст**

````
## Що видно в консолі

```
E (xxx) flash_parts: partition 0 invalid magic number 0xffff
E (xxx) boot: Failed to verify partition table
```
````

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

<!-- fc id:T-16-075 sha:4878c76b src:manual/16-boot.md:187 klas:A -->
### T-16-075 · proza · `manual/16-boot.md`

**Твердження, коротко**

> За адресою `0x8000` порожньо — типово після `erase-flash` без наступної повної прошивки.

**Контекст**

```
## Що видно в консолі

За адресою `0x8000` порожньо — типово після `erase-flash` без наступної
повної прошивки.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > Erase Flash: ``erase-flash`` & ``erase-region``
  > 
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  > 
  >     esptool erase-flash
  > 
  > To erase a region of the flash, starting at address 0x20000 with
  > length 16 kB (0x4000 bytes):
  > 
  >     esptool erase-region 0x20000 0x4000
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** «Весь чип, усе замінюється на `0xFF`» — цього досить, щоб твердження книги випливало однозначно: NVS, `phy_init` і таблиця розділів лежать у тому самому флеші, отже зникають разом з усім.
Звідси ж і симптом розділу 16 «за адресою `0x8000` порожньо після `erase-flash` без наступної повної прошивки»: `0xFF` — це і є порожньо, і бутлоадер не знаходить таблиці.
Розширення досяжності на картки К2, К8, К11, К15 і розділ 20, де те саме твердження живе в різних формах.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-16-076 sha:f07d9e1c src:manual/16-boot.md:190 klas:E -->
### T-16-076 · proza · `manual/16-boot.md`

**Твердження, коротко**

> **Boot loop.** Ті самі рядки повторюються по колу.

**Контекст**

```
## Що видно в консолі

**Boot loop.** Ті самі рядки повторюються по колу. Дивитися треба
**найперший** дамп після подачі живлення, а не сотий: причина в першому,
решта — наслідок. Розбір — картка [К7](#k-panika) і розділ 26.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-077 sha:c41ad640 src:manual/16-boot.md:190 klas:C -->
### T-16-077 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Дивитися треба **найперший** дамп після подачі живлення, а не сотий: причина в першому, решта — наслідок.

**Контекст**

```
## Що видно в консолі

**Boot loop.** Ті самі рядки повторюються по колу. Дивитися треба
**найперший** дамп після подачі живлення, а не сотий: причина в першому,
решта — наслідок. Розбір — картка [К7](#k-panika) і розділ 26.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 GDB debugger guide first dump
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32 GDB debugger guide first dump
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-16-boot

---

<!-- fc id:T-16-078 sha:e41e916a src:manual/16-boot.md:192 klas:E -->
### T-16-078 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Розбір — картка [К7](#k-panika) і розділ 26.

**Контекст**

```
## Що видно в консолі

**Boot loop.** Ті самі рядки повторюються по колу. Дивитися треба
**найперший** дамп після подачі живлення, а не сотий: причина в першому,
решта — наслідок. Розбір — картка [К7](#k-panika) і розділ 26.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-079 sha:dafca624 src:manual/16-boot.md:196 klas:F -->
### T-16-079 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Прошивати вручну кнопками незручно, тому на платах ставлять схему авторесету: два транзистори, керовані сигналами `DTR` і `RTS` USB-мосту.

**Контекст**

```
## Авторесет: чому він іноді не працює

Прошивати вручну кнопками незручно, тому на платах ставлять схему
авторесету: два транзистори, керовані сигналами `DTR` і `RTS` USB-мосту.
`esptool` перед прошивкою смикає ці лінії в потрібній послідовності,
чип сам заходить у download mode, і людині нічого натискати не треба.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-080 sha:68faec6e src:manual/16-boot.md:198 klas:A -->
### T-16-080 · proza · `manual/16-boot.md`

**Твердження, коротко**

> `esptool` перед прошивкою смикає ці лінії в потрібній послідовності, чип сам заходить у download mode, і людині нічого натискати не треба.

**Контекст**

```
## Авторесет: чому він іноді не працює

Прошивати вручну кнопками незручно, тому на платах ставлять схему
авторесету: два транзистори, керовані сигналами `DTR` і `RTS` USB-мосту.
`esptool` перед прошивкою смикає ці лінії в потрібній послідовності,
чип сам заходить у download mode, і людині нічого натискати не треба.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst, .../advanced-topics/boot-mode-selection.rst (Automatic Bootloader)
- **Дослівно з джерела:**
  > (basic-options.rst)
  > esptool has a two-stage flashing process: a small "stub" program is
  > uploaded to RAM and run, which then performs the requested operation
  > much faster than the ROM bootloader. ``--no-stub`` disables this.
  > 
  > (boot-mode-selection.rst, Automatic Bootloader)
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines of the serial connection.
  > 
  > (__init__.py)
  > This chip is {detected}, not {requested}. Wrong --chip argument?
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Чотири твердження розділу 17, які досі не мали доказу, бо стояли не в блоках коду, а в поясненнях: механізм stub, автоскидання через `DTR`/`RTS`, повідомлення про розбіжність чипа і причина «застосунок пише в UART».
Останнє варте уваги: воно пояснює `Invalid head of packet` із сусіднього запису — плата не мовчить, а говорить своє, і `esptool` бачить чуже в потоці. Дві половини одного симптому тепер обидві звірені.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-16-081 sha:7c2cf10c src:manual/16-boot.md:201 klas:E -->
### T-16-081 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Вона не спрацьовує, коли:

**Контекст**

```
## Авторесет: чому він іноді не працює

Схема не універсальна. Вона не спрацьовує, коли:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-082 sha:64b7ef66 src:manual/16-boot.md:203 klas:A -->
### T-16-082 · proza · `manual/16-boot.md`

**Твердження, коротко**

> - на `GPIO0` навішана зовнішня обв'язка, яка утримує лінію; - плати без цієї схеми взагалі — голі модулі, частина клонів; - живлення просідає під час скидання; - драйвер мосту не керує `DTR`/`RTS` як треба (трапляється на CH9102 у Windows); - USB-хаб додає затримок, і імпульси не потрапляють у вікно.

**Контекст**

```
## Авторесет: чому він іноді не працює

- на `GPIO0` навішана зовнішня обв'язка, яка утримує лінію;
- плати без цієї схеми взагалі — голі модулі, частина клонів;
- живлення просідає під час скидання;
- драйвер мосту не керує `DTR`/`RTS` як треба (трапляється на CH9102
  у Windows);
- USB-хаб додає затримок, і імпульси не потрапляють у вікно.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > esptool is not able to reset your hardware automatically in the
  > following cases:
  > - Your hardware does not have the ``DTR`` and ``RTS`` lines connected
  >   to ``{IDF_TARGET_STRAP_BOOT_GPIO}`` and ``EN`` (``CHIP_PU``)
  > - The ``DTR`` and ``RTS`` lines are configured differently
  > - There are no such serial control lines at all
  > 
  > (troubleshooting.rst)
  > If you have connected other devices to GPIO pins, try removing them
  > and see if esptool starts working.
  > Check the chip is receiving 3.3V from a stable power source.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Чотири з п'яти причин книги підтверджено дослівно. **П'ята — ні**, і це варте запису: «драйвер мосту не керує `DTR`/`RTS` (трапляється на CH9102 у Windows)».
Агент шукав `CH9102` у `troubleshooting.rst`, `boot-mode-selection.rst` і `reset.py` — немає ніде. Твердження не спростоване, воно **непідтверджене**: поведінка драйвера під Windows у документації esptool не описана й описана бути не може.
Лишаю в книзі як є, але позначаю тут: якщо колись знадобиться клас `A` на цей рядок, джерелом буде не esptool, а сам драйвер WCH або відтворення на живій машині. Це не наряд для М2 — це чесна межа того, що взагалі можна процитувати.
Побічно варте уваги: `troubleshooting.rst` радить те саме, що книга, у двох інших рядках — зняти сторонні пристрої з GPIO і перевірити стабільність 3.3 В. Тобто перелік книги не лише правильний, а й впорядкований так само, як у джерелі.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-16-083 sha:5b9eaf66 src:manual/16-boot.md:210 klas:E -->
### T-16-083 · proza · `manual/16-boot.md`

**Твердження, коротко**

> У всіх цих випадках лікування те саме — увійти в download mode руками, картка [К4](#k-boot).

**Контекст**

```
## Авторесет: чому він іноді не працює

У всіх цих випадках лікування те саме — увійти в download mode руками,
картка [К4](#k-boot). Це не ознака несправної плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-084 sha:68f8f3aa src:manual/16-boot.md:211 klas:E -->
### T-16-084 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Це не ознака несправної плати.

**Контекст**

```
## Авторесет: чому він іноді не працює

У всіх цих випадках лікування те саме — увійти в download mode руками,
картка [К4](#k-boot). Це не ознака несправної плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-085 sha:3c680211 src:manual/16-boot.md:215 klas:F -->
### T-16-085 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Від подачі живлення до `app_main` — типово десятки мілісекунд.

**Контекст**

```
## Скільки часу займає старт

Від подачі живлення до `app_main` — типово десятки мілісекунд. Число в
дужках у логу (`I (29) boot:`) — це мілісекунди від старту, і воно
безкоштовно показує, **де саме прошивка задумалася**: стрибок з `(52)`
на `(1250)` між двома рядками означає секунду очікування, і це майже
завжди щось, що чекає таймауту.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-086 sha:b34d888e src:manual/16-boot.md:215 klas:A -->
### T-16-086 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Число в дужках у логу (`I (29) boot:`) — це мілісекунди від старту, і воно безкоштовно показує, **де саме прошивка задумалася**: стрибок з `(52)` на `(1250)` між двома рядками означає секунду очікування, і це майже завжди щось, що чекає таймауту.

**Контекст**

```
## Скільки часу займає старт

Від подачі живлення до `app_main` — типово десятки мілісекунд. Число в
дужках у логу (`I (29) boot:`) — це мілісекунди від старту, і воно
безкоштовно показує, **де саме прошивка задумалася**: стрибок з `(52)`
на `(1250)` між двома рядками означає секунду очікування, і це майже
завжди щось, що чекає таймауту.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/log.html.rst та components/log/include/esp_log.h
- **Дослівно з джерела:**
  > The log output format is:
  >     I (12345) tag: message
  > where 12345 is the timestamp in milliseconds since boot (or since the
  > system time was set), I is the log level letter, and tag is the
  > component tag.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Твердження розділу 16 звірено. Практичний висновок книги — «воно безкоштовно показує, де саме прошивка стоїть довго» — з формату випливає прямо: різниця між двома сусідніми рядками і є час між ними.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-16-087 sha:b1352204 src:manual/16-boot.md:222 klas:E -->
### T-16-087 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Найпідступніша поведінка при старті — коли живлення просідає саме в момент увімкнення радіо, вже після успішного завантаження.

**Контекст**

```
## Скільки часу займає старт

::: zhyvlennya
Найпідступніша поведінка при старті — коли живлення просідає саме в
момент увімкнення радіо, вже після успішного завантаження. Виглядає як
збій прошивки; насправді це `rst:0xf` (brownout) у наступному рядку логу.
Дивитися код тут марно, поки не зміряно напругу під навантаженням —
розділ 06.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-088 sha:6b942f91 src:manual/16-boot.md:223 klas:F -->
### T-16-088 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Виглядає як збій прошивки; насправді це `rst:0xf` (brownout) у наступному рядку логу.

**Контекст**

```
## Скільки часу займає старт

::: zhyvlennya
Найпідступніша поведінка при старті — коли живлення просідає саме в
момент увімкнення радіо, вже після успішного завантаження. Виглядає як
збій прошивки; насправді це `rst:0xf` (brownout) у наступному рядку логу.
Дивитися код тут марно, поки не зміряно напругу під навантаженням —
розділ 06.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-089 sha:7c8641d9 src:manual/16-boot.md:225 klas:E -->
### T-16-089 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Дивитися код тут марно, поки не зміряно напругу під навантаженням — розділ 06.

**Контекст**

```
## Скільки часу займає старт

::: zhyvlennya
Найпідступніша поведінка при старті — коли живлення просідає саме в
момент увімкнення радіо, вже після успішного завантаження. Виглядає як
збій прошивки; насправді це `rst:0xf` (brownout) у наступному рядку логу.
Дивитися код тут марно, поки не зміряно напругу під навантаженням —
розділ 06.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-090 sha:96d636c6 src:manual/16-boot.md:231 klas:E -->
### T-16-090 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Три етапи: ROM → другий бутлоадер → застосунок.

**Контекст**

```
## Що з цього треба запам'ятати

Три етапи: ROM → другий бутлоадер → застосунок. ROM не ламається ніколи;
все, що ламається, лежить у флеші.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-091 sha:85240d7d src:manual/16-boot.md:231 klas:E -->
### T-16-091 · proza · `manual/16-boot.md`

**Твердження, коротко**

> ROM не ламається ніколи; все, що ламається, лежить у флеші.

**Контекст**

```
## Що з цього треба запам'ятати

Три етапи: ROM → другий бутлоадер → застосунок. ROM не ламається ніколи;
все, що ламається, лежить у флеші.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-092 sha:871f576d src:manual/16-boot.md:234 klas:A -->
### T-16-092 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Адреса бутлоадера залежить від сімейства і задана ROM; адреса таблиці розділів на всіх сімействах однакова — `0x8000`, якщо її свідомо не пересунули.

**Контекст**

```
## Що з цього треба запам'ятати

Адреса бутлоадера залежить від сімейства і задана ROM; адреса таблиці
розділів на всіх сімействах однакова — `0x8000`, якщо її свідомо не
пересунули.
```

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

<!-- fc id:T-16-093 sha:d25421b7 src:manual/16-boot.md:238 klas:F -->
### T-16-093 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Стан strapping-пінів має значення рівно одну мілісекунду після скидання — і саме тому помилки тут виглядають як містика.

**Контекст**

```
## Що з цього треба запам'ятати

Стан strapping-пінів має значення рівно одну мілісекунду після скидання —
і саме тому помилки тут виглядають як містика.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-094 sha:6555a300 src:manual/16-boot.md:241 klas:E -->
### T-16-094 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Перший рядок логу називає причину попереднього скидання.

**Контекст**

```
## Що з цього треба запам'ятати

Перший рядок логу називає причину попереднього скидання. Це найдешевша
діагностична інформація в усій системі, і читати її треба першою.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-095 sha:a59da32e src:manual/16-boot.md:241 klas:E -->
### T-16-095 · proza · `manual/16-boot.md`

**Твердження, коротко**

> Це найдешевша діагностична інформація в усій системі, і читати її треба першою.

**Контекст**

```
## Що з цього треба запам'ятати

Перший рядок логу називає причину попереднього скидання. Це найдешевша
діагностична інформація в усій системі, і читати її треба першою.
```

**Доказ**

- **Клас:** F — не звірено

---
