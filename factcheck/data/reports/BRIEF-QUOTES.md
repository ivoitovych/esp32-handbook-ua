# Наряд: 60 цитат, яких немає в джерелі

**Генерується** `tools/work_orders.py`. Питання **не** про цитату.

Третій шар уже сказав, що цитати за адресою немає. Причина відома і
здебільшого та сама: супровідник **причепурив** цитату — скоротив
`{IDF_TARGET_STRAP_BOOT_2_GPIO}` до `{STRAP_BOOT_2_GPIO}`, зібрав рядок
таблиці рукою, переставив відступи. Це брак реєстру, і його виправляє
супровідник.

**Твоє питання інше й важливіше: чи правильне те, що написано в книзі.**

Цитата може бути причесана, а факт — правильний. Може бути й навпаки:
причесування іноді ховає те, що джерело каже щось інше. Книга йде в
друк, тож нас цікавить саме другий випадок.

This is a printed field handbook. Its reader has no network and no time
to check anything. Our job is to put every factual claim in it beside an
external document that supports it — and to record where we looked.

Your answer does not go into the book. It goes through three layers:

1. **Mechanical.** An address pointing at the handbook itself is
   rejected. A verdict with no source is rejected as "did not look".
2. **Literal.** Every `quote` is searched for **as a substring** in the
   document you named — we fetch it again and check. Spaces and quote
   marks do not count; words, numbers and capitals do.
3. **Human.** A maintainer reads the extract and judges whether it
   actually supports the claim.

Layer 2 is not a formality. In one earlier wave, of **528** claimed
confirmations only **235** survived it. The other 293 died as
paraphrase, as fragments glued across an ellipsis, or as a correct fact
with the wrong file's address.

Everything in `quote` is checked as a substring of the document. A
retelling does not pass. Neither does a line you assembled by hand from
a table, nor two sentences joined across an ellipsis.

**Knowing the answer is not grounds for writing a quote.** If the fact is
familiar but you cannot see the line in the document, that is
`not_found`.

**Paste the line with its markup. Do not clean it up.** This is the one
that costs most, because it does not feel like an error. The document
says

    Print registers and reboot (``CONFIG_ESP_SYSTEM_PANIC_PRINT_REBOOT``) — default option

and the tidy version — `Print registers and reboot — default option` —
is the same fact, reads better, and **fails**. So does dropping a
`:doc:` role, a trailing underscore on a link, or the brackets around an
option name. Measured over 200 tickets: of the confirmations that
failed, 13 of 14 had found the right passage and lost it in the copying.

Copy the characters that are there — backticks, colons, brackets,
underscores and all. If two useful sentences are not adjacent, send two
entries or one entry and say so; do not join them.

It is not a failure and not a lesser result. It records where we have
already looked, and those records are what let us print a sentence at
all.

A quote from an almost-right source is worse than no quote. Invented
support does not go unnoticed — layer 2 discards it and the unit returns
to the queue — so guessing is cheaper than reading only inside your own
answer. Past that boundary it costs everyone, and you most: your work
disappears entirely.

Only `raw.githubusercontent.com`, via `curl`. Everything else answers
`403` — this is an organisation-level policy, not your doing and not
ours. Chip datasheets are not on GitHub, and that is nobody's fault.

**Do not repeat a request that returned 403.**

Some `espressif.com` addresses return an **HTML placeholder of about
15 500 bytes with status 200**. The request "succeeds" and there is no
document. If what came back does not look like the document you asked
for, the verdict is `unreachable`.

Used when the unit already carries a class and the question is whether
that class is right.

| Verdict | When |
|---|---|
| `confirmed` | the existing class is correct |
| `disputes` | the source contradicts the handbook |
| `truly_none` | there really is no external referent: this is the author's position |
| `not_found` | you could not tell — say what you read |

An address inside this repository, or a chapter of the handbook cited as
the source for a claim in the handbook, is rejected mechanically. If a
claim is supported only by another part of the book, say so plainly —
there is a class for it, and it is not a failure.

```yaml
- unit: T-42-023
  verdict: confirmed
  source: https://raw.githubusercontent.com/espressif/esp-idf/master/...
  quote: |
    the verbatim line from the document
  comment: one sentence, optional
```

One entry per unit. Do not reorder or renumber the units. If you have
nothing for a unit, still write an entry with the honest verdict — a
missing entry is indistinguishable from work not done.

**YAML:** if a value contains `: ` or starts with a quote mark, wrap the
whole value in single quotes. Otherwise the file will not parse and the
whole batch is lost, not just that entry.

---

*Task spec `0a35a92e` · blocks: ORIENTATION, VERBATIM, HONEST-MISS, NETWORK, STUB, VERDICTS-VERDICT-TEST, NO-SELF-REFERENCE, FORMAT. Quote this version when reporting results from this wave.*

## Пакет 1

**`m2-01-esp32-datasheet-iomux`** · Розпіновка JTAG classic — datasheet як друге джерело до io_mux_reg.h

- джерело: https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf — ESP32 Series Datasheet v5.3, розділ 2.2 «Pin Overview», Table 2-1 «Pin Overview», с. 14-15
- у книзі шукати за взірцем: `\| TMS \| `GPIO14` \||\| TCK \| `GPIO13` \|`
- третій шар: 1 з 8 рядків

**`m2-62-bootlog-k06`** · T-K06-045: На 115200 нічого, на 74880 осмислений текст — це ESP8266

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `74880.*осмислений текст.*ESP8266`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flash`** · Етап 1 — ROM bootloader зашитий у кремній

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `Етап 1.*ROM bootloader.*кремній`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flash`** · Етап 2 — другий бутлоадер bootloader.bin у флеші

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `Етап 2.*другий бутлоадер.*bootloader`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flash`** · Адреса bootloader.bin для ESP32 чипів — 0x1000

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `Останнє\s+тягне\s+за\s+собою\s+перерахунок\s+явних\s+зсувів\s+у\s+CSV:\s+жоден\s+розділ\s+не\s+може\s+починатися\s+раніше\s+ніж\s+нова\s+адреса|\[\[classic\]\]\s+Адреса\s+`0x1000`\s+тут\s+—\s+знову\s+`
- третій шар: 1 з 1 рядків


## Пакет 2

**`m2-82-boot-flash`** · GPIO0 як ключовий strapping-пін для вибору режиму завантаження

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``GPIO0`\s+·\s+Що\s+задає\s+→\s+звичайний\s+старт\s+або\s+download\s+mode|\|\s+`DOWNLOAD_BOOT\(UART0/UART1/\.\.\.\)`\s+\|\s+download\s+mode,\s+`GPIO0`\s+низький\s+\||GPIO0\s+→\s+білий\s+→\s+кнопка\s+на`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flash`** · Розділи ota_0 та ota_1 у таблиці розділів для OTA

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- у книзі шукати за взірцем: ``ota_0`.*`ota_1``
- третій шар: 2 з 2 рядків

**`m2-83-esptool`** · esptool версія v4 та v5 у ESP-IDF

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `v4.*v5|esptool.*version`
- третій шар: 2 з 2 рядків

**`m2-83-esptool`** · Адреса bootloader.bin для ESP32 — 0x1000

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `0x1000.*classic|адреса.*0x1000`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Адреса merge-bin завжди на 0x0 незалежно від конфігурації

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `0x0.*незалежно`
- третій шар: 1 з 1 рядків


## Пакет 3

**`m2-83-esptool`** · Таблиця розділів за замовчуванням на адресі 0x8000

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- у книзі шукати за взірцем: `partition.*table.*0x8000`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · MAC-адреса унікальна від заводу і лежить в eFuse

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `MAC-адреса.*унікальна.*eFuse`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Команда esptool flash-id додає інформацію про флеш

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `flash-id.*шапка`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Максимальна швидкість baudu для більшості мостів 460800

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `460800`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Розміри флешу 2 МБ або 4 МБ для ESP32 модулів

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- у книзі шукати за взірцем: `2.*МБ|4.*МБ`
- третій шар: 1 з 1 рядків


## Пакет 4

**`m2-84-freertos`** · Пріоритет задачі від 0 до configMAX_PRIORITIES мінус 1

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `0.*configMAX_PRIORITIES|пріоритет.*0`
- третій шар: 2 з 2 рядків

**`m2-84-freertos`** · Core 0 (PRO_CPU) переважно займає радіостек, Core 1 (APP_CPU) — застосунок

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `Core.*0.*Core.*1|APP_CPU|PRO_CPU`
- третій шар: 3 з 3 рядків

**`m2-84-freertos`** · Функції FromISR єдині дозволені в обробнику переривання

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `FromISR|обробнику переривання`
- третій шар: 1 з 1 рядків

**`m2-84-freertos`** · Бітові прапори WIFI_OK та TIME_OK в event group

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `WIFI_OK|TIME_OK|BIT0|BIT1`
- третій шар: 1 з 1 рядків

**`m2-84-freertos`** · Реле на GPIO при зависанні переходить в безпечний стан

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- у книзі шукати за взірцем: `реле.*GPIO|зависанні`
- третій шар: 1 з 1 рядків


## Пакет 5

**`m2-93-sample`** · Код 0x10 означає RTCWDT_RTC_RESET (RTC watchdog скинув усе)

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/fatal-errors.rst — ESP-IDF, розділ «RTC Watchdog Timeout» (рядок 306)
- у книзі шукати за взірцем: `\\| `0x10` \\|\\| RTCWDT_RTC_RESET \\|\\| RTC watchdog скинув усе`
- третій шар: 2 з 5 рядків

**`nosignal-02-chipy`** · T-02-105: Але зроблене без збереження `sdkconfig.defaults` доведеться налаштовувати заново.

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/build-system.rst
- у книзі шукати за взірцем: `Але\s+зроблене\s+без\s+збереження`
- третій шар: 1 з 1 рядків

**`pass-01-tverde-yadro`** · Перевірка переповнення стека і розмір стека app_main

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/Kconfig
- у книзі шукати за взірцем: `configCHECK_FOR_STACK_OVERFLOW|canary|3\.5 КБ|3584`
- третій шар: 3 з 8 рядків

**`pass-02-povedinka`** · На C3 ADC2 непридатний через апаратну ваду, а не через Wi-Fi

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/adc_oneshot.rst
- у книзі шукати за взірцем: `ADC2 на C3 непридатний|разовий режим не підтримується`
- третій шар: 1 з 3 рядків

**`pass-08-strapping`** · Strapping-піни за сімействами

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `strapping.{0,120}`GPIO0`|`GPIO0`, `GPIO2`, `GPIO5`, `GPIO12`, `GPIO15`|`GPIO9` притиснутий|`GPIO8` при цьому|`GPIO46``
- третій шар: 2 з 6 рядків


## Пакет 6

**`pass-10-povidomlennya`** · Розбіжність обсягу флешу — два різні рядки й різні наслідки

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/spi_flash/esp_flash_spi_init.c
- у книзі шукати за взірцем: `Detected size|smaller than the size in the binary image header|Probe failed|Using the size in the binary image header|Реальний флеш \*\*менший\*\*`
- третій шар: 3 з 3 рядків

**`pass-10-povidomlennya`** · Помилки купи розрізняють бік переповнення

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- у книзі шукати за взірцем: `CORRUPT HEAP|Bad tail|Bad head|канарки|stack overflow in task X has been detected`
- третій шар: 2 з 2 рядків

**`pass-11-menuconfig`** · Дерево menuconfig — корінь і Component config

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- у книзі шукати за взірцем: `Serial flasher config|Partition Table`|Component config` → `ESP System Settings|Component config` → `Core dump|Component config` → `ESP PSRAM|Три перші пункти меню`
- третій шар: 9 з 13 рядків

**`pass-12-piny`** · GPIO15 низький глушить boot-лог ROM

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `глушить лог ROM|вимикає boot-лог ROM|чи друкує ROM boot-лог|silences boot messages`
- третій шар: 2 з 3 рядків

**`pass-16-interfeysy`** · Режими SPI — CPHA задає номер фронту, не напрямок

- джерело: https://raw.githubusercontent.com/adafruit/Adafruit-ST7735-Library/master/Adafruit_ST7789.h та .../Adafruit_ST7789.cpp, https://raw.githubusercontent.com/jgromes/RadioLib/master/src/BuildOpt.h
- у книзі шукати за взірцем: `по \*\*першому\*\* фронту|по \*\*другому\*\*|котрому за ліком|режими 0 і 3 читають по\s*одному й тому самому фронту|режими 1 і 2|починати треба з пари 0 і 3|0 або 3`
- третій шар: 1 з 3 рядків


## Пакет 7

**`pass-17-simeystva-proektiv`** · pioarduino, а не офіційна платформа PlatformIO

- джерело: https://raw.githubusercontent.com/pioarduino/platform-espressif32/main/README.md та .../55.03.311/platform.json
- у книзі шукати за взірцем: `pioarduino/platform-espressif32/releases/download|Чому в рядку `platform` посилання|Офіційна платформа PlatformIO лишилася на Arduino 2\.x`
- третій шар: 1 з 5 рядків

**`pass-18-schemy`** · Підтягування I²C — діапазон, а не одне число

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/i2c.rst
- у книзі шукати за взірцем: `ESP-IDF\s*рекомендує \*\*2–5 кОм\*\*|що вища частота, то менший резистор|не менше 1 кОм`
- третій шар: 2 з 5 рядків

**`pass-20-jtag-obvyazka`** · Кольорова обв'язка прикладів — classic і тільки classic

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32/include/soc/soc_caps.h (маски дійсних пінів) + `tools/pins.py`
- у книзі шукати за взірцем: `GPIO\d+\s+→ (?:синій|зелений|жовтий|білий|червоний|чорний)|→ датчик DS18B20, лінія DATA|→ дисплей SSD1306`
- третій шар: 1 з 1 рядків

**`pass-26-strapping`** · Рівні strapping і недійсна комбінація — усі сімейства

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``GPIO2` низький або вільний|`GPIO46` низький або вільний|`GPIO8` \*\*високим\*\*|`GPIO8` = 0\s*\n?і `GPIO9` = 0 недійсна|другий пін ігнорується|Комбінація `GPIO8` = 0`
- третій шар: 6 з 12 рядків

**`pass-26-strapping`** · Маска GPIO_STRAP — усі шість бітів classic і два біти решти

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``0x0[1248]`=`GPIO|`0x[12]0`=`GPIO|\| `0x0[1248]` \| `GPIO|\| `0x[12]0` \| `GPIO|Найцінніший біт — `0x20`|На решті сімейств маска коротша|обрано непідтримуваний режим|DOWNLOAD_BOOT\(UART0|DOWNLOAD\(USB`
- третій шар: 3 з 21 рядків


## Пакет 8

**`pass-28-komandy-suciljno`** · flash-id як засіб упізнати перемаркований модуль

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst та .../advanced-commands.rst
- у книзі шукати за взірцем: ``flash-id` називає обсяг|`flash-id` показує 2 МБ`
- третій шар: 4 з 4 рядків

**`pass-28-komandy-suciljno`** · erase-flash стирає весь чип, включно з NVS і калібруванням

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst
- у книзі шукати за взірцем: ``erase-flash` знищує NVS|Після `erase-flash` або перепрошивки|Після `erase-flash` нічого немає|`erase-flash` — тільки після дампа|За адресою `0x8000` порожньо`
- третій шар: 1 з 6 рядків

**`pass-28-komandy-suciljno`** · merge-bin дає один образ на адресу 0x0 незалежно від сімейства

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst (merge-bin) та .../esp-idf/docs/en/api-guides/tools/idf-py.rst
- у книзі шукати за взірцем: `зібраний `merge-bin` · [^→]+→ `0x0`|адреса завжди `0x0`, незалежно від сімейства|Зібрано \*\*один образ\*\* через `merge-bin`|Є лише `\.bin`-файли — `esptool --chip … merge-bin``
- третій шар: 4 з 5 рядків

**`pass-29-log-i-reshta-komand`** · Рядки помилок з'єднання — Failed to connect і сусіди

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/troubleshooting.rst
- у книзі шукати за взірцем: ``Failed to connect`|`Invalid head of packet`|`Device or resource busy`|`Permission denied`|шукати варто за початком рядка`
- третій шар: 3 з 3 рядків

**`pass-29-log-i-reshta-komand`** · Паніка, backtrace і watchdog — назви рядків у логу

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_system/panic.c, .../components/esp_system/task_wdt/task_wdt.c, .../docs/en/api-guides/fatal-errors.rst
- у книзі шукати за взірцем: ``Guru Meditation`|\*\*`Backtrace`\*\*|`Interrupt wdt timeout`|`Task watchdog got triggered`|дамп регістрів, слово `Guru Meditation``
- третій шар: 2 з 3 рядків


## Пакет 9

**`pass-29-log-i-reshta-komand`** · esptool і stub, автоскидання, розбіжність чипа

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst, .../advanced-topics/boot-mode-selection.rst (Automatic Bootloader)
- у книзі шукати за взірцем: `вантажить у RAM невелику допоміжну програму|визначив чип сам і побачив розбіжність|смикає ці лінії в потрібній послідовності|застосунок, який сам щось пише в UART`
- третій шар: 5 з 5 рядків

**`pass-29-log-i-reshta-komand`** · merge-bin — прапорці флешу і призначення формату

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-commands.rst
- у книзі шукати за взірцем: ``--chip` у `merge-bin` обов.язковий|`--flash-mode`, `--flash-size` і `--flash-freq`|склеює їх в один образ, у якому зсуви вже всередині|формат передачі прошивки людині|Адреси всередині `merge-bin` маю`
- третій шар: 4 з 9 рядків

**`pass-30-piny-suciljno`** · Функції strapping-пінів classic — таблиця розділу 07 поштучно

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``GPIO0` · Що задає|`GPIO0` · Наслідок помилки|`GPIO12` · Наслідок помилки|`GPIO2` · Що задає|`GPIO2` · Наслідок помилки|`GPIO15` · Наслідок помилки|`GPIO5` · Що задає|`GPIO12` · Що задає|`GPIO15` · Що`
- третій шар: 4 з 10 рядків

**`pass-30-piny-suciljno`** · Піни флешу, тільки-вхідні й ADC1 при Wi-Fi

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32/include/soc/spi_pins.h, .../components/soc/esp32/include/soc/adc_channel.h, .../components/soc/esp32/include/soc/soc_caps.h, .../docs/en/api-reference/peripherals/gpio.rst
- у книзі шукати за взірцем: `GPIO 6–11 не працюють ·|GPIO 6–11 нічого не роблять|Не чіпати GPIO 6, 7, 8, 9, 10, 11|Піни флешу\*\* \[\[classic\]\] GPIO 6–11 зайняті фізично|Тільки-вхідні піни\*\* \[\[classic\]\] GPIO 34–39|Кнопка `
- третій шар: 5 з 5 рядків

**`pass-30-piny-suciljno`** · Вхід у download mode вручну — порядок і його причина

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst (Select Bootloader Mode, Automatic Bootloader)
- у книзі шукати за взірцем: `Вирішує `GPIO0`:|`GPIO0` вільний \(підтягнутий вгору\)|Кнопка `BOOT` \(іноді `IO0`, `FLASH`\)|стан `GPIO0` читається один раз|схема, що смикає `GPIO0` і `EN`|перемичкою або пінцетом замкнути `GPIO0`|К`
- третій шар: 4 з 7 рядків


## Пакет 10

**`pass-30-piny-suciljno`** · I²C і strapping на C3 — підтяжки збігаються з потрібними рівнями

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../esp-idf/components/soc/esp32c3/include/soc/adc_channel.h
- у книзі шукати за взірцем: `зовнішні підтягувальні резистори I²C тягнуть обидві лінії вгору|ведений, що притискає `SDA` до землі|Комбінація `GPIO8`=0 і `GPIO9`=0 недійсна|аналоговий вхід — це `GPIO0`–`GPIO4``
- третій шар: 4 з 6 рядків

**`pass-31-adresy-i-api`** · ESP_ERROR_CHECK — це assert, а не обробка помилок

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- у книзі шукати за взірцем: ``ESP_ERROR_CHECK` — це `assert`|викликає паніку й перезавантажує чип|`ESP_ERROR_CHECK` навколо|`ESP_ERROR_CHECK` доречний там|Замінити `ESP_ERROR_CHECK` на явну обробку|повертає `esp_err_t` — код поми`
- третій шар: 2 з 15 рядків

**`pass-31-adresy-i-api`** · ESP_LOGD не коштує нічого при рівні збирання Info

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h та .../docs/en/api-reference/system/log.html.rst
- у книзі шукати за взірцем: ``ESP_LOGD` у гарячому циклі не коштує нічого|рядки `ESP_LOGD` лишаються у флеші|Логувати переходи станів|`ESP_LOGI\(TAG, "тут"\)` не каже нічого`
- третій шар: 6 з 6 рядків

**`pass-31-adresy-i-api`** · Коди помилок OTA і NVS, які книга називає поіменно

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/app_update/include/esp_ota_ops.h, .../components/esp_common/include/esp_err.h, .../docs/en/api-reference/storage/{wear-levelling,fatfs}.rst
- у книзі шукати за взірцем: ``ESP_ERR_OTA_VALIDATE_FAILED`|`ESP_ERR_OTA_PARTITION_CONFLICT`|`ESP_ERR_INVALID_ARG` при налаштуванні|`wear_levelling`|`esp_vfs_fat``
- третій шар: 2 з 6 рядків

**`pass-32-pul-shmatky-1-3`** · DAC, ADC-затухання й обв'язка входу — розділ 33

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- у книзі шукати за взірцем: `Канал 1 → `GPIO25`|Канал 2 → `GPIO26`|Канал 1 → `GPIO17`|Канал 2 → `GPIO18`|з максимальним затуханням доступний майже весь|\*\*Конденсатор\*\* 100 нФ від входу до землі|На classic `GPIO8` брати не мож`
- третій шар: 8 з 11 рядків


## Пакет 11

**`pass-32-pul-shmatky-1-3`** · Рівні логу, esp_err_to_name і монітор — розділ 25

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/Kconfig.level, .../components/esp_common/include/esp_err.h, .../components/esp_driver_i2c/include/driver/i2c_master.h, .../docs/en/api-guides/tools/idf-monitor.rst
- у книзі шукати за взірцем: ``Default log verbosity` \| рівень, з яким прошивка стартує|`esp_err_to_name` перетворює число на читабельне|в лозі буде `0x105`|розшифровує backtrace\*\* у назви функцій`
- третій шар: 1 з 10 рядків

**`pass-32-pul-shmatky-1-3`** · Типова розбивка флешу — зсуви, розміри й суфікси

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та .../components/bootloader_support/src/bootloader_utility.c
- у книзі шукати за взірцем: ``nvs` · Зсув → `0x9000`|`nvs` · Розмір → `0x6000`|`phy_init` · Розмір → `0x1000`|застосунок іде на `0x10000`|Розмір записується числом|Адреса `0x9000` — початок розділу `nvs`|Таблиця розділів лежить н`
- третій шар: 3 з 11 рядків

**`pass-32-pul-shmatky-1-3`** · Буфер у PSRAM без MALLOC_CAP_SPIRAM — і що це коштує

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/system/mem_alloc.rst, .../docs/en/api-guides/external-ram.rst, .../components/esp_common/include/esp_attr.h, .../components/freertos/Kconfig.freertos
- у книзі шукати за взірцем: `буфер на 64 КБ опиниться в PSRAM \*\*без\*\* жодного `MALLOC_CAP_SPIRAM`|`DRAM_ATTR`|Вимикати цю перевірку \(`No checking`\)`
- третій шар: 5 з 11 рядків

**`pass-33-pul-shmatky-4-5`** · Strapping classic і C3 — таблиця розділу 07 проти gpio/*.inc

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/gpio/esp32c3.inc та https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `C3: `GPIO2`, `GPIO8`, `GPIO9`|Головний пін → `GPIO0` = 0|Головний пін → `GPIO9` = 0|Другий пін для входу в бутлоадер → `GPIO8` \*\*високий\*\*|недійсна комбінація» існує лише в правому стовпці`
- третій шар: 1 з 3 рядків

**`pass-34-pul-shmatok-6`** · erase-flash, flash-id і коли стирання справді потрібне

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-commands.rst, .../docs/en/migration-guide.rst, https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/storage/nvs_flash.rst
- у книзі шукати за взірцем: ``erase-flash` знищує \*\*весь\*\* флеш|`flash-id` показує те, що каже сама мікросхема|залишки старої розбивки заважають новій таблиці|Перевірити версію `esptool` \*\*перш ніж\*\*`
- третій шар: 1 з 12 рядків


## Пакет 12

**`pass-34-pul-shmatok-6`** · Автоскидання не працює — перелік причин, крім однієї

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../docs/en/troubleshooting.rst
- у книзі шукати за взірцем: `схема, що смикає `GPIO0` і `EN` сигналами `DTR`/`RTS`|плата без такої схеми взагалі|живлення просідає під час скидання`
- третій шар: 2 з 9 рядків

**`pass-35-vlasna-pomylka-boot`** · Коди RESET_REASON — уся таблиця причин скидання

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- у книзі шукати за взірцем: `Числові коди з ROM-заголовка ESP-IDF \(enum `RESET_REASON`\)|POWERON_RESET \| подано живлення|SW_CPU_RESET \| програмне скидання ядра|RTCWDT_BROWN_OUT_RESET \| \*\*просіло живлення\*\*`
- третій шар: 1 з 19 рядків

**`pass-35-vlasna-pomylka-boot`** · ROM класифікує boot: значення цілком, а не пін за піном

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32c3/include/soc/boot_mode.h
- у книзі шукати за взірцем: `Далі значення не розшифровуються, і це свідоме рішення|ETS_IS_FLASH_BOOT|дивіться на рядок у дужках`
- третій шар: 1 з 7 рядків

**`pass-45-sdkconfig-defaults`** · sdkconfig.defaults рекомендовано тримати в системі контролю версій

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/build-system.rst
- у книзі шукати за взірцем: `Саме він\s+має лежати в git`
- третій шар: 1 з 1 рядків

**`sweep-17-esptool`** · T-17-118: Друга половина рядка залежить від версії.

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py
- у книзі шукати за взірцем: `Друга\s+половина\s+рядка\s+залежить`
- третій шар: 1 з 1 рядків

