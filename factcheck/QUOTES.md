# Третій шар: цитати проти джерел

**Генерується** `tools/citaty.py --zvit`. Правити вручну нема сенсу.

Перевірено механічно: чи справді уривок, наведений у доказі, стоїть за
названою адресою. Це **не** оцінка того, чи доказ доречний — це окреме
питання, і його вирішує людина.

| Стан | Означає |
|---|---|
| `звірено` | усі придатні уривки знайдено в джерелі дослівно |
| `не знайдено` | уривка в джерелі немає — переказ, помилка адреси або джерело змінилося |
| `джерело не в кеші` | нема з чим звіряти: `--kachaty`, або егрес не пускає |
| `нема чого звіряти` | доказ без URL або без дослівного уривка (клас `C`, `E`, `K`) |
| `джерело вигадане` | клас `A` чи `B`, а в полі джерела — міркування, не документ |
| `у кеші заглушка` | сервер віддав HTML із кодом 200 замість PDF |
| `звірено очима` | витягання тексту руйнує структуру; звірив супровідник, причина названа |

Записів доказів: **1337**. Звірено дослівно: **381**. Не знайдено: **95**. Джерело не в кеші: **161**. Нема чого звіряти: **670**.

Станом на 2026-08-28 15:45 UTC.


## **хибний запис** — 6

| Доказ | Файл | Деталі |
|---|---|---|
| Модуль без стабілізатора: логічні рівні 3.3 В, під'єднувати прямо | `m2-93-vybirka` | доказ класу F — F означає відсутність доказу |
| Застосунок з Wi-Fi і TLS займає від 1 МБ | `m2-97-vybirka` | доказ класу F — F означає відсутність доказу |
| Модулі мають власний стабілізатор, але мікросхема працює від 3.3 В | `m2-97-vybirka` | доказ класу F — F означає відсутність доказу |
| Сучасні роутери часто розділяють SSID для діапазонів; ESP32 не бачить 5 ГГц | `m2-97-vybirka` | доказ класу F — F означає відсутність доказу |
| Літієві батареї не заряджаються нижче 0 °C і втрачають ємність на морозі | `m2-97-vybirka` | доказ класу F — F означає відсутність доказу |
| Прошивка з Wi-Fi, TLS та веб-інтерфейсом займає близько 1.5 МБ | `m2-97-vybirka` | доказ класу F — F означає відсутність доказу |

## клас E на твердженні з числом — перевірити — 24

| Доказ | Файл | Деталі |
|---|---|---|
| Живлення 5 В і виводи 3.3 В на одному модулі — загальна можливість, не вимірюваний факт | `m2-20-rivni-i-klyuchi` | клас E, а в назві число з одиницею |
| Живлення 3.3 В без сприйняття 3.3 В як одиниці — та сама логічна можливість | `m2-20-rivni-i-klyuchi` | клас E, а в назві число з одиницею |
| «USB-роз'єм... стабілізатор... 3.3 В» — топологія плати розробки, не факт із datasheet кристала | `m2-21-zhyvlennya-06` | клас E, а в назві число з одиницею |
| «Сюди можна подавати 5 В (залежить від стабілізатора на платі)» — явно позначена залежність від конкретної плати | `m2-21-zhyvlennya-06` | клас E, а в назві число з одиницею |
| Релейний модуль з оптопарою — 5 В і інверсна логіка не паспортні | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| Конвертер рівнів на польових — призначення 3.3↔5 В | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| Buck-boost 3.3 В — призначення «автономний пристрій» | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| Buck-boost і резистори 4.7 кОм — кількість і службова примітка в BOM | `m2-23-proekty-60-62` | клас E, а в назві число з одиницею |
| Модуль реле — коло котушки на окремих 5 В, а не 3V3 (без конкретної мікросхеми) | `m2-23-proekty-60-62` | клас E, а в назві число з одиницею |
| Резистори 220 Ом і 10 кОм модуля реле й поплавка — кількість у BOM | `m2-23-proekty-60-62` | клас E, а в назві число з одиницею |
| HC-SR04 — дільник напруги 10кОм + 20кОм | `m2-28-sensory-45` | клас E, а в назві число з одиницею |
| Конденсатор 470 мкФ між 3V3 і GND поруч із модулем | `m2-31-kartka-k13` | клас E, а в назві число з одиницею |
| Керамічний 100 нФ біля кожної мікросхеми | `m2-31-kartka-k13` | клас E, а в назві число з одиницею |
| Живлення 3.3 В напряму, мимо бортовий LDO — коли він слабкий на клоне | `m2-31-kartka-k13` | клас E, а в назві число з одиницею |
| Проблема: низька напруга живлення — додати 470 мкФ конденсатор | `m2-45-motory-symptomy` | клас E, а в назві число з одиницею |
| Wi-Fi відвалюється: подивитися RSSI гірше за −80 дБм | `m2-48-symptomy-29` | клас E, а в назві число з одиницею |
| T-K12-007: Паяльник повинен мати терморегулятор, потужність 60 Вт, жало «скіс» 2–3 мм | `m2-50-kartky` | клас E, а в назві число з одиницею |
| Конденсатор 100–470 мкФ біля живлення — стабілізація напруги | `m2-65-elektronika-05` | клас E, а в назві число з одиницею |
| MOSFET затвор — резистор 100–220 Ом від GPIO, захист від перегріву | `m2-65-elektronika-05` | клас E, а в назві число з одиницею |
| MOSFET затвор — резистор 10 кОм від затвора до землі, утримання LOW при старті | `m2-65-elektronika-05` | клас E, а в назві число з одиницею |
| T-36-120: SPI діагностика — знизити швидкість до 1 МГц | `m2-92-vybirka` | клас E, а в назві число з одиницею |
| T-59-114: 16 КБ з купи замість локального масиву | `m2-94-vybirka` | клас E, а в назві число з одиницею |
| T-60-123: Запис на картку займає 400 мс | `m2-94-vybirka` | клас E, а в назві число з одиницею |
| Модулі на 8 і 16 МБ флешу коштують істотно дорожче за різницю у ціні | `m2-95-vybirka` | клас E, а в назві число з одиницею |

## **не знайдено** — 95

| Доказ | Файл | Деталі |
|---|---|---|
| T-11-042: **Версія ESP-IDF фіксується на початку проєкту й записується.** | `cherga-a-11-idf` | 1 з 1 рядків: «use the current stable version…» |
| T-02-105: Але зроблене без збереження `sdkconfig.defaults` доведеться налаштовувати заново. | `klas-f-02-chipy` | 1 з 1 рядків: «For example projects or other projects where you dont want to specify …» |
| T-11-025: Спокуса прописати `export.sh` у `.bashrc` є в усіх, | `klas-f-11-idf` | 1 з 1 рядків: «Technically, you can add export.sh to your shell's profile directly; h…» |
| T-12-049: Тоді доступні `setup`/`loop` і бібліотеки Arduino — і | `klas-f-12-arduino` | 1 з 1 рядків: «For usage of setup() and loop() functions - Turn on Autostart Arduino …» |
| T-K06-045: На 115200 нічого, на 74880 осмислений текст — це ESP8266 | `m2-62-bootlog-k06` | 1 з 1 рядків: «The ESP8266 boot rom writes a log to the UART when booting at ``74880 …» |
| Етап 1 — ROM bootloader зашитий у кремній | `m2-82-boot-flesh` | 1 з 1 рядків: «The ROM bootloader is in read-only memory (ROM) on the ESP32 chip.…» |
| Етап 2 — другий бутлоадер bootloader.bin у флеші | `m2-82-boot-flesh` | 1 з 1 рядків: «After reset, the second line printed by the ESP32 ROM is a reset & boo…» |
| Адреса bootloader.bin для ESP32 чипів — 0x1000 | `m2-82-boot-flesh` | 1 з 1 рядків: «{IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="…» |
| GPIO0 як ключовий strapping-пін для вибору режиму завантаження | `m2-82-boot-flesh` | 1 з 1 рядків: «0x10  - GPIO0…» |
| Розділи ota_0 та ota_1 у таблиці розділів для OTA | `m2-82-boot-flesh` | 2 з 2 рядків: «ota_0,    app,  ota_0,   0x20000,  1M,…»; «ota_1,    app,  ota_1,   0x120000, 1M,…» |
| esptool версія v4 та v5 у ESP-IDF | `m2-83-esptool` | 2 з 2 рядків: «{IDF_TARGET_NAME} ROM (at 115200bps) is a reset & boot mode message.…»; «ESP-IDF version compatibility documented.…» |
| Адреса bootloader.bin для ESP32 — 0x1000 | `m2-83-esptool` | 1 з 1 рядків: «{IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="…» |
| Адреса merge-bin завжди на 0x0 незалежно від конфігурації | `m2-83-esptool` | 1 з 1 рядків: «Bootloader at {IDF_TARGET_BOOTLOADER_OFFSET} configurable by chip type…» |
| Таблиця розділів за замовчуванням на адресі 0x8000 | `m2-83-esptool` | 1 з 1 рядків: «partition table is flashed to (default offset) 0x8000 in the flash.…» |
| MAC-адреса унікальна від заводу і лежить в eFuse | `m2-83-esptool` | 1 з 1 рядків: «unique identifier stored in eFuse…» |
| Команда esptool flash-id додає інформацію про флеш | `m2-83-esptool` | 1 з 1 рядків: «esptool provides commands for flash operations…» |
| Максимальна швидкість baudu для більшості мостів 460800 | `m2-83-esptool` | 1 з 1 рядків: «serial connection parameters for flash operations…» |
| Розміри флешу 2 МБ або 4 МБ для ESP32 модулів | `m2-83-esptool` | 1 з 1 рядків: «flash capacity and partition allocation…» |
| Пріоритет задачі від 0 до configMAX_PRIORITIES мінус 1 | `m2-84-freertos` | 2 з 2 рядків: «Task priorities range from 0 (lowest) to configMAX_PRIORITIES - 1 (hig…»; «Vanilla FreeRTOS provides the following functions to create a task.…» |
| Core 0 (PRO_CPU) переважно займає радіостек, Core 1 (APP_CPU) — застосунок | `m2-84-freertos` | 3 з 3 рядків: «Within ESP-IDF, Core 0 and Core 1 are sometimes referred to as PRO_CPU…»; «Typically, tasks responsible for protocol processing such as Wi-Fi are…»; «while the remainder of the application are pinned to Core 1.…» |
| Функції FromISR єдині дозволені в обробнику переривання | `m2-84-freertos` | 1 з 1 рядків: «FromISR functions are ISR-safe variants of FreeRTOS APIs.…» |
| Бітові прапори WIFI_OK та TIME_OK в event group | `m2-84-freertos` | 1 з 1 рядків: «Event group bits are used for task synchronization.…» |
| Реле на GPIO при зависанні переходить в безпечний стан | `m2-84-freertos` | 1 з 1 рядків: «System recovery and restart mechanism through watchdog monitoring.…» |
| Код 0x10 означає RTCWDT_RTC_RESET (RTC watchdog скинув усе) | `m2-93-vybirka` | 2 з 5 рядків: «rst:0x10 (RTCWDT_RTC_RESET)…»; «unstable power source. It is enabled by default. If the execution…» |
| Перевірка переповнення стека і розмір стека app_main | `pass-01-tverde-yadro` | 3 з 8 рядків: «config ESP_MAIN_TASK_STACK_SIZE…»; «int "Main task stack size"…»; «default 3584…» |
| На C3 ADC2 непридатний через апаратну ваду, а не через Wi-Fi | `pass-02-povedinka` | 1 з 3 рядків: «The results are not stable. This issue can be found in `ESP32-C3 Serie…» |
| Strapping-піни за сімействами | `pass-08-strapping` | 2 з 6 рядків: «esp32h21="GPIO14", esp32h4="GPIO14"}…»; «esp32h4="GPIO13"}…» |
| merge-bin вимагає --chip; без нього команда падає | `pass-09-komandy` | 2 з 7 рядків: «* Binary image generation commands, such as elf2image or merge-bin,…»; «require the chip type to be specified.…» |
| Стиснення при передачі ввімкнене за замовчуванням | `pass-09-komandy` | 2 з 10 рядків: «By default, the serial transfer data is compressed for better performa…»; «The ``-u/--no-compress`` option disables this behaviour.…» |
| Розбіжність обсягу флешу — два різні рядки й різні наслідки | `pass-10-povidomlennya` | 3 з 3 рядків: «ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the b…»; «"header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chi…»; «ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the bi…» |
| Помилки купи розрізняють бік переповнення | `pass-10-povidomlennya` | 2 з 2 рядків: «#define ERR_STR1 "***ERROR*** A stack overflow in task "…»; «#define ERR_STR2 " has been detected."…» |
| Тексти помилок esptool змінилися між версіями | `pass-10-povidomlennya` | 6 з 8 рядків: «msg = ("Serial data stream stopped: Possible serial noise or corruptio…»; «if successful_slip else "No serial data received.")…»; «raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wro…» |
| Дерево menuconfig — корінь і Component config | `pass-11-menuconfig` | 9 з 13 рядків: «esptool_py:        menu "Serial flasher config"…»; «partition_table:   menu "Partition Table"…»; «bootloader:        menu "Bootloader config"…» |
| GPIO15 низький глушить boot-лог ROM | `pass-12-piny` | 2 з 3 рядків: «|            | bootloader. Has an internal pull-up, so unconnected = H…»; «|            | normal output.…» |
| Режими SPI — CPHA задає номер фронту, не напрямок | `pass-16-interfeysy` | 1 з 3 рядків: «@param  mode   SPI data mode; one of SPI_MODE0, SPI_MODE1, SPI_MODE2…» |
| pioarduino, а не офіційна платформа PlatformIO | `pass-17-simeystva-proektiv` | 1 з 5 рядків: «"version": "55.03.311"…» |
| Підтягування I²C — діапазон, а не одне число | `pass-18-schemy` | 2 з 5 рядків: «The recommended value for pull-up resistors usually ranges from 1 kΩ t…»; «should be (but not less than 1 kΩ). Indeed, large resistors will decli…» |
| Кольорова обв'язка прикладів — classic і тільки classic | `pass-20-jtag-obvyazka` | 1 з 1 рядків: «esp32: SOC_GPIO_PIN_COUNT 40…» |
| Зсув бутлоадера по сімействах — числа праві, причина хибна | `pass-24-zsuvy-i-matrycya` | 14 з 21 рядків: «#   (flash encryption) purpose…»; «.. only:: esp32…»; «sector of flash is used to store secure boot IV and digest of the…» |
| Таблиця розділів — 0xC00 і 95 записів; 0x7000 належить бутлоадерові | `pass-24-zsuvy-i-matrycya` | 8 з 18 рядків: «located at (default offset) + 0x1000.…»; «config PARTITION_TABLE_OFFSET…»; «hex "Offset of partition table"…» |
| Піновий план проєкту 60 — обидва сімейства | `pass-24-zsuvy-i-matrycya` | 8 з 17 рядків: «(esp32/adc_channel.h)          (esp32c3/adc_channel.h)…»; «#define ADC1_GPIO34_CHANNEL 6  #define ADC1_GPIO3_CHANNEL      3…»; «#define ADC1_CHANNEL_6_GPIO_NUM 34  #define ADC1_CHANNEL_3_GPIO_NUM 3…» |
| Рівні strapping і недійсна комбінація — усі сімейства | `pass-26-strapping` | 6 з 12 рядків: «{IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",…»; «{STRAP_BOOT_2_GPIO} must also be either left unconnected/floating,…»; «{STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the…» |
| Маска GPIO_STRAP — усі шість бітів classic і два біти решти | `pass-26-strapping` | 3 з 21 рядків: «represented in the GPIO_STRAP register.…»; «most cases, one of these modes is selected if {STRAP_BOOT_2_GPIO}…»; «has been pulled high when {STRAP_BOOT_GPIO} is low).…» |
| Іменування й версії esptool — version, esptool.py, дефіси проти підкреслень | `pass-28-komandy-suciljno` | 4 з 4 рядків: «The `esptool.py` name is kept as an alias; the recommended entry point…»; «is `esptool`. Command names use dashes: `write-flash`, `read-flash`,…»; «`erase-flash`, `merge-bin`. The underscore forms are deprecated and…» |
| flash-id як засіб упізнати перемаркований модуль | `pass-28-komandy-suciljno` | 4 з 4 рядків: «chip-id     Read Chip ID…»; «flash-id    Read SPI flash manufacturer and device ID…»; «The flash-id command outputs the manufacturer and device ID of the…» |
| erase-flash стирає весь чип, включно з NVS і калібруванням | `pass-28-komandy-suciljno` | 1 з 6 рядків: «esptool erase-region 0x20000 0x4000…» |
| merge-bin дає один образ на адресу 0x0 незалежно від сімейства | `pass-28-komandy-suciljno` | 4 з 5 рядків: «The merge-bin command will merge multiple binary files (of any kind)…»; «between the input files are padded with 0xFF bytes (or 0x00 in…»; «--format hex).…» |
| Рядки помилок з'єднання — Failed to connect і сусіди | `pass-29-log-i-reshta-komand` | 3 з 3 рядків: «A fatal error occurred: Failed to connect to {chip}: {reason}…»; «The most common reason for "Failed to connect" is that the chip is not…»; «to the same UART.…» |
| Паніка, backtrace і watchdog — назви рядків у логу | `pass-29-log-i-reshta-komand` | 2 з 3 рядків: «Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception wa…»; «Interrupt wdt timeout on CPU0…» |
| esptool і stub, автоскидання, розбіжність чипа | `pass-29-log-i-reshta-komand` | 5 з 5 рядків: «esptool has a two-stage flashing process: a small "stub" program is…»; «uploaded to RAM and run, which then performs the requested operation…»; «much faster than the ROM bootloader. ``--no-stub`` disables this.…» |
| merge-bin — прапорці флешу і призначення формату | `pass-29-log-i-reshta-komand` | 4 з 9 рядків: «between the input files are padded with 0xFF bytes.…»; «Options such as ``--flash-mode``, ``--flash-size`` and ``--flash-freq`…»; «are used to set the corresponding values in the image header, exactly…» |
| Роль esptool і послідовність дій із незнайомою платою | `pass-29-log-i-reshta-komand` | 2 з 2 рядків: «esptool is a Python-based, open-source, platform-independent utility t…»; «communicate with the ROM bootloader in Espressif chips.…» |
| Функції strapping-пінів classic — таблиця розділу 07 поштучно | `pass-30-piny-suciljno` | 4 з 10 рядків: «GPIO2 must also be either left unconnected/floating, or driven Low,…»; «bootloader. |…»; «0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4…» |
| Піни флешу, тільки-вхідні й ADC1 при Wi-Fi | `pass-30-piny-suciljno` | 5 з 5 рядків: «MSPI_IOMUX_PIN_NUM_CLK   6      MSPI_IOMUX_PIN_NUM_MISO  7…»; «MSPI_IOMUX_PIN_NUM_MOSI  8      MSPI_IOMUX_PIN_NUM_HD    9…»; «MSPI_IOMUX_PIN_NUM_WP   10      MSPI_IOMUX_PIN_NUM_CS0  11…» |
| Вхід у download mode вручну — порядок і його причина | `pass-30-piny-suciljno` | 4 з 7 рядків: «The {chip} will enter the serial bootloader when {STRAP_BOOT_GPIO} is…»; «{STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left…»; «development boards) that pulls {STRAP_BOOT_GPIO} low when pressed.…» |
| I²C і strapping на C3 — підтяжки збігаються з потрібними рівнями | `pass-30-piny-suciljno` | 4 з 6 рядків: «{STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the…»; «{STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and will…»; «ADC1_GPIO0_CHANNEL 0   ADC1_GPIO1_CHANNEL 1   ADC1_GPIO2_CHANNEL 2…» |
| Таблиці адрес прошивки — три рядки на три сімейства | `pass-31-adresy-i-api` | 3 з 9 рядків: «* At a 0x10000 (64 KB) offset in the flash is the app labelled…»; «"factory". The bootloader runs this app by default.…»; «nvs,      data, nvs,     0x9000,  0x6000,…» |
| ESP_ERROR_CHECK — це assert, а не обробка помилок | `pass-31-adresy-i-api` | 2 з 15 рядків: «#define ESP_OK          0    /*!< esp_err_t value indicating success *…»; «* message but isn't terminating the program.…» |
| ESP_LOGD не коштує нічого при рівні збирання Info | `pass-31-adresy-i-api` | 6 з 6 рядків: «* @brief Compile-time log level.…»; «* removed by the preprocessor and take no space in the binary and no…»; «* time at runtime.…» |
| Коди помилок OTA і NVS, які книга називає поіменно | `pass-31-adresy-i-api` | 2 з 6 рядків: «partition, and is used together with the FAT filesystem via…»; «esp_vfs_fat_spiflash_mount_rw_wl.…» |
| DAC, ADC-затухання й обв'язка входу — розділ 33 | `pass-32-pul-shmatky-1-3` | 8 з 11 рядків: «Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input…»; «voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,…»; «the attenuation of ADC is set to 11 dB, and input voltage higher than…» |
| LISTEN_ONLY і NO_ACK — режими TWAI дослівно | `pass-32-pul-shmatky-1-3` | 2 з 7 рядків: «The {IDF_TARGET_NAME} does not integrate an internal TWAI transceiver.…»; «Therefore, an external transceiver is required to connect to a TWAI…» |
| Рівні логу, esp_err_to_name і монітор — розділ 25 | `pass-32-pul-shmatky-1-3` | 4 з 10 рядків: «*        with specific address you gave.…»; «Whenever the chip outputs a hexadecimal address that points to…»; «executable code, IDF monitor looks up the location in the source code…» |
| Типова розбивка флешу — зсуви, розміри й суфікси | `pass-32-pul-shmatky-1-3` | 3 з 11 рядків: «ESP_LOGI(TAG, "Partition Table:");…»; «ESP_LOGI(TAG, "## Label            Usage          Type ST Offset   Len…»; «ESP_LOGI(TAG, "End of partition table");…» |
| Буфер у PSRAM без MALLOC_CAP_SPIRAM — і що це коштує | `pass-32-pul-shmatky-1-3` | 5 з 11 рядків: «// Forces data into DRAM instead of flash…»; «#define DRAM_ATTR _SECTION_ATTR_IMPL(".dram1", __COUNTER__)…»; «config FREERTOS_CHECK_STACKOVERFLOW_NONE…» |
| Strapping classic і C3 — таблиця розділу 07 проти gpio/*.inc | `pass-33-pul-shmatky-4-5` | 1 з 3 рядків: «{IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",…» |
| erase-flash, flash-id і коли стирання справді потрібне | `pass-34-pul-shmatok-6` | 1 з 12 рядків: «Old command and option names are **deprecated**.…» |
| Автоскидання не працює — перелік причин, крім однієї | `pass-34-pul-shmatok-6` | 2 з 9 рядків: «esptool is not able to reset your hardware automatically in the…»; «Check the chip is receiving 3.3V from a stable power source.…» |
| Коди RESET_REASON — уся таблиця причин скидання | `pass-35-vlasna-pomylka-boot` | 1 з 19 рядків: «SDIO_RESET             =  6,    /**<6, Reset by SLC module*/…» |
| ROM класифікує boot: значення цілком, а не пін за піном | `pass-35-vlasna-pomylka-boot` | 1 з 7 рядків: «#define ETS_IS_FLASH_BOOT()  (IS_1XXX(BOOT_MODE_GET()) || \…» |
| chip-id на сімействі ESP32 повертає попередження, а не Chip ID | `pass-36-chip-id` | 10 з 17 рядків: «log.warn(f"{esp.CHIP_NAME} has no chip ID. "…»; «"Reading MAC address instead.")…»; «def chip_id(self):…» |
| Драйвер I²C називає причину в консолі, а не мовчить | `pass-38-pul-shmatky-9-11` | 2 з 7 рядків: «config COMPILER_OPTIMIZATION_CHECKS_SILENT…»; «bool "Disable messages in ESP_RETURN_ON_* and ESP_EXIT_ON_* macros"…» |
| ESP_DRAM_LOGx — єдиний виняток із заборони логувати в ISR | `pass-38-pul-shmatky-9-11` | 2 з 5 рядків: «* interrupts are disabled or inside an ISR.…»; «* when absolutely essential.…» |
| На RISC-V рядка Backtrace немає — його будує монітор | `pass-38-pul-shmatky-9-11` | 2 з 12 рядків: «Moreover, IDF Monitor is also capable of generating and printing a…»; «IDF Monitor. Thus, in order to generate and print a backtrace while…» |
| sdkconfig.defaults рекомендовано тримати в системі контролю версій | `pass-45-sdkconfig-defaults` | 1 з 1 рядків: «It is recommended to commit sdkconfig.defaults for providing baseline …» |
| T-11-042: **Версія ESP-IDF фіксується на початку проєкту й записується.** | `prochid-11-idf` | 1 з 1 рядків: «use the current stable version…» |
| T-17-118: Друга половина рядка залежить від версії. | `prochid-17-esptool` | 1 з 1 рядків: «'esptool v{__version__}'…» |
| T-18-038: У проєкті ESP-IDF розбивка задається текстовим файлом: | `prochid-18-rozdily-fleshu` | 1 з 1 рядків: «If you configure the partition table CSV name in the project configura…» |
| T-18-080: У складі ESP-IDF · SPIFFS → так | `prochid-18-rozdily-fleshu` | 1 з 1 рядків: «spiffs (0x82) is for :doc:`/api-reference/storage/spiffs`…» |
| T-18-088: Після цього розділ у меню з'являється, а тип | `prochid-18-rozdily-fleshu` | 1 з 1 рядків: «littlefs (0x83) is for LittleFS filesystem…» |
| T-18-103: **Взяти готову розбивку з більшим розділом застосунку** для | `prochid-18-rozdily-fleshu` | 1 з 1 рядків: «The simplest way to use the partition table is to open the project con…» |
| T-18-107: Практично це означає: **розбивку треба обирати з запасом | `prochid-18-rozdily-fleshu` | 1 з 1 рядків: «Note that updating the partition table does not erase data that may ha…» |
| T-18-108: Змінити її потім можна лише з фізичним доступом | `prochid-18-rozdily-fleshu` | 1 з 1 рядків: «If Secure Boot V1 is enabled, then the partition of type app needs to …» |
| T-18-028: **`phy_init`** зберігає калібрувальні дані радіо. | `prochid-18-rozdily-fleshu` | 1 з 1 рядків: «phy (1) is for storing PHY initialisation data. This allows PHY to be …» |
| T-23-100: Напис на модулі звіряється з шапкою `esptool`. | `prochid-23-triazh` | 1 з 1 рядків: «If no -c option or ESPTOOL_CHIP value is specified, esptool automatica…» |
| T-27-002: Відлагоджувач показує все: поточне значення будь-якої змінної, вміст | `prochid-27-jtag` | 1 з 1 рядків: «figuring out a bug that is caused by two threads, running even simulta…» |
| T-31-031: Прив'язати задачу до ядра явно: | `prochid-31-freertos` | 1 з 1 рядків: «xTaskCreatePinnedToCore creates a task with a particular core affinity…» |
| T-31-034: Коли це має сенс: щось із жорсткими таймінгами | `prochid-31-freertos` | 1 з 1 рядків: «Typically, the tasks responsible for handling protocol related process…» |
| T-31-035: Щось важке й тривале — теж на ядро | `prochid-31-freertos` | 1 з 1 рядків: «Typically, the tasks responsible for handling protocol related process…» |
| T-33-091: Пам'ятайте: вхід не толерантний до перевищення — понад | `prochid-33-peryferiya-kod` | 1 з 1 рядків: «By design, Vref is set to 1100 mV…» |
| T-34-045: Багато модулів мають термінатор на платі, іноді припаяний | `prochid-34-uart` | 1 з 1 рядків: «This circuit does not allow for collision detection. It suppresses the…» |
| T-35-035: Сканер перебирає всі адреси й друкує ті, що | `prochid-35-i2c` | 1 з 1 рядків: «i2c_master_probe to detect whether the specific device has been connec…» |
| T-35-087: **Аналізатор** — `ACK` чи `NACK` (розділ 28). | `prochid-35-i2c` | 1 з 1 рядків: «Note to always ensure the last byte read before the stop condition is …» |
| T-G-116: | коефіцієнт заповнення | duty cycle | | `prochid-g-glosariy` | 1 з 1 рядків: «The range of the duty cycle values passed to functions depends on sele…» |
| T-Z-143: i2c_new_master_bus — 215, 326, 332 | `prochid-z-pokazhchyk` | 1 з 1 рядків: «i2c_new_master_bus can be called to allocate and initialize an I2C mas…» |

## джерело не в кеші — 161

| Доказ | Файл | Деталі |
|---|---|---|
| T-02-096: **Переноситься майже завжди:** код на ESP-IDF, написаний через | `klas-f-02-chipy` | 1 джерел не в кеші |
| T-02-099: Перенесення проєкту на інший чип в ESP-IDF починається | `klas-f-02-chipy` | 1 джерел не в кеші |
| T-02-103: Усі налаштування, зроблені через `menuconfig`, повертаються до типових. | `klas-f-02-chipy` | 1 джерел не в кеші |
| T-11-112: `set-target` стирає `sdkconfig`; у git кладеться `sdkconfig.defaults`. | `klas-f-11-idf` | 1 джерел не в кеші |
| Розпіновка JTAG classic — datasheet як друге джерело до io_mux_reg.h | `m2-01-esp32-datasheet-iomux` | 1 джерел не в кеші |
| Споживання ESP32 за режимами — порядки збігаються з Table 4-2 | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Пін віддає більше, ніж приймає — IOH 40 мА проти IOL 28 мА | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Робочий діапазон чипа ESP32 — від −40 до 125 °C | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Діапазон модуля WROOM — 85 °C у версіях N, 105 °C у версіях H | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Абсолютний максимум входу — 3.6 В, тому 5 В убивають пін | `m2-06-napruga-mezhi` | 1 джерел не в кеші |
| Нижня межа частот STM32 — 24 МГц у Value line | `m2-13-stm32-chastoty` | 2 джерел не в кеші |
| Свинцевий припій плавиться нижче за безсвинцевий | `m2-17-pripiy-i-ip` | 1 джерел не в кеші |
| «IVDD, current delivered by external power supply, Min 0.5 A» — дослівна цитата datasheet | `m2-21-zhyvlennya-06` | 1 джерел не в кеші |
| I2C: на спокої обидві лінії мають бути HIGH (3.3 В). Якщо немає — поломаний резистор підтягування. | `m2-90-vybirka` | 1 джерел не в кеші |
| Адреса bootloader.bin для S3, C3, C6, H2 — 0x0 | `m2-90-vybirka` | 1 джерел не в кеші |
| Код скидання 0xa — INTRUSION_RESET (детектор втручання), рідко трапляється | `m2-90-vybirka` | 1 джерел не в кеші |
| Код скидання 0xd названий RTCWDT_CPU_RESET | `m2-95-vybirka` | 1 джерел не в кеші |
| Код скидання 0x10 названий RTCWDT_RTC_RESET | `m2-95-vybirka` | 1 джерел не в кеші |
| Код скидання 0xc означає скидання ядра з коду | `m2-95-vybirka` | 1 джерел не в кеші |
| Код 0x08 на ESP32-C3 відповідає GPIO9 (strapping pin) | `m2-95-vybirka` | 1 джерел не в кеші |
| Bootloader розташований за адресою 0x0 на S3, C3, C6, H2 | `m2-95-vybirka` | 1 джерел не в кеші |
| T-D-025 — `0x8` код помилки, watchdog таймера 1 | `m2-96-vybirka` | 1 джерел не в кеші |
| T-D-046 — `0xf` код помилки RTCWDT_BROWN_OUT_RESET | `m2-96-vybirka` | 1 джерел не в кеші |
| Кількість блоків периферії за сімействами | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Апаратні піни IOMUX для UART0 і SPI | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Типові піни I²C і бортового світлодіода в Arduino | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Виклики FreeRTOS і атрибути розміщення | `pass-07-api-rozbyvka` | 1 джерел не в кеші |
| Решта команд esptool і idf.py, що вживає книга, існує дослівно | `pass-09-komandy` | 1 джерел не в кеші |
| Повідомлення бутлоадера про образ і розділи | `pass-10-povidomlennya` | 1 джерел не в кеші |
| Канали ADC і touch за GPIO — усі три сімейства | `pass-12-piny` | 1 джерел не в кеші |
| Піни IOMUX для UART0 і SPI | `pass-12-piny` | 1 джерел не в кеші |
| Зведена таблиця розділу 02 — ядра, радіо, PSRAM, USB | `pass-13-mozhlyvosti` | 1 джерел не в кеші |
| Кількість блоків периферії за сімействами | `pass-13-mozhlyvosti` | 1 джерел не в кеші |
| Компонент led_strip версії 3.0.3 і межа ^ у менеджері | `pass-15-versiyi` | 1 джерел не в кеші |
| GPIO22 не існує в S3, а GPIO22/23/34 — у C3 | `pass-17-simeystva-proektiv` | 1 джерел не в кеші |
| DAC на S2 — GPIO17 і GPIO18, а не 25/26 | `pass-17-simeystva-proektiv` | 1 джерел не в кеші |
| Проєкт 62 свідомо на classic через тільки-вхідний GPIO34 | `pass-18-schemy` | 1 джерел не в кеші |
| Поля конфігураційних структур збігаються із заголовками ESP-IDF | `pass-21-polya-struktur` | 1 джерел не в кеші |
| DAC на S2 — GPIO17 і GPIO18; розділ 07 виправлено | `pass-23-dac-propahaciya` | 1 джерел не в кеші |
| Мілісекунди в дужках у рядку логу | `pass-29-log-i-reshta-komand` | 1 джерел не в кеші |
| Номери GPIO книги дійсні для сімейств, яким приписані | `pass-30-piny-suciljno` | 1 джерел не в кеші |
| Тільки-вхідні, консоль і USB-JTAG у довіднику пінів | `pass-33-pul-shmatky-4-5` | 1 джерел не в кеші |
| Піновий план проєкту 62 — три сімейства, кожен пін вільний | `pass-33-pul-shmatky-4-5` | 1 джерел не в кеші |
| T-05-077: Звичайний вихід активно тримає лінію в обох станах. | `prochid-05-elektronika` | 1 джерел не в кеші |
| T-07-065: Спроба їх використати підвішує чип або псує вміст | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-067: Ніколи, за жодних умов, у жодному проєкті. | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-069: Різниця між шісткою й цією парою — у | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-072: Практично це означає, що правило «шість пінів» безпечне | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-083: Друге важливіше, бо менш очевидне. | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-085: Виглядає як несправний пін або несправна кнопка. | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-086: Налаштуванням у коді це не змінюється: апаратної схеми | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-093: Людина шукає помилку в коді вимірювання, а справа | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-107: Використати їх під щось інше можна, але тоді | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-108: Правило: чіпати UART0 тільки тоді, коли пінів справді | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-136: Strapping-піни краще використовувати як виходи й лишати вільними | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-045: | | Головний пін | Другий пін для | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-053: На classic і S3 такої комбінації немає — | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-064: Вони **виведені на гребінку** більшості плат, підписані як | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-066: Правило категоричне: [[classic]] шість пінів 6–11 не існують. | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-071: На голому `WROOM-32` вони вільні. | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-078: [[S3]] Це найпоширеніша причина «купив S3 із 16 | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-080: Перед проєктуванням плати на S3 варто точно знати, | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-087: У пізніших сімействах (S3, C3) тільки-вхідних пінів немає | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-101: Більше ніде в лінійці DAC немає (розділи 04 | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-104: Для всіх трьох матриця GPIO не діє: це | `prochid-07-gpio` | 1 джерел не в кеші |
| T-07-121: **Чип із більшою кількістю пінів** — S3 має | `prochid-07-gpio` | 1 джерел не в кеші |
| T-09-007: Тому між ними ставлять **міст USB-UART**: окремий чип, | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-037: **Linux у більшості випадків не потребує нічого.** Драйвери | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-042: Мосту не потрібно взагалі: чип під'єднується до комп'ютера | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-045: **Драйвер не потрібен.** Пристрій відповідає стандарту USB CDC, | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-070: У деяких дистрибутивах група називається `uucp` замість `dialout` | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-069: Без цього нова група не застосується до поточної | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-077: Порт відкриває **лише один процес одночасно**. | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-087: Кабель, роз'єм або живлення плати. | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-09-010: Звідси випливає головне: **порт у системі створює міст, | `prochid-09-pidklyuchennya` | 1 джерел не в кеші |
| T-13-024: Запис `espressif32 @ 6.5.0` збереться — і дасть | `prochid-13-pio` | 1 джерел не в кеші |
| T-13-014: **Версії фіксуються в проєкті.** Це головне. | `prochid-13-pio` | 1 джерел не в кеші |
| T-13-020: Весь проєкт описується одним файлом: | `prochid-13-pio` | 1 джерел не в кеші |
| T-13-002: Для ESP32 воно дає те, чого не дає | `prochid-13-pio` | 1 джерел не в кеші |
| T-13-004: Підтримка ESP32 у PlatformIO забезпечується платформою `platform-espressif32`. | `prochid-13-pio` | 1 джерел не в кеші |
| T-13-005: Офіційна платформа від PlatformIO **відстала** від Arduino core: | `prochid-13-pio` | 1 джерел не в кеші |
| T-13-015: `platformio.ini` лежить у git і повністю описує, чим | `prochid-13-pio` | 1 джерел не в кеші |
| T-14-005: Ви прошиваєте його один раз, далі працюєте з | `prochid-14-shvydki-shlyakhy` | 1 джерел не в кеші |
| T-14-015: Частина периферії доступна частково. | `prochid-14-shvydki-shlyakhy` | 1 джерел не в кеші |
| T-14-071: **Розвідка заліза** — MicroPython у консолі: чи відповідає | `prochid-14-shvydki-shlyakhy` | 1 джерел не в кеші |
| T-17-051: Файл, менший за очікуваний, — це обірваний дамп, | `prochid-17-esptool` | 1 джерел не в кеші |
| T-17-074: Адреси залежать від сімейства чипа — таблиця в | `prochid-17-esptool` | 1 джерел не в кеші |
| T-24-057: Цього достатньо, щоб написати власну прошивку, яка робить | `prochid-24-chuzha-proshyvka` | 1 джерел не в кеші |
| T-24-068: Якщо ввімкнено — дамп зашифрований ключем, що не | `prochid-24-chuzha-proshyvka` | 1 джерел не в кеші |
| T-27-020: Якщо в проєкті ці піни переналаштовані під щось | `prochid-27-jtag` | 1 джерел не в кеші |
| T-30-076: IRAM небагато, і кожна така функція займає її | `prochid-30-struktura` | 1 джерел не в кеші |
| T-30-004: `app_main` викликається як звичайна задача FreeRTOS. | `prochid-30-struktura` | 1 джерел не в кеші |
| T-30-006: **`app_main` може завершитися.** І це нормально: система продовжує | `prochid-30-struktura` | 1 джерел не в кеші |
| T-30-007: Задача `app_main` просто зникає, звільняючи свій стек. | `prochid-30-struktura` | 1 джерел не в кеші |
| T-30-016: **Статична.** Глобальні змінні й `static`. | `prochid-30-struktura` | 1 джерел не в кеші |
| T-30-032: **Великі буфери — не на стек.** `static` або | `prochid-30-struktura` | 1 джерел не в кеші |
| T-30-067: Коли вільно 40 КБ, а найбільший блок — | `prochid-30-struktura` | 1 джерел не в кеші |
| T-31-002: Це не бібліотека, яку треба підключати, — це | `prochid-31-freertos` | 1 джерел не в кеші |
| T-31-085: Усі програмні таймери виконуються в **одній** службовій задачі. | `prochid-31-freertos` | 1 джерел не в кеші |
| T-33-029: Для більшості періодичних задач цього досить: | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-034: Це основний спосіб міряти час: переповнення не станеться | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-060: - **мертвий час** між верхнім і нижнім плечем | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-075: Це правильний спосіб читати ІЧ-пульти й датчики з | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-077: Енкодер, витратомір, лічильник обертів — усе це не | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-079: PCNT уміє й апаратний фільтр коротких сплесків — | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-127: PCNT рахує імпульси без переривань і має апаратний | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-062: RMT задумувався для інфрачервоних пультів, а виявився універсальним | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-33-074: RMT уміє й приймати — вимірювати тривалість вхідних | `prochid-33-peryferiya-kod` | 1 джерел не в кеші |
| T-34-055: ESP-IDF має штатний компонент `esp-modbus` для обох ролей: | `prochid-34-uart` | 1 джерел не в кеші |
| T-39-044: Пристрій гріється, з'їдає батарею і не робить нічого | `prochid-39-wifi` | 1 джерел не в кеші |
| T-39-033: Робота йде **через події**: під'єднання асинхронне, і код | `prochid-39-wifi` | 1 джерел не в кеші |
| T-39-047: ESP_LOGW(TAG, "зв'язок втрачено, спроба через %d мс", pauza); | `prochid-39-wifi` | 1 джерел не в кеші |
| T-39-054: Правильно — зберігати в NVS (розділ 18), а | `prochid-39-wifi` | 1 джерел не в кеші |
| T-39-064: ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary); | `prochid-39-wifi` | 1 джерел не в кеші |
| T-39-087: **Modem sleep** — радіо вимикається між маячками, з'єднання | `prochid-39-wifi` | 1 джерел не в кеші |
| T-39-088: Вмикається за замовчуванням і майже безкоштовне. | `prochid-39-wifi` | 1 джерел не в кеші |
| T-39-019: Якщо роутер працює на 13-му, ESP32 із неправильно | `prochid-39-wifi` | 1 джерел не в кеші |
| T-46-068: Правильний спосіб читання — **PCNT** (розділ 33): апаратний | `prochid-46-dyspleyi` | 1 джерел не в кеші |
| T-A-010: 1 · Обмеження → UART0 TX | `prochid-a-pinouty` | 1 джерел не в кеші |
| T-A-011: 1 · Примітка → консоль | `prochid-a-pinouty` | 1 джерел не в кеші |
| T-A-016: 3 · Обмеження → UART0 RX | `prochid-a-pinouty` | 1 джерел не в кеші |
| T-A-017: 3 · Примітка → консоль | `prochid-a-pinouty` | 1 джерел не в кеші |
| T-A-099: UART0 TX / RX · [[classic]] → 1 | `prochid-a-pinouty` | 1 джерел не в кеші |
| T-A-009: 0 · Примітка → `BOOT`; низький = download | `prochid-a-pinouty` | 1 джерел не в кеші |
| T-A-088: 5 · Обмеження → ADC2 | `prochid-a-pinouty` | 1 джерел не в кеші |
| T-C-092: `/dev/ttyUSB*` — зовнішній міст. | `prochid-c-komandy` | 1 джерел не в кеші |
| T-E-125: WS2812 / SK6812 · Як → **RMT**, не | `prochid-e-interfeysy` | 1 джерел не в кеші |
| T-G-036: | стабілізатор | voltage regulator | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-085: | відтворюване збирання | reproducible build | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-054: | прошивка | firmware | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-056: | збирання | build | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-077: | зворотний виклик | callback | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-095: | маячок | beacon | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-102: | центр сертифікації | certificate authority, CA | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-103: | рукостискання | handshake | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-104: | широкомовна розсилка | broadcast | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-109: | струм | current | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-111: | потужність | power | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-118: | точність | accuracy | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-119: | калібрування | calibration | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-120: | усереднення | averaging | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-121: | шум | noise | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-141: | IDF | IoT Development Framework | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-142: | RTOS | Real-Time Operating System | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-G-162: | ULP | Ultra-Low-Power (співпроцесор) | | `prochid-g-glosariy` | 1 джерел не в кеші |
| T-K03-018: Windows: `Диспетчер пристроїв` → жовтий знак оклику означає | `prochid-k03-pidkl` | 1 джерел не в кеші |
| T-K03-020: Порт `/dev/ttyUSB0` є, але програма пише «Permission denied» | `prochid-k03-pidkl` | 1 джерел не в кеші |
| T-K03-027: Порт зайнятий іншою програмою: відкритий монітор, Arduino IDE, | `prochid-k03-pidkl` | 1 джерел не в кеші |
| T-K08-008: 2 · Найчастіша причина → плата не в | `prochid-k08-symptomy` | 1 джерел не в кеші |
| T-K11-008: **Не вмикати Flash Encryption і Secure Boot «щоб | `prochid-k11-nikoly` | 1 джерел не в кеші |
| T-Z-012: серійна прошивка — 4, 143, 145, 398 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-056: ESP_ERR_INVALID_ARG — 207, 326 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-062: esp_err_t — 131, 136, 164, 197–198, 327, 329–331, | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-108: FreeRTOS — 4–5, 40–41, 46, 94, 100, 103, | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-154: merge-bin — 15, 25–26, 35, 125–126, 128, 137, | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-046: ESP32-C3-MINI-1 — 7, 79, 152, 401 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-047: ESP32-CAM — 14, 80, 82, 279–281 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-051: ESP32-WROOM-32 — 7, 39, 79, 123, 152, 401 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-052: ESP32-WROOM-32D — 79, 152 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-053: ESP32-WROVER — 7, 79, 152 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |
| T-Z-156: Modbus — 156, 209, 211, 356, 358, 360 | `prochid-z-pokazhchyk` | 1 джерел не в кеші |

## звірено — 381

| Доказ | Файл | Деталі |
|---|---|---|
| T-04-061: **MCPWM** [[classic]] [[S3]] зроблений спеціально для силової електроніки: | `cherga-a-04-peryferiya` | 1 рядків |
| T-11-023: Ця команда додає інструменти в `PATH` і ставить | `cherga-a-11-idf` | 3 рядків |
| T-16-056: Якщо є лише `factory` — беруть його. | `cherga-a-16-boot` | 1 рядків |
| T-17-061: Аргументи йдуть парами: адреса, файл. | `cherga-a-17-esptool` | 1 рядків |
| T-17-063: `-z` вмикає стиснення при передачі. | `cherga-a-17-esptool` | 1 рядків |
| T-18-074: Швидкість при заповненні · SPIFFS → різко падає | `cherga-a-18-rozdily-fleshu` | 1 рядків |
| T-19-023: Схема з двох слотів без `factory` — робоча | `cherga-a-19-ota` | 1 рядків |
| T-19-013: Пристрій виконується зі слоту `ota_0`. | `cherga-a-19-ota` | 1 рядків |
| T-19-014: Приходить оновлення — воно записується в `ota_1`, при | `cherga-a-19-ota` | 1 рядків |
| T-25-051: Один тег на файл або на логічний модуль; | `cherga-a-25-log` | 1 рядків |
| T-H-017: **`github.com/espressif/esp-idf`** — сам фреймворк. | `cherga-a-h-dzherela` | 1 рядків |
| T-02-042: Wi-Fi · ESP32 → так | `klas-f-02-chipy` | 1 рядків |
| T-02-043: Wi-Fi · S2 → так | `klas-f-02-chipy` | 1 рядків |
| T-02-044: Wi-Fi · S3 → так | `klas-f-02-chipy` | 1 рядків |
| T-02-047: Wi-Fi · H2 → **ні** | `klas-f-02-chipy` | 1 рядків |
| T-02-054: BLE · ESP32 → так | `klas-f-02-chipy` | 1 рядків |
| T-02-055: BLE · S2 → **ні** | `klas-f-02-chipy` | 1 рядків |
| T-02-057: BLE · C3 → так | `klas-f-02-chipy` | 1 рядків |
| T-11-001: ESP-IDF (Espressif IoT Development Framework) — офіційний фреймворк | `klas-f-11-idf` | 1 рядків |
| T-11-013: **Windows.** Офіційний інсталятор ESP-IDF Tools Installer ставить усе | `klas-f-11-idf` | 1 рядків |
| T-12-009: **`loop` — звичайна задача FreeRTOS.** Вона має свій | `klas-f-12-arduino` | 1 рядків |
| T-12-033: Arduino core версії 3.x — велике оновлення: він | `klas-f-12-arduino` | 1 рядків |
| T-12-048: **Arduino як компонент ESP-IDF.** Найцікавіший варіант: проєкт будується | `klas-f-12-arduino` | 1 рядків |
| T-12-061: `delay` тут не блокує систему, а `loop` — | `klas-f-12-arduino` | 2 рядків |
| T-13-070: | Виріб, OTA, серійність, довгий супровід | ESP-IDF | `klas-f-13-pio` | 1 рядків |
| T-14-053: Треба писати код · MicroPython → так, Python | `klas-f-14-shvydki-shlyakhy` | 1 рядків |
| T-19-007: `otadata` · Тип → data | `klas-f-19-ota` | 1 рядків |
| T-19-009: `ota_0` · Тип → app | `klas-f-19-ota` | 1 рядків |
| T-19-011: `ota_1` · Тип → app | `klas-f-19-ota` | 1 рядків |
| T-19-013: Пристрій виконується зі слоту `ota_0`. | `klas-f-19-ota` | 1 рядків |
| T-19-014: Приходить оновлення — воно записується в `ota_1`, при | `klas-f-19-ota` | 1 рядків |
| T-19-016: Наступне оновлення піде у слот `ota_0`. | `klas-f-19-ota` | 1 рядків |
| T-19-059: Компонент сам знаходить неактивний слот, пише в нього | `klas-f-19-ota` | 1 рядків |
| T-41-007: Проєкт на SPP, що переїжджає на S3, доведеться | `klas-f-41-ble` | 1 рядків |
| T-41-011: Де є · BLE → уся лінійка, крім | `klas-f-41-ble` | 7 рядків |
| T-41-015: Швидкість · BLE → десятки кбіт/с | `klas-f-41-ble` | 1 рядків |
| T-41-019: Спарювання · BLE → не обов'язкове | `klas-f-41-ble` | 1 рядків |
| T-41-038: Тоді пристрій самоописовий — будь-який універсальний BLE-застосунок покаже | `klas-f-41-ble` | 1 рядків |
| T-41-040: В ESP-IDF два стеки BLE, і вибір між | `klas-f-41-ble` | 1 рядків |
| T-41-041: **Bluedroid** — повний стек, підтримує і Classic, і | `klas-f-41-ble` | 1 рядків |
| T-41-043: **NimBLE** — тільки BLE, компактніший, займає в рази | `klas-f-41-ble` | 1 рядків |
| T-41-049: **Wi-Fi і Bluetooth одночасно** працюють, але ділять одне | `klas-f-41-ble` | 1 рядків |
| T-41-054: BLE спроєктований для батарейок, і його головний параметр | `klas-f-41-ble` | 1 рядків |
| T-41-078: Для BLE-проєкту брати NimBLE: різниця в пам'яті вирішальна | `klas-f-41-ble` | 1 рядків |
| T-42-001: ESP-NOW — власний протокол Espressif для прямого обміну | `klas-f-42-espnow` | 1 рядків |
| T-42-006: ESP-NOW не робить нічого з цього. | `klas-f-42-espnow` | 1 рядків |
| T-42-015: Кожен пристрій має унікальну MAC від заводу (розділ | `klas-f-42-espnow` | 1 рядків |
| T-42-027: Обробник прийому виконується в контексті **задачі** Wi-Fi, а | `klas-f-42-espnow` | 1 рядків |
| T-42-045: ESP-NOW підтримує шифрування з ключами PMK і LMK. | `klas-f-42-espnow` | 1 рядків |
| T-42-048: Без шифрування ESP-NOW — це відкритий радіоефір. | `klas-f-42-espnow` | 1 рядків |
| T-42-060: Усі вузли на фіксованому каналі, Wi-Fi не використовується. | `klas-f-42-espnow` | 1 рядків |
| 0x1: Що сталося → подано живлення або EN | `m2-60-panik-a` | 1 рядків |
| 0x1: Що робити → норма | `m2-60-panik-a` | 1 рядків |
| 0x3: Назва → SW_RESET | `m2-60-panik-a` | 1 рядків |
| 0x3: Що робити → норма, якщо ваша | `m2-60-panik-a` | 1 рядків |
| 0x4: Назва → OWDT_RESET | `m2-60-panik-a` | 1 рядків |
| 0x4: Що сталося → застарілий watchdog | `m2-60-panik-a` | 1 рядків |
| 0x4: Що робити → рідко | `m2-60-panik-a` | 1 рядків |
| 0x5: Назва → DEEPSLEEP_RESET | `m2-60-panik-a` | 1 рядків |
| 0x5: Що сталося → прокинувся з deep sleep | `m2-60-panik-a` | 1 рядків |
| 0x5: Що робити → норма | `m2-60-panik-a` | 1 рядків |
| 0x6: Назва → SDIO_RESET | `m2-60-panik-a` | 1 рядків |
| 0x6: Що сталося → скидання модулем SLC | `m2-60-panik-a` | 1 рядків |
| 0x6: Що робити → рідко | `m2-60-panik-a` | 1 рядків |
| 0x7: Що сталося → watchdog таймера 0 | `m2-60-panik-a` | 1 рядків |
| 0x8: Назва → TG1WDT_SYS_RESET | `m2-60-panik-a` | 1 рядків |
| 0x8: Що сталося → watchdog таймера 1 | `m2-60-panik-a` | 1 рядків |
| 0x9: Назва → RTCWDT_SYS_RESET | `m2-60-panik-a` | 1 рядків |
| 0x9: Що сталося → RTC watchdog | `m2-60-panik-a` | 1 рядків |
| 0xa: Назва → INTRUSION_RESET | `m2-60-panik-a` | 1 рядків |
| T-D-153: EXCVADDR — найшвидша підказка | `m2-61-panik-b` | 1 рядків |
| T-D-159: IDLE0 та Task Watchdog Timeout | `m2-61-panik-b` | 1 рядків |
| T-D-172: assert failed як порушення інваріанта | `m2-61-panik-b` | 3 рядків |
| T-D-183: rst: у першому рядку RTC Watchdog Timeout | `m2-61-panik-b` | 3 рядків |
| T-D-184: Причина паніки і EXCVADDR | `m2-61-panik-b` | 1 рядків |
| T-D-185: Backtrace через .elf за допомогою IDF Monitor | `m2-61-panik-b` | 5 рядків |
| T-D-187: Coredump та логування переходів станів при невідтворюванні | `m2-61-panik-b` | 1 рядків |
| T-D-188: Backtrace без .elf нерозшифровний | `m2-61-panik-b` | 1 рядків |
| T-K06-001: Монітор на 115200 бод для читання boot-логу | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-005: rst: — причина останнього скидання чипа | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-009: 0x1 (POWERON_RESET) — подано живлення або натиснуто EN | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-026: boot: — куди пішов чип (SPI_FAST_FLASH_BOOT або DOWNLOAD_BOOT) | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-038: Garbage символи при 115200 означають ESP8266; на 74880 читається | `m2-62-bootlog-k06` | 1 рядків |
| Таблиця розділів з адресами nvs 0x9000 та factory 0x10000 | `m2-82-boot-flesh` | 2 рядків |
| Сторож (Watchdog) автоматично перезавантажує систему при зависанні | `m2-84-freertos` | 2 рядків |
| Task Watchdog Timer та Interrupt Watchdog Timer у ESP-IDF | `m2-84-freertos` | 3 рядків |
| T-D-040: 0xd = RTCWDT_CPU_RESET, що робити → розділ 32 | `m2-94-vybirka` | 1 рядків |
| T-D-043: 0xe = EXT_CPU_RESET, норма | `m2-94-vybirka` | 1 рядків |
| T-D-041: 0xe = EXT_CPU_RESET (Назва) | `m2-94-vybirka` | 1 рядків |
| Адреса другого бутлоадера задається ROM і має три значення | `pass-01-tverde-yadro` | 7 рядків |
| Таблиця розділів лежить на 0x8000, застосунок на 0x10000 | `pass-01-tverde-yadro` | 3 рядків |
| Коди причин скидання (RESET_REASON) | `pass-01-tverde-yadro` | 18 рядків |
| C6 має два I²C, другий низькоспоживчий | `pass-01-tverde-yadro` | 3 рядків |
| Придатних каналів Touch на S2 і S3 — чотирнадцять, а не п'ятнадцять | `pass-01-tverde-yadro` | 3 рядків |
| Термін підтримки ESP-IDF — 30 місяців, із них 12 Service | `pass-01-tverde-yadro` | 5 рядків |
| Межі ESP-NOW і сигнатури зворотних викликів | `pass-01-tverde-yadro` | 7 рядків |
| Рівні оптимізації в menuconfig | `pass-01-tverde-yadro` | 11 рядків |
| ADC2 конфліктує з Wi-Fi на classic, S2 і S3 — не лише на classic | `pass-02-povedinka` | 2 рядків |
| Матриця GPIO обмежує SPI до 40 МГц проти 80 МГц на IOMUX | `pass-02-povedinka` | 5 рядків |
| TWAI сумісний з ISO 11898-1 і потребує зовнішнього трансивера | `pass-02-povedinka` | 4 рядків |
| CAN FD не підтримується жодним із сімейств книги | `pass-02-povedinka` | 2 рядків |
| ESP32 у ролі веденого I²C не вміє розтягувати SCL | `pass-02-povedinka` | 4 рядків |
| Механізм відкату OTA і його стани | `pass-02-povedinka` | 6 рядків |
| Вміст RTC-пам'яті переживає deep sleep | `pass-02-povedinka` | 3 рядків |
| Частота і розрядність LEDC пов'язані обернено | `pass-02-povedinka` | 5 рядків |
| BME280 — карта регістрів і довжини блоків калібрування | `pass-04-obkhidni` | 11 рядків |
| BME280 — старший байт dig_H4 і dig_H5 знаковий | `pass-04-obkhidni` | 9 рядків |
| DS18B20 — −127 °C як код помилки і межа 750 мс | `pass-04-obkhidni` | 4 рядків |
| Типовий ATT MTU дорівнює 23 байтам в обох стеках | `pass-04-obkhidni` | 6 рядків |
| SH1106 зсунуто на два пікселі відносно SSD1306 | `pass-04-obkhidni` | 6 рядків |
| LoRa — апаратний діапазон SF починається з шістки | `pass-04-obkhidni` | 6 рядків |
| RP2040 — обсяг SRAM 264 КБ | `pass-04-obkhidni` | 4 рядків |
| Синтаксис esptool v5 — дефіси замість підкреслень, без .py | `pass-06-komandy-strapping` | 11 рядків |
| read-flash з ALL визначає обсяг флешу сам | `pass-06-komandy-strapping` | 8 рядків |
| MTDI (GPIO12) задає напругу VDDSDIO для мікросхеми флешу | `pass-06-komandy-strapping` | 10 рядків |
| Стеля пріоритетів FreeRTOS в ESP-IDF — 25 | `pass-07-api-rozbyvka` | 1 рядків |
| Типова розбивка флешу та вирівнювання розділів | `pass-07-api-rozbyvka` | 9 рядків |
| Сила драйвера GPIO налаштовується, типова — середня | `pass-07-api-rozbyvka` | 3 рядків |
| gpio_dump_io_configuration показує реальну конфігурацію піна | `pass-07-api-rozbyvka` | 9 рядків |
| boot: у логу — бітова маска станів strapping-пінів | `pass-08-strapping` | 9 рядків |
| GPIO12 високий дає VDDSDIO 1.8 В і brownout тривольтового флешу | `pass-08-strapping` | 2 рядків |
| idf.py merge-bin бере адреси з конфігурації проєкту | `pass-09-komandy` | 6 рядків |
| --after watchdog-reset для чипів із native USB | `pass-09-komandy` | 7 рядків |
| Формат паніки Guru Meditation і назви винятків | `pass-10-povidomlennya` | 14 рядків |
| Дамп Task WDT — два різні переліки | `pass-10-povidomlennya` | 4 рядків |
| Camera probe failed — повний вигляд рядка | `pass-10-povidomlennya` | 1 рядків |
| Меню логування зветься Log, а не Log output | `pass-11-menuconfig` | 5 рядків |
| Maximum log verbosity — стеля компіляції окремо від типового рівня | `pass-11-menuconfig` | 17 рядків |
| Відкат вмикається в підменю Application Rollback | `pass-11-menuconfig` | 4 рядків |
| Рівні оптимізації компілятора | `pass-11-menuconfig` | 12 рядків |
| Хост Bluetooth і перевірка переповнення стека | `pass-11-menuconfig` | 12 рядків |
| Номери ліній USB-Serial-JTAG | `pass-12-piny` | 4 рядків |
| Другий strapping-пін на classic і S3 працює навпаки до C3 | `pass-12-piny` | 4 рядків |
| Політика підтримки ESP-IDF — 30 місяців, без окремого LTS | `pass-15-versiyi` | 7 рядків |
| BME280 — адреси, ідентифікатор чипа, регістр | `pass-18-schemy` | 4 рядків |
| DS18B20 повертає −127 при відсутності зв'язку | `pass-18-schemy` | 1 рядків |
| JTAG-піни classic — усі чотири з таблиці IOMUX | `pass-24-zsuvy-i-matrycya` | 9 рядків |
| Матриця GPIO і SPI — 40 проти 80 МГц, і коли різниці немає | `pass-24-zsuvy-i-matrycya` | 11 рядків |
| MSPI на S3 — GPIO26–32 під флеш, GPIO33–37 під восьмилінійний режим | `pass-25-psram` | 14 рядків |
| PSRAM вимкнена типово, а винесення в неї — навпаки, ввімкнене | `pass-25-psram` | 23 рядків |
| Octal PSRAM треба зазначити — типово стоїть Quad | `pass-25-psram` | 7 рядків |
| Внутрішнє підтягування strapping — 45 кОм, кнопці треба 10 кОм | `pass-26-strapping` | 5 рядків |
| GPIO12 має внутрішнє підтягування вниз — безпечний за замовчуванням | `pass-26-strapping` | 5 рядків |
| idf.py monitor — вихід Ctrl+], скидання через Ctrl+T | `pass-28-komandy-suciljno` | 12 рядків |
| espefuse палить в один бік; остання перепона — слово BURN | `pass-28-komandy-suciljno` | 12 рядків |
| esp_timer — мікросекундна роздільність, обробники в одній задачі | `pass-31-adresy-i-api` | 7 рядків |
| JTAG на classic — чотири піни, два з них strapping | `pass-32-pul-shmatky-1-3` | 13 рядків |
| USB-JTAG і вбудований відлагоджувач — піни по сімействах | `pass-32-pul-shmatky-1-3` | 3 рядків |
| Зміна розбивки, erase-flash і незворотність | `pass-32-pul-shmatky-1-3` | 6 рядків |
| На модулях із PSRAM зайняті ще GPIO16 і GPIO17 | `pass-33-pul-shmatky-4-5` | 3 рядків |
| ADC2 при Wi-Fi — драйвер розводить, а не віддає сміття | `pass-33-pul-shmatky-4-5` | 5 рядків |
| GPIO5 на classic — теж strapping, і книга це тепер каже | `pass-33-pul-shmatky-4-5` | 3 рядків |
| Асиметрія двох зсувів і те, що esptool не перевіряє адресу | `pass-34-pul-shmatok-6` | 13 рядків |
| Порядок читання backtrace — знахідку відхилено | `pass-35-vlasna-pomylka-boot` | 2 рядків |
| Сімейство, ревізію, кристал і MAC друкує преамбула з'єднання | `pass-36-chip-id` | 8 рядків |
| Межі --baud — 230400 у більшості, 460800 лише в деяких | `pass-38-baud-mezhi` | 1 рядків |
| З'єднання завжди на 115200 — --baud стосується лише передавання | `pass-38-baud-mezhi` | 1 рядків |
| GPIO11 на C3 — це майданчик VDD_SPI, живлення флешу | `pass-38-pul-shmatky-9-11` | 7 рядків |
| Рядки режиму завантаження — перелік із документації esptool | `pass-39-pul-haiku` | 3 рядків |
| Пін входу в бутлоадер за сімействами — підстановки esptool | `pass-39-pul-haiku` | 3 рядків |
| Внутрішнє підтягування 45 кОм на піні входу в бутлоадер | `pass-39-pul-haiku` | 2 рядків |
| GPIO16 і GPIO17 на classic живляться з домену VDD_SDIO | `pass-39-pul-haiku` | 3 рядків |
| GPIO5 на classic — CS апаратного VSPI | `pass-39-pul-haiku` | 1 рядків |
| Сила драйвера GPIO — типова середня, і файл лежить не там | `pass-39-pul-haiku` | 5 рядків |
| Піни 34–39 classic не мають вбудованого підтягування | `pass-39-slidy` | 1 рядків |
| ESP-NOW — прийом через зареєстрований обробник | `pass-39-slidy` | 1 рядків |
| Вбудований USB — окремого моста немає | `pass-39-slidy` | 1 рядків |
| ESP-NOW — важка робота в обробнику шкодить | `pass-39-slidy` | 1 рядків |
| OTA — сертифікат сервера вбудовано в образ | `pass-39-slidy` | 1 рядків |
| Тільки-вхідні піни — ні драйвера, ні підтягування | `pass-39-slidy` | 1 рядків |
| Можливості сімейств за soc_caps.h — ядра, Wi-Fi, BLE, USB | `pass-40-mira-f` | 4 рядків |
| Вбудований ADC нелінійний | `pass-40-mira-f` | 1 рядків |
| main — теж компонент ESP-IDF | `pass-40-mira-f` | 1 рядків |
| Оновлення файлу не фіксується до sync або close | `pass-41-littlefs-vtrata-zhyvlennya` | 1 рядків |
| Розділ factory в схемі OTA не обов'язковий | `pass-43-ota-bez-factory` | 1 рядків |
| Таблиця розділів лежить за зсувом 0x8000 | `pass-44-presud-e-buv-hybnyy` | 1 рядків |
| SPI через матрицю обмежений 40 МГц замість 80 на рідних пінах | `pass-44-presud-e-buv-hybnyy` | 1 рядків |
| T-18-024: **Застосунок починається з `0x10000`** — це не випадкове | `presud-18-rozdily-fleshu` | 1 рядків |
| T-35-028: Стандартні швидкості — 100 кГц і 400 кГц. | `presud-35-i2c` | 1 рядків |
| T-36-062: Проміжного стану немає, і «майже рідний» набір пінів | `presud-36-spi` | 1 рядків |
| T-C-013: esptool --port PORT read-flash 0x8000 0x1000 pt.bin # | `presud-c-komandy` | 1 рядків |
| T-04-061: **MCPWM** [[classic]] [[S3]] зроблений спеціально для силової електроніки: | `prochid-04-peryferiya` | 1 рядків |
| T-05-089: У цифровій схемі це локальний запас енергії на | `prochid-05-elektronika` | 1 рядків |
| T-05-017: Світлодіод не можна вмикати без резистора: він не | `prochid-05-elektronika` | 1 рядків |
| T-05-064: **Pull-up** — резистор від піна до 3.3 В. | `prochid-05-elektronika` | 1 рядків |
| T-05-066: **Pull-down** — резистор до землі, дзеркально. | `prochid-05-elektronika` | 1 рядків |
| T-05-067: Хороша новина: у ESP32 підтягувальні резистори **вбудовані** і | `prochid-05-elektronika` | 1 рядків |
| T-05-074: Це не налаштовується — апаратної схеми немає. | `prochid-05-elektronika` | 1 рядків |
| T-05-079: **Open-drain** уміє лише притискати лінію до землі, а | `prochid-05-elektronika` | 1 рядків |
| T-07-055: **Практичне правило:** strapping-піни можна використовувати, але як **виходи**, | `prochid-07-gpio` | 1 рядків |
| T-07-005: При скиданні ROM-бутлоадер має вирішити, звідки завантажуватися. | `prochid-07-gpio` | 1 рядків |
| T-07-006: Джерелом рішення служать кілька звичайних GPIO, стан яких | `prochid-07-gpio` | 1 рядків |
| T-08-004: Це те, що ставлять на власну плату у | `prochid-08-platy` | 1 рядків |
| T-08-024: **Міст USB-UART.** Створює порт у системі. | `prochid-08-platy` | 1 рядків |
| T-11-023: Ця команда додає інструменти в `PATH` і ставить | `prochid-11-idf` | 3 рядків |
| T-12-005: насправді відбувається таке: ESP-IDF стартує звичайним чином, створює | `prochid-12-arduino` | 3 рядків |
| T-12-059: | Прототип уже є, треба довести до виробу | `prochid-12-arduino` | 1 рядків |
| T-12-064: Прототип на Arduino доводиться до виробу підключенням Arduino | `prochid-12-arduino` | 1 рядків |
| T-13-025: `pioarduino` розповсюджується не через реєстр PlatformIO, а архівом | `prochid-13-pio` | 1 рядків |
| T-13-006: Форк називається **pioarduino** і супроводжується спільнотою. | `prochid-13-pio` | 1 рядків |
| T-13-007: Він підтримує актуальні версії Arduino core і нові | `prochid-13-pio` | 1 рядків |
| T-13-029: **`platform`.** Тут — джерело платформи, а не лише | `prochid-13-pio` | 1 рядків |
| T-13-032: Для `pioarduino` пінування — це заміна мітки `stable` | `prochid-13-pio` | 1 рядків |
| T-13-048: Для S3 це не косметика — офіційна платформа | `prochid-13-pio` | 1 рядків |
| T-16-056: Якщо є лише `factory` — беруть його. | `prochid-16-boot` | 1 рядків |
| T-17-064: Воно **вже ввімкнене** за замовчуванням, тож у звичайній | `prochid-17-esptool` | 1 рядків |
| T-17-066: Користь від стиснення там подвійна: менше байтів пройшло | `prochid-17-esptool` | 1 рядків |
| T-17-071: Швидкість тут не той параметр, на якому варто | `prochid-17-esptool` | 1 рядків |
| T-17-149: There was no response.`** | `prochid-17-esptool` | 1 рядків |
| T-18-106: Якщо нова прошивка розрахована на іншу розбивку, вона | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-109: Другий наслідок того самого: якщо ви змінили розбивку, | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-003: Це та частина системи, яку більшість не чіпає | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-009: Типова розбивка для пристрою без OTA виглядає так: | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-010: | Назва | Тип | Підтип | Зсув | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-015: `phy_init` · Тип → data | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-016: `phy_init` · Підтип → phy | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-019: `factory` · Тип → app | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-18-020: `factory` · Підтип → factory | `prochid-18-rozdily-fleshu` | 1 рядків |
| T-19-023: Схема з двох слотів без `factory` — робоча | `prochid-19-ota` | 1 рядків |
| T-19-013: Пристрій виконується зі слоту `ota_0`. | `prochid-19-ota` | 1 рядків |
| T-19-014: Приходить оновлення — воно записується в `ota_1`, при | `prochid-19-ota` | 1 рядків |
| T-22-057: Лог зберігається у файл, а не читається з | `prochid-22-zberezhennya-stanu` | 1 рядків |
| T-23-075: Ніякого струму, ніякого ризику. | `prochid-23-triazh` | 1 рядків |
| T-24-012: Таблиця відповідає на кілька питань одразу. | `prochid-24-chuzha-proshyvka` | 1 рядків |
| T-24-035: Витягти розділ (адреса і розмір — з таблиці | `prochid-24-chuzha-proshyvka` | 1 рядків |
| T-24-015: **Чи є файлова система.** Розділ типу `spiffs`, `littlefs` | `prochid-24-chuzha-proshyvka` | 1 рядків |
| T-25-051: Один тег на файл або на логічний модуль; | `prochid-25-log` | 1 рядків |
| T-27-044: Коли справді варте: складна помилка з пошкодженням пам'яті, | `prochid-27-jtag` | 1 рядків |
| T-30-073: Функція, яка може спрацювати в цей момент — | `prochid-30-struktura` | 1 рядків |
| T-30-023: Розмір стека задається при створенні задачі — числом, | `prochid-30-struktura` | 1 рядків |
| T-30-026: Переповнення стека на мікроконтролері не дає ні винятку, | `prochid-30-struktura` | 1 рядків |
| T-30-027: Задача просто пише за межі свого стека — | `prochid-30-struktura` | 1 рядків |
| T-30-030: Що з'їдає стек несподівано багато: | `prochid-30-struktura` | 1 рядків |
| T-30-085: **32-бітне читання й запис вирівняного слова атомарні** апаратно. | `prochid-30-struktura` | 1 рядків |
| T-30-087: Складніші структури — ні. | `prochid-30-struktura` | 1 рядків |
| T-30-021: **Купа.** `malloc` і `new`. | `prochid-30-struktura` | 1 рядків |
| T-30-041: Купа на ESP32 не однорідна (розділ 03), і | `prochid-30-struktura` | 1 рядків |
| T-30-047: **Не та область.** Буфер для DMA має бути | `prochid-30-struktura` | 1 рядків |
| T-30-086: Тому проста передача одного значення (прапорець, ціле число) | `prochid-30-struktura` | 1 рядків |
| T-30-101: Результат `malloc` перевіряти завжди. | `prochid-30-struktura` | 1 рядків |
| T-30-102: `volatile` не робить операцію атомарною. | `prochid-30-struktura` | 1 рядків |
| T-31-020: Планувальник завжди виконує **найпріоритетнішу готову** задачу. | `prochid-31-freertos` | 1 рядків |
| T-31-027: Це не помилка планувальника, а його правило. | `prochid-31-freertos` | 1 рядків |
| T-31-029: Високий пріоритет означає «швидко відреагувати й заснути», а | `prochid-31-freertos` | 1 рядків |
| T-31-059: Зручно для «дочекатися, поки є і Wi-Fi, і | `prochid-31-freertos` | 1 рядків |
| T-31-036: Двоядерність робить помилки синхронізації **реальними, а не теоретичними**. | `prochid-31-freertos` | 1 рядків |
| T-31-055: **Двійковий семафор** — сигнал «сталося». | `prochid-31-freertos` | 1 рядків |
| T-31-057: **Лічильний семафор** — облік обмеженого ресурсу. | `prochid-31-freertos` | 1 рядків |
| T-31-058: **Група подій** — набір прапорців, на комбінацію яких | `prochid-31-freertos` | 1 рядків |
| T-31-063: **ISR має бути коротким.** Прочитати, покласти в чергу, | `prochid-31-freertos` | 1 рядків |
| T-31-070: Це інструмент для відлагодження, а не для роботи. | `prochid-31-freertos` | 1 рядків |
| T-31-071: Але коли ISR поводиться незрозуміло, а покласти в | `prochid-31-freertos` | 1 рядків |
| T-31-079: Механічний контакт при натисканні дає десятки перемикань за | `prochid-31-freertos` | 1 рядків |
| T-31-090: **Спільна змінна без захисту.** На двох ядрах ламається | `prochid-31-freertos` | 1 рядків |
| T-31-095: Високий пріоритет означає «швидко відреагувати й заснути». | `prochid-31-freertos` | 1 рядків |
| T-31-098: Ніякого логування й пам'яті. | `prochid-31-freertos` | 1 рядків |
| T-31-006: ESP_LOGI(TAG, "температура %.1f", t); | `prochid-31-freertos` | 1 рядків |
| T-33-012: `1ULL` обов'язково: на пінах вище 31 звичайний `1` | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-023: gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5); | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-049: Яскравість світлодіода **не лінійна** щодо коефіцієнта заповнення. | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-051: Плавне згасання, зроблене лінійно, виглядає як різкий стрибок | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-058: Спільна земля обов'язкова (розділ 48). | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-103: Найдешевше і найдієвіше. 2. | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-113: Піни **різні** за сімействами: | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-124: Яскравість світлодіода нелінійна щодо коефіцієнта заповнення. | `prochid-33-peryferiya-kod` | 1 рядків |
| T-33-059: [[classic]] [[S3]] MCPWM зроблений для силової електроніки й | `prochid-33-peryferiya-kod` | 1 рядків |
| T-34-044: На коротких лініях працює і без них; на | `prochid-34-uart` | 1 рядків |
| T-34-048: Якщо обмін не йде — поміняти місцями. | `prochid-34-uart` | 1 рядків |
| T-34-049: Це безпечно і розв'язує половину випадків. | `prochid-34-uart` | 1 рядків |
| T-34-001: UART — найстаріший і найнадійніший спосіб з'єднати два | `prochid-34-uart` | 1 рядків |
| T-34-002: Два дроти, жодного протоколу поверх, працює завжди. | `prochid-34-uart` | 1 рядків |
| T-34-004: [[classic]] ESP32 classic має три контролери UART, S3 | `prochid-34-uart` | 1 рядків |
| T-34-020: **Розмір буфера драйвера має значення.** Дані приходять, поки | `prochid-34-uart` | 1 рядків |
| T-34-030: Звичайний UART працює на десятки сантиметрів. | `prochid-34-uart` | 1 рядків |
| T-34-041: Перемкнути напрямок відразу після нього означає обрізати власну | `prochid-34-uart` | 1 рядків |
| T-34-070: Буфер драйвера робити з запасом: переповнення губить дані | `prochid-34-uart` | 1 рядків |
| T-34-036: Напрямком керує окремий пін `DE`/`RE`: | `prochid-34-uart` | 1 рядків |
| T-35-038: Це замінює логічний аналізатор для питання «чи є | `prochid-35-i2c` | 1 рядків |
| T-35-029: Реальна межа задається **ємністю шини**: що довші проводи | `prochid-35-i2c` | 1 рядків |
| T-35-067: Вбудоване підтягування — не заміна, а рятувальний круг. | `prochid-35-i2c` | 1 рядків |
| T-35-069: Ведучий мусить це витримати. | `prochid-35-i2c` | 1 рядків |
| T-35-071: Повільний ведений (наприклад, датчик, що довго міряє) може | `prochid-35-i2c` | 1 рядків |
| T-35-078: Ведучий, що опитує швидше, ніж ваш обробник готує | `prochid-35-i2c` | 1 рядків |
| T-35-085: **Скоротити проводи**, знизити швидкість до 100 кГц. 6. | `prochid-35-i2c` | 1 рядків |
| T-35-090: Один комплект резисторів на шину; кілька модулів зі | `prochid-35-i2c` | 1 рядків |
| T-35-007: Дві лінії: `SDA` (дані) і `SCL` (тактування). | `prochid-35-i2c` | 1 рядків |
| T-35-070: ESP32 це підтримує, але з обмеженим таймаутом. | `prochid-35-i2c` | 1 рядків |
| T-35-075: Усе вище — про ESP32 у ролі **ведучого**, | `prochid-35-i2c` | 1 рядків |
| T-35-079: Якщо роль веденого потрібна, а встигати не гарантовано | `prochid-35-i2c` | 1 рядків |
| T-39-035: Її ще немає: під'єднання займає від сотень мілісекунд | `prochid-39-wifi` | 1 рядків |
| T-39-037: Саме наявність IP, а не факт під'єднання, означає, | `prochid-39-wifi` | 1 рядків |
| T-39-018: **Канали 12 і 13** доступні не за всіх | `prochid-39-wifi` | 1 рядків |
| T-39-021: Роутер, переведений у режим «тільки WPA3», відрізає такі | `prochid-39-wifi` | 1 рядків |
| T-39-001: Wi-Fi — головна причина, чому беруть ESP32 (розділ | `prochid-39-wifi` | 1 рядків |
| T-39-066: | від −50 дБм | відмінно | | `prochid-39-wifi` | 1 рядків |
| T-39-091: **Не під'єднуватися взагалі.** Для датчика на батарейці ESP-NOW | `prochid-39-wifi` | 1 рядків |
| T-39-098: RSSI логувати завжди: на межі OTA не проходить, | `prochid-39-wifi` | 1 рядків |
| T-46-043: Це незручно і ламається при оновленні бібліотеки; варто | `prochid-46-dyspleyi` | 1 рядків |
| T-46-046: LVGL дає красиві інтерфейси і коштує ресурсів. | `prochid-46-dyspleyi` | 1 рядків |
| T-46-038: **U8g2** — монохромні дисплеї. | `prochid-46-dyspleyi` | 1 рядків |
| T-46-042: Особливість, що дивує: конфігурація (модель дисплея, піни) задається | `prochid-46-dyspleyi` | 1 рядків |
| T-46-055: **Кодування.** Рядки в коді — UTF-8; бібліотека має | `prochid-46-dyspleyi` | 1 рядків |
| T-59-079: Різниця виникає лише тоді, коли в старшому байті | `prochid-59-proj-monitor` | 6 рядків |
| T-A-045: 25 · Обмеження → **DAC1** | `prochid-a-pinouty` | 1 рядків |
| T-A-046: 25 · ADC → ADC2_8 | `prochid-a-pinouty` | 1 рядків |
| T-A-047: 26 · Обмеження → **DAC2** | `prochid-a-pinouty` | 1 рядків |
| T-A-049: 27 · ADC → ADC2_7 | `prochid-a-pinouty` | 1 рядків |
| T-C-075: `-i` обов'язковий: без нього inline-кадри зникають. | `prochid-c-komandy` | 1 рядків |
| T-G-055: | образ | image, binary | | `prochid-g-glosariy` | 1 рядків |
| T-G-063: | семафор | semaphore | | `prochid-g-glosariy` | 1 рядків |
| T-G-064: | м'ютекс | mutex | | `prochid-g-glosariy` | 1 рядків |
| T-G-065: | група подій | event group | | `prochid-g-glosariy` | 1 рядків |
| T-G-066: | переривання | interrupt | | `prochid-g-glosariy` | 1 рядків |
| T-G-068: | критична секція | critical section | | `prochid-g-glosariy` | 1 рядків |
| T-G-074: | атомарна операція | atomic operation | | `prochid-g-glosariy` | 1 рядків |
| T-G-076: | взаємне блокування | deadlock | | `prochid-g-glosariy` | 1 рядків |
| T-G-088: | точка доступу | access point | | `prochid-g-glosariy` | 1 рядків |
| T-G-089: | станція, клієнт | station | | `prochid-g-glosariy` | 1 рядків |
| T-G-090: | канал | channel | | `prochid-g-glosariy` | 1 рядків |
| T-G-091: | рівень сигналу | RSSI, signal strength | | `prochid-g-glosariy` | 1 рядків |
| T-G-094: | дальність | range | | `prochid-g-glosariy` | 1 рядків |
| T-G-098: | топік | topic | | `prochid-g-glosariy` | 1 рядків |
| T-G-099: | підписка | subscription | | `prochid-g-glosariy` | 1 рядків |
| T-G-100: | публікація | publish | | `prochid-g-glosariy` | 1 рядків |
| T-G-101: | сертифікат | certificate | | `prochid-g-glosariy` | 1 рядків |
| T-G-108: | напруга | voltage | | `prochid-g-glosariy` | 1 рядків |
| T-G-117: | роздільність | resolution | | `prochid-g-glosariy` | 1 рядків |
| T-G-150: | UART | Universal Asynchronous Receiver/Transmitter | | `prochid-g-glosariy` | 1 рядків |
| T-G-163: | WDT | Watchdog Timer | | `prochid-g-glosariy` | 1 рядків |
| T-G-146: | OTA | Over-The-Air (оновлення) | | `prochid-g-glosariy` | 1 рядків |
| T-G-153: | I²S | Inter-IC Sound | | `prochid-g-glosariy` | 1 рядків |
| T-G-155: | JTAG | Joint Test Action Group (інтерфейс | `prochid-g-glosariy` | 1 рядків |
| T-H-017: **`github.com/espressif/esp-idf`** — сам фреймворк. | `prochid-h-dzherela` | 1 рядків |
| T-K07-002: Це звіт про те, де саме програма померла. | `prochid-k07-panika` | 1 рядків |
| T-K07-021: Backtrace — це ланцюжок адрес. | `prochid-k07-panika` | 1 рядків |
| T-K07-022: Сам по собі він нечитний; його треба перекласти | `prochid-k07-panika` | 1 рядків |
| T-K07-027: Інструмент **свій для кожної архітектури**: [[S3]] — `xtensa-esp32s3-elf-addr2line`, | `prochid-k07-panika` | 1 рядків |
| T-K07-035: Якщо причина паніки лишилася, це стає boot loop: | `prochid-k07-panika` | 1 рядків |
| T-K07-020: Найчастіше — результат `malloc`, який не перевірили. | `prochid-k07-panika` | 1 рядків |
| T-K07-024: Вручну, коли лог знято з чужого пристрою і | `prochid-k07-panika` | 1 рядків |
| T-K07-031: `.elf` того самого збирання, що й `.bin`, — | `prochid-k07-panika` | 1 рядків |
| T-K08-021: 6 · Що робити → перший дамп після | `prochid-k08-symptomy` | 1 рядків |
| T-K08-026: 8 · Найчастіша причина → немає підтягування або | `prochid-k08-symptomy` | 1 рядків |
| T-K08-011: 3 · Найчастіша причина → адреса бутлоадера не | `prochid-k08-symptomy` | 1 рядків |
| T-K08-019: 6 · Симптом → Boot loop | `prochid-k08-symptomy` | 1 рядків |
| T-K08-020: 6 · Найчастіша причина → паніка в застосунку | `prochid-k08-symptomy` | 1 рядків |
| T-K08-035: 11 · Найчастіша причина → вони зайняті флешем | `prochid-k08-symptomy` | 6 рядків |
| T-K09-004: | **6, 7, 8, 9, 10, 11** | | `prochid-k09-pinouty` | 6 рядків |
| T-Z-010: паспорт виробу — 224, 310–311, 313, 398 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-011: серво — 32, 54, 203–204, 207, 274–277, 369, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-013: таблиця розділів — 15, 18, 129, 133, 135, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-038: DMA — 50, 52, 55–56, 188, 220, 222, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-055: esp_deep_sleep_start — 68, 100, 338, 340, 344 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-109: GPIO12 — 14, 17, 28, 71–72, 74, 77, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-110: GPIO15 — 14, 17–18, 28, 71, 142, 173, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-111: GPIO17 — 67, 73–75, 206, 335 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-112: GPIO18 — 75, 172, 206, 335 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-113: GPIO2 — 13–14, 17, 28, 71–72, 142, 335–337, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-114: GPIO21 — 149, 310, 326, 335 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-115: GPIO22 — 149, 310, 326, 335 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-116: GPIO25 — 75, 206–207, 310, 349–350 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-117: GPIO26 — 74–75, 206–207, 349–350 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-118: GPIO3 — 14, 72, 75, 335, 337 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-119: GPIO32 — 53, 74–75, 182, 389 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-120: GPIO34 — 53, 62, 74, 77, 182, 335, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-121: GPIO4 — 9, 17, 149, 310, 335, 349, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-123: GPIO6 — 21, 27, 53, 73, 76, 154, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-124: GPIO8 — 13–14, 24, 72–73, 118, 205, 326, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-125: GPIO9 — 13–14, 17, 24, 72–73, 82, 118, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-128: gpio_isr_handler — 50, 189 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-149: MALLOC_CAP_DMA — 188, 220, 222, 281, 368 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-151: MALLOC_CAP_SPIRAM — 153, 188–189 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-024: bootloader — 5, 15, 18, 26, 98, 117–120, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-044: ESP-NOW — 69, 231, 233, 236, 240, 246–249, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-048: ESP32-S2 — 45–46, 118, 242 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-049: ESP32-S3 — 7, 23, 39, 44, 118, 127, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-054: ESP8266 — 7, 18, 21, 80, 123, 152, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-144: I²S — 40, 53–56, 280–281, 388, 399 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-153: MCP23017 — 57, 76, 365, 386 | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-173: SR04 — 27, 34, 61, 258, 262, 264, | `prochid-z-pokazhchyk` | 1 рядків |
| T-Z-194: WS2812 — 54–55, 200, 204, 207, 388 | `prochid-z-pokazhchyk` | 1 рядків |

## нема чого звіряти — 670

| Доказ | Файл | Деталі |
|---|---|---|
| T-E-065: SX1262 · Бібліотека → RadioLib | `cherga-a-e-interfeysy` | немає придатних уривків |
| T-00-055: Чотири типи блоків трапляються по всьому тексту. | `cherga-c-00-pro-dovidnyk` | немає придатних уривків |
| T-00-014: Замість людської вичитки застосовано **автоматизовану перевірку**, і зроблено | `cherga-c-00-pro-dovidnyk` | немає придатних уривків |
| T-00-089: Мінімальний комплект, з яким можна робити все, що | `cherga-c-00-pro-dovidnyk` | немає придатних уривків |
| T-01-011: **Плата розробки.** Модуль плюс USB-роз'єм, міст USB-UART, стабілізатор, | `cherga-c-01-platforma` | немає придатних уривків |
| T-02-018: Ядер · ESP32 → **2** | `cherga-c-02-chipy` | немає придатних уривків |
| T-04-057: Керування адресними світлодіодами WS2812, де таймінги вимірюються сотнями | `cherga-c-04-peryferiya` | немає придатних уривків |
| T-05-078: Два таких виходи на одному дроті, що хочуть | `cherga-c-05-elektronika` | немає придатних уривків |
| T-05-116: Статична електрика — це кіловольти. | `cherga-c-05-elektronika` | немає придатних уривків |
| T-06-113: На платі розробки живуть USB-міст, стабілізатор і світлодіод | `cherga-c-06-zhyvlennya` | немає придатних уривків |
| T-06-116: **LDO** (лінійний) — стоїть майже на всіх платах | `cherga-c-06-zhyvlennya` | немає придатних уривків |
| T-08-051: Найдешевший спосіб отримати мережеву камеру, і найнезручніша плата | `cherga-c-08-platy` | немає придатних уривків |
| T-08-033: **ESP32-DevKitC V4** — офіційна плата Espressif на 38 | `cherga-c-08-platy` | немає придатних уривків |
| T-08-027: **Схема авторесету.** Два транзистори, керовані `DTR` і `RTS`. | `cherga-c-08-platy` | немає придатних уривків |
| T-09-036: Сьогодні це рідше, але сам факт: якщо плата | `cherga-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-008: На типовій платі розробки цей міст уже стоїть | `cherga-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-043: **Порт має інше ім'я.** `/dev/ttyACM0` замість `/dev/ttyUSB0` у | `cherga-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-030: **CH9102 з'являється як `/dev/ttyACM0`, а не `ttyUSB0`**: у | `cherga-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-110: На S3 і C3 порт називається `ttyACM`, драйвер | `cherga-c-09-pidklyuchennya` | немає придатних уривків |
| T-16-021: Світлодіод із резистором на `GPIO0`, датчик, що тримає | `cherga-c-16-boot` | немає придатних уривків |
| T-16-005: Він стартує завжди, незалежно від того, що у | `cherga-c-16-boot` | немає придатних уривків |
| T-16-011: Головне практичне: **етапи 2 і 3 живуть у | `cherga-c-16-boot` | немає придатних уривків |
| T-16-077: Дивитися треба **найперший** дамп після подачі живлення, а | `cherga-c-16-boot` | немає придатних уривків |
| T-17-131: Повторюється стабільно на тій самій адресі — підозра | `cherga-c-17-esptool` | немає придатних уривків |
| T-18-075: Швидкість при заповненні · FAT → рівна | `cherga-c-18-rozdily-fleshu` | немає придатних уривків |
| T-18-062: Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, | `cherga-c-18-rozdily-fleshu` | немає придатних уривків |
| T-19-069: Мінімум, який реально працює: HTTPS із перевіркою сертифіката | `cherga-c-19-ota` | немає придатних уривків |
| T-21-079: Цей файл відповідає на питання, які виникають через | `cherga-c-21-seriyna` | немає придатних уривків |
| T-26-042: Наслідок практичний і неприємний: лог з C3, знятий | `cherga-c-26-zboyi` | немає придатних уривків |
| T-37-007: Найпоширеніший датчик температури в саморобній техніці. | `cherga-c-37-onewire` | немає придатних уривків |
| T-38-087: Один вузол на шині дає помилки: підтверджувати нема | `cherga-c-38-can` | немає придатних уривків |
| T-38-035: **Швидкість має бути однаковою в усіх вузлів.** Один | `cherga-c-38-can` | немає придатних уривків |
| T-39-023: **Тільки один канал одночасно.** Звідси обмеження APSTA вище | `cherga-c-39-wifi` | немає придатних уривків |
| T-COM-036: A4988 · Замінники → DRV8825 (більший струм, мікрокрок | `cherga-c-components-2026-08` | немає придатних уривків |
| T-COM-076: | **470 мкФ** | біля роз'єму живлення | | `cherga-c-components-2026-08` | немає придатних уривків |
| T-E-096: PMS5003, SDS011 · Що дає → пилові частинки | `cherga-c-e-interfeysy` | немає придатних уривків |
| T-E-100: A6 / SIM800 / SIM7600 · Що дає | `cherga-c-e-interfeysy` | немає придатних уривків |
| T-E-137: A4988 / DRV8825 · Як → `STEP` + | `cherga-c-e-interfeysy` | немає придатних уривків |
| T-K03-016: немає окремого чипа · Міст → native USB | `cherga-c-k03-pidkl` | немає придатних уривків |
| T-REG-021: **LoRa-модулі продаються на різні частоти**, і не всі | `cherga-c-regulatory-2026-08` | немає придатних уривків |
| T-REG-010: **Потужність передавача.** Обмежується як випромінювана потужність (з урахуванням | `cherga-c-regulatory-2026-08` | немає придатних уривків |
| Робочий діапазон SF у LoRa — 7…12, а SF6 окремий режим | `m2-03-semtech-lora` | немає URL |
| Ширша смуга — швидше й менш далеко | `m2-03-semtech-lora` | немає URL |
| RFM69 не є LoRa-модулем | `m2-03-semtech-lora` | немає URL |
| SX1262 ефективніший за SX1276 — числа не отримано | `m2-03-semtech-lora` | немає придатних уривків |
| DS18B20 — діапазон, роздільність і час перетворення | `m2-04-ds18b20` | немає URL |
| Унікальний 64-бітний код і кількість пристроїв на лінії | `m2-04-ds18b20` | немає URL |
| Підтягування 4.7 кОм на лінії 1-Wire | `m2-04-ds18b20` | немає URL |
| Чому 4.7 кОм годиться на 100 кГц і не годиться на 400 кГц | `m2-05-i2c-pidtyaguvannya` | немає URL |
| Ємність шини I²C нормується, і саме вона обмежує довжину | `m2-05-i2c-pidtyaguvannya` | немає URL |
| Робоча напруга живлення — 3.0–3.6 В, типова 3.3 В | `m2-06-napruga-mezhi` | немає URL |
| Джерело мусить давати щонайменше 0.5 А за datasheet | `m2-06-napruga-mezhi` | немає URL |
| CP2102 — Silicon Labs, драйвер cp210x у ядрі Linux | `m2-07-mosty-usb-uart` | немає URL |
| CH340 і CH341 — WCH, драйвер ch341 у ядрі Linux | `m2-07-mosty-usb-uart` | немає URL |
| FT232RL — FTDI, драйвер ftdi_sio у ядрі Linux | `m2-07-mosty-usb-uart` | немає URL |
| CH9102 у ядрі є, але через cdc_acm, а не ch341 | `m2-07-mosty-usb-uart` | немає URL |
| PCF8574 — вісім ліній, розширювач по I²C | `m2-08-dyspleyi-rozshyryuvachi` | немає URL |
| MCP23017 — шістнадцять ліній | `m2-08-dyspleyi-rozshyryuvachi` | немає URL |
| ILI9341 — 240×320, інтерфейс SPI | `m2-08-dyspleyi-rozshyryuvachi` | немає URL |
| HC-SR04 — діапазон 2-400 см | `m2-09-hc-sr04` | немає URL |
| HC-SR04 живиться від 5 В, тому ECHO дає 5 В | `m2-09-hc-sr04` | немає URL |
| DS3231 і BH1750 — джерела недосяжні з цієї мережі | `m2-09-hc-sr04` | немає придатних уривків |
| ATmega328P — немає радіомодуля серед периферії | `m2-10-rp2040-atmega` | немає URL |
| ATmega328P — 16 МГц серед «типових» тактових частот | `m2-10-rp2040-atmega` | немає URL |
| ATmega328P — 2 КБ внутрішньої SRAM | `m2-10-rp2040-atmega` | немає URL |
| ATmega328P — немає операційної системи серед можливостей чипа | `m2-10-rp2040-atmega` | немає URL |
| ATmega328P — час старту вимірюється циклами й мілісекундами | `m2-10-rp2040-atmega` | немає URL |
| ATmega328P — струм у Power-down вимірюється мікроамперами | `m2-10-rp2040-atmega` | немає URL |
| ATmega328P — детермінована й мінімальна затримка переривання | `m2-10-rp2040-atmega` | немає URL |
| Ціна плати Arduino Uno — не факт із datasheet кристала | `m2-10-rp2040-atmega` | немає придатних уривків |
| TP4056 — заряджання фіксоване на 4.2 В | `m2-11-akumulyator` | немає URL |
| TP4056 — струм заряджання задає резистор, 1.2 кОм дає 1 А | `m2-11-akumulyator` | немає URL |
| TP4056 продається із захистом DW01 — два транзистори в типовій схемі | `m2-11-akumulyator` | немає URL |
| TP4056 — паралельне навантаження заважає визначенню кінця заряду | `m2-11-akumulyator` | немає URL |
| SSD1306 — інтерфейс I²C або SPI, обидва пін-вибіркові | `m2-12-oled-ssd1306` | немає URL |
| SSD1306 — монохромний дисплей | `m2-12-oled-ssd1306` | немає URL |
| Raspberry Pi 4 — Wi-Fi і Bluetooth на борту | `m2-14-raspberry-pi` | немає URL |
| Raspberry Pi 4 — ядро на 1.5 ГГц, більше за 1 ГГц | `m2-14-raspberry-pi` | немає URL |
| Raspberry Pi 4 — гігабайти LPDDR4 SDRAM | `m2-14-raspberry-pi` | немає URL |
| Raspberry Pi 4 — Linux, «Mature Linux software stack» | `m2-14-raspberry-pi` | немає URL |
| Raspberry Pi — час завантаження поза межами обох документів | `m2-14-raspberry-pi` | немає придатних уривків |
| Raspberry Pi — жодної згадки режиму сну там, де про живлення говорять детально | `m2-14-raspberry-pi` | немає URL |
| Raspberry Pi — «реальний час» поза тим, що документи оцінюють | `m2-14-raspberry-pi` | немає придатних уривків |
| Raspberry Pi 5 — офіційний прайс-лист, висока ціна проти мікроконтролерних плат | `m2-14-raspberry-pi` | немає придатних уривків |
| «Проти Raspberry Pi» — редакційна рамка, не технічне твердження | `m2-14-raspberry-pi` | немає придатних уривків |
| «Найчастіша помилка вибору» — редакційна порада, не факт | `m2-14-raspberry-pi` | немає придатних уривків |
| Ємність ходових елементів 18650 — від 2500 до 3500 мА·год | `m2-15-element-18650` | немає URL |
| Номінальна напруга 18650 — 3.6 В, а не 3.7 | `m2-15-element-18650` | немає URL |
| Паспортна межа розряду 18650 — 2.5 В, а не 3.0 | `m2-15-element-18650` | немає URL |
| Заряджання 18650 нижче 0 °C — Panasonic NCR18650B і LG MJ1 | `m2-15-element-18650` | немає URL |
| SHT3x / SHT4x — точна вологість, ±1–1.5 %RH | `m2-16-datchyky-dodatok-e` | немає URL |
| MPU6050 — акселерометр і гіроскоп на одному кристалі | `m2-16-datchyky-dodatok-e` | немає URL |
| SHT3x / SHT4x — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-16-datchyky-dodatok-e` | немає придатних уривків |
| MPU6050 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-16-datchyky-dodatok-e` | немає придатних уривків |
| Безсвинцевий потребує на 30-40 °C більше | `m2-17-pripiy-i-ip` | немає URL |
| DS3231 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| INA219 / INA226 — обидва повідомляють струм і напругу | `m2-18-dodatok-e-reshta` | немає URL |
| INA219 / INA226 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| PCF8574 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| MCP23017 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| ST7789 — однокристальний драйвер TFT | `m2-18-dodatok-e-reshta` | немає URL |
| ILI9341 — однокристальний драйвер TFT | `m2-18-dodatok-e-reshta` | немає URL |
| ILI9341 — SPI Mode 0 (CPHA=0, зразок на першому фронті) | `m2-18-dodatok-e-reshta` | немає URL |
| ILI9341 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| ST7789 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| MCP2515 — окремий CAN-контролер по SPI, Mode 0 підтримується | `m2-18-dodatok-e-reshta` | немає URL |
| MCP2515 — стендалон CAN-контролер із SPI | `m2-18-dodatok-e-reshta` | немає URL |
| MCP2515 — «Бібліотека → —» це посилання на вбудований контролер ESP32, не факт про MCP2515 | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| MAX31855 / MAX6675 — обидва термопарні перетворювачі | `m2-18-dodatok-e-reshta` | немає URL |
| MAX31855 / MAX6675 — SPI Mode 0 в обох референсних бібліотеках | `m2-18-dodatok-e-reshta` | немає URL |
| MAX31855 / MAX6675 — «Бібліотека → Adafruit MAX31855» не працює з MAX6675 | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| HC-SR04 — тригер і ECHO, 5 В TTL | `m2-18-dodatok-e-reshta` | немає URL |
| HC-SR04 — «Розділ → 45» це внутрішнє посилання книги, не факт про модуль | `m2-18-dodatok-e-reshta` | немає придатних уривків |
| Червоний LED — падіння близько 2 В | `m2-19-elektronika-05` | немає URL |
| Резистор 220–330 Ом для червоного LED — арифметика закону Ома | `m2-19-elektronika-05` | немає придатних уривків |
| Синій/білий LED — падіння близько 3 В | `m2-19-elektronika-05` | немає URL |
| Логічні рівні ESP32 — близько 0 В / близько 3.3 В | `m2-19-elektronika-05` | немає URL |
| Знижувати 5 В обов'язково — абсолютний максимум входу 3.6 В | `m2-19-elektronika-05` | немає URL |
| 3.3 В — практична межа GPIO, консервативніша за паспортну 3.6 В | `m2-19-elektronika-05` | немає URL |
| I²C — внутрішнє підтягування ESP32 (45 кОм) заслабке, потрібні зовнішні резистори | `m2-19-elektronika-05` | немає URL |
| WROOM-32E — 100 нФ близько до виводів живлення в референсній схемі | `m2-19-elektronika-05` | немає URL |
| MOSFET логічного рівня — офіційний термін і поріг відкривання | `m2-19-elektronika-05` | немає URL |
| Звичайний MOSFET при 3.3 В — поріг близько, відкривається частково | `m2-19-elektronika-05` | немає URL |
| Величезна кількість модулів «для Arduino» на 5 В — ринкове спостереження, не з документа | `m2-19-elektronika-05` | немає придатних уривків |
| Конденсатор 470 мкФ — «найдешевше рішення найчастішої проблеми» — авторська оцінка | `m2-19-elektronika-05` | немає придатних уривків |
| «5 В на GPIO. Абсолютний лідер.» — рейтинг причин спалених плат, авторська оцінка | `m2-19-elektronika-05` | немає придатних уривків |
| «100 нФ і 470 мкФ знімають більшість збоїв» — авторський підсумок, не вимірювана частка | `m2-19-elektronika-05` | немає придатних уривків |
| Половина модулів «для Arduino» — спостереження за ринком, не специфікація | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| 5 В на GPIO — понад абсолютний максимум входу ESP32 | `m2-20-rivni-i-klyuchi` | немає URL |
| Таблиця рішень К14 — авторська схема категоризації модулів, не факт із джерела | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Немає стабілізатора · Сигнали» | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Є стабілізатор 5→3.3 · Живлення» | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Є стабілізатор і конвертер · Живлення» | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Є стабілізатор і конвертер · Сигнали» | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| «Більшість 5-вольтових входів бере 3.3 В за одиницю» — узагальнення про чужі пристрої | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| 5 В на вхід ESP32 — зниження обов'язкове через абсолютний максимум | `m2-20-rivni-i-klyuchi` | немає URL |
| LV/HV-конвертер — маркування модуля, не характеристика транзистора | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Заголовок таблиці «Часті винуватці 5 В» — назви колонок, не факт | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| 74HC на 5 В — вихід близький до напруги живлення, вище за абсолютний максимум ESP32 | `m2-20-rivni-i-klyuchi` | немає URL |
| LED до 10 мА через резистор — IOH ESP32 з великим запасом | `m2-20-rivni-i-klyuchi` | немає URL |
| LED до 10 мА — «вистачає піна», та сама причина | `m2-20-rivni-i-klyuchi` | немає URL |
| MOSFET логічного рівня IRLZ44N — характеризований і при 4–5 В, не лише 10 В | `m2-20-rivni-i-klyuchi` | немає URL |
| 10 В на затворі — контрольна точка, від якої відлічує сам IRLZ44N | `m2-20-rivni-i-klyuchi` | немає URL |
| Перегрів звичайного MOSFET від 3.3 В — не звірено цим набором джерел | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Резистор 100–220 Ом — межа кидка струму в межах можливостей піна ESP32 | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| 10 кОм від затвора на землю — стандартна практика, не звірена окремим джерелом | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Реле на 5 В — спостереження за ринком модулів | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Нестабільна робота реле від 3.3 В — не звірено джерелами цього кроку | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Мережеве живлення 230 В — редакційна межа теми, не факт | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Найчастіша задача з'єднання ESP32 і 5-вольтового пристрою — емпіричне узагальнення | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| «Напрямок 3.3 → 5 В» — той самий випадок узагальнення про чужі пристрої | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| «Напрямок 5 → 3.3 В» — зниження обов'язкове через абсолютний максимум ESP32 | `m2-20-rivni-i-klyuchi` | немає URL |
| Схема LV/HV-конвертера в розділі 47 — та сама межа джерел, що й у К14 | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Дешевизна й раптова потреба в конвертері рівнів — практична порада, не факт | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| 10 кОм від затвора на землю (підсумок) — той самий випадок, що й основний виклад | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Релейні модулі — 5 В та інверсна логіка, спостереження за ринком | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| «Два джерела працюють одне проти одного» при одночасній подачі на 3V3 і зовнішньому вході — загальний електротехнічний принцип, не цитата з datasheet | `m2-21-zhyvlennya-06` | немає придатних уривків |
| Пін `3V3` модуля — це напряму `VDD33`, без проміжного стабілізатора на самому модулі | `m2-21-zhyvlennya-06` | немає URL |
| «Тобто блок на 500 мА формально відповідає вимозі — і все одно найпоширеніша помилка» — частка «найпоширеніша» це практика/спостереження, а не показник із datasheet | `m2-21-zhyvlennya-06` | немає придатних уривків |
| «Дешевий блок... просідає задовго до цього» — пояснення поведінки дешевих блоків живлення, практика без джерела | `m2-21-zhyvlennya-06` | немає придатних уривків |
| «Тому 1 А — це не суперечність datasheet, а запас на якість джерела» — авторський підсумок аргументації, спирається на практичне (E), а не лише документне твердження | `m2-21-zhyvlennya-06` | немає придатних уривків |
| Конденсатор 470 мкФ між 3V3 і GND — стандартна практика розв'язки живлення, номінал не з datasheet ESP32 | `m2-21-zhyvlennya-06` | немає придатних уривків |
| «Окреме джерело від 1 А» і «знизити пікове споживання» — поради з порядку дешевизни, практика | `m2-21-zhyvlennya-06` | немає придатних уривків |
| 0.086 + 0.02 ≈ 0.106 мА·год — арифметика бюджету енергії за прикладом книги | `m2-21-zhyvlennya-06` | немає придатних уривків |
| «Шунт і осцилограф. Єдиний спосіб побачити реальну картину...» — методика вимірювання, авторська оцінка «єдиний спосіб» | `m2-21-zhyvlennya-06` | немає придатних уривків |
| LDO — третина енергії йде в нагрів при вході 5 В, виході 3.3 В — арифметика ККД | `m2-21-zhyvlennya-06` | немає придатних уривків |
| «Лікується зовнішнім живленням 3.3 В на відповідний пін, минаючи бортовий стабілізатор» — та сама архітектура, що й пін 3V3 напряму на VDD33 | `m2-21-zhyvlennya-06` | немає URL |
| «Джерело має тягнути 1 А... платить воно за піки» — той самий висновок з IVDD і пікового струму передачі, що вже встановлено класом B | `m2-21-zhyvlennya-06` | немає URL |
| «Конденсатор 470 мкФ... найдешевше розв'язання найчастішої проблеми в книзі» — авторська оцінка, порівняльне судження | `m2-21-zhyvlennya-06` | немає придатних уривків |
| DHT11, DHT22 — власний протокол і паспортна точність | `m2-22-vkladysh-components` | немає URL |
| HC-SR04 — 5 В на ECHO підтверджено, «м'які поверхні» — ні | `m2-22-vkladysh-components` | немає URL |
| не L298N — застарів і втрачає ~2 В на собі | `m2-22-vkladysh-components` | немає URL |
| Buck-boost проти LDO — використання ємності батареї | `m2-22-vkladysh-components` | немає URL |
| ACS712 — «беріть INA219/INA226» — редакційна порада | `m2-22-vkladysh-components` | немає придатних уривків |
| HC-SR04 — «беріть VL53L0X» — редакційна порада | `m2-22-vkladysh-components` | немає придатних уривків |
| Фейковий CP2102/FT232 — ознака без паспортного числа | `m2-22-vkladysh-components` | немає придатних уривків |
| 220–330 Ом резистора світлодіода — узгоджується з реальним VF | `m2-22-vkladysh-components` | немає URL |
| 4.7 кОм — підтягування 1-Wire підтверджено, I²C — похідне | `m2-22-vkladysh-components` | немає URL |
| 10 кОм — підтягування входів і затвор MOSFET на землю — практика без чипа | `m2-22-vkladysh-components` | немає придатних уривків |
| 100–220 Ом послідовно з затвором — практика без чипа | `m2-22-vkladysh-components` | немає придатних уривків |
| 120 Ом термінаторів RS-485/CAN — стандарт, недосяжний з мережі | `m2-22-vkladysh-components` | немає придатних уривків |
| 100 нФ біля кожної мікросхеми — загальна практика, не паспорт | `m2-22-vkladysh-components` | немає придатних уривків |
| 470 мкФ біля роз'єму живлення — загальна практика, не паспорт | `m2-22-vkladysh-components` | немає придатних уривків |
| DS18B20 — ±0.5 °C на один датчик, звідси розбіжність до 1 °C у двох справних | `m2-22-vkladysh-components` | немає URL |
| DS18B20 — ±2 °C поза −10…+85 °C, тому міряти в кімнатній воді | `m2-22-vkladysh-components` | немає URL |
| Що тримати в запасі — редакційний список, не факт | `m2-22-vkladysh-components` | немає придатних уривків |
| DS3231 має власну батарейку — джерело недосяжне з цієї мережі | `m2-23-proekty-60-62` | немає придатних уривків |
| DS3231 — кількість модуля в BOM, не факт про мікросхему | `m2-23-proekty-60-62` | немає придатних уривків |
| Резистори 4.7 кОм для I²C і 1-Wire — номінал, який справді рекомендують обидва джерела | `m2-23-proekty-60-62` | немає URL |
| Звичайний LDO й buck-boost — межі роботи без конкретної мікросхеми | `m2-23-proekty-60-62` | немає придатних уривків |
| Дільник напруги на 200 кОм — арифметика верна, але «на порядок» перебільшує | `m2-23-proekty-60-62` | немає придатних уривків |
| Бюджет енергії логера — множення часу на струм | `m2-23-proekty-60-62` | немає придатних уривків |
| Струм на фазах бюджету — оцінні величини системи, не паспортні числа однієї деталі | `m2-23-proekty-60-62` | немає придатних уривків |
| Тест на 3.1 В — узгоджено з порогом коду й нижньою межею buck-boost | `m2-23-proekty-60-62` | немає URL |
| Оптопара не гарантує сумісності з 3.3 В — падіння струму світлодіода | `m2-23-proekty-60-62` | немає придатних уривків |
| Перевірка модуля до монтажу й запасний варіант — транзисторний ключ | `m2-23-proekty-60-62` | немає придатних уривків |
| Резистор утримує керувальний GPIO при завантаженні — усі піни output-disabled під час reset | `m2-23-proekty-60-62` | немає URL |
| GPIO34 — input-only, без внутрішнього підтягування; зовнішній резистор для поплавкового вимикача | `m2-23-proekty-60-62` | немає URL |
| CP2102 · Windows — драйвер від SiLabs | `m2-25-pidklyuchennya-09` | немає URL |
| CH340 · Windows — драйвер від WCH | `m2-25-pidklyuchennya-09` | немає URL |
| CH9102 · Windows — окремий драйвер (не CH340) | `m2-25-pidklyuchennya-09` | немає придатних уривків |
| FT232RL · Windows — драйвер FTDI | `m2-25-pidklyuchennya-09` | немає придатних уривків |
| CH9102 — окрема пастка (схожий на CH340, але інший драйвер) | `m2-25-pidklyuchennya-09` | немає придатних уривків |
| Драйвер CH340 на CH9102 — не працює | `m2-25-pidklyuchennya-09` | немає придатних уривків |
| Різні плати — різні імена портів | `m2-25-pidklyuchennya-09` | немає придатних уривків |
| S3 та C3 — USB-контролер на кристалі | `m2-25-pidklyuchennya-09` | немає придатних уривків |
| CH9102 — окремий драйвер від CH340 (резюме) | `m2-25-pidklyuchennya-09` | немає придатних уривків |
| K03 CH9102/CH9102F · Windows окремий драйвер | `m2-26-k03-i-platy` | немає придатних уривків |
| Стабілізатор (LDO) · 3.3 В із 5 В | `m2-26-k03-i-platy` | немає придатних уривків |
| USB-міст на платі · CP2102, CH340, CH9102 | `m2-26-k03-i-platy` | немає придатних уривків |
| ESP32-CAM · немає USB-роз'єму | `m2-26-k03-i-platy` | немає придатних уривків |
| Фейковий USB-міст · клони CP2102 і FT232 | `m2-26-k03-i-platy` | немає придатних уривків |
| Піни для прошивки на власній платі | `m2-26-k03-i-platy` | немає придатних уривків |
| ST7789 — 4-line SPI інтерфейс | `m2-27-dyspleyi-46` | немає URL |
| ST7789 — 65K кольорів у режимі RGB 5-6-5 | `m2-27-dyspleyi-46` | немає URL |
| ILI9341 — 4-line SPI інтерфейс | `m2-27-dyspleyi-46` | немає URL |
| ILI9341 — 65K кольорів у режимі RGB 5-6-5 | `m2-27-dyspleyi-46` | немає URL |
| ST7789 · Розмір → 1.3–2.4" | `m2-27-dyspleyi-46` | немає придатних уривків |
| ST7789 · Особливості → яскравий, швидкий | `m2-27-dyspleyi-46` | немає придатних уривків |
| ILI9341 · Розмір → 2.4–3.2" | `m2-27-dyspleyi-46` | немає придатних уривків |
| ILI9341 · Особливості → великий, класика | `m2-27-dyspleyi-46` | немає придатних уривків |
| Альтернативи до матричної клавіатури 4×4 | `m2-27-dyspleyi-46` | немає придатних уривків |
| DHT11 - дешевий датчик температури й вологості | `m2-28-sensory-45` | немає придатних уривків |
| DHT11 — роздільність вологості 1%RH | `m2-28-sensory-45` | немає URL |
| HC-SR04 — ультразвуковий далекомір, 2–400 см | `m2-28-sensory-45` | немає URL |
| HC-SR04 — 5 В на виводі ECHO | `m2-28-sensory-45` | немає URL |
| HC-SR04 — 5 В на ECHO обов'язковий дільник | `m2-28-sensory-45` | немає URL |
| INA219 — вимірювання струму й напруги по I²C | `m2-28-sensory-45` | немає URL |
| Калібрування датчиків за відомою точкою | `m2-28-sensory-45` | немає придатних уривків |
| GPS модулі NMEA — UART, текстові речення | `m2-28-sensory-45` | немає придатних уривків |
| Типовий номінал 4.7 кОм для підтягування I²C | `m2-29-i2c-35` | немає URL |
| Три модулі по 4.7 кОм дають близько 1.6 кОм паралельно | `m2-29-i2c-35` | немає URL |
| На метрові дистанції I²C не призначений; RS-485 або менші резистори | `m2-29-i2c-35` | немає URL |
| Зовнішні 4.7 кОм обов'язкові для сумарного навантаження | `m2-29-i2c-35` | немає придатних уривків |
| Без зовнішніх резисторів 4.7 кОм I²C взагалі не працює | `m2-29-i2c-35` | немає URL |
| Вхідна напруга на роз'ємі від USB — норма 5 В ±5 % | `m2-31-kartka-k13` | немає придатних уривків |
| 3.3 В на холостому ході — норма 3.2–3.4 В | `m2-31-kartka-k13` | немає URL |
| Окреме джерело від 1 А — не 500 мА, тому що платити треба за піки | `m2-31-kartka-k13` | немає URL |
| Джерело для ESP32 з Wi-Fi — щонайменше 1 А, навіть якщо середнє споживання сто міліампер | `m2-31-kartka-k13` | немає URL |
| `rst:0xf` — симптом просідання живлення | `m2-32-symptomy-b` | немає придатних уривків |
| Перезавантаження при Wi-Fi — джерело не тягне піків | `m2-32-symptomy-b` | немає URL |
| Стабілізатор гарячий — перевантаження або слабкий клон | `m2-32-symptomy-b` | немає придатних уривків |
| I²C не знаходить пристрій — немає підтягування | `m2-32-symptomy-b` | немає придатних уривків |
| RS-485: помилки на довгій лінії — потрібни термінатори | `m2-32-symptomy-b` | немає придатних уривків |
| Реле вмикається при старті — вхід ключа висить при завантаженні | `m2-32-symptomy-b` | немає придатних уривків |
| Реле не спрацьовує — модуль керування на 5 В | `m2-32-symptomy-b` | немає придатних уривків |
| Реле не спрацьовує — дія: живити модуль від 5 В | `m2-32-symptomy-b` | немає придатних уривків |
| 74HC595 — зсувний регістр, вихід | `m2-33-gpio-07` | немає URL |
| 74HC165 — зсувний регістр, вхід | `m2-33-gpio-07` | немає URL |
| CD4051 — аналоговий мультиплексор, восьми каналів | `m2-33-gpio-07` | немає URL |
| T-A-123: посилання на розділ 07 | `m2-33-gpio-07` | немає придатних уривків |
| T-F-006: інсталятор й перше збирання | `m2-34-dodatky-reshta` | немає придатних уривків |
| T-F-014: .elf файли й backtrace | `m2-34-dodatky-reshta` | немає придатних уривків |
| T-F-012: драйвери USB-UART (CP2102, CH340, CH9102) | `m2-34-dodatky-reshta` | немає URL |
| T-K10-039: інтерфейси /dev/ttyUSB* і /dev/ttyACM* | `m2-34-dodatky-reshta` | немає URL |
| manual/60-proj-loger.md: відсутні факти про мікросхеми | `m2-34-dodatky-reshta` | немає придатних уривків |
| Raspberry Pi 4 — Wi-Fi і Bluetooth на борту | `m2-42-raspberry` | немає URL |
| Raspberry Pi 4 — ядро на 1.5 ГГц, більше за 1 ГГц | `m2-42-raspberry` | немає URL |
| Raspberry Pi 4 — гігабайти LPDDR4 SDRAM | `m2-42-raspberry` | немає URL |
| Raspberry Pi 4 — Linux, «Mature Linux software stack» | `m2-42-raspberry` | немає URL |
| Raspberry Pi — час завантаження поза межами обох документів | `m2-42-raspberry` | немає придатних уривків |
| Raspberry Pi — жодної згадки режиму сну там, де про живлення говорять детально | `m2-42-raspberry` | немає URL |
| Raspberry Pi — «реальний час» поза тим, що документи оцінюють | `m2-42-raspberry` | немає придатних уривків |
| Raspberry Pi 5 — офіційний прайс-лист, висока ціна проти мікроконтролерних плат | `m2-42-raspberry` | немає придатних уривків |
| «Проти Raspberry Pi» — редакційна рамка, не технічне твердження | `m2-42-raspberry` | немає придатних уривків |
| «Найчастіша помилка вибору» — редакційна порада, не факт | `m2-42-raspberry` | немає придатних уривків |
| Напруга відключення регулятора (перетворювача) близько 3.0 В | `m2-43-akum-53` | немає URL |
| Різниця між напругою регулятора (3.0 В) і захисту (2.5 В) | `m2-43-akum-53` | немає URL |
| Заряджання LG HG2 нижче −5 °C дозволено за паспортом | `m2-43-akum-53` | немає URL |
| LDO з малим падінням: 100–200 мВ | `m2-43-akum-53` | немає придатних уривків |
| Регулятор 4.2 В → 3.3 В: підходить при такому падінні | `m2-43-akum-53` | немає URL |
| Максимальний струм GPIO — 1200 мА сумарно | `m2-44-elektronika-05` | немає URL |
| Один GPIO — шоста частина від 1200 мА | `m2-44-elektronika-05` | немає придатних уривків |
| Спільна земля — сигнал це напруга відносно землі | `m2-44-elektronika-05` | немає придатних уривків |
| Конденсатор живлення 100–470 мкФ біля роз'єма | `m2-44-elektronika-05` | немає URL |
| L298N падіння напруги при 12 В — близько 2-3 В | `m2-45-motory-symptomy` | немає URL |
| L298N при 5 В живленні дає ~3 В на виход | `m2-45-motory-symptomy` | немає придатних уривків |
| Серво живиться від окремого джерела, земля спільна | `m2-45-motory-symptomy` | немає придатних уривків |
| Конденсатори 100 нФ на виводах двигуна для фільтрації шумів | `m2-45-motory-symptomy` | немає URL |
| Логічна помилка: 5 В на 3.3-вольтовий вхід пошкоджує чип | `m2-45-motory-symptomy` | немає URL |
| HC-SR04 живиться від 5 В | `m2-46-modul-44` | немає URL |
| Живлення і логічні рівні — різні питання | `m2-46-modul-44` | немає придатних уривків |
| Таблиця модулів: шість модулів дають 780 Ом паралельного опору | `m2-47-i2c-35` | немає придатних уривків |
| CH9102 потрібен не той самий драйвер, що CH340 | `m2-48-symptomy-29` | немає придатних уривків |
| rst:0xf brownout — зміряти напругу під навантаженням | `m2-48-symptomy-29` | немає придатних уривків |
| T-28-014: Напруга 3V3 під навантаженням повинна бути близько 3.3 В | `m2-49-analizator-28` | немає URL |
| T-28-015: Просідання нижче 3.0 В причина незрозумілих глюків | `m2-49-analizator-28` | немає URL |
| T-28-019: На лініях I²C у спокої має бути 3.3 В від pull-up резисторів | `m2-49-analizator-28` | немає URL |
| T-28-024: Мультиметр показує середнє, швидкий сигнал виглядає як середина 0…3.3 В | `m2-49-analizator-28` | немає придатних уривків |
| T-28-041: Лінії не піднімаються до 3.3 В — немає підтягування або завелике | `m2-49-analizator-28` | немає URL |
| T-28-063: Практичний порядок пошуку — крок 3: чи піднято лінії до 3.3 В | `m2-49-analizator-28` | немає придатних уривків |
| T-K03-011: CP2102 драйвер для Windows — з сайту SiLabs, Linux у ядрі | `m2-50-kartky` | немає придатних уривків |
| T-K03-013: CH340 драйвер для Windows — з сайту WCH, Linux у ядрі | `m2-50-kartky` | немає придатних уривків |
| T-K12-004: Мінімум комплекту — плата ESP32 DevKit 38 пінів з CP2102 або CH9102 | `m2-50-kartky` | немає придатних уривків |
| T-K14-026: HC-SR04 — частий винуватець 5 В, вихід ECHO 5 В | `m2-50-kartky` | немає придатних уривків |
| T-K11-017: Виняток із заборони 5 В — пін VIN або 5V (вхід стабілізатора) | `m2-50-kartky` | немає придатних уривків |
| T-09-034: FT232RL масово підробляють, клони працюють, доки їх не розпізнає офіційний драйвер | `m2-51-mosty` | немає придатних уривків |
| T-09-036: Плата з FT232 раптом перестала визначатися після оновлення драйвера — можлива причина підробка | `m2-51-mosty` | немає придатних уривків |
| Слова «LoRa» в документації RFM69 немає жодного разу | `m2-52-lora-43` | немає URL |
| RFM69 — сусіднє сімейство для вузькосмугового FSK без дальності LoRa | `m2-52-lora-43` | немає URL |
| ILI9341 — RGB565 формат пікселя, не ціль контролера | `m2-53-detali-reshta` | немає URL |
| T-D-151: A1 — вказівник стека | `m2-61-panik-b` | немає придатних уривків |
| T-D-177: Шукати memcpy, sprintf, цикл із <= замість < | `m2-61-panik-b` | немає придатних уривків |
| T-D-181: Порівняння з тим, що повернув malloc | `m2-61-panik-b` | немає придатних уривків |
| T-D-190: .elf разом з образом, розділ 21 | `m2-61-panik-b` | немає придатних уривків |
| T-D-193: Швидке відсікання — залити справний hello_world | `m2-61-panik-b` | немає придатних уривків |
| Матриця GPIO робить більшість пінів взаємозамінними, але не всі | `m2-63-gpio-07` | немає придатних уривків |
| Стан GPIO читається один раз при відпусканні скидання | `m2-63-gpio-07` | немає придатних уривків |
| Таблиця: пін, що задає режим, наслідок помилки | `m2-63-gpio-07` | немає придатних уривків |
| GPIO5 рідко впливає на проблеми поза SDIO режимом | `m2-63-gpio-07` | немає URL |
| На модулях з флешем 1.8 В це правильне налаштування для SDIO | `m2-63-gpio-07` | немає URL |
| ADC1 и ADC2 не рівноправні у использовании | `m2-63-gpio-07` | немає URL |
| Таблиця АДС чанели - канал 1 та канал 2 | `m2-63-gpio-07` | немає придатних уривків |
| Touch сенсори є лише на classic, S2 и S3 | `m2-63-gpio-07` | немає URL |
| На classic ESP32: 6 пінів флешу, 2 консолі, 6 тільки-вхідних, 5 strapping | `m2-63-gpio-07` | немає URL |
| Таблиця завантаження: GPIO0/GPIO15 комбінації для режимів | `m2-63-gpio-07` | немає придатних уривків |
| Потужність (P, вати) — формула P = U × I | `m2-65-elektronika-05` | немає придатних уривків |
| Закон Ома — формула U = I × R | `m2-65-elektronika-05` | немає придатних уривків |
| Дешевий USB-кабель — причина перезавантаження через падіння напруги | `m2-65-elektronika-05` | немає придатних уривків |
| Формула резистора для світлодіода — R = (U_живлення − U_світлодіода) / I_бажаний | `m2-65-elektronika-05` | немає придатних уривків |
| Пін ESP32 віддає обмежений струм — більше немає стану "необмеженого" | `m2-65-elektronika-05` | немає URL |
| Параметри GPIO — в таблиці DC Characteristics, а не в Absolute Maximum | `m2-65-elektronika-05` | немає придатних уривків |
| Сумарний максимум всіх GPIO — 1200 мА на всі виводи разом | `m2-65-elektronika-05` | немає URL |
| GPIO drive capability — "medium" на основі GPIO_DRIVE_CAP_DEFAULT | `m2-65-elektronika-05` | немає придатних уривків |
| Десять світлодіодів на одному домені — перевищення за межею домену, не за сумарною | `m2-65-elektronika-05` | немає придатних уривків |
| Пін 5V/VIN — це вхід стабілізатора, а не GPIO вхід | `m2-65-elektronika-05` | немає придатних уривків |
| VIN принаймні 5 В — це заявлена напруга для модулів ESP32 | `m2-65-elektronika-05` | немає придатних уривків |
| Ультразвуковий далекомір HC-SR04 — вихід ECHO 5 В | `m2-65-elektronika-05` | немає URL |
| Логічні мікросхеми серії 74HC при 5 В живленні — 5-вольтовий вихід | `m2-65-elektronika-05` | немає URL |
| Релейні модулі для Arduino — 5-вольтові логічні входи | `m2-65-elektronika-05` | немає придатних уривків |
| Дисплеї "для Arduino" — 5-вольтові входи | `m2-65-elektronika-05` | немає придатних уривків |
| ESP32 3.3 В часто сприймається як HIGH 5-вольтовими входами | `m2-65-elektronika-05` | немає URL |
| Дільник напруги 5 В → 3.3 В: R1=10 кОм, R2=20 кОм, V_out ≈ 1.65 В | `m2-65-elektronika-05` | немає придатних уривків |
| Резистор як перетворювач рівня — не працює для SPI (завалює фронти) | `m2-65-elektronika-05` | немає придатних уривків |
| Резистор як перетворювач рівня — не працює для I²C (відкриває коло) | `m2-65-elektronika-05` | немає URL |
| I²C потребує двонапрямленого перетворювача на базі FET | `m2-65-elektronika-05` | немає URL |
| Pull-up резистор — електричний опір від сигнальної лінії до живлення | `m2-65-elektronika-05` | немає придатних уривків |
| ESP32 має вбудовані pull-up резистори, активуються з коду | `m2-65-elektronika-05` | немає URL |
| Код GPIO конфіг — режим input з pull-up вмиканням | `m2-65-elektronika-05` | немає URL |
| I²C та 1-Wire використовують open-drain/open-collector (pull-up) | `m2-65-elektronika-05` | немає URL |
| Спільна земля — сигнали це напруги відносно точки відліку (GND) | `m2-65-elektronika-05` | немає придатних уривків |
| Brownout — перезавантаження при короткому просідання напруги | `m2-65-elektronika-05` | немає придатних уривків |
| MOSFET low-side схема — навантаження між +V та стоком, витік на GND | `m2-65-elektronika-05` | немає URL |
| GPIO при старті не налаштований, лінія "висить" — небезпека вмкнення | `m2-65-elektronika-05` | немає придатних уривків |
| Таблиця порівняння приладів діагностики — назва, призначення, ціна | `m2-66-analizator-28` | немає URL |
| GND (земля) між пристроями мусить мати нульовий опір (спільна земля) | `m2-66-analizator-28` | немає придатних уривків |
| Восьмиканальний USB-аналізатор коштує як пара плат (≈100–200 грн) | `m2-66-analizator-28` | немає придатних уривків |
| I²C помилка: SCL йде, SDA мовчить → ведений не відповідає | `m2-66-analizator-28` | немає придатних уривків |
| I²C помилка: START, адреса, NACK → пристрою з такою адресою немає | `m2-66-analizator-28` | немає придатних уривків |
| I²C успішна передача: START, адреса, ACK, дані → шина працює правильно | `m2-66-analizator-28` | немає придатних уривків |
| I²C помилка: SCL розтягнутий, SDA чекає → clock stretching | `m2-66-analizator-28` | немає придатних уривків |
| UART декодування — один канал на лінію, помилка швидкості видна як сміття | `m2-66-analizator-28` | немає придатних уривків |
| SPI діагностика — потрібні чотири канали (SCK, MOSI, MISO, CS) | `m2-66-analizator-28` | немає придатних уривків |
| SPI помилка: дані зчитуються не по тому фронту → видно на аналізаторі | `m2-66-analizator-28` | немає придатних уривків |
| I²C (100–400 кГц) та UART вистачає дешевого аналізатора (24 МГц) | `m2-66-analizator-28` | немає придатних уривків |
| SPI на 40 МГц — недостатньо 24 МГц аналізатора, потребує осцилографа | `m2-66-analizator-28` | немає придатних уривків |
| I²C сканер — програма що перебирає адреси й друкує які відповідають | `m2-66-analizator-28` | немає URL |
| Мультиметр — вимір напруги, опору, малих струмів | `m2-66-analizator-28` | немає придатних уривків |
| Осцилограф — спостереження форми сигналу та часових параметрів | `m2-66-analizator-28` | немає придатних уривків |
| GPIO5 для поплавкового вимикача на ESP32-S3 | `m2-67-proj-62` | немає придатних уривків |
| GPIO5 для поплавкового вимикача на ESP32-C3 | `m2-67-proj-62` | немає придатних уривків |
| Кнопка, що подає сигнал на GPIO, не працює, коли чип завис | `m2-67-proj-62` | немає придатних уривків |
| Схема реле: +12 В → насос → реле (NO) → аварійний вимикач → GND | `m2-67-proj-62` | немає придатних уривків |
| Лог переходу між станами чипа з причиною | `m2-67-proj-62` | немає URL |
| Керування насосом функцією nasos_keruvaty на основі стану | `m2-67-proj-62` | немає URL |
| Оновлення індикації при зміні стану | `m2-67-proj-62` | немає URL |
| Максимум часу безперервної роботи насоса: 600 секунд (10 хвилин) | `m2-67-proj-62` | немає придатних уривків |
| Час паузи після вимкнення насоса: 300 секунд (5 хвилин) | `m2-67-proj-62` | немає придатних уривків |
| ESP32 classic або C3 — одиниця в проєкті логера | `m2-68-proj-60` | немає придатних уривків |
| Таблиця розпіновки: Сигнал | classic | C3 | `m2-68-proj-60` | немає придатних уривків |
| На C3 рідним для MISO залишився тільки GPIO2, який уже інакше використовується | `m2-68-proj-60` | немає придатних уривків |
| GPIO2 використовується як strapping-пін для дільника, чинний лише як вихід | `m2-68-proj-60` | немає придатних уривків |
| Для C3 піни слід взяти з таблиці розпіновки | `m2-68-proj-60` | немає придатних уривків |
| GPIO2 як strapping-пін на C3 — свідомий компроміс | `m2-68-proj-60` | немає придатних уривків |
| Лог при розрядженому акумуляторі (< 3.2 В) | `m2-68-proj-60` | немає придатних уривків |
| Лог про недоступність карти microSD | `m2-68-proj-60` | немає придатних уривків |
| Базовий проєкт із Wi-Fi, I²C, веб-сервером, mDNS, зберіганням стану й обробкою помилок | `m2-69-proj-59` | немає придатних уривків |
| ESP32-S3-DevKitC-1 або classic DevKitC — одиниця в проєкті моніторингу | `m2-69-proj-59` | немає придатних уривків |
| Таблиця розпіновки: Сигнал | classic DevKitC | S3-DevKitC-1 | `m2-69-proj-59` | немає придатних уривків |
| GPIO22 на S3 не існує; запит повертає ESP_ERR_INVALID_ARG без ESP_ERROR_CHECK | `m2-69-proj-59` | немає URL |
| Include драйвера I²C master | `m2-69-proj-59` | немає URL |
| Константа для історії: 720 записів (12 годин при вимірюванні раз на хвилину) | `m2-69-proj-59` | немає придатних уривків |
| HC-SR04 видає 5 В на виводі ECHO | `m2-70-modul-44` | немає URL |
| Подача 5 В на GPIO ESP32 пошкоджує вхід | `m2-70-modul-44` | немає URL |
| I²C потребує підтягувальних резисторів | `m2-71-i2c-35` | немає URL |
| ESP-IDF рекомендує 2–5 кОм для I²C підтягування | `m2-71-i2c-35` | немає придатних уривків |
| На 100 кГц 4.7 кОм годиться, на 400 кГц — ні | `m2-71-i2c-35` | немає URL |
| Мінімум 1 кОм для обмеження струму через open-drain вихід | `m2-71-i2c-35` | немає URL |
| Адреса бутлоадера залежить від чипу | `m2-72-symptomy-29` | немає URL |
| Linux: Доступ до серійного порту вимагає групи dialout | `m2-72-symptomy-29` | немає придатних уривків |
| Deep sleep споживає 10 мкА; з ULP — близько 150 мкА | `m2-79-zhyvlennya-klyuchi` | немає URL |
| SPI витримує десятки мегагерц | `m2-80-shyny` | немає придатних уривків |
| RS-485 має термінаторів 120 Ом на обох кінцях лінії | `m2-80-shyny` | немає придатних уривків |
| CAN має термінаторів 120 Ом на обох кінцях | `m2-80-shyny` | немає придатних уривків |
| CAN пакет несе до 8 байтів даних | `m2-80-shyny` | немає придатних уривків |
| Модулі на 5 В трансиверах можуть не бути сумісними з ESP32 | `m2-80-shyny` | немає придатних уривків |
| HC-SR04 вимірює тривалість імпульсу | `m2-81-sensory-lora` | немає придатних уривків |
| LoRa модулі продаються на частоти 433, 868, 915 МГц | `m2-81-sensory-lora` | немає придатних уривків |
| DS18B20 вимагає delay(750 мс) для читання температури | `m2-81-sensory-lora` | немає придатних уривків |
| VL53L0X / VL53L1X — лазерні далекомісні на I²C | `m2-81-sensory-lora` | немає придатних уривків |
| OneWire бібліотеки — OneWire і DallasTemperature для Arduino | `m2-81-sensory-lora` | немає придатних уривків |
| ACS712 — датчик струму на ефекті Холла з аналоговим виходом | `m2-81-sensory-lora` | немає URL |
| Сервомотор керується імпульсами 50 Гц з тривалістю 1–2 мс. | `m2-90-vybirka` | немає придатних уривків |
| Індекс GPIO21: сторінки 149, 310, 326, 335 додатку z | `m2-90-vybirka` | немає придатних уривків |
| Сервомотор приймає 50-герцові імпульси з тривалістю 1–2 мс. | `m2-90-vybirka` | немає придатних уривків |
| Реальні межі серво-імпульсів часто відрізняються від заявлених 1–2 мс (можуть бути 0.6–2.4 мс). | `m2-90-vybirka` | немає придатних уривків |
| ESP32-C3 дешевий, простий, має 400 КБ пам'яті — достатньо для простих проєктів | `m2-90-vybirka` | немає придатних уривків |
| При живленні модуля від 3.3 В це не гарантує, що його сигнальні рівні — 3.3 В | `m2-90-vybirka` | немає придатних уривків |
| Лабораторний блок живлення з обмеженням струму запобігає випаленню доріжок при коротких замиканнях | `m2-90-vybirka` | немає придатних уривків |
| Індекс GPIO15: сторінки 14, 17–18, 28, 71, 142, 173, 379 додатку z | `m2-90-vybirka` | немає придатних уривків |
| На ESP32-C3 з 400 КБ два одночасні TLS-з'єднання створюють помітне навантаження | `m2-90-vybirka` | немає придатних уривків |
| Практичний підхід SPI — почати з 1 МГц | `m2-91-vybirka` | немає придатних уривків |
| GPIO12 у покажчику розділу Z | `m2-91-vybirka` | немає придатних уривків |
| Поведінка ESP32 при 1.8В flash та неправильній конфігурації | `m2-91-vybirka` | немає придатних уривків |
| Wi-Fi канали 2.4 ГГц та регіональні обмеження | `m2-91-vybirka` | немає придатних уривків |
| Енергоспоживання ESP-NOW за цикл передачі | `m2-91-vybirka` | немає придатних уривків |
| Доступність ESP-IDF функцій прямо з коду Arduino | `m2-91-vybirka` | немає придатних уривків |
| Помилка 0xc (SW_CPU_RESET) — типово після паніки | `m2-91-vybirka` | немає придатних уривків |
| GPIO17 у покажчику розділу Z | `m2-91-vybirka` | немає придатних уривків |
| GPIO9 у покажчику розділу Z | `m2-91-vybirka` | немає придатних уривків |
| Доступ до поля структури за NULL покажчиком зі зсувом | `m2-91-vybirka` | немає придатних уривків |
| Причини непрошивання модуля | `m2-91-vybirka` | немає придатних уривків |
| Помилка 0xf — просіло живлення (BROWN_OUT_RESET) | `m2-91-vybirka` | немає придатних уривків |
| Призначення кнопок BOOT та EN на платі | `m2-91-vybirka` | немає придатних уривків |
| T-D-081: GPIO4 як другий за цінністю біт у boot масці | `m2-92-vybirka` | немає придатних уривків |
| T-D-042: Код скидання 0xe — EXT_CPU_RESET | `m2-92-vybirka` | немає придатних уривків |
| T-02-108: ESP32-C5 з Wi-Fi у двох діапазонах | `m2-92-vybirka` | немає придатних уривків |
| T-39-093: ESP32 не бачить 5 ГГц мережі | `m2-92-vybirka` | немає URL |
| T-07-063: Піни GPIO6-GPIO11 під'єднані до флешу в модулі | `m2-92-vybirka` | немає URL |
| T-E-110: Промислова шина потребує трансивера на 3.3 В | `m2-92-vybirka` | немає придатних уривків |
| T-K06-024: Код скидання 0x10 — RTCWDT_RTC_RESET | `m2-92-vybirka` | немає придатних уривків |
| T-D-022: Код скидання 0x7 — TG0WDT_SYS_RESET | `m2-92-vybirka` | немає придатних уривків |
| T-08-048: ESP32-C3 SuperMini обмежене 400 КБ пам'яті | `m2-92-vybirka` | немає придатних уривків |
| T-D-030: Код скидання 0xa — INTRUSION_RESET | `m2-92-vybirka` | немає придатних уривків |
| T-30-056: Розподіл пам'яті: 16 КБ і більше — PSRAM | `m2-92-vybirka` | немає придатних уривків |
| Дешево і масово: C3 з 400 КБ SRAM для простих задач | `m2-93-vybirka` | немає придатних уривків |
| Час пробудження й ініціалізації в розрахунку — 300 мілісекунд | `m2-93-vybirka` | немає придатних уривків |
| DS18B20 має похибку ±0.5°C у діапазоні −10…+85°C та ±2°C поза ним | `m2-93-vybirka` | немає URL |
| GPIO32 розраховується у розділах 53, 74–75, 182, 389 | `m2-93-vybirka` | немає придатних уривків |
| Заряд на цикл передачі Wi-Fi становить близько 500 мА·с | `m2-93-vybirka` | немає придатних уривків |
| Трансивер CAN повинен відповідати логіці 3.3 В, або потрібен конвертер рівнів на RX | `m2-93-vybirka` | немає придатних уривків |
| Код 0x04 в таблиці strapping пінів C3 означає GPIO8 | `m2-93-vybirka` | немає URL |
| Код 0x08 в таблиці strapping пінів S3 означає GPIO0 | `m2-93-vybirka` | немає URL |
| WROVER за схемою WROOM: GPIO16 вже нічий на WROVER через PSRAM | `m2-93-vybirka` | немає придатних уривків |
| T-41-044: Для BLE беріть NimBLE, C3 має 400 КБ | `m2-94-vybirka` | немає придатних уривків |
| T-16-034: У наступному поколінні бутлоадер став на `0x0` | `m2-94-vybirka` | немає URL |
| T-K08-044: WiFi не під'єднується — пароль, канал 12–13 або 5 ГГц | `m2-94-vybirka` | немає придатних уривків |
| T-Z-117: GPIO26 page references | `m2-94-vybirka` | немає придатних уривків |
| T-33-054: Період при 50 Гц — 20 мс, формула duty | `m2-94-vybirka` | немає придатних уривків |
| T-Z-113: GPIO2 page references | `m2-94-vybirka` | немає придатних уривків |
| T-C-103: bootloader address table — S3, C3, C6, H2 at 0x0 | `m2-94-vybirka` | немає URL |
| ESP-NOW використовує той самий діапазон частот, що Wi-Fi 2.4 ГГц | `m2-95-vybirka` | немає URL |
| Діод послідовно для захисту від переполюсовки, падіння 0.3–0.7 В | `m2-95-vybirka` | немає придатних уривків |
| GPIO12 з високим рівнем — правильне налаштування на модулях з 1.8В флешем | `m2-95-vybirka` | немає придатних уривків |
| Wi-Fi 5 ГГц доступний тільки на ESP32-C5 | `m2-95-vybirka` | немає придатних уривків |
| ESP32-C3 має 400 КБ SRAM — це головне обмеження | `m2-95-vybirka` | немає придатних уривків |
| DS3231 та MPU6050 мають однакову I2C адресу 0x68 | `m2-95-vybirka` | немає придатних уривків |
| T-E-067 — NRF24L01 · радіо 2.4 ГГц | `m2-96-vybirka` | немає придатних уривків |
| T-Z-123 — GPIO6 у індексі | `m2-96-vybirka` | немає придатних уривків |
| T-02-135 — Мережа 5 ГГц, чип C5 | `m2-96-vybirka` | немає придатних уривків |
| T-38-012 — CAN вузол публікує температуру з ідентифікатором | `m2-96-vybirka` | немає придатних уривків |
| T-23-023 — Суфікс модуля кодує обсяг флешу й PSRAM | `m2-96-vybirka` | немає придатних уривків |
| T-Z-115 — GPIO22 у індексі | `m2-96-vybirka` | немає придатних уривків |
| T-Z-112 — GPIO18 у індексі | `m2-96-vybirka` | немає придатних уривків |
| Просадка нижче 3.0 В — знак проблеми з живленням | `m2-97-vybirka` | немає придатних уривків |
| GPIO4 — індекс посилань | `m2-97-vybirka` | немає придатних уривків |
| Октальна PSRAM на S3 використовує п'ять додаткових пінів | `m2-97-vybirka` | немає придатних уривків |
| GPIO25 — індекс посилань | `m2-97-vybirka` | немає придатних уривків |
| Похибка датчика DS18B20 — два справні можуть розходитись до 1 °C | `m2-97-vybirka` | немає придатних уривків |
| GPIO34 — індекс посилань | `m2-97-vybirka` | немає придатних уривків |
| Дамп флешу починається з адреси 0x0 і містить бутлоадер | `m2-97-vybirka` | немає придатних уривків |
| SCL пін розпиновки I2C: GPIO22 на ESP32 classic та GPIO9 на ESP32-S3 | `m2-98-vybirka` | немає придатних уривків |
| Покажчик до GPIO8 в розділі z-pokazhchyk | `m2-98-vybirka` | немає придатних уривків |
| Код помилки 0xc: програмне скидання ядра | `m2-98-vybirka` | немає придатних уривків |
| Arduino IDE часто копіює код під AVR без адаптування до ESP32 | `m2-98-vybirka` | немає придатних уривків |
| Покажчик до GPIO3 в розділі z-pokazhchyk | `m2-98-vybirka` | немає придатних уривків |
| SDA пін розпиновки I2C: GPIO21 на ESP32 classic та GPIO8 на ESP32-S3 | `m2-98-vybirka` | немає придатних уривків |
| GPIO12 утримується високим в схемі ESP32 | `m2-98-vybirka` | немає придатних уривків |
| Таблиця GPIO0 при скиданні розпиновки та ROM адреси | `m2-98-vybirka` | немає придатних уривків |
| ESP32 і його варіанти не підтримують 5 ГГц Wi-Fi, крім ESP32-C5 | `m2-98-vybirka` | немає URL |
| GPIO0 — ключовий пін для вибору режиму завантаження на ESP32 classic та S3 | `m2-98-vybirka` | немає придатних уривків |
| Суфікс в назві ESP32 плати кодує обсяг флеш та PSRAM: N8, N16R8 і т.д. | `m2-98-vybirka` | немає придатних уривків |
| На ESP32-C3 з 400 КБ доступної пам'яті MicroPython інтерпретатор залишає мало місця | `m2-98-vybirka` | немає придатних уривків |
| Радіо на борту · RP2040 → ні (крім W) | `m2-detali-klasC` | немає URL |
| ОС · RP2040 → немає або RTOS | `m2-detali-klasC` | немає URL |
| Сон · RP2040 → мА | `m2-detali-klasC` | немає URL |
| Реальний час · RP2040 → добре | `m2-detali-klasC` | немає URL |
| Ціна плати · RP2040 → низька | `m2-detali-klasC` | немає URL |
| CP2102 — 11, 25, 29, 79, 81, 83, 114, 366, 391 | `m2-detali-klasC` | немає придатних уривків |
| PCF8574 — 57, 76, 267, 365, 386 | `m2-detali-klasC` | немає придатних уривків |
| ESP32-C3 дешевий, простий, має 400 КБ пам'яті — достатньо для простих | `m2-detali-klasC` | немає URL |
| Дешево і масово: C3 з 400 КБ SRAM для простих задач | `m2-detali-klasC` | немає URL |
| ESP32-C3 має 400 КБ SRAM — це головне обмеження | `m2-detali-klasC` | немає URL |
| Специфікація I²C — адресація, ємність шини, режими | `m2-detali-klasC` | немає URL |
| DS18B20 — час перетворення, діапазон, роздільність | `m2-detali-klasC` | немає URL |
| Паспортна похибка DS18B20 — на датчик, а не між датчиками | `m2-detali-klasC` | немає URL |
| BME280 — карта регістрів і формули компенсації | `m2-detali-klasC` | немає URL |
| S3 та C3 — USB-контролер на кристалі | `m2-detali-klasC` | немає URL |
| GPIO0 — ключовий пін для вибору режиму завантаження на ESP32 classic т | `m2-detali-klasC` | немає URL |
| LoRa SX127x і SX126x — параметри модуляції | `m2-detali-klasC` | немає URL |
| SPI витримує десятки мегагерц | `m2-detali-klasC` | немає URL |
| Дисплеї — зсув SH1106 і адреси I²C-модулів | `m2-detali-klasC` | немає URL |
| T-02-108: ESP32-C5 з Wi-Fi у двох діапазонах | `m2-detali-klasC` | немає URL |
| T-02-135 — Мережа 5 ГГц, чип C5 | `m2-detali-klasC` | немає URL |
| Дамп флешу починається з адреси 0x0 і містить бутлоадер | `m2-detali-klasC` | немає URL |
| GPIO12 з високим рівнем — правильне налаштування на модулях з 1.8В фле | `m2-detali-klasC` | немає URL |
| T-H-013: **Datasheet модуля** (`ESP32-WROOM-32`, `ESP32-S3-WROOM-1`,  | `m2-hvylya2` | немає URL |
| T-23-011: `ESP32-WROOM-32` · Що це значить практично → двоядерний Xten | `m2-hvylya2` | немає URL |
| T-36-055: SPI витримує десятки мегагерц, але не завжди | `m2-hvylya2` | немає URL |
| T-12-058: | Серійне виробництво, OTA, відтворюваність | ESP-IDF | | `m2-hvylya2` | немає URL |
| T-15-014: Виріб на роки, OTA, серійність · Чому → відтворюваність і ді | `m2-hvylya2` | немає URL |
| T-58-062: | OTA | оновлення і відкат проходять | | `m2-hvylya2` | немає URL |
| T-COM-025: MPU6050 · Чому → сам зводить дані, менше роботи | `m2-hvylya2` | немає URL |
| T-24-038: Формат NVS — сторінковий, з простором імен, ключем і типізов | `m2-hvylya2` | немає URL |
| T-18-052: NVS стійкий до зникнення живлення: запис влаштований так, що | `m2-hvylya2` | немає URL |
| T-53-017: Паспорти більшості елементів нормують заряджання від 0 до +4 | `m2-hvylya2` | немає URL |
| T-01-061: Старт · RP2040 → миттєво | `m2-hvylya2` | немає URL |
| T-25-037: Документація ESP-IDF описує це так: `Ctrl + L` — «Stop/resum | `m2-hvylya2` | немає URL |
| T-25-105: Лог пишеться у файл (`Ctrl+L` в `idf.py monitor`, для решти  | `m2-hvylya2` | немає URL |
| T-K10-019: idf.py -p /dev/ttyUSB0 monitor # монітор з розшифровкою back | `m2-hvylya2` | немає URL |
| T-K06-024: `0x10` · Назва → RTCWDT_RTC_RESET | `m2-hvylya2` | немає URL |
| T-D-047: `0x10` · Назва → RTCWDT_RTC_RESET | `m2-hvylya2` | немає URL |
| T-E-107: DS18B20 · Що дає → температура, кілька на лінії | `m2-hvylya2` | немає URL |
| T-59-146: - **MQTT** замість або разом із веб-інтерфейсом (розділ 40); | `m2-hvylya2` | немає URL |
| T-COM-030: **Лишаються добрим вибором:** DS18B20 (довгий дріт, герметич | `m2-hvylya2` | немає URL |
| T-09-046: **JTAG іде тим самим кабелем.** Повноцінне покрокове налагод | `m2-hvylya2` | немає URL |
| T-20-030: esptool --port /dev/ttyUSB0 flash-id | `m2-hvylya2` | немає URL |
| T-18-026: **`nvs` лежить перед застосунком.** Це сховище пар «ключ — з | `m2-hvylya3` | немає URL |
| T-18-061: Якщо серед налаштувань є те, чого не відновити (серійний ном | `m2-hvylya3` | немає URL |
| T-24-033: NVS зберігає конфігурацію конкретного екземпляра | `m2-hvylya3` | немає URL |
| T-22-066: У всіх інших випадках — від чужого виробу до власного пристр | `m2-hvylya3` | немає URL |
| T-56-018: Налаштування.** Що зберігається в NVS, як задається, як скин | `m2-hvylya3` | немає URL |
| T-32-052: **Незавершений запис у флеш.** NVS до цього стійкий за задум | `m2-hvylya3` | немає URL |
| T-18-012: `nvs` · Підтип → nvs | `m2-hvylya3` | немає URL |
| T-18-048: NVS (Non-Volatile Storage) — сховище пар «ключ — значення»,  | `m2-hvylya3` | немає URL |
| T-G-145: | NVS | Non-Volatile Storage | | `m2-hvylya3` | немає URL |
| T-55-083: У NVS може лежати конфігурація, якої немає більше ніде, і пі | `m2-hvylya3` | немає URL |
| T-18-011: `nvs` · Тип → data | `m2-hvylya3` | немає URL |
| T-H-027: **Документація на конкретні мікросхеми** — сайти виробників: | `m2-hvylya3` | немає URL |
| T-37-002: Практично весь його світ для нас — це датчики температури DS | `m2-hvylya3` | немає URL |
| T-COM-085: Поріг для DS18B20 не випадковий і не збігається з паспортною | `m2-hvylya3` | немає URL |
| T-45-013: **DS18B20** — тільки температура, але на довгому дроті, у ге | `m2-hvylya3` | немає URL |
| T-56-025: **Перелік компонентів** із конкретними позначеннями: не «дат | `m2-hvylya3` | немає URL |
| T-37-016: Паспортна похибка DS18B20 — **±0.5 °C у діапазоні −10…+85 °C | `m2-hvylya3` | немає URL |
| T-COM-055: SX1276 / RFM95 · Застереження → більше бібліотек і прикладів | `m2-hvylya3` | немає URL |
| T-COM-053: SX1262 · Застереження → ефективніший за SX1276 | `m2-hvylya3` | немає URL |
| T-COM-054: SX1276 / RFM95 · Для чого → LoRa | `m2-hvylya3` | немає URL |
| T-E-061: SX1276 / RFM95 · Що дає → LoRa | `m2-hvylya3` | немає URL |
| T-E-062: SX1276 / RFM95 · Бібліотека → RadioLib, LoRa | `m2-hvylya3` | немає URL |
| T-43-022: `RFM95` — це модуль на чипі `SX1276`, тому в бібліотеках вон | `m2-hvylya3` | немає URL |
| T-43-021: **SX1276 / RFM95** — класика, широко доступні, море бібліоте | `m2-hvylya3` | немає URL |
| T-E-060: SX1276 / RFM95 · Режим → 0 | `m2-hvylya3` | немає URL |
| T-30-052: Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` * | `m2-hvylya3` | немає придатних уривків |
| T-A-067: 33–37 · Обмеження → флеш/PSRAM на Octal-модулях | `m2-hvylya3` | немає URL |
| T-A-065: 26–32 · Обмеження → **флеш і PSRAM** | `m2-hvylya3` | немає URL |
| T-G-159: | PSRAM | Pseudo-Static RAM | | `m2-hvylya3` | немає URL |
| T-30-050: **PSRAM є, але поводиться не так, як гадають.** Тут два поши | `m2-hvylya3` | немає URL |
| T-H-014: Саме він каже, які виводи доступні й скільки флешу та PSRAM  | `m2-hvylya3` | немає URL |
| T-02-097: **Потребує уваги:** номери пінів — вони інші скрізь (картка  | `m2-hvylya3` | немає URL |
| T-K10-001: Синтаксис esptool **v5** (дефіси, без `.py`) | `m2-hvylya3` | немає URL |
| T-08-088: Модуль — джерело істини про те, що всередині; звіряти напис  | `m2-hvylya3` | немає URL |
| T-17-034: `flash-id` як перша команда зручна тим, що після шапки додає | `m2-hvylya3` | немає URL |
| T-E-048: Разом на одній шині — конфлікт; розв'язується перемичкою на  | `m2-hvylya3` | немає URL |
| T-E-027: INA219 / INA226 · Адреса → `0x40`+ | `m2-hvylya3` | немає URL |
| T-25-038: Монітор — інтерактивна програма з кольорами й керуванням із  | `m2-hvylya3` | немає URL |
| T-C-067: idf.py monitor # з розшифровкою backtrace на льоту | `m2-hvylya3` | немає URL |
| T-25-036: Для `idf.py monitor` є **власний спосіб**, і він кращий за п | `m2-hvylya3` | немає URL |
| T-26-044: Тому **на RISC-V лог знімають `idf.py monitor`**, не чимось  | `m2-hvylya3` | немає URL |
| T-26-035: **Автоматично.** `idf.py monitor`, запущений з каталогу проє | `m2-hvylya3` | немає URL |
| T-11-097: - **IntelliSense**, налаштований на конкретний чип: автодопо | `m2-hvylya3` | немає URL |
| T-E-073: MAX31855 · Що дає → термопара | `m2-hvylya3` | немає URL |
| T-44-005: `BME280`, `SSD1306`, `MAX485`, `A4988` | `m2-hvylya3` | немає URL |
| T-E-007: BME280 · Що дає → тиск, T, вологість | `m2-hvylya3` | немає URL |
| T-45-019: **BMP280 / BME280** — атмосферний тиск | `m2-hvylya3` | немає URL |
| T-44-054: Для SPI — прочитати регістр ідентифікації, який є майже в ко | `m2-hvylya3` | немає URL |
| T-E-010: BMP280 · Що дає → тиск, T — **без** вологості | `m2-hvylya3` | немає URL |
| T-45-011: **BMP280** — те саме без вологості, дешевший | `m2-hvylya3` | немає URL |
| T-48-069: L298N втрачає близько двох вольтів на собі — для нового проє | `m2-hvylya3` | немає URL |
| T-19-086: Для OTA потрібен саме образ застосунку, без бутлоадера і таб | `m2-hvylya3` | немає URL |
| T-23-066: За один цикл скидання звідси дістається: причина попередньог | `m2-hvylya3` | немає URL |
| T-18-001: Флеш ESP32 — не один суцільний шматок пам'яті, а набір облас | `m2-hvylya3` | немає URL |
| T-22-055: Другий бутлоадер безкоштовно друкує версію ESP-IDF, обсяг фл | `m2-hvylya3` | немає URL |
| T-D-106: Звідси безкоштовно читається: **версія ESP-IDF**, **обсяг фл | `m2-hvylya3` | немає URL |
| T-50-026: Важливо розуміти межу: шифрування NVS має сенс **разом із**  | `m2-hvylya3` | немає URL |
| T-04-105: DAC · S2 → **2** | `m2-hvylya3` | немає URL |
| T-K09-009: | 25, 26 | єдині DAC-виходи | | `m2-hvylya3` | немає URL |
| T-04-050: DAC · Що це → [[classic]] [[S2]] справжній аналоговий вихід | `m2-hvylya3` | немає URL |
| T-04-150: DAC — тільки classic і S2 | `m2-hvylya3` | немає URL |
| T-04-104: DAC · classic → **2** | `m2-hvylya3` | немає URL |
| T-04-132: **DAC є лише в classic і S2.** Справжній аналоговий вихід бі | `m2-hvylya3` | немає URL |
| T-18-035: python $IDF_PATH/components/partition_table/gen_esp32part.py | `m2-hvylya3` | немає URL |
| T-24-011: python $IDF_PATH/components/partition_table/gen_esp32part.py | `m2-hvylya3` | немає URL |
| T-26-101: Потребує розділу типу `coredump` у таблиці розділів (розділ  | `m2-hvylya3` | немає URL |
| T-C-121: python $IDF_PATH/components/partition_table/gen_esp32part.py | `m2-hvylya3` | немає URL |
| T-K05-008: `partition-table.bin` · Що це → таблиця розділів | `m2-hvylya3` | немає URL |
| T-19-097: Rollback — окремий механізм, і він працює лише тоді, коли пі | `m2-hvylya3` | немає URL |
| T-19-098: OTA не оновлює таблицю розділів | `m2-hvylya3` | немає URL |
| T-19-062: OTA — це кілька хвилин безперервної роботи радіо на прийом п | `m2-hvylya3` | немає URL |
| T-19-001: OTA (over-the-air) — оновлення прошивки без фізичного доступ | `m2-hvylya3` | немає URL |
| T-19-029: OTA оновлює лише образ застосунку — таблиця розділів через O | `m2-hvylya3` | немає URL |
| T-50-067: - креденшели в NVS, унікальні на екземпляр — не в коді; - жо | `m2-hvylya3` | немає URL |
| T-18-105: **Зміна розбивки несумісна з OTA-оновленням.** Пристрій у по | `m2-hvylya3` | немає URL |
| T-19-024: Головне проєктне обмеження OTA — **застосунок займає місце д | `m2-hvylya3` | немає URL |
| T-19-005: Розбивка з OTA має **два розділи для застосунку** замість од | `m2-hvylya3` | немає URL |
| T-50-036: OTA — це канал, яким у пристрій потрапляє код | `m2-hvylya3` | немає URL |
| T-58-050: **OTA з відкатом**, якщо пристрій має оновлюватися | `m2-hvylya3` | немає URL |
| T-58-065: Випробування зникнення живлення варто робити **грубо**: вими | `m2-hvylya3` | немає URL |
| T-B-142: ADC читає дурницю · Причина → [[classic]] ADC2 при Wi-Fi | `m2-hvylya3` | немає URL |
| T-K08-028: 9 · Симптом → ADC читає дурницю | `m2-hvylya3` | немає URL |
| T-G-147: | ADC / DAC | Analog-to-Digital / Digital-to-Analog Converte | `m2-hvylya3` | немає URL |
| T-50-045: Обидва реалізовані через **eFuse** — біти, які пропалюються  | `m2-hvylya3` | немає URL |
| T-20-088: Флеш лікується завжди. eFuse — ніколи | `m2-hvylya3` | немає URL |
| T-20-014: **eFuse.** Це набір однорозрядних запобіжників у кремнії | `m2-hvylya3` | немає URL |
| T-20-005: Практично незворотний лише один клас операцій — запис eFuse | `m2-hvylya3` | немає URL |
| T-00-062: **Незворотне.** Операція, яку не можна скасувати: перепалени | `m2-hvylya3` | немає URL |
| T-20-043: **Не перенесеться MAC-адреса.** Вона зашита в eFuse кожного  | `m2-hvylya3` | немає URL |
| T-46-007: OLED SSD1306 · Особливості → контраст, малий, дешевий | `m2-hvylya3` | немає URL |
| T-46-004: OLED SSD1306 · Розмір → 0.96–1.3" | `m2-hvylya3` | немає URL |
| T-46-027: **OLED SSD1306** — типовий вибір для службової інформації | `m2-hvylya3` | немає URL |
| T-23-010: `ESP32-WROOM-32` · Чип → ESP32 classic | `m2-hvylya3` | немає URL |
| T-08-017: Літера `U` в кінці (`WROOM-1U`) означає роз'єм під зовнішню  | `m2-hvylya3` | немає URL |
| T-K01-006: `ESP32-WROOM-32` · Чип → ESP32 classic | `m2-hvylya3` | немає URL |
| T-39-078: **Зовнішня антена через роз'єм IPEX** — модулі з літерою `U` | `m2-hvylya3` | немає URL |
| T-39-076: **PCB-антена** — доріжка на платі модуля (`WROOM-1`) | `m2-hvylya3` | немає URL |
| T-01-009: **Модуль.** Кристал плюс кварц, флеш-пам'ять, антена і обв'я | `m2-hvylya3` | немає URL |
| T-23-012: `ESP32-WROOM-32D`, `-32E` · Чип → ESP32 classic | `m2-hvylya3` | немає URL |
| T-04-037: LEDC · Що це → PWM: яскравість світлодіодів, сервоприводи | `m2-hvylya3` | немає URL |
| T-06-088: **Ємність джерела.** Ходові елементи 18650 — від 2500 до 350 | `m2-hvylya3` | немає URL |
| T-60-006: **Живлення:** 18650, ціль — не менше трьох місяців при вимір | `m2-hvylya3` | немає URL |
| T-B-134: CAN: лічильник помилок росте · Розділ → 38 | `m2-hvylya3` | немає URL |
| T-04-098: TWAI (CAN) · classic → 1 | `m2-hvylya3` | немає URL |
| T-04-028: TWAI · Що це → CAN-шина, сумісна з автомобільною | `m2-hvylya3` | немає URL |
| T-63-080: - **Modbus RTU ↔ TCP** зі штатним компонентом `esp-modbus` з | `m2-hvylya3` | немає URL |
| T-63-061: Міст на CAN за замовчуванням має працювати в режимі **`LISTE | `m2-hvylya3` | немає URL |
| T-38-059: CAN сам стежить за помилками й має лічильники | `m2-hvylya3` | немає URL |
| BME280 — карта регістрів і формули компенсації | `pass-03-nedostupni` | немає придатних уривків |
| DS18B20 — час перетворення, діапазон, роздільність | `pass-03-nedostupni` | немає придатних уривків |
| Специфікація I²C — адресація, ємність шини, режими | `pass-03-nedostupni` | немає придатних уривків |
| Bluetooth Core — типовий ATT MTU | `pass-03-nedostupni` | немає придатних уривків |
| Datasheet ESP32 — електричні межі, струми, температура | `pass-03-nedostupni` | немає придатних уривків |
| Трансивери CAN і RS-485 — рівні живлення й логіки | `pass-03-nedostupni` | немає придатних уривків |
| Li-ion і TP4056 — напруги, ємність, захист | `pass-03-nedostupni` | немає придатних уривків |
| Паливоміри акумулятора — MAX17048 проти лічильників кулонів | `pass-03-nedostupni` | немає придатних уривків |
| Дисплеї — зсув SH1106 і адреси I²C-модулів | `pass-03-nedostupni` | немає придатних уривків |
| LoRa SX127x і SX126x — параметри модуляції | `pass-03-nedostupni` | немає придатних уривків |
| Ступені захисту IP | `pass-03-nedostupni` | немає придатних уривків |
| Порівняльна таблиця — числа, ще не звірені жодною стороною | `pass-03-nedostupni` | немає придатних уривків |
| Припої та інструмент | `pass-03-nedostupni` | немає придатних уривків |
| Арифметика книги перерахована й закріплена в make check | `pass-05-obchyslennya` | немає придатних уривків |
| Усі виклики API книги існують у заголовках | `pass-07-api-rozbyvka` | немає придатних уривків |
| Обсяг SRAM у таблиці — datasheet, а не адресні вікна | `pass-13-mozhlyvosti` | немає придатних уривків |
| Усі 689 згадок розділів, карток і додатків ведуть у наявні файли | `pass-14-marshruty` | немає придатних уривків |
| Таблиця симптомів веде в тематично правильні розділи | `pass-14-marshruty` | немає придатних уривків |
| Версії тулчейну — усі чотири найновіші на дату ревізії | `pass-15-versiyi` | немає URL |
| Адреси I²C у додатку E — усі тринадцять рядків | `pass-16-interfeysy` | немає URL |
| Програмний ліміт часу не рятує від зварених контактів реле | `pass-17-simeystva-proektiv` | немає придатних уривків |
| Шістнадцяткові обсяги флешу в командах read-flash | `pass-19-adresy-flesh` | немає придатних уривків |
| Службова область флешу до застосунку — 64 КБ | `pass-19-adresy-flesh` | немає придатних уривків |
| MTDI і MTDO — це GPIO12 і GPIO15 | `pass-20-jtag-obvyazka` | немає придатних уривків |
| TCK і TMS на classic — GPIO13 і GPIO14 | `pass-20-jtag-obvyazka` | немає придатних уривків |
| espefuse summary і menuconfig — досяжність доказу проходів 9 і 11 | `pass-23-dac-propahaciya` | немає придатних уривків |
| PSRAM підтримують лише classic, S2 і S3 | `pass-25-psram` | немає придатних уривків |
| Паспортна похибка DS18B20 — на датчик, а не між датчиками | `pass-37-ds18b20-porih` | немає придатних уривків |
| Режим завантаження словами друкує ROM, не esptool | `pass-38-pul-shmatky-9-11` | немає придатних уривків |
| T-23-048: Помітно менше — просадка, і далі спершу розділ | `prochid-23-triazh` | немає придатних уривків |
| T-23-035: Подавати живлення на плату з видимим дефектом означає | `prochid-23-triazh` | немає придатних уривків |
| T-23-039: Дзвенить — шукати замикання, не вмикати. | `prochid-23-triazh` | немає придатних уривків |
| T-G-061: | пріоритет | priority | | `prochid-g-glosariy` | немає придатних уривків |
| T-G-062: | черга | queue | | `prochid-g-glosariy` | немає придатних уривків |
| T-Z-135: i2c_device_config_t — 215, 327 | `prochid-z-pokazhchyk` | немає придатних уривків |
