# Наряд: сліди класу `E`, які можна відпрацювати звідси

**Генерується** `tools/leady.py`. Це **не** перевірка присуду — присуд
уже випробуваний. Це відпрацювання того, що штурм і міра лишили як
`ideya`: «джерела не дістав, але знаю, де воно».

Кожен рядок нижче — одиниця книги плюс здогад попереднього помічника
про те, у якому документі шукати. **Здогад ніхто не перевіряв**, і
серед них уже траплялися шляхи, яких не існує. Не знайшов за названою
адресою — це не поразка й не привід шукати «щось схоже».

## Три відповіді

| Вердикт | Коли |
|---|---|
| `znayshov` | знайшов: адреса + **дослівна** цитата з документа |
| `ne_znayshov` | документ є, місця в ньому немає — напиши, що дивився |
| `nedosyazhne` | документ звідси не дістається (403, 404, заглушка) |

**`ne_znayshov` — повноцінна відповідь.** Здогад попереднього помічника
міг бути хибним; сказати про це прямо цінніше, ніж підібрати схожий
документ. Цитата з «майже того» джерела гірша за її відсутність.

## Заборони

Ті самі п'ять, що в `factcheck/POMICHNYKY.md`, і найважливіші тут дві:

- **не переказувати** — усе в полі `cytata` звіряється підрядком;
- **знати відповідь — не підстава написати цитату.** Якщо факт відомий,
  а рядка в документі не видно, це `ne_znayshov`.

Досяжне звідси лише `raw.githubusercontent.com` (через `curl`). Усе
інше — 403. **Не повторюй запит, що дав 403.**

Окремо: `espressif.com` на деякі адреси віддає **HTML-заглушку
15 495 байтів із кодом 200**. Відповідь «успішна», документа немає. Якщо
завантажене не схоже на документ — це `nedosyazhne`.

## Формат

```yaml
- odynycya: T-42-023
  verdykt: znayshov
  dzherelo: https://raw.githubusercontent.com/espressif/esp-idf/master/...
  cytata: |
    дослівний рядок із документа
  komentar: що саме він підтверджує
```

Слідів усього **154**, з них відпрацьовуються звідси **56**. Решта — борг із чесною причиною: названий документ за політикою мережі недосяжний.


## Пакет 1

**`T-09-077`**

- де шукати (здогад, не перевірений): POSIX стандарти та документація операційних систем (Linux, Windows) — там описується монопольний доступ до послідовного порту

**`T-11-072`**

- де шукати (здогад, не перевірений): Документація ESP-IDF (menuconfig користувацька інтерфейс та конфігураційні опції) — там описуються всі доступні параметри налаштування

**`T-19-070`**

- де шукати (здогад, не перевірений): ESP-IDF app_update компонента або native_ota_example - там розраховано механізм перевірки сертифіката при OTA-оновленні

**`T-42-023`**

- де шукати (здогад, не перевірений): ESP-IDF ESP-NOW documentation - там описаний API для реєстрації обробника приймання `esp_now_register_recv_cb`

**`T-42-029`**

- де шукати (здогад, не перевірений): ESP-IDF ESP-NOW implementation or documentation - там описана поведінка обробника в контексті Wi-Fi задачі та правила про блокування радіостека

**`T-46-039`**

- де шукати (здогад, не перевірений): U8g2 GitHub repository (README) - там перераховані всі підтримувані дисплеї (майже 50 моделей) і згадані шрифти


## Пакет 2

**`T-46-045`**

- де шукати (здогад, не перевірений): LVGL GitHub repository (README) або офіційна документація - там описано, що LVGL це «30+ built-in Widgets: Button, Label, Slider, Chart, Keyboard» і інші компоненти

**`T-50-040`**

- де шукати (здогад, не перевірений): ESP-IDF документація про Flash Encryption та Secure Boot - там описано, що це irreversible механізми, які змінюють eFuse фізично

**`T-40-088`**

- де шукати (здогад, не перевірений): ESP-IDF Hardware Security Architecture або документація конкретного чипа (напр. ESP32 Technical Reference Manual) - там описані апаратні акселератори криптографії

**`T-E-094`**

- де шукати (здогад, не перевірений): Datasheet сенсора MH-Z19 від виробника — там буде вказана швидкість UART (9600 baud). Однак datasheet розташований на сайті виробника, а не на GitHub.

**`T-K03-028`**

- де шукати (здогад, не перевірений): Операційна система Windows/Linux документує, що послідовний порт може утримуватися лише одним процесом за раз. Помилка "Device or resource busy" в довіднику підтверджує цей принцип.

**`T-46-042`**

- де шукати (здогад, не перевірений): U8g2's Wiki documentation at https://github.com/olikraus/u8g2/wiki/u8g2setupcpp describes the configuration method (whether in-library or in-project); the README references this page but the full configuration guidance is on the Wiki, not directly accessible via raw.githubusercontent


## Пакет 3

**`T-02-146`**

- де шукати (здогад, не перевірений): CPU/ISA reference manuals or ESP-IDF architecture documentation would document that Xtensa and RISC-V have different instruction sets and ABIs (affecting binary libraries and assembly), while high-level application code remains portable; the claim is a fundamental architecture principle but would need formal ISA documentation or ESP32 porting guides that detail architecture-specific binary compatibility

**`T-K03-017`**

- де шукати (здогад, не перевірений): ESP-IDF documentation for specific ESP32 variants (particularly ESP32-S3 and newer models with built-in USB) would document whether they have a separate USB-UART bridge chip and driver requirements.

**`T-04-141`**

- де шукати (здогад, не перевірений): ESP32 Technical Reference Manual Section on interrupts and the maximum interrupt source limit; ESP-IDF examples with high-frequency interrupts and their impact on task scheduling would document this behaviour.

**`T-03-015`**

- де шукати (здогад, не перевірений): ESP-IDF optimization guide or application notes would document the design pattern of separating heavy computation tasks from connectivity tasks across the two cores.

**`T-03-016`**

- де шукати (здогад, не перевірений): FreeRTOS documentation and ESP-IDF threading guide explain that single-threaded code runs on only one core, leaving the other core unused.

**`T-31-034`**

- де шукати (здогад, не перевірений): ESP-IDF documentation on task scheduling, core affinity, and timing constraints would explain why timing-critical tasks should run on core 1 away from radio operations on core 0.


## Пакет 4

**`T-31-035`**

- де шукати (здогад, не перевірений): ESP-IDF FreeRTOS task scheduling and core affinity guide would document how to assign heavy/long-running tasks to core 1 to avoid interference with network operations on core 0.

**`T-05-033`**

- де шукати (здогад, не перевірений): ESP-IDF GPIO driver API documentation (esp_gpio_set_drive_capability) or default configuration files would document the default GPIO output drive strength.

**`T-26-059`**

- де шукати (здогад, не перевірений): FreeRTOS documentation and ESP-IDF RTOS guide explain the IDLE task's role in detecting when a core is over-subscribed by checking if it receives scheduled time.

**`T-29-070`**

- де шукати (здогад, не перевірений): Driver source code (in esp-idf components or Linux kernel) documents where and how drivers reconfigure GPIO pin modes/functions and why reading hardware registers is sometimes necessary to verify.

**`T-06-036`**

- де шукати (здогад, не перевірений): ESP-IDF boot loader code or log format documentation would show what messages appear in the boot log for power supply detection.

**`T-A-123`**

- де шукати (здогад, не перевірений): Datasheets for PCF8574, MCP23017, 74HC595/165, and CD4051 confirm their I/O expansion capabilities; ESP-IDF examples or Arduino libraries document their use for extending GPIO/analog pins.


## Пакет 5

**`T-COM-016`**

- де шукати (здогад, не перевірений): ESP32-CAM board schematic and pinout documentation (available from Espressif or board manufacturer); Arduino-ESP32 board profile for ESP32-CAM that specifies the physical connectors and programming interface.

**`T-G-091`**

- де шукати (здогад, не перевірений): IEEE 802.11-2020 standard or Espressif ESP-IDF API documentation (components/esp_wifi/include/esp_wifi.h) would define RSSI and signal strength terminology formally; check the official WiFi specification or ESP-IDF header file comments.

**`T-39-065`**

- де шукати (здогад, не перевірений): Espressif ESP-IDF source code (components/esp_wifi/include/esp_wifi.h or examples/wifi/getting_started/station/) documents what RSSI represents; IEEE 802.11 standard defines it formally as Received Signal Strength Indication in dBm units.

**`T-14-012`**

- де шукати (здогад, не перевірений): Micropython repository (micropython/micropython) and its benchmarks, or detailed performance comparisons between MicroPython and C implementations on ESP32 would quantify the "tens of times slower" claim; check benchmark documentation or performance test suites.

**`T-62-052`**

- де шукати (здогад, не перевірений): Relay module datasheets and Arduino-based relay control documentation would specify voltage requirements for relay coils; motor control and relay driver IC specifications (e.g., ULN2803, SN754410) document why separate 5V supply is needed for relay coils when controlled from 3.3V logic.

**`T-06-053`**

- де шукати (здогад, не перевірений): ESP32 datasheet and Espressif power supply design guidelines document the minimum recommended power source current (1A) for stable WiFi operation; ESP-IDF power management documentation would specify TX power reduction options and core frequency scaling for peak consumption reduction.


## Пакет 6

**`T-30-053`**

- де шукати (здогад, не перевірений): ESP-IDF compiler documentation and source code (components/compiler/CMakeLists.txt or compiler options) specify automatic function inlining settings and the size threshold that triggers inlining decisions; check Kconfig compiler options for the specific threshold value.

**`T-B-072`**

- де шукати (здогад, не перевірений): ESP-IDF system power management and reset error documentation (esp-idf/components/esp_system/ or esp_hw_support/) would document rst:0xf reset code and its relationship to power supply stability and current requirements.

**`T-B-075`**

- де шукати (здогад, не перевірений): ESP-IDF WiFi component documentation (esp-idf/components/esp_wifi/) or WiFi example code would specify power supply requirements (current and capacitance) for stable WiFi operation during transmit peaks.

**`T-B-094`**

- де шукати (здогад, не перевірений): I2C bus specification from NXP (formerly Philips) or Linux kernel I2C documentation (linux/drivers/i2c/) would define the standard 4.7 kΩ pull-up resistor value for SDA and SCL lines as recommended for standard mode I2C operation.

**`T-B-161`**

- де шукати (здогад, не перевірений): ESP-IDF GPIO driver examples (esp-idf/examples/peripherals/gpio/) or relay driver documentation would demonstrate pull-down resistor sizing for controlling relay coils and preventing spurious activation at startup.

**`T-E-146`**

- де шукати (здогад, не перевірений): Soil moisture sensor datasheets and technical comparisons (found in manufacturer documentation or sensor evaluation guides on GitHub) would compare capacitive vs resistive sensor technologies and their advantages in terms of durability and lifespan.


## Пакет 7

**`T-K08-015`**

- де шукати (здогад, не перевірений): Card K13 (referenced here) would be a prior card in the handbook documenting the power-cable-capacitor troubleshooting steps; the external verification would be in the handbook's own prior sections or in ESP-IDF power management documentation.

**`T-K08-026`**

- де шукати (здогад, не перевірений): ESP-IDF GPIO and I2C driver documentation would support this troubleshooting principle that missing pull-ups or inadequate grounding cause most communication failures; Linux kernel I2C documentation would also confirm pull-up requirements.

**`T-07-082`**

- де шукати (здогад, не перевірений): ESP-IDF GPIO driver documentation (components/esp_driver_gpio/) would detail pin states: which pins support only input/output, which have no built-in pull-up/pull-down capability.

**`T-35-090`**

- де шукати (здогад, не перевірений): I2C specification (Philips I2C standard) or Linux kernel I2C documentation would specify maximum pull-up current limits for the bus; multiple pull-ups in parallel could exceed these limits and cause signal quality issues.

**`T-47-012`**

- де шукати (здогад, не перевірений): Isolation for low-power switching: Look in optocoupler/isolation IC datasheets (e.g., TLP291, PC817) and ESP-IDF examples using opto-isolators. Example directories in espressif/esp-idf under examples/ that use external isolation would settle whether isolation is considered necessary for certain power levels.

**`T-47-040`**

- де шукати (здогад, не перевірений): MOSFET gate as capacitance: Verify in MOSFET datasheets (any manufacturer - STMicroelectronics, Infineon, Texas Instruments, NXP), MOScontroller driver documentation in espressif/esp-idf components, or any CMOS/transistor theory textbook. Every MOSFET datasheet lists gate-source capacitance (Cgs) and input capacitance (Ciss) specifications.


## Пакет 8

**`T-47-042`**

- де шукати (здогад, не перевірений): Gate series resistor as safety feature: Verify in MOScontroller/gate driver datasheets (IRS2101, IR2110 etc.), MOSFET application notes, or circuit protection guidelines. ESP-IDF MCPWM documentation mentions gate resistors but omits safety rationale.

**`T-47-085`**

- де шукати (здогад, не перевірений): Voltage divider definition (two resistors): Basic circuit theory documented in any electronics textbook, circuit design guides, or ESP-IDF examples showing level shifting (5V/3.3V conversion). Examples likely in espressif/esp-idf under peripherals documentation.

**`T-47-098`**

- де шукати (здогад, не перевірений): Common mistake of connecting grounds across isolation: Optocoupler, magnetic isolator, and galvanic isolation IC datasheets (TLP291, IL217, ADUM series) document why grounds must NOT be connected when isolation is the intent. Linux CAN driver documentation (drivers/net/can/) also discusses this for isolated CAN transceivers.

**`T-47-101`**

- де шукати (здогад, не перевірений): 10 kΩ pull-down prevents load turn-on during ESP32 boot: Verify in ESP32 datasheet (startup sequence, GPIO default states), ESP-IDF bootloader documentation, or MOSFET gate pull-down design guides. The specific claim ties bootloader behavior (when GPIO pins are high-impedance) to pull-down resistor function.

**`T-37-034`**

- де шукати (здогад, не перевірений): OneWire/DS18B20 increased current draw during temperature conversion: DS18B20 datasheet (Maxim-Integrated/Analog Devices) states typical and maximum conversion current. ESP-IDF OneWire/DS18B20 driver examples or application notes from Maxim would specify pull-up resistor sizing for this peak current.

**`T-05-050`**

- де шукати (здогад, не перевірений): Voltage divider definition: Basic circuit theory documented in every electronics textbook (Horowitz & Hill, Art of Electronics), circuit analysis references, and DIY electronics resources. Confirmed in ESP-IDF level-shifting examples.


## Пакет 9

**`T-05-063`**

- де шукати (здогад, не перевірений): Pull-up resistor for defined GPIO state: Microcontroller GPIO driver documentation (esp_driver_gpio in ESP-IDF), general GPIO design guidelines, and open-collector/open-drain logic requirements. ESP32 Technical Reference Manual would specify GPIO pull-up/pull-down electrical characteristics.

**`T-05-073`**

- де шукати (здогад, не перевірений): ESP32 pins 34-39 lack built-in pull-ups: Verify in ESP32 Technical Reference Manual (pin capabilities table), ESP32 datasheet (Espressif), or esp_driver_gpio source code in espressif/esp-idf components. The pinout diagram and GPIO specifications would list which pins have internal pull-ups/pull-downs.

**`T-05-098`**

- де шукати (здогад, не перевірений): 470 μF decoupling capacitor as common power supply fix: Verify in ESP32 design guidelines, Espressif reference designs, espressif/esp-idf hardware requirements documentation, or PCB layout guidelines. The specific value 470 μF appears in many ESP32 development board schematics available in Espressif or community repositories.

**`T-05-130`**

- де шукати (здогад, не перевірений): ESP32 pins 34-39 lack built-in pull-ups (repeated claim): Same as T-05-073 - verify in ESP32 Technical Reference Manual or esp_driver_gpio documentation in espressif/esp-idf.

**`T-58-049`**

- де шукати (здогад, не перевірений): Gate resistors prevent load turn-on during boot: Same concept as T-47-101 - verify in microcontroller bootloader documentation and MOSFET gate pull-down design practices in espressif/esp-idf bootloader code or hardware guidelines.

**`T-46-073`**

- де шукати (здогад, не перевірений): Port expansion alternatives - I2C expander (PCF8574), resistive analog keyboard divider, or capacitive touch: Verify in component datasheets (PCF8574 functional description), resistive keyboard design guides, and ESP32 Touch controller documentation (esp_driver_touch_sens in ESP-IDF).


## Пакет 10

**`T-44-009`**

- де шукати (здогад, не перевірений): What to look for in a module schematic: regulator, pull-ups, level converter. Verify in typical module schematics (e.g., Adafruit breakout boards, SparkFun datasheets) or ESP32 module design guidelines. These are common components in module periphery.

**`T-COM-072`**

- де шукати (здогад, не перевірений): 10 kΩ resistors for pull-ups and gate pull-down: Typical value in GPIO design guides and MOSFET application notes. Verify in microcontroller GPIO design documents, MOSFET datasheets with gate circuit recommendations, and reference designs in espressif/esp-idf.

