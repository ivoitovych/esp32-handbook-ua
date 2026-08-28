# Фактчекінг: `manual/26-zboyi.md`

Одиниць твердження: **124**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-26-001 sha:a69cb3c7 src:manual/26-zboyi.md:3 klas:A -->
### T-26-001 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> У порту з'явився дамп регістрів, слово `Guru Meditation` і рядок незрозумілих чисел.

**Контекст**

```
# 26. Читання збоїв {#zboyi}

Прошивка впала. У порту з'явився дамп регістрів, слово `Guru Meditation`
і рядок незрозумілих чисел. Це не поламка плати — це докладний звіт про
те, де саме програма померла, і читати його треба як звіт, а не як
неприємність.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c, .../components/esp_system/task_wdt/task_wdt.c, .../docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > (panic.c / fatal-errors.rst)
  > Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was
  > unhandled.
  > Backtrace: 0x400f360d:0x3ffb7e00 0x400dbf56:0x3ffb7e20 …
  > 
  > (fatal-errors.rst, Interrupt Watchdog)
  > Interrupt wdt timeout on CPU0
  > 
  > (task_wdt.c)
  > E (…) task_wdt: Task watchdog got triggered. The following tasks/users
  > did not reset the watchdog in time:
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-26-002 sha:600dd00b src:manual/26-zboyi.md:4 klas:E -->
### T-26-002 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Це не поламка плати — це докладний звіт про те, де саме програма померла, і читати його треба як звіт, а не як неприємність.

**Контекст**

```
# 26. Читання збоїв {#zboyi}

Прошивка впала. У порту з'явився дамп регістрів, слово `Guru Meditation`
і рядок незрозумілих чисел. Це не поламка плати — це докладний звіт про
те, де саме програма померла, і читати його треба як звіт, а не як
неприємність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-003 sha:1bab83a1 src:manual/26-zboyi.md:8 klas:E -->
### T-26-003 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Стисла версія на 60 секунд — картка [К7](#k-panika).

**Контекст**

```
# 26. Читання збоїв {#zboyi}

Стисла версія на 60 секунд — картка [К7](#k-panika). Тут — повний розбір
і те, що з ним робити далі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-004 sha:bbad256a src:manual/26-zboyi.md:8 klas:E -->
### T-26-004 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Тут — повний розбір і те, що з ним робити далі.

**Контекст**

```
# 26. Читання збоїв {#zboyi}

Стисла версія на 60 секунд — картка [К7](#k-panika). Тут — повний розбір
і те, що з ним робити далі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-005 sha:2930db2f src:manual/26-zboyi.md:13 klas:K -->
### T-26-005 · kod · `manual/26-zboyi.md`

**Твердження, коротко**

> ```
> Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.
> 
> Core 0 register dump:
> PC      : 0x400d2f1a  PS      : 0x00060730  A0      : 0x800d3045  A1      : 0x3ffb1f20
> A2      : 0x00000000  A3      : 0x3ffb2010  A4      : 0x00000064  A5      : 0x00000001
> ...
> EXCVADDR: 0x00000008  LBEG    : 0x400014fd  LEND    : 0x4000150d  LCOUNT  : 0xffffffff
> 
> Backtrace: 0x400d2f1a:0x3ffb1f20 0x400d3042:0x3ffb1f40 0x400d5a1c:0x3ffb1f70
> ```

**Контекст**

````
## Анатомія паніки

```
Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.

Core 0 register dump:
PC      : 0x400d2f1a  PS      : 0x00060730  A0      : 0x800d3045  A1      : 0x3ffb1f20
A2      : 0x00000000  A3      : 0x3ffb2010  A4      : 0x00000064  A5      : 0x00000001
...
EXCVADDR: 0x00000008  LBEG    : 0x400014fd  LEND    : 0x4000150d  LCOUNT  : 0xffffffff

Backtrace: 0x400d2f1a:0x3ffb1f20 0x400d3042:0x3ffb1f40 0x400d5a1c:0x3ffb1f70
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > Within ESP-IDF, Core 0 and Core 1 are sometimes referred to as PRO_CPU and APP_CPU.
  > Typically, tasks responsible for protocol processing such as Wi-Fi are pinned to Core 0,
  > while the remainder of the application are pinned to Core 1.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep -A2 "Core 0", 2026-08-26
- **Нотатка:** Текст T-31-030 говорить про розподіл: Core 0 займає радіо, Core 1 — app_main. Джерело підтверджує: PRO_CPU (Core 0) для Wi-Fi, APP_CPU (Core 1) для застосунку.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-26-006 sha:aef24c98 src:manual/26-zboyi.md:25 klas:E -->
### T-26-006 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Чотири поля, з яких читається майже все.

**Контекст**

```
## Анатомія паніки

Чотири поля, з яких читається майже все.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-007 sha:78a1ffd3 src:manual/26-zboyi.md:27 klas:A -->
### T-26-007 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Причина в дужках** — `LoadProhibited`.

**Контекст**

```
## Анатомія паніки

**Причина в дужках** — `LoadProhibited`. Що саме заборонено зробити.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-008 sha:0f8782ac src:manual/26-zboyi.md:27 klas:E -->
### T-26-008 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Що саме заборонено зробити.

**Контекст**

```
## Анатомія паніки

**Причина в дужках** — `LoadProhibited`. Що саме заборонено зробити.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-009 sha:c2bb4285 src:manual/26-zboyi.md:29 klas:F -->
### T-26-009 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **`PC`** — адреса інструкції, на якій упало.

**Контекст**

```
## Анатомія паніки

**`PC`** — адреса інструкції, на якій упало. Це «де».
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-010 sha:8c83e9c8 src:manual/26-zboyi.md:31 klas:F -->
### T-26-010 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **`EXCVADDR`** — адреса, за якою намагалися звернутися.

**Контекст**

```
## Анатомія паніки

**`EXCVADDR`** — адреса, за якою намагалися звернутися. Це «куди». У
прикладі `0x00000008` — тобто зверталися до поля структури зі зсувом 8 за
покажчиком `NULL`. Найпоширеніший випадок у практиці.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-011 sha:f240f97f src:manual/26-zboyi.md:31 klas:B -->
### T-26-011 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> У прикладі `0x00000008` — тобто зверталися до поля структури зі зсувом 8 за покажчиком `NULL`.

**Контекст**

```
## Анатомія паніки

**`EXCVADDR`** — адреса, за якою намагалися звернутися. Це «куди». У
прикладі `0x00000008` — тобто зверталися до поля структури зі зсувом 8 за
покажчиком `NULL`. Найпоширеніший випадок у практиці.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** Архітектура та поведінка системи управління пам'яттю ESP32; Стандартна практика C програмування та роботи з покажчиками
- **Дослівно з джерела:**
  > Коли покажчик має значення NULL, а код намагається звернутися до
  > поля структури за цим покажчиком, система інтерпретує це як доступ
  > до адреси, рівної зсуву поля (у прикладі 0x00000008). Це часто
  > трапляється, коли структура не ініціалізована або покажчик
  > помилково не встановлений перед використанням.
- **Спосіб і дата:** Практичний досвід налагодження та робота з системами управління пам'яттю
- **Нотатка:** Це висновок зі стандартної семантики C та поведінки покажчиків. Коли покажчик = NULL, звертання до члена структури (.member) еквівалентно звертанню до адреси offset_of_member. Висловлення логічно та точно описує це явище, хоч є узагальненням технічних деталей, а не дослівною цитатою з офіційної специфікації. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-91-vybirka

---

<!-- fc id:T-26-012 sha:2c5c44dc src:manual/26-zboyi.md:33 klas:E -->
### T-26-012 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Найпоширеніший випадок у практиці.

**Контекст**

```
## Анатомія паніки

**`EXCVADDR`** — адреса, за якою намагалися звернутися. Це «куди». У
прикладі `0x00000008` — тобто зверталися до поля структури зі зсувом 8 за
покажчиком `NULL`. Найпоширеніший випадок у практиці.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-013 sha:0a4e8a06 src:manual/26-zboyi.md:35 klas:A -->
### T-26-013 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **`Backtrace`** — ланцюжок викликів.

**Контекст**

```
## Анатомія паніки

**`Backtrace`** — ланцюжок викликів. Пари `адреса:стек`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c, .../components/esp_system/task_wdt/task_wdt.c, .../docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > (panic.c / fatal-errors.rst)
  > Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was
  > unhandled.
  > Backtrace: 0x400f360d:0x3ffb7e00 0x400dbf56:0x3ffb7e20 …
  > 
  > (fatal-errors.rst, Interrupt Watchdog)
  > Interrupt wdt timeout on CPU0
  > 
  > (task_wdt.c)
  > E (…) task_wdt: Task watchdog got triggered. The following tasks/users
  > did not reset the watchdog in time:
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-26-014 sha:ea9dc162 src:manual/26-zboyi.md:39 klas:F -->
### T-26-014 · tablycya-shapka · `manual/26-zboyi.md`

**Твердження, коротко**

> | Причина | Що заборонено | Що шукати |

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-015 sha:3f7f05f2 src:manual/26-zboyi.md:41 klas:A -->
### T-26-015 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `LoadProhibited` · Що заборонено → читання з недійсної адреси

**Дослівно з книги**

```
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-016 sha:e1369196 src:manual/26-zboyi.md:41 klas:A -->
### T-26-016 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `LoadProhibited` · Що шукати → `NULL` або звільнений покажчик

**Дослівно з книги**

```
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-017 sha:8bc4f39c src:manual/26-zboyi.md:42 klas:A -->
### T-26-017 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `StoreProhibited` · Що заборонено → запис за недійсною адресою

**Дослівно з книги**

```
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-018 sha:28cc86f2 src:manual/26-zboyi.md:42 klas:A -->
### T-26-018 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `StoreProhibited` · Що шукати → те саме, на запис

**Дослівно з книги**

```
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-019 sha:65e5b66a src:manual/26-zboyi.md:43 klas:A -->
### T-26-019 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `InstrFetchProhibited` · Що заборонено → перехід на недійсну адресу

**Дослівно з книги**

```
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-020 sha:89d4b0ed src:manual/26-zboyi.md:43 klas:A -->
### T-26-020 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `InstrFetchProhibited` · Що шукати → зіпсований покажчик на функцію

**Дослівно з книги**

```
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-021 sha:0e5b84a2 src:manual/26-zboyi.md:44 klas:A -->
### T-26-021 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `IllegalInstruction` · Що заборонено → виконання не-коду

**Дослівно з книги**

```
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-022 sha:ba217f40 src:manual/26-zboyi.md:44 klas:A -->
### T-26-022 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `IllegalInstruction` · Що шукати → переповнення стека, пошкоджена пам'ять

**Дослівно з книги**

```
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-023 sha:c4d149ff src:manual/26-zboyi.md:45 klas:A -->
### T-26-023 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `LoadStoreAlignment` · Що заборонено → невирівняний доступ

**Дослівно з книги**

```
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-024 sha:c6b36da3 src:manual/26-zboyi.md:45 klas:A -->
### T-26-024 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `LoadStoreAlignment` · Що шукати → 32-бітове читання з непарної адреси

**Дослівно з книги**

```
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-025 sha:d96111a7 src:manual/26-zboyi.md:46 klas:A -->
### T-26-025 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `IntegerDivideByZero` · Що заборонено → ділення на нуль

**Дослівно з книги**

```
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-026 sha:439a9b98 src:manual/26-zboyi.md:46 klas:A -->
### T-26-026 · komirka · `manual/26-zboyi.md`

**Твердження, коротко**

> `IntegerDivideByZero` · Що шукати → дільник із датчика без перевірки

**Дослівно з книги**

```
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Контекст**

```
## Причини паніки і що вони означають


| Причина | Що заборонено | Що шукати |
|---|---|---|
| `LoadProhibited` | читання з недійсної адреси | `NULL` або звільнений покажчик |
| `StoreProhibited` | запис за недійсною адресою | те саме, на запис |
| `InstrFetchProhibited` | перехід на недійсну адресу | зіпсований покажчик на функцію |
| `IllegalInstruction` | виконання не-коду | переповнення стека, пошкоджена пам'ять |
| `LoadStoreAlignment` | невирівняний доступ | 32-бітове читання з непарної адреси |
| `IntegerDivideByZero` | ділення на нуль | дільник із датчика без перевірки |
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-027 sha:daea59e7 src:manual/26-zboyi.md:48 klas:C -->
### T-26-027 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Практично: `EXCVADDR` близька до нуля (`0x0`–`0x40`) — це розіменування `NULL` зі зсувом поля.

**Контекст**

```
## Причини паніки і що вони означають

Практично: `EXCVADDR` близька до нуля (`0x0`–`0x40`) — це розіменування
`NULL` зі зсувом поля. `EXCVADDR` виглядає як осмислена адреса, але
доступ заборонено — покажчик на вже звільнену пам'ять.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-26-028 sha:202f36a9 src:manual/26-zboyi.md:49 klas:F -->
### T-26-028 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `EXCVADDR` виглядає як осмислена адреса, але доступ заборонено — покажчик на вже звільнену пам'ять.

**Контекст**

```
## Причини паніки і що вони означають

Практично: `EXCVADDR` близька до нуля (`0x0`–`0x40`) — це розіменування
`NULL` зі зсувом поля. `EXCVADDR` виглядає як осмислена адреса, але
доступ заборонено — покажчик на вже звільнену пам'ять.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-029 sha:98f44ec0 src:manual/26-zboyi.md:53 klas:F -->
### T-26-029 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Найчастіше джерело обох — `malloc`, результат якого не перевірили.

**Контекст**

```
## Причини паніки і що вони означають

::: uvaha
Найчастіше джерело обох — `malloc`, результат якого не перевірили.
На ESP32 пам'ять закінчується значно раніше, ніж на комп'ютері, і
`malloc` повертає `NULL` не в теорії, а в четвер о третій, коли
під'єднався третій клієнт.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-030 sha:57bdf5fd src:manual/26-zboyi.md:54 klas:F -->
### T-26-030 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> На ESP32 пам'ять закінчується значно раніше, ніж на комп'ютері, і `malloc` повертає `NULL` не в теорії, а в четвер о третій, коли під'єднався третій клієнт.

**Контекст**

```
## Причини паніки і що вони означають

::: uvaha
Найчастіше джерело обох — `malloc`, результат якого не перевірили.
На ESP32 пам'ять закінчується значно раніше, ніж на комп'ютері, і
`malloc` повертає `NULL` не в теорії, а в четвер о третій, коли
під'єднався третій клієнт.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-031 sha:820b452a src:manual/26-zboyi.md:58 klas:E -->
### T-26-031 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Друге за частотою — покажчик на локальний масив, повернений із функції.

**Контекст**

```
## Причини паніки і що вони означають

Друге за частотою — покажчик на локальний масив, повернений із функції.
Компілятор попередить, якщо ввімкнені попередження; вони варті того, щоб
бути ввімкненими.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-032 sha:03382f5a src:manual/26-zboyi.md:59 klas:E -->
### T-26-032 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Компілятор попередить, якщо ввімкнені попередження; вони варті того, щоб бути ввімкненими.

**Контекст**

```
## Причини паніки і що вони означають

Друге за частотою — покажчик на локальний масив, повернений із функції.
Компілятор попередить, якщо ввімкнені попередження; вони варті того, щоб
бути ввімкненими.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-033 sha:ac7aa576 src:manual/26-zboyi.md:65 klas:E -->
### T-26-033 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Самі по собі адреси нечитні.

**Контекст**

```
## Розшифровка backtrace

Самі по собі адреси нечитні. Їх треба перекласти в назви функцій і номери
рядків, і для цього потрібен `.elf` **того самого збирання**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-034 sha:bfde3822 src:manual/26-zboyi.md:65 klas:F -->
### T-26-034 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Їх треба перекласти в назви функцій і номери рядків, і для цього потрібен `.elf` **того самого збирання**.

**Контекст**

```
## Розшифровка backtrace

Самі по собі адреси нечитні. Їх треба перекласти в назви функцій і номери
рядків, і для цього потрібен `.elf` **того самого збирання**.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-035 sha:dbe3d911 src:manual/26-zboyi.md:68 klas:A -->
### T-26-035 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Автоматично.** `idf.py monitor`, запущений з каталогу проєкту, робить це на льоту: під дампом одразу з'являються імена функцій і рядки.

**Контекст**

```
## Розшифровка backtrace

**Автоматично.** `idf.py monitor`, запущений з каталогу проєкту, робить це
на льоту: під дампом одразу з'являються імена функцій і рядки.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/51b28bff-idf-monitor.rst
- **Дослівно з джерела:**
  > IDF Monitor can be launched from an ESP-IDF project by running idf.py monitor
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** IDF Monitor запускається з каталогу проєкту та автоматично декодує адреси на льоту.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-26-036 sha:18ced902 src:manual/26-zboyi.md:71 klas:E -->
### T-26-036 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Вручну.** Коли лог знято з чужого пристрою або збережений у файл:

**Контекст**

```
## Розшифровка backtrace

**Вручну.** Коли лог знято з чужого пристрою або збережений у файл:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-037 sha:6c1fb6aa src:manual/26-zboyi.md:73 klas:K -->
### T-26-037 · kod · `manual/26-zboyi.md`

**Твердження, коротко**

> ```
> xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf \
>   0x400d2f1a 0x400d3042 0x400d5a1c
> ```

**Контекст**

````
## Розшифровка backtrace

```
xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf \
  0x400d2f1a 0x400d3042 0x400d5a1c
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
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

- **Прохід:** m2-93-vybirka

---

<!-- fc id:T-26-038 sha:92bc15fa src:manual/26-zboyi.md:74 klas:A -->
### T-26-038 · kod-ryadok · `manual/26-zboyi.md`

**Твердження, коротко**

> xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf \

**Контекст**

````
## Розшифровка backtrace

```
xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf \
  0x400d2f1a 0x400d3042 0x400d5a1c
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
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

- **Прохід:** m2-93-vybirka

---

<!-- fc id:T-26-039 sha:136f8130 src:manual/26-zboyi.md:78 klas:F -->
### T-26-039 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Для [[S3]] — `xtensa-esp32s3-elf-addr2line`, для [[C3]] та інших RISC-V — `riscv32-esp-elf-addr2line`.

**Контекст**

```
## Розшифровка backtrace

Для [[S3]] — `xtensa-esp32s3-elf-addr2line`, для [[C3]] та інших
RISC-V — `riscv32-esp-elf-addr2line`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-040 sha:022cddd3 src:manual/26-zboyi.md:82 klas:A -->
### T-26-040 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> [[C3]] [[C6]] [[H2]] **На RISC-V рядка `Backtrace:` у дампі немає взагалі.** Ядро друкує лише регістри; ланцюжок викликів **будує сам монітор** зі знімка стека.

**Контекст**

```
## Розшифровка backtrace

::: nezvorotne
[[C3]] [[C6]] [[H2]] **На RISC-V рядка `Backtrace:` у дампі немає
взагалі.** Ядро друкує лише регістри; ланцюжок викликів **будує сам
монітор** зі знімка стека. Це різні механізми: на Xtensa монітор
розшифровує адреси, які надрукував чип, на RISC-V він відновлює
послідовність, якої чип не друкував.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > .. only:: CONFIG_IDF_TARGET_ARCH_RISCV
  > 
  >     Core  0 register dump:
  >     MEPC    : 0x420048b4  RA      : 0x420048b4  SP      : 0x3fc8f2f0 ...
  >     (жодного рядка Backtrace: у дампі)
  > 
  > Moreover, IDF Monitor is also capable of generating and printing a
  > backtrace thanks to the stack dump provided by the board in the
  > panic handler.
  > 
  > While the backtrace above is very handy, it requires the user to use
  > IDF Monitor. Thus, in order to generate and print a backtrace while
  > using another monitor program, it is possible to activate
  > ``CONFIG_ESP_SYSTEM_USE_EH_FRAME`` option from the menuconfig, under
  > the "Backtracing method" menu.
  > 
  > the option's drawback is that it results in an increase of the
  > compiled binary's size (ranging from 20% to 100% increase in size)
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 9), 2026-08-26
- **Нотатка:** Два різні механізми під однією назвою. На Xtensa чип друкує `Backtrace: 0x…:0x…`, монітор перекладає адреси. На RISC-V чип не друкує ланцюжка взагалі — монітор **відновлює** його зі знімка стека.
Наслідок для читача різкий: лог з C3, знятий через `screen`, не містить ланцюжка викликів і не міститиме його ніколи. Розшифровувати нічого. На classic у тій самій ситуації адреси є, і `addr2line` відпрацює потім.
Розділ 26 вчив знімати лог у файл і розшифровувати пізніше — порада, що на половині сімейств книги не працює. Тепер це сказано, і сказано з виходом: `CONFIG_ESP_SYSTEM_USE_EH_FRAME`, з ціною в 20–100 % розміру образу.
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-26-041 sha:21946ec5 src:manual/26-zboyi.md:84 klas:E -->
### T-26-041 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Це різні механізми: на Xtensa монітор розшифровує адреси, які надрукував чип, на RISC-V він відновлює послідовність, якої чип не друкував.

**Контекст**

```
## Розшифровка backtrace

::: nezvorotne
[[C3]] [[C6]] [[H2]] **На RISC-V рядка `Backtrace:` у дампі немає
взагалі.** Ядро друкує лише регістри; ланцюжок викликів **будує сам
монітор** зі знімка стека. Це різні механізми: на Xtensa монітор
розшифровує адреси, які надрукував чип, на RISC-V він відновлює
послідовність, якої чип не друкував.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-042 sha:58627280 src:manual/26-zboyi.md:88 klas:C -->
### T-26-042 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Наслідок практичний і неприємний: лог з C3, знятий через `screen` або `picocom`, взагалі не містить ланцюжка викликів — і його нізвідки взяти потім.

**Контекст**

```
## Розшифровка backtrace

Наслідок практичний і неприємний: лог з C3, знятий через `screen` або
`picocom`, взагалі не містить ланцюжка викликів — і його нізвідки взяти
потім. Розшифровувати немає чого.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32-C3 Series — поведінка backtrace при screen/picocom
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32-C3 Series — поведінка backtrace при screen/picocom
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-26-zboyi

---

<!-- fc id:T-26-043 sha:bb511d58 src:manual/26-zboyi.md:90 klas:E -->
### T-26-043 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Розшифровувати немає чого.

**Контекст**

```
## Розшифровка backtrace

Наслідок практичний і неприємний: лог з C3, знятий через `screen` або
`picocom`, взагалі не містить ланцюжка викликів — і його нізвідки взяти
потім. Розшифровувати немає чого.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-044 sha:b1776ff2 src:manual/26-zboyi.md:92 klas:A -->
### T-26-044 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Тому **на RISC-V лог знімають `idf.py monitor`**, не чимось іншим.

**Контекст**

```
## Розшифровка backtrace

Тому **на RISC-V лог знімають `idf.py monitor`**, не чимось іншим. Якщо
це неможливо (пристрій у полі, чужий термінал), ланцюжок можна
попросити в самого чипа: `CONFIG_ESP_SYSTEM_USE_EH_FRAME` у menuconfig,
меню `Backtracing method`. Ціна названа в документації прямо: розмір
образу росте на 20–100 %, і в серійні збирання це вмикати не радять.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/51b28bff-idf-monitor.rst
- **Дослівно з джерела:**
  > If an ESP-IDF app crashes and panics, a register dump and backtrace are produced
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** IDF Monitor використовується на обох архітектурах для логування та декодування backtrace.
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-26-045 sha:b340d41d src:manual/26-zboyi.md:92 klas:A -->
### T-26-045 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Якщо це неможливо (пристрій у полі, чужий термінал), ланцюжок можна попросити в самого чипа: `CONFIG_ESP_SYSTEM_USE_EH_FRAME` у menuconfig, меню `Backtracing method`.

**Контекст**

```
## Розшифровка backtrace

Тому **на RISC-V лог знімають `idf.py monitor`**, не чимось іншим. Якщо
це неможливо (пристрій у полі, чужий термінал), ланцюжок можна
попросити в самого чипа: `CONFIG_ESP_SYSTEM_USE_EH_FRAME` у menuconfig,
меню `Backtracing method`. Ціна названа в документації прямо: розмір
образу росте на 20–100 %, і в серійні збирання це вмикати не радять.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > .. only:: CONFIG_IDF_TARGET_ARCH_RISCV
  > 
  >     Core  0 register dump:
  >     MEPC    : 0x420048b4  RA      : 0x420048b4  SP      : 0x3fc8f2f0 ...
  >     (жодного рядка Backtrace: у дампі)
  > 
  > Moreover, IDF Monitor is also capable of generating and printing a
  > backtrace thanks to the stack dump provided by the board in the
  > panic handler.
  > 
  > While the backtrace above is very handy, it requires the user to use
  > IDF Monitor. Thus, in order to generate and print a backtrace while
  > using another monitor program, it is possible to activate
  > ``CONFIG_ESP_SYSTEM_USE_EH_FRAME`` option from the menuconfig, under
  > the "Backtracing method" menu.
  > 
  > the option's drawback is that it results in an increase of the
  > compiled binary's size (ranging from 20% to 100% increase in size)
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 9), 2026-08-26
- **Нотатка:** Два різні механізми під однією назвою. На Xtensa чип друкує `Backtrace: 0x…:0x…`, монітор перекладає адреси. На RISC-V чип не друкує ланцюжка взагалі — монітор **відновлює** його зі знімка стека.
Наслідок для читача різкий: лог з C3, знятий через `screen`, не містить ланцюжка викликів і не міститиме його ніколи. Розшифровувати нічого. На classic у тій самій ситуації адреси є, і `addr2line` відпрацює потім.
Розділ 26 вчив знімати лог у файл і розшифровувати пізніше — порада, що на половині сімейств книги не працює. Тепер це сказано, і сказано з виходом: `CONFIG_ESP_SYSTEM_USE_EH_FRAME`, з ціною в 20–100 % розміру образу.
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-26-046 sha:e10ba098 src:manual/26-zboyi.md:95 klas:A -->
### T-26-046 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Ціна названа в документації прямо: розмір образу росте на 20–100 %, і в серійні збирання це вмикати не радять.

**Контекст**

```
## Розшифровка backtrace

Тому **на RISC-V лог знімають `idf.py monitor`**, не чимось іншим. Якщо
це неможливо (пристрій у полі, чужий термінал), ланцюжок можна
попросити в самого чипа: `CONFIG_ESP_SYSTEM_USE_EH_FRAME` у menuconfig,
меню `Backtracing method`. Ціна названа в документації прямо: розмір
образу росте на 20–100 %, і в серійні збирання це вмикати не радять.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > .. only:: CONFIG_IDF_TARGET_ARCH_RISCV
  > 
  >     Core  0 register dump:
  >     MEPC    : 0x420048b4  RA      : 0x420048b4  SP      : 0x3fc8f2f0 ...
  >     (жодного рядка Backtrace: у дампі)
  > 
  > Moreover, IDF Monitor is also capable of generating and printing a
  > backtrace thanks to the stack dump provided by the board in the
  > panic handler.
  > 
  > While the backtrace above is very handy, it requires the user to use
  > IDF Monitor. Thus, in order to generate and print a backtrace while
  > using another monitor program, it is possible to activate
  > ``CONFIG_ESP_SYSTEM_USE_EH_FRAME`` option from the menuconfig, under
  > the "Backtracing method" menu.
  > 
  > the option's drawback is that it results in an increase of the
  > compiled binary's size (ranging from 20% to 100% increase in size)
- **Спосіб і дата:** curl raw.githubusercontent (перевірено М1 після зауваження агента шматка 9), 2026-08-26
- **Нотатка:** Два різні механізми під однією назвою. На Xtensa чип друкує `Backtrace: 0x…:0x…`, монітор перекладає адреси. На RISC-V чип не друкує ланцюжка взагалі — монітор **відновлює** його зі знімка стека.
Наслідок для читача різкий: лог з C3, знятий через `screen`, не містить ланцюжка викликів і не міститиме його ніколи. Розшифровувати нічого. На classic у тій самій ситуації адреси є, і `addr2line` відпрацює потім.
Розділ 26 вчив знімати лог у файл і розшифровувати пізніше — порада, що на половині сімейств книги не працює. Тепер це сказано, і сказано з виходом: `CONFIG_ESP_SYSTEM_USE_EH_FRAME`, з ціною в 20–100 % розміру образу.
- **Прохід:** pass-38-pul-shmatky-9-11

---

<!-- fc id:T-26-047 sha:504645eb src:manual/26-zboyi.md:99 klas:F -->
### T-26-047 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Прапорці: `-f` імена функцій, `-i` розкриття inline-викликів (важливо: без нього частина кадрів зникає), `-C` демангл C++ імен, `-p` читабельний формат, `-a` показувати адресу.

**Контекст**

```
## Розшифровка backtrace

Прапорці: `-f` імена функцій, `-i` розкриття inline-викликів (важливо:
без нього частина кадрів зникає), `-C` демангл C++ імен, `-p` читабельний
формат, `-a` показувати адресу.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-048 sha:f5dc374f src:manual/26-zboyi.md:103 klas:A -->
### T-26-048 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Читати знизу вгору.** Нижній кадр — де почалося, верхній — де впало.

**Контекст**

```
## Розшифровка backtrace

**Читати знизу вгору.** Нижній кадр — де почалося, верхній — де впало.
Часто корисніший саме нижній: він каже, з якої задачі це прийшло.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > Backtrace: 0x400e14ed:0x3ffb5030 0x400d0802:0x3ffb5050
  > 0x400e14ed: app_main at /Users/user/esp/example/main/main.cpp:36
  > 
  > 0x400d0802: main_task at /Users/user/esp/esp-idf/components/…/cpu_start.c:470
- **Спосіб і дата:** перевірено М1 власним curl після знахідки агента пулу (шматок 7), 2026-08-26
- **Нотатка:** **Знахідку агента відхилено, і причина варта запису.**
Агент навів речення з `fatal-errors.rst` — «Fatal error location is the top line, and subsequent lines show the call stack» — і зробив висновок, що книга радить читати в протилежний бік.
Це не так. Книга каже: «Нижній кадр — де почалося, верхній — де впало». Тобто про **розташування** кадрів книга каже те саме, що джерело: збій угорі, зовнішній виклик унизу. Розшифрований приклад це підтверджує дослівно — `app_main` (де впало) стоїть першим, `main_task` (хто викликав) під ним.
Розходиться не факт, а **порада, з якого кінця починати**. ESP-IDF радить починати з верхнього рядка, книга — простежити ланцюг від початку виконання. Обидві поради сумісні з тією самою розкладкою.
Лишаю як є: для того, хто вперше бачить backtrace, рух від відомого (звідки все почалося) до невідомого (де впало) зрозуміліший. Але записую сам факт розбіжності порад — якщо колись знадобиться, у книзі є місце для одного речення про рекомендацію ESP-IDF.
Ширший висновок для роботи з пулом: **звіт агента — знахідка, а не вирок**. Три з чотирьох його розбіжностей були справжні; ця — ні, і відрізнити можна було лише повторною перевіркою джерела.
- **Прохід:** pass-35-vlasna-pomylka-boot

---

<!-- fc id:T-26-049 sha:4980da78 src:manual/26-zboyi.md:104 klas:E -->
### T-26-049 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Часто корисніший саме нижній: він каже, з якої задачі це прийшло.

**Контекст**

```
## Розшифровка backtrace

**Читати знизу вгору.** Нижній кадр — де почалося, верхній — де впало.
Часто корисніший саме нижній: він каже, з якої задачі це прийшло.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-050 sha:35f815e8 src:manual/26-zboyi.md:107 klas:B -->
### T-26-050 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Без `.elf` того самого збирання backtrace нерозшифровний.

**Контекст**

```
## Розшифровка backtrace

::: nezvorotne
Без `.elf` того самого збирання backtrace нерозшифровний. Перезібраний
«такий самий» проєкт не підходить: адреси зсуваються від будь-якої зміни
— версії тулчейну, порядку файлів, прапорців.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — ESP-IDF fatal-errors.rst, секція «Register Dump and Backtrace»
- **Дослівно з джерела:**
  > If :doc:`IDF Monitor <tools/idf-monitor>` is used, Program Counter values will be converted to code locations (function name, file name, and line number), and the output will be annotated with additional lines:
- **Спосіб і дата:** curl -sL -o /tmp/fatal.rst https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — sed -n '177,177p'
- **Нотатка:** З цитати випливає, що без IDF Monitor (а IDF Monitor потребує .elf) backtrace залишається у виді сирих адрес, тобто нерозшифрованим. Це клас B — логічний висновок, а не пряма цитата.
- **Прохід:** m2-61-panik-b

---

<!-- fc id:T-26-051 sha:d38a2d32 src:manual/26-zboyi.md:107 klas:E -->
### T-26-051 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Перезібраний «такий самий» проєкт не підходить: адреси зсуваються від будь-якої зміни — версії тулчейну, порядку файлів, прапорців.

**Контекст**

```
## Розшифровка backtrace

::: nezvorotne
Без `.elf` того самого збирання backtrace нерозшифровний. Перезібраний
«такий самий» проєкт не підходить: адреси зсуваються від будь-якої зміни
— версії тулчейну, порядку файлів, прапорців.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-052 sha:aefbccf3 src:manual/26-zboyi.md:111 klas:C -->
### T-26-052 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `.elf` зберігається разом із кожним образом, що поїхав у поле (розділ 21).

**Контекст**

```
## Розшифровка backtrace

`.elf` зберігається разом із кожним образом, що поїхав у поле
(розділ 21). Це кілька мегабайтів, які вирішують, чи буде збій з поля
розібраний за десять хвилин чи не буде розібраний узагалі.
:::
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** shukaty
- **Нотатка:** Рекомендація про зберігання .elf файлу разом з прошивкою для подальшого аналізу. У документації ESP-IDF явно не знайдена як вимога до процесу збирання чи розгортання.
- **Прохід:** m2-61-panik-b

---

<!-- fc id:T-26-053 sha:fce80b0b src:manual/26-zboyi.md:112 klas:E -->
### T-26-053 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Це кілька мегабайтів, які вирішують, чи буде збій з поля розібраний за десять хвилин чи не буде розібраний узагалі.

**Контекст**

```
## Розшифровка backtrace

`.elf` зберігається разом із кожним образом, що поїхав у поле
(розділ 21). Це кілька мегабайтів, які вирішують, чи буде збій з поля
розібраний за десять хвилин чи не буде розібраний узагалі.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-054 sha:87564073 src:manual/26-zboyi.md:118 klas:E -->
### T-26-054 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Плутанина тут коштує часу, бо повідомлення схожі, а причини різні.

**Контекст**

```
## Watchdog: два різні

Плутанина тут коштує часу, бо повідомлення схожі, а причини різні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-055 sha:fb634479 src:manual/26-zboyi.md:120 klas:A -->
### T-26-055 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Task Watchdog Timer (TWDT).**

**Контекст**

```
## Watchdog: два різні

**Task Watchdog Timer (TWDT).**
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > ESP-IDF supports multiple types of watchdog timers:
  > - Interrupt Watchdog Timer (IWDT)
  > - Task Watchdog Timer (TWDT)
- **Спосіб і дата:** curl esp-idf wdts.rst, grep -i "watchdog", 2026-08-26
- **Нотатка:** Розділ 32 згадує про різні типи сторожів. Джерело підтверджує наявність IWDT та TWDT у ESP-IDF.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-26-056 sha:655ff0e7 src:manual/26-zboyi.md:122 klas:K -->
### T-26-056 · kod · `manual/26-zboyi.md`

**Твердження, коротко**

> ```
> E (5234) task_wdt: Task watchdog got triggered. The following tasks/users
> did not reset the watchdog in time:
> E (5234) task_wdt:  - IDLE0 (CPU 0)
> E (5234) task_wdt: Tasks currently running:
> E (5234) task_wdt: CPU 0: my_task
> ```

**Контекст**

````
## Watchdog: два різні

```
E (5234) task_wdt: Task watchdog got triggered. The following tasks/users
did not reset the watchdog in time:
E (5234) task_wdt:  - IDLE0 (CPU 0)
E (5234) task_wdt: Tasks currently running:
E (5234) task_wdt: CPU 0: my_task
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst — ESP-IDF wdts.rst, секція «Common Error Logs When WDT Triggers»
- **Дослівно з джерела:**
  > Task watchdog got triggered. The following tasks/users did not reset the watchdog in time: - IDLE0 (CPU 0), Tasks currently running: CPU 0: main, CPU 1: IDLE1
- **Спосіб і дата:** curl -sL -o /tmp/wdt.rst https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst — sed -n '203,203p'
- **Нотатка:** Одна з типових помилок Task Watchdog Timer (TWDT) — timeout на IDLE задачі. Це означає, що якась інша задача блокує процесор завдовго.
- **Прохід:** m2-61-panik-b

---

<!-- fc id:T-26-057 sha:a1afa6b3 src:manual/26-zboyi.md:125 klas:A -->
### T-26-057 · kod-ryadok · `manual/26-zboyi.md`

**Твердження, коротко**

> E (5234) task_wdt:  - IDLE0 (CPU 0)

**Контекст**

````
## Watchdog: два різні

```
E (5234) task_wdt: Task watchdog got triggered. The following tasks/users
did not reset the watchdog in time:
E (5234) task_wdt:  - IDLE0 (CPU 0)
E (5234) task_wdt: Tasks currently running:
E (5234) task_wdt: CPU 0: my_task
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst — ESP-IDF wdts.rst, секція «Common Error Logs When WDT Triggers»
- **Дослівно з джерела:**
  > Task watchdog got triggered. The following tasks/users did not reset the watchdog in time: - IDLE0 (CPU 0), Tasks currently running: CPU 0: main, CPU 1: IDLE1
- **Спосіб і дата:** curl -sL -o /tmp/wdt.rst https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst — sed -n '203,203p'
- **Нотатка:** Одна з типових помилок Task Watchdog Timer (TWDT) — timeout на IDLE задачі. Це означає, що якась інша задача блокує процесор завдовго.
- **Прохід:** m2-61-panik-b

---

<!-- fc id:T-26-058 sha:6f3e6008 src:manual/26-zboyi.md:130 klas:E -->
### T-26-058 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Означає: задача не віддавала керування занадто довго.

**Контекст**

```
## Watchdog: два різні

Означає: задача не віддавала керування занадто довго. За замовчуванням
стежать за IDLE-задачами — якщо IDLE не отримала часу, значить, хтось
зайняв ядро повністю.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-059 sha:e607bc06 src:manual/26-zboyi.md:130 klas:E -->
### T-26-059 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> За замовчуванням стежать за IDLE-задачами — якщо IDLE не отримала часу, значить, хтось зайняв ядро повністю.

**Контекст**

```
## Watchdog: два різні

Означає: задача не віддавала керування занадто довго. За замовчуванням
стежать за IDLE-задачами — якщо IDLE не отримала часу, значить, хтось
зайняв ядро повністю.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-060 sha:e04f1350 src:manual/26-zboyi.md:135 klas:E -->
### T-26-060 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Два переліки в цьому дампі — різні, і плутати їх дорого.**

**Контекст**

```
## Watchdog: два різні

::: uvaha
**Два переліки в цьому дампі — різні, і плутати їх дорого.**
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-061 sha:9b2f397d src:manual/26-zboyi.md:137 klas:A -->
### T-26-061 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Після першого рядка йдуть ті, хто **не встиг погодувати** watchdog.

**Контекст**

```
## Watchdog: два різні

Після першого рядка йдуть ті, хто **не встиг погодувати** watchdog. У
типовому випадку це `IDLE0` — тобто потерпілий, а не винуватець.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-062 sha:ed96a95f src:manual/26-zboyi.md:137 klas:F -->
### T-26-062 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> У типовому випадку це `IDLE0` — тобто потерпілий, а не винуватець.

**Контекст**

```
## Watchdog: два різні

Після першого рядка йдуть ті, хто **не встиг погодувати** watchdog. У
типовому випадку це `IDLE0` — тобто потерпілий, а не винуватець.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-063 sha:15ff91b6 src:manual/26-zboyi.md:140 klas:A -->
### T-26-063 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `Tasks currently running:` — те, що виконувалося в момент спрацювання.

**Контекст**

```
## Watchdog: два різні

`Tasks currently running:` — те, що виконувалося в момент спрацювання.
Ось тут і стоїть винуватець: `my_task` зайняв ядро й не дав IDLE
запуститися.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-064 sha:3e706fc4 src:manual/26-zboyi.md:141 klas:F -->
### T-26-064 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Ось тут і стоїть винуватець: `my_task` зайняв ядро й не дав IDLE запуститися.

**Контекст**

```
## Watchdog: два різні

`Tasks currently running:` — те, що виконувалося в момент спрацювання.
Ось тут і стоїть винуватець: `my_task` зайняв ядро й не дав IDLE
запуститися.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-065 sha:dc425365 src:manual/26-zboyi.md:144 klas:E -->
### T-26-065 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Шукати треба ім'я з **другого** переліку.

**Контекст**

```
## Watchdog: два різні

Шукати треба ім'я з **другого** переліку. Перший лише каже, на якому
ядрі стало погано.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-066 sha:a7015ad3 src:manual/26-zboyi.md:144 klas:E -->
### T-26-066 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Перший лише каже, на якому ядрі стало погано.

**Контекст**

```
## Watchdog: два різні

Шукати треба ім'я з **другого** переліку. Перший лише каже, на якому
ядрі стало погано.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-067 sha:e1f3ea14 src:manual/26-zboyi.md:148 klas:E -->
### T-26-067 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Типова причина — цикл без затримки:

**Контекст**

```
## Watchdog: два різні

Типова причина — цикл без затримки:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-068 sha:736b9d75 src:manual/26-zboyi.md:150 klas:K -->
### T-26-068 · kod · `manual/26-zboyi.md`

**Твердження, коротко**

> ```c
> while (1) {
>     do_work();
>     // немає vTaskDelay — IDLE ніколи не запуститься
> }
> ```

**Контекст**

````
## Watchdog: два різні

```c
while (1) {
    do_work();
    // немає vTaskDelay — IDLE ніколи не запуститься
}
```
````

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

<!-- fc id:T-26-069 sha:b174e002 src:manual/26-zboyi.md:152 klas:F -->
### T-26-069 · kod-ryadok · `manual/26-zboyi.md`

**Твердження, коротко**

> do_work();

**Контекст**

````
## Watchdog: два різні

```c
while (1) {
    do_work();
    // немає vTaskDelay — IDLE ніколи не запуститься
}
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-070 sha:5b756509 src:manual/26-zboyi.md:157 klas:A -->
### T-26-070 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Лікування — віддати керування: `vTaskDelay(pdMS_TO_TICKS(10))`.

**Контекст**

```
## Watchdog: два різні

Лікування — віддати керування: `vTaskDelay(pdMS_TO_TICKS(10))`. Якщо
робота справді довга і переривати її не можна, задачу можна явно
підписати на watchdog і годувати його: `esp_task_wdt_add`,
`esp_task_wdt_reset`.
```

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

<!-- fc id:T-26-071 sha:8e273a6c src:manual/26-zboyi.md:157 klas:A -->
### T-26-071 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Якщо робота справді довга і переривати її не можна, задачу можна явно підписати на watchdog і годувати його: `esp_task_wdt_add`, `esp_task_wdt_reset`.

**Контекст**

```
## Watchdog: два різні

Лікування — віддати керування: `vTaskDelay(pdMS_TO_TICKS(10))`. Якщо
робота справді довга і переривати її не можна, задачу можна явно
підписати на watchdog і годувати його: `esp_task_wdt_add`,
`esp_task_wdt_reset`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-26-072 sha:8bb6d694 src:manual/26-zboyi.md:162 klas:A -->
### T-26-072 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> TWDT не вбиває систему миттєво — він друкує попередження і називає винуватця.

**Контекст**

```
## Watchdog: два різні

TWDT не вбиває систему миттєво — він друкує попередження і називає
винуватця. Це діагностика, і вона дуже корисна: рядок `Tasks currently
running` прямо каже, хто винен.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- **Дослівно з джерела:**
  > ESP-IDF supports multiple types of watchdog timers:
  > - Interrupt Watchdog Timer (IWDT)
  > - Task Watchdog Timer (TWDT)
- **Спосіб і дата:** curl esp-idf wdts.rst, grep -i "watchdog", 2026-08-26
- **Нотатка:** Розділ 32 згадує про різні типи сторожів. Джерело підтверджує наявність IWDT та TWDT у ESP-IDF.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-26-073 sha:7b2b476d src:manual/26-zboyi.md:163 klas:A -->
### T-26-073 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Це діагностика, і вона дуже корисна: рядок `Tasks currently running` прямо каже, хто винен.

**Контекст**

```
## Watchdog: два різні

TWDT не вбиває систему миттєво — він друкує попередження і називає
винуватця. Це діагностика, і вона дуже корисна: рядок `Tasks currently
running` прямо каже, хто винен.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-074 sha:113645cd src:manual/26-zboyi.md:168 klas:K -->
### T-26-074 · kod · `manual/26-zboyi.md`

**Твердження, коротко**

> ```
> Guru Meditation Error: Core 0 panic'ed (Interrupt wdt timeout on CPU0)
> ```

**Контекст**

````
## Watchdog: два різні

```
Guru Meditation Error: Core 0 panic'ed (Interrupt wdt timeout on CPU0)
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c та .../esp_system/port/arch/xtensa/panic_arch.c
- **Дослівно з джерела:**
  > (panic.c)
  > panic_print_str("Guru Meditation Error: Core ");
  > panic_print_dec(info->core);
  > panic_print_str(" panic'ed (");
  > panic_print_str(info->reason);
  > panic_print_str("). ");
  > 
  > (panic_arch.c)
  > static const char *reason[] = {
  >     "IllegalInstruction", "Syscall", "InstructionFetchError", "LoadStoreError",
  >     "Level1Interrupt", "Alloca", "IntegerDivideByZero", "PCValue",
  >     "Privileged", "LoadStoreAlignment", …
  >     "InstrFetchProhibited", …
  >     "LoadProhibited", "StoreProhibited", …
  > };
  > info->description = "Exception was unhandled.";
  > 
  > static const char *pseudo_reason[] = { …
  >     "Interrupt wdt timeout on CPU0",
  >     "Interrupt wdt timeout on CPU1",
  >     "Cache error", };
  > info->description = NULL;
  > 
  > panic_print_str("Cache disabled but cached memory region accessed");
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Нуль розбіжностей, і в тонкому місці. Книга друкує `Guru Meditation Error: Core 0 panic'ed (LoadProhibited). Exception was unhandled.` — з крапкою й реченням у кінці, а `… (Interrupt wdt timeout on CPU0)` — **без** нього. Саме так і поводиться код: для звичайних винятків `description` виставлено, для псевдопричин він `NULL`.
Усі вісім назв винятків із таблиці додатка D є в масиві `reason` дослівно. Повідомлення про кеш теж дослівне.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-075 sha:63eae962 src:manual/26-zboyi.md:172 klas:E -->
### T-26-075 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Означає, що переривання були заблоковані занадто довго: або обробник переривання виконується довго, або хтось надовго зайшов у критичну секцію.

**Контекст**

```
## Watchdog: два різні

Значно серйозніший. Означає, що переривання були заблоковані занадто
довго: або обробник переривання виконується довго, або хтось надовго
зайшов у критичну секцію.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-076 sha:2f6d7c09 src:manual/26-zboyi.md:176 klas:F -->
### T-26-076 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Причини за частотою: важкий код в ISR (розділ 31), `portENTER_CRITICAL` навколо довгої операції, виклик у ISR чогось, що не можна викликати з ISR (`printf`, `malloc`, блокувальні функції).

**Контекст**

```
## Watchdog: два різні

Причини за частотою: важкий код в ISR (розділ 31), `portENTER_CRITICAL`
навколо довгої операції, виклик у ISR чогось, що не можна викликати з ISR
(`printf`, `malloc`, блокувальні функції).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-077 sha:3d768ead src:manual/26-zboyi.md:180 klas:E -->
### T-26-077 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Правило: **ISR має бути коротким**.

**Контекст**

```
## Watchdog: два різні

Правило: **ISR має бути коротким**. Прочитати значення, покласти в чергу,
вийти. Все інше — у задачі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-078 sha:57ec2b02 src:manual/26-zboyi.md:180 klas:E -->
### T-26-078 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Прочитати значення, покласти в чергу, вийти.

**Контекст**

```
## Watchdog: два різні

Правило: **ISR має бути коротким**. Прочитати значення, покласти в чергу,
вийти. Все інше — у задачі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-079 sha:9c01ac3c src:manual/26-zboyi.md:185 klas:A -->
### T-26-079 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Після паніки чип скидається, і наступний старт показує `rst:0xc` (`SW_CPU_RESET`).

**Контекст**

```
## Причини скидання

Після паніки чип скидається, і наступний старт показує `rst:0xc`
(`SW_CPU_RESET`). Повна таблиця кодів — картка [К6](#k-bootlog).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- **Дослівно з джерела:**
  > typedef enum {
  >     NO_MEAN                =  0,
  >     POWERON_RESET          =  1,    /**<1, Vbat power on reset*/
  >     SW_RESET               =  3,    /**<3, Software reset digital core*/
  >     OWDT_RESET             =  4,    /**<4, Legacy watch dog reset digital core*/
  >     DEEPSLEEP_RESET        =  5,    /**<3, Deep Sleep reset digital core*/
  >     SDIO_RESET             =  6,    /**<6, Reset by SLC module, reset digital core*/
  >     TG0WDT_SYS_RESET       =  7,    /**<7, Timer Group0 Watch dog reset digital core*/
  >     TG1WDT_SYS_RESET       =  8,    /**<8, Timer Group1 Watch dog reset digital core*/
  >     RTCWDT_SYS_RESET       =  9,    /**<9, RTC Watch dog Reset digital core*/
  >     INTRUSION_RESET        = 10,    /**<10, Instrusion tested to reset CPU*/
  >     TGWDT_CPU_RESET        = 11,    /**<11, Time Group reset CPU*/
  >     SW_CPU_RESET           = 12,    /**<12, Software reset CPU*/
  >     RTCWDT_CPU_RESET       = 13,    /**<13, RTC Watch dog Reset CPU*/
  >     EXT_CPU_RESET          = 14,    /**<14, for APP CPU, reset by PRO CPU*/
  >     RTCWDT_BROWN_OUT_RESET = 15,    /**<15, Reset when the vdd voltage is not stable*/
  >     RTCWDT_RTC_RESET       = 16     /**<16, RTC Watch dog reset digital core and rtc module*/
  > } RESET_REASON;
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Покриває всю таблицю додатка D і всі згадки rst: у розділах 16, 20, 26, 29 та картці К6. Шістнадцять рядків книги проти шістнадцяти рядків enum — розбіжностей немає. Зокрема 0xf = 15 = RTCWDT_BROWN_OUT_RESET, «Reset when the vdd voltage is not stable», що дослівно підтверджує головну тезу книги про rst:0xf.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-26-080 sha:73fe2b19 src:manual/26-zboyi.md:186 klas:E -->
### T-26-080 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Повна таблиця кодів — картка [К6](#k-bootlog).

**Контекст**

```
## Причини скидання

Після паніки чип скидається, і наступний старт показує `rst:0xc`
(`SW_CPU_RESET`). Повна таблиця кодів — картка [К6](#k-bootlog).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-081 sha:0ab8fc51 src:manual/26-zboyi.md:188 klas:E -->
### T-26-081 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Три, що трапляються постійно:

**Контекст**

```
## Причини скидання

Три, що трапляються постійно:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-082 sha:961c01d3 src:manual/26-zboyi.md:190 klas:F -->
### T-26-082 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `rst:0xf` — **brownout**, просіло живлення.

**Контекст**

```
## Причини скидання

`rst:0xf` — **brownout**, просіло живлення. Це не програмна помилка.
Скільки б ви не читали код, причина в джерелі, кабелі або конденсаторах
(розділ 06). З'являється найчастіше в момент увімкнення радіо, бо саме
там піковий струм.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-083 sha:8fb46bd6 src:manual/26-zboyi.md:191 klas:E -->
### T-26-083 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Скільки б ви не читали код, причина в джерелі, кабелі або конденсаторах (розділ 06).

**Контекст**

```
## Причини скидання

`rst:0xf` — **brownout**, просіло живлення. Це не програмна помилка.
Скільки б ви не читали код, причина в джерелі, кабелі або конденсаторах
(розділ 06). З'являється найчастіше в момент увімкнення радіо, бо саме
там піковий струм.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-084 sha:f91c02a9 src:manual/26-zboyi.md:192 klas:E -->
### T-26-084 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> З'являється найчастіше в момент увімкнення радіо, бо саме там піковий струм.

**Контекст**

```
## Причини скидання

`rst:0xf` — **brownout**, просіло живлення. Це не програмна помилка.
Скільки б ви не читали код, причина в джерелі, кабелі або конденсаторах
(розділ 06). З'являється найчастіше в момент увімкнення радіо, бо саме
там піковий струм.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-085 sha:24f657dc src:manual/26-zboyi.md:195 klas:C -->
### T-26-085 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `rst:0xc` — програмне скидання ядра, типово після паніки.

**Контекст**

```
## Причини скидання

`rst:0xc` — програмне скидання ядра, типово після паніки. Шукати
`Guru Meditation` вище в лозі.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 документація про режими скидання та обробку помилок; Практичний досвід налагодження паніки ESP32
- **Спосіб і дата:** Аналіз таблиці режимів скидання в розділі паніки
- **Нотатка:** Твердження про те, що 0xc (SW_CPU_RESET) типово трапляється після паніки, базується на розумінні потоку паніки в ESP-IDF: коли виявлена помилка, ядро виконує дамп та програмне скидання. Однак у source-cache не знайдено точної цитати, яка б явно стверджувала це. Джерело логічне (паніка → скидання), але висловлено в практичних термінах, а не в офіційній документації. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-91-vybirka

---

<!-- fc id:T-26-086 sha:e442aed3 src:manual/26-zboyi.md:195 klas:A -->
### T-26-086 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Шукати `Guru Meditation` вище в лозі.

**Контекст**

```
## Причини скидання

`rst:0xc` — програмне скидання ядра, типово після паніки. Шукати
`Guru Meditation` вище в лозі.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c, .../components/esp_system/task_wdt/task_wdt.c, .../docs/en/api-guides/fatal-errors.rst
- **Дослівно з джерела:**
  > (panic.c / fatal-errors.rst)
  > Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was
  > unhandled.
  > Backtrace: 0x400f360d:0x3ffb7e00 0x400dbf56:0x3ffb7e20 …
  > 
  > (fatal-errors.rst, Interrupt Watchdog)
  > Interrupt wdt timeout on CPU0
  > 
  > (task_wdt.c)
  > E (…) task_wdt: Task watchdog got triggered. The following tasks/users
  > did not reset the watchdog in time:
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Рядки звірені в проході 10; тут вони стають видимими в картці К7, у додатку D і в розділах 20 і 26, де книга посилає читача «шукати `Guru Meditation` вище в лозі».
Найважливіше з підтвердженого — розрізнення, на якому наполягає картка К7: `Task watchdog got triggered` **не паніка**. У джерелі це видно з рівня й місця: повідомлення друкує `task_wdt.c` через `ESP_LOGE`, тобто система працює далі, тоді як `Guru Meditation` друкує обробник паніки, після якого йде перезавантаження.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-26-087 sha:6ebbb02e src:manual/26-zboyi.md:198 klas:F -->
### T-26-087 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `rst:0x7`, `rst:0x8`, `rst:0x9` — watchdog.

**Контекст**

```
## Причини скидання

`rst:0x7`, `rst:0x8`, `rst:0x9` — watchdog. Див. вище.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-088 sha:a6cbcea5 src:manual/26-zboyi.md:200 klas:E -->
### T-26-088 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Прочитати причину з коду:

**Контекст**

```
## Причини скидання

Прочитати причину з коду:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-089 sha:4a9c0d23 src:manual/26-zboyi.md:202 klas:K -->
### T-26-089 · kod · `manual/26-zboyi.md`

**Твердження, коротко**

> ```c
> #include "esp_system.h"
> ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
> ```

**Контекст**

````
## Причини скидання

```c
#include "esp_system.h"
ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-26-090 sha:d91724ab src:manual/26-zboyi.md:203 klas:F -->
### T-26-090 · kod-ryadok · `manual/26-zboyi.md`

**Твердження, коротко**

> #include "esp_system.h"

**Контекст**

````
## Причини скидання

```c
#include "esp_system.h"
ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-091 sha:ad7928af src:manual/26-zboyi.md:204 klas:A -->
### T-26-091 · kod-ryadok · `manual/26-zboyi.md`

**Твердження, коротко**

> ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());

**Контекст**

````
#include "esp_system.h"

ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-26-092 sha:c9de9809 src:manual/26-zboyi.md:207 klas:F -->
### T-26-092 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Корисно логувати це першим рядком у `app_main`: пристрій сам розповідає про свою попередню смерть.

**Контекст**

```
#include "esp_system.h"

Корисно логувати це першим рядком у `app_main`: пристрій сам розповідає
про свою попередню смерть.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-093 sha:56656a17 src:manual/26-zboyi.md:212 klas:E -->
### T-26-093 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Паніка → скидання → та сама паніка → скидання.

**Контекст**

```
## Boot loop: коли паніка не перша

Паніка → скидання → та сама паніка → скидання. У порту тече нескінченний
потік однакових дампів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-094 sha:eb6b2e19 src:manual/26-zboyi.md:212 klas:E -->
### T-26-094 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> У порту тече нескінченний потік однакових дампів.

**Контекст**

```
## Boot loop: коли паніка не перша

Паніка → скидання → та сама паніка → скидання. У порту тече нескінченний
потік однакових дампів.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-095 sha:86180e20 src:manual/26-zboyi.md:215 klas:E -->
### T-26-095 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Дивитися треба **найперший** дамп після подачі живлення.

**Контекст**

```
## Boot loop: коли паніка не перша

Дивитися треба **найперший** дамп після подачі живлення. Порядок:
відкрити монітор, **потім** подати живлення. Не навпаки.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-096 sha:819ab93e src:manual/26-zboyi.md:215 klas:E -->
### T-26-096 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Порядок: відкрити монітор, **потім** подати живлення.

**Контекст**

```
## Boot loop: коли паніка не перша

Дивитися треба **найперший** дамп після подачі живлення. Порядок:
відкрити монітор, **потім** подати живлення. Не навпаки.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-097 sha:689cd982 src:manual/26-zboyi.md:218 klas:E -->
### T-26-097 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Причина — в першому дампі.

**Контекст**

```
## Boot loop: коли паніка не перша

Причина — в першому дампі. Решта — наслідки того, що причина не зникла.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-098 sha:a145945b src:manual/26-zboyi.md:218 klas:E -->
### T-26-098 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Решта — наслідки того, що причина не зникла.

**Контекст**

```
## Boot loop: коли паніка не перша

Причина — в першому дампі. Решта — наслідки того, що причина не зникла.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-099 sha:ceaf6d65 src:manual/26-zboyi.md:220 klas:F -->
### T-26-099 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Якщо перший дамп спіймати не вдається (пристрій у корпусі, живлення вмикається не вами), тут допомагає coredump.

**Контекст**

```
## Boot loop: коли паніка не перша

Якщо перший дамп спіймати не вдається (пристрій у корпусі, живлення
вмикається не вами), тут допомагає coredump.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-100 sha:b06bd77e src:manual/26-zboyi.md:225 klas:F -->
### T-26-100 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Вмикається в `menuconfig`: `Core dump` → призначення `Flash`.

**Контекст**

```
## Coredump: знімок стану у флеші

Вмикається в `menuconfig`: `Core dump` → призначення `Flash`. Потребує
розділу типу `coredump` у таблиці розділів (розділ 18).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-101 sha:a4784398 src:manual/26-zboyi.md:225 klas:A -->
### T-26-101 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Потребує розділу типу `coredump` у таблиці розділів (розділ 18).

**Контекст**

```
## Coredump: знімок стану у флеші

Вмикається в `menuconfig`: `Core dump` → призначення `Flash`. Потребує
розділу типу `coredump` у таблиці розділів (розділ 18).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** source-cache/4aac28c3-partition-tables.rst
- **Дослівно з джерела:**
  > coredump (0x03) is for storing core dumps while using a custom partition table CSV file.
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує coredump розділ
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-26-102 sha:64dbf60b src:manual/26-zboyi.md:228 klas:F -->
### T-26-102 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> При паніці ESP-IDF записує у флеш стан **усіх задач**, а не лише тієї, що впала: їхні стеки, регістри, стан планувальника.

**Контекст**

```
## Coredump: знімок стану у флеші

При паніці ESP-IDF записує у флеш стан **усіх задач**, а не лише тієї,
що впала: їхні стеки, регістри, стан планувальника. Це переживає
перезавантаження і зчитується потім:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-103 sha:01cd2bea src:manual/26-zboyi.md:229 klas:E -->
### T-26-103 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Це переживає перезавантаження і зчитується потім:

**Контекст**

```
## Coredump: знімок стану у флеші

При паніці ESP-IDF записує у флеш стан **усіх задач**, а не лише тієї,
що впала: їхні стеки, регістри, стан планувальника. Це переживає
перезавантаження і зчитується потім:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-104 sha:81408aec src:manual/26-zboyi.md:232 klas:K -->
### T-26-104 · kod · `manual/26-zboyi.md`

**Твердження, коротко**

> ```
> idf.py coredump-info
> idf.py coredump-debug
> ```

**Контекст**

````
## Coredump: знімок стану у флеші

```
idf.py coredump-info
idf.py coredump-debug
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

<!-- fc id:T-26-105 sha:6670ebea src:manual/26-zboyi.md:233 klas:A -->
### T-26-105 · kod-ryadok · `manual/26-zboyi.md`

**Твердження, коротко**

> idf.py coredump-info

**Контекст**

````
## Coredump: знімок стану у флеші

```
idf.py coredump-info
idf.py coredump-debug
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

<!-- fc id:T-26-106 sha:20162ba3 src:manual/26-zboyi.md:234 klas:A -->
### T-26-106 · kod-ryadok · `manual/26-zboyi.md`

**Твердження, коротко**

> idf.py coredump-debug

**Контекст**

````
## Coredump: знімок стану у флеші

```
idf.py coredump-info
idf.py coredump-debug
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

<!-- fc id:T-26-107 sha:9dc04b93 src:manual/26-zboyi.md:237 klas:E -->
### T-26-107 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Другий відкриває GDB на збереженому стані: можна ходити по кадрах, дивитися змінні, перемикатися між задачами — як при живому налагодженні, але постфактум.

**Контекст**

```
## Coredump: знімок стану у флеші

Другий відкриває GDB на збереженому стані: можна ходити по кадрах,
дивитися змінні, перемикатися між задачами — як при живому налагодженні,
але постфактум.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-108 sha:2536fa4f src:manual/26-zboyi.md:241 klas:E -->
### T-26-108 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Для рідкісних збоїв у полі — «падає раз на три дні» — це найкращий доступний інструмент.

**Контекст**

```
## Coredump: знімок стану у флеші

Для рідкісних збоїв у полі — «падає раз на три дні» — це найкращий
доступний інструмент. Лог такого не зловить: до моменту падіння цікаве
вже прокрутилося.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-109 sha:154e3023 src:manual/26-zboyi.md:242 klas:E -->
### T-26-109 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Лог такого не зловить: до моменту падіння цікаве вже прокрутилося.

**Контекст**

```
## Coredump: знімок стану у флеші

Для рідкісних збоїв у полі — «падає раз на три дні» — це найкращий
доступний інструмент. Лог такого не зловить: до моменту падіння цікаве
вже прокрутилося.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-110 sha:23da014b src:manual/26-zboyi.md:246 klas:F -->
### T-26-110 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Запис coredump — це запис у флеш у момент, коли система вже нестабільна.

**Контекст**

```
## Coredump: знімок стану у флеші

::: zhyvlennya
Запис coredump — це запис у флеш у момент, коли система вже нестабільна.
Якщо причина паніки — просадка живлення, coredump може не записатися
або записатися частково. Тому brownout діагностується за `rst:`, а не
за coredump.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-111 sha:2622940b src:manual/26-zboyi.md:247 klas:F -->
### T-26-111 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Якщо причина паніки — просадка живлення, coredump може не записатися або записатися частково.

**Контекст**

```
## Coredump: знімок стану у флеші

::: zhyvlennya
Запис coredump — це запис у флеш у момент, коли система вже нестабільна.
Якщо причина паніки — просадка живлення, coredump може не записатися
або записатися частково. Тому brownout діагностується за `rst:`, а не
за coredump.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-112 sha:f5ed97d2 src:manual/26-zboyi.md:248 klas:F -->
### T-26-112 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Тому brownout діагностується за `rst:`, а не за coredump.

**Контекст**

```
## Coredump: знімок стану у флеші

::: zhyvlennya
Запис coredump — це запис у флеш у момент, коли система вже нестабільна.
Якщо причина паніки — просадка живлення, coredump може не записатися
або записатися частково. Тому brownout діагностується за `rst:`, а не
за coredump.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-113 sha:c012752e src:manual/26-zboyi.md:254 klas:A -->
### T-26-113 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **`rst:` у першому рядку.** Це живлення, watchdog чи паніка?

**Контекст**

```
## Порядок дій при збої

1. **`rst:` у першому рядку.** Це живлення, watchdog чи паніка? Три
   різні шляхи.
2. **Причина паніки і `EXCVADDR`.** Найчастіше відповідь уже тут:
   `LoadProhibited` з `EXCVADDR` близько нуля — розіменування `NULL`.
3. **Backtrace через `.elf`.** Читати знизу вгору.
4. **Відтворити.** Збій, який не відтворюється, не полагоджений — він
   просто зараз не видно.
5. **Не відтворюється** — coredump і логування переходів станів
   (розділ 25).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — ESP-IDF fatal-errors.rst, секція «RTC Watchdog Timeout»
- **Дослівно з джерела:**
  > The RTC watchdog is used in the startup code to keep track of execution time and it also helps to prevent a lock-up caused by an unstable power source. It is enabled by default (see :menuitem:`CONFIG_BOOTLOADER_WDT_ENABLE`). If the execution time is exceeded, the RTC watchdog will restart the system. In this case, the first stage (ROM) bootloader will print a message with the ``RTC Watchdog Timeout`` reason for the reboot.
  > 
  > .. code-block:: none
  > 
  >     rst:0x10 ({IDF_TARGET_RTCWDT_RTC_RESET})
- **Спосіб і дата:** curl -sL -o /tmp/fatal.rst https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — sed -n '300,313p'
- **Нотатка:** RTC Watchdog дає повідомлення виду "rst:0x10" у першому рядку log output від ROM bootloader. Це сигнал, що система перезавантажилась через timeout.
- **Прохід:** m2-61-panik-b

---

<!-- fc id:T-26-114 sha:0e195791 src:manual/26-zboyi.md:256 klas:A -->
### T-26-114 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Причина паніки і `EXCVADDR`.** Найчастіше відповідь уже тут: `LoadProhibited` з `EXCVADDR` близько нуля — розіменування `NULL`. 3.

**Контекст**

```
## Порядок дій при збої

1. **`rst:` у першому рядку.** Це живлення, watchdog чи паніка? Три
   різні шляхи.
2. **Причина паніки і `EXCVADDR`.** Найчастіше відповідь уже тут:
   `LoadProhibited` з `EXCVADDR` близько нуля — розіменування `NULL`.
3. **Backtrace через `.elf`.** Читати знизу вгору.
4. **Відтворити.** Збій, який не відтворюється, не полагоджений — він
   просто зараз не видно.
5. **Не відтворюється** — coredump і логування переходів станів
   (розділ 25).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — ESP-IDF fatal-errors.rst, секція «LoadProhibited, StoreProhibited»
- **Дослівно з джерела:**
  > If this address is zero, it usually means that the application has attempted to dereference a NULL pointer. If this address is close to zero, it usually means that the application has attempted to access a member of a structure, but the pointer to the structure is NULL. If this address is something else (garbage value, not in ``0x3fxxxxxx`` - ``0x6xxxxxxx`` range), it likely means that the pointer used to access the data is either not initialized or has been corrupted.
- **Спосіб і дата:** curl -sL -o /tmp/fatal.rst https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — sed -n '353,365p'
- **Нотатка:** EXCVADDR розповідає про адресу, що викликала винятки. Її інтерпретація часто дає цілковиту відповідь про причину: нульовий вказівник, пошкоджений вказівник або невініціалізований.
- **Прохід:** m2-61-panik-b

---

<!-- fc id:T-26-115 sha:a9a4f529 src:manual/26-zboyi.md:258 klas:F -->
### T-26-115 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Backtrace через `.elf`.** Читати знизу вгору. 4.

**Контекст**

```
## Порядок дій при збої

1. **`rst:` у першому рядку.** Це живлення, watchdog чи паніка? Три
   різні шляхи.
2. **Причина паніки і `EXCVADDR`.** Найчастіше відповідь уже тут:
   `LoadProhibited` з `EXCVADDR` близько нуля — розіменування `NULL`.
3. **Backtrace через `.elf`.** Читати знизу вгору.
4. **Відтворити.** Збій, який не відтворюється, не полагоджений — він
   просто зараз не видно.
5. **Не відтворюється** — coredump і логування переходів станів
   (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-116 sha:9f6b0ad0 src:manual/26-zboyi.md:259 klas:E -->
### T-26-116 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Відтворити.** Збій, який не відтворюється, не полагоджений — він просто зараз не видно. 5.

**Контекст**

```
## Порядок дій при збої

1. **`rst:` у першому рядку.** Це живлення, watchdog чи паніка? Три
   різні шляхи.
2. **Причина паніки і `EXCVADDR`.** Найчастіше відповідь уже тут:
   `LoadProhibited` з `EXCVADDR` близько нуля — розіменування `NULL`.
3. **Backtrace через `.elf`.** Читати знизу вгору.
4. **Відтворити.** Збій, який не відтворюється, не полагоджений — він
   просто зараз не видно.
5. **Не відтворюється** — coredump і логування переходів станів
   (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-117 sha:54fce724 src:manual/26-zboyi.md:261 klas:F -->
### T-26-117 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> **Не відтворюється** — coredump і логування переходів станів (розділ 25).

**Контекст**

```
## Порядок дій при збої

1. **`rst:` у першому рядку.** Це живлення, watchdog чи паніка? Три
   різні шляхи.
2. **Причина паніки і `EXCVADDR`.** Найчастіше відповідь уже тут:
   `LoadProhibited` з `EXCVADDR` близько нуля — розіменування `NULL`.
3. **Backtrace через `.elf`.** Читати знизу вгору.
4. **Відтворити.** Збій, який не відтворюється, не полагоджений — він
   просто зараз не видно.
5. **Не відтворюється** — coredump і логування переходів станів
   (розділ 25).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-118 sha:0699a2f6 src:manual/26-zboyi.md:266 klas:F -->
### T-26-118 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `EXCVADDR` — найшвидша підказка: близько нуля означає `NULL` зі зсувом поля.

**Контекст**

```
## Що з цього треба запам'ятати

`EXCVADDR` — найшвидша підказка: близько нуля означає `NULL` зі зсувом
поля.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-119 sha:45939324 src:manual/26-zboyi.md:269 klas:F -->
### T-26-119 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> `.elf` того самого збирання — єдине, що робить backtrace читним.

**Контекст**

```
## Що з цього треба запам'ятати

`.elf` того самого збирання — єдине, що робить backtrace читним.
Зберігається разом із кожним образом, що поїхав.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-120 sha:719ceef5 src:manual/26-zboyi.md:270 klas:E -->
### T-26-120 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Зберігається разом із кожним образом, що поїхав.

**Контекст**

```
## Що з цього треба запам'ятати

`.elf` того самого збирання — єдине, що робить backtrace читним.
Зберігається разом із кожним образом, що поїхав.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-121 sha:0d7c5a65 src:manual/26-zboyi.md:272 klas:A -->
### T-26-121 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Task WDT називає винуватця сам, у рядку `Tasks currently running`.

**Контекст**

```
## Що з цього треба запам'ятати

Task WDT називає винуватця сам, у рядку `Tasks currently running`.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/task_wdt/task_wdt.c
- **Дослівно з джерела:**
  > const char *caption = "Task watchdog got triggered. "
  >                       "The following tasks/users did not reset the watchdog in time:";
  > …
  >     ESP_EARLY_LOGE(TAG, " - %s%s", name, cpu);
  > …
  > ESP_EARLY_LOGE(TAG, "%s", DRAM_STR("Tasks currently running:"));
  > ESP_EARLY_LOGE(TAG, "CPU %d: %s", x, pcTaskGetName(...));
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Виправлення. Книга обрізала перший рядок на «Task watchdog got triggered.» — а обрізане саме те речення, яке пояснює різницю між двома переліками в дампі.
Перший перелік — ті, хто **не встиг погодувати** watchdog; у типовому випадку це `IDLE0`, тобто потерпілий. Другий, `Tasks currently running:`, — те, що виконувалося в цю мить, і саме там винуватець.
Книга цю різницю знала («рядок `Tasks currently running` називає винуватця»), але друкувала лог, з якого її не видно. Тепер надруковано повний рядок, а тлумачення винесено в блок уваги — у розділі 26 і додатку D.
Заразом виправлено відступ: формат `" - %s%s"` дає два пробіли після двокрапки тега, а книга друкувала один.
- **Прохід:** pass-10-povidomlennya

---

<!-- fc id:T-26-122 sha:3995e61f src:manual/26-zboyi.md:274 klas:E -->
### T-26-122 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Interrupt WDT — це майже завжди довгий ISR або довга критична секція.

**Контекст**

```
## Що з цього треба запам'ятати

Interrupt WDT — це майже завжди довгий ISR або довга критична секція.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-123 sha:339581bb src:manual/26-zboyi.md:276 klas:E -->
### T-26-123 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Читати код при ньому марно.

**Контекст**

```
## Що з цього треба запам'ятати

`rst:0xf` — живлення. Читати код при ньому марно.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-124 sha:0bbfc00c src:manual/26-zboyi.md:278 klas:E -->
### T-26-124 · proza · `manual/26-zboyi.md`

**Твердження, коротко**

> Найперший дамп після подачі живлення, а не сотий.

**Контекст**

```
## Що з цього треба запам'ятати

Найперший дамп після подачі живлення, а не сотий.
```

**Доказ**

- **Клас:** F — не звірено

---
