# Фактчекінг: `manual/17-esptool.md`

Одиниць твердження: **154**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-17-001 sha:760be9ee src:manual/17-esptool.md:3 klas:B -->
### T-17-001 · proza · рядок 3

**Книга каже, дослівно:**

> `esptool` — програма, що розмовляє з ROM-бутлоадером чипа.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/index.rst та .../esptool/basic-commands.rst
- **Дослівно з джерела:**
  > esptool is a Python-based, open-source, platform-independent utility to
  > communicate with the ROM bootloader in Espressif chips.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і це свідомо. Дослівно з джерела випливає лише перше твердження — що `esptool` розмовляє з ROM-бутлоадером.
Решта («перші дві команди для незнайомої плати», «дамп до першої зміни», «доки чип відповідає на `chip-id`, він живий») — **порядок дій**, який випливає з властивостей команд однозначно, але в жодному документі так не сформульований. Це рекомендація книги, побудована на звірених фактах, і чесний клас для неї — `B`.
Записую це окремо, бо спокуса поставити `A` тут така сама, як була з JTAG-пінами в проході 20: твердження здається загальновідомим і безсумнівним. Але «безсумнівне» і «процитоване» — різні класи.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-002 sha:4b3198e0 src:manual/17-esptool.md:3 klas:F -->
### T-17-002 · proza · рядок 3

**Книга каже, дослівно:**

> Вона не знає нічого про ваш проєкт, не потребує встановленого ESP-IDF і працює з будь-якою платою на ESP32, включно з тією, прошивку якої зібрав хтось інший десять років тому.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-003 sha:8ea7354e src:manual/17-esptool.md:8 klas:E -->
### T-17-003 · proza · рядок 8

**Книга каже, дослівно:**

> Це головний інструмент для всього, що стосується чужого заліза: визначити чип, зняти дамп, залити готовий образ, стерти.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-004 sha:9395569b src:manual/17-esptool.md:8 klas:B -->
### T-17-004 · proza · рядок 8

**Книга каже, дослівно:**

> Якщо з плати можна взяти хоч щось — це буде через `esptool`.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/index.rst та .../esptool/basic-commands.rst
- **Дослівно з джерела:**
  > esptool is a Python-based, open-source, platform-independent utility to
  > communicate with the ROM bootloader in Espressif chips.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і це свідомо. Дослівно з джерела випливає лише перше твердження — що `esptool` розмовляє з ROM-бутлоадером.
Решта («перші дві команди для незнайомої плати», «дамп до першої зміни», «доки чип відповідає на `chip-id`, він живий») — **порядок дій**, який випливає з властивостей команд однозначно, але в жодному документі так не сформульований. Це рекомендація книги, побудована на звірених фактах, і чесний клас для неї — `B`.
Записую це окремо, бо спокуса поставити `A` тут така сама, як була з JTAG-пінами в проході 20: твердження здається загальновідомим і безсумнівним. Але «безсумнівне» і «процитоване» — різні класи.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-005 sha:2ed9656d src:manual/17-esptool.md:14 klas:E -->
### T-17-005 · proza · рядок 14

**Книга каже, дослівно:**

> Перше, що треба з'ясувати, — яка версія у вас:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-006 sha:64f486d7 src:manual/17-esptool.md:16 klas:K -->
### T-17-006 · kod · рядок 16

**Книга каже, дослівно:**

> ```
> esptool version
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-007 sha:fcbae1b9 src:manual/17-esptool.md:17 klas:F -->
### T-17-007 · kod-ryadok · рядок 17

**Книга каже, дослівно:**

> esptool version

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-008 sha:9c3eef10 src:manual/17-esptool.md:20 klas:E -->
### T-17-008 · proza · рядок 20

**Книга каже, дослівно:**

> Команда друкує номер версії — це і є відповідь.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-009 sha:ea8f78cc src:manual/17-esptool.md:20 klas:A -->
### T-17-009 · proza · рядок 20

**Книга каже, дослівно:**

> Якщо `esptool` не знайдено взагалі, спробувати `esptool.py version`: у v4 інакшого імені немає.

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

<!-- fc id:T-17-010 sha:790431ab src:manual/17-esptool.md:20 klas:A -->
### T-17-010 · proza · рядок 20

**Книга каже, дослівно:**

> Зворотне не працює: у v5 обидва імені є, і те, що команда запустилася під іменем `esptool.py`, ще нічого не означає — дивитися треба на надрукований номер.

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

<!-- fc id:T-17-011 sha:332e0818 src:manual/17-esptool.md:26 klas:A -->
### T-17-011 · proza · рядок 26

**Книга каже, дослівно:**

> **esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають копіювання команд з інтернету:

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

<!-- fc id:T-17-012 sha:0e9fb3f8 src:manual/17-esptool.md:29 klas:F -->
### T-17-012 · tablycya-shapka · рядок 29

**Книга каже, дослівно:**

> | | v4 і раніше | v5 |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-013 sha:e59d8c4e src:manual/17-esptool.md:30 klas:A -->
### T-17-013 · komirka · рядок 30

**Книга каже, дослівно:**

> виклик · v4 і раніше → `esptool.py`

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

<!-- fc id:T-17-014 sha:15c8ed07 src:manual/17-esptool.md:30 klas:A -->
### T-17-014 · komirka · рядок 30

**Книга каже, дослівно:**

> виклик · v5 → `esptool`

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

<!-- fc id:T-17-015 sha:f36c79a8 src:manual/17-esptool.md:31 klas:A -->
### T-17-015 · komirka · рядок 31

**Книга каже, дослівно:**

> команди · v4 і раніше → `write_flash`, `chip_id`

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

<!-- fc id:T-17-016 sha:4fe690f3 src:manual/17-esptool.md:31 klas:A -->
### T-17-016 · komirka · рядок 31

**Книга каже, дослівно:**

> команди · v5 → `write-flash`, `chip-id`

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

<!-- fc id:T-17-017 sha:c2641f27 src:manual/17-esptool.md:34 klas:F -->
### T-17-017 · proza · рядок 34

**Книга каже, дослівно:**

> Переважна більшість інструкцій, статей і відповідей на форумах написана під v4, і напрямки несиметричні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-018 sha:5b950f2b src:manual/17-esptool.md:37 klas:F -->
### T-17-018 · proza · рядок 37

**Книга каже, дослівно:**

> **Стара команда на новій версії поки що працює.** У v5 старі імена позначені як застарілі: виконуються з попередженням і будуть прибрані в наступному major-релізі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-019 sha:2b706815 src:manual/17-esptool.md:37 klas:A -->
### T-17-019 · proza · рядок 37

**Книга каже, дослівно:**

> Тобто `write_flash` на v5 спрацює — і тим неприємніше буде, коли одного дня перестане.

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

<!-- fc id:T-17-020 sha:424c39d1 src:manual/17-esptool.md:42 klas:A -->
### T-17-020 · proza · рядок 42

**Книга каже, дослівно:**

> **Нова команда на старій версії не працює.** `write-flash` на v4 дає «невідома команда», і це збиває з пантелику: команда відома, просто пишеться інакше.

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

<!-- fc id:T-17-021 sha:2058f23b src:manual/17-esptool.md:46 klas:A -->
### T-17-021 · proza · рядок 46

**Книга каже, дослівно:**

> Перейменування торкнулося не лише команд, а й **опцій**: `--flash_size`, `--flash_mode`, `--flash_freq`, а також значень `--before` і `--after`.

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

<!-- fc id:T-17-022 sha:8254cee9 src:manual/17-esptool.md:49 klas:A -->
### T-17-022 · proza · рядок 49

**Книга каже, дослівно:**

> **У цьому довіднику команди подаються в синтаксисі v5.** Щоб отримати варіант для v4: замінити дефіси на підкреслення і додати `.py`.

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

<!-- fc id:T-17-023 sha:9063d84c src:manual/17-esptool.md:53 klas:A -->
### T-17-023 · proza · рядок 53

**Книга каже, дослівно:**

> Версія `esptool` залежить не від вашого вибору, а від того, звідки вона взялася.

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

<!-- fc id:T-17-024 sha:a5e9385a src:manual/17-esptool.md:53 klas:F -->
### T-17-024 · proza · рядок 53

**Книга каже, дослівно:**

> Разом з ESP-IDF 5.x іде v4, разом з ESP-IDF 6.x — v5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-025 sha:5d432647 src:manual/17-esptool.md:53 klas:F -->
### T-17-025 · proza · рядок 53

**Книга каже, дослівно:**

> Встановлена окремо через `pip` — та, що була свіжою на момент встановлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-026 sha:8e12e7bb src:manual/17-esptool.md:53 klas:A -->
### T-17-026 · proza · рядок 53

**Книга каже, дослівно:**

> Якщо у вас на машині є і те, і те, `esptool` і `esptool.py` можуть бути **різних версій** — це джерело дуже дивних годин.

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

<!-- fc id:T-17-027 sha:85f599cb src:manual/17-esptool.md:62 klas:K -->
### T-17-027 · kod · рядок 62

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 chip-id
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

<!-- fc id:T-17-028 sha:32416a21 src:manual/17-esptool.md:63 klas:F -->
### T-17-028 · kod-ryadok · рядок 63

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 chip-id

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-029 sha:286e1ec5 src:manual/17-esptool.md:66 klas:E -->
### T-17-029 · proza · рядок 66

**Книга каже, дослівно:**

> Відповідь називає сімейство, ревізію кремнію і MAC-адресу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-030 sha:5d3f09ae src:manual/17-esptool.md:66 klas:E -->
### T-17-030 · proza · рядок 66

**Книга каже, дослівно:**

> Це перша команда для будь-якої незнайомої плати: вона одночасно перевіряє, що зв'язок є, і каже, з чим маєте справу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-031 sha:e66c9553 src:manual/17-esptool.md:70 klas:K -->
### T-17-031 · kod · рядок 70

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 flash-id
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

<!-- fc id:T-17-032 sha:4c5a16ee src:manual/17-esptool.md:71 klas:F -->
### T-17-032 · kod-ryadok · рядок 71

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 flash-id

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-033 sha:337e3191 src:manual/17-esptool.md:74 klas:E -->
### T-17-033 · proza · рядок 74

**Книга каже, дослівно:**

> Виробник і **обсяг** флешу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-034 sha:50a21c79 src:manual/17-esptool.md:74 klas:E -->
### T-17-034 · proza · рядок 74

**Книга каже, дослівно:**

> Обсяг важливий двічі: він потрібен для дампа і він викриває підробки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-035 sha:3d4176e9 src:manual/17-esptool.md:74 klas:F -->
### T-17-035 · proza · рядок 74

**Книга каже, дослівно:**

> Модуль з написом `ESP32-WROOM-32` і флешем 2 МБ замість 4 МБ — перемаркований клон.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-036 sha:43e4d49a src:manual/17-esptool.md:79 klas:F -->
### T-17-036 · proza · рядок 79

**Книга каже, дослівно:**

> `flash-id` показує те, що каже сама мікросхема флешу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-037 sha:724102a6 src:manual/17-esptool.md:79 klas:E -->
### T-17-037 · proza · рядок 79

**Книга каже, дослівно:**

> Бутлоадер у логу (розділ 16) показує те, що йому **сконфігуровано**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-038 sha:a5d0e23b src:manual/17-esptool.md:79 klas:E -->
### T-17-038 · proza · рядок 79

**Книга каже, дослівно:**

> Розбіжність між цими двома числами означає неправильно зібрану прошивку: частина флешу просто не використовується, або, гірше, прошивка розраховує на пам'ять, якої немає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-039 sha:c1db89f4 src:manual/17-esptool.md:88 klas:E -->
### T-17-039 · proza · рядок 88

**Книга каже, дослівно:**

> Найважливіша команда в усьому розділі, бо єдина незворотна операція — це та, перед якою не зробили дамп.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-040 sha:8b4f4b75 src:manual/17-esptool.md:91 klas:K -->
### T-17-040 · kod · рядок 91

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump-2026-08-26.bin
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

<!-- fc id:T-17-041 sha:213017c0 src:manual/17-esptool.md:92 klas:A -->
### T-17-041 · kod-ryadok · рядок 92

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump-2026-08-26.bin

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

<!-- fc id:T-17-042 sha:1856248d src:manual/17-esptool.md:95 klas:A -->
### T-17-042 · proza · рядок 95

**Книга каже, дослівно:**

> `ALL` читає рівно стільки, скільки є на чипі.

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

<!-- fc id:T-17-043 sha:dd810cb6 src:manual/17-esptool.md:95 klas:D -->
### T-17-043 · proza · рядок 95

**Книга каже, дослівно:**

> Якщо ваша версія цього не розуміє — підставити обсяг явно: `0x400000` (4 МБ), `0x800000` (8 МБ), `0x1000000` (16 МБ).

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

<!-- fc id:T-17-044 sha:a3ccf901 src:manual/17-esptool.md:99 klas:E -->
### T-17-044 · proza · рядок 99

**Книга каже, дослівно:**

> Перевірка результату — одразу, не потім: **розмір файлу має точно дорівнювати обсягу флешу**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-045 sha:1b2d4902 src:manual/17-esptool.md:99 klas:E -->
### T-17-045 · proza · рядок 99

**Книга каже, дослівно:**

> Файл, менший за очікуваний, — це обірваний дамп, а не «стисненіший».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-046 sha:4cbc54f8 src:manual/17-esptool.md:99 klas:F -->
### T-17-046 · proza · рядок 99

**Книга каже, дослівно:**

> Читання на високій швидкості через довгий кабель обривається частіше, ніж хотілося б; при найменшому сумніві повторити з `--baud 115200` і порівняти розміри.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-047 sha:eada110b src:manual/17-esptool.md:105 klas:F -->
### T-17-047 · proza · рядок 105

**Книга каже, дослівно:**

> Можна читати й окремий шматок — наприклад, лише розділ NVS:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-048 sha:0615bf62 src:manual/17-esptool.md:107 klas:K -->
### T-17-048 · kod · рядок 107

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 read-flash 0x9000 0x6000 nvs.bin
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

<!-- fc id:T-17-049 sha:fe1f802d src:manual/17-esptool.md:108 klas:D -->
### T-17-049 · kod-ryadok · рядок 108

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 read-flash 0x9000 0x6000 nvs.bin

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

<!-- fc id:T-17-050 sha:b46fc5e5 src:manual/17-esptool.md:113 klas:F -->
### T-17-050 · proza · рядок 113

**Книга каже, дослівно:**

> [[classic]] Адреси в цьому прикладі — для ESP32 classic:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-051 sha:911de04d src:manual/17-esptool.md:115 klas:K -->
### T-17-051 · kod · рядок 115

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
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

<!-- fc id:T-17-052 sha:bdd61138 src:manual/17-esptool.md:116 klas:A -->
### T-17-052 · kod-ryadok · рядок 116

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \

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

<!-- fc id:T-17-053 sha:add669dc src:manual/17-esptool.md:122 klas:A -->
### T-17-053 · proza · рядок 122

**Книга каже, дослівно:**

> На [[S3]] [[C3]], C6 і H2 бутлоадер іде не на `0x1000`, а на `0x0`; на P4, C5 і H4 — на `0x2000`; решта адрес та сама (таблиця в розділі 16).

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

<!-- fc id:T-17-054 sha:e548f18b src:manual/17-esptool.md:122 klas:F -->
### T-17-054 · proza · рядок 122

**Книга каже, дослівно:**

> Скопіювати цей приклад дослівно на інший чип означає покласти бутлоадер у порожнє місце — і `esptool` не поскаржиться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-055 sha:782ec293 src:manual/17-esptool.md:127 klas:E -->
### T-17-055 · proza · рядок 127

**Книга каже, дослівно:**

> Аргументи йдуть парами: адреса, файл.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-056 sha:cb74d03e src:manual/17-esptool.md:127 klas:E -->
### T-17-056 · proza · рядок 127

**Книга каже, дослівно:**

> Скільки завгодно пар за один виклик.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-057 sha:8627aec2 src:manual/17-esptool.md:129 klas:F -->
### T-17-057 · proza · рядок 129

**Книга каже, дослівно:**

> `-z` вмикає стиснення при передачі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-058 sha:85b9b718 src:manual/17-esptool.md:129 klas:E -->
### T-17-058 · proza · рядок 129

**Книга каже, дослівно:**

> Воно **вже ввімкнене** за замовчуванням, тож у звичайній команді прапорець нічого не змінює.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-059 sha:f86910b1 src:manual/17-esptool.md:129 klas:F -->
### T-17-059 · proza · рядок 129

**Книга каже, дослівно:**

> Сенс він має лише разом із `--no-stub`, де стиснення типово вимкнене — а це саме той випадок із клонами, який розібрано нижче.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-060 sha:dafa4e9c src:manual/17-esptool.md:129 klas:E -->
### T-17-060 · proza · рядок 129

**Книга каже, дослівно:**

> Користь від стиснення там подвійна: менше байтів пройшло довгим кабелем — менше нагод зіпсуватися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-061 sha:12ca7f51 src:manual/17-esptool.md:136 klas:F -->
### T-17-061 · proza · рядок 136

**Книга каже, дослівно:**

> `--baud 460800` — розумний максимум для більшості мостів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-062 sha:2711187e src:manual/17-esptool.md:136 klas:F -->
### T-17-062 · proza · рядок 136

**Книга каже, дослівно:**

> Не з'єднується або обривається — знижувати: `230400`, далі `115200`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-063 sha:d5bda61e src:manual/17-esptool.md:136 klas:E -->
### T-17-063 · proza · рядок 136

**Книга каже, дослівно:**

> Швидкість тут не той параметр, на якому варто економити хвилини.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-064 sha:c7be6edf src:manual/17-esptool.md:140 klas:E -->
### T-17-064 · proza · рядок 140

**Книга каже, дослівно:**

> Адреси залежать від сімейства чипа — таблиця в розділі 16 і на картці [К5](#k-proshyvka).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-065 sha:6cc1d835 src:manual/17-esptool.md:140 klas:E -->
### T-17-065 · proza · рядок 140

**Книга каже, дослівно:**

> Це те місце, де помиляються найчастіше.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-066 sha:1edaa56d src:manual/17-esptool.md:145 klas:K -->
### T-17-066 · kod · рядок 145

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 erase-flash
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-067 sha:7a96df73 src:manual/17-esptool.md:146 klas:F -->
### T-17-067 · kod-ryadok · рядок 146

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 erase-flash

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-068 sha:4c597925 src:manual/17-esptool.md:150 klas:F -->
### T-17-068 · proza · рядок 150

**Книга каже, дослівно:**

> `erase-flash` знищує **весь** флеш, включно з розділом NVS.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-069 sha:675172ea src:manual/17-esptool.md:150 klas:F -->
### T-17-069 · proza · рядок 150

**Книга каже, дослівно:**

> У NVS лежать не лише ваші налаштування, а й калібрувальні дані радіо, збережені креденшели Wi-Fi і конфігурація конкретного пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-070 sha:02d4467f src:manual/17-esptool.md:150 klas:E -->
### T-17-070 · proza · рядок 150

**Книга каже, дослівно:**

> Перезбирання прошивки цього не повертає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-071 sha:501abb75 src:manual/17-esptool.md:155 klas:B -->
### T-17-071 · proza · рядок 155

**Книга каже, дослівно:**

> Дамп (`read-flash`) робиться **до**, а не після.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/index.rst та .../esptool/basic-commands.rst
- **Дослівно з джерела:**
  > esptool is a Python-based, open-source, platform-independent utility to
  > communicate with the ROM bootloader in Espressif chips.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і це свідомо. Дослівно з джерела випливає лише перше твердження — що `esptool` розмовляє з ROM-бутлоадером.
Решта («перші дві команди для незнайомої плати», «дамп до першої зміни», «доки чип відповідає на `chip-id`, він живий») — **порядок дій**, який випливає з властивостей команд однозначно, але в жодному документі так не сформульований. Це рекомендація книги, побудована на звірених фактах, і чесний клас для неї — `B`.
Записую це окремо, бо спокуса поставити `A` тут така сама, як була з JTAG-пінами в проході 20: твердження здається загальновідомим і безсумнівним. Але «безсумнівне» і «процитоване» — різні класи.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-072 sha:2b455157 src:manual/17-esptool.md:158 klas:F -->
### T-17-072 · proza · рядок 158

**Книга каже, дослівно:**

> Коли `erase-flash` справді потрібен: залишки старої розбивки заважають новій таблиці розділів; підозра на пошкоджений NVS, через який застосунок падає при старті; підготовка плати до продажу чи передачі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-073 sha:d9b8c3fc src:manual/17-esptool.md:162 klas:E -->
### T-17-073 · proza · рядок 162

**Книга каже, дослівно:**

> Коли не потрібен: «щоб напевно».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-074 sha:72b6debe src:manual/17-esptool.md:162 klas:A -->
### T-17-074 · proza · рядок 162

**Книга каже, дослівно:**

> `write-flash` і так перезаписує те, що записує; стирати все заради оновлення застосунку — зайвий ризик.

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

<!-- fc id:T-17-075 sha:6361b41c src:manual/17-esptool.md:165 klas:E -->
### T-17-075 · proza · рядок 165

**Книга каже, дослівно:**

> Стерти лише частину — точніше і безпечніше:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-076 sha:5a1c829e src:manual/17-esptool.md:167 klas:K -->
### T-17-076 · kod · рядок 167

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 erase-region 0x9000 0x6000
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

<!-- fc id:T-17-077 sha:b3a989e0 src:manual/17-esptool.md:168 klas:A -->
### T-17-077 · kod-ryadok · рядок 168

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 erase-region 0x9000 0x6000

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

<!-- fc id:T-17-078 sha:31d5a3a2 src:manual/17-esptool.md:173 klas:K -->
### T-17-078 · kod · рядок 173

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin
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

<!-- fc id:T-17-079 sha:c93ce3ef src:manual/17-esptool.md:174 klas:A -->
### T-17-079 · kod-ryadok · рядок 174

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin

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

<!-- fc id:T-17-080 sha:61989c98 src:manual/17-esptool.md:177 klas:E -->
### T-17-080 · proza · рядок 177

**Книга каже, дослівно:**

> Порівнює вміст флешу з файлом.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-081 sha:6337a912 src:manual/17-esptool.md:177 klas:A -->
### T-17-081 · proza · рядок 177

**Книга каже, дослівно:**

> «Прошилося без помилок» і «у флеші лежить те, що треба» — різні твердження, і `verify-flash` перетворює перше на друге.

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

<!-- fc id:T-17-082 sha:306c9a4d src:manual/17-esptool.md:177 klas:E -->
### T-17-082 · proza · рядок 177

**Книга каже, дослівно:**

> На серійній прошивці (розділ 21) це обов'язковий крок, не опція.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-083 sha:3f578024 src:manual/17-esptool.md:183 klas:E -->
### T-17-083 · proza · рядок 183

**Книга каже, дослівно:**

> Три файли на трьох адресах — незручно передавати іншій людині й легко переплутати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-084 sha:fc4482af src:manual/17-esptool.md:183 klas:A -->
### T-17-084 · proza · рядок 183

**Книга каже, дослівно:**

> `merge-bin` склеює їх в один образ, у якому зсуви вже всередині:

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-commands.rst)
  > The ``merge-bin`` command will merge multiple binary files … Any gaps
  > between the input files are padded with 0xFF bytes.
  > Options such as ``--flash-mode``, ``--flash-size`` and ``--flash-freq``
  > are used to set the corresponding values in the image header, exactly
  > as they would be when flashing.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-085 sha:c1d44c0d src:manual/17-esptool.md:187 klas:K -->
### T-17-085 · kod · рядок 187

**Книга каже, дослівно:**

> ```
> esptool --chip esp32 merge-bin -o vyrib-v1.bin --flash-mode dio \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
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

<!-- fc id:T-17-086 sha:86df9991 src:manual/17-esptool.md:188 klas:A -->
### T-17-086 · kod-ryadok · рядок 188

**Книга каже, дослівно:**

> esptool --chip esp32 merge-bin -o vyrib-v1.bin --flash-mode dio \

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

<!-- fc id:T-17-087 sha:265e633f src:manual/17-esptool.md:194 klas:A -->
### T-17-087 · proza · рядок 194

**Книга каже, дослівно:**

> `--chip` тут **обов'язковий**, і це єдина команда розділу, де він не опція.

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

<!-- fc id:T-17-088 sha:6579e87b src:manual/17-esptool.md:194 klas:A -->
### T-17-088 · proza · рядок 194

**Книга каже, дослівно:**

> Решта команд працює через порт і визначає чип сама; `merge-bin` порту не має — вона складає файл офлайн.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-commands.rst)
  > The ``merge-bin`` command will merge multiple binary files … Any gaps
  > between the input files are padded with 0xFF bytes.
  > Options such as ``--flash-mode``, ``--flash-size`` and ``--flash-freq``
  > are used to set the corresponding values in the image header, exactly
  > as they would be when flashing.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-089 sha:7acf702f src:manual/17-esptool.md:194 klas:A -->
### T-17-089 · proza · рядок 194

**Книга каже, дослівно:**

> Без `--chip` esptool не вгадує, а зупиняється: `Specify the --chip argument`.

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

<!-- fc id:T-17-090 sha:2431f38a src:manual/17-esptool.md:199 klas:F -->
### T-17-090 · proza · рядок 199

**Книга каже, дослівно:**

> [[classic]] Адреса `0x1000` тут — знову classic, і тепер вона узгоджена з `--chip esp32` у тому ж рядку; для інших чипів див. таблицю в розділі 16.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-091 sha:66ee792a src:manual/17-esptool.md:199 klas:A -->
### T-17-091 · proza · рядок 199

**Книга каже, дослівно:**

> Адреси всередині `merge-bin` мають бути ті самі, якими прошивали б окремо.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-commands.rst)
  > The ``merge-bin`` command will merge multiple binary files … Any gaps
  > between the input files are padded with 0xFF bytes.
  > Options such as ``--flash-mode``, ``--flash-size`` and ``--flash-freq``
  > are used to set the corresponding values in the image header, exactly
  > as they would be when flashing.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-092 sha:a8ba7c8e src:manual/17-esptool.md:204 klas:F -->
### T-17-092 · proza · рядок 204

**Книга каже, дослівно:**

> Отриманий файл заливається завжди на адресу `0x0`, незалежно від сімейства чипа:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-093 sha:ba49e524 src:manual/17-esptool.md:207 klas:K -->
### T-17-093 · kod · рядок 207

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.bin
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

<!-- fc id:T-17-094 sha:f1947da9 src:manual/17-esptool.md:208 klas:A -->
### T-17-094 · kod-ryadok · рядок 208

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.bin

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

<!-- fc id:T-17-095 sha:d53fd3ce src:manual/17-esptool.md:211 klas:E -->
### T-17-095 · proza · рядок 211

**Книга каже, дослівно:**

> Це формат, у якому варто віддавати прошивку тому, хто не читав цієї книги: одна команда, одна адреса, нема чого переплутати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-096 sha:a0822607 src:manual/17-esptool.md:211 klas:E -->
### T-17-096 · proza · рядок 211

**Книга каже, дослівно:**

> Основа серійної прошивки — розділ 21.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-097 sha:0c354cb5 src:manual/17-esptool.md:217 klas:F -->
### T-17-097 · proza · рядок 217

**Книга каже, дослівно:**

> Усе вище потрібне тоді, коли у вас на руках лише три `.bin`-файли.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-098 sha:ed62f710 src:manual/17-esptool.md:217 klas:F -->
### T-17-098 · proza · рядок 217

**Книга каже, дослівно:**

> Якщо ж є сам проєкт ESP-IDF, є коротший і надійніший шлях:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-099 sha:aa4bc88d src:manual/17-esptool.md:220 klas:K -->
### T-17-099 · kod · рядок 220

**Книга каже, дослівно:**

> ```
> idf.py merge-bin -o vyrib-v1.bin
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

<!-- fc id:T-17-100 sha:8d510e99 src:manual/17-esptool.md:221 klas:A -->
### T-17-100 · kod-ryadok · рядок 221

**Книга каже, дослівно:**

> idf.py merge-bin -o vyrib-v1.bin

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

<!-- fc id:T-17-101 sha:85f58bc1 src:manual/17-esptool.md:224 klas:E -->
### T-17-101 · proza · рядок 224

**Книга каже, дослівно:**

> Ця команда бере бутлоадер, таблицю розділів, застосунок і решту розділів **за конфігурацією проєкту**: адреси, чип, режим і частота флешу підставляються самі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-102 sha:06b69d9f src:manual/17-esptool.md:224 klas:A -->
### T-17-102 · proza · рядок 224

**Книга каже, дослівно:**

> Без параметрів результат лягає у `build/merged-binary.bin`.

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

<!-- fc id:T-17-103 sha:6edab381 src:manual/17-esptool.md:230 klas:F -->
### T-17-103 · proza · рядок 230

**Книга каже, дослівно:**

> У ручному варіанті адреса бутлоадера набирається з голови, і саме там роблять помилку: `0x1000` на S3 дає образ, який прошивається без жодної скарги і не стартує (розділ 16).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-104 sha:c0359df7 src:manual/17-esptool.md:234 klas:A -->
### T-17-104 · proza · рядок 234

**Книга каже, дослівно:**

> `idf.py merge-bin` цю можливість прибирає повністю — воно читає адресу з конфігурації того самого проєкту, який ви щойно зібрали.

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

<!-- fc id:T-17-105 sha:5a1fb7e0 src:manual/17-esptool.md:237 klas:A -->
### T-17-105 · proza · рядок 237

**Книга каже, дослівно:**

> Правило просте: є проєкт — `idf.py merge-bin`; є тільки файли — `esptool --chip … merge-bin` з адресами з таблиці.

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

<!-- fc id:T-17-106 sha:36e4678e src:manual/17-esptool.md:243 klas:A -->
### T-17-106 · proza · рядок 243

**Книга каже, дослівно:**

> **`A fatal error occurred: Failed to connect to ESP32: No serial data received.`**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-17-107 sha:046e97d7 src:manual/17-esptool.md:246 klas:E -->
### T-17-107 · proza · рядок 246

**Книга каже, дослівно:**

> Спробувати вручну (картка [К4](#k-boot)), знизити швидкість, перевірити, що порт не зайнятий відкритим монітором.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-108 sha:7eae188f src:manual/17-esptool.md:250 klas:E -->
### T-17-108 · proza · рядок 250

**Книга каже, дослівно:**

> Друга половина рядка залежить від версії.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-109 sha:a9001ab8 src:manual/17-esptool.md:250 klas:A -->
### T-17-109 · proza · рядок 250

**Книга каже, дослівно:**

> `No serial data received.` — esptool v4 і v5; `Timed out waiting for packet header` — старіші v3, які ще трапляються в готових складаннях і в чужих інструкціях.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-17-110 sha:2936ba3a src:manual/17-esptool.md:250 klas:A -->
### T-17-110 · proza · рядок 250

**Книга каже, дослівно:**

> Причина в обох випадках та сама, і шукати варто за початком рядка — `Failed to connect`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-111 sha:81eb3b69 src:manual/17-esptool.md:256 klas:F -->
### T-17-111 · proza · рядок 256

**Книга каже, дослівно:**

> **`Serial port ... could not be opened: Permission denied`**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-112 sha:c018ab70 src:manual/17-esptool.md:258 klas:F -->
### T-17-112 · proza · рядок 258

**Книга каже, дослівно:**

> Linux: група `dialout`, потім **перезайти в систему** (картка [К3](#k-pidkl)).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-113 sha:1070199a src:manual/17-esptool.md:258 klas:F -->
### T-17-113 · proza · рядок 258

**Книга каже, дослівно:**

> Не лікувати це запуском через `sudo`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-114 sha:7c5d9fa9 src:manual/17-esptool.md:261 klas:A -->
### T-17-114 · proza · рядок 261

**Книга каже, дослівно:**

> **`Device or resource busy`**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- **Дослівно з джерела:**
  > A fatal error occurred: Failed to connect to {chip}: {reason}
  > A fatal error occurred: Invalid head of packet (0x…)
  > 
  > (troubleshooting.rst)
  > The most common reason for "Failed to connect" is that the chip is not
  > in the download mode… Another cause is a running application writing
  > to the same UART.
  > 
  > (системні, не від esptool)
  > Permission denied: '/dev/ttyUSB0'      — права, група dialout
  > Device or resource busy: '/dev/ttyUSB0' — порт зайнятий іншою програмою
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 10), 2026-08-26
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-115 sha:d0ad404c src:manual/17-esptool.md:263 klas:F -->
### T-17-115 · proza · рядок 263

**Книга каже, дослівно:**

> Порт тримає інша програма: монітор, Arduino IDE, `screen`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-116 sha:cf4197d0 src:manual/17-esptool.md:263 klas:E -->
### T-17-116 · proza · рядок 263

**Книга каже, дослівно:**

> Одночасно порт відкриває лише один процес.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-117 sha:e7619250 src:manual/17-esptool.md:266 klas:A -->
### T-17-117 · proza · рядок 266

**Книга каже, дослівно:**

> **`A fatal error occurred: MD5 of file does not match data in flash!`**

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-17-118 sha:c6ae817f src:manual/17-esptool.md:268 klas:E -->
### T-17-118 · proza · рядок 268

**Книга каже, дослівно:**

> Записалося не те, що передавали.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-119 sha:dc7b5a5b src:manual/17-esptool.md:268 klas:E -->
### T-17-119 · proza · рядок 268

**Книга каже, дослівно:**

> Причини за частотою: погане живлення, довгий чи неякісний кабель, завелика швидкість, зношений флеш.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-120 sha:ea00dd94 src:manual/17-esptool.md:268 klas:F -->
### T-17-120 · proza · рядок 268

**Книга каже, дослівно:**

> Знизити `--baud`, повторити.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-121 sha:acad2592 src:manual/17-esptool.md:268 klas:E -->
### T-17-121 · proza · рядок 268

**Книга каже, дослівно:**

> Повторюється стабільно на тій самій адресі — підозра на пошкоджену комірку флешу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-122 sha:ec91ebc5 src:manual/17-esptool.md:273 klas:F -->
### T-17-122 · proza · рядок 273

**Книга каже, дослівно:**

> **`Invalid head of packet (0x00)`**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-123 sha:290a4865 src:manual/17-esptool.md:275 klas:E -->
### T-17-123 · proza · рядок 275

**Книга каже, дослівно:**

> Зв'язок є, але на лінії сміття.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-124 sha:5e738a7f src:manual/17-esptool.md:275 klas:A -->
### T-17-124 · proza · рядок 275

**Книга каже, дослівно:**

> Класично — плата стартує в застосунок, який сам щось пише в UART, поки `esptool` намагається говорити.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst, .../advanced-topics/boot-mode-selection.rst (Automatic Bootloader)
- **Дослівно з джерела:**
  > (basic-options.rst)
  > esptool has a two-stage flashing process: a small "stub" program is
  > uploaded to RAM and run, which then performs the requested operation
  > much faster than the ROM bootloader. ``--no-stub`` disables this.
  > 
  > (boot-mode-selection.rst, Automatic Bootloader)
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines of the serial connection.
  > 
  > (__init__.py)
  > This chip is {detected}, not {requested}. Wrong --chip argument?
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Чотири твердження розділу 17, які досі не мали доказу, бо стояли не в блоках коду, а в поясненнях: механізм stub, автоскидання через `DTR`/`RTS`, повідомлення про розбіжність чипа і причина «застосунок пише в UART».
Останнє варте уваги: воно пояснює `Invalid head of packet` із сусіднього запису — плата не мовчить, а говорить своє, і `esptool` бачить чуже в потоці. Дві половини одного симптому тепер обидві звірені.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-125 sha:c0befa74 src:manual/17-esptool.md:275 klas:E -->
### T-17-125 · proza · рядок 275

**Книга каже, дослівно:**

> Увійти в download mode вручну.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-126 sha:c229b138 src:manual/17-esptool.md:279 klas:A -->
### T-17-126 · proza · рядок 279

**Книга каже, дослівно:**

> **`This chip is ESP32-S3, not ESP32.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-17-127 sha:2d9087c4 src:manual/17-esptool.md:281 klas:A -->
### T-17-127 · proza · рядок 281

**Книга каже, дослівно:**

> `esptool` визначив чип сам і побачив розбіжність із тим, що йому сказали.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst, .../advanced-topics/boot-mode-selection.rst (Automatic Bootloader)
- **Дослівно з джерела:**
  > (basic-options.rst)
  > esptool has a two-stage flashing process: a small "stub" program is
  > uploaded to RAM and run, which then performs the requested operation
  > much faster than the ROM bootloader. ``--no-stub`` disables this.
  > 
  > (boot-mode-selection.rst, Automatic Bootloader)
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines of the serial connection.
  > 
  > (__init__.py)
  > This chip is {detected}, not {requested}. Wrong --chip argument?
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Чотири твердження розділу 17, які досі не мали доказу, бо стояли не в блоках коду, а в поясненнях: механізм stub, автоскидання через `DTR`/`RTS`, повідомлення про розбіжність чипа і причина «застосунок пише в UART».
Останнє варте уваги: воно пояснює `Invalid head of packet` із сусіднього запису — плата не мовчить, а говорить своє, і `esptool` бачить чуже в потоці. Дві половини одного симптому тепер обидві звірені.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-128 sha:efdb570a src:manual/17-esptool.md:281 klas:F -->
### T-17-128 · proza · рядок 281

**Книга каже, дослівно:**

> Прибрати `--chip`, дати визначити автоматично.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-129 sha:8a18dd3e src:manual/17-esptool.md:284 klas:F -->
### T-17-129 · proza · рядок 284

**Книга каже, дослівно:**

> **Плата лишається в download mode після прошивки** [[S3]] [[C3]]

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-130 sha:f7560ce0 src:manual/17-esptool.md:286 klas:E -->
### T-17-130 · proza · рядок 286

**Книга каже, дослівно:**

> Прошивка пройшла, а застосунок не стартував: чип так і сидить у завантажувачі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-131 sha:567f0570 src:manual/17-esptool.md:286 klas:A -->
### T-17-131 · proza · рядок 286

**Книга каже, дослівно:**

> На платах із native USB (картка [К3](#k-pidkl)) причина в тому, що скидання по лінії `RTS` через USB-Serial/JTAG не завжди спрацьовує — фізичної лінії там немає.

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

<!-- fc id:T-17-132 sha:f93a70ab src:manual/17-esptool.md:291 klas:F -->
### T-17-132 · proza · рядок 291

**Книга каже, дослівно:**

> Обхід — скидання внутрішнім watchdog замість `RTS`:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-133 sha:c2ed87c0 src:manual/17-esptool.md:293 klas:K -->
### T-17-133 · kod · рядок 293

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyACM0 --after watchdog-reset write-flash 0x0 vyrib.bin
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

<!-- fc id:T-17-134 sha:e196de7b src:manual/17-esptool.md:294 klas:A -->
### T-17-134 · kod-ryadok · рядок 294

**Книга каже, дослівно:**

> esptool --port /dev/ttyACM0 --after watchdog-reset write-flash 0x0 vyrib.bin

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

<!-- fc id:T-17-135 sha:10d41f6e src:manual/17-esptool.md:297 klas:A -->
### T-17-135 · proza · рядок 297

**Книга каже, дослівно:**

> Побічний ефект, до якого треба бути готовим: порт перелічується заново, і `/dev/ttyACM0` може стати `/dev/ttyACM1`.

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

<!-- fc id:T-17-136 sha:6ac44b20 src:manual/17-esptool.md:297 klas:E -->
### T-17-136 · proza · рядок 297

**Книга каже, дослівно:**

> Монітор доведеться відкрити на новому імені.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-137 sha:59239464 src:manual/17-esptool.md:301 klas:F -->
### T-17-137 · proza · рядок 301

**Книга каже, дослівно:**

> На ESP32 classic, C6 і H2 цього режиму немає — там працює звичайне `hard-reset` по `RTS`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-138 sha:391b6f3d src:manual/17-esptool.md:304 klas:A -->
### T-17-138 · proza · рядок 304

**Книга каже, дослівно:**

> **`Failed to start stub flasher.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-17-139 sha:2d2315ba src:manual/17-esptool.md:304 klas:E -->
### T-17-139 · proza · рядок 304

**Книга каже, дослівно:**

> There was no response.`**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-140 sha:6f4d2986 src:manual/17-esptool.md:306 klas:A -->
### T-17-140 · proza · рядок 306

**Книга каже, дослівно:**

> `esptool` вантажить у RAM невелику допоміжну програму («stub») для пришвидшення.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst, .../advanced-topics/boot-mode-selection.rst (Automatic Bootloader)
- **Дослівно з джерела:**
  > (basic-options.rst)
  > esptool has a two-stage flashing process: a small "stub" program is
  > uploaded to RAM and run, which then performs the requested operation
  > much faster than the ROM bootloader. ``--no-stub`` disables this.
  > 
  > (boot-mode-selection.rst, Automatic Bootloader)
  > esptool can automatically reset the board into bootloader mode … using
  > the DTR and RTS lines of the serial connection.
  > 
  > (__init__.py)
  > This chip is {detected}, not {requested}. Wrong --chip argument?
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Чотири твердження розділу 17, які досі не мали доказу, бо стояли не в блоках коду, а в поясненнях: механізм stub, автоскидання через `DTR`/`RTS`, повідомлення про розбіжність чипа і причина «застосунок пише в UART».
Останнє варте уваги: воно пояснює `Invalid head of packet` із сусіднього запису — плата не мовчить, а говорить своє, і `esptool` бачить чуже в потоці. Дві половини одного симптому тепер обидві звірені.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-141 sha:4a61aa2a src:manual/17-esptool.md:306 klas:E -->
### T-17-141 · proza · рядок 306

**Книга каже, дослівно:**

> На частині клонів це не працює.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-142 sha:6c0640de src:manual/17-esptool.md:306 klas:F -->
### T-17-142 · proza · рядок 306

**Книга каже, дослівно:**

> Обійти: `--no-stub`, буде повільніше, але працюватиме.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-143 sha:0df8e570 src:manual/17-esptool.md:310 klas:A -->
### T-17-143 · proza · рядок 310

**Книга каже, дослівно:**

> Сусіднє попередження `Stub flasher has been disabled for compatibility, set --no-stub to suppress this warning.` — не помилка: `esptool` сам вимкнув stub і працює далі.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- **Дослівно з джерела:**
  > (v5 loader.py)
  > raise FatalError(f"Failed to connect to {self.CHIP_NAME}: {last_error}" …)
  > msg = ("Serial data stream stopped: Possible serial noise or corruption."
  >        if successful_slip else "No serial data received.")
  > raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wrong chip argument?")
  > raise FatalError("Failed to start stub flasher. There was no response.\n" …)
  > log.warn("Stub flasher has been disabled for compatibility, "
  >          "set --no-stub to suppress this warning.")
  > 
  > (cmds.py)
  > raise FatalError("MD5 of file does not match data in flash!")
  > 
  > (v4.8.1 loader.py — для порівняння)
  > "This chip is %s not %s. Wrong --chip argument?"
  > "Failed to start stub. There was no response."
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Чотири виправлення разом, і всі однакової природи: книга наводила тексти esptool 3.x, які застаріли на дві мажорні версії.
`Timed out waiting for packet header` → `No serial data received.` Це найчастіша помилка взагалі, і книга сама називає її найчастішою.
`This chip is X not Y` → `This chip is X, not Y. Wrong chip argument?` — з комою, якої не було, і без дефісів у `--chip` (у v4 було `Wrong --chip argument?`).
`Stub is disabled` / `Failed to run stub` → таких рядків немає зовсім; є `Failed to start stub flasher.` і окреме попередження `Stub flasher has been disabled for compatibility…`, яке взагалі не помилка.
`MD5 does not match` — теж не існує як рядок: у тексті `MD5 of file does not match data in flash!` немає підрядка `MD5 does not match`. Тобто пошук у логу давав порожньо. Виправлено в п'яти місцях книги.
Висновок ширший за самі рядки: книга вже розрізняє синтаксис v4 і v5 у командах, але тексти помилок лишалися від старішої версії. Тепер там, де формулювання розійшлися помітно, названо обидва.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-17-144 sha:d286f7b3 src:manual/17-esptool.md:314 klas:F -->
### T-17-144 · proza · рядок 314

**Книга каже, дослівно:**

> У v4 ті самі рядки коротші — `Failed to start stub.` Шукати варто за словом `stub`, а не за повним реченням.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-145 sha:2a9519b0 src:manual/17-esptool.md:319 klas:E -->
### T-17-145 · proza · рядок 319

**Книга каже, дослівно:**

> Espressif дає графічну програму (Flash Download Tool) — той самий функціонал у вікні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-146 sha:918d6503 src:manual/17-esptool.md:319 klas:E -->
### T-17-146 · proza · рядок 319

**Книга каже, дослівно:**

> Вона зручна там, де прошивку заливає людина без командного рядка: оператор на складанні, замовник, колега.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-147 sha:313ef396 src:manual/17-esptool.md:323 klas:F -->
### T-17-147 · proza · рядок 323

**Книга каже, дослівно:**

> Практично: підготувати `merge-bin`-образ, налаштувати один раз, зберегти конфігурацію і передати разом з інструкцією на одну сторінку (розділ 56).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-148 sha:e977c57d src:manual/17-esptool.md:323 klas:E -->
### T-17-148 · proza · рядок 323

**Книга каже, дослівно:**

> Все, що складніше, робиться з командного рядка — його простіше відтворити і покласти в скрипт.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-149 sha:2d322667 src:manual/17-esptool.md:330 klas:F -->
### T-17-149 · proza · рядок 330

**Книга каже, дослівно:**

> Перевірити версію `esptool` **перш ніж** копіювати команду звідкись.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-150 sha:8eda1231 src:manual/17-esptool.md:332 klas:B -->
### T-17-150 · proza · рядок 332

**Книга каже, дослівно:**

> `chip-id` і `flash-id` — перші дві команди для будь-якої незнайомої плати.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/index.rst та .../esptool/basic-commands.rst
- **Дослівно з джерела:**
  > esptool is a Python-based, open-source, platform-independent utility to
  > communicate with the ROM bootloader in Espressif chips.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і це свідомо. Дослівно з джерела випливає лише перше твердження — що `esptool` розмовляє з ROM-бутлоадером.
Решта («перші дві команди для незнайомої плати», «дамп до першої зміни», «доки чип відповідає на `chip-id`, він живий») — **порядок дій**, який випливає з властивостей команд однозначно, але в жодному документі так не сформульований. Це рекомендація книги, побудована на звірених фактах, і чесний клас для неї — `B`.
Записую це окремо, бо спокуса поставити `A` тут така сама, як була з JTAG-пінами в проході 20: твердження здається загальновідомим і безсумнівним. Але «безсумнівне» і «процитоване» — різні класи.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-151 sha:a7f08f37 src:manual/17-esptool.md:334 klas:B -->
### T-17-151 · proza · рядок 334

**Книга каже, дослівно:**

> `read-flash` робиться до першої зміни.

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/index.rst та .../esptool/basic-commands.rst
- **Дослівно з джерела:**
  > esptool is a Python-based, open-source, platform-independent utility to
  > communicate with the ROM bootloader in Espressif chips.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Клас `B`, а не `A`, і це свідомо. Дослівно з джерела випливає лише перше твердження — що `esptool` розмовляє з ROM-бутлоадером.
Решта («перші дві команди для незнайомої плати», «дамп до першої зміни», «доки чип відповідає на `chip-id`, він живий») — **порядок дій**, який випливає з властивостей команд однозначно, але в жодному документі так не сформульований. Це рекомендація книги, побудована на звірених фактах, і чесний клас для неї — `B`.
Записую це окремо, бо спокуса поставити `A` тут така сама, як була з JTAG-пінами в проході 20: твердження здається загальновідомим і безсумнівним. Але «безсумнівне» і «процитоване» — різні класи.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-152 sha:0de9cf8b src:manual/17-esptool.md:334 klas:E -->
### T-17-152 · proza · рядок 334

**Книга каже, дослівно:**

> Розмір файлу звіряється з обсягом флешу одразу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-17-153 sha:42368b26 src:manual/17-esptool.md:337 klas:A -->
### T-17-153 · proza · рядок 337

**Книга каже, дослівно:**

> `verify-flash` перетворює «прошилося» на «у флеші лежить те, що треба».

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

<!-- fc id:T-17-154 sha:33a8f7c8 src:manual/17-esptool.md:339 klas:A -->
### T-17-154 · proza · рядок 339

**Книга каже, дослівно:**

> `merge-bin` — формат передачі прошивки людині, яка не мусить знати адрес.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > def merge_bin_cli(ctx, addr_filename, **kwargs):
  >     """Merge multiple raw binary files into a single flashable file."""
  >     if ctx.obj["chip"] == "auto":
  >         raise FatalError(
  >             f"Specify the --chip argument (choose from {', '.join(CHIP_LIST)})."
  >         )
  > 
  > (basic-commands.rst)
  > The ``merge-bin`` command will merge multiple binary files … Any gaps
  > between the input files are padded with 0xFF bytes.
  > Options such as ``--flash-mode``, ``--flash-size`` and ``--flash-freq``
  > are used to set the corresponding values in the image header, exactly
  > as they would be when flashing.
- **Спосіб і дата:** curl raw.githubusercontent (повторно, прохід 9), 2026-08-26
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---
