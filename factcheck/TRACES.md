# Відпрацьовані сліди класу `E`

**Генерується** `tools/leady.py --zvit`. Наряд —
`factcheck/BRIEF-LEADS.md`.

Слід (`ideya`) — це здогад попереднього помічника про те, де шукати.
Тут — що з нього вийшло, коли по ньому справді пішли.

## Результат

Відповідей: **55**.

| Вердикт | Скільки |
|---|---|
| Джерело знайдено | 10 |
| Здогад не підтвердився | 31 |
| Документ звідси недосяжний | 14 |


Із **10** заявлених `znayshov` третій шар витримали **8**. Решта — не докази: цитати за названою адресою немає.

`ne_znayshov` тут — **не** провал помічника, а спростування здогаду: документ прочитано, місця в ньому немає. Здогад ніхто не перевіряв, коли записував, тож частина їх хибна за побудовою.


## Витримали третій шар — кандидати в реєстр

Дослівність доведено машиною. **Чи підпирає цитата саме це твердження — вирішує супровідник** (шар 2), і доти жоден із них не є доказом.

| Одиниця | Джерело |
|---|---|
| `T-19-070` | [`simple_ota_example.c`](https://raw.githubusercontent.com/espressif/esp-idf/master/examples/system/ota/simple_ota_example/main/simple_ota_example.c) |
| `T-42-023` | [`esp_now.rst`](https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst) |
| `T-42-029` | [`esp_now.rst`](https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst) |
| `T-46-039` | [`README.md`](https://raw.githubusercontent.com/olikraus/u8g2/master/README.md) |
| `T-K03-017` | [`usb-serial-jtag-console.rst`](https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/usb-serial-jtag-console.rst) |
| `T-07-082` | [`gpio.h`](https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_driver_gpio/include/driver/gpio.h) |
| `T-05-073` | [`gpio.h`](https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_driver_gpio/include/driver/gpio.h) |
| `T-05-130` | [`gpio.h`](https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_driver_gpio/include/driver/gpio.h) |


## Здогади, що не підтвердилися

| Одиниця | Що дивилися |
|---|---|
| `T-11-072` | Документація ESP-IDF прочитана, але точна фраза про сотні розділів не знайдена |
| `T-50-040` | Документація про Flash Encryption прочитана, але точна фраза про незворотні механізми не знайдена |
| `T-E-094` | Документ про RS-485 відстань (MAX485/SP3485) не знайдений в доступних GitHub сховищах |
| `T-46-042` | U8g2 README згадує Wiki для деталей конфігурації, але точна фраза не знайдена в README |
| `T-04-141` | Interrupt allocation documentation found but contains no specific claim about high-frequency interrupt sources consuming core reso |
| `T-03-015` | FreeRTOS documentation discusses task creation with core affinity and scheduling but contains no exact quote about separating comp |
| `T-03-016` | FreeRTOS IDF documentation discusses dual-core SMP and task scheduling but contains no exact quote about single-threaded code util |
| `T-31-034` | Task scheduling and core affinity documentation available but contains no exact quote about timing-critical tasks running on core  |
| `T-31-035` | FreeRTOS dual-core SMP documentation available with task creation and core affinity APIs, but no exact quote about assigning heavy |
| `T-05-033` | GPIO driver API documentation found with gpio_set_drive_capability function reference but no specific quote about default drive st |
| `T-26-059` | FreeRTOS documentation discusses idle tasks and task scheduling but no exact quote about monitoring IDLE tasks to detect core over |
| `T-29-070` | GPIO driver documentation available but no specific quote about drivers reconfiguring GPIO pins and need to read hardware register |
| `T-06-036` | Bootloader code is available but boot log format documentation with power supply detection messages not found in accessible source |
| `T-G-091` | Document reviewed. Found RSSI definition as "Received signal strength indication" but not in glossary table format "рівень сигналу |
| `T-39-065` | Document reviewed. RSSI definition found but not in table format "| RSSI | Що це означає |" as claimed |
| `T-14-012` | Document reviewed. Performance comparisons exist but specific phrase "десятки разів повільніше за C" not found |
| `T-B-072` | Document reviewed. Found reset reason enum definitions, but specific rst:0xf error code not in enum values; would need boot log fo |
| `T-B-094` | Document reviewed. I2C pull-up value 4.7kΩ is industry standard but UM10204 specification itself (PDF) not accessible on raw.githu |
| `T-B-161` | Document reviewed. GPIO examples found but no specific mention of 10kΩ pull-down for relay gate control during ESP32 boot |
| `T-E-146` | Document reviewed. ADC and sensor examples available but specific claim about photoresistor vs capacitive sensor comparison not fo |
| `T-K08-015` | Зміст посилається на Card K13 (виключено за правилом 4 - книга не є джерелом для себе); документація ESP-IDF про живлення не знайд |
| `T-K08-026` | Знайдено інформацію про необхідність pull-up резисторів, але не конкретну заяву, що це найчастіша причина комунікаційних збоїв |
| `T-47-085` | Основна теорія схем - пошук відповідного джерела на raw.githubusercontent.com не дав результату |
| `T-47-101` | ESP32 datasheet та bootloader документація - не знайдені за очікуваними адресами на raw.githubusercontent.com |
| `T-05-050` | Основна теорія електроніки - текстові джерела не локалізовані на raw.githubusercontent.com |
| `T-44-009` | На raw.githubusercontent.com знайдено інформацію про модулі та їх даташі, але не знайдено конкретної цитати про те, що саме шукати |
| `T-COM-072` | На raw.githubusercontent.com не знайдено конкретної цитати, яка вказує, що 10 кОм є типовою величиною для pull-up резисторів на вх |
| `T-05-063` | Файл містить документацію про конфігурацію GPIO pull-up/pull-down резисторів, але конкретна цитата про те, що pull-up потрібен для |
| `T-05-098` | На raw.githubusercontent.com не знайдено конкретного джерела, яке рекомендує 470 мкФ конденсатор як розв'язання проблем живлення E |
| `T-58-049` | На raw.githubusercontent.com не знайдено конкретного джерела про поведінку GPIO розетів під час завантаження bootloader та потребу |
| `T-46-073` | На raw.githubusercontent.com не знайдено конкретної цитати, яка підтверджує всі три альтернативи розширення портів (PCF8574 I2C ex |

