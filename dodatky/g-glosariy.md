# Додаток G. Глосарій {#dod-glosariy}

Українська назва — канонічний англійський термін. Мовна політика — Р8 і
розділ 00: усталені в галузі терміни не перекладаються, бо шукати їх ви
все одно будете англійською.

## Не перекладаються

Терміни, які лишаються як є навіть в українському тексті.

| Термін | Що це |
|---|---|
| **brownout** | скидання через просідання напруги живлення |
| **watchdog** | сторожовий таймер, що перезавантажує зависле |
| **backtrace** | ланцюжок викликів у момент збою |
| **strapping** | піни, стан яких при скиданні задає режим завантаження |
| **bootloader** | програма, що завантажує наступну програму |
| **firmware** | прошивка |
| **datasheet** | документація на компонент |
| **pinout** | розводка виводів |
| **breadboard** | макетна плата без пайки |
| **pull-up / pull-down** | підтягування вгору / вниз |
| **open-drain** | вихід, що вміє лише притискати лінію до землі |
| **duty cycle** | коефіцієнт заповнення: частка періоду в активному стані |
| **deep sleep** | глибокий сон із втратою вмісту RAM |
| **coredump** | знімок стану всіх задач у момент паніки |
| **conformal coating** | захисне лакове покриття плати |
| **strain relief** | механічне закріплення кабелю проти натягу |
| **power path** | схема одночасної роботи й заряджання |
| **sensor fusion** | злиття даних кількох датчиків |
| **provisioning** | початкове передавання пристрою креденшелів мережі |

## Українська ↔ англійська

### Апаратне

| Українською | English |
|---|---|
| кристал, мікросхема | die, SoC, chip |
| модуль | module |
| плата розробки | development board |
| пін, вивід | pin |
| контактна площадка | pad |
| гребінка | pin header |
| перемичка | jumper |
| доріжка | trace |
| шина | bus |
| земля, спільна земля | ground, common ground |
| живлення | power supply |
| стабілізатор | voltage regulator |
| понижувальний перетворювач | buck converter |
| підвищувальний перетворювач | boost converter |
| дільник напруги | voltage divider |
| конвертер рівнів | level shifter |
| розв'язувальний конденсатор | decoupling capacitor |
| захисний діод | flyback diode |
| ключ (транзисторний) | switch |
| оптопара | optocoupler |
| гальванічна розв'язка | galvanic isolation |
| термоусадка | heat shrink tubing |
| оплітка для випаювання | desoldering wick |
| припій | solder |
| холодна пайка | cold joint |
| перфборд | perfboard, protoboard |
| корпус (виробу) | enclosure |
| гермоввід, сальник | cable gland |

### Програмне

| Українською | English |
|---|---|
| прошивка | firmware |
| образ | image, binary |
| збирання | build |
| тулчейн | toolchain |
| компонент | component |
| задача | task |
| планувальник | scheduler |
| пріоритет | priority |
| черга | queue |
| семафор | semaphore |
| м'ютекс | mutex |
| група подій | event group |
| переривання | interrupt |
| обробник переривання | interrupt handler, ISR |
| критична секція | critical section |
| стек | stack |
| купа | heap |
| фрагментація | fragmentation |
| витік пам'яті | memory leak |
| переповнення стека | stack overflow |
| атомарна операція | atomic operation |
| гонка | race condition |
| взаємне блокування | deadlock |
| зворотний виклик | callback |
| таблиця розділів | partition table |
| розділ | partition |
| файлова система | filesystem |
| дамп | dump |
| прапорець | flag |
| автомат станів | state machine |
| ідемпотентність | idempotence |
| відтворюване збирання | reproducible build |
| відкат | rollback |

### Радіо і мережа

| Українською | English |
|---|---|
| точка доступу | access point |
| станція, клієнт | station |
| канал | channel |
| рівень сигналу | RSSI, signal strength |
| антена | antenna |
| узгодження | matching |
| дальність | range |
| маячок | beacon |
| креденшели | credentials |
| брокер | broker |
| топік | topic |
| підписка | subscription |
| публікація | publish |
| сертифікат | certificate |
| центр сертифікації | certificate authority, CA |
| рукостискання | handshake |
| широкомовна розсилка | broadcast |
| комірчаста мережа | mesh network |
| ретрансляція | relay |

### Вимірювання і живлення

| Українською | English |
|---|---|
| напруга | voltage |
| струм | current |
| опір | resistance |
| потужність | power |
| ємність (конденсатора) | capacitance |
| ємність (акумулятора) | capacity |
| просадка | voltage drop, sag |
| пікове споживання | peak current |
| коефіцієнт заповнення | duty cycle |
| роздільність | resolution |
| точність | accuracy |
| калібрування | calibration |
| усереднення | averaging |
| шум | noise |
| завада | interference |
| шунт | shunt |
| навантаження | load |
| холостий хід | no load |

### Процес

| Українською | English |
|---|---|
| постановка задачі | requirements |
| прототип | prototype |
| доведення | hardening |
| приймальні випробування | acceptance testing |
| критерій приймання | acceptance criterion |
| паспорт виробу | device documentation |
| журнал змін | changelog |
| версіонування | versioning |
| серійна прошивка | batch flashing |
| партія | batch |
| брак | defective unit |
| супровід | maintenance |

## Скорочення

| Скорочення | Розшифровка |
|---|---|
| SoC | System on Chip |
| IDF | IoT Development Framework |
| RTOS | Real-Time Operating System |
| ISR | Interrupt Service Routine |
| DMA | Direct Memory Access |
| NVS | Non-Volatile Storage |
| OTA | Over-The-Air (оновлення) |
| ADC / DAC | Analog-to-Digital / Digital-to-Analog Converter |
| PWM | Pulse-Width Modulation |
| GPIO | General-Purpose Input/Output |
| UART | Universal Asynchronous Receiver/Transmitter |
| SPI | Serial Peripheral Interface |
| I²C | Inter-Integrated Circuit |
| I²S | Inter-IC Sound |
| TWAI | Two-Wire Automotive Interface (CAN в ESP32) |
| JTAG | Joint Test Action Group (інтерфейс налагодження) |
| LDO | Low-Dropout regulator |
| BMS | Battery Management System |
| ESD | Electrostatic Discharge |
| PSRAM | Pseudo-Static RAM |
| IRAM / DRAM | Instruction / Data RAM |
| RTC | Real-Time Clock |
| ULP | Ultra-Low-Power (співпроцесор) |
| WDT | Watchdog Timer |
| TWDT | Task Watchdog Timer |
| MTU | Maximum Transmission Unit |
| SSR | Solid-State Relay |
| THT / SMD | Through-Hole Technology / Surface-Mount Device |
| DRC | Design Rule Check |
| BOM | Bill of Materials (перелік компонентів) |

## Мовні рішення довідника

**Українська назва + англійський термін у дужках при першій згадці в
розділі:** «черги (queues)», «підтягування (pull-up)».

**Назви команд, файлів, регістрів і функцій не перекладаються** і
набираються моноширинним шрифтом: `idf.py`, `app_main`, `sdkconfig`.

**Одиниці й позначення** — за стандартом: В, А, Ом, Гц, Ф, °C.
Шістнадцяткові числа — `0x` і малі літери: `0x76`, `0x3ff`.

**`duty cycle` — це «коефіцієнт заповнення», а не «шпаруватість».** Ці
дві величини **обернені** одна до одної: коефіцієнт заповнення — це
`tі/T` (частка періоду, коли сигнал активний, від 0 до 1), а
шпаруватість — `T/tі` (у скільки разів період довший за імпульс, від 1 і
вище). Сплутати їх означає отримати обернене число, тому в довіднику
вживається лише «коефіцієнт заповнення».
