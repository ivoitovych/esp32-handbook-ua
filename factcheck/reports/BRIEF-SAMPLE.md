# Наряд: випадкова вибірка класу `F` — ще не звірене

**Генерується** `tools/sample.py`. Насіння **20260829**, з популяції
**1742** одиниць відібрано **4**.

## Що це за одиниці

Клас `F` — «ще не звірено». Не «сумнівне»: до цих рядків просто ніхто
не дійшов.

## Правило, яке важить більше за вердикт

**Кожна відповідь мусить назвати документ, який ти дивився.** Кожна —
включно з тими, де нічого не знайшлося.

Причина проста: без цього «не знайшов» коштує нуль, і його пишуть, не
відкривши нічого. Такий запис не є ані знахідкою, ані свідченням її
відсутності, і `tools/measure_f.py` відкидає його як «не дивився» ще до
лічби.

> Наряд не каже, якої відповіді чекає. Він каже, що кожна відповідь
> мусить пред'явити.

Перелік вердиктів і те, чого кожен вимагає, стоїть нижче, у блоці
завдання. Тут його немає навмисно: **жоден генератор не пише власної
копії цих правил**, і саме така копія тут і стояла — з іменами
вердиктів, яких ворота вже не вживають.

`source` завжди починається з `https://raw.githubusercontent.com/`.

**Адреса, що вказує на сам довідник** (`esp32-handbook`, `ivoitovych`,
`voytovych`, або шлях виду `manual/…`, `kartky/…`, `dodatky/…`)
відкидається механічно: довідник не є джерелом для себе. Текст книги,
наведений нижче, — це те, що **перевіряють**, а не те, чим перевіряють.

## Як шукати

По кожній одиниці: вибери документ, у якому це мало б стояти, завантаж
його `curl`-ом, подивися. Далі — вердикт за таблицею вище.

Досяжне лише `raw.githubusercontent.com`. Усе інше — 403; **не
повторюй запит, що дав 403**.

Куди дивитися:
`espressif/esp-idf` (`docs/en/…`, `components/…`, `examples/…`),
`espressif/esptool`, `espressif/arduino-esp32`, `torvalds/linux`
(`drivers/…`), `esphome/esphome`, `micropython/micropython`,
`adafruit/*`, `jgromes/RadioLib`, `olikraus/u8g2`, `Bodmer/TFT_eSPI`,
`lvgl/lvgl`.

Окремо: `espressif.com` на деякі адреси віддає **HTML-заглушку
15 495 байтів із кодом 200**. Відповідь «успішна», документа немає. Не
схоже на документ — `nedosyazhne`.

## Заборони

Повністю — `factcheck/HELPERS.md`; найважливіші стоять нижче, у блоках
завдання, і тут не повторюються.

## Про `disputes`

Найцінніша відповідь: книгу ще можна виправити. Але лише коли **бачиш
інший текст**, а не пам'ятаєш інакше.

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

*Task spec `4b626429` · blocks: ORIENTATION, VERBATIM, HONEST-MISS, NETWORK, STUB, VERDICTS-EXTERNAL, NO-SELF-REFERENCE, FORMAT. Quote this version when reporting results from this wave.*


## Пакет 1

**`T-27-062`** · `manual/27-jtag.md:146`

> **Піни JTAG зайняті проєктом** — див. попередження вище. 5.

**`T-36-107`** · `manual/36-spi.md:179`

> Адресація · SPI → окремий пін

**`T-61-016`** · `manual/61-proj-kanal.md:32`

> Потрібен роутер · ESP-NOW → **ні**

**`T-K04-020`** · `kartky/k04-boot.md:55`

> [[classic]] На платах ESP32-CAM кнопки `BOOT` немає взагалі: `GPIO0` з'єднується з `GND` перемичкою на самій платі.

