# Фактчекінг: `kartky/k15-seriyna.md`

Одиниць твердження: **47**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K15-001 sha:c84dcf0a src:kartky/k15-seriyna.md:3 klas:F -->
### T-K15-001 · proza · рядок 3

**Книга каже, дослівно:**

> Прошити партію так, щоб через півроку можна було відповісти, що в кожному пристрої.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-002 sha:1c127630 src:kartky/k15-seriyna.md:8 klas:F -->
### T-K15-002 · proza · рядок 8

**Книга каже, дослівно:**

> - [ ] Зібрано **один образ** через `merge-bin` — одна команда, одна адреса, нема чого переплутати (без проєкту — К10) - [ ] `--flash-mode`, `--flash-size`, `--flash-freq` збігаються з `sdkconfig` проєкту - [ ] Образ перевірено на одній платі повністю: прошивка → boot-лог → функціональний тест - [ ] Збережено: `.bin`, **`.elf` того самого збирання**, `sdkconfig`, версія ESP-IDF, версії компонентів - [ ] Заведено журнал партії - [ ] Живлення для прошивки — окреме, з запасом, не від ноутбука

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-003 sha:f21b91a9 src:kartky/k15-seriyna.md:19 klas:K -->
### T-K15-003 · kod · рядок 19

**Книга каже, дослівно:**

> ```
> idf.py merge-bin -o vyrib-v1.4.bin      # адреси — з конфігурації проєкту
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

<!-- fc id:T-K15-004 sha:a7e17db1 src:kartky/k15-seriyna.md:20 klas:A -->
### T-K15-004 · kod-ryadok · рядок 20

**Книга каже, дослівно:**

> idf.py merge-bin -o vyrib-v1.4.bin      # адреси — з конфігурації проєкту

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

<!-- fc id:T-K15-005 sha:8511d99d src:kartky/k15-seriyna.md:25 klas:F -->
### T-K15-005 · tablycya-shapka · рядок 25

**Книга каже, дослівно:**

> | ☐ | Крок | Чим |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-006 sha:4fb5c876 src:kartky/k15-seriyna.md:26 klas:F -->
### T-K15-006 · komirka · рядок 26

**Книга каже, дослівно:**

> ☐ · Крок → 1. Прошити

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-007 sha:996855d9 src:kartky/k15-seriyna.md:26 klas:A -->
### T-K15-007 · komirka · рядок 26

**Книга каже, дослівно:**

> ☐ · Чим → `write-flash -z 0x0 vyrib-v1.4.bin`

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

<!-- fc id:T-K15-008 sha:b6338e2f src:kartky/k15-seriyna.md:27 klas:F -->
### T-K15-008 · komirka · рядок 27

**Книга каже, дослівно:**

> ☐ · Крок → 2. **Звірити**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-009 sha:8c04de3d src:kartky/k15-seriyna.md:27 klas:A -->
### T-K15-009 · komirka · рядок 27

**Книга каже, дослівно:**

> ☐ · Чим → `verify-flash 0x0 vyrib-v1.4.bin`

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

<!-- fc id:T-K15-010 sha:f91fb570 src:kartky/k15-seriyna.md:28 klas:F -->
### T-K15-010 · komirka · рядок 28

**Книга каже, дослівно:**

> ☐ · Крок → 3. Записати унікальне

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-011 sha:faca8f2d src:kartky/k15-seriyna.md:28 klas:F -->
### T-K15-011 · komirka · рядок 28

**Книга каже, дослівно:**

> ☐ · Чим → NVS: номер, ключі, калібрування

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-012 sha:d7deee82 src:kartky/k15-seriyna.md:29 klas:F -->
### T-K15-012 · komirka · рядок 29

**Книга каже, дослівно:**

> ☐ · Крок → 4. Зняти MAC

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-013 sha:27735e3c src:kartky/k15-seriyna.md:29 klas:F -->
### T-K15-013 · komirka · рядок 29

**Книга каже, дослівно:**

> ☐ · Чим → єдиний надійний ідентифікатор плати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-014 sha:fa0d7841 src:kartky/k15-seriyna.md:30 klas:F -->
### T-K15-014 · komirka · рядок 30

**Книга каже, дослівно:**

> ☐ · Крок → 5. **Прочитати boot-лог**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-015 sha:c289cc01 src:kartky/k15-seriyna.md:30 klas:F -->
### T-K15-015 · komirka · рядок 30

**Книга каже, дослівно:**

> ☐ · Чим → пристрій справді стартує

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-016 sha:935c8ea3 src:kartky/k15-seriyna.md:31 klas:F -->
### T-K15-016 · komirka · рядок 31

**Книга каже, дослівно:**

> ☐ · Крок → 6. **Функціональна перевірка**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-017 sha:1455628b src:kartky/k15-seriyna.md:31 klas:F -->
### T-K15-017 · komirka · рядок 31

**Книга каже, дослівно:**

> ☐ · Чим → те, заради чого виріб існує

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-018 sha:324b565a src:kartky/k15-seriyna.md:32 klas:F -->
### T-K15-018 · komirka · рядок 32

**Книга каже, дослівно:**

> ☐ · Крок → 7. Маркувати

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-019 sha:4253d18a src:kartky/k15-seriyna.md:32 klas:F -->
### T-K15-019 · komirka · рядок 32

**Книга каже, дослівно:**

> ☐ · Чим → номер, версія, дата — на видний бік

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-020 sha:b24d7bca src:kartky/k15-seriyna.md:33 klas:F -->
### T-K15-020 · komirka · рядок 33

**Книга каже, дослівно:**

> ☐ · Крок → 8. Записати рядок у журнал

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-021 sha:cf346d2a src:kartky/k15-seriyna.md:36 klas:F -->
### T-K15-021 · proza · рядок 36

**Книга каже, дослівно:**

> Кроки 2, 5 і 6 — обов'язкові, не опції.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-022 sha:ea9b0c14 src:kartky/k15-seriyna.md:36 klas:F -->
### T-K15-022 · proza · рядок 36

**Книга каже, дослівно:**

> «Прошилося без помилок» ловить не все: крок 6 виявляє справний образ на платі з непропаяним модулем.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-023 sha:75def2ca src:kartky/k15-seriyna.md:41 klas:F -->
### T-K15-023 · tablycya-shapka · рядок 41

**Книга каже, дослівно:**

> | № | MAC | Версія | Дата | Контроль | Примітка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-024 sha:e706eb63 src:kartky/k15-seriyna.md:42 klas:F -->
### T-K15-024 · komirka · рядок 42

**Книга каже, дослівно:**

> 0041 · MAC → `A0:B7:…:14`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-025 sha:a8bb95c8 src:kartky/k15-seriyna.md:42 klas:F -->
### T-K15-025 · komirka · рядок 42

**Книга каже, дослівно:**

> 0041 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-026 sha:e4e73586 src:kartky/k15-seriyna.md:42 klas:F -->
### T-K15-026 · komirka · рядок 42

**Книга каже, дослівно:**

> 0041 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-027 sha:29d3900f src:kartky/k15-seriyna.md:42 klas:F -->
### T-K15-027 · komirka · рядок 42

**Книга каже, дослівно:**

> 0041 · Контроль → OK

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-028 sha:79ce9a1f src:kartky/k15-seriyna.md:43 klas:F -->
### T-K15-028 · komirka · рядок 43

**Книга каже, дослівно:**

> 0043 · MAC → `A0:B7:…:31`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-029 sha:9f488b42 src:kartky/k15-seriyna.md:43 klas:F -->
### T-K15-029 · komirka · рядок 43

**Книга каже, дослівно:**

> 0043 · Версія → v1.4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-030 sha:a6590e77 src:kartky/k15-seriyna.md:43 klas:F -->
### T-K15-030 · komirka · рядок 43

**Книга каже, дослівно:**

> 0043 · Дата → 2026-08-26

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-031 sha:37c1710c src:kartky/k15-seriyna.md:43 klas:F -->
### T-K15-031 · komirka · рядок 43

**Книга каже, дослівно:**

> 0043 · Контроль → **брак**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-032 sha:0554d11b src:kartky/k15-seriyna.md:43 klas:F -->
### T-K15-032 · komirka · рядок 43

**Книга каже, дослівно:**

> 0043 · Примітка → не стартує

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-033 sha:2fd35e3c src:kartky/k15-seriyna.md:49 klas:F -->
### T-K15-033 · proza · рядок 49

**Книга каже, дослівно:**

> **Спільний образ ≠ спільна конфігурація.**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-034 sha:9149b7e4 src:kartky/k15-seriyna.md:51 klas:F -->
### T-K15-034 · proza · рядок 51

**Книга каже, дослівно:**

> Залити двадцятьом платам однаковий NVS означає двадцять пристроїв з однаковою особистістю: однаковий серійний номер, однакові ключі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-035 sha:8ae34cb3 src:kartky/k15-seriyna.md:51 klas:F -->
### T-K15-035 · proza · рядок 51

**Книга каже, дослівно:**

> Виявиться це пізно, у полі, і виглядатиме як містика — два пристрої «крадуть» з'єднання одне в одного.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-036 sha:49dd7b20 src:kartky/k15-seriyna.md:56 klas:F -->
### T-K15-036 · proza · рядок 56

**Книга каже, дослівно:**

> Один ключ на всі також означає, що захоплення одного компрометує всі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-037 sha:60d02320 src:kartky/k15-seriyna.md:58 klas:F -->
### T-K15-037 · proza · рядок 58

**Книга каже, дослівно:**

> Якщо треба лише відрізняти пристрої — **беріть MAC**: він унікальний від заводу і не потребує нічого.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-038 sha:51bbff59 src:kartky/k15-seriyna.md:62 klas:K -->
### T-K15-038 · kod · рядок 62

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

<!-- fc id:T-K15-039 sha:aa33e38e src:kartky/k15-seriyna.md:63 klas:F -->
### T-K15-039 · kod-ryadok · рядок 63

**Книга каже, дослівно:**

> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-040 sha:8fc5b038 src:kartky/k15-seriyna.md:64 klas:A -->
### T-K15-040 · kod-ryadok · рядок 64

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

<!-- fc id:T-K15-041 sha:306c0a40 src:kartky/k15-seriyna.md:69 klas:F -->
### T-K15-041 · proza · рядок 69

**Книга каже, дослівно:**

> **Не зупиняти партію.** Відкласти, позначити, продовжити з рештою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-042 sha:f7220973 src:kartky/k15-seriyna.md:71 klas:F -->
### T-K15-042 · proza · рядок 71

**Книга каже, дослівно:**

> Найчастіші причини саме в партії: непропаяний модуль, замикання при монтажі, плата іншої ревізії в тій самій коробці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-043 sha:28cc3b5c src:kartky/k15-seriyna.md:76 klas:F -->
### T-K15-043 · proza · рядок 76

**Книга каже, дослівно:**

> Кілька портів паралельно, оснастка з pogo pins, ведення журналу і відновлення після браку — розділ 21.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-044 sha:db835ae1 src:kartky/k15-seriyna.md:76 klas:F -->
### T-K15-044 · proza · рядок 76

**Книга каже, дослівно:**

> Тут лише те, що робиться руками над кожною платою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-045 sha:d94b9526 src:kartky/k15-seriyna.md:80 klas:F -->
### T-K15-045 · proza · рядок 80

**Книга каже, дослівно:**

> Дві дрібниці, що економлять найбільше: скрипт із `set -e` (інакше збій губиться в потоці виводу) і звертання до порту через `/dev/serial/by-id/`, а не `ttyUSB0` — номери плутаються після кожного перевтикання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-046 sha:8082acae src:kartky/k15-seriyna.md:88 klas:F -->
### T-K15-046 · proza · рядок 88

**Книга каже, дослівно:**

> - `erase-flash` — тільки після дампа (картка К2) - `espefuse burn-*` — не запускати, доки не зрозуміло дослівно, що робить кожен аргумент - Flash Encryption і Secure Boot у release — незворотні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K15-047 sha:a5422053 src:kartky/k15-seriyna.md:88 klas:F -->
### T-K15-047 · proza · рядок 88

**Книга каже, дослівно:**

> На партію — лише після випробування на платі, яку не шкода

**Доказ**

- **Клас:** F — не звірено

---
