# Наряд: випадкова вибірка класу `F` — ще не звірене

**Генерується** `tools/sample.py`. Насіння **20260828**, з популяції
**1749** одиниць відібрано **6**.

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

## Вердикти й що кожен вимагає

| Вердикт | Обов'язково |
|---|---|
| `pidtverdzheno` | `dzherelo` + `cytata` — дослівний рядок із документа |
| `sperechayetsya` | `dzherelo` + `cytata` — рядок, що каже **інакше** |
| `ne_znayshov` | `dzherelo` — **адреса документа, який дивився** |
| `nedosyazhne` | `dzherelo` + код відповіді в `komentar` (403, 404, заглушка) |

`dzherelo` завжди починається з `https://raw.githubusercontent.com/`.

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

Повністю — `factcheck/HELPERS.md`. Тут найважливіші:

- **переказ — не цитата.** Усе в полі `cytata` звіряється підрядком у
  завантаженому документі;
- **пам'ять — не документ.** Велика літера замість малої валить запис
  навіть при правильному факті;
- **«стандартна практика» — не джерело**;
- **знати відповідь — не підстава написати цитату.** Факт відомий, а
  рядка не видно — це `ne_znayshov` із назвою того, де дивився.

## Про `sperechayetsya`

Найцінніша відповідь: книгу ще можна виправити. Але лише коли **бачиш
інший текст**, а не пам'ятаєш інакше.

## Формат

```yaml
- odynycya: T-12-034
  verdykt: ne_znayshov
  dzherelo: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst
  komentar: документ прочитано, про це в ньому не сказано

- odynycya: T-12-035
  verdykt: pidtverdzheno
  dzherelo: https://raw.githubusercontent.com/espressif/esp-idf/master/...
  cytata: |
    дослівний рядок із завантаженого документа
  komentar: що саме він підтверджує
```

**YAML:** якщо значення містить `: ` або починається з лапки — бери все
значення в одинарні лапки.

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

Used when the unit already carries a class and the question is whether
that class is right.

| Verdict | When |
|---|---|
| `confirmed` | the existing class is correct |
| `disputes` | the source contradicts the handbook |
| `truly_none` | there really is no external referent: this is the author's position |
| `not_found` | you could not tell — say what you read |

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

*Task spec `4e65092f` · blocks: ORIENTATION, VERBATIM, HONEST-MISS, NETWORK, STUB, VERDICTS-VERDICT-TEST, NO-SELF-REFERENCE, FORMAT. Quote this version when reporting results from this wave.*


## Пакет 1

**`T-15-016`** · `manual/15-oflayn.md:16`

> Потрібні MCPWM, PCNT, TWAI · Чому → повний доступ до периферії

**`T-21-069`** · `manual/21-seriyna.md:153`

> 0042 · MAC → `A0:B7:…:2C`

**`T-26-110`** · `manual/26-zboyi.md:246`

> Запис coredump — це запис у флеш у момент, коли система вже нестабільна.

**`T-32-042`** · `manual/32-nadiynist.md:113`

> robota();

**`T-42-056`** · `manual/42-espnow.md:135`

> ESP-NOW і Wi-Fi ділять одне радіо і **один канал**.

**`T-K08-003`** · `kartky/k08-symptomy.md:6`

> | # | Симптом | Найчастіша причина | Що робити |

