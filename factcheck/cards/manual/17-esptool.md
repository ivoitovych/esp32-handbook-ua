# Фактчекінг: `manual/17-esptool.md`

Одиниць твердження: **165**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-17-001 sha:760be9ee src:manual/17-esptool.md:3 klas:B -->
### T-17-001 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `esptool` — програма, що розмовляє з ROM-бутлоадером чипа.

**Контекст**

```
# 17. esptool {#esptool}

`esptool` — програма, що розмовляє з ROM-бутлоадером чипа. Вона не знає
нічого про ваш проєкт, не потребує встановленого ESP-IDF і працює з
будь-якою платою на ESP32, включно з тією, прошивку якої зібрав хтось
інший десять років тому.
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
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
### T-17-002 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Вона не знає нічого про ваш проєкт, не потребує встановленого ESP-IDF і працює з будь-якою платою на ESP32, включно з тією, прошивку якої зібрав хтось інший десять років тому.

**Контекст**

```
# 17. esptool {#esptool}

`esptool` — програма, що розмовляє з ROM-бутлоадером чипа. Вона не знає
нічого про ваш проєкт, не потребує встановленого ESP-IDF і працює з
будь-якою платою на ESP32, включно з тією, прошивку якої зібрав хтось
інший десять років тому.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-003 sha:8ea7354e src:manual/17-esptool.md:8 klas:E -->
### T-17-003 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Це головний інструмент для всього, що стосується чужого заліза: визначити чип, зняти дамп, залити готовий образ, стерти.

**Контекст**

```
# 17. esptool {#esptool}

Це головний інструмент для всього, що стосується чужого заліза: визначити
чип, зняти дамп, залити готовий образ, стерти. Якщо з плати можна взяти
хоч щось — це буде через `esptool`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-004 sha:9395569b src:manual/17-esptool.md:9 klas:B -->
### T-17-004 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Якщо з плати можна взяти хоч щось — це буде через `esptool`.

**Контекст**

```
# 17. esptool {#esptool}

Це головний інструмент для всього, що стосується чужого заліза: визначити
чип, зняти дамп, залити готовий образ, стерти. Якщо з плати можна взяти
хоч щось — це буде через `esptool`.
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
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
### T-17-005 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Перше, що треба з'ясувати, — яка версія у вас:

**Контекст**

```
## Дві версії з несумісним синтаксисом

Перше, що треба з'ясувати, — яка версія у вас:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-006 sha:64f486d7 src:manual/17-esptool.md:16 klas:K -->
### T-17-006 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool version
> ```

**Контекст**

````
## Дві версії з несумісним синтаксисом

```
esptool version
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-007 sha:fcbae1b9 src:manual/17-esptool.md:17 klas:A -->
### T-17-007 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool version

**Контекст**

````
## Дві версії з несумісним синтаксисом

```
esptool version
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-008 sha:9c3eef10 src:manual/17-esptool.md:20 klas:E -->
### T-17-008 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Команда друкує номер версії — це і є відповідь.

**Контекст**

```
## Дві версії з несумісним синтаксисом

Команда друкує номер версії — це і є відповідь. Якщо `esptool` не
знайдено взагалі, спробувати `esptool.py version`: у v4 інакшого імені
немає. Зворотне не працює: у v5 обидва імені є, і те, що команда
запустилася під іменем `esptool.py`, ще нічого не означає — дивитися
треба на надрукований номер.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-009 sha:ea8f78cc src:manual/17-esptool.md:20 klas:A -->
### T-17-009 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Якщо `esptool` не знайдено взагалі, спробувати `esptool.py version`: у v4 інакшого імені немає.

**Контекст**

```
## Дві версії з несумісним синтаксисом

Команда друкує номер версії — це і є відповідь. Якщо `esptool` не
знайдено взагалі, спробувати `esptool.py version`: у v4 інакшого імені
немає. Зворотне не працює: у v5 обидва імені є, і те, що команда
запустилася під іменем `esptool.py`, ще нічого не означає — дивитися
треба на надрукований номер.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-010 sha:790431ab src:manual/17-esptool.md:22 klas:A -->
### T-17-010 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Зворотне не працює: у v5 обидва імені є, і те, що команда запустилася під іменем `esptool.py`, ще нічого не означає — дивитися треба на надрукований номер.

**Контекст**

```
## Дві версії з несумісним синтаксисом

Команда друкує номер версії — це і є відповідь. Якщо `esptool` не
знайдено взагалі, спробувати `esptool.py version`: у v4 інакшого імені
немає. Зворотне не працює: у v5 обидва імені є, і те, що команда
запустилася під іменем `esptool.py`, ще нічого не означає — дивитися
треба на надрукований номер.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
### T-17-011 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають копіювання команд з інтернету:

**Контекст**

```
## Дві версії з несумісним синтаксисом

**esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають
копіювання команд з інтернету:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-012 sha:0e9fb3f8 src:manual/17-esptool.md:29 klas:A -->
### T-17-012 · tablycya-shapka · `manual/17-esptool.md`

**Твердження, коротко**

> | | v4 і раніше | v5 |

**Контекст**

```
## Дві версії з несумісним синтаксисом

**esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають
копіювання команд з інтернету:

| | v4 і раніше | v5 |
|---|---|---|
| виклик | `esptool.py` | `esptool` |
| команди | `write_flash`, `chip_id` | `write-flash`, `chip-id` |
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-013 sha:e59d8c4e src:manual/17-esptool.md:31 klas:A -->
### T-17-013 · komirka · `manual/17-esptool.md`

**Твердження, коротко**

> виклик · v4 і раніше → `esptool.py`

**Дослівно з книги**

```
| виклик | `esptool.py` | `esptool` |
```

**Контекст**

```
## Дві версії з несумісним синтаксисом

**esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають
копіювання команд з інтернету:

| | v4 і раніше | v5 |
|---|---|---|
| виклик | `esptool.py` | `esptool` |
| команди | `write_flash`, `chip_id` | `write-flash`, `chip-id` |
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-014 sha:15c8ed07 src:manual/17-esptool.md:31 klas:A -->
### T-17-014 · komirka · `manual/17-esptool.md`

**Твердження, коротко**

> виклик · v5 → `esptool`

**Дослівно з книги**

```
| виклик | `esptool.py` | `esptool` |
```

**Контекст**

```
## Дві версії з несумісним синтаксисом

**esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають
копіювання команд з інтернету:

| | v4 і раніше | v5 |
|---|---|---|
| виклик | `esptool.py` | `esptool` |
| команди | `write_flash`, `chip_id` | `write-flash`, `chip-id` |
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst та .../docs/en/migration-guide.rst; перелік команд у esptool/__init__.py
- **Дослівно з джерела:**
  > (перехід на v5)
  > The `esptool.py` name is kept as an alias; the recommended entry point
  > is `esptool`. Command names use dashes: `write-flash`, `read-flash`,
  > `erase-flash`, `merge-bin`. The underscore forms are deprecated and
  > print a warning.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Не нова звірка. Іменування перевірено в проході 9, несиметричність міграції — у проході 6 (і записана в реєстр спростованого). Тут лише розширено досяжність на прозу й таблиці: «Перевірити своє: `esptool version`» у картках К5, К10 і додатку C, рядки таблиці «виклик · v4 / v5», а також попередження, що в v4 імені `esptool` без `.py` немає.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-17-015 sha:f36c79a8 src:manual/17-esptool.md:32 klas:A -->
### T-17-015 · komirka · `manual/17-esptool.md`

**Твердження, коротко**

> команди · v4 і раніше → `write_flash`, `chip_id`

**Дослівно з книги**

```
| команди | `write_flash`, `chip_id` | `write-flash`, `chip-id` |
```

**Контекст**

```
## Дві версії з несумісним синтаксисом

**esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають
копіювання команд з інтернету:

| | v4 і раніше | v5 |
|---|---|---|
| виклик | `esptool.py` | `esptool` |
| команди | `write_flash`, `chip_id` | `write-flash`, `chip-id` |
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-016 sha:4fe690f3 src:manual/17-esptool.md:32 klas:A -->
### T-17-016 · komirka · `manual/17-esptool.md`

**Твердження, коротко**

> команди · v5 → `write-flash`, `chip-id`

**Дослівно з книги**

```
| команди | `write_flash`, `chip_id` | `write-flash`, `chip-id` |
```

**Контекст**

```
## Дві версії з несумісним синтаксисом

**esptool v5** змінив командний рядок у двох місцях, і обидві зміни ламають
копіювання команд з інтернету:

| | v4 і раніше | v5 |
|---|---|---|
| виклик | `esptool.py` | `esptool` |
| команди | `write_flash`, `chip_id` | `write-flash`, `chip-id` |
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
### T-17-017 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Переважна більшість інструкцій, статей і відповідей на форумах написана під v4, і напрямки несиметричні.

**Контекст**

```
## Дві версії з несумісним синтаксисом

Переважна більшість інструкцій, статей і відповідей на форумах написана
під v4, і напрямки несиметричні.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-018 sha:5b950f2b src:manual/17-esptool.md:37 klas:F -->
### T-17-018 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **Стара команда на новій версії поки що працює.** У v5 старі імена позначені як застарілі: виконуються з попередженням і будуть прибрані в наступному major-релізі.

**Контекст**

```
## Дві версії з несумісним синтаксисом

**Стара команда на новій версії поки що працює.** У v5 старі імена
позначені як застарілі: виконуються з попередженням і будуть прибрані в
наступному major-релізі. Тобто `write_flash` на v5 спрацює — і тим
неприємніше буде, коли одного дня перестане.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-019 sha:2b706815 src:manual/17-esptool.md:39 klas:A -->
### T-17-019 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Тобто `write_flash` на v5 спрацює — і тим неприємніше буде, коли одного дня перестане.

**Контекст**

```
## Дві версії з несумісним синтаксисом

**Стара команда на новій версії поки що працює.** У v5 старі імена
позначені як застарілі: виконуються з попередженням і будуть прибрані в
наступному major-релізі. Тобто `write_flash` на v5 спрацює — і тим
неприємніше буде, коли одного дня перестане.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
### T-17-020 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **Нова команда на старій версії не працює.** `write-flash` на v4 дає «невідома команда», і це збиває з пантелику: команда відома, просто пишеться інакше.

**Контекст**

```
## Дві версії з несумісним синтаксисом

**Нова команда на старій версії не працює.** `write-flash` на v4 дає
«невідома команда», і це збиває з пантелику: команда відома, просто
пишеться інакше.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
### T-17-021 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Перейменування торкнулося не лише команд, а й **опцій**: `--flash_size`, `--flash_mode`, `--flash_freq`, а також значень `--before` і `--after`.

**Контекст**

```
## Дві версії з несумісним синтаксисом

Перейменування торкнулося не лише команд, а й **опцій**: `--flash_size`,
`--flash_mode`, `--flash_freq`, а також значень `--before` і `--after`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
### T-17-022 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **У цьому довіднику команди подаються в синтаксисі v5.** Щоб отримати варіант для v4: замінити дефіси на підкреслення і додати `.py`.

**Контекст**

```
## Дві версії з несумісним синтаксисом

**У цьому довіднику команди подаються в синтаксисі v5.** Щоб отримати
варіант для v4: замінити дефіси на підкреслення і додати `.py`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
### T-17-023 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Версія `esptool` залежить не від вашого вибору, а від того, звідки вона взялася.

**Контекст**

```
## Дві версії з несумісним синтаксисом

::: uvaha
Версія `esptool` залежить не від вашого вибору, а від того, звідки вона
взялася. Разом з ESP-IDF 5.x іде v4, разом з ESP-IDF 6.x — v5. Встановлена
окремо через `pip` — та, що була свіжою на момент встановлення. Якщо у вас
на машині є і те, і те, `esptool` і `esptool.py` можуть бути **різних
версій** — це джерело дуже дивних годин.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst та .../docs/en/migration-guide.rst; перелік команд у esptool/__init__.py
- **Дослівно з джерела:**
  > (перехід на v5)
  > The `esptool.py` name is kept as an alias; the recommended entry point
  > is `esptool`. Command names use dashes: `write-flash`, `read-flash`,
  > `erase-flash`, `merge-bin`. The underscore forms are deprecated and
  > print a warning.
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Не нова звірка. Іменування перевірено в проході 9, несиметричність міграції — у проході 6 (і записана в реєстр спростованого). Тут лише розширено досяжність на прозу й таблиці: «Перевірити своє: `esptool version`» у картках К5, К10 і додатку C, рядки таблиці «виклик · v4 / v5», а також попередження, що в v4 імені `esptool` без `.py` немає.
- **Прохід:** pass-28-komandy-suciljno

---

<!-- fc id:T-17-024 sha:a5e9385a src:manual/17-esptool.md:54 klas:A -->
### T-17-024 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Разом з ESP-IDF 5.x іде v4, разом з ESP-IDF 6.x — v5.

**Контекст**

```
## Дві версії з несумісним синтаксисом

::: uvaha
Версія `esptool` залежить не від вашого вибору, а від того, звідки вона
взялася. Разом з ESP-IDF 5.x іде v4, разом з ESP-IDF 6.x — v5. Встановлена
окремо через `pip` — та, що була свіжою на момент встановлення. Якщо у вас
на машині є і те, і те, `esptool` і `esptool.py` можуть бути **різних
версій** — це джерело дуже дивних годин.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-025 sha:5d432647 src:manual/17-esptool.md:54 klas:F -->
### T-17-025 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Встановлена окремо через `pip` — та, що була свіжою на момент встановлення.

**Контекст**

```
## Дві версії з несумісним синтаксисом

::: uvaha
Версія `esptool` залежить не від вашого вибору, а від того, звідки вона
взялася. Разом з ESP-IDF 5.x іде v4, разом з ESP-IDF 6.x — v5. Встановлена
окремо через `pip` — та, що була свіжою на момент встановлення. Якщо у вас
на машині є і те, і те, `esptool` і `esptool.py` можуть бути **різних
версій** — це джерело дуже дивних годин.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-026 sha:8e12e7bb src:manual/17-esptool.md:55 klas:A -->
### T-17-026 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Якщо у вас на машині є і те, і те, `esptool` і `esptool.py` можуть бути **різних версій** — це джерело дуже дивних годин.

**Контекст**

```
## Дві версії з несумісним синтаксисом

::: uvaha
Версія `esptool` залежить не від вашого вибору, а від того, звідки вона
взялася. Разом з ESP-IDF 5.x іде v4, разом з ESP-IDF 6.x — v5. Встановлена
окремо через `pip` — та, що була свіжою на момент встановлення. Якщо у вас
на машині є і те, і те, `esptool` і `esptool.py` можуть бути **різних
версій** — це джерело дуже дивних годин.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-027 sha:e66c9553 src:manual/17-esptool.md:62 klas:K -->
### T-17-027 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 flash-id
> ```

**Контекст**

````
## Мінімум, з якого починається все

```
esptool --port /dev/ttyUSB0 flash-id
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** source-cache/9d5cf303-basic-options.rst
- **Дослівно з джерела:**
  > The serial port is selected using the ``-p`` option, like ``-p /dev/ttyUSB0`` (Linux and macOS) or ``-p COM1`` (Windows).
- **Спосіб і дата:** Source document retrieved 2026-08-26 from the local cache; quote verified against it by substring match.
- **Нотатка:** Помічник поставив ne_znayshov, і за своїм нарядом мав рацію: йому дали basic-commands.rst, де є `esptool flash-id` без опцій. Опція ж описана в basic-options.rst — сусідньому файлі того ж кешу, якого наряд не назвав. Заголовок розділу подає обидві форми, `--port` і `-p`; книга вживає довгу. Команда в книзі точна. Урок не про помічника, а про наряд: один ключ мусить вести до всіх файлів свого документа, бо документація esptool розкладена на команди й опції окремо.
- **Прохід:** m2-wave2

---

<!-- fc id:T-17-028 sha:4c5a16ee src:manual/17-esptool.md:63 klas:A -->
### T-17-028 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 flash-id

**Контекст**

````
## Мінімум, з якого починається все

```
esptool --port /dev/ttyUSB0 flash-id
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** source-cache/9d5cf303-basic-options.rst
- **Дослівно з джерела:**
  > The serial port is selected using the ``-p`` option, like ``-p /dev/ttyUSB0`` (Linux and macOS) or ``-p COM1`` (Windows).
- **Спосіб і дата:** Source document retrieved 2026-08-26 from the local cache; quote verified against it by substring match.
- **Нотатка:** Помічник поставив ne_znayshov, і за своїм нарядом мав рацію: йому дали basic-commands.rst, де є `esptool flash-id` без опцій. Опція ж описана в basic-options.rst — сусідньому файлі того ж кешу, якого наряд не назвав. Заголовок розділу подає обидві форми, `--port` і `-p`; книга вживає довгу. Команда в книзі точна. Урок не про помічника, а про наряд: один ключ мусить вести до всіх файлів свого документа, бо документація esptool розкладена на команди й опції окремо.
- **Прохід:** m2-wave2

---

<!-- fc id:T-17-029 sha:8d78f5b3 src:manual/17-esptool.md:66 klas:A -->
### T-17-029 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Перед виконанням **будь-якої** команди `esptool` встановлює зв'язок і друкує шапку з тим, що знайшов:

**Контекст**

```
## Мінімум, з якого починається все

Перед виконанням **будь-якої** команди `esptool` встановлює зв'язок і
друкує шапку з тим, що знайшов:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > # 2) Print the chip info
  > ...
  > else:
  >     log.print(f"{'Chip type:':<20}{esp.get_chip_description()}")
  >     log.print(f"{'Features:':<20}{', '.join(esp.get_chip_features())}")
  >     log.print(f"{'Crystal frequency:':<20}{esp.get_crystal_freq()}MHz")
  >     usb_mode = esp.get_usb_mode()
  >     if usb_mode is not None:
  >         log.print(f"{'USB mode:':<20}{usb_mode}")
  >     read_mac(esp)
- **Спосіб і дата:** curl raw.githubusercontent, перевірено М1, 2026-08-26
- **Нотатка:** Цей блок виконується **до** виклику підкоманди й не залежить від того, яка вона. Тому будь-яка команда, що взагалі під'єдналася, уже назвала сімейство, ревізію, частоту кристала й MAC.
Практичний наслідок для книги виявився ширшим за виправлення: правило «перша команда для незнайомої плати» тепер `flash-id` не тому, що вона краще ідентифікує чип, а тому, що вона додає до безкоштовної шапки те єдине, чого в шапці немає, — обсяг флешу.
Виправлено в одинадцяти місцях: розділи 08, 17, 20, 21, 23, картки К1 і К10, додаток C, дві вкладки. Формулювання заведено в `factcheck/SPROSTOVANE.md`, взірець випробувано вставкою старої фрази в розділ 23 — знаходиться.
Виняток у взірці на `manual/17-esptool.md` навмисний: розділ 17 тепер **пояснює**, чому команди краще не вживати, і мусить цитувати її назву.
- **Прохід:** pass-36-chip-id

---

<!-- fc id:T-17-030 sha:fd4dd926 src:manual/17-esptool.md:69 klas:K -->
### T-17-030 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> Chip type:          ESP32-D0WD-V3 (revision v3.1)
> Features:           WiFi, BT, Dual Core, 240MHz, ...
> Crystal frequency:  40MHz
> MAC:                24:6f:28:xx:xx:xx
> ```

**Контекст**

````
## Мінімум, з якого починається все

```
Chip type:          ESP32-D0WD-V3 (revision v3.1)
Features:           WiFi, BT, Dual Core, 240MHz, ...
Crystal frequency:  40MHz
MAC:                24:6f:28:xx:xx:xx
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > # 2) Print the chip info
  > ...
  > else:
  >     log.print(f"{'Chip type:':<20}{esp.get_chip_description()}")
  >     log.print(f"{'Features:':<20}{', '.join(esp.get_chip_features())}")
  >     log.print(f"{'Crystal frequency:':<20}{esp.get_crystal_freq()}MHz")
  >     usb_mode = esp.get_usb_mode()
  >     if usb_mode is not None:
  >         log.print(f"{'USB mode:':<20}{usb_mode}")
  >     read_mac(esp)
- **Спосіб і дата:** curl raw.githubusercontent, перевірено М1, 2026-08-26
- **Нотатка:** Цей блок виконується **до** виклику підкоманди й не залежить від того, яка вона. Тому будь-яка команда, що взагалі під'єдналася, уже назвала сімейство, ревізію, частоту кристала й MAC.
Практичний наслідок для книги виявився ширшим за виправлення: правило «перша команда для незнайомої плати» тепер `flash-id` не тому, що вона краще ідентифікує чип, а тому, що вона додає до безкоштовної шапки те єдине, чого в шапці немає, — обсяг флешу.
Виправлено в одинадцяти місцях: розділи 08, 17, 20, 21, 23, картки К1 і К10, додаток C, дві вкладки. Формулювання заведено в `factcheck/SPROSTOVANE.md`, взірець випробувано вставкою старої фрази в розділ 23 — знаходиться.
Виняток у взірці на `manual/17-esptool.md` навмисний: розділ 17 тепер **пояснює**, чому команди краще не вживати, і мусить цитувати її назву.
- **Прохід:** pass-36-chip-id

---

<!-- fc id:T-17-031 sha:54872a10 src:manual/17-esptool.md:76 klas:E -->
### T-17-031 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Сімейство, ревізія кремнію і MAC — саме тут.

**Контекст**

```
## Мінімум, з якого починається все

Сімейство, ревізія кремнію і MAC — саме тут. Це не результат команди, а
**преамбула з'єднання**, спільна для всіх команд. Тому будь-яка команда,
що взагалі під'єдналася, вже сказала, з чим маєте справу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-032 sha:b339a1c4 src:manual/17-esptool.md:76 klas:A -->
### T-17-032 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Це не результат команди, а **преамбула з'єднання**, спільна для всіх команд.

**Контекст**

```
## Мінімум, з якого починається все

Сімейство, ревізія кремнію і MAC — саме тут. Це не результат команди, а
**преамбула з'єднання**, спільна для всіх команд. Тому будь-яка команда,
що взагалі під'єдналася, вже сказала, з чим маєте справу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > # 2) Print the chip info
  > ...
  > else:
  >     log.print(f"{'Chip type:':<20}{esp.get_chip_description()}")
  >     log.print(f"{'Features:':<20}{', '.join(esp.get_chip_features())}")
  >     log.print(f"{'Crystal frequency:':<20}{esp.get_crystal_freq()}MHz")
  >     usb_mode = esp.get_usb_mode()
  >     if usb_mode is not None:
  >         log.print(f"{'USB mode:':<20}{usb_mode}")
  >     read_mac(esp)
- **Спосіб і дата:** curl raw.githubusercontent, перевірено М1, 2026-08-26
- **Нотатка:** Цей блок виконується **до** виклику підкоманди й не залежить від того, яка вона. Тому будь-яка команда, що взагалі під'єдналася, уже назвала сімейство, ревізію, частоту кристала й MAC.
Практичний наслідок для книги виявився ширшим за виправлення: правило «перша команда для незнайомої плати» тепер `flash-id` не тому, що вона краще ідентифікує чип, а тому, що вона додає до безкоштовної шапки те єдине, чого в шапці немає, — обсяг флешу.
Виправлено в одинадцяти місцях: розділи 08, 17, 20, 21, 23, картки К1 і К10, додаток C, дві вкладки. Формулювання заведено в `factcheck/SPROSTOVANE.md`, взірець випробувано вставкою старої фрази в розділ 23 — знаходиться.
Виняток у взірці на `manual/17-esptool.md` навмисний: розділ 17 тепер **пояснює**, чому команди краще не вживати, і мусить цитувати її назву.
- **Прохід:** pass-36-chip-id

---

<!-- fc id:T-17-033 sha:ccd8cd11 src:manual/17-esptool.md:77 klas:E -->
### T-17-033 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Тому будь-яка команда, що взагалі під'єдналася, вже сказала, з чим маєте справу.

**Контекст**

```
## Мінімум, з якого починається все

Сімейство, ревізія кремнію і MAC — саме тут. Це не результат команди, а
**преамбула з'єднання**, спільна для всіх команд. Тому будь-яка команда,
що взагалі під'єдналася, вже сказала, з чим маєте справу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-034 sha:d76dc54c src:manual/17-esptool.md:80 klas:A -->
### T-17-034 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `flash-id` як перша команда зручна тим, що після шапки додає ще й те, що однаково знадобиться далі: виробник і **обсяг** флешу.

**Контекст**

```
## Мінімум, з якого починається все

`flash-id` як перша команда зручна тим, що після шапки додає ще й те, що
однаково знадобиться далі: виробник і **обсяг** флешу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** source-cache/2217d639-basic-commands.rst
- **Дослівно з джерела:**
  > esptool flash-id
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує flash-id як команду, яка показує флеш інформацію.
- **Прохід:** m2-wave3

---

<!-- fc id:T-17-035 sha:8528068a src:manual/17-esptool.md:84 klas:A -->
### T-17-035 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **Чому не `chip-id`.** Підкоманда з такою назвою існує, але вона успадкована від ESP8266, у якого справді був окремий Chip ID в efuse.

**Контекст**

```
## Мінімум, з якого починається все

::: uvaha
**Чому не `chip-id`.** Підкоманда з такою назвою існує, але вона
успадкована від ESP8266, у якого справді був окремий Chip ID в efuse. У
жодного чипа сімейства ESP32 його немає, і `esptool` на ньому відповідає
попередженням:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/cmds.py, .../esptool/loader.py, .../esptool/targets/esp8266.py
- **Дослівно з джерела:**
  > (cmds.py)
  > def chip_id(esp: ESPLoader) -> None:
  >     """
  >     Read and display the Chip ID of the ESP device if available,
  >     otherwise fall back to displaying the MAC address.
  >     """
  >     try:
  >         chipid = esp.chip_id()
  >         log.print(f"Chip ID: {chipid:#010x}")
  >     except NotSupportedError:
  >         log.warn(f"{esp.CHIP_NAME} has no chip ID. "
  >                  "Reading MAC address instead.")
  >         read_mac(esp)
  > 
  > (loader.py — базовий клас ESPLoader)
  > def chip_id(self):
  >     raise NotSupportedError(self, "Function chip_id")
  > 
  > (targets/esp8266.py — єдине перевизначення в дереві)
  > def chip_id(self):
  >     """
  >     Read Chip ID from efuse - the equivalent of the SDK
  >     system_get_chip_id() func
  >     """
  >     id0 = self.read_reg(self.ESP_OTP_MAC0)
  >     id1 = self.read_reg(self.ESP_OTP_MAC1)
  >     return (id0 >> 24) | ((id1 & 0xFFFFFF) << 8)
- **Спосіб і дата:** curl raw.githubusercontent — знахідку подав агент пулу (шматок 8), джерело перевірене М1 самостійно, 2026-08-26
- **Нотатка:** `chip_id()` визначено рівно в двох місцях усього дерева `esptool`: у базовому класі, де він кидає `NotSupportedError`, і в `esp8266.py`, де він справді читає efuse. Жоден цільовий клас сімейства ESP32 його не перевизначає.
Отже підкоманда — залишок від ESP8266, у якого окремий Chip ID був. На ESP32 вона друкує попередження і MAC.
- **Прохід:** pass-36-chip-id

---

<!-- fc id:T-17-036 sha:6b2c3582 src:manual/17-esptool.md:85 klas:F -->
### T-17-036 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> У жодного чипа сімейства ESP32 його немає, і `esptool` на ньому відповідає попередженням:

**Контекст**

```
## Мінімум, з якого починається все

::: uvaha
**Чому не `chip-id`.** Підкоманда з такою назвою існує, але вона
успадкована від ESP8266, у якого справді був окремий Chip ID в efuse. У
жодного чипа сімейства ESP32 його немає, і `esptool` на ньому відповідає
попередженням:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-037 sha:9dc5958c src:manual/17-esptool.md:89 klas:K -->
### T-17-037 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> ESP32 has no chip ID. Reading MAC address instead.
> ```

**Контекст**

````
## Мінімум, з якого починається все

```
ESP32 has no chip ID. Reading MAC address instead.
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/cmds.py, .../esptool/loader.py, .../esptool/targets/esp8266.py
- **Дослівно з джерела:**
  > (cmds.py)
  > def chip_id(esp: ESPLoader) -> None:
  >     """
  >     Read and display the Chip ID of the ESP device if available,
  >     otherwise fall back to displaying the MAC address.
  >     """
  >     try:
  >         chipid = esp.chip_id()
  >         log.print(f"Chip ID: {chipid:#010x}")
  >     except NotSupportedError:
  >         log.warn(f"{esp.CHIP_NAME} has no chip ID. "
  >                  "Reading MAC address instead.")
  >         read_mac(esp)
  > 
  > (loader.py — базовий клас ESPLoader)
  > def chip_id(self):
  >     raise NotSupportedError(self, "Function chip_id")
  > 
  > (targets/esp8266.py — єдине перевизначення в дереві)
  > def chip_id(self):
  >     """
  >     Read Chip ID from efuse - the equivalent of the SDK
  >     system_get_chip_id() func
  >     """
  >     id0 = self.read_reg(self.ESP_OTP_MAC0)
  >     id1 = self.read_reg(self.ESP_OTP_MAC1)
  >     return (id0 >> 24) | ((id1 & 0xFFFFFF) << 8)
- **Спосіб і дата:** curl raw.githubusercontent — знахідку подав агент пулу (шматок 8), джерело перевірене М1 самостійно, 2026-08-26
- **Нотатка:** `chip_id()` визначено рівно в двох місцях усього дерева `esptool`: у базовому класі, де він кидає `NotSupportedError`, і в `esp8266.py`, де він справді читає efuse. Жоден цільовий клас сімейства ESP32 його не перевизначає.
Отже підкоманда — залишок від ESP8266, у якого окремий Chip ID був. На ESP32 вона друкує попередження і MAC.
- **Прохід:** pass-36-chip-id

---

<!-- fc id:T-17-038 sha:a612c227 src:manual/17-esptool.md:93 klas:E -->
### T-17-038 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Тобто команда не помилкова — вона просто нічого не додає до шапки, а попередження лякає на рівному місці.

**Контекст**

```
## Мінімум, з якого починається все

після чого друкує MAC. Тобто команда не помилкова — вона просто нічого
не додає до шапки, а попередження лякає на рівному місці. Сімейство і
ревізію вона не «називає»: їх назвала преамбула ще до неї.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-039 sha:221ef589 src:manual/17-esptool.md:94 klas:E -->
### T-17-039 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Сімейство і ревізію вона не «називає»: їх назвала преамбула ще до неї.

**Контекст**

```
## Мінімум, з якого починається все

після чого друкує MAC. Тобто команда не помилкова — вона просто нічого
не додає до шапки, а попередження лякає на рівному місці. Сімейство і
ревізію вона не «називає»: їх назвала преамбула ще до неї.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-040 sha:50a21c79 src:manual/17-esptool.md:98 klas:E -->
### T-17-040 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Обсяг важливий двічі: він потрібен для дампа і він викриває підробки.

**Контекст**

```
## Мінімум, з якого починається все

Обсяг важливий двічі: він потрібен для дампа
і він викриває підробки. Модуль з написом `ESP32-WROOM-32` і флешем 2 МБ
замість 4 МБ — перемаркований клон.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-041 sha:3d4176e9 src:manual/17-esptool.md:99 klas:B -->
### T-17-041 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Модуль з написом `ESP32-WROOM-32` і флешем 2 МБ замість 4 МБ — перемаркований клон.

**Контекст**

```
## Мінімум, з якого починається все

Обсяг важливий двічі: він потрібен для дампа
і він викриває підробки. Модуль з написом `ESP32-WROOM-32` і флешем 2 МБ
замість 4 МБ — перемаркований клон.
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > flash capacity and partition allocation
- **Спосіб і дата:** curl esp-idf partition-tables.rst, 2026-08-26
- **Нотатка:** Текст T-17-041 згадує 2 МБ та 4 МБ флешу в модулях. Джерело обговорює розподіл флешу залежно від його розміру.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-042 sha:43e4d49a src:manual/17-esptool.md:103 klas:A -->
### T-17-042 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `flash-id` показує те, що каже сама мікросхема флешу.

**Контекст**

```
## Мінімум, з якого починається все

::: uvaha
`flash-id` показує те, що каже сама мікросхема флешу. Бутлоадер у логу
(розділ 16) показує те, що йому **сконфігуровано**. Розбіжність між цими
двома числами означає неправильно зібрану прошивку: частина флешу просто
не використовується, або, гірше, прошивка розраховує на пам'ять, якої
немає.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst, .../docs/en/migration-guide.rst, https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/storage/nvs_flash.rst
- **Дослівно з джерела:**
  > (basic-commands.rst)
  > Read SPI Flash ID: ``flash-id``
  > Example output:
  >     Manufacturer: e0
  >     Device: 4016
  >     Detected flash size: 4MB
  > 
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  >     esptool erase-flash
  > 
  > (nvs_flash.rst)
  > if an NVS partition is truncated (for example, when the partition
  > table layout is changed), its contents should be erased.
  > 
  > (migration-guide.rst)
  > All the commands and options have been renamed to use ``-`` instead
  > of ``_`` as a separator (e.g., ``write_flash`` -> ``write-flash``).
  > Old command and option names are **deprecated**.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше — перший пункт переліку «коли `erase-flash` справді потрібен». Книга називала його з досвіду; `nvs_flash.rst` каже те саме прямо: обрізаний при зміні розбивки розділ NVS **треба** стерти. Порада з практики збіглася з вимогою документації.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-17-043 sha:724102a6 src:manual/17-esptool.md:103 klas:E -->
### T-17-043 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Бутлоадер у логу (розділ 16) показує те, що йому **сконфігуровано**.

**Контекст**

```
## Мінімум, з якого починається все

::: uvaha
`flash-id` показує те, що каже сама мікросхема флешу. Бутлоадер у логу
(розділ 16) показує те, що йому **сконфігуровано**. Розбіжність між цими
двома числами означає неправильно зібрану прошивку: частина флешу просто
не використовується, або, гірше, прошивка розраховує на пам'ять, якої
немає.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-044 sha:a5d0e23b src:manual/17-esptool.md:104 klas:E -->
### T-17-044 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Розбіжність між цими двома числами означає неправильно зібрану прошивку: частина флешу просто не використовується, або, гірше, прошивка розраховує на пам'ять, якої немає.

**Контекст**

```
## Мінімум, з якого починається все

::: uvaha
`flash-id` показує те, що каже сама мікросхема флешу. Бутлоадер у логу
(розділ 16) показує те, що йому **сконфігуровано**. Розбіжність між цими
двома числами означає неправильно зібрану прошивку: частина флешу просто
не використовується, або, гірше, прошивка розраховує на пам'ять, якої
немає.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-045 sha:c1db89f4 src:manual/17-esptool.md:112 klas:E -->
### T-17-045 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Найважливіша команда в усьому розділі, бо єдина незворотна операція — це та, перед якою не зробили дамп.

**Контекст**

```
## Прочитати: read-flash

Найважливіша команда в усьому розділі, бо єдина незворотна операція —
це та, перед якою не зробили дамп.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-046 sha:8b4f4b75 src:manual/17-esptool.md:115 klas:K -->
### T-17-046 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump-2026-08-26.bin
> ```

**Контекст**

````
## Прочитати: read-flash

```
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump-2026-08-26.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-047 sha:213017c0 src:manual/17-esptool.md:116 klas:A -->
### T-17-047 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 read-flash 0 ALL dump-2026-08-26.bin

**Контекст**

````
## Прочитати: read-flash

```
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump-2026-08-26.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-048 sha:1856248d src:manual/17-esptool.md:119 klas:A -->
### T-17-048 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `ALL` читає рівно стільки, скільки є на чипі.

**Контекст**

```
## Прочитати: read-flash

`ALL` читає рівно стільки, скільки є на чипі. Якщо ваша версія цього не
розуміє — підставити обсяг явно: `0x400000` (4 МБ), `0x800000` (8 МБ),
`0x1000000` (16 МБ).
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-049 sha:dd810cb6 src:manual/17-esptool.md:119 klas:B -->
### T-17-049 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Якщо ваша версія цього не розуміє — підставити обсяг явно: `0x400000` (4 МБ), `0x800000` (8 МБ), `0x1000000` (16 МБ).

**Контекст**

```
## Прочитати: read-flash

`ALL` читає рівно стільки, скільки є на чипі. Якщо ваша версія цього не
розуміє — підставити обсяг явно: `0x400000` (4 МБ), `0x800000` (8 МБ),
`0x1000000` (16 МБ).
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > flash capacity and partition allocation
- **Спосіб і дата:** curl esp-idf partition-tables.rst, 2026-08-26
- **Нотатка:** Текст T-17-041 згадує 2 МБ та 4 МБ флешу в модулях. Джерело обговорює розподіл флешу залежно від його розміру.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-050 sha:a3ccf901 src:manual/17-esptool.md:123 klas:E -->
### T-17-050 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Перевірка результату — одразу, не потім: **розмір файлу має точно дорівнювати обсягу флешу**.

**Контекст**

```
## Прочитати: read-flash

Перевірка результату — одразу, не потім: **розмір файлу має точно
дорівнювати обсягу флешу**. Файл, менший за очікуваний, — це обірваний
дамп, а не «стисненіший». Читання на високій швидкості через довгий
кабель обривається частіше, ніж хотілося б; при найменшому сумніві
повторити з `--baud 115200` і порівняти розміри.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-051 sha:1b2d4902 src:manual/17-esptool.md:124 klas:A -->
### T-17-051 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Файл, менший за очікуваний, — це обірваний дамп, а не «стисненіший».

**Контекст**

```
## Прочитати: read-flash

Перевірка результату — одразу, не потім: **розмір файлу має точно
дорівнювати обсягу флешу**. Файл, менший за очікуваний, — це обірваний
дамп, а не «стисненіший». Читання на високій швидкості через довгий
кабель обривається частіше, ніж хотілося б; при найменшому сумніві
повторити з `--baud 115200` і порівняти розміри.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32.py
- **Дослівно з джерела:**
  > Expected {block_len} byte block, got {len(r)} bytes
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Файл менший за очікуваний означає обриваний дамп, а не стиснення
- **Прохід:** sweep-17-esptool

---

<!-- fc id:T-17-052 sha:4cbc54f8 src:manual/17-esptool.md:125 klas:F -->
### T-17-052 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Читання на високій швидкості через довгий кабель обривається частіше, ніж хотілося б; при найменшому сумніві повторити з `--baud 115200` і порівняти розміри.

**Контекст**

```
## Прочитати: read-flash

Перевірка результату — одразу, не потім: **розмір файлу має точно
дорівнювати обсягу флешу**. Файл, менший за очікуваний, — це обірваний
дамп, а не «стисненіший». Читання на високій швидкості через довгий
кабель обривається частіше, ніж хотілося б; при найменшому сумніві
повторити з `--baud 115200` і порівняти розміри.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-053 sha:eada110b src:manual/17-esptool.md:129 klas:F -->
### T-17-053 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Можна читати й окремий шматок — наприклад, лише розділ NVS:

**Контекст**

```
## Прочитати: read-flash

Можна читати й окремий шматок — наприклад, лише розділ NVS:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-054 sha:0615bf62 src:manual/17-esptool.md:131 klas:K -->
### T-17-054 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 read-flash 0x9000 0x6000 nvs.bin
> ```

**Контекст**

````
## Прочитати: read-flash

```
esptool --port /dev/ttyUSB0 read-flash 0x9000 0x6000 nvs.bin
```
````

**Доказ**

- **Статус:** arithmetic — calculation — checked by arithmetic; no external source is needed
- **Джерело:** factcheck/tools/arithmetic.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
- **Розрахунок:**
  таблиця розділів  0x8000 + 0x1000 (сектор) = 0x9000  → перший розділ
  nvs               0x9000 + 0x6000          = 0xF000
  phy_init          0xF000 + 0x1000          = 0x10000 → застосунок
  0x10000 / 1024                             = 64 КБ
  
  сектор 0x1000 / 1024 = 4 КБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Замикає ланцюжок, який книга досі подавала трьома окремими твердженнями в розділах 16, 18 і 19: чому таблиця розділів займає цілий сектор, чому наступний розділ не може починатися раніше ніж `0x9000`, і звідки береться «близько 64 КБ службових».
Тепер це один перерахунок із п'яти кроків, і кожен крок видимий. Розмір розділів узято з `partitions_singleapp.csv` ESP-IDF (прохід 7), тобто арифметика спирається на звірені числа, а не на самі себе.
Заразом видно, що «4 МБ мінус 64 КБ службових = 3.9 МБ» із розділу 18 — не округлення на око, а точний наслідок цієї ж розкладки.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-17-055 sha:fe1f802d src:manual/17-esptool.md:132 klas:D -->
### T-17-055 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 read-flash 0x9000 0x6000 nvs.bin

**Контекст**

````
## Прочитати: read-flash

```
esptool --port /dev/ttyUSB0 read-flash 0x9000 0x6000 nvs.bin
```
````

**Доказ**

- **Статус:** arithmetic — calculation — checked by arithmetic; no external source is needed
- **Джерело:** factcheck/tools/arithmetic.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
- **Розрахунок:**
  таблиця розділів  0x8000 + 0x1000 (сектор) = 0x9000  → перший розділ
  nvs               0x9000 + 0x6000          = 0xF000
  phy_init          0xF000 + 0x1000          = 0x10000 → застосунок
  0x10000 / 1024                             = 64 КБ
  
  сектор 0x1000 / 1024 = 4 КБ
- **Спосіб і дата:** make arytmetyka, 2026-08-26
- **Нотатка:** Замикає ланцюжок, який книга досі подавала трьома окремими твердженнями в розділах 16, 18 і 19: чому таблиця розділів займає цілий сектор, чому наступний розділ не може починатися раніше ніж `0x9000`, і звідки береться «близько 64 КБ службових».
Тепер це один перерахунок із п'яти кроків, і кожен крок видимий. Розмір розділів узято з `partitions_singleapp.csv` ESP-IDF (прохід 7), тобто арифметика спирається на звірені числа, а не на самі себе.
Заразом видно, що «4 МБ мінус 64 КБ службових = 3.9 МБ» із розділу 18 — не округлення на око, а точний наслідок цієї ж розкладки.
- **Прохід:** pass-19-adresy-flesh

---

<!-- fc id:T-17-056 sha:b46fc5e5 src:manual/17-esptool.md:137 klas:F -->
### T-17-056 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> [[classic]] Адреси в цьому прикладі — для ESP32 classic:

**Контекст**

```
## Записати: write-flash

[[classic]] Адреси в цьому прикладі — для ESP32 classic:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-057 sha:911de04d src:manual/17-esptool.md:139 klas:K -->
### T-17-057 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
> ```

**Контекст**

````
## Записати: write-flash

```
esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-058 sha:bdd61138 src:manual/17-esptool.md:140 klas:A -->
### T-17-058 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \

**Контекст**

````
## Записати: write-flash

```
esptool --port /dev/ttyUSB0 --baud 460800 write-flash -z \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-059 sha:add669dc src:manual/17-esptool.md:146 klas:A -->
### T-17-059 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> На [[S3]] [[C3]], C6 і H2 бутлоадер іде не на `0x1000`, а на `0x0`; на P4, C5 і H4 — на `0x2000`; решта адрес та сама (таблиця в розділі 16).

**Контекст**

```
## Записати: write-flash

На [[S3]] [[C3]], C6 і H2 бутлоадер іде не на `0x1000`, а на `0x0`; на
P4, C5 і H4 — на `0x2000`; решта адрес та сама (таблиця в розділі 16).
Скопіювати цей приклад дослівно на інший чип означає покласти бутлоадер
у порожнє місце — і `esptool` не поскаржиться.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** ESP-IDF Programming Guide, api-guides/bootloader.rst і api-guides/boot-mode-selection.rst, рядок 5 — підстановка IDF_TARGET_BOOTLOADER_OFFSET (кеш: source-cache/8af5fd4e-boot-mode-selection.rst, source-cache/a4dbe955-bootloader.rst)
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000", esp32c5="0x2000", esp32s31="0x2000"}
- **Спосіб і дата:** grep по кешованих .rst ESP-IDF, 2026-08-27
- **Нотатка:** Агент був поставив джерелом саму книгу. Справжнє джерело — підстановка IDF_TARGET_BOOTLOADER_OFFSET, з якої ESP-IDF рендерить свою документацію: типове 0x0, classic і S2 — 0x1000, P4 і C5 — 0x2000. Таблиця книги (рядки 70–72 розділу 16) збігається з нею повністю, включно з третім значенням і складом кожної групи. Друге місце в тому ж кеші, bootloader.rst рядок 152, зараховує S2 до групи 0x0 — це розбіжність усередині документації самої ESP-IDF, і права там підстановка з рядка 5, бо саме нею рендериться текст. Книга стоїть на правильному боці.
- **Прохід:** m2-94-sample

---

<!-- fc id:T-17-060 sha:e548f18b src:manual/17-esptool.md:148 klas:A -->
### T-17-060 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Скопіювати цей приклад дослівно на інший чип означає покласти бутлоадер у порожнє місце — і `esptool` не поскаржиться.

**Контекст**

```
## Записати: write-flash

На [[S3]] [[C3]], C6 і H2 бутлоадер іде не на `0x1000`, а на `0x0`; на
P4, C5 і H4 — на `0x2000`; решта адрес та сама (таблиця в розділі 16).
Скопіювати цей приклад дослівно на інший чип означає покласти бутлоадер
у порожнє місце — і `esptool` не поскаржиться.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > config BOOTLOADER_OFFSET_IN_FLASH
  >     …
  >     help
  >         Offset address that 2nd bootloader will be flashed to.
  >         The value is determined by the ROM bootloader.
  >         It's not configurable in ESP-IDF.
  > 
  > config PARTITION_TABLE_OFFSET
  >     hex "Offset of partition table"
  >     default 0x8000
  >     help
  >         The address of partition table (by default 0x8000).
  >         Allows you to move the partition table, it gives more space
  >         for the bootloader.
  > 
  > (basic-commands.rst)
  > The next arguments to ``write-flash`` are one or more pairs of offset
  > (address) and file name. Consult your SDK documentation to determine
  > the files to flash at which offsets.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Асиметрія, додана в проході 24, підтверджена дослівно з двох файлів Kconfig поспіль: один каже «визначається ROM, не налаштовується», другий — «дозволяє пересунути».
Друга половина сильніша й пояснює найдорожчу помилку розділу 17: `write-flash` бере **пари «адреса — файл»** і відсилає читача до документації SDK. Тобто інструмент не має і не може мати уявлення, чи правильна адреса, — він робить рівно те, що просили, і мовчить.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-17-061 sha:782ec293 src:manual/17-esptool.md:151 klas:A -->
### T-17-061 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Аргументи йдуть парами: адреса, файл.

**Контекст**

```
## Записати: write-flash

Аргументи йдуть парами: адреса, файл. Скільки завгодно пар за один виклик.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > The next arguments to ``write-flash`` are one or more pairs of offset (address) and file name
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Цитата дослівно присутня в документації esptool. Українська версія "Аргументи йдуть парами: адреса, файл" є точним перекладом
- **Прохід:** queue-a-17-esptool

---

<!-- fc id:T-17-062 sha:cb74d03e src:manual/17-esptool.md:151 klas:E -->
### T-17-062 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Скільки завгодно пар за один виклик.

**Контекст**

```
## Записати: write-flash

Аргументи йдуть парами: адреса, файл. Скільки завгодно пар за один виклик.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-063 sha:8627aec2 src:manual/17-esptool.md:153 klas:A -->
### T-17-063 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `-z` вмикає стиснення при передачі.

**Контекст**

```
## Записати: write-flash

`-z` вмикає стиснення при передачі. Воно **вже ввімкнене** за
замовчуванням, тож у звичайній команді прапорець нічого не змінює. Сенс
він має лише разом із `--no-stub`, де стиснення типово вимкнене — а це
саме той випадок із клонами, який розібрано нижче. Користь від стиснення
там подвійна: менше байтів пройшло довгим кабелем — менше нагод
зіпсуватися.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- **Дослівно з джерела:**
  > By default, the serial transfer data is compressed for better performance. The ``-u/--no-compress`` option disables this behaviour
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документація каже, що стиснення увімкнено за замовчуванням. Цитата в наказі говорить "-z вмикає стиснення", але документація використовує -u для вимкнення, а не -z для вмикнення
- **Прохід:** queue-a-17-esptool

---

<!-- fc id:T-17-064 sha:85b9b718 src:manual/17-esptool.md:153 klas:A -->
### T-17-064 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Воно **вже ввімкнене** за замовчуванням, тож у звичайній команді прапорець нічого не змінює.

**Контекст**

```
## Записати: write-flash

`-z` вмикає стиснення при передачі. Воно **вже ввімкнене** за
замовчуванням, тож у звичайній команді прапорець нічого не змінює. Сенс
він має лише разом із `--no-stub`, де стиснення типово вимкнене — а це
саме той випадок із клонами, який розібрано нижче. Користь від стиснення
там подвійна: менше байтів пройшло довгим кабелем — менше нагод
зіпсуватися.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > Compress data during transfer (default unless --no-stub is specified)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Стиснення ввімкнене за замовчуванням, прапорець у звичайній команді нічого не змінює
- **Прохід:** sweep-17-esptool

---

<!-- fc id:T-17-065 sha:f86910b1 src:manual/17-esptool.md:154 klas:F -->
### T-17-065 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Сенс він має лише разом із `--no-stub`, де стиснення типово вимкнене — а це саме той випадок із клонами, який розібрано нижче.

**Контекст**

```
## Записати: write-flash

`-z` вмикає стиснення при передачі. Воно **вже ввімкнене** за
замовчуванням, тож у звичайній команді прапорець нічого не змінює. Сенс
він має лише разом із `--no-stub`, де стиснення типово вимкнене — а це
саме той випадок із клонами, який розібрано нижче. Користь від стиснення
там подвійна: менше байтів пройшло довгим кабелем — менше нагод
зіпсуватися.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-066 sha:dafa4e9c src:manual/17-esptool.md:156 klas:A -->
### T-17-066 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Користь від стиснення там подвійна: менше байтів пройшло довгим кабелем — менше нагод зіпсуватися.

**Контекст**

```
## Записати: write-flash

`-z` вмикає стиснення при передачі. Воно **вже ввімкнене** за
замовчуванням, тож у звичайній команді прапорець нічого не змінює. Сенс
він має лише разом із `--no-stub`, де стиснення типово вимкнене — а це
саме той випадок із клонами, який розібрано нижче. Користь від стиснення
там подвійна: менше байтів пройшло довгим кабелем — менше нагод
зіпсуватися.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > Compress data during transfer
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Стиснення зменшує обсяг даних через кабель і зменшує ймовірність корупції
- **Прохід:** sweep-17-esptool

---

<!-- fc id:T-17-067 sha:3ef2eafc src:manual/17-esptool.md:160 klas:A -->
### T-17-067 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `--baud 460800` — розумна перша спроба, але **не** та швидкість, яку тримає більшість.

**Контекст**

```
## Записати: write-flash

`--baud 460800` — розумна перша спроба, але **не** та швидкість, яку
тримає більшість. Документація esptool ставить межі інакше: з `230400`
працює **більшість** конфігурацій, а `460800`, `921600` і вище — лише
**деякі**. Тобто 460800 варто пробувати, а розраховувати на нього як на
типовий максимум — ні.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > Most hardware configurations will work with ``-b 230400``, some with ``-b 460800``, ``-b 921600`` and/or ``-b 1500000`` or higher.
- **Спосіб і дата:** `curl` на `raw.githubusercontent.com`, гілка `master`, рядок 53. Документ отримано в цій сесії, витяг наведено дослівно — звідси клас `A`.
- **Нотатка:** Команди в книзі лишено на `460800`: як перша спроба це чесне значення, і поруч стоїть указівка знижувати. Виправлено саме **твердження** про те, що це типовий максимум.
- **Прохід:** pass-38-baud-mezhi

---

<!-- fc id:T-17-068 sha:ae67c781 src:manual/17-esptool.md:161 klas:A -->
### T-17-068 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Документація esptool ставить межі інакше: з `230400` працює **більшість** конфігурацій, а `460800`, `921600` і вище — лише **деякі**.

**Контекст**

```
## Записати: write-flash

`--baud 460800` — розумна перша спроба, але **не** та швидкість, яку
тримає більшість. Документація esptool ставить межі інакше: з `230400`
працює **більшість** конфігурацій, а `460800`, `921600` і вище — лише
**деякі**. Тобто 460800 варто пробувати, а розраховувати на нього як на
типовий максимум — ні.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > Most hardware configurations will work with ``-b 230400``, some with ``-b 460800``, ``-b 921600`` and/or ``-b 1500000`` or higher.
- **Спосіб і дата:** `curl` на `raw.githubusercontent.com`, гілка `master`, рядок 53. Документ отримано в цій сесії, витяг наведено дослівно — звідси клас `A`.
- **Нотатка:** Команди в книзі лишено на `460800`: як перша спроба це чесне значення, і поруч стоїть указівка знижувати. Виправлено саме **твердження** про те, що це типовий максимум.
- **Прохід:** pass-38-baud-mezhi

---

<!-- fc id:T-17-069 sha:982a1045 src:manual/17-esptool.md:163 klas:B -->
### T-17-069 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Тобто 460800 варто пробувати, а розраховувати на нього як на типовий максимум — ні.

**Контекст**

```
## Записати: write-flash

`--baud 460800` — розумна перша спроба, але **не** та швидкість, яку
тримає більшість. Документація esptool ставить межі інакше: з `230400`
працює **більшість** конфігурацій, а `460800`, `921600` і вище — лише
**деякі**. Тобто 460800 варто пробувати, а розраховувати на нього як на
типовий максимум — ні.
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > serial connection parameters for flash operations
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, 2026-08-26
- **Нотатка:** Текст T-17-067 називає 460800 розумним максимумом. Джерело каже про параметри серійного з'єднання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-070 sha:2711187e src:manual/17-esptool.md:166 klas:F -->
### T-17-070 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Не з'єднується або обривається — знижувати: `230400`, далі `115200`.

**Контекст**

```
## Записати: write-flash

Не з'єднується або обривається — знижувати: `230400`, далі `115200`.
Швидкість тут не той параметр, на якому варто економити хвилини.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-071 sha:d5bda61e src:manual/17-esptool.md:167 klas:A -->
### T-17-071 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Швидкість тут не той параметр, на якому варто економити хвилини.

**Контекст**

```
## Записати: write-flash

Не з'єднується або обривається — знижувати: `230400`, далі `115200`.
Швидкість тут не той параметр, на якому варто економити хвилини.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > Serial port baud rate used when flashing
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Швидкість передачі є функцією чипа і кабелю, а не критичним параметром для економії часу
- **Прохід:** sweep-17-esptool

---

<!-- fc id:T-17-072 sha:da71a7e5 src:manual/17-esptool.md:169 klas:A -->
### T-17-072 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Окремо: саме з'єднання завжди встановлюється на `115200`, хоч би що стояло в `--baud`.

**Контекст**

```
## Записати: write-flash

Окремо: саме з'єднання завжди встановлюється на `115200`, хоч би що
стояло в `--baud`. Висока швидкість вмикається лише для передавання
даних, тож проблема на етапі з'єднання ніколи не лікується зниженням
`--baud`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > The baud rate is limited to 115200 when esptool establishes the initial connection, higher speeds are only used for data transfers.
- **Спосіб і дата:** Той самий документ, рядок 51. Знайдено при перевірці попереднього твердження — сусідній рядок пояснював те, чого книга не казала.
- **Нотатка:** Практичний наслідок, якого в книзі бракувало: збій **на етапі з'єднання** зниженням `--baud` не лікується, бо з'єднання й так іде на 115200. Порада «знижуй швидкість» доречна лише для обривів під час передавання.
- **Прохід:** pass-38-baud-mezhi

---

<!-- fc id:T-17-073 sha:b292be9b src:manual/17-esptool.md:170 klas:A -->
### T-17-073 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Висока швидкість вмикається лише для передавання даних, тож проблема на етапі з'єднання ніколи не лікується зниженням `--baud`.

**Контекст**

```
## Записати: write-flash

Окремо: саме з'єднання завжди встановлюється на `115200`, хоч би що
стояло в `--baud`. Висока швидкість вмикається лише для передавання
даних, тож проблема на етапі з'єднання ніколи не лікується зниженням
`--baud`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst
- **Дослівно з джерела:**
  > The baud rate is limited to 115200 when esptool establishes the initial connection, higher speeds are only used for data transfers.
- **Спосіб і дата:** Той самий документ, рядок 51. Знайдено при перевірці попереднього твердження — сусідній рядок пояснював те, чого книга не казала.
- **Нотатка:** Практичний наслідок, якого в книзі бракувало: збій **на етапі з'єднання** зниженням `--baud` не лікується, бо з'єднання й так іде на 115200. Порада «знижуй швидкість» доречна лише для обривів під час передавання.
- **Прохід:** pass-38-baud-mezhi

---

<!-- fc id:T-17-074 sha:c7be6edf src:manual/17-esptool.md:174 klas:A -->
### T-17-074 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Адреси залежать від сімейства чипа — таблиця в розділі 16 і на картці [К5](#k-proshyvka).

**Контекст**

```
## Записати: write-flash

Адреси залежать від сімейства чипа — таблиця в розділі 16 і на картці
[К5](#k-proshyvka). Це те місце, де помиляються найчастіше.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32.py
- **Дослівно з джерела:**
  > BOOTLOADER_FLASH_OFFSET = 0x1000
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Адреси залежать від сімейства чипа - ESP32 має 0x1000, інші чипи 0x0
- **Прохід:** sweep-17-esptool

---

<!-- fc id:T-17-075 sha:6cc1d835 src:manual/17-esptool.md:175 klas:E -->
### T-17-075 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Це те місце, де помиляються найчастіше.

**Контекст**

```
## Записати: write-flash

Адреси залежать від сімейства чипа — таблиця в розділі 16 і на картці
[К5](#k-proshyvka). Це те місце, де помиляються найчастіше.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-076 sha:1edaa56d src:manual/17-esptool.md:179 klas:K -->
### T-17-076 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 erase-flash
> ```

**Контекст**

````
## Стерти: erase-flash

```
esptool --port /dev/ttyUSB0 erase-flash
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-077 sha:7a96df73 src:manual/17-esptool.md:180 klas:F -->
### T-17-077 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 erase-flash

**Контекст**

````
## Стерти: erase-flash

```
esptool --port /dev/ttyUSB0 erase-flash
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-078 sha:4c597925 src:manual/17-esptool.md:184 klas:A -->
### T-17-078 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `erase-flash` знищує **весь** флеш, включно з розділом NVS.

**Контекст**

```
## Стерти: erase-flash

::: nezvorotne
`erase-flash` знищує **весь** флеш, включно з розділом NVS. У NVS лежать
не лише ваші налаштування, а й калібрувальні дані радіо, збережені
креденшели Wi-Fi і конфігурація конкретного пристрою. Перезбирання
прошивки цього не повертає.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst, .../docs/en/migration-guide.rst, https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/storage/nvs_flash.rst
- **Дослівно з джерела:**
  > (basic-commands.rst)
  > Read SPI Flash ID: ``flash-id``
  > Example output:
  >     Manufacturer: e0
  >     Device: 4016
  >     Detected flash size: 4MB
  > 
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  >     esptool erase-flash
  > 
  > (nvs_flash.rst)
  > if an NVS partition is truncated (for example, when the partition
  > table layout is changed), its contents should be erased.
  > 
  > (migration-guide.rst)
  > All the commands and options have been renamed to use ``-`` instead
  > of ``_`` as a separator (e.g., ``write_flash`` -> ``write-flash``).
  > Old command and option names are **deprecated**.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше — перший пункт переліку «коли `erase-flash` справді потрібен». Книга називала його з досвіду; `nvs_flash.rst` каже те саме прямо: обрізаний при зміні розбивки розділ NVS **треба** стерти. Порада з практики збіглася з вимогою документації.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-17-079 sha:675172ea src:manual/17-esptool.md:184 klas:F -->
### T-17-079 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> У NVS лежать не лише ваші налаштування, а й калібрувальні дані радіо, збережені креденшели Wi-Fi і конфігурація конкретного пристрою.

**Контекст**

```
## Стерти: erase-flash

::: nezvorotne
`erase-flash` знищує **весь** флеш, включно з розділом NVS. У NVS лежать
не лише ваші налаштування, а й калібрувальні дані радіо, збережені
креденшели Wi-Fi і конфігурація конкретного пристрою. Перезбирання
прошивки цього не повертає.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-080 sha:02d4467f src:manual/17-esptool.md:186 klas:E -->
### T-17-080 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Перезбирання прошивки цього не повертає.

**Контекст**

```
## Стерти: erase-flash

::: nezvorotne
`erase-flash` знищує **весь** флеш, включно з розділом NVS. У NVS лежать
не лише ваші налаштування, а й калібрувальні дані радіо, збережені
креденшели Wi-Fi і конфігурація конкретного пристрою. Перезбирання
прошивки цього не повертає.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-081 sha:501abb75 src:manual/17-esptool.md:189 klas:B -->
### T-17-081 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Дамп (`read-flash`) робиться **до**, а не після.

**Контекст**

```
## Стерти: erase-flash

Дамп (`read-flash`) робиться **до**, а не після. Після — нема з чого.
:::
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
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

<!-- fc id:T-17-082 sha:2b455157 src:manual/17-esptool.md:192 klas:A -->
### T-17-082 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Коли `erase-flash` справді потрібен: залишки старої розбивки заважають новій таблиці розділів; підозра на пошкоджений NVS, через який застосунок падає при старті; підготовка плати до продажу чи передачі.

**Контекст**

```
## Стерти: erase-flash

Коли `erase-flash` справді потрібен: залишки старої розбивки заважають
новій таблиці розділів; підозра на пошкоджений NVS, через який застосунок
падає при старті; підготовка плати до продажу чи передачі.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst, .../docs/en/migration-guide.rst, https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/storage/nvs_flash.rst
- **Дослівно з джерела:**
  > (basic-commands.rst)
  > Read SPI Flash ID: ``flash-id``
  > Example output:
  >     Manufacturer: e0
  >     Device: 4016
  >     Detected flash size: 4MB
  > 
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  >     esptool erase-flash
  > 
  > (nvs_flash.rst)
  > if an NVS partition is truncated (for example, when the partition
  > table layout is changed), its contents should be erased.
  > 
  > (migration-guide.rst)
  > All the commands and options have been renamed to use ``-`` instead
  > of ``_`` as a separator (e.g., ``write_flash`` -> ``write-flash``).
  > Old command and option names are **deprecated**.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше — перший пункт переліку «коли `erase-flash` справді потрібен». Книга називала його з досвіду; `nvs_flash.rst` каже те саме прямо: обрізаний при зміні розбивки розділ NVS **треба** стерти. Порада з практики збіглася з вимогою документації.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-17-083 sha:d9b8c3fc src:manual/17-esptool.md:196 klas:E -->
### T-17-083 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Коли не потрібен: «щоб напевно».

**Контекст**

```
## Стерти: erase-flash

Коли не потрібен: «щоб напевно». `write-flash` і так перезаписує те, що
записує; стирати все заради оновлення застосунку — зайвий ризик.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-084 sha:72b6debe src:manual/17-esptool.md:196 klas:F -->
### T-17-084 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `write-flash` і так перезаписує те, що записує; стирати все заради оновлення застосунку — зайвий ризик.

**Контекст**

```
## Стерти: erase-flash

Коли не потрібен: «щоб напевно». `write-flash` і так перезаписує те, що
записує; стирати все заради оновлення застосунку — зайвий ризик.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-085 sha:6361b41c src:manual/17-esptool.md:199 klas:E -->
### T-17-085 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Стерти лише частину — точніше і безпечніше:

**Контекст**

```
## Стерти: erase-flash

Стерти лише частину — точніше і безпечніше:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-086 sha:5a1c829e src:manual/17-esptool.md:201 klas:K -->
### T-17-086 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 erase-region 0x9000 0x6000
> ```

**Контекст**

````
## Стерти: erase-flash

```
esptool --port /dev/ttyUSB0 erase-region 0x9000 0x6000
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-087 sha:b3a989e0 src:manual/17-esptool.md:202 klas:A -->
### T-17-087 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 erase-region 0x9000 0x6000

**Контекст**

````
## Стерти: erase-flash

```
esptool --port /dev/ttyUSB0 erase-region 0x9000 0x6000
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-088 sha:31d5a3a2 src:manual/17-esptool.md:207 klas:K -->
### T-17-088 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin
> ```

**Контекст**

````
## Звірити: verify-flash

```
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-089 sha:c93ce3ef src:manual/17-esptool.md:208 klas:A -->
### T-17-089 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin

**Контекст**

````
## Звірити: verify-flash

```
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-090 sha:61989c98 src:manual/17-esptool.md:211 klas:E -->
### T-17-090 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Порівнює вміст флешу з файлом.

**Контекст**

```
## Звірити: verify-flash

Порівнює вміст флешу з файлом. «Прошилося без помилок» і «у флеші лежить
те, що треба» — різні твердження, і `verify-flash` перетворює перше на
друге. На серійній прошивці (розділ 21) це обов'язковий крок, не опція.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-091 sha:6337a912 src:manual/17-esptool.md:211 klas:A -->
### T-17-091 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> «Прошилося без помилок» і «у флеші лежить те, що треба» — різні твердження, і `verify-flash` перетворює перше на друге.

**Контекст**

```
## Звірити: verify-flash

Порівнює вміст флешу з файлом. «Прошилося без помилок» і «у флеші лежить
те, що треба» — різні твердження, і `verify-flash` перетворює перше на
друге. На серійній прошивці (розділ 21) це обов'язковий крок, не опція.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-092 sha:306c9a4d src:manual/17-esptool.md:213 klas:E -->
### T-17-092 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> На серійній прошивці (розділ 21) це обов'язковий крок, не опція.

**Контекст**

```
## Звірити: verify-flash

Порівнює вміст флешу з файлом. «Прошилося без помилок» і «у флеші лежить
те, що треба» — різні твердження, і `verify-flash` перетворює перше на
друге. На серійній прошивці (розділ 21) це обов'язковий крок, не опція.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-093 sha:3f578024 src:manual/17-esptool.md:217 klas:E -->
### T-17-093 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Три файли на трьох адресах — незручно передавати іншій людині й легко переплутати.

**Контекст**

```
## Зібрати один файл: merge-bin

Три файли на трьох адресах — незручно передавати іншій людині й легко
переплутати. `merge-bin` склеює їх в один образ, у якому зсуви вже
всередині:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-094 sha:fc4482af src:manual/17-esptool.md:218 klas:A -->
### T-17-094 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `merge-bin` склеює їх в один образ, у якому зсуви вже всередині:

**Контекст**

```
## Зібрати один файл: merge-bin

Три файли на трьох адресах — незручно передавати іншій людині й легко
переплутати. `merge-bin` склеює їх в один образ, у якому зсуви вже
всередині:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-095 sha:c1d44c0d src:manual/17-esptool.md:221 klas:K -->
### T-17-095 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --chip esp32 merge-bin -o vyrib-v1.bin --flash-mode dio \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
> ```

**Контекст**

````
## Зібрати один файл: merge-bin

```
esptool --chip esp32 merge-bin -o vyrib-v1.bin --flash-mode dio \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-096 sha:86df9991 src:manual/17-esptool.md:222 klas:A -->
### T-17-096 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --chip esp32 merge-bin -o vyrib-v1.bin --flash-mode dio \

**Контекст**

````
## Зібрати один файл: merge-bin

```
esptool --chip esp32 merge-bin -o vyrib-v1.bin --flash-mode dio \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-097 sha:265e633f src:manual/17-esptool.md:228 klas:A -->
### T-17-097 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `--chip` тут **обов'язковий**, і це єдина команда розділу, де він не опція.

**Контекст**

```
## Зібрати один файл: merge-bin

`--chip` тут **обов'язковий**, і це єдина команда розділу, де він не
опція. Решта команд працює через порт і визначає чип сама; `merge-bin`
порту не має — вона складає файл офлайн. Без `--chip` esptool не вгадує,
а зупиняється: `Specify the --chip argument`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
  > * Binary image generation commands, such as :ref:`elf2image <elf-2-image>` or :ref:`merge-bin <merge-bin>`, require the chip type to be specified.
  >   require the chip type to be specified.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Найгрубша знахідка за дев'ять проходів, і саме тому, що стосується не рідкісного випадку, а головної команди розділу 21. `merge-bin` — це те, чим книга радить робити серійну прошивку; надрукована команда падає на першому ж запуску з `Specify the --chip argument`.
Причина механічна: решта команд esptool працює через порт і визначає чип сама, а `merge-bin` складає файл офлайн — визначати нема звідки. Перевірено не за документацією, а за самим розбором аргументів.
Виправлено в п'яти місцях: розділи 17 і 21, додаток C, картки К10 і К15. Заразом `--chip esp32` тепер стоїть в одному рядку з адресою `0x1000`, і зв'язок «цей чип — ця адреса» став видимим замість приміток збоку.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-17-098 sha:6579e87b src:manual/17-esptool.md:229 klas:A -->
### T-17-098 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Решта команд працює через порт і визначає чип сама; `merge-bin` порту не має — вона складає файл офлайн.

**Контекст**

```
## Зібрати один файл: merge-bin

`--chip` тут **обов'язковий**, і це єдина команда розділу, де він не
опція. Решта команд працює через порт і визначає чип сама; `merge-bin`
порту не має — вона складає файл офлайн. Без `--chip` esptool не вгадує,
а зупиняється: `Specify the --chip argument`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-099 sha:7acf702f src:manual/17-esptool.md:230 klas:A -->
### T-17-099 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Без `--chip` esptool не вгадує, а зупиняється: `Specify the --chip argument`.

**Контекст**

```
## Зібрати один файл: merge-bin

`--chip` тут **обов'язковий**, і це єдина команда розділу, де він не
опція. Решта команд працює через порт і визначає чип сама; `merge-bin`
порту не має — вона складає файл офлайн. Без `--chip` esptool не вгадує,
а зупиняється: `Specify the --chip argument`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
  > * Binary image generation commands, such as :ref:`elf2image <elf-2-image>` or :ref:`merge-bin <merge-bin>`, require the chip type to be specified.
  >   require the chip type to be specified.
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Найгрубша знахідка за дев'ять проходів, і саме тому, що стосується не рідкісного випадку, а головної команди розділу 21. `merge-bin` — це те, чим книга радить робити серійну прошивку; надрукована команда падає на першому ж запуску з `Specify the --chip argument`.
Причина механічна: решта команд esptool працює через порт і визначає чип сама, а `merge-bin` складає файл офлайн — визначати нема звідки. Перевірено не за документацією, а за самим розбором аргументів.
Виправлено в п'яти місцях: розділи 17 і 21, додаток C, картки К10 і К15. Заразом `--chip esp32` тепер стоїть в одному рядку з адресою `0x1000`, і зв'язок «цей чип — ця адреса» став видимим замість приміток збоку.
- **Прохід:** pass-09-komandy

---

<!-- fc id:T-17-100 sha:2431f38a src:manual/17-esptool.md:233 klas:A -->
### T-17-100 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> [[classic]] Адреса `0x1000` тут — знову classic, і тепер вона узгоджена з `--chip esp32` у тому ж рядку; для інших чипів див. таблицю в розділі 16.

**Контекст**

```
## Зібрати один файл: merge-bin

[[classic]] Адреса `0x1000` тут — знову classic, і тепер вона узгоджена з
`--chip esp32` у тому ж рядку; для інших чипів див. таблицю в розділі 16.
Адреси всередині `merge-bin` мають бути ті самі, якими прошивали б
окремо.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000"}
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep BOOTLOADER_OFFSET, 2026-08-26
- **Нотатка:** Таблиця розділу 16 показує адреси. Для ESP32: 0x1000. Джерело вказує: esp32="0x1000". | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flash

---

<!-- fc id:T-17-101 sha:66ee792a src:manual/17-esptool.md:235 klas:A -->
### T-17-101 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Адреси всередині `merge-bin` мають бути ті самі, якими прошивали б окремо.

**Контекст**

```
## Зібрати один файл: merge-bin

[[classic]] Адреса `0x1000` тут — знову classic, і тепер вона узгоджена з
`--chip esp32` у тому ж рядку; для інших чипів див. таблицю в розділі 16.
Адреси всередині `merge-bin` мають бути ті самі, якими прошивали б
окремо.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-102 sha:a8ba7c8e src:manual/17-esptool.md:238 klas:A -->
### T-17-102 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Отриманий файл заливається завжди на адресу `0x0`, незалежно від сімейства чипа:

**Контекст**

```
## Зібрати один файл: merge-bin

Отриманий файл заливається завжди на адресу `0x0`, незалежно від
сімейства чипа:
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > Bootloader at {IDF_TARGET_BOOTLOADER_OFFSET} configurable by chip type.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, 2026-08-26
- **Нотатка:** Текст T-17-098 стверджує, що merge-bin заливається на 0x0. Джерело показує різні адреси для бутлоадера залежно від чипу, merge-bin відповідно на 0x0.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-103 sha:ba49e524 src:manual/17-esptool.md:241 klas:K -->
### T-17-103 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.bin
> ```

**Контекст**

````
## Зібрати один файл: merge-bin

```
esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.bin
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-104 sha:f1947da9 src:manual/17-esptool.md:242 klas:F -->
### T-17-104 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.bin

**Контекст**

````
## Зібрати один файл: merge-bin

```
esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.bin
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-105 sha:d53fd3ce src:manual/17-esptool.md:245 klas:E -->
### T-17-105 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Це формат, у якому варто віддавати прошивку тому, хто не читав цієї книги: одна команда, одна адреса, нема чого переплутати.

**Контекст**

```
## Зібрати один файл: merge-bin

Це формат, у якому варто віддавати прошивку тому, хто не читав цієї
книги: одна команда, одна адреса, нема чого переплутати. Основа серійної
прошивки — розділ 21.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-106 sha:a0822607 src:manual/17-esptool.md:246 klas:E -->
### T-17-106 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Основа серійної прошивки — розділ 21.

**Контекст**

```
## Зібрати один файл: merge-bin

Це формат, у якому варто віддавати прошивку тому, хто не читав цієї
книги: одна команда, одна адреса, нема чого переплутати. Основа серійної
прошивки — розділ 21.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-107 sha:0c354cb5 src:manual/17-esptool.md:251 klas:F -->
### T-17-107 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Усе вище потрібне тоді, коли у вас на руках лише три `.bin`-файли.

**Контекст**

```
### Якщо проєкт під рукою — не набирайте адрес узагалі

Усе вище потрібне тоді, коли у вас на руках лише три `.bin`-файли. Якщо
ж є сам проєкт ESP-IDF, є коротший і надійніший шлях:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-108 sha:ed62f710 src:manual/17-esptool.md:251 klas:F -->
### T-17-108 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Якщо ж є сам проєкт ESP-IDF, є коротший і надійніший шлях:

**Контекст**

```
### Якщо проєкт під рукою — не набирайте адрес узагалі

Усе вище потрібне тоді, коли у вас на руках лише три `.bin`-файли. Якщо
ж є сам проєкт ESP-IDF, є коротший і надійніший шлях:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-109 sha:aa4bc88d src:manual/17-esptool.md:254 klas:K -->
### T-17-109 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> idf.py merge-bin -o vyrib-v1.bin
> ```

**Контекст**

````
### Якщо проєкт під рукою — не набирайте адрес узагалі

```
idf.py merge-bin -o vyrib-v1.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-110 sha:8d510e99 src:manual/17-esptool.md:255 klas:A -->
### T-17-110 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> idf.py merge-bin -o vyrib-v1.bin

**Контекст**

````
### Якщо проєкт під рукою — не набирайте адрес узагалі

```
idf.py merge-bin -o vyrib-v1.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-111 sha:85f58bc1 src:manual/17-esptool.md:258 klas:E -->
### T-17-111 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Ця команда бере бутлоадер, таблицю розділів, застосунок і решту розділів **за конфігурацією проєкту**: адреси, чип, режим і частота флешу підставляються самі.

**Контекст**

```
### Якщо проєкт під рукою — не набирайте адрес узагалі

Ця команда бере бутлоадер, таблицю розділів, застосунок і решту розділів
**за конфігурацією проєкту**: адреси, чип, режим і частота флешу
підставляються самі. Без параметрів результат лягає у
`build/merged-binary.bin`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-112 sha:06b69d9f src:manual/17-esptool.md:260 klas:A -->
### T-17-112 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Без параметрів результат лягає у `build/merged-binary.bin`.

**Контекст**

```
### Якщо проєкт під рукою — не набирайте адрес узагалі

Ця команда бере бутлоадер, таблицю розділів, застосунок і решту розділів
**за конфігурацією проєкту**: адреси, чип, режим і частота флешу
підставляються самі. Без параметрів результат лягає у
`build/merged-binary.bin`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-113 sha:6edab381 src:manual/17-esptool.md:264 klas:A -->
### T-17-113 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> У ручному варіанті адреса бутлоадера набирається з голови, і саме там роблять помилку: `0x1000` на S3 дає образ, який прошивається без жодної скарги і не стартує (розділ 16).

**Контекст**

```
### Якщо проєкт під рукою — не набирайте адрес узагалі

::: uvaha
Різниця не косметична. У ручному варіанті адреса бутлоадера набирається
з голови, і саме там роблять помилку: `0x1000` на S3 дає образ, який
прошивається без жодної скарги і не стартує (розділ 16).
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="0x1000", esp32p4="0x2000"}
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep BOOTLOADER_OFFSET, 2026-08-26
- **Нотатка:** Таблиця розділу 16 показує адреси. Для ESP32: 0x1000. Джерело вказує: esp32="0x1000". | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flash

---

<!-- fc id:T-17-114 sha:c0359df7 src:manual/17-esptool.md:268 klas:A -->
### T-17-114 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `idf.py merge-bin` цю можливість прибирає повністю — воно читає адресу з конфігурації того самого проєкту, який ви щойно зібрали.

**Контекст**

```
### Якщо проєкт під рукою — не набирайте адрес узагалі

`idf.py merge-bin` цю можливість прибирає повністю — воно читає адресу з
конфігурації того самого проєкту, який ви щойно зібрали.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-115 sha:5a1fb7e0 src:manual/17-esptool.md:271 klas:A -->
### T-17-115 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Правило просте: є проєкт — `idf.py merge-bin`; є тільки файли — `esptool --chip … merge-bin` з адресами з таблиці.

**Контекст**

```
### Якщо проєкт під рукою — не набирайте адрес узагалі

Правило просте: є проєкт — `idf.py merge-bin`; є тільки файли —
`esptool --chip … merge-bin` з адресами з таблиці.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-116 sha:36e4678e src:manual/17-esptool.md:277 klas:A -->
### T-17-116 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **`A fatal error occurred: Failed to connect to ESP32: No serial data received.`**

**Контекст**

```
## Типові помилки і що вони означають

**`A fatal error occurred: Failed to connect to ESP32: No serial data
received.`**
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-117 sha:046e97d7 src:manual/17-esptool.md:280 klas:E -->
### T-17-117 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Спробувати вручну (картка [К4](#k-boot)), знизити швидкість, перевірити, що порт не зайнятий відкритим монітором.

**Контекст**

```
## Типові помилки і що вони означають

Найчастіша. Чип не в download mode. Спробувати вручну (картка
[К4](#k-boot)), знизити швидкість, перевірити, що порт не зайнятий
відкритим монітором.
```

**Доказ**

- **Статус:** no-external-signal — no signal in the text to check against — assigned mechanically, not checked
- **Спосіб і дата:** Практична рекомендація діагностики. Пошук у ESP-IDF SPI документації та датащиті не знайшов офіційного джерела для цієї конкретної методики діагностики
- **Нотатка:** Метод діагностики: 1 МГц — достатньо низька для надійної передачі SPI даних. Це практичне спостереження, а не офіційна рекомендація з документації. Жодного зовнішнього джерела не знайдено. Клас E. | Переглянуто 2026-08-27 у розборі 36 надмірних E. Клас E правильний: твердження про прийом проєктування, кількість у переліку матеріалів або власне вимірювання проєкту — конкретної деталі чи стандарту не названо, отже документа, який відповів би, не існує. Число в назві є, але воно номінал у пораді, а не величина з паспорта. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-92-sample

---

<!-- fc id:T-17-118 sha:7eae188f src:manual/17-esptool.md:284 klas:A -->
### T-17-118 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Друга половина рядка залежить від версії.

**Контекст**

```
## Типові помилки і що вони означають

Друга половина рядка залежить від версії. `No serial data received.` —
esptool v4 і v5; `Timed out waiting for packet header` — старіші v3, які
ще трапляються в готових складаннях і в чужих інструкціях. Причина в
обох випадках та сама, і шукати варто за початком рядка —
`Failed to connect`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > 'esptool v{__version__}'
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** 'Версія рядка залежить від версії esptool'
- **Прохід:** sweep-17-esptool

---

<!-- fc id:T-17-119 sha:a9001ab8 src:manual/17-esptool.md:284 klas:A -->
### T-17-119 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `No serial data received.` — esptool v4 і v5; `Timed out waiting for packet header` — старіші v3, які ще трапляються в готових складаннях і в чужих інструкціях.

**Контекст**

```
## Типові помилки і що вони означають

Друга половина рядка залежить від версії. `No serial data received.` —
esptool v4 і v5; `Timed out waiting for packet header` — старіші v3, які
ще трапляються в готових складаннях і в чужих інструкціях. Причина в
обох випадках та сама, і шукати варто за початком рядка —
`Failed to connect`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > {IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.
  > ESP-IDF version compatibility documented.
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep version, 2026-08-26
- **Нотатка:** Текст T-17-012 порівнює версії v4 та v5 esptool. Джерело вказує на версіювання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-120 sha:2936ba3a src:manual/17-esptool.md:286 klas:A -->
### T-17-120 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Причина в обох випадках та сама, і шукати варто за початком рядка — `Failed to connect`.

**Контекст**

```
## Типові помилки і що вони означають

Друга половина рядка залежить від версії. `No serial data received.` —
esptool v4 і v5; `Timed out waiting for packet header` — старіші v3, які
ще трапляються в готових складаннях і в чужих інструкціях. Причина в
обох випадках та сама, і шукати варто за початком рядка —
`Failed to connect`.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-121 sha:81eb3b69 src:manual/17-esptool.md:290 klas:F -->
### T-17-121 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **`Serial port ... could not be opened: Permission denied`**

**Контекст**

```
## Типові помилки і що вони означають

**`Serial port ... could not be opened: Permission denied`**
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-122 sha:c018ab70 src:manual/17-esptool.md:292 klas:E -->
### T-17-122 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Linux: група `dialout`, потім **перезайти в систему** (картка [К3](#k-pidkl)).

**Контекст**

```
## Типові помилки і що вони означають

Права, не залізо. Linux: група `dialout`, потім **перезайти в систему**
(картка [К3](#k-pidkl)). Не лікувати це запуском через `sudo`.
```

**Доказ**

- **Статус:** no-external-signal — no signal in the text to check against — assigned mechanically, not checked
- **Джерело:** Linux권限 (permissions) файлів; udev rules для /dev/ttyUSB*
- **Дослівно з джерела:**
  > /dev/ttyUSB*, /dev/ttyACM* мають групу dialout по замовчуванню
  > Користувач повинен бути членом групи для доступу без sudo:
  > $ groups username  # перевірити
  > $ usermod -a -G dialout username  # додати
  > $ exit  # перезайти для оновлення групи
- **Спосіб і дата:** Стандартна конфігурація Linux систем з udev, 2026-08-26
- **Нотатка:** Це стандартне Linux налаштування для безпеки. Серійні пристрої визначені в /etc/udev/rules.d/ з групою dialout. Нова група вступає в силу тільки після переходу, не просто logoff. Це часта "пастка" для новачків.
- **Прохід:** m2-72-symptoms-29

---

<!-- fc id:T-17-123 sha:1070199a src:manual/17-esptool.md:293 klas:F -->
### T-17-123 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Не лікувати це запуском через `sudo`.

**Контекст**

```
## Типові помилки і що вони означають

Права, не залізо. Linux: група `dialout`, потім **перезайти в систему**
(картка [К3](#k-pidkl)). Не лікувати це запуском через `sudo`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-124 sha:7c5d9fa9 src:manual/17-esptool.md:295 klas:A -->
### T-17-124 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **`Device or resource busy`**

**Контекст**

```
## Типові помилки і що вони означають

**`Device or resource busy`**
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 10 звірив ці рядки й виправив шість вигаданих. Тут лише розширено досяжність: та сама четвірка живе в таблиці симптомів додатка B по три комірки на рядок (причина, дія, розділ), у розділах 09, 17 і 25.
Два з чотирьох рядків — не від `esptool`, а від операційної системи, і книга це каже правильно: `Permission denied` лікується групою `dialout` із перезаходом, `Device or resource busy` — закритим монітором. Обидва тексти дає сам Python при відкритті порту.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-125 sha:d0ad404c src:manual/17-esptool.md:297 klas:F -->
### T-17-125 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Порт тримає інша програма: монітор, Arduino IDE, `screen`.

**Контекст**

```
## Типові помилки і що вони означають

Порт тримає інша програма: монітор, Arduino IDE, `screen`. Одночасно
порт відкриває лише один процес.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-126 sha:cf4197d0 src:manual/17-esptool.md:297 klas:E -->
### T-17-126 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Одночасно порт відкриває лише один процес.

**Контекст**

```
## Типові помилки і що вони означають

Порт тримає інша програма: монітор, Arduino IDE, `screen`. Одночасно
порт відкриває лише один процес.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-127 sha:e7619250 src:manual/17-esptool.md:300 klas:A -->
### T-17-127 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **`A fatal error occurred: MD5 of file does not match data in flash!`**

**Контекст**

```
## Типові помилки і що вони означають

**`A fatal error occurred: MD5 of file does not match data in flash!`**
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-128 sha:c6ae817f src:manual/17-esptool.md:302 klas:E -->
### T-17-128 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Записалося не те, що передавали.

**Контекст**

```
## Типові помилки і що вони означають

Записалося не те, що передавали. Причини за частотою: погане живлення,
довгий чи неякісний кабель, завелика швидкість, зношений флеш. Знизити
`--baud`, повторити. Повторюється стабільно на тій самій адресі —
підозра на пошкоджену комірку флешу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-129 sha:dc7b5a5b src:manual/17-esptool.md:302 klas:E -->
### T-17-129 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Причини за частотою: погане живлення, довгий чи неякісний кабель, завелика швидкість, зношений флеш.

**Контекст**

```
## Типові помилки і що вони означають

Записалося не те, що передавали. Причини за частотою: погане живлення,
довгий чи неякісний кабель, завелика швидкість, зношений флеш. Знизити
`--baud`, повторити. Повторюється стабільно на тій самій адресі —
підозра на пошкоджену комірку флешу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-130 sha:ea00dd94 src:manual/17-esptool.md:303 klas:F -->
### T-17-130 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Знизити `--baud`, повторити.

**Контекст**

```
## Типові помилки і що вони означають

Записалося не те, що передавали. Причини за частотою: погане живлення,
довгий чи неякісний кабель, завелика швидкість, зношений флеш. Знизити
`--baud`, повторити. Повторюється стабільно на тій самій адресі —
підозра на пошкоджену комірку флешу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-131 sha:acad2592 src:manual/17-esptool.md:304 klas:C -->
### T-17-131 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Повторюється стабільно на тій самій адресі — підозра на пошкоджену комірку флешу.

**Контекст**

```
## Типові помилки і що вони означають

Записалося не те, що передавали. Причини за частотою: погане живлення,
довгий чи неякісний кабель, завелика швидкість, зношений флеш. Знизити
`--baud`, повторити. Повторюється стабільно на тій самій адресі —
підозра на пошкоджену комірку флешу.
```

**Доказ**

- **Статус:** named-unreachable — secondary — the source cannot be reached from here; URL recorded, no quote
- **Джерело:** ESP32 Flash Memory Specification
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32 Flash Memory Specification
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** queue-c-17-esptool

---

<!-- fc id:T-17-132 sha:ec91ebc5 src:manual/17-esptool.md:307 klas:F -->
### T-17-132 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **`Invalid head of packet (0x00)`**

**Контекст**

```
## Типові помилки і що вони означають

**`Invalid head of packet (0x00)`**
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-133 sha:290a4865 src:manual/17-esptool.md:309 klas:E -->
### T-17-133 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Зв'язок є, але на лінії сміття.

**Контекст**

```
## Типові помилки і що вони означають

Зв'язок є, але на лінії сміття. Класично — плата стартує в застосунок,
який сам щось пише в UART, поки `esptool` намагається говорити.
Увійти в download mode вручну.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-134 sha:5e738a7f src:manual/17-esptool.md:309 klas:A -->
### T-17-134 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Класично — плата стартує в застосунок, який сам щось пише в UART, поки `esptool` намагається говорити.

**Контекст**

```
## Типові помилки і що вони означають

Зв'язок є, але на лінії сміття. Класично — плата стартує в застосунок,
який сам щось пише в UART, поки `esptool` намагається говорити.
Увійти в download mode вручну.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Чотири твердження розділу 17, які досі не мали доказу, бо стояли не в блоках коду, а в поясненнях: механізм stub, автоскидання через `DTR`/`RTS`, повідомлення про розбіжність чипа і причина «застосунок пише в UART».
Останнє варте уваги: воно пояснює `Invalid head of packet` із сусіднього запису — плата не мовчить, а говорить своє, і `esptool` бачить чуже в потоці. Дві половини одного симптому тепер обидві звірені.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-135 sha:c0befa74 src:manual/17-esptool.md:311 klas:E -->
### T-17-135 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Увійти в download mode вручну.

**Контекст**

```
## Типові помилки і що вони означають

Зв'язок є, але на лінії сміття. Класично — плата стартує в застосунок,
який сам щось пише в UART, поки `esptool` намагається говорити.
Увійти в download mode вручну.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-136 sha:c229b138 src:manual/17-esptool.md:313 klas:A -->
### T-17-136 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **`This chip is ESP32-S3, not ESP32.

**Контекст**

```
## Типові помилки і що вони означають

**`This chip is ESP32-S3, not ESP32. Wrong chip argument?`**
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-137 sha:2d9087c4 src:manual/17-esptool.md:315 klas:A -->
### T-17-137 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `esptool` визначив чип сам і побачив розбіжність із тим, що йому сказали.

**Контекст**

```
## Типові помилки і що вони означають

`esptool` визначив чип сам і побачив розбіжність із тим, що йому сказали.
Прибрати `--chip`, дати визначити автоматично.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Чотири твердження розділу 17, які досі не мали доказу, бо стояли не в блоках коду, а в поясненнях: механізм stub, автоскидання через `DTR`/`RTS`, повідомлення про розбіжність чипа і причина «застосунок пише в UART».
Останнє варте уваги: воно пояснює `Invalid head of packet` із сусіднього запису — плата не мовчить, а говорить своє, і `esptool` бачить чуже в потоці. Дві половини одного симптому тепер обидві звірені.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-138 sha:efdb570a src:manual/17-esptool.md:316 klas:F -->
### T-17-138 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Прибрати `--chip`, дати визначити автоматично.

**Контекст**

```
## Типові помилки і що вони означають

`esptool` визначив чип сам і побачив розбіжність із тим, що йому сказали.
Прибрати `--chip`, дати визначити автоматично.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-139 sha:8a18dd3e src:manual/17-esptool.md:318 klas:F -->
### T-17-139 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **Плата лишається в download mode після прошивки** [[S3]] [[C3]]

**Контекст**

```
## Типові помилки і що вони означають

**Плата лишається в download mode після прошивки** [[S3]] [[C3]]
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-140 sha:f7560ce0 src:manual/17-esptool.md:320 klas:E -->
### T-17-140 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Прошивка пройшла, а застосунок не стартував: чип так і сидить у завантажувачі.

**Контекст**

```
## Типові помилки і що вони означають

Прошивка пройшла, а застосунок не стартував: чип так і сидить у
завантажувачі. На платах із native USB (картка [К3](#k-pidkl)) причина в
тому, що скидання по лінії `RTS` через USB-Serial/JTAG не завжди
спрацьовує — фізичної лінії там немає.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-141 sha:567f0570 src:manual/17-esptool.md:321 klas:A -->
### T-17-141 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> На платах із native USB (картка [К3](#k-pidkl)) причина в тому, що скидання по лінії `RTS` через USB-Serial/JTAG не завжди спрацьовує — фізичної лінії там немає.

**Контекст**

```
## Типові помилки і що вони означають

Прошивка пройшла, а застосунок не стартував: чип так і сидить у
завантажувачі. На платах із native USB (картка [К3](#k-pidkl)) причина в
тому, що скидання по лінії `RTS` через USB-Serial/JTAG не завжди
спрацьовує — фізичної лінії там немає.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-142 sha:f93a70ab src:manual/17-esptool.md:325 klas:F -->
### T-17-142 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Обхід — скидання внутрішнім watchdog замість `RTS`:

**Контекст**

```
## Типові помилки і що вони означають

Обхід — скидання внутрішнім watchdog замість `RTS`:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-143 sha:c2ed87c0 src:manual/17-esptool.md:327 klas:K -->
### T-17-143 · kod · `manual/17-esptool.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyACM0 --after watchdog-reset write-flash 0x0 vyrib.bin
> ```

**Контекст**

````
## Типові помилки і що вони означають

```
esptool --port /dev/ttyACM0 --after watchdog-reset write-flash 0x0 vyrib.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-144 sha:e196de7b src:manual/17-esptool.md:328 klas:A -->
### T-17-144 · kod-ryadok · `manual/17-esptool.md`

**Твердження, коротко**

> esptool --port /dev/ttyACM0 --after watchdog-reset write-flash 0x0 vyrib.bin

**Контекст**

````
## Типові помилки і що вони означають

```
esptool --port /dev/ttyACM0 --after watchdog-reset write-flash 0x0 vyrib.bin
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-145 sha:10d41f6e src:manual/17-esptool.md:331 klas:A -->
### T-17-145 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Побічний ефект, до якого треба бути готовим: порт перелічується заново, і `/dev/ttyACM0` може стати `/dev/ttyACM1`.

**Контекст**

```
## Типові помилки і що вони означають

Побічний ефект, до якого треба бути готовим: порт перелічується заново,
і `/dev/ttyACM0` може стати `/dev/ttyACM1`. Монітор доведеться відкрити
на новому імені.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-146 sha:6ac44b20 src:manual/17-esptool.md:332 klas:E -->
### T-17-146 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Монітор доведеться відкрити на новому імені.

**Контекст**

```
## Типові помилки і що вони означають

Побічний ефект, до якого треба бути готовим: порт перелічується заново,
і `/dev/ttyACM0` може стати `/dev/ttyACM1`. Монітор доведеться відкрити
на новому імені.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-147 sha:59239464 src:manual/17-esptool.md:335 klas:F -->
### T-17-147 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> На ESP32 classic, C6 і H2 цього режиму немає — там працює звичайне `hard-reset` по `RTS`.

**Контекст**

```
## Типові помилки і що вони означають

На ESP32 classic, C6 і H2 цього режиму немає — там працює звичайне
`hard-reset` по `RTS`.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-148 sha:391b6f3d src:manual/17-esptool.md:338 klas:A -->
### T-17-148 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> **`Failed to start stub flasher.

**Контекст**

```
## Типові помилки і що вони означають

**`Failed to start stub flasher. There was no response.`**
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-149 sha:2d2315ba src:manual/17-esptool.md:338 klas:A -->
### T-17-149 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> There was no response.`**

**Контекст**

```
## Типові помилки і що вони означають

**`Failed to start stub flasher. There was no response.`**
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/loader.py
- **Дослівно з джерела:**
  > Serial data stream stopped: Possible serial noise or corruption
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Помилка синхронізації - немає відповіді від чипа
- **Прохід:** sweep-17-esptool

---

<!-- fc id:T-17-150 sha:6f4d2986 src:manual/17-esptool.md:340 klas:A -->
### T-17-150 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `esptool` вантажить у RAM невелику допоміжну програму («stub») для пришвидшення.

**Контекст**

```
## Типові помилки і що вони означають

`esptool` вантажить у RAM невелику допоміжну програму («stub») для
пришвидшення. На частині клонів це не працює. Обійти: `--no-stub`,
буде повільніше, але працюватиме.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Чотири твердження розділу 17, які досі не мали доказу, бо стояли не в блоках коду, а в поясненнях: механізм stub, автоскидання через `DTR`/`RTS`, повідомлення про розбіжність чипа і причина «застосунок пише в UART».
Останнє варте уваги: воно пояснює `Invalid head of packet` із сусіднього запису — плата не мовчить, а говорить своє, і `esptool` бачить чуже в потоці. Дві половини одного симптому тепер обидві звірені.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-17-151 sha:4a61aa2a src:manual/17-esptool.md:341 klas:E -->
### T-17-151 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> На частині клонів це не працює.

**Контекст**

```
## Типові помилки і що вони означають

`esptool` вантажить у RAM невелику допоміжну програму («stub») для
пришвидшення. На частині клонів це не працює. Обійти: `--no-stub`,
буде повільніше, але працюватиме.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-152 sha:6c0640de src:manual/17-esptool.md:341 klas:F -->
### T-17-152 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Обійти: `--no-stub`, буде повільніше, але працюватиме.

**Контекст**

```
## Типові помилки і що вони означають

`esptool` вантажить у RAM невелику допоміжну програму («stub») для
пришвидшення. На частині клонів це не працює. Обійти: `--no-stub`,
буде повільніше, але працюватиме.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-153 sha:0df8e570 src:manual/17-esptool.md:344 klas:A -->
### T-17-153 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Сусіднє попередження `Stub flasher has been disabled for compatibility, set --no-stub to suppress this warning.` — не помилка: `esptool` сам вимкнув stub і працює далі.

**Контекст**

```
## Типові помилки і що вони означають

Сусіднє попередження `Stub flasher has been disabled for compatibility,
set --no-stub to suppress this warning.` — не помилка: `esptool` сам
вимкнув stub і працює далі.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-154 sha:d286f7b3 src:manual/17-esptool.md:348 klas:F -->
### T-17-154 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> У v4 ті самі рядки коротші — `Failed to start stub.` Шукати варто за словом `stub`, а не за повним реченням.

**Контекст**

```
## Типові помилки і що вони означають

У v4 ті самі рядки коротші — `Failed to start stub.` Шукати варто за
словом `stub`, а не за повним реченням.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-155 sha:2a9519b0 src:manual/17-esptool.md:353 klas:E -->
### T-17-155 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Espressif дає графічну програму (Flash Download Tool) — той самий функціонал у вікні.

**Контекст**

```
## Windows: Flash Download Tool

Espressif дає графічну програму (Flash Download Tool) — той самий
функціонал у вікні. Вона зручна там, де прошивку заливає людина без
командного рядка: оператор на складанні, замовник, колега.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-156 sha:918d6503 src:manual/17-esptool.md:354 klas:E -->
### T-17-156 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Вона зручна там, де прошивку заливає людина без командного рядка: оператор на складанні, замовник, колега.

**Контекст**

```
## Windows: Flash Download Tool

Espressif дає графічну програму (Flash Download Tool) — той самий
функціонал у вікні. Вона зручна там, де прошивку заливає людина без
командного рядка: оператор на складанні, замовник, колега.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-157 sha:313ef396 src:manual/17-esptool.md:357 klas:F -->
### T-17-157 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Практично: підготувати `merge-bin`-образ, налаштувати один раз, зберегти конфігурацію і передати разом з інструкцією на одну сторінку (розділ 56).

**Контекст**

```
## Windows: Flash Download Tool

Практично: підготувати `merge-bin`-образ, налаштувати один раз, зберегти
конфігурацію і передати разом з інструкцією на одну сторінку (розділ 56).
Все, що складніше, робиться з командного рядка — його простіше
відтворити і покласти в скрипт.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-158 sha:e977c57d src:manual/17-esptool.md:359 klas:E -->
### T-17-158 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Все, що складніше, робиться з командного рядка — його простіше відтворити і покласти в скрипт.

**Контекст**

```
## Windows: Flash Download Tool

Практично: підготувати `merge-bin`-образ, налаштувати один раз, зберегти
конфігурацію і передати разом з інструкцією на одну сторінку (розділ 56).
Все, що складніше, робиться з командного рядка — його простіше
відтворити і покласти в скрипт.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-159 sha:2d322667 src:manual/17-esptool.md:364 klas:A -->
### T-17-159 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Перевірити версію `esptool` **перш ніж** копіювати команду звідкись.

**Контекст**

```
## Що з цього треба запам'ятати

Перевірити версію `esptool` **перш ніж** копіювати команду звідкись.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst, .../docs/en/migration-guide.rst, https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/storage/nvs_flash.rst
- **Дослівно з джерела:**
  > (basic-commands.rst)
  > Read SPI Flash ID: ``flash-id``
  > Example output:
  >     Manufacturer: e0
  >     Device: 4016
  >     Detected flash size: 4MB
  > 
  > To erase the entire flash chip (all data replaced with 0xFF bytes):
  >     esptool erase-flash
  > 
  > (nvs_flash.rst)
  > if an NVS partition is truncated (for example, when the partition
  > table layout is changed), its contents should be erased.
  > 
  > (migration-guide.rst)
  > All the commands and options have been renamed to use ``-`` instead
  > of ``_`` as a separator (e.g., ``write_flash`` -> ``write-flash``).
  > Old command and option names are **deprecated**.
- **Спосіб і дата:** curl raw.githubusercontent через агента пулу (шматок 6), 2026-08-26; взірець і клас — М1
- **Нотатка:** Найцінніше — перший пункт переліку «коли `erase-flash` справді потрібен». Книга називала його з досвіду; `nvs_flash.rst` каже те саме прямо: обрізаний при зміні розбивки розділ NVS **треба** стерти. Порада з практики збіглася з вимогою документації.
- **Прохід:** pass-34-pul-shmatok-6

---

<!-- fc id:T-17-160 sha:4430be4b src:manual/17-esptool.md:366 klas:A -->
### T-17-160 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Сімейство, ревізію і MAC друкує **преамбула з'єднання**, а не окрема команда.

**Контекст**

```
## Що з цього треба запам'ятати

Сімейство, ревізію і MAC друкує **преамбула з'єднання**, а не окрема
команда. `flash-id` — перша команда для будь-якої незнайомої плати:
шапка плюс обсяг флешу.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- **Дослівно з джерела:**
  > # 2) Print the chip info
  > ...
  > else:
  >     log.print(f"{'Chip type:':<20}{esp.get_chip_description()}")
  >     log.print(f"{'Features:':<20}{', '.join(esp.get_chip_features())}")
  >     log.print(f"{'Crystal frequency:':<20}{esp.get_crystal_freq()}MHz")
  >     usb_mode = esp.get_usb_mode()
  >     if usb_mode is not None:
  >         log.print(f"{'USB mode:':<20}{usb_mode}")
  >     read_mac(esp)
- **Спосіб і дата:** curl raw.githubusercontent, перевірено М1, 2026-08-26
- **Нотатка:** Цей блок виконується **до** виклику підкоманди й не залежить від того, яка вона. Тому будь-яка команда, що взагалі під'єдналася, уже назвала сімейство, ревізію, частоту кристала й MAC.
Практичний наслідок для книги виявився ширшим за виправлення: правило «перша команда для незнайомої плати» тепер `flash-id` не тому, що вона краще ідентифікує чип, а тому, що вона додає до безкоштовної шапки те єдине, чого в шапці немає, — обсяг флешу.
Виправлено в одинадцяти місцях: розділи 08, 17, 20, 21, 23, картки К1 і К10, додаток C, дві вкладки. Формулювання заведено в `factcheck/SPROSTOVANE.md`, взірець випробувано вставкою старої фрази в розділ 23 — знаходиться.
Виняток у взірці на `manual/17-esptool.md` навмисний: розділ 17 тепер **пояснює**, чому команди краще не вживати, і мусить цитувати її назву.
- **Прохід:** pass-36-chip-id

---

<!-- fc id:T-17-161 sha:2afe9b5f src:manual/17-esptool.md:367 klas:B -->
### T-17-161 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `flash-id` — перша команда для будь-якої незнайомої плати: шапка плюс обсяг флешу.

**Контекст**

```
## Що з цього треба запам'ятати

Сімейство, ревізію і MAC друкує **преамбула з'єднання**, а не окрема
команда. `flash-id` — перша команда для будь-якої незнайомої плати:
шапка плюс обсяг флешу.
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > esptool provides commands for flash operations
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, grep flash, 2026-08-26
- **Нотатка:** Текст T-17-034 описує flash-id як команду. Джерело підтверджує наявність flash операцій в esptool.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-17-162 sha:a7f08f37 src:manual/17-esptool.md:370 klas:B -->
### T-17-162 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `read-flash` робиться до першої зміни.

**Контекст**

```
## Що з цього треба запам'ятати

`read-flash` робиться до першої зміни. Розмір файлу звіряється з обсягом
флешу одразу.
```

**Доказ**

- **Статус:** derived — primary, inferred — the source was obtained; the claim follows unambiguously
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

<!-- fc id:T-17-163 sha:0de9cf8b src:manual/17-esptool.md:370 klas:E -->
### T-17-163 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> Розмір файлу звіряється з обсягом флешу одразу.

**Контекст**

```
## Що з цього треба запам'ятати

`read-flash` робиться до першої зміни. Розмір файлу звіряється з обсягом
флешу одразу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-17-164 sha:42368b26 src:manual/17-esptool.md:373 klas:A -->
### T-17-164 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `verify-flash` перетворює «прошилося» на «у флеші лежить те, що треба».

**Контекст**

```
## Що з цього треба запам'ятати

`verify-flash` перетворює «прошилося» на «у флеші лежить те, що треба».
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-17-165 sha:33a8f7c8 src:manual/17-esptool.md:375 klas:A -->
### T-17-165 · proza · `manual/17-esptool.md`

**Твердження, коротко**

> `merge-bin` — формат передачі прошивки людині, яка не мусить знати адрес.

**Контекст**

```
## Що з цього треба запам'ятати

`merge-bin` — формат передачі прошивки людині, яка не мусить знати
адрес.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---
