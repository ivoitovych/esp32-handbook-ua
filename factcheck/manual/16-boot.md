# Фактчекінг: `manual/16-boot.md`

Одиниць твердження: **95**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-16-001 sha:349f6843 src:manual/16-boot.md:3 klas:E -->
### T-16-001 · proza · рядок 3

**Книга каже, дослівно:**

> Між подачею живлення і першим рядком вашого коду проходить три етапи, і на кожному чип може зупинитися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-002 sha:11f1c487 src:manual/16-boot.md:3 klas:A -->
### T-16-002 · proza · рядок 3

**Книга каже, дослівно:**

> Розуміння цього ланцюжка — різниця між «плата чомусь не працює» і «плата зупинилася на другому етапі, бо не знайшла таблицю розділів за адресою `0x8000`».

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
### T-16-003 · proza · рядок 8

**Книга каже, дослівно:**

> Це найкорисніші двадцять хвилин, які можна витратити на теорію: майже вся діагностика прошивки (розділ 29) зводиться до питання «на якому етапі воно стало».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-004 sha:37a50017 src:manual/16-boot.md:14 klas:F -->
### T-16-004 · proza · рядок 14

**Книга каже, дослівно:**

> **Етап 1 — ROM bootloader.** Зашитий у кремній на заводі, змінити його неможливо.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-005 sha:df2dec6a src:manual/16-boot.md:14 klas:E -->
### T-16-005 · proza · рядок 14

**Книга каже, дослівно:**

> Він стартує завжди, незалежно від того, що у флеші.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-006 sha:e47891e7 src:manual/16-boot.md:14 klas:E -->
### T-16-006 · proza · рядок 14

**Книга каже, дослівно:**

> Саме тому плата з повністю стертим флешем все одно подає ознаки життя: ROM живий.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-007 sha:d51c3c70 src:manual/16-boot.md:18 klas:F -->
### T-16-007 · proza · рядок 18

**Книга каже, дослівно:**

> Завдання ROM-бутлоадера: подивитися на strapping-піни і вирішити, звідки брати наступний код — з флешу чи з UART.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-008 sha:371e3feb src:manual/16-boot.md:21 klas:F -->
### T-16-008 · proza · рядок 21

**Книга каже, дослівно:**

> **Етап 2 — другий бутлоадер (bootloader.bin).** Уже ваш, лежить у флеші, збирається разом із проєктом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-009 sha:73a47ca1 src:manual/16-boot.md:21 klas:E -->
### T-16-009 · proza · рядок 21

**Книга каже, дослівно:**

> Він налаштовує тактування і флеш, читає таблицю розділів, обирає активний розділ застосунку, перевіряє його і передає керування.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-010 sha:8b2614cd src:manual/16-boot.md:26 klas:F -->
### T-16-010 · proza · рядок 26

**Книга каже, дослівно:**

> **Етап 3 — застосунок.** Ініціалізація FreeRTOS, потім `app_main` (в ESP-IDF) або `setup`/`loop` (в Arduino core).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-011 sha:b8f3d5d1 src:manual/16-boot.md:29 klas:E -->
### T-16-011 · proza · рядок 29

**Книга каже, дослівно:**

> Головне практичне: **етапи 2 і 3 живуть у флеші за фіксованими адресами**, і якщо хоч одна адреса не та, ланцюжок рветься мовчки — без повідомлення про помилку, просто без результату.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-012 sha:719a564d src:manual/16-boot.md:35 klas:F -->
### T-16-012 · proza · рядок 35

**Книга каже, дослівно:**

> Strapping-пін — це звичайний GPIO, стан якого читається **один раз**, у момент відпускання скидання, і потім більше не має значення для завантаження.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-013 sha:2e09aa20 src:manual/16-boot.md:35 klas:E -->
### T-16-013 · proza · рядок 35

**Книга каже, дослівно:**

> Далі пін працює як звичайний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-014 sha:bd61d296 src:manual/16-boot.md:39 klas:F -->
### T-16-014 · proza · рядок 39

**Книга каже, дослівно:**

> Ключовий — `GPIO0` [[classic]] [[S3]]:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-015 sha:10272434 src:manual/16-boot.md:41 klas:F -->
### T-16-015 · tablycya · рядок 41

**Книга каже, дослівно:**

> | `GPIO0` при скиданні | Куди піде ROM |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-016 sha:93a3f980 src:manual/16-boot.md:43 klas:E -->
### T-16-016 · tablycya · рядок 43

**Книга каже, дослівно:**

> | високий (підтягнутий вгору) | звичайний старт із флешу |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-017 sha:08cf4b01 src:manual/16-boot.md:44 klas:F -->
### T-16-017 · tablycya · рядок 44

**Книга каже, дослівно:**

> | низький (притиснутий до землі) | download mode: чекає прошивку по UART |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-018 sha:232b5f4b src:manual/16-boot.md:46 klas:A -->
### T-16-018 · proza · рядок 46

**Книга каже, дослівно:**

> Для [[C3]] роль іншу грає пара пінів: `GPIO9` притиснутий до землі вмикає download mode, і `GPIO8` при цьому має бути високим.

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
### T-16-019 · proza · рядок 49

**Книга каже, дослівно:**

> Повний перелік strapping-пінів по сімействах — картка [К9](#k-pinouty), вхід у download mode вручну — картка [К4](#k-boot).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-020 sha:3a71c61e src:manual/16-boot.md:53 klas:F -->
### T-16-020 · proza · рядок 53

**Книга каже, дослівно:**

> Це пояснює цілий клас загадкових несправностей: **зовнішня обв'язка на strapping-піні**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-021 sha:728e14e7 src:manual/16-boot.md:53 klas:F -->
### T-16-021 · proza · рядок 53

**Книга каже, дослівно:**

> Світлодіод із резистором на `GPIO0`, датчик, що тримає лінію низькою, довгий дріт, який ловить наводку — і плата стартує не туди або не стартує взагалі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-022 sha:1a088eeb src:manual/16-boot.md:53 klas:F -->
### T-16-022 · proza · рядок 53

**Книга каже, дослівно:**

> Причому в коді все правильно, і в 99 % часу пін поводиться нормально: значення має лише мілісекунда після скидання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-023 sha:b274c770 src:manual/16-boot.md:59 klas:A -->
### T-16-023 · proza · рядок 59

**Книга каже, дослівно:**

> [[classic]] Найзліший випадок — `GPIO12` (MTDI).

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
### T-16-024 · proza · рядок 59

**Книга каже, дослівно:**

> Він задає напругу живлення флешу.

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

<!-- fc id:T-16-025 sha:4de10478 src:manual/16-boot.md:59 klas:E -->
### T-16-025 · proza · рядок 59

**Книга каже, дослівно:**

> Підтягнутий вгору при старті — і плата не стартує взагалі, без жодного повідомлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-026 sha:a976fca3 src:manual/16-boot.md:66 klas:A -->
### T-16-026 · proza · рядок 66

**Книга каже, дослівно:**

> Другий бутлоадер лежить за адресою, яка **залежить від сімейства чипа**:

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
### T-16-027 · tablycya · рядок 68

**Книга каже, дослівно:**

> | Сімейство | Адреса `bootloader.bin` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-028 sha:30495adc src:manual/16-boot.md:70 klas:A -->
### T-16-028 · tablycya · рядок 70

**Книга каже, дослівно:**

> | ESP32 classic, ESP32-S2 | `0x1000` |

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
### T-16-029 · tablycya · рядок 71

**Книга каже, дослівно:**

> | ESP32-S3, C3, C6, H2 | `0x0` |

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

<!-- fc id:T-16-030 sha:f3920dcd src:manual/16-boot.md:72 klas:A -->
### T-16-030 · tablycya · рядок 72

**Книга каже, дослівно:**

> | ESP32-P4, C5, H4 | `0x2000` |

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
### T-16-031 · proza · рядок 74

**Книга каже, дослівно:**

> Причина в кожному рядку своя, і в першому вона не та, про яку зазвичай думають.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-032 sha:b1de2763 src:manual/16-boot.md:74 klas:A -->
### T-16-032 · proza · рядок 74

**Книга каже, дослівно:**

> [[classic]] На classic перший сектор (`0x0`–`0x1000`) відведено під **IV і дайджест Secure Boot v1**; коли secure boot не ввімкнено — а це звичайний випадок — сектор просто не використовується.

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

<!-- fc id:T-16-033 sha:f4c2a592 src:manual/16-boot.md:74 klas:F -->
### T-16-033 · proza · рядок 74

**Книга каже, дослівно:**

> [[S2]] На S2 він не використовується взагалі ніколи.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-034 sha:04eedad6 src:manual/16-boot.md:74 klas:F -->
### T-16-034 · proza · рядок 74

**Книга каже, дослівно:**

> У наступному поколінні зайвий сектор прибрали, і бутлоадер став на `0x0`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-035 sha:93217872 src:manual/16-boot.md:74 klas:A -->
### T-16-035 · proza · рядок 74

**Книга каже, дослівно:**

> У найновішому — перші два сектори (8 КБ) віддані менеджерові ключів апаратного шифрування флешу (AES-XTS), і бутлоадер зсунувся вдруге.

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
### T-16-036 · proza · рядок 84

**Книга каже, дослівно:**

> **Правила «що новіше, то ближче до нуля» не існує** — і саме таке припущення робить помилку.

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

<!-- fc id:T-16-037 sha:f5be32d6 src:manual/16-boot.md:84 klas:A -->
### T-16-037 · proza · рядок 84

**Книга каже, дослівно:**

> Значення задається ROM конкретного чипа й у ESP-IDF не налаштовується взагалі: це `CONFIG_BOOTLOADER_OFFSET_IN_FLASH`, і в довідці до нього сказано прямо, що воно визначене ROM.

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
### T-16-038 · proza · рядок 89

**Книга каже, дослівно:**

> Практичний висновок: адресу не пригадують, а дивляться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-039 sha:7780ccef src:manual/16-boot.md:89 klas:F -->
### T-16-039 · proza · рядок 89

**Книга каже, дослівно:**

> `idf.py flash` знає її сам; коли заливаєте `esptool` вручну — беріть адресу з таблиці вище для **свого** чипа, а не з чужої інструкції.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-040 sha:50435e63 src:manual/16-boot.md:95 klas:E -->
### T-16-040 · proza · рядок 95

**Книга каже, дослівно:**

> Це найчастіша причина «прошилося без жодної помилки, а плата мовчить».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-041 sha:34472fe4 src:manual/16-boot.md:95 klas:F -->
### T-16-041 · proza · рядок 95

**Книга каже, дослівно:**

> Інструкція з інтернету, написана для ESP32 classic, кладе бутлоадер S3 на `0x1000` — тобто в порожнє місце.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-042 sha:a123154f src:manual/16-boot.md:95 klas:F -->
### T-16-042 · proza · рядок 95

**Книга каже, дослівно:**

> `esptool` при цьому не має підстав скаржитися: він робить рівно те, що просили.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-043 sha:b57ee9e2 src:manual/16-boot.md:95 klas:E -->
### T-16-043 · proza · рядок 95

**Книга каже, дослівно:**

> Спершу визначити чип (картка [К1](#k-triazh)), потім брати адресу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-044 sha:2e8a35eb src:manual/16-boot.md:102 klas:A -->
### T-16-044 · proza · рядок 102

**Книга каже, дослівно:**

> Далі бутлоадер читає **таблицю розділів** за адресою `0x8000` — ця адреса однакова на всіх сімействах.

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

<!-- fc id:T-16-045 sha:22d5057d src:manual/16-boot.md:102 klas:D -->
### T-16-045 · proza · рядок 102

**Книга каже, дослівно:**

> Таблиця займає цілий сектор флешу (`0x1000`, тобто 4 КБ), тому наступний розділ не може починатися раніше ніж `0x9000`.

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

<!-- fc id:T-16-046 sha:c95b1a3f src:manual/16-boot.md:102 klas:E -->
### T-16-046 · proza · рядок 102

**Книга каже, дослівно:**

> Детально про розділи — розділ 18.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-047 sha:ed9083b2 src:manual/16-boot.md:107 klas:F -->
### T-16-047 · proza · рядок 107

**Книга каже, дослівно:**

> Тут варта уваги асиметрія: адреса бутлоадера задана ROM і не налаштовується, а адреса таблиці розділів — звичайний параметр (`CONFIG_PARTITION_TABLE_OFFSET`), який **можна** зсунути.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-048 sha:bbad0666 src:manual/16-boot.md:107 klas:E -->
### T-16-048 · proza · рядок 107

**Книга каже, дослівно:**

> Це не дрібниця, бо саме цим зсувом лікують наступну проблему.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-049 sha:13fb9aa2 src:manual/16-boot.md:113 klas:A -->
### T-16-049 · proza · рядок 113

**Книга каже, дослівно:**

> **Простір бутлоадера — це проміжок до таблиці розділів, і він скінченний.** [[classic]] На classic це `0x8000 − 0x1000 = 0x7000` (28 КБ); на S3 і C3, де бутлоадер починається з нуля, — цілі `0x8000` (32 КБ).

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
### T-16-050 · proza · рядок 117

**Книга каже, дослівно:**

> Звичайному бутлоадеру цього з великим запасом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-051 sha:7515725f src:manual/16-boot.md:117 klas:A -->
### T-16-051 · proza · рядок 117

**Книга каже, дослівно:**

> Але шифрування флешу, Secure Boot і піднятий рівень логу бутлоадера додають відчутно, і збірка падає з `Bootloader binary size [..] is too large for partition table offset`.

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
### T-16-052 · proza · рядок 122

**Книга каже, дослівно:**

> Ліки в порядку дешевизни: повернути оптимізацію бутлоадера на «Size», знизити його рівень логу, і лише потім — відсунути таблицю розділів на адресу більшу за `0x8000`.

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

<!-- fc id:T-16-053 sha:66180914 src:manual/16-boot.md:122 klas:D -->
### T-16-053 · proza · рядок 122

**Книга каже, дослівно:**

> Останнє тягне за собою перерахунок явних зсувів у CSV: жоден розділ не може починатися раніше ніж нова адреса таблиці плюс `0x1000`.

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

<!-- fc id:T-16-054 sha:99ffdfc9 src:manual/16-boot.md:129 klas:E -->
### T-16-054 · proza · рядок 129

**Книга каже, дослівно:**

> З таблиці бутлоадер дізнається, де лежить застосунок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-055 sha:53494bdf src:manual/16-boot.md:129 klas:F -->
### T-16-055 · proza · рядок 129

**Книга каже, дослівно:**

> Якщо розділів `ota_0`/`ota_1` кілька, вибір робиться за вмістом службового розділу `otadata` (розділ 19).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-056 sha:36fdba60 src:manual/16-boot.md:129 klas:F -->
### T-16-056 · proza · рядок 129

**Книга каже, дослівно:**

> Якщо є лише `factory` — беруть його.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-057 sha:6f9388d2 src:manual/16-boot.md:135 klas:E -->
### T-16-057 · proza · рядок 135

**Книга каже, дослівно:**

> Монітор на **115200 бод** — це швидкість ROM, і вона не залежить від налаштувань вашого застосунку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-058 sha:4a5d1bee src:manual/16-boot.md:135 klas:F -->
### T-16-058 · proza · рядок 135

**Книга каже, дослівно:**

> Скинути плату кнопкою `EN`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-059 sha:17b0b9ca src:manual/16-boot.md:140 klas:K -->
### T-16-059 · kod · рядок 140

**Книга каже, дослівно:**

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

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-16-060 sha:490ee98b src:manual/16-boot.md:141 klas:A -->
### T-16-060 · kod-ryadok · рядок 141

**Книга каже, дослівно:**

> rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-16-061 sha:cafabedc src:manual/16-boot.md:155 klas:E -->
### T-16-061 · proza · рядок 155

**Книга каже, дослівно:**

> Читається тут більше, ніж здається.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-062 sha:8c83e86c src:manual/16-boot.md:155 klas:F -->
### T-16-062 · proza · рядок 155

**Книга каже, дослівно:**

> `rst:` — причина скидання (повна таблиця кодів на картці [К6](#k-bootlog)).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-063 sha:9687babe src:manual/16-boot.md:155 klas:E -->
### T-16-063 · proza · рядок 155

**Книга каже, дослівно:**

> Версія IDF, якою зібрано прошивку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-064 sha:50f40ab5 src:manual/16-boot.md:155 klas:E -->
### T-16-064 · proza · рядок 155

**Книга каже, дослівно:**

> Обсяг флешу, який **бачить бутлоадер** — а це не завжди те, що написано на модулі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-065 sha:b91c3393 src:manual/16-boot.md:155 klas:E -->
### T-16-065 · proza · рядок 155

**Книга каже, дослівно:**

> І вся таблиця розділів з адресами: готова відповідь на «а що там усередині», без розбирання дампа.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-066 sha:e5f9555a src:manual/16-boot.md:163 klas:K -->
### T-16-066 · kod · рядок 163

**Книга каже, дослівно:**

> ```
> rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))
> waiting for download
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-16-067 sha:5b0e39f3 src:manual/16-boot.md:164 klas:A -->
### T-16-067 · kod-ryadok · рядок 164

**Книга каже, дослівно:**

> rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-16-068 sha:2987ec81 src:manual/16-boot.md:168 klas:F -->
### T-16-068 · proza · рядок 168

**Книга каже, дослівно:**

> `waiting for download` — рівно те, чого треба досягти перед прошивкою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-069 sha:dfc19c84 src:manual/16-boot.md:172 klas:K -->
### T-16-069 · kod · рядок 172

**Книга каже, дослівно:**

> ```
> E (xxx) esp_image: image at 0x10000 has invalid magic byte (nothing flashed here?)
> E (xxx) boot: Factory app partition is not bootable
> ```

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
### T-16-070 · kod-ryadok · рядок 173

**Книга каже, дослівно:**

> E (xxx) esp_image: image at 0x10000 has invalid magic byte (nothing flashed here?)

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
### T-16-071 · proza · рядок 177

**Книга каже, дослівно:**

> Другий бутлоадер живий, розділи знайшов, але за адресою застосунку не те, чого він очікує.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-072 sha:120fecd6 src:manual/16-boot.md:177 klas:E -->
### T-16-072 · proza · рядок 177

**Книга каже, дослівно:**

> Або застосунок не заливали, або залили не туди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-073 sha:65aa20e8 src:manual/16-boot.md:180 klas:E -->
### T-16-073 · proza · рядок 180

**Книга каже, дослівно:**

> **Не знайдено таблицю розділів:**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-074 sha:df92f5bb src:manual/16-boot.md:182 klas:K -->
### T-16-074 · kod · рядок 182

**Книга каже, дослівно:**

> ```
> E (xxx) flash_parts: partition 0 invalid magic number 0xffff
> E (xxx) boot: Failed to verify partition table
> ```

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

<!-- fc id:T-16-075 sha:4878c76b src:manual/16-boot.md:187 klas:F -->
### T-16-075 · proza · рядок 187

**Книга каже, дослівно:**

> За адресою `0x8000` порожньо — типово після `erase-flash` без наступної повної прошивки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-076 sha:f07d9e1c src:manual/16-boot.md:190 klas:E -->
### T-16-076 · proza · рядок 190

**Книга каже, дослівно:**

> **Boot loop.** Ті самі рядки повторюються по колу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-077 sha:c41ad640 src:manual/16-boot.md:190 klas:E -->
### T-16-077 · proza · рядок 190

**Книга каже, дослівно:**

> Дивитися треба **найперший** дамп після подачі живлення, а не сотий: причина в першому, решта — наслідок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-078 sha:e41e916a src:manual/16-boot.md:190 klas:E -->
### T-16-078 · proza · рядок 190

**Книга каже, дослівно:**

> Розбір — картка [К7](#k-panika) і розділ 26.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-079 sha:dafca624 src:manual/16-boot.md:196 klas:F -->
### T-16-079 · proza · рядок 196

**Книга каже, дослівно:**

> Прошивати вручну кнопками незручно, тому на платах ставлять схему авторесету: два транзистори, керовані сигналами `DTR` і `RTS` USB-мосту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-080 sha:68faec6e src:manual/16-boot.md:196 klas:F -->
### T-16-080 · proza · рядок 196

**Книга каже, дослівно:**

> `esptool` перед прошивкою смикає ці лінії в потрібній послідовності, чип сам заходить у download mode, і людині нічого натискати не треба.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-081 sha:7c2cf10c src:manual/16-boot.md:201 klas:E -->
### T-16-081 · proza · рядок 201

**Книга каже, дослівно:**

> Вона не спрацьовує, коли:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-082 sha:64b7ef66 src:manual/16-boot.md:203 klas:F -->
### T-16-082 · proza · рядок 203

**Книга каже, дослівно:**

> - на `GPIO0` навішана зовнішня обв'язка, яка утримує лінію; - плати без цієї схеми взагалі — голі модулі, частина клонів; - живлення просідає під час скидання; - драйвер мосту не керує `DTR`/`RTS` як треба (трапляється на CH9102 у Windows); - USB-хаб додає затримок, і імпульси не потрапляють у вікно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-083 sha:5b9eaf66 src:manual/16-boot.md:210 klas:E -->
### T-16-083 · proza · рядок 210

**Книга каже, дослівно:**

> У всіх цих випадках лікування те саме — увійти в download mode руками, картка [К4](#k-boot).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-084 sha:68f8f3aa src:manual/16-boot.md:210 klas:E -->
### T-16-084 · proza · рядок 210

**Книга каже, дослівно:**

> Це не ознака несправної плати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-085 sha:3c680211 src:manual/16-boot.md:215 klas:F -->
### T-16-085 · proza · рядок 215

**Книга каже, дослівно:**

> Від подачі живлення до `app_main` — типово десятки мілісекунд.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-086 sha:b34d888e src:manual/16-boot.md:215 klas:F -->
### T-16-086 · proza · рядок 215

**Книга каже, дослівно:**

> Число в дужках у логу (`I (29) boot:`) — це мілісекунди від старту, і воно безкоштовно показує, **де саме прошивка задумалася**: стрибок з `(52)` на `(1250)` між двома рядками означає секунду очікування, і це майже завжди щось, що чекає таймауту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-087 sha:b1352204 src:manual/16-boot.md:222 klas:E -->
### T-16-087 · proza · рядок 222

**Книга каже, дослівно:**

> Найпідступніша поведінка при старті — коли живлення просідає саме в момент увімкнення радіо, вже після успішного завантаження.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-088 sha:6b942f91 src:manual/16-boot.md:222 klas:F -->
### T-16-088 · proza · рядок 222

**Книга каже, дослівно:**

> Виглядає як збій прошивки; насправді це `rst:0xf` (brownout) у наступному рядку логу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-089 sha:7c8641d9 src:manual/16-boot.md:222 klas:E -->
### T-16-089 · proza · рядок 222

**Книга каже, дослівно:**

> Дивитися код тут марно, поки не зміряно напругу під навантаженням — розділ 06.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-090 sha:96d636c6 src:manual/16-boot.md:231 klas:E -->
### T-16-090 · proza · рядок 231

**Книга каже, дослівно:**

> Три етапи: ROM → другий бутлоадер → застосунок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-091 sha:85240d7d src:manual/16-boot.md:231 klas:E -->
### T-16-091 · proza · рядок 231

**Книга каже, дослівно:**

> ROM не ламається ніколи; все, що ламається, лежить у флеші.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-092 sha:871f576d src:manual/16-boot.md:234 klas:A -->
### T-16-092 · proza · рядок 234

**Книга каже, дослівно:**

> Адреса бутлоадера залежить від сімейства і задана ROM; адреса таблиці розділів на всіх сімействах однакова — `0x8000`, якщо її свідомо не пересунули.

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
### T-16-093 · proza · рядок 238

**Книга каже, дослівно:**

> Стан strapping-пінів має значення рівно одну мілісекунду після скидання — і саме тому помилки тут виглядають як містика.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-094 sha:6555a300 src:manual/16-boot.md:241 klas:E -->
### T-16-094 · proza · рядок 241

**Книга каже, дослівно:**

> Перший рядок логу називає причину попереднього скидання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-16-095 sha:a59da32e src:manual/16-boot.md:241 klas:E -->
### T-16-095 · proza · рядок 241

**Книга каже, дослівно:**

> Це найдешевша діагностична інформація в усій системі, і читати її треба першою.

**Доказ**

- **Клас:** F — не звірено

---
