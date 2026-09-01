# Dividing the unchecked between maintainers

> **generated** — written by `factcheck/tools/split_queue.py --naryad`; editing it by hand is wasted work

Divided by one question: **in which document does the answer lie**. ESP-IDF, esptool and the `soc/` headers are reachable from M1's container; part datasheets and electrical data are not, and that is M2's work.

| | Basket | Units | Source |
|---|---|---|---|
| **M1** | `api` | 5 | ESP-IDF calls and constants — component headers |
| **M1** | `komandy` | 27 | the esptool and idf.py command line |
| **M1** | `piny` | 7 | GPIO numbers — soc/ headers and valid-pin masks |
| **M1** | `adresy` | 0 | hexadecimal addresses and sizes |
| **M1** | `log` | 7 | lines the book promises you will see in the console |
| **M2** | `detali` | 35 | specific parts — the vendor's datasheet |
| **M2** | `elektro` | 19 | electrical quantities — datasheets and specifications |

**M1 total: 46. M2 total: 54.**

## The whole remainder, not only the strong signal

The table above divides what has a source visible in the unit's own text. That is the smaller part of the debt. Below is all of it, including what nobody will take up soon: **an entry saying "nobody, and here is why" is also a division; a silent gap is not.**

| Layer | Units | To whom | Why |
|---|---|---|---|
| `unchecked`, source visible in the text | 100 | M1 46, M2 54 | by reachability of the source |
| `unchecked`, weak signal | 1346 | **nobody** | there is no marker to divide by; waits for continuous passes |
| `no-external-signal`, estimated with a referent | ~1399 | both equally | 37% of 3780 by random sample; divided by chapter, because the source is unknown in advance |
| `named-unreachable` | 178 | M2 | their network reaches further; for M1 it is 403 by construction |

### Repairing the records we have

A separate kind of work: it adds nothing to the checked count, but without it the percentages lie. A registry that lies about itself is worse than a smaller honest one.

| What | How many | To whom |
|---|---|---|
| the quote does not match — a maintainer tidied the quote; check the book, then rewrite | 60 | both |
| source not in the cache — download it, or move to `named-unreachable` with an honest reason | 36 | M1 |
| no-external-signal on a number — "no source exists" on a claim carrying a rated value | 23 | M2 |

### `no-external-signal` divided by file — M1 1890, M2 1890

Divided by **files, not units**: two people in one file produce a merge conflict on every record. The intersection is asserted in the tool.

**M1 (45):** `00-pro-dovidnyk.md`, `05-elektronika.md`, `06-zhyvlennya.md`, `07-gpio.md`, `08-platy.md`, `10-instrumenty.md`, `12-arduino.md`, `16-boot.md`, `17-esptool.md`, `19-ota.md`, `20-bekap.md`, `22-zberezhennya-stanu.md`, `23-triazh.md`, `24-chuzha-proshyvka.md`, `28-analizator.md`, `29-symptomy.md`, `30-struktura.md`, `31-freertos.md`, `33-peryferiya-kod.md`, `37-onewire.md`, `42-espnow.md`, `44-neznayomyy-modul.md`, `46-dyspleyi.md`, `47-klyuchi.md`, `48-motory.md`, `52-montazh.md`, `53-akum.md`, `56-pasport.md`, `59-proj-monitor.md`, `60-proj-loger.md`, `63-proj-mist.md`, `a-pinouty.md`, `c-komandy.md`, `e-interfeysy.md`, `f-oflayn.md`, `g-glosariy.md`, `h-dzherela.md`, `k03-pidkl.md`, `k05-proshyvka.md`, `k11-nikoly.md`, `k12-komplekt.md`, `k14-rivni.md`, `regulatory-2026-08.md`, `ua-market-2026-08.md`, `z-pokazhchyk.md`

**M2 (46):** `01-platforma.md`, `02-chipy.md`, `03-soc.md`, `04-peryferiya.md`, `09-pidklyuchennya.md`, `11-idf.md`, `13-pio.md`, `14-shvydki-shlyakhy.md`, `15-oflayn.md`, `18-rozdily-fleshu.md`, `21-seriyna.md`, `25-log.md`, `26-zboyi.md`, `27-jtag.md`, `32-nadiynist.md`, `34-uart.md`, `35-i2c.md`, `36-spi.md`, `38-can.md`, `39-wifi.md`, `40-merezha.md`, `41-ble.md`, `43-lora.md`, `45-sensory.md`, `49-kamera.md`, `50-bezpeka.md`, `51-payannya.md`, `54-korpus.md`, `55-polova-diagnostyka.md`, `57-vid-zadachi.md`, `58-dovedennya.md`, `61-proj-kanal.md`, `62-proj-keruvannya.md`, `b-symptomy.md`, `components-2026-08.md`, `d-panik.md`, `k01-triazh.md`, `k02-stan.md`, `k04-boot.md`, `k06-bootlog.md`, `k07-panika.md`, `k08-symptomy.md`, `k09-pinouty.md`, `k10-komandy.md`, `k13-zhyvlennya.md`, `k15-seriyna.md`

### Why this status is divided by chapter, not by source

Because the source there is **unknown in advance** — that is the whole point of the status. Reachability can only divide what you already know the location of. So it is divided by ranges of chapters: the only division that guarantees two people will not take the same unit.


## M1 · `api` — 5

Esp-idf calls and constants — component headers.


### `manual/25-log.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-25-077` | 173 | `ESP_LOGI(TAG, "стан: ОЧІКУВАННЯ → РОБОТА, причина: тиск %d", p)` каже все. |

### `manual/31-freertos.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-31-010` | 35 | Функція, що дійшла до кінця й вийшла, викликає паніку — задачу треба або зациклити, або явно видалити через `vTaskDelete(NULL)`. |
| `T-31-064` | 191 | Що не можна робити в ISR: викликати `printf` і `ESP_LOGx`, виділяти пам'ять, брати м'ютекси, викликати блокувальні функції, чекати. |

### `manual/59-proj-monitor.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-59-131` | 412 | `ESP_ERROR_CHECK` тут стоїть лише навколо NVS і створення шини — того, без чого пристрій не має сенсу. |

### `manual/62-proj-keruvannya.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-62-133` | 292 | Найгірший варіант — **не думати про це**: тоді поведінка визначається випадковим місцем у коді, де мережевий виклик заблокувався або `ESP_ERROR_CHECK` |

## M1 · `komandy` — 27

The esptool and idf.py command line.


### `dodatky/d-panik.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-D-102` | 130 | Друкує він її в **boot-лог по UART** (приклад одразу нижче), тобто видно її в моніторі: `idf.py monitor`, `screen`, `picocom`. |

### `dodatky/g-glosariy.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-G-171` | 210 | **Назви команд, файлів, регістрів і функцій не перекладаються** і набираються моноширинним шрифтом: `idf.py`, `app_main`, `sdkconfig`. |

### `inserts/components-2026-08.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-COM-080` | 89 | \| Менша флеш \| `flash-id` показує менше за заявлене \| |

### `kartky/k01-triazh.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-K01-033` | 56 | Якщо `esptool` не бачить чип — це ще не вирок платі. |

### `kartky/k05-proshyvka.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-K05-039` | 69 | Після `write-flash` початкового вмісту вже немає. |

### `kartky/k15-seriyna.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-K15-007` | 27 | ☐ · Чим → `write-flash -z 0x0 vyrib-v1.4.bin` |

### `manual/00-pro-dovidnyk.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-00-095` | 230 | Назви команд, файлів, регістрів і функцій ніколи не перекладаються і набрані моноширинним шрифтом: `idf.py`, `app_main`, `sdkconfig`. |

### `manual/11-idf.md` — 5

| Claim | Line | Verbatim |
|---|---|---|
| `T-11-010` | 22 | **Інструменти** — `idf.py`, `esptool`, монітор, менеджер компонентів. |
| `T-11-024` | 58 | Забути її — найчастіша причина «команду `idf.py` не знайдено». |
| `T-11-058` | 138 | \| `idf.py erase-flash` \| стерти (⚠ спершу дамп, картка К2) \| |
| `T-11-093` | 233 | Офіційне розширення від Espressif робить те саме, що `idf.py`, тільки кнопками, і додає інтеграцію з відлагоджувачем. |
| `T-11-100` | 254 | Червоні підкреслення при успішному `idf.py build` — це проблема редактора, а не коду. |

### `manual/17-esptool.md` — 3

| Claim | Line | Verbatim |
|---|---|---|
| `T-17-036` | 85 | У жодного чипа сімейства ESP32 його немає, і `esptool` на ньому відповідає попередженням: |
| `T-17-084` | 196 | `write-flash` і так перезаписує те, що записує; стирати все заради оновлення застосунку — зайвий ризик. |
| `T-17-157` | 357 | Практично: підготувати `merge-bin`-образ, налаштувати один раз, зберегти конфігурацію і передати разом з інструкцією на одну сторінку (розділ 56). |

### `manual/19-ota.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-19-085` | 187 | Найчастіше на сервері лежить не той файл: `merge-bin`-образ або повний дамп замість `app.bin`. |

### `manual/20-bekap.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-20-015` | 32 | Спільне в усьому переліку: доки чип відповідає `esptool` шапкою з'єднання, він живий. |

### `manual/21-seriyna.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-21-045` | 108 | Однаковий для всієї партії, з `merge-bin`. |
| `T-21-094` | 198 | `merge-bin` — один файл, одна адреса, нема чого переплутати. |

### `manual/22-zberezhennya-stanu.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-22-049` | 110 | Дамп, знятий після `erase-flash` або після перепрошивки, не має сенсу: він фіксує вже змінений стан. |

### `manual/23-triazh.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-23-030` | 51 | Переходьте до кроку 4: `esptool` назве сімейство сам, щойно під'єднається. |
| `T-23-052` | 104 | Шапка з'єднання, яку `esptool` друкує перед будь-якою командою, називає сімейство, ревізію кремнію і MAC (розділ 17). |

### `manual/25-log.md` — 3

| Claim | Line | Verbatim |
|---|---|---|
| `T-25-006` | 18 | `idf.py monitor` · Коли він → працюєте зі своїм проєктом ESP-IDF |
| `T-25-039` | 76 | Ключа командного рядка для цього в `idf.py monitor` **немає**: його параметри — `--print-filter`, `--monitor-baud`, `--encrypted`, `--no-reset`, `--ti |
| `T-25-040` | 81 | Прапорець `--save-log` існує в **самостійному пакеті** `esp-idf-monitor`, але `idf.py` його не передає. |

### `manual/29-symptomy.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-29-023` | 58 | Команда, скопійована з чужої інструкції, кладе бутлоадер у порожнє місце, і `esptool` не має підстав скаржитися. |
| `T-29-024` | 62 | **Залито не той файл.** Для OTA потрібен `app.bin`, а не `merge-bin`-образ; для повної прошивки — навпаки. |

## M1 · `piny` — 7

Gpio numbers — soc/ headers and valid-pin masks.


### `kartky/k02-stan.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-K02-009` | 18 | Не «синій до плати», а: `синій → GPIO4`, `червоний → 3V3`, `чорний → GND`. |

### `kartky/k04-boot.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-K04-020` | 55 | [[classic]] На платах ESP32-CAM кнопки `BOOT` немає взагалі: `GPIO0` з'єднується з `GND` перемичкою на самій платі. |

### `manual/07-gpio.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-07-026` | 40 | Перевірка коштує нуль: зняти обв'язку з `GPIO15` і скинути. |

### `manual/22-zberezhennya-stanu.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-22-032` | 71 | Кнопка на `GPIO0` пояснює, чому пристрій іноді не стартує (розділ 16), і без запису це б довелося шукати годинами. |

### `manual/49-kamera.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-49-024` | 71 | - **немає USB-роз'єму** — потрібен окремий USB-UART-перехідник; - `GPIO0` замикається на землю **перемичкою вручну** для входу в download mode (картка |

### `manual/60-proj-loger.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-60-036` | 49 | I²C `SDA` / `SCL` · classic → `GPIO21` / `GPIO22` |
| `T-60-079` | 167 | Вільних більше немає, а `GPIO2` тут працює **лише як вихід** і лише після старту, тож на завантаження не впливає (розділ 07). |

## M1 · `log` — 7

Lines the book promises you will see in the console.


### `manual/24-chuzha-proshyvka.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-24-027` | 56 | **Тексти повідомлень.** `Failed to connect to broker`, `Calibration required` — прямо називають, що пристрій робить і на що скаржиться. |

### `manual/26-zboyi.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-26-100` | 225 | Вмикається в `menuconfig`: `Core dump` → призначення `Flash`. |

### `manual/38-can.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-38-073` | 178 | Якщо документації немає — перебрати стандартні значення в режимі `LISTEN_ONLY`, доки не з'являться коректні пакети. 2. |
| `T-38-074` | 181 | **Слухати в `LISTEN_ONLY`** і записати, які ідентифікатори ходять і як часто. 3. |

### `manual/39-wifi.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-39-036` | 85 | Правильний спосіб дочекатися — група подій FreeRTOS (розділ 31), яку встановлює обробник `IP_EVENT_STA_GOT_IP`. |

### `manual/40-merezha.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-40-019` | 42 | Розмір стека сервера задається в `HTTPD_DEFAULT_CONFIG` і його часто доводиться збільшувати. |

### `manual/46-dyspleyi.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-46-025` | 19 | `RGB565` стоїть у таблиці тому, що його дають типово `TFT_eSPI` і `LovyanGFX`: удвічі менше байтів на піксель — удвічі швидший кадр. |

## M2 · `detali` — 35

Specific parts — the vendor's datasheet.


### `dodatky/e-interfeysy.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-E-008` | 13 | BME280 · Бібліотека → реєстр IDF; Adafruit BME280 |
| `T-E-011` | 14 | BMP280 · Бібліотека → Adafruit BMP280 |

### `dodatky/z-pokazhchyk.md` — 5

| Claim | Line | Verbatim |
|---|---|---|
| `T-Z-023` | 90 | BME280 — 105–107, 215, 257, 259, 261, 264, 325–326, 328, 332, 334, 336, 340, 386, 402 |
| `T-Z-026` | 105 | CH340 — 11, 25, 79, 83, 87, 114, 180, 366, 391 |
| `T-Z-027` | 111 | CH9102 — 11, 14, 29, 79, 83, 87, 114, 121, 180, 366, 391 |
| `T-Z-040` | 160 | DS18B20 — 149, 223, 261, 264, 310–311, 333–334, 336, 340, 369, 388, 402 |
| `T-Z-041` | 164 | DS3231 — 334, 336, 340, 386 |

### `inserts/components-2026-08.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-COM-018` | 27 | DHT11, DHT22 · Беріть → **BME280** або SHT3x |

### `manual/01-platforma.md` — 11

| Claim | Line | Verbatim |
|---|---|---|
| `T-01-029` | 68 | Якщо вам потрібна гарантована реакція за фіксовані мікросекунди — беріть STM32 або окремий чип на критичну частину. |
| `T-01-040` | 91 | Радіо на борту · STM32 → ні (крім WB/WL) |
| `T-01-050` | 93 | RAM · STM32 → десятки–сотні КБ |
| `T-01-055` | 94 | ОС · STM32 → немає або RTOS |
| `T-01-060` | 95 | Старт · STM32 → миттєво |
| `T-01-065` | 96 | Сон · STM32 → мкА |
| `T-01-070` | 97 | Реальний час · STM32 → **дуже добре** |
| `T-01-075` | 98 | Ціна плати · STM32 → середня |
| `T-01-080` | 106 | **Проти STM32.** STM32 кращий у реальному часі, у різноманітті периферії і в промисловій доступності на роки вперед. |
| `T-01-082` | 108 | Часто правильна відповідь — обидва: STM32 керує процесом, ESP32 стоїть збоку і забезпечує зв'язок (розділ 57). |
| `T-01-083` | 112 | **Проти RP2040.** RP2040 має PIO — програмовані блоки вводу-виводу, які роблять неможливе можливим у нестандартних протоколах. |

### `manual/04-peryferiya.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-04-142` | 173 | Практичний вихід, коли пінів не вистачає: розширювачі портів по I²C (PCF8574, MCP23017), зсувні регістри по SPI, або перенесення частини задачі на дру |

### `manual/13-pio.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-13-060` | 186 | **Бібліотека не знаходиться.** Ім'я в `lib_deps` має точно відповідати реєстру, разом з іменем автора: `adafruit/Adafruit BME280 Library`, а не просто |

### `manual/32-nadiynist.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-32-076` | 184 | Задача, де потрібне й те, й те, природно ділиться між двома чипами: STM32 тримає таймінги, ESP32 стоїть збоку і забезпечує зв'язок (розділ 01). |

### `manual/37-onewire.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-37-012` | 33 | Ринок наповнений підробками DS18B20. |
| `T-37-022` | 57 | Даташит DS18B20 видавав Maxim, потім права перейшли до Analog Devices, і пізніші ревізії могли додати проміжні східці похибки. |

### `manual/44-neznayomyy-modul.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-44-064` | 127 | **Знайти бібліотеку для іншої платформи.** Код для Arduino AVR, STM32 чи Raspberry Pi показує послідовність команд — а це і є найцінніше. |

### `manual/45-sensory.md` — 3

| Claim | Line | Verbatim |
|---|---|---|
| `T-45-004` | 12 | Чесна оцінка: **DHT22 гірший за BME280 і SHT3x майже за всіма параметрами**, а коштує не набагато менше. |
| `T-45-009` | 24 | **BME280** — тиск, температура, вологість, I²C або SPI. |
| `T-45-079` | 194 | DHT22 гірший за BME280 майже в усьому; для нового проєкту вибір інший. |

### `manual/59-proj-monitor.md` — 3

| Claim | Line | Verbatim |
|---|---|---|
| `T-59-004` | 11 | **Вхід:** BME280 по I²C — температура, вологість, тиск. |
| `T-59-014` | 34 | BME280, модуль I²C · Кількість → 1 |
| `T-59-139` | 431 | У лозі — `BME280 знайдено і налаштовано`. |

### `manual/60-proj-loger.md` — 4

| Claim | Line | Verbatim |
|---|---|---|
| `T-60-012` | 30 | BME280 · Кількість → 1 |
| `T-60-013` | 30 | BME280 · Примітка → I²C |
| `T-60-014` | 31 | DS18B20 у зонді · Кількість → 1 |
| `T-60-112` | 300 | **Живлення периферії вмикається ключем.** Модуль microSD, BME280 і RTC споживають уві сні — разом це можуть бути мілі-, а не мікроампери. |

## M2 · `elektro` — 19

Electrical quantities — datasheets and specifications.


### `inserts/components-2026-08.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-COM-087` | 98 | Поріг 0.5 °C бракував би чесний товар. |

### `manual/05-elektronika.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-05-044` | 101 | Туди 5 В подавати можна і треба. |
| `T-05-047` | 110 | **ESP32 → пристрій на 5 В.** Часто працює без нічого: більшість 5-вольтових входів сприймає 3.3 В як одиницю. |

### `manual/20-bekap.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-20-026` | 62 | Поза цими двома — фізичні пошкодження: спалений пін (5 В на GPIO), вигорілий стабілізатор, відірваний роз'єм, пробитий ESD-розрядом вхід. |

### `manual/23-triazh.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-23-045` | 87 | Обмеження на рівні 200–300 мА зупинить струм при замиканні замість того, щоб випалювати доріжку. |

### `manual/29-symptomy.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-29-076` | 188 | Подати 5 В на `3V3` означає подати їх напряму в чип. |

### `manual/34-uart.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-34-028` | 65 | **Різні логічні рівні.** Пристрій на 5 В подає 5 В на вхід ESP32 (розділ 47). |

### `manual/37-onewire.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-37-020` | 50 | Сто градусів лежать за межами вузького діапазону, там діє ±2 °C, і два справні датчики законно розійдуться **до 4 °C** — тобто перевірка почне бракува |

### `manual/44-neznayomyy-modul.md` — 5

| Claim | Line | Verbatim |
|---|---|---|
| `T-44-012` | 25 | Багато модулів мають на платі власний стабілізатор і підписані `VCC 5 В`. |
| `T-44-019` | 35 | Є стабілізатор і конвертер рівнів · Живлення → 5 В |
| `T-44-020` | 35 | Є стабілізатор і конвертер рівнів · Логічні рівні на виводах → 5 В — потрібен конвертер |
| `T-44-078` | 160 | **Рівні** — чи не подано 5 В на GPIO; чи сприймає модуль 3.3 В. 4. |
| `T-44-079` | 161 | **Підтягування** для I²C — 3.3 В на лініях у спокої (розділ 35). 5. |

### `manual/46-dyspleyi.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-46-037` | 53 | Логічні рівні перевіряти обов'язково (розділ 44): частина модулів дисплеїв розрахована на 5 В, частина на 3.3 В, і зустрічаються обидві. |

### `manual/49-kamera.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-49-028` | 83 | Живити треба від окремого джерела на 5 В через пін `5V`, а не від перехідника. |

### `manual/53-akum.md` — 2

| Claim | Line | Verbatim |
|---|---|---|
| `T-53-038` | 102 | Для звичайного LDO це означає, що при 3.5 В на акумуляторі виходу вже немає — тобто половина ємності недоступна. |
| `T-53-043` | 113 | Це єдиний спосіб використати ємність акумулятора **повністю**, до 3.0 В. |

### `manual/55-polova-diagnostyka.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-55-041` | 85 | Причина — 5 В або статика (розділ 05). |

### `manual/61-proj-kanal.md` — 1

| Claim | Line | Verbatim |
|---|---|---|
| `T-61-014` | 31 | Заряд на цикл · ESP-NOW → **~5 мА·с** |
