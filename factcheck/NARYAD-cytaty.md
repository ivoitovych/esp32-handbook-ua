# Наряд: 50 цитат, яких немає в джерелі

**Генерується** `tools/naryad.py`. Питання **не** про цитату.

Третій шар уже сказав, що цитати за адресою немає. Причина відома і
здебільшого та сама: супровідник **причепурив** цитату — скоротив
`{IDF_TARGET_STRAP_BOOT_2_GPIO}` до `{STRAP_BOOT_2_GPIO}`, зібрав рядок
таблиці рукою, переставив відступи. Це брак реєстру, і його виправляє
супровідник.

**Твоє питання інше й важливіше: чи правильне те, що написано в книзі.**

Цитата може бути причесана, а факт — правильний. Може бути й навпаки:
причесування іноді ховає те, що джерело каже щось інше. Книга йде в
друк, тож нас цікавить саме другий випадок.

По кожному запису:

1. завантаж джерело (`curl` на `raw.githubusercontent.com`);
2. знайди місце, про яке йдеться;
3. відповідай **одним із трьох**:

| Вердикт | Коли |
|---|---|
| `pidtverdzheno` | джерело каже те саме; наведи **дослівний** рядок звідти |
| `sperechayetsya` | джерело каже **інакше** — це знахідка, опиши точно |
| `ne_vyrishyv` | джерело недосяжне або місця не знайшов |

`sperechayetsya` — те, заради чого це робиться. Не бійся його ставити:
книгу ще можна виправити. Але став його, лише коли **бачиш** інший
текст, а не коли пам'ятаєш інакше.

Цитату копіюй дослівно: вона перевіряється підрядком.

**YAML:** якщо значення містить `: ` або починається з лапки — бери все
значення в одинарні лапки.

Формат:

```yaml
- zapys: pass-26-strapping
  nazva: Рівні strapping і недійсна комбінація — усі сімейства
  verdykt: pidtverdzheno
  dzherelo: https://raw.githubusercontent.com/...
  cytata: |
    дослівний рядок із джерела
  komentar: одне речення
```

## Пакет 1

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

**`pass-09-komandy`** · merge-bin вимагає --chip; без нього команда падає

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-options.rst
- у книзі шукати за взірцем: `--chip esp32 merge-bin|`--chip` тут \*\*обов.язковий\*\*|Specify the --chip argument`
- третій шар: 2 з 7 рядків

**`pass-09-komandy`** · Стиснення при передачі ввімкнене за замовчуванням

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py та .../docs/en/esptool/basic-commands.rst
- у книзі шукати за взірцем: `\*\*Уже ввімкнене\*\*|стиснення ввімкнене \*\*за замовчуванням\*\*|`-u` \| вимкнути стиснення`
- третій шар: 2 з 10 рядків


## Пакет 2

**`pass-10-povidomlennya`** · Розбіжність обсягу флешу — два різні рядки й різні наслідки

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/spi_flash/esp_flash_spi_init.c
- у книзі шукати за взірцем: `Detected size|smaller than the size in the binary image header|Probe failed|Using the size in the binary image header|Реальний флеш \*\*менший\*\*`
- третій шар: 3 з 3 рядків

**`pass-10-povidomlennya`** · Помилки купи розрізняють бік переповнення

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/heap/multi_heap_poisoning.c та .../freertos/FreeRTOS-Kernel/portable/xtensa/port.c
- у книзі шукати за взірцем: `CORRUPT HEAP|Bad tail|Bad head|канарки|stack overflow in task X has been detected`
- третій шар: 2 з 2 рядків

**`pass-10-povidomlennya`** · Тексти помилок esptool змінилися між версіями

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/{loader,cmds}.py та https://raw.githubusercontent.com/espressif/esptool/v4.8.1/esptool/loader.py
- у книзі шукати за взірцем: `No serial data received|Failed to start stub flasher|This chip is ESP32-S3, not ESP32|Wrong chip argument|MD5 of file does not match|Stub flasher has been disabled`
- третій шар: 6 з 8 рядків

**`pass-11-menuconfig`** · Дерево menuconfig — корінь і Component config

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/Kconfig та components/{esptool_py,partition_table,bootloader}/Kconfig.projbuild, components/{esp_system,espcoredump,esp_psram,log,bt,freertos}/Kconfig
- у книзі шукати за взірцем: `Serial flasher config|Partition Table`|Component config` → `ESP System Settings|Component config` → `Core dump|Component config` → `ESP PSRAM|Три перші пункти меню`
- третій шар: 9 з 13 рядків

**`pass-12-piny`** · GPIO15 низький глушить boot-лог ROM

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `глушить лог ROM|вимикає boot-лог ROM|чи друкує ROM boot-лог|silences boot messages`
- третій шар: 2 з 3 рядків


## Пакет 3

**`pass-16-interfeysy`** · Режими SPI — CPHA задає номер фронту, не напрямок

- джерело: https://raw.githubusercontent.com/adafruit/Adafruit-ST7735-Library/master/Adafruit_ST7789.h та .../Adafruit_ST7789.cpp, https://raw.githubusercontent.com/jgromes/RadioLib/master/src/BuildOpt.h
- у книзі шукати за взірцем: `по \*\*першому\*\* фронту|по \*\*другому\*\*|котрому за ліком|режими 0 і 3 читають по\s*одному й тому самому фронту|режими 1 і 2|починати треба з пари 0 і 3|0 або 3`
- третій шар: 1 з 3 рядків

**`pass-17-simeystva-proektiv`** · pioarduino, а не офіційна платформа PlatformIO

- джерело: https://raw.githubusercontent.com/pioarduino/platform-espressif32/main/README.md та .../55.03.311/platform.json
- у книзі шукати за взірцем: `pioarduino/platform-espressif32/releases/download|Чому в рядку `platform` посилання|Офіційна платформа PlatformIO лишилася на Arduino 2\.x`
- третій шар: 1 з 5 рядків

**`pass-18-schemy`** · Підтягування I²C — діапазон, а не одне число

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/i2c.rst
- у книзі шукати за взірцем: `ESP-IDF\s*рекомендує \*\*2–5 кОм\*\*|що вища частота, то менший резистор|не менше 1 кОм`
- третій шар: 2 з 5 рядків

**`pass-20-jtag-obvyazka`** · Кольорова обв'язка прикладів — classic і тільки classic

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32/include/soc/soc_caps.h (маски дійсних пінів) + `tools/piny.py`
- у книзі шукати за взірцем: `GPIO\d+\s+→ (?:синій|зелений|жовтий|білий|червоний|чорний)|→ датчик DS18B20, лінія DATA|→ дисплей SSD1306`
- третій шар: 1 з 1 рядків

**`pass-24-zsuvy-i-matrycya`** · Зсув бутлоадера по сімействах — числа праві, причина хибна

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild та .../docs/en/api-guides/startup.rst; https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32*.py
- у книзі шукати за взірцем: `ESP32 classic, ESP32-S2 \| `0x1000`|ESP32-S3, C3, C6, H2 \| `0x0`|ESP32-P4, C5, H4 \| `0x2000`|Secure Boot v1\*\*; коли secure boot|менеджерові ключів апаратного шифрування`
- третій шар: 14 з 21 рядків


## Пакет 4

**`pass-24-zsuvy-i-matrycya`** · Таблиця розділів — 0xC00 і 95 записів; 0x7000 належить бутлоадерові

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst, .../docs/en/api-guides/bootloader.rst, .../components/partition_table/Kconfig.projbuild
- у книзі шукати за взірцем: `не більше 95 записів|максимум \*\*95 записів\*\*|`0xC00`|too large for partition table offset|Простір бутлоадера — це проміжок`
- третій шар: 8 з 18 рядків

**`pass-24-zsuvy-i-matrycya`** · Піновий план проєкту 60 — обидва сімейства

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32c3}/include/soc/adc_channel.h, .../components/soc/{esp32,esp32c3}/include/soc/spi_pins.h, .../components/soc/esp32c3/include/soc/soc_caps.h
- у книзі шукати за взірцем: `ADC дільника · (classic|C3) →|Ключ дільника \(вихід\) · (classic|C3) →|SPI `SCK` / `MOSI` / `MISO` · (classic|C3) →|SPI `CS` microSD · (classic|C3) →|Четвірка `18`/`23`/`19`/`5` на classic|ADC_CHANNEL`
- третій шар: 8 з 17 рядків

**`pass-26-strapping`** · Рівні strapping і недійсна комбінація — усі сімейства

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``GPIO2` низький або вільний|`GPIO46` низький або вільний|`GPIO8` \*\*високим\*\*|`GPIO8` = 0\s*\n?і `GPIO9` = 0 недійсна|другий пін ігнорується|Комбінація `GPIO8` = 0`
- третій шар: 6 з 12 рядків

**`pass-26-strapping`** · Маска GPIO_STRAP — усі шість бітів classic і два біти решти

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``0x0[1248]`=`GPIO|`0x[12]0`=`GPIO|\| `0x0[1248]` \| `GPIO|\| `0x[12]0` \| `GPIO|Найцінніший біт — `0x20`|На решті сімейств маска коротша|обрано непідтримуваний режим|DOWNLOAD_BOOT\(UART0|DOWNLOAD\(USB`
- третій шар: 3 з 21 рядків

**`pass-28-komandy-suciljno`** · Іменування й версії esptool — version, esptool.py, дефіси проти підкреслень

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst та .../docs/en/migration-guide.rst; перелік команд у esptool/__init__.py
- у книзі шукати за взірцем: `esptool version`|esptool\.py version`|виклик · v[45] →|Версія `esptool` залежить не від вашого вибору|у v4 інакшого імені немає`
- третій шар: 4 з 4 рядків


## Пакет 5

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


## Пакет 6

**`pass-29-log-i-reshta-komand`** · esptool і stub, автоскидання, розбіжність чипа

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst, .../advanced-topics/boot-mode-selection.rst (Automatic Bootloader)
- у книзі шукати за взірцем: `вантажить у RAM невелику допоміжну програму|визначив чип сам і побачив розбіжність|смикає ці лінії в потрібній послідовності|застосунок, який сам щось пише в UART`
- третій шар: 5 з 5 рядків

**`pass-29-log-i-reshta-komand`** · merge-bin — прапорці флешу і призначення формату

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py (merge_bin_cli) та .../docs/en/esptool/basic-commands.rst
- у книзі шукати за взірцем: ``--chip` у `merge-bin` обов.язковий|`--flash-mode`, `--flash-size` і `--flash-freq`|склеює їх в один образ, у якому зсуви вже всередині|формат передачі прошивки людині|Адреси всередині `merge-bin` маю`
- третій шар: 4 з 9 рядків

**`pass-29-log-i-reshta-komand`** · Роль esptool і послідовність дій із незнайомою платою

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/index.rst та .../esptool/basic-commands.rst
- у книзі шукати за взірцем: `програма, що розмовляє з ROM-бутлоадером|це буде через `esptool`|`chip-id` і `flash-id` — перші дві команди|`read-flash` робиться до першої зміни|Дамп \(`read-flash`\) робиться \*\*до\*\*|доки чип від`
- третій шар: 2 з 2 рядків

**`pass-30-piny-suciljno`** · Функції strapping-пінів classic — таблиця розділу 07 поштучно

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``GPIO0` · Що задає|`GPIO0` · Наслідок помилки|`GPIO12` · Наслідок помилки|`GPIO2` · Що задає|`GPIO2` · Наслідок помилки|`GPIO15` · Наслідок помилки|`GPIO5` · Що задає|`GPIO12` · Що задає|`GPIO15` · Що`
- третій шар: 4 з 10 рядків

**`pass-30-piny-suciljno`** · Піни флешу, тільки-вхідні й ADC1 при Wi-Fi

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32/include/soc/spi_pins.h, .../components/soc/esp32/include/soc/adc_channel.h, .../components/soc/esp32/include/soc/soc_caps.h, .../docs/en/api-reference/peripherals/gpio.rst
- у книзі шукати за взірцем: `GPIO 6–11 не працюють ·|GPIO 6–11 нічого не роблять|Не чіпати GPIO 6, 7, 8, 9, 10, 11|Піни флешу\*\* \[\[classic\]\] GPIO 6–11 зайняті фізично|Тільки-вхідні піни\*\* \[\[classic\]\] GPIO 34–39|Кнопка `
- третій шар: 5 з 5 рядків


## Пакет 7

**`pass-30-piny-suciljno`** · Вхід у download mode вручну — порядок і його причина

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst (Select Bootloader Mode, Automatic Bootloader)
- у книзі шукати за взірцем: `Вирішує `GPIO0`:|`GPIO0` вільний \(підтягнутий вгору\)|Кнопка `BOOT` \(іноді `IO0`, `FLASH`\)|стан `GPIO0` читається один раз|схема, що смикає `GPIO0` і `EN`|перемичкою або пінцетом замкнути `GPIO0`|К`
- третій шар: 4 з 7 рядків

**`pass-30-piny-suciljno`** · I²C і strapping на C3 — підтяжки збігаються з потрібними рівнями

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../esp-idf/components/soc/esp32c3/include/soc/adc_channel.h
- у книзі шукати за взірцем: `зовнішні підтягувальні резистори I²C тягнуть обидві лінії вгору|ведений, що притискає `SDA` до землі|Комбінація `GPIO8`=0 і `GPIO9`=0 недійсна|аналоговий вхід — це `GPIO0`–`GPIO4``
- третій шар: 4 з 6 рядків

**`pass-31-adresy-i-api`** · Таблиці адрес прошивки — три рядки на три сімейства

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader/Kconfig.projbuild, .../components/partition_table/Kconfig.projbuild, .../docs/en/api-guides/partition-tables.rst
- у книзі шукати за взірцем: `bootloader · [^→]+→ `0x[12]000`|`bootloader\.bin` · [^→]+→ `0x[12]000`|partition table · [^→]+→ `0x8000`|`partition-table\.bin` · [^→]+→ `0x8000`|застосунок[^→]*· [^→]+→ `0x10000`|`nvs` \(типово\) · [`
- третій шар: 3 з 9 рядків

**`pass-31-adresy-i-api`** · ESP_ERROR_CHECK — це assert, а не обробка помилок

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- у книзі шукати за взірцем: ``ESP_ERROR_CHECK` — це `assert`|викликає паніку й перезавантажує чип|`ESP_ERROR_CHECK` навколо|`ESP_ERROR_CHECK` доречний там|Замінити `ESP_ERROR_CHECK` на явну обробку|повертає `esp_err_t` — код поми`
- третій шар: 2 з 15 рядків

**`pass-31-adresy-i-api`** · ESP_LOGD не коштує нічого при рівні збирання Info

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h та .../docs/en/api-reference/system/log.html.rst
- у книзі шукати за взірцем: ``ESP_LOGD` у гарячому циклі не коштує нічого|рядки `ESP_LOGD` лишаються у флеші|Логувати переходи станів|`ESP_LOGI\(TAG, "тут"\)` не каже нічого`
- третій шар: 6 з 6 рядків


## Пакет 8

**`pass-31-adresy-i-api`** · Коди помилок OTA і NVS, які книга називає поіменно

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/app_update/include/esp_ota_ops.h, .../components/esp_common/include/esp_err.h, .../docs/en/api-reference/storage/{wear-levelling,fatfs}.rst
- у книзі шукати за взірцем: ``ESP_ERR_OTA_VALIDATE_FAILED`|`ESP_ERR_OTA_PARTITION_CONFLICT`|`ESP_ERR_INVALID_ARG` при налаштуванні|`wear_levelling`|`esp_vfs_fat``
- третій шар: 2 з 6 рядків

**`pass-32-pul-shmatky-1-3`** · DAC, ADC-затухання й обв'язка входу — розділ 33

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-reference/peripherals/dac.rst, .../adc_calibration.rst, .../peripherals/gpio/esp32.inc
- у книзі шукати за взірцем: `Канал 1 → `GPIO25`|Канал 2 → `GPIO26`|Канал 1 → `GPIO17`|Канал 2 → `GPIO18`|з максимальним затуханням доступний майже весь|\*\*Конденсатор\*\* 100 нФ від входу до землі|На classic `GPIO8` брати не мож`
- третій шар: 8 з 11 рядків

**`pass-32-pul-shmatky-1-3`** · LISTEN_ONLY і NO_ACK — режими TWAI дослівно

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/hal/include/hal/twai_types_deprecated.h та .../docs/en/api-reference/peripherals/twai.rst
- у книзі шукати за взірцем: `TWAI_MODE_LISTEN_ONLY|TWAI_MODE_NO_ACK|не порада для акуратних, а спосіб не зіпсувати чужу шину|правильний спосіб знайомитися з чужою шиною|Трансивер обов.язковий`
- третій шар: 2 з 7 рядків

**`pass-32-pul-shmatky-1-3`** · Рівні логу, esp_err_to_name і монітор — розділ 25

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/Kconfig.level, .../components/esp_common/include/esp_err.h, .../components/esp_driver_i2c/include/driver/i2c_master.h, .../docs/en/api-guides/tools/idf-monitor.rst
- у книзі шукати за взірцем: ``Default log verbosity` \| рівень, з яким прошивка стартує|`esp_err_to_name` перетворює число на читабельне|в лозі буде `0x105`|розшифровує backtrace\*\* у назви функцій`
- третій шар: 4 з 10 рядків

**`pass-32-pul-shmatky-1-3`** · Типова розбивка флешу — зсуви, розміри й суфікси

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/partition-tables.rst та .../components/bootloader_support/src/bootloader_utility.c
- у книзі шукати за взірцем: ``nvs` · Зсув → `0x9000`|`nvs` · Розмір → `0x6000`|`phy_init` · Розмір → `0x1000`|застосунок іде на `0x10000`|Розмір записується числом|Адреса `0x9000` — початок розділу `nvs`|Таблиця розділів лежить н`
- третій шар: 3 з 11 рядків


## Пакет 9

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

**`pass-34-pul-shmatok-6`** · Автоскидання не працює — перелік причин, крім однієї

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst та .../docs/en/troubleshooting.rst
- у книзі шукати за взірцем: `схема, що смикає `GPIO0` і `EN` сигналами `DTR`/`RTS`|плата без такої схеми взагалі|живлення просідає під час скидання`
- третій шар: 2 з 9 рядків

**`pass-35-vlasna-pomylka-boot`** · Коди RESET_REASON — уся таблиця причин скидання

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_rom/esp32/include/esp32/rom/rtc.h
- у книзі шукати за взірцем: `Числові коди з ROM-заголовка ESP-IDF \(enum `RESET_REASON`\)|POWERON_RESET \| подано живлення|SW_CPU_RESET \| програмне скидання ядра|RTCWDT_BROWN_OUT_RESET \| \*\*просіло живлення\*\*`
- третій шар: 1 з 19 рядків


## Пакет 10

**`pass-35-vlasna-pomylka-boot`** · ROM класифікує boot: значення цілком, а не пін за піном

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32c3/include/soc/boot_mode.h
- у книзі шукати за взірцем: `Далі значення не розшифровуються, і це свідоме рішення|ETS_IS_FLASH_BOOT|дивіться на рядок у дужках`
- третій шар: 1 з 7 рядків

**`pass-36-chip-id`** · chip-id на сімействі ESP32 повертає попередження, а не Chip ID

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/esptool/cmds.py, .../esptool/loader.py, .../esptool/targets/esp8266.py
- у книзі шукати за взірцем: `Чому не `chip-id`|успадкована від ESP8266, у якого справді був окремий Chip ID|has no chip ID\. Reading MAC address instead|`chip_id`, `flash_id``
- третій шар: 10 з 17 рядків

**`pass-38-pul-shmatky-9-11`** · Драйвер I²C називає причину в консолі, а не мовчить

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_driver_i2c/i2c_master.c, .../components/esp_common/include/esp_check.h, .../Kconfig
- у книзі шукати за взірцем: `i2c_new_master_bus\(1049\): invalid SDA/SCL pin number|називає причину в консолі|мовчазним воно\s*\n?стає лише тоді`
- третій шар: 2 з 7 рядків

**`pass-38-pul-shmatky-9-11`** · ESP_DRAM_LOGx — єдиний виняток із заборони логувати в ISR

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/log/include/esp_log.h
- у книзі шукати за взірцем: `ESP_DRAM_LOGE|переривання вимкнені або всередині ISR|DRAM_STR\("mij_teg"\)`
- третій шар: 2 з 5 рядків

**`pass-38-pul-shmatky-9-11`** · На RISC-V рядка Backtrace немає — його будує монітор

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/docs/en/api-guides/fatal-errors.rst
- у книзі шукати за взірцем: `рядка `Backtrace:` у дампі немає\s*\n?взагалі|CONFIG_ESP_SYSTEM_USE_EH_FRAME|розмір\s*\n?образу росте на 20–100`
- третій шар: 2 з 12 рядків

