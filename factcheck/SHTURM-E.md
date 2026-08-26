# Штурм класу `E`

**Генерується** `tools/shturm.py`. Правити вручну нема сенсу.

Клас `E` присвоюється механічно — за браком у тексті цифри,
ідентифікатора, назви, одиниці виміру, — а читається як «джерела не
існує». Присуд винесено майже чотири тисячі разів і **жодного разу не
перевірявся**. Тут — що повернули помічники, коли їх послали його
штурмувати.

**Це здобич, а не міра.** Вибірку відібрано рукою там, де джерело
найімовірніше, тож відсотка звідси називати не можна: він завищений за
побудовою. Міру дає `tools/vybirka.py` — випадкова вибірка з насінням,
записаним у наряді.

Це **не докази**. Жоден запис звідси не входить у реєстр, доки
супровідник не звірить його сам: `znayshov` треба перевірити по суті
(шар 2), `ideya` — відпрацювати.

Зокрема адреси в колонці «де шукати» **ніхто не відкривав**. Це здогад
помічника про те, який документ мав би це містити, і серед них уже
трапляються шляхи, яких не існує. Здогад — теж робота: він перетворює
«неперевірне» на «ще не перевірене», а це різні стани, і другий має
адресата. Але доказом він не стає.

## Що з цим зробив третій шар

Кандидатів `znayshov` пропущено через `tools/citaty.py` **до** того, як
їх побачив супровідник. Шість не витримали, і кожен по-своєму:

- три — джерело за адресою просто не існує (404), а в полі цитати
  стоїть власна проза помічника, не текст документа. Обидві вигадки
  зловлено без жодного судження про зміст;
- один — рядок ядра Linux, **перенабраний з великої літери**
  (`Static struct` замість `static struct`). Факт правильний; цитата —
  ні. Відрізнити перенабір від вигадки, не дивлячись у джерело, не
  можна, тому підрядок і не пробачає;
- два — переказ замість цитати.

Це і є довід на користь дешевої моделі. Вигадка не проходить не тому,
що її хтось розпізнав, а тому, що її **нема за адресою**.

Записів: **239**. Підтверджено як чесний E — **113**, Названо, де шукати — **104**, Джерело знайдено — **22**.


## Джерело знайдено — 22

З них третій шар витримали **16**. Решта лишається тут із позначкою: спростування помічника теж результат, і ховати його нема за чим.

| Одиниця | Третій шар | Сила | Джерело | Що каже |
|---|---|---|---|---|
| `T-E-020` | **витримав** | повністю | [`library.properties`](https://raw.githubusercontent.com/adafruit/RTClib/master/library.properties) | RTClib library.properties explicitly lists DS3231 as supported |
| `T-E-029` | **витримав** | частково | [`library.properties`](https://raw.githubusercontent.com/adafruit/Adafruit_INA219/master/library.properties) | Library documentation only mentions INA219, not INA226; claim states both chips but library only supports INA2 |
| `T-E-053` | **витримав** | повністю | [`README.md`](https://raw.githubusercontent.com/Bodmer/TFT_eSPI/master/README.md) | TFT_eSPI README explicitly lists ST7789 as a supported display controller |
| `T-E-056` | **витримав** | повністю | [`README.md`](https://raw.githubusercontent.com/Bodmer/TFT_eSPI/master/README.md) | TFT_eSPI README explicitly lists ILI9341 as a supported display controller |
| `T-E-074` | **витримав** | частково | [`library.properties`](https://raw.githubusercontent.com/adafruit/Adafruit-MAX31855-library/master/library.properties) | Library documentation only mentions MAX31855K, not MAX6675; claim states both chips but library explicitly onl |
| `T-43-031` | **витримав** | повністю | [`README.md`](https://raw.githubusercontent.com/jgromes/RadioLib/master/README.md) | RadioLib README explicitly documents support for multiple LoRa module families from different manufacturers (S |
| `T-46-038` | **витримав** | повністю | [`README.md`](https://raw.githubusercontent.com/olikraus/u8g2/master/README.md) | U8g2 README explicitly states it is a library for monochrome displays |
| `T-46-045` | цитати немає | повністю | [`README.md`](https://raw.githubusercontent.com/lvgl/lvgl/master/README.md) | LVGL README explicitly describes it as a UI library with widgets, not a display driver |
| `T-F-013` | **витримав** | повністю | [`ch341.c`](https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/serial/ch341.c) | Linux kernel contains built-in drivers for all mentioned chips (cp210x.c, ch341.c, ftdi_sio.c); users do not n |
| `T-K10-038` | **витримав** | повністю | [`usb-serial.c`](https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/serial/usb-serial.c) | All USB serial drivers in Linux (including ch341.c for CH340 and cp210x.c for CP2102) register devices as ttyU |
| `T-08-025` | цитати немає | частково | [`cp210x.c`](https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/serial/cp210x.c) | CP2102 and CH340 confirmed as separate drivers in Linux kernel (cp210x.c and ch341.c respectively); CH9102 dri |
| `T-03-004` | **витримав** | повністю | [`soc.h`](https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/soc.h) | The ESP32 has two cores named PRO_CPU and APP_CPU; the definitions confirm their existence and numbering. |
| `T-34-020` | **витримав** | повністю | [`uart.rst`](https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst) | ESP-IDF UART documentation confirms that RX buffer size matters and overflow can occur when data arrives faste |
| `T-34-070` | цитати немає | повністю | [`uart.rst`](https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst) | Same source confirms that UART buffer overflow occurs silently if not configured properly with adequate size a |
| `T-09-039` | **витримав** | повністю | [`usb-serial.c`](https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/serial/usb-serial.c) | Linux USB serial driver dynamically allocates minor numbers to devices in the order they are detected, resulti |
| `T-A-054` | **витримав** | повністю | [`gpio.h`](https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_driver_gpio/include/driver/gpio.h) | Directly confirms that GPIO pins 34-39 on ESP32 are input-only and lack pull-up and pull-down capability. |
| `T-E-138` | **витримав** | частково | [`gpio_example_main.c`](https://raw.githubusercontent.com/espressif/esp-idf/master/examples/peripherals/gpio/generic_gpio/main/gpio_example_main.c) | Confirms input with pull-up configuration in ESP32 GPIO examples; debouncing is implemented in software logic, |
| `T-H-015` | **витримав** | дотично | [`index.rst`](https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/hw-reference/index.rst) | References Espressif's official Hardware Design Guidelines which exist and document PCB routing, antenna zone, |
| `T-K09-005` | **витримав** | повністю | [`gpio.h`](https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_driver_gpio/include/driver/gpio.h) | Directly confirms that GPIO pins 34-39 on ESP32 are input-only with no pull-up or pull-down capability. |
| `T-05-017` | джерело недосяжне | повністю | [`ledc_example_main.c`](https://raw.githubusercontent.com/espressif/esp-idf/master/examples/peripherals/ledc/ledc_example_main.c) | While I cannot directly access and quote the specific file due to API issues, LED circuit fundamentals are doc |
| `T-05-100` | джерело недосяжне | повністю | [`gpio_ll.h`](https://raw.githubusercontent.com/espressif/esp-idf/master/components/hal/include/hal/gpio_ll.h) | Capacitor polarity is a fundamental electronic component requirement documented in IEC/ISO standards and every |
| `T-06-108` | джерело недосяжне | частково | [`get-started-pico-devkit.rst`](https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/hw-reference/esp32/get-started-pico-devkit.rst) | The specific technique (shunt + scope) is a well-established measurement method documented in electronics test |


## Названо, де шукати — 104

| Одиниця | Де шукати |
|---|---|
| `T-46-042` | U8g2's Wiki documentation at https://github.com/olikraus/u8g2/wiki/u8g2setupcpp describes the configuration method (whether in-library or in-project); |
| `T-02-146` | CPU/ISA reference manuals or ESP-IDF architecture documentation would document that Xtensa and RISC-V have different instruction sets and ABIs (affect |
| `T-F-012` | Silicon Labs CP2102/CP2102N official driver documentation and WCH CH340/CH341 driver datasheet would specify Windows driver requirements and USB vendo |
| `T-K03-017` | ESP-IDF documentation for specific ESP32 variants (particularly ESP32-S3 and newer models with built-in USB) would document whether they have a separa |
| `T-04-141` | ESP32 Technical Reference Manual Section on interrupts and the maximum interrupt source limit; ESP-IDF examples with high-frequency interrupts and the |
| `T-33-061` | Motor driver IC datasheets (e.g., DRV8833, L298N, or similar) document the protection mechanisms built into bridge drivers and why they are essential  |
| `T-48-006` | Motor driver IC datasheets (e.g., DRV8833, L298N, A4988) specify the bulk capacitor requirement near power pins for stable operation. |
| `T-48-031` | Motor driver datasheets document the consequence of inadequate current limiting or improper frequency setting, showing thermal dissipation curves and  |
| `T-48-034` | Motor driver IC datasheets provide the formulas for calculating current-limiting potentiometer settings based on sense resistor values and desired cur |
| `T-48-035` | Motor driver IC application notes and datasheets document the risk of back-EMF from motor disconnection under power and explain why it can damage the  |
| `T-48-036` | Stepper motor driver IC datasheets (e.g., DRV8825, A4988, TMC2209) document microstepping feature and the step division ratios (1/2, 1/4, 1/8, 1/16, 1 |
| `T-48-070` | Stepper driver application notes and datasheets explain why current limiting must be set before first startup to prevent damage and ensure correct ope |
| `T-03-015` | ESP-IDF optimization guide or application notes would document the design pattern of separating heavy computation tasks from connectivity tasks across |
| `T-03-016` | FreeRTOS documentation and ESP-IDF threading guide explain that single-threaded code runs on only one core, leaving the other core unused. |
| `T-31-034` | ESP-IDF documentation on task scheduling, core affinity, and timing constraints would explain why timing-critical tasks should run on core 1 away from |
| `T-31-035` | ESP-IDF FreeRTOS task scheduling and core affinity guide would document how to assign heavy/long-running tasks to core 1 to avoid interference with ne |
| `T-47-048` | Power electronics and MOSFET driver IC datasheets (e.g., IR2104, IRS2104) explain why high-side switching requires either P-channel transistors or boo |
| `T-05-033` | ESP-IDF GPIO driver API documentation (esp_gpio_set_drive_capability) or default configuration files would document the default GPIO output drive stre |
| `T-26-059` | FreeRTOS documentation and ESP-IDF RTOS guide explain the IDLE task's role in detecting when a core is over-subscribed by checking if it receives sche |
| `T-09-035` | FTDI driver source code (ftdi_sio.c) and commit history, or FTDI official statements about driver behavior regarding counterfeit chips and their handl |
| `T-09-091` | Windows Device Manager documentation or driver installation guides explain that yellow exclamation marks indicate driver issues rather than hardware f |
| `T-29-070` | Driver source code (in esp-idf components or Linux kernel) documents where and how drivers reconfigure GPIO pin modes/functions and why reading hardwa |
| `T-06-036` | ESP-IDF boot loader code or log format documentation would show what messages appear in the boot log for power supply detection. |
| `T-COM-081` | FTDI forums, driver source code, or technical documentation about counterfeit chips and their stability issues; also technical articles on counterfeit |
| `T-A-123` | Datasheets for PCF8574, MCP23017, 74HC595/165, and CD4051 confirm their I/O expansion capabilities; ESP-IDF examples or Arduino libraries document the |
| `T-G-172` | IEC 60027 standard for electrical units and symbols; international standards for unit notation and abbreviations. |
| `T-K13-011` | USB 2.0/3.0 specification documents define the nominal USB power supply voltage as 5V ±5%; also ESP32 development board schematics showing USB connect |
| `T-43-082` | Zigbee Alliance (now Connectivity Standards Alliance) documentation about Zigbee protocol adoption in building automation; market analysis of the Zigb |
| `T-54-017` | Cable gland component datasheets and standards (e.g., IP67/IP68 ratings) that define these standardized components for sealing enclosures. |
| `T-06-007` | USB power specification (5V nominal); ESP32 development board schematics (e.g., ESP32-DevKitC) showing USB connector to 3.3V LDO regulator circuit. |
| `T-COM-016` | ESP32-CAM board schematic and pinout documentation (available from Espressif or board manufacturer); Arduino-ESP32 board profile for ESP32-CAM that sp |
| `T-G-091` | IEEE 802.11-2020 standard or Espressif ESP-IDF API documentation (components/esp_wifi/include/esp_wifi.h) would define RSSI and signal strength termin |
| `T-K14-004` | Espressif ESP32 datasheet and Technical Reference Manual (available at espressif.com/products/socs/esp32/resources) document GPIO voltage levels as 3. |
| `T-K14-005` | IEEE 802.11 digital logic threshold specifications and the datasheet of the specific module would define the minimum input voltage threshold for recog |
| `T-K14-023` | Level converter module datasheets (e.g., BSS138-based I2C level converters) or Espressif's official documentation about hardware design would specify  |
| `T-39-065` | Espressif ESP-IDF source code (components/esp_wifi/include/esp_wifi.h or examples/wifi/getting_started/station/) documents what RSSI represents; IEEE  |
| `T-14-012` | Micropython repository (micropython/micropython) and its benchmarks, or detailed performance comparisons between MicroPython and C implementations on  |
| `T-35-029` | Philips/NXP I2C specification or the I2C Bus Specification documents (UM10204) specify timing parameters including rise time, which is directly affect |
| `T-48-060` | Motor control safety standards and ESC (Electronic Speed Controller) datasheets (e.g., SimonK firmware documentation, ArduPilot motor safety documenta |
| `T-62-052` | Relay module datasheets and Arduino-based relay control documentation would specify voltage requirements for relay coils; motor control and relay driv |
| `T-47-091` | Level converter module datasheets (e.g., BSS138 or similar FET-based bidirectional converters) and Espressif hardware design application notes would d |
| `T-34-051` | Modbus Application Protocol Specification (available from the Modbus Organization) documents slave address ranges; specification states addresses 1-24 |
| `T-49-030` | OV2640 camera module datasheet and Espressif esp32-camera repository documentation would confirm the 2 Megapixel resolution and JPEG hardware compress |
| `T-05-029` | ESP32 Technical Reference Manual and datasheet (DC Characteristics table) document GPIO output current specifications; specifically, the relationship  |
| `T-05-031` | ESP32 datasheet DC Characteristics table specifies different output current capability for source (40 mA typical at max drive) versus sink (28 mA) mod |
| `T-06-053` | ESP32 datasheet and Espressif power supply design guidelines document the minimum recommended power source current (1A) for stable WiFi operation; ESP |
| `T-60-070` | Typical LDO (Low-Dropout) regulator datasheets specify minimum input voltage for maintaining output voltage; for a 3.3V output with typical 0.4-0.5V d |
| `T-60-071` | Buck-boost (step-down/step-up) converter datasheets and application notes specify operating input voltage range; typical devices support down to 2.5-3 |
| `T-30-053` | ESP-IDF compiler documentation and source code (components/compiler/CMakeLists.txt or compiler options) specify automatic function inlining settings a |
| `T-B-072` | ESP-IDF system power management and reset error documentation (esp-idf/components/esp_system/ or esp_hw_support/) would document rst:0xf reset code an |
| `T-B-075` | ESP-IDF WiFi component documentation (esp-idf/components/esp_wifi/) or WiFi example code would specify power supply requirements (current and capacita |
| `T-B-094` | I2C bus specification from NXP (formerly Philips) or Linux kernel I2C documentation (linux/drivers/i2c/) would define the standard 4.7 kΩ pull-up resi |
| `T-B-161` | ESP-IDF GPIO driver examples (esp-idf/examples/peripherals/gpio/) or relay driver documentation would demonstrate pull-down resistor sizing for contro |
| `T-E-146` | Soil moisture sensor datasheets and technical comparisons (found in manufacturer documentation or sensor evaluation guides on GitHub) would compare ca |
| `T-K08-015` | Card K13 (referenced here) would be a prior card in the handbook documenting the power-cable-capacitor troubleshooting steps; the external verificatio |
| `T-K08-026` | ESP-IDF GPIO and I2C driver documentation would support this troubleshooting principle that missing pull-ups or inadequate grounding cause most commun |
| `T-K13-025` | ESP32 power supply design documentation (esp-idf Hardware Design Guidelines or power management examples) would specify bulk capacitor requirements (t |
| `T-K13-027` | Decoupling capacitor standards (documented in IC datasheets, power supply application notes, and PCB design guides) recommend 100 nF ceramic capacitor |
| `T-07-082` | ESP-IDF GPIO driver documentation (components/esp_driver_gpio/) would detail pin states: which pins support only input/output, which have no built-in  |
| `T-45-023` | Photoresistor (LDR) datasheets and application notes would document the nonlinearity of response, temperature drift, and part-to-part variation in lig |
| `T-45-041` | PIR motion sensor datasheets (e.g., for BISS0001 or similar sensor modules) document warmup time (typically 30-60 seconds), response to moving heat so |
| `T-35-090` | I2C specification (Philips I2C standard) or Linux kernel I2C documentation would specify maximum pull-up current limits for the bus; multiple pull-ups |
| `T-28-077` | Audio interface specifications (AC coupling and DC offset requirements) or soundcard documentation would explain why audio inputs require DC blocking  |
| `T-48-030` | Stepper motor driver datasheets (A4988, DRV8825, TB6600, etc.) or motor controller application notes would document that current limiting must be set  |
| `T-48-068` | Motor and servo application notes would recommend separate power supplies for high-current loads, shared ground for reference, and bypass capacitors n |
| `T-51-049` | Electronic component datasheets (for capacitors, diodes, LEDs, and ICs) or soldering/assembly guides would document the standard polarity markings use |
| `T-47-012` | Isolation for low-power switching: Look in optocoupler/isolation IC datasheets (e.g., TLP291, PC817) and ESP-IDF examples using opto-isolators. Exampl |
| `T-47-040` | MOSFET gate as capacitance: Verify in MOSFET datasheets (any manufacturer - STMicroelectronics, Infineon, Texas Instruments, NXP), MOScontroller drive |
| `T-47-041` | 10 kΩ pull-down value: Verify in ESP-IDF GPIO driver documentation (esp_driver_gpio), microcontroller reference manuals for GPIO electrical characteri |
| `T-47-042` | Gate series resistor as safety feature: Verify in MOScontroller/gate driver datasheets (IRS2101, IR2110 etc.), MOSFET application notes, or circuit pr |
| `T-47-044` | Gate floating behavior without pull-down: MOSFET datasheets, GPIO driver documentation (especially sections on pin state before initialization), and c |
| `T-47-085` | Voltage divider definition (two resistors): Basic circuit theory documented in any electronics textbook, circuit design guides, or ESP-IDF examples sh |
| `T-47-095` | Common ground requirement: Fundamental circuit theory. Verify in circuit design guidelines, PCB layout standards, any tutorial on voltage reference, i |
| `T-47-098` | Common mistake of connecting grounds across isolation: Optocoupler, magnetic isolator, and galvanic isolation IC datasheets (TLP291, IL217, ADUM serie |
| `T-47-101` | 10 kΩ pull-down prevents load turn-on during ESP32 boot: Verify in ESP32 datasheet (startup sequence, GPIO default states), ESP-IDF bootloader documen |
| `T-47-105` | Common ground principle with isolation exception: Fundamental circuit theory in textbooks, bus standards (CAN, RS-485 specifications), and isolation I |
| `T-37-034` | OneWire/DS18B20 increased current draw during temperature conversion: DS18B20 datasheet (Maxim-Integrated/Analog Devices) states typical and maximum c |
| `T-53-051` | Separate analog supply filtering with LC or RC: Look in analog design handbooks (analog.com layout guides), ADC application notes (e.g., Maxim/Analog  |
| `T-53-063` | Enable voltage divider transistor only during measurement for power saving: Battery management design patterns, low-power system guidelines, or ADC me |
| `T-53-070` | Coulomb counter circuit design: Coulomb counter IC datasheets (BQ27441, LM25066), battery management system application notes, and power supply design |
| `T-49-016` | Backup power for graceful shutdown: Look in battery management application notes, UPS design guidelines, camera/video system design (professional vide |
| `T-49-050` | Audio amplifier power supply decoupling: Audio amplifier IC datasheets (e.g., LM4871, TPA2012), Espressif's audio/codec documentation, and PCB layout  |
| `T-54-054` | Mechanical stress from heavy components: PCB design guides (IPC standards), component manufacturer mounting recommendations, and vibration analysis do |
| `T-05-050` | Voltage divider definition: Basic circuit theory documented in every electronics textbook (Horowitz & Hill, Art of Electronics), circuit analysis refe |
| `T-05-063` | Pull-up resistor for defined GPIO state: Microcontroller GPIO driver documentation (esp_driver_gpio in ESP-IDF), general GPIO design guidelines, and o |
| `T-05-066` | Pull-down resistor to ground as mirror of pull-up: Electronics textbooks, GPIO driver documentation, and microcontroller reference manuals all define  |
| `T-05-073` | ESP32 pins 34-39 lack built-in pull-ups: Verify in ESP32 Technical Reference Manual (pin capabilities table), ESP32 datasheet (Espressif), or esp_driv |
| `T-05-098` | 470 μF decoupling capacitor as common power supply fix: Verify in ESP32 design guidelines, Espressif reference designs, espressif/esp-idf hardware req |
| `T-05-101` | Reversed electrolytic capacitor failure mode: Capacitor failure analysis (electrolytic capacitor specifications from manufacturers like Nichicon, Ruby |
| `T-05-129` | Floating input reads random value: Microcontroller GPIO design guides, digital logic documentation, and noise analysis tutorials explain why undefined |
| `T-05-130` | ESP32 pins 34-39 lack built-in pull-ups (repeated claim): Same as T-05-073 - verify in ESP32 Technical Reference Manual or esp_driver_gpio documentati |
| `T-05-131` | 100 nF per IC and 470 μF at power connector as universal decoupling strategy: Power integrity guidelines (IPC standards), PCB design handbooks, and IC |
| `T-55-047` | Troubleshooting reboot under load by checking power/cable/capacitor: Hardware diagnostics guides and power supply failure analysis documentation suppo |
| `T-55-050` | Silent sensors troubleshooting: check bus pull-ups and common ground: Bus standards (I2C, SPI, UART specifications) and communication peripheral docum |
| `T-58-049` | Gate resistors prevent load turn-on during boot: Same concept as T-47-101 - verify in microcontroller bootloader documentation and MOSFET gate pull-do |
| `T-46-073` | Port expansion alternatives - I2C expander (PCF8574), resistive analog keyboard divider, or capacitive touch: Verify in component datasheets (PCF8574  |
| `T-06-051` | 470 μF decoupling capacitor near module: Same claim as T-05-098 and T-05-131 - verify in Espressif reference designs, ESP32 development board schemati |
| `T-06-129` | 470 μF capacitor and short thick cable as power supply solution: PCB layout guidelines, cable impedance analysis, and power distribution design handbo |
| `T-44-009` | What to look for in a module schematic: regulator, pull-ups, level converter. Verify in typical module schematics (e.g., Adafruit breakout boards, Spa |
| `T-44-027` | Voltage divider or converter needed for level shifting: Same as T-05-050, T-05-085 - basic electronics and level-shifting documentation. TTL/CMOS volt |
| `T-COM-072` | 10 kΩ resistors for pull-ups and gate pull-down: Typical value in GPIO design guides and MOSFET application notes. Verify in microcontroller GPIO desi |
| `T-COM-073` | 100-220 Ω series gate resistor: MOSFET gate driver application notes and gate protection guidelines. Verify in MOSFET datasheets, gate driver IC datas |
| `T-COM-075` | 100 nF decoupling capacitor per IC: Same as T-05-131 - standard PCB design practice documented in IPC guidelines, IC manufacturer datasheets, and powe |
| `T-COM-076` | 470 μF bulk capacitor at power connector: Same as T-05-098, T-06-051, T-06-129 - power supply design practice. Documented in power integrity guideline |


## Підтверджено як чесний E — 113

| Одиниця | Чому джерела немає |
|---|---|
| `T-D-189` | This is a technical explanation about compiler and build system behavior, not a claim about external dependencies or product compatibility |
| `T-K12-025` | This describes the contents of an offline package/bundle which is a product description, not a claim verifiable against external sources |
| `T-04-009` | This describes GPIO design flexibility and software configuration patterns which are design principles, not claims about specific libraries or chip su |
| `T-45-065` | This is the author's advice on whether a ready-made library or custom implementation is easier, a matter of personal judgment and project scope |
| `T-01-106` | This describes recommended components for an offline package, which is a product/content description rather than a verifiable claim about dependencies |
| `T-14-025` | This is a characterization of the library ecosystem ("huge library of ready components") which is subjective description, not a verifiable factual cla |
| `T-08-054` | This describes a general property of custom PCBs (they require board-specific libraries), not a verifiable claim about specific libraries or products |
| `T-41-005` | This is a technical assertion about BLE hardware limitations and Bluetooth specifications which is not a claim about library features, but about proto |
| `T-56-044` | This is an observation about rebuilding reproducibility when toolchain or library versions change, which is a general engineering observation rather t |
| `T-11-041` | This is advice/guidance on version management strategy, not a factual claim about which versions are required or compatible |
| `T-11-085` | This describes Espressif's package management infrastructure, not a verifiable claim about library compatibility or features |
| `T-36-046` | This is an observation about how different libraries interpret the same SPI mode specification differently, which is about naming conventions and stan |
| `T-31-002` | This is a classification/conceptual statement that FreeRTOS is not a library to install but an execution environment, which is architectural framing r |
| `T-15-030` | This is performance optimization advice about which components to refactor first based on project constraints, not a verifiable fact |
| `T-37-001` | This is a technical description of the 1-Wire protocol specification, which is factual but describes the standard itself rather than a claim about spe |
| `T-46-031` | This is a general statement about library features ("most libraries have a separate mode"), too vague to verify against specific repositories |
| `T-46-043` | This is criticism and advice about U8g2 configuration methodology, which is the author's assessment of library design choices rather than a verifiable |
| `T-46-050` | This is a performance/architectural judgment about LVGL being overkill for simple displays, a design recommendation not a verifiable claim |
| `T-46-051` | This is an observation about typical library font support, too general and library-variant dependent to verify as a single statement |
| `T-46-055` | This states a requirement for UTF-8 support in libraries, which is a capability need rather than a verifiable claim about specific libraries |
| `T-46-056` | This is an observation about legacy libraries and their encoding limitations, which describes historical software patterns rather than current verifia |
| `T-12-028` | This is a subjective assessment of third-party library quality ("very uneven"), a matter of opinion rather than a verifiable fact |
| `T-12-037` | This describes a general pattern of library compatibility across Arduino versions (some work, some updated, some abandoned), which is an observation a |
| `T-13-054` | This is an observation about common build failure patterns, describing project management issues rather than verifiable claims about specific librarie |
| `T-13-069` | This is advice/best practice guidance about dependency pinning strategy, a procedural recommendation rather than a verifiable fact |
| `T-21-082` | This is an observation about reproducibility challenges in embedded projects, a general software engineering pattern rather than a specific verifiable |
| `T-02-098` | This is a classification statement about what types of components don't port across architectures, which describes general principles but not verifiab |
| `T-02-115` | This is an observation about typical timing of library support relative to new chip releases, a market/ecosystem pattern rather than a verifiable clai |
| `T-10-058` | This describes the contents of an offline development package, which is a product description rather than a verifiable claim about library features or |
| `T-K01-042` | This is operational troubleshooting guidance (if chip doesn't respond, check K3 checklist) without external technical reference to verify or refute. |
| `T-23-087` | Operational troubleshooting statement describing a symptom and reference to another section without external technical claim. |
| `T-20-012` | Advice about common causes of port detection failure; this is practical experience-based guidance rather than a statement with external technical refe |
| `T-08-002` | Meta-description of book section structure; this is editorial framing without external technical referent. |
| `T-08-074` | General design principle about board variations; this is architectural guidance rather than a verifiable technical fact. |
| `T-11-002` | Editorial statement about this reference being normative and requiring examples to work; this is a book structure declaration without external technic |
| `T-36-082` | Author's observation of a common mistake when learning to use a driver; this is experiential guidance without external reference to verify. |
| `T-09-028` | Anecdotal observation about common troubleshooting misinterpretation; this is experiential troubleshooting guidance without external technical referen |
| `T-44-001` | Meta-description of a book section's universal applicability; editorial statement without external technical referent. |
| `T-02-141` | Design principle explanation for hardware variation complexity; this is architectural reasoning rather than a verifiable external fact. |
| `T-52-064` | Practical engineering observation about prototyping methods; this is industry practice and practical convention rather than an externally verifiable f |
| `T-00-042` | Editorial description of the reference scope and coverage; this is a book structure statement without external technical referent. |
| `T-44-048` | Troubleshooting guidance suggesting trying standard components when specific ones are unavailable; this is practical advice without external reference |
| `T-B-195` | Troubleshooting advice linking disconnection symptom to diagnostic checks (RSSI, power) is based on practical experience patterns, not external standa |
| `T-K12-019` | Multimeter measurement accuracy at range boundaries is a general principle observed in analog circuit testing practice, but without specification of a |
| `T-39-073` | The advice to log RSSI for field diagnostics is based on practical troubleshooting experience with WiFi connectivity issues; while wise engineering pr |
| `T-43-003` | Positioning a section as an "overview" with "boundaries" is editorial framing of content; the decision to demarcate where LoRa becomes impractical is  |
| `T-14-003` | Describing when each tool is the "shortest path" and where "boundary" exists reflects the author's assessment of relative efficiency and applicability |
| `T-14-011` | The claim that Python has "minimal entry threshold" for people already familiar with Python is subjective assessment; entry threshold depends on indiv |
| `T-14-026` | The boundary where ESPHome YAML scripting becomes inconvenient for complex logic is a judgment about usability and code maintainability; different dev |
| `T-14-042` | "Simulation is not reality" reflects a philosophical observation about simulation limitations (no power supply droop, no noise, no contact bounce); wh |
| `T-15-043` | The threshold where custom logic becomes complex is a subjective boundary dependent on individual programming skill and project complexity; no externa |
| `T-50-058` | The security principle that a compromised sensor should only be able to falsify its own readings (and not cause system-wide damage) is a best-practice |
| `T-50-065` | The observation that configuration changes can have consequences beyond the device itself is an architectural principle reflective of system-of-system |
| `T-54-076` | Placing a temperature sensor outside the enclosure rather than inside is a measurement best practice based on the principle that the sensor reads its  |
| `T-54-086` | Placing temperature sensor outside the enclosure is a measurement best practice; the principle is that a sensor reads its immediate environment, not a |
| `T-24-051` | The "realistic boundary" for when to transition from one firmware flashing approach to another is a judgment call dependent on the specific firmware t |
| `T-58-027` | The advice to log RSSI during every communication session is a practical debugging guideline based on troubleshooting experience; while valuable pract |
| `T-46-026` | The statement that choosing an LCD type is a trade-off choice rather than a hardware boundary reflects the author's design philosophy; the distinction |
| `T-32-058` | The reliability engineering practice of incrementally tracking maximum observed values ("reached 1000 in RAM, then 2000") is a design methodology; it  |
| `T-10-007` | The observation that budget multimeters are inaccurate at range boundaries and have slow continuity beep response is a general electronics principle b |
| `T-A-003` | This is a meta-principle about PCB design (the board interface being more relevant than the chip pinout) rather than a measurable technical fact that  |
| `T-B-089` | This describes one possible cause of battery drain (a voltage divider drawing quiescent current) which is an implementation detail and design choice,  |
| `T-B-090` | This is a proposed circuit design solution (adding a switch to a voltage divider) that follows from T-B-089, representing a design pattern rather than |
| `T-E-132` | This is a circuit design recommendation (gate resistor for MOSFET control) whose value depends on specific gate drive current requirements and switchi |
| `T-E-142` | This is a cross-reference to another section of the handbook itself (section 53), not an independent claim that could be verified against an external  |
| `T-E-143` | This describes a standard analog sensor measurement pattern (voltage divider) used with various resistive sensors; the choice to use a divider with a  |
| `T-G-014` | This is a terminology entry and translation (pull-up/pull-down = підтягування вгору/вниз), which is a definitional matter, not a technical claim to be |
| `T-G-039` | This is a terminology entry and translation (voltage divider = дільник напруги), which is a definitional matter, not a technical claim. |
| `T-G-041` | This is a terminology entry and translation (decoupling capacitor = розв'язувальний конденсатор), which is a definitional matter, not a technical clai |
| `T-G-045` | This is a terminology entry (galvanic isolation = гальванічна розв'язка), which is a definitional matter, not a technical claim to verify. |
| `T-G-112` | This is a terminology entry (capacitance = ємність), which is a definitional matter, not a technical claim. |
| `T-G-170` | This is a style guide entry documenting the handbook's own writing convention (Ukrainian name + English term in brackets), not a universal technical s |
| `T-D-052` | This is troubleshooting heuristic advice (the problem is likely in power source, cable, or capacitors) rather than a documented technical requirement; |
| `T-K09-034` | This is the same principle as T-A-003: board-level design reality (the PCB manufacturer's choices about routing and components) is more relevant to th |
| `T-K06-030` | This is the same troubleshooting heuristic as T-D-052: practical debugging experience that code is usually not the root cause of these symptoms, but r |
| `T-K14-016` | This is a basic definition of a voltage divider circuit (two resistors to scale voltage), which is a fundamental circuit concept, not a claim that req |
| `T-K14-031` | This is a fundamental circuit design principle: for circuits to work correctly, they must share a common reference voltage (ground); this is not a doc |
| `T-K14-033` | This is a design warning explaining the inverse mistake of T-K14-031: if galvanic isolation is implemented to keep grounds separate, connecting them d |
| `T-07-022` | This describes basic pull-up resistor behavior in electronics: when a pin with an enabled pull-up is not actively driven low, it will read as high. Th |
| `T-45-028` | The specific resistor values (10 kΩ + 20 kΩ) for a photoresistor divider are design choices that depend on the sensor's characteristics and desired me |
| `T-45-053` | This describes a recognized design pitfall: when measuring battery voltage with a resistive divider, the divider's quiescent current can drain the bat |
| `T-45-054` | This is a cross-reference to other sections within the handbook itself (sections 33 and 53), not a claim that could be verified against an external so |
| `T-45-058` | This describes the principle that galvanic isolation (via optoisolator or Hall effect current sensor) allows measuring current in a circuit without co |
| `T-45-060` | This is a basic definition of a current shunt measurement technique (small resistor in series to measure voltage drop), which is a fundamental measure |
| `T-23-074` | This is a practical testing procedure (configure GPIO as pulled-up input, then short to ground to test for shorts or connectivity issues) that represe |
| `T-14-047` | This is a summary list of factors that affect serial communication and GPIO behavior, representing practical design experience rather than a specific  |
| `T-35-016` | This is an observation that many commercial sensor modules include I2C pull-up resistors on their boards; while true of many products, it is not a uni |
| `T-35-025` | This is a design principle for I2C with multiple pull-ups: calculate the parallel resistance rather than removing resistors randomly. This is a sound  |
| `T-35-067` | This describes the role of built-in GPIO pull-ups in I2C: they are insufficient alone but can be useful as a fallback when external pull-ups are missi |
| `T-28-020` | This is troubleshooting guidance: if a logic analyzer shows a bus line stuck at zero, it indicates either missing pull-ups or the line being actively  |
| `T-33-108` | This is a well-known embedded systems design issue: resistive voltage dividers for battery monitoring consume significant quiescent current, draining  |
| `T-33-110` | This quantifies the battery drain problem: the divider's current can exceed the chip's sleep current, making it the dominant drain. This is a conseque |
| `T-33-111` | This is a reference to another section within the handbook (section 53) describing a circuit solution (using a transistor to disable the divider durin |
| `T-62-019` | This is a bill of materials entry specifying component quantities for a specific project; it is project-specific data, not a universal technical claim |
| `T-62-043` | This is a reference to a design table within the handbook that determines pull-up/pull-down direction based on the specific module's active-high vs ac |
| `T-62-068` | This describes a common problem with optoisolator modules designed for 5V systems when used with 3.3V controllers: the current through the LED falls b |
| `T-62-083` | This is troubleshooting guidance: spurious sensor activation is often caused by missing pull-up resistors (causing floating inputs to be read as false |
| `T-47-038` | The specific claim requires context from the book's circuit diagram showing which two resistors and their exact function. Without seeing the schematic |
| `T-57-014` | This is a design methodology principle: when to ask safety questions about system robustness. It's the author's teaching approach to defensive design, |
| `T-53-029` | The claim 'for small elements this is too much' lacks context: which elements, which resistor value, which application? This is application-specific t |
| `T-53-064` | Claim that 'through divider nothing flows in sleep' is a specific circuit design optimization. Whether this is true depends on the divider's Thevenin  |
| `T-05-080` | Basic principle of pull-up resistor function - stated as fact without needing external verification. This is fundamental circuit theory documented eve |
| `T-05-083` | Pedagogical observation: why understanding pull-ups matters for bus operation. This is teaching methodology, not a technical fact to be verified. |
| `T-00-065` | This is a documentation style guideline for the handbook itself - a meta-claim about formatting convention, not a technical fact to verify. |
| `T-26-083` | Teaching heuristic: code issues are rare compared to hardware problems. This is the author's design philosophy and practical experience-based advice,  |
| `T-06-045` | Problem diagnosis: 'no capacitor on power supply' is a symptom-based troubleshooting step, not a verifiable principle. Whether a capacitor is needed d |
| `T-32-036` | Design methodology question: 'what if chip disappears now?' is the author's teaching approach to safety-first circuit design, not a verifiable technic |
| `T-32-087` | Principle that safe state is hardware-defined by resistor rather than software-defined: This is a design philosophy and best practice, not a verifiabl |
| `T-60-026` | Bill of materials entry: resistor value and quantity for a specific project. The choice of 4.7 kΩ for this project is context-dependent, not generaliz |
| `T-60-028` | Bill of materials entry: MOSFET and resistor count for a specific project. These are project-specific component selections. |
| `T-60-029` | Project-specific note about component function in this particular design. Application-specific, not a generalizable principle. |
| `T-10-040` | Tool/equipment recommendation: what materials to keep on hand. Not a technical claim to verify. |
| `T-COM-090` | Practical recommendation for a maker's toolkit. The specific items (4.7k, 10k resistors, 100nF, 470μF capacitors) are common values verified by experi |

