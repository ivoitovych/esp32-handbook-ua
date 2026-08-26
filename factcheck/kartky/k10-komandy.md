# Фактчекінг: `kartky/k10-komandy.md`

Одиниць твердження: **49**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K10-001 sha:56ac242d src:kartky/k10-komandy.md:3 klas:F -->
### T-K10-001 · proza · рядок 3

**Книга каже, дослівно:**

> Синтаксис esptool **v5** (дефіси, без `.py`).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-002 sha:90dbd689 src:kartky/k10-komandy.md:3 klas:F -->
### T-K10-002 · proza · рядок 3

**Книга каже, дослівно:**

> Для v4 — підкреслення і суфікс `.py`: `esptool.py write_flash`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-003 sha:6ac69acd src:kartky/k10-komandy.md:3 klas:F -->
### T-K10-003 · proza · рядок 3

**Книга каже, дослівно:**

> Перевірити своє: `esptool version`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-004 sha:95237904 src:kartky/k10-komandy.md:8 klas:F -->
### T-K10-004 · kod · рядок 8

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 chip-id            # що за чип і ревізія
> esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
> esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
> esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
> esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
> esptool merge-bin -o all.bin --flash-mode dio \
>   0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # 0x1000 → classic/S2; інші чипи — див. таблицю
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-005 sha:df0648fe src:kartky/k10-komandy.md:9 klas:F -->
### T-K10-005 · kod-ryadok · рядок 9

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 chip-id            # що за чип і ревізія

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-006 sha:8af1928d src:kartky/k10-komandy.md:10 klas:F -->
### T-K10-006 · kod-ryadok · рядок 10

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-007 sha:74ec190c src:kartky/k10-komandy.md:11 klas:F -->
### T-K10-007 · kod-ryadok · рядок 11

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-008 sha:a177909e src:kartky/k10-komandy.md:12 klas:F -->
### T-K10-008 · kod-ryadok · рядок 12

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-009 sha:94bd45fa src:kartky/k10-komandy.md:13 klas:F -->
### T-K10-009 · kod-ryadok · рядок 13

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-010 sha:d6945e3a src:kartky/k10-komandy.md:14 klas:F -->
### T-K10-010 · kod-ryadok · рядок 14

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-011 sha:931ffa15 src:kartky/k10-komandy.md:15 klas:F -->
### T-K10-011 · kod-ryadok · рядок 15

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-012 sha:aecfd191 src:kartky/k10-komandy.md:16 klas:F -->
### T-K10-012 · kod-ryadok · рядок 16

**Книга каже, дослівно:**

> esptool merge-bin -o all.bin --flash-mode dio \

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-013 sha:4dc75968 src:kartky/k10-komandy.md:22 klas:F -->
### T-K10-013 · kod · рядок 22

**Книга каже, дослівно:**

> ```
> idf.py create-project my-project    # новий проєкт (назва латиницею)
> idf.py set-target esp32s3           # ⚠ стирає sdkconfig
> idf.py menuconfig                   # налаштування
> idf.py build                        # зібрати
> idf.py -p /dev/ttyUSB0 flash        # залити
> idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
> idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
> idf.py fullclean                    # коли збирання поводиться незрозуміло
> idf.py size                         # скільки зайнято флешу і RAM
> idf.py coredump-info                # розбір coredump із флешу
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-014 sha:c4f6cb74 src:kartky/k10-komandy.md:23 klas:F -->
### T-K10-014 · kod-ryadok · рядок 23

**Книга каже, дослівно:**

> idf.py create-project my-project    # новий проєкт (назва латиницею)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-015 sha:bb9f7106 src:kartky/k10-komandy.md:24 klas:F -->
### T-K10-015 · kod-ryadok · рядок 24

**Книга каже, дослівно:**

> idf.py set-target esp32s3           # ⚠ стирає sdkconfig

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-016 sha:cc032d7c src:kartky/k10-komandy.md:25 klas:F -->
### T-K10-016 · kod-ryadok · рядок 25

**Книга каже, дослівно:**

> idf.py menuconfig                   # налаштування

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-017 sha:5e640044 src:kartky/k10-komandy.md:26 klas:F -->
### T-K10-017 · kod-ryadok · рядок 26

**Книга каже, дослівно:**

> idf.py build                        # зібрати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-018 sha:399d8dd5 src:kartky/k10-komandy.md:27 klas:F -->
### T-K10-018 · kod-ryadok · рядок 27

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash        # залити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-019 sha:e95261df src:kartky/k10-komandy.md:28 klas:F -->
### T-K10-019 · kod-ryadok · рядок 28

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-020 sha:7879c453 src:kartky/k10-komandy.md:29 klas:F -->
### T-K10-020 · kod-ryadok · рядок 29

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-021 sha:21c29912 src:kartky/k10-komandy.md:30 klas:F -->
### T-K10-021 · kod-ryadok · рядок 30

**Книга каже, дослівно:**

> idf.py fullclean                    # коли збирання поводиться незрозуміло

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-022 sha:0f34d83d src:kartky/k10-komandy.md:31 klas:F -->
### T-K10-022 · kod-ryadok · рядок 31

**Книга каже, дослівно:**

> idf.py size                         # скільки зайнято флешу і RAM

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-023 sha:48df8d47 src:kartky/k10-komandy.md:32 klas:F -->
### T-K10-023 · kod-ryadok · рядок 32

**Книга каже, дослівно:**

> idf.py coredump-info                # розбір coredump із флешу

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-024 sha:c64c8733 src:kartky/k10-komandy.md:37 klas:F -->
### T-K10-024 · proza · рядок 37

**Книга каже, дослівно:**

> `idf.py monitor`: вийти — `Ctrl+]`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-025 sha:51eec05c src:kartky/k10-komandy.md:37 klas:F -->
### T-K10-025 · proza · рядок 37

**Книга каже, дослівно:**

> Скинути плату — `Ctrl+T`, потім `Ctrl+R`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-026 sha:ab211d67 src:kartky/k10-komandy.md:39 klas:F -->
### T-K10-026 · kod · рядок 39

**Книга каже, дослівно:**

> ```
> minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
> screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
> picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-027 sha:746a4901 src:kartky/k10-komandy.md:40 klas:F -->
### T-K10-027 · kod-ryadok · рядок 40

**Книга каже, дослівно:**

> minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-028 sha:d4bff93f src:kartky/k10-komandy.md:41 klas:F -->
### T-K10-028 · kod-ryadok · рядок 41

**Книга каже, дослівно:**

> screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-029 sha:c8e23e02 src:kartky/k10-komandy.md:42 klas:F -->
### T-K10-029 · kod-ryadok · рядок 42

**Книга каже, дослівно:**

> picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-030 sha:c5afa127 src:kartky/k10-komandy.md:47 klas:F -->
### T-K10-030 · kod · рядок 47

**Книга каже, дослівно:**

> ```
> ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
> dmesg | tail                     # що ядро побачило при під'єднанні
> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
> lsof /dev/ttyUSB0                # хто тримає порт
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-031 sha:805c4c57 src:kartky/k10-komandy.md:48 klas:F -->
### T-K10-031 · kod-ryadok · рядок 48

**Книга каже, дослівно:**

> ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-032 sha:65b20b9d src:kartky/k10-komandy.md:49 klas:F -->
### T-K10-032 · kod-ryadok · рядок 49

**Книга каже, дослівно:**

> dmesg | tail                     # що ядро побачило при під'єднанні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-033 sha:459deb70 src:kartky/k10-komandy.md:50 klas:F -->
### T-K10-033 · kod-ryadok · рядок 50

**Книга каже, дослівно:**

> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-034 sha:04c7f41f src:kartky/k10-komandy.md:51 klas:F -->
### T-K10-034 · kod-ryadok · рядок 51

**Книга каже, дослівно:**

> lsof /dev/ttyUSB0                # хто тримає порт

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-035 sha:4ffb7aee src:kartky/k10-komandy.md:54 klas:F -->
### T-K10-035 · proza · рядок 54

**Книга каже, дослівно:**

> `/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-036 sha:2130100e src:kartky/k10-komandy.md:54 klas:F -->
### T-K10-036 · proza · рядок 54

**Книга каже, дослівно:**

> `/dev/ttyACM*` — native USB [[S3]] [[C3]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-037 sha:3c153db1 src:kartky/k10-komandy.md:59 klas:F -->
### T-K10-037 · tablycya-shapka · рядок 59

**Книга каже, дослівно:**

> | Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-038 sha:03becf94 src:kartky/k10-komandy.md:60 klas:F -->
### T-K10-038 · komirka · рядок 60

**Книга каже, дослівно:**

> bootloader · classic, S2 → `0x1000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-039 sha:1fe1e089 src:kartky/k10-komandy.md:60 klas:F -->
### T-K10-039 · komirka · рядок 60

**Книга каже, дослівно:**

> bootloader · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-040 sha:ddb10a79 src:kartky/k10-komandy.md:60 klas:F -->
### T-K10-040 · komirka · рядок 60

**Книга каже, дослівно:**

> bootloader · P4, C5, H4 → `0x2000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-041 sha:4e987ef9 src:kartky/k10-komandy.md:61 klas:F -->
### T-K10-041 · komirka · рядок 61

**Книга каже, дослівно:**

> partition table · classic, S2 → `0x8000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-042 sha:8c7b7a5f src:kartky/k10-komandy.md:61 klas:F -->
### T-K10-042 · komirka · рядок 61

**Книга каже, дослівно:**

> partition table · S3, C3, C6, H2 → `0x8000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-043 sha:cb052eb6 src:kartky/k10-komandy.md:61 klas:F -->
### T-K10-043 · komirka · рядок 61

**Книга каже, дослівно:**

> partition table · P4, C5, H4 → `0x8000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-044 sha:55b5b58b src:kartky/k10-komandy.md:62 klas:F -->
### T-K10-044 · komirka · рядок 62

**Книга каже, дослівно:**

> застосунок · classic, S2 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-045 sha:55a122c0 src:kartky/k10-komandy.md:62 klas:F -->
### T-K10-045 · komirka · рядок 62

**Книга каже, дослівно:**

> застосунок · S3, C3, C6, H2 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-046 sha:eb3f0062 src:kartky/k10-komandy.md:62 klas:F -->
### T-K10-046 · komirka · рядок 62

**Книга каже, дослівно:**

> застосунок · P4, C5, H4 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-047 sha:ceaada41 src:kartky/k10-komandy.md:63 klas:F -->
### T-K10-047 · komirka · рядок 63

**Книга каже, дослівно:**

> зібраний `merge-bin` · classic, S2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-048 sha:9feefdcc src:kartky/k10-komandy.md:63 klas:F -->
### T-K10-048 · komirka · рядок 63

**Книга каже, дослівно:**

> зібраний `merge-bin` · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-049 sha:c94bfb00 src:kartky/k10-komandy.md:63 klas:F -->
### T-K10-049 · komirka · рядок 63

**Книга каже, дослівно:**

> зібраний `merge-bin` · P4, C5, H4 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---
