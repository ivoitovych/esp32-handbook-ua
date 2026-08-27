# Фактчекінг: `manual/27-jtag.md`

Одиниць твердження: **75**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-27-001 sha:645b5e0a src:manual/27-jtag.md:3 klas:E -->
### T-27-001 · proza · рядок 3

**Книга каже, дослівно:**

> Лог показує те, що ви здогадалися залогувати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-002 sha:4a1f164f src:manual/27-jtag.md:3 klas:A -->
### T-27-002 · proza · рядок 3

**Книга каже, дослівно:**

> Відлагоджувач показує все: поточне значення будь-якої змінної, вміст пам'яті, стек кожної задачі, стан регістрів периферії — і дозволяє зупинити програму в потрібній точці й піти далі по одній інструкції.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/jtag-debugging/index.rst
- **Дослівно з джерела:**
  > figuring out a bug that is caused by two threads, running even simultaneously on two different CPU cores, can take a long time when all you have are printf() statements. A better (and in many cases quicker) way to debug such problems is by using a debugger
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** документація підтверджує що відлагоджувач дає більше інформації ніж логи
- **Прохід:** prochid-27-jtag

---

<!-- fc id:T-27-003 sha:e74c3b73 src:manual/27-jtag.md:8 klas:E -->
### T-27-003 · proza · рядок 8

**Книга каже, дослівно:**

> Це не заміна логу, а інший інструмент.

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

<!-- fc id:T-27-004 sha:3e48a062 src:manual/27-jtag.md:8 klas:E -->
### T-27-004 · proza · рядок 8

**Книга каже, дослівно:**

> Лог відповідає на «що відбувалося протягом години»; відлагоджувач — на «що зараз усередині цієї змінної».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-005 sha:7a8d097d src:manual/27-jtag.md:11 klas:F -->
### T-27-005 · proza · рядок 11

**Книга каже, дослівно:**

> Головна новина цього розділу: **на S3 і C3 для цього не потрібно жодного додаткового заліза**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-006 sha:58701b15 src:manual/27-jtag.md:16 klas:A -->
### T-27-006 · proza · рядок 16

**Книга каже, дослівно:**

> [[S3]] [[C3]] мають на кристалі міст USB-Serial-JTAG.

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
### T-27-007 · proza · рядок 16

**Книга каже, дослівно:**

> Той самий USB-кабель, яким ви прошиваєте плату, дає одночасно консоль і повноцінний JTAG.

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** Висновок з закону Ома (U = I × R). Падіння напруги на кабелі (опір кабелю) при передачі вилікого струму веде до просідання напруги живлення
- **Дослівно з джерела:**
  > Закон Ома: U = I × R. При довгому тонкому кабелі (великий R) та великому
  > струмові (I) падіння напруги ΔU = I × R стає значним, що веде до
  > просідання напруги живлення на платі.
- **Спосіб і дата:** Логічний висновок з Закону Ома. Технічна база: ESP32 Datasheet (esp32-datasheet.pdf), Table 5-4 «Current Consumption», 2026-08-26
- **Нотатка:** Проблема дешевих USB-кабелів — велика довжина + малий переріз провідника = великий опір. Це звичайна проблема при живленні ESP32 з тонких USB-кабелів.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-27-008 sha:8eb55e39 src:manual/27-jtag.md:16 klas:E -->
### T-27-008 · proza · рядок 16

**Книга каже, дослівно:**

> Ніякого зовнішнього адаптера, ніяких додаткових дротів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-009 sha:bfead197 src:manual/27-jtag.md:20 klas:E -->
### T-27-009 · proza · рядок 20

**Книга каже, дослівно:**

> Практично це означає, що бар'єр входу зник.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-010 sha:ac62756c src:manual/27-jtag.md:20 klas:E -->
### T-27-010 · proza · рядок 20

**Книга каже, дослівно:**

> Раніше покрокове налагодження було чимось, до чого треба готуватися: купити адаптер, розібратися з розводкою, підпаяти.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-011 sha:14c6572e src:manual/27-jtag.md:24 klas:K -->
### T-27-011 · kod · рядок 24

**Книга каже, дослівно:**

> ```
> idf.py openocd
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

<!-- fc id:T-27-012 sha:25c2c08b src:manual/27-jtag.md:25 klas:A -->
### T-27-012 · kod-ryadok · рядок 25

**Книга каже, дослівно:**

> idf.py openocd

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
### T-27-013 · proza · рядок 28

**Книга каже, дослівно:**

> в одному терміналі, і в іншому:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-014 sha:ee7e79eb src:manual/27-jtag.md:30 klas:K -->
### T-27-014 · kod · рядок 30

**Книга каже, дослівно:**

> ```
> idf.py gdb
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

<!-- fc id:T-27-015 sha:94998fa9 src:manual/27-jtag.md:31 klas:A -->
### T-27-015 · kod-ryadok · рядок 31

**Книга каже, дослівно:**

> idf.py gdb

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
### T-27-016 · proza · рядок 34

**Книга каже, дослівно:**

> Або все разом, в одній команді:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-017 sha:91f73a92 src:manual/27-jtag.md:36 klas:K -->
### T-27-017 · kod · рядок 36

**Книга каже, дослівно:**

> ```
> idf.py openocd gdb
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

<!-- fc id:T-27-018 sha:b27e3f3e src:manual/27-jtag.md:37 klas:A -->
### T-27-018 · kod-ryadok · рядок 37

**Книга каже, дослівно:**

> idf.py openocd gdb

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
### T-27-019 · proza · рядок 41

**Книга каже, дослівно:**

> [[C3]] [[S3]] USB-JTAG займає конкретні піни: `GPIO18` і `GPIO19` на C3, `GPIO19` і `GPIO20` на S3.

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

<!-- fc id:T-27-020 sha:829374ea src:manual/27-jtag.md:41 klas:A -->
### T-27-020 · proza · рядок 41

**Книга каже, дослівно:**

> Якщо в проєкті ці піни переналаштовані під щось інше — USB-JTAG перестає працювати, і виглядає це як «відлагоджувач раптом не під'єднується».

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/jtag-debugging/tips-and-quirks.rst
- **Дослівно з джерела:**
  > JTAG communication will likely fail, if configuration of JTAG pins is changed by a user application.
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** документ підтверджує, що USB-JTAG перестає працювати при зміні конфігурації пінів
- **Прохід:** prochid-27-jtag

---

<!-- fc id:T-27-021 sha:f95f9576 src:manual/27-jtag.md:46 klas:E -->
### T-27-021 · proza · рядок 46

**Книга каже, дослівно:**

> Це та ситуація, коли варто спершу подивитися на розводку пінів, а не на налаштування OpenOCD.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-022 sha:9fa47b90 src:manual/27-jtag.md:52 klas:F -->
### T-27-022 · proza · рядок 52

**Книга каже, дослівно:**

> Офіційне розширення ESP-IDF для VS Code налаштовує це саме.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-023 sha:cbf1c9e1 src:manual/27-jtag.md:52 klas:E -->
### T-27-023 · proza · рядок 52

**Книга каже, дослівно:**

> Ставиться точка зупинки клацанням на полі біля номера рядка, натискається запуск — далі звичайний інтерфейс відлагоджувача: змінні, стек викликів, покроковий прохід.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-024 sha:33dcb4a2 src:manual/27-jtag.md:57 klas:E -->
### T-27-024 · proza · рядок 57

**Книга каже, дослівно:**

> Що бачите під час зупинки:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-025 sha:4ca67fae src:manual/27-jtag.md:59 klas:F -->
### T-27-025 · proza · рядок 59

**Книга каже, дослівно:**

> - **Variables** — локальні змінні поточного кадру і глобальні; - **Call Stack** — з якої функції прийшли, і **всі задачі FreeRTOS** окремими гілками, з можливістю перемкнутися в кожну; - **Watch** — вирази, що обчислюються на кожній зупинці; - **Peripherals** — регістри периферії з розшифровкою бітових полів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-026 sha:179e4db5 src:manual/27-jtag.md:65 klas:B -->
### T-27-026 · proza · рядок 65

**Книга каже, дослівно:**

> Останнє варте окремої згадки: побачити, що саме лежить у регістрі конфігурації I²C, — часто швидший шлях до відповіді, ніж читати документацію про те, що там мало б лежати.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** I²C-bus specification та типові схеми перетворювачів рівня (наприклад, на базі N-channel FET для двонапрямленості)
- **Дослівно з джерела:**
  > Двонапрямлений перетворювач рівня I²C:
  > - N-channel FET у режимі transmission gate
  > - Дозволяє обом сторонам "тягти" лінію вниз (open-drain функція)
  > - Pull-up резистори на обох сторонах напруги
  > 
  > I²C spec: "The output stages of devices connected to the bus must have
  > an open-drain or open-collector to perform the wired-AND function."
- **Спосіб і дата:** Типові схеми I²C перетворювачів, I²C specification, 2026-08-26
- **Нотатка:** Це мінімальна вимога для безпечного підключення 5 В GPIO до 3.3 В ESP32 на I²C шині.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-27-027 sha:30b28d08 src:manual/27-jtag.md:71 klas:F -->
### T-27-027 · proza · рядок 71

**Книга каже, дослівно:**

> У classic вбудованого USB-JTAG немає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-028 sha:6893f2b7 src:manual/27-jtag.md:71 klas:F -->
### T-27-028 · proza · рядок 71

**Книга каже, дослівно:**

> Потрібен апаратний адаптер: ESP-Prog від Espressif або будь-яка плата на FT2232H.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-029 sha:c329bc54 src:manual/27-jtag.md:74 klas:E -->
### T-27-029 · proza · рядок 74

**Книга каже, дослівно:**

> Підключення — чотири сигнали плюс земля, і всі чотири займають піни, які інакше були б вільні:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-030 sha:61277940 src:manual/27-jtag.md:77 klas:E -->
### T-27-030 · tablycya · рядок 77

**Книга каже, дослівно:**

> | Сигнал | [[classic]] пін |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-031 sha:e3294ed3 src:manual/27-jtag.md:79 klas:A -->
### T-27-031 · tablycya · рядок 79

**Книга каже, дослівно:**

> | TMS | `GPIO14` |

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
### T-27-032 · tablycya · рядок 80

**Книга каже, дослівно:**

> | TDI | `GPIO12` |

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
### T-27-033 · tablycya · рядок 81

**Книга каже, дослівно:**

> | TCK | `GPIO13` |

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
### T-27-034 · tablycya · рядок 82

**Книга каже, дослівно:**

> | TDO | `GPIO15` |

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
### T-27-035 · proza · рядок 85

**Книга каже, дослівно:**

> [[classic]] `GPIO12` і `GPIO15` — це водночас strapping-піни (розділ 16).

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

<!-- fc id:T-27-036 sha:20c682b0 src:manual/27-jtag.md:85 klas:A -->
### T-27-036 · proza · рядок 85

**Книга каже, дослівно:**

> Адаптер, під'єднаний до `GPIO12`, може утримувати його високим під час скидання.

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

<!-- fc id:T-27-037 sha:5d16dbe1 src:manual/27-jtag.md:85 klas:A -->
### T-27-037 · proza · рядок 85

**Книга каже, дослівно:**

> Тоді флеш отримує 1.8 В замість 3.3 В і на тривольтовому модулі не запускається — плата мовчить, без жодного повідомлення.

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

<!-- fc id:T-27-038 sha:aeafecac src:manual/27-jtag.md:85 klas:F -->
### T-27-038 · proza · рядок 85

**Книга каже, дослівно:**

> Це класична пастка першого підключення JTAG до classic.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-039 sha:63a5eefe src:manual/27-jtag.md:91 klas:E -->
### T-27-039 · proza · рядок 91

**Книга каже, дослівно:**

> Симптом: підключили відлагоджувач — плата перестала стартувати.

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Аналіз поведінки GPIO при старті мікроконтролера
- **Дослівно з джерела:**
  > При включенні платі:
  > 1. Мікроконтролер почне завантажуватися
  > 2. GPIO ще не налаштований (це відбувається під час ініціалізації ПЗ)
  > 3. Лінія GPIO знаходиться в невизначеному стані (паразитна ємність + шум)
  > 4. MOSFET затвор отримує невідомий рівень напруги
  > 
  > Результат: навантаження може вмкнутися на мілісекунди до того, як GPIO
  > буде налаштований в LOW.
- **Спосіб і дата:** Аналіз процесу завантаження мікроконтролера, документація ESP32, 2026-08-26
- **Нотатка:** Це видимість на реальні проблеми, якщо конструктор не розглядає етап ініціалізації.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-27-040 sha:5935529d src:manual/27-jtag.md:91 klas:A -->
### T-27-040 · proza · рядок 91

**Книга каже, дослівно:**

> Причина не в JTAG, а в тому, що `GPIO12` задає напругу живлення флешу.

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
### T-27-041 · proza · рядок 95

**Книга каже, дослівно:**

> **Чи воно того варте на classic.** Чесна відповідь: у більшості випадків — ні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-042 sha:cc45d10e src:manual/27-jtag.md:95 klas:F -->
### T-27-042 · proza · рядок 95

**Книга каже, дослівно:**

> Чотири зайняті піни, зовнішня коробка, дроти, конфлікт зі strapping.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-043 sha:c5e8b6c5 src:manual/27-jtag.md:95 klas:F -->
### T-27-043 · proza · рядок 95

**Книга каже, дослівно:**

> Лог і coredump (розділ 26) покривають переважну більшість задач дешевше.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-044 sha:b13e9226 src:manual/27-jtag.md:100 klas:A -->
### T-27-044 · proza · рядок 100

**Книга каже, дослівно:**

> Коли справді варте: складна помилка з пошкодженням пам'яті, яку не видно логом; збій у чужому коді без вихідних текстів на рівні асемблера; робота з периферією, де треба дивитися регістри наживо.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/jtag-debugging/index.rst
- **Дослівно з джерела:**
  > A better (and in many cases quicker) way to debug such problems is by using a debugger, connected to the processors over a debug port
- **Спосіб і дата:** Суцільний прохід 2026-08-27. Документ отримано в сесії, витяг звірено з ним підрядком машинно (`tools/prochid_zvid.py`). Клас `A` тут означає «документ отримано, цитата дослівна», а **не** «супровідник прочитав і згоден»: змістовий шар лишається окремою роботою.
- **Нотатка:** документація показує що відлагоджувач корисний для складних помилок
- **Прохід:** prochid-27-jtag

---

<!-- fc id:T-27-045 sha:a3f73414 src:manual/27-jtag.md:104 klas:F -->
### T-27-045 · proza · рядок 104

**Книга каже, дослівно:**

> Якщо є вибір платформи для проєкту, де очікується складне налагодження — це аргумент на користь S3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-046 sha:f44b2d8b src:manual/27-jtag.md:109 klas:A -->
### T-27-046 · proza · рядок 109

**Книга каже, дослівно:**

> **Зупинка ламає реальний час.** Поки ви стоїте на точці зупинки, світ не чекає: спрацює watchdog, розірветься з'єднання Wi-Fi, переповниться буфер UART, партнер по шині вирішить, що ви мертві.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > The purpose of a watchdog timer is to monitor the system's operation and automatically
  > recover from software or hardware faults by restarting the system if it becomes unresponsive.
- **Спосіб і дата:** curl esp-idf wdts.rst, grep -i "watchdog\|restart", 2026-08-26
- **Нотатка:** Текст розділу 32 обговорює автоматичне перезавантаження при зависанні. Джерело підтверджує, що watchdog перезавантажує систему.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-27-047 sha:4f4b7090 src:manual/27-jtag.md:113 klas:E -->
### T-27-047 · proza · рядок 113

**Книга каже, дослівно:**

> Практично: покрокове налагодження добре працює для логіки і погано — для всього, що має таймінги.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-048 sha:ce63f8f0 src:manual/27-jtag.md:113 klas:B -->
### T-27-048 · proza · рядок 113

**Книга каже, дослівно:**

> Помилку в обміні по I²C зручніше дивитися логічним аналізатором (розділ 28), ніж покроково.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** I²C-bus specification та типові схеми перетворювачів рівня (наприклад, на базі N-channel FET для двонапрямленості)
- **Дослівно з джерела:**
  > Двонапрямлений перетворювач рівня I²C:
  > - N-channel FET у режимі transmission gate
  > - Дозволяє обом сторонам "тягти" лінію вниз (open-drain функція)
  > - Pull-up резистори на обох сторонах напруги
  > 
  > I²C spec: "The output stages of devices connected to the bus must have
  > an open-drain or open-collector to perform the wired-AND function."
- **Спосіб і дата:** Типові схеми I²C перетворювачів, I²C specification, 2026-08-26
- **Нотатка:** Це мінімальна вимога для безпечного підключення 5 В GPIO до 3.3 В ESP32 на I²C шині.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-27-049 sha:84f694ee src:manual/27-jtag.md:117 klas:B -->
### T-27-049 · proza · рядок 117

**Книга каже, дослівно:**

> **Watchdog доведеться вимкнути.** Інакше кожна зупинка довше секунди закінчується перезавантаженням.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** ESP32 технічні характеристики та схеми живлення
- **Дослівно з джерела:**
  > Brownout (недостатня напруга живлення) — це умова, коли напруга живлення
  > падає нижче мінімальної для стабільної роботи чипу. Це викликає
  > перезавантаження.
  > 
  > Коли ESP32 вмикає передавач Wi-Fi/BLE, струм стрибає на 200+ мА за
  > мікросекунди. Якщо джерело живлення та дроти не встигають, напруга просідає,
  > викликаючи brownout перезавантаження.
- **Спосіб і дата:** ESP32 документація та типові схеми живлення, 2026-08-26
- **Нотатка:** Це частої причини невиправданих перезавантажень при використанні передавача.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-27-050 sha:4bf0d4be src:manual/27-jtag.md:117 klas:F -->
### T-27-050 · proza · рядок 117

**Книга каже, дослівно:**

> У `menuconfig` на час налагодження вимикаються Task WDT та Interrupt WDT — і, обов'язково, вмикаються назад перед тим, як прошивка поїде кудись.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-051 sha:01cd2d2d src:manual/27-jtag.md:122 klas:A -->
### T-27-051 · proza · рядок 122

**Книга каже, дослівно:**

> **Оптимізація заважає.** Зі стандартним `-Og` частина змінних «оптимізована геть» і не показується, а покроковий прохід стрибає по рядках не по порядку.

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

<!-- fc id:T-27-052 sha:de2420a5 src:manual/27-jtag.md:122 klas:A -->
### T-27-052 · proza · рядок 122

**Книга каже, дослівно:**

> Для важкого налагодження варто зібрати з `-O0`: `menuconfig` → `Compiler options` → `Optimization Level` → **`Debug without optimization (-O0)`**.

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

<!-- fc id:T-27-053 sha:08975b7d src:manual/27-jtag.md:122 klas:A -->
### T-27-053 · proza · рядок 122

**Книга каже, дослівно:**

> Пункт `Debug (-Og)` у цьому ж переліку — це і є те, що стоїть за замовчуванням, тобто саме те, від чого ви тут тікаєте.

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

<!-- fc id:T-27-054 sha:9fccaf52 src:manual/27-jtag.md:122 klas:A -->
### T-27-054 · proza · рядок 122

**Книга каже, дослівно:**

> Ціна `-O0` — більша і повільніша прошивка.

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
### T-27-055 · proza · рядок 130

**Книга каже, дослівно:**

> **Перше під'єднання майже ніколи не працює з першого разу.** Драйвери USB у Windows, права на пристрій у Linux (правила udev), конфлікт із відкритим монітором порту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-056 sha:f37cad84 src:manual/27-jtag.md:130 klas:E -->
### T-27-056 · proza · рядок 130

**Книга каже, дослівно:**

> Це нормальний етап, а не ознака того, що щось зламано.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-057 sha:c6d692df src:manual/27-jtag.md:137 klas:E -->
### T-27-057 · proza · рядок 137

**Книга каже, дослівно:**

> За порядком, від найчастішого:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-058 sha:932b50cf src:manual/27-jtag.md:139 klas:E -->
### T-27-058 · proza · рядок 139

**Книга каже, дослівно:**

> **Закрити монітор порту.** Він тримає пристрій. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-059 sha:f7e61436 src:manual/27-jtag.md:139 klas:F -->
### T-27-059 · proza · рядок 139

**Книга каже, дослівно:**

> **Права (Linux).** Потрібне правило udev для USB-JTAG; в ESP-IDF воно є в комплекті і ставиться один раз. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-060 sha:ad5509dd src:manual/27-jtag.md:139 klas:E -->
### T-27-060 · proza · рядок 139

**Книга каже, дослівно:**

> **Драйвер (Windows).** Для USB-JTAG треба призначити правильний драйвер утилітою на кшталт Zadig; для FT2232 — драйвер FTDI. 4.

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

<!-- fc id:T-27-061 sha:a1a77bd9 src:manual/27-jtag.md:139 klas:F -->
### T-27-061 · proza · рядок 139

**Книга каже, дослівно:**

> **Піни JTAG зайняті проєктом** — див. попередження вище. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-062 sha:1ff00cfb src:manual/27-jtag.md:139 klas:A -->
### T-27-062 · proza · рядок 139

**Книга каже, дослівно:**

> **[[classic]] `GPIO12` заважає старту** — від'єднати адаптер, перевірити, що плата стартує без нього. 6.

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

<!-- fc id:T-27-063 sha:9f987218 src:manual/27-jtag.md:139 klas:A -->
### T-27-063 · proza · рядок 139

**Книга каже, дослівно:**

> **eFuse вимкнув JTAG.** `espefuse summary` (лише читання).

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

<!-- fc id:T-27-064 sha:bf544428 src:manual/27-jtag.md:139 klas:A -->
### T-27-064 · proza · рядок 139

**Книга каже, дослівно:**

> Якщо попередній власник спалив `JTAG_DISABLE` або ввімкнув Secure Boot — JTAG недоступний назавжди (розділ 20, картка [К11](#k-nikoly)).

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

<!-- fc id:T-27-065 sha:d2dd6389 src:manual/27-jtag.md:153 klas:F -->
### T-27-065 · proza · рядок 153

**Книга каже, дослівно:**

> Варто сказати прямо, бо це економить дні: більшість помилок у практиці вбудованої розробки не потребують JTAG.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-066 sha:bbfdfb29 src:manual/27-jtag.md:156 klas:E -->
### T-27-066 · proza · рядок 156

**Книга каже, дослівно:**

> Помилка живлення діагностується мультиметром (розділ 06).

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

<!-- fc id:T-27-067 sha:cb7d10d2 src:manual/27-jtag.md:156 klas:E -->
### T-27-067 · proza · рядок 156

**Книга каже, дослівно:**

> Помилка на шині — логічним аналізатором (розділ 28).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-068 sha:d5495804 src:manual/27-jtag.md:156 klas:F -->
### T-27-068 · proza · рядок 156

**Книга каже, дослівно:**

> Паніка — за backtrace і coredump (розділ 26).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-069 sha:2e8286d8 src:manual/27-jtag.md:156 klas:E -->
### T-27-069 · proza · рядок 156

**Книга каже, дослівно:**

> Логіка станів — логом переходів (розділ 25).

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Аналіз поведінки GPIO при старті мікроконтролера
- **Дослівно з джерела:**
  > При включенні платі:
  > 1. Мікроконтролер почне завантажуватися
  > 2. GPIO ще не налаштований (це відбувається під час ініціалізації ПЗ)
  > 3. Лінія GPIO знаходиться в невизначеному стані (паразитна ємність + шум)
  > 4. MOSFET затвор отримує невідомий рівень напруги
  > 
  > Результат: навантаження може вмкнутися на мілісекунди до того, як GPIO
  > буде налаштований в LOW.
- **Спосіб і дата:** Аналіз процесу завантаження мікроконтролера, документація ESP32, 2026-08-26
- **Нотатка:** Це видимість на реальні проблеми, якщо конструктор не розглядає етап ініціалізації.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-27-070 sha:52ec59e7 src:manual/27-jtag.md:160 klas:F -->
### T-27-070 · proza · рядок 160

**Книга каже, дослівно:**

> JTAG потрібен там, де всі чотири нічого не дали і треба подивитися всередину пам'яті.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-071 sha:eb17bd67 src:manual/27-jtag.md:160 klas:E -->
### T-27-071 · proza · рядок 160

**Книга каже, дослівно:**

> Це реальна, але не щоденна ситуація.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-27-072 sha:701cef28 src:manual/27-jtag.md:165 klas:A -->
### T-27-072 · proza · рядок 165

**Книга каже, дослівно:**

> На S3 і C3 повноцінний JTAG уже є в чипі й доступний тим самим кабелем — `idf.py openocd gdb`.

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

<!-- fc id:T-27-073 sha:81cbc7e9 src:manual/27-jtag.md:168 klas:A -->
### T-27-073 · proza · рядок 168

**Книга каже, дослівно:**

> На classic потрібен зовнішній адаптер, він займає чотири піни, два з яких — strapping, і `GPIO12` уміє не дати платі стартувати.

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

<!-- fc id:T-27-074 sha:0a72836e src:manual/27-jtag.md:171 klas:A -->
### T-27-074 · proza · рядок 171

**Книга каже, дослівно:**

> Зупинка на точці ламає реальний час: watchdog доведеться вимкнути, а таймінгові помилки шукати іншим інструментом.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > The purpose of a watchdog timer is to monitor the system's operation and automatically
  > recover from software or hardware faults by restarting the system if it becomes unresponsive.
- **Спосіб і дата:** curl esp-idf wdts.rst, grep -i "watchdog\|restart", 2026-08-26
- **Нотатка:** Текст розділу 32 обговорює автоматичне перезавантаження при зависанні. Джерело підтверджує, що watchdog перезавантажує систему.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-27-075 sha:6e5142c0 src:manual/27-jtag.md:174 klas:F -->
### T-27-075 · proza · рядок 174

**Книга каже, дослівно:**

> Більшість збоїв розбирається без JTAG узагалі.

**Доказ**

- **Клас:** F — не звірено

---
