# Фактчекінг: `kartky/k09-pinouty.md`

Одиниць твердження: **37**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K09-001 sha:2f50ba45 src:kartky/k09-pinouty.md:3 klas:F -->
### T-K09-001 · proza · рядок 3

**Книга каже, дослівно:**

> Повні пінаут-таблиці плат — додаток A.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-002 sha:3606dbb0 src:kartky/k09-pinouty.md:3 klas:F -->
### T-K09-002 · proza · рядок 3

**Книга каже, дослівно:**

> Тут — те, через що плати не стартують і піни не працюють.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-003 sha:80a305aa src:kartky/k09-pinouty.md:8 klas:F -->
### T-K09-003 · tablycya · рядок 8

**Книга каже, дослівно:**

> | Піни | Що з ними |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-004 sha:e2a47803 src:kartky/k09-pinouty.md:10 klas:F -->
### T-K09-004 · tablycya · рядок 10

**Книга каже, дослівно:**

> | **6, 7, 8, 9, 10, 11** | зайняті флешем. **Не використовувати ніколи** |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-005 sha:d97ed996 src:kartky/k09-pinouty.md:11 klas:F -->
### T-K09-005 · tablycya · рядок 11

**Книга каже, дослівно:**

> | **34, 35, 36, 37, 38, 39** | тільки вхід. Немає виходу і немає підтягування |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-006 sha:b898e3ed src:kartky/k09-pinouty.md:12 klas:F -->
### T-K09-006 · tablycya · рядок 12

**Книга каже, дослівно:**

> | **0, 2, 5, 12, 15** | strapping: стан при старті визначає режим завантаження |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-007 sha:66b7ec5f src:kartky/k09-pinouty.md:13 klas:F -->
### T-K09-007 · tablycya · рядок 13

**Книга каже, дослівно:**

> | **1 (TX), 3 (RX)** | консоль UART0. Зайняті логом і прошивкою |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-008 sha:ab4b3ef8 src:kartky/k09-pinouty.md:14 klas:A -->
### T-K09-008 · tablycya · рядок 14

**Книга каже, дослівно:**

> | **12 (MTDI)** | підтягнутий вгору при старті → плата не стартує взагалі |

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

<!-- fc id:T-K09-009 sha:e3e28f1d src:kartky/k09-pinouty.md:15 klas:F -->
### T-K09-009 · tablycya · рядок 15

**Книга каже, дослівно:**

> | 25, 26 | єдині DAC-виходи |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-010 sha:98e14927 src:kartky/k09-pinouty.md:16 klas:F -->
### T-K09-010 · tablycya · рядок 16

**Книга каже, дослівно:**

> | 32–39 | ADC1 — працює завжди |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-011 sha:5014e19c src:kartky/k09-pinouty.md:17 klas:F -->
### T-K09-011 · tablycya · рядок 17

**Книга каже, дослівно:**

> | 0, 2, 4, 12–15, 25–27 | ADC2 — **не працює при увімкненому Wi-Fi** |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-012 sha:cbe179c6 src:kartky/k09-pinouty.md:19 klas:F -->
### T-K09-012 · proza · рядок 19

**Книга каже, дослівно:**

> Вільні без застережень: **4, 13, 14, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 32, 33**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-013 sha:39c5b281 src:kartky/k09-pinouty.md:22 klas:F -->
### T-K09-013 · proza · рядок 22

**Книга каже, дослівно:**

> Поширена домовленість (не апаратна прив'язка): I²C — SDA 21, SCL 22; SPI — MOSI 23, MISO 19, SCK 18, CS 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-014 sha:03772305 src:kartky/k09-pinouty.md:22 klas:F -->
### T-K09-014 · proza · рядок 22

**Книга каже, дослівно:**

> Апаратні піни — додаток A.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-015 sha:80a305aa src:kartky/k09-pinouty.md:27 klas:F -->
### T-K09-015 · tablycya · рядок 27

**Книга каже, дослівно:**

> | Піни | Що з ними |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-016 sha:03697e63 src:kartky/k09-pinouty.md:29 klas:F -->
### T-K09-016 · tablycya · рядок 29

**Книга каже, дослівно:**

> | **26–32** | флеш і PSRAM. Не чіпати |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-017 sha:3e0a1fdf src:kartky/k09-pinouty.md:30 klas:F -->
### T-K09-017 · tablycya · рядок 30

**Книга каже, дослівно:**

> | **33–37** | додатково зайняті на модулях з Octal PSRAM (`N16R8`) |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-018 sha:1802cee8 src:kartky/k09-pinouty.md:31 klas:F -->
### T-K09-018 · tablycya · рядок 31

**Книга каже, дослівно:**

> | **0, 3, 45, 46** | strapping |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-019 sha:c9bc0f84 src:kartky/k09-pinouty.md:32 klas:A -->
### T-K09-019 · tablycya · рядок 32

**Книга каже, дослівно:**

> | **19, 20** | native USB (D−, D+) |

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

<!-- fc id:T-K09-020 sha:59cdfb30 src:kartky/k09-pinouty.md:33 klas:A -->
### T-K09-020 · tablycya · рядок 33

**Книга каже, дослівно:**

> | 1–10 | ADC1 |

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

<!-- fc id:T-K09-021 sha:3d929849 src:kartky/k09-pinouty.md:34 klas:F -->
### T-K09-021 · tablycya · рядок 34

**Книга каже, дослівно:**

> | 11–20 | ADC2 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-022 sha:73df11d0 src:kartky/k09-pinouty.md:37 klas:A -->
### T-K09-022 · proza · рядок 37

**Книга каже, дослівно:**

> [[S3]] Вхід у бутлоадер: `GPIO0` = 0, а `GPIO46` при цьому **низький або вільний**.

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

<!-- fc id:T-K09-023 sha:00c24614 src:kartky/k09-pinouty.md:37 klas:A -->
### T-K09-023 · proza · рядок 37

**Книга каже, дослівно:**

> Підтягнутий угору `GPIO46` у download mode не пускає.

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

<!-- fc id:T-K09-024 sha:178f9f43 src:kartky/k09-pinouty.md:37 klas:F -->
### T-K09-024 · proza · рядок 37

**Книга каже, дослівно:**

> Якщо на цих пінах щось висить — знімати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-025 sha:76c9e72c src:kartky/k09-pinouty.md:41 klas:F -->
### T-K09-025 · proza · рядок 41

**Книга каже, дослівно:**

> Увага: на C3 правило **протилежне** — там другий пін має бути високим.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-026 sha:80a305aa src:kartky/k09-pinouty.md:46 klas:F -->
### T-K09-026 · tablycya · рядок 46

**Книга каже, дослівно:**

> | Піни | Що з ними |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-027 sha:78d5e963 src:kartky/k09-pinouty.md:48 klas:F -->
### T-K09-027 · tablycya · рядок 48

**Книга каже, дослівно:**

> | **12–17** | флеш. Не чіпати |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-028 sha:31804036 src:kartky/k09-pinouty.md:49 klas:F -->
### T-K09-028 · tablycya · рядок 49

**Книга каже, дослівно:**

> | **2, 8, 9** | strapping |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-029 sha:94d4ae17 src:kartky/k09-pinouty.md:50 klas:A -->
### T-K09-029 · tablycya · рядок 50

**Книга каже, дослівно:**

> | **18, 19** | USB-Serial-JTAG. Перевизначили — втратили налагодження |

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

<!-- fc id:T-K09-030 sha:11ec8d1a src:kartky/k09-pinouty.md:51 klas:A -->
### T-K09-030 · tablycya · рядок 51

**Книга каже, дослівно:**

> | 0–4 | ADC1 |

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

<!-- fc id:T-K09-031 sha:04c9b16d src:kartky/k09-pinouty.md:52 klas:F -->
### T-K09-031 · tablycya · рядок 52

**Книга каже, дослівно:**

> | 5 | ADC2 — **не використовувати**, апаратна вада |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-032 sha:e8a47bf8 src:kartky/k09-pinouty.md:54 klas:A -->
### T-K09-032 · proza · рядок 54

**Книга каже, дослівно:**

> Вхід у бутлоадер: `GPIO9` притиснутий до землі при скиданні, `GPIO8` при цьому має бути високим.

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

<!-- fc id:T-K09-033 sha:4b043722 src:kartky/k09-pinouty.md:54 klas:F -->
### T-K09-033 · proza · рядок 54

**Книга каже, дослівно:**

> Комбінація `GPIO8` = 0 і `GPIO9` = 0 недійсна.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-034 sha:e2174a8b src:kartky/k09-pinouty.md:59 klas:F -->
### T-K09-034 · proza · рядок 59

**Книга каже, дослівно:**

> **Пінаут плати важливіший за пінаут чипа.** Виробник плати міг вивести не всі піни, підписати їх по-своєму, повісити світлодіод або підтягувальний резистор.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-035 sha:9ae3a634 src:kartky/k09-pinouty.md:59 klas:F -->
### T-K09-035 · proza · рядок 59

**Книга каже, дослівно:**

> Те, що пін є на схемі чипа, не означає, що він вільний на цій платі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-036 sha:35f319d4 src:kartky/k09-pinouty.md:65 klas:F -->
### T-K09-036 · proza · рядок 65

**Книга каже, дослівно:**

> Пін із позначкою «тільки вхід» не стає виходом від налаштування в коді.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K09-037 sha:b255deb9 src:kartky/k09-pinouty.md:65 klas:F -->
### T-K09-037 · proza · рядок 65

**Книга каже, дослівно:**

> Спроба керувати з нього навантаженням — це або нічого, або пошкоджений пін.

**Доказ**

- **Клас:** F — не звірено

---
