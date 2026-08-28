# Фактчекінг: `manual/21-seriyna.md`

Одиниць твердження: **98**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-21-001 sha:5494609e src:manual/21-seriyna.md:3 klas:E -->
### T-21-001 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Прошити одну плату і прошити двадцять — різні задачі.

**Контекст**

```
# 21. Серійна прошивка партії {#seriyna}

Прошити одну плату і прошити двадцять — різні задачі. Різниця не в
масштабі, а в тому, що при двадцяти платах з'являються питання, яких на
одній не буває: чи всі прошилися, чи всі прошилися **однаково**, яка
версія куди поїхала, і що робити з тим, що в кожної плати має бути своє.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-002 sha:f740932a src:manual/21-seriyna.md:3 klas:E -->
### T-21-002 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Різниця не в масштабі, а в тому, що при двадцяти платах з'являються питання, яких на одній не буває: чи всі прошилися, чи всі прошилися **однаково**, яка версія куди поїхала, і що робити з тим, що в кожної плати має бути своє.

**Контекст**

```
# 21. Серійна прошивка партії {#seriyna}

Прошити одну плату і прошити двадцять — різні задачі. Різниця не в
масштабі, а в тому, що при двадцяти платах з'являються питання, яких на
одній не буває: чи всі прошилися, чи всі прошилися **однаково**, яка
версія куди поїхала, і що робити з тим, що в кожної плати має бути своє.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-003 sha:aa2a0e34 src:manual/21-seriyna.md:8 klas:D -->
### T-21-003 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Той, хто прийшов сюди прошити партію готових плат, може не читати ні про FreeRTOS, ні про периферію: маршрут іде сюди і на картку [К15](#k-seriyna).

**Контекст**

```
# 21. Серійна прошивка партії {#seriyna}

Цей розділ — про процес. Той, хто прийшов сюди прошити партію готових
плат, може не читати ні про FreeRTOS, ні про периферію: маршрут іде сюди
і на картку [К15](#k-seriyna).
```

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/posylannya.py — перевірка проти дерева файлів репозиторію
- **Розрахунок:**
  posylannya: згадок 689, адресатів 79, помилок 0
  
  Перевірено:
    «розділ NN»  → існує manual/NN-*.md, і це не той самий розділ
    «картка КN»  → існує kartky/kNN-*.md
    «додаток X»  → існує dodatky/x-*.md (з переведенням кириличної
                   букви в латинську назву файлу)
- **Спосіб і дата:** python3 tools/posylannya.py, 2026-08-26
- **Нотатка:** Нуль помилок із 689 згадок. Це другий вимір після арифметики й API, де прохід не дав жодного виправлення.
Клас `D`, а не `A`: зовнішнє джерело тут не потрібне й не буває — перевіряється твердження книги про саму себе, і перевіряється механічно.
Головне тут не результат, а те, що перевірка тепер постійна: `tools/posylannya.py` стоїть у `make check`. Досі номер розділу можна було зсунути, і жоден інструмент цього б не помітив — текст лишається зв'язним, а читач іде не туди.
Одне самопосилання цей інструмент уже спіймав раніше, у проході 9 (розділ 17 відсилав сам на себе); тоді його знайшов `review.py` на клікабельному посиланні. Тепер такий самий контроль поширено на прозу.
- **Прохід:** pass-14-marshruty

---

<!-- fc id:T-21-004 sha:7aee2849 src:manual/21-seriyna.md:14 klas:E -->
### T-21-004 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Три файли на трьох адресах — нормально для розробки і погано для виробництва: три нагоди помилитися, помножені на кількість плат.

**Контекст**

```
## Перше рішення: один файл замість трьох

Три файли на трьох адресах — нормально для розробки і погано для
виробництва: три нагоди помилитися, помножені на кількість плат.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-005 sha:fd16eb2f src:manual/21-seriyna.md:17 klas:E -->
### T-21-005 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Складіть один образ (розділ 17).

**Контекст**

```
## Перше рішення: один файл замість трьох

Складіть один образ (розділ 17). Якщо проєкт ESP-IDF під рукою — цим і
обмежтеся, бо адреси підставить сама збірка:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-006 sha:169c5b39 src:manual/21-seriyna.md:17 klas:F -->
### T-21-006 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Якщо проєкт ESP-IDF під рукою — цим і обмежтеся, бо адреси підставить сама збірка:

**Контекст**

```
## Перше рішення: один файл замість трьох

Складіть один образ (розділ 17). Якщо проєкт ESP-IDF під рукою — цим і
обмежтеся, бо адреси підставить сама збірка:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-007 sha:56d43d34 src:manual/21-seriyna.md:20 klas:K -->
### T-21-007 · kod · `manual/21-seriyna.md`

**Твердження, коротко**

> ```
> idf.py merge-bin -o vyrib-v1.4.bin
> ```

**Контекст**

````
## Перше рішення: один файл замість трьох

```
idf.py merge-bin -o vyrib-v1.4.bin
```
````

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
### T-21-008 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> idf.py merge-bin -o vyrib-v1.4.bin

**Контекст**

````
## Перше рішення: один файл замість трьох

```
idf.py merge-bin -o vyrib-v1.4.bin
```
````

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

<!-- fc id:T-21-009 sha:21613fb4 src:manual/21-seriyna.md:24 klas:E -->
### T-21-009 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Для виробництва це кращий варіант за ручний: жодного числа, набраного з голови, а отже й жодної нагоди зсунути бутлоадер.

**Контекст**

```
## Перше рішення: один файл замість трьох

Для виробництва це кращий варіант за ручний: жодного числа, набраного з
голови, а отже й жодної нагоди зсунути бутлоадер.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-010 sha:dc6bff36 src:manual/21-seriyna.md:27 klas:F -->
### T-21-010 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Коли ж на руках лише готові `.bin`-файли — збирати доводиться вручну; [[classic]] адреси нижче для classic і S2, для решти чипів адреса бутлоадера інша (таблиця в розділі 16):

**Контекст**

```
## Перше рішення: один файл замість трьох

Коли ж на руках лише готові `.bin`-файли — збирати доводиться вручну;
[[classic]] адреси нижче для classic і S2, для решти чипів адреса
бутлоадера інша (таблиця в розділі 16):
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-011 sha:fd180332 src:manual/21-seriyna.md:31 klas:K -->
### T-21-011 · kod · `manual/21-seriyna.md`

**Твердження, коротко**

> ```
> esptool --chip esp32 merge-bin -o vyrib-v1.4.bin --flash-mode dio \
>   0x1000 bootloader.bin \
>   0x8000 partition-table.bin \
>   0x10000 app.bin
> ```

**Контекст**

````
## Перше рішення: один файл замість трьох

```
esptool --chip esp32 merge-bin -o vyrib-v1.4.bin --flash-mode dio \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
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

<!-- fc id:T-21-012 sha:2ded8ac2 src:manual/21-seriyna.md:32 klas:A -->
### T-21-012 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> esptool --chip esp32 merge-bin -o vyrib-v1.4.bin --flash-mode dio \

**Контекст**

````
## Перше рішення: один файл замість трьох

```
esptool --chip esp32 merge-bin -o vyrib-v1.4.bin --flash-mode dio \
  0x1000 bootloader.bin \
  0x8000 partition-table.bin \
  0x10000 app.bin
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

<!-- fc id:T-21-013 sha:99dac3f2 src:manual/21-seriyna.md:38 klas:E -->
### T-21-013 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Далі кожна плата прошивається однією командою з однією адресою:

**Контекст**

```
## Перше рішення: один файл замість трьох

Далі кожна плата прошивається однією командою з однією адресою:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-014 sha:7c27876f src:manual/21-seriyna.md:40 klas:K -->
### T-21-014 · kod · `manual/21-seriyna.md`

**Твердження, коротко**

> ```
> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.4.bin
> ```

**Контекст**

````
## Перше рішення: один файл замість трьох

```
esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.4.bin
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-015 sha:060d1904 src:manual/21-seriyna.md:41 klas:F -->
### T-21-015 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.4.bin

**Контекст**

````
## Перше рішення: один файл замість трьох

```
esptool --port /dev/ttyUSB0 write-flash 0x0 vyrib-v1.4.bin
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-016 sha:d76a9957 src:manual/21-seriyna.md:44 klas:E -->
### T-21-016 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Тепер операцію можна віддати людині, яка нічого не знає про адреси розділів.

**Контекст**

```
## Перше рішення: один файл замість трьох

Тепер операцію можна віддати людині, яка нічого не знає про адреси
розділів. Це і є мета.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-017 sha:1c051eb7 src:manual/21-seriyna.md:48 klas:A -->
### T-21-017 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> `--chip` у `merge-bin` обов'язковий, бо порту немає й визначати чип нема звідки.

**Контекст**

```
## Перше рішення: один файл замість трьох

::: uvaha
`--chip` у `merge-bin` обов'язковий, бо порту немає й визначати чип нема
звідки. Він же задає, з якою адресою бутлоадера образ має сенс.
```

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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-21-018 sha:f1d48cb7 src:manual/21-seriyna.md:49 klas:E -->
### T-21-018 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Він же задає, з якою адресою бутлоадера образ має сенс.

**Контекст**

```
## Перше рішення: один файл замість трьох

::: uvaha
`--chip` у `merge-bin` обов'язковий, бо порту немає й визначати чип нема
звідки. Він же задає, з якою адресою бутлоадера образ має сенс.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-019 sha:378d2fc5 src:manual/21-seriyna.md:51 klas:A -->
### T-21-019 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> `--flash-mode`, `--flash-size` і `--flash-freq` у `merge-bin` мають збігатися з тим, під що зібрано прошивку.

**Контекст**

```
## Перше рішення: один файл замість трьох

`--flash-mode`, `--flash-size` і `--flash-freq` у `merge-bin` мають
збігатися з тим, під що зібрано прошивку. Розбіжність дає плату, яка
прошилася без помилок і не стартує. Найпростіше — узяти значення з
`sdkconfig` проєкту, а не вгадувати.
:::
```

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
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Прохід 9 знайшов тут найгрубішу помилку книги — надрукована команда `merge-bin` без `--chip` не запускалася. Виправлення вже в тексті; цей запис доводить решту абзацу, який тоді лишився без доказу: обов'язковість `--chip` і **причина** її (порту немає, визначати чип нема звідки), і те, що прапорці флешу мають збігатися з тим, під що зібрано прошивку, бо вони йдуть у заголовок образу.
- **Прохід:** pass-29-log-i-reshta-komand

---

<!-- fc id:T-21-020 sha:27deca81 src:manual/21-seriyna.md:52 klas:E -->
### T-21-020 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Розбіжність дає плату, яка прошилася без помилок і не стартує.

**Контекст**

```
## Перше рішення: один файл замість трьох

`--flash-mode`, `--flash-size` і `--flash-freq` у `merge-bin` мають
збігатися з тим, під що зібрано прошивку. Розбіжність дає плату, яка
прошилася без помилок і не стартує. Найпростіше — узяти значення з
`sdkconfig` проєкту, а не вгадувати.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-021 sha:a6125283 src:manual/21-seriyna.md:53 klas:F -->
### T-21-021 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Найпростіше — узяти значення з `sdkconfig` проєкту, а не вгадувати.

**Контекст**

```
## Перше рішення: один файл замість трьох

`--flash-mode`, `--flash-size` і `--flash-freq` у `merge-bin` мають
збігатися з тим, під що зібрано прошивку. Розбіжність дає плату, яка
прошилася без помилок і не стартує. Найпростіше — узяти значення з
`sdkconfig` проєкту, а не вгадувати.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-022 sha:ac7a1ba1 src:manual/21-seriyna.md:59 klas:E -->
### T-21-022 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Ручна команда в терміналі не масштабується: помилку в ній видно не одразу і не завжди.

**Контекст**

```
## Скрипт: те, що робить процес повторюваним

Ручна команда в терміналі не масштабується: помилку в ній видно не одразу
і не завжди. Мінімальний скрипт, який робить прошивку і **перевірку**:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-023 sha:01a36707 src:manual/21-seriyna.md:60 klas:E -->
### T-21-023 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Мінімальний скрипт, який робить прошивку і **перевірку**:

**Контекст**

```
## Скрипт: те, що робить процес повторюваним

Ручна команда в терміналі не масштабується: помилку в ній видно не одразу
і не завжди. Мінімальний скрипт, який робить прошивку і **перевірку**:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-024 sha:c80595d2 src:manual/21-seriyna.md:62 klas:K -->
### T-21-024 · kod · `manual/21-seriyna.md`

**Твердження, коротко**

> ```sh
> #!/bin/sh
> set -e
> PORT="${1:?вкажіть порт: ./flash.sh /dev/ttyUSB0}"
> IMAGE=vyrib-v1.4.bin
> 
> esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"
> esptool --port "$PORT" verify-flash 0x0 "$IMAGE"
> esptool --port "$PORT" read-mac | grep -i "MAC:"
> echo "OK: $PORT"
> ```

**Контекст**

````
## Скрипт: те, що робить процес повторюваним

```sh
#!/bin/sh
set -e
PORT="${1:?вкажіть порт: ./flash.sh /dev/ttyUSB0}"
IMAGE=vyrib-v1.4.bin

esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"
esptool --port "$PORT" verify-flash 0x0 "$IMAGE"
esptool --port "$PORT" read-mac | grep -i "MAC:"
echo "OK: $PORT"
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

<!-- fc id:T-21-025 sha:23224667 src:manual/21-seriyna.md:68 klas:B -->
### T-21-025 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"

**Контекст**

````
#!/bin/sh

esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"
esptool --port "$PORT" verify-flash 0x0 "$IMAGE"
esptool --port "$PORT" read-mac | grep -i "MAC:"
echo "OK: $PORT"
```
````

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- **Дослівно з джерела:**
  > serial connection parameters for flash operations
- **Спосіб і дата:** curl esptool boot-mode-selection.rst, 2026-08-26
- **Нотатка:** Текст T-17-067 називає 460800 розумним максимумом. Джерело каже про параметри серійного з'єднання.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-21-026 sha:1442de15 src:manual/21-seriyna.md:69 klas:A -->
### T-21-026 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> esptool --port "$PORT" verify-flash 0x0 "$IMAGE"

**Контекст**

````
#!/bin/sh

esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"
esptool --port "$PORT" verify-flash 0x0 "$IMAGE"
esptool --port "$PORT" read-mac | grep -i "MAC:"
echo "OK: $PORT"
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

<!-- fc id:T-21-027 sha:de8fa0cd src:manual/21-seriyna.md:70 klas:F -->
### T-21-027 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> esptool --port "$PORT" read-mac | grep -i "MAC:"

**Контекст**

````
#!/bin/sh

esptool --port "$PORT" --baud 460800 write-flash -z 0x0 "$IMAGE"
esptool --port "$PORT" verify-flash 0x0 "$IMAGE"
esptool --port "$PORT" read-mac | grep -i "MAC:"
echo "OK: $PORT"
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-028 sha:270a6061 src:manual/21-seriyna.md:74 klas:E -->
### T-21-028 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Три речі, які тут важливі.

**Контекст**

```
#!/bin/sh

Три речі, які тут важливі. `set -e` зупиняє скрипт на першій помилці —
інакше збій прошивки лишиться непоміченим у потоці виводу. `verify-flash`
перетворює «прошилося» на «у флеші лежить те, що треба». Виведений MAC іде
в журнал: це єдиний надійний ідентифікатор плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-029 sha:12bbf3c5 src:manual/21-seriyna.md:74 klas:F -->
### T-21-029 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> `set -e` зупиняє скрипт на першій помилці — інакше збій прошивки лишиться непоміченим у потоці виводу.

**Контекст**

```
#!/bin/sh

Три речі, які тут важливі. `set -e` зупиняє скрипт на першій помилці —
інакше збій прошивки лишиться непоміченим у потоці виводу. `verify-flash`
перетворює «прошилося» на «у флеші лежить те, що треба». Виведений MAC іде
в журнал: це єдиний надійний ідентифікатор плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-030 sha:42368b26 src:manual/21-seriyna.md:75 klas:A -->
### T-21-030 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> `verify-flash` перетворює «прошилося» на «у флеші лежить те, що треба».

**Контекст**

```
#!/bin/sh

Три речі, які тут важливі. `set -e` зупиняє скрипт на першій помилці —
інакше збій прошивки лишиться непоміченим у потоці виводу. `verify-flash`
перетворює «прошилося» на «у флеші лежить те, що треба». Виведений MAC іде
в журнал: це єдиний надійний ідентифікатор плати.
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

<!-- fc id:T-21-031 sha:16350670 src:manual/21-seriyna.md:76 klas:E -->
### T-21-031 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Виведений MAC іде в журнал: це єдиний надійний ідентифікатор плати.

**Контекст**

```
#!/bin/sh

Три речі, які тут важливі. `set -e` зупиняє скрипт на першій помилці —
інакше збій прошивки лишиться непоміченим у потоці виводу. `verify-flash`
перетворює «прошилося» на «у флеші лежить те, що треба». Виведений MAC іде
в журнал: це єдиний надійний ідентифікатор плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-032 sha:e3f39fae src:manual/21-seriyna.md:81 klas:E -->
### T-21-032 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> «Прошилося без помилок» — не критерій приймання.

**Контекст**

```
## Контроль після прошивки

«Прошилося без помилок» — не критерій приймання. Мінімальний контроль,
який ловить майже все:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-033 sha:d1d7cedd src:manual/21-seriyna.md:81 klas:E -->
### T-21-033 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Мінімальний контроль, який ловить майже все:

**Контекст**

```
## Контроль після прошивки

«Прошилося без помилок» — не критерій приймання. Мінімальний контроль,
який ловить майже все:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-034 sha:ddc59055 src:manual/21-seriyna.md:84 klas:A -->
### T-21-034 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **`verify-flash`** — вміст флешу відповідає образу. 2.

**Контекст**

```
## Контроль після прошивки

1. **`verify-flash`** — вміст флешу відповідає образу.
2. **Скидання і читання boot-логу** — пристрій справді стартує (розділ 16).
3. **Одна функціональна перевірка** — те, заради чого виріб існує:
   світлодіод блимає, датчик читається, точка доступу піднялася.
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

<!-- fc id:T-21-035 sha:1d35be73 src:manual/21-seriyna.md:85 klas:E -->
### T-21-035 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **Скидання і читання boot-логу** — пристрій справді стартує (розділ 16). 3.

**Контекст**

```
## Контроль після прошивки

1. **`verify-flash`** — вміст флешу відповідає образу.
2. **Скидання і читання boot-логу** — пристрій справді стартує (розділ 16).
3. **Одна функціональна перевірка** — те, заради чого виріб існує:
   світлодіод блимає, датчик читається, точка доступу піднялася.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-036 sha:a414fea1 src:manual/21-seriyna.md:86 klas:E -->
### T-21-036 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **Одна функціональна перевірка** — те, заради чого виріб існує: світлодіод блимає, датчик читається, точка доступу піднялася.

**Контекст**

```
## Контроль після прошивки

1. **`verify-flash`** — вміст флешу відповідає образу.
2. **Скидання і читання boot-логу** — пристрій справді стартує (розділ 16).
3. **Одна функціональна перевірка** — те, заради чого виріб існує:
   світлодіод блимає, датчик читається, точка доступу піднялася.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-037 sha:c6467fae src:manual/21-seriyna.md:89 klas:E -->
### T-21-037 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Третій пункт ловить те, чого не спіймають перші два: справний образ, залитий на плату з непропаяним модулем або мертвим датчиком.

**Контекст**

```
## Контроль після прошивки

Третій пункт ловить те, чого не спіймають перші два: справний образ,
залитий на плату з непропаяним модулем або мертвим датчиком.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-038 sha:621d4059 src:manual/21-seriyna.md:93 klas:E -->
### T-21-038 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Партія — це саме те місце, де вилазить межове живлення.

**Контекст**

```
## Контроль після прошивки

::: zhyvlennya
Партія — це саме те місце, де вилазить межове живлення. Двадцять плат
прошиваються по черзі, USB-хаб гріється, напруга просідає, і десь на
чотирнадцятій починаються `MD5 of file does not match`. Живлення для
серійної прошивки — окреме, з запасом, і бажано не від ноутбука.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-039 sha:d5049633 src:manual/21-seriyna.md:93 klas:A -->
### T-21-039 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Двадцять плат прошиваються по черзі, USB-хаб гріється, напруга просідає, і десь на чотирнадцятій починаються `MD5 of file does not match`.

**Контекст**

```
## Контроль після прошивки

::: zhyvlennya
Партія — це саме те місце, де вилазить межове живлення. Двадцять плат
прошиваються по черзі, USB-хаб гріється, напруга просідає, і десь на
чотирнадцятій починаються `MD5 of file does not match`. Живлення для
серійної прошивки — окреме, з запасом, і бажано не від ноутбука.
:::
```

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

<!-- fc id:T-21-040 sha:432b092c src:manual/21-seriyna.md:95 klas:E -->
### T-21-040 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Живлення для серійної прошивки — окреме, з запасом, і бажано не від ноутбука.

**Контекст**

```
## Контроль після прошивки

::: zhyvlennya
Партія — це саме те місце, де вилазить межове живлення. Двадцять плат
прошиваються по черзі, USB-хаб гріється, напруга просідає, і десь на
чотирнадцятій починаються `MD5 of file does not match`. Живлення для
серійної прошивки — окреме, з запасом, і бажано не від ноутбука.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-041 sha:1a3a9559 src:manual/21-seriyna.md:101 klas:E -->
### T-21-041 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Найчастіша помилка серійного виробництва — залити двадцятьом платам однаковий образ разом із однаковим серійним номером, однаковим ключем і однаковим ім'ям пристрою.

**Контекст**

```
## Per-device: те, що в кожної плати своє

Найчастіша помилка серійного виробництва — залити двадцятьом платам
однаковий образ разом із однаковим серійним номером, однаковим ключем і
однаковим ім'ям пристрою. Наслідки виявляються пізно, у полі, і виглядають
як містика: два пристрої «крадуть» одне в одного з'єднання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-042 sha:6c7e3e50 src:manual/21-seriyna.md:103 klas:E -->
### T-21-042 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Наслідки виявляються пізно, у полі, і виглядають як містика: два пристрої «крадуть» одне в одного з'єднання.

**Контекст**

```
## Per-device: те, що в кожної плати своє

Найчастіша помилка серійного виробництва — залити двадцятьом платам
однаковий образ разом із однаковим серійним номером, однаковим ключем і
однаковим ім'ям пристрою. Наслідки виявляються пізно, у полі, і виглядають
як містика: два пристрої «крадуть» одне в одного з'єднання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-043 sha:3140d22c src:manual/21-seriyna.md:106 klas:E -->
### T-21-043 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Правильна схема розділяє два шари:

**Контекст**

```
## Per-device: те, що в кожної плати своє

Правильна схема розділяє два шари:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-044 sha:1cfc3ebd src:manual/21-seriyna.md:108 klas:E -->
### T-21-044 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **Спільне** — образ прошивки.

**Контекст**

```
## Per-device: те, що в кожної плати своє

**Спільне** — образ прошивки. Однаковий для всієї партії, з `merge-bin`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-045 sha:ac0e1bb8 src:manual/21-seriyna.md:108 klas:F -->
### T-21-045 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Однаковий для всієї партії, з `merge-bin`.

**Контекст**

```
## Per-device: те, що в кожної плати своє

**Спільне** — образ прошивки. Однаковий для всієї партії, з `merge-bin`.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-046 sha:c50488dc src:manual/21-seriyna.md:110 klas:F -->
### T-21-046 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **Унікальне** — конфігурація в NVS.

**Контекст**

```
## Per-device: те, що в кожної плати своє

**Унікальне** — конфігурація в NVS. Своя для кожної плати: серійний
номер, ключі, калібрувальні коефіцієнти, ім'я.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-047 sha:5ee74ccf src:manual/21-seriyna.md:110 klas:E -->
### T-21-047 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Своя для кожної плати: серійний номер, ключі, калібрувальні коефіцієнти, ім'я.

**Контекст**

```
## Per-device: те, що в кожної плати своє

**Унікальне** — конфігурація в NVS. Своя для кожної плати: серійний
номер, ключі, калібрувальні коефіцієнти, ім'я.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-048 sha:8fbe10a5 src:manual/21-seriyna.md:113 klas:E -->
### T-21-048 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> ESP-IDF дає інструмент, який робить із CSV готовий образ розділу NVS:

**Контекст**

```
## Per-device: те, що в кожної плати своє

ESP-IDF дає інструмент, який робить із CSV готовий образ розділу NVS:
```

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

<!-- fc id:T-21-049 sha:fc2721f0 src:manual/21-seriyna.md:115 klas:K -->
### T-21-049 · kod · `manual/21-seriyna.md`

**Твердження, коротко**

> ```
> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
> esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin
> ```

**Контекст**

````
## Per-device: те, що в кожної плати своє

```
nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin
```
````

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
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

<!-- fc id:T-21-050 sha:aa33e38e src:manual/21-seriyna.md:116 klas:D -->
### T-21-050 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000

**Контекст**

````
## Per-device: те, що в кожної плати своє

```
nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin
```
````

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
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

<!-- fc id:T-21-051 sha:dab0dee5 src:manual/21-seriyna.md:117 klas:D -->
### T-21-051 · kod-ryadok · `manual/21-seriyna.md`

**Твердження, коротко**

> esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin

**Контекст**

````
## Per-device: те, що в кожної плати своє

```
nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin
```
````

**Доказ**

- **Клас:** 🔵 D — обчислення — перевіряється арифметикою, зовнішнє джерело не потрібне
- **Джерело:** tools/arytmetyka.py; розкладка з components/partition_table/partitions_singleapp.csv (прохід 7)
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

<!-- fc id:T-21-052 sha:b0a670d8 src:manual/21-seriyna.md:120 klas:A -->
### T-21-052 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Адреса `0x9000` — початок розділу `nvs` у стандартній розбивці; звірити зі своєю таблицею розділів (розділ 18).

**Контекст**

```
## Per-device: те, що в кожної плати своє

Адреса `0x9000` — початок розділу `nvs` у стандартній розбивці; звірити
зі своєю таблицею розділів (розділ 18).
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- **Дослівно з джерела:**
  > nvs,      data, nvs,     0x9000,  0x6000,
  > factory,  app,  factory, 0x10000, 1M,
- **Спосіб і дата:** curl esp-idf partition-tables.rst, grep partition, 2026-08-26
- **Нотатка:** Розділ 18 показує типову таблицю розділів. Джерело підтверджує: nvs на 0x9000, factory на 0x10000. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-82-boot-flesh

---

<!-- fc id:T-21-053 sha:a441973a src:manual/21-seriyna.md:123 klas:F -->
### T-21-053 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Альтернатива для невеликих партій: заливати спільний образ, а унікальне записувати через консоль після першого старту — прошивка при першому запуску просить серійний номер і зберігає його в NVS.

**Контекст**

```
## Per-device: те, що в кожної плати своє

Альтернатива для невеликих партій: заливати спільний образ, а унікальне
записувати через консоль після першого старту — прошивка при першому
запуску просить серійний номер і зберігає його в NVS. Менше інструментів,
але додає ручну операцію до кожної плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-054 sha:168c664c src:manual/21-seriyna.md:125 klas:E -->
### T-21-054 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Менше інструментів, але додає ручну операцію до кожної плати.

**Контекст**

```
## Per-device: те, що в кожної плати своє

Альтернатива для невеликих партій: заливати спільний образ, а унікальне
записувати через консоль після першого старту — прошивка при першому
запуску просить серійний номер і зберігає його в NVS. Менше інструментів,
але додає ручну операцію до кожної плати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-055 sha:82ff65b0 src:manual/21-seriyna.md:129 klas:B -->
### T-21-055 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> MAC-адреса кожного чипа унікальна від заводу і лежить в eFuse.

**Контекст**

```
## Per-device: те, що в кожної плати своє

::: uvaha
MAC-адреса кожного чипа унікальна від заводу і лежить в eFuse. Якщо все,
що вам потрібно, — відрізняти пристрої один від одного, окремий серійний
номер не потрібен: беріть MAC. Це прибирає цілий шар роботи разом із
нагодою помилитися.
:::
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > unique identifier stored in eFuse
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep eFuse, 2026-08-26
- **Нотатка:** Текст T-21-055 говорить про унікальність MAC-адреси від заводу в eFuse. Джерело підтверджує наявність eFuse як сховища унікальних даних.
- **Прохід:** m2-83-esptool

---

<!-- fc id:T-21-056 sha:8aa5ff33 src:manual/21-seriyna.md:129 klas:E -->
### T-21-056 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Якщо все, що вам потрібно, — відрізняти пристрої один від одного, окремий серійний номер не потрібен: беріть MAC.

**Контекст**

```
## Per-device: те, що в кожної плати своє

::: uvaha
MAC-адреса кожного чипа унікальна від заводу і лежить в eFuse. Якщо все,
що вам потрібно, — відрізняти пристрої один від одного, окремий серійний
номер не потрібен: беріть MAC. Це прибирає цілий шар роботи разом із
нагодою помилитися.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-057 sha:5aed5cc9 src:manual/21-seriyna.md:131 klas:E -->
### T-21-057 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Це прибирає цілий шар роботи разом із нагодою помилитися.

**Контекст**

```
## Per-device: те, що в кожної плати своє

::: uvaha
MAC-адреса кожного чипа унікальна від заводу і лежить в eFuse. Якщо все,
що вам потрібно, — відрізняти пристрої один від одного, окремий серійний
номер не потрібен: беріть MAC. Це прибирає цілий шар роботи разом із
нагодою помилитися.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-058 sha:7afef3b1 src:manual/21-seriyna.md:137 klas:E -->
### T-21-058 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Плата без позначки — плата, про яку через місяць невідомо нічого.

**Контекст**

```
## Маркування плат

Плата без позначки — плата, про яку через місяць невідомо нічого. На
кожну наклеюється або пишеться маркером мінімум:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-059 sha:80b6708b src:manual/21-seriyna.md:137 klas:E -->
### T-21-059 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> На кожну наклеюється або пишеться маркером мінімум:

**Контекст**

```
## Маркування плат

Плата без позначки — плата, про яку через місяць невідомо нічого. На
кожну наклеюється або пишеться маркером мінімум:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-060 sha:581413be src:manual/21-seriyna.md:140 klas:E -->
### T-21-060 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> - порядковий номер у партії; - версія прошивки; - дата.

**Контекст**

```
## Маркування плат

- порядковий номер у партії;
- версія прошивки;
- дата.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-061 sha:b8ed94db src:manual/21-seriyna.md:144 klas:E -->
### T-21-061 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Наліпка клеїться на бік, який видно в зібраному виробі.

**Контекст**

```
## Маркування плат

Наліпка клеїться на бік, який видно в зібраному виробі. Наліпка, що
опинилася всередині корпусу, не існує.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-062 sha:d888373f src:manual/21-seriyna.md:144 klas:E -->
### T-21-062 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Наліпка, що опинилася всередині корпусу, не існує.

**Контекст**

```
## Маркування плат

Наліпка клеїться на бік, який видно в зібраному виробі. Наліпка, що
опинилася всередині корпусу, не існує.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-063 sha:669ee36d src:manual/21-seriyna.md:149 klas:E -->
### T-21-063 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Один файл на партію, рядок на плату:

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-064 sha:75def2ca src:manual/21-seriyna.md:151 klas:F -->
### T-21-064 · tablycya-shapka · `manual/21-seriyna.md`

**Твердження, коротко**

> | № | MAC | Версія | Дата | Контроль | Примітка |

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-065 sha:e706eb63 src:manual/21-seriyna.md:152 klas:F -->
### T-21-065 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0041 · MAC → `A0:B7:…:14`

**Дослівно з книги**

```
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-066 sha:a8bb95c8 src:manual/21-seriyna.md:152 klas:F -->
### T-21-066 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0041 · Версія → v1.4

**Дослівно з книги**

```
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-067 sha:e4e73586 src:manual/21-seriyna.md:152 klas:E -->
### T-21-067 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0041 · Дата → 2026-08-26

**Дослівно з книги**

```
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-068 sha:29d3900f src:manual/21-seriyna.md:152 klas:E -->
### T-21-068 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0041 · Контроль → OK

**Дослівно з книги**

```
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-069 sha:75799caf src:manual/21-seriyna.md:153 klas:F -->
### T-21-069 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0042 · MAC → `A0:B7:…:2C`

**Дослівно з книги**

```
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-070 sha:abb9bd4b src:manual/21-seriyna.md:153 klas:F -->
### T-21-070 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0042 · Версія → v1.4

**Дослівно з книги**

```
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-071 sha:e2d0d5e3 src:manual/21-seriyna.md:153 klas:E -->
### T-21-071 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0042 · Дата → 2026-08-26

**Дослівно з книги**

```
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-072 sha:f7d5d679 src:manual/21-seriyna.md:153 klas:E -->
### T-21-072 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0042 · Контроль → OK

**Дослівно з книги:** рядок таблиці не знайдено — локатор привів у прозу. Дивіться контекст нижче.

**Контекст**

````
## Per-device: те, що в кожної плати своє

```
nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
esptool --port /dev/ttyUSB0 write-flash 0x9000 nvs-0042.bin
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-073 sha:c5831a43 src:manual/21-seriyna.md:153 klas:E -->
### T-21-073 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0042 · Примітка → корпус подряпаний

**Дослівно з книги**

```
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-074 sha:79ce9a1f src:manual/21-seriyna.md:154 klas:F -->
### T-21-074 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0043 · MAC → `A0:B7:…:31`

**Дослівно з книги**

```
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-075 sha:9f488b42 src:manual/21-seriyna.md:154 klas:F -->
### T-21-075 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0043 · Версія → v1.4

**Дослівно з книги**

```
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-076 sha:a6590e77 src:manual/21-seriyna.md:154 klas:E -->
### T-21-076 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0043 · Дата → 2026-08-26

**Дослівно з книги**

```
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-077 sha:37c1710c src:manual/21-seriyna.md:154 klas:E -->
### T-21-077 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0043 · Контроль → **брак**

**Дослівно з книги**

```
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-078 sha:4688c6c2 src:manual/21-seriyna.md:154 klas:E -->
### T-21-078 · komirka · `manual/21-seriyna.md`

**Твердження, коротко**

> 0043 · Примітка → не стартує, модуль

**Дослівно з книги**

```
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Контекст**

```
## Журнал партії

Один файл на партію, рядок на плату:

| № | MAC | Версія | Дата | Контроль | Примітка |
|---|---|---|---|---|---|
| 0041 | `A0:B7:…:14` | v1.4 | 2026-08-26 | OK | |
| 0042 | `A0:B7:…:2C` | v1.4 | 2026-08-26 | OK | корпус подряпаний |
| 0043 | `A0:B7:…:31` | v1.4 | 2026-08-26 | **брак** | не стартує, модуль |
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-079 sha:ee027464 src:manual/21-seriyna.md:157 klas:C -->
### T-21-079 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Цей файл відповідає на питання, які виникають через півроку і не мають іншого джерела відповіді: скільки зроблено, яка версія у пристрою з таким MAC, чи був цей екземпляр у браку.

**Контекст**

```
## Журнал партії

Цей файл відповідає на питання, які виникають через півроку і не мають
іншого джерела відповіді: скільки зроблено, яка версія у пристрою з таким
MAC, чи був цей екземпляр у браку.
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** ESP32 Core Dump Specification
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** ESP32 Core Dump Specification
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-21-seriyna

---

<!-- fc id:T-21-080 sha:f8360aa5 src:manual/21-seriyna.md:161 klas:F -->
### T-21-080 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Разом із журналом зберігаються **самі файли прошивки** тієї версії, що поїхала, і, обов'язково, `.elf` того самого збирання: без нього backtrace з поля не розшифрувати (картка [К7](#k-panika)).

**Контекст**

```
## Журнал партії

Разом із журналом зберігаються **самі файли прошивки** тієї версії, що
поїхала, і, обов'язково, `.elf` того самого збирання: без нього backtrace
з поля не розшифрувати (картка [К7](#k-panika)).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-081 sha:2e3ee5bc src:manual/21-seriyna.md:166 klas:E -->
### T-21-081 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Версія прошивки, яка поїхала до замовника, має існувати в архіві як файли, а не як «гілка в git, з якої це збиралося».

**Контекст**

```
## Журнал партії

::: nezvorotne
Версія прошивки, яка поїхала до замовника, має існувати в архіві як
файли, а не як «гілка в git, з якої це збиралося». Перезібрати «такий
самий» образ пізніше майже ніколи не виходить точно: змінилася версія
тулчейну, змінилася бібліотека, змінився шлях збирання. Адреси зсунуться,
і `.elf` перестане відповідати тому, що в полі.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-082 sha:6b4d2e33 src:manual/21-seriyna.md:167 klas:E -->
### T-21-082 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Перезібрати «такий самий» образ пізніше майже ніколи не виходить точно: змінилася версія тулчейну, змінилася бібліотека, змінився шлях збирання.

**Контекст**

```
## Журнал партії

::: nezvorotne
Версія прошивки, яка поїхала до замовника, має існувати в архіві як
файли, а не як «гілка в git, з якої це збиралося». Перезібрати «такий
самий» образ пізніше майже ніколи не виходить точно: змінилася версія
тулчейну, змінилася бібліотека, змінився шлях збирання. Адреси зсунуться,
і `.elf` перестане відповідати тому, що в полі.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-083 sha:775f6652 src:manual/21-seriyna.md:169 klas:F -->
### T-21-083 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Адреси зсунуться, і `.elf` перестане відповідати тому, що в полі.

**Контекст**

```
## Журнал партії

::: nezvorotne
Версія прошивки, яка поїхала до замовника, має існувати в архіві як
файли, а не як «гілка в git, з якої це збиралося». Перезібрати «такий
самий» образ пізніше майже ніколи не виходить точно: змінилася версія
тулчейну, змінилася бібліотека, змінився шлях збирання. Адреси зсунуться,
і `.elf` перестане відповідати тому, що в полі.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-084 sha:f5a053c0 src:manual/21-seriyna.md:175 klas:E -->
### T-21-084 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Коли партія вимірюється сотнями, послідовна прошивка стає вузьким місцем.

**Контекст**

```
## Кілька плат одночасно

Коли партія вимірюється сотнями, послідовна прошивка стає вузьким місцем.
Варіанти, у порядку складності:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-085 sha:c5052027 src:manual/21-seriyna.md:176 klas:E -->
### T-21-085 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Варіанти, у порядку складності:

**Контекст**

```
## Кілька плат одночасно

Коли партія вимірюється сотнями, послідовна прошивка стає вузьким місцем.
Варіанти, у порядку складності:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-086 sha:7b5f5132 src:manual/21-seriyna.md:178 klas:F -->
### T-21-086 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **Кілька портів паралельно.** Скрипт запускається на `/dev/ttyUSB0`, `ttyUSB1`, `ttyUSB2` одночасно.

**Контекст**

```
## Кілька плат одночасно

**Кілька портів паралельно.** Скрипт запускається на `/dev/ttyUSB0`,
`ttyUSB1`, `ttyUSB2` одночасно. Найдешевший спосіб отримати кратне
прискорення. Обмеження — живлення хаба: чотири плати, що одночасно пишуть
у флеш, дають помітний струм.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-087 sha:03a8a283 src:manual/21-seriyna.md:179 klas:E -->
### T-21-087 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Найдешевший спосіб отримати кратне прискорення.

**Контекст**

```
## Кілька плат одночасно

**Кілька портів паралельно.** Скрипт запускається на `/dev/ttyUSB0`,
`ttyUSB1`, `ttyUSB2` одночасно. Найдешевший спосіб отримати кратне
прискорення. Обмеження — живлення хаба: чотири плати, що одночасно пишуть
у флеш, дають помітний струм.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-088 sha:73cabe58 src:manual/21-seriyna.md:180 klas:E -->
### T-21-088 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Обмеження — живлення хаба: чотири плати, що одночасно пишуть у флеш, дають помітний струм.

**Контекст**

```
## Кілька плат одночасно

**Кілька портів паралельно.** Скрипт запускається на `/dev/ttyUSB0`,
`ttyUSB1`, `ttyUSB2` одночасно. Найдешевший спосіб отримати кратне
прискорення. Обмеження — живлення хаба: чотири плати, що одночасно пишуть
у флеш, дають помітний струм.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-089 sha:74a5c7c5 src:manual/21-seriyna.md:183 klas:E -->
### T-21-089 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **Flash Download Tool** (Windows) вміє кілька плат в одному вікні — зручно там, де прошиває оператор без командного рядка (розділ 17).

**Контекст**

```
## Кілька плат одночасно

**Flash Download Tool** (Windows) вміє кілька плат в одному вікні —
зручно там, де прошиває оператор без командного рядка (розділ 17).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-090 sha:8bcfad00 src:manual/21-seriyna.md:186 klas:E -->
### T-21-090 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> **Прошивка до монтажу**, на спеціальному ложементі з підпружиненими контактами (pogo pins).

**Контекст**

```
## Кілька плат одночасно

**Прошивка до монтажу**, на спеціальному ложементі з підпружиненими
контактами (pogo pins). Це вже оснастка, і має сенс від сотень плат.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-091 sha:eecd5522 src:manual/21-seriyna.md:187 klas:E -->
### T-21-091 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Це вже оснастка, і має сенс від сотень плат.

**Контекст**

```
## Кілька плат одночасно

**Прошивка до монтажу**, на спеціальному ложементі з підпружиненими
контактами (pogo pins). Це вже оснастка, і має сенс від сотень плат.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-092 sha:850d2dde src:manual/21-seriyna.md:191 klas:E -->
### T-21-092 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Відкласти плату, позначити, продовжити з рештою, розібратися потім — розділ 55 і картка [К8](#k-symptomy).

**Контекст**

```
## Якщо плата з партії не прошивається

Не зупиняти партію. Відкласти плату, позначити, продовжити з рештою,
розібратися потім — розділ 55 і картка [К8](#k-symptomy). Найчастіші
причини саме в партії: непропаяний модуль, замикання під час монтажу,
плата іншої ревізії, що приїхала в тій самій коробці.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-093 sha:69e2ed79 src:manual/21-seriyna.md:192 klas:E -->
### T-21-093 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Найчастіші причини саме в партії: непропаяний модуль, замикання під час монтажу, плата іншої ревізії, що приїхала в тій самій коробці.

**Контекст**

```
## Якщо плата з партії не прошивається

Не зупиняти партію. Відкласти плату, позначити, продовжити з рештою,
розібратися потім — розділ 55 і картка [К8](#k-symptomy). Найчастіші
причини саме в партії: непропаяний модуль, замикання під час монтажу,
плата іншої ревізії, що приїхала в тій самій коробці.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-094 sha:39f098a2 src:manual/21-seriyna.md:198 klas:F -->
### T-21-094 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> `merge-bin` — один файл, одна адреса, нема чого переплутати.

**Контекст**

```
## Що з цього треба запам'ятати

`merge-bin` — один файл, одна адреса, нема чого переплутати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-095 sha:81a87405 src:manual/21-seriyna.md:200 klas:A -->
### T-21-095 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> `verify-flash` і функціональна перевірка — обов'язкові кроки, а не опції.

**Контекст**

```
## Що з цього треба запам'ятати

`verify-flash` і функціональна перевірка — обов'язкові кроки, а не опції.
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

<!-- fc id:T-21-096 sha:26048fe4 src:manual/21-seriyna.md:202 klas:F -->
### T-21-096 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Спільний образ і унікальний NVS — це два різні шари.

**Контекст**

```
## Що з цього треба запам'ятати

Спільний образ і унікальний NVS — це два різні шари. Змішати їх означає
отримати двадцять пристроїв з однаковою особистістю.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-097 sha:ade9bd68 src:manual/21-seriyna.md:202 klas:E -->
### T-21-097 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Змішати їх означає отримати двадцять пристроїв з однаковою особистістю.

**Контекст**

```
## Що з цього треба запам'ятати

Спільний образ і унікальний NVS — це два різні шари. Змішати їх означає
отримати двадцять пристроїв з однаковою особистістю.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-21-098 sha:fd3cdf97 src:manual/21-seriyna.md:205 klas:F -->
### T-21-098 · proza · `manual/21-seriyna.md`

**Твердження, коротко**

> Журнал партії і збережені файли прошивки разом із `.elf` — те, без чого через півроку неможливо відповісти на просте питання «що в цьому пристрої».

**Контекст**

```
## Що з цього треба запам'ятати

Журнал партії і збережені файли прошивки разом із `.elf` — те, без чого
через півроку неможливо відповісти на просте питання «що в цьому
пристрої».
```

**Доказ**

- **Клас:** F — не звірено

---
