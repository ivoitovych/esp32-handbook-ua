# Фактчекінг: `dodatky/c-komandy.md`

Одиниць твердження: **129**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-C-001 sha:76d16ded src:dodatky/c-komandy.md:3 klas:D -->
### T-C-001 · proza · рядок 3

**Книга каже, дослівно:**

> Розгорнута версія картки [К10](#k-komandy).

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/posylannya.py — перевірка проти дерева файлів репозиторію
- **Дослівно з джерела:**
  > posylannya: згадок 689, адресатів 79, помилок 0
  > 
  > Перевірено:
  >   «розділ NN»  → існує manual/NN-*.md, і це не той самий розділ
  >   «картка КN»  → існує kartky/kNN-*.md
  >   «додаток X»  → існує dodatky/x-*.md (з переведенням кириличної
  >                  букви в латинську назву файлу)
- **Спосіб і дата:** python3 tools/posylannya.py, 2026-08-26
- **Нотатка:** Нуль помилок із 689 згадок. Це другий вимір після арифметики й API, де прохід не дав жодного виправлення.
Клас `D`, а не `A`: зовнішнє джерело тут не потрібне й не буває — перевіряється твердження книги про саму себе, і перевіряється механічно.
Головне тут не результат, а те, що перевірка тепер постійна: `tools/posylannya.py` стоїть у `make check`. Досі номер розділу можна було зсунути, і жоден інструмент цього б не помітив — текст лишається зв'язним, а читач іде не туди.
Одне самопосилання цей інструмент уже спіймав раніше, у проході 9 (розділ 17 відсилав сам на себе); тоді його знайшов `review.py` на клікабельному посиланні. Тепер такий самий контроль поширено на прозу.
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-C-002 sha:5afd5f63 src:dodatky/c-komandy.md:5 klas:A -->
### T-C-002 · proza · рядок 5

**Книга каже, дослівно:**

> **Синтаксис esptool v5** (дефіси, без `.py`).

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-C-003 sha:644789be src:dodatky/c-komandy.md:5 klas:F -->
### T-C-003 · proza · рядок 5

**Книга каже, дослівно:**

> Для v4 — підкреслення і суфікс `.py`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-004 sha:6ac69acd src:dodatky/c-komandy.md:5 klas:A -->
### T-C-004 · proza · рядок 5

**Книга каже, дослівно:**

> Перевірити своє: `esptool version`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst та .../docs/en/migration-guide.rst; перелік команд у esptool/__init__.py
- **Дослівно з джерела:**
  > (перехід на v5)
  > The `esptool.py` name is kept as an alias; the recommended entry point
  > is `esptool`. Command names use dashes: `write-flash`, `read-flash`,
  > `erase-flash`, `merge-bin`. The underscore forms are deprecated and
  > print a warning.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, проходи 9 і 15), 2026-08-26
- **Нотатка:** Не нова звірка. Іменування перевірено в проході 9, несиметричність міграції — у проході 6 (і записана в реєстр спростованого). Тут лише розширено досяжність на прозу й таблиці: «Перевірити своє: `esptool version`» у картках К5, К10 і додатку C, рядки таблиці «виклик · v4 / v5», а також попередження, що в v4 імені `esptool` без `.py` немає.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-C-005 sha:b9d7b8df src:dodatky/c-komandy.md:12 klas:K -->
### T-C-005 · kod · рядок 12

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 chip-id          # сімейство, ревізія, MAC
> esptool --port /dev/ttyUSB0 flash-id         # виробник і обсяг флешу
> esptool --port /dev/ttyUSB0 read-mac
> esptool version
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

<!-- fc id:T-C-006 sha:b1a7ffe5 src:dodatky/c-komandy.md:13 klas:A -->
### T-C-006 · kod-ryadok · рядок 13

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 chip-id          # сімейство, ревізія, MAC

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

<!-- fc id:T-C-007 sha:39838a17 src:dodatky/c-komandy.md:14 klas:A -->
### T-C-007 · kod-ryadok · рядок 14

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 flash-id         # виробник і обсяг флешу

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

<!-- fc id:T-C-010 sha:881f86c6 src:dodatky/c-komandy.md:21 klas:K -->
### T-C-010 · kod · рядок 21

**Книга каже, дослівно:**

> ```
> esptool --port PORT read-flash 0 ALL dump.bin           # повний дамп
> esptool --port PORT read-flash 0 0x400000 dump.bin      # 4 МБ явно
> esptool --port PORT read-flash 0x9000 0x6000 nvs.bin    # лише NVS
> esptool --port PORT read-flash 0x8000 0x1000 pt.bin     # таблиця розділів
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > The read-flash command allows reading back the contents of flash. The arguments to the
  > command are an address, a size, and a file path to output to. For example, to read a full
  > 2MB of attached flash:
  > 
  >     esptool -p PORT -b 460800 read-flash 0 0x200000 flash_contents.bin
  > 
  > Size can be specified in bytes, or with suffixes like ``k`` and ``M``. So ``0x200000`` in
  > example can be replaced with ``2M``.
  > 
  > It is also possible to autodetect flash size by using ``ALL`` as size.
  > 
  >     esptool -p PORT -b 460800 read-flash 0 ALL flash_contents.bin
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і саму команду знімання дампа (картка К2, розділи 17, 20, 22), і запасний варіант із явним обсягом, який книга радить, коли `ALL` не підтримується. Заразом видно те, чого книга не згадує й що варте наступного проходу: розмір приймає суфікси `k` і `M`, тобто `4M` замість `0x400000`.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-C-011 sha:bb087e09 src:dodatky/c-komandy.md:22 klas:A -->
### T-C-011 · kod-ryadok · рядок 22

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0 ALL dump.bin           # повний дамп

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > The read-flash command allows reading back the contents of flash. The arguments to the
  > command are an address, a size, and a file path to output to. For example, to read a full
  > 2MB of attached flash:
  > 
  >     esptool -p PORT -b 460800 read-flash 0 0x200000 flash_contents.bin
  > 
  > Size can be specified in bytes, or with suffixes like ``k`` and ``M``. So ``0x200000`` in
  > example can be replaced with ``2M``.
  > 
  > It is also possible to autodetect flash size by using ``ALL`` as size.
  > 
  >     esptool -p PORT -b 460800 read-flash 0 ALL flash_contents.bin
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і саму команду знімання дампа (картка К2, розділи 17, 20, 22), і запасний варіант із явним обсягом, який книга радить, коли `ALL` не підтримується. Заразом видно те, чого книга не згадує й що варте наступного проходу: розмір приймає суфікси `k` і `M`, тобто `4M` замість `0x400000`.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-C-012 sha:df2bf3b7 src:dodatky/c-komandy.md:23 klas:D -->
### T-C-012 · kod-ryadok · рядок 23

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0 0x400000 dump.bin      # 4 МБ явно

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py — перерахунок при кожній перевірці
- **Дослівно з джерела:**
  > 0x400000  / 1024 / 1024 =  4 МБ
  > 0x800000  / 1024 / 1024 =  8 МБ
  > 0x1000000 / 1024 / 1024 = 16 МБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Книга друкує ці три числа в розділі 17, додатку C і на картці К2 як явну заміну для `ALL`. Зовнішнього джерела тут не потрібно — це перерахунок, і він тепер постійний: змінене число завалить `make arytmetyka`.
Практична вага більша, ніж здається. `read-flash 0 0x400000` на восьмимегабайтному чипі дає рівно половину дампа, і файл при цьому цілком «правильного» вигляду. Книга тому й вимагає звіряти розмір файлу з обсягом флешу — тепер обидва числа перевірені.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-C-013 sha:4353e19f src:dodatky/c-komandy.md:24 klas:D -->
### T-C-013 · kod-ryadok · рядок 24

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0x9000 0x6000 nvs.bin    # лише NVS

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

<!-- fc id:T-C-014 sha:88b7dfd4 src:dodatky/c-komandy.md:25 klas:D -->
### T-C-014 · kod-ryadok · рядок 25

**Книга каже, дослівно:**

> esptool --port PORT read-flash 0x8000 0x1000 pt.bin     # таблиця розділів

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

<!-- fc id:T-C-015 sha:75b577e4 src:dodatky/c-komandy.md:28 klas:E -->
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

<!-- fc id:T-C-017 sha:fcd6b026 src:dodatky/c-komandy.md:33 klas:K -->
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

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-C-018 sha:3f0f4284 src:dodatky/c-komandy.md:34 klas:A -->
### T-C-018 · kod-ryadok · рядок 34

**Книга каже, дослівно:**

> esptool --port PORT --baud 460800 write-flash -z \

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-C-019 sha:c6c4971b src:dodatky/c-komandy.md:37 klas:A -->
### T-C-019 · kod-ryadok · рядок 37

**Книга каже, дослівно:**

> esptool --port PORT write-flash 0x0 merged.bin          # зібраний образ

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-C-020 sha:efde820e src:dodatky/c-komandy.md:38 klas:A -->
### T-C-020 · kod-ryadok · рядок 38

**Книга каже, дослівно:**

> esptool --port PORT verify-flash 0x10000 app.bin        # звірити

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

<!-- fc id:T-C-021 sha:00142e5e src:dodatky/c-komandy.md:43 klas:K -->
### T-C-021 · kod · рядок 43

**Книга каже, дослівно:**

> ```
> esptool --port PORT erase-flash                  # ⛔ усе, спершу дамп
> esptool --port PORT erase-region 0x9000 0x6000   # лише NVS
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

<!-- fc id:T-C-022 sha:2dca50d4 src:dodatky/c-komandy.md:44 klas:F -->
### T-C-022 · kod-ryadok · рядок 44

**Книга каже, дослівно:**

> esptool --port PORT erase-flash                  # ⛔ усе, спершу дамп

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-023 sha:9802b297 src:dodatky/c-komandy.md:45 klas:A -->
### T-C-023 · kod-ryadok · рядок 45

**Книга каже, дослівно:**

> esptool --port PORT erase-region 0x9000 0x6000   # лише NVS

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

<!-- fc id:T-C-024 sha:56d01430 src:dodatky/c-komandy.md:50 klas:K -->
### T-C-024 · kod · рядок 50

**Книга каже, дослівно:**

> ```
> esptool --chip esp32 merge-bin -o vyrib.bin --flash-mode dio --flash-size 4MB \
>   0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 app.bin
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-options.rst)
  > * Binary image generation commands, such as elf2image or merge-bin,
  >   require the chip type to be specified.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Найгрубша знахідка за дев'ять проходів, і саме тому, що стосується не рідкісного випадку, а головної команди розділу 21. `merge-bin` — це те, чим книга радить робити серійну прошивку; надрукована команда падає на першому ж запуску з `Specify the --chip argument`.
Причина механічна: решта команд esptool працює через порт і визначає чип сама, а `merge-bin` складає файл офлайн — визначати нема звідки. Перевірено не за документацією, а за самим розбором аргументів.
Виправлено в п'яти місцях: розділи 17 і 21, додаток C, картки К10 і К15. Заразом `--chip esp32` тепер стоїть в одному рядку з адресою `0x1000`, і зв'язок «цей чип — ця адреса» став видимим замість приміток збоку.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-025 sha:ccf461f5 src:dodatky/c-komandy.md:51 klas:A -->
### T-C-025 · kod-ryadok · рядок 51

**Книга каже, дослівно:**

> esptool --chip esp32 merge-bin -o vyrib.bin --flash-mode dio --flash-size 4MB \

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-options.rst)
  > * Binary image generation commands, such as elf2image or merge-bin,
  >   require the chip type to be specified.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Найгрубша знахідка за дев'ять проходів, і саме тому, що стосується не рідкісного випадку, а головної команди розділу 21. `merge-bin` — це те, чим книга радить робити серійну прошивку; надрукована команда падає на першому ж запуску з `Specify the --chip argument`.
Причина механічна: решта команд esptool працює через порт і визначає чип сама, а `merge-bin` складає файл офлайн — визначати нема звідки. Перевірено не за документацією, а за самим розбором аргументів.
Виправлено в п'яти місцях: розділи 17 і 21, додаток C, картки К10 і К15. Заразом `--chip esp32` тепер стоїть в одному рядку з адресою `0x1000`, і зв'язок «цей чип — ця адреса» став видимим замість приміток збоку.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-026 sha:4b3d6fe1 src:dodatky/c-komandy.md:55 klas:A -->
### T-C-026 · proza · рядок 55

**Книга каже, дослівно:**

> `--chip` тут **обов'язковий**: порту немає, автовизначенню нема звідки взятися.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-options.rst)
  > * Binary image generation commands, such as elf2image or merge-bin,
  >   require the chip type to be specified.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Найгрубша знахідка за дев'ять проходів, і саме тому, що стосується не рідкісного випадку, а головної команди розділу 21. `merge-bin` — це те, чим книга радить робити серійну прошивку; надрукована команда падає на першому ж запуску з `Specify the --chip argument`.
Причина механічна: решта команд esptool працює через порт і визначає чип сама, а `merge-bin` складає файл офлайн — визначати нема звідки. Перевірено не за документацією, а за самим розбором аргументів.
Виправлено в п'яти місцях: розділи 17 і 21, додаток C, картки К10 і К15. Заразом `--chip esp32` тепер стоїть в одному рядку з адресою `0x1000`, і зв'язок «цей чип — ця адреса» став видимим замість приміток збоку.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-027 sha:2ca78c71 src:dodatky/c-komandy.md:55 klas:A -->
### T-C-027 · proza · рядок 55

**Книга каже, дослівно:**

> Без нього esptool одразу відповідає `Specify the --chip argument`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-options.rst)
  > * Binary image generation commands, such as elf2image or merge-bin,
  >   require the chip type to be specified.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Найгрубша знахідка за дев'ять проходів, і саме тому, що стосується не рідкісного випадку, а головної команди розділу 21. `merge-bin` — це те, чим книга радить робити серійну прошивку; надрукована команда падає на першому ж запуску з `Specify the --chip argument`.
Причина механічна: решта команд esptool працює через порт і визначає чип сама, а `merge-bin` складає файл офлайн — визначати нема звідки. Перевірено не за документацією, а за самим розбором аргументів.
Виправлено в п'яти місцях: розділи 17 і 21, додаток C, картки К10 і К15. Заразом `--chip esp32` тепер стоїть в одному рядку з адресою `0x1000`, і зв'язок «цей чип — ця адреса» став видимим замість приміток збоку.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-028 sha:1bd7ba52 src:dodatky/c-komandy.md:55 klas:E -->
### T-C-028 · proza · рядок 55

**Книга каже, дослівно:**

> Значення має збігатися з чипом, під який зібрано прошивку, — і з адресою бутлоадера з таблиці нижче.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-029 sha:36969ccb src:dodatky/c-komandy.md:62 klas:E -->
### T-C-029 · tablycya · рядок 62

**Книга каже, дослівно:**

> | Прапорець | Навіщо |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-030 sha:1d6f7adf src:dodatky/c-komandy.md:64 klas:F -->
### T-C-030 · tablycya · рядок 64

**Книга каже, дослівно:**

> | `--baud 115200` | коли обривається на високій швидкості |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-031 sha:4fb5cfd6 src:dodatky/c-komandy.md:65 klas:A -->
### T-C-031 · tablycya · рядок 65

**Книга каже, дослівно:**

> | `-z` | стиснення при передачі. **Уже ввімкнене** — крім `--no-stub` |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > @click.option(
  >     "--compress",
  >     "-z",
  >     is_flag=True,
  >     help="Compress data during transfer (default unless --no-stub is specified).",
  > )
  > @click.option(
  >     "--no-compress",
  >     "-u",
  >     is_flag=True,
  >     help="Disable data compression during transfer (default if --no-stub is specified)",
  > )
  > 
  > (basic-commands.rst)
  > By default, the serial transfer data is compressed for better performance.
  > The ``-u/--no-compress`` option disables this behaviour.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Книга подавала `-z` як прапорець, що додається заради швидкості («швидше й надійніше»). Насправді стиснення й так увімкнене, і в звичайній команді `-z` не змінює нічого.
Сенс він має рівно в одному випадку — разом із `--no-stub`, де стиснення типово вимкнене. А це саме той випадок, який книга розбирає окремо (клони, що не приймають stub), тож уточнення не академічне.
Те саме стосується `--before default-reset --after hard-reset`: книга подавала їх як «керування скиданням», а це значення за замовчуванням. Таблицю прапорців замінено на ту, де перелічені значення, що справді щось міняють.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-032 sha:fd864248 src:dodatky/c-komandy.md:66 klas:A -->
### T-C-032 · tablycya · рядок 66

**Книга каже, дослівно:**

> | `-u` | вимкнути стиснення |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > @click.option(
  >     "--compress",
  >     "-z",
  >     is_flag=True,
  >     help="Compress data during transfer (default unless --no-stub is specified).",
  > )
  > @click.option(
  >     "--no-compress",
  >     "-u",
  >     is_flag=True,
  >     help="Disable data compression during transfer (default if --no-stub is specified)",
  > )
  > 
  > (basic-commands.rst)
  > By default, the serial transfer data is compressed for better performance.
  > The ``-u/--no-compress`` option disables this behaviour.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Книга подавала `-z` як прапорець, що додається заради швидкості («швидше й надійніше»). Насправді стиснення й так увімкнене, і в звичайній команді `-z` не змінює нічого.
Сенс він має рівно в одному випадку — разом із `--no-stub`, де стиснення типово вимкнене. А це саме той випадок, який книга розбирає окремо (клони, що не приймають stub), тож уточнення не академічне.
Те саме стосується `--before default-reset --after hard-reset`: книга подавала їх як «керування скиданням», а це значення за замовчуванням. Таблицю прапорців замінено на ту, де перелічені значення, що справді щось міняють.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-033 sha:602ee8fd src:dodatky/c-komandy.md:67 klas:F -->
### T-C-033 · tablycya · рядок 67

**Книга каже, дослівно:**

> | `--no-stub` | коли клон не приймає допоміжну програму |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-034 sha:d2f41919 src:dodatky/c-komandy.md:68 klas:F -->
### T-C-034 · tablycya · рядок 68

**Книга каже, дослівно:**

> | `--before no-reset` | коли на платі немає DTR/RTS і скидання робиться рукою |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-035 sha:4528aa3a src:dodatky/c-komandy.md:69 klas:F -->
### T-C-035 · tablycya · рядок 69

**Книга каже, дослівно:**

> | `--after no-reset` | лишити чип у завантажувачі: кілька команд поспіль |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-036 sha:83305673 src:dodatky/c-komandy.md:70 klas:A -->
### T-C-036 · tablycya · рядок 70

**Книга каже, дослівно:**

> | `--after watchdog-reset` | [[S3]] [[C3]] застряг у download mode через native USB |

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/advanced-options.rst
- **Дослівно з джерела:**
  > :not esp8266 and not esp32 and not esp32h2 and not esp32c6 and not esp32h4
  >  and not esp32e22: * ``--after watchdog-reset`` hard-resets the chip by
  >  triggering an internal watchdog reset. This is useful when the RTS control
  >  line is not available, especially in the USB-OTG and USB-Serial/JTAG modes.
  >  Use this if a chip is getting stuck in download mode when using the default
  >  reset method in USB-Serial/JTAG mode. Using this may cause the port to
  >  re-enumerate on Linux (e.g. ``/dev/ttyACM0`` -> ``/dev/ttyACM1``).
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення до переліку типових помилок розділу 17. Симптом «прошилося, а застосунок не стартував, чип сидить у завантажувачі» книга не розбирала, хоча на платах S3 і C3 із native USB він звичайний: лінії `RTS` фізично немає.
Умова застосовності взята з самої директиви, а не вгадана: режим є на S2, S3, C3, P4, C5 і новіших, і його немає на classic, C6 та H2 — саме так і записано в книзі. Побічний ефект із перелічуванням порту теж названо, бо без нього читач вирішить, що плата зникла.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-037 sha:8e5b5b76 src:dodatky/c-komandy.md:71 klas:F -->
### T-C-037 · tablycya · рядок 71

**Книга каже, дослівно:**

> | `--chip esp32s3` | коли автовизначення заважає |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-038 sha:544b21a9 src:dodatky/c-komandy.md:73 klas:A -->
### T-C-038 · proza · рядок 73

**Книга каже, дослівно:**

> Про `-z` варто знати точно: стиснення ввімкнене **за замовчуванням**, тож у звичайній команді цей прапорець нічого не змінює.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > @click.option(
  >     "--compress",
  >     "-z",
  >     is_flag=True,
  >     help="Compress data during transfer (default unless --no-stub is specified).",
  > )
  > @click.option(
  >     "--no-compress",
  >     "-u",
  >     is_flag=True,
  >     help="Disable data compression during transfer (default if --no-stub is specified)",
  > )
  > 
  > (basic-commands.rst)
  > By default, the serial transfer data is compressed for better performance.
  > The ``-u/--no-compress`` option disables this behaviour.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Книга подавала `-z` як прапорець, що додається заради швидкості («швидше й надійніше»). Насправді стиснення й так увімкнене, і в звичайній команді `-z` не змінює нічого.
Сенс він має рівно в одному випадку — разом із `--no-stub`, де стиснення типово вимкнене. А це саме той випадок, який книга розбирає окремо (клони, що не приймають stub), тож уточнення не академічне.
Те саме стосується `--before default-reset --after hard-reset`: книга подавала їх як «керування скиданням», а це значення за замовчуванням. Таблицю прапорців замінено на ту, де перелічені значення, що справді щось міняють.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-039 sha:3fe48028 src:dodatky/c-komandy.md:73 klas:F -->
### T-C-039 · proza · рядок 73

**Книга каже, дослівно:**

> Сенс він має рівно в одному випадку — разом із `--no-stub`, де стиснення типово вимкнене.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-040 sha:119466dc src:dodatky/c-komandy.md:78 klas:F -->
### T-C-040 · proza · рядок 78

**Книга каже, дослівно:**

> `--before default-reset` і `--after hard-reset` — теж значення за замовчуванням; писати їх, щоб «керувати скиданням», сенсу немає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-041 sha:e708ae5d src:dodatky/c-komandy.md:78 klas:E -->
### T-C-041 · proza · рядок 78

**Книга каже, дослівно:**

> Корисні саме інші значення, наведені в таблиці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-042 sha:dbb08ae1 src:dodatky/c-komandy.md:85 klas:F -->
### T-C-042 · proza · рядок 85

**Книга каже, дослівно:**

> `burn-*` пропалює біти **фізично й назавжди** (розділ 20).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-043 sha:d25d8e19 src:dodatky/c-komandy.md:89 klas:K -->
### T-C-043 · kod · рядок 89

**Книга каже, дослівно:**

> ```
> espefuse --port PORT summary        # безпечно: подивитися стан
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

<!-- fc id:T-C-044 sha:cdc968e6 src:dodatky/c-komandy.md:90 klas:A -->
### T-C-044 · kod-ryadok · рядок 90

**Книга каже, дослівно:**

> espefuse --port PORT summary        # безпечно: подивитися стан

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

<!-- fc id:T-C-045 sha:d06f73ae src:dodatky/c-komandy.md:97 klas:K -->
### T-C-045 · kod · рядок 97

**Книга каже, дослівно:**

> ```
> idf.py create-project imya
> idf.py create-component imya
> idf.py set-target esp32s3       # ⚠ стирає sdkconfig
> idf.py menuconfig               # пошук усередині — клавіша /
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

<!-- fc id:T-C-046 sha:3e0a67c9 src:dodatky/c-komandy.md:98 klas:A -->
### T-C-046 · kod-ryadok · рядок 98

**Книга каже, дослівно:**

> idf.py create-project imya

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

<!-- fc id:T-C-047 sha:c06327b4 src:dodatky/c-komandy.md:99 klas:A -->
### T-C-047 · kod-ryadok · рядок 99

**Книга каже, дослівно:**

> idf.py create-component imya

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

<!-- fc id:T-C-048 sha:bb9f7106 src:dodatky/c-komandy.md:100 klas:A -->
### T-C-048 · kod-ryadok · рядок 100

**Книга каже, дослівно:**

> idf.py set-target esp32s3       # ⚠ стирає sdkconfig

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

<!-- fc id:T-C-049 sha:93619e04 src:dodatky/c-komandy.md:101 klas:A -->
### T-C-049 · kod-ryadok · рядок 101

**Книга каже, дослівно:**

> idf.py menuconfig               # пошук усередині — клавіша /

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

<!-- fc id:T-C-050 sha:4f12da8e src:dodatky/c-komandy.md:106 klas:K -->
### T-C-050 · kod · рядок 106

**Книга каже, дослівно:**

> ```
> idf.py build
> idf.py -p /dev/ttyUSB0 flash
> idf.py -p /dev/ttyUSB0 monitor          # вихід Ctrl+]
> idf.py -p /dev/ttyUSB0 flash monitor    # найчастіша команда
> idf.py -p /dev/ttyUSB0 app-flash        # лише застосунок, швидше
> idf.py fullclean                        # коли збирання поводиться дивно
> idf.py merge-bin -o vyrib.bin           # один образ; адреси — з конфігурації
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > The command ``idf.py merge-bin`` will merge the bootloader, partition table,
  > the application itself, and other partitions (if there are any) according to
  > the project configuration and create a single binary file
  > ``merged-binary.[bin|hex]`` in the build folder, which can then be flashed later.
  > 
  > Example usage:
  >   idf.py merge-bin -o my-merged-binary.bin -f raw
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, яке прибирає цілий клас помилок. Книга вчила лише `esptool merge-bin` із адресами, набраними вручну, — і сама ж на сусідній сторінці попереджає, що `0x1000` на S3 дає образ, який прошивається без скарг і не стартує.
`idf.py merge-bin` цієї можливості не лишає: адреса бутлоадера, чип, режим і частота флешу беруться з конфігурації того самого проєкту. Правило, додане в книгу: є проєкт — `idf.py merge-bin`; є лише `.bin`-файли — `esptool --chip … merge-bin`.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-051 sha:343d9bab src:dodatky/c-komandy.md:107 klas:F -->
### T-C-051 · kod-ryadok · рядок 107

**Книга каже, дослівно:**

> idf.py build

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-052 sha:aaa1cf80 src:dodatky/c-komandy.md:108 klas:F -->
### T-C-052 · kod-ryadok · рядок 108

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-053 sha:770cf8b9 src:dodatky/c-komandy.md:109 klas:F -->
### T-C-053 · kod-ryadok · рядок 109

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 monitor          # вихід Ctrl+]

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-054 sha:7879c453 src:dodatky/c-komandy.md:110 klas:F -->
### T-C-054 · kod-ryadok · рядок 110

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash monitor    # найчастіша команда

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-055 sha:5410fc3a src:dodatky/c-komandy.md:111 klas:A -->
### T-C-055 · kod-ryadok · рядок 111

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 app-flash        # лише застосунок, швидше

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

<!-- fc id:T-C-056 sha:345eb1d8 src:dodatky/c-komandy.md:112 klas:A -->
### T-C-056 · kod-ryadok · рядок 112

**Книга каже, дослівно:**

> idf.py fullclean                        # коли збирання поводиться дивно

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

<!-- fc id:T-C-057 sha:42aea75b src:dodatky/c-komandy.md:113 klas:A -->
### T-C-057 · kod-ryadok · рядок 113

**Книга каже, дослівно:**

> idf.py merge-bin -o vyrib.bin           # один образ; адреси — з конфігурації

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > The command ``idf.py merge-bin`` will merge the bootloader, partition table,
  > the application itself, and other partitions (if there are any) according to
  > the project configuration and create a single binary file
  > ``merged-binary.[bin|hex]`` in the build folder, which can then be flashed later.
  > 
  > Example usage:
  >   idf.py merge-bin -o my-merged-binary.bin -f raw
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, яке прибирає цілий клас помилок. Книга вчила лише `esptool merge-bin` із адресами, набраними вручну, — і сама ж на сусідній сторінці попереджає, що `0x1000` на S3 дає образ, який прошивається без скарг і не стартує.
`idf.py merge-bin` цієї можливості не лишає: адреса бутлоадера, чип, режим і частота флешу беруться з конфігурації того самого проєкту. Правило, додане в книгу: є проєкт — `idf.py merge-bin`; є лише `.bin`-файли — `esptool --chip … merge-bin`.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-058 sha:46891766 src:dodatky/c-komandy.md:116 klas:A -->
### T-C-058 · proza · рядок 116

**Книга каже, дослівно:**

> `idf.py merge-bin` кращий за `esptool merge-bin` завжди, коли проєкт під рукою: адресу бутлоадера, чип, режим і частоту флешу він бере з конфігурації, а не з набраного вручну рядка.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > The command ``idf.py merge-bin`` will merge the bootloader, partition table,
  > the application itself, and other partitions (if there are any) according to
  > the project configuration and create a single binary file
  > ``merged-binary.[bin|hex]`` in the build folder, which can then be flashed later.
  > 
  > Example usage:
  >   idf.py merge-bin -o my-merged-binary.bin -f raw
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, яке прибирає цілий клас помилок. Книга вчила лише `esptool merge-bin` із адресами, набраними вручну, — і сама ж на сусідній сторінці попереджає, що `0x1000` на S3 дає образ, який прошивається без скарг і не стартує.
`idf.py merge-bin` цієї можливості не лишає: адреса бутлоадера, чип, режим і частота флешу беруться з конфігурації того самого проєкту. Правило, додане в книгу: є проєкт — `idf.py merge-bin`; є лише `.bin`-файли — `esptool --chip … merge-bin`.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-059 sha:850fe94c src:dodatky/c-komandy.md:116 klas:A -->
### T-C-059 · proza · рядок 116

**Книга каже, дослівно:**

> Без `-o` результат — `build/merged-binary.bin`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > The command ``idf.py merge-bin`` will merge the bootloader, partition table,
  > the application itself, and other partitions (if there are any) according to
  > the project configuration and create a single binary file
  > ``merged-binary.[bin|hex]`` in the build folder, which can then be flashed later.
  > 
  > Example usage:
  >   idf.py merge-bin -o my-merged-binary.bin -f raw
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Доповнення, яке прибирає цілий клас помилок. Книга вчила лише `esptool merge-bin` із адресами, набраними вручну, — і сама ж на сусідній сторінці попереджає, що `0x1000` на S3 дає образ, який прошивається без скарг і не стартує.
`idf.py merge-bin` цієї можливості не лишає: адреса бутлоадера, чип, режим і частота флешу беруться з конфігурації того самого проєкту. Правило, додане в книгу: є проєкт — `idf.py merge-bin`; є лише `.bin`-файли — `esptool --chip … merge-bin`.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-C-060 sha:e06292bb src:dodatky/c-komandy.md:123 klas:K -->
### T-C-060 · kod · рядок 123

**Книга каже, дослівно:**

> ```
> idf.py size                 # скільки зайнято флешу і RAM
> idf.py size-components      # ХТО САМЕ займає — найкорисніша
> idf.py size-files
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

<!-- fc id:T-C-061 sha:0f34d83d src:dodatky/c-komandy.md:124 klas:A -->
### T-C-061 · kod-ryadok · рядок 124

**Книга каже, дослівно:**

> idf.py size                 # скільки зайнято флешу і RAM

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

<!-- fc id:T-C-062 sha:ab73f933 src:dodatky/c-komandy.md:125 klas:A -->
### T-C-062 · kod-ryadok · рядок 125

**Книга каже, дослівно:**

> idf.py size-components      # ХТО САМЕ займає — найкорисніша

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

<!-- fc id:T-C-063 sha:9136076f src:dodatky/c-komandy.md:126 klas:A -->
### T-C-063 · kod-ryadok · рядок 126

**Книга каже, дослівно:**

> idf.py size-files

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

<!-- fc id:T-C-064 sha:d3c38986 src:dodatky/c-komandy.md:131 klas:K -->
### T-C-064 · kod · рядок 131

**Книга каже, дослівно:**

> ```
> idf.py coredump-info        # розбір coredump із флешу
> idf.py coredump-debug       # GDB на збереженому стані
> idf.py openocd gdb          # покрокове налагодження (S3, C3)
> idf.py monitor              # з розшифровкою backtrace на льоту
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

<!-- fc id:T-C-065 sha:48df8d47 src:dodatky/c-komandy.md:132 klas:A -->
### T-C-065 · kod-ryadok · рядок 132

**Книга каже, дослівно:**

> idf.py coredump-info        # розбір coredump із флешу

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

<!-- fc id:T-C-066 sha:f88382bd src:dodatky/c-komandy.md:133 klas:A -->
### T-C-066 · kod-ryadok · рядок 133

**Книга каже, дослівно:**

> idf.py coredump-debug       # GDB на збереженому стані

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

<!-- fc id:T-C-067 sha:b89c04ed src:dodatky/c-komandy.md:134 klas:A -->
### T-C-067 · kod-ryadok · рядок 134

**Книга каже, дослівно:**

> idf.py openocd gdb          # покрокове налагодження (S3, C3)

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

<!-- fc id:T-C-068 sha:249fc25a src:dodatky/c-komandy.md:135 klas:F -->
### T-C-068 · kod-ryadok · рядок 135

**Книга каже, дослівно:**

> idf.py monitor              # з розшифровкою backtrace на льоту

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-069 sha:f027758e src:dodatky/c-komandy.md:140 klas:K -->
### T-C-069 · kod · рядок 140

**Книга каже, дослівно:**

> ```
> idf.py add-dependency "espressif/led_strip^3.0.3"
> idf.py reconfigure
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

<!-- fc id:T-C-070 sha:4f76e0f2 src:dodatky/c-komandy.md:141 klas:A -->
### T-C-070 · kod-ryadok · рядок 141

**Книга каже, дослівно:**

> idf.py add-dependency "espressif/led_strip^3.0.3"

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

<!-- fc id:T-C-071 sha:bd18c568 src:dodatky/c-komandy.md:142 klas:A -->
### T-C-071 · kod-ryadok · рядок 142

**Книга каже, дослівно:**

> idf.py reconfigure

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

<!-- fc id:T-C-072 sha:14ee9040 src:dodatky/c-komandy.md:147 klas:K -->
### T-C-072 · kod · рядок 147

**Книга каже, дослівно:**

> ```
> xtensa-esp32-elf-addr2line   -pfiaC -e build/app.elf 0x400d1234 0x400d5678
> xtensa-esp32s3-elf-addr2line -pfiaC -e build/app.elf 0x42001234
> riscv32-esp-elf-addr2line    -pfiaC -e build/app.elf 0x42001234
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-073 sha:5f267d8c src:dodatky/c-komandy.md:148 klas:F -->
### T-C-073 · kod-ryadok · рядок 148

**Книга каже, дослівно:**

> xtensa-esp32-elf-addr2line   -pfiaC -e build/app.elf 0x400d1234 0x400d5678

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-074 sha:f57b50fb src:dodatky/c-komandy.md:149 klas:F -->
### T-C-074 · kod-ryadok · рядок 149

**Книга каже, дослівно:**

> xtensa-esp32s3-elf-addr2line -pfiaC -e build/app.elf 0x42001234

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-075 sha:69e46646 src:dodatky/c-komandy.md:150 klas:F -->
### T-C-075 · kod-ryadok · рядок 150

**Книга каже, дослівно:**

> riscv32-esp-elf-addr2line    -pfiaC -e build/app.elf 0x42001234

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-076 sha:2a969ef0 src:dodatky/c-komandy.md:153 klas:F -->
### T-C-076 · proza · рядок 153

**Книга каже, дослівно:**

> `-i` обов'язковий: без нього inline-кадри зникають.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-077 sha:828c36b3 src:dodatky/c-komandy.md:157 klas:F -->
### T-C-077 · tablycya-shapka · рядок 157

**Книга каже, дослівно:**

> | Програма | Вихід | Особливість |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-078 sha:af9c4cd0 src:dodatky/c-komandy.md:158 klas:A -->
### T-C-078 · komirka · рядок 158

**Книга каже, дослівно:**

> `idf.py monitor` · Вихід → `Ctrl+]`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/tools/idf-monitor.rst
- **Дослівно з джерела:**
  > * - Ctrl + ]
  >   - Exit the program
  > * - Ctrl + T
  >   - Menu escape key
  >   - Press and follow it by one of the keys given below.
  > * - * Ctrl + R
  >   - Reset target board via RTS
  >   - Reset the target board and re-starts the application via the RTS
  >     line (if connected).
  > * - * Ctrl + P
  >   - Reset target into bootloader to pause app via RTS and DTR lines
  > 
  > If an ESP-IDF app crashes and panics, a register dump and backtrace
  > are produced… IDF Monitor … looks up each address in the ELF file.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Звірено дослівно, розбіжностей немає — включно з тонкістю, яку легко записати неправильно: `Ctrl+R` не самостійна комбінація, а **друга** клавіша після `Ctrl+T`. Книга пише саме «`Ctrl+T`, `Ctrl+R`», через кому, і це відповідає джерелу (`Ctrl+T` — menu escape key).
Підтверджено й твердження картки К7: монітор розшифровує backtrace автоматично, якщо запущений із каталогу того самого проєкту — у джерелі це прив'язка до `.elf` того збирання.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-C-079 sha:1b645088 src:dodatky/c-komandy.md:158 klas:A -->
### T-C-079 · komirka · рядок 158

**Книга каже, дослівно:**

> `idf.py monitor` · Особливість → розшифровує backtrace; скидання `Ctrl+T`, `Ctrl+R`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/tools/idf-monitor.rst
- **Дослівно з джерела:**
  > * - Ctrl + ]
  >   - Exit the program
  > * - Ctrl + T
  >   - Menu escape key
  >   - Press and follow it by one of the keys given below.
  > * - * Ctrl + R
  >   - Reset target board via RTS
  >   - Reset the target board and re-starts the application via the RTS
  >     line (if connected).
  > * - * Ctrl + P
  >   - Reset target into bootloader to pause app via RTS and DTR lines
  > 
  > If an ESP-IDF app crashes and panics, a register dump and backtrace
  > are produced… IDF Monitor … looks up each address in the ELF file.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Звірено дослівно, розбіжностей немає — включно з тонкістю, яку легко записати неправильно: `Ctrl+R` не самостійна комбінація, а **друга** клавіша після `Ctrl+T`. Книга пише саме «`Ctrl+T`, `Ctrl+R`», через кому, і це відповідає джерелу (`Ctrl+T` — menu escape key).
Підтверджено й твердження картки К7: монітор розшифровує backtrace автоматично, якщо запущений із каталогу того самого проєкту — у джерелі це прив'язка до `.elf` того збирання.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-C-080 sha:e7670044 src:dodatky/c-komandy.md:159 klas:F -->
### T-C-080 · komirka · рядок 159

**Книга каже, дослівно:**

> `picocom -b 115200 /dev/ttyUSB0` · Вихід → `Ctrl+A`, `Ctrl+X`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-081 sha:3e00cb93 src:dodatky/c-komandy.md:159 klas:F -->
### T-C-081 · komirka · рядок 159

**Книга каже, дослівно:**

> `picocom -b 115200 /dev/ttyUSB0` · Особливість → найпростіший

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-082 sha:b668a28a src:dodatky/c-komandy.md:160 klas:F -->
### T-C-082 · komirka · рядок 160

**Книга каже, дослівно:**

> `minicom -D /dev/ttyUSB0 -b 115200` · Вихід → `Ctrl+A`, `X`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-083 sha:00c75e9e src:dodatky/c-komandy.md:161 klas:F -->
### T-C-083 · komirka · рядок 161

**Книга каже, дослівно:**

> `screen /dev/ttyUSB0 115200` · Вихід → `Ctrl+A`, `K`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-084 sha:a33fb442 src:dodatky/c-komandy.md:161 klas:F -->
### T-C-084 · komirka · рядок 161

**Книга каже, дослівно:**

> `screen /dev/ttyUSB0 115200` · Особливість → є майже скрізь

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-085 sha:03ecbe4f src:dodatky/c-komandy.md:166 klas:K -->
### T-C-085 · kod · рядок 166

**Книга каже, дослівно:**

> ```
> picocom -b 115200 /dev/ttyUSB0 | tee log-2026-08-26.txt
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-086 sha:999b86b5 src:dodatky/c-komandy.md:167 klas:F -->
### T-C-086 · kod-ryadok · рядок 167

**Книга каже, дослівно:**

> picocom -b 115200 /dev/ttyUSB0 | tee log-2026-08-26.txt

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-087 sha:5bc221cd src:dodatky/c-komandy.md:172 klas:K -->
### T-C-087 · kod · рядок 172

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

<!-- fc id:T-C-088 sha:7140ef8e src:dodatky/c-komandy.md:173 klas:F -->
### T-C-088 · kod-ryadok · рядок 173

**Книга каже, дослівно:**

> ls /dev/ttyUSB* /dev/ttyACM*     # що є

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-089 sha:583a0a4a src:dodatky/c-komandy.md:174 klas:F -->
### T-C-089 · kod-ryadok · рядок 174

**Книга каже, дослівно:**

> ls -l /dev/serial/by-id/         # стабільні імена для скриптів

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-090 sha:88976550 src:dodatky/c-komandy.md:175 klas:F -->
### T-C-090 · kod-ryadok · рядок 175

**Книга каже, дослівно:**

> dmesg | tail -20                 # що ядро побачило

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-091 sha:04c7f41f src:dodatky/c-komandy.md:176 klas:F -->
### T-C-091 · kod-ryadok · рядок 176

**Книга каже, дослівно:**

> lsof /dev/ttyUSB0                # хто тримає порт

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-092 sha:459deb70 src:dodatky/c-komandy.md:177 klas:F -->
### T-C-092 · kod-ryadok · рядок 177

**Книга каже, дослівно:**

> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-093 sha:b97a16ef src:dodatky/c-komandy.md:180 klas:F -->
### T-C-093 · proza · рядок 180

**Книга каже, дослівно:**

> `/dev/ttyUSB*` — зовнішній міст.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-094 sha:2130100e src:dodatky/c-komandy.md:180 klas:F -->
### T-C-094 · proza · рядок 180

**Книга каже, дослівно:**

> `/dev/ttyACM*` — native USB [[S3]] [[C3]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-095 sha:f68e2f06 src:dodatky/c-komandy.md:184 klas:K -->
### T-C-095 · kod · рядок 184

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

<!-- fc id:T-C-096 sha:0b0001c2 src:dodatky/c-komandy.md:185 klas:F -->
### T-C-096 · kod-ryadok · рядок 185

**Книга каже, дослівно:**

> pio run                    # зібрати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-097 sha:307983fc src:dodatky/c-komandy.md:186 klas:F -->
### T-C-097 · kod-ryadok · рядок 186

**Книга каже, дослівно:**

> pio run -e s3              # конкретне середовище

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-098 sha:82ea1803 src:dodatky/c-komandy.md:187 klas:F -->
### T-C-098 · kod-ryadok · рядок 187

**Книга каже, дослівно:**

> pio run -t upload

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-099 sha:364802c1 src:dodatky/c-komandy.md:188 klas:F -->
### T-C-099 · kod-ryadok · рядок 188

**Книга каже, дослівно:**

> pio device monitor

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-100 sha:1a074688 src:dodatky/c-komandy.md:189 klas:F -->
### T-C-100 · kod-ryadok · рядок 189

**Книга каже, дослівно:**

> pio run -t clean

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-101 sha:a092446e src:dodatky/c-komandy.md:190 klas:F -->
### T-C-101 · kod-ryadok · рядок 190

**Книга каже, дослівно:**

> pio pkg update

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-102 sha:3c153db1 src:dodatky/c-komandy.md:195 klas:F -->
### T-C-102 · tablycya-shapka · рядок 195

**Книга каже, дослівно:**

> | Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-103 sha:03becf94 src:dodatky/c-komandy.md:196 klas:F -->
### T-C-103 · komirka · рядок 196

**Книга каже, дослівно:**

> bootloader · classic, S2 → `0x1000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-104 sha:1fe1e089 src:dodatky/c-komandy.md:196 klas:F -->
### T-C-104 · komirka · рядок 196

**Книга каже, дослівно:**

> bootloader · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-105 sha:ddb10a79 src:dodatky/c-komandy.md:196 klas:F -->
### T-C-105 · komirka · рядок 196

**Книга каже, дослівно:**

> bootloader · P4, C5, H4 → `0x2000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-106 sha:a6442276 src:dodatky/c-komandy.md:197 klas:A -->
### T-C-106 · komirka · рядок 197

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

<!-- fc id:T-C-107 sha:21c0d046 src:dodatky/c-komandy.md:197 klas:A -->
### T-C-107 · komirka · рядок 197

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

<!-- fc id:T-C-108 sha:59461729 src:dodatky/c-komandy.md:197 klas:A -->
### T-C-108 · komirka · рядок 197

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

<!-- fc id:T-C-109 sha:55b5b58b src:dodatky/c-komandy.md:198 klas:F -->
### T-C-109 · komirka · рядок 198

**Книга каже, дослівно:**

> застосунок · classic, S2 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-110 sha:55a122c0 src:dodatky/c-komandy.md:198 klas:F -->
### T-C-110 · komirka · рядок 198

**Книга каже, дослівно:**

> застосунок · S3, C3, C6, H2 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-111 sha:eb3f0062 src:dodatky/c-komandy.md:198 klas:F -->
### T-C-111 · komirka · рядок 198

**Книга каже, дослівно:**

> застосунок · P4, C5, H4 → `0x10000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-112 sha:96022a5e src:dodatky/c-komandy.md:199 klas:F -->
### T-C-112 · komirka · рядок 199

**Книга каже, дослівно:**

> `nvs` (типово) · classic, S2 → `0x9000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-113 sha:906f56bc src:dodatky/c-komandy.md:199 klas:F -->
### T-C-113 · komirka · рядок 199

**Книга каже, дослівно:**

> `nvs` (типово) · S3, C3, C6, H2 → `0x9000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-114 sha:5efc2dcb src:dodatky/c-komandy.md:199 klas:F -->
### T-C-114 · komirka · рядок 199

**Книга каже, дослівно:**

> `nvs` (типово) · P4, C5, H4 → `0x9000`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-115 sha:ceaada41 src:dodatky/c-komandy.md:200 klas:A -->
### T-C-115 · komirka · рядок 200

**Книга каже, дослівно:**

> зібраний `merge-bin` · classic, S2 → `0x0`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst (merge-bin) та .../esp-idf/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > The merge-bin command will merge multiple binary files (of any kind)
  > into a single file that can be flashed to a device later. Any gaps
  > between the input files are padded with 0xFF bytes (or 0x00 in
  > --format hex).
  > 
  > (idf-py.rst)
  > …create a single binary file ``merged-binary.[bin|hex]`` in the build
  > folder, which can then be flashed later.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Твердження книги випливає з механіки прямо: якщо злиття доповнює проміжки до суцільного образу від нуля, то зсуви вже всередині файлу, і прошивати його треба на `0x0` — на будь-якому чипі.
Саме тому три рядки таблиці «зібраний `merge-bin` · classic, S2 → `0x0`», «S3, C3, C6, H2 → `0x0`», «P4, C5, H4 → `0x0`» однакові, хоча сусідня таблиця для окремих файлів має три різні адреси. Ця пара таблиць — головне, що картка К10 і додаток C мусять донести, і тепер вона звірена в обох.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-C-116 sha:9feefdcc src:dodatky/c-komandy.md:200 klas:A -->
### T-C-116 · komirka · рядок 200

**Книга каже, дослівно:**

> зібраний `merge-bin` · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst (merge-bin) та .../esp-idf/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > The merge-bin command will merge multiple binary files (of any kind)
  > into a single file that can be flashed to a device later. Any gaps
  > between the input files are padded with 0xFF bytes (or 0x00 in
  > --format hex).
  > 
  > (idf-py.rst)
  > …create a single binary file ``merged-binary.[bin|hex]`` in the build
  > folder, which can then be flashed later.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Твердження книги випливає з механіки прямо: якщо злиття доповнює проміжки до суцільного образу від нуля, то зсуви вже всередині файлу, і прошивати його треба на `0x0` — на будь-якому чипі.
Саме тому три рядки таблиці «зібраний `merge-bin` · classic, S2 → `0x0`», «S3, C3, C6, H2 → `0x0`», «P4, C5, H4 → `0x0`» однакові, хоча сусідня таблиця для окремих файлів має три різні адреси. Ця пара таблиць — головне, що картка К10 і додаток C мусять донести, і тепер вона звірена в обох.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-C-117 sha:c94bfb00 src:dodatky/c-komandy.md:200 klas:A -->
### T-C-117 · komirka · рядок 200

**Книга каже, дослівно:**

> зібраний `merge-bin` · P4, C5, H4 → `0x0`

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst (merge-bin) та .../esp-idf/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > The merge-bin command will merge multiple binary files (of any kind)
  > into a single file that can be flashed to a device later. Any gaps
  > between the input files are padded with 0xFF bytes (or 0x00 in
  > --format hex).
  > 
  > (idf-py.rst)
  > …create a single binary file ``merged-binary.[bin|hex]`` in the build
  > folder, which can then be flashed later.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Твердження книги випливає з механіки прямо: якщо злиття доповнює проміжки до суцільного образу від нуля, то зсуви вже всередині файлу, і прошивати його треба на `0x0` — на будь-якому чипі.
Саме тому три рядки таблиці «зібраний `merge-bin` · classic, S2 → `0x0`», «S3, C3, C6, H2 → `0x0`», «P4, C5, H4 → `0x0`» однакові, хоча сусідня таблиця для окремих файлів має три різні адреси. Ця пара таблиць — головне, що картка К10 і додаток C мусять донести, і тепер вона звірена в обох.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-C-118 sha:9ab6d1e4 src:dodatky/c-komandy.md:203 klas:A -->
### T-C-118 · proza · рядок 203

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

<!-- fc id:T-C-119 sha:aa2e7ddd src:dodatky/c-komandy.md:203 klas:A -->
### T-C-119 · proza · рядок 203

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

<!-- fc id:T-C-120 sha:20c177db src:dodatky/c-komandy.md:210 klas:K -->
### T-C-120 · kod · рядок 210

**Книга каже, дослівно:**

> ```
> dd if=dump.bin of=pt.bin bs=1 skip=$((0x8000)) count=$((0x1000))
> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
> ```

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

<!-- fc id:T-C-121 sha:d1458242 src:dodatky/c-komandy.md:211 klas:D -->
### T-C-121 · kod-ryadok · рядок 211

**Книга каже, дослівно:**

> dd if=dump.bin of=pt.bin bs=1 skip=$((0x8000)) count=$((0x1000))

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

<!-- fc id:T-C-122 sha:4438754b src:dodatky/c-komandy.md:212 klas:F -->
### T-C-122 · kod-ryadok · рядок 212

**Книга каже, дослівно:**

> python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-123 sha:9fd4791b src:dodatky/c-komandy.md:217 klas:K -->
### T-C-123 · kod · рядок 217

**Книга каже, дослівно:**

> ```
> strings -n 6 dump.bin | less
> strings -n 6 dump.bin | grep -iE "v[0-9]+\.[0-9]+|20[0-9]{2}-"
> strings -n 6 dump.bin | grep -iE "http|mqtt|ssid|pass"
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-124 sha:3e391da0 src:dodatky/c-komandy.md:218 klas:F -->
### T-C-124 · kod-ryadok · рядок 218

**Книга каже, дослівно:**

> strings -n 6 dump.bin | less

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-125 sha:580bb88f src:dodatky/c-komandy.md:219 klas:F -->
### T-C-125 · kod-ryadok · рядок 219

**Книга каже, дослівно:**

> strings -n 6 dump.bin | grep -iE "v[0-9]+\.[0-9]+|20[0-9]{2}-"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-126 sha:f102892d src:dodatky/c-komandy.md:220 klas:F -->
### T-C-126 · kod-ryadok · рядок 220

**Книга каже, дослівно:**

> strings -n 6 dump.bin | grep -iE "http|mqtt|ssid|pass"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-C-127 sha:51bbff59 src:dodatky/c-komandy.md:227 klas:K -->
### T-C-127 · kod · рядок 227

**Книга каже, дослівно:**

> ```
> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
> esptool --port PORT write-flash 0x9000 nvs-0042.bin
> ```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---

<!-- fc id:T-C-128 sha:aa33e38e src:dodatky/c-komandy.md:228 klas:D -->
### T-C-128 · kod-ryadok · рядок 228

**Книга каже, дослівно:**

> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000

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

<!-- fc id:T-C-129 sha:8fc5b038 src:dodatky/c-komandy.md:229 klas:A -->
### T-C-129 · kod-ryadok · рядок 229

**Книга каже, дослівно:**

> esptool --port PORT write-flash 0x9000 nvs-0042.bin

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/migration-guide.rst
- **Дослівно з джерела:**
  > The preferred way to invoke esptool command-line tools has changed. Instead of running
  > the scripts with `.py` suffix, you should now use the console scripts without the `.py` suffix.
  > - ``esptool.py`` → ``esptool``
  > - ``espefuse.py`` → ``espefuse``
  > …
  > All the commands and options have been renamed to use ``-`` instead of ``_`` as a separator
  > (e.g., ``write_flash`` -> ``write-flash``).
  > 
  > Old command and option names are **deprecated**, meaning they will work for now with a
  > warning, but will be removed in the next major release.
  > 
  > This change affects most of the commands and the following options: ``--flash_size``,
  > ``--flash_mode``, ``--flash_freq``, ``--use_segments``.
  > …
  > 1. Replace all underscores in the ``--before`` and ``--after`` options with ``-`` in your scripts.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Знахідка проходу. Книга стверджувала, що команди v4 «дослівно на v5 не працюють, і навпаки» — симетрично. Насправді напрямки різні: старе ім'я на v5 **працює** з попередженням про застарілість, а нове ім'я на v4 не працює зовсім. Різниця практична: читач, який скопіював `write_flash` і побачив результат, вирішить, що все гаразд, — і зламається на наступному major-релізі. Виправлено в розділі 17, заразом додано те, чого бракувало: перейменування торкнулося й опцій (`--flash_size`, `--flash_mode`, `--flash_freq`) та значень `--before` і `--after`, які книга вже вживає в новій формі в додатку C.
- **Прохід:** pass-06-komandy-strapping

---
