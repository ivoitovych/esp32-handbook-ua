# Фактчекінг: `kartky/k07-panika.md`

Одиниць твердження: **37**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-K07-001 sha:b2a29f58 src:kartky/k07-panika.md:3 klas:F -->
### T-K07-001 · kod · рядок 3

**Книга каже, дослівно:**

> ```
> Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.
> Core 0 register dump:
> PC      : 0x400d1234  PS      : 0x00060730  A0      : 0x800d5678
> ...
> Backtrace: 0x400d1234:0x3ffb1f30 0x400d5678:0x3ffb1f50
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-002 sha:e4f265e4 src:kartky/k07-panika.md:11 klas:F -->
### T-K07-002 · proza · рядок 11

**Книга каже, дослівно:**

> Це звіт про те, де саме програма померла.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-003 sha:398c272f src:kartky/k07-panika.md:15 klas:F -->
### T-K07-003 · tablycya-shapka · рядок 15

**Книга каже, дослівно:**

> | Причина | Що сталося | Куди дивитися |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-004 sha:43e6233d src:kartky/k07-panika.md:16 klas:F -->
### T-K07-004 · komirka · рядок 16

**Книга каже, дослівно:**

> `LoadProhibited` · Що сталося → читання за недійсною адресою

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-005 sha:c9684ba0 src:kartky/k07-panika.md:16 klas:F -->
### T-K07-005 · komirka · рядок 16

**Книга каже, дослівно:**

> `LoadProhibited` · Куди дивитися → покажчик `NULL` або звільнений

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-006 sha:17665be2 src:kartky/k07-panika.md:17 klas:F -->
### T-K07-006 · komirka · рядок 17

**Книга каже, дослівно:**

> `StoreProhibited` · Що сталося → запис за недійсною адресою

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-007 sha:79b748d0 src:kartky/k07-panika.md:17 klas:F -->
### T-K07-007 · komirka · рядок 17

**Книга каже, дослівно:**

> `StoreProhibited` · Куди дивитися → те саме, але на запис

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-008 sha:81fd026c src:kartky/k07-panika.md:18 klas:F -->
### T-K07-008 · komirka · рядок 18

**Книга каже, дослівно:**

> `InstrFetchProhibited` · Що сталося → перехід на недійсну адресу

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-009 sha:a365c033 src:kartky/k07-panika.md:18 klas:F -->
### T-K07-009 · komirka · рядок 18

**Книга каже, дослівно:**

> `InstrFetchProhibited` · Куди дивитися → зіпсований покажчик на функцію

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-010 sha:a2d38223 src:kartky/k07-panika.md:19 klas:F -->
### T-K07-010 · komirka · рядок 19

**Книга каже, дослівно:**

> `IllegalInstruction` · Що сталося → виконання не-коду

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-011 sha:5208283b src:kartky/k07-panika.md:19 klas:F -->
### T-K07-011 · komirka · рядок 19

**Книга каже, дослівно:**

> `IllegalInstruction` · Куди дивитися → пошкоджений стек, переповнення

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-012 sha:3df94a10 src:kartky/k07-panika.md:20 klas:F -->
### T-K07-012 · komirka · рядок 20

**Книга каже, дослівно:**

> `LoadStoreAlignment` · Що сталося → невирівняний доступ

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-013 sha:1d31178b src:kartky/k07-panika.md:20 klas:F -->
### T-K07-013 · komirka · рядок 20

**Книга каже, дослівно:**

> `LoadStoreAlignment` · Куди дивитися → читання 32 біт з непарної адреси

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-014 sha:23917c21 src:kartky/k07-panika.md:21 klas:F -->
### T-K07-014 · komirka · рядок 21

**Книга каже, дослівно:**

> `Interrupt wdt timeout` · Що сталося → ISR або critical section триває задовго

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-015 sha:58d7dba4 src:kartky/k07-panika.md:21 klas:F -->
### T-K07-015 · komirka · рядок 21

**Книга каже, дослівно:**

> `Interrupt wdt timeout` · Куди дивитися → код у перериванні

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-016 sha:8c383197 src:kartky/k07-panika.md:24 klas:F -->
### T-K07-016 · proza · рядок 24

**Книга каже, дослівно:**

> `Task watchdog got triggered` — **не паніка**: це окреме повідомлення, і система при ньому лишається живою.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-017 sha:e501e2ce src:kartky/k07-panika.md:24 klas:F -->
### T-K07-017 · proza · рядок 24

**Книга каже, дослівно:**

> Воно саме називає винуватця в рядку `Tasks currently running`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-018 sha:28db66bc src:kartky/k07-panika.md:24 klas:A -->
### T-K07-018 · proza · рядок 24

**Книга каже, дослівно:**

> Причина майже завжди — цикл без `vTaskDelay`.

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/FreeRTOS-Kernel/include/freertos/{task,queue,semphr,event_groups,timers}.h та components/esp_common/include/esp_attr.h
- **Дослівно з джерела:**
  > Усі 15 викликів FreeRTOS, що вживає книга, знайдено в заголовках ядра.
  > Макроси:
  >   #define IRAM_ATTR _SECTION_ATTR_IMPL(".iram1", __COUNTER__)
  >   #define RTC_DATA_ATTR _SECTION_ATTR_IMPL(".rtc.data", __COUNTER__)
  >   #define configMAX_PRIORITIES ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** `RTC_DATA_ATTR` кладе змінну в секцію `.rtc.data` — це і є механічне підтвердження того, чому вона переживає deep sleep, тоді як звичайна змінна не переживає. `IRAM_ATTR` кладе функцію в `.iram1`, звідки вона виконується при вимкненому кеші флешу.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-K07-019 sha:7474c60a src:kartky/k07-panika.md:28 klas:F -->
### T-K07-019 · proza · рядок 28

**Книга каже, дослівно:**

> Найчастіші дві — `LoadProhibited` і `StoreProhibited`, і обидві майже завжди означають одне: **розіменування покажчика, який не той, що ви думаєте**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-020 sha:9ad1110b src:kartky/k07-panika.md:28 klas:F -->
### T-K07-020 · proza · рядок 28

**Книга каже, дослівно:**

> Найчастіше — результат `malloc`, який не перевірили.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-021 sha:db4c2e3d src:kartky/k07-panika.md:34 klas:F -->
### T-K07-021 · proza · рядок 34

**Книга каже, дослівно:**

> Backtrace — це ланцюжок адрес.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-022 sha:ce22291b src:kartky/k07-panika.md:34 klas:F -->
### T-K07-022 · proza · рядок 34

**Книга каже, дослівно:**

> Сам по собі він нечитний; його треба перекласти в назви функцій і номери рядків.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-023 sha:e0cf8dca src:kartky/k07-panika.md:34 klas:F -->
### T-K07-023 · proza · рядок 34

**Книга каже, дослівно:**

> `idf.py monitor` робить це автоматично, якщо запущений з каталогу того самого проєкту.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-024 sha:1346d34d src:kartky/k07-panika.md:38 klas:F -->
### T-K07-024 · proza · рядок 38

**Книга каже, дослівно:**

> Вручну, коли лог знято з чужого пристрою і є `.elf`:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-025 sha:4490d7ba src:kartky/k07-panika.md:40 klas:F -->
### T-K07-025 · kod · рядок 40

**Книга каже, дослівно:**

> ```
> xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf 0x400d1234 0x400d5678
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-026 sha:5f267d8c src:kartky/k07-panika.md:41 klas:F -->
### T-K07-026 · kod-ryadok · рядок 41

**Книга каже, дослівно:**

> xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf 0x400d1234 0x400d5678

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-027 sha:e408ef53 src:kartky/k07-panika.md:44 klas:F -->
### T-K07-027 · proza · рядок 44

**Книга каже, дослівно:**

> Інструмент **свій для кожної архітектури**: [[S3]] — `xtensa-esp32s3-elf-addr2line`, [[C3]] та інші RISC-V — `riscv32-esp-elf-addr2line`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-028 sha:691fefcb src:kartky/k07-panika.md:48 klas:F -->
### T-K07-028 · proza · рядок 48

**Книга каже, дослівно:**

> Читати **знизу вгору**: нижні кадри — хто викликав, верхній — де впало.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-029 sha:f4767606 src:kartky/k07-panika.md:52 klas:F -->
### T-K07-029 · proza · рядок 52

**Книга каже, дослівно:**

> Без `.elf` адреси перекласти нема в що: символів у прошивці немає.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-030 sha:4837dd6e src:kartky/k07-panika.md:52 klas:F -->
### T-K07-030 · proza · рядок 52

**Книга каже, дослівно:**

> Лишається причина паніки і `PC` — цього досить, щоб відрізнити збій у власному коді від збою в стеку Wi-Fi, але не досить для рядка.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-031 sha:0b3b2823 src:kartky/k07-panika.md:57 klas:F -->
### T-K07-031 · proza · рядок 57

**Книга каже, дослівно:**

> `.elf` того самого збирання, що й `.bin`, — єдине, що робить backtrace читним.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-032 sha:9b8eb9e1 src:kartky/k07-panika.md:57 klas:F -->
### T-K07-032 · proza · рядок 57

**Книга каже, дослівно:**

> Зберігати `.elf` разом із кожною прошивкою, яку віддали в поле.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-033 sha:0c9a59fb src:kartky/k07-panika.md:57 klas:F -->
### T-K07-033 · proza · рядок 57

**Книга каже, дослівно:**

> Перезібрати «такий самий» пізніше не вийде: адреси зсунуться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-034 sha:9e14d394 src:kartky/k07-panika.md:64 klas:F -->
### T-K07-034 · proza · рядок 64

**Книга каже, дослівно:**

> Після паніки чип скидається — і в логу з'являється `rst:0xc`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-035 sha:fc205c28 src:kartky/k07-panika.md:64 klas:F -->
### T-K07-035 · proza · рядок 64

**Книга каже, дослівно:**

> Якщо причина паніки лишилася, це стає boot loop: паніка → скидання → паніка.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-036 sha:95c093b4 src:kartky/k07-panika.md:64 klas:F -->
### T-K07-036 · proza · рядок 64

**Книга каже, дослівно:**

> Дивитися треба **найперший** дамп після подачі живлення, а не сотий.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-K07-037 sha:f79bd0a9 src:kartky/k07-panika.md:68 klas:A -->
### T-K07-037 · proza · рядок 68

**Книга каже, дослівно:**

> Coredump у флеші (якщо ввімкнено в `menuconfig`) зберігає стан усіх задач, а не лише тієї, що впала: `idf.py coredump-info`.

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
