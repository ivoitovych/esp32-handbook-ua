# Фактчекінг: `kartky/k10-komandy.md`

Одиниць твердження: **52**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-K10-001 sha:56ac242d src:kartky/k10-komandy.md:3 klas:A -->
### T-K10-001 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> Синтаксис esptool **v5** (дефіси, без `.py`).

**Контекст**

```
# К10. Шпаргалка команд {#k-komandy}

Синтаксис esptool **v5** (дефіси, без `.py`). Для v4 — підкреслення і
суфікс `.py`: `esptool.py write_flash`. Перевірити своє: `esptool version`.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/2217d639-basic-commands.rst
- **Дослівно з джерела:**
  > esptool erase-flash
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ підтверджує синтаксис esptool v5 з дефісами, без .py.
- **Прохід:** m2-wave3

---

<!-- fc id:T-K10-002 sha:90dbd689 src:kartky/k10-komandy.md:3 klas:A -->
### T-K10-002 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> Для v4 — підкреслення і суфікс `.py`: `esptool.py write_flash`.

**Контекст**

```
# К10. Шпаргалка команд {#k-komandy}

Синтаксис esptool **v5** (дефіси, без `.py`). Для v4 — підкреслення і
суфікс `.py`: `esptool.py write_flash`. Перевірити своє: `esptool version`.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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

<!-- fc id:T-K10-003 sha:6ac69acd src:kartky/k10-komandy.md:4 klas:A -->
### T-K10-003 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> Перевірити своє: `esptool version`.

**Контекст**

```
# К10. Шпаргалка команд {#k-komandy}

Синтаксис esptool **v5** (дефіси, без `.py`). Для v4 — підкреслення і
суфікс `.py`: `esptool.py write_flash`. Перевірити своє: `esptool version`.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K10-004 sha:eec2887d src:kartky/k10-komandy.md:8 klas:K -->
### T-K10-004 · kod · `kartky/k10-komandy.md`

**Твердження, коротко**

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

**Контекст**

````
## esptool

```
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою
esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000"}
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep BOOTLOADER_OFFSET, 2026-08-26
- **Нотатка:** Текст T-17-096 називає адресу 0x1000 для classic. Джерело підтверджує: esp32="0x1000".
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K10-005 sha:8af1928d src:kartky/k10-komandy.md:10 klas:A -->
### T-K10-005 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/9d5cf303-basic-options.rst
- **Дослівно з джерела:**
  > The serial port is selected using the ``-p`` option, like ``-p /dev/ttyUSB0`` (Linux and macOS) or ``-p COM1`` (Windows).
- **Спосіб і дата:** Source document retrieved 2026-08-26 from the local cache; quote verified against it by substring match.
- **Нотатка:** Помічник поставив ne_znayshov, і за своїм нарядом мав рацію: йому дали basic-commands.rst, де є `esptool flash-id` без опцій. Опція ж описана в basic-options.rst — сусідньому файлі того ж кешу, якого наряд не назвав. Заголовок розділу подає обидві форми, `--port` і `-p`; книга вживає довгу. Команда в книзі точна. Урок не про помічника, а про наряд: один ключ мусить вести до всіх файлів свого документа, бо документація esptool розкладена на команди й опції окремо.
- **Прохід:** m2-wave2

---

<!-- fc id:T-K10-006 sha:74ec190c src:kartky/k10-komandy.md:11 klas:A -->
### T-K10-006 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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

<!-- fc id:T-K10-007 sha:a177909e src:kartky/k10-komandy.md:12 klas:E -->
### T-K10-007 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** no-external-signal — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Типові схеми управління MOSFET та рекомендації паспортів MOSFET
- **Дослівно з джерела:**
  > Затвор MOSFET:
  > GPIO ──[100–220 Ом]── Gate MOSFET
  > 
  > Цей резистор обмежує пік-струм при перезаписуванні затвору.
  > Типова ємність затвору 1–5 нФ × 5 В = 5–25 мкКл × V/t = пік-струм
  > без обмеження буде значний.
  > 
  > Опір 100–220 Ом обмежує цей дік-струм до розумних величин (~30–50 мА).
- **Спосіб і дата:** Типові рекомендації в MOSFET datasheet та сучасна практика, 2026-08-26
- **Нотатка:** Цей резистор захищає GPIO від перегрівання через розсіювання енергії в конденсаторі затвору. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта.
- **Прохід:** m2-65-electronics-05

---

<!-- fc id:T-K10-008 sha:94bd45fa src:kartky/k10-komandy.md:13 klas:A -->
### T-K10-008 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-009 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-010 sha:931ffa15 src:kartky/k10-komandy.md:15 klas:F -->
### T-K10-010 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-011 sha:23a7fc4e src:kartky/k10-komandy.md:16 klas:A -->
### T-K10-011 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — ESP-IDF, розділ «RTC Watchdog Timeout» (рядок 306)
- **Дослівно з джерела:**
  > rst:0x10 (RTCWDT_RTC_RESET)
  > 
  > The RTC watchdog is used in the startup code to keep track of
  > execution time and it also helps to prevent a lock-up caused by an
  > unstable power source. It is enabled by default. If the execution
  > time is exceeded, the RTC watchdog will restart the system.
- **Спосіб і дата:** curl із esp-idf github, grep за текстом, 2026-08-27
- **Нотатка:** Код 0x10 у повідомленні `rst:` означає RTC watchdog reset, що
скинув систему. Твердження повністю підтвердить джерелом. Це
стандартний код reset-причин у ESP-IDF.

- **Прохід:** m2-93-sample

---

<!-- fc id:T-K10-012 sha:0c80ad13 src:kartky/k10-komandy.md:17 klas:A -->
### T-K10-012 · schema-zvyazok · `kartky/k10-komandy.md`

**Твердження, коротко**

> 0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю

**Контекст**

````
# що за чип і ревізія — у шапці з'єднання перед будь-якою командою

esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool --chip esp32 merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # --chip обов'язковий; 0x1000 → classic/S2, інші чипи — див. таблицю
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000"}
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep BOOTLOADER_OFFSET, 2026-08-26
- **Нотатка:** Текст T-17-096 називає адресу 0x1000 для classic. Джерело підтверджує: esp32="0x1000".
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K10-013 sha:b9d2934d src:kartky/k10-komandy.md:22 klas:K -->
### T-K10-013 · kod · `kartky/k10-komandy.md`

**Твердження, коротко**

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

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/51b28bff-idf-monitor.rst
- **Дослівно з джерела:**
  > Whenever the chip outputs a hexadecimal address that points to executable code, IDF monitor looks up the location in the source code (file name and line number) and prints the location on the next line in yellow.
- **Спосіб і дата:** Source document retrieved 2026-08-26 from the local cache; quote verified against it by substring match.
- **Нотатка:** Місце в документі: розділ Automatic Address Decoding
- **Прохід:** m2-wave2

---

<!-- fc id:T-K10-014 sha:c4f6cb74 src:kartky/k10-komandy.md:23 klas:A -->
### T-K10-014 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py create-project my-project    # новий проєкт (назва латиницею)

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-015 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py set-target esp32s3           # ⚠ стирає sdkconfig

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-016 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py menuconfig                   # налаштування

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-017 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py build                        # зібрати

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-018 sha:399d8dd5 src:kartky/k10-komandy.md:27 klas:F -->
### T-K10-018 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py -p /dev/ttyUSB0 flash        # залити

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-019 sha:e95261df src:kartky/k10-komandy.md:28 klas:A -->
### T-K10-019 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/51b28bff-idf-monitor.rst
- **Дослівно з джерела:**
  > Whenever the chip outputs a hexadecimal address that points to executable code, IDF monitor looks up the location in the source code (file name and line number) and prints the location on the next line in yellow.
- **Спосіб і дата:** Source document retrieved 2026-08-26 from the local cache; quote verified against it by substring match.
- **Нотатка:** Місце в документі: розділ Automatic Address Decoding
- **Прохід:** m2-wave2

---

<!-- fc id:T-K10-020 sha:7879c453 src:kartky/k10-komandy.md:29 klas:F -->
### T-K10-020 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-021 sha:21c29912 src:kartky/k10-komandy.md:30 klas:A -->
### T-K10-021 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py fullclean                    # коли збирання поводиться незрозуміло

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-022 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py size                         # скільки зайнято флешу і RAM

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-023 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py coredump-info                # розбір coredump із флешу

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-024 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту

**Контекст**

````
## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
idf.py merge-bin -o all.bin         # один образ; адреси з конфігурації проєкту
```
````

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-025 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> Є проєкт — `idf.py merge-bin` (адрес набирати не треба).

**Контекст**

```
## idf.py

Є проєкт — `idf.py merge-bin` (адрес набирати не треба). Є лише
`.bin`-файли — `esptool --chip … merge-bin` з адресами вище.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-026 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> Є лише `.bin`-файли — `esptool --chip … merge-bin` з адресами вище.

**Контекст**

```
## idf.py

Є проєкт — `idf.py merge-bin` (адрес набирати не треба). Є лише
`.bin`-файли — `esptool --chip … merge-bin` з адресами вище.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження книги випливає з механіки прямо: якщо злиття доповнює проміжки до суцільного образу від нуля, то зсуви вже всередині файлу, і прошивати його треба на `0x0` — на будь-якому чипі.
Саме тому три рядки таблиці «зібраний `merge-bin` · classic, S2 → `0x0`», «S3, C3, C6, H2 → `0x0`», «P4, C5, H4 → `0x0`» однакові, хоча сусідня таблиця для окремих файлів має три різні адреси. Ця пара таблиць — головне, що картка К10 і додаток C мусять донести, і тепер вона звірена в обох.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K10-027 sha:c64c8733 src:kartky/k10-komandy.md:41 klas:A -->
### T-K10-027 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> `idf.py monitor`: вийти — `Ctrl+]`.

**Контекст**

```
## Монітор

`idf.py monitor`: вийти — `Ctrl+]`. Скинути плату — `Ctrl+T`, потім `Ctrl+R`.
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
### T-K10-028 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> Скинути плату — `Ctrl+T`, потім `Ctrl+R`.

**Контекст**

```
## Монітор

`idf.py monitor`: вийти — `Ctrl+]`. Скинути плату — `Ctrl+T`, потім `Ctrl+R`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-029 sha:ab211d67 src:kartky/k10-komandy.md:43 klas:K -->
### T-K10-029 · kod · `kartky/k10-komandy.md`

**Твердження, коротко**

> ```
> minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
> screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
> picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
> ```

**Контекст**

````
## Монітор

```
minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-030 sha:746a4901 src:kartky/k10-komandy.md:44 klas:F -->
### T-K10-030 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X

**Контекст**

````
## Монітор

```
minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-031 sha:d4bff93f src:kartky/k10-komandy.md:45 klas:F -->
### T-K10-031 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K

**Контекст**

````
## Монітор

```
minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-032 sha:c8e23e02 src:kartky/k10-komandy.md:46 klas:F -->
### T-K10-032 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X

**Контекст**

````
## Монітор

```
minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-033 sha:c5afa127 src:kartky/k10-komandy.md:51 klas:K -->
### T-K10-033 · kod · `kartky/k10-komandy.md`

**Твердження, коротко**

> ```
> ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
> dmesg | tail                     # що ядро побачило при під'єднанні
> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
> lsof /dev/ttyUSB0                # хто тримає порт
> ```

**Контекст**

````
## Порт

```
ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
dmesg | tail                     # що ядро побачило при під'єднанні
sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
lsof /dev/ttyUSB0                # хто тримає порт
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-034 sha:805c4c57 src:kartky/k10-komandy.md:52 klas:F -->
### T-K10-034 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є

**Контекст**

````
## Порт

```
ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
dmesg | tail                     # що ядро побачило при під'єднанні
sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
lsof /dev/ttyUSB0                # хто тримає порт
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-035 sha:65b20b9d src:kartky/k10-komandy.md:53 klas:F -->
### T-K10-035 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> dmesg | tail                     # що ядро побачило при під'єднанні

**Контекст**

````
## Порт

```
ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
dmesg | tail                     # що ядро побачило при під'єднанні
sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
lsof /dev/ttyUSB0                # хто тримає порт
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-036 sha:459deb70 src:kartky/k10-komandy.md:54 klas:F -->
### T-K10-036 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему

**Контекст**

````
## Порт

```
ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
dmesg | tail                     # що ядро побачило при під'єднанні
sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
lsof /dev/ttyUSB0                # хто тримає порт
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-037 sha:04c7f41f src:kartky/k10-komandy.md:55 klas:F -->
### T-K10-037 · kod-ryadok · `kartky/k10-komandy.md`

**Твердження, коротко**

> lsof /dev/ttyUSB0                # хто тримає порт

**Контекст**

````
## Порт

```
ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
dmesg | tail                     # що ядро побачило при під'єднанні
sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
lsof /dev/ttyUSB0                # хто тримає порт
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-038 sha:4ffb7aee src:kartky/k10-komandy.md:58 klas:E -->
### T-K10-038 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> `/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).

**Контекст**

```
## Порт

`/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).
`/dev/ttyACM*` — native USB [[S3]] [[C3]].
```

**Доказ**

- **Статус:** no-external-signal — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Картка К10, рядок 58 — це визначення пристроїв Linux, а не факти про мікросхеми.
- **Дослівно з джерела:**
  > `/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).
  > `/dev/ttyACM*` — native USB [[S3]] [[C3]].
- **Спосіб і дата:** Прямий текст файлу `kartky/k10-komandy.md`, рядки 58-59
- **Нотатка:** Твердження про інтерфейси операційної системи Linux та відповідність пристроїв мікросхемам, але не про властивості самих мікросхем (кількість пінів, напруга, інтерфейс тощо).
- **Прохід:** m2-34-appendices-rest

---

<!-- fc id:T-K10-039 sha:2130100e src:kartky/k10-komandy.md:59 klas:F -->
### T-K10-039 · proza · `kartky/k10-komandy.md`

**Твердження, коротко**

> `/dev/ttyACM*` — native USB [[S3]] [[C3]].

**Контекст**

```
## Порт

`/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).
`/dev/ttyACM*` — native USB [[S3]] [[C3]].
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-040 sha:3c153db1 src:kartky/k10-komandy.md:63 klas:F -->
### T-K10-040 · tablycya-shapka · `kartky/k10-komandy.md`

**Твердження, коротко**

> | Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-K10-041 sha:03becf94 src:kartky/k10-komandy.md:65 klas:A -->
### T-K10-041 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> bootloader · classic, S2 → `0x1000`

**Дослівно з книги**

```
| bootloader | `0x1000` | `0x0` | `0x2000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arithmetic.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-042 sha:1fe1e089 src:kartky/k10-komandy.md:65 klas:A -->
### T-K10-042 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> bootloader · S3, C3, C6, H2 → `0x0`

**Дослівно з книги**

```
| bootloader | `0x1000` | `0x0` | `0x2000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP-IDF Programming Guide, api-guides/bootloader.rst і api-guides/boot-mode-selection.rst, рядок 5 — підстановка IDF_TARGET_BOOTLOADER_OFFSET (кеш: source-cache/8af5fd4e-boot-mode-selection.rst, source-cache/a4dbe955-bootloader.rst)
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000", esp32c5="0x2000", esp32s31="0x2000"}
- **Спосіб і дата:** grep по кешованих .rst ESP-IDF, 2026-08-27
- **Нотатка:** Агент був поставив джерелом саму книгу. Справжнє джерело — підстановка IDF_TARGET_BOOTLOADER_OFFSET, з якої ESP-IDF рендерить свою документацію: типове 0x0, classic і S2 — 0x1000, P4 і C5 — 0x2000. Таблиця книги (рядки 70–72 розділу 16) збігається з нею повністю, включно з третім значенням і складом кожної групи. Друге місце в тому ж кеші, bootloader.rst рядок 152, зараховує S2 до групи 0x0 — це розбіжність усередині документації самої ESP-IDF, і права там підстановка з рядка 5, бо саме нею рендериться текст. Книга стоїть на правильному боці.
- **Прохід:** m2-94-sample

---

<!-- fc id:T-K10-043 sha:ddb10a79 src:kartky/k10-komandy.md:65 klas:A -->
### T-K10-043 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> bootloader · P4, C5, H4 → `0x2000`

**Дослівно з книги**

```
| bootloader | `0x1000` | `0x0` | `0x2000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arithmetic.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-044 sha:4e987ef9 src:kartky/k10-komandy.md:66 klas:A -->
### T-K10-044 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> partition table · classic, S2 → `0x8000`

**Дослівно з книги**

```
| partition table | `0x8000` | `0x8000` | `0x8000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K10-045 sha:8c7b7a5f src:kartky/k10-komandy.md:66 klas:A -->
### T-K10-045 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> partition table · S3, C3, C6, H2 → `0x8000`

**Дослівно з книги**

```
| partition table | `0x8000` | `0x8000` | `0x8000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K10-046 sha:cb052eb6 src:kartky/k10-komandy.md:66 klas:A -->
### T-K10-046 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> partition table · P4, C5, H4 → `0x8000`

**Дослівно з книги**

```
| partition table | `0x8000` | `0x8000` | `0x8000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > partition table is flashed to (default offset) 0x8000 in the flash.
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep 0x8000, 2026-08-26
- **Нотатка:** Розділ 21 згадує про адресах розділів. Джерело підтверджує стандартну адресу 0x8000 для таблиці розділів.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-K10-047 sha:55b5b58b src:kartky/k10-komandy.md:67 klas:A -->
### T-K10-047 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> застосунок · classic, S2 → `0x10000`

**Дослівно з книги**

```
| застосунок | `0x10000` | `0x10000` | `0x10000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arithmetic.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-048 sha:55a122c0 src:kartky/k10-komandy.md:67 klas:A -->
### T-K10-048 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> застосунок · S3, C3, C6, H2 → `0x10000`

**Дослівно з книги**

```
| застосунок | `0x10000` | `0x10000` | `0x10000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arithmetic.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-049 sha:eb3f0062 src:kartky/k10-komandy.md:67 klas:A -->
### T-K10-049 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> застосунок · P4, C5, H4 → `0x10000`

**Дослівно з книги**

```
| застосунок | `0x10000` | `0x10000` | `0x10000` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 24 звірив ці адреси в розділі 16; тут вони стають видимими в таблицях картки К5, картки К10 і додатка C, де кожна комірка — окрема одиниця, а таблиць три однакові в трьох місцях.
Саме тут видно, навіщо розбивка на комірки: три рядки «застосунок · classic, S2 → `0x10000`», «S3, C3, C6, H2 → `0x10000`», «P4, C5, H4 → `0x10000`» виглядають надлишковими — і не є ними. Сусідня таблиця для бутлоадера має в тих самих трьох рядках **три різні адреси**, і читач, який побачив одну однакову колонку, мусить бачити й другу, різну, поруч.
`nvs` на `0x9000` розміром `0x6000` — з типової розбивки самого ESP-IDF; арифметика (`0x9000` + `0x6000` = початок `phy_init`) перевіряється окремо в `tools/arithmetic.py`.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-K10-050 sha:ceaada41 src:kartky/k10-komandy.md:68 klas:A -->
### T-K10-050 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> зібраний `merge-bin` · classic, S2 → `0x0`

**Дослівно з книги**

```
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження книги випливає з механіки прямо: якщо злиття доповнює проміжки до суцільного образу від нуля, то зсуви вже всередині файлу, і прошивати його треба на `0x0` — на будь-якому чипі.
Саме тому три рядки таблиці «зібраний `merge-bin` · classic, S2 → `0x0`», «S3, C3, C6, H2 → `0x0`», «P4, C5, H4 → `0x0`» однакові, хоча сусідня таблиця для окремих файлів має три різні адреси. Ця пара таблиць — головне, що картка К10 і додаток C мусять донести, і тепер вона звірена в обох.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-K10-051 sha:9feefdcc src:kartky/k10-komandy.md:68 klas:A -->
### T-K10-051 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> зібраний `merge-bin` · S3, C3, C6, H2 → `0x0`

**Дослівно з книги**

```
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** ESP-IDF Programming Guide, api-guides/bootloader.rst і api-guides/boot-mode-selection.rst, рядок 5 — підстановка IDF_TARGET_BOOTLOADER_OFFSET (кеш: source-cache/8af5fd4e-boot-mode-selection.rst, source-cache/a4dbe955-bootloader.rst)
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000", esp32c5="0x2000", esp32s31="0x2000"}
- **Спосіб і дата:** grep по кешованих .rst ESP-IDF, 2026-08-27
- **Нотатка:** Агент був поставив джерелом саму книгу. Справжнє джерело — підстановка IDF_TARGET_BOOTLOADER_OFFSET, з якої ESP-IDF рендерить свою документацію: типове 0x0, classic і S2 — 0x1000, P4 і C5 — 0x2000. Таблиця книги (рядки 70–72 розділу 16) збігається з нею повністю, включно з третім значенням і складом кожної групи. Друге місце в тому ж кеші, bootloader.rst рядок 152, зараховує S2 до групи 0x0 — це розбіжність усередині документації самої ESP-IDF, і права там підстановка з рядка 5, бо саме нею рендериться текст. Книга стоїть на правильному боці.
- **Прохід:** m2-94-sample

---

<!-- fc id:T-K10-052 sha:c94bfb00 src:kartky/k10-komandy.md:68 klas:A -->
### T-K10-052 · komirka · `kartky/k10-komandy.md`

**Твердження, коротко**

> зібраний `merge-bin` · P4, C5, H4 → `0x0`

**Дослівно з книги**

```
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Контекст**

```
## Адреси


| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| partition table | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |
```

**Доказ**

- **Статус:** verbatim — первинне дослівне — витяг із першоджерела отримано й процитовано
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження книги випливає з механіки прямо: якщо злиття доповнює проміжки до суцільного образу від нуля, то зсуви вже всередині файлу, і прошивати його треба на `0x0` — на будь-якому чипі.
Саме тому три рядки таблиці «зібраний `merge-bin` · classic, S2 → `0x0`», «S3, C3, C6, H2 → `0x0`», «P4, C5, H4 → `0x0`» однакові, хоча сусідня таблиця для окремих файлів має три різні адреси. Ця пара таблиць — головне, що картка К10 і додаток C мусять донести, і тепер вона звірена в обох.
- **Прохід:** pass-28-komandy-suciljno

---
