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

Записів доказів: **233**. Звірено дослівно: **68**. Не знайдено: **51**. Джерело не в кеші: **32**. Нема чого звіряти: **82**.

Станом на 2026-08-26 19:46 UTC.


## **не знайдено** — 51

| Доказ | Файл | Деталі |
|---|---|---|
| Перевірка переповнення стека і розмір стека app_main | `pass-01-tverde-yadro` | 3 з 8 рядків: «config ESP_MAIN_TASK_STACK_SIZE…»; «int "Main task stack size"…»; «default 3584…» |
| На C3 ADC2 непридатний через апаратну ваду, а не через Wi-Fi | `pass-02-povedinka` | 1 з 3 рядків: «The results are not stable. This issue can be found in `ESP32-C3 Serie…» |
| Strapping-піни за сімействами | `pass-08-strapping` | 2 з 6 рядків: «esp32h21="GPIO14", esp32h4="GPIO14"}…»; «esp32h4="GPIO13"}…» |
| merge-bin вимагає --chip; без нього команда падає | `pass-09-komandy` | 2 з 7 рядків: «* Binary image generation commands, such as elf2image or merge-bin,…»; «require the chip type to be specified.…» |
| Стиснення при передачі ввімкнене за замовчуванням | `pass-09-komandy` | 2 з 10 рядків: «By default, the serial transfer data is compressed for better performa…»; «The ``-u/--no-compress`` option disables this behaviour.…» |
| Розбіжність обсягу флешу — два різні рядки й різні наслідки | `pass-10-povidomlennya` | 3 з 3 рядків: «ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the b…»; «"header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chi…»; «ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the bi…» |
| Помилки купи розрізняють бік переповнення | `pass-10-povidomlennya` | 2 з 2 рядків: «#define ERR_STR1 "***ERROR*** A stack overflow in task "…»; «#define ERR_STR2 " has been detected."…» |
| Тексти помилок esptool змінилися між версіями | `pass-10-povidomlennya` | 6 з 8 рядків: «msg = ("Serial data stream stopped: Possible serial noise or corruptio…»; «if successful_slip else "No serial data received.")…»; «raise FatalError(f"This chip is {chip_type}, not {self.CHIP_NAME}. Wro…» |
| Дерево menuconfig — корінь і Component config | `pass-11-menuconfig` | 9 з 13 рядків: «esptool_py:        menu "Serial flasher config"…»; «partition_table:   menu "Partition Table"…»; «bootloader:        menu "Bootloader config"…» |
| Меню логування зветься Log, а не Log output | `pass-11-menuconfig` | 4 з 5 рядків: «menu "Log Level"…»; «choice LOG_DEFAULT_LEVEL…»; «bool "Default log verbosity"…» |
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
| Рівні логу, esp_err_to_name і монітор — розділ 25 | `pass-32-pul-shmatky-1-3` | 7 з 10 рядків: «choice LOG_DEFAULT_LEVEL…»; «bool "Default log verbosity"…»; «default LOG_DEFAULT_LEVEL_INFO…» |
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

## джерело не в кеші — 32

| Доказ | Файл | Деталі |
|---|---|---|
| Розпіновка JTAG classic — datasheet як друге джерело до io_mux_reg.h | `m2-01-esp32-datasheet-iomux` | 1 джерел не в кеші |
| Споживання ESP32 за режимами — порядки збігаються з Table 4-2 | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Пін віддає більше, ніж приймає — IOH 40 мА проти IOL 28 мА | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Робочий діапазон чипа ESP32 — від −40 до 125 °C | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Діапазон модуля WROOM — 85 °C у версіях N, 105 °C у версіях H | `m2-02-esp32-datasheet` | 1 джерел не в кеші |
| Абсолютний максимум входу — 3.6 В, тому 5 В убивають пін | `m2-06-napruga-mezhi` | 1 джерел не в кеші |
| Нижня межа частот STM32 — 24 МГц у Value line | `m2-13-stm32-chastoty` | 2 джерел не в кеші |
| Свинцевий припій плавиться нижче за безсвинцевий | `m2-17-pripiy-i-ip` | 1 джерел не в кеші |
| Кількість блоків периферії за сімействами | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Апаратні піни IOMUX для UART0 і SPI | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Типові піни I²C і бортового світлодіода в Arduino | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Виклики FreeRTOS і атрибути розміщення | `pass-07-api-rozbyvka` | 1 джерел не в кеші |
| Решта команд esptool і idf.py, що вживає книга, існує дослівно | `pass-09-komandy` | 1 джерел не в кеші |
| Повідомлення бутлоадера про образ і розділи | `pass-10-povidomlennya` | 1 джерел не в кеші |
| Maximum log verbosity — стеля компіляції окремо від типового рівня | `pass-11-menuconfig` | 2 джерел не в кеші |
| Відкат вмикається в підменю Application Rollback | `pass-11-menuconfig` | 1 джерел не в кеші |
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
| PSRAM вимкнена типово, а винесення в неї — навпаки, ввімкнене | `pass-25-psram` | 3 джерел не в кеші |
| Octal PSRAM треба зазначити — типово стоїть Quad | `pass-25-psram` | 1 джерел не в кеші |
| Мілісекунди в дужках у рядку логу | `pass-29-log-i-reshta-komand` | 1 джерел не в кеші |
| Номери GPIO книги дійсні для сімейств, яким приписані | `pass-30-piny-suciljno` | 1 джерел не в кеші |
| Тільки-вхідні, консоль і USB-JTAG у довіднику пінів | `pass-33-pul-shmatky-4-5` | 1 джерел не в кеші |
| Піновий план проєкту 62 — три сімейства, кожен пін вільний | `pass-33-pul-shmatky-4-5` | 1 джерел не в кеші |

## звірено — 68

| Доказ | Файл | Деталі |
|---|---|---|
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
| GPIO11 на C3 — це майданчик VDD_SPI, живлення флешу | `pass-38-pul-shmatky-9-11` | 7 рядків |
| Рядки режиму завантаження — перелік із документації esptool | `pass-39-pul-haiku` | 3 рядків |
| Пін входу в бутлоадер за сімействами — підстановки esptool | `pass-39-pul-haiku` | 3 рядків |
| Внутрішнє підтягування 45 кОм на піні входу в бутлоадер | `pass-39-pul-haiku` | 2 рядків |
| GPIO16 і GPIO17 на classic живляться з домену VDD_SDIO | `pass-39-pul-haiku` | 3 рядків |
| GPIO5 на classic — CS апаратного VSPI | `pass-39-pul-haiku` | 1 рядків |
| Сила драйвера GPIO — типова середня, і файл лежить не там | `pass-39-pul-haiku` | 5 рядків |

## нема чого звіряти — 82

| Доказ | Файл | Деталі |
|---|---|---|
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
| Таблиця симптомів веде в тематично правильні розділи | `pass-14-marshruty` | немає URL |
| Версії тулчейну — усі чотири найновіші на дату ревізії | `pass-15-versiyi` | немає URL |
| Адреси I²C у додатку E — усі тринадцять рядків | `pass-16-interfeysy` | немає URL |
| Програмний ліміт часу не рятує від зварених контактів реле | `pass-17-simeystva-proektiv` | немає придатних уривків |
| Шістнадцяткові обсяги флешу в командах read-flash | `pass-19-adresy-flesh` | немає придатних уривків |
| Службова область флешу до застосунку — 64 КБ | `pass-19-adresy-flesh` | немає URL |
| MTDI і MTDO — це GPIO12 і GPIO15 | `pass-20-jtag-obvyazka` | немає придатних уривків |
| TCK і TMS на classic — GPIO13 і GPIO14 | `pass-20-jtag-obvyazka` | немає придатних уривків |
| espefuse summary і menuconfig — досяжність доказу проходів 9 і 11 | `pass-23-dac-propahaciya` | немає придатних уривків |
| PSRAM підтримують лише classic, S2 і S3 | `pass-25-psram` | немає придатних уривків |
| Режим завантаження словами друкує ROM, не esptool | `pass-38-pul-shmatky-9-11` | немає придатних уривків |
