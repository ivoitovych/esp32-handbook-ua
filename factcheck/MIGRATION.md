# Переїзд: із внутрішнього жаргону в придатну технологію

Цей документ описує, як фактчекінг цієї книги перетворюється на щось,
що можна віддати людині й перенести на іншу книгу — зокрема
англомовну.

Він написаний **до** робіт, а не після, і кожен етап має три частини:
що змінюється, який скрипт це робить, і **чим доводиться, що нічого не
загубилося**.

## Навіщо

Дві незалежні хиби, знайдені власником одного вечора.

**Перша: картка не самодостатня.** Ось як вона виглядала:

    T-K01-014 · komirka · рядок 15
    Книга каже, дослівно:
    > `ESP8266` / `ESP-12` · Чип → не ESP32

Це **рендер**, а не цитата — такого рядка в книзі немає. Зникло все,
що робить твердження твердженням: що це напис на кришці модуля, що це
таблиця розпізнавання, що поруч стоять родичі, і що третя колонка —
«інша архітектура, інший тулчейн» — узагалі відрізана.

Наслідок був вимірний. Ми три сесії поспіль записували роди хибних
тривог — «поділ відрізає застереження», «комірка без контексту»,
«суперечка про ступінь» — і всі вони одна причина: **помічник судив
половину думки.** Одинадцять заявлених суперечностей, жодної
справжньої.

**Друга: жаргон.** `наряд`, `помічник`, `посадка`, `присуд`, `прохід`,
`помірка`, `холостий`, `штурм`. Робочі слова двох супровідників, які
протекли туди, де їх читає стороння людина: **710 записів** несуть їх
у полях `sposib` і `notatka`.

А поля звуться `nazva`, `zbih`, `klas`, `dzherelo`, `cytata`, `sposib`,
`notatka` — транслітерація, непридатна для англомовної книги й несмачна
для української.

## Що з чим сплутано

Три різні речі лежать в одному:

| Шар | Що це | Якою мовою |
|---|---|---|
| **модель** | поля запису | англійська — це код |
| **картка** | те, що людина відкриває й гортає | мовою книги |
| **процес** | наряд, помічник, посадка, хвиля | **лише в документах супровідника** |

Через це перенесення на англомовну книгу означало б переклад **коду**,
тобто форк замість перенесення.

## Чим доводиться, що робота не втрачається

`tools/znimok.py` знімає, до яких **одиниць** чіпляється кожен доказ.
Доказ прив'язаний не до тексту, а до одиниці; текст — лише спосіб її
назвати.

    знімок до переїзду: доказів 1337, прив'язок 5446, холостих 0

Після кожного етапу:

    tools/znimok.py factcheck/znimky/pryvyazky-do-pereyizdu.json --zvirty

Якщо рядок «втратили одиниці» не нуль — етап відкочується. Це не
формальність: сьогодні одна посадка вже мовчки переписала файли
попередньої, і 335 доказів стали 324. Тоді врятував `git`; після зміни
формату рятувати буде нічому, бо старі взірці не збігатимуться ні з
чим.

**Знімок мусив бути першим, і він перший.**

---

## Етап 1 — англійські імена полів · ✅ зроблено

`tools/imena.py --rozshyryty`

**Розширення, а не заміна.** Над тими самими файлами працює другий
супровідник; одномоментна заміна зламала б його інструменти тієї ж
хвилини. Тому нові імена стоять **поруч** зі старими:

| Було | Стало |
|---|---|
| `nazva` | `title` |
| `zbih` | `match` — **внутрішнє**, це регулярний вираз |
| `klas` | `status` |
| `dzherelo` | `source` |
| `cytata` | `quote` |
| `sposib` | `method` |
| `notatka` | `note` |
| `shukaty` | `look_for` |
| `rozrakhunok` | `calculation` |

Стан перевірки перестає бути літерою:

    A → verbatim              D → arithmetic         G → refuted
    B → derived               E → no-external-signal K → code-context
    C → named-unreachable     F → unchecked

**Доведено:** `imena.py --zvirty` — 1337 записів, без англійських імен
нуль. `znimok --zvirty` — втрачених одиниць нуль. `make check` — 46 з 46.

---

## Етап 2 — жаргон геть із записів · ✅ зроблено

`tools/bez_slenhu.py --pysaty`

Поле `method` тепер каже, **як і коли** джерело отримано, і більше
нічого. Двадцять два різні формулювання, з них шість покривали 570
записів, тож заміна адресна, а не ручна.

    переписано 582, лишилося без правила 22

**Двадцять два лишилися навмисно.** Там названий інструмент **і є**
методом: «`python3 tools/arytmetyka.py`, 2026-08-26» для перевірки
обчисленням. Це чесний запис способу, а не прикраса; скрипт їх
доповідає, а не переписує мовчки.

> Найдешевша помилка тут — переписати гуртом усе, що збіглося зі
> списком слів. Тоді інструмент, зроблений проти неясності, сам
> знищив би двадцять два ясні записи.

**Доведено:** `znimok --zvirty` — втрачених одиниць нуль.
`imena --zvirty` — 1337 записів, усі з англійськими іменами.
`make check` — 46 з 46.

---

## Етап 3 — картка стає самодостатньою

**Що змінюється.** Замість одного рендерованого рядка картка несе
три речі:

    ЩО СТВЕРДЖУЄТЬСЯ  одним реченням, людською мовою
    ДОСЛІВНО З КНИГИ  сирий рядок markdown, як він є у файлі
    КОНТЕКСТ          заголовок розділу, шапка таблиці, сусідні рядки
                      (для прози — абзац цілком)

Заголовок «Книга каже, **дослівно**» перестає бути неправдою: він
стоятиме над справді дослівним.

**Чим доводиться.** Звірка першого шару шукає дослівний рядок у книзі
**пошуком**, а не за номером рядка. Номер лишається довідковим — М2
поміряли, що він бреше в 1311 одиницях із 8090.

---

## Етап 4 — прив'язка переїжджає на хеш · пілот пройдено

### Спершу: план цього етапу був неправильний, і його скасовано

Тут стояло «`match` зіставляється з дослівним рядком книги замість
рендера». Перед тим, як чіпати 1265 прив'язок, я це поміряв:

    одиниць усього                                    8331
    різних рядків книги                               5298
    одиниць, що ділять рядок книги з іншими           5225
    найгустіший рядок                                 10 одиниць

Рядок таблиці містить багато комірок, і кожна комірка — окрема
одиниця. Взірець по сирому рядку **не може їх розрізнити**. Тобто той
план узяв би найгіршу хибу проєкту — широкий взірець, що мовчки
позначає «звірено» те, чого ніхто не звіряв, — і зробив би її
структурною для 63 % реєстру.

### І етап 5 теж скасовано

«Рендер прибирається» суперечить тому, чого власник просив із самого
початку: у картці має бути **назва, що стверджується**, пряма цитата й
контекст. Рендер (`BME280 · Адреса → 0x76`) — це і є назва. Прибрати
його означало б викинути одну з трьох частин, заради яких усе
починалося.

Етап 3 уже дав те, що було потрібно: рендер лишився й **названий**
рендером, а поруч стали дослівний рядок і контекст.

### Що робиться натомість

Точна прив'язка за хешем **уже існувала і вже працювала**:

    sha: [f98283f2, 3161b4c1]

`vsi_kandydaty` віддає їй перевагу над будь-яким взірцем. Нічого не
довелося винаходити — просто **жоден із 1337 записів нею не
користувався**.

Хеш не має жодної з двох бід: він точний і не залежить від формату,
яким володіємо ми. І він **сам відв'язується**, щойно формулювання
змінили, — що правильно: доказ стосувався тих слів, а не цих.

### Чому записи переїжджають родинами

Точна прив'язка перебиває взірець. Тож якщо запис A отримав `sha` на
одиницю X, а запис B досі доходив до X взірцем, — B **втрачає** X.
Половинчастий переїзд мовчки перекладає одиниці з одного доказу на
інший.

Тому переїжджають **компоненти зв'язності** за спільними одиницями:

    713 записів  поодинці        — безпечно по одному
     49 пар, 6 трійок            — разом
      1 компонента з 508 записів — 4444 прив'язки, усі сплутані

Остання — знахідка сама собою: 508 доказів транзитивно зчеплені тим,
що їхні взірці перекриваються.

`tools/bind_by_hash.py` **відмовляється** писати запис, чия родина не
вибрана цілком. Ця відмова — і є вся безпека етапу.

### Пілот

`pass-40-mira-f.yaml`, 3 записи, 9 одиниць. Перевірено трьома
доказами, а не одним:

1. `znimok --zvirty` після запису — **0 змін**;
2. перегенерування `02-chipy` — картки байт у байт ті самі;
3. взірці в тих трьох записах **навмисно зламано** на
   `ЦЕЙ-ВЗІРЕЦЬ-НЕ-ЗБІГАЄТЬСЯ-НІ-З-ЧИМ` — прив'язки лишилися ті самі.

Третій і є справжнім доказом етапу: він показує, що взірець більше не
несе навантаження. Перші два показали б те саме й тоді, якби нічого не
переїхало.

Відмову теж перевірено в дії: `--only m2-84-freertos` зупиняється й
називає родичів поза вибіркою.

### Порядок далі

    713 одиночних  партіями по файлах, `--zvirty` після кожної
     55 пар/трійок разом
    508 сплутаних  окремою роботою: спершу розчепити взірці
                   (це та сама робота, що й «широкий взірець»),
                   і лише потім переїзд

---

## Етап 6 — документи

`SCHEMA.md`, `ARCHITECTURE.md`, `POMICHNYKY.md`, `METODYKA.md`
переписуються під нову архітектуру. Робочий жаргон лишається **тільки
тут** — це документи супровідника, і в них він доречний.

Окремо: розділити документи на дві теки — те, що описує **технологію**
(переноситься на іншу книгу), і те, що описує **цю книгу**.

---

## Що цей переїзд НЕ полагодить

Одиниці, де твердження розмазане по кількох абзацах: контекст їх не
врятує, бо контекст сам потребуватиме контексту. За нинішнім розбором
це вузький хвіст, не половина черги — але сказати, що його не буде,
було б неправдою.

---

## Inventory: what is actually in `factcheck/`

Taken before any rewriting, so the size of the job is known rather than
guessed.

**Re-measured 2026-08-28 by opening every file, not by reading its
name.** The previous table was built from filenames, and it is the
worked example of defect kind 12 in its own directory: it sentenced six
files to deletion as "spent work orders", and two of those were a
generated report and the specimen whose gates section is the evidence
for the self-citation law. That plan was cancelled; the table outlived
the cancellation.

| Kind | Files | Size | How it was recognised | What happens to it |
|---|---:|---:|---|---|
| **governing** | 10 | 255 KB | on the list, by content | translate; this is the whole job |
| **generated** | 10 | 317 KB | the file **names its own generator** | translate the generator; the file rebuilds |
| **work order** | 1 | 61 KB | opens with `# Наряд` | stays with this book |
| **this book's data** | 8 | 74 KB | none of the above | stays; only prose headers matter |

**317 KB never needs hand-translation** — every generated file opens by
naming the tool that writes it. **The real work is the ten governing
documents**, and of those four are already in English.

### How the classification was done, and the one false positive it gave

A first pass searched the whole header for the word «генерується» and
put `ARCHITECTURE.md` — a governing document — among the generated
ones. The word was there, in a sentence about the **registry** being
generated from the book.

Narrowing the test to the actual convention (a line that **names the
generator**: ``Генерується `tools/…` ``) removed it.

> A classifier that matches a word matches every sentence containing
> that word. The convention it should test is not "does this word
> appear" but "does the file declare the thing".

That is kind 12 again, in the tool built to repair kind 12 — and it is
recorded here because catching it took one check and believing it would
have cost a document.

**Nothing is deleted until its durable content has moved.** The lessons
in these files were bought with waves that cost real money; a
translation must not become their loss.

## Glossary: the slang, and what it should have been

The problem was never the Ukrainian language. It was inventing words
where ordinary ones exist.

| Slang used | English | What it actually is |
|---|---|---|
| наряд | **work order** | a batch of claims for one worker |
| помічник | **worker** | the cheap model that runs a batch |
| посадка | **import** | writing evidence into the registry |
| присуд | **verdict** | an assertion that no source exists |
| прохід | **pass** | one traversal of the queue |
| штурм / вибірка | **sweep** / **sample** | targeted vs random, and only the random one yields quotable percentages |
| холостий взірець | **dead pattern** | matches no claim at all |
| комірка | **table cell** | — |
| одиниця | **claim** | the smallest checkable statement |
| `zbih` | **match pattern** | internal: the regex binding evidence to claims |

`наряд` was Soviet-industrial vocabulary picked up without thinking;
`комірка` is just a table cell. In English the natural terms are plain,
which is the point: **a term that needs explaining is a term that hides
something.**

---

## Stage 7 — the file names themselves

The slang is not only inside the documents. It **is** the documents:

    POMICHNYKY.md   BRIEF-SAMPLE.md   SWEEP-NO-SIGNAL.md   MEASURE-NO-SIGNAL.md
    SPLIT.md        PROKHID-POVNYY.md   TRACES.md      SPROSTOVANE.md
    dokazy/  rozbir/  prokhid/  doslidy/  znimky/  hvylya2/

And so are the tools: `naryad_f.py`, `prochid_zvid.py`,
`prochid_posadka.py`, `posadka_c.py`, `znimok.py`, `mira_f.py`,
`shturm.py`, `vybirka.py`.

A repository whose file names need a glossary cannot be handed to
anyone. Renaming is therefore not cosmetics — it is the same defect as
the card that needed the book to be understood.

### Mapping

**Documents that stay (technology):**

| Now | Becomes | |
|---|---|---|
| `ARKHITEKTURA.md` | `ARCHITECTURE.md` | done |
| `PEREYIZD.md` | `MIGRATION.md` | done |
| `PEREVIRYTY.md` | `TO-VERIFY.md` | done |
| `POMICHNYKY.md` | `WORKERS.md` | |
| `METODYKA.md` | `METHOD.md` | done — М2, вміст перекладено |
| `SPROSTOVANE.md` | `REFUTED.md` | |
| `UROKY-M2.md` | `LESSONS-M2.md` | M2's file — theirs to rename |
| `SCHEMA.md` | `SCHEMA.md` | already plain |

**Generated reports:**

| Now | Becomes |
|---|---|
| `QUOTES.md` | `QUOTES.md` |
| `SWEEP-NO-SIGNAL.md` | `SWEEP-NO-SIGNAL.md` |
| `MEASURE-NO-SIGNAL.md` · `MEASURE-UNCHECKED.md` | `MEASURE-NO-SIGNAL.md` · `MEASURE-UNCHECKED.md` |
| `SPLIT.md` | `SPLIT.md` |
| `TRACES.md` | `TRACES.md` |
| `BOOK-VS-SOURCES.md` | `BOOK-VS-SOURCES.md` |

**Directories:**

| Now | Becomes |
|---|---|
| `dokazy/` | `evidence/` |
| `rozbir/` | `triage/` |
| `prokhid/` · `prokhid-vidkydka/` | `pass/` · `pass-rejected/` |
| `doslidy/` | `experiments/` |
| `znimky/` | `snapshots/` |
| `detali/` · `klasC/` | `details/` · `class-c/` |

`manual/`, `dodatky/`, `kartky/`, `inserts/` **keep their names**: they
mirror the book's own directory layout, and renaming them would break
that correspondence for a Ukrainian book.

**Tools:**

| Now | Becomes |
|---|---|
| `naryad_f.py` | `brief_unchecked.py` |
| `prochid_zvid.py` | `verify_quotes.py` |
| `prochid_posadka.py` | `import_evidence.py` |
| `posadka_c.py` | `import_unreachable.py` |
| `znimok.py` | `snapshot.py` |
| `imena.py` | `rename_fields.py` |
| `bez_slenhu.py` | `strip_jargon.py` |
| `mira_f.py` | `measure.py` |
| `shturm.py` · `vybirka.py` | `sweep.py` · `sample.py` |
| `modalnist.py` | `modality.py` |
| `citaty.py` · `sprostovane.py` | `quotes.py` · `refuted.py` |

### Order, and why this order

Renames are done in three batches, safest first, each verified before
the next:

1. **Spent work orders** — *was* "deleted, not renamed". Done, and the
   plan was wrong twice in the same batch. See below.
2. **Data directories and generated reports** — nothing imports them by
   name except a handful of path constants.
3. **Tools** — riskiest: every rename is an import to update, and the
   `Makefile` names them. Done last, one at a time, `make check` after
   each.

After every batch: `tools/znimok.py … --zvirty`. Zero lost claims or
the batch is reverted.

### What batch 1 actually did, and what it got wrong

Five renames, three archivals, no deletions:

    ARKHITEKTURA.md          → ARCHITECTURE.md
    PEREYIZD.md              → MIGRATION.md
    PEREVIRYTY.md            → TO-VERIFY.md
    NARYAD-nedostupni.md     → UNREACHABLE-SOURCES.md
    NARYAD-m2-poyasnenyy.md  → WORK-ORDER-EXAMPLE.md
    NARYAD-m2-{hvylya2,hvylya3,rozbir}.md → archive/

The plan above called the `NARYAD-*.md` files "spent work orders,
reproducible from tools" and said to delete them. Two were not:

- **`NARYAD-nedostupni.md` is generated** — by `factcheck.py blocked`,
  from class-`C` records. Deleting it would have deleted a report that
  regenerates itself, which is harmless; but I had it filed as
  hand-written, which means the *reason* I kept it was wrong, and next
  time the same wrong reason could keep something that mattered.
- **`NARYAD-m2-poyasnenyy.md` is a specimen.** It is the work order that
  explains its gates instead of only forbidding, and dropping that
  section is what brought self-citation back (2 of 120 → 0 of 85). The
  document is the evidence for that measurement.

The three archived ones carry at least one rule each that I could not
find recorded anywhere else — `hvylya2`'s "a claim whose document is
not in the cache never enters the order" among them. Archived rather
than deleted until each rule is confirmed present in `WORKERS.md`.

> The plan said *delete*, and the plan had never opened the files. An
> inventory made from file names is a guess wearing a table's clothes.

Batch 1 also broke four readers and none of them raised a word: see
`RE_TVERDZHENNYA` in `tools/factcheck.py`.

---

## Stage 8 — the names themselves, measured 2026-08-28

The owner asked why script and field names are still transliterated
Ukrainian. They are, and here is the exact size of what is left.

### Fields: the expand phase is complete, the contract phase has not started

| | |
|---|---|
| records carrying **both** names | 1337 of 1337 |
| records carrying only Ukrainian | 0 |
| `skhema.py` accepts both | yes |

So the English names are fully in place. What remains is dropping the
Ukrainian ones — and that is blocked by a measured fact:

    tools reading Ukrainian field names directly   25
      of them the other maintainer's               4
    tools using the shared loader                   3
    tools parsing YAML themselves                  26

A normalising loader would free only three. The other twenty-five each
need their field access converted. **That is the whole of the contract
phase: mechanical, countable, and not uncertain.**

It cannot be done unilaterally: dropping the old names breaks the other
maintainer's four tools the moment it lands. It is the one step of this
migration that both must take on the same day.

### Tools: 43 of 52 still transliterated

    English already   build, preview, review, linkcheck, budgets,
                      bind_by_hash, claims, kod-stubs, pdf-smoke
    to rename         43

Each rename is an import and a `Makefile` line. The plan's own rule
stands: last, one at a time, `make check` after each.

### Directories: 11 of 17

    dokazy → evidence      rozbir → triage        prokhid → pass
    doslidy → experiments  znimky → snapshots     detali → details
    klasC → class-c        hvylya2, hvylya3 → waves/…
    prokhid-vidkydka → pass-rejected             slidy-m2 → theirs

`manual`, `dodatky`, `kartky`, `inserts` keep their names: they mirror
the book's own layout.

### Why this is the honest order

Fields before tools before directories, because a field name is read by
code that a rename would also touch — doing them in the other order
means touching the same twenty-five files twice.

> The migration is not stalled for want of a decision. It is at the one
> point where both maintainers must move together, and that is worth
> saying plainly rather than letting it look like drift.
