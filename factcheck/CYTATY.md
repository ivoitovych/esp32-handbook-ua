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

Записів доказів: **469**. Звірено дослівно: **73**. Не знайдено: **50**. Джерело не в кеші: **40**. Нема чого звіряти: **274**.

Станом на 2026-08-26 22:57 UTC.


## клас E на твердженні з числом — перевірити — 32

| Доказ | Файл | Деталі |
|---|---|---|
| Живлення 5 В і виводи 3.3 В на одному модулі — загальна можливість, не вимірюваний факт | `m2-20-rivni-i-klyuchi` | клас E, а в назві число з одиницею |
| Живлення 3.3 В без сприйняття 3.3 В як одиниці — та сама логічна можливість | `m2-20-rivni-i-klyuchi` | клас E, а в назві число з одиницею |
| Перегрів звичайного MOSFET від 3.3 В — не звірено цим набором джерел | `m2-20-rivni-i-klyuchi` | клас E, а в назві число з одиницею |
| 10 кОм від затвора на землю — стандартна практика, не звірена окремим джерелом | `m2-20-rivni-i-klyuchi` | клас E, а в назві число з одиницею |
| Нестабільна робота реле від 3.3 В — не звірено джерелами цього кроку | `m2-20-rivni-i-klyuchi` | клас E, а в назві число з одиницею |
| «USB-роз'єм... стабілізатор... 3.3 В» — топологія плати розробки, не факт із datasheet кристала | `m2-21-zhyvlennya-06` | клас E, а в назві число з одиницею |
| «Сюди можна подавати 5 В (залежить від стабілізатора на платі)» — явно позначена залежність від конкретної плати | `m2-21-zhyvlennya-06` | клас E, а в назві число з одиницею |
| Конденсатор 470 мкФ між 3V3 і GND — стандартна практика розв'язки живлення, номінал не з datasheet ESP32 | `m2-21-zhyvlennya-06` | клас E, а в назві число з одиницею |
| «Окреме джерело від 1 А» і «знизити пікове споживання» — поради з порядку дешевизни, практика | `m2-21-zhyvlennya-06` | клас E, а в назві число з одиницею |
| Релейний модуль з оптопарою — 5 В і інверсна логіка не паспортні | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| Конвертер рівнів на польових — призначення 3.3↔5 В | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| Buck-boost 3.3 В — призначення «автономний пристрій» | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| 10 кОм — підтягування входів і затвор MOSFET на землю — практика без чипа | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| 100–220 Ом послідовно з затвором — практика без чипа | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| 100 нФ біля кожної мікросхеми — загальна практика, не паспорт | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| 470 мкФ біля роз'єму живлення — загальна практика, не паспорт | `m2-22-vkladysh-components` | клас E, а в назві число з одиницею |
| Buck-boost і резистори 4.7 кОм — кількість і службова примітка в BOM | `m2-23-proekty-60-62` | клас E, а в назві число з одиницею |
| Модуль реле — коло котушки на окремих 5 В, а не 3V3 (без конкретної мікросхеми) | `m2-23-proekty-60-62` | клас E, а в назві число з одиницею |
| Оптопара не гарантує сумісності з 3.3 В — падіння струму світлодіода | `m2-23-proekty-60-62` | клас E, а в назві число з одиницею |
| Резистори 220 Ом і 10 кОм модуля реле й поплавка — кількість у BOM | `m2-23-proekty-60-62` | клас E, а в назві число з одиницею |
| Стабілізатор (LDO) · 3.3 В із 5 В | `m2-26-k03-i-platy` | клас E, а в назві число з одиницею |
| HC-SR04 — дільник напруги 10кОм + 20кОм | `m2-28-sensory-45` | клас E, а в назві число з одиницею |
| Вхідна напруга на роз'ємі від USB — норма 5 В ±5 % | `m2-31-kartka-k13` | клас E, а в назві число з одиницею |
| Конденсатор 470 мкФ між 3V3 і GND поруч із модулем | `m2-31-kartka-k13` | клас E, а в назві число з одиницею |
| Керамічний 100 нФ біля кожної мікросхеми | `m2-31-kartka-k13` | клас E, а в назві число з одиницею |
| Живлення 3.3 В напряму, мимо бортовий LDO — коли він слабкий на клоне | `m2-31-kartka-k13` | клас E, а в назві число з одиницею |
| Реле не спрацьовує — модуль керування на 5 В | `m2-32-symptomy-b` | клас E, а в назві число з одиницею |
| Реле не спрацьовує — дія: живити модуль від 5 В | `m2-32-symptomy-b` | клас E, а в назві число з одиницею |
| LDO з малим падінням: 100–200 мВ | `m2-43-akum-53` | клас E, а в назві число з одиницею |
| Проблема: низька напруга живлення — додати 470 мкФ конденсатор | `m2-45-motory-symptomy` | клас E, а в назві число з одиницею |
| Wi-Fi відвалюється: подивитися RSSI гірше за −80 дБм | `m2-48-symptomy-29` | клас E, а в назві число з одиницею |
| T-K12-007: Паяльник повинен мати терморегулятор, потужність 60 Вт, жало «скіс» 2–3 мм | `m2-50-kartky` | клас E, а в назві число з одиницею |

## **не знайдено** — 50

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

## джерело не в кеші — 40

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
| «IVDD, current delivered by external power supply, Min 0.5 A» — дослівна цитата datasheet | `m2-21-zhyvlennya-06` | 1 джерел не в кеші |
| Частота RP2040 | `m2-40-rp2040` | 1 джерел не в кеші |
| RAM RP2040 | `m2-40-rp2040` | 1 джерел не в кеші |
| Радіо (Wireless) на RP2040 | `m2-40-rp2040` | 1 джерел не в кеші |
| Real-time Clock (RTC) на RP2040 | `m2-40-rp2040` | 1 джерел не в кеші |
| DORMANT режим - сон з мінімальним споживанням | `m2-40-rp2040` | 1 джерел не в кеші |
| DORMANT режим - типовий струм | `m2-40-rp2040` | 1 джерел не в кеші |
| SLEEP режим - сон з більшим споживанням | `m2-40-rp2040` | 1 джерел не в кеші |
| Boot Sequence - контрольована апаратом | `m2-40-rp2040` | 1 джерел не в кеші |
| UF2 Bootloader в ROM | `m2-40-rp2040` | 1 джерел не в кеші |
| ОС - MicroPython порт | `m2-40-rp2040` | 1 джерел не в кеші |
| 264kB SRAM в 6 банках | `m2-40-rp2040` | 1 джерел не в кеші |
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

## звірено — 73

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
| GPIO11 на C3 — це майданчик VDD_SPI, живлення флешу | `pass-38-pul-shmatky-9-11` | 7 рядків |
| Рядки режиму завантаження — перелік із документації esptool | `pass-39-pul-haiku` | 3 рядків |
| Пін входу в бутлоадер за сімействами — підстановки esptool | `pass-39-pul-haiku` | 3 рядків |
| Внутрішнє підтягування 45 кОм на піні входу в бутлоадер | `pass-39-pul-haiku` | 2 рядків |
| GPIO16 і GPIO17 на classic живляться з домену VDD_SDIO | `pass-39-pul-haiku` | 3 рядків |
| GPIO5 на classic — CS апаратного VSPI | `pass-39-pul-haiku` | 1 рядків |
| Сила драйвера GPIO — типова середня, і файл лежить не там | `pass-39-pul-haiku` | 5 рядків |

## нема чого звіряти — 274

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
| Резистор 100–220 Ом — межа кидка струму в межах можливостей піна ESP32 | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
| Реле на 5 В — спостереження за ринком модулів | `m2-20-rivni-i-klyuchi` | немає придатних уривків |
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
| 120 Ом термінаторів RS-485/CAN — стандарт, недосяжний з мережі | `m2-22-vkladysh-components` | немає придатних уривків |
| DS18B20 — ±0.5 °C на один датчик, звідси розбіжність до 1 °C у двох справних | `m2-22-vkladysh-components` | немає URL |
| DS18B20 — поріг 0.5 °C бракував би справні датчики | `m2-22-vkladysh-components` | немає придатних уривків |
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
| 3.3 В на холостому ході — норма 3.2–3.4 В | `m2-31-kartka-k13` | немає URL |
| Окреме джерело від 1 А — не 500 мА, тому що платити треба за піки | `m2-31-kartka-k13` | немає URL |
| Джерело для ESP32 з Wi-Fi — щонайменше 1 А, навіть якщо середнє споживання сто міліампер | `m2-31-kartka-k13` | немає URL |
| `rst:0xf` — симптом просідання живлення | `m2-32-symptomy-b` | немає придатних уривків |
| Перезавантаження при Wi-Fi — джерело не тягне піків | `m2-32-symptomy-b` | немає URL |
| Стабілізатор гарячий — перевантаження або слабкий клон | `m2-32-symptomy-b` | немає придатних уривків |
| I²C не знаходить пристрій — немає підтягування | `m2-32-symptomy-b` | немає придатних уривків |
| RS-485: помилки на довгій лінії — потрібни термінатори | `m2-32-symptomy-b` | немає придатних уривків |
| Реле вмикається при старті — вхід ключа висить при завантаженні | `m2-32-symptomy-b` | немає придатних уривків |
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
