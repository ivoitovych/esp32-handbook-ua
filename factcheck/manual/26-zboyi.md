# Фактчекінг: `manual/26-zboyi.md`

Одиниць твердження: **117**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-26-001 sha:a69cb3c7 src:manual/26-zboyi.md:3 klas:F -->
### T-26-001 · proza · рядок 3

**Книга каже, дослівно:**

> У порту з'явився дамп регістрів, слово `Guru Meditation` і рядок незрозумілих чисел.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-002 sha:600dd00b src:manual/26-zboyi.md:3 klas:F -->
### T-26-002 · proza · рядок 3

**Книга каже, дослівно:**

> Це не поламка плати — це докладний звіт про те, де саме програма померла, і читати його треба як звіт, а не як неприємність.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-003 sha:1bab83a1 src:manual/26-zboyi.md:8 klas:F -->
### T-26-003 · proza · рядок 8

**Книга каже, дослівно:**

> Стисла версія на 60 секунд — картка [К7](#k-panika).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-004 sha:bbad256a src:manual/26-zboyi.md:8 klas:F -->
### T-26-004 · proza · рядок 8

**Книга каже, дослівно:**

> Тут — повний розбір і те, що з ним робити далі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-005 sha:2930db2f src:manual/26-zboyi.md:13 klas:K -->
### T-26-005 · kod · рядок 13

**Книга каже, дослівно:**

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

<!-- fc id:T-26-006 sha:aef24c98 src:manual/26-zboyi.md:25 klas:F -->
### T-26-006 · proza · рядок 25

**Книга каже, дослівно:**

> Чотири поля, з яких читається майже все.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-007 sha:78a1ffd3 src:manual/26-zboyi.md:27 klas:A -->
### T-26-007 · proza · рядок 27

**Книга каже, дослівно:**

> **Причина в дужках** — `LoadProhibited`.

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

<!-- fc id:T-26-008 sha:0f8782ac src:manual/26-zboyi.md:27 klas:F -->
### T-26-008 · proza · рядок 27

**Книга каже, дослівно:**

> Що саме заборонено зробити.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-009 sha:c2bb4285 src:manual/26-zboyi.md:29 klas:F -->
### T-26-009 · proza · рядок 29

**Книга каже, дослівно:**

> **`PC`** — адреса інструкції, на якій упало.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-010 sha:8c83e9c8 src:manual/26-zboyi.md:31 klas:F -->
### T-26-010 · proza · рядок 31

**Книга каже, дослівно:**

> **`EXCVADDR`** — адреса, за якою намагалися звернутися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-011 sha:f240f97f src:manual/26-zboyi.md:31 klas:F -->
### T-26-011 · proza · рядок 31

**Книга каже, дослівно:**

> У прикладі `0x00000008` — тобто зверталися до поля структури зі зсувом 8 за покажчиком `NULL`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-012 sha:2c5c44dc src:manual/26-zboyi.md:31 klas:F -->
### T-26-012 · proza · рядок 31

**Книга каже, дослівно:**

> Найпоширеніший випадок у практиці.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-013 sha:0a4e8a06 src:manual/26-zboyi.md:35 klas:F -->
### T-26-013 · proza · рядок 35

**Книга каже, дослівно:**

> **`Backtrace`** — ланцюжок викликів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-014 sha:ea9dc162 src:manual/26-zboyi.md:39 klas:F -->
### T-26-014 · tablycya-shapka · рядок 39

**Книга каже, дослівно:**

> | Причина | Що заборонено | Що шукати |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-015 sha:3f7f05f2 src:manual/26-zboyi.md:40 klas:A -->
### T-26-015 · komirka · рядок 40

**Книга каже, дослівно:**

> `LoadProhibited` · Що заборонено → читання з недійсної адреси

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

<!-- fc id:T-26-016 sha:e1369196 src:manual/26-zboyi.md:40 klas:A -->
### T-26-016 · komirka · рядок 40

**Книга каже, дослівно:**

> `LoadProhibited` · Що шукати → `NULL` або звільнений покажчик

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

<!-- fc id:T-26-017 sha:8bc4f39c src:manual/26-zboyi.md:41 klas:A -->
### T-26-017 · komirka · рядок 41

**Книга каже, дослівно:**

> `StoreProhibited` · Що заборонено → запис за недійсною адресою

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

<!-- fc id:T-26-018 sha:28cc86f2 src:manual/26-zboyi.md:41 klas:A -->
### T-26-018 · komirka · рядок 41

**Книга каже, дослівно:**

> `StoreProhibited` · Що шукати → те саме, на запис

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

<!-- fc id:T-26-019 sha:65e5b66a src:manual/26-zboyi.md:42 klas:A -->
### T-26-019 · komirka · рядок 42

**Книга каже, дослівно:**

> `InstrFetchProhibited` · Що заборонено → перехід на недійсну адресу

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

<!-- fc id:T-26-020 sha:89d4b0ed src:manual/26-zboyi.md:42 klas:A -->
### T-26-020 · komirka · рядок 42

**Книга каже, дослівно:**

> `InstrFetchProhibited` · Що шукати → зіпсований покажчик на функцію

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

<!-- fc id:T-26-021 sha:0e5b84a2 src:manual/26-zboyi.md:43 klas:A -->
### T-26-021 · komirka · рядок 43

**Книга каже, дослівно:**

> `IllegalInstruction` · Що заборонено → виконання не-коду

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

<!-- fc id:T-26-022 sha:ba217f40 src:manual/26-zboyi.md:43 klas:A -->
### T-26-022 · komirka · рядок 43

**Книга каже, дослівно:**

> `IllegalInstruction` · Що шукати → переповнення стека, пошкоджена пам'ять

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

<!-- fc id:T-26-023 sha:c4d149ff src:manual/26-zboyi.md:44 klas:A -->
### T-26-023 · komirka · рядок 44

**Книга каже, дослівно:**

> `LoadStoreAlignment` · Що заборонено → невирівняний доступ

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

<!-- fc id:T-26-024 sha:c6b36da3 src:manual/26-zboyi.md:44 klas:A -->
### T-26-024 · komirka · рядок 44

**Книга каже, дослівно:**

> `LoadStoreAlignment` · Що шукати → 32-бітове читання з непарної адреси

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

<!-- fc id:T-26-025 sha:d96111a7 src:manual/26-zboyi.md:45 klas:A -->
### T-26-025 · komirka · рядок 45

**Книга каже, дослівно:**

> `IntegerDivideByZero` · Що заборонено → ділення на нуль

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

<!-- fc id:T-26-026 sha:439a9b98 src:manual/26-zboyi.md:45 klas:A -->
### T-26-026 · komirka · рядок 45

**Книга каже, дослівно:**

> `IntegerDivideByZero` · Що шукати → дільник із датчика без перевірки

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
### T-26-027 · proza · рядок 48

**Книга каже, дослівно:**

> Практично: `EXCVADDR` близька до нуля (`0x0`–`0x40`) — це розіменування `NULL` зі зсувом поля.

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** datasheet відповідних мікросхем (Solomon Systech, Bosch, Sensirion, ROHM, ST, TI, Microchip)
- **Що шукати в джерелі:** для SH1106 — розмір внутрішньої відеопам'яті (132 стовпці проти 128 у SSD1306), звідки береться зсув на два пікселі; для решти — таблиця адрес I²C і піни вибору адреси в кожному datasheet.
- **Нотатка:** Покриває таблицю адрес у додатку E й таблицю дисплеїв у розділі 46 — десятки окремих тверджень, кожне з яких перевіряється швидко, але лише за наявності доступу.
- **Прохід:** pass-03-nedostupni

---

<!-- fc id:T-26-028 sha:202f36a9 src:manual/26-zboyi.md:48 klas:F -->
### T-26-028 · proza · рядок 48

**Книга каже, дослівно:**

> `EXCVADDR` виглядає як осмислена адреса, але доступ заборонено — покажчик на вже звільнену пам'ять.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-029 sha:98f44ec0 src:manual/26-zboyi.md:53 klas:F -->
### T-26-029 · proza · рядок 53

**Книга каже, дослівно:**

> Найчастіше джерело обох — `malloc`, результат якого не перевірили.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-030 sha:57bdf5fd src:manual/26-zboyi.md:53 klas:F -->
### T-26-030 · proza · рядок 53

**Книга каже, дослівно:**

> На ESP32 пам'ять закінчується значно раніше, ніж на комп'ютері, і `malloc` повертає `NULL` не в теорії, а в четвер о третій, коли під'єднався третій клієнт.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-031 sha:820b452a src:manual/26-zboyi.md:58 klas:F -->
### T-26-031 · proza · рядок 58

**Книга каже, дослівно:**

> Друге за частотою — покажчик на локальний масив, повернений із функції.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-032 sha:03382f5a src:manual/26-zboyi.md:58 klas:F -->
### T-26-032 · proza · рядок 58

**Книга каже, дослівно:**

> Компілятор попередить, якщо ввімкнені попередження; вони варті того, щоб бути ввімкненими.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-033 sha:ac7aa576 src:manual/26-zboyi.md:65 klas:F -->
### T-26-033 · proza · рядок 65

**Книга каже, дослівно:**

> Самі по собі адреси нечитні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-034 sha:bfde3822 src:manual/26-zboyi.md:65 klas:F -->
### T-26-034 · proza · рядок 65

**Книга каже, дослівно:**

> Їх треба перекласти в назви функцій і номери рядків, і для цього потрібен `.elf` **того самого збирання**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-035 sha:dbe3d911 src:manual/26-zboyi.md:68 klas:F -->
### T-26-035 · proza · рядок 68

**Книга каже, дослівно:**

> **Автоматично.** `idf.py monitor`, запущений з каталогу проєкту, робить це на льоту: під дампом одразу з'являються імена функцій і рядки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-036 sha:18ced902 src:manual/26-zboyi.md:71 klas:F -->
### T-26-036 · proza · рядок 71

**Книга каже, дослівно:**

> **Вручну.** Коли лог знято з чужого пристрою або збережений у файл:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-037 sha:6c1fb6aa src:manual/26-zboyi.md:73 klas:K -->
### T-26-037 · kod · рядок 73

**Книга каже, дослівно:**

> ```
> xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf \
>   0x400d2f1a 0x400d3042 0x400d5a1c
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-038 sha:92bc15fa src:manual/26-zboyi.md:74 klas:F -->
### T-26-038 · kod-ryadok · рядок 74

**Книга каже, дослівно:**

> xtensa-esp32-elf-addr2line -pfiaC -e build/app.elf \

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-039 sha:136f8130 src:manual/26-zboyi.md:78 klas:F -->
### T-26-039 · proza · рядок 78

**Книга каже, дослівно:**

> Для [[S3]] — `xtensa-esp32s3-elf-addr2line`, для [[C3]] та інших RISC-V — `riscv32-esp-elf-addr2line`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-040 sha:504645eb src:manual/26-zboyi.md:81 klas:F -->
### T-26-040 · proza · рядок 81

**Книга каже, дослівно:**

> Прапорці: `-f` імена функцій, `-i` розкриття inline-викликів (важливо: без нього частина кадрів зникає), `-C` демангл C++ імен, `-p` читабельний формат, `-a` показувати адресу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-041 sha:f5dc374f src:manual/26-zboyi.md:85 klas:F -->
### T-26-041 · proza · рядок 85

**Книга каже, дослівно:**

> **Читати знизу вгору.** Нижній кадр — де почалося, верхній — де впало.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-042 sha:4980da78 src:manual/26-zboyi.md:85 klas:F -->
### T-26-042 · proza · рядок 85

**Книга каже, дослівно:**

> Часто корисніший саме нижній: він каже, з якої задачі це прийшло.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-043 sha:35f815e8 src:manual/26-zboyi.md:89 klas:F -->
### T-26-043 · proza · рядок 89

**Книга каже, дослівно:**

> Без `.elf` того самого збирання backtrace нерозшифровний.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-044 sha:d38a2d32 src:manual/26-zboyi.md:89 klas:F -->
### T-26-044 · proza · рядок 89

**Книга каже, дослівно:**

> Перезібраний «такий самий» проєкт не підходить: адреси зсуваються від будь-якої зміни — версії тулчейну, порядку файлів, прапорців.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-045 sha:aefbccf3 src:manual/26-zboyi.md:93 klas:F -->
### T-26-045 · proza · рядок 93

**Книга каже, дослівно:**

> `.elf` зберігається разом із кожним образом, що поїхав у поле (розділ 21).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-046 sha:fce80b0b src:manual/26-zboyi.md:93 klas:F -->
### T-26-046 · proza · рядок 93

**Книга каже, дослівно:**

> Це кілька мегабайтів, які вирішують, чи буде збій з поля розібраний за десять хвилин чи не буде розібраний узагалі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-047 sha:87564073 src:manual/26-zboyi.md:100 klas:F -->
### T-26-047 · proza · рядок 100

**Книга каже, дослівно:**

> Плутанина тут коштує часу, бо повідомлення схожі, а причини різні.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-048 sha:fb634479 src:manual/26-zboyi.md:102 klas:F -->
### T-26-048 · proza · рядок 102

**Книга каже, дослівно:**

> **Task Watchdog Timer (TWDT).**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-049 sha:655ff0e7 src:manual/26-zboyi.md:104 klas:K -->
### T-26-049 · kod · рядок 104

**Книга каже, дослівно:**

> ```
> E (5234) task_wdt: Task watchdog got triggered. The following tasks/users
> did not reset the watchdog in time:
> E (5234) task_wdt:  - IDLE0 (CPU 0)
> E (5234) task_wdt: Tasks currently running:
> E (5234) task_wdt: CPU 0: my_task
> ```

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

<!-- fc id:T-26-050 sha:a1afa6b3 src:manual/26-zboyi.md:107 klas:F -->
### T-26-050 · kod-ryadok · рядок 107

**Книга каже, дослівно:**

> E (5234) task_wdt:  - IDLE0 (CPU 0)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-051 sha:6f3e6008 src:manual/26-zboyi.md:112 klas:F -->
### T-26-051 · proza · рядок 112

**Книга каже, дослівно:**

> Означає: задача не віддавала керування занадто довго.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-052 sha:e607bc06 src:manual/26-zboyi.md:112 klas:F -->
### T-26-052 · proza · рядок 112

**Книга каже, дослівно:**

> За замовчуванням стежать за IDLE-задачами — якщо IDLE не отримала часу, значить, хтось зайняв ядро повністю.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-053 sha:e04f1350 src:manual/26-zboyi.md:117 klas:F -->
### T-26-053 · proza · рядок 117

**Книга каже, дослівно:**

> **Два переліки в цьому дампі — різні, і плутати їх дорого.**

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-054 sha:9b2f397d src:manual/26-zboyi.md:119 klas:A -->
### T-26-054 · proza · рядок 119

**Книга каже, дослівно:**

> Після першого рядка йдуть ті, хто **не встиг погодувати** watchdog.

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

<!-- fc id:T-26-055 sha:ed96a95f src:manual/26-zboyi.md:119 klas:F -->
### T-26-055 · proza · рядок 119

**Книга каже, дослівно:**

> У типовому випадку це `IDLE0` — тобто потерпілий, а не винуватець.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-056 sha:15ff91b6 src:manual/26-zboyi.md:122 klas:A -->
### T-26-056 · proza · рядок 122

**Книга каже, дослівно:**

> `Tasks currently running:` — те, що виконувалося в момент спрацювання.

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

<!-- fc id:T-26-057 sha:3e706fc4 src:manual/26-zboyi.md:122 klas:F -->
### T-26-057 · proza · рядок 122

**Книга каже, дослівно:**

> Ось тут і стоїть винуватець: `my_task` зайняв ядро й не дав IDLE запуститися.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-058 sha:dc425365 src:manual/26-zboyi.md:126 klas:F -->
### T-26-058 · proza · рядок 126

**Книга каже, дослівно:**

> Шукати треба ім'я з **другого** переліку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-059 sha:a7015ad3 src:manual/26-zboyi.md:126 klas:F -->
### T-26-059 · proza · рядок 126

**Книга каже, дослівно:**

> Перший лише каже, на якому ядрі стало погано.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-060 sha:e1f3ea14 src:manual/26-zboyi.md:130 klas:F -->
### T-26-060 · proza · рядок 130

**Книга каже, дослівно:**

> Типова причина — цикл без затримки:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-061 sha:736b9d75 src:manual/26-zboyi.md:132 klas:K -->
### T-26-061 · kod · рядок 132

**Книга каже, дослівно:**

> ```c
> while (1) {
>     do_work();
>     // немає vTaskDelay — IDLE ніколи не запуститься
> }
> ```

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

<!-- fc id:T-26-062 sha:b174e002 src:manual/26-zboyi.md:134 klas:F -->
### T-26-062 · kod-ryadok · рядок 134

**Книга каже, дослівно:**

> do_work();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-063 sha:5b756509 src:manual/26-zboyi.md:139 klas:A -->
### T-26-063 · proza · рядок 139

**Книга каже, дослівно:**

> Лікування — віддати керування: `vTaskDelay(pdMS_TO_TICKS(10))`.

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

<!-- fc id:T-26-064 sha:8e273a6c src:manual/26-zboyi.md:139 klas:A -->
### T-26-064 · proza · рядок 139

**Книга каже, дослівно:**

> Якщо робота справді довга і переривати її не можна, задачу можна явно підписати на watchdog і годувати його: `esp_task_wdt_add`, `esp_task_wdt_reset`.

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

<!-- fc id:T-26-065 sha:8bb6d694 src:manual/26-zboyi.md:144 klas:F -->
### T-26-065 · proza · рядок 144

**Книга каже, дослівно:**

> TWDT не вбиває систему миттєво — він друкує попередження і називає винуватця.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-066 sha:7b2b476d src:manual/26-zboyi.md:144 klas:A -->
### T-26-066 · proza · рядок 144

**Книга каже, дослівно:**

> Це діагностика, і вона дуже корисна: рядок `Tasks currently running` прямо каже, хто винен.

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

<!-- fc id:T-26-067 sha:113645cd src:manual/26-zboyi.md:150 klas:K -->
### T-26-067 · kod · рядок 150

**Книга каже, дослівно:**

> ```
> Guru Meditation Error: Core 0 panic'ed (Interrupt wdt timeout on CPU0)
> ```

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

<!-- fc id:T-26-068 sha:63eae962 src:manual/26-zboyi.md:154 klas:F -->
### T-26-068 · proza · рядок 154

**Книга каже, дослівно:**

> Означає, що переривання були заблоковані занадто довго: або обробник переривання виконується довго, або хтось надовго зайшов у критичну секцію.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-069 sha:2f6d7c09 src:manual/26-zboyi.md:158 klas:F -->
### T-26-069 · proza · рядок 158

**Книга каже, дослівно:**

> Причини за частотою: важкий код в ISR (розділ 31), `portENTER_CRITICAL` навколо довгої операції, виклик у ISR чогось, що не можна викликати з ISR (`printf`, `malloc`, блокувальні функції).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-070 sha:3d768ead src:manual/26-zboyi.md:162 klas:F -->
### T-26-070 · proza · рядок 162

**Книга каже, дослівно:**

> Правило: **ISR має бути коротким**.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-071 sha:57ec2b02 src:manual/26-zboyi.md:162 klas:F -->
### T-26-071 · proza · рядок 162

**Книга каже, дослівно:**

> Прочитати значення, покласти в чергу, вийти.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-072 sha:9c01ac3c src:manual/26-zboyi.md:167 klas:A -->
### T-26-072 · proza · рядок 167

**Книга каже, дослівно:**

> Після паніки чип скидається, і наступний старт показує `rst:0xc` (`SW_CPU_RESET`).

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

<!-- fc id:T-26-073 sha:73fe2b19 src:manual/26-zboyi.md:167 klas:F -->
### T-26-073 · proza · рядок 167

**Книга каже, дослівно:**

> Повна таблиця кодів — картка [К6](#k-bootlog).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-074 sha:0ab8fc51 src:manual/26-zboyi.md:170 klas:F -->
### T-26-074 · proza · рядок 170

**Книга каже, дослівно:**

> Три, що трапляються постійно:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-075 sha:961c01d3 src:manual/26-zboyi.md:172 klas:F -->
### T-26-075 · proza · рядок 172

**Книга каже, дослівно:**

> `rst:0xf` — **brownout**, просіло живлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-076 sha:8fb46bd6 src:manual/26-zboyi.md:172 klas:F -->
### T-26-076 · proza · рядок 172

**Книга каже, дослівно:**

> Скільки б ви не читали код, причина в джерелі, кабелі або конденсаторах (розділ 06).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-077 sha:f91c02a9 src:manual/26-zboyi.md:172 klas:F -->
### T-26-077 · proza · рядок 172

**Книга каже, дослівно:**

> З'являється найчастіше в момент увімкнення радіо, бо саме там піковий струм.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-078 sha:24f657dc src:manual/26-zboyi.md:177 klas:F -->
### T-26-078 · proza · рядок 177

**Книга каже, дослівно:**

> `rst:0xc` — програмне скидання ядра, типово після паніки.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-079 sha:e442aed3 src:manual/26-zboyi.md:177 klas:F -->
### T-26-079 · proza · рядок 177

**Книга каже, дослівно:**

> Шукати `Guru Meditation` вище в лозі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-080 sha:6ebbb02e src:manual/26-zboyi.md:180 klas:F -->
### T-26-080 · proza · рядок 180

**Книга каже, дослівно:**

> `rst:0x7`, `rst:0x8`, `rst:0x9` — watchdog.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-081 sha:a6cbcea5 src:manual/26-zboyi.md:182 klas:F -->
### T-26-081 · proza · рядок 182

**Книга каже, дослівно:**

> Прочитати причину з коду:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-082 sha:4a9c0d23 src:manual/26-zboyi.md:184 klas:K -->
### T-26-082 · kod · рядок 184

**Книга каже, дослівно:**

> ```c
> #include "esp_system.h"
> ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());
> ```

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

<!-- fc id:T-26-083 sha:d91724ab src:manual/26-zboyi.md:185 klas:F -->
### T-26-083 · kod-ryadok · рядок 185

**Книга каже, дослівно:**

> #include "esp_system.h"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-084 sha:ad7928af src:manual/26-zboyi.md:186 klas:A -->
### T-26-084 · kod-ryadok · рядок 186

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "причина скидання: %d", esp_reset_reason());

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

<!-- fc id:T-26-085 sha:c9de9809 src:manual/26-zboyi.md:189 klas:F -->
### T-26-085 · proza · рядок 189

**Книга каже, дослівно:**

> Корисно логувати це першим рядком у `app_main`: пристрій сам розповідає про свою попередню смерть.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-086 sha:56656a17 src:manual/26-zboyi.md:194 klas:F -->
### T-26-086 · proza · рядок 194

**Книга каже, дослівно:**

> Паніка → скидання → та сама паніка → скидання.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-087 sha:eb6b2e19 src:manual/26-zboyi.md:194 klas:F -->
### T-26-087 · proza · рядок 194

**Книга каже, дослівно:**

> У порту тече нескінченний потік однакових дампів.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-088 sha:86180e20 src:manual/26-zboyi.md:197 klas:F -->
### T-26-088 · proza · рядок 197

**Книга каже, дослівно:**

> Дивитися треба **найперший** дамп після подачі живлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-089 sha:819ab93e src:manual/26-zboyi.md:197 klas:F -->
### T-26-089 · proza · рядок 197

**Книга каже, дослівно:**

> Порядок: відкрити монітор, **потім** подати живлення.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-090 sha:689cd982 src:manual/26-zboyi.md:200 klas:F -->
### T-26-090 · proza · рядок 200

**Книга каже, дослівно:**

> Причина — в першому дампі.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-091 sha:a145945b src:manual/26-zboyi.md:200 klas:F -->
### T-26-091 · proza · рядок 200

**Книга каже, дослівно:**

> Решта — наслідки того, що причина не зникла.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-092 sha:ceaf6d65 src:manual/26-zboyi.md:202 klas:F -->
### T-26-092 · proza · рядок 202

**Книга каже, дослівно:**

> Якщо перший дамп спіймати не вдається (пристрій у корпусі, живлення вмикається не вами), тут допомагає coredump.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-093 sha:b06bd77e src:manual/26-zboyi.md:207 klas:F -->
### T-26-093 · proza · рядок 207

**Книга каже, дослівно:**

> Вмикається в `menuconfig`: `Core dump` → призначення `Flash`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-094 sha:a4784398 src:manual/26-zboyi.md:207 klas:F -->
### T-26-094 · proza · рядок 207

**Книга каже, дослівно:**

> Потребує розділу типу `coredump` у таблиці розділів (розділ 18).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-095 sha:64dbf60b src:manual/26-zboyi.md:210 klas:F -->
### T-26-095 · proza · рядок 210

**Книга каже, дослівно:**

> При паніці ESP-IDF записує у флеш стан **усіх задач**, а не лише тієї, що впала: їхні стеки, регістри, стан планувальника.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-096 sha:01cd2bea src:manual/26-zboyi.md:210 klas:F -->
### T-26-096 · proza · рядок 210

**Книга каже, дослівно:**

> Це переживає перезавантаження і зчитується потім:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-097 sha:81408aec src:manual/26-zboyi.md:214 klas:K -->
### T-26-097 · kod · рядок 214

**Книга каже, дослівно:**

> ```
> idf.py coredump-info
> idf.py coredump-debug
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

<!-- fc id:T-26-098 sha:6670ebea src:manual/26-zboyi.md:215 klas:A -->
### T-26-098 · kod-ryadok · рядок 215

**Книга каже, дослівно:**

> idf.py coredump-info

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

<!-- fc id:T-26-099 sha:20162ba3 src:manual/26-zboyi.md:216 klas:A -->
### T-26-099 · kod-ryadok · рядок 216

**Книга каже, дослівно:**

> idf.py coredump-debug

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

<!-- fc id:T-26-100 sha:9dc04b93 src:manual/26-zboyi.md:219 klas:F -->
### T-26-100 · proza · рядок 219

**Книга каже, дослівно:**

> Другий відкриває GDB на збереженому стані: можна ходити по кадрах, дивитися змінні, перемикатися між задачами — як при живому налагодженні, але постфактум.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-101 sha:2536fa4f src:manual/26-zboyi.md:223 klas:F -->
### T-26-101 · proza · рядок 223

**Книга каже, дослівно:**

> Для рідкісних збоїв у полі — «падає раз на три дні» — це найкращий доступний інструмент.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-102 sha:154e3023 src:manual/26-zboyi.md:223 klas:F -->
### T-26-102 · proza · рядок 223

**Книга каже, дослівно:**

> Лог такого не зловить: до моменту падіння цікаве вже прокрутилося.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-103 sha:23da014b src:manual/26-zboyi.md:228 klas:F -->
### T-26-103 · proza · рядок 228

**Книга каже, дослівно:**

> Запис coredump — це запис у флеш у момент, коли система вже нестабільна.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-104 sha:2622940b src:manual/26-zboyi.md:228 klas:F -->
### T-26-104 · proza · рядок 228

**Книга каже, дослівно:**

> Якщо причина паніки — просадка живлення, coredump може не записатися або записатися частково.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-105 sha:f5ed97d2 src:manual/26-zboyi.md:228 klas:F -->
### T-26-105 · proza · рядок 228

**Книга каже, дослівно:**

> Тому brownout діагностується за `rst:`, а не за coredump.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-106 sha:c012752e src:manual/26-zboyi.md:236 klas:F -->
### T-26-106 · proza · рядок 236

**Книга каже, дослівно:**

> **`rst:` у першому рядку.** Це живлення, watchdog чи паніка?

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-107 sha:0e195791 src:manual/26-zboyi.md:236 klas:A -->
### T-26-107 · proza · рядок 236

**Книга каже, дослівно:**

> **Причина паніки і `EXCVADDR`.** Найчастіше відповідь уже тут: `LoadProhibited` з `EXCVADDR` близько нуля — розіменування `NULL`. 3.

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

<!-- fc id:T-26-108 sha:a9a4f529 src:manual/26-zboyi.md:236 klas:F -->
### T-26-108 · proza · рядок 236

**Книга каже, дослівно:**

> **Backtrace через `.elf`.** Читати знизу вгору. 4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-109 sha:9f6b0ad0 src:manual/26-zboyi.md:236 klas:F -->
### T-26-109 · proza · рядок 236

**Книга каже, дослівно:**

> **Відтворити.** Збій, який не відтворюється, не полагоджений — він просто зараз не видно. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-110 sha:54fce724 src:manual/26-zboyi.md:236 klas:F -->
### T-26-110 · proza · рядок 236

**Книга каже, дослівно:**

> **Не відтворюється** — coredump і логування переходів станів (розділ 25).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-111 sha:0699a2f6 src:manual/26-zboyi.md:248 klas:F -->
### T-26-111 · proza · рядок 248

**Книга каже, дослівно:**

> `EXCVADDR` — найшвидша підказка: близько нуля означає `NULL` зі зсувом поля.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-112 sha:45939324 src:manual/26-zboyi.md:251 klas:F -->
### T-26-112 · proza · рядок 251

**Книга каже, дослівно:**

> `.elf` того самого збирання — єдине, що робить backtrace читним.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-113 sha:719ceef5 src:manual/26-zboyi.md:251 klas:F -->
### T-26-113 · proza · рядок 251

**Книга каже, дослівно:**

> Зберігається разом із кожним образом, що поїхав.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-114 sha:0d7c5a65 src:manual/26-zboyi.md:254 klas:A -->
### T-26-114 · proza · рядок 254

**Книга каже, дослівно:**

> Task WDT називає винуватця сам, у рядку `Tasks currently running`.

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

<!-- fc id:T-26-115 sha:3995e61f src:manual/26-zboyi.md:256 klas:F -->
### T-26-115 · proza · рядок 256

**Книга каже, дослівно:**

> Interrupt WDT — це майже завжди довгий ISR або довга критична секція.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-116 sha:339581bb src:manual/26-zboyi.md:258 klas:F -->
### T-26-116 · proza · рядок 258

**Книга каже, дослівно:**

> Читати код при ньому марно.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-26-117 sha:0bbfc00c src:manual/26-zboyi.md:260 klas:F -->
### T-26-117 · proza · рядок 260

**Книга каже, дослівно:**

> Найперший дамп після подачі живлення, а не сотий.

**Доказ**

- **Клас:** F — не звірено

---
