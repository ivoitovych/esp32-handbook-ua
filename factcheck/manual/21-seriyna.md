# Фактчекінг: `manual/21-seriyna.md`

Одиниць твердження: **98**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-21-001 sha:5494609e src:manual/21-seriyna.md:3 klas:F -->
### T-21-001 · proza · рядок 3

**Книга каже, дослівно:**

> Прошити одну плату і прошити двадцять — різні задачі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-002 sha:f740932a src:manual/21-seriyna.md:3 klas:F -->
### T-21-002 · proza · рядок 3

**Книга каже, дослівно:**

> Різниця не в масштабі, а в тому, що при двадцяти платах з'являються питання, яких на одній не буває: чи всі прошилися, чи всі прошилися **однаково**, яка версія куди поїхала, і що робити з тим, що в кожної плати має бути своє.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-003 sha:aa2a0e34 src:manual/21-seriyna.md:8 klas:D -->
### T-21-003 · proza · рядок 8

**Книга каже, дослівно:**

> Той, хто прийшов сюди прошити партію готових плат, може не читати ні про FreeRTOS, ні про периферію: маршрут іде сюди і на картку [К15](#k-seriyna).

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

<!-- fc id:T-21-004 sha:7aee2849 src:manual/21-seriyna.md:14 klas:F -->
### T-21-004 · proza · рядок 14

**Книга каже, дослівно:**

> Три файли на трьох адресах — нормально для розробки і погано для виробництва: три нагоди помилитися, помножені на кількість плат.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-005 sha:fd16eb2f src:manual/21-seriyna.md:17 klas:F -->
### T-21-005 · proza · рядок 17

**Книга каже, дослівно:**

> Складіть один образ (розділ 17).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-006 sha:169c5b39 src:manual/21-seriyna.md:17 klas:F -->
### T-21-006 · proza · рядок 17

**Книга каже, дослівно:**

> Якщо проєкт ESP-IDF під рукою — цим і обмежтеся, бо адреси підставить сама збірка:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-007 sha:56d43d34 src:manual/21-seriyna.md:20 klas:K -->
### T-21-007 · kod · рядок 20

**Книга каже, дослівно:**

> ```
> idf.py merge-bin -o vyrib-v1.4.bin
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

<!-- fc id:T-21-008 sha:4286f2a3 src:manual/21-seriyna.md:21 klas:A -->
### T-21-008 · kod-ryadok · рядок 21

**Книга каже, дослівно:**

> idf.py merge-bin -o vyrib-v1.4.bin

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

<!-- fc id:T-21-009 sha:21613fb4 src:manual/21-seriyna.md:24 klas:F -->
### T-21-009 · proza · рядок 24

**Книга каже, дослівно:**

> Для виробництва це кращий варіант за ручний: жодного числа, набраного з голови, а отже й жодної нагоди зсунути бутлоадер.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-010 sha:dc6bff36 src:manual/21-seriyna.md:27 klas:F -->
### T-21-010 · proza · рядок 27

**Книга каже, дослівно:**

> Коли ж на руках лише готові `.bin`-файли — збирати доводиться вручну; [[classic]] адреси нижче для classic і S2, для решти чипів адреса бутлоадера інша (таблиця в розділі 16):

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-011 sha:fd180332 src:manual/21-seriyna.md:31 klas:K -->
### T-21-011 · kod · рядок 31

**Книга каже, дослівно:**

> ```
> esptool --chip esp32 merge-bin -o vyrib-v1.4.bin --flash-mode dio \
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

<!-- fc id:T-21-012 sha:2ded8ac2 src:manual/21-seriyna.md:32 klas:A -->
### T-21-012 · kod-ryadok · рядок 32

**Книга каже, дослівно:**

> esptool --chip esp32 merge-bin -o vyrib-v1.4.bin --flash-mode dio \

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

<!-- fc id:T-21-013 sha:99dac3f2 src:manual/21-seriyna.md:38 klas:F -->
### T-21-013 · proza · рядок 38

**Книга каже, дослівно:**

> Далі кожна плата прошивається однією командою з однією адресою:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-014 sha:7c27876f src:manual/21-seriyna.md:40 klas:K -->
### T-21-014 · kod · рядок 40

**Книга каже, дослівно:**

> ```
> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.4.bin
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

<!-- fc id:T-21-015 sha:060d1904 src:manual/21-seriyna.md:41 klas:A -->
### T-21-015 · kod-ryadok · рядок 41

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.4.bin

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

<!-- fc id:T-21-016 sha:d76a9957 src:manual/21-seriyna.md:44 klas:F -->
### T-21-016 · proza · рядок 44

**Книга каже, дослівно:**

> Тепер операцію можна віддати людині, яка нічого не знає про адреси розділів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-017 sha:1c051eb7 src:manual/21-seriyna.md:48 klas:F -->
### T-21-017 · proza · рядок 48

**Книга каже, дослівно:**

> `--chip` у `merge-bin` обов'язковий, бо порту немає й визначати чип нема звідки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-018 sha:f1d48cb7 src:manual/21-seriyna.md:48 klas:F -->
### T-21-018 · proza · рядок 48

**Книга каже, дослівно:**

> Він же задає, з якою адресою бутлоадера образ має сенс.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-019 sha:378d2fc5 src:manual/21-seriyna.md:51 klas:F -->
### T-21-019 · proza · рядок 51

**Книга каже, дослівно:**

> `--flash-mode`, `--flash-size` і `--flash-freq` у `merge-bin` мають збігатися з тим, під що зібрано прошивку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-020 sha:27deca81 src:manual/21-seriyna.md:51 klas:F -->
### T-21-020 · proza · рядок 51

**Книга каже, дослівно:**

> Розбіжність дає плату, яка прошилася без помилок і не стартує.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-021 sha:a6125283 src:manual/21-seriyna.md:51 klas:F -->
### T-21-021 · proza · рядок 51

**Книга каже, дослівно:**

> Найпростіше — узяти значення з `sdkconfig` проєкту, а не вгадувати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-022 sha:ac7a1ba1 src:manual/21-seriyna.md:59 klas:F -->
### T-21-022 · proza · рядок 59

**Книга каже, дослівно:**

> Ручна команда в терміналі не масштабується: помилку в ній видно не одразу і не завжди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-023 sha:01a36707 src:manual/21-seriyna.md:59 klas:F -->
### T-21-023 · proza · рядок 59

**Книга каже, дослівно:**

> Мінімальний скрипт, який робить прошивку і **перевірку**:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-024 sha:41cc9c7f src:manual/21-seriyna.md:62 klas:K -->
### T-21-024 · kod · рядок 62

**Книга каже, дослівно:**

> ```sh
> #!/bin/sh
> set -e
> PORT="${1:?вкажіть порт: ./flash.sh /dev/ttyUSB0}"
> IMAGE=vyrib-v1.4.bin
> 
> esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"
> esptool --port "$PORT" verify-flash 0x0 "$IMAGE"
> esptool --port "$PORT" chip-id | grep -i "MAC:"
> echo "OK: $PORT"
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

<!-- fc id:T-21-025 sha:23224667 src:manual/21-seriyna.md:68 klas:A -->
### T-21-025 · kod-ryadok · рядок 68

**Книга каже, дослівно:**

> esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"

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

<!-- fc id:T-21-026 sha:1442de15 src:manual/21-seriyna.md:69 klas:A -->
### T-21-026 · kod-ryadok · рядок 69

**Книга каже, дослівно:**

> esptool --port "$PORT" verify-flash 0x0 "$IMAGE"

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

<!-- fc id:T-21-027 sha:e7dfc363 src:manual/21-seriyna.md:70 klas:A -->
### T-21-027 · kod-ryadok · рядок 70

**Книга каже, дослівно:**

> esptool --port "$PORT" chip-id | grep -i "MAC:"

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

<!-- fc id:T-21-028 sha:270a6061 src:manual/21-seriyna.md:74 klas:F -->
### T-21-028 · proza · рядок 74

**Книга каже, дослівно:**

> Три речі, які тут важливі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-029 sha:12bbf3c5 src:manual/21-seriyna.md:74 klas:F -->
### T-21-029 · proza · рядок 74

**Книга каже, дослівно:**

> `set -e` зупиняє скрипт на першій помилці — інакше збій прошивки лишиться непоміченим у потоці виводу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-030 sha:42368b26 src:manual/21-seriyna.md:74 klas:A -->
### T-21-030 · proza · рядок 74

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

<!-- fc id:T-21-031 sha:16350670 src:manual/21-seriyna.md:74 klas:F -->
### T-21-031 · proza · рядок 74

**Книга каже, дослівно:**

> Виведений MAC іде в журнал: це єдиний надійний ідентифікатор плати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-032 sha:e3f39fae src:manual/21-seriyna.md:81 klas:F -->
### T-21-032 · proza · рядок 81

**Книга каже, дослівно:**

> «Прошилося без помилок» — не критерій приймання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-033 sha:d1d7cedd src:manual/21-seriyna.md:81 klas:F -->
### T-21-033 · proza · рядок 81

**Книга каже, дослівно:**

> Мінімальний контроль, який ловить майже все:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-034 sha:ddc59055 src:manual/21-seriyna.md:84 klas:A -->
### T-21-034 · proza · рядок 84

**Книга каже, дослівно:**

> **`verify-flash`** — вміст флешу відповідає образу. 2.

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

<!-- fc id:T-21-035 sha:1d35be73 src:manual/21-seriyna.md:84 klas:F -->
### T-21-035 · proza · рядок 84

**Книга каже, дослівно:**

> **Скидання і читання boot-логу** — пристрій справді стартує (розділ 16). 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-036 sha:a414fea1 src:manual/21-seriyna.md:84 klas:F -->
### T-21-036 · proza · рядок 84

**Книга каже, дослівно:**

> **Одна функціональна перевірка** — те, заради чого виріб існує: світлодіод блимає, датчик читається, точка доступу піднялася.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-037 sha:c6467fae src:manual/21-seriyna.md:89 klas:F -->
### T-21-037 · proza · рядок 89

**Книга каже, дослівно:**

> Третій пункт ловить те, чого не спіймають перші два: справний образ, залитий на плату з непропаяним модулем або мертвим датчиком.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-038 sha:621d4059 src:manual/21-seriyna.md:93 klas:F -->
### T-21-038 · proza · рядок 93

**Книга каже, дослівно:**

> Партія — це саме те місце, де вилазить межове живлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-039 sha:d5049633 src:manual/21-seriyna.md:93 klas:A -->
### T-21-039 · proza · рядок 93

**Книга каже, дослівно:**

> Двадцять плат прошиваються по черзі, USB-хаб гріється, напруга просідає, і десь на чотирнадцятій починаються `MD5 of file does not match`.

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

<!-- fc id:T-21-040 sha:432b092c src:manual/21-seriyna.md:93 klas:F -->
### T-21-040 · proza · рядок 93

**Книга каже, дослівно:**

> Живлення для серійної прошивки — окреме, з запасом, і бажано не від ноутбука.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-041 sha:1a3a9559 src:manual/21-seriyna.md:101 klas:F -->
### T-21-041 · proza · рядок 101

**Книга каже, дослівно:**

> Найчастіша помилка серійного виробництва — залити двадцятьом платам однаковий образ разом із однаковим серійним номером, однаковим ключем і однаковим ім'ям пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-042 sha:6c7e3e50 src:manual/21-seriyna.md:101 klas:F -->
### T-21-042 · proza · рядок 101

**Книга каже, дослівно:**

> Наслідки виявляються пізно, у полі, і виглядають як містика: два пристрої «крадуть» одне в одного з'єднання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-043 sha:3140d22c src:manual/21-seriyna.md:106 klas:F -->
### T-21-043 · proza · рядок 106

**Книга каже, дослівно:**

> Правильна схема розділяє два шари:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-044 sha:1cfc3ebd src:manual/21-seriyna.md:108 klas:F -->
### T-21-044 · proza · рядок 108

**Книга каже, дослівно:**

> **Спільне** — образ прошивки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-045 sha:ac0e1bb8 src:manual/21-seriyna.md:108 klas:F -->
### T-21-045 · proza · рядок 108

**Книга каже, дослівно:**

> Однаковий для всієї партії, з `merge-bin`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-046 sha:c50488dc src:manual/21-seriyna.md:110 klas:F -->
### T-21-046 · proza · рядок 110

**Книга каже, дослівно:**

> **Унікальне** — конфігурація в NVS.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-047 sha:5ee74ccf src:manual/21-seriyna.md:110 klas:F -->
### T-21-047 · proza · рядок 110

**Книга каже, дослівно:**

> Своя для кожної плати: серійний номер, ключі, калібрувальні коефіцієнти, ім'я.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-048 sha:8fbe10a5 src:manual/21-seriyna.md:113 klas:F -->
### T-21-048 · proza · рядок 113

**Книга каже, дослівно:**

> ESP-IDF дає інструмент, який робить із CSV готовий образ розділу NVS:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-049 sha:fc2721f0 src:manual/21-seriyna.md:115 klas:K -->
### T-21-049 · kod · рядок 115

**Книга каже, дослівно:**

> ```
> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
> esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin
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

<!-- fc id:T-21-050 sha:aa33e38e src:manual/21-seriyna.md:116 klas:F -->
### T-21-050 · kod-ryadok · рядок 116

**Книга каже, дослівно:**

> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-051 sha:dab0dee5 src:manual/21-seriyna.md:117 klas:A -->
### T-21-051 · kod-ryadok · рядок 117

**Книга каже, дослівно:**

> esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin

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

<!-- fc id:T-21-052 sha:b0a670d8 src:manual/21-seriyna.md:120 klas:F -->
### T-21-052 · proza · рядок 120

**Книга каже, дослівно:**

> Адреса `0x9000` — початок розділу `nvs` у стандартній розбивці; звірити зі своєю таблицею розділів (розділ 18).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-053 sha:a441973a src:manual/21-seriyna.md:123 klas:F -->
### T-21-053 · proza · рядок 123

**Книга каже, дослівно:**

> Альтернатива для невеликих партій: заливати спільний образ, а унікальне записувати через консоль після першого старту — прошивка при першому запуску просить серійний номер і зберігає його в NVS.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-054 sha:168c664c src:manual/21-seriyna.md:123 klas:F -->
### T-21-054 · proza · рядок 123

**Книга каже, дослівно:**

> Менше інструментів, але додає ручну операцію до кожної плати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-055 sha:82ff65b0 src:manual/21-seriyna.md:129 klas:F -->
### T-21-055 · proza · рядок 129

**Книга каже, дослівно:**

> MAC-адреса кожного чипа унікальна від заводу і лежить в eFuse.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-056 sha:8aa5ff33 src:manual/21-seriyna.md:129 klas:F -->
### T-21-056 · proza · рядок 129

**Книга каже, дослівно:**

> Якщо все, що вам потрібно, — відрізняти пристрої один від одного, окремий серійний номер не потрібен: беріть MAC.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-057 sha:5aed5cc9 src:manual/21-seriyna.md:129 klas:F -->
### T-21-057 · proza · рядок 129

**Книга каже, дослівно:**

> Це прибирає цілий шар роботи разом із нагодою помилитися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-058 sha:7afef3b1 src:manual/21-seriyna.md:137 klas:F -->
### T-21-058 · proza · рядок 137

**Книга каже, дослівно:**

> Плата без позначки — плата, про яку через місяць невідомо нічого.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-059 sha:80b6708b src:manual/21-seriyna.md:137 klas:F -->
### T-21-059 · proza · рядок 137

**Книга каже, дослівно:**

> На кожну наклеюється або пишеться маркером мінімум:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-060 sha:581413be src:manual/21-seriyna.md:140 klas:F -->
### T-21-060 · proza · рядок 140

**Книга каже, дослівно:**

> - порядковий номер у партії; - версія прошивки; - дата.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-061 sha:b8ed94db src:manual/21-seriyna.md:144 klas:F -->
### T-21-061 · proza · рядок 144

**Книга каже, дослівно:**

> Наліпка клеїться на бік, який видно в зібраному виробі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-062 sha:d888373f src:manual/21-seriyna.md:144 klas:F -->
### T-21-062 · proza · рядок 144

**Книга каже, дослівно:**

> Наліпка, що опинилася всередині корпусу, не існує.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-063 sha:669ee36d src:manual/21-seriyna.md:149 klas:F -->
### T-21-063 · proza · рядок 149

**Книга каже, дослівно:**

> Один файл на партію, рядок на плату:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-064 sha:75def2ca src:manual/21-seriyna.md:151 klas:F -->
### T-21-064 · tablycya-shapka · рядок 151

**Книга каже, дослівно:**

> | № | MAC | Версія | Дата | Контроль | Примітка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-065 sha:e706eb63 src:manual/21-seriyna.md:152 klas:F -->
### T-21-065 · komirka · рядок 152

**Книга каже, дослівно:**

> 0041 · MAC → `A0:B7:…:14`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-066 sha:a8bb95c8 src:manual/21-seriyna.md:152 klas:F -->
### T-21-066 · komirka · рядок 152

**Книга каже, дослівно:**

> 0041 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-067 sha:e4e73586 src:manual/21-seriyna.md:152 klas:F -->
### T-21-067 · komirka · рядок 152

**Книга каже, дослівно:**

> 0041 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-068 sha:29d3900f src:manual/21-seriyna.md:152 klas:F -->
### T-21-068 · komirka · рядок 152

**Книга каже, дослівно:**

> 0041 · Контроль → OK

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-069 sha:75799caf src:manual/21-seriyna.md:153 klas:F -->
### T-21-069 · komirka · рядок 153

**Книга каже, дослівно:**

> 0042 · MAC → `A0:B7:…:2C`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-070 sha:abb9bd4b src:manual/21-seriyna.md:153 klas:F -->
### T-21-070 · komirka · рядок 153

**Книга каже, дослівно:**

> 0042 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-071 sha:e2d0d5e3 src:manual/21-seriyna.md:153 klas:F -->
### T-21-071 · komirka · рядок 153

**Книга каже, дослівно:**

> 0042 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-072 sha:f7d5d679 src:manual/21-seriyna.md:153 klas:F -->
### T-21-072 · komirka · рядок 153

**Книга каже, дослівно:**

> 0042 · Контроль → OK

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-073 sha:c5831a43 src:manual/21-seriyna.md:153 klas:F -->
### T-21-073 · komirka · рядок 153

**Книга каже, дослівно:**

> 0042 · Примітка → корпус подряпаний

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-074 sha:79ce9a1f src:manual/21-seriyna.md:154 klas:F -->
### T-21-074 · komirka · рядок 154

**Книга каже, дослівно:**

> 0043 · MAC → `A0:B7:…:31`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-075 sha:9f488b42 src:manual/21-seriyna.md:154 klas:F -->
### T-21-075 · komirka · рядок 154

**Книга каже, дослівно:**

> 0043 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-076 sha:a6590e77 src:manual/21-seriyna.md:154 klas:F -->
### T-21-076 · komirka · рядок 154

**Книга каже, дослівно:**

> 0043 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-077 sha:37c1710c src:manual/21-seriyna.md:154 klas:F -->
### T-21-077 · komirka · рядок 154

**Книга каже, дослівно:**

> 0043 · Контроль → **брак**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-078 sha:4688c6c2 src:manual/21-seriyna.md:154 klas:F -->
### T-21-078 · komirka · рядок 154

**Книга каже, дослівно:**

> 0043 · Примітка → не стартує, модуль

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-079 sha:ee027464 src:manual/21-seriyna.md:157 klas:F -->
### T-21-079 · proza · рядок 157

**Книга каже, дослівно:**

> Цей файл відповідає на питання, які виникають через півроку і не мають іншого джерела відповіді: скільки зроблено, яка версія у пристрою з таким MAC, чи був цей екземпляр у браку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-080 sha:f8360aa5 src:manual/21-seriyna.md:161 klas:F -->
### T-21-080 · proza · рядок 161

**Книга каже, дослівно:**

> Разом із журналом зберігаються **самі файли прошивки** тієї версії, що поїхала, і, обов'язково, `.elf` того самого збирання: без нього backtrace з поля не розшифрувати (картка [К7](#k-panika)).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-081 sha:2e3ee5bc src:manual/21-seriyna.md:166 klas:F -->
### T-21-081 · proza · рядок 166

**Книга каже, дослівно:**

> Версія прошивки, яка поїхала до замовника, має існувати в архіві як файли, а не як «гілка в git, з якої це збиралося».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-082 sha:6b4d2e33 src:manual/21-seriyna.md:166 klas:F -->
### T-21-082 · proza · рядок 166

**Книга каже, дослівно:**

> Перезібрати «такий самий» образ пізніше майже ніколи не виходить точно: змінилася версія тулчейну, змінилася бібліотека, змінився шлях збирання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-083 sha:775f6652 src:manual/21-seriyna.md:166 klas:F -->
### T-21-083 · proza · рядок 166

**Книга каже, дослівно:**

> Адреси зсунуться, і `.elf` перестане відповідати тому, що в полі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-084 sha:f5a053c0 src:manual/21-seriyna.md:175 klas:F -->
### T-21-084 · proza · рядок 175

**Книга каже, дослівно:**

> Коли партія вимірюється сотнями, послідовна прошивка стає вузьким місцем.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-085 sha:c5052027 src:manual/21-seriyna.md:175 klas:F -->
### T-21-085 · proza · рядок 175

**Книга каже, дослівно:**

> Варіанти, у порядку складності:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-086 sha:7b5f5132 src:manual/21-seriyna.md:178 klas:F -->
### T-21-086 · proza · рядок 178

**Книга каже, дослівно:**

> **Кілька портів паралельно.** Скрипт запускається на `/dev/ttyUSB0`, `ttyUSB1`, `ttyUSB2` одночасно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-087 sha:03a8a283 src:manual/21-seriyna.md:178 klas:F -->
### T-21-087 · proza · рядок 178

**Книга каже, дослівно:**

> Найдешевший спосіб отримати кратне прискорення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-088 sha:73cabe58 src:manual/21-seriyna.md:178 klas:F -->
### T-21-088 · proza · рядок 178

**Книга каже, дослівно:**

> Обмеження — живлення хаба: чотири плати, що одночасно пишуть у флеш, дають помітний струм.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-089 sha:74a5c7c5 src:manual/21-seriyna.md:183 klas:F -->
### T-21-089 · proza · рядок 183

**Книга каже, дослівно:**

> **Flash Download Tool** (Windows) вміє кілька плат в одному вікні — зручно там, де прошиває оператор без командного рядка (розділ 17).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-090 sha:8bcfad00 src:manual/21-seriyna.md:186 klas:F -->
### T-21-090 · proza · рядок 186

**Книга каже, дослівно:**

> **Прошивка до монтажу**, на спеціальному ложементі з підпружиненими контактами (pogo pins).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-091 sha:eecd5522 src:manual/21-seriyna.md:186 klas:F -->
### T-21-091 · proza · рядок 186

**Книга каже, дослівно:**

> Це вже оснастка, і має сенс від сотень плат.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-092 sha:850d2dde src:manual/21-seriyna.md:191 klas:F -->
### T-21-092 · proza · рядок 191

**Книга каже, дослівно:**

> Відкласти плату, позначити, продовжити з рештою, розібратися потім — розділ 55 і картка [К8](#k-symptomy).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-093 sha:69e2ed79 src:manual/21-seriyna.md:191 klas:F -->
### T-21-093 · proza · рядок 191

**Книга каже, дослівно:**

> Найчастіші причини саме в партії: непропаяний модуль, замикання під час монтажу, плата іншої ревізії, що приїхала в тій самій коробці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-094 sha:39f098a2 src:manual/21-seriyna.md:198 klas:F -->
### T-21-094 · proza · рядок 198

**Книга каже, дослівно:**

> `merge-bin` — один файл, одна адреса, нема чого переплутати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-095 sha:81a87405 src:manual/21-seriyna.md:200 klas:A -->
### T-21-095 · proza · рядок 200

**Книга каже, дослівно:**

> `verify-flash` і функціональна перевірка — обов'язкові кроки, а не опції.

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

<!-- fc id:T-21-096 sha:26048fe4 src:manual/21-seriyna.md:202 klas:F -->
### T-21-096 · proza · рядок 202

**Книга каже, дослівно:**

> Спільний образ і унікальний NVS — це два різні шари.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-097 sha:ade9bd68 src:manual/21-seriyna.md:202 klas:F -->
### T-21-097 · proza · рядок 202

**Книга каже, дослівно:**

> Змішати їх означає отримати двадцять пристроїв з однаковою особистістю.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-098 sha:fd3cdf97 src:manual/21-seriyna.md:205 klas:F -->
### T-21-098 · proza · рядок 205

**Книга каже, дослівно:**

> Журнал партії і збережені файли прошивки разом із `.elf` — те, без чого через півроку неможливо відповісти на просте питання «що в цьому пристрої».

**Доказ**

- **Клас:** F — не звірено

---
