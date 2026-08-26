# Фактчекінг: `dodatky/c-komandy.md`

Одиниць твердження: **47**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

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

<!-- fc id:T-C-006 sha:881f86c6 src:dodatky/c-komandy.md:21 klas:F -->
### T-C-006 · kod · рядок 21

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

<!-- fc id:T-C-007 sha:75b577e4 src:dodatky/c-komandy.md:28 klas:F -->
### T-C-007 · proza · рядок 28

**Книга каже, дослівно:**

> Розмір файлу має **точно** дорівнювати запитаному.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-008 sha:751b08c4 src:dodatky/c-komandy.md:28 klas:F -->
### T-C-008 · proza · рядок 28

**Книга каже, дослівно:**

> Менший — обірваний дамп; повторити на `--baud 115200`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-009 sha:fcd6b026 src:dodatky/c-komandy.md:33 klas:F -->
### T-C-009 · kod · рядок 33

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

<!-- fc id:T-C-010 sha:00142e5e src:dodatky/c-komandy.md:43 klas:F -->
### T-C-010 · kod · рядок 43

**Книга каже, дослівно:**

> ```
> esptool --port PORT erase-flash                  # ⛔ усе, спершу дамп
> esptool --port PORT erase-region 0x9000 0x6000   # лише NVS
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-011 sha:9c10fa1f src:dodatky/c-komandy.md:50 klas:F -->
### T-C-011 · kod · рядок 50

**Книга каже, дослівно:**

> ```
> esptool merge-bin -o vyrib.bin --flash-mode dio --flash-size 4MB \
>   0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 app.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-012 sha:36969ccb src:dodatky/c-komandy.md:57 klas:F -->
### T-C-012 · tablycya · рядок 57

**Книга каже, дослівно:**

> | Прапорець | Навіщо |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-013 sha:1d6f7adf src:dodatky/c-komandy.md:59 klas:F -->
### T-C-013 · tablycya · рядок 59

**Книга каже, дослівно:**

> | `--baud 115200` | коли обривається на високій швидкості |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-014 sha:09265f42 src:dodatky/c-komandy.md:60 klas:F -->
### T-C-014 · tablycya · рядок 60

**Книга каже, дослівно:**

> | `-z` | стиснення при передачі: швидше й надійніше |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-015 sha:602ee8fd src:dodatky/c-komandy.md:61 klas:F -->
### T-C-015 · tablycya · рядок 61

**Книга каже, дослівно:**

> | `--no-stub` | коли клон не приймає допоміжну програму |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-016 sha:ae5119de src:dodatky/c-komandy.md:62 klas:F -->
### T-C-016 · tablycya · рядок 62

**Книга каже, дослівно:**

> | `--before default-reset --after hard-reset` | керування скиданням |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-017 sha:8e5b5b76 src:dodatky/c-komandy.md:63 klas:F -->
### T-C-017 · tablycya · рядок 63

**Книга каже, дослівно:**

> | `--chip esp32s3` | коли автовизначення заважає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-018 sha:dbb08ae1 src:dodatky/c-komandy.md:68 klas:F -->
### T-C-018 · proza · рядок 68

**Книга каже, дослівно:**

> `burn-*` пропалює біти **фізично й назавжди** (розділ 20).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-019 sha:d25d8e19 src:dodatky/c-komandy.md:72 klas:F -->
### T-C-019 · kod · рядок 72

**Книга каже, дослівно:**

> ```
> espefuse --port PORT summary        # безпечно: подивитися стан
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-020 sha:d06f73ae src:dodatky/c-komandy.md:80 klas:F -->
### T-C-020 · kod · рядок 80

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

<!-- fc id:T-C-021 sha:0d79ed38 src:dodatky/c-komandy.md:89 klas:F -->
### T-C-021 · kod · рядок 89

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

<!-- fc id:T-C-022 sha:e06292bb src:dodatky/c-komandy.md:100 klas:F -->
### T-C-022 · kod · рядок 100

**Книга каже, дослівно:**

> ```
> idf.py size                 # скільки зайнято флешу і RAM
> idf.py size-components      # ХТО САМЕ займає — найкорисніша
> idf.py size-files
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-023 sha:d3c38986 src:dodatky/c-komandy.md:108 klas:F -->
### T-C-023 · kod · рядок 108

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

<!-- fc id:T-C-024 sha:f027758e src:dodatky/c-komandy.md:117 klas:F -->
### T-C-024 · kod · рядок 117

**Книга каже, дослівно:**

> ```
> idf.py add-dependency "espressif/led_strip^3.0.3"
> idf.py reconfigure
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-025 sha:14ee9040 src:dodatky/c-komandy.md:124 klas:F -->
### T-C-025 · kod · рядок 124

**Книга каже, дослівно:**

> ```
> xtensa-esp32-elf-addr2line   -pfiaC -e build/app.elf 0x400d1234 0x400d5678
> xtensa-esp32s3-elf-addr2line -pfiaC -e build/app.elf 0x42001234
> riscv32-esp-elf-addr2line    -pfiaC -e build/app.elf 0x42001234
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-026 sha:2a969ef0 src:dodatky/c-komandy.md:130 klas:F -->
### T-C-026 · proza · рядок 130

**Книга каже, дослівно:**

> `-i` обов'язковий: без нього inline-кадри зникають.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-027 sha:828c36b3 src:dodatky/c-komandy.md:134 klas:F -->
### T-C-027 · tablycya · рядок 134

**Книга каже, дослівно:**

> | Програма | Вихід | Особливість |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-028 sha:3d1877ae src:dodatky/c-komandy.md:136 klas:F -->
### T-C-028 · tablycya · рядок 136

**Книга каже, дослівно:**

> | `idf.py monitor` | `Ctrl+]` | розшифровує backtrace; скидання `Ctrl+T`, `Ctrl+R` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-029 sha:a46ffd3c src:dodatky/c-komandy.md:137 klas:F -->
### T-C-029 · tablycya · рядок 137

**Книга каже, дослівно:**

> | `picocom -b 115200 /dev/ttyUSB0` | `Ctrl+A`, `Ctrl+X` | найпростіший |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-030 sha:61109db9 src:dodatky/c-komandy.md:138 klas:F -->
### T-C-030 · tablycya · рядок 138

**Книга каже, дослівно:**

> | `minicom -D /dev/ttyUSB0 -b 115200` | `Ctrl+A`, `X` | |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-031 sha:ce8f8e4b src:dodatky/c-komandy.md:139 klas:F -->
### T-C-031 · tablycya · рядок 139

**Книга каже, дослівно:**

> | `screen /dev/ttyUSB0 115200` | `Ctrl+A`, `K` | є майже скрізь |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-032 sha:03ecbe4f src:dodatky/c-komandy.md:143 klas:F -->
### T-C-032 · kod · рядок 143

**Книга каже, дослівно:**

> ```
> picocom -b 115200 /dev/ttyUSB0 | tee log-2026-08-26.txt
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-033 sha:5bc221cd src:dodatky/c-komandy.md:149 klas:F -->
### T-C-033 · kod · рядок 149

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

<!-- fc id:T-C-034 sha:b97a16ef src:dodatky/c-komandy.md:157 klas:F -->
### T-C-034 · proza · рядок 157

**Книга каже, дослівно:**

> `/dev/ttyUSB*` — зовнішній міст.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-035 sha:2130100e src:dodatky/c-komandy.md:157 klas:F -->
### T-C-035 · proza · рядок 157

**Книга каже, дослівно:**

> `/dev/ttyACM*` — native USB [[S3]] [[C3]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-036 sha:f68e2f06 src:dodatky/c-komandy.md:161 klas:F -->
### T-C-036 · kod · рядок 161

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

<!-- fc id:T-C-037 sha:3c153db1 src:dodatky/c-komandy.md:172 klas:F -->
### T-C-037 · tablycya · рядок 172

**Книга каже, дослівно:**

> | Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-038 sha:b6d12a55 src:dodatky/c-komandy.md:174 klas:F -->
### T-C-038 · tablycya · рядок 174

**Книга каже, дослівно:**

> | bootloader | `0x1000` | `0x0` | `0x2000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-039 sha:c332a993 src:dodatky/c-komandy.md:175 klas:A -->
### T-C-039 · tablycya · рядок 175

**Книга каже, дослівно:**

> | таблиця розділів | `0x8000` | `0x8000` | `0x8000` |

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

<!-- fc id:T-C-040 sha:259b5c05 src:dodatky/c-komandy.md:176 klas:F -->
### T-C-040 · tablycya · рядок 176

**Книга каже, дослівно:**

> | застосунок | `0x10000` | `0x10000` | `0x10000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-041 sha:41ecf4fa src:dodatky/c-komandy.md:177 klas:F -->
### T-C-041 · tablycya · рядок 177

**Книга каже, дослівно:**

> | `nvs` (типово) | `0x9000` | `0x9000` | `0x9000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-042 sha:e3d7c0ea src:dodatky/c-komandy.md:178 klas:F -->
### T-C-042 · tablycya · рядок 178

**Книга каже, дослівно:**

> | зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-043 sha:9ab6d1e4 src:dodatky/c-komandy.md:180 klas:A -->
### T-C-043 · proza · рядок 180

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

<!-- fc id:T-C-044 sha:aa2e7ddd src:dodatky/c-komandy.md:180 klas:A -->
### T-C-044 · proza · рядок 180

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

<!-- fc id:T-C-045 sha:20c177db src:dodatky/c-komandy.md:187 klas:F -->
### T-C-045 · kod · рядок 187

**Книга каже, дослівно:**

> ```
> dd if=dump.bin of=pt.bin bs=1 skip=$((0x8000)) count=$((0x1000))
> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-046 sha:9fd4791b src:dodatky/c-komandy.md:194 klas:F -->
### T-C-046 · kod · рядок 194

**Книга каже, дослівно:**

> ```
> strings -n 6 dump.bin | less
> strings -n 6 dump.bin | grep -iE "v[0-9]+\.[0-9]+|20[0-9]{2}-"
> strings -n 6 dump.bin | grep -iE "http|mqtt|ssid|pass"
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-047 sha:51bbff59 src:dodatky/c-komandy.md:204 klas:F -->
### T-C-047 · kod · рядок 204

**Книга каже, дослівно:**

> ```
> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
> esptool --port PORT write-flash 0x9000 nvs-0042.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---
