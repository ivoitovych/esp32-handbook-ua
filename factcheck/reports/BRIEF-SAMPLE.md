# Order: a random sample of `unchecked` — not yet checked

> **generated** — `factcheck/tools/sample.py`; editing it by hand is
> wasted work

Seed **20260901**; **200** units drawn from a population of
**1742**.

## What these units are

`unchecked` means "not yet checked". Not "doubtful": nobody simply got to
these lines.

## The rule that matters more than the verdict

**Every answer must name the document you looked at.** Every one —
including those where nothing was found.

The reason is simple: without that, "not found" costs nothing, and it gets
written without opening anything. Such a record is neither a finding nor
evidence of the absence of one, and `factcheck/tools/measure_f.py`
discards it as "did not look" before the counting begins.

> The order does not say which answer it expects. It says what every
> answer must produce.

The list of verdicts and what each requires is below, in the task blocks.
It is deliberately absent here: **no generator writes its own copy of
these rules**, and such a copy is exactly what used to stand here — with
verdict names the gate no longer accepts.

`source` always begins with `https://raw.githubusercontent.com/`.

**An address pointing at the handbook itself** is rejected mechanically:
a handbook is not a source for itself. The book's text quoted below is
what is being **checked**, not what it is checked against.

## How to search

For each unit: choose the document this ought to be in, download it with
`curl`, look. Then a verdict from the table above.

Only `raw.githubusercontent.com` is reachable. Everything else answers
403; **do not repeat a request that returned 403**.


Where to look:
`espressif/esp-idf` (`docs/en/…`, `components/…`, `examples/…`),
`espressif/esptool`, `espressif/arduino-esp32`, `torvalds/linux`
(`drivers/…`), `esphome/esphome`, `micropython/micropython`,
`adafruit/*`, `jgromes/RadioLib`, `olikraus/u8g2`, `Bodmer/TFT_eSPI`,
`lvgl/lvgl`.

Separately: `espressif.com` returns, for some addresses, an **HTML
stub of 15 495 bytes with status 200**. The response is "successful"
and the document is absent. It does not look like a document —
`nedosyazhne`.


## Prohibitions

In full — `METHOD.md` Part V; the most important are below, in the task
blocks, and are not repeated here.

## On `disputes`

The most valuable answer: the book can still be corrected. But only when
you **see a different text**, not when you remember otherwise.

This is a printed field handbook. Its reader has no network and no time
to check anything. Our job is to put every factual claim in it beside an
external document that supports it — and to record where we looked.

Your answer does not go into the book. It goes through three layers:

1. **Mechanical.** An address pointing at the handbook itself is
   rejected. A verdict with no source is rejected as "did not look".
2. **Literal.** Every `quote` is searched for **as a substring** in the
   document you named — we fetch it again and check. Spaces and quote
   marks do not count; words, numbers and capitals do.
3. **Human.** A maintainer reads the extract and judges whether it
   actually supports the claim.

Layer 2 is not a formality. In one earlier wave, of **528** claimed
confirmations only **235** survived it. The other 293 died as
paraphrase, as fragments glued across an ellipsis, or as a correct fact
with the wrong file's address.

Everything in `quote` is checked as a substring of the document. A
retelling does not pass. Neither does a line you assembled by hand from
a table, nor two sentences joined across an ellipsis.

**Knowing the answer is not grounds for writing a quote.** If the fact is
familiar but you cannot see the line in the document, that is
`not_found`.

**Paste the line with its markup. Do not clean it up.** This is the one
that costs most, because it does not feel like an error. The document
says

    Print registers and reboot (``CONFIG_ESP_SYSTEM_PANIC_PRINT_REBOOT``) — default option

and the tidy version — `Print registers and reboot — default option` —
is the same fact, reads better, and **fails**. So does dropping a
`:doc:` role, a trailing underscore on a link, or the brackets around an
option name. Measured over 200 tickets: of the confirmations that
failed, 13 of 14 had found the right passage and lost it in the copying.

Copy the characters that are there — backticks, colons, brackets,
underscores and all. If two useful sentences are not adjacent, send two
entries or one entry and say so; do not join them.

It is not a failure and not a lesser result. It records where we have
already looked, and those records are what let us print a sentence at
all.

A quote from an almost-right source is worse than no quote. Invented
support does not go unnoticed — layer 2 discards it and the unit returns
to the queue — so guessing is cheaper than reading only inside your own
answer. Past that boundary it costs everyone, and you most: your work
disappears entirely.

Only `raw.githubusercontent.com`, via `curl`. Everything else answers
`403` — this is an organisation-level policy, not your doing and not
ours. Chip datasheets are not on GitHub, and that is nobody's fault.

**Do not repeat a request that returned 403.**

Some `espressif.com` addresses return an **HTML placeholder of about
15 500 bytes with status 200**. The request "succeeds" and there is no
document. If what came back does not look like the document you asked
for, the verdict is `unreachable`.

| Verdict | When |
|---|---|
| `confirmed` | address plus a **verbatim** quote from the document |
| `not_found` | the document exists, the passage is not in it — say what you read |
| `unreachable` | the document does not come down from here (403, 404, stub) |
| `advice` | you did not get the document, but can name where it would be |
| `disputes` | the source **contradicts** the handbook — the most valuable answer there is |

An address inside this repository, or a chapter of the handbook cited as
the source for a claim in the handbook, is rejected mechanically. If a
claim is supported only by another part of the book, say so plainly —
there is a class for it, and it is not a failure.

Every answer that names a source must also name **where in it** — the
section heading, the line, the table, the register name. Add a `where:`
field beside `source:`.

    where: "section 6.2.1, Recommended Operating Conditions"
    where: "line defining SOC_UART_NUM"

Why this is required here. Normally the count of tool calls tells honest
work from rubber-stamping: an honest wave makes 66–89 calls for 25–30
units, a broken one 14–18 for 25. This order lets you fetch documents in
bulk before you begin, which is sensible and which **removes that
signal** — every batch then looks like one download and twenty answers.

`where:` replaces it. Twenty units judged honestly against one document
produce twenty different locations in it. Twenty rubber-stamped produce
one, or none.

A location you cannot give is itself an answer: write the honest verdict
instead. `where:` is not a field to fill in — it is the evidence that you
looked.

Fetch whatever documents you expect to need first, in one go. Then make
**two passes**.

**First pass, over all twenty units.** For each, decide whether it can be
settled from what you already hold. If it can, settle it now and write
the entry in full — with `source:`, `where:` and a verbatim `quote:`,
exactly as any other answer. If it cannot, mark it for the second pass
and write nothing else.

A unit "settled quickly" is held to the same standard as any other. There
is no lighter verdict for an easy unit, and marking something easy is not
an answer.

**Second pass, over what remains.** Take those units one at a time and go
deeper: other documents, other sections, the source of the code rather
than its documentation.

Report both passes: in `comment:`, say which pass settled the unit.

```yaml
- unit: T-42-023
  verdict: confirmed
  source: https://raw.githubusercontent.com/espressif/esp-idf/master/...
  quote: |
    the verbatim line from the document
  comment: one sentence, optional
```

One entry per unit. Do not reorder or renumber the units. If you have
nothing for a unit, still write an entry with the honest verdict — a
missing entry is indistinguishable from work not done.

**YAML:** if a value contains `: ` or starts with a quote mark, wrap the
whole value in single quotes. Otherwise the file will not parse and the
whole batch is lost, not just that entry.

---

*Task spec `8f43ffc2` · blocks: ORIENTATION, VERBATIM, HONEST-MISS, NETWORK, STUB, VERDICTS-EXTERNAL, NO-SELF-REFERENCE, LOCATION, STRATEGY-TRIAGE, FORMAT. Quote this version when reporting results from this wave.*


## Batch 1

**`T-00-031`** · `manual/00-pro-dovidnyk.md:67`

> Тому клас `E` перевіряється **окремо і навмисно**: із нього беруть випадкову вибірку — випадкову, щоб відсоток можна було перенести на всі одиниці, — і питають по кожній, чи існує документ, за яким її можна звірити.

**`T-00-079`** · `manual/00-pro-dovidnyk.md:187`

> Там, де правило стосується інших сімейств, позначка називає і їх: [[S2]], [[C6]], [[H2]].

**`T-01-017`** · `manual/01-platforma.md:42`

> **Радіо на кристалі.** Wi-Fi і Bluetooth без зовнішніх мікросхем.

**`T-01-081`** · `manual/01-platforma.md:107`

> ESP32 кращий у радіо і в швидкості початку роботи.

**`T-01-082`** · `manual/01-platforma.md:108`

> Часто правильна відповідь — обидва: STM32 керує процесом, ESP32 стоїть збоку і забезпечує зв'язок (розділ 57).

**`T-01-083`** · `manual/01-platforma.md:112`

> **Проти RP2040.** RP2040 має PIO — програмовані блоки вводу-виводу, які роблять неможливе можливим у нестандартних протоколах.

**`T-01-093`** · `manual/01-platforma.md:135`

> ESP32 підключений до нього по UART або CAN і відповідає лише за зв'язок: віддає телеметрію, приймає команди, оновлює себе по повітрю.

**`T-02-150`** · `manual/02-chipy.md:211`

> Для нового проєкту типова відповідь — S3; для навчання — classic; для дешевого вузла — C3, якщо 400 КБ вистачає.

**`T-04-001`** · `manual/04-peryferiya.md:3`

> Периферія — це апаратні блоки всередині чипа, які роблять роботу без участі процесора: передають байти по UART, генерують імпульси PWM, міряють напругу.

**`T-04-005`** · `manual/04-peryferiya.md:12`

> Найважливіша архітектурна особливість ESP32, і вона суттєво відрізняє його від класичних мікроконтролерів.

**`T-04-072`** · `manual/04-peryferiya.md:115`

> UART · C6 → 2 + 1 LP

**`T-04-076`** · `manual/04-peryferiya.md:116`

> I²C · S3 → 2

**`T-04-099`** · `manual/04-peryferiya.md:120`

> TWAI (CAN) · S2 → 1

**`T-04-108`** · `manual/04-peryferiya.md:121`

> DAC · C6 → ні

**`T-04-112`** · `manual/04-peryferiya.md:122`

> Touch · S3 → 14

**`T-04-115`** · `manual/04-peryferiya.md:122`

> Touch · H2 → ні

**`T-04-120`** · `manual/04-peryferiya.md:123`

> USB · C6 → JTAG

**`T-05-044`** · `manual/05-elektronika.md:101`

> Туди 5 В подавати можна і треба.

**`T-06-015`** · `manual/06-zhyvlennya.md:30`

> Помилка трапляється частіше, ніж здається: на гребінці піни `5V` і `3V3` часто стоять поруч, підписані дрібно, а Dupont-роз'єм легко зсунути на один контакт.

**`T-06-022`** · `manual/06-zhyvlennya.md:46`

> | Активний, Wi-Fi у роботі | близько сотні мА середнє |


## Batch 2

**`T-06-042`** · `manual/06-zhyvlennya.md:95`

> Кабель USB — тонкий, довгий, дешевий.

**`T-06-096`** · `manual/06-zhyvlennya.md:204`

> Розрахунок майже завжди виявляється оптимістичним, і головний винуватець — **час під'єднання до Wi-Fi**.

**`T-06-120`** · `manual/06-zhyvlennya.md:255`

> **Buck** (понижувальний імпульсний) — ефективність 85–95 %.

**`T-07-113`** · `manual/07-gpio.md:243`

> Лишається близько **20 повноцінних** пінів, з яких п'ять — strapping і потребують уваги.

**`T-08-008`** · `manual/08-platy.md:15`

> `ESP32-WROOM-32D`, `-32E` · Чип → classic

**`T-09-073`** · `manual/09-pidklyuchennya.md:136`

> Спокуса запустити прошивку через `sudo` дуже велика, і вона працює — один раз.

**`T-10-020`** · `manual/10-instrumenty.md:43`

> **USB-хаб із власним живленням.** Знімає навантаження з порту ноутбука і рятує сам порт при замиканні на платі.

**`T-10-037`** · `manual/10-instrumenty.md:81`

> **JTAG-адаптер.** [[classic]] Потрібен лише для classic; на S3 і C3 вбудований (розділ 27).

**`T-11-033`** · `manual/11-idf.md:89`

> | Період | Тривалість | Для нового проєкту |

**`T-11-099`** · `manual/11-idf.md:252`

> Причина зазвичай у тому, що конфігурація розширення вказує на іншу версію ESP-IDF, ніж та, якою збирається проєкт.

**`T-11-114`** · `manual/11-idf.md:292`

> Клавіша `/` у `menuconfig`.

**`T-12-014`** · `manual/12-arduino.md:42`

> Саме так робиться доступ до тих блоків периферії, яких немає в Arduino API: MCPWM, PCNT, TWAI, тонке керування живленням.

**`T-12-056`** · `manual/12-arduino.md:149`

> | Потрібні MCPWM, PCNT, TWAI | ESP-IDF або виклики IDF зі скетча |

**`T-13-009`** · `manual/13-pio.md:23`

> - працюєте з **Arduino 2.x** і старим кодом → офіційна платформа працює; - потрібен **Arduino 3.x**, S3, C3, C6 або новіші → **pioarduino**.

**`T-13-072`** · `manual/13-pio.md:212`

> Офіційна платформа PlatformIO відстала від Arduino core; спільнотний форк pioarduino підтримує актуальні версії.

**`T-14-024`** · `manual/14-shvydki-shlyakhy.md:79`

> OTA, веб-інтерфейс, відновлення зв'язку, інтеграція з системами домашньої автоматизації — усе вже є.

**`T-14-059`** · `manual/14-shvydki-shlyakhy.md:137`

> OTA з коробки · MicroPython → ні

**`T-14-077`** · `manual/14-shvydki-shlyakhy.md:168`

> ESPHome дає працюючий датчик із OTA за десять хвилин без коду і добре працює як спосіб довести, що залізо зібране правильно.

**`T-15-017`** · `manual/15-oflayn.md:18`

> Жорсткі вимоги до пам'яті чи таймінгів · Тулчейн → ESP-IDF

**`T-15-029`** · `manual/15-oflayn.md:39`

> Код при цьому лишається тим самим — `setup`/`loop` і бібліотеки Arduino продовжують працювати (розділ 12).


## Batch 3

**`T-15-031`** · `manual/15-oflayn.md:44`

> Решта може лишатися на Arduino API як завгодно довго.

**`T-16-058`** · `manual/16-boot.md:136`

> Скинути плату кнопкою `EN`.

**`T-16-085`** · `manual/16-boot.md:215`

> Від подачі живлення до `app_main` — типово десятки мілісекунд.

**`T-17-036`** · `manual/17-esptool.md:85`

> У жодного чипа сімейства ESP32 його немає, і `esptool` на ньому відповідає попередженням:

**`T-17-065`** · `manual/17-esptool.md:154`

> Сенс він має лише разом із `--no-stub`, де стиснення типово вимкнене — а це саме той випадок із клонами, який розібрано нижче.

**`T-17-132`** · `manual/17-esptool.md:307`

> **`Invalid head of packet (0x00)`**

**`T-17-157`** · `manual/17-esptool.md:357`

> Практично: підготувати `merge-bin`-образ, налаштувати один раз, зберегти конфігурацію і передати разом з інструкцією на одну сторінку (розділ 56).

**`T-18-060`** · `manual/18-rozdily-fleshu.md:120`

> У прошивці, що йде в поле, цей код спрацює саме тоді, коли NVS переповнився — тобто несподівано, у роботі.

**`T-19-030`** · `manual/19-ota.md:53`

> Пристрій, залитий з однією `factory` без слотів OTA, неможливо перевести на OTA дистанційно: для цього потрібна повна перепрошивка з фізичним доступом.

**`T-19-031`** · `manual/19-ota.md:57`

> Практично: якщо є хоч найменша ймовірність, що виріб доведеться оновлювати в полі, — OTA-розбивка ставиться одразу, навіть якщо сама функція поки не написана.

**`T-19-061`** · `manual/19-ota.md:131`

> Він потрібен тоді, коли під час завантаження треба годувати watchdog, малювати смужку прогресу або мати можливість скасувати.

**`T-19-075`** · `manual/19-ota.md:166`

> **ArduinoOTA.** Оновлення з середовища Arduino по локальній мережі: плата з'являється як мережевий порт.

**`T-20-015`** · `manual/20-bekap.md:32`

> Спільне в усьому переліку: доки чип відповідає `esptool` шапкою з'єднання, він живий.

**`T-20-018`** · `manual/20-bekap.md:42`

> Що можна втратити помилковим записом: доступ по JTAG, можливість увійти в download mode, можливість прошивати чип узагалі, здатність читати флеш поза цим конкретним чипом.

**`T-20-021`** · `manual/20-bekap.md:52`

> **Flash Encryption і Secure Boot у release-режимі.** Це односторонні двері, реалізовані через ті самі eFuse.

**`T-20-062`** · `manual/20-bekap.md:134`

> - `rst:0x7`, `rst:0x8`, `rst:0x9` (watchdog) → щось не віддає керування.

**`T-20-084`** · `manual/20-bekap.md:179`

> **Живлення від окремого джерела**, а не від USB-порту ноутбука через хаб.

**`T-21-006`** · `manual/21-seriyna.md:17`

> Якщо проєкт ESP-IDF під рукою — цим і обмежтеся, бо адреси підставить сама збірка:

**`T-21-066`** · `manual/21-seriyna.md:153`

> 0041 · Версія → v1.4

**`T-21-074`** · `manual/21-seriyna.md:155`

> 0043 · MAC → `A0:B7:…:31`


## Batch 4

**`T-22-049`** · `manual/22-zberezhennya-stanu.md:110`

> Дамп, знятий після `erase-flash` або після перепрошивки, не має сенсу: він фіксує вже змінений стан.

**`T-23-014`** · `manual/23-triazh.md:24`

> `ESP32-WROVER`, `-B`, `-E` · Чип → ESP32 classic

**`T-23-017`** · `manual/23-triazh.md:25`

> `ESP32-S3-WROOM-1` · Що це значить практично → двоядерний, native USB

**`T-23-030`** · `manual/23-triazh.md:51`

> Переходьте до кроку 4: `esptool` назве сімейство сам, щойно під'єднається.

**`T-23-033`** · `manual/23-triazh.md:59`

> - цілий USB-роз'єм, не хитається, площадки не відірвані; - стабілізатор не здутий, без темних плям і запаху; - немає перемичок припою між сусідніми пінами; - немає слідів води, окислення, білого нальоту від флюсу; - нічого не обвуглене.

**`T-23-037`** · `manual/23-triazh.md:73`

> Між `3V3` і `GND` не має бути короткого замикання.

**`T-23-052`** · `manual/23-triazh.md:104`

> Шапка з'єднання, яку `esptool` друкує перед будь-якою командою, називає сімейство, ревізію кремнію і MAC (розділ 17).

**`T-23-084`** · `manual/23-triazh.md:161`

> Чип відповідає, `invalid header` · Далі → розділ 18

**`T-24-027`** · `manual/24-chuzha-proshyvka.md:56`

> **Тексти повідомлень.** `Failed to connect to broker`, `Calibration required` — прямо називають, що пристрій робить і на що скаржиться.

**`T-24-044`** · `manual/24-chuzha-proshyvka.md:98`

> Далі розбирати відповідним інструментом: `mklittlefs`, `mkspiffs` — обидва вміють не лише пакувати, а й розпаковувати.

**`T-25-013`** · `manual/25-log.md:21`

> `minicom` · Вихід → `Ctrl+A`, потім `X`

**`T-25-014`** · `manual/25-log.md:22`

> `screen` · Коли він → чужий пристрій, є під рукою скрізь

**`T-25-016`** · `manual/25-log.md:23`

> `picocom` · Коли він → чужий пристрій, найпростіший

**`T-25-096`** · `manual/25-log.md:218`

> **По мережі.** Відправка логів на сервер — MQTT, HTTP, syslog.

**`T-26-029`** · `manual/26-zboyi.md:53`

> Найчастіше джерело обох — `malloc`, результат якого не перевірили.

**`T-26-069`** · `manual/26-zboyi.md:152`

> do_work();

**`T-27-022`** · `manual/27-jtag.md:52`

> Офіційне розширення ESP-IDF для VS Code налаштовує це саме.

**`T-27-043`** · `manual/27-jtag.md:97`

> Лог і coredump (розділ 26) покривають переважну більшість задач дешевше.

**`T-27-062`** · `manual/27-jtag.md:146`

> **Піни JTAG зайняті проєктом** — див. попередження вище. 5.

**`T-27-071`** · `manual/27-jtag.md:162`

> JTAG потрібен там, де всі чотири нічого не дали і треба подивитися всередину пам'яті.


## Batch 5

**`T-28-048`** · `manual/28-analizator.md:89`

> Дешеві аналізатори мають межу частоти дискретизації — типово 24 МГц.

**`T-28-070`** · `manual/28-analizator.md:136`

> Кілька прийомів, що працюють на самому ESP32:

**`T-31-001`** · `manual/31-freertos.md:3`

> FreeRTOS уже працює, коли викликається ваш перший рядок (розділ 30).

**`T-31-030`** · `manual/31-freertos.md:91`

> [[classic]] [[S3]] Ядро 0 переважно зайняте радіостеком, `app_main` за замовчуванням іде на ядро 1 (розділ 03).

**`T-33-011`** · `manual/33-peryferiya-kod.md:22`

> `pin_bit_mask` — бітова маска, тому кілька пінів налаштовуються однією дією.

**`T-33-063`** · `manual/33-peryferiya-kod.md:159`

> Головне застосування — **адресні світлодіоди WS2812**.

**`T-33-083`** · `manual/33-peryferiya-kod.md:205`

> .atten = ADC_ATTEN_DB_12,

**`T-33-092`** · `manual/33-peryferiya-kod.md:224`

> **Точність.** ADC ESP32 нелінійний, і сирі відліки не переводяться в вольти простим множенням.

**`T-33-095`** · `manual/33-peryferiya-kod.md:230`

> .unit_id = ADC_UNIT_1,

**`T-33-096`** · `manual/33-peryferiya-kod.md:231`

> .atten = ADC_ATTEN_DB_12,

**`T-33-112`** · `manual/33-peryferiya-kod.md:264`

> Справжній аналоговий вихід, 8 розрядів, два канали.

**`T-33-126`** · `manual/33-peryferiya-kod.md:289`

> WS2812 керуються через RMT апаратно — у коді це робити не варто.

**`T-34-057`** · `manual/34-uart.md:132`

> При налагодженні Modbus логічний аналізатор економить години (розділ 28).

**`T-35-056`** · `manual/35-i2c.md:129`

> .glitch_ignore_cnt = 7,

**`T-35-077`** · `manual/35-i2c.md:178`

> Практично це означає, що ваш пристрій, який прикидається I²C-датчиком для чужої системи, мусить встигати відповідати завжди.

**`T-36-016`** · `manual/36-spi.md:24`

> Звідси головна арифметика SPI: `4 + n` пінів на `n` пристроїв.

**`T-36-084`** · `manual/36-spi.md:136`

> Для великих передач — кадр дисплея, блок з картки — DMA передає дані без участі процесора.

**`T-36-111`** · `manual/36-spi.md:181`

> Довжина · SPI → ще менше

**`T-36-113`** · `manual/36-spi.md:186`

> **SPI** — коли даних багато: кольорові дисплеї, картки пам'яті, радіомодулі, зовнішні АЦП з високою частотою вибірки.

**`T-38-040`** · `manual/38-can.md:94`

> .data_length_code = 4,


## Batch 6

**`T-39-057`** · `manual/39-wifi.md:147`

> **SoftAP або BLE provisioning** — штатні механізми ESP-IDF із застосунками для телефона.

**`T-40-019`** · `manual/40-merezha.md:42`

> Розмір стека сервера задається в `HTTPD_DEFAULT_CONFIG` і його часто доводиться збільшувати.

**`T-40-028`** · `manual/40-merezha.md:61`

> На ESP32 кілька одночасних клієнтів — межа, і поводитися з нею треба свідомо.

**`T-40-047`** · `manual/40-merezha.md:102`

> Рядок `TZ` вище — правило переходу на літній час для України; воно працює автономно, без оновлень.

**`T-41-017`** · `manual/41-ble.md:31`

> Споживання · BLE → **дуже низька**

**`T-41-023`** · `manual/41-ble.md:34`

> Термінал на телефоні · BLE → потрібен BLE-застосунок

**`T-42-018`** · `manual/42-espnow.md:41`

> .channel = 1,

**`T-42-020`** · `manual/42-espnow.md:44`

> memcpy(peer.peer_addr, mac_pryimacha, 6);

**`T-42-058`** · `manual/42-espnow.md:138`

> Щоб ESP-NOW працював, партнери мусять бути **на тому самому каналі** — а він визначається роутером і може змінитися.

**`T-42-063`** · `manual/42-espnow.md:148`

> Шлюз мусить тримати канал ESP-NOW рівним каналу точки доступу — і, якщо роутер змінить канал, повідомити датчики або перейти сам.

**`T-43-015`** · `manual/43-lora.md:22`

> Споживання при передачі · Wi-Fi / ESP-NOW → сотні мА

**`T-43-037`** · `manual/43-lora.md:70`

> **Ніколи не вмикати LoRa-модуль без антени.** Передавач без узгодженого навантаження відбиває потужність назад у вихідний каскад і **вигорає**.

**`T-43-060`** · `manual/43-lora.md:127`

> **Підтвердження й повтори.** LoRa нічого не гарантує.

**`T-44-039`** · `manual/44-neznayomyy-modul.md:64`

> `VCC`, `GND`, один сигнал · Розділ → 33

**`T-44-040`** · `manual/44-neznayomyy-modul.md:65`

> `VCC`, `GND`, `A0`/`OUT` аналоговий · Інтерфейс → ADC

**`T-45-079`** · `manual/45-sensory.md:194`

> DHT22 гірший за BME280 майже в усьому; для нового проєкту вибір інший.

**`T-47-004`** · `manual/47-klyuchi.md:12`

> | Навантаження | Чим | Чому |

**`T-47-037`** · `manual/47-klyuchi.md:57`

> Діод, якщо навантаження індуктивне, стоїть **паралельно самому навантаженню**, катодом до `+V` — тобто в нормальній роботі закритий, а викид при вимиканні пропускає по колу навантаження, минаючи транзистор.

**`T-48-049`** · `manual/48-motory.md:123`

> Керування через LEDC (розділ 33).

**`T-48-057`** · `manual/48-motory.md:139`

> З боку ESP32 керування виглядає так само.


## Batch 7

**`T-49-007`** · `manual/49-kamera.md:16`

> Для конфігурації, логу раз на хвилину чи невеликих файлів SPI достатньо з запасом.

**`T-49-067`** · `manual/49-kamera.md:176`

> Буфери виділяти один раз при старті; для DMA — з правильними властивостями.

**`T-50-020`** · `manual/50-bezpeka.md:53`

> **Дефолтні паролі — не варіант.** Пристрій, що піднімає точку доступу з паролем `12345678` або веб-інтерфейс без пароля, доступний усім у радіусі дії.

**`T-50-038`** · `manual/50-bezpeka.md:92`

> Мінімум: HTTPS із перевіркою сервера (розділ 19).

**`T-50-068`** · `manual/50-bezpeka.md:189`

> Ключі в коді дістаються за п'ять хвилин; місце їм у NVS, унікальними на екземпляр.

**`T-53-043`** · `manual/53-akum.md:113`

> Це єдиний спосіб використати ємність акумулятора **повністю**, до 3.0 В.

**`T-55-026`** · `manual/55-polova-diagnostyka.md:63`

> **Роз'єм живлення або USB.** Механічно розхитаний, відірваний із площадками, окислений.

**`T-57-007`** · `manual/57-vid-zadachi.md:20`

> **Який канал зв'язку?** Wi-Fi, ESP-NOW, LoRa, дріт — визначається відстанню, енергією й тим, що вже є на об'єкті (розділи 39–43).

**`T-57-020`** · `manual/57-vid-zadachi.md:52`

> | Zigbee, Thread, Matter | C6 або H2 |

**`T-57-022`** · `manual/57-vid-zadachi.md:54`

> | Новий проєкт без особливих умов | **S3** |

**`T-59-103`** · `manual/59-proj-monitor.md:340`

> snprintf(buf + n, 16384 - n, "]}");

**`T-59-123`** · `manual/59-proj-monitor.md:391`

> .glitch_ignore_cnt = 7,

**`T-59-125`** · `manual/59-proj-monitor.md:397`

> ESP_LOGE(TAG, "датчик не знайдено — працюємо без нього");

**`T-59-137`** · `manual/59-proj-monitor.md:425`

> idf.py build

**`T-60-095`** · `manual/60-proj-loger.md:235`

> gpio_set_level(PIN_DILNYK_EN, 1);

**`T-60-099`** · `manual/60-proj-loger.md:265`

> fflush(f);

**`T-60-116`** · `manual/60-proj-loger.md:313`

> | Фаза | Час | Струм | Заряд |

**`T-61-016`** · `manual/61-proj-kanal.md:32`

> Потрібен роутер · ESP-NOW → **ні**

**`T-61-044`** · `manual/61-proj-kanal.md:129`

> Статус приходить у зворотний виклик `on_sent`, і саме його треба дочекатися перед засинанням — інакше чип засне посеред передачі.

**`T-61-053`** · `manual/61-proj-kanal.md:155`

> memcpy(peer.peer_addr, MAC_PRYIMACHA, 6);


## Batch 8

**`T-61-054`** · `manual/61-proj-kanal.md:156`

> memcpy(peer.lmk, lmk, 16);

**`T-61-072`** · `manual/61-proj-kanal.md:249`

> Якщо приймач також під'єднаний до Wi-Fi, його канал визначає **роутер** — і більшість роутерів обирають канал автоматично й змінюють його самі.

**`T-61-084`** · `manual/61-proj-kanal.md:281`

> - **Кілька передавачів на один приймач** — структура вже готова (масив `vuzly`); - **Двонапрямлений обмін**: приймач надсилає команди у відповідь на пакет, поки передавач не заснув; - **Заміна на LoRa** (розділ 43), коли потрібні кілометри: формат пакета й логіка лишаються, змінюється транспорт; - **Ретрансляція** через проміжний вузол для збільшення покриття.

**`T-62-103`** · `manual/62-proj-keruvannya.md:219`

> if (stan == STAN_BLOKUVANNYA && u_stani > PAUZA_PISLYA_S)

**`T-62-139`** · `manual/62-proj-keruvannya.md:315`

> perejty(STAN_ROBOTA, "команда з мережі");

**`T-63-018`** · `manual/63-proj-mist.md:35`

> │                                      │

**`T-63-039`** · `manual/63-proj-mist.md:120`

> .sin_port = htons(PORT),

**`T-63-042`** · `manual/63-proj-mist.md:131`

> ESP_LOGI(TAG, "клієнт під'єднався");

**`T-A-013`** · `dodatky/a-pinouty.md:19`

> 2 · ADC → ADC2_2

**`T-A-055`** · `dodatky/a-pinouty.md:36`

> 34–39 · ADC → ADC1

**`T-A-068`** · `dodatky/a-pinouty.md:52`

> 33–37 · Примітка → `N16R8` і подібні

**`T-A-077`** · `dodatky/a-pinouty.md:67`

> | GPIO | Обмеження | Примітка |

**`T-B-005`** · `dodatky/b-symptomy.md:18`

> | Симптом | Причина | Дія | Розділ |

**`T-B-076`** · `dodatky/b-symptomy.md:52`

> Перезавантаження при Wi-Fi · Розділ → 06

**`T-B-082`** · `dodatky/b-symptomy.md:54`

> Працює від USB, не від БЖ · Розділ → 05

**`T-B-123`** · `dodatky/b-symptomy.md:73`

> UART: нічого · Причина → переплутані TX/RX

**`T-B-144`** · `dodatky/b-symptomy.md:84`

> ADC читає дурницю · Розділ → 07, 33

**`T-B-152`** · `dodatky/b-symptomy.md:87`

> GPIO дивно при старті · Дія → інший пін

**`T-B-197`** · `dodatky/b-symptomy.md:107`

> Пінги ходять, OTA не проходить · Причина → межа покриття

**`T-B-209`** · `dodatky/b-symptomy.md:111`

> BLE: не вміщається · Причина → Bluedroid замість NimBLE


## Batch 9

**`T-B-223`** · `dodatky/b-symptomy.md:115`

> LoRa: модуль згорів · Розділ → 43

**`T-C-074`** · `dodatky/c-komandy.md:151`

> riscv32-esp-elf-addr2line    -pfiaC -e build/app.elf 0x42001234

**`T-C-090`** · `dodatky/c-komandy.md:177`

> lsof /dev/ttyUSB0                # хто тримає порт

**`T-COM-007`** · `inserts/components-2026-08.md:17`

> ESP32-S3-DevKitC-1 · Коли брати → новий проєкт за замовчуванням

**`T-COM-008`** · `inserts/components-2026-08.md:17`

> ESP32-S3-DevKitC-1 · На що дивитися → `N8` чи `N16R8` — різна кількість вільних пінів

**`T-COM-013`** · `inserts/components-2026-08.md:20`

> ESP32-C3 SuperMini · Коли брати → простий дешевий вузол

**`T-COM-015`** · `inserts/components-2026-08.md:21`

> ESP32-CAM · Коли брати → камера за подією

**`T-COM-018`** · `inserts/components-2026-08.md:27`

> DHT11, DHT22 · Беріть → **BME280** або SHT3x

**`T-COM-087`** · `inserts/components-2026-08.md:98`

> Поріг 0.5 °C бракував би чесний товар.

**`T-D-028`** · `dodatky/d-panik.md:19`

> `0x9` · Що робити → розділ 32

**`T-D-032`** · `dodatky/d-panik.md:21`

> `0xb` · Назва → TGWDT_CPU_RESET

**`T-D-049`** · `dodatky/d-panik.md:26`

> `0x10` · Що робити → розділ 32

**`T-D-051`** · `dodatky/d-panik.md:32`

> `rst:0xf` — це **живлення**, не помилка в коді.

**`T-D-092`** · `dodatky/d-panik.md:107`

> Спокусливо взяти цю таблицю бітів, скласти з нею правила strapping із розділу 07 і дістати «`boot:0x4` означає ось це».

**`T-E-005`** · `dodatky/e-interfeysy.md:11`

> | Пристрій | Адреса | Що дає | Бібліотека |

**`T-E-043`** · `dodatky/e-interfeysy.md:25`

> TCA9548A · Що дає → мультиплексор шини

**`T-E-085`** · `dodatky/e-interfeysy.md:51`

> E-paper (SSD16xx) · Бібліотека → GxEPD2

**`T-E-088`** · `dodatky/e-interfeysy.md:57`

> Adafruit за замовчуванням ставить `SPI_MODE0`, частина інших бібліотек — третій (розділ 36).

**`T-F-016`** · `dodatky/f-oflayn.md:76`

> - [ ] **PulseView / sigrok** для логічного аналізатора (розділ 28) - [ ] Термінальна програма: `picocom`, `minicom`, PuTTY - [ ] `mklittlefs` / `mkspiffs` для роботи з файловими системами - [ ] `gen_esp32part.py` — іде з IDF - [ ] KiCad із бібліотеками, якщо розводите плати - [ ] Редактор і засоби, до яких ви звикли

**`T-G-008`** · `dodatky/g-glosariy.md:16`

> | **strapping** | піни, стан яких при скиданні задає режим завантаження |


## Batch 10

**`T-G-009`** · `dodatky/g-glosariy.md:17`

> | **bootloader** | програма, що завантажує наступну програму |

**`T-G-161`** · `dodatky/g-glosariy.md:195`

> | RTC | Real-Time Clock |

**`T-H-022`** · `dodatky/h-dzherela.md:55`

> **`github.com/espressif/arduino-esp32`** — Arduino core, релізи, міграційні нотатки 2.x → 3.x (розділ 12).

**`T-K01-005`** · `kartky/k01-triazh.md:10`

> | Напис на модулі | Чип | Що це значить |

**`T-K01-010`** · `kartky/k01-triazh.md:14`

> `ESP32-S3-WROOM-1` · Чип → ESP32-S3

**`T-K04-012`** · `kartky/k04-boot.md:29`

> Натиснути і **тримати** `BOOT`. 2.

**`T-K04-013`** · `kartky/k04-boot.md:30`

> Не відпускаючи `BOOT`, коротко натиснути й відпустити `EN`. 3.

**`T-K05-004`** · `kartky/k05-proshyvka.md:11`

> `bootloader.bin` · Що це → другий бутлоадер

**`T-K05-026`** · `kartky/k05-proshyvka.md:37`

> Не з'єднується — знизити до `--baud 115200`.

**`T-K08-031`** · `kartky/k08-symptomy.md:17`

> 10 · Симптом → GPIO поводиться дивно при старті

**`T-K08-047`** · `kartky/k08-symptomy.md:22`

> 15 · Найчастіша причина → стерто разом із калібруванням і NVS

**`T-K09-016`** · `kartky/k09-pinouty.md:29`

> | **26–32** | флеш і PSRAM. Не чіпати |

**`T-K09-017`** · `kartky/k09-pinouty.md:30`

> | **33–37** | додатково зайняті на модулях з Octal PSRAM (`N16R8`) |

**`T-K09-021`** · `kartky/k09-pinouty.md:34`

> | 11–20 | ADC2 |

**`T-K10-028`** · `kartky/k10-komandy.md:41`

> Скинути плату — `Ctrl+T`, потім `Ctrl+R`.

**`T-K13-016`** · `kartky/k13-zhyvlennya.md:25`

> 4 · Що міряти → **`3V3` під навантаженням, Wi-Fi увімкнений**

**`T-K13-039`** · `kartky/k13-zhyvlennya.md:72`

> | `rst:0xf` | кабель, хаб, немає конденсатора |

**`T-REG-024`** · `inserts/regulatory-2026-08.md:57`

> ESP-IDF має налаштування регіону, що обмежує доступні канали й потужність.

**`T-Z-002`** · `dodatky/z-pokazhchyk.md:5`

> Слова, які трапляються більш ніж на двох десятках сторінок, сюди не входять: покажчик, який на «GPIO» дає сорок номерів, заважає більше, ніж допомагає.

**`T-Z-148`** · `dodatky/z-pokazhchyk.md:550`

> LoRa — 80, 231, 249, 251–255, 283, 316, 347, 370, 387

