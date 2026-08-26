# Фактчекінг: `manual/21-seriyna.md`

Одиниць твердження: **91**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

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

<!-- fc id:T-21-003 sha:aa2a0e34 src:manual/21-seriyna.md:8 klas:F -->
### T-21-003 · proza · рядок 8

**Книга каже, дослівно:**

> Той, хто прийшов сюди прошити партію готових плат, може не читати ні про FreeRTOS, ні про периферію: маршрут іде сюди і на картку [К15](#k-seriyna).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-004 sha:7aee2849 src:manual/21-seriyna.md:14 klas:F -->
### T-21-004 · proza · рядок 14

**Книга каже, дослівно:**

> Три файли на трьох адресах — нормально для розробки і погано для виробництва: три нагоди помилитися, помножені на кількість плат.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-005 sha:aeed64f9 src:manual/21-seriyna.md:17 klas:F -->
### T-21-005 · proza · рядок 17

**Книга каже, дослівно:**

> Складіть один образ (розділ 17); [[classic]] адреси нижче — для classic і S2, для решти чипів адреса бутлоадера інша (таблиця в розділі 16):

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-006 sha:2fec7c9d src:manual/21-seriyna.md:20 klas:F -->
### T-21-006 · kod · рядок 20

**Книга каже, дослівно:**

> ```
> esptool merge-bin -o vyrib-v1.4.bin --flash-mode dio \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-007 sha:d650ca01 src:manual/21-seriyna.md:21 klas:F -->
### T-21-007 · kod-ryadok · рядок 21

**Книга каже, дослівно:**

> esptool merge-bin -o vyrib-v1.4.bin --flash-mode dio \

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-008 sha:99dac3f2 src:manual/21-seriyna.md:27 klas:F -->
### T-21-008 · proza · рядок 27

**Книга каже, дослівно:**

> Далі кожна плата прошивається однією командою з однією адресою:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-009 sha:7c27876f src:manual/21-seriyna.md:29 klas:A -->
### T-21-009 · kod · рядок 29

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

<!-- fc id:T-21-010 sha:060d1904 src:manual/21-seriyna.md:30 klas:A -->
### T-21-010 · kod-ryadok · рядок 30

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

<!-- fc id:T-21-011 sha:d76a9957 src:manual/21-seriyna.md:33 klas:F -->
### T-21-011 · proza · рядок 33

**Книга каже, дослівно:**

> Тепер операцію можна віддати людині, яка нічого не знає про адреси розділів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-012 sha:378d2fc5 src:manual/21-seriyna.md:37 klas:F -->
### T-21-012 · proza · рядок 37

**Книга каже, дослівно:**

> `--flash-mode`, `--flash-size` і `--flash-freq` у `merge-bin` мають збігатися з тим, під що зібрано прошивку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-013 sha:27deca81 src:manual/21-seriyna.md:37 klas:F -->
### T-21-013 · proza · рядок 37

**Книга каже, дослівно:**

> Розбіжність дає плату, яка прошилася без помилок і не стартує.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-014 sha:a6125283 src:manual/21-seriyna.md:37 klas:F -->
### T-21-014 · proza · рядок 37

**Книга каже, дослівно:**

> Найпростіше — узяти значення з `sdkconfig` проєкту, а не вгадувати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-015 sha:ac7a1ba1 src:manual/21-seriyna.md:45 klas:F -->
### T-21-015 · proza · рядок 45

**Книга каже, дослівно:**

> Ручна команда в терміналі не масштабується: помилку в ній видно не одразу і не завжди.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-016 sha:01a36707 src:manual/21-seriyna.md:45 klas:F -->
### T-21-016 · proza · рядок 45

**Книга каже, дослівно:**

> Мінімальний скрипт, який робить прошивку і **перевірку**:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-017 sha:41cc9c7f src:manual/21-seriyna.md:48 klas:A -->
### T-21-017 · kod · рядок 48

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

<!-- fc id:T-21-018 sha:23224667 src:manual/21-seriyna.md:54 klas:A -->
### T-21-018 · kod-ryadok · рядок 54

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

<!-- fc id:T-21-019 sha:1442de15 src:manual/21-seriyna.md:55 klas:F -->
### T-21-019 · kod-ryadok · рядок 55

**Книга каже, дослівно:**

> esptool --port "$PORT" verify-flash 0x0 "$IMAGE"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-020 sha:e7dfc363 src:manual/21-seriyna.md:56 klas:F -->
### T-21-020 · kod-ryadok · рядок 56

**Книга каже, дослівно:**

> esptool --port "$PORT" chip-id | grep -i "MAC:"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-021 sha:270a6061 src:manual/21-seriyna.md:60 klas:F -->
### T-21-021 · proza · рядок 60

**Книга каже, дослівно:**

> Три речі, які тут важливі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-022 sha:12bbf3c5 src:manual/21-seriyna.md:60 klas:F -->
### T-21-022 · proza · рядок 60

**Книга каже, дослівно:**

> `set -e` зупиняє скрипт на першій помилці — інакше збій прошивки лишиться непоміченим у потоці виводу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-023 sha:42368b26 src:manual/21-seriyna.md:60 klas:F -->
### T-21-023 · proza · рядок 60

**Книга каже, дослівно:**

> `verify-flash` перетворює «прошилося» на «у флеші лежить те, що треба».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-024 sha:16350670 src:manual/21-seriyna.md:60 klas:F -->
### T-21-024 · proza · рядок 60

**Книга каже, дослівно:**

> Виведений MAC іде в журнал: це єдиний надійний ідентифікатор плати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-025 sha:e3f39fae src:manual/21-seriyna.md:67 klas:F -->
### T-21-025 · proza · рядок 67

**Книга каже, дослівно:**

> «Прошилося без помилок» — не критерій приймання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-026 sha:d1d7cedd src:manual/21-seriyna.md:67 klas:F -->
### T-21-026 · proza · рядок 67

**Книга каже, дослівно:**

> Мінімальний контроль, який ловить майже все:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-027 sha:ddc59055 src:manual/21-seriyna.md:70 klas:F -->
### T-21-027 · proza · рядок 70

**Книга каже, дослівно:**

> **`verify-flash`** — вміст флешу відповідає образу. 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-028 sha:1d35be73 src:manual/21-seriyna.md:70 klas:F -->
### T-21-028 · proza · рядок 70

**Книга каже, дослівно:**

> **Скидання і читання boot-логу** — пристрій справді стартує (розділ 16). 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-029 sha:a414fea1 src:manual/21-seriyna.md:70 klas:F -->
### T-21-029 · proza · рядок 70

**Книга каже, дослівно:**

> **Одна функціональна перевірка** — те, заради чого виріб існує: світлодіод блимає, датчик читається, точка доступу піднялася.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-030 sha:c6467fae src:manual/21-seriyna.md:75 klas:F -->
### T-21-030 · proza · рядок 75

**Книга каже, дослівно:**

> Третій пункт ловить те, чого не спіймають перші два: справний образ, залитий на плату з непропаяним модулем або мертвим датчиком.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-031 sha:621d4059 src:manual/21-seriyna.md:79 klas:F -->
### T-21-031 · proza · рядок 79

**Книга каже, дослівно:**

> Партія — це саме те місце, де вилазить межове живлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-032 sha:14a2790e src:manual/21-seriyna.md:79 klas:F -->
### T-21-032 · proza · рядок 79

**Книга каже, дослівно:**

> Двадцять плат прошиваються по черзі, USB-хаб гріється, напруга просідає, і десь на чотирнадцятій починаються `MD5 does not match`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-033 sha:432b092c src:manual/21-seriyna.md:79 klas:F -->
### T-21-033 · proza · рядок 79

**Книга каже, дослівно:**

> Живлення для серійної прошивки — окреме, з запасом, і бажано не від ноутбука.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-034 sha:1a3a9559 src:manual/21-seriyna.md:87 klas:F -->
### T-21-034 · proza · рядок 87

**Книга каже, дослівно:**

> Найчастіша помилка серійного виробництва — залити двадцятьом платам однаковий образ разом із однаковим серійним номером, однаковим ключем і однаковим ім'ям пристрою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-035 sha:6c7e3e50 src:manual/21-seriyna.md:87 klas:F -->
### T-21-035 · proza · рядок 87

**Книга каже, дослівно:**

> Наслідки виявляються пізно, у полі, і виглядають як містика: два пристрої «крадуть» одне в одного з'єднання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-036 sha:3140d22c src:manual/21-seriyna.md:92 klas:F -->
### T-21-036 · proza · рядок 92

**Книга каже, дослівно:**

> Правильна схема розділяє два шари:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-037 sha:1cfc3ebd src:manual/21-seriyna.md:94 klas:F -->
### T-21-037 · proza · рядок 94

**Книга каже, дослівно:**

> **Спільне** — образ прошивки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-038 sha:ac0e1bb8 src:manual/21-seriyna.md:94 klas:F -->
### T-21-038 · proza · рядок 94

**Книга каже, дослівно:**

> Однаковий для всієї партії, з `merge-bin`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-039 sha:c50488dc src:manual/21-seriyna.md:96 klas:F -->
### T-21-039 · proza · рядок 96

**Книга каже, дослівно:**

> **Унікальне** — конфігурація в NVS.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-040 sha:5ee74ccf src:manual/21-seriyna.md:96 klas:F -->
### T-21-040 · proza · рядок 96

**Книга каже, дослівно:**

> Своя для кожної плати: серійний номер, ключі, калібрувальні коефіцієнти, ім'я.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-041 sha:8fbe10a5 src:manual/21-seriyna.md:99 klas:F -->
### T-21-041 · proza · рядок 99

**Книга каже, дослівно:**

> ESP-IDF дає інструмент, який робить із CSV готовий образ розділу NVS:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-042 sha:fc2721f0 src:manual/21-seriyna.md:101 klas:A -->
### T-21-042 · kod · рядок 101

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

<!-- fc id:T-21-043 sha:aa33e38e src:manual/21-seriyna.md:102 klas:F -->
### T-21-043 · kod-ryadok · рядок 102

**Книга каже, дослівно:**

> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-044 sha:dab0dee5 src:manual/21-seriyna.md:103 klas:A -->
### T-21-044 · kod-ryadok · рядок 103

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

<!-- fc id:T-21-045 sha:b0a670d8 src:manual/21-seriyna.md:106 klas:F -->
### T-21-045 · proza · рядок 106

**Книга каже, дослівно:**

> Адреса `0x9000` — початок розділу `nvs` у стандартній розбивці; звірити зі своєю таблицею розділів (розділ 18).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-046 sha:a441973a src:manual/21-seriyna.md:109 klas:F -->
### T-21-046 · proza · рядок 109

**Книга каже, дослівно:**

> Альтернатива для невеликих партій: заливати спільний образ, а унікальне записувати через консоль після першого старту — прошивка при першому запуску просить серійний номер і зберігає його в NVS.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-047 sha:168c664c src:manual/21-seriyna.md:109 klas:F -->
### T-21-047 · proza · рядок 109

**Книга каже, дослівно:**

> Менше інструментів, але додає ручну операцію до кожної плати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-048 sha:82ff65b0 src:manual/21-seriyna.md:115 klas:F -->
### T-21-048 · proza · рядок 115

**Книга каже, дослівно:**

> MAC-адреса кожного чипа унікальна від заводу і лежить в eFuse.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-049 sha:8aa5ff33 src:manual/21-seriyna.md:115 klas:F -->
### T-21-049 · proza · рядок 115

**Книга каже, дослівно:**

> Якщо все, що вам потрібно, — відрізняти пристрої один від одного, окремий серійний номер не потрібен: беріть MAC.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-050 sha:5aed5cc9 src:manual/21-seriyna.md:115 klas:F -->
### T-21-050 · proza · рядок 115

**Книга каже, дослівно:**

> Це прибирає цілий шар роботи разом із нагодою помилитися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-051 sha:7afef3b1 src:manual/21-seriyna.md:123 klas:F -->
### T-21-051 · proza · рядок 123

**Книга каже, дослівно:**

> Плата без позначки — плата, про яку через місяць невідомо нічого.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-052 sha:80b6708b src:manual/21-seriyna.md:123 klas:F -->
### T-21-052 · proza · рядок 123

**Книга каже, дослівно:**

> На кожну наклеюється або пишеться маркером мінімум:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-053 sha:581413be src:manual/21-seriyna.md:126 klas:F -->
### T-21-053 · proza · рядок 126

**Книга каже, дослівно:**

> - порядковий номер у партії; - версія прошивки; - дата.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-054 sha:b8ed94db src:manual/21-seriyna.md:130 klas:F -->
### T-21-054 · proza · рядок 130

**Книга каже, дослівно:**

> Наліпка клеїться на бік, який видно в зібраному виробі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-055 sha:d888373f src:manual/21-seriyna.md:130 klas:F -->
### T-21-055 · proza · рядок 130

**Книга каже, дослівно:**

> Наліпка, що опинилася всередині корпусу, не існує.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-056 sha:669ee36d src:manual/21-seriyna.md:135 klas:F -->
### T-21-056 · proza · рядок 135

**Книга каже, дослівно:**

> Один файл на партію, рядок на плату:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-057 sha:75def2ca src:manual/21-seriyna.md:137 klas:F -->
### T-21-057 · tablycya-shapka · рядок 137

**Книга каже, дослівно:**

> | № | MAC | Версія | Дата | Контроль | Примітка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-058 sha:e706eb63 src:manual/21-seriyna.md:138 klas:F -->
### T-21-058 · komirka · рядок 138

**Книга каже, дослівно:**

> 0041 · MAC → `A0:B7:…:14`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-059 sha:a8bb95c8 src:manual/21-seriyna.md:138 klas:F -->
### T-21-059 · komirka · рядок 138

**Книга каже, дослівно:**

> 0041 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-060 sha:e4e73586 src:manual/21-seriyna.md:138 klas:F -->
### T-21-060 · komirka · рядок 138

**Книга каже, дослівно:**

> 0041 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-061 sha:29d3900f src:manual/21-seriyna.md:138 klas:F -->
### T-21-061 · komirka · рядок 138

**Книга каже, дослівно:**

> 0041 · Контроль → OK

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-062 sha:75799caf src:manual/21-seriyna.md:139 klas:F -->
### T-21-062 · komirka · рядок 139

**Книга каже, дослівно:**

> 0042 · MAC → `A0:B7:…:2C`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-063 sha:abb9bd4b src:manual/21-seriyna.md:139 klas:F -->
### T-21-063 · komirka · рядок 139

**Книга каже, дослівно:**

> 0042 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-064 sha:e2d0d5e3 src:manual/21-seriyna.md:139 klas:F -->
### T-21-064 · komirka · рядок 139

**Книга каже, дослівно:**

> 0042 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-065 sha:f7d5d679 src:manual/21-seriyna.md:139 klas:F -->
### T-21-065 · komirka · рядок 139

**Книга каже, дослівно:**

> 0042 · Контроль → OK

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-066 sha:c5831a43 src:manual/21-seriyna.md:139 klas:F -->
### T-21-066 · komirka · рядок 139

**Книга каже, дослівно:**

> 0042 · Примітка → корпус подряпаний

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-067 sha:79ce9a1f src:manual/21-seriyna.md:140 klas:F -->
### T-21-067 · komirka · рядок 140

**Книга каже, дослівно:**

> 0043 · MAC → `A0:B7:…:31`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-068 sha:9f488b42 src:manual/21-seriyna.md:140 klas:F -->
### T-21-068 · komirka · рядок 140

**Книга каже, дослівно:**

> 0043 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-069 sha:a6590e77 src:manual/21-seriyna.md:140 klas:F -->
### T-21-069 · komirka · рядок 140

**Книга каже, дослівно:**

> 0043 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-070 sha:37c1710c src:manual/21-seriyna.md:140 klas:F -->
### T-21-070 · komirka · рядок 140

**Книга каже, дослівно:**

> 0043 · Контроль → **брак**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-071 sha:4688c6c2 src:manual/21-seriyna.md:140 klas:F -->
### T-21-071 · komirka · рядок 140

**Книга каже, дослівно:**

> 0043 · Примітка → не стартує, модуль

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-072 sha:ee027464 src:manual/21-seriyna.md:143 klas:F -->
### T-21-072 · proza · рядок 143

**Книга каже, дослівно:**

> Цей файл відповідає на питання, які виникають через півроку і не мають іншого джерела відповіді: скільки зроблено, яка версія у пристрою з таким MAC, чи був цей екземпляр у браку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-073 sha:f8360aa5 src:manual/21-seriyna.md:147 klas:F -->
### T-21-073 · proza · рядок 147

**Книга каже, дослівно:**

> Разом із журналом зберігаються **самі файли прошивки** тієї версії, що поїхала, і, обов'язково, `.elf` того самого збирання: без нього backtrace з поля не розшифрувати (картка [К7](#k-panika)).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-074 sha:2e3ee5bc src:manual/21-seriyna.md:152 klas:F -->
### T-21-074 · proza · рядок 152

**Книга каже, дослівно:**

> Версія прошивки, яка поїхала до замовника, має існувати в архіві як файли, а не як «гілка в git, з якої це збиралося».

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-075 sha:6b4d2e33 src:manual/21-seriyna.md:152 klas:F -->
### T-21-075 · proza · рядок 152

**Книга каже, дослівно:**

> Перезібрати «такий самий» образ пізніше майже ніколи не виходить точно: змінилася версія тулчейну, змінилася бібліотека, змінився шлях збирання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-076 sha:775f6652 src:manual/21-seriyna.md:152 klas:F -->
### T-21-076 · proza · рядок 152

**Книга каже, дослівно:**

> Адреси зсунуться, і `.elf` перестане відповідати тому, що в полі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-077 sha:f5a053c0 src:manual/21-seriyna.md:161 klas:F -->
### T-21-077 · proza · рядок 161

**Книга каже, дослівно:**

> Коли партія вимірюється сотнями, послідовна прошивка стає вузьким місцем.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-078 sha:c5052027 src:manual/21-seriyna.md:161 klas:F -->
### T-21-078 · proza · рядок 161

**Книга каже, дослівно:**

> Варіанти, у порядку складності:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-079 sha:7b5f5132 src:manual/21-seriyna.md:164 klas:F -->
### T-21-079 · proza · рядок 164

**Книга каже, дослівно:**

> **Кілька портів паралельно.** Скрипт запускається на `/dev/ttyUSB0`, `ttyUSB1`, `ttyUSB2` одночасно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-080 sha:03a8a283 src:manual/21-seriyna.md:164 klas:F -->
### T-21-080 · proza · рядок 164

**Книга каже, дослівно:**

> Найдешевший спосіб отримати кратне прискорення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-081 sha:73cabe58 src:manual/21-seriyna.md:164 klas:F -->
### T-21-081 · proza · рядок 164

**Книга каже, дослівно:**

> Обмеження — живлення хаба: чотири плати, що одночасно пишуть у флеш, дають помітний струм.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-082 sha:74a5c7c5 src:manual/21-seriyna.md:169 klas:F -->
### T-21-082 · proza · рядок 169

**Книга каже, дослівно:**

> **Flash Download Tool** (Windows) вміє кілька плат в одному вікні — зручно там, де прошиває оператор без командного рядка (розділ 17).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-083 sha:8bcfad00 src:manual/21-seriyna.md:172 klas:F -->
### T-21-083 · proza · рядок 172

**Книга каже, дослівно:**

> **Прошивка до монтажу**, на спеціальному ложементі з підпружиненими контактами (pogo pins).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-084 sha:eecd5522 src:manual/21-seriyna.md:172 klas:F -->
### T-21-084 · proza · рядок 172

**Книга каже, дослівно:**

> Це вже оснастка, і має сенс від сотень плат.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-085 sha:850d2dde src:manual/21-seriyna.md:177 klas:F -->
### T-21-085 · proza · рядок 177

**Книга каже, дослівно:**

> Відкласти плату, позначити, продовжити з рештою, розібратися потім — розділ 55 і картка [К8](#k-symptomy).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-086 sha:69e2ed79 src:manual/21-seriyna.md:177 klas:F -->
### T-21-086 · proza · рядок 177

**Книга каже, дослівно:**

> Найчастіші причини саме в партії: непропаяний модуль, замикання під час монтажу, плата іншої ревізії, що приїхала в тій самій коробці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-087 sha:39f098a2 src:manual/21-seriyna.md:184 klas:F -->
### T-21-087 · proza · рядок 184

**Книга каже, дослівно:**

> `merge-bin` — один файл, одна адреса, нема чого переплутати.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-088 sha:81a87405 src:manual/21-seriyna.md:186 klas:F -->
### T-21-088 · proza · рядок 186

**Книга каже, дослівно:**

> `verify-flash` і функціональна перевірка — обов'язкові кроки, а не опції.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-089 sha:26048fe4 src:manual/21-seriyna.md:188 klas:F -->
### T-21-089 · proza · рядок 188

**Книга каже, дослівно:**

> Спільний образ і унікальний NVS — це два різні шари.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-090 sha:ade9bd68 src:manual/21-seriyna.md:188 klas:F -->
### T-21-090 · proza · рядок 188

**Книга каже, дослівно:**

> Змішати їх означає отримати двадцять пристроїв з однаковою особистістю.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-091 sha:fd3cdf97 src:manual/21-seriyna.md:191 klas:F -->
### T-21-091 · proza · рядок 191

**Книга каже, дослівно:**

> Журнал партії і збережені файли прошивки разом із `.elf` — те, без чого через півроку неможливо відповісти на просте питання «що в цьому пристрої».

**Доказ**

- **Клас:** F — не звірено

---
