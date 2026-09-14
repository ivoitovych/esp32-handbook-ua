# Order: a random sample of `no-external-signal`

> **generated** — `factcheck/tools/sample.py`; editing it by hand is
> wasted work

Seed **20260914**; **120** units drawn from a population of
**3277**.

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

Used on the queue of units the tool closed **mechanically** — prose
carrying no digit, identifier, chip name or unit of measure. The question
is not "is the claim true" but "does an external referent exist at all".

| Verdict | When |
|---|---|
| `confirmed` | address plus a **verbatim** quote from the document |
| `advice` | you did not get the document, but can name where it would be |
| `disputes` | the source **contradicts** the handbook — the most valuable answer there is |
| `not_found` | the document exists, the passage is not in it — say what you read |
| `unreachable` | the document does not come down from here — give the `status:` code |
| `truly_none` | you looked and there is genuinely no external referent: this is the author's position, advice, or a framing sentence |

**`truly_none` is not a failure and not a lesser result.** The verdict
under test was assigned nearly four thousand times and had never once
been examined. Confirming one instance of it is worth as much as
overturning one — it is the first evidence the rule works at all.

Without this word a helper who correctly sees that a sentence is the
author's opinion has nowhere to put it, and under pressure to "find
something" begins inventing a source. That has been caught on both
maintainers, so the word is a safety device, not a courtesy.

**A unit that is not a claim at all** — a column heading, the lead-in to
a list, a row where the book describes its own registry — is also
`truly_none`, and say so in the comment. That is a fact about the
**granularity of the tool**, not about the book.

An address inside this repository, or a chapter of the handbook cited as
the source for a claim in the handbook, is rejected mechanically. If a
claim is supported only by another part of the book, say so plainly —
there is a class for it, and it is not a failure.

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

*Task spec `d2fb76e7` · blocks: ORIENTATION, VERBATIM, HONEST-MISS, NETWORK, STUB, VERDICTS-CONTEST-E, NO-SELF-REFERENCE, FORMAT. Quote this version when reporting results from this wave.*


## Batch 1

**`T-00-009`** · `manual/00-pro-dovidnyk.md:25`

> Тому книга не заміняє документацію Espressif і не претендує на це.

**`T-00-060`** · `manual/00-pro-dovidnyk.md:132`

> Механічна звірка цитати не бачить, що дослівна цитата зі справжнього документа підпирає хибний висновок.

**`T-00-068`** · `manual/00-pro-dovidnyk.md:154`

> Довідник охоплює стандартну embedded-інженерію: залізо, код, протоколи, периферію, живлення, збирання, ремонт.

**`T-02-083`** · `manual/02-chipy.md:73`

> Це не «поки не реалізовано», а відсутність апаратного блоку.

**`T-02-144`** · `manual/02-chipy.md:198`

> Три однакові плати в шухляді корисніші за шість різних.

**`T-03-015`** · `manual/03-soc.md:32`

> Вона дає можливість **розвести** конкуренцію: важку роботу на одне ядро, зв'язок на інше.

**`T-05-065`** · `manual/05-elektronika.md:141`

> У спокої вхід читає одиницю, натиснута кнопка притискає до нуля.

**`T-05-086`** · `manual/05-elektronika.md:187`

> Або обмін є, але з випадковими помилками.


## Batch 2

**`T-05-100`** · `manual/05-elektronika.md:215`

> Полярність електролітичного конденсатора обов'язкова: мінус позначений смугою.

**`T-05-110`** · `manual/05-elektronika.md:241`

> Реле, двигун, електромагнітний клапан — це котушка.

**`T-07-035`** · `manual/07-gpio.md:64`

> Саме тому діагностика проста, а плати все одно викидають, вважаючи їх мертвими.

**`T-08-003`** · `manual/08-platy.md:9`

> Модуль — кристал плюс кварц, флеш, антена й обв'язка в екранованому корпусі.

**`T-08-052`** · `manual/08-platy.md:88`

> Камера з'їдає більшість пінів (розділ 49).

**`T-08-069`** · `manual/08-platy.md:124`

> Практична стратегія: **купувати з запасом і перевіряти одразу**.

**`T-09-003`** · `manual/09-pidklyuchennya.md:8`

> Порядок пошуку — картка [К3](#k-pidkl).

**`T-10-012`** · `manual/10-instrumenty.md:27`

> Потужність 60 Вт, жало «скіс» 2–3 мм як основне.


## Batch 3

**`T-10-042`** · `manual/10-instrumenty.md:94`

> Набір із сотні номіналів коштує дешево і рятує десятки разів.

**`T-10-043`** · `manual/10-instrumenty.md:99`

> **Макетна плата.** Різниці майже немає.

**`T-10-045`** · `manual/10-instrumenty.md:105`

> Загальне правило: **вимірювальні прилади й те, що торкається плати гарячим, — не економити.

**`T-10-047`** · `manual/10-instrumenty.md:110`

> Кілька дрібниць, що впливають більше, ніж здається:

**`T-11-019`** · `manual/11-idf.md:42`

> Перелік цілей обмежує обсяг завантаження: тулчейни ставляться під кожну архітектуру окремо, і ставити всі немає сенсу.

**`T-13-037`** · `manual/13-pio.md:110`

> Плату, якої немає в переліку, описують власним файлом або беруть найближчу й правлять параметри.

**`T-14-047`** · `manual/14-shvydki-shlyakhy.md:125`

> Живлення, рівні, довжина дротів, підтягування.

**`T-15-063`** · `manual/15-oflayn.md:115`

> **Роздруковані картки К1–К15**, заламіновані.


## Batch 4

**`T-18-090`** · `manual/18-rozdily-fleshu.md:160`

> FAT має сенс в одному випадку: коли той самий носій (найчастіше картку microSD) читатиме звичайний комп'ютер.

**`T-19-032`** · `manual/19-ota.md:59`

> Місце коштує дешевше, ніж поїздка до кожного пристрою (розділ 18).

**`T-20-009`** · `manual/20-bekap.md:16`

> **Boot loop будь-якої природи.** Прошивка, що падає при старті, не заважає увійти в download mode: цей вибір робиться до того, як застосунок узагалі запуститься.

**`T-22-009`** · `manual/22-zberezhennya-stanu.md:26`

> Фото тут — не «на всяк випадок», а джерело даних, до якого ви повертатиметеся.

**`T-23-073`** · `manual/23-triazh.md:146`

> Те, що вони виведені на гребінку, не означає, що вони вільні.

**`T-23-094`** · `manual/23-triazh.md:169`

> Він **не** відповідає на «що воно робить» і «звідки взявся код».

**`T-24-060`** · `manual/24-chuzha-proshyvka.md:156`

> Умови, за яких це працює:

**`T-25-049`** · `manual/25-log.md:111`

> **Тег** — це ім'я підсистеми.


## Batch 5

**`T-25-064`** · `manual/25-log.md:139`

> Причина не в тегу і не в порядку викликів — рядка просто немає у прошивці.

**`T-25-098`** · `manual/25-log.md:222`

> **Coredump у флеші.** Не лог, а знімок стану в момент паніки — розділ 26.

**`T-25-103`** · `manual/25-log.md:237`

> Тимчасове має властивість доїжджати до замовника.

**`T-27-003`** · `manual/27-jtag.md:8`

> Це не заміна логу, а інший інструмент.

**`T-27-013`** · `manual/27-jtag.md:28`

> в одному терміналі, і в іншому:

**`T-28-013`** · `manual/28-analizator.md:23`

> **Живлення під навантаженням.** Не на холостому ходу, а коли пристрій працює і радіо ввімкнене.

**`T-28-020`** · `manual/28-analizator.md:32`

> Нуль означає, що підтягування немає або лінія кимось притиснута — і шина не працюватиме ніколи.

**`T-28-031`** · `manual/28-analizator.md:54`

> **PulseView** (з пакета sigrok) — вільна програма, що працює з більшістю дешевих аналізаторів.


## Batch 6

**`T-28-043`** · `manual/28-analizator.md:74`

> Найцінніший рядок — четвертий: він знімає з шини всі підозри й переводить пошук у код.

**`T-30-002`** · `manual/30-struktura.md:5`

> Найголовніша з них — ставлення до пам'яті.

**`T-31-008`** · `manual/31-freertos.md:33`

> Два правила, які варто засвоїти одразу.

**`T-31-038`** · `manual/31-freertos.md:107`

> На двох ядрах воно ламається одразу.

**`T-32-066`** · `manual/32-nadiynist.md:169`

> **Переривання** мають пріоритет над усіма задачами.

**`T-32-080`** · `manual/32-nadiynist.md:196`

> Те, що варто мати в кожній прошивці, яка їде в поле:

**`T-33-093`** · `manual/33-peryferiya-kod.md:225`

> Штатний шлях — калібрування:

**`T-33-123`** · `manual/33-peryferiya-kod.md:283`

> Антидребезг — порівнянням часу, ніколи не затримкою в ISR.


## Batch 7

**`T-34-053`** · `manual/34-uart.md:119`

> Сам ведений не говорить ніколи.

**`T-36-002`** · `manual/36-spi.md:4`

> Десятки мегагерц замість сотень кілогерц, ціною більшої кількості пінів.

**`T-36-017`** · `manual/36-spi.md:28`

> Це те, на чому спотикаються всі, і причина класичного симптому «пристрій повертає нулі або сміття».

**`T-36-041`** · `manual/36-spi.md:44`

> Останній стовпець варто прочитати уважно, бо саме тут роблять помилку.

**`T-36-092`** · `manual/36-spi.md:157`

> Кілька пристроїв вішаються на одну шину — саме для цього існує `CS`.

**`T-37-043`** · `manual/37-onewire.md:112`

> Виглядає привабливо і працює нестабільно, особливо на довгих лініях і з кількома датчиками.

**`T-38-015`** · `manual/38-can.md:35`

> Тому аварійні повідомлення отримують малі номери, а телеметрія — великі.

**`T-39-017`** · `manual/39-wifi.md:43`

> Інші обмеження, що трапляються:


## Batch 8

**`T-39-077`** · `manual/39-wifi.md:193`

> Дешево, компактно, достатньо для більшості задач.

**`T-40-081`** · `manual/40-merezha.md:175`

> **Зашивати сертифікат центру сертифікації, а не сервера.** Сертифікат сервера протермінується через рік, і всі пристрої одночасно втратять зв'язок.

**`T-41-006`** · `manual/41-ble.md:15`

> Практичний наслідок величезний: профіль **SPP** — послідовний порт по Bluetooth, на якому тримається безліч старих проєктів і на який розраховані прості термінальні застосунки для телефона, — існує **тільки на classic**.

**`T-42-068`** · `manual/42-espnow.md:161`

> Лікування: зафіксувати канал у налаштуваннях роутера або передбачити процедуру повторного узгодження каналу.

**`T-43-097`** · `manual/43-lora.md:221`

> Антена має відповідати діапазону модуля; розміщення важить більше за все інше.

**`T-44-060`** · `manual/44-neznayomyy-modul.md:112`

> Що перевірити перед тим, як брати:

**`T-45-048`** · `manual/45-sensory.md:107`

> Сирі показання гіроскопа безкорисні через хвилину інтегрування.

**`T-45-059`** · `manual/45-sensory.md:134`

> Шумний, потребує усереднення, дрейфує від температури.


## Batch 9

**`T-45-071`** · `manual/45-sensory.md:167`

> Разом із передавачем це створює наслідки, які варто продумати до розгортання, а не після: хто отримує дані, як вони захищені, що станеться, якщо їх перехоплять.

**`T-45-076`** · `manual/45-sensory.md:184`

> **Калібрувати за відомим.** Порівняти з повіреним приладом або з очевидною точкою: танення льоду — це 0 °C.

**`T-45-078`** · `manual/45-sensory.md:188`

> Виріб має розрізняти «датчик каже 25» і «датчик завис на 25»: слідкувати за тим, що значення взагалі змінюються (розділ 32).

**`T-46-026`** · `manual/46-dyspleyi.md:21`

> Для більшості задач книги це правильний вибір, але це **вибір**, а не межа заліза.

**`T-46-031`** · `manual/46-dyspleyi.md:33`

> Більшість бібліотек мають окремий режим — треба лише його ввімкнути.

**`T-46-033`** · `manual/46-dyspleyi.md:38`

> Для датчика на батарейці, який показує значення раз на годину, це ідеально.

**`T-46-080`** · `manual/46-dyspleyi.md:160`

> І окремо: **не перемальовувати весь екран, коли змінилося одне число**.

**`T-47-052`** · `manual/47-klyuchi.md:95`

> Він пробиває транзистор — іноді одразу, іноді після сотні спрацювань.


## Batch 10

**`T-47-055`** · `manual/47-klyuchi.md:102`

> Готові релейні модулі зазвичай мають діод на платі.

**`T-48-036`** · `manual/48-motory.md:92`

> **Мікрокрок** — драйвер ділить крок на частини (1/2, 1/4, ..., 1/32), що дає плавніший рух і менше шуму.

**`T-48-070`** · `manual/48-motory.md:184`

> Обмеження струму на кроковому драйвері виставляється **до** першого запуску.

**`T-51-001`** · `manual/51-payannya.md:3`

> Паяння — навичка, яка ставиться за один вечір і працює все життя.

**`T-51-004`** · `manual/51-payannya.md:11`

> Припій має **змочити** обидві поверхні — вивід і контактну площадку — і розтектися по них, утворивши плавну галтель.

**`T-51-019`** · `manual/51-payannya.md:34`

> **Прибрати припій, потім жало.** 6.

**`T-51-022`** · `manual/51-payannya.md:39`

> Уся операція займає 2–3 секунди на з'єднання.

**`T-51-025`** · `manual/51-payannya.md:46`

> Правильно: жало гріє, припій подається окремо, у точку контакту.


## Batch 11

**`T-51-078`** · `manual/51-payannya.md:159`

> Флюс обов'язковий; жало гріє обидві поверхні; припій подається в точку контакту, а не на жало.

**`T-51-082`** · `manual/51-payannya.md:168`

> Флюс змивати завжди — залишки роз'їдають доріжки.

**`T-52-056`** · `manual/52-montazh.md:140`

> І шосте, не менш важливе: **перевірити посадкові місця перед замовленням**.

**`T-53-068`** · `manual/53-akum.md:179`

> - **міряти в спокої**, коли радіо вимкнене; - **усереднювати** кілька відліків; - **не показувати відсотки з точністю до одиниць** — це самообман; чотири градації (повний, більше половини, менше, критично) чесніші; - для точного обліку — **окрема мікросхема-паливомір**, і тут важливо розрізняти два різні класи, які легко сплутати за назвою.

**`T-56-021`** · `manual/56-pasport.md:45`

> Контакти й дата.** Хто зробив, коли, як зв'язатися.

**`T-56-038`** · `manual/56-pasport.md:92`

> Це не привід їх прибирати: відповідь на «яка це збірка» коштує дорожче за побайтову відтворюваність, і саме тому книга наполягає зберігати сам файл образу, а не сподіватися перезібрати його (розділ 21).

**`T-57-002`** · `manual/57-vid-zadachi.md:3`

> Обраний не той чип, не врахований бюджет живлення, не продумана поведінка при відмові — і це виявляється тоді, коли пристрій уже зібраний.

**`T-57-006`** · `manual/57-vid-zadachi.md:17`

> **Які затримки допустимі?** Реакція за мілісекунди чи за хвилини — це різні пристрої (розділ 32).


## Batch 12

**`T-57-030`** · `manual/57-vid-zadachi.md:80`

> **Ідея.** Основний контролер робить свою роботу — керує механізмом, тримає таймінги, забезпечує безпеку.

**`T-57-065`** · `manual/57-vid-zadachi.md:179`

> Питання «що станеться, якщо чип зникне зараз» ставиться до кожного виходу на етапі проєктування.

**`T-58-016`** · `manual/58-dovedennya.md:36`

> Тиждень витрачено на частину, яку доведеться викинути разом із рештою.

**`T-58-030`** · `manual/58-dovedennya.md:70`

> **Прискорений час.** Пристрій, що має щось робити раз на годину, під час випробувань робить це раз на хвилину.

**`T-58-032`** · `manual/58-dovedennya.md:74`

> **Штучні відмови.** Не чекати, поки зв'язок обірветься сам — вимкнути роутер.

**`T-59-047`** · `manual/59-proj-monitor.md:98`

> Піни винесені в одне місце нагорі — так їх видно й так вони не розповзаються по коду:

**`T-59-113`** · `manual/59-proj-monitor.md:366`

> Уважніше треба з іншим: обробник виконується в задачі веб-сервера з обмеженим стеком.

**`T-60-136`** · `manual/60-proj-loger.md:334`

> Розрахунок на рік із запасом утричі означає, що три місяці ви отримаєте навіть при неприємних сюрпризах.


## Batch 13

**`T-62-035`** · `manual/62-proj-keruvannya.md:53`

> Замість неї доведеться покладатися на дисципліну коду — а в проєкті, де помилка заливає приміщення, це гірший захист.

**`T-62-045`** · `manual/62-proj-keruvannya.md:82`

> **Апаратний аварійний вимикач у розрив живлення насоса**, не в логіку.

**`T-62-065`** · `manual/62-proj-keruvannya.md:125`

> Від 3.3 В реле або не спрацює, або спрацьовуватиме через раз — класичне «іноді вмикається».

**`T-A-074`** · `dodatky/a-pinouty.md:57`

> Тільки-вхідних пінів немає — усі повнофункціональні.

**`T-A-095`** · `dodatky/a-pinouty.md:95`

> Тут змішано дві різні речі, і плутати їх дорого.

**`T-COM-016`** · `inserts/components-2026-08.md:21`

> ESP32-CAM · На що дивитися → **немає USB**, потрібен перехідник

**`T-COM-090`** · `inserts/components-2026-08.md:108`

> **Завжди:** перевірені USB-кабелі, гребінки, Dupont усіх трьох видів, термоусадка, резистори 4.7 і 10 кОм, конденсатори 100 нФ і 470 мкФ, пара конвертерів рівнів.

**`T-F-026`** · `dodatky/f-oflayn.md:104`

> Знайти пінаут потрібної плати.


## Batch 14

**`T-G-001`** · `dodatky/g-glosariy.md:3`

> Українська назва — канонічний англійський термін.

**`T-G-110`** · `dodatky/g-glosariy.md:136`

> | опір | resistance |

**`T-K01-004`** · `kartky/k01-triazh.md:8`

> Прочитати напис на металевій кришці модуля — це головне джерело істини:

**`T-K02-012`** · `kartky/k02-stan.md:25`

> Записати обидва значення.

**`T-K06-006`** · `kartky/k06-bootlog.md:12`

> Найчастіші значення для [[classic]] (повна таблиця — додаток D):

**`T-K09-013`** · `kartky/k09-pinouty.md:22`

> Поширена домовленість (не апаратна прив'язка): I²C — SDA 21, SCL 22; SPI — MOSI 23, MISO 19, SCK 18, CS 5.

**`T-K11-016`** · `kartky/k11-nikoly.md:35`

> Дільник або конвертер рівнів — обов'язково.

**`T-K13-003`** · `kartky/k13-zhyvlennya.md:4`

> Ця картка — перше, що робиться замість цього.


## Batch 15

**`T-K14-023`** · `kartky/k14-rivni.md:45`

> `LV` до 3.3 В, `HV` до 5 В, землі з'єднані.

**`T-K14-035`** · `kartky/k14-rivni.md:76`

> Мультиметром, до з'єднання:

**`T-K15-022`** · `kartky/k15-seriyna.md:36`

> «Прошилося без помилок» ловить не все: крок 6 виявляє справний образ на платі з непропаяним модулем.

**`T-K15-037`** · `kartky/k15-seriyna.md:58`

> Якщо треба лише відрізняти пристрої — **беріть MAC**: він унікальний від заводу і не потребує нічого.

**`T-UA--008`** · `inserts/ua-market-2026-08.md:23`

> **Українські маркетплейси.** Ширший вибір, продавці різної якості.

**`T-Z-065`** · `dodatky/z-pokazhchyk.md:239`

> esp_get_minimum_free_heap_size — 190, 330

**`T-Z-166`** · `dodatky/z-pokazhchyk.md:674`

> set-target — 25, 46–48, 96, 99, 327, 332, 374, 392

**`T-Z-193`** · `dodatky/z-pokazhchyk.md:828`

> WROOM-32 — 23, 67, 72–73, 362, 390

