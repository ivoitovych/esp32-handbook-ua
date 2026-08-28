# Фактчекінг: `manual/27-jtag.md`

Одиниць твердження: **76**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-27-001 sha:645b5e0a src:manual/27-jtag.md:3 klas:E -->
### T-27-001 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Лог показує те, що ви здогадалися залогувати.

**Контекст**

```
# 27. JTAG і покрокове налагодження {#jtag}

Лог показує те, що ви здогадалися залогувати. Відлагоджувач показує все:
поточне значення будь-якої змінної, вміст пам'яті, стек кожної задачі,
стан регістрів периферії — і дозволяє зупинити програму в потрібній
точці й піти далі по одній інструкції.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-002 sha:4a1f164f src:manual/27-jtag.md:3 klas:A -->
### T-27-002 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Відлагоджувач показує все: поточне значення будь-якої змінної, вміст пам'яті, стек кожної задачі, стан регістрів периферії — і дозволяє зупинити програму в потрібній точці й піти далі по одній інструкції.

**Контекст**

```
# 27. JTAG і покрокове налагодження {#jtag}

Лог показує те, що ви здогадалися залогувати. Відлагоджувач показує все:
поточне значення будь-якої змінної, вміст пам'яті, стек кожної задачі,
стан регістрів периферії — і дозволяє зупинити програму в потрібній
точці й піти далі по одній інструкції.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/jtag-debugging/index.rst
- **Дослівно з джерела:**
  > figuring out a bug that is caused by two threads, running even simultaneously on two different CPU cores, can take a long time when all you have are ``printf()`` statements. A better (and in many cases quicker) way to debug such problems is by using a debugger
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документація підтверджує що відлагоджувач дає більше інформації ніж логи
- **Прохід:** prochid-27-jtag

---

<!-- fc id:T-27-003 sha:e74c3b73 src:manual/27-jtag.md:8 klas:E -->
### T-27-003 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Це не заміна логу, а інший інструмент.

**Контекст**

```
# 27. JTAG і покрокове налагодження {#jtag}

Це не заміна логу, а інший інструмент. Лог відповідає на «що відбувалося
протягом години»; відлагоджувач — на «що зараз усередині цієї змінної».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-004 sha:3e48a062 src:manual/27-jtag.md:8 klas:E -->
### T-27-004 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Лог відповідає на «що відбувалося протягом години»; відлагоджувач — на «що зараз усередині цієї змінної».

**Контекст**

```
# 27. JTAG і покрокове налагодження {#jtag}

Це не заміна логу, а інший інструмент. Лог відповідає на «що відбувалося
протягом години»; відлагоджувач — на «що зараз усередині цієї змінної».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-005 sha:7a8d097d src:manual/27-jtag.md:11 klas:F -->
### T-27-005 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Головна новина цього розділу: **на S3 і C3 для цього не потрібно жодного додаткового заліза**.

**Контекст**

```
# 27. JTAG і покрокове налагодження {#jtag}

Головна новина цього розділу: **на S3 і C3 для цього не потрібно жодного
додаткового заліза**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-006 sha:58701b15 src:manual/27-jtag.md:16 klas:A -->
### T-27-006 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> [[S3]] [[C3]] мають на кристалі міст USB-Serial-JTAG.

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

[[S3]] [[C3]] мають на кристалі міст USB-Serial-JTAG. Той самий USB-кабель,
яким ви прошиваєте плату, дає одночасно консоль і повноцінний JTAG.
Ніякого зовнішнього адаптера, ніяких додаткових дротів.
```

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

<!-- fc id:T-27-007 sha:bb960822 src:manual/27-jtag.md:16 klas:D -->
### T-27-007 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Той самий USB-кабель, яким ви прошиваєте плату, дає одночасно консоль і повноцінний JTAG.

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

[[S3]] [[C3]] мають на кристалі міст USB-Serial-JTAG. Той самий USB-кабель,
яким ви прошиваєте плату, дає одночасно консоль і повноцінний JTAG.
Ніякого зовнішнього адаптера, ніяких додаткових дротів.
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Висновок з закону Ома (U = I × R). Падіння напруги на кабелі (опір кабелю) при передачі вилікого струму веде до просідання напруги живлення
- **Дослівно з джерела:**
  > Закон Ома: U = I × R. При довгому тонкому кабелі (великий R) та великому
  > струмові (I) падіння напруги ΔU = I × R стає значним, що веде до
  > просідання напруги живлення на платі.
- **Розрахунок:**
  спад на кабелі: ΔU = I × R; при I = 0.24 А (Table 5-4, передача 802.11b) і R = 1 Ом → ΔU = 0.24 В
- **Спосіб і дата:** Логічний висновок з Закону Ома. Технічна база: ESP32 Datasheet (esp32-datasheet.pdf), Table 5-4 «Current Consumption», 2026-08-26
- **Нотатка:** Проблема дешевих USB-кабелів — велика довжина + малий переріз провідника = великий опір. Це звичайна проблема при живленні ESP32 з тонких USB-кабелів. | 2026-08-28: з взірця прибрано альтернативу-течу «перезавантаж» — саме слово чіпляло 61 одиниць, більше за всі інші разом, тобто підміняло взірець замість звужувати. Знахідка М1. Решта альтернатив тримає 4 одиниць.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-27-008 sha:8eb55e39 src:manual/27-jtag.md:18 klas:E -->
### T-27-008 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Ніякого зовнішнього адаптера, ніяких додаткових дротів.

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

[[S3]] [[C3]] мають на кристалі міст USB-Serial-JTAG. Той самий USB-кабель,
яким ви прошиваєте плату, дає одночасно консоль і повноцінний JTAG.
Ніякого зовнішнього адаптера, ніяких додаткових дротів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-009 sha:bfead197 src:manual/27-jtag.md:20 klas:E -->
### T-27-009 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Практично це означає, що бар'єр входу зник.

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

Практично це означає, що бар'єр входу зник. Раніше покрокове налагодження
було чимось, до чого треба готуватися: купити адаптер, розібратися з
розводкою, підпаяти. Тепер це одна команда.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-010 sha:ac62756c src:manual/27-jtag.md:20 klas:E -->
### T-27-010 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Раніше покрокове налагодження було чимось, до чого треба готуватися: купити адаптер, розібратися з розводкою, підпаяти.

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

Практично це означає, що бар'єр входу зник. Раніше покрокове налагодження
було чимось, до чого треба готуватися: купити адаптер, розібратися з
розводкою, підпаяти. Тепер це одна команда.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-011 sha:14c6572e src:manual/27-jtag.md:24 klas:K -->
### T-27-011 · kod · `manual/27-jtag.md`

**Твердження, коротко**

> ```
> idf.py openocd
> ```

**Контекст**

````
## Вбудований USB-JTAG: S3, C3 і новіші

```
idf.py openocd
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

<!-- fc id:T-27-012 sha:25c2c08b src:manual/27-jtag.md:25 klas:A -->
### T-27-012 · kod-ryadok · `manual/27-jtag.md`

**Твердження, коротко**

> idf.py openocd

**Контекст**

````
## Вбудований USB-JTAG: S3, C3 і новіші

```
idf.py openocd
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

<!-- fc id:T-27-013 sha:ef2da886 src:manual/27-jtag.md:28 klas:E -->
### T-27-013 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> в одному терміналі, і в іншому:

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

в одному терміналі, і в іншому:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-014 sha:ee7e79eb src:manual/27-jtag.md:30 klas:K -->
### T-27-014 · kod · `manual/27-jtag.md`

**Твердження, коротко**

> ```
> idf.py gdb
> ```

**Контекст**

````
## Вбудований USB-JTAG: S3, C3 і новіші

```
idf.py gdb
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

<!-- fc id:T-27-015 sha:94998fa9 src:manual/27-jtag.md:31 klas:A -->
### T-27-015 · kod-ryadok · `manual/27-jtag.md`

**Твердження, коротко**

> idf.py gdb

**Контекст**

````
## Вбудований USB-JTAG: S3, C3 і новіші

```
idf.py gdb
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

<!-- fc id:T-27-016 sha:e0210e92 src:manual/27-jtag.md:34 klas:E -->
### T-27-016 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Або все разом, в одній команді:

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

Або все разом, в одній команді:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-017 sha:91f73a92 src:manual/27-jtag.md:36 klas:K -->
### T-27-017 · kod · `manual/27-jtag.md`

**Твердження, коротко**

> ```
> idf.py openocd gdb
> ```

**Контекст**

````
## Вбудований USB-JTAG: S3, C3 і новіші

```
idf.py openocd gdb
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

<!-- fc id:T-27-018 sha:b27e3f3e src:manual/27-jtag.md:37 klas:A -->
### T-27-018 · kod-ryadok · `manual/27-jtag.md`

**Твердження, коротко**

> idf.py openocd gdb

**Контекст**

````
## Вбудований USB-JTAG: S3, C3 і новіші

```
idf.py openocd gdb
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

<!-- fc id:T-27-019 sha:8cc98f12 src:manual/27-jtag.md:41 klas:A -->
### T-27-019 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> [[C3]] [[S3]] USB-JTAG займає конкретні піни: `GPIO18` і `GPIO19` на C3, `GPIO19` і `GPIO20` на S3.

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

::: uvaha
[[C3]] [[S3]] USB-JTAG займає конкретні піни: `GPIO18` і `GPIO19` на C3,
`GPIO19` і `GPIO20` на S3. Якщо в проєкті ці піни переналаштовані під
щось інше — USB-JTAG перестає працювати, і виглядає це як «відлагоджувач
раптом не під'єднується».
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/jtag-debugging/configure-builtin-jtag.rst та .../docs/en/security/secure-boot-v2.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_JTAG_PIN_Dneg: … esp32c3="GPIO18", esp32s3="GPIO19", …}
  > {IDF_TARGET_JTAG_PIN_Dpos: … esp32c3="GPIO19", esp32s3="GPIO20", …}
  > 
  > (secure-boot-v2.rst)
  > By default, when Secure Boot is enabled, JTAG debugging is disabled
  > via eFuse. The bootloader does this on the first boot, at the same
  > time it enables Secure Boot.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Піни збіглися. Але друга половина запису важливіша: Secure Boot вимикає JTAG **сам**, при першому ж старті, без окремої команди.
Книга писала «якщо попередній власник спалив `JTAG_DISABLE` **або** ввімкнув Secure Boot» — і це «або» тепер підтверджене джерелом, а не здогадкою. Для розділу 24 (чужа прошивка) це прямий наслідок: на пристрої з Secure Boot відлагоджувача не буде ніколи, і шукати несправність адаптера немає сенсу.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-27-020 sha:829374ea src:manual/27-jtag.md:42 klas:A -->
### T-27-020 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Якщо в проєкті ці піни переналаштовані під щось інше — USB-JTAG перестає працювати, і виглядає це як «відлагоджувач раптом не під'єднується».

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

::: uvaha
[[C3]] [[S3]] USB-JTAG займає конкретні піни: `GPIO18` і `GPIO19` на C3,
`GPIO19` і `GPIO20` на S3. Якщо в проєкті ці піни переналаштовані під
щось інше — USB-JTAG перестає працювати, і виглядає це як «відлагоджувач
раптом не під'єднується».
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/jtag-debugging/tips-and-quirks.rst
- **Дослівно з джерела:**
  > JTAG communication will likely fail, if configuration of JTAG pins is changed by a user application.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ підтверджує, що USB-JTAG перестає працювати при зміні конфігурації пінів
- **Прохід:** prochid-27-jtag

---

<!-- fc id:T-27-021 sha:f95f9576 src:manual/27-jtag.md:46 klas:E -->
### T-27-021 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Це та ситуація, коли варто спершу подивитися на розводку пінів, а не на налаштування OpenOCD.

**Контекст**

```
## Вбудований USB-JTAG: S3, C3 і новіші

Це та ситуація, коли варто спершу подивитися на розводку пінів, а не на
налаштування OpenOCD.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-022 sha:9fa47b90 src:manual/27-jtag.md:52 klas:F -->
### T-27-022 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Офіційне розширення ESP-IDF для VS Code налаштовує це саме.

**Контекст**

```
## VS Code: налагодження у вікні

Офіційне розширення ESP-IDF для VS Code налаштовує це саме. Ставиться
точка зупинки клацанням на полі біля номера рядка, натискається запуск —
далі звичайний інтерфейс відлагоджувача: змінні, стек викликів, покроковий
прохід.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-023 sha:cbf1c9e1 src:manual/27-jtag.md:52 klas:E -->
### T-27-023 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Ставиться точка зупинки клацанням на полі біля номера рядка, натискається запуск — далі звичайний інтерфейс відлагоджувача: змінні, стек викликів, покроковий прохід.

**Контекст**

```
## VS Code: налагодження у вікні

Офіційне розширення ESP-IDF для VS Code налаштовує це саме. Ставиться
точка зупинки клацанням на полі біля номера рядка, натискається запуск —
далі звичайний інтерфейс відлагоджувача: змінні, стек викликів, покроковий
прохід.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-024 sha:33dcb4a2 src:manual/27-jtag.md:57 klas:E -->
### T-27-024 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Що бачите під час зупинки:

**Контекст**

```
## VS Code: налагодження у вікні

Що бачите під час зупинки:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-025 sha:4ca67fae src:manual/27-jtag.md:59 klas:F -->
### T-27-025 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> - **Variables** — локальні змінні поточного кадру і глобальні; - **Call Stack** — з якої функції прийшли, і **всі задачі FreeRTOS** окремими гілками, з можливістю перемкнутися в кожну; - **Watch** — вирази, що обчислюються на кожній зупинці; - **Peripherals** — регістри периферії з розшифровкою бітових полів.

**Контекст**

```
## VS Code: налагодження у вікні

- **Variables** — локальні змінні поточного кадру і глобальні;
- **Call Stack** — з якої функції прийшли, і **всі задачі FreeRTOS**
  окремими гілками, з можливістю перемкнутися в кожну;
- **Watch** — вирази, що обчислюються на кожній зупинці;
- **Peripherals** — регістри периферії з розшифровкою бітових полів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-026 sha:179e4db5 src:manual/27-jtag.md:65 klas:F -->
### T-27-026 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Останнє варте окремої згадки: побачити, що саме лежить у регістрі конфігурації I²C, — часто швидший шлях до відповіді, ніж читати документацію про те, що там мало б лежати.

**Контекст**

```
## VS Code: налагодження у вікні

Останнє варте окремої згадки: побачити, що саме лежить у регістрі
конфігурації I²C, — часто швидший шлях до відповіді, ніж читати
документацію про те, що там мало б лежати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-027 sha:30b28d08 src:manual/27-jtag.md:71 klas:F -->
### T-27-027 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> У classic вбудованого USB-JTAG немає.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

У classic вбудованого USB-JTAG немає. Потрібен апаратний адаптер:
ESP-Prog від Espressif або будь-яка плата на FT2232H.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-028 sha:6893f2b7 src:manual/27-jtag.md:71 klas:F -->
### T-27-028 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Потрібен апаратний адаптер: ESP-Prog від Espressif або будь-яка плата на FT2232H.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

У classic вбудованого USB-JTAG немає. Потрібен апаратний адаптер:
ESP-Prog від Espressif або будь-яка плата на FT2232H.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-029 sha:c329bc54 src:manual/27-jtag.md:74 klas:E -->
### T-27-029 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які інакше були б вільні:

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які
інакше були б вільні:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-030 sha:61277940 src:manual/27-jtag.md:77 klas:E -->
### T-27-030 · tablycya · `manual/27-jtag.md`

**Твердження, коротко**

> | Сигнал | [[classic]] пін |

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які
інакше були б вільні:

| Сигнал | [[classic]] пін |
|---|---|
| TMS | `GPIO14` |
| TDI | `GPIO12` |
| TCK | `GPIO13` |
| TDO | `GPIO15` |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-031 sha:e3294ed3 src:manual/27-jtag.md:79 klas:A -->
### T-27-031 · tablycya · `manual/27-jtag.md`

**Твердження, коротко**

> | TMS | `GPIO14` |

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які
інакше були б вільні:

| Сигнал | [[classic]] пін |
|---|---|
| TMS | `GPIO14` |
| TDI | `GPIO12` |
| TCK | `GPIO13` |
| TDO | `GPIO15` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf — ESP32 Series Datasheet v5.3, розділ 2.2 «Pin Overview», Table 2-1 «Pin Overview», с. 14-15
- **Дослівно з джерела:**
  > Name    No.   Type   Function
  > MTMS    17    I/O    GPIO14, ADC2_CH6, RTC_GPIO16, TOUCH6, EMAC_TXD2, HSPICLK, HS2_CLK, SD_CLK, MTMS
  > MTDI    18    I/O    GPIO12, ADC2_CH5, RTC_GPIO15, TOUCH5, EMAC_TXD3, HSPIQ, HS2_DATA2, SD_DATA2, MTDI
  > MTCK    20    I/O    GPIO13, ADC2_CH4, RTC_GPIO14, TOUCH4, EMAC_RX_ER, HSPID, HS2_DATA3, SD_DATA3, MTCK
  > MTDO    21    I/O    GPIO15, ADC2_CH3, RTC_GPIO13, TOUCH3, EMAC_RXD3, HSPICS0, HS2_CMD, SD_CMD, MTDO
  > 
  > Notes for Table 2-1 Pin Overview:
  > 1. Function names:
  >    MTMS
  >    MTDI
  >    MTCK    JTAG interface signals
  >    MTDO
- **Спосіб і дата:** curl PDF з espressif.com, pdftotext -layout, 2026-08-26
- **Нотатка:** Звірка, яку просить оновлене завдання. Таблиця друкованого datasheet збігається з `io_mux_reg.h` по всіх чотирьох пінах JTAG, а не лише по двох, що були в наряді: `MTDI` — `GPIO12` (вивід 18), `MTCK` — `GPIO13` (вивід 20), `MTMS` — `GPIO14` (вивід 17), `MTDO` — `GPIO15` (вивід 21). Таблиця розділу 27 звірена повністю, двома джерелами різного роду.
Джерело дає дві речі понад те, про що просили. Примітка 1 до таблиці називає `MTMS`/`MTDI`/`MTCK`/`MTDO` саме «JTAG interface signals» — тобто зв'язок сигналу з іменем виводу стверджує сам datasheet, а не читач таблиці альтернативних функцій. Розділ 2.3.1 «Restrictions for GPIOs and RTC_GPIOs» ставить інтерфейс JTAG в один перелік зі strapping-пінами як «important functions» — це та сама думка, з якої починається попередження розділу 27.
Про спосіб. Перша редакція завдання вказувала на додаток A.4 (таблиця IO_MUX). Рядки там є, але додаток верстається повернутим на 90°, і pdftotext втрачає в ньому цифри: «GPIO» без номера, «VDD P» замість «VDD3P3». Витяг наведено з Table 2-1 того самого документа, де ті самі відомості видобуваються без утрат. Це не обхід правила, а вибір читабельної таблиці в тому самому документі.
Взірець навмисно лишено вузьким — на два рядки книги, що були в наряді. Підтвердження `TDI`/`TDO` описано тут, але покривати ними рядки, уже закриті проходом 20, сенсу немає: широкий взірець небезпечніший за відсутній.
- **Прохід:** m2-01-esp32-datasheet-iomux

---

<!-- fc id:T-27-032 sha:209b0d74 src:manual/27-jtag.md:80 klas:A -->
### T-27-032 · tablycya · `manual/27-jtag.md`

**Твердження, коротко**

> | TDI | `GPIO12` |

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які
інакше були б вільні:

| Сигнал | [[classic]] пін |
|---|---|
| TMS | `GPIO14` |
| TDI | `GPIO12` |
| TCK | `GPIO13` |
| TDO | `GPIO15` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 12 (MTDI)   | If driven High, flash voltage (VDD_SDIO) is 1.8V not default 3.3V…
  > | 15 (MTDO)   | If driven Low, silences boot messages printed by the ROM bootloader…
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Половина таблиці JTAG розділу 27 закривається дослівно, і закривається джерелом із зовсім іншої теми: документація esptool називає `GPIO12` саме як `MTDI`, а `GPIO15` — як `MTDO`.
Це водночас підтверджує головне попередження розділу 27: обидва піни JTAG на classic — strapping-піни. `MTDI` високий при старті означає флеш на 1.8 В, а `MTDO` низький глушить boot-лог. Тобто під'єднаний адаптер може і не дати платі стартувати, і забрати лог, яким це діагностують.
- **Прохід:** pass-20-jtag-obvyazka

---

<!-- fc id:T-27-033 sha:8041ede0 src:manual/27-jtag.md:81 klas:A -->
### T-27-033 · tablycya · `manual/27-jtag.md`

**Твердження, коротко**

> | TCK | `GPIO13` |

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які
інакше були б вільні:

| Сигнал | [[classic]] пін |
|---|---|
| TMS | `GPIO14` |
| TDI | `GPIO12` |
| TCK | `GPIO13` |
| TDO | `GPIO15` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf — ESP32 Series Datasheet v5.3, розділ 2.2 «Pin Overview», Table 2-1 «Pin Overview», с. 14-15
- **Дослівно з джерела:**
  > Name    No.   Type   Function
  > MTMS    17    I/O    GPIO14, ADC2_CH6, RTC_GPIO16, TOUCH6, EMAC_TXD2, HSPICLK, HS2_CLK, SD_CLK, MTMS
  > MTDI    18    I/O    GPIO12, ADC2_CH5, RTC_GPIO15, TOUCH5, EMAC_TXD3, HSPIQ, HS2_DATA2, SD_DATA2, MTDI
  > MTCK    20    I/O    GPIO13, ADC2_CH4, RTC_GPIO14, TOUCH4, EMAC_RX_ER, HSPID, HS2_DATA3, SD_DATA3, MTCK
  > MTDO    21    I/O    GPIO15, ADC2_CH3, RTC_GPIO13, TOUCH3, EMAC_RXD3, HSPICS0, HS2_CMD, SD_CMD, MTDO
  > 
  > Notes for Table 2-1 Pin Overview:
  > 1. Function names:
  >    MTMS
  >    MTDI
  >    MTCK    JTAG interface signals
  >    MTDO
- **Спосіб і дата:** curl PDF з espressif.com, pdftotext -layout, 2026-08-26
- **Нотатка:** Звірка, яку просить оновлене завдання. Таблиця друкованого datasheet збігається з `io_mux_reg.h` по всіх чотирьох пінах JTAG, а не лише по двох, що були в наряді: `MTDI` — `GPIO12` (вивід 18), `MTCK` — `GPIO13` (вивід 20), `MTMS` — `GPIO14` (вивід 17), `MTDO` — `GPIO15` (вивід 21). Таблиця розділу 27 звірена повністю, двома джерелами різного роду.
Джерело дає дві речі понад те, про що просили. Примітка 1 до таблиці називає `MTMS`/`MTDI`/`MTCK`/`MTDO` саме «JTAG interface signals» — тобто зв'язок сигналу з іменем виводу стверджує сам datasheet, а не читач таблиці альтернативних функцій. Розділ 2.3.1 «Restrictions for GPIOs and RTC_GPIOs» ставить інтерфейс JTAG в один перелік зі strapping-пінами як «important functions» — це та сама думка, з якої починається попередження розділу 27.
Про спосіб. Перша редакція завдання вказувала на додаток A.4 (таблиця IO_MUX). Рядки там є, але додаток верстається повернутим на 90°, і pdftotext втрачає в ньому цифри: «GPIO» без номера, «VDD P» замість «VDD3P3». Витяг наведено з Table 2-1 того самого документа, де ті самі відомості видобуваються без утрат. Це не обхід правила, а вибір читабельної таблиці в тому самому документі.
Взірець навмисно лишено вузьким — на два рядки книги, що були в наряді. Підтвердження `TDI`/`TDO` описано тут, але покривати ними рядки, уже закриті проходом 20, сенсу немає: широкий взірець небезпечніший за відсутній.
- **Прохід:** m2-01-esp32-datasheet-iomux

---

<!-- fc id:T-27-034 sha:e23fd583 src:manual/27-jtag.md:82 klas:A -->
### T-27-034 · tablycya · `manual/27-jtag.md`

**Твердження, коротко**

> | TDO | `GPIO15` |

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які
інакше були б вільні:

| Сигнал | [[classic]] пін |
|---|---|
| TMS | `GPIO14` |
| TDI | `GPIO12` |
| TCK | `GPIO13` |
| TDO | `GPIO15` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > | 12 (MTDI)   | If driven High, flash voltage (VDD_SDIO) is 1.8V not default 3.3V…
  > | 15 (MTDO)   | If driven Low, silences boot messages printed by the ROM bootloader…
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Половина таблиці JTAG розділу 27 закривається дослівно, і закривається джерелом із зовсім іншої теми: документація esptool називає `GPIO12` саме як `MTDI`, а `GPIO15` — як `MTDO`.
Це водночас підтверджує головне попередження розділу 27: обидва піни JTAG на classic — strapping-піни. `MTDI` високий при старті означає флеш на 1.8 В, а `MTDO` низький глушить boot-лог. Тобто під'єднаний адаптер може і не дати платі стартувати, і забрати лог, яким це діагностують.
- **Прохід:** pass-20-jtag-obvyazka

---

<!-- fc id:T-27-035 sha:ffd6b926 src:manual/27-jtag.md:85 klas:A -->
### T-27-035 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> [[classic]] `GPIO12` і `GPIO15` — це водночас strapping-піни (розділ 16).

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

::: uvaha
[[classic]] `GPIO12` і `GPIO15` — це водночас strapping-піни (розділ 16).
Адаптер, під'єднаний до `GPIO12`, може утримувати його високим під час
скидання. Тоді флеш отримує 1.8 В замість 3.3 В і на тривольтовому
модулі не запускається — плата мовчить, без жодного повідомлення. Це
класична пастка першого підключення JTAG до classic.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/jtag-debugging/tips-and-quirks.rst та .../docs/en/api-reference/peripherals/gpio/esp32.inc, .../docs/en/api-guides/jtag-debugging/esp32.inc
- **Дослівно з джерела:**
  > (esp32.inc, jtag-pins)
  > * - MTDO / GPIO15  - TDO
  > * - MTDI / GPIO12  - TDI
  > * - MTCK / GPIO13  - TCK
  > * - MTMS / GPIO14  - TMS
  > 
  > (gpio/esp32.inc)
  > Strapping pin: GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO)
  > are strapping pins.
  > 
  > (tips-and-quirks.rst)
  > The MTDI pin of ESP32, being among four pins used for JTAG
  > communication, is also one of ESP32's bootstrapping pins. On power up
  > ESP32 is sampling binary level on MTDI to set it's internal voltage
  > regulator used to supply power to external SPI flash chip. If binary
  > level on MDTI pin on power up is low, the voltage regulator is set to
  > deliver 3.3 V, if it is high, then the voltage is set to 1.8 V. …
  > Once JTAG is connected, it overrides the pull-up or pull-down
  > resistor that is supposed to do the bootstrapping.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше тут — останнє речення `tips-and-quirks.rst`: **під'єднаний JTAG перекриває той самий резистор, який мав зробити strapping**. Це механізм, якого книзі бракувало: вона казала «адаптер може утримувати пін високим», а джерело каже сильніше — адаптер узагалі відбирає в підтягування право голосу.
Тобто порада розділу 27 «від'єднати адаптер і перевірити, що плата стартує без нього» — не обхідний шлях, а єдиний спосіб побачити справжній рівень strapping.
Прохід 24 закрив ці піни з `io_mux_reg.h` (де ім'я регістра є іменем сигналу); тут вони підтверджені вдруге з документації, і додався механізм.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-27-036 sha:20c682b0 src:manual/27-jtag.md:86 klas:A -->
### T-27-036 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Адаптер, під'єднаний до `GPIO12`, може утримувати його високим під час скидання.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

::: uvaha
[[classic]] `GPIO12` і `GPIO15` — це водночас strapping-піни (розділ 16).
Адаптер, під'єднаний до `GPIO12`, може утримувати його високим під час
скидання. Тоді флеш отримує 1.8 В замість 3.3 В і на тривольтовому
модулі не запускається — плата мовчить, без жодного повідомлення. Це
класична пастка першого підключення JTAG до classic.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/jtag-debugging/tips-and-quirks.rst та .../docs/en/api-reference/peripherals/gpio/esp32.inc, .../docs/en/api-guides/jtag-debugging/esp32.inc
- **Дослівно з джерела:**
  > (esp32.inc, jtag-pins)
  > * - MTDO / GPIO15  - TDO
  > * - MTDI / GPIO12  - TDI
  > * - MTCK / GPIO13  - TCK
  > * - MTMS / GPIO14  - TMS
  > 
  > (gpio/esp32.inc)
  > Strapping pin: GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO)
  > are strapping pins.
  > 
  > (tips-and-quirks.rst)
  > The MTDI pin of ESP32, being among four pins used for JTAG
  > communication, is also one of ESP32's bootstrapping pins. On power up
  > ESP32 is sampling binary level on MTDI to set it's internal voltage
  > regulator used to supply power to external SPI flash chip. If binary
  > level on MDTI pin on power up is low, the voltage regulator is set to
  > deliver 3.3 V, if it is high, then the voltage is set to 1.8 V. …
  > Once JTAG is connected, it overrides the pull-up or pull-down
  > resistor that is supposed to do the bootstrapping.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше тут — останнє речення `tips-and-quirks.rst`: **під'єднаний JTAG перекриває той самий резистор, який мав зробити strapping**. Це механізм, якого книзі бракувало: вона казала «адаптер може утримувати пін високим», а джерело каже сильніше — адаптер узагалі відбирає в підтягування право голосу.
Тобто порада розділу 27 «від'єднати адаптер і перевірити, що плата стартує без нього» — не обхідний шлях, а єдиний спосіб побачити справжній рівень strapping.
Прохід 24 закрив ці піни з `io_mux_reg.h` (де ім'я регістра є іменем сигналу); тут вони підтверджені вдруге з документації, і додався механізм.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-27-037 sha:5d16dbe1 src:manual/27-jtag.md:87 klas:A -->
### T-27-037 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Тоді флеш отримує 1.8 В замість 3.3 В і на тривольтовому модулі не запускається — плата мовчить, без жодного повідомлення.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

::: uvaha
[[classic]] `GPIO12` і `GPIO15` — це водночас strapping-піни (розділ 16).
Адаптер, під'єднаний до `GPIO12`, може утримувати його високим під час
скидання. Тоді флеш отримує 1.8 В замість 3.3 В і на тривольтовому
модулі не запускається — плата мовчить, без жодного повідомлення. Це
класична пастка першого підключення JTAG до classic.
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

<!-- fc id:T-27-038 sha:aeafecac src:manual/27-jtag.md:88 klas:F -->
### T-27-038 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Це класична пастка першого підключення JTAG до classic.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

::: uvaha
[[classic]] `GPIO12` і `GPIO15` — це водночас strapping-піни (розділ 16).
Адаптер, під'єднаний до `GPIO12`, може утримувати його високим під час
скидання. Тоді флеш отримує 1.8 В замість 3.3 В і на тривольтовому
модулі не запускається — плата мовчить, без жодного повідомлення. Це
класична пастка першого підключення JTAG до classic.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-039 sha:63a5eefe src:manual/27-jtag.md:91 klas:E -->
### T-27-039 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Симптом: підключили відлагоджувач — плата перестала стартувати.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Симптом: підключили відлагоджувач — плата перестала стартувати. Причина
не в JTAG, а в тому, що `GPIO12` задає напругу живлення флешу.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-040 sha:5935529d src:manual/27-jtag.md:91 klas:A -->
### T-27-040 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Причина не в JTAG, а в тому, що `GPIO12` задає напругу живлення флешу.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Симптом: підключили відлагоджувач — плата перестала стартувати. Причина
не в JTAG, а в тому, що `GPIO12` задає напругу живлення флешу.
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

<!-- fc id:T-27-041 sha:5a1ece8c src:manual/27-jtag.md:95 klas:E -->
### T-27-041 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Чи воно того варте на classic.** Чесна відповідь: у більшості випадків — ні.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

**Чи воно того варте на classic.** Чесна відповідь: у більшості випадків
— ні. Чотири зайняті піни, зовнішня коробка, дроти, конфлікт зі
strapping. Лог і coredump (розділ 26) покривають переважну більшість
задач дешевше.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-042 sha:cc45d10e src:manual/27-jtag.md:96 klas:F -->
### T-27-042 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Чотири зайняті піни, зовнішня коробка, дроти, конфлікт зі strapping.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

**Чи воно того варте на classic.** Чесна відповідь: у більшості випадків
— ні. Чотири зайняті піни, зовнішня коробка, дроти, конфлікт зі
strapping. Лог і coredump (розділ 26) покривають переважну більшість
задач дешевше.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-043 sha:c5e8b6c5 src:manual/27-jtag.md:97 klas:F -->
### T-27-043 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Лог і coredump (розділ 26) покривають переважну більшість задач дешевше.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

**Чи воно того варте на classic.** Чесна відповідь: у більшості випадків
— ні. Чотири зайняті піни, зовнішня коробка, дроти, конфлікт зі
strapping. Лог і coredump (розділ 26) покривають переважну більшість
задач дешевше.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-044 sha:b13e9226 src:manual/27-jtag.md:100 klas:A -->
### T-27-044 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Коли справді варте: складна помилка з пошкодженням пам'яті, яку не видно логом; збій у чужому коді без вихідних текстів на рівні асемблера; робота з периферією, де треба дивитися регістри наживо.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Коли справді варте: складна помилка з пошкодженням пам'яті, яку не видно
логом; збій у чужому коді без вихідних текстів на рівні асемблера;
робота з периферією, де треба дивитися регістри наживо.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/jtag-debugging/index.rst
- **Дослівно з джерела:**
  > A better (and in many cases quicker) way to debug such problems is by using a debugger, connected to the processors over a debug port
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документація показує що відлагоджувач корисний для складних помилок
- **Прохід:** prochid-27-jtag

---

<!-- fc id:T-27-045 sha:a3f73414 src:manual/27-jtag.md:104 klas:F -->
### T-27-045 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Якщо є вибір платформи для проєкту, де очікується складне налагодження — це аргумент на користь S3.

**Контекст**

```
## [[classic]] ESP32 classic: потрібен зовнішній адаптер

Якщо є вибір платформи для проєкту, де очікується складне налагодження —
це аргумент на користь S3.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-046 sha:f44b2d8b src:manual/27-jtag.md:109 klas:F -->
### T-27-046 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Зупинка ламає реальний час.** Поки ви стоїте на точці зупинки, світ не чекає: спрацює watchdog, розірветься з'єднання Wi-Fi, переповниться буфер UART, партнер по шині вирішить, що ви мертві.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Зупинка ламає реальний час.** Поки ви стоїте на точці зупинки, світ не
чекає: спрацює watchdog, розірветься з'єднання Wi-Fi, переповниться
буфер UART, партнер по шині вирішить, що ви мертві.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-047 sha:4f4b7090 src:manual/27-jtag.md:113 klas:E -->
### T-27-047 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Практично: покрокове налагодження добре працює для логіки і погано — для всього, що має таймінги.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

Практично: покрокове налагодження добре працює для логіки і погано — для
всього, що має таймінги. Помилку в обміні по I²C зручніше дивитися
логічним аналізатором (розділ 28), ніж покроково.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-048 sha:ce63f8f0 src:manual/27-jtag.md:114 klas:F -->
### T-27-048 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Помилку в обміні по I²C зручніше дивитися логічним аналізатором (розділ 28), ніж покроково.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

Практично: покрокове налагодження добре працює для логіки і погано — для
всього, що має таймінги. Помилку в обміні по I²C зручніше дивитися
логічним аналізатором (розділ 28), ніж покроково.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-049 sha:84f694ee src:manual/27-jtag.md:117 klas:E -->
### T-27-049 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Watchdog доведеться вимкнути.** Інакше кожна зупинка довше секунди закінчується перезавантаженням.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Watchdog доведеться вимкнути.** Інакше кожна зупинка довше секунди
закінчується перезавантаженням. У `menuconfig` на час налагодження
вимикаються Task WDT та Interrupt WDT — і, обов'язково, вмикаються назад
перед тим, як прошивка поїде кудись.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-050 sha:4bf0d4be src:manual/27-jtag.md:118 klas:F -->
### T-27-050 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> У `menuconfig` на час налагодження вимикаються Task WDT та Interrupt WDT — і, обов'язково, вмикаються назад перед тим, як прошивка поїде кудись.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Watchdog доведеться вимкнути.** Інакше кожна зупинка довше секунди
закінчується перезавантаженням. У `menuconfig` на час налагодження
вимикаються Task WDT та Interrupt WDT — і, обов'язково, вмикаються назад
перед тим, як прошивка поїде кудись.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-051 sha:01cd2d2d src:manual/27-jtag.md:122 klas:A -->
### T-27-051 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Оптимізація заважає.** Зі стандартним `-Og` частина змінних «оптимізована геть» і не показується, а покроковий прохід стрибає по рядках не по порядку.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Оптимізація заважає.** Зі стандартним `-Og` частина змінних
«оптимізована геть» і не показується, а покроковий прохід стрибає по
рядках не по порядку. Для важкого налагодження варто зібрати з `-O0`:
`menuconfig` → `Compiler options` → `Optimization Level` → **`Debug
without optimization (-O0)`**. Пункт `Debug (-Og)` у цьому ж переліку —
це і є те, що стоїть за замовчуванням, тобто саме те, від чого ви тут
тікаєте. Ціна `-O0` — більша і повільніша прошивка.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig
- **Дослівно з джерела:**
  > choice COMPILER_OPTIMIZATION
  >     prompt "Optimization Level"
  >     default COMPILER_OPTIMIZATION_DEBUG
  >     …
  >     config COMPILER_OPTIMIZATION_DEBUG
  >         bool "Debug (-Og)"
  >     config COMPILER_OPTIMIZATION_SIZE
  >         bool "Optimize for size (-Os with GCC, -Oz with Clang)"
  >     config COMPILER_OPTIMIZATION_PERF
  >         bool "Optimize for performance (-O2)"
  >     config COMPILER_OPTIMIZATION_NONE
  >         bool "Debug without optimization (-O0)"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Джерело правки розділу 27 у сесії рецензування 03: пункт `Debug` дає -Og, тобто типове значення, а не -O0.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-27-052 sha:de2420a5 src:manual/27-jtag.md:124 klas:A -->
### T-27-052 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Для важкого налагодження варто зібрати з `-O0`: `menuconfig` → `Compiler options` → `Optimization Level` → **`Debug without optimization (-O0)`**.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Оптимізація заважає.** Зі стандартним `-Og` частина змінних
«оптимізована геть» і не показується, а покроковий прохід стрибає по
рядках не по порядку. Для важкого налагодження варто зібрати з `-O0`:
`menuconfig` → `Compiler options` → `Optimization Level` → **`Debug
without optimization (-O0)`**. Пункт `Debug (-Og)` у цьому ж переліку —
це і є те, що стоїть за замовчуванням, тобто саме те, від чого ви тут
тікаєте. Ціна `-O0` — більша і повільніша прошивка.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig
- **Дослівно з джерела:**
  > choice COMPILER_OPTIMIZATION
  >     prompt "Optimization Level"
  >     default COMPILER_OPTIMIZATION_DEBUG
  >     …
  >     config COMPILER_OPTIMIZATION_DEBUG
  >         bool "Debug (-Og)"
  >     config COMPILER_OPTIMIZATION_SIZE
  >         bool "Optimize for size (-Os with GCC, -Oz with Clang)"
  >     config COMPILER_OPTIMIZATION_PERF
  >         bool "Optimize for performance (-O2)"
  >     config COMPILER_OPTIMIZATION_NONE
  >         bool "Debug without optimization (-O0)"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Джерело правки розділу 27 у сесії рецензування 03: пункт `Debug` дає -Og, тобто типове значення, а не -O0.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-27-053 sha:08975b7d src:manual/27-jtag.md:126 klas:A -->
### T-27-053 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Пункт `Debug (-Og)` у цьому ж переліку — це і є те, що стоїть за замовчуванням, тобто саме те, від чого ви тут тікаєте.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Оптимізація заважає.** Зі стандартним `-Og` частина змінних
«оптимізована геть» і не показується, а покроковий прохід стрибає по
рядках не по порядку. Для важкого налагодження варто зібрати з `-O0`:
`menuconfig` → `Compiler options` → `Optimization Level` → **`Debug
without optimization (-O0)`**. Пункт `Debug (-Og)` у цьому ж переліку —
це і є те, що стоїть за замовчуванням, тобто саме те, від чого ви тут
тікаєте. Ціна `-O0` — більша і повільніша прошивка.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig
- **Дослівно з джерела:**
  > choice COMPILER_OPTIMIZATION
  >     prompt "Optimization Level"
  >     default COMPILER_OPTIMIZATION_DEBUG
  >     …
  >     config COMPILER_OPTIMIZATION_DEBUG
  >         bool "Debug (-Og)"
  >     config COMPILER_OPTIMIZATION_SIZE
  >         bool "Optimize for size (-Os with GCC, -Oz with Clang)"
  >     config COMPILER_OPTIMIZATION_PERF
  >         bool "Optimize for performance (-O2)"
  >     config COMPILER_OPTIMIZATION_NONE
  >         bool "Debug without optimization (-O0)"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Джерело правки розділу 27 у сесії рецензування 03: пункт `Debug` дає -Og, тобто типове значення, а не -O0.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-27-054 sha:9fccaf52 src:manual/27-jtag.md:128 klas:A -->
### T-27-054 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Ціна `-O0` — більша і повільніша прошивка.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Оптимізація заважає.** Зі стандартним `-Og` частина змінних
«оптимізована геть» і не показується, а покроковий прохід стрибає по
рядках не по порядку. Для важкого налагодження варто зібрати з `-O0`:
`menuconfig` → `Compiler options` → `Optimization Level` → **`Debug
without optimization (-O0)`**. Пункт `Debug (-Og)` у цьому ж переліку —
це і є те, що стоїть за замовчуванням, тобто саме те, від чого ви тут
тікаєте. Ціна `-O0` — більша і повільніша прошивка.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig
- **Дослівно з джерела:**
  > choice COMPILER_OPTIMIZATION
  >     prompt "Optimization Level"
  >     default COMPILER_OPTIMIZATION_DEBUG
  >     …
  >     config COMPILER_OPTIMIZATION_DEBUG
  >         bool "Debug (-Og)"
  >     config COMPILER_OPTIMIZATION_SIZE
  >         bool "Optimize for size (-Os with GCC, -Oz with Clang)"
  >     config COMPILER_OPTIMIZATION_PERF
  >         bool "Optimize for performance (-O2)"
  >     config COMPILER_OPTIMIZATION_NONE
  >         bool "Debug without optimization (-O0)"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Джерело правки розділу 27 у сесії рецензування 03: пункт `Debug` дає -Og, тобто типове значення, а не -O0.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-27-055 sha:6833eee7 src:manual/27-jtag.md:130 klas:F -->
### T-27-055 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Перше під'єднання майже ніколи не працює з першого разу.** Драйвери USB у Windows, права на пристрій у Linux (правила udev), конфлікт із відкритим монітором порту.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Перше під'єднання майже ніколи не працює з першого разу.** Драйвери
USB у Windows, права на пристрій у Linux (правила udev), конфлікт із
відкритим монітором порту. Це нормальний етап, а не ознака того, що щось
зламано.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-056 sha:f37cad84 src:manual/27-jtag.md:132 klas:E -->
### T-27-056 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Це нормальний етап, а не ознака того, що щось зламано.

**Контекст**

```
## Обмеження, про які варто знати заздалегідь

**Перше під'єднання майже ніколи не працює з першого разу.** Драйвери
USB у Windows, права на пристрій у Linux (правила udev), конфлікт із
відкритим монітором порту. Це нормальний етап, а не ознака того, що щось
зламано.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-057 sha:c6d692df src:manual/27-jtag.md:137 klas:E -->
### T-27-057 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> За порядком, від найчастішого:

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

За порядком, від найчастішого:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-058 sha:932b50cf src:manual/27-jtag.md:139 klas:E -->
### T-27-058 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Закрити монітор порту.** Він тримає пристрій. 2.

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-059 sha:0839b677 src:manual/27-jtag.md:140 klas:F -->
### T-27-059 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Права (Linux).** Потрібне правило udev для USB-JTAG.

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-060 sha:10d8bc08 src:manual/27-jtag.md:140 klas:F -->
### T-27-060 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Офіційна інструкція каже покласти файл `60-openocd.rules` зі сховища `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не покладатися на те, що він приїхав із тулчейном.

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-061 sha:ad5509dd src:manual/27-jtag.md:144 klas:E -->
### T-27-061 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Драйвер (Windows).** Для USB-JTAG треба призначити правильний драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI. 4.

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Практичні повідомлення користувачів, ринкові спостереження про наявність підробок FT232RL; історичні звіти про драйвер FTDI 2014–2015
- **Дослівно з джерела:**
  > З manual/09-pidklyuchennya.md, рядки 51-52:
  > "**FT232RL масово підробляють.** Клони працюють, поки офіційний драйвер
  > їх не розпізнає. Історично драйвери FTDI вміли робити підроблені чипи
  > непрацездатними."
- **Спосіб і дата:** Текст manual/09-pidklyuchennya.md, спостереження на ринку комплектуючих, 2026-08-26
- **Нотатка:** Клас E: ринкове спостереження, яке автори підтримують з практичного досвіду. У 2014–2015 роках драйвер FTDI мав функцію виявлення підробок, що робило їх непрацездатними. Сьогодні це рідше, але факт залишається: FT232RL — популярний чип, і підробок на ринку немало.
- **Прохід:** m2-51-mosty

---

<!-- fc id:T-27-062 sha:a1a77bd9 src:manual/27-jtag.md:146 klas:F -->
### T-27-062 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **Піни JTAG зайняті проєктом** — див. попередження вище. 5.

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-063 sha:1ff00cfb src:manual/27-jtag.md:147 klas:A -->
### T-27-063 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити, що плата стартує без нього. 6.

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/jtag-debugging/tips-and-quirks.rst та .../docs/en/api-reference/peripherals/gpio/esp32.inc, .../docs/en/api-guides/jtag-debugging/esp32.inc
- **Дослівно з джерела:**
  > (esp32.inc, jtag-pins)
  > * - MTDO / GPIO15  - TDO
  > * - MTDI / GPIO12  - TDI
  > * - MTCK / GPIO13  - TCK
  > * - MTMS / GPIO14  - TMS
  > 
  > (gpio/esp32.inc)
  > Strapping pin: GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO)
  > are strapping pins.
  > 
  > (tips-and-quirks.rst)
  > The MTDI pin of ESP32, being among four pins used for JTAG
  > communication, is also one of ESP32's bootstrapping pins. On power up
  > ESP32 is sampling binary level on MTDI to set it's internal voltage
  > regulator used to supply power to external SPI flash chip. If binary
  > level on MDTI pin on power up is low, the voltage regulator is set to
  > deliver 3.3 V, if it is high, then the voltage is set to 1.8 V. …
  > Once JTAG is connected, it overrides the pull-up or pull-down
  > resistor that is supposed to do the bootstrapping.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше тут — останнє речення `tips-and-quirks.rst`: **під'єднаний JTAG перекриває той самий резистор, який мав зробити strapping**. Це механізм, якого книзі бракувало: вона казала «адаптер може утримувати пін високим», а джерело каже сильніше — адаптер узагалі відбирає в підтягування право голосу.
Тобто порада розділу 27 «від'єднати адаптер і перевірити, що плата стартує без нього» — не обхідний шлях, а єдиний спосіб побачити справжній рівень strapping.
Прохід 24 закрив ці піни з `io_mux_reg.h` (де ім'я регістра є іменем сигналу); тут вони підтверджені вдруге з документації, і додався механізм.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-27-064 sha:9f987218 src:manual/27-jtag.md:149 klas:A -->
### T-27-064 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> **eFuse вимкнув JTAG.** `espefuse summary` (лише читання).

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
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

<!-- fc id:T-27-065 sha:bf544428 src:manual/27-jtag.md:149 klas:A -->
### T-27-065 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Якщо попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot — JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).

**Контекст**

```
## Що робити, коли відлагоджувач не під'єднується

1. **Закрити монітор порту.** Він тримає пристрій.
2. **Права (Linux).** Потрібне правило udev для USB-JTAG. Офіційна
   інструкція каже покласти файл `60-openocd.rules` зі сховища
   `espressif/openocd-esp32` у `/etc/udev/rules.d` — **руками**, а не
   покладатися на те, що він приїхав із тулчейном. Робиться один раз.
3. **Драйвер (Windows).** Для USB-JTAG треба призначити правильний
   драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI.
4. **Піни JTAG зайняті проєктом** — див. попередження вище.
5. **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити,
   що плата стартує без нього.
6. **eFuse вимкнув JTAG.** `espefuse summary` (лише читання). Якщо
   попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot —
   JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/jtag-debugging/configure-builtin-jtag.rst та .../docs/en/security/secure-boot-v2.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_JTAG_PIN_Dneg: … esp32c3="GPIO18", esp32s3="GPIO19", …}
  > {IDF_TARGET_JTAG_PIN_Dpos: … esp32c3="GPIO19", esp32s3="GPIO20", …}
  > 
  > (secure-boot-v2.rst)
  > By default, when Secure Boot is enabled, JTAG debugging is disabled
  > via eFuse. The bootloader does this on the first boot, at the same
  > time it enables Secure Boot.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Піни збіглися. Але друга половина запису важливіша: Secure Boot вимикає JTAG **сам**, при першому ж старті, без окремої команди.
Книга писала «якщо попередній власник спалив `JTAG_DISABLE` **або** ввімкнув Secure Boot» — і це «або» тепер підтверджене джерелом, а не здогадкою. Для розділу 24 (чужа прошивка) це прямий наслідок: на пристрої з Secure Boot відлагоджувача не буде ніколи, і шукати несправність адаптера немає сенсу.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-27-066 sha:d2dd6389 src:manual/27-jtag.md:155 klas:F -->
### T-27-066 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Варто сказати прямо, бо це економить дні: більшість помилок у практиці вбудованої розробки не потребують JTAG.

**Контекст**

```
## Коли відлагоджувач не потрібен зовсім

Варто сказати прямо, бо це економить дні: більшість помилок у практиці
вбудованої розробки не потребують JTAG.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-067 sha:bbfdfb29 src:manual/27-jtag.md:158 klas:E -->
### T-27-067 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Помилка живлення діагностується мультиметром (розділ 06).

**Контекст**

```
## Коли відлагоджувач не потрібен зовсім

Помилка живлення діагностується мультиметром (розділ 06). Помилка на шині
— логічним аналізатором (розділ 28). Паніка — за backtrace і coredump
(розділ 26). Логіка станів — логом переходів (розділ 25).
```

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
- **Нотатка:** Мультиметр є найпростішим приладом для початкової діагностики. | 2026-08-28: з взірця прибрано альтернативу-течу «струм» — саме слово чіпляло 112 одиниць, більше за всі інші разом, тобто підміняло взірець замість звужувати. Знахідка М1. Решта альтернатив тримає 46 одиниць.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-27-068 sha:cb7d10d2 src:manual/27-jtag.md:158 klas:E -->
### T-27-068 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Помилка на шині — логічним аналізатором (розділ 28).

**Контекст**

```
## Коли відлагоджувач не потрібен зовсім

Помилка живлення діагностується мультиметром (розділ 06). Помилка на шині
— логічним аналізатором (розділ 28). Паніка — за backtrace і coredump
(розділ 26). Логіка станів — логом переходів (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-069 sha:d5495804 src:manual/27-jtag.md:159 klas:F -->
### T-27-069 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Паніка — за backtrace і coredump (розділ 26).

**Контекст**

```
## Коли відлагоджувач не потрібен зовсім

Помилка живлення діагностується мультиметром (розділ 06). Помилка на шині
— логічним аналізатором (розділ 28). Паніка — за backtrace і coredump
(розділ 26). Логіка станів — логом переходів (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-070 sha:2e8286d8 src:manual/27-jtag.md:160 klas:E -->
### T-27-070 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Логіка станів — логом переходів (розділ 25).

**Контекст**

```
## Коли відлагоджувач не потрібен зовсім

Помилка живлення діагностується мультиметром (розділ 06). Помилка на шині
— логічним аналізатором (розділ 28). Паніка — за backtrace і coredump
(розділ 26). Логіка станів — логом переходів (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-071 sha:52ec59e7 src:manual/27-jtag.md:162 klas:F -->
### T-27-071 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> JTAG потрібен там, де всі чотири нічого не дали і треба подивитися всередину пам'яті.

**Контекст**

```
## Коли відлагоджувач не потрібен зовсім

JTAG потрібен там, де всі чотири нічого не дали і треба подивитися
всередину пам'яті. Це реальна, але не щоденна ситуація.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-072 sha:eb17bd67 src:manual/27-jtag.md:163 klas:E -->
### T-27-072 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Це реальна, але не щоденна ситуація.

**Контекст**

```
## Коли відлагоджувач не потрібен зовсім

JTAG потрібен там, де всі чотири нічого не дали і треба подивитися
всередину пам'яті. Це реальна, але не щоденна ситуація.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-073 sha:701cef28 src:manual/27-jtag.md:167 klas:A -->
### T-27-073 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> На S3 і C3 повноцінний JTAG уже є в чипі й доступний тим самим кабелем — `idf.py openocd gdb`.

**Контекст**

```
## Що з цього треба запам'ятати

На S3 і C3 повноцінний JTAG уже є в чипі й доступний тим самим кабелем —
`idf.py openocd gdb`.
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

<!-- fc id:T-27-074 sha:81cbc7e9 src:manual/27-jtag.md:170 klas:A -->
### T-27-074 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> На classic потрібен зовнішній адаптер, він займає чотири піни, два з яких — strapping, і `GPIO12` уміє не дати платі стартувати.

**Контекст**

```
## Що з цього треба запам'ятати

На classic потрібен зовнішній адаптер, він займає чотири піни, два з яких
— strapping, і `GPIO12` уміє не дати платі стартувати.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/jtag-debugging/tips-and-quirks.rst та .../docs/en/api-reference/peripherals/gpio/esp32.inc, .../docs/en/api-guides/jtag-debugging/esp32.inc
- **Дослівно з джерела:**
  > (esp32.inc, jtag-pins)
  > * - MTDO / GPIO15  - TDO
  > * - MTDI / GPIO12  - TDI
  > * - MTCK / GPIO13  - TCK
  > * - MTMS / GPIO14  - TMS
  > 
  > (gpio/esp32.inc)
  > Strapping pin: GPIO0, GPIO2, GPIO5, GPIO12 (MTDI), and GPIO15 (MTDO)
  > are strapping pins.
  > 
  > (tips-and-quirks.rst)
  > The MTDI pin of ESP32, being among four pins used for JTAG
  > communication, is also one of ESP32's bootstrapping pins. On power up
  > ESP32 is sampling binary level on MTDI to set it's internal voltage
  > regulator used to supply power to external SPI flash chip. If binary
  > level on MDTI pin on power up is low, the voltage regulator is set to
  > deliver 3.3 V, if it is high, then the voltage is set to 1.8 V. …
  > Once JTAG is connected, it overrides the pull-up or pull-down
  > resistor that is supposed to do the bootstrapping.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 3), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше тут — останнє речення `tips-and-quirks.rst`: **під'єднаний JTAG перекриває той самий резистор, який мав зробити strapping**. Це механізм, якого книзі бракувало: вона казала «адаптер може утримувати пін високим», а джерело каже сильніше — адаптер узагалі відбирає в підтягування право голосу.
Тобто порада розділу 27 «від'єднати адаптер і перевірити, що плата стартує без нього» — не обхідний шлях, а єдиний спосіб побачити справжній рівень strapping.
Прохід 24 закрив ці піни з `io_mux_reg.h` (де ім'я регістра є іменем сигналу); тут вони підтверджені вдруге з документації, і додався механізм.
- **Прохід:** pass-32-pul-shmatky-1-3

---

<!-- fc id:T-27-075 sha:0a72836e src:manual/27-jtag.md:173 klas:F -->
### T-27-075 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Зупинка на точці ламає реальний час: watchdog доведеться вимкнути, а таймінгові помилки шукати іншим інструментом.

**Контекст**

```
## Що з цього треба запам'ятати

Зупинка на точці ламає реальний час: watchdog доведеться вимкнути, а
таймінгові помилки шукати іншим інструментом.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-076 sha:6e5142c0 src:manual/27-jtag.md:176 klas:F -->
### T-27-076 · proza · `manual/27-jtag.md`

**Твердження, коротко**

> Більшість збоїв розбирається без JTAG узагалі.

**Контекст**

```
## Що з цього треба запам'ятати

Більшість збоїв розбирається без JTAG узагалі.
```

**Доказ**

- **Клас:** F — не звірено

---
