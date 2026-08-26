# Фактчекінг: `kartky/k10-komandy.md`

Одиниць твердження: **16**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

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

<!-- fc id:T-K10-005 sha:4dc75968 src:kartky/k10-komandy.md:22 klas:F -->
### T-K10-005 · kod · рядок 22

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

<!-- fc id:T-K10-006 sha:c64c8733 src:kartky/k10-komandy.md:37 klas:F -->
### T-K10-006 · proza · рядок 37

**Книга каже, дослівно:**

> `idf.py monitor`: вийти — `Ctrl+]`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-007 sha:51eec05c src:kartky/k10-komandy.md:37 klas:F -->
### T-K10-007 · proza · рядок 37

**Книга каже, дослівно:**

> Скинути плату — `Ctrl+T`, потім `Ctrl+R`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-008 sha:ab211d67 src:kartky/k10-komandy.md:39 klas:F -->
### T-K10-008 · kod · рядок 39

**Книга каже, дослівно:**

> ```
> minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
> screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
> picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-009 sha:c5afa127 src:kartky/k10-komandy.md:47 klas:F -->
### T-K10-009 · kod · рядок 47

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

<!-- fc id:T-K10-010 sha:4ffb7aee src:kartky/k10-komandy.md:54 klas:F -->
### T-K10-010 · proza · рядок 54

**Книга каже, дослівно:**

> `/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-011 sha:2130100e src:kartky/k10-komandy.md:54 klas:F -->
### T-K10-011 · proza · рядок 54

**Книга каже, дослівно:**

> `/dev/ttyACM*` — native USB [[S3]] [[C3]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-012 sha:3c153db1 src:kartky/k10-komandy.md:59 klas:F -->
### T-K10-012 · tablycya · рядок 59

**Книга каже, дослівно:**

> | Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-013 sha:b6d12a55 src:kartky/k10-komandy.md:61 klas:F -->
### T-K10-013 · tablycya · рядок 61

**Книга каже, дослівно:**

> | bootloader | `0x1000` | `0x0` | `0x2000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-014 sha:027efc02 src:kartky/k10-komandy.md:62 klas:F -->
### T-K10-014 · tablycya · рядок 62

**Книга каже, дослівно:**

> | partition table | `0x8000` | `0x8000` | `0x8000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-015 sha:259b5c05 src:kartky/k10-komandy.md:63 klas:F -->
### T-K10-015 · tablycya · рядок 63

**Книга каже, дослівно:**

> | застосунок | `0x10000` | `0x10000` | `0x10000` |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-016 sha:e3d7c0ea src:kartky/k10-komandy.md:64 klas:F -->
### T-K10-016 · tablycya · рядок 64

**Книга каже, дослівно:**

> | зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |

**Доказ**

- **Клас:** F — не звірено

---
