# Фактчекінг: `dodatky/c-komandy.md`

Одиниць твердження: **116**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-C-001 sha:76d16ded src:dodatky/c-komandy.md:3 klas:F -->
### T-C-001 · proza · рядок 3

**Книга каже, дослівно:**

> Розгорнута версія картки [К10](#k-komandy).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-002 sha:5afd5f63 src:dodatky/c-komandy.md:5 klas:F -->
### T-C-002 · proza · рядок 5

**Книга каже, дослівно:**

> **Синтаксис esptool v5** (дефіси, без `.py`).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-003 sha:644789be src:dodatky/c-komandy.md:5 klas:F -->
### T-C-003 · proza · рядок 5

**Книга каже, дослівно:**

> Для v4 — підкреслення і суфікс `.py`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-004 sha:6ac69acd src:dodatky/c-komandy.md:5 klas:F -->
### T-C-004 · proza · рядок 5

**Книга каже, дослівно:**

> Перевірити своє: `esptool version`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-005 sha:b9d7b8df src:dodatky/c-komandy.md:12 klas:F -->
### T-C-005 · kod · рядок 12

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 chip-id          # сімейство, ревізія, MAC
> esptool --port /dev/ttyUSB0 flash-id         # виробник і обсяг флешу
> esptool --port /dev/ttyUSB0 read-mac
> esptool version
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-006 sha:b1a7ffe5 src:dodatky/c-komandy.md:13 klas:F -->
### T-C-006 · kod-ryadok · рядок 13

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 chip-id          # сімейство, ревізія, MAC

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-007 sha:39838a17 src:dodatky/c-komandy.md:14 klas:F -->
### T-C-007 · kod-ryadok · рядок 14

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 flash-id         # виробник і обсяг флешу

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-008 sha:049fb9cd src:dodatky/c-komandy.md:15 klas:F -->
### T-C-008 · kod-ryadok · рядок 15

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 read-mac

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-009 sha:fcbae1b9 src:dodatky/c-komandy.md:16 klas:F -->
### T-C-009 · kod-ryadok · рядок 16

**Книга каже, дослівно:**

> esptool version

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-010 sha:881f86c6 src:dodatky/c-komandy.md:21 klas:F -->
### T-C-010 · kod · рядок 21

**Книга каже, дослівно:**

> ```
> esptool --port PORT read-flash 0 ALL dump.bin           # повний дамп
> esptool --port PORT read-flash 0 0x400000 dump.bin      # 4 МБ явно
> esptool --port PORT read-flash 0x9000 0x6000 nvs.bin    # лише NVS
> esptool --port PORT read-flash 0x8000 0x1000 pt.bin     # таблиця розділів
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-011 sha:bb087e09 src:dodatky/c-komandy.md:22 klas:F -->
### T-C-011 · kod-ryadok · рядок 22

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0 ALL dump.bin           # повний дамп

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-012 sha:df2bf3b7 src:dodatky/c-komandy.md:23 klas:F -->
### T-C-012 · kod-ryadok · рядок 23

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0 0x400000 dump.bin      # 4 МБ явно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-013 sha:4353e19f src:dodatky/c-komandy.md:24 klas:F -->
### T-C-013 · kod-ryadok · рядок 24

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0x9000 0x6000 nvs.bin    # лише NVS

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-014 sha:88b7dfd4 src:dodatky/c-komandy.md:25 klas:F -->
### T-C-014 · kod-ryadok · рядок 25

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0x8000 0x1000 pt.bin     # таблиця розділів

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-015 sha:75b577e4 src:dodatky/c-komandy.md:28 klas:F -->
### T-C-015 · proza · рядок 28

**Книга каже, дослівно:**

> Розмір файлу має **точно** дорівнювати запитаному.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-016 sha:751b08c4 src:dodatky/c-komandy.md:28 klas:F -->
### T-C-016 · proza · рядок 28

**Книга каже, дослівно:**

> Менший — обірваний дамп; повторити на `--baud 115200`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-017 sha:fcd6b026 src:dodatky/c-komandy.md:33 klas:F -->
### T-C-017 · kod · рядок 33

**Книга каже, дослівно:**

> ```
> esptool --port PORT --baud 460800 write-flash -z \
>   0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 app.bin
> 
> esptool --port PORT write-flash 0x0 merged.bin          # зібраний образ
> esptool --port PORT verify-flash 0x10000 app.bin        # звірити
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-018 sha:3f0f4284 src:dodatky/c-komandy.md:34 klas:F -->
### T-C-018 · kod-ryadok · рядок 34

**Книга каже, дослівно:**

> esptool --port PORT --baud 460800 write-flash -z \

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-019 sha:c6c4971b src:dodatky/c-komandy.md:37 klas:F -->
### T-C-019 · kod-ryadok · рядок 37

**Книга каже, дослівно:**

> esptool --port PORT write-flash 0x0 merged.bin          # зібраний образ

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-020 sha:efde820e src:dodatky/c-komandy.md:38 klas:F -->
### T-C-020 · kod-ryadok · рядок 38

**Книга каже, дослівно:**

> esptool --port PORT verify-flash 0x10000 app.bin        # звірити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-021 sha:00142e5e src:dodatky/c-komandy.md:43 klas:F -->
### T-C-021 · kod · рядок 43

**Книга каже, дослівно:**

> ```
> esptool --port PORT erase-flash                  # ⛔ усе, спершу дамп
> esptool --port PORT erase-region 0x9000 0x6000   # лише NVS
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-022 sha:2dca50d4 src:dodatky/c-komandy.md:44 klas:F -->
### T-C-022 · kod-ryadok · рядок 44

**Книга каже, дослівно:**

> esptool --port PORT erase-flash                  # ⛔ усе, спершу дамп

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-023 sha:9802b297 src:dodatky/c-komandy.md:45 klas:F -->
### T-C-023 · kod-ryadok · рядок 45

**Книга каже, дослівно:**

> esptool --port PORT erase-region 0x9000 0x6000   # лише NVS

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-024 sha:9c10fa1f src:dodatky/c-komandy.md:50 klas:F -->
### T-C-024 · kod · рядок 50

**Книга каже, дослівно:**

> ```
> esptool merge-bin -o vyrib.bin --flash-mode dio --flash-size 4MB \
>   0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 app.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-025 sha:d2bd4362 src:dodatky/c-komandy.md:51 klas:F -->
### T-C-025 · kod-ryadok · рядок 51

**Книга каже, дослівно:**

> esptool merge-bin -o vyrib.bin --flash-mode dio --flash-size 4MB \

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-026 sha:36969ccb src:dodatky/c-komandy.md:57 klas:F -->
### T-C-026 · tablycya · рядок 57

**Книга каже, дослівно:**

> | Прапорець | Навіщо |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-027 sha:1d6f7adf src:dodatky/c-komandy.md:59 klas:F -->
### T-C-027 · tablycya · рядок 59

**Книга каже, дослівно:**

> | `--baud 115200` | коли обривається на високій швидкості |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-028 sha:09265f42 src:dodatky/c-komandy.md:60 klas:F -->
### T-C-028 · tablycya · рядок 60

**Книга каже, дослівно:**

> | `-z` | стиснення при передачі: швидше й надійніше |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-029 sha:602ee8fd src:dodatky/c-komandy.md:61 klas:F -->
### T-C-029 · tablycya · рядок 61

**Книга каже, дослівно:**

> | `--no-stub` | коли клон не приймає допоміжну програму |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-030 sha:ae5119de src:dodatky/c-komandy.md:62 klas:F -->
### T-C-030 · tablycya · рядок 62

**Книга каже, дослівно:**

> | `--before default-reset --after hard-reset` | керування скиданням |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-031 sha:8e5b5b76 src:dodatky/c-komandy.md:63 klas:F -->
### T-C-031 · tablycya · рядок 63

**Книга каже, дослівно:**

> | `--chip esp32s3` | коли автовизначення заважає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-032 sha:dbb08ae1 src:dodatky/c-komandy.md:68 klas:F -->
### T-C-032 · proza · рядок 68

**Книга каже, дослівно:**

> `burn-*` пропалює біти **фізично й назавжди** (розділ 20).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-033 sha:d25d8e19 src:dodatky/c-komandy.md:72 klas:F -->
### T-C-033 · kod · рядок 72

**Книга каже, дослівно:**

> ```
> espefuse --port PORT summary        # безпечно: подивитися стан
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-034 sha:cdc968e6 src:dodatky/c-komandy.md:73 klas:F -->
### T-C-034 · kod-ryadok · рядок 73

**Книга каже, дослівно:**

> espefuse --port PORT summary        # безпечно: подивитися стан

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-035 sha:d06f73ae src:dodatky/c-komandy.md:80 klas:F -->
### T-C-035 · kod · рядок 80

**Книга каже, дослівно:**

> ```
> idf.py create-project imya
> idf.py create-component imya
> idf.py set-target esp32s3       # ⚠ стирає sdkconfig
> idf.py menuconfig               # пошук усередині — клавіша /
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-036 sha:3e0a67c9 src:dodatky/c-komandy.md:81 klas:F -->
### T-C-036 · kod-ryadok · рядок 81

**Книга каже, дослівно:**

> idf.py create-project imya

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-037 sha:c06327b4 src:dodatky/c-komandy.md:82 klas:F -->
### T-C-037 · kod-ryadok · рядок 82

**Книга каже, дослівно:**

> idf.py create-component imya

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-038 sha:bb9f7106 src:dodatky/c-komandy.md:83 klas:F -->
### T-C-038 · kod-ryadok · рядок 83

**Книга каже, дослівно:**

> idf.py set-target esp32s3       # ⚠ стирає sdkconfig

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-039 sha:93619e04 src:dodatky/c-komandy.md:84 klas:F -->
### T-C-039 · kod-ryadok · рядок 84

**Книга каже, дослівно:**

> idf.py menuconfig               # пошук усередині — клавіша /

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-040 sha:0d79ed38 src:dodatky/c-komandy.md:89 klas:F -->
### T-C-040 · kod · рядок 89

**Книга каже, дослівно:**

> ```
> idf.py build
> idf.py -p /dev/ttyUSB0 flash
> idf.py -p /dev/ttyUSB0 monitor          # вихід Ctrl+]
> idf.py -p /dev/ttyUSB0 flash monitor    # найчастіша команда
> idf.py -p /dev/ttyUSB0 app-flash        # лише застосунок, швидше
> idf.py fullclean                        # коли збирання поводиться дивно
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-041 sha:343d9bab src:dodatky/c-komandy.md:90 klas:F -->
### T-C-041 · kod-ryadok · рядок 90

**Книга каже, дослівно:**

> idf.py build

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-042 sha:aaa1cf80 src:dodatky/c-komandy.md:91 klas:F -->
### T-C-042 · kod-ryadok · рядок 91

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-043 sha:770cf8b9 src:dodatky/c-komandy.md:92 klas:F -->
### T-C-043 · kod-ryadok · рядок 92

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 monitor          # вихід Ctrl+]

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-044 sha:7879c453 src:dodatky/c-komandy.md:93 klas:F -->
### T-C-044 · kod-ryadok · рядок 93

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash monitor    # найчастіша команда

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-045 sha:5410fc3a src:dodatky/c-komandy.md:94 klas:F -->
### T-C-045 · kod-ryadok · рядок 94

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 app-flash        # лише застосунок, швидше

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-046 sha:345eb1d8 src:dodatky/c-komandy.md:95 klas:F -->
### T-C-046 · kod-ryadok · рядок 95

**Книга каже, дослівно:**

> idf.py fullclean                        # коли збирання поводиться дивно

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-047 sha:e06292bb src:dodatky/c-komandy.md:100 klas:F -->
### T-C-047 · kod · рядок 100

**Книга каже, дослівно:**

> ```
> idf.py size                 # скільки зайнято флешу і RAM
> idf.py size-components      # ХТО САМЕ займає — найкорисніша
> idf.py size-files
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-048 sha:0f34d83d src:dodatky/c-komandy.md:101 klas:F -->
### T-C-048 · kod-ryadok · рядок 101

**Книга каже, дослівно:**

> idf.py size                 # скільки зайнято флешу і RAM

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-049 sha:ab73f933 src:dodatky/c-komandy.md:102 klas:F -->
### T-C-049 · kod-ryadok · рядок 102

**Книга каже, дослівно:**

> idf.py size-components      # ХТО САМЕ займає — найкорисніша

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-050 sha:9136076f src:dodatky/c-komandy.md:103 klas:F -->
### T-C-050 · kod-ryadok · рядок 103

**Книга каже, дослівно:**

> idf.py size-files

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-051 sha:d3c38986 src:dodatky/c-komandy.md:108 klas:F -->
### T-C-051 · kod · рядок 108

**Книга каже, дослівно:**

> ```
> idf.py coredump-info        # розбір coredump із флешу
> idf.py coredump-debug       # GDB на збереженому стані
> idf.py openocd gdb          # покрокове налагодження (S3, C3)
> idf.py monitor              # з розшифровкою backtrace на льоту
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-052 sha:48df8d47 src:dodatky/c-komandy.md:109 klas:F -->
### T-C-052 · kod-ryadok · рядок 109

**Книга каже, дослівно:**

> idf.py coredump-info        # розбір coredump із флешу

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-053 sha:f88382bd src:dodatky/c-komandy.md:110 klas:F -->
### T-C-053 · kod-ryadok · рядок 110

**Книга каже, дослівно:**

> idf.py coredump-debug       # GDB на збереженому стані

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-054 sha:b89c04ed src:dodatky/c-komandy.md:111 klas:F -->
### T-C-054 · kod-ryadok · рядок 111

**Книга каже, дослівно:**

> idf.py openocd gdb          # покрокове налагодження (S3, C3)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-055 sha:249fc25a src:dodatky/c-komandy.md:112 klas:F -->
### T-C-055 · kod-ryadok · рядок 112

**Книга каже, дослівно:**

> idf.py monitor              # з розшифровкою backtrace на льоту

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-056 sha:f027758e src:dodatky/c-komandy.md:117 klas:F -->
### T-C-056 · kod · рядок 117

**Книга каже, дослівно:**

> ```
> idf.py add-dependency "espressif/led_strip^3.0.3"
> idf.py reconfigure
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-057 sha:4f76e0f2 src:dodatky/c-komandy.md:118 klas:F -->
### T-C-057 · kod-ryadok · рядок 118

**Книга каже, дослівно:**

> idf.py add-dependency "espressif/led_strip^3.0.3"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-058 sha:bd18c568 src:dodatky/c-komandy.md:119 klas:F -->
### T-C-058 · kod-ryadok · рядок 119

**Книга каже, дослівно:**

> idf.py reconfigure

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-059 sha:14ee9040 src:dodatky/c-komandy.md:124 klas:F -->
### T-C-059 · kod · рядок 124

**Книга каже, дослівно:**

> ```
> xtensa-esp32-elf-addr2line   -pfiaC -e build/app.elf 0x400d1234 0x400d5678
> xtensa-esp32s3-elf-addr2line -pfiaC -e build/app.elf 0x42001234
> riscv32-esp-elf-addr2line    -pfiaC -e build/app.elf 0x42001234
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-060 sha:5f267d8c src:dodatky/c-komandy.md:125 klas:F -->
### T-C-060 · kod-ryadok · рядок 125

**Книга каже, дослівно:**

> xtensa-esp32-elf-addr2line   -pfiaC -e build/app.elf 0x400d1234 0x400d5678

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-061 sha:f57b50fb src:dodatky/c-komandy.md:126 klas:F -->
### T-C-061 · kod-ryadok · рядок 126

**Книга каже, дослівно:**

> xtensa-esp32s3-elf-addr2line -pfiaC -e build/app.elf 0x42001234

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-062 sha:69e46646 src:dodatky/c-komandy.md:127 klas:F -->
### T-C-062 · kod-ryadok · рядок 127

**Книга каже, дослівно:**

> riscv32-esp-elf-addr2line    -pfiaC -e build/app.elf 0x42001234

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-063 sha:2a969ef0 src:dodatky/c-komandy.md:130 klas:F -->
### T-C-063 · proza · рядок 130

**Книга каже, дослівно:**

> `-i` обов'язковий: без нього inline-кадри зникають.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-064 sha:828c36b3 src:dodatky/c-komandy.md:134 klas:F -->
### T-C-064 · tablycya-shapka · рядок 134

**Книга каже, дослівно:**

> | Програма | Вихід | Особливість |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-065 sha:af9c4cd0 src:dodatky/c-komandy.md:135 klas:F -->
### T-C-065 · komirka · рядок 135

**Книга каже, дослівно:**

> `idf.py monitor` · Вихід → `Ctrl+]`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-066 sha:1b645088 src:dodatky/c-komandy.md:135 klas:F -->
### T-C-066 · komirka · рядок 135

**Книга каже, дослівно:**

> `idf.py monitor` · Особливість → розшифровує backtrace; скидання `Ctrl+T`, `Ctrl+R`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-067 sha:e7670044 src:dodatky/c-komandy.md:136 klas:F -->
### T-C-067 · komirka · рядок 136

**Книга каже, дослівно:**

> `picocom -b 115200 /dev/ttyUSB0` · Вихід → `Ctrl+A`, `Ctrl+X`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-068 sha:3e00cb93 src:dodatky/c-komandy.md:136 klas:F -->
### T-C-068 · komirka · рядок 136

**Книга каже, дослівно:**

> `picocom -b 115200 /dev/ttyUSB0` · Особливість → найпростіший

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-069 sha:b668a28a src:dodatky/c-komandy.md:137 klas:F -->
### T-C-069 · komirka · рядок 137

**Книга каже, дослівно:**

> `minicom -D /dev/ttyUSB0 -b 115200` · Вихід → `Ctrl+A`, `X`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-070 sha:00c75e9e src:dodatky/c-komandy.md:138 klas:F -->
### T-C-070 · komirka · рядок 138

**Книга каже, дослівно:**

> `screen /dev/ttyUSB0 115200` · Вихід → `Ctrl+A`, `K`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-071 sha:a33fb442 src:dodatky/c-komandy.md:138 klas:F -->
### T-C-071 · komirka · рядок 138

**Книга каже, дослівно:**

> `screen /dev/ttyUSB0 115200` · Особливість → є майже скрізь

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-072 sha:03ecbe4f src:dodatky/c-komandy.md:143 klas:F -->
### T-C-072 · kod · рядок 143

**Книга каже, дослівно:**

> ```
> picocom -b 115200 /dev/ttyUSB0 | tee log-2026-08-26.txt
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-073 sha:999b86b5 src:dodatky/c-komandy.md:144 klas:F -->
### T-C-073 · kod-ryadok · рядок 144

**Книга каже, дослівно:**

> picocom -b 115200 /dev/ttyUSB0 | tee log-2026-08-26.txt

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-074 sha:5bc221cd src:dodatky/c-komandy.md:149 klas:F -->
### T-C-074 · kod · рядок 149

**Книга каже, дослівно:**

> ```
> ls /dev/ttyUSB* /dev/ttyACM*     # що є
> ls -l /dev/serial/by-id/         # стабільні імена для скриптів
> dmesg | tail -20                 # що ядро побачило
> lsof /dev/ttyUSB0                # хто тримає порт
> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-075 sha:7140ef8e src:dodatky/c-komandy.md:150 klas:F -->
### T-C-075 · kod-ryadok · рядок 150

**Книга каже, дослівно:**

> ls /dev/ttyUSB* /dev/ttyACM*     # що є

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-076 sha:583a0a4a src:dodatky/c-komandy.md:151 klas:F -->
### T-C-076 · kod-ryadok · рядок 151

**Книга каже, дослівно:**

> ls -l /dev/serial/by-id/         # стабільні імена для скриптів

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-077 sha:88976550 src:dodatky/c-komandy.md:152 klas:F -->
### T-C-077 · kod-ryadok · рядок 152

**Книга каже, дослівно:**

> dmesg | tail -20                 # що ядро побачило

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-078 sha:04c7f41f src:dodatky/c-komandy.md:153 klas:F -->
### T-C-078 · kod-ryadok · рядок 153

**Книга каже, дослівно:**

> lsof /dev/ttyUSB0                # хто тримає порт

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-079 sha:459deb70 src:dodatky/c-komandy.md:154 klas:F -->
### T-C-079 · kod-ryadok · рядок 154

**Книга каже, дослівно:**

> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-080 sha:b97a16ef src:dodatky/c-komandy.md:157 klas:F -->
### T-C-080 · proza · рядок 157

**Книга каже, дослівно:**

> `/dev/ttyUSB*` — зовнішній міст.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-081 sha:2130100e src:dodatky/c-komandy.md:157 klas:F -->
### T-C-081 · proza · рядок 157

**Книга каже, дослівно:**

> `/dev/ttyACM*` — native USB [[S3]] [[C3]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-082 sha:f68e2f06 src:dodatky/c-komandy.md:161 klas:F -->
### T-C-082 · kod · рядок 161

**Книга каже, дослівно:**

> ```
> pio run                    # зібрати
> pio run -e s3              # конкретне середовище
> pio run -t upload
> pio device monitor
> pio run -t clean
> pio pkg update
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-083 sha:0b0001c2 src:dodatky/c-komandy.md:162 klas:F -->
### T-C-083 · kod-ryadok · рядок 162

**Книга каже, дослівно:**

> pio run                    # зібрати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-084 sha:307983fc src:dodatky/c-komandy.md:163 klas:F -->
### T-C-084 · kod-ryadok · рядок 163

**Книга каже, дослівно:**

> pio run -e s3              # конкретне середовище

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-085 sha:82ea1803 src:dodatky/c-komandy.md:164 klas:F -->
### T-C-085 · kod-ryadok · рядок 164

**Книга каже, дослівно:**

> pio run -t upload

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-086 sha:364802c1 src:dodatky/c-komandy.md:165 klas:F -->
### T-C-086 · kod-ryadok · рядок 165

**Книга каже, дослівно:**

> pio device monitor

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-087 sha:1a074688 src:dodatky/c-komandy.md:166 klas:F -->
### T-C-087 · kod-ryadok · рядок 166

**Книга каже, дослівно:**

> pio run -t clean

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-088 sha:a092446e src:dodatky/c-komandy.md:167 klas:F -->
### T-C-088 · kod-ryadok · рядок 167

**Книга каже, дослівно:**

> pio pkg update

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-089 sha:3c153db1 src:dodatky/c-komandy.md:172 klas:F -->
### T-C-089 · tablycya-shapka · рядок 172

**Книга каже, дослівно:**

> | Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-090 sha:03becf94 src:dodatky/c-komandy.md:173 klas:F -->
### T-C-090 · komirka · рядок 173

**Книга каже, дослівно:**

> bootloader · classic, S2 → `0x1000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-091 sha:1fe1e089 src:dodatky/c-komandy.md:173 klas:F -->
### T-C-091 · komirka · рядок 173

**Книга каже, дослівно:**

> bootloader · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-092 sha:ddb10a79 src:dodatky/c-komandy.md:173 klas:F -->
### T-C-092 · komirka · рядок 173

**Книга каже, дослівно:**

> bootloader · P4, C5, H4 → `0x2000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-093 sha:a6442276 src:dodatky/c-komandy.md:174 klas:A -->
### T-C-093 · komirka · рядок 174

**Книга каже, дослівно:**

> таблиця розділів · classic, S2 → `0x8000`

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

<!-- fc id:T-C-094 sha:21c0d046 src:dodatky/c-komandy.md:174 klas:A -->
### T-C-094 · komirka · рядок 174

**Книга каже, дослівно:**

> таблиця розділів · S3, C3, C6, H2 → `0x8000`

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

<!-- fc id:T-C-095 sha:59461729 src:dodatky/c-komandy.md:174 klas:A -->
### T-C-095 · komirka · рядок 174

**Книга каже, дослівно:**

> таблиця розділів · P4, C5, H4 → `0x8000`

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

<!-- fc id:T-C-096 sha:55b5b58b src:dodatky/c-komandy.md:175 klas:F -->
### T-C-096 · komirka · рядок 175

**Книга каже, дослівно:**

> застосунок · classic, S2 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-097 sha:55a122c0 src:dodatky/c-komandy.md:175 klas:F -->
### T-C-097 · komirka · рядок 175

**Книга каже, дослівно:**

> застосунок · S3, C3, C6, H2 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-098 sha:eb3f0062 src:dodatky/c-komandy.md:175 klas:F -->
### T-C-098 · komirka · рядок 175

**Книга каже, дослівно:**

> застосунок · P4, C5, H4 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-099 sha:96022a5e src:dodatky/c-komandy.md:176 klas:F -->
### T-C-099 · komirka · рядок 176

**Книга каже, дослівно:**

> `nvs` (типово) · classic, S2 → `0x9000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-100 sha:906f56bc src:dodatky/c-komandy.md:176 klas:F -->
### T-C-100 · komirka · рядок 176

**Книга каже, дослівно:**

> `nvs` (типово) · S3, C3, C6, H2 → `0x9000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-101 sha:5efc2dcb src:dodatky/c-komandy.md:176 klas:F -->
### T-C-101 · komirka · рядок 176

**Книга каже, дослівно:**

> `nvs` (типово) · P4, C5, H4 → `0x9000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-102 sha:ceaada41 src:dodatky/c-komandy.md:177 klas:F -->
### T-C-102 · komirka · рядок 177

**Книга каже, дослівно:**

> зібраний `merge-bin` · classic, S2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-103 sha:9feefdcc src:dodatky/c-komandy.md:177 klas:F -->
### T-C-103 · komirka · рядок 177

**Книга каже, дослівно:**

> зібраний `merge-bin` · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-104 sha:c94bfb00 src:dodatky/c-komandy.md:177 klas:F -->
### T-C-104 · komirka · рядок 177

**Книга каже, дослівно:**

> зібраний `merge-bin` · P4, C5, H4 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-105 sha:9ab6d1e4 src:dodatky/c-komandy.md:180 klas:A -->
### T-C-105 · proza · рядок 180

**Книга каже, дослівно:**

> Адресу бутлоадера задає ROM чипа (`CONFIG_BOOTLOADER_OFFSET_IN_FLASH`), і в ESP-IDF вона не налаштовується.

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

<!-- fc id:T-C-106 sha:aa2e7ddd src:dodatky/c-komandy.md:180 klas:A -->
### T-C-106 · proza · рядок 180

**Книга каже, дослівно:**

> Правила «що новіше, то ближче до нуля» немає: у P4, C5 і H4 перші два сектори віддані під ключі шифрування флешу, і бутлоадер зсунуто на `0x2000`.

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

<!-- fc id:T-C-107 sha:20c177db src:dodatky/c-komandy.md:187 klas:F -->
### T-C-107 · kod · рядок 187

**Книга каже, дослівно:**

> ```
> dd if=dump.bin of=pt.bin bs=1 skip=$((0x8000)) count=$((0x1000))
> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-108 sha:d1458242 src:dodatky/c-komandy.md:188 klas:F -->
### T-C-108 · kod-ryadok · рядок 188

**Книга каже, дослівно:**

> dd if=dump.bin of=pt.bin bs=1 skip=$((0x8000)) count=$((0x1000))

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-109 sha:4438754b src:dodatky/c-komandy.md:189 klas:F -->
### T-C-109 · kod-ryadok · рядок 189

**Книга каже, дослівно:**

> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-110 sha:9fd4791b src:dodatky/c-komandy.md:194 klas:F -->
### T-C-110 · kod · рядок 194

**Книга каже, дослівно:**

> ```
> strings -n 6 dump.bin | less
> strings -n 6 dump.bin | grep -iE "v[0-9]+\.[0-9]+|20[0-9]{2}-"
> strings -n 6 dump.bin | grep -iE "http|mqtt|ssid|pass"
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-111 sha:3e391da0 src:dodatky/c-komandy.md:195 klas:F -->
### T-C-111 · kod-ryadok · рядок 195

**Книга каже, дослівно:**

> strings -n 6 dump.bin | less

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-112 sha:580bb88f src:dodatky/c-komandy.md:196 klas:F -->
### T-C-112 · kod-ryadok · рядок 196

**Книга каже, дослівно:**

> strings -n 6 dump.bin | grep -iE "v[0-9]+\.[0-9]+|20[0-9]{2}-"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-113 sha:f102892d src:dodatky/c-komandy.md:197 klas:F -->
### T-C-113 · kod-ryadok · рядок 197

**Книга каже, дослівно:**

> strings -n 6 dump.bin | grep -iE "http|mqtt|ssid|pass"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-114 sha:51bbff59 src:dodatky/c-komandy.md:204 klas:F -->
### T-C-114 · kod · рядок 204

**Книга каже, дослівно:**

> ```
> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
> esptool --port PORT write-flash 0x9000 nvs-0042.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-115 sha:aa33e38e src:dodatky/c-komandy.md:205 klas:F -->
### T-C-115 · kod-ryadok · рядок 205

**Книга каже, дослівно:**

> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-116 sha:8fc5b038 src:dodatky/c-komandy.md:206 klas:F -->
### T-C-116 · kod-ryadok · рядок 206

**Книга каже, дослівно:**

> esptool --port PORT write-flash 0x9000 nvs-0042.bin

**Доказ**

- **Клас:** F — не звірено

---
