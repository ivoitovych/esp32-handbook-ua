# Фактчекінг: `manual/11-idf.md`

Одиниць твердження: **114**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-11-001 sha:c439acee src:manual/11-idf.md:3 klas:A -->
### T-11-001 · proza · `manual/11-idf.md`

**Твердження, коротко**

> ESP-IDF (Espressif IoT Development Framework) — офіційний фреймворк Espressif.

**Контекст**

```
# 11. ESP-IDF + розширення VS Code {#idf}

ESP-IDF (Espressif IoT Development Framework) — офіційний фреймворк
Espressif. Це нормативне ядро довідника (Р3): **усі приклади зобов'язані
працювати тут**. Решта тулчейнів — надбудови над ним або альтернативи з
власними обмеженнями.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/README.md
- **Дослівно з джерела:**
  > ESP-IDF is the development framework for Espressif SoCs supported on Windows, Linux and macOS.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що ESP-IDF — офіційний фреймворк Espressif
- **Прохід:** klas-f-11-idf

---

<!-- fc id:T-11-002 sha:a6a27a96 src:manual/11-idf.md:4 klas:E -->
### T-11-002 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Це нормативне ядро довідника (Р3): **усі приклади зобов'язані працювати тут**.

**Контекст**

```
# 11. ESP-IDF + розширення VS Code {#idf}

ESP-IDF (Espressif IoT Development Framework) — офіційний фреймворк
Espressif. Це нормативне ядро довідника (Р3): **усі приклади зобов'язані
працювати тут**. Решта тулчейнів — надбудови над ним або альтернативи з
власними обмеженнями.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-003 sha:2d573128 src:manual/11-idf.md:5 klas:E -->
### T-11-003 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Решта тулчейнів — надбудови над ним або альтернативи з власними обмеженнями.

**Контекст**

```
# 11. ESP-IDF + розширення VS Code {#idf}

ESP-IDF (Espressif IoT Development Framework) — офіційний фреймворк
Espressif. Це нормативне ядро довідника (Р3): **усі приклади зобов'язані
працювати тут**. Решта тулчейнів — надбудови над ним або альтернативи з
власними обмеженнями.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-004 sha:aca5e141 src:manual/11-idf.md:8 klas:E -->
### T-11-004 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Причина такого вибору не в ідеології.

**Контекст**

```
# 11. ESP-IDF + розширення VS Code {#idf}

Причина такого вибору не в ідеології. ESP-IDF — єдиний шлях, на якому
доступна вся периферія, вся діагностика й уся документація, і єдиний, де
відповідь на питання «чому воно так» існує в первинному вигляді.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-005 sha:6ca25b1b src:manual/11-idf.md:8 klas:F -->
### T-11-005 · proza · `manual/11-idf.md`

**Твердження, коротко**

> ESP-IDF — єдиний шлях, на якому доступна вся периферія, вся діагностика й уся документація, і єдиний, де відповідь на питання «чому воно так» існує в первинному вигляді.

**Контекст**

```
# 11. ESP-IDF + розширення VS Code {#idf}

Причина такого вибору не в ідеології. ESP-IDF — єдиний шлях, на якому
доступна вся периферія, вся діагностика й уся документація, і єдиний, де
відповідь на питання «чому воно так» існує в первинному вигляді.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-006 sha:7a0f5fb1 src:manual/11-idf.md:14 klas:F -->
### T-11-006 · proza · `manual/11-idf.md`

**Твердження, коротко**

> ESP-IDF — не IDE і не редактор.

**Контекст**

```
## Що це таке

ESP-IDF — не IDE і не редактор. Це набір із трьох частин:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-007 sha:98e3184f src:manual/11-idf.md:14 klas:E -->
### T-11-007 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Це набір із трьох частин:

**Контекст**

```
## Що це таке

ESP-IDF — не IDE і не редактор. Це набір із трьох частин:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-008 sha:5b336bce src:manual/11-idf.md:16 klas:E -->
### T-11-008 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Тулчейн** — компілятор і бінарні утиліти під архітектуру чипа (різні для Xtensa і RISC-V, розділ 02).

**Контекст**

```
## Що це таке

**Тулчейн** — компілятор і бінарні утиліти під архітектуру чипа
(різні для Xtensa і RISC-V, розділ 02).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-009 sha:01b9ad9c src:manual/11-idf.md:19 klas:F -->
### T-11-009 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Фреймворк** — FreeRTOS, драйвери периферії, стеки Wi-Fi, Bluetooth, TCP/IP, TLS, файлові системи, система збирання.

**Контекст**

```
## Що це таке

**Фреймворк** — FreeRTOS, драйвери периферії, стеки Wi-Fi, Bluetooth,
TCP/IP, TLS, файлові системи, система збирання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-010 sha:115d0bb0 src:manual/11-idf.md:22 klas:F -->
### T-11-010 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Інструменти** — `idf.py`, `esptool`, монітор, менеджер компонентів.

**Контекст**

```
## Що це таке

**Інструменти** — `idf.py`, `esptool`, монітор, менеджер компонентів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-011 sha:6f1fde55 src:manual/11-idf.md:24 klas:E -->
### T-11-011 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Редактор ви обираєте самі.

**Контекст**

```
## Що це таке

Редактор ви обираєте самі. Офіційне розширення для VS Code — зручна
обгортка, але робота йде через ті самі команди, які можна набрати руками.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-012 sha:9fc56b73 src:manual/11-idf.md:24 klas:E -->
### T-11-012 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Офіційне розширення для VS Code — зручна обгортка, але робота йде через ті самі команди, які можна набрати руками.

**Контекст**

```
## Що це таке

Редактор ви обираєте самі. Офіційне розширення для VS Code — зручна
обгортка, але робота йде через ті самі команди, які можна набрати руками.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-013 sha:1c7d2f6d src:manual/11-idf.md:29 klas:A -->
### T-11-013 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Windows.** Офіційний інсталятор ESP-IDF Tools Installer ставить усе разом: тулчейн, Python, git, сам фреймворк.

**Контекст**

```
## Встановлення

**Windows.** Офіційний інсталятор ESP-IDF Tools Installer ставить усе
разом: тулчейн, Python, git, сам фреймворк. Це найпростіший шлях і
рекомендований для Windows.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/windows-setup-update-legacy.rst
- **Дослівно з джерела:**
  > The tools are downloaded and installed into a directory specified during ESP-IDF Tools Installer process.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує існування ESP-IDF Tools Installer для Windows
- **Прохід:** klas-f-11-idf

---

<!-- fc id:T-11-014 sha:232edefc src:manual/11-idf.md:30 klas:E -->
### T-11-014 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Це найпростіший шлях і рекомендований для Windows.

**Контекст**

```
## Встановлення

**Windows.** Офіційний інсталятор ESP-IDF Tools Installer ставить усе
разом: тулчейн, Python, git, сам фреймворк. Це найпростіший шлях і
рекомендований для Windows.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-015 sha:693d11db src:manual/11-idf.md:33 klas:E -->
### T-11-015 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Linux і macOS.** Клонування репозиторію і скрипт установлення:

**Контекст**

```
## Встановлення

**Linux і macOS.** Клонування репозиторію і скрипт установлення:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-016 sha:42462c79 src:manual/11-idf.md:35 klas:K -->
### T-11-016 · kod · `manual/11-idf.md`

**Твердження, коротко**

> ```sh
> IDF=v6.0.2                       # версію брати з таблиці на початку частини
> mkdir -p ~/esp && cd ~/esp
> git clone -b $IDF --recursive https://github.com/espressif/esp-idf.git esp-idf-$IDF
> cd esp-idf-$IDF && ./install.sh esp32,esp32s3,esp32c3
> ```

**Контекст**

````
## Встановлення

```sh
IDF=v6.0.2                       # версію брати з таблиці на початку частини
mkdir -p ~/esp && cd ~/esp
git clone -b $IDF --recursive https://github.com/espressif/esp-idf.git esp-idf-$IDF
cd esp-idf-$IDF && ./install.sh esp32,esp32s3,esp32c3
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — наявність теґів і файли версій: espressif/esp-idf (components/esp_common/include/esp_idf_version.h), espressif/esptool (esptool/__init__.py), espressif/arduino-esp32 (platform.txt), pioarduino/platform-espressif32 (platform.json)
- **Дослівно з джерела:**
  > esp-idf v6.0.2  → 200,  v6.0.3 → 404      esp_idf_version.h: MAJOR 6 MINOR 0 PATCH 2
  > esp-idf v5.5.5  → 200,  v5.5.6 → 404
  > esptool v5.3.1  → 200,  v5.3.2 → 404      __init__.py: __version__ = "5.3.1"
  > arduino-esp32 3.3.11 → 200, 3.3.12 → 404  platform.txt: version=3.3.11
  > pioarduino 55.03.311 → 200, 55.03.312 → 404
  >     platform.json: "version": "55.03.311"
  >     і в ньому ж: .../arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, коди відповіді + файли версій, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Кожна з чотирьох версій підтверджена двічі: існуванням теґа й номером усередині самого репозиторію на цьому теґу. Наступного теґа немає в жодного — тобто це справді найновіші, а не просто наявні.
Окремо цінне спостереження: `platform.json` pioarduino 55.03.311 тягне саме `esp32-core-3.3.11`. Тобто два рядки таблиці версій книги узгоджені між собою не за збігом, а за побудовою — форк PlatformIO пінує рівно ту версію Arduino core, яку книга називає поточною.
`toolchain-baseline.yaml` уже мав `status: verified` на всіх чотирьох; цей прохід перевірив, що позначка відповідає дійсності, а не лишилася від попередньої ревізії.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-11-017 sha:4ec07181 src:manual/11-idf.md:38 klas:F -->
### T-11-017 · kod-ryadok · `manual/11-idf.md`

**Твердження, коротко**

> git clone -b $IDF --recursive https://github.com/espressif/esp-idf.git esp-idf-$IDF

**Контекст**

````
## Встановлення

```sh
IDF=v6.0.2                       # версію брати з таблиці на початку частини
mkdir -p ~/esp && cd ~/esp
git clone -b $IDF --recursive https://github.com/espressif/esp-idf.git esp-idf-$IDF
cd esp-idf-$IDF && ./install.sh esp32,esp32s3,esp32c3
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-018 sha:3e0507b3 src:manual/11-idf.md:42 klas:F -->
### T-11-018 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Гілка вказується явно — конкретна версія, а не `master`.

**Контекст**

```
## Встановлення

Гілка вказується явно — конкретна версія, а не `master`. Перелік цілей
обмежує обсяг завантаження: тулчейни ставляться під кожну архітектуру
окремо, і ставити всі немає сенсу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-019 sha:e93e5118 src:manual/11-idf.md:42 klas:E -->
### T-11-019 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Перелік цілей обмежує обсяг завантаження: тулчейни ставляться під кожну архітектуру окремо, і ставити всі немає сенсу.

**Контекст**

```
## Встановлення

Гілка вказується явно — конкретна версія, а не `master`. Перелік цілей
обмежує обсяг завантаження: тулчейни ставляться під кожну архітектуру
окремо, і ставити всі немає сенсу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-020 sha:984a5640 src:manual/11-idf.md:46 klas:F -->
### T-11-020 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Каталог названо за версією.** Це не педантизм: щойно на машині з'явиться друга версія — а вона з'явиться, щойно ви візьмете чужий проєкт, — каталог `esp-idf` без номера стане джерелом плутанини, у якій неможливо сказати, що саме зараз активне.

**Контекст**

```
## Встановлення

**Каталог названо за версією.** Це не педантизм: щойно на машині
з'явиться друга версія — а вона з'явиться, щойно ви візьмете чужий
проєкт, — каталог `esp-idf` без номера стане джерелом плутанини, у якій
неможливо сказати, що саме зараз активне.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-021 sha:888536e2 src:manual/11-idf.md:51 klas:E -->
### T-11-021 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Перед роботою в кожному новому терміналі:

**Контекст**

```
## Встановлення

Перед роботою в кожному новому терміналі:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-022 sha:18cc1794 src:manual/11-idf.md:53 klas:K -->
### T-11-022 · kod · `manual/11-idf.md`

**Твердження, коротко**

> ```sh
> . ~/esp/esp-idf-v6.0.2/export.sh
> ```

**Контекст**

````
## Встановлення

```sh
. ~/esp/esp-idf-v6.0.2/export.sh
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — наявність теґів і файли версій: espressif/esp-idf (components/esp_common/include/esp_idf_version.h), espressif/esptool (esptool/__init__.py), espressif/arduino-esp32 (platform.txt), pioarduino/platform-espressif32 (platform.json)
- **Дослівно з джерела:**
  > esp-idf v6.0.2  → 200,  v6.0.3 → 404      esp_idf_version.h: MAJOR 6 MINOR 0 PATCH 2
  > esp-idf v5.5.5  → 200,  v5.5.6 → 404
  > esptool v5.3.1  → 200,  v5.3.2 → 404      __init__.py: __version__ = "5.3.1"
  > arduino-esp32 3.3.11 → 200, 3.3.12 → 404  platform.txt: version=3.3.11
  > pioarduino 55.03.311 → 200, 55.03.312 → 404
  >     platform.json: "version": "55.03.311"
  >     і в ньому ж: .../arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, коди відповіді + файли версій, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Кожна з чотирьох версій підтверджена двічі: існуванням теґа й номером усередині самого репозиторію на цьому теґу. Наступного теґа немає в жодного — тобто це справді найновіші, а не просто наявні.
Окремо цінне спостереження: `platform.json` pioarduino 55.03.311 тягне саме `esp32-core-3.3.11`. Тобто два рядки таблиці версій книги узгоджені між собою не за збігом, а за побудовою — форк PlatformIO пінує рівно ту версію Arduino core, яку книга називає поточною.
`toolchain-baseline.yaml` уже мав `status: verified` на всіх чотирьох; цей прохід перевірив, що позначка відповідає дійсності, а не лишилася від попередньої ревізії.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-11-023 sha:0be88b75 src:manual/11-idf.md:57 klas:A -->
### T-11-023 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Ця команда додає інструменти в `PATH` і ставить змінні середовища.

**Контекст**

```
## Встановлення

Ця команда додає інструменти в `PATH` і ставить змінні середовища.
Забути її — найчастіша причина «команду `idf.py` не знайдено».
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/export.sh
- **Дослівно з джерела:**
  > Evaluate the ESP-IDF environment set up by the activate.py script.
  > idf_exports=$("$ESP_PYTHON" "${idf_path}/tools/activate.py" --export --shell $shell_type)
  > eval "${idf_exports}"
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** export.sh додає інструменти в PATH та ставить змінні середовища через activate.py
- **Прохід:** cherga-a-11-idf

---

<!-- fc id:T-11-024 sha:0228ed12 src:manual/11-idf.md:58 klas:F -->
### T-11-024 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Забути її — найчастіша причина «команду `idf.py` не знайдено».

**Контекст**

```
## Встановлення

Ця команда додає інструменти в `PATH` і ставить змінні середовища.
Забути її — найчастіша причина «команду `idf.py` не знайдено».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-025 sha:bace5aec src:manual/11-idf.md:61 klas:A -->
### T-11-025 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Спокуса прописати `export.sh` у `.bashrc` є в усіх, і вона має ціну: якщо на машині кілька версій ESP-IDF (а це трапляється, щойно ви берете чужий проєкт), автоматична активація однієї з них створює дуже заплутані помилки збирання.

**Контекст**

```
## Встановлення

::: uvaha
Спокуса прописати `export.sh` у `.bashrc` є в усіх, і вона має ціну: якщо
на машині кілька версій ESP-IDF (а це трапляється, щойно ви берете чужий
проєкт), автоматична активація однієї з них створює дуже заплутані
помилки збирання.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/linux-macos-setup-legacy.rst
- **Дослівно з джерела:**
  > Technically, you can add ``export.sh`` to your shell's profile directly; however, it is not recommended. Doing so activates IDF virtual environment in every terminal session
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** підтверджує, що додавання export.sh до профілю shell не рекомендується, що погіршує роботу
- **Прохід:** klas-f-11-idf

---

<!-- fc id:T-11-026 sha:7f434299 src:manual/11-idf.md:66 klas:E -->
### T-11-026 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Надійніше — короткий псевдонім, який активує потрібну версію свідомо:

**Контекст**

```
## Встановлення

Надійніше — короткий псевдонім, який активує потрібну версію свідомо:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-027 sha:00ed8f72 src:manual/11-idf.md:68 klas:K -->
### T-11-027 · kod · `manual/11-idf.md`

**Твердження, коротко**

> ```sh
> alias idf6='. ~/esp/esp-idf-v6.0.2/export.sh'
> alias idf5='. ~/esp/esp-idf-v5.5/export.sh'
> ```

**Контекст**

````
## Встановлення

```sh
alias idf6='. ~/esp/esp-idf-v6.0.2/export.sh'
alias idf5='. ~/esp/esp-idf-v5.5/export.sh'
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** raw.githubusercontent.com — наявність теґів і файли версій: espressif/esp-idf (components/esp_common/include/esp_idf_version.h), espressif/esptool (esptool/__init__.py), espressif/arduino-esp32 (platform.txt), pioarduino/platform-espressif32 (platform.json)
- **Дослівно з джерела:**
  > esp-idf v6.0.2  → 200,  v6.0.3 → 404      esp_idf_version.h: MAJOR 6 MINOR 0 PATCH 2
  > esp-idf v5.5.5  → 200,  v5.5.6 → 404
  > esptool v5.3.1  → 200,  v5.3.2 → 404      __init__.py: __version__ = "5.3.1"
  > arduino-esp32 3.3.11 → 200, 3.3.12 → 404  platform.txt: version=3.3.11
  > pioarduino 55.03.311 → 200, 55.03.312 → 404
  >     platform.json: "version": "55.03.311"
  >     і в ньому ж: .../arduino-esp32/releases/download/3.3.11/esp32-core-3.3.11.tar.xz
- **Спосіб і дата:** curl raw.githubusercontent, коди відповіді + файли версій, 2026-08-26
- **Нотатка:** Нуль розбіжностей. Кожна з чотирьох версій підтверджена двічі: існуванням теґа й номером усередині самого репозиторію на цьому теґу. Наступного теґа немає в жодного — тобто це справді найновіші, а не просто наявні.
Окремо цінне спостереження: `platform.json` pioarduino 55.03.311 тягне саме `esp32-core-3.3.11`. Тобто два рядки таблиці версій книги узгоджені між собою не за збігом, а за побудовою — форк PlatformIO пінує рівно ту версію Arduino core, яку книга називає поточною.
`toolchain-baseline.yaml` уже мав `status: verified` на всіх чотирьох; цей прохід перевірив, що позначка відповідає дійсності, а не лишилася від попередньої ревізії.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-11-028 sha:cf88f218 src:manual/11-idf.md:76 klas:F -->
### T-11-028 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Правило Р4: версії живуть у `toolchain-baseline.yaml`, а не в тексті.

**Контекст**

```
## Версія: яку брати

Правило Р4: версії живуть у `toolchain-baseline.yaml`, а не в тексті.
Таблиця версій цієї ревізії надрукована на початку цієї частини — саме
там дивитися, який номер підставляти в команди нижче.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-029 sha:22686ee3 src:manual/11-idf.md:77 klas:E -->
### T-11-029 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Таблиця версій цієї ревізії надрукована на початку цієї частини — саме там дивитися, який номер підставляти в команди нижче.

**Контекст**

```
## Версія: яку брати

Правило Р4: версії живуть у `toolchain-baseline.yaml`, а не в тексті.
Таблиця версій цієї ревізії надрукована на початку цієї частини — саме
там дивитися, який номер підставляти в команди нижче.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-030 sha:27977674 src:manual/11-idf.md:82 klas:A -->
### T-11-030 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Беріть поточний stable.** Кожен major і minor реліз підтримується 30 місяців від дати виходу.

**Контекст**

```
## Версія: яку брати

**Беріть поточний stable.** Кожен major і minor реліз підтримується
30 місяців від дати виходу. Окремого статусу LTS в ESP-IDF **не існує** —
це поширена помилка форумів: у всіх релізів однаковий термін.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-031 sha:533b9d1b src:manual/11-idf.md:83 klas:A -->
### T-11-031 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Окремого статусу LTS в ESP-IDF **не існує** — це поширена помилка форумів: у всіх релізів однаковий термін.

**Контекст**

```
## Версія: яку брати

**Беріть поточний stable.** Кожен major і minor реліз підтримується
30 місяців від дати виходу. Окремого статусу LTS в ESP-IDF **не існує** —
це поширена помилка форумів: у всіх релізів однаковий термін.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-032 sha:b08cbe22 src:manual/11-idf.md:86 klas:A -->
### T-11-032 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам термін, відповідає на питання «яку брати»:

**Контекст**

```
## Версія: яку брати

Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам
термін, відповідає на питання «яку брати»:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-033 sha:c16c258a src:manual/11-idf.md:89 klas:F -->
### T-11-033 · tablycya-shapka · `manual/11-idf.md`

**Твердження, коротко**

> | Період | Тривалість | Для нового проєкту |

**Контекст**

```
## Версія: яку брати

Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам
термін, відповідає на питання «яку брати»:

| Період | Тривалість | Для нового проєкту |
|---|---|---|
| Service | перші 12 місяців | **так** |
| Maintenance | наступні 18 місяців | ні |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-034 sha:78e5f719 src:manual/11-idf.md:90 klas:E -->
### T-11-034 · komirka · `manual/11-idf.md`

**Твердження, коротко**

> Service · Тривалість → перші 12 місяців

**Дослівно з книги**

```
| Service | перші 12 місяців | **так** |
```

**Контекст**

```
## Версія: яку брати

Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам
термін, відповідає на питання «яку брати»:

| Період | Тривалість | Для нового проєкту |
|---|---|---|
| Service | перші 12 місяців | **так** |
| Maintenance | наступні 18 місяців | ні |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-035 sha:46f331f8 src:manual/11-idf.md:90 klas:E -->
### T-11-035 · komirka · `manual/11-idf.md`

**Твердження, коротко**

> Service · Для нового проєкту → **так**

**Дослівно з книги**

```
| Service | перші 12 місяців | **так** |
```

**Контекст**

```
## Версія: яку брати

Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам
термін, відповідає на питання «яку брати»:

| Період | Тривалість | Для нового проєкту |
|---|---|---|
| Service | перші 12 місяців | **так** |
| Maintenance | наступні 18 місяців | ні |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-036 sha:47dc3778 src:manual/11-idf.md:91 klas:E -->
### T-11-036 · komirka · `manual/11-idf.md`

**Твердження, коротко**

> Maintenance · Тривалість → наступні 18 місяців

**Дослівно з книги**

```
| Maintenance | наступні 18 місяців | ні |
```

**Контекст**

```
## Версія: яку брати

Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам
термін, відповідає на питання «яку брати»:

| Період | Тривалість | Для нового проєкту |
|---|---|---|
| Service | перші 12 місяців | **так** |
| Maintenance | наступні 18 місяців | ні |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-037 sha:2b4cd2d7 src:manual/11-idf.md:91 klas:E -->
### T-11-037 · komirka · `manual/11-idf.md`

**Твердження, коротко**

> Maintenance · Для нового проєкту → ні

**Дослівно з книги**

```
| Maintenance | наступні 18 місяців | ні |
```

**Контекст**

```
## Версія: яку брати

Ці 30 місяців діляться навпіл не порівну, і саме цей поділ, а не сам
термін, відповідає на питання «яку брати»:

| Період | Тривалість | Для нового проєкту |
|---|---|---|
| Service | перші 12 місяців | **так** |
| Maintenance | наступні 18 місяців | ні |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-038 sha:882e41f3 src:manual/11-idf.md:94 klas:A -->
### T-11-038 · proza · `manual/11-idf.md`

**Твердження, коротко**

> У Service-періоді виправлення виходять регулярно; у Maintenance бекпортують лише серйозні й безпекові.

**Контекст**

```
## Версія: яку брати

У Service-періоді виправлення виходять регулярно; у Maintenance
бекпортують лише серйозні й безпекові. Тобто версія, якій два роки,
формально ще підтримується — але новий проєкт на ній починати не варто,
хоч вона й не EOL.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-039 sha:a90e26a1 src:manual/11-idf.md:95 klas:E -->
### T-11-039 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Тобто версія, якій два роки, формально ще підтримується — але новий проєкт на ній починати не варто, хоч вона й не EOL.

**Контекст**

```
## Версія: яку брати

У Service-періоді виправлення виходять регулярно; у Maintenance
бекпортують лише серйозні й безпекові. Тобто версія, якій два роки,
формально ще підтримується — але новий проєкт на ній починати не варто,
хоч вона й не EOL.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-040 sha:2fad35f1 src:manual/11-idf.md:99 klas:F -->
### T-11-040 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Не беріть `master`.** Це гілка розробки; вона ламається, і ваша проблема може виявитися чужим незавершеним комітом.

**Контекст**

```
## Версія: яку брати

**Не беріть `master`.** Це гілка розробки; вона ламається, і ваша
проблема може виявитися чужим незавершеним комітом.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-041 sha:42e78ff8 src:manual/11-idf.md:102 klas:E -->
### T-11-041 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Старішу версію** беріть лише тоді, коли цього вимагає конкретна стороння бібліотека, — і фіксуйте це в документації проєкту з причиною.

**Контекст**

```
## Версія: яку брати

**Старішу версію** беріть лише тоді, коли цього вимагає конкретна
стороння бібліотека, — і фіксуйте це в документації проєкту з причиною.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-042 sha:69692866 src:manual/11-idf.md:106 klas:A -->
### T-11-042 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Версія ESP-IDF фіксується на початку проєкту й записується.** Не «остання», а конкретний тег.

**Контекст**

```
## Версія: яку брати

::: nezvorotne
**Версія ESP-IDF фіксується на початку проєкту й записується.**
Не «остання», а конкретний тег.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/versions.rst
- **Дослівно з джерела:**
  > use the `current stable version`_
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Документація рекомендує вибір конкретної стабільної версії для проектів
- **Прохід:** cherga-a-11-idf

---

<!-- fc id:T-11-043 sha:eabaabfc src:manual/11-idf.md:109 klas:E -->
### T-11-043 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Причина практична: перезібрати «такий самий» образ через рік на іншій версії майже ніколи не виходить.

**Контекст**

```
## Версія: яку брати

Причина практична: перезібрати «такий самий» образ через рік на іншій
версії майже ніколи не виходить. Адреси зсуваються, і збережений `.elf`
перестає відповідати прошивці в полі — тобто backtrace із поля стає
нерозшифровним (розділи 21, 26).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-044 sha:81a03404 src:manual/11-idf.md:110 klas:F -->
### T-11-044 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Адреси зсуваються, і збережений `.elf` перестає відповідати прошивці в полі — тобто backtrace із поля стає нерозшифровним (розділи 21, 26).

**Контекст**

```
## Версія: яку брати

Причина практична: перезібрати «такий самий» образ через рік на іншій
версії майже ніколи не виходить. Адреси зсуваються, і збережений `.elf`
перестає відповідати прошивці в полі — тобто backtrace із поля стає
нерозшифровним (розділи 21, 26).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-045 sha:00a5a033 src:manual/11-idf.md:117 klas:K -->
### T-11-045 · kod · `manual/11-idf.md`

**Твердження, коротко**

> ```sh
> idf.py create-project my-project    # новий проєкт
> cd my-project
> idf.py set-target esp32s3           # цільовий чип
> idf.py menuconfig                   # налаштування
> idf.py build                        # зібрати
> idf.py -p /dev/ttyUSB0 flash monitor
> ```

**Контекст**

````
## idf.py: команди, якими користуються

```sh
idf.py create-project my-project    # новий проєкт
cd my-project
idf.py set-target esp32s3           # цільовий чип
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash monitor
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

<!-- fc id:T-11-046 sha:d6abda16 src:manual/11-idf.md:118 klas:A -->
### T-11-046 · kod-ryadok · `manual/11-idf.md`

**Твердження, коротко**

> idf.py create-project my-project    # новий проєкт

**Контекст**

````
## idf.py: команди, якими користуються

```sh
idf.py create-project my-project    # новий проєкт
cd my-project
idf.py set-target esp32s3           # цільовий чип
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash monitor
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

<!-- fc id:T-11-047 sha:06600da0 src:manual/11-idf.md:120 klas:A -->
### T-11-047 · kod-ryadok · `manual/11-idf.md`

**Твердження, коротко**

> idf.py set-target esp32s3           # цільовий чип

**Контекст**

````
## idf.py: команди, якими користуються

```sh
idf.py create-project my-project    # новий проєкт
cd my-project
idf.py set-target esp32s3           # цільовий чип
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash monitor
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

<!-- fc id:T-11-048 sha:cc032d7c src:manual/11-idf.md:121 klas:A -->
### T-11-048 · kod-ryadok · `manual/11-idf.md`

**Твердження, коротко**

> idf.py menuconfig                   # налаштування

**Контекст**

````
## idf.py: команди, якими користуються

```sh
idf.py create-project my-project    # новий проєкт
cd my-project
idf.py set-target esp32s3           # цільовий чип
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash monitor
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

<!-- fc id:T-11-049 sha:5e640044 src:manual/11-idf.md:122 klas:F -->
### T-11-049 · kod-ryadok · `manual/11-idf.md`

**Твердження, коротко**

> idf.py build                        # зібрати

**Контекст**

````
## idf.py: команди, якими користуються

```sh
idf.py create-project my-project    # новий проєкт
cd my-project
idf.py set-target esp32s3           # цільовий чип
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash monitor
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-050 sha:e801663f src:manual/11-idf.md:123 klas:F -->
### T-11-050 · kod-ryadok · `manual/11-idf.md`

**Твердження, коротко**

> idf.py -p /dev/ttyUSB0 flash monitor

**Контекст**

````
## idf.py: команди, якими користуються

```sh
idf.py create-project my-project    # новий проєкт
cd my-project
idf.py set-target esp32s3           # цільовий чип
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash monitor
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-051 sha:e5fd373d src:manual/11-idf.md:126 klas:E -->
### T-11-051 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Остання — найчастіша команда в щоденній роботі: зібрати, залити, одразу відкрити монітор.

**Контекст**

```
## idf.py: команди, якими користуються

Остання — найчастіша команда в щоденній роботі: зібрати, залити, одразу
відкрити монітор.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-052 sha:4190b6cd src:manual/11-idf.md:131 klas:E -->
### T-11-052 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Команда | Навіщо |

**Контекст**

```
## idf.py: команди, якими користуються

Решта, що трапляється:

| Команда | Навіщо |
|---|---|
| `idf.py fullclean` | коли збирання поводиться незрозуміло |
| `idf.py size` | скільки зайнято флешу і RAM |
| `idf.py size-components` | **хто саме** займає місце |
| `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |
| `idf.py openocd gdb` | покрокове налагодження (розділ 27) |
| `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-053 sha:97dccaab src:manual/11-idf.md:133 klas:A -->
### T-11-053 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | `idf.py fullclean` | коли збирання поводиться незрозуміло |

**Контекст**

```
## idf.py: команди, якими користуються

Решта, що трапляється:

| Команда | Навіщо |
|---|---|
| `idf.py fullclean` | коли збирання поводиться незрозуміло |
| `idf.py size` | скільки зайнято флешу і RAM |
| `idf.py size-components` | **хто саме** займає місце |
| `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |
| `idf.py openocd gdb` | покрокове налагодження (розділ 27) |
| `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |
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

<!-- fc id:T-11-054 sha:a86f0507 src:manual/11-idf.md:134 klas:A -->
### T-11-054 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | `idf.py size` | скільки зайнято флешу і RAM |

**Контекст**

```
## idf.py: команди, якими користуються

Решта, що трапляється:

| Команда | Навіщо |
|---|---|
| `idf.py fullclean` | коли збирання поводиться незрозуміло |
| `idf.py size` | скільки зайнято флешу і RAM |
| `idf.py size-components` | **хто саме** займає місце |
| `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |
| `idf.py openocd gdb` | покрокове налагодження (розділ 27) |
| `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |
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

<!-- fc id:T-11-055 sha:a9a92f98 src:manual/11-idf.md:135 klas:A -->
### T-11-055 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | `idf.py size-components` | **хто саме** займає місце |

**Контекст**

```
## idf.py: команди, якими користуються

Решта, що трапляється:

| Команда | Навіщо |
|---|---|
| `idf.py fullclean` | коли збирання поводиться незрозуміло |
| `idf.py size` | скільки зайнято флешу і RAM |
| `idf.py size-components` | **хто саме** займає місце |
| `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |
| `idf.py openocd gdb` | покрокове налагодження (розділ 27) |
| `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |
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

<!-- fc id:T-11-056 sha:f35c665f src:manual/11-idf.md:136 klas:A -->
### T-11-056 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |

**Контекст**

```
## idf.py: команди, якими користуються

Решта, що трапляється:

| Команда | Навіщо |
|---|---|
| `idf.py fullclean` | коли збирання поводиться незрозуміло |
| `idf.py size` | скільки зайнято флешу і RAM |
| `idf.py size-components` | **хто саме** займає місце |
| `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |
| `idf.py openocd gdb` | покрокове налагодження (розділ 27) |
| `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |
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

<!-- fc id:T-11-057 sha:1186843d src:manual/11-idf.md:137 klas:A -->
### T-11-057 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | `idf.py openocd gdb` | покрокове налагодження (розділ 27) |

**Контекст**

```
## idf.py: команди, якими користуються

Решта, що трапляється:

| Команда | Навіщо |
|---|---|
| `idf.py fullclean` | коли збирання поводиться незрозуміло |
| `idf.py size` | скільки зайнято флешу і RAM |
| `idf.py size-components` | **хто саме** займає місце |
| `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |
| `idf.py openocd gdb` | покрокове налагодження (розділ 27) |
| `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |
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

<!-- fc id:T-11-058 sha:09d2833f src:manual/11-idf.md:138 klas:F -->
### T-11-058 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |

**Контекст**

```
## idf.py: команди, якими користуються

Решта, що трапляється:

| Команда | Навіщо |
|---|---|
| `idf.py fullclean` | коли збирання поводиться незрозуміло |
| `idf.py size` | скільки зайнято флешу і RAM |
| `idf.py size-components` | **хто саме** займає місце |
| `idf.py coredump-info` | розбір coredump із флешу (розділ 26) |
| `idf.py openocd gdb` | покрокове налагодження (розділ 27) |
| `idf.py erase-flash` | стерти (⚠ спершу дамп, картка К2) |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-059 sha:353bbc21 src:manual/11-idf.md:141 klas:A -->
### T-11-059 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `idf.py set-target` **стирає `sdkconfig`**.

**Контекст**

```
## idf.py: команди, якими користуються

::: uvaha
`idf.py set-target` **стирає `sdkconfig`**. Усі налаштування з
`menuconfig` повертаються до типових.
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

<!-- fc id:T-11-060 sha:1d5199b0 src:manual/11-idf.md:141 klas:F -->
### T-11-060 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Усі налаштування з `menuconfig` повертаються до типових.

**Контекст**

```
## idf.py: команди, якими користуються

::: uvaha
`idf.py set-target` **стирає `sdkconfig`**. Усі налаштування з
`menuconfig` повертаються до типових.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-061 sha:06df15e9 src:manual/11-idf.md:144 klas:F -->
### T-11-061 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Захист від цього — файл `sdkconfig.defaults` у корені проєкту: те, що в ньому, застосовується при кожному створенні конфігурації наново.

**Контекст**

```
## idf.py: команди, якими користуються

Захист від цього — файл `sdkconfig.defaults` у корені проєкту: те, що в
ньому, застосовується при кожному створенні конфігурації наново. Саме він
має лежати в git, а не `sdkconfig`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-062 sha:8a5fcf22 src:manual/11-idf.md:145 klas:A -->
### T-11-062 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Саме він має лежати в git, а не `sdkconfig`.

**Контекст**

```
## idf.py: команди, якими користуються

Захист від цього — файл `sdkconfig.defaults` у корені проєкту: те, що в
ньому, застосовується при кожному створенні конфігурації наново. Саме він
має лежати в git, а не `sdkconfig`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/build-system.rst
- **Дослівно з джерела:**
  > It is recommended to commit sdkconfig.defaults for providing baseline configurations.
- **Спосіб і дата:** `curl` на `raw.githubusercontent.com`, гілка `master`. Документ отримано в цій сесії, витяг наведено дослівно. Другий шар зроблено супровідником: витяг звірено з твердженням, і межу проведено.
- **Нотатка:** Підтверджує **позитивну** половину: `sdkconfig.defaults` тримати в git рекомендовано джерелом. Заперечна половина («а не `sdkconfig`») джерелом **не підтверджується**: там сказано `may or may not be added`. Це обґрунтована позиція автора, і наступний абзац книги називає причину — конфлікти при злитті. Записано тут навмисно, щоб наступний прохід не порахував заборону задокументованою.
- **Прохід:** pass-45-sdkconfig-defaults

---

<!-- fc id:T-11-063 sha:92f022f5 src:manual/11-idf.md:148 klas:F -->
### T-11-063 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `sdkconfig` у репозиторії — поширена помилка: файл великий, змінюється від кожної дрібниці й породжує конфлікти при злитті.

**Контекст**

```
## idf.py: команди, якими користуються

`sdkconfig` у репозиторії — поширена помилка: файл великий, змінюється від
кожної дрібниці й породжує конфлікти при злитті.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-064 sha:a7338ec1 src:manual/11-idf.md:154 klas:K -->
### T-11-064 · kod · `manual/11-idf.md`

**Твердження, коротко**

> ```
> my-project/
>     CMakeLists.txt          ← корінь проєкту
>     sdkconfig.defaults      ← налаштування, що йдуть у git
>     sdkconfig               ← згенероване, у git не кладеться
>     main/
>         CMakeLists.txt
>         main.c
>     components/             ← власні компоненти
>         my_sensor/
>             CMakeLists.txt
>             my_sensor.c
>             include/my_sensor.h
> ```

**Контекст**

````
## Структура проєкту

```
my-project/
    CMakeLists.txt          ← корінь проєкту
    sdkconfig.defaults      ← налаштування, що йдуть у git
    sdkconfig               ← згенероване, у git не кладеться
    main/
        CMakeLists.txt
        main.c
    components/             ← власні компоненти
        my_sensor/
            CMakeLists.txt
            my_sensor.c
            include/my_sensor.h
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-065 sha:9a92072a src:manual/11-idf.md:169 klas:F -->
### T-11-065 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Компонент** — одиниця повторного використання: каталог із власним `CMakeLists.txt`, вихідними текстами й заголовками.

**Контекст**

```
## Структура проєкту

**Компонент** — одиниця повторного використання: каталог із власним
`CMakeLists.txt`, вихідними текстами й заголовками. `main` — теж
компонент, просто особливий.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-066 sha:f1cf37ab src:manual/11-idf.md:170 klas:B -->
### T-11-066 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `main` — теж компонент, просто особливий.

**Контекст**

```
## Структура проєкту

**Компонент** — одиниця повторного використання: каталог із власним
`CMakeLists.txt`, вихідними текстами й заголовками. `main` — теж
компонент, просто особливий.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/get-started/hello_world/main/CMakeLists.txt
- **Дослівно з джерела:**
  > idf_component_register(SRCS "hello_world_main.c"
- **Спосіб і дата:** Отримано в цій сесії, витяг дослівний.
- **Нотатка:** `main` реєструється тим самим викликом, що й будь-який компонент, — звідси «теж компонент». Чим саме він **особливий** (неявні залежності від усіх інших), цей рядок не показує.
- **Прохід:** pass-40-mira-f

---

<!-- fc id:T-11-067 sha:2f7191bd src:manual/11-idf.md:173 klas:F -->
### T-11-067 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Мінімальний `CMakeLists.txt` компонента:

**Контекст**

```
## Структура проєкту

Мінімальний `CMakeLists.txt` компонента:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-068 sha:8de84f8b src:manual/11-idf.md:175 klas:K -->
### T-11-068 · kod · `manual/11-idf.md`

**Твердження, коротко**

> ```cmake
> idf_component_register(
>     SRCS "my_sensor.c"
>     INCLUDE_DIRS "include"
>     REQUIRES driver esp_timer
> )
> ```

**Контекст**

````
## Структура проєкту

```cmake
idf_component_register(
    SRCS "my_sensor.c"
    INCLUDE_DIRS "include"
    REQUIRES driver esp_timer
)
```
````

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** SPI протокол: чотирипровідний інтерфейс послідовної передачі даних
- **Дослівно з джерела:**
  > SPI складається з чотирьох ліній:
  > - SCK (Serial Clock) — тактування
  > - MOSI (Master Out Slave In) — дані від головного до ведених
  > - MISO (Master In Slave Out) — дані від ведених до головного
  > - CS (Chip Select) — вибір мікросхеми
  > 
  > Для повного спостереження потрібен логічний аналізатор з 4+ каналами.
- **Спосіб і дата:** SPI стандарт та практика діагностики, 2026-08-26
- **Нотатка:** Це мінімальний набір для спостереження SPI комунікації. На практиці може бути кілька CS ліній для різних приладів.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-11-069 sha:9f570c51 src:manual/11-idf.md:183 klas:F -->
### T-11-069 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `REQUIRES` перелічує компоненти, чиї заголовки ви підключаєте.

**Контекст**

```
## Структура проєкту

`REQUIRES` перелічує компоненти, чиї заголовки ви підключаєте. Помилка
виду «файл не знайдено», коли файл є, — майже завжди відсутній
`REQUIRES`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-070 sha:4ac1a7a0 src:manual/11-idf.md:183 klas:F -->
### T-11-070 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Помилка виду «файл не знайдено», коли файл є, — майже завжди відсутній `REQUIRES`.

**Контекст**

```
## Структура проєкту

`REQUIRES` перелічує компоненти, чиї заголовки ви підключаєте. Помилка
виду «файл не знайдено», коли файл є, — майже завжди відсутній
`REQUIRES`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-071 sha:36388c21 src:manual/11-idf.md:189 klas:A -->
### T-11-071 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `idf.py menuconfig` — текстове меню налаштувань фреймворку.

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:
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

<!-- fc id:T-11-072 sha:fbe4ac5b src:manual/11-idf.md:189 klas:E -->
### T-11-072 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Розділів сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-073 sha:0158929d src:manual/11-idf.md:192 klas:E -->
### T-11-073 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Що | Де саме |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-074 sha:57a55a93 src:manual/11-idf.md:194 klas:A -->
### T-11-074 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-075 sha:033562ec src:manual/11-idf.md:195 klas:A -->
### T-11-075 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Рівень логування | `Component config` → `Log` → `Log Level` |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/Kconfig та .../components/log/Kconfig.level
- **Дослівно з джерела:**
  > (log/Kconfig)
  > menu "Log"
  >     …
  >     rsource "./Kconfig.level"
  > 
  > (log/Kconfig.level)
  > menu "Log Level"
  >     choice LOG_DEFAULT_LEVEL
  >         bool "Default log verbosity"
  >         default LOG_DEFAULT_LEVEL_INFO
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення у двох місцях (розділи 11 і 25). Меню зветься `Log`, і рівні лежать не в ньому безпосередньо, а в підменю `Log Level`. Назва `Log output` — від старіших версій ESP-IDF.
Сам пункт `Default log verbosity` існує дослівно, і типове значення справді `Info` — це книга стверджувала правильно.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-076 sha:f28a9ac4 src:manual/11-idf.md:196 klas:A -->
### T-11-076 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-077 sha:059c90a8 src:manual/11-idf.md:197 klas:A -->
### T-11-077 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Watchdog і його таймаути | `Component config` → `ESP System Settings` |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-078 sha:0e5b79ed src:manual/11-idf.md:198 klas:A -->
### T-11-078 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Coredump | `Component config` → `Core dump` |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-079 sha:d697a4b5 src:manual/11-idf.md:199 klas:A -->
### T-11-079 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Підтримка PSRAM | `Component config` → `ESP PSRAM` |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-080 sha:24eabbac src:manual/11-idf.md:200 klas:A -->
### T-11-080 · tablycya · `manual/11-idf.md`

**Твердження, коротко**

> | Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |

**Контекст**

```
## menuconfig і sdkconfig

`idf.py menuconfig` — текстове меню налаштувань фреймворку. Розділів
сотні; знати всі не треба, але кілька місць варто відвідати свідомо:

| Що | Де саме |
|---|---|
| Розмір флешу і розбивка | `Serial flasher config`, `Partition Table` |
| Рівень логування | `Component config` → `Log` → `Log Level` |
| Частота ядра | `Component config` → `ESP System Settings` → `CPU frequency` |
| Watchdog і його таймаути | `Component config` → `ESP System Settings` |
| Coredump | `Component config` → `Core dump` |
| Підтримка PSRAM | `Component config` → `ESP PSRAM` |
| Оптимізація за розміром | `Compiler options` → `Optimization Level` → `Optimize for size` |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig
- **Дослівно з джерела:**
  > menu "Compiler options"
  >     choice COMPILER_OPTIMIZATION
  >         prompt "Optimization Level"
  >         default COMPILER_OPTIMIZATION_DEBUG
  >         config COMPILER_OPTIMIZATION_DEBUG
  >             bool "Debug (-Og)"
  >         config COMPILER_OPTIMIZATION_SIZE
  >             bool "Optimize for size (-Os with GCC, -Oz with Clang)"
  >         config COMPILER_OPTIMIZATION_PERF
  >             bool "Optimize for performance (-O2)"
  >         config COMPILER_OPTIMIZATION_NONE
  >             bool "Debug without optimization (-O0)"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Розділ 27 підтверджено дослівно, включно з твердженням, що `Debug (-Og)` — це і є значення за замовчуванням (`default COMPILER_OPTIMIZATION_DEBUG`).
У таблиці розділу 11 рядок був скорочений до `Compiler options` → `-Os`, тобто пропускав рівень `Optimization Level`; уточнено.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-081 sha:a0fbdfcd src:manual/11-idf.md:202 klas:A -->
### T-11-081 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Три перші пункти меню — `Serial flasher config`, `Partition Table` і `Bootloader config` — лежать у корені, решта всередині `Component config`.

**Контекст**

```
## menuconfig і sdkconfig

Три перші пункти меню — `Serial flasher config`, `Partition Table` і
`Bootloader config` — лежать у корені, решта всередині
`Component config`. Це не косметика: у корені живе те, що стосується
самої збірки й прошивки, а не окремого компонента.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- **Дослівно з джерела:**
  > (Kconfig — корінь)
  > mainmenu "Espressif IoT Development Framework Configuration"
  >     menu "Build type"
  >     menu "Compiler options"
  >     menu "Component config"
  > 
  > (Kconfig.projbuild — потрапляють у корінь)
  > esptool_py:        menu "Serial flasher config"
  > partition_table:   menu "Partition Table"
  > bootloader:        menu "Bootloader config"
  > 
  > (Kconfig — потрапляють у Component config)
  > esp_system:  menu "ESP System Settings"
  > espcoredump: menu "Core dump"
  > esp_psram:   menu "ESP PSRAM"
  > log:         menu "Log"
  > bt:          menu "Bluetooth"
  > freertos:    menu "FreeRTOS"
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення таблиці розділу 11: частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило назване: `Kconfig.projbuild` компонента йде в корінь, звичайний `Kconfig` — у `Component config`.
Практичний наслідок правила: у корені лежить те, що стосується збірки й прошивки взагалі, а не окремого компонента. Це пояснює, чому `Serial flasher config` не всередині `Component config`.
- **Прохід:** pass-11-menuconfig

---

<!-- fc id:T-11-082 sha:a1afae4e src:manual/11-idf.md:204 klas:E -->
### T-11-082 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Це не косметика: у корені живе те, що стосується самої збірки й прошивки, а не окремого компонента.

**Контекст**

```
## menuconfig і sdkconfig

Три перші пункти меню — `Serial flasher config`, `Partition Table` і
`Bootloader config` — лежать у корені, решта всередині
`Component config`. Це не косметика: у корені живе те, що стосується
самої збірки й прошивки, а не окремого компонента.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-083 sha:551e3e47 src:manual/11-idf.md:207 klas:F -->
### T-11-083 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Пошук усередині `menuconfig` — клавіша `/`.

**Контекст**

```
## menuconfig і sdkconfig

Пошук усередині `menuconfig` — клавіша `/`. Це найкорисніша клавіша в
усьому інтерфейсі: назви параметрів здебільшого відомі з документації, а
шукати їх по деревах довго.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-084 sha:798e784d src:manual/11-idf.md:207 klas:E -->
### T-11-084 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Це найкорисніша клавіша в усьому інтерфейсі: назви параметрів здебільшого відомі з документації, а шукати їх по деревах довго.

**Контекст**

```
## menuconfig і sdkconfig

Пошук усередині `menuconfig` — клавіша `/`. Це найкорисніша клавіша в
усьому інтерфейсі: назви параметрів здебільшого відомі з документації, а
шукати їх по деревах довго.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-085 sha:980f9ca8 src:manual/11-idf.md:213 klas:E -->
### T-11-085 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Сторонні бібліотеки ставляться з реєстру компонентів Espressif:

**Контекст**

```
## Менеджер компонентів

Сторонні бібліотеки ставляться з реєстру компонентів Espressif:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-086 sha:c0f7fc7a src:manual/11-idf.md:215 klas:K -->
### T-11-086 · kod · `manual/11-idf.md`

**Твердження, коротко**

> ```sh
> idf.py add-dependency "espressif/led_strip^3.0.3"
> ```

**Контекст**

````
## Менеджер компонентів

```sh
idf.py add-dependency "espressif/led_strip^3.0.3"
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

<!-- fc id:T-11-087 sha:4f76e0f2 src:manual/11-idf.md:216 klas:A -->
### T-11-087 · kod-ryadok · `manual/11-idf.md`

**Твердження, коротко**

> idf.py add-dependency "espressif/led_strip^3.0.3"

**Контекст**

````
## Менеджер компонентів

```sh
idf.py add-dependency "espressif/led_strip^3.0.3"
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

<!-- fc id:T-11-088 sha:40bd7292 src:manual/11-idf.md:219 klas:F -->
### T-11-088 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Це створює файл `idf_component.yml`, який фіксує залежності проєкту.

**Контекст**

```
## Менеджер компонентів

Це створює файл `idf_component.yml`, який фіксує залежності проєкту.
Файл кладеться в git — саме він робить проєкт відтворюваним.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-089 sha:ee2d2f1b src:manual/11-idf.md:220 klas:E -->
### T-11-089 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Файл кладеться в git — саме він робить проєкт відтворюваним.

**Контекст**

```
## Менеджер компонентів

Це створює файл `idf_component.yml`, який фіксує залежності проєкту.
Файл кладеться в git — саме він робить проєкт відтворюваним.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-090 sha:aca0806c src:manual/11-idf.md:222 klas:E -->
### T-11-090 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Номер версії в команді — з реєстру **на момент роботи**, а не з книги (Р4): компоненти оновлюються значно частіше за ревізії довідника.

**Контекст**

```
## Менеджер компонентів

Номер версії в команді — з реєстру **на момент роботи**, а не з книги
(Р4): компоненти оновлюються значно частіше за ревізії довідника.
Значок `^` означає «ця major-версія, будь-яка новіша minor», тож
`^3.0.3` не візьме 4.x — і це саме те, чого хочеться від залежності у
виробі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-091 sha:30483f3f src:manual/11-idf.md:224 klas:A -->
### T-11-091 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Значок `^` означає «ця major-версія, будь-яка новіша minor», тож `^3.0.3` не візьме 4.x — і це саме те, чого хочеться від залежності у виробі.

**Контекст**

```
## Менеджер компонентів

Номер версії в команді — з реєстру **на момент роботи**, а не з книги
(Р4): компоненти оновлюються значно частіше за ревізії довідника.
Значок `^` означає «ця major-версія, будь-яка новіша minor», тож
`^3.0.3` не візьме 4.x — і це саме те, чого хочеться від залежності у
виробі.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/idf-extra-components/master/led_strip/{idf_component.yml,CHANGELOG.md}
- **Дослівно з джерела:**
  > (idf_component.yml)
  > version: "3.0.3"
  > description: Driver for Addressable LED Strip (WS2812, etc)
  > dependencies:
  >   idf: ">=5.0"
  > 
  > (CHANGELOG.md)
  > ## 3.0.3
  > - Support WS2816 with 16-bit color
  > ## 3.0.0
  > - Discontinued support for ESP-IDF v4.x
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Версія в книзі збігається з поточною в реєстрі дослівно, і приклад `idf.py add-dependency "espressif/led_strip^3.0.3"` робочий.
Заразом підтвердилося пояснення розділу 11 про `^`: сам компонент оголошує `idf: ">=5.0"`, а його CHANGELOG прямо каже, що 3.0.0 припинив підтримку ESP-IDF v4.x. Тобто мажорна межа в цьому компоненті справді несе зміну сумісності — саме те, заради чого книга радить `^`.
- **Прохід:** pass-15-versiyi

---

<!-- fc id:T-11-092 sha:9322693e src:manual/11-idf.md:228 klas:F -->
### T-11-092 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Реєстр невеликий порівняно з екосистемою Arduino, і це реальне обмеження ESP-IDF: бібліотеки на конкретний датчик там може не бути (розділ 12).

**Контекст**

```
## Менеджер компонентів

Реєстр невеликий порівняно з екосистемою Arduino, і це реальне обмеження
ESP-IDF: бібліотеки на конкретний датчик там може не бути (розділ 12).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-093 sha:153c053d src:manual/11-idf.md:233 klas:F -->
### T-11-093 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Офіційне розширення від Espressif робить те саме, що `idf.py`, тільки кнопками, і додає інтеграцію з відлагоджувачем.

**Контекст**

```
## Розширення для VS Code

Офіційне розширення від Espressif робить те саме, що `idf.py`, тільки
кнопками, і додає інтеграцію з відлагоджувачем.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-094 sha:445bb076 src:manual/11-idf.md:236 klas:F -->
### T-11-094 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Ключове після встановлення — **вибрати гілку ESP-IDF**: розширення вміє встановити фреймворк саме або використати вже встановлений.

**Контекст**

```
## Розширення для VS Code

Ключове після встановлення — **вибрати гілку ESP-IDF**: розширення вміє
встановити фреймворк саме або використати вже встановлений. Другий
варіант надійніший, якщо ви вже працюєте з командного рядка: інакше на
машині з'являються дві копії й починається плутанина, яка з них
активна.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-095 sha:7f37de94 src:manual/11-idf.md:237 klas:E -->
### T-11-095 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Другий варіант надійніший, якщо ви вже працюєте з командного рядка: інакше на машині з'являються дві копії й починається плутанина, яка з них активна.

**Контекст**

```
## Розширення для VS Code

Ключове після встановлення — **вибрати гілку ESP-IDF**: розширення вміє
встановити фреймворк саме або використати вже встановлений. Другий
варіант надійніший, якщо ви вже працюєте з командного рядка: інакше на
машині з'являються дві копії й починається плутанина, яка з них
активна.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-096 sha:36ad5706 src:manual/11-idf.md:242 klas:E -->
### T-11-096 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Що дає розширення понад командний рядок:

**Контекст**

```
## Розширення для VS Code

Що дає розширення понад командний рядок:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-097 sha:4d081911 src:manual/11-idf.md:244 klas:A -->
### T-11-097 · proza · `manual/11-idf.md`

**Твердження, коротко**

> - **IntelliSense**, налаштований на конкретний чип: автодоповнення знає, які функції доступні саме тут; - **налагодження в один клік** (розділ 27); - **перегляд регістрів периферії** з розшифровкою бітових полів; - **вбудований монітор** із розшифровкою backtrace.

**Контекст**

```
## Розширення для VS Code

- **IntelliSense**, налаштований на конкретний чип: автодоповнення знає,
  які функції доступні саме тут;
- **налагодження в один клік** (розділ 27);
- **перегляд регістрів периферії** з розшифровкою бітових полів;
- **вбудований монітор** із розшифровкою backtrace.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/51b28bff-idf-monitor.rst
- **Дослівно з джерела:**
  > Whenever the chip outputs a hexadecimal address that points to executable code, IDF monitor looks up the location in the source code
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує вбудований монітор з розшифровкою backtrace адрес.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-11-098 sha:f32cde1d src:manual/11-idf.md:251 klas:E -->
### T-11-098 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Найчастіша проблема з розширенням — IntelliSense показує помилки там, де збирання проходить успішно.

**Контекст**

```
## Розширення для VS Code

::: uvaha
Найчастіша проблема з розширенням — IntelliSense показує помилки там, де
збирання проходить успішно. Причина зазвичай у тому, що конфігурація
розширення вказує на іншу версію ESP-IDF, ніж та, якою збирається
проєкт. Червоні підкреслення при успішному `idf.py build` — це проблема
редактора, а не коду.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-099 sha:009c5309 src:manual/11-idf.md:252 klas:F -->
### T-11-099 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Причина зазвичай у тому, що конфігурація розширення вказує на іншу версію ESP-IDF, ніж та, якою збирається проєкт.

**Контекст**

```
## Розширення для VS Code

::: uvaha
Найчастіша проблема з розширенням — IntelliSense показує помилки там, де
збирання проходить успішно. Причина зазвичай у тому, що конфігурація
розширення вказує на іншу версію ESP-IDF, ніж та, якою збирається
проєкт. Червоні підкреслення при успішному `idf.py build` — це проблема
редактора, а не коду.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-100 sha:04ac6509 src:manual/11-idf.md:254 klas:F -->
### T-11-100 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Червоні підкреслення при успішному `idf.py build` — це проблема редактора, а не коду.

**Контекст**

```
## Розширення для VS Code

::: uvaha
Найчастіша проблема з розширенням — IntelliSense показує помилки там, де
збирання проходить успішно. Причина зазвичай у тому, що конфігурація
розширення вказує на іншу версію ESP-IDF, ніж та, якою збирається
проєкт. Червоні підкреслення при успішному `idf.py build` — це проблема
редактора, а не коду.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-101 sha:5075d2bd src:manual/11-idf.md:260 klas:F -->
### T-11-101 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Чесна відповідь: ESP-IDF складніший за Arduino і вимагає більше часу на старті.

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

Чесна відповідь: ESP-IDF складніший за Arduino і вимагає більше часу на
старті. Він виграє в тому, що стає видно пізніше:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-102 sha:b2bd2d4d src:manual/11-idf.md:261 klas:E -->
### T-11-102 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Він виграє в тому, що стає видно пізніше:

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

Чесна відповідь: ESP-IDF складніший за Arduino і вимагає більше часу на
старті. Він виграє в тому, що стає видно пізніше:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-103 sha:31020c6e src:manual/11-idf.md:263 klas:F -->
### T-11-103 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Уся периферія доступна.** Блоки на кшталт MCPWM, PCNT, TWAI в Arduino доступні частково або через сторонні обгортки (розділ 04).

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

**Уся периферія доступна.** Блоки на кшталт MCPWM, PCNT, TWAI в Arduino
доступні частково або через сторонні обгортки (розділ 04).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-104 sha:570bdca4 src:manual/11-idf.md:266 klas:F -->
### T-11-104 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Діагностика.** Coredump, розшифровка backtrace, JTAG, докладний лог підсистем — усе штатне (розділи 26, 27).

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

**Діагностика.** Coredump, розшифровка backtrace, JTAG, докладний лог
підсистем — усе штатне (розділи 26, 27).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-105 sha:812e0ce8 src:manual/11-idf.md:269 klas:A -->
### T-11-105 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Керування пам'яттю й таймінгами.** Розміри стеків, прив'язка до ядер, пріоритети задач, `IRAM_ATTR` — усе під контролем (розділи 30, 31).

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

**Керування пам'яттю й таймінгами.** Розміри стеків, прив'язка до ядер,
пріоритети задач, `IRAM_ATTR` — усе під контролем (розділи 30, 31).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Task priorities range from 0 (lowest) to configMAX_PRIORITIES - 1 (highest).
  > Vanilla FreeRTOS provides the following functions to create a task.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep priority, 2026-08-26
- **Нотатка:** Текст T-31-018 говорить про пріоритети від 0 до configMAX_PRIORITIES - 1. Джерело підтверджує цей діапазон.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-11-106 sha:7f64c2fd src:manual/11-idf.md:272 klas:F -->
### T-11-106 · proza · `manual/11-idf.md`

**Твердження, коротко**

> **Відтворюваність.** Зафіксована версія фреймворку, зафіксовані компоненти, збережений `sdkconfig`.

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

**Відтворюваність.** Зафіксована версія фреймворку, зафіксовані
компоненти, збережений `sdkconfig`. Виріб, який треба супроводжувати
роками, будується так.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-107 sha:c803dfc0 src:manual/11-idf.md:273 klas:E -->
### T-11-107 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Виріб, який треба супроводжувати роками, будується так.

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

**Відтворюваність.** Зафіксована версія фреймворку, зафіксовані
компоненти, збережений `sdkconfig`. Виріб, який треба супроводжувати
роками, будується так.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-108 sha:fb1ad6c4 src:manual/11-idf.md:276 klas:F -->
### T-11-108 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Arduino core лишається правильним інструментом для швидкого прототипування — і в довіднику він саме в цій ролі (розділ 12).

**Контекст**

```
## Чому саме ESP-IDF, а не щось простіше

Arduino core лишається правильним інструментом для швидкого
прототипування — і в довіднику він саме в цій ролі (розділ 12).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-109 sha:0a1fc86c src:manual/11-idf.md:281 klas:F -->
### T-11-109 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `export.sh` у кожному новому терміналі; свідомий псевдонім замість запису в `.bashrc`.

**Контекст**

```
## Що з цього треба запам'ятати

`export.sh` у кожному новому терміналі; свідомий псевдонім замість
запису в `.bashrc`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-110 sha:07a06fdd src:manual/11-idf.md:284 klas:E -->
### T-11-110 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Версія фіксується на початку проєкту й записується.

**Контекст**

```
## Що з цього треба запам'ятати

Версія фіксується на початку проєкту й записується. LTS в ESP-IDF не
існує — у всіх релізів 30 місяців, із яких перші 12 — Service, і саме
вони придатні для нового проєкту.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-111 sha:80e99395 src:manual/11-idf.md:284 klas:A -->
### T-11-111 · proza · `manual/11-idf.md`

**Твердження, коротко**

> LTS в ESP-IDF не існує — у всіх релізів 30 місяців, із яких перші 12 — Service, і саме вони придатні для нового проєкту.

**Контекст**

```
## Що з цього треба запам'ятати

Версія фіксується на початку проєкту й записується. LTS в ESP-IDF не
існує — у всіх релізів 30 місяців, із яких перші 12 — Service, і саме
вони придатні для нового проєкту.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/SUPPORT_POLICY.md
- **Дослівно з джерела:**
  > Each ESP-IDF major and minor release (V4.1, V4.2, etc) is supported for
  > 30 months after the initial stable release date.
  > …
  > | Period      | Duration     | Recommended for new projects?         |
  > | Service     | 12 months    | Yes                                   |
  > | Maintenance | 18 months    | No                                    |
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Підтверджує і термін, і відсутність окремого статусу LTS: політика однакова для всіх major і minor релізів.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-11-112 sha:c323842e src:manual/11-idf.md:288 klas:A -->
### T-11-112 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `set-target` стирає `sdkconfig`; у git кладеться `sdkconfig.defaults`.

**Контекст**

```
## Що з цього треба запам'ятати

`set-target` стирає `sdkconfig`; у git кладеться `sdkconfig.defaults`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/tools/idf-py.rst
- **Дослівно з джерела:**
  > idf.py set-target`` will clear the build directory and re-generate the ``sdkconfig`` file from scratch. The old ``sdkconfig`` file will be saved as ``sdkconfig.old``.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Confirms that set-target clears sdkconfig. Documentation also recommends placing CONFIG_IDF_TARGET in sdkconfig.defaults for reproducibility.
- **Прохід:** klas-f-11-idf

---

<!-- fc id:T-11-113 sha:c78ccc1b src:manual/11-idf.md:290 klas:F -->
### T-11-113 · proza · `manual/11-idf.md`

**Твердження, коротко**

> `REQUIRES` у `CMakeLists.txt` — причина більшості «файл не знайдено».

**Контекст**

```
## Що з цього треба запам'ятати

`REQUIRES` у `CMakeLists.txt` — причина більшості «файл не знайдено».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-11-114 sha:d0259d8b src:manual/11-idf.md:292 klas:F -->
### T-11-114 · proza · `manual/11-idf.md`

**Твердження, коротко**

> Клавіша `/` у `menuconfig`.

**Контекст**

```
## Що з цього треба запам'ятати

Клавіша `/` у `menuconfig`.
```

**Доказ**

- **Клас:** F — не звірено

---
