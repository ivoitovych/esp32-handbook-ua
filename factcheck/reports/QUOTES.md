# Третій шар: цитати проти джерел

**Генерується** `factcheck/tools/layer3.py --zvit`. Правити вручну нема сенсу.

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

Записів доказів: **1366**. Звірено дослівно: **589**. Не знайдено: **60**. Джерело не в кеші: **36**. Нема чого звіряти: **658**.

Станом на 2026-09-01 04:18 UTC.


## клас E на твердженні з числом — перевірити — 23

| Доказ | Файл | Деталі |
|---|---|---|
| Живлення 5 В і виводи 3.3 В на одному модулі — загальна можливість, не вимірюваний факт | `m2-20-levels-and-switches` | клас E, а в назві число з одиницею |
| Живлення 3.3 В без сприйняття 3.3 В як одиниці — та сама логічна можливість | `m2-20-levels-and-switches` | клас E, а в назві число з одиницею |
| «USB-роз'єм... стабілізатор... 3.3 В» — топологія плати розробки, не факт із datasheet кристала | `m2-21-power-06` | клас E, а в назві число з одиницею |
| «Сюди можна подавати 5 В (залежить від стабілізатора на платі)» — явно позначена залежність від конкретної плати | `m2-21-power-06` | клас E, а в назві число з одиницею |
| Релейний модуль з оптопарою — 5 В і інверсна логіка не паспортні | `m2-22-insert-components` | клас E, а в назві число з одиницею |
| Конвертер рівнів на польових — призначення 3.3↔5 В | `m2-22-insert-components` | клас E, а в назві число з одиницею |
| Buck-boost 3.3 В — призначення «автономний пристрій» | `m2-22-insert-components` | клас E, а в назві число з одиницею |
| Buck-boost і резистори 4.7 кОм — кількість і службова примітка в BOM | `m2-23-projects-60-62` | клас E, а в назві число з одиницею |
| Модуль реле — коло котушки на окремих 5 В, а не 3V3 (без конкретної мікросхеми) | `m2-23-projects-60-62` | клас E, а в назві число з одиницею |
| Резистори 220 Ом і 10 кОм модуля реле й поплавка — кількість у BOM | `m2-23-projects-60-62` | клас E, а в назві число з одиницею |
| Конденсатор 470 мкФ між 3V3 і GND поруч із модулем | `m2-31-card-k13` | клас E, а в назві число з одиницею |
| Керамічний 100 нФ біля кожної мікросхеми | `m2-31-card-k13` | клас E, а в назві число з одиницею |
| Живлення 3.3 В напряму, мимо бортовий LDO — коли він слабкий на клоне | `m2-31-card-k13` | клас E, а в назві число з одиницею |
| Проблема: низька напруга живлення — додати 470 мкФ конденсатор | `m2-45-motors-symptoms` | клас E, а в назві число з одиницею |
| Wi-Fi відвалюється: подивитися RSSI гірше за −80 дБм | `m2-48-symptoms-29` | клас E, а в назві число з одиницею |
| T-K12-007: Паяльник повинен мати терморегулятор, потужність 60 Вт, жало «скіс» 2–3 мм | `m2-50-cards` | клас E, а в назві число з одиницею |
| Конденсатор 100–470 мкФ біля живлення — стабілізація напруги | `m2-65-electronics-05` | клас E, а в назві число з одиницею |
| MOSFET затвор — резистор 100–220 Ом від GPIO, захист від перегріву | `m2-65-electronics-05` | клас E, а в назві число з одиницею |
| MOSFET затвор — резистор 10 кОм від затвора до землі, утримання LOW при старті | `m2-65-electronics-05` | клас E, а в назві число з одиницею |
| T-36-120: SPI діагностика — знизити швидкість до 1 МГц | `m2-92-sample` | клас E, а в назві число з одиницею |
| T-59-114: 16 КБ з купи замість локального масиву | `m2-94-sample` | клас E, а в назві число з одиницею |
| T-60-123: Запис на картку займає 400 мс | `m2-94-sample` | клас E, а в назві число з одиницею |
| Модулі на 8 і 16 МБ флешу коштують істотно дорожче за різницю у ціні | `m2-95-sample` | клас E, а в назві число з одиницею |

## **не знайдено** — 60

| Доказ | Файл | Деталі |
|---|---|---|
| Розпіновка JTAG classic — datasheet як друге джерело до io_mux_reg.h | `m2-01-esp32-datasheet-iomux` | 1 з 8 рядків: «MTCK    JTAG interface signals…» |
| T-K06-045: На 115200 нічого, на 74880 осмислений текст — це ESP8266 | `m2-62-bootlog-k06` | 1 з 1 рядків: «The ESP8266 boot rom writes a log to the UART when booting at ``74880 …» |
| Етап 1 — ROM bootloader зашитий у кремній | `m2-82-boot-flash` | 1 з 1 рядків: «The ROM bootloader is in read-only memory (ROM) on the ESP32 chip.…» |
| Етап 2 — другий бутлоадер bootloader.bin у флеші | `m2-82-boot-flash` | 1 з 1 рядків: «After reset, the second line printed by the ESP32 ROM is a reset & boo…» |
| Адреса bootloader.bin для ESP32 чипів — 0x1000 | `m2-82-boot-flash` | 1 з 1 рядків: «{IDF_TARGET_BOOTLOADER_OFFSET:default="0x0", esp32="0x1000", esp32s2="…» |
| GPIO0 як ключовий strapping-пін для вибору режиму завантаження | `m2-82-boot-flash` | 1 з 1 рядків: «0x10  - GPIO0…» |
| Розділи ota_0 та ota_1 у таблиці розділів для OTA | `m2-82-boot-flash` | 2 з 2 рядків: «ota_0,    app,  ota_0,   0x20000,  1M,…»; «ota_1,    app,  ota_1,   0x120000, 1M,…» |
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
| Код 0x10 означає RTCWDT_RTC_RESET (RTC watchdog скинув усе) | `m2-93-sample` | 2 з 5 рядків: «rst:0x10 (RTCWDT_RTC_RESET)…»; «unstable power source. It is enabled by default. If the execution…» |
| T-02-105: Але зроблене без збереження `sdkconfig.defaults` доведеться налаштовувати заново. | `nosignal-02-chipy` | 1 з 1 рядків: «For example projects or other projects where you dont want to specify …» |
| Перевірка переповнення стека і розмір стека app_main | `pass-01-tverde-yadro` | 3 з 8 рядків: «config ESP_MAIN_TASK_STACK_SIZE…»; «int "Main task stack size"…»; «default 3584…» |
| На C3 ADC2 непридатний через апаратну ваду, а не через Wi-Fi | `pass-02-povedinka` | 1 з 3 рядків: «The results are not stable. This issue can be found in `ESP32-C3 Serie…» |
| Strapping-піни за сімействами | `pass-08-strapping` | 2 з 6 рядків: «esp32h21="GPIO14", esp32h4="GPIO14"}…»; «esp32h4="GPIO13"}…» |
| Розбіжність обсягу флешу — два різні рядки й різні наслідки | `pass-10-povidomlennya` | 3 з 3 рядків: «ESP_EARLY_LOGE(TAG, "Detected size(%dk) smaller than the size in the b…»; «"header(%dk). Probe failed.", default_chip.size/1024, legacy_chip->chi…»; «ESP_EARLY_LOGW(TAG, "Detected size(%dk) larger than the size in the bi…» |
| Помилки купи розрізняють бік переповнення | `pass-10-povidomlennya` | 2 з 2 рядків: «#define ERR_STR1 "***ERROR*** A stack overflow in task "…»; «#define ERR_STR2 " has been detected."…» |
| Дерево menuconfig — корінь і Component config | `pass-11-menuconfig` | 9 з 13 рядків: «esptool_py:        menu "Serial flasher config"…»; «partition_table:   menu "Partition Table"…»; «bootloader:        menu "Bootloader config"…» |
| GPIO15 низький глушить boot-лог ROM | `pass-12-piny` | 2 з 3 рядків: «|            | bootloader. Has an internal pull-up, so unconnected = H…»; «|            | normal output.…» |
| Режими SPI — CPHA задає номер фронту, не напрямок | `pass-16-interfeysy` | 1 з 3 рядків: «@param  mode   SPI data mode; one of SPI_MODE0, SPI_MODE1, SPI_MODE2…» |
| pioarduino, а не офіційна платформа PlatformIO | `pass-17-simeystva-proektiv` | 1 з 5 рядків: «"version": "55.03.311"…» |
| Підтягування I²C — діапазон, а не одне число | `pass-18-schemy` | 2 з 5 рядків: «The recommended value for pull-up resistors usually ranges from 1 kΩ t…»; «should be (but not less than 1 kΩ). Indeed, large resistors will decli…» |
| Кольорова обв'язка прикладів — classic і тільки classic | `pass-20-jtag-obvyazka` | 1 з 1 рядків: «esp32: SOC_GPIO_PIN_COUNT 40…» |
| Рівні strapping і недійсна комбінація — усі сімейства | `pass-26-strapping` | 6 з 12 рядків: «{IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",…»; «{STRAP_BOOT_2_GPIO} must also be either left unconnected/floating,…»; «{STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the…» |
| Маска GPIO_STRAP — усі шість бітів classic і два біти решти | `pass-26-strapping` | 3 з 21 рядків: «represented in the GPIO_STRAP register.…»; «most cases, one of these modes is selected if {STRAP_BOOT_2_GPIO}…»; «has been pulled high when {STRAP_BOOT_GPIO} is low).…» |
| flash-id як засіб упізнати перемаркований модуль | `pass-28-komandy-suciljno` | 4 з 4 рядків: «chip-id     Read Chip ID…»; «flash-id    Read SPI flash manufacturer and device ID…»; «The flash-id command outputs the manufacturer and device ID of the…» |
| erase-flash стирає весь чип, включно з NVS і калібруванням | `pass-28-komandy-suciljno` | 1 з 6 рядків: «esptool erase-region 0x20000 0x4000…» |
| merge-bin дає один образ на адресу 0x0 незалежно від сімейства | `pass-28-komandy-suciljno` | 4 з 5 рядків: «The merge-bin command will merge multiple binary files (of any kind)…»; «between the input files are padded with 0xFF bytes (or 0x00 in…»; «--format hex).…» |
| Рядки помилок з'єднання — Failed to connect і сусіди | `pass-29-log-i-reshta-komand` | 3 з 3 рядків: «A fatal error occurred: Failed to connect to {chip}: {reason}…»; «The most common reason for "Failed to connect" is that the chip is not…»; «to the same UART.…» |
| Паніка, backtrace і watchdog — назви рядків у логу | `pass-29-log-i-reshta-komand` | 2 з 3 рядків: «Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception wa…»; «Interrupt wdt timeout on CPU0…» |
| esptool і stub, автоскидання, розбіжність чипа | `pass-29-log-i-reshta-komand` | 5 з 5 рядків: «esptool has a two-stage flashing process: a small "stub" program is…»; «uploaded to RAM and run, which then performs the requested operation…»; «much faster than the ROM bootloader. ``--no-stub`` disables this.…» |
| merge-bin — прапорці флешу і призначення формату | `pass-29-log-i-reshta-komand` | 4 з 9 рядків: «between the input files are padded with 0xFF bytes.…»; «Options such as ``--flash-mode``, ``--flash-size`` and ``--flash-freq`…»; «are used to set the corresponding values in the image header, exactly…» |
| Функції strapping-пінів classic — таблиця розділу 07 поштучно | `pass-30-piny-suciljno` | 4 з 10 рядків: «GPIO2 must also be either left unconnected/floating, or driven Low,…»; «bootloader. |…»; «0x01 - GPIO5   0x02 - MTDO (GPIO15)   0x04 - GPIO4…» |
| Піни флешу, тільки-вхідні й ADC1 при Wi-Fi | `pass-30-piny-suciljno` | 5 з 5 рядків: «MSPI_IOMUX_PIN_NUM_CLK   6      MSPI_IOMUX_PIN_NUM_MISO  7…»; «MSPI_IOMUX_PIN_NUM_MOSI  8      MSPI_IOMUX_PIN_NUM_HD    9…»; «MSPI_IOMUX_PIN_NUM_WP   10      MSPI_IOMUX_PIN_NUM_CS0  11…» |
| Вхід у download mode вручну — порядок і його причина | `pass-30-piny-suciljno` | 4 з 7 рядків: «The {chip} will enter the serial bootloader when {STRAP_BOOT_GPIO} is…»; «{STRAP_BOOT_GPIO} has an internal pullup resistor, so if it is left…»; «development boards) that pulls {STRAP_BOOT_GPIO} low when pressed.…» |
| I²C і strapping на C3 — підтяжки збігаються з потрібними рівнями | `pass-30-piny-suciljno` | 4 з 6 рядків: «{STRAP_BOOT_2_GPIO} must also be driven High, in order to enter the…»; «{STRAP_BOOT_2_GPIO} = 0 and {STRAP_BOOT_GPIO} = 0 is invalid and will…»; «ADC1_GPIO0_CHANNEL 0   ADC1_GPIO1_CHANNEL 1   ADC1_GPIO2_CHANNEL 2…» |
| ESP_ERROR_CHECK — це assert, а не обробка помилок | `pass-31-adresy-i-api` | 2 з 15 рядків: «#define ESP_OK          0    /*!< esp_err_t value indicating success *…»; «* message but isn't terminating the program.…» |
| ESP_LOGD не коштує нічого при рівні збирання Info | `pass-31-adresy-i-api` | 6 з 6 рядків: «* @brief Compile-time log level.…»; «* removed by the preprocessor and take no space in the binary and no…»; «* time at runtime.…» |
| Коди помилок OTA і NVS, які книга називає поіменно | `pass-31-adresy-i-api` | 2 з 6 рядків: «partition, and is used together with the FAT filesystem via…»; «esp_vfs_fat_spiflash_mount_rw_wl.…» |
| DAC, ADC-затухання й обв'язка входу — розділ 33 | `pass-32-pul-shmatky-1-3` | 8 з 11 рядків: «Under ADC_ATTEN_DB_0, the attenuation of ADC is set to 0 dB, and input…»; «voltage higher than 950 mV is not supported. Under ADC_ATTEN_DB_12,…»; «the attenuation of ADC is set to 11 dB, and input voltage higher than…» |
| Рівні логу, esp_err_to_name і монітор — розділ 25 | `pass-32-pul-shmatky-1-3` | 1 з 10 рядків: «*        with specific address you gave.…» |
| Типова розбивка флешу — зсуви, розміри й суфікси | `pass-32-pul-shmatky-1-3` | 3 з 11 рядків: «ESP_LOGI(TAG, "Partition Table:");…»; «ESP_LOGI(TAG, "## Label            Usage          Type ST Offset   Len…»; «ESP_LOGI(TAG, "End of partition table");…» |
| Буфер у PSRAM без MALLOC_CAP_SPIRAM — і що це коштує | `pass-32-pul-shmatky-1-3` | 5 з 11 рядків: «// Forces data into DRAM instead of flash…»; «#define DRAM_ATTR _SECTION_ATTR_IMPL(".dram1", __COUNTER__)…»; «config FREERTOS_CHECK_STACKOVERFLOW_NONE…» |
| Strapping classic і C3 — таблиця розділу 07 проти gpio/*.inc | `pass-33-pul-shmatky-4-5` | 1 з 3 рядків: «{IDF_TARGET_STRAP_BOOT_GPIO:default="GPIO9", esp32="GPIO0",…» |
| erase-flash, flash-id і коли стирання справді потрібне | `pass-34-pul-shmatok-6` | 1 з 12 рядків: «Old command and option names are **deprecated**.…» |
| Автоскидання не працює — перелік причин, крім однієї | `pass-34-pul-shmatok-6` | 2 з 9 рядків: «esptool is not able to reset your hardware automatically in the…»; «Check the chip is receiving 3.3V from a stable power source.…» |
| Коди RESET_REASON — уся таблиця причин скидання | `pass-35-vlasna-pomylka-boot` | 1 з 19 рядків: «SDIO_RESET             =  6,    /**<6, Reset by SLC module*/…» |
| ROM класифікує boot: значення цілком, а не пін за піном | `pass-35-vlasna-pomylka-boot` | 1 з 7 рядків: «#define ETS_IS_FLASH_BOOT()  (IS_1XXX(BOOT_MODE_GET()) || \…» |
| sdkconfig.defaults рекомендовано тримати в системі контролю версій | `pass-45-sdkconfig-defaults` | 1 з 1 рядків: «It is recommended to commit sdkconfig.defaults for providing baseline …» |
| T-17-118: Друга половина рядка залежить від версії. | `sweep-17-esptool` | 1 з 1 рядків: «'esptool v{__version__}'…» |

## джерело не в кеші — 36

| Доказ | Файл | Деталі |
|---|---|---|
| Нижня межа частот STM32 — 24 МГц у Value line | `m2-13-stm32-clocks` | 2 джерел не в кеші |
| Адреса bootloader.bin для S3, C3, C6, H2 — 0x0 | `m2-90-sample` | 1 джерел не в кеші |
| Код скидання 0xa — INTRUSION_RESET (детектор втручання), рідко трапляється | `m2-90-sample` | 1 джерел не в кеші |
| Код скидання 0xd названий RTCWDT_CPU_RESET | `m2-95-sample` | 1 джерел не в кеші |
| Код скидання 0x10 названий RTCWDT_RTC_RESET | `m2-95-sample` | 1 джерел не в кеші |
| Код скидання 0xc означає скидання ядра з коду | `m2-95-sample` | 1 джерел не в кеші |
| Код 0x08 на ESP32-C3 відповідає GPIO9 (strapping pin) | `m2-95-sample` | 1 джерел не в кеші |
| Bootloader розташований за адресою 0x0 на S3, C3, C6, H2 | `m2-95-sample` | 1 джерел не в кеші |
| T-D-025 — `0x8` код помилки, watchdog таймера 1 | `m2-96-sample` | 1 джерел не в кеші |
| T-D-046 — `0xf` код помилки RTCWDT_BROWN_OUT_RESET | `m2-96-sample` | 1 джерел не в кеші |
| Кількість блоків периферії за сімействами | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Апаратні піни IOMUX для UART0 і SPI | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Типові піни I²C і бортового світлодіода в Arduino | `pass-01-tverde-yadro` | 1 джерел не в кеші |
| Виклики FreeRTOS і атрибути розміщення | `pass-07-api-rozbyvka` | 1 джерел не в кеші |
| Решта команд esptool і idf.py, що вживає книга, існує дослівно | `pass-09-komandy` | 1 джерел не в кеші |
| Повідомлення бутлоадера про образ і розділи | `pass-10-povidomlennya` | 1 джерел не в кеші |
| Тексти помилок esptool змінилися між версіями | `pass-10-povidomlennya` | 1 з 2 джерел не в кеші; решта не покрила 6 з 8 рядків |
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
| Зсув бутлоадера по сімействах — числа праві, причина хибна | `pass-24-zsuvy-i-matrycya` | 1 з 2 джерел не в кеші; решта не покрила 14 з 21 рядків |
| Піновий план проєкту 60 — обидва сімейства | `pass-24-zsuvy-i-matrycya` | 1 з 4 джерел не в кеші; решта не покрила 8 з 17 рядків |
| Іменування й версії esptool — version, esptool.py, дефіси проти підкреслень | `pass-28-komandy-suciljno` | 1 з 2 джерел не в кеші; решта не покрила 4 з 4 рядків |
| Мілісекунди в дужках у рядку логу | `pass-29-log-i-reshta-komand` | 1 джерел не в кеші |
| Роль esptool і послідовність дій із незнайомою платою | `pass-29-log-i-reshta-komand` | 1 з 2 джерел не в кеші; решта не покрила 2 з 2 рядків |
| Номери GPIO книги дійсні для сімейств, яким приписані | `pass-30-piny-suciljno` | 1 джерел не в кеші |
| Тільки-вхідні, консоль і USB-JTAG у довіднику пінів | `pass-33-pul-shmatky-4-5` | 1 з 2 джерел не в кеші; решта не покрила 7 з 7 рядків |
| Піновий план проєкту 62 — три сімейства, кожен пін вільний | `pass-33-pul-shmatky-4-5` | 1 з 4 джерел не в кеші; решта не покрила 3 з 3 рядків |
| chip-id на сімействі ESP32 повертає попередження, а не Chip ID | `pass-36-chip-id` | 2 з 3 джерел не в кеші; решта не покрила 10 з 17 рядків |

## звірено — 589

| Доказ | Файл | Деталі |
|---|---|---|
| Споживання ESP32 за режимами — порядки збігаються з Table 4-2 | `m2-02-esp32-datasheet` | 5 рядків |
| Пін віддає більше, ніж приймає — IOH 40 мА проти IOL 28 мА | `m2-02-esp32-datasheet` | 2 рядків |
| Робочий діапазон чипа ESP32 — від −40 до 125 °C | `m2-02-esp32-datasheet` | 2 рядків |
| Діапазон модуля WROOM — 85 °C у версіях N, 105 °C у версіях H | `m2-02-esp32-datasheet` | 10 рядків |
| Абсолютний максимум входу — 3.6 В, тому 5 В убивають пін | `m2-06-voltage-limits` | 3 рядків |
| Свинцевий припій плавиться нижче за безсвинцевий | `m2-17-solder-and-ip` | 5 рядків |
| Перегрів звичайного MOSFET від 3.3 В — не звірено цим набором джерел | `m2-20-levels-and-switches` | 1 рядків |
| «IVDD, current delivered by external power supply, Min 0.5 A» — дослівна цитата datasheet | `m2-21-power-06` | 2 рядків |
| Тест на 3.1 В — узгоджено з порогом коду й нижньою межею buck-boost | `m2-23-projects-60-62` | 4 рядків |
| HC-SR04 — дільник напруги 10кОм + 20кОм | `m2-28-sensors-45` | 1 рядків |
| 0x1: Що сталося → подано живлення або EN | `m2-60-panic-a` | 1 рядків |
| 0x1: Що робити → норма | `m2-60-panic-a` | 1 рядків |
| 0x3: Назва → SW_RESET | `m2-60-panic-a` | 1 рядків |
| 0x3: Що робити → норма, якщо ваша | `m2-60-panic-a` | 1 рядків |
| 0x4: Назва → OWDT_RESET | `m2-60-panic-a` | 1 рядків |
| 0x4: Що сталося → застарілий watchdog | `m2-60-panic-a` | 1 рядків |
| 0x4: Що робити → рідко | `m2-60-panic-a` | 1 рядків |
| 0x5: Назва → DEEPSLEEP_RESET | `m2-60-panic-a` | 1 рядків |
| 0x5: Що сталося → прокинувся з deep sleep | `m2-60-panic-a` | 1 рядків |
| 0x5: Що робити → норма | `m2-60-panic-a` | 1 рядків |
| 0x6: Назва → SDIO_RESET | `m2-60-panic-a` | 1 рядків |
| 0x6: Що сталося → скидання модулем SLC | `m2-60-panic-a` | 1 рядків |
| 0x6: Що робити → рідко | `m2-60-panic-a` | 1 рядків |
| 0x7: Що сталося → watchdog таймера 0 | `m2-60-panic-a` | 1 рядків |
| 0x8: Назва → TG1WDT_SYS_RESET | `m2-60-panic-a` | 1 рядків |
| 0x8: Що сталося → watchdog таймера 1 | `m2-60-panic-a` | 1 рядків |
| 0x9: Назва → RTCWDT_SYS_RESET | `m2-60-panic-a` | 1 рядків |
| 0x9: Що сталося → RTC watchdog | `m2-60-panic-a` | 1 рядків |
| 0xa: Назва → INTRUSION_RESET | `m2-60-panic-a` | 1 рядків |
| T-D-153: EXCVADDR — найшвидша підказка | `m2-61-panic-b` | 1 рядків |
| T-D-159: IDLE0 та Task Watchdog Timeout | `m2-61-panic-b` | 1 рядків |
| T-D-172: assert failed як порушення інваріанта | `m2-61-panic-b` | 3 рядків |
| T-D-183: rst: у першому рядку RTC Watchdog Timeout | `m2-61-panic-b` | 3 рядків |
| T-D-184: Причина паніки і EXCVADDR | `m2-61-panic-b` | 1 рядків |
| T-D-185: Backtrace через .elf за допомогою IDF Monitor | `m2-61-panic-b` | 5 рядків |
| T-D-187: Coredump та логування переходів станів при невідтворюванні | `m2-61-panic-b` | 1 рядків |
| T-D-188: Backtrace без .elf нерозшифровний | `m2-61-panic-b` | 1 рядків |
| T-K06-001: Монітор на 115200 бод для читання boot-логу | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-005: rst: — причина останнього скидання чипа | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-009: 0x1 (POWERON_RESET) — подано живлення або натиснуто EN | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-026: boot: — куди пішов чип (SPI_FAST_FLASH_BOOT або DOWNLOAD_BOOT) | `m2-62-bootlog-k06` | 1 рядків |
| T-K06-038: Garbage символи при 115200 означають ESP8266; на 74880 читається | `m2-62-bootlog-k06` | 1 рядків |
| Touch сенсори є лише на classic, S2 и S3 | `m2-63-gpio-07` | 1 рядків |
| Схема реле: +12 В → насос → реле (NO) → аварійний вимикач → GND | `m2-67-project-62` | 1 рядків |
| Лог переходу між станами чипа з причиною | `m2-67-project-62` | 1 рядків |
| Керування насосом функцією nasos_keruvaty на основі стану | `m2-67-project-62` | 1 рядків |
| Оновлення індикації при зміні стану | `m2-67-project-62` | 1 рядків |
| Максимум часу безперервної роботи насоса: 600 секунд (10 хвилин) | `m2-67-project-62` | 1 рядків |
| Час паузи після вимкнення насоса: 300 секунд (5 хвилин) | `m2-67-project-62` | 1 рядків |
| ESP32 classic або C3 — одиниця в проєкті логера | `m2-68-project-60` | 1 рядків |
| Таблиця розпіновки: Сигнал | classic | C3 | `m2-68-project-60` | 1 рядків |
| На C3 рідним для MISO залишився тільки GPIO2, який уже інакше використовується | `m2-68-project-60` | 2 рядків |
| GPIO2 використовується як strapping-пін для дільника, чинний лише як вихід | `m2-68-project-60` | 3 рядків |
| Для C3 піни слід взяти з таблиці розпіновки | `m2-68-project-60` | 1 рядків |
| GPIO2 як strapping-пін на C3 — свідомий компроміс | `m2-68-project-60` | 2 рядків |
| Лог при розрядженому акумуляторі (< 3.2 В) | `m2-68-project-60` | 1 рядків |
| Лог про недоступність карти microSD | `m2-68-project-60` | 1 рядків |
| Базовий проєкт із Wi-Fi, I²C, веб-сервером, mDNS, зберіганням стану й обробкою помилок | `m2-69-project-59` | 2 рядків |
| ESP32-S3-DevKitC-1 або classic DevKitC — одиниця в проєкті моніторингу | `m2-69-project-59` | 1 рядків |
| Таблиця розпіновки: Сигнал | classic DevKitC | S3-DevKitC-1 | `m2-69-project-59` | 1 рядків |
| GPIO22 на S3 не існує; запит повертає ESP_ERR_INVALID_ARG без ESP_ERROR_CHECK | `m2-69-project-59` | 10 рядків |
| Include драйвера I²C master | `m2-69-project-59` | 1 рядків |
| Константа для історії: 720 записів (12 годин при вимірюванні раз на хвилину) | `m2-69-project-59` | 1 рядків |
| Таблиця розділів з адресами nvs 0x9000 та factory 0x10000 | `m2-82-boot-flash` | 2 рядків |
| Сторож (Watchdog) автоматично перезавантажує систему при зависанні | `m2-84-freertos` | 2 рядків |
| Task Watchdog Timer та Interrupt Watchdog Timer у ESP-IDF | `m2-84-freertos` | 3 рядків |
| I2C: на спокої обидві лінії мають бути HIGH (3.3 В). Якщо немає — поломаний резистор підтягування. | `m2-90-sample` | 3 рядків |
| T-D-040: 0xd = RTCWDT_CPU_RESET, що робити → розділ 32 | `m2-94-sample` | 1 рядків |
| T-D-043: 0xe = EXT_CPU_RESET, норма | `m2-94-sample` | 1 рядків |
| T-D-041: 0xe = EXT_CPU_RESET (Назва) | `m2-94-sample` | 1 рядків |
| Сучасні роутери часто розділяють SSID для діапазонів; ESP32 не бачить 5 ГГц | `m2-97-sample` | 1 рядків |
| Літієві батареї не заряджаються нижче 0 °C і втрачають ємність на морозі | `m2-97-sample` | 1 рядків |
| T-02-024: Частота, МГц · ESP32 → 240 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-027: Частота, МГц · C3 → 160 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-029: Частота, МГц · H2 → 96 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-031: SRAM, КБ · S2 → 320 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-032: SRAM, КБ · S3 → 512 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-033: SRAM, КБ · C3 → 400 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-034: SRAM, КБ · C6 → 512 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-013: Ядро · S2 → Xtensa LX7 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-016: Ядро · C6 → RISC-V | `m2-98-chips-datasheets` | 1 рядків |
| T-02-017: Ядро · H2 → RISC-V | `m2-98-chips-datasheets` | 1 рядків |
| T-02-020: Ядер · S3 → **2** | `m2-98-chips-datasheets` | 1 рядків |
| T-02-133: Zigbee, Thread, Matter · Чип → C6 або H2 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-139: Налагодження без адаптера · Чип → S3, C3 | `m2-98-chips-datasheets` | 1 рядків |
| T-02-146: S2 без Bluetooth узагалі. | `m2-98-chips-datasheets` | 1 рядків |
| T-04-092: I²S · classic → 2 | `m2-99-peripherals-cores` | 1 рядків |
| T-04-070: UART · S3 → 3 | `m2-99-peripherals-cores` | 1 рядків |
| T-A-021: 5 · Обмеження → **strapping** | `m2-a1-pinouts-adc-strapping` | 1 рядків |
| T-A-078: 2 · Обмеження → **strapping** | `m2-a1-pinouts-adc-strapping` | 1 рядків |
| T-A-053: 32, 33 · Примітка → **ADC1 — працює при Wi-Fi** | `m2-a1-pinouts-adc-strapping` | 1 рядків |
| T-A-058: **ADC2** (не працює при Wi-Fi): 0, 2, 4, 12, 13, 14, 15, 25, 26, 2 | `m2-a1-pinouts-adc-strapping` | 1 рядків |
| T-A-101: UART0 TX / RX · [[C3]] → 21 / 20 | `m2-a1-pinouts-adc-strapping` | 1 рядків |
| T-02-042: Wi-Fi · ESP32 → так | `nosignal-02-chipy` | 1 рядків |
| T-02-043: Wi-Fi · S2 → так | `nosignal-02-chipy` | 1 рядків |
| T-02-044: Wi-Fi · S3 → так | `nosignal-02-chipy` | 1 рядків |
| T-02-047: Wi-Fi · H2 → **ні** | `nosignal-02-chipy` | 1 рядків |
| T-02-054: BLE · ESP32 → так | `nosignal-02-chipy` | 1 рядків |
| T-02-055: BLE · S2 → **ні** | `nosignal-02-chipy` | 1 рядків |
| T-02-057: BLE · C3 → так | `nosignal-02-chipy` | 1 рядків |
| T-02-096: **Переноситься майже завжди:** код на ESP-IDF, написаний через | `nosignal-02-chipy` | 1 рядків |
| T-02-099: Перенесення проєкту на інший чип в ESP-IDF починається | `nosignal-02-chipy` | 2 рядків |
| T-02-103: Усі налаштування, зроблені через `menuconfig`, повертаються до типових. | `nosignal-02-chipy` | 1 рядків |
| T-11-001: ESP-IDF (Espressif IoT Development Framework) — офіційний фреймворк | `nosignal-11-idf` | 1 рядків |
| T-11-013: **Windows.** Офіційний інсталятор ESP-IDF Tools Installer ставить усе | `nosignal-11-idf` | 1 рядків |
| T-11-025: Спокуса прописати `export.sh` у `.bashrc` є в усіх, | `nosignal-11-idf` | 1 рядків |
| T-11-112: `set-target` стирає `sdkconfig`; у git кладеться `sdkconfig.defaults`. | `nosignal-11-idf` | 1 рядків |
| T-12-009: **`loop` — звичайна задача FreeRTOS.** Вона має свій | `nosignal-12-arduino` | 1 рядків |
| T-12-033: Arduino core версії 3.x — велике оновлення: він | `nosignal-12-arduino` | 1 рядків |
| T-12-048: **Arduino як компонент ESP-IDF.** Найцікавіший варіант: проєкт будується | `nosignal-12-arduino` | 1 рядків |
| T-12-049: Тоді доступні `setup`/`loop` і бібліотеки Arduino — і | `nosignal-12-arduino` | 1 рядків |
| T-12-061: `delay` тут не блокує систему, а `loop` — | `nosignal-12-arduino` | 2 рядків |
| T-13-070: | Виріб, OTA, серійність, довгий супровід | ESP-IDF | `nosignal-13-pio` | 1 рядків |
| T-14-053: Треба писати код · MicroPython → так, Python | `nosignal-14-shvydki-shlyakhy` | 1 рядків |
| T-19-007: `otadata` · Тип → data | `nosignal-19-ota` | 1 рядків |
| T-19-009: `ota_0` · Тип → app | `nosignal-19-ota` | 1 рядків |
| T-19-011: `ota_1` · Тип → app | `nosignal-19-ota` | 1 рядків |
| T-19-013: Пристрій виконується зі слоту `ota_0`. | `nosignal-19-ota` | 1 рядків |
| T-19-014: Приходить оновлення — воно записується в `ota_1`, при | `nosignal-19-ota` | 1 рядків |
| T-19-016: Наступне оновлення піде у слот `ota_0`. | `nosignal-19-ota` | 1 рядків |
| T-19-059: Компонент сам знаходить неактивний слот, пише в нього | `nosignal-19-ota` | 1 рядків |
| T-41-007: Проєкт на SPP, що переїжджає на S3, доведеться | `nosignal-41-ble` | 1 рядків |
| T-41-011: Де є · BLE → уся лінійка, крім | `nosignal-41-ble` | 7 рядків |
| T-41-015: Швидкість · BLE → десятки кбіт/с | `nosignal-41-ble` | 1 рядків |
| T-41-019: Спарювання · BLE → не обов'язкове | `nosignal-41-ble` | 1 рядків |
| T-41-038: Тоді пристрій самоописовий — будь-який універсальний BLE-застосунок покаже | `nosignal-41-ble` | 1 рядків |
| T-41-040: В ESP-IDF два стеки BLE, і вибір між | `nosignal-41-ble` | 1 рядків |
| T-41-041: **Bluedroid** — повний стек, підтримує і Classic, і | `nosignal-41-ble` | 1 рядків |
| T-41-043: **NimBLE** — тільки BLE, компактніший, займає в рази | `nosignal-41-ble` | 1 рядків |
| T-41-049: **Wi-Fi і Bluetooth одночасно** працюють, але ділять одне | `nosignal-41-ble` | 1 рядків |
| T-41-054: BLE спроєктований для батарейок, і його головний параметр | `nosignal-41-ble` | 1 рядків |
| T-41-078: Для BLE-проєкту брати NimBLE: різниця в пам'яті вирішальна | `nosignal-41-ble` | 1 рядків |
| T-42-001: ESP-NOW — власний протокол Espressif для прямого обміну | `nosignal-42-espnow` | 1 рядків |
| T-42-006: ESP-NOW не робить нічого з цього. | `nosignal-42-espnow` | 1 рядків |
| T-42-015: Кожен пристрій має унікальну MAC від заводу (розділ | `nosignal-42-espnow` | 1 рядків |
| T-42-027: Обробник прийому виконується в контексті **задачі** Wi-Fi, а | `nosignal-42-espnow` | 1 рядків |
| T-42-045: ESP-NOW підтримує шифрування з ключами PMK і LMK. | `nosignal-42-espnow` | 1 рядків |
| T-42-048: Без шифрування ESP-NOW — це відкритий радіоефір. | `nosignal-42-espnow` | 1 рядків |
| T-42-060: Усі вузли на фіксованому каналі, Wi-Fi не використовується. | `nosignal-42-espnow` | 1 рядків |
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
| merge-bin вимагає --chip; без нього команда падає | `pass-09-komandy` | 7 рядків |
| idf.py merge-bin бере адреси з конфігурації проєкту | `pass-09-komandy` | 6 рядків |
| Стиснення при передачі ввімкнене за замовчуванням | `pass-09-komandy` | 10 рядків |
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
| Таблиця симптомів веде в тематично правильні розділи | `pass-14-marshruty` | 2 рядків |
| Політика підтримки ESP-IDF — 30 місяців, без окремого LTS | `pass-15-versiyi` | 7 рядків |
| BME280 — адреси, ідентифікатор чипа, регістр | `pass-18-schemy` | 4 рядків |
| DS18B20 повертає −127 при відсутності зв'язку | `pass-18-schemy` | 1 рядків |
| Таблиця розділів — 0xC00 і 95 записів; 0x7000 належить бутлоадерові | `pass-24-zsuvy-i-matrycya` | 18 рядків |
| JTAG-піни classic — усі чотири з таблиці IOMUX | `pass-24-zsuvy-i-matrycya` | 9 рядків |
| Матриця GPIO і SPI — 40 проти 80 МГц, і коли різниці немає | `pass-24-zsuvy-i-matrycya` | 11 рядків |
| MSPI на S3 — GPIO26–32 під флеш, GPIO33–37 під восьмилінійний режим | `pass-25-psram` | 14 рядків |
| PSRAM вимкнена типово, а винесення в неї — навпаки, ввімкнене | `pass-25-psram` | 23 рядків |
| Octal PSRAM треба зазначити — типово стоїть Quad | `pass-25-psram` | 7 рядків |
| Внутрішнє підтягування strapping — 45 кОм, кнопці треба 10 кОм | `pass-26-strapping` | 5 рядків |
| GPIO12 має внутрішнє підтягування вниз — безпечний за замовчуванням | `pass-26-strapping` | 5 рядків |
| idf.py monitor — вихід Ctrl+], скидання через Ctrl+T | `pass-28-komandy-suciljno` | 12 рядків |
| espefuse палить в один бік; остання перепона — слово BURN | `pass-28-komandy-suciljno` | 12 рядків |
| Таблиці адрес прошивки — три рядки на три сімейства | `pass-31-adresy-i-api` | 9 рядків |
| esp_timer — мікросекундна роздільність, обробники в одній задачі | `pass-31-adresy-i-api` | 7 рядків |
| JTAG на classic — чотири піни, два з них strapping | `pass-32-pul-shmatky-1-3` | 13 рядків |
| USB-JTAG і вбудований відлагоджувач — піни по сімействах | `pass-32-pul-shmatky-1-3` | 3 рядків |
| LISTEN_ONLY і NO_ACK — режими TWAI дослівно | `pass-32-pul-shmatky-1-3` | 7 рядків |
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
| Драйвер I²C називає причину в консолі, а не мовчить | `pass-38-pul-shmatky-9-11` | 7 рядків |
| ESP_DRAM_LOGx — єдиний виняток із заборони логувати в ISR | `pass-38-pul-shmatky-9-11` | 5 рядків |
| На RISC-V рядка Backtrace немає — його будує монітор | `pass-38-pul-shmatky-9-11` | 12 рядків |
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
| T-04-061: **MCPWM** [[classic]] [[S3]] зроблений спеціально для силової електроніки: | `queue-a-04-peryferiya` | 1 рядків |
| T-11-042: **Версія ESP-IDF фіксується на початку проєкту й записується.** | `queue-a-11-idf` | 1 рядків |
| T-11-023: Ця команда додає інструменти в `PATH` і ставить | `queue-a-11-idf` | 3 рядків |
| T-16-056: Якщо є лише `factory` — беруть його. | `queue-a-16-boot` | 1 рядків |
| T-17-061: Аргументи йдуть парами: адреса, файл. | `queue-a-17-esptool` | 1 рядків |
| T-17-063: `-z` вмикає стиснення при передачі. | `queue-a-17-esptool` | 1 рядків |
| T-18-074: Швидкість при заповненні · SPIFFS → різко падає | `queue-a-18-rozdily-fleshu` | 1 рядків |
| T-19-023: Схема з двох слотів без `factory` — робоча | `queue-a-19-ota` | 1 рядків |
| T-19-013: Пристрій виконується зі слоту `ota_0`. | `queue-a-19-ota` | 1 рядків |
| T-19-014: Приходить оновлення — воно записується в `ota_1`, при | `queue-a-19-ota` | 1 рядків |
| T-25-051: Один тег на файл або на логічний модуль; | `queue-a-25-log` | 1 рядків |
| T-H-017: **`github.com/espressif/esp-idf`** — сам фреймворк. | `queue-a-h-dzherela` | 1 рядків |
| T-04-061: **MCPWM** [[classic]] [[S3]] зроблений спеціально для силової електроніки: | `sweep-04-peryferiya` | 1 рядків |
| T-05-089: У цифровій схемі це локальний запас енергії на | `sweep-05-elektronika` | 1 рядків |
| T-05-017: Світлодіод не можна вмикати без резистора: він не | `sweep-05-elektronika` | 1 рядків |
| T-05-064: **Pull-up** — резистор від піна до 3.3 В. | `sweep-05-elektronika` | 1 рядків |
| T-05-066: **Pull-down** — резистор до землі, дзеркально. | `sweep-05-elektronika` | 1 рядків |
| T-05-067: Хороша новина: у ESP32 підтягувальні резистори **вбудовані** і | `sweep-05-elektronika` | 1 рядків |
| T-05-074: Це не налаштовується — апаратної схеми немає. | `sweep-05-elektronika` | 1 рядків |
| T-05-077: Звичайний вихід активно тримає лінію в обох станах. | `sweep-05-elektronika` | 1 рядків |
| T-05-079: **Open-drain** уміє лише притискати лінію до землі, а | `sweep-05-elektronika` | 1 рядків |
| T-07-055: **Практичне правило:** strapping-піни можна використовувати, але як **виходи**, | `sweep-07-gpio` | 1 рядків |
| T-07-005: При скиданні ROM-бутлоадер має вирішити, звідки завантажуватися. | `sweep-07-gpio` | 1 рядків |
| T-07-006: Джерелом рішення служать кілька звичайних GPIO, стан яких | `sweep-07-gpio` | 1 рядків |
| T-07-065: Спроба їх використати підвішує чип або псує вміст | `sweep-07-gpio` | 1 рядків |
| T-07-067: Ніколи, за жодних умов, у жодному проєкті. | `sweep-07-gpio` | 1 рядків |
| T-07-069: Різниця між шісткою й цією парою — у | `sweep-07-gpio` | 1 рядків |
| T-07-072: Практично це означає, що правило «шість пінів» безпечне | `sweep-07-gpio` | 1 рядків |
| T-07-083: Друге важливіше, бо менш очевидне. | `sweep-07-gpio` | 1 рядків |
| T-07-085: Виглядає як несправний пін або несправна кнопка. | `sweep-07-gpio` | 1 рядків |
| T-07-086: Налаштуванням у коді це не змінюється: апаратної схеми | `sweep-07-gpio` | 1 рядків |
| T-07-093: Людина шукає помилку в коді вимірювання, а справа | `sweep-07-gpio` | 1 рядків |
| T-07-107: Використати їх під щось інше можна, але тоді | `sweep-07-gpio` | 1 рядків |
| T-07-108: Правило: чіпати UART0 тільки тоді, коли пінів справді | `sweep-07-gpio` | 1 рядків |
| T-07-136: Strapping-піни краще використовувати як виходи й лишати вільними | `sweep-07-gpio` | 1 рядків |
| T-07-045: | | Головний пін | Другий пін для | `sweep-07-gpio` | 1 рядків |
| T-07-053: На classic і S3 такої комбінації немає — | `sweep-07-gpio` | 1 рядків |
| T-07-064: Вони **виведені на гребінку** більшості плат, підписані як | `sweep-07-gpio` | 1 рядків |
| T-07-066: Правило категоричне: [[classic]] шість пінів 6–11 не існують. | `sweep-07-gpio` | 1 рядків |
| T-07-071: На голому `WROOM-32` вони вільні. | `sweep-07-gpio` | 1 рядків |
| T-07-078: [[S3]] Це найпоширеніша причина «купив S3 із 16 | `sweep-07-gpio` | 1 рядків |
| T-07-080: Перед проєктуванням плати на S3 варто точно знати, | `sweep-07-gpio` | 1 рядків |
| T-07-087: У пізніших сімействах (S3, C3) тільки-вхідних пінів немає | `sweep-07-gpio` | 1 рядків |
| T-07-101: Більше ніде в лінійці DAC немає (розділи 04 | `sweep-07-gpio` | 1 рядків |
| T-07-104: Для всіх трьох матриця GPIO не діє: це | `sweep-07-gpio` | 1 рядків |
| T-07-121: **Чип із більшою кількістю пінів** — S3 має | `sweep-07-gpio` | 1 рядків |
| T-08-004: Це те, що ставлять на власну плату у | `sweep-08-platy` | 1 рядків |
| T-08-024: **Міст USB-UART.** Створює порт у системі. | `sweep-08-platy` | 1 рядків |
| T-09-007: Тому між ними ставлять **міст USB-UART**: окремий чип, | `sweep-09-pidklyuchennya` | 1 рядків |
| T-09-037: **Linux у більшості випадків не потребує нічого.** Драйвери | `sweep-09-pidklyuchennya` | 1 рядків |
| T-09-042: Мосту не потрібно взагалі: чип під'єднується до комп'ютера | `sweep-09-pidklyuchennya` | 1 рядків |
| T-09-045: **Драйвер не потрібен.** Пристрій відповідає стандарту USB CDC, | `sweep-09-pidklyuchennya` | 1 рядків |
| T-09-070: У деяких дистрибутивах група називається `uucp` замість `dialout` | `sweep-09-pidklyuchennya` | 1 рядків |
| T-09-069: Без цього нова група не застосується до поточної | `sweep-09-pidklyuchennya` | 1 рядків |
| T-09-077: Порт відкриває **лише один процес одночасно**. | `sweep-09-pidklyuchennya` | 1 рядків |
| T-09-087: Кабель, роз'єм або живлення плати. | `sweep-09-pidklyuchennya` | 3 рядків |
| T-09-010: Звідси випливає головне: **порт у системі створює міст, | `sweep-09-pidklyuchennya` | 1 рядків |
| T-11-042: **Версія ESP-IDF фіксується на початку проєкту й записується.** | `sweep-11-idf` | 1 рядків |
| T-11-023: Ця команда додає інструменти в `PATH` і ставить | `sweep-11-idf` | 3 рядків |
| T-12-005: насправді відбувається таке: ESP-IDF стартує звичайним чином, створює | `sweep-12-arduino` | 3 рядків |
| T-12-059: | Прототип уже є, треба довести до виробу | `sweep-12-arduino` | 1 рядків |
| T-12-064: Прототип на Arduino доводиться до виробу підключенням Arduino | `sweep-12-arduino` | 1 рядків |
| T-13-024: Запис `espressif32 @ 6.5.0` збереться — і дасть | `sweep-13-pio` | 1 рядків |
| T-13-025: `pioarduino` розповсюджується не через реєстр PlatformIO, а архівом | `sweep-13-pio` | 1 рядків |
| T-13-006: Форк називається **pioarduino** і супроводжується спільнотою. | `sweep-13-pio` | 1 рядків |
| T-13-014: **Версії фіксуються в проєкті.** Це головне. | `sweep-13-pio` | 4 рядків |
| T-13-020: Весь проєкт описується одним файлом: | `sweep-13-pio` | 4 рядків |
| T-13-002: Для ESP32 воно дає те, чого не дає | `sweep-13-pio` | 1 рядків |
| T-13-004: Підтримка ESP32 у PlatformIO забезпечується платформою `platform-espressif32`. | `sweep-13-pio` | 1 рядків |
| T-13-005: Офіційна платформа від PlatformIO **відстала** від Arduino core: | `sweep-13-pio` | 1 рядків |
| T-13-007: Він підтримує актуальні версії Arduino core і нові | `sweep-13-pio` | 1 рядків |
| T-13-015: `platformio.ini` лежить у git і повністю описує, чим | `sweep-13-pio` | 3 рядків |
| T-13-029: **`platform`.** Тут — джерело платформи, а не лише | `sweep-13-pio` | 1 рядків |
| T-13-032: Для `pioarduino` пінування — це заміна мітки `stable` | `sweep-13-pio` | 1 рядків |
| T-13-048: Для S3 це не косметика — офіційна платформа | `sweep-13-pio` | 1 рядків |
| T-14-005: Ви прошиваєте його один раз, далі працюєте з | `sweep-14-shvydki-shlyakhy` | 1 рядків |
| T-14-015: Частина периферії доступна частково. | `sweep-14-shvydki-shlyakhy` | 1 рядків |
| T-14-071: **Розвідка заліза** — MicroPython у консолі: чи відповідає | `sweep-14-shvydki-shlyakhy` | 3 рядків |
| T-16-056: Якщо є лише `factory` — беруть його. | `sweep-16-boot` | 1 рядків |
| T-17-051: Файл, менший за очікуваний, — це обірваний дамп, | `sweep-17-esptool` | 1 рядків |
| T-17-064: Воно **вже ввімкнене** за замовчуванням, тож у звичайній | `sweep-17-esptool` | 1 рядків |
| T-17-066: Користь від стиснення там подвійна: менше байтів пройшло | `sweep-17-esptool` | 1 рядків |
| T-17-071: Швидкість тут не той параметр, на якому варто | `sweep-17-esptool` | 1 рядків |
| T-17-074: Адреси залежать від сімейства чипа — таблиця в | `sweep-17-esptool` | 1 рядків |
| T-17-149: There was no response.`** | `sweep-17-esptool` | 1 рядків |
| T-18-038: У проєкті ESP-IDF розбивка задається текстовим файлом: | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-080: У складі ESP-IDF · SPIFFS → так | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-088: Після цього розділ у меню з'являється, а тип | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-103: **Взяти готову розбивку з більшим розділом застосунку** для | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-106: Якщо нова прошивка розрахована на іншу розбивку, вона | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-107: Практично це означає: **розбивку треба обирати з запасом | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-108: Змінити її потім можна лише з фізичним доступом | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-109: Другий наслідок того самого: якщо ви змінили розбивку, | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-003: Це та частина системи, яку більшість не чіпає | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-009: Типова розбивка для пристрою без OTA виглядає так: | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-010: | Назва | Тип | Підтип | Зсув | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-015: `phy_init` · Тип → data | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-016: `phy_init` · Підтип → phy | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-019: `factory` · Тип → app | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-020: `factory` · Підтип → factory | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-18-028: **`phy_init`** зберігає калібрувальні дані радіо. | `sweep-18-rozdily-fleshu` | 1 рядків |
| T-19-023: Схема з двох слотів без `factory` — робоча | `sweep-19-ota` | 1 рядків |
| T-19-013: Пристрій виконується зі слоту `ota_0`. | `sweep-19-ota` | 1 рядків |
| T-19-014: Приходить оновлення — воно записується в `ota_1`, при | `sweep-19-ota` | 1 рядків |
| T-22-057: Лог зберігається у файл, а не читається з | `sweep-22-zberezhennya-stanu` | 1 рядків |
| T-23-075: Ніякого струму, ніякого ризику. | `sweep-23-triazh` | 1 рядків |
| T-23-100: Напис на модулі звіряється з шапкою `esptool`. | `sweep-23-triazh` | 1 рядків |
| T-24-012: Таблиця відповідає на кілька питань одразу. | `sweep-24-chuzha-proshyvka` | 1 рядків |
| T-24-035: Витягти розділ (адреса і розмір — з таблиці | `sweep-24-chuzha-proshyvka` | 1 рядків |
| T-24-057: Цього достатньо, щоб написати власну прошивку, яка робить | `sweep-24-chuzha-proshyvka` | 1 рядків |
| T-24-068: Якщо ввімкнено — дамп зашифрований ключем, що не | `sweep-24-chuzha-proshyvka` | 1 рядків |
| T-24-015: **Чи є файлова система.** Розділ типу `spiffs`, `littlefs` | `sweep-24-chuzha-proshyvka` | 1 рядків |
| T-25-051: Один тег на файл або на логічний модуль; | `sweep-25-log` | 1 рядків |
| T-27-002: Відлагоджувач показує все: поточне значення будь-якої змінної, вміст | `sweep-27-jtag` | 1 рядків |
| T-27-044: Коли справді варте: складна помилка з пошкодженням пам'яті, | `sweep-27-jtag` | 1 рядків |
| T-27-020: Якщо в проєкті ці піни переналаштовані під щось | `sweep-27-jtag` | 1 рядків |
| T-30-073: Функція, яка може спрацювати в цей момент — | `sweep-30-struktura` | 1 рядків |
| T-30-023: Розмір стека задається при створенні задачі — числом, | `sweep-30-struktura` | 1 рядків |
| T-30-026: Переповнення стека на мікроконтролері не дає ні винятку, | `sweep-30-struktura` | 1 рядків |
| T-30-027: Задача просто пише за межі свого стека — | `sweep-30-struktura` | 1 рядків |
| T-30-030: Що з'їдає стек несподівано багато: | `sweep-30-struktura` | 1 рядків |
| T-30-076: IRAM небагато, і кожна така функція займає її | `sweep-30-struktura` | 1 рядків |
| T-30-085: **32-бітне читання й запис вирівняного слова атомарні** апаратно. | `sweep-30-struktura` | 1 рядків |
| T-30-087: Складніші структури — ні. | `sweep-30-struktura` | 1 рядків |
| T-30-004: `app_main` викликається як звичайна задача FreeRTOS. | `sweep-30-struktura` | 1 рядків |
| T-30-006: **`app_main` може завершитися.** І це нормально: система продовжує | `sweep-30-struktura` | 1 рядків |
| T-30-007: Задача `app_main` просто зникає, звільняючи свій стек. | `sweep-30-struktura` | 1 рядків |
| T-30-016: **Статична.** Глобальні змінні й `static`. | `sweep-30-struktura` | 1 рядків |
| T-30-021: **Купа.** `malloc` і `new`. | `sweep-30-struktura` | 1 рядків |
| T-30-032: **Великі буфери — не на стек.** `static` або | `sweep-30-struktura` | 1 рядків |
| T-30-041: Купа на ESP32 не однорідна (розділ 03), і | `sweep-30-struktura` | 1 рядків |
| T-30-047: **Не та область.** Буфер для DMA має бути | `sweep-30-struktura` | 1 рядків |
| T-30-067: Коли вільно 40 КБ, а найбільший блок — | `sweep-30-struktura` | 1 рядків |
| T-30-086: Тому проста передача одного значення (прапорець, ціле число) | `sweep-30-struktura` | 1 рядків |
| T-30-101: Результат `malloc` перевіряти завжди. | `sweep-30-struktura` | 1 рядків |
| T-30-102: `volatile` не робить операцію атомарною. | `sweep-30-struktura` | 1 рядків |
| T-31-020: Планувальник завжди виконує **найпріоритетнішу готову** задачу. | `sweep-31-freertos` | 1 рядків |
| T-31-002: Це не бібліотека, яку треба підключати, — це | `sweep-31-freertos` | 1 рядків |
| T-31-027: Це не помилка планувальника, а його правило. | `sweep-31-freertos` | 1 рядків |
| T-31-029: Високий пріоритет означає «швидко відреагувати й заснути», а | `sweep-31-freertos` | 1 рядків |
| T-31-059: Зручно для «дочекатися, поки є і Wi-Fi, і | `sweep-31-freertos` | 1 рядків |
| T-31-031: Прив'язати задачу до ядра явно: | `sweep-31-freertos` | 1 рядків |
| T-31-034: Коли це має сенс: щось із жорсткими таймінгами | `sweep-31-freertos` | 1 рядків |
| T-31-035: Щось важке й тривале — теж на ядро | `sweep-31-freertos` | 1 рядків |
| T-31-036: Двоядерність робить помилки синхронізації **реальними, а не теоретичними**. | `sweep-31-freertos` | 1 рядків |
| T-31-055: **Двійковий семафор** — сигнал «сталося». | `sweep-31-freertos` | 1 рядків |
| T-31-057: **Лічильний семафор** — облік обмеженого ресурсу. | `sweep-31-freertos` | 1 рядків |
| T-31-058: **Група подій** — набір прапорців, на комбінацію яких | `sweep-31-freertos` | 1 рядків |
| T-31-063: **ISR має бути коротким.** Прочитати, покласти в чергу, | `sweep-31-freertos` | 1 рядків |
| T-31-070: Це інструмент для відлагодження, а не для роботи. | `sweep-31-freertos` | 1 рядків |
| T-31-071: Але коли ISR поводиться незрозуміло, а покласти в | `sweep-31-freertos` | 1 рядків |
| T-31-079: Механічний контакт при натисканні дає десятки перемикань за | `sweep-31-freertos` | 1 рядків |
| T-31-085: Усі програмні таймери виконуються в **одній** службовій задачі. | `sweep-31-freertos` | 1 рядків |
| T-31-090: **Спільна змінна без захисту.** На двох ядрах ламається | `sweep-31-freertos` | 1 рядків |
| T-31-095: Високий пріоритет означає «швидко відреагувати й заснути». | `sweep-31-freertos` | 1 рядків |
| T-31-098: Ніякого логування й пам'яті. | `sweep-31-freertos` | 1 рядків |
| T-31-006: ESP_LOGI(TAG, "температура %.1f", t); | `sweep-31-freertos` | 1 рядків |
| T-33-012: `1ULL` обов'язково: на пінах вище 31 звичайний `1` | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-023: gpio_isr_handler_add(GPIO_NUM_5, isr, (void *)GPIO_NUM_5); | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-029: Для більшості періодичних задач цього досить: | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-034: Це основний спосіб міряти час: переповнення не станеться | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-049: Яскравість світлодіода **не лінійна** щодо коефіцієнта заповнення. | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-051: Плавне згасання, зроблене лінійно, виглядає як різкий стрибок | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-058: Спільна земля обов'язкова (розділ 48). | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-060: - **мертвий час** між верхнім і нижнім плечем | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-075: Це правильний спосіб читати ІЧ-пульти й датчики з | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-077: Енкодер, витратомір, лічильник обертів — усе це не | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-079: PCNT уміє й апаратний фільтр коротких сплесків — | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-091: Пам'ятайте: вхід не толерантний до перевищення — понад | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-103: Найдешевше і найдієвіше. 2. | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-113: Піни **різні** за сімействами: | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-124: Яскравість світлодіода нелінійна щодо коефіцієнта заповнення. | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-127: PCNT рахує імпульси без переривань і має апаратний | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-059: [[classic]] [[S3]] MCPWM зроблений для силової електроніки й | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-062: RMT задумувався для інфрачервоних пультів, а виявився універсальним | `sweep-33-peryferiya-kod` | 1 рядків |
| T-33-074: RMT уміє й приймати — вимірювати тривалість вхідних | `sweep-33-peryferiya-kod` | 1 рядків |
| T-34-044: На коротких лініях працює і без них; на | `sweep-34-uart` | 1 рядків |
| T-34-045: Багато модулів мають термінатор на платі, іноді припаяний | `sweep-34-uart` | 1 рядків |
| T-34-048: Якщо обмін не йде — поміняти місцями. | `sweep-34-uart` | 1 рядків |
| T-34-049: Це безпечно і розв'язує половину випадків. | `sweep-34-uart` | 1 рядків |
| T-34-001: UART — найстаріший і найнадійніший спосіб з'єднати два | `sweep-34-uart` | 1 рядків |
| T-34-002: Два дроти, жодного протоколу поверх, працює завжди. | `sweep-34-uart` | 1 рядків |
| T-34-004: [[classic]] ESP32 classic має три контролери UART, S3 | `sweep-34-uart` | 1 рядків |
| T-34-020: **Розмір буфера драйвера має значення.** Дані приходять, поки | `sweep-34-uart` | 1 рядків |
| T-34-030: Звичайний UART працює на десятки сантиметрів. | `sweep-34-uart` | 1 рядків |
| T-34-041: Перемкнути напрямок відразу після нього означає обрізати власну | `sweep-34-uart` | 1 рядків |
| T-34-055: ESP-IDF має штатний компонент `esp-modbus` для обох ролей: | `sweep-34-uart` | 1 рядків |
| T-34-070: Буфер драйвера робити з запасом: переповнення губить дані | `sweep-34-uart` | 1 рядків |
| T-34-036: Напрямком керує окремий пін `DE`/`RE`: | `sweep-34-uart` | 1 рядків |
| T-35-038: Це замінює логічний аналізатор для питання «чи є | `sweep-35-i2c` | 1 рядків |
| T-35-029: Реальна межа задається **ємністю шини**: що довші проводи | `sweep-35-i2c` | 1 рядків |
| T-35-035: Сканер перебирає всі адреси й друкує ті, що | `sweep-35-i2c` | 1 рядків |
| T-35-067: Вбудоване підтягування — не заміна, а рятувальний круг. | `sweep-35-i2c` | 1 рядків |
| T-35-069: Ведучий мусить це витримати. | `sweep-35-i2c` | 1 рядків |
| T-35-071: Повільний ведений (наприклад, датчик, що довго міряє) може | `sweep-35-i2c` | 1 рядків |
| T-35-078: Ведучий, що опитує швидше, ніж ваш обробник готує | `sweep-35-i2c` | 1 рядків |
| T-35-085: **Скоротити проводи**, знизити швидкість до 100 кГц. 6. | `sweep-35-i2c` | 1 рядків |
| T-35-090: Один комплект резисторів на шину; кілька модулів зі | `sweep-35-i2c` | 1 рядків |
| T-35-007: Дві лінії: `SDA` (дані) і `SCL` (тактування). | `sweep-35-i2c` | 1 рядків |
| T-35-070: ESP32 це підтримує, але з обмеженим таймаутом. | `sweep-35-i2c` | 1 рядків |
| T-35-075: Усе вище — про ESP32 у ролі **ведучого**, | `sweep-35-i2c` | 1 рядків |
| T-35-079: Якщо роль веденого потрібна, а встигати не гарантовано | `sweep-35-i2c` | 1 рядків |
| T-35-087: **Аналізатор** — `ACK` чи `NACK` (розділ 28). | `sweep-35-i2c` | 1 рядків |
| T-39-035: Її ще немає: під'єднання займає від сотень мілісекунд | `sweep-39-wifi` | 1 рядків |
| T-39-037: Саме наявність IP, а не факт під'єднання, означає, | `sweep-39-wifi` | 1 рядків |
| T-39-018: **Канали 12 і 13** доступні не за всіх | `sweep-39-wifi` | 1 рядків |
| T-39-021: Роутер, переведений у режим «тільки WPA3», відрізає такі | `sweep-39-wifi` | 1 рядків |
| T-39-044: Пристрій гріється, з'їдає батарею і не робить нічого | `sweep-39-wifi` | 5 рядків |
| T-39-033: Робота йде **через події**: під'єднання асинхронне, і код | `sweep-39-wifi` | 1 рядків |
| T-39-047: ESP_LOGW(TAG, "зв'язок втрачено, спроба через %d мс", pauza); | `sweep-39-wifi` | 1 рядків |
| T-39-054: Правильно — зберігати в NVS (розділ 18), а | `sweep-39-wifi` | 1 рядків |
| T-39-064: ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary); | `sweep-39-wifi` | 1 рядків |
| T-39-087: **Modem sleep** — радіо вимикається між маячками, з'єднання | `sweep-39-wifi` | 1 рядків |
| T-39-088: Вмикається за замовчуванням і майже безкоштовне. | `sweep-39-wifi` | 1 рядків |
| T-39-001: Wi-Fi — головна причина, чому беруть ESP32 (розділ | `sweep-39-wifi` | 1 рядків |
| T-39-019: Якщо роутер працює на 13-му, ESP32 із неправильно | `sweep-39-wifi` | 2 рядків |
| T-39-066: | від −50 дБм | відмінно | | `sweep-39-wifi` | 1 рядків |
| T-39-091: **Не під'єднуватися взагалі.** Для датчика на батарейці ESP-NOW | `sweep-39-wifi` | 1 рядків |
| T-39-098: RSSI логувати завжди: на межі OTA не проходить, | `sweep-39-wifi` | 1 рядків |
| T-46-043: Це незручно і ламається при оновленні бібліотеки; варто | `sweep-46-dyspleyi` | 1 рядків |
| T-46-046: LVGL дає красиві інтерфейси і коштує ресурсів. | `sweep-46-dyspleyi` | 1 рядків |
| T-46-038: **U8g2** — монохромні дисплеї. | `sweep-46-dyspleyi` | 1 рядків |
| T-46-042: Особливість, що дивує: конфігурація (модель дисплея, піни) задається | `sweep-46-dyspleyi` | 1 рядків |
| T-46-055: **Кодування.** Рядки в коді — UTF-8; бібліотека має | `sweep-46-dyspleyi` | 1 рядків |
| T-46-068: Правильний спосіб читання — **PCNT** (розділ 33): апаратний | `sweep-46-dyspleyi` | 1 рядків |
| T-59-079: Різниця виникає лише тоді, коли в старшому байті | `sweep-59-proj-monitor` | 6 рядків |
| T-A-010: 1 · Обмеження → UART0 TX | `sweep-a-pinouty` | 1 рядків |
| T-A-011: 1 · Примітка → консоль | `sweep-a-pinouty` | 1 рядків |
| T-A-016: 3 · Обмеження → UART0 RX | `sweep-a-pinouty` | 1 рядків |
| T-A-017: 3 · Примітка → консоль | `sweep-a-pinouty` | 1 рядків |
| T-A-099: UART0 TX / RX · [[classic]] → 1 | `sweep-a-pinouty` | 2 рядків |
| T-A-009: 0 · Примітка → `BOOT`; низький = download | `sweep-a-pinouty` | 1 рядків |
| T-A-045: 25 · Обмеження → **DAC1** | `sweep-a-pinouty` | 1 рядків |
| T-A-046: 25 · ADC → ADC2_8 | `sweep-a-pinouty` | 1 рядків |
| T-A-047: 26 · Обмеження → **DAC2** | `sweep-a-pinouty` | 1 рядків |
| T-A-049: 27 · ADC → ADC2_7 | `sweep-a-pinouty` | 1 рядків |
| T-A-088: 5 · Обмеження → ADC2 | `sweep-a-pinouty` | 1 рядків |
| T-C-075: `-i` обов'язковий: без нього inline-кадри зникають. | `sweep-c-komandy` | 1 рядків |
| T-C-092: `/dev/ttyUSB*` — зовнішній міст. | `sweep-c-komandy` | 1 рядків |
| T-E-125: WS2812 / SK6812 · Як → **RMT**, не | `sweep-e-interfeysy` | 1 рядків |
| T-G-036: | стабілізатор | voltage regulator | | `sweep-g-glosariy` | 1 рядків |
| T-G-085: | відтворюване збирання | reproducible build | | `sweep-g-glosariy` | 1 рядків |
| T-G-054: | прошивка | firmware | | `sweep-g-glosariy` | 1 рядків |
| T-G-055: | образ | image, binary | | `sweep-g-glosariy` | 1 рядків |
| T-G-056: | збирання | build | | `sweep-g-glosariy` | 1 рядків |
| T-G-063: | семафор | semaphore | | `sweep-g-glosariy` | 1 рядків |
| T-G-064: | м'ютекс | mutex | | `sweep-g-glosariy` | 1 рядків |
| T-G-065: | група подій | event group | | `sweep-g-glosariy` | 1 рядків |
| T-G-066: | переривання | interrupt | | `sweep-g-glosariy` | 1 рядків |
| T-G-068: | критична секція | critical section | | `sweep-g-glosariy` | 1 рядків |
| T-G-074: | атомарна операція | atomic operation | | `sweep-g-glosariy` | 1 рядків |
| T-G-076: | взаємне блокування | deadlock | | `sweep-g-glosariy` | 1 рядків |
| T-G-077: | зворотний виклик | callback | | `sweep-g-glosariy` | 1 рядків |
| T-G-088: | точка доступу | access point | | `sweep-g-glosariy` | 1 рядків |
| T-G-089: | станція, клієнт | station | | `sweep-g-glosariy` | 1 рядків |
| T-G-090: | канал | channel | | `sweep-g-glosariy` | 1 рядків |
| T-G-091: | рівень сигналу | RSSI, signal strength | | `sweep-g-glosariy` | 1 рядків |
| T-G-094: | дальність | range | | `sweep-g-glosariy` | 1 рядків |
| T-G-095: | маячок | beacon | | `sweep-g-glosariy` | 1 рядків |
| T-G-098: | топік | topic | | `sweep-g-glosariy` | 1 рядків |
| T-G-099: | підписка | subscription | | `sweep-g-glosariy` | 1 рядків |
| T-G-100: | публікація | publish | | `sweep-g-glosariy` | 1 рядків |
| T-G-101: | сертифікат | certificate | | `sweep-g-glosariy` | 1 рядків |
| T-G-102: | центр сертифікації | certificate authority, CA | | `sweep-g-glosariy` | 1 рядків |
| T-G-103: | рукостискання | handshake | | `sweep-g-glosariy` | 1 рядків |
| T-G-104: | широкомовна розсилка | broadcast | | `sweep-g-glosariy` | 1 рядків |
| T-G-108: | напруга | voltage | | `sweep-g-glosariy` | 1 рядків |
| T-G-109: | струм | current | | `sweep-g-glosariy` | 1 рядків |
| T-G-111: | потужність | power | | `sweep-g-glosariy` | 1 рядків |
| T-G-116: | коефіцієнт заповнення | duty cycle | | `sweep-g-glosariy` | 1 рядків |
| T-G-117: | роздільність | resolution | | `sweep-g-glosariy` | 1 рядків |
| T-G-118: | точність | accuracy | | `sweep-g-glosariy` | 1 рядків |
| T-G-119: | калібрування | calibration | | `sweep-g-glosariy` | 1 рядків |
| T-G-120: | усереднення | averaging | | `sweep-g-glosariy` | 1 рядків |
| T-G-121: | шум | noise | | `sweep-g-glosariy` | 1 рядків |
| T-G-141: | IDF | IoT Development Framework | | `sweep-g-glosariy` | 1 рядків |
| T-G-142: | RTOS | Real-Time Operating System | | `sweep-g-glosariy` | 1 рядків |
| T-G-150: | UART | Universal Asynchronous Receiver/Transmitter | | `sweep-g-glosariy` | 1 рядків |
| T-G-163: | WDT | Watchdog Timer | | `sweep-g-glosariy` | 1 рядків |
| T-G-146: | OTA | Over-The-Air (оновлення) | | `sweep-g-glosariy` | 1 рядків |
| T-G-153: | I²S | Inter-IC Sound | | `sweep-g-glosariy` | 1 рядків |
| T-G-155: | JTAG | Joint Test Action Group (інтерфейс | `sweep-g-glosariy` | 1 рядків |
| T-G-162: | ULP | Ultra-Low-Power (співпроцесор) | | `sweep-g-glosariy` | 1 рядків |
| T-H-017: **`github.com/espressif/esp-idf`** — сам фреймворк. | `sweep-h-dzherela` | 1 рядків |
| T-K03-018: Windows: `Диспетчер пристроїв` → жовтий знак оклику означає | `sweep-k03-pidkl` | 1 рядків |
| T-K03-020: Порт `/dev/ttyUSB0` є, але програма пише «Permission denied» | `sweep-k03-pidkl` | 1 рядків |
| T-K03-027: Порт зайнятий іншою програмою: відкритий монітор, Arduino IDE, | `sweep-k03-pidkl` | 1 рядків |
| T-K07-002: Це звіт про те, де саме програма померла. | `sweep-k07-panika` | 1 рядків |
| T-K07-021: Backtrace — це ланцюжок адрес. | `sweep-k07-panika` | 1 рядків |
| T-K07-022: Сам по собі він нечитний; його треба перекласти | `sweep-k07-panika` | 1 рядків |
| T-K07-027: Інструмент **свій для кожної архітектури**: [[S3]] — `xtensa-esp32s3-elf-addr2line`, | `sweep-k07-panika` | 1 рядків |
| T-K07-035: Якщо причина паніки лишилася, це стає boot loop: | `sweep-k07-panika` | 1 рядків |
| T-K07-020: Найчастіше — результат `malloc`, який не перевірили. | `sweep-k07-panika` | 1 рядків |
| T-K07-024: Вручну, коли лог знято з чужого пристрою і | `sweep-k07-panika` | 1 рядків |
| T-K07-031: `.elf` того самого збирання, що й `.bin`, — | `sweep-k07-panika` | 1 рядків |
| T-K08-021: 6 · Що робити → перший дамп після | `sweep-k08-symptomy` | 1 рядків |
| T-K08-026: 8 · Найчастіша причина → немає підтягування або | `sweep-k08-symptomy` | 1 рядків |
| T-K08-008: 2 · Найчастіша причина → плата не в | `sweep-k08-symptomy` | 1 рядків |
| T-K08-011: 3 · Найчастіша причина → адреса бутлоадера не | `sweep-k08-symptomy` | 1 рядків |
| T-K08-019: 6 · Симптом → Boot loop | `sweep-k08-symptomy` | 1 рядків |
| T-K08-020: 6 · Найчастіша причина → паніка в застосунку | `sweep-k08-symptomy` | 1 рядків |
| T-K08-035: 11 · Найчастіша причина → вони зайняті флешем | `sweep-k08-symptomy` | 6 рядків |
| T-K09-004: | **6, 7, 8, 9, 10, 11** | | `sweep-k09-pinouty` | 6 рядків |
| T-K11-008: **Не вмикати Flash Encryption і Secure Boot «щоб | `sweep-k11-nikoly` | 1 рядків |
| T-Z-010: паспорт виробу — 224, 310–311, 313, 398 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-011: серво — 32, 54, 203–204, 207, 274–277, 369, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-012: серійна прошивка — 4, 143, 145, 398 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-013: таблиця розділів — 15, 18, 129, 133, 135, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-038: DMA — 50, 52, 55–56, 188, 220, 222, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-055: esp_deep_sleep_start — 68, 100, 338, 340, 344 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-056: ESP_ERR_INVALID_ARG — 207, 326 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-062: esp_err_t — 131, 136, 164, 197–198, 327, 329–331, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-108: FreeRTOS — 4–5, 40–41, 46, 94, 100, 103, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-109: GPIO12 — 14, 17, 28, 71–72, 74, 77, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-110: GPIO15 — 14, 17–18, 28, 71, 142, 173, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-111: GPIO17 — 67, 73–75, 206, 335 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-112: GPIO18 — 75, 172, 206, 335 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-113: GPIO2 — 13–14, 17, 28, 71–72, 142, 335–337, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-114: GPIO21 — 149, 310, 326, 335 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-115: GPIO22 — 149, 310, 326, 335 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-116: GPIO25 — 75, 206–207, 310, 349–350 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-117: GPIO26 — 74–75, 206–207, 349–350 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-118: GPIO3 — 14, 72, 75, 335, 337 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-119: GPIO32 — 53, 74–75, 182, 389 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-120: GPIO34 — 53, 62, 74, 77, 182, 335, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-121: GPIO4 — 9, 17, 149, 310, 335, 349, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-123: GPIO6 — 21, 27, 53, 73, 76, 154, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-124: GPIO8 — 13–14, 24, 72–73, 118, 205, 326, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-125: GPIO9 — 13–14, 17, 24, 72–73, 82, 118, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-128: gpio_isr_handler — 50, 189 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-143: i2c_new_master_bus — 215, 326, 332 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-149: MALLOC_CAP_DMA — 188, 220, 222, 281, 368 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-151: MALLOC_CAP_SPIRAM — 153, 188–189 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-154: merge-bin — 15, 25–26, 35, 125–126, 128, 137, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-024: bootloader — 5, 15, 18, 26, 98, 117–120, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-044: ESP-NOW — 69, 231, 233, 236, 240, 246–249, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-046: ESP32-C3-MINI-1 — 7, 79, 152, 401 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-047: ESP32-CAM — 14, 80, 82, 279–281 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-048: ESP32-S2 — 45–46, 118, 242 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-049: ESP32-S3 — 7, 23, 39, 44, 118, 127, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-051: ESP32-WROOM-32 — 7, 39, 79, 123, 152, 401 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-052: ESP32-WROOM-32D — 79, 152 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-053: ESP32-WROVER — 7, 79, 152 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-054: ESP8266 — 7, 18, 21, 80, 123, 152, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-144: I²S — 40, 53–56, 280–281, 388, 399 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-153: MCP23017 — 57, 76, 365, 386 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-156: Modbus — 156, 209, 211, 356, 358, 360 | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-173: SR04 — 27, 34, 61, 258, 262, 264, | `sweep-z-pokazhchyk` | 1 рядків |
| T-Z-194: WS2812 — 54–55, 200, 204, 207, 388 | `sweep-z-pokazhchyk` | 1 рядків |
| T-18-024: **Застосунок починається з `0x10000`** — це не випадкове | `verdict-18-rozdily-fleshu` | 1 рядків |
| T-35-028: Стандартні швидкості — 100 кГц і 400 кГц. | `verdict-35-i2c` | 1 рядків |
| T-36-062: Проміжного стану немає, і «майже рідний» набір пінів | `verdict-36-spi` | 1 рядків |
| T-C-013: esptool --port PORT read-flash 0x8000 0x1000 pt.bin # | `verdict-c-komandy` | 1 рядків |

## нема чого звіряти — 658

| Доказ | Файл | Деталі |
|---|---|---|
| Робочий діапазон SF у LoRa — 7…12, а SF6 окремий режим | `m2-03-semtech-lora` | немає URL |
| Ширша смуга — швидше й менш далеко | `m2-03-semtech-lora` | немає URL |
| RFM69 не є LoRa-модулем | `m2-03-semtech-lora` | немає URL |
| SX1262 ефективніший за SX1276 — числа не отримано | `m2-03-semtech-lora` | немає придатних уривків |
| DS18B20 — діапазон, роздільність і час перетворення | `m2-04-ds18b20` | немає URL |
| Унікальний 64-бітний код і кількість пристроїв на лінії | `m2-04-ds18b20` | немає URL |
| Підтягування 4.7 кОм на лінії 1-Wire | `m2-04-ds18b20` | немає URL |
| Чому 4.7 кОм годиться на 100 кГц і не годиться на 400 кГц | `m2-05-i2c-pullups` | немає URL |
| Ємність шини I²C нормується, і саме вона обмежує довжину | `m2-05-i2c-pullups` | немає URL |
| Робоча напруга живлення — 3.0–3.6 В, типова 3.3 В | `m2-06-voltage-limits` | немає URL |
| Джерело мусить давати щонайменше 0.5 А за datasheet | `m2-06-voltage-limits` | немає URL |
| CP2102 — Silicon Labs, драйвер cp210x у ядрі Linux | `m2-07-bridges-usb-uart` | немає URL |
| CH340 і CH341 — WCH, драйвер ch341 у ядрі Linux | `m2-07-bridges-usb-uart` | немає URL |
| FT232RL — FTDI, драйвер ftdi_sio у ядрі Linux | `m2-07-bridges-usb-uart` | немає URL |
| CH9102 у ядрі є, але через cdc_acm, а не ch341 | `m2-07-bridges-usb-uart` | немає URL |
| PCF8574 — вісім ліній, розширювач по I²C | `m2-08-displays-expanders` | немає URL |
| MCP23017 — шістнадцять ліній | `m2-08-displays-expanders` | немає URL |
| ILI9341 — 240×320, інтерфейс SPI | `m2-08-displays-expanders` | немає URL |
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
| TP4056 — заряджання фіксоване на 4.2 В | `m2-11-battery` | немає URL |
| TP4056 — струм заряджання задає резистор, 1.2 кОм дає 1 А | `m2-11-battery` | немає URL |
| TP4056 продається із захистом DW01 — два транзистори в типовій схемі | `m2-11-battery` | немає URL |
| TP4056 — паралельне навантаження заважає визначенню кінця заряду | `m2-11-battery` | немає URL |
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
| Ємність ходових елементів 18650 — від 2500 до 3500 мА·год | `m2-15-cell-18650` | немає URL |
| Номінальна напруга 18650 — 3.6 В, а не 3.7 | `m2-15-cell-18650` | немає URL |
| Паспортна межа розряду 18650 — 2.5 В, а не 3.0 | `m2-15-cell-18650` | немає URL |
| Заряджання 18650 нижче 0 °C — Panasonic NCR18650B і LG MJ1 | `m2-15-cell-18650` | немає URL |
| SHT3x / SHT4x — точна вологість, ±1–1.5 %RH | `m2-16-sensors-appendix-e` | немає URL |
| MPU6050 — акселерометр і гіроскоп на одному кристалі | `m2-16-sensors-appendix-e` | немає URL |
| SHT3x / SHT4x — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-16-sensors-appendix-e` | немає придатних уривків |
| MPU6050 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-16-sensors-appendix-e` | немає придатних уривків |
| Безсвинцевий потребує на 30-40 °C більше | `m2-17-solder-and-ip` | немає URL |
| DS3231 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-appendix-e-rest` | немає придатних уривків |
| INA219 / INA226 — обидва повідомляють струм і напругу | `m2-18-appendix-e-rest` | немає URL |
| INA219 / INA226 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-appendix-e-rest` | немає придатних уривків |
| PCF8574 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-appendix-e-rest` | немає придатних уривків |
| MCP23017 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-appendix-e-rest` | немає придатних уривків |
| ST7789 — однокристальний драйвер TFT | `m2-18-appendix-e-rest` | немає URL |
| ILI9341 — однокристальний драйвер TFT | `m2-18-appendix-e-rest` | немає URL |
| ILI9341 — SPI Mode 0 (CPHA=0, зразок на першому фронті) | `m2-18-appendix-e-rest` | немає URL |
| ILI9341 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-appendix-e-rest` | немає придатних уривків |
| ST7789 — колонка «Бібліотека» це стан репозиторію, не факт про мікросхему | `m2-18-appendix-e-rest` | немає придатних уривків |
| MCP2515 — окремий CAN-контролер по SPI, Mode 0 підтримується | `m2-18-appendix-e-rest` | немає URL |
| MCP2515 — стендалон CAN-контролер із SPI | `m2-18-appendix-e-rest` | немає URL |
| MCP2515 — «Бібліотека → —» це посилання на вбудований контролер ESP32, не факт про MCP2515 | `m2-18-appendix-e-rest` | немає придатних уривків |
| MAX31855 / MAX6675 — обидва термопарні перетворювачі | `m2-18-appendix-e-rest` | немає URL |
| MAX31855 / MAX6675 — SPI Mode 0 в обох референсних бібліотеках | `m2-18-appendix-e-rest` | немає URL |
| MAX31855 / MAX6675 — «Бібліотека → Adafruit MAX31855» не працює з MAX6675 | `m2-18-appendix-e-rest` | немає придатних уривків |
| HC-SR04 — тригер і ECHO, 5 В TTL | `m2-18-appendix-e-rest` | немає URL |
| HC-SR04 — «Розділ → 45» це внутрішнє посилання книги, не факт про модуль | `m2-18-appendix-e-rest` | немає придатних уривків |
| Червоний LED — падіння близько 2 В | `m2-19-electronics-05` | немає URL |
| Резистор 220–330 Ом для червоного LED — арифметика закону Ома | `m2-19-electronics-05` | немає придатних уривків |
| Синій/білий LED — падіння близько 3 В | `m2-19-electronics-05` | немає URL |
| Логічні рівні ESP32 — близько 0 В / близько 3.3 В | `m2-19-electronics-05` | немає URL |
| Знижувати 5 В обов'язково — абсолютний максимум входу 3.6 В | `m2-19-electronics-05` | немає URL |
| 3.3 В — практична межа GPIO, консервативніша за паспортну 3.6 В | `m2-19-electronics-05` | немає URL |
| I²C — внутрішнє підтягування ESP32 (45 кОм) заслабке, потрібні зовнішні резистори | `m2-19-electronics-05` | немає URL |
| WROOM-32E — 100 нФ близько до виводів живлення в референсній схемі | `m2-19-electronics-05` | немає URL |
| MOSFET логічного рівня — офіційний термін і поріг відкривання | `m2-19-electronics-05` | немає URL |
| Звичайний MOSFET при 3.3 В — поріг близько, відкривається частково | `m2-19-electronics-05` | немає URL |
| Величезна кількість модулів «для Arduino» на 5 В — ринкове спостереження, не з документа | `m2-19-electronics-05` | немає придатних уривків |
| Конденсатор 470 мкФ — «найдешевше рішення найчастішої проблеми» — авторська оцінка | `m2-19-electronics-05` | немає придатних уривків |
| «5 В на GPIO. Абсолютний лідер.» — рейтинг причин спалених плат, авторська оцінка | `m2-19-electronics-05` | немає придатних уривків |
| «100 нФ і 470 мкФ знімають більшість збоїв» — авторський підсумок, не вимірювана частка | `m2-19-electronics-05` | немає придатних уривків |
| Половина модулів «для Arduino» — спостереження за ринком, не специфікація | `m2-20-levels-and-switches` | немає придатних уривків |
| 5 В на GPIO — понад абсолютний максимум входу ESP32 | `m2-20-levels-and-switches` | немає URL |
| Таблиця рішень К14 — авторська схема категоризації модулів, не факт із джерела | `m2-20-levels-and-switches` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Немає стабілізатора · Сигнали» | `m2-20-levels-and-switches` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Є стабілізатор 5→3.3 · Живлення» | `m2-20-levels-and-switches` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Є стабілізатор і конвертер · Живлення» | `m2-20-levels-and-switches` | немає придатних уривків |
| Таблиця рішень К14 — рядок «Є стабілізатор і конвертер · Сигнали» | `m2-20-levels-and-switches` | немає придатних уривків |
| «Більшість 5-вольтових входів бере 3.3 В за одиницю» — узагальнення про чужі пристрої | `m2-20-levels-and-switches` | немає придатних уривків |
| 5 В на вхід ESP32 — зниження обов'язкове через абсолютний максимум | `m2-20-levels-and-switches` | немає URL |
| LV/HV-конвертер — маркування модуля, не характеристика транзистора | `m2-20-levels-and-switches` | немає придатних уривків |
| Заголовок таблиці «Часті винуватці 5 В» — назви колонок, не факт | `m2-20-levels-and-switches` | немає придатних уривків |
| 74HC на 5 В — вихід близький до напруги живлення, вище за абсолютний максимум ESP32 | `m2-20-levels-and-switches` | немає URL |
| LED до 10 мА через резистор — IOH ESP32 з великим запасом | `m2-20-levels-and-switches` | немає URL |
| LED до 10 мА — «вистачає піна», та сама причина | `m2-20-levels-and-switches` | немає URL |
| MOSFET логічного рівня IRLZ44N — характеризований і при 4–5 В, не лише 10 В | `m2-20-levels-and-switches` | немає URL |
| 10 В на затворі — контрольна точка, від якої відлічує сам IRLZ44N | `m2-20-levels-and-switches` | немає URL |
| Резистор 100–220 Ом — межа кидка струму в межах можливостей піна ESP32 | `m2-20-levels-and-switches` | немає придатних уривків |
| 10 кОм від затвора на землю — стандартна практика, не звірена окремим джерелом | `m2-20-levels-and-switches` | немає придатних уривків |
| Реле на 5 В — спостереження за ринком модулів | `m2-20-levels-and-switches` | немає придатних уривків |
| Нестабільна робота реле від 3.3 В — не звірено джерелами цього кроку | `m2-20-levels-and-switches` | немає придатних уривків |
| Мережеве живлення 230 В — редакційна межа теми, не факт | `m2-20-levels-and-switches` | немає придатних уривків |
| Найчастіша задача з'єднання ESP32 і 5-вольтового пристрою — емпіричне узагальнення | `m2-20-levels-and-switches` | немає придатних уривків |
| «Напрямок 3.3 → 5 В» — той самий випадок узагальнення про чужі пристрої | `m2-20-levels-and-switches` | немає придатних уривків |
| «Напрямок 5 → 3.3 В» — зниження обов'язкове через абсолютний максимум ESP32 | `m2-20-levels-and-switches` | немає URL |
| Схема LV/HV-конвертера в розділі 47 — та сама межа джерел, що й у К14 | `m2-20-levels-and-switches` | немає придатних уривків |
| Дешевизна й раптова потреба в конвертері рівнів — практична порада, не факт | `m2-20-levels-and-switches` | немає придатних уривків |
| 10 кОм від затвора на землю (підсумок) — той самий випадок, що й основний виклад | `m2-20-levels-and-switches` | немає придатних уривків |
| Релейні модулі — 5 В та інверсна логіка, спостереження за ринком | `m2-20-levels-and-switches` | немає придатних уривків |
| «Два джерела працюють одне проти одного» при одночасній подачі на 3V3 і зовнішньому вході — загальний електротехнічний принцип, не цитата з datasheet | `m2-21-power-06` | немає придатних уривків |
| Пін `3V3` модуля — це напряму `VDD33`, без проміжного стабілізатора на самому модулі | `m2-21-power-06` | немає URL |
| «Тобто блок на 500 мА формально відповідає вимозі — і все одно найпоширеніша помилка» — частка «найпоширеніша» це практика/спостереження, а не показник із datasheet | `m2-21-power-06` | немає придатних уривків |
| «Дешевий блок... просідає задовго до цього» — пояснення поведінки дешевих блоків живлення, практика без джерела | `m2-21-power-06` | немає придатних уривків |
| «Тому 1 А — це не суперечність datasheet, а запас на якість джерела» — авторський підсумок аргументації, спирається на практичне (E), а не лише документне твердження | `m2-21-power-06` | немає придатних уривків |
| Конденсатор 470 мкФ між 3V3 і GND — стандартна практика розв'язки живлення, номінал не з datasheet ESP32 | `m2-21-power-06` | немає придатних уривків |
| «Окреме джерело від 1 А» і «знизити пікове споживання» — поради з порядку дешевизни, практика | `m2-21-power-06` | немає придатних уривків |
| 0.086 + 0.02 ≈ 0.106 мА·год — арифметика бюджету енергії за прикладом книги | `m2-21-power-06` | немає придатних уривків |
| «Шунт і осцилограф. Єдиний спосіб побачити реальну картину...» — методика вимірювання, авторська оцінка «єдиний спосіб» | `m2-21-power-06` | немає придатних уривків |
| LDO — третина енергії йде в нагрів при вході 5 В, виході 3.3 В — арифметика ККД | `m2-21-power-06` | немає придатних уривків |
| «Лікується зовнішнім живленням 3.3 В на відповідний пін, минаючи бортовий стабілізатор» — та сама архітектура, що й пін 3V3 напряму на VDD33 | `m2-21-power-06` | немає URL |
| «Джерело має тягнути 1 А... платить воно за піки» — той самий висновок з IVDD і пікового струму передачі, що вже встановлено класом B | `m2-21-power-06` | немає URL |
| «Конденсатор 470 мкФ... найдешевше розв'язання найчастішої проблеми в книзі» — авторська оцінка, порівняльне судження | `m2-21-power-06` | немає придатних уривків |
| DHT11, DHT22 — власний протокол і паспортна точність | `m2-22-insert-components` | немає URL |
| HC-SR04 — 5 В на ECHO підтверджено, «м'які поверхні» — ні | `m2-22-insert-components` | немає URL |
| не L298N — застарів і втрачає ~2 В на собі | `m2-22-insert-components` | немає URL |
| Buck-boost проти LDO — використання ємності батареї | `m2-22-insert-components` | немає URL |
| ACS712 — «беріть INA219/INA226» — редакційна порада | `m2-22-insert-components` | немає придатних уривків |
| HC-SR04 — «беріть VL53L0X» — редакційна порада | `m2-22-insert-components` | немає придатних уривків |
| Фейковий CP2102/FT232 — ознака без паспортного числа | `m2-22-insert-components` | немає придатних уривків |
| 220–330 Ом резистора світлодіода — узгоджується з реальним VF | `m2-22-insert-components` | немає URL |
| 4.7 кОм — підтягування 1-Wire підтверджено, I²C — похідне | `m2-22-insert-components` | немає URL |
| 10 кОм — підтягування входів і затвор MOSFET на землю — практика без чипа | `m2-22-insert-components` | немає придатних уривків |
| 100–220 Ом послідовно з затвором — практика без чипа | `m2-22-insert-components` | немає придатних уривків |
| 120 Ом термінаторів RS-485/CAN — стандарт, недосяжний з мережі | `m2-22-insert-components` | немає придатних уривків |
| 100 нФ біля кожної мікросхеми — загальна практика, не паспорт | `m2-22-insert-components` | немає придатних уривків |
| 470 мкФ біля роз'єму живлення — загальна практика, не паспорт | `m2-22-insert-components` | немає придатних уривків |
| DS18B20 — ±0.5 °C на один датчик, звідси розбіжність до 1 °C у двох справних | `m2-22-insert-components` | немає URL |
| DS18B20 — ±2 °C поза −10…+85 °C, тому міряти в кімнатній воді | `m2-22-insert-components` | немає URL |
| Що тримати в запасі — редакційний список, не факт | `m2-22-insert-components` | немає придатних уривків |
| DS3231 має власну батарейку — джерело недосяжне з цієї мережі | `m2-23-projects-60-62` | немає придатних уривків |
| DS3231 — кількість модуля в BOM, не факт про мікросхему | `m2-23-projects-60-62` | немає придатних уривків |
| Резистори 4.7 кОм для I²C і 1-Wire — номінал, який справді рекомендують обидва джерела | `m2-23-projects-60-62` | немає URL |
| Звичайний LDO й buck-boost — межі роботи без конкретної мікросхеми | `m2-23-projects-60-62` | немає придатних уривків |
| Дільник напруги на 200 кОм — арифметика верна, але «на порядок» перебільшує | `m2-23-projects-60-62` | немає придатних уривків |
| Бюджет енергії логера — множення часу на струм | `m2-23-projects-60-62` | немає придатних уривків |
| Струм на фазах бюджету — оцінні величини системи, не паспортні числа однієї деталі | `m2-23-projects-60-62` | немає придатних уривків |
| Оптопара не гарантує сумісності з 3.3 В — падіння струму світлодіода | `m2-23-projects-60-62` | немає придатних уривків |
| Перевірка модуля до монтажу й запасний варіант — транзисторний ключ | `m2-23-projects-60-62` | немає придатних уривків |
| Резистор утримує керувальний GPIO при завантаженні — усі піни output-disabled під час reset | `m2-23-projects-60-62` | немає URL |
| GPIO34 — input-only, без внутрішнього підтягування; зовнішній резистор для поплавкового вимикача | `m2-23-projects-60-62` | немає URL |
| CP2102 · Windows — драйвер від SiLabs | `m2-25-wiring-09` | немає URL |
| CH340 · Windows — драйвер від WCH | `m2-25-wiring-09` | немає URL |
| CH9102 · Windows — окремий драйвер (не CH340) | `m2-25-wiring-09` | немає придатних уривків |
| FT232RL · Windows — драйвер FTDI | `m2-25-wiring-09` | немає придатних уривків |
| CH9102 — окрема пастка (схожий на CH340, але інший драйвер) | `m2-25-wiring-09` | немає придатних уривків |
| Драйвер CH340 на CH9102 — не працює | `m2-25-wiring-09` | немає придатних уривків |
| Різні плати — різні імена портів | `m2-25-wiring-09` | немає придатних уривків |
| S3 та C3 — USB-контролер на кристалі | `m2-25-wiring-09` | немає придатних уривків |
| CH9102 — окремий драйвер від CH340 (резюме) | `m2-25-wiring-09` | немає придатних уривків |
| K03 CH9102/CH9102F · Windows окремий драйвер | `m2-26-k03-and-boards` | немає придатних уривків |
| Стабілізатор (LDO) · 3.3 В із 5 В | `m2-26-k03-and-boards` | немає придатних уривків |
| USB-міст на платі · CP2102, CH340, CH9102 | `m2-26-k03-and-boards` | немає придатних уривків |
| ESP32-CAM · немає USB-роз'єму | `m2-26-k03-and-boards` | немає придатних уривків |
| Фейковий USB-міст · клони CP2102 і FT232 | `m2-26-k03-and-boards` | немає придатних уривків |
| Піни для прошивки на власній платі | `m2-26-k03-and-boards` | немає придатних уривків |
| ST7789 — 4-line SPI інтерфейс | `m2-27-displays-46` | немає URL |
| ST7789 — 65K кольорів у режимі RGB 5-6-5 | `m2-27-displays-46` | немає URL |
| ILI9341 — 4-line SPI інтерфейс | `m2-27-displays-46` | немає URL |
| ILI9341 — 65K кольорів у режимі RGB 5-6-5 | `m2-27-displays-46` | немає URL |
| ST7789 · Розмір → 1.3–2.4" | `m2-27-displays-46` | немає придатних уривків |
| ST7789 · Особливості → яскравий, швидкий | `m2-27-displays-46` | немає придатних уривків |
| ILI9341 · Розмір → 2.4–3.2" | `m2-27-displays-46` | немає придатних уривків |
| ILI9341 · Особливості → великий, класика | `m2-27-displays-46` | немає придатних уривків |
| Альтернативи до матричної клавіатури 4×4 | `m2-27-displays-46` | немає придатних уривків |
| DHT11 - дешевий датчик температури й вологості | `m2-28-sensors-45` | немає придатних уривків |
| DHT11 — роздільність вологості 1%RH | `m2-28-sensors-45` | немає URL |
| HC-SR04 — ультразвуковий далекомір, 2–400 см | `m2-28-sensors-45` | немає URL |
| HC-SR04 — 5 В на виводі ECHO | `m2-28-sensors-45` | немає URL |
| HC-SR04 — 5 В на ECHO обов'язковий дільник | `m2-28-sensors-45` | немає URL |
| INA219 — вимірювання струму й напруги по I²C | `m2-28-sensors-45` | немає URL |
| Калібрування датчиків за відомою точкою | `m2-28-sensors-45` | немає придатних уривків |
| GPS модулі NMEA — UART, текстові речення | `m2-28-sensors-45` | немає придатних уривків |
| Типовий номінал 4.7 кОм для підтягування I²C | `m2-29-i2c-35` | немає URL |
| Три модулі по 4.7 кОм дають близько 1.6 кОм паралельно | `m2-29-i2c-35` | немає URL |
| На метрові дистанції I²C не призначений; RS-485 або менші резистори | `m2-29-i2c-35` | немає URL |
| Зовнішні 4.7 кОм обов'язкові для сумарного навантаження | `m2-29-i2c-35` | немає придатних уривків |
| Без зовнішніх резисторів 4.7 кОм I²C взагалі не працює | `m2-29-i2c-35` | немає URL |
| Вхідна напруга на роз'ємі від USB — норма 5 В ±5 % | `m2-31-card-k13` | немає придатних уривків |
| 3.3 В на холостому ході — норма 3.2–3.4 В | `m2-31-card-k13` | немає URL |
| Окреме джерело від 1 А — не 500 мА, тому що платити треба за піки | `m2-31-card-k13` | немає URL |
| Джерело для ESP32 з Wi-Fi — щонайменше 1 А, навіть якщо середнє споживання сто міліампер | `m2-31-card-k13` | немає URL |
| `rst:0xf` — симптом просідання живлення | `m2-32-symptoms-b` | немає придатних уривків |
| Перезавантаження при Wi-Fi — джерело не тягне піків | `m2-32-symptoms-b` | немає URL |
| Стабілізатор гарячий — перевантаження або слабкий клон | `m2-32-symptoms-b` | немає придатних уривків |
| I²C не знаходить пристрій — немає підтягування | `m2-32-symptoms-b` | немає придатних уривків |
| RS-485: помилки на довгій лінії — потрібни термінатори | `m2-32-symptoms-b` | немає придатних уривків |
| Реле вмикається при старті — вхід ключа висить при завантаженні | `m2-32-symptoms-b` | немає придатних уривків |
| Реле не спрацьовує — модуль керування на 5 В | `m2-32-symptoms-b` | немає придатних уривків |
| Реле не спрацьовує — дія: живити модуль від 5 В | `m2-32-symptoms-b` | немає придатних уривків |
| 74HC595 — зсувний регістр, вихід | `m2-33-gpio-07` | немає URL |
| 74HC165 — зсувний регістр, вхід | `m2-33-gpio-07` | немає URL |
| CD4051 — аналоговий мультиплексор, восьми каналів | `m2-33-gpio-07` | немає URL |
| T-A-123: посилання на розділ 07 | `m2-33-gpio-07` | немає придатних уривків |
| T-F-006: інсталятор й перше збирання | `m2-34-appendices-rest` | немає придатних уривків |
| T-F-014: .elf файли й backtrace | `m2-34-appendices-rest` | немає придатних уривків |
| T-F-012: драйвери USB-UART (CP2102, CH340, CH9102) | `m2-34-appendices-rest` | немає URL |
| T-K10-039: інтерфейси /dev/ttyUSB* і /dev/ttyACM* | `m2-34-appendices-rest` | немає URL |
| manual/60-proj-loger.md: відсутні факти про мікросхеми | `m2-34-appendices-rest` | немає придатних уривків |
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
| Напруга відключення регулятора (перетворювача) близько 3.0 В | `m2-43-battery-53` | немає URL |
| Різниця між напругою регулятора (3.0 В) і захисту (2.5 В) | `m2-43-battery-53` | немає URL |
| Заряджання LG HG2 нижче −5 °C дозволено за паспортом | `m2-43-battery-53` | немає URL |
| LDO з малим падінням: 100–200 мВ | `m2-43-battery-53` | немає придатних уривків |
| Регулятор 4.2 В → 3.3 В: підходить при такому падінні | `m2-43-battery-53` | немає URL |
| Максимальний струм GPIO — 1200 мА сумарно | `m2-44-electronics-05` | немає URL |
| Один GPIO — шоста частина від 1200 мА | `m2-44-electronics-05` | немає придатних уривків |
| Спільна земля — сигнал це напруга відносно землі | `m2-44-electronics-05` | немає придатних уривків |
| Конденсатор живлення 100–470 мкФ біля роз'єма | `m2-44-electronics-05` | немає URL |
| L298N падіння напруги при 12 В — близько 2-3 В | `m2-45-motors-symptoms` | немає URL |
| L298N при 5 В живленні дає ~3 В на виход | `m2-45-motors-symptoms` | немає придатних уривків |
| Серво живиться від окремого джерела, земля спільна | `m2-45-motors-symptoms` | немає придатних уривків |
| Конденсатори 100 нФ на виводах двигуна для фільтрації шумів | `m2-45-motors-symptoms` | немає URL |
| Логічна помилка: 5 В на 3.3-вольтовий вхід пошкоджує чип | `m2-45-motors-symptoms` | немає URL |
| HC-SR04 живиться від 5 В | `m2-46-module-44` | немає URL |
| Живлення і логічні рівні — різні питання | `m2-46-module-44` | немає придатних уривків |
| Таблиця модулів: шість модулів дають 780 Ом паралельного опору | `m2-47-i2c-35` | немає придатних уривків |
| CH9102 потрібен не той самий драйвер, що CH340 | `m2-48-symptoms-29` | немає придатних уривків |
| rst:0xf brownout — зміряти напругу під навантаженням | `m2-48-symptoms-29` | немає придатних уривків |
| T-28-014: Напруга 3V3 під навантаженням повинна бути близько 3.3 В | `m2-49-analyzer-28` | немає URL |
| T-28-015: Просідання нижче 3.0 В причина незрозумілих глюків | `m2-49-analyzer-28` | немає URL |
| T-28-019: На лініях I²C у спокої має бути 3.3 В від pull-up резисторів | `m2-49-analyzer-28` | немає URL |
| T-28-024: Мультиметр показує середнє, швидкий сигнал виглядає як середина 0…3.3 В | `m2-49-analyzer-28` | немає придатних уривків |
| T-28-041: Лінії не піднімаються до 3.3 В — немає підтягування або завелике | `m2-49-analyzer-28` | немає URL |
| T-28-063: Практичний порядок пошуку — крок 3: чи піднято лінії до 3.3 В | `m2-49-analyzer-28` | немає придатних уривків |
| T-K03-011: CP2102 драйвер для Windows — з сайту SiLabs, Linux у ядрі | `m2-50-cards` | немає придатних уривків |
| T-K03-013: CH340 драйвер для Windows — з сайту WCH, Linux у ядрі | `m2-50-cards` | немає придатних уривків |
| T-K12-004: Мінімум комплекту — плата ESP32 DevKit 38 пінів з CP2102 або CH9102 | `m2-50-cards` | немає придатних уривків |
| T-K14-026: HC-SR04 — частий винуватець 5 В, вихід ECHO 5 В | `m2-50-cards` | немає придатних уривків |
| T-K11-017: Виняток із заборони 5 В — пін VIN або 5V (вхід стабілізатора) | `m2-50-cards` | немає придатних уривків |
| T-09-034: FT232RL масово підробляють, клони працюють, доки їх не розпізнає офіційний драйвер | `m2-51-bridges` | немає придатних уривків |
| T-09-036: Плата з FT232 раптом перестала визначатися після оновлення драйвера — можлива причина підробка | `m2-51-bridges` | немає придатних уривків |
| Слова «LoRa» в документації RFM69 немає жодного разу | `m2-52-lora-43` | немає URL |
| RFM69 — сусіднє сімейство для вузькосмугового FSK без дальності LoRa | `m2-52-lora-43` | немає URL |
| ILI9341 — RGB565 формат пікселя, не ціль контролера | `m2-53-parts-rest` | немає URL |
| T-D-151: A1 — вказівник стека | `m2-61-panic-b` | немає придатних уривків |
| T-D-177: Шукати memcpy, sprintf, цикл із <= замість < | `m2-61-panic-b` | немає придатних уривків |
| T-D-181: Порівняння з тим, що повернув malloc | `m2-61-panic-b` | немає придатних уривків |
| T-D-190: .elf разом з образом, розділ 21 | `m2-61-panic-b` | немає придатних уривків |
| T-D-193: Швидке відсікання — залити справний hello_world | `m2-61-panic-b` | немає придатних уривків |
| Матриця GPIO робить більшість пінів взаємозамінними, але не всі | `m2-63-gpio-07` | немає придатних уривків |
| Стан GPIO читається один раз при відпусканні скидання | `m2-63-gpio-07` | немає придатних уривків |
| Таблиця: пін, що задає режим, наслідок помилки | `m2-63-gpio-07` | немає придатних уривків |
| GPIO5 рідко впливає на проблеми поза SDIO режимом | `m2-63-gpio-07` | немає URL |
| На модулях з флешем 1.8 В це правильне налаштування для SDIO | `m2-63-gpio-07` | немає URL |
| ADC1 и ADC2 не рівноправні у использовании | `m2-63-gpio-07` | немає URL |
| Таблиця АДС чанели - канал 1 та канал 2 | `m2-63-gpio-07` | немає придатних уривків |
| На classic ESP32: 6 пінів флешу, 2 консолі, 6 тільки-вхідних, 5 strapping | `m2-63-gpio-07` | немає URL |
| Таблиця завантаження: GPIO0/GPIO15 комбінації для режимів | `m2-63-gpio-07` | немає придатних уривків |
| Потужність (P, вати) — формула P = U × I | `m2-65-electronics-05` | немає придатних уривків |
| Закон Ома — формула U = I × R | `m2-65-electronics-05` | немає придатних уривків |
| Дешевий USB-кабель — причина перезавантаження через падіння напруги | `m2-65-electronics-05` | немає придатних уривків |
| Формула резистора для світлодіода — R = (U_живлення − U_світлодіода) / I_бажаний | `m2-65-electronics-05` | немає придатних уривків |
| Пін ESP32 віддає обмежений струм — більше немає стану "необмеженого" | `m2-65-electronics-05` | немає URL |
| Параметри GPIO — в таблиці DC Characteristics, а не в Absolute Maximum | `m2-65-electronics-05` | немає придатних уривків |
| Сумарний максимум всіх GPIO — 1200 мА на всі виводи разом | `m2-65-electronics-05` | немає URL |
| GPIO drive capability — "medium" на основі GPIO_DRIVE_CAP_DEFAULT | `m2-65-electronics-05` | немає придатних уривків |
| Десять світлодіодів на одному домені — перевищення за межею домену, не за сумарною | `m2-65-electronics-05` | немає придатних уривків |
| Пін 5V/VIN — це вхід стабілізатора, а не GPIO вхід | `m2-65-electronics-05` | немає придатних уривків |
| VIN принаймні 5 В — це заявлена напруга для модулів ESP32 | `m2-65-electronics-05` | немає придатних уривків |
| Ультразвуковий далекомір HC-SR04 — вихід ECHO 5 В | `m2-65-electronics-05` | немає URL |
| Логічні мікросхеми серії 74HC при 5 В живленні — 5-вольтовий вихід | `m2-65-electronics-05` | немає URL |
| Релейні модулі для Arduino — 5-вольтові логічні входи | `m2-65-electronics-05` | немає придатних уривків |
| Дисплеї "для Arduino" — 5-вольтові входи | `m2-65-electronics-05` | немає придатних уривків |
| ESP32 3.3 В часто сприймається як HIGH 5-вольтовими входами | `m2-65-electronics-05` | немає URL |
| Дільник напруги 5 В → 3.3 В: R1=10 кОм, R2=20 кОм, V_out ≈ 1.65 В | `m2-65-electronics-05` | немає придатних уривків |
| Резистор як перетворювач рівня — не працює для SPI (завалює фронти) | `m2-65-electronics-05` | немає придатних уривків |
| Резистор як перетворювач рівня — не працює для I²C (відкриває коло) | `m2-65-electronics-05` | немає URL |
| I²C потребує двонапрямленого перетворювача на базі FET | `m2-65-electronics-05` | немає URL |
| Pull-up резистор — електричний опір від сигнальної лінії до живлення | `m2-65-electronics-05` | немає придатних уривків |
| ESP32 має вбудовані pull-up резистори, активуються з коду | `m2-65-electronics-05` | немає URL |
| Код GPIO конфіг — режим input з pull-up вмиканням | `m2-65-electronics-05` | немає URL |
| I²C та 1-Wire використовують open-drain/open-collector (pull-up) | `m2-65-electronics-05` | немає URL |
| Спільна земля — сигнали це напруги відносно точки відліку (GND) | `m2-65-electronics-05` | немає придатних уривків |
| Brownout — перезавантаження при короткому просідання напруги | `m2-65-electronics-05` | немає придатних уривків |
| MOSFET low-side схема — навантаження між +V та стоком, витік на GND | `m2-65-electronics-05` | немає URL |
| GPIO при старті не налаштований, лінія "висить" — небезпека вмкнення | `m2-65-electronics-05` | немає придатних уривків |
| Таблиця порівняння приладів діагностики — назва, призначення, ціна | `m2-66-analyzer-28` | немає URL |
| GND (земля) між пристроями мусить мати нульовий опір (спільна земля) | `m2-66-analyzer-28` | немає придатних уривків |
| Восьмиканальний USB-аналізатор коштує як пара плат (≈100–200 грн) | `m2-66-analyzer-28` | немає придатних уривків |
| I²C помилка: SCL йде, SDA мовчить → ведений не відповідає | `m2-66-analyzer-28` | немає придатних уривків |
| I²C помилка: START, адреса, NACK → пристрою з такою адресою немає | `m2-66-analyzer-28` | немає придатних уривків |
| I²C успішна передача: START, адреса, ACK, дані → шина працює правильно | `m2-66-analyzer-28` | немає придатних уривків |
| I²C помилка: SCL розтягнутий, SDA чекає → clock stretching | `m2-66-analyzer-28` | немає придатних уривків |
| UART декодування — один канал на лінію, помилка швидкості видна як сміття | `m2-66-analyzer-28` | немає придатних уривків |
| SPI діагностика — потрібні чотири канали (SCK, MOSI, MISO, CS) | `m2-66-analyzer-28` | немає придатних уривків |
| SPI помилка: дані зчитуються не по тому фронту → видно на аналізаторі | `m2-66-analyzer-28` | немає придатних уривків |
| I²C (100–400 кГц) та UART вистачає дешевого аналізатора (24 МГц) | `m2-66-analyzer-28` | немає придатних уривків |
| SPI на 40 МГц — недостатньо 24 МГц аналізатора, потребує осцилографа | `m2-66-analyzer-28` | немає придатних уривків |
| I²C сканер — програма що перебирає адреси й друкує які відповідають | `m2-66-analyzer-28` | немає URL |
| Мультиметр — вимір напруги, опору, малих струмів | `m2-66-analyzer-28` | немає придатних уривків |
| Осцилограф — спостереження форми сигналу та часових параметрів | `m2-66-analyzer-28` | немає придатних уривків |
| GPIO5 для поплавкового вимикача на ESP32-S3 | `m2-67-project-62` | немає придатних уривків |
| GPIO5 для поплавкового вимикача на ESP32-C3 | `m2-67-project-62` | немає придатних уривків |
| Кнопка, що подає сигнал на GPIO, не працює, коли чип завис | `m2-67-project-62` | немає придатних уривків |
| HC-SR04 видає 5 В на виводі ECHO | `m2-70-module-44` | немає URL |
| Подача 5 В на GPIO ESP32 пошкоджує вхід | `m2-70-module-44` | немає URL |
| I²C потребує підтягувальних резисторів | `m2-71-i2c-35` | немає URL |
| ESP-IDF рекомендує 2–5 кОм для I²C підтягування | `m2-71-i2c-35` | немає придатних уривків |
| На 100 кГц 4.7 кОм годиться, на 400 кГц — ні | `m2-71-i2c-35` | немає URL |
| Мінімум 1 кОм для обмеження струму через open-drain вихід | `m2-71-i2c-35` | немає URL |
| Адреса бутлоадера залежить від чипу | `m2-72-symptoms-29` | немає URL |
| Linux: Доступ до серійного порту вимагає групи dialout | `m2-72-symptoms-29` | немає придатних уривків |
| Deep sleep споживає 10 мкА; з ULP — близько 150 мкА | `m2-79-power-switches` | немає URL |
| SPI витримує десятки мегагерц | `m2-80-buses` | немає придатних уривків |
| RS-485 має термінаторів 120 Ом на обох кінцях лінії | `m2-80-buses` | немає придатних уривків |
| CAN має термінаторів 120 Ом на обох кінцях | `m2-80-buses` | немає придатних уривків |
| CAN пакет несе до 8 байтів даних | `m2-80-buses` | немає придатних уривків |
| Модулі на 5 В трансиверах можуть не бути сумісними з ESP32 | `m2-80-buses` | немає придатних уривків |
| HC-SR04 вимірює тривалість імпульсу | `m2-81-sensors-lora` | немає придатних уривків |
| LoRa модулі продаються на частоти 433, 868, 915 МГц | `m2-81-sensors-lora` | немає придатних уривків |
| DS18B20 вимагає delay(750 мс) для читання температури | `m2-81-sensors-lora` | немає придатних уривків |
| VL53L0X / VL53L1X — лазерні далекомісні на I²C | `m2-81-sensors-lora` | немає придатних уривків |
| OneWire бібліотеки — OneWire і DallasTemperature для Arduino | `m2-81-sensors-lora` | немає придатних уривків |
| ACS712 — датчик струму на ефекті Холла з аналоговим виходом | `m2-81-sensors-lora` | немає URL |
| Сервомотор керується імпульсами 50 Гц з тривалістю 1–2 мс. | `m2-90-sample` | немає придатних уривків |
| Індекс GPIO21: сторінки 149, 310, 326, 335 додатку z | `m2-90-sample` | немає придатних уривків |
| Сервомотор приймає 50-герцові імпульси з тривалістю 1–2 мс. | `m2-90-sample` | немає придатних уривків |
| Реальні межі серво-імпульсів часто відрізняються від заявлених 1–2 мс (можуть бути 0.6–2.4 мс). | `m2-90-sample` | немає придатних уривків |
| ESP32-C3 дешевий, простий, має 400 КБ пам'яті — достатньо для простих проєктів | `m2-90-sample` | немає придатних уривків |
| При живленні модуля від 3.3 В це не гарантує, що його сигнальні рівні — 3.3 В | `m2-90-sample` | немає придатних уривків |
| Лабораторний блок живлення з обмеженням струму запобігає випаленню доріжок при коротких замиканнях | `m2-90-sample` | немає придатних уривків |
| Індекс GPIO15: сторінки 14, 17–18, 28, 71, 142, 173, 379 додатку z | `m2-90-sample` | немає придатних уривків |
| На ESP32-C3 з 400 КБ два одночасні TLS-з'єднання створюють помітне навантаження | `m2-90-sample` | немає придатних уривків |
| Практичний підхід SPI — почати з 1 МГц | `m2-91-sample` | немає придатних уривків |
| GPIO12 у покажчику розділу Z | `m2-91-sample` | немає придатних уривків |
| Поведінка ESP32 при 1.8В flash та неправильній конфігурації | `m2-91-sample` | немає придатних уривків |
| Wi-Fi канали 2.4 ГГц та регіональні обмеження | `m2-91-sample` | немає придатних уривків |
| Енергоспоживання ESP-NOW за цикл передачі | `m2-91-sample` | немає придатних уривків |
| Доступність ESP-IDF функцій прямо з коду Arduino | `m2-91-sample` | немає придатних уривків |
| Помилка 0xc (SW_CPU_RESET) — типово після паніки | `m2-91-sample` | немає придатних уривків |
| GPIO17 у покажчику розділу Z | `m2-91-sample` | немає придатних уривків |
| GPIO9 у покажчику розділу Z | `m2-91-sample` | немає придатних уривків |
| Доступ до поля структури за NULL покажчиком зі зсувом | `m2-91-sample` | немає придатних уривків |
| Причини непрошивання модуля | `m2-91-sample` | немає придатних уривків |
| Помилка 0xf — просіло живлення (BROWN_OUT_RESET) | `m2-91-sample` | немає придатних уривків |
| Призначення кнопок BOOT та EN на платі | `m2-91-sample` | немає придатних уривків |
| T-D-081: GPIO4 як другий за цінністю біт у boot масці | `m2-92-sample` | немає придатних уривків |
| T-D-042: Код скидання 0xe — EXT_CPU_RESET | `m2-92-sample` | немає придатних уривків |
| T-02-108: ESP32-C5 з Wi-Fi у двох діапазонах | `m2-92-sample` | немає придатних уривків |
| T-39-093: ESP32 не бачить 5 ГГц мережі | `m2-92-sample` | немає URL |
| T-07-063: Піни GPIO6-GPIO11 під'єднані до флешу в модулі | `m2-92-sample` | немає URL |
| T-E-110: Промислова шина потребує трансивера на 3.3 В | `m2-92-sample` | немає придатних уривків |
| T-K06-024: Код скидання 0x10 — RTCWDT_RTC_RESET | `m2-92-sample` | немає придатних уривків |
| T-D-022: Код скидання 0x7 — TG0WDT_SYS_RESET | `m2-92-sample` | немає придатних уривків |
| T-08-048: ESP32-C3 SuperMini обмежене 400 КБ пам'яті | `m2-92-sample` | немає придатних уривків |
| T-D-030: Код скидання 0xa — INTRUSION_RESET | `m2-92-sample` | немає придатних уривків |
| T-30-056: Розподіл пам'яті: 16 КБ і більше — PSRAM | `m2-92-sample` | немає придатних уривків |
| Дешево і масово: C3 з 400 КБ SRAM для простих задач | `m2-93-sample` | немає придатних уривків |
| Час пробудження й ініціалізації в розрахунку — 300 мілісекунд | `m2-93-sample` | немає придатних уривків |
| DS18B20 має похибку ±0.5°C у діапазоні −10…+85°C та ±2°C поза ним | `m2-93-sample` | немає URL |
| Модуль без стабілізатора: логічні рівні 3.3 В, під'єднувати прямо | `m2-93-sample` | немає придатних уривків |
| GPIO32 розраховується у розділах 53, 74–75, 182, 389 | `m2-93-sample` | немає придатних уривків |
| Заряд на цикл передачі Wi-Fi становить близько 500 мА·с | `m2-93-sample` | немає придатних уривків |
| Трансивер CAN повинен відповідати логіці 3.3 В, або потрібен конвертер рівнів на RX | `m2-93-sample` | немає придатних уривків |
| Код 0x04 в таблиці strapping пінів C3 означає GPIO8 | `m2-93-sample` | немає URL |
| Код 0x08 в таблиці strapping пінів S3 означає GPIO0 | `m2-93-sample` | немає URL |
| WROVER за схемою WROOM: GPIO16 вже нічий на WROVER через PSRAM | `m2-93-sample` | немає придатних уривків |
| T-41-044: Для BLE беріть NimBLE, C3 має 400 КБ | `m2-94-sample` | немає придатних уривків |
| T-16-034: У наступному поколінні бутлоадер став на `0x0` | `m2-94-sample` | немає URL |
| T-K08-044: WiFi не під'єднується — пароль, канал 12–13 або 5 ГГц | `m2-94-sample` | немає придатних уривків |
| T-Z-117: GPIO26 page references | `m2-94-sample` | немає придатних уривків |
| T-33-054: Період при 50 Гц — 20 мс, формула duty | `m2-94-sample` | немає придатних уривків |
| T-Z-113: GPIO2 page references | `m2-94-sample` | немає придатних уривків |
| T-C-103: bootloader address table — S3, C3, C6, H2 at 0x0 | `m2-94-sample` | немає URL |
| ESP-NOW використовує той самий діапазон частот, що Wi-Fi 2.4 ГГц | `m2-95-sample` | немає URL |
| Діод послідовно для захисту від переполюсовки, падіння 0.3–0.7 В | `m2-95-sample` | немає придатних уривків |
| GPIO12 з високим рівнем — правильне налаштування на модулях з 1.8В флешем | `m2-95-sample` | немає придатних уривків |
| Wi-Fi 5 ГГц доступний тільки на ESP32-C5 | `m2-95-sample` | немає придатних уривків |
| ESP32-C3 має 400 КБ SRAM — це головне обмеження | `m2-95-sample` | немає придатних уривків |
| DS3231 та MPU6050 мають однакову I2C адресу 0x68 | `m2-95-sample` | немає придатних уривків |
| T-E-067 — NRF24L01 · радіо 2.4 ГГц | `m2-96-sample` | немає придатних уривків |
| T-Z-123 — GPIO6 у індексі | `m2-96-sample` | немає придатних уривків |
| T-02-135 — Мережа 5 ГГц, чип C5 | `m2-96-sample` | немає придатних уривків |
| T-38-012 — CAN вузол публікує температуру з ідентифікатором | `m2-96-sample` | немає придатних уривків |
| T-23-023 — Суфікс модуля кодує обсяг флешу й PSRAM | `m2-96-sample` | немає придатних уривків |
| T-Z-115 — GPIO22 у індексі | `m2-96-sample` | немає придатних уривків |
| T-Z-112 — GPIO18 у індексі | `m2-96-sample` | немає придатних уривків |
| Просадка нижче 3.0 В — знак проблеми з живленням | `m2-97-sample` | немає придатних уривків |
| GPIO4 — індекс посилань | `m2-97-sample` | немає придатних уривків |
| Октальна PSRAM на S3 використовує п'ять додаткових пінів | `m2-97-sample` | немає придатних уривків |
| GPIO25 — індекс посилань | `m2-97-sample` | немає придатних уривків |
| Застосунок з Wi-Fi і TLS займає від 1 МБ | `m2-97-sample` | немає придатних уривків |
| Модулі мають власний стабілізатор, але мікросхема працює від 3.3 В | `m2-97-sample` | немає придатних уривків |
| Похибка датчика DS18B20 — два справні можуть розходитись до 1 °C | `m2-97-sample` | немає придатних уривків |
| GPIO34 — індекс посилань | `m2-97-sample` | немає придатних уривків |
| Дамп флешу починається з адреси 0x0 і містить бутлоадер | `m2-97-sample` | немає придатних уривків |
| Прошивка з Wi-Fi, TLS та веб-інтерфейсом займає близько 1.5 МБ | `m2-97-sample` | немає придатних уривків |
| T-02-030: SRAM, КБ · ESP32 → 520 | `m2-98-chips-datasheets` | немає придатних уривків |
| SCL пін розпиновки I2C: GPIO22 на ESP32 classic та GPIO9 на ESP32-S3 | `m2-98-sample` | немає придатних уривків |
| Покажчик до GPIO8 в розділі z-pokazhchyk | `m2-98-sample` | немає придатних уривків |
| Код помилки 0xc: програмне скидання ядра | `m2-98-sample` | немає придатних уривків |
| Arduino IDE часто копіює код під AVR без адаптування до ESP32 | `m2-98-sample` | немає придатних уривків |
| Покажчик до GPIO3 в розділі z-pokazhchyk | `m2-98-sample` | немає придатних уривків |
| SDA пін розпиновки I2C: GPIO21 на ESP32 classic та GPIO8 на ESP32-S3 | `m2-98-sample` | немає придатних уривків |
| GPIO12 утримується високим в схемі ESP32 | `m2-98-sample` | немає придатних уривків |
| Таблиця GPIO0 при скиданні розпиновки та ROM адреси | `m2-98-sample` | немає придатних уривків |
| ESP32 і його варіанти не підтримують 5 ГГц Wi-Fi, крім ESP32-C5 | `m2-98-sample` | немає URL |
| GPIO0 — ключовий пін для вибору режиму завантаження на ESP32 classic та S3 | `m2-98-sample` | немає придатних уривків |
| Суфікс в назві ESP32 плати кодує обсяг флеш та PSRAM: N8, N16R8 і т.д. | `m2-98-sample` | немає придатних уривків |
| На ESP32-C3 з 400 КБ доступної пам'яті MicroPython інтерпретатор залишає мало місця | `m2-98-sample` | немає придатних уривків |
| T-04-069: UART · S2 → 2 | `m2-99-peripherals-cores` | немає придатних уривків |
| T-04-093: I²S · S2 → 1 | `m2-99-peripherals-cores` | немає придатних уривків |
| T-04-096: I²S · C6 → 1 | `m2-99-peripherals-cores` | немає придатних уривків |
| T-03-003: [[classic]] [[S3]] ESP32 classic і S3 мають **два ядра**. | `m2-99-peripherals-cores` | немає придатних уривків |
| T-03-011: [[C3]] C3, C6, H2 і S2 **одноядерні**. | `m2-99-peripherals-cores` | немає придатних уривків |
| T-02-093: ESP32, S2 і S3 побудовані на ядрах Xtensa; C3, C6, H2 і решта нової лі | `m2-99-peripherals-cores` | немає придатних уривків |
| T-A-087: 0–4 · Обмеження → ADC1 | `m2-a1-pinouts-adc-strapping` | немає придатних уривків |
| Радіо на борту · RP2040 → ні (крім W) | `m2-parts-class-c` | немає URL |
| ОС · RP2040 → немає або RTOS | `m2-parts-class-c` | немає URL |
| Сон · RP2040 → мА | `m2-parts-class-c` | немає URL |
| Реальний час · RP2040 → добре | `m2-parts-class-c` | немає URL |
| Ціна плати · RP2040 → низька | `m2-parts-class-c` | немає URL |
| CP2102 — 11, 25, 29, 79, 81, 83, 114, 366, 391 | `m2-parts-class-c` | немає придатних уривків |
| PCF8574 — 57, 76, 267, 365, 386 | `m2-parts-class-c` | немає придатних уривків |
| ESP32-C3 дешевий, простий, має 400 КБ пам'яті — достатньо для простих | `m2-parts-class-c` | немає URL |
| Дешево і масово: C3 з 400 КБ SRAM для простих задач | `m2-parts-class-c` | немає URL |
| ESP32-C3 має 400 КБ SRAM — це головне обмеження | `m2-parts-class-c` | немає URL |
| Специфікація I²C — адресація, ємність шини, режими | `m2-parts-class-c` | немає URL |
| DS18B20 — час перетворення, діапазон, роздільність | `m2-parts-class-c` | немає URL |
| Паспортна похибка DS18B20 — на датчик, а не між датчиками | `m2-parts-class-c` | немає URL |
| BME280 — карта регістрів і формули компенсації | `m2-parts-class-c` | немає URL |
| S3 та C3 — USB-контролер на кристалі | `m2-parts-class-c` | немає URL |
| GPIO0 — ключовий пін для вибору режиму завантаження на ESP32 classic т | `m2-parts-class-c` | немає URL |
| LoRa SX127x і SX126x — параметри модуляції | `m2-parts-class-c` | немає URL |
| SPI витримує десятки мегагерц | `m2-parts-class-c` | немає URL |
| Дисплеї — зсув SH1106 і адреси I²C-модулів | `m2-parts-class-c` | немає URL |
| T-02-108: ESP32-C5 з Wi-Fi у двох діапазонах | `m2-parts-class-c` | немає URL |
| T-02-135 — Мережа 5 ГГц, чип C5 | `m2-parts-class-c` | немає URL |
| Дамп флешу починається з адреси 0x0 і містить бутлоадер | `m2-parts-class-c` | немає URL |
| GPIO12 з високим рівнем — правильне налаштування на модулях з 1.8В фле | `m2-parts-class-c` | немає URL |
| T-H-013: **Datasheet модуля** (`ESP32-WROOM-32`, `ESP32-S3-WROOM-1`,  | `m2-wave2` | немає URL |
| T-23-011: `ESP32-WROOM-32` · Що це значить практично → двоядерний Xten | `m2-wave2` | немає URL |
| T-36-055: SPI витримує десятки мегагерц, але не завжди | `m2-wave2` | немає URL |
| T-12-058: | Серійне виробництво, OTA, відтворюваність | ESP-IDF | | `m2-wave2` | немає URL |
| T-15-014: Виріб на роки, OTA, серійність · Чому → відтворюваність і ді | `m2-wave2` | немає URL |
| T-58-062: | OTA | оновлення і відкат проходять | | `m2-wave2` | немає URL |
| T-COM-025: MPU6050 · Чому → сам зводить дані, менше роботи | `m2-wave2` | немає URL |
| T-24-038: Формат NVS — сторінковий, з простором імен, ключем і типізов | `m2-wave2` | немає URL |
| T-18-052: NVS стійкий до зникнення живлення: запис влаштований так, що | `m2-wave2` | немає URL |
| T-53-017: Паспорти більшості елементів нормують заряджання від 0 до +4 | `m2-wave2` | немає URL |
| T-01-061: Старт · RP2040 → миттєво | `m2-wave2` | немає URL |
| T-25-037: Документація ESP-IDF описує це так: `Ctrl + L` — «Stop/resum | `m2-wave2` | немає URL |
| T-25-105: Лог пишеться у файл (`Ctrl+L` в `idf.py monitor`, для решти  | `m2-wave2` | немає URL |
| T-K10-019: idf.py -p /dev/ttyUSB0 monitor # монітор з розшифровкою back | `m2-wave2` | немає URL |
| T-K06-024: `0x10` · Назва → RTCWDT_RTC_RESET | `m2-wave2` | немає URL |
| T-D-047: `0x10` · Назва → RTCWDT_RTC_RESET | `m2-wave2` | немає URL |
| T-E-107: DS18B20 · Що дає → температура, кілька на лінії | `m2-wave2` | немає URL |
| T-59-146: - **MQTT** замість або разом із веб-інтерфейсом (розділ 40); | `m2-wave2` | немає URL |
| T-COM-030: **Лишаються добрим вибором:** DS18B20 (довгий дріт, герметич | `m2-wave2` | немає URL |
| T-09-046: **JTAG іде тим самим кабелем.** Повноцінне покрокове налагод | `m2-wave2` | немає URL |
| T-20-030: esptool --port /dev/ttyUSB0 flash-id | `m2-wave2` | немає URL |
| T-18-026: **`nvs` лежить перед застосунком.** Це сховище пар «ключ — з | `m2-wave3` | немає URL |
| T-18-061: Якщо серед налаштувань є те, чого не відновити (серійний ном | `m2-wave3` | немає URL |
| T-24-033: NVS зберігає конфігурацію конкретного екземпляра | `m2-wave3` | немає URL |
| T-22-066: У всіх інших випадках — від чужого виробу до власного пристр | `m2-wave3` | немає URL |
| T-56-018: Налаштування.** Що зберігається в NVS, як задається, як скин | `m2-wave3` | немає URL |
| T-32-052: **Незавершений запис у флеш.** NVS до цього стійкий за задум | `m2-wave3` | немає URL |
| T-18-012: `nvs` · Підтип → nvs | `m2-wave3` | немає URL |
| T-18-048: NVS (Non-Volatile Storage) — сховище пар «ключ — значення»,  | `m2-wave3` | немає URL |
| T-G-145: | NVS | Non-Volatile Storage | | `m2-wave3` | немає URL |
| T-55-083: У NVS може лежати конфігурація, якої немає більше ніде, і пі | `m2-wave3` | немає URL |
| T-18-011: `nvs` · Тип → data | `m2-wave3` | немає URL |
| T-H-027: **Документація на конкретні мікросхеми** — сайти виробників: | `m2-wave3` | немає URL |
| T-37-002: Практично весь його світ для нас — це датчики температури DS | `m2-wave3` | немає URL |
| T-COM-085: Поріг для DS18B20 не випадковий і не збігається з паспортною | `m2-wave3` | немає URL |
| T-45-013: **DS18B20** — тільки температура, але на довгому дроті, у ге | `m2-wave3` | немає URL |
| T-56-025: **Перелік компонентів** із конкретними позначеннями: не «дат | `m2-wave3` | немає URL |
| T-37-016: Паспортна похибка DS18B20 — **±0.5 °C у діапазоні −10…+85 °C | `m2-wave3` | немає URL |
| T-COM-055: SX1276 / RFM95 · Застереження → більше бібліотек і прикладів | `m2-wave3` | немає URL |
| T-COM-053: SX1262 · Застереження → ефективніший за SX1276 | `m2-wave3` | немає URL |
| T-COM-054: SX1276 / RFM95 · Для чого → LoRa | `m2-wave3` | немає URL |
| T-E-061: SX1276 / RFM95 · Що дає → LoRa | `m2-wave3` | немає URL |
| T-E-062: SX1276 / RFM95 · Бібліотека → RadioLib, LoRa | `m2-wave3` | немає URL |
| T-43-022: `RFM95` — це модуль на чипі `SX1276`, тому в бібліотеках вон | `m2-wave3` | немає URL |
| T-43-021: **SX1276 / RFM95** — класика, широко доступні, море бібліоте | `m2-wave3` | немає URL |
| T-E-060: SX1276 / RFM95 · Режим → 0 | `m2-wave3` | немає URL |
| T-30-052: Друге, і саме воно частіше: коли PSRAM увімкнено, `malloc` * | `m2-wave3` | немає придатних уривків |
| T-A-067: 33–37 · Обмеження → флеш/PSRAM на Octal-модулях | `m2-wave3` | немає URL |
| T-A-065: 26–32 · Обмеження → **флеш і PSRAM** | `m2-wave3` | немає URL |
| T-G-159: | PSRAM | Pseudo-Static RAM | | `m2-wave3` | немає URL |
| T-30-050: **PSRAM є, але поводиться не так, як гадають.** Тут два поши | `m2-wave3` | немає URL |
| T-H-014: Саме він каже, які виводи доступні й скільки флешу та PSRAM  | `m2-wave3` | немає URL |
| T-02-097: **Потребує уваги:** номери пінів — вони інші скрізь (картка  | `m2-wave3` | немає URL |
| T-K10-001: Синтаксис esptool **v5** (дефіси, без `.py`) | `m2-wave3` | немає URL |
| T-08-088: Модуль — джерело істини про те, що всередині; звіряти напис  | `m2-wave3` | немає URL |
| T-17-034: `flash-id` як перша команда зручна тим, що після шапки додає | `m2-wave3` | немає URL |
| T-E-048: Разом на одній шині — конфлікт; розв'язується перемичкою на  | `m2-wave3` | немає URL |
| T-E-027: INA219 / INA226 · Адреса → `0x40`+ | `m2-wave3` | немає URL |
| T-25-038: Монітор — інтерактивна програма з кольорами й керуванням із  | `m2-wave3` | немає URL |
| T-C-067: idf.py monitor # з розшифровкою backtrace на льоту | `m2-wave3` | немає URL |
| T-25-036: Для `idf.py monitor` є **власний спосіб**, і він кращий за п | `m2-wave3` | немає URL |
| T-26-044: Тому **на RISC-V лог знімають `idf.py monitor`**, не чимось  | `m2-wave3` | немає URL |
| T-26-035: **Автоматично.** `idf.py monitor`, запущений з каталогу проє | `m2-wave3` | немає URL |
| T-11-097: - **IntelliSense**, налаштований на конкретний чип: автодопо | `m2-wave3` | немає URL |
| T-E-073: MAX31855 · Що дає → термопара | `m2-wave3` | немає URL |
| T-44-005: `BME280`, `SSD1306`, `MAX485`, `A4988` | `m2-wave3` | немає URL |
| T-E-007: BME280 · Що дає → тиск, T, вологість | `m2-wave3` | немає URL |
| T-45-019: **BMP280 / BME280** — атмосферний тиск | `m2-wave3` | немає URL |
| T-44-054: Для SPI — прочитати регістр ідентифікації, який є майже в ко | `m2-wave3` | немає URL |
| T-E-010: BMP280 · Що дає → тиск, T — **без** вологості | `m2-wave3` | немає URL |
| T-45-011: **BMP280** — те саме без вологості, дешевший | `m2-wave3` | немає URL |
| T-48-069: L298N втрачає близько двох вольтів на собі — для нового проє | `m2-wave3` | немає URL |
| T-19-086: Для OTA потрібен саме образ застосунку, без бутлоадера і таб | `m2-wave3` | немає URL |
| T-23-066: За один цикл скидання звідси дістається: причина попередньог | `m2-wave3` | немає URL |
| T-18-001: Флеш ESP32 — не один суцільний шматок пам'яті, а набір облас | `m2-wave3` | немає URL |
| T-22-055: Другий бутлоадер безкоштовно друкує версію ESP-IDF, обсяг фл | `m2-wave3` | немає URL |
| T-D-106: Звідси безкоштовно читається: **версія ESP-IDF**, **обсяг фл | `m2-wave3` | немає URL |
| T-50-026: Важливо розуміти межу: шифрування NVS має сенс **разом із**  | `m2-wave3` | немає URL |
| T-04-105: DAC · S2 → **2** | `m2-wave3` | немає URL |
| T-K09-009: | 25, 26 | єдині DAC-виходи | | `m2-wave3` | немає URL |
| T-04-050: DAC · Що це → [[classic]] [[S2]] справжній аналоговий вихід | `m2-wave3` | немає URL |
| T-04-150: DAC — тільки classic і S2 | `m2-wave3` | немає URL |
| T-04-104: DAC · classic → **2** | `m2-wave3` | немає URL |
| T-04-132: **DAC є лише в classic і S2.** Справжній аналоговий вихід бі | `m2-wave3` | немає URL |
| T-18-035: python $IDF_PATH/components/partition_table/gen_esp32part.py | `m2-wave3` | немає URL |
| T-24-011: python $IDF_PATH/components/partition_table/gen_esp32part.py | `m2-wave3` | немає URL |
| T-26-101: Потребує розділу типу `coredump` у таблиці розділів (розділ  | `m2-wave3` | немає URL |
| T-C-121: python $IDF_PATH/components/partition_table/gen_esp32part.py | `m2-wave3` | немає URL |
| T-K05-008: `partition-table.bin` · Що це → таблиця розділів | `m2-wave3` | немає URL |
| T-19-097: Rollback — окремий механізм, і він працює лише тоді, коли пі | `m2-wave3` | немає URL |
| T-19-098: OTA не оновлює таблицю розділів | `m2-wave3` | немає URL |
| T-19-062: OTA — це кілька хвилин безперервної роботи радіо на прийом п | `m2-wave3` | немає URL |
| T-19-001: OTA (over-the-air) — оновлення прошивки без фізичного доступ | `m2-wave3` | немає URL |
| T-19-029: OTA оновлює лише образ застосунку — таблиця розділів через O | `m2-wave3` | немає URL |
| T-50-067: - креденшели в NVS, унікальні на екземпляр — не в коді; - жо | `m2-wave3` | немає URL |
| T-18-105: **Зміна розбивки несумісна з OTA-оновленням.** Пристрій у по | `m2-wave3` | немає URL |
| T-19-024: Головне проєктне обмеження OTA — **застосунок займає місце д | `m2-wave3` | немає URL |
| T-19-005: Розбивка з OTA має **два розділи для застосунку** замість од | `m2-wave3` | немає URL |
| T-50-036: OTA — це канал, яким у пристрій потрапляє код | `m2-wave3` | немає URL |
| T-58-050: **OTA з відкатом**, якщо пристрій має оновлюватися | `m2-wave3` | немає URL |
| T-58-065: Випробування зникнення живлення варто робити **грубо**: вими | `m2-wave3` | немає URL |
| T-B-142: ADC читає дурницю · Причина → [[classic]] ADC2 при Wi-Fi | `m2-wave3` | немає URL |
| T-K08-028: 9 · Симптом → ADC читає дурницю | `m2-wave3` | немає URL |
| T-G-147: | ADC / DAC | Analog-to-Digital / Digital-to-Analog Converte | `m2-wave3` | немає URL |
| T-50-045: Обидва реалізовані через **eFuse** — біти, які пропалюються  | `m2-wave3` | немає URL |
| T-20-088: Флеш лікується завжди. eFuse — ніколи | `m2-wave3` | немає URL |
| T-20-014: **eFuse.** Це набір однорозрядних запобіжників у кремнії | `m2-wave3` | немає URL |
| T-20-005: Практично незворотний лише один клас операцій — запис eFuse | `m2-wave3` | немає URL |
| T-00-062: **Незворотне.** Операція, яку не можна скасувати: перепалени | `m2-wave3` | немає URL |
| T-20-043: **Не перенесеться MAC-адреса.** Вона зашита в eFuse кожного  | `m2-wave3` | немає URL |
| T-46-007: OLED SSD1306 · Особливості → контраст, малий, дешевий | `m2-wave3` | немає URL |
| T-46-004: OLED SSD1306 · Розмір → 0.96–1.3" | `m2-wave3` | немає URL |
| T-46-027: **OLED SSD1306** — типовий вибір для службової інформації | `m2-wave3` | немає URL |
| T-23-010: `ESP32-WROOM-32` · Чип → ESP32 classic | `m2-wave3` | немає URL |
| T-08-017: Літера `U` в кінці (`WROOM-1U`) означає роз'єм під зовнішню  | `m2-wave3` | немає URL |
| T-K01-006: `ESP32-WROOM-32` · Чип → ESP32 classic | `m2-wave3` | немає URL |
| T-39-078: **Зовнішня антена через роз'єм IPEX** — модулі з літерою `U` | `m2-wave3` | немає URL |
| T-39-076: **PCB-антена** — доріжка на платі модуля (`WROOM-1`) | `m2-wave3` | немає URL |
| T-01-009: **Модуль.** Кристал плюс кварц, флеш-пам'ять, антена і обв'я | `m2-wave3` | немає URL |
| T-23-012: `ESP32-WROOM-32D`, `-32E` · Чип → ESP32 classic | `m2-wave3` | немає URL |
| T-04-037: LEDC · Що це → PWM: яскравість світлодіодів, сервоприводи | `m2-wave3` | немає URL |
| T-06-088: **Ємність джерела.** Ходові елементи 18650 — від 2500 до 350 | `m2-wave3` | немає URL |
| T-60-006: **Живлення:** 18650, ціль — не менше трьох місяців при вимір | `m2-wave3` | немає URL |
| T-B-134: CAN: лічильник помилок росте · Розділ → 38 | `m2-wave3` | немає URL |
| T-04-098: TWAI (CAN) · classic → 1 | `m2-wave3` | немає URL |
| T-04-028: TWAI · Що це → CAN-шина, сумісна з автомобільною | `m2-wave3` | немає URL |
| T-63-080: - **Modbus RTU ↔ TCP** зі штатним компонентом `esp-modbus` з | `m2-wave3` | немає URL |
| T-63-061: Міст на CAN за замовчуванням має працювати в режимі **`LISTE | `m2-wave3` | немає URL |
| T-38-059: CAN сам стежить за помилками й має лічильники | `m2-wave3` | немає URL |
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
| T-E-065: SX1262 · Бібліотека → RadioLib | `queue-a-e-interfeysy` | немає придатних уривків |
| T-00-055: Чотири типи блоків трапляються по всьому тексту. | `queue-c-00-pro-dovidnyk` | немає придатних уривків |
| T-00-014: Замість людської вичитки застосовано **автоматизовану перевірку**, і зроблено | `queue-c-00-pro-dovidnyk` | немає придатних уривків |
| T-00-089: Мінімальний комплект, з яким можна робити все, що | `queue-c-00-pro-dovidnyk` | немає придатних уривків |
| T-01-011: **Плата розробки.** Модуль плюс USB-роз'єм, міст USB-UART, стабілізатор, | `queue-c-01-platforma` | немає придатних уривків |
| T-02-018: Ядер · ESP32 → **2** | `queue-c-02-chipy` | немає придатних уривків |
| T-04-057: Керування адресними світлодіодами WS2812, де таймінги вимірюються сотнями | `queue-c-04-peryferiya` | немає придатних уривків |
| T-05-078: Два таких виходи на одному дроті, що хочуть | `queue-c-05-elektronika` | немає придатних уривків |
| T-05-116: Статична електрика — це кіловольти. | `queue-c-05-elektronika` | немає придатних уривків |
| T-06-113: На платі розробки живуть USB-міст, стабілізатор і світлодіод | `queue-c-06-zhyvlennya` | немає придатних уривків |
| T-06-116: **LDO** (лінійний) — стоїть майже на всіх платах | `queue-c-06-zhyvlennya` | немає придатних уривків |
| T-08-051: Найдешевший спосіб отримати мережеву камеру, і найнезручніша плата | `queue-c-08-platy` | немає придатних уривків |
| T-08-033: **ESP32-DevKitC V4** — офіційна плата Espressif на 38 | `queue-c-08-platy` | немає придатних уривків |
| T-08-027: **Схема авторесету.** Два транзистори, керовані `DTR` і `RTS`. | `queue-c-08-platy` | немає придатних уривків |
| T-09-036: Сьогодні це рідше, але сам факт: якщо плата | `queue-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-008: На типовій платі розробки цей міст уже стоїть | `queue-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-043: **Порт має інше ім'я.** `/dev/ttyACM0` замість `/dev/ttyUSB0` у | `queue-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-030: **CH9102 з'являється як `/dev/ttyACM0`, а не `ttyUSB0`**: у | `queue-c-09-pidklyuchennya` | немає придатних уривків |
| T-09-110: На S3 і C3 порт називається `ttyACM`, драйвер | `queue-c-09-pidklyuchennya` | немає придатних уривків |
| T-16-021: Світлодіод із резистором на `GPIO0`, датчик, що тримає | `queue-c-16-boot` | немає придатних уривків |
| T-16-005: Він стартує завжди, незалежно від того, що у | `queue-c-16-boot` | немає придатних уривків |
| T-16-011: Головне практичне: **етапи 2 і 3 живуть у | `queue-c-16-boot` | немає придатних уривків |
| T-16-077: Дивитися треба **найперший** дамп після подачі живлення, а | `queue-c-16-boot` | немає придатних уривків |
| T-17-131: Повторюється стабільно на тій самій адресі — підозра | `queue-c-17-esptool` | немає придатних уривків |
| T-18-075: Швидкість при заповненні · FAT → рівна | `queue-c-18-rozdily-fleshu` | немає придатних уривків |
| T-18-062: Коли треба зберігати файли — веб-сторінки, конфігурацію, логи, | `queue-c-18-rozdily-fleshu` | немає придатних уривків |
| T-19-069: Мінімум, який реально працює: HTTPS із перевіркою сертифіката | `queue-c-19-ota` | немає придатних уривків |
| T-21-079: Цей файл відповідає на питання, які виникають через | `queue-c-21-seriyna` | немає придатних уривків |
| T-26-042: Наслідок практичний і неприємний: лог з C3, знятий | `queue-c-26-zboyi` | немає придатних уривків |
| T-37-007: Найпоширеніший датчик температури в саморобній техніці. | `queue-c-37-onewire` | немає придатних уривків |
| T-38-087: Один вузол на шині дає помилки: підтверджувати нема | `queue-c-38-can` | немає придатних уривків |
| T-38-035: **Швидкість має бути однаковою в усіх вузлів.** Один | `queue-c-38-can` | немає придатних уривків |
| T-39-023: **Тільки один канал одночасно.** Звідси обмеження APSTA вище | `queue-c-39-wifi` | немає придатних уривків |
| T-COM-036: A4988 · Замінники → DRV8825 (більший струм, мікрокрок | `queue-c-components-2026-08` | немає придатних уривків |
| T-COM-076: | **470 мкФ** | біля роз'єму живлення | | `queue-c-components-2026-08` | немає придатних уривків |
| T-E-096: PMS5003, SDS011 · Що дає → пилові частинки | `queue-c-e-interfeysy` | немає придатних уривків |
| T-E-100: A6 / SIM800 / SIM7600 · Що дає | `queue-c-e-interfeysy` | немає придатних уривків |
| T-E-137: A4988 / DRV8825 · Як → `STEP` + | `queue-c-e-interfeysy` | немає придатних уривків |
| T-K03-016: немає окремого чипа · Міст → native USB | `queue-c-k03-pidkl` | немає придатних уривків |
| T-REG-021: **LoRa-модулі продаються на різні частоти**, і не всі | `queue-c-regulatory-2026-08` | немає придатних уривків |
| T-REG-010: **Потужність передавача.** Обмежується як випромінювана потужність (з урахуванням | `queue-c-regulatory-2026-08` | немає придатних уривків |
| T-23-048: Помітно менше — просадка, і далі спершу розділ | `sweep-23-triazh` | немає придатних уривків |
| T-23-035: Подавати живлення на плату з видимим дефектом означає | `sweep-23-triazh` | немає придатних уривків |
| T-23-039: Дзвенить — шукати замикання, не вмикати. | `sweep-23-triazh` | немає придатних уривків |
| T-G-061: | пріоритет | priority | | `sweep-g-glosariy` | немає придатних уривків |
| T-G-062: | черга | queue | | `sweep-g-glosariy` | немає придатних уривків |
| T-Z-135: i2c_device_config_t — 215, 327 | `sweep-z-pokazhchyk` | немає придатних уривків |
