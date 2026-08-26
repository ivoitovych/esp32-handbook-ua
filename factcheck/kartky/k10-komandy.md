# Фактчекінг: `kartky/k10-komandy.md`

Одиниць твердження: **52**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K10-001 sha:56ac242d src:kartky/k10-komandy.md:3 klas:F -->
### T-K10-001 · proza · рядок 3

**Книга каже, дослівно:**

> Синтаксис esptool **v5** (дефіси, без `.py`).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-002 sha:90dbd689 src:kartky/k10-komandy.md:3 klas:A -->
### T-K10-002 · proza · рядок 3

**Книга каже, дослівно:**

> Для v4 — підкреслення і суфікс `.py`: `esptool.py write_flash`.

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

<!-- fc id:T-K10-003 sha:6ac69acd src:kartky/k10-komandy.md:3 klas:A -->
### T-K10-003 · proza · рядок 3

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

<!-- fc id:T-K10-004 sha:eec2887d src:kartky/k10-komandy.md:8 klas:K -->
### T-K10-004 · kod · рядок 8

**Книга каже, дослівно:**

> ```
> # що за чип і ревізія — у шапці з'єднання перед будь-якою командою
> esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
> esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
> esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
> esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
> esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
>   0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
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

<!-- fc id:T-K10-005 sha:8af1928d src:kartky/k10-komandy.md:10 klas:A -->
### T-K10-005 · kod-ryadok · рядок 10

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу

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

<!-- fc id:T-K10-006 sha:74ec190c src:kartky/k10-komandy.md:11 klas:A -->
### T-K10-006 · kod-ryadok · рядок 11

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп

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

<!-- fc id:T-K10-007 sha:a177909e src:kartky/k10-komandy.md:12 klas:A -->
### T-K10-007 · kod-ryadok · рядок 12

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити

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

<!-- fc id:T-K10-008 sha:94bd45fa src:kartky/k10-komandy.md:13 klas:A -->
### T-K10-008 · kod-ryadok · рядок 13

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити

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

<!-- fc id:T-K10-009 sha:d6945e3a src:kartky/k10-komandy.md:14 klas:F -->
### T-K10-009 · kod-ryadok · рядок 14

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-010 sha:931ffa15 src:kartky/k10-komandy.md:15 klas:F -->
### T-K10-010 · kod-ryadok · рядок 15

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-011 sha:23a7fc4e src:kartky/k10-komandy.md:16 klas:A -->
### T-K10-011 · kod-ryadok · рядок 16

**Книга каже, дослівно:**

> esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \

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

<!-- fc id:T-K10-012 sha:0c80ad13 src:kartky/k10-komandy.md:17 klas:D -->
### T-K10-012 · schema-zvyazok · рядок 17

**Книга каже, дослівно:**

> 0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю

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

<!-- fc id:T-K10-013 sha:b9d2934d src:kartky/k10-komandy.md:22 klas:K -->
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
> idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
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

<!-- fc id:T-K10-014 sha:c4f6cb74 src:kartky/k10-komandy.md:23 klas:A -->
### T-K10-014 · kod-ryadok · рядок 23

**Книга каже, дослівно:**

> idf.py create-project my-project    # новий проєкт (назва латиницею)

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

<!-- fc id:T-K10-015 sha:bb9f7106 src:kartky/k10-komandy.md:24 klas:A -->
### T-K10-015 · kod-ryadok · рядок 24

**Книга каже, дослівно:**

> idf.py set-target esp32s3           # ⚠ стирає sdkconfig

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

<!-- fc id:T-K10-016 sha:cc032d7c src:kartky/k10-komandy.md:25 klas:A -->
### T-K10-016 · kod-ryadok · рядок 25

**Книга каже, дослівно:**

> idf.py menuconfig                   # налаштування

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

<!-- fc id:T-K10-021 sha:21c29912 src:kartky/k10-komandy.md:30 klas:A -->
### T-K10-021 · kod-ryadok · рядок 30

**Книга каже, дослівно:**

> idf.py fullclean                    # коли збирання поводиться незрозуміло

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

<!-- fc id:T-K10-022 sha:0f34d83d src:kartky/k10-komandy.md:31 klas:A -->
### T-K10-022 · kod-ryadok · рядок 31

**Книга каже, дослівно:**

> idf.py size                         # скільки зайнято флешу і RAM

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

<!-- fc id:T-K10-023 sha:48df8d47 src:kartky/k10-komandy.md:32 klas:A -->
### T-K10-023 · kod-ryadok · рядок 32

**Книга каже, дослівно:**

> idf.py coredump-info                # розбір coredump із флешу

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

<!-- fc id:T-K10-024 sha:a2ff386f src:kartky/k10-komandy.md:33 klas:A -->
### T-K10-024 · kod-ryadok · рядок 33

**Книга каже, дослівно:**

> idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту

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

<!-- fc id:T-K10-025 sha:0c9d449b src:kartky/k10-komandy.md:36 klas:A -->
### T-K10-025 · proza · рядок 36

**Книга каже, дослівно:**

> Є проєкт — `idf.py merge-bin` (адрес набирати не треба).

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

<!-- fc id:T-K10-026 sha:f5cb6136 src:kartky/k10-komandy.md:36 klas:A -->
### T-K10-026 · proza · рядок 36

**Книга каже, дослівно:**

> Є лише `.bin`-файли — `esptool --chip … merge-bin` з адресами вище.

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

<!-- fc id:T-K10-027 sha:c64c8733 src:kartky/k10-komandy.md:41 klas:A -->
### T-K10-027 · proza · рядок 41

**Книга каже, дослівно:**

> `idf.py monitor`: вийти — `Ctrl+]`.

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

<!-- fc id:T-K10-028 sha:51eec05c src:kartky/k10-komandy.md:41 klas:F -->
### T-K10-028 · proza · рядок 41

**Книга каже, дослівно:**

> Скинути плату — `Ctrl+T`, потім `Ctrl+R`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-029 sha:ab211d67 src:kartky/k10-komandy.md:43 klas:K -->
### T-K10-029 · kod · рядок 43

**Книга каже, дослівно:**

> ```
> minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
> screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
> picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-030 sha:746a4901 src:kartky/k10-komandy.md:44 klas:F -->
### T-K10-030 · kod-ryadok · рядок 44

**Книга каже, дослівно:**

> minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-031 sha:d4bff93f src:kartky/k10-komandy.md:45 klas:F -->
### T-K10-031 · kod-ryadok · рядок 45

**Книга каже, дослівно:**

> screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-032 sha:c8e23e02 src:kartky/k10-komandy.md:46 klas:F -->
### T-K10-032 · kod-ryadok · рядок 46

**Книга каже, дослівно:**

> picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-033 sha:c5afa127 src:kartky/k10-komandy.md:51 klas:K -->
### T-K10-033 · kod · рядок 51

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

<!-- fc id:T-K10-034 sha:805c4c57 src:kartky/k10-komandy.md:52 klas:F -->
### T-K10-034 · kod-ryadok · рядок 52

**Книга каже, дослівно:**

> ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-035 sha:65b20b9d src:kartky/k10-komandy.md:53 klas:F -->
### T-K10-035 · kod-ryadok · рядок 53

**Книга каже, дослівно:**

> dmesg | tail                     # що ядро побачило при під'єднанні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-036 sha:459deb70 src:kartky/k10-komandy.md:54 klas:F -->
### T-K10-036 · kod-ryadok · рядок 54

**Книга каже, дослівно:**

> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-037 sha:04c7f41f src:kartky/k10-komandy.md:55 klas:F -->
### T-K10-037 · kod-ryadok · рядок 55

**Книга каже, дослівно:**

> lsof /dev/ttyUSB0                # хто тримає порт

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-038 sha:4ffb7aee src:kartky/k10-komandy.md:58 klas:F -->
### T-K10-038 · proza · рядок 58

**Книга каже, дослівно:**

> `/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-039 sha:2130100e src:kartky/k10-komandy.md:58 klas:F -->
### T-K10-039 · proza · рядок 58

**Книга каже, дослівно:**

> `/dev/ttyACM*` — native USB [[S3]] [[C3]].

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-040 sha:3c153db1 src:kartky/k10-komandy.md:63 klas:F -->
### T-K10-040 · tablycya-shapka · рядок 63

**Книга каже, дослівно:**

> | Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-041 sha:03becf94 src:kartky/k10-komandy.md:64 klas:A -->
### T-K10-041 · komirka · рядок 64

**Книга каже, дослівно:**

> bootloader · classic, S2 → `0x1000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-042 sha:1fe1e089 src:kartky/k10-komandy.md:64 klas:F -->
### T-K10-042 · komirka · рядок 64

**Книга каже, дослівно:**

> bootloader · S3, C3, C6, H2 → `0x0`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K10-043 sha:ddb10a79 src:kartky/k10-komandy.md:64 klas:A -->
### T-K10-043 · komirka · рядок 64

**Книга каже, дослівно:**

> bootloader · P4, C5, H4 → `0x2000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-044 sha:4e987ef9 src:kartky/k10-komandy.md:65 klas:A -->
### T-K10-044 · komirka · рядок 65

**Книга каже, дослівно:**

> partition table · classic, S2 → `0x8000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-045 sha:8c7b7a5f src:kartky/k10-komandy.md:65 klas:A -->
### T-K10-045 · komirka · рядок 65

**Книга каже, дослівно:**

> partition table · S3, C3, C6, H2 → `0x8000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-046 sha:cb052eb6 src:kartky/k10-komandy.md:65 klas:A -->
### T-K10-046 · komirka · рядок 65

**Книга каже, дослівно:**

> partition table · P4, C5, H4 → `0x8000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-047 sha:55b5b58b src:kartky/k10-komandy.md:66 klas:A -->
### T-K10-047 · komirka · рядок 66

**Книга каже, дослівно:**

> застосунок · classic, S2 → `0x10000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-048 sha:55a122c0 src:kartky/k10-komandy.md:66 klas:A -->
### T-K10-048 · komirka · рядок 66

**Книга каже, дослівно:**

> застосунок · S3, C3, C6, H2 → `0x10000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-049 sha:eb3f0062 src:kartky/k10-komandy.md:66 klas:A -->
### T-K10-049 · komirka · рядок 66

**Книга каже, дослівно:**

> застосунок · P4, C5, H4 → `0x10000`

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
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 24), 2026-08-26
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arytmetyka.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-050 sha:ceaada41 src:kartky/k10-komandy.md:67 klas:A -->
### T-K10-050 · komirka · рядок 67

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

<!-- fc id:T-K10-051 sha:9feefdcc src:kartky/k10-komandy.md:67 klas:A -->
### T-K10-051 · komirka · рядок 67

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

<!-- fc id:T-K10-052 sha:c94bfb00 src:kartky/k10-komandy.md:67 klas:A -->
### T-K10-052 · komirka · рядок 67

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
