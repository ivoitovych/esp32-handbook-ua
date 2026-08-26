// ─────────────────────────────────────────────────────────────────────────
// ESP32: практичний довідник — спільний шаблон верстання
//
// Один шаблон обслуговує три цілі збирання (Р12):
//   dovidnyk — A5, основне тіло, двобічний друк з полем на підшивку
//   kartky   — A4, ярус 0, одна картка = одна сторінка під ламінування
//   proekty  — A4, ярус 2, проєкти з довгими лістингами
//
// Друк чорно-білий: жодних кольорових плашок і жодних emoji-гліфів.
// Маркери ⚡ ⚠ 🛒 ⛔ з розмітки джерел (Р-позначки) відображаються
// типографічними блоками з лінійкою і словесною міткою — так вони
// переживають ксерокс, факс і дешеву друкарню.
// ─────────────────────────────────────────────────────────────────────────

#let font-serif = ("Libertinus Serif", "Liberation Serif", "DejaVu Serif")
#let font-sans  = ("Libertinus Sans", "Liberation Sans", "DejaVu Sans")
#let font-mono  = ("DejaVu Sans Mono", "Liberation Mono")

#let ink   = luma(0%)
#let dim   = luma(38%)
#let hair  = luma(72%)
#let panel = luma(94%)

// ── Маркери області дії: [classic] [S3] [C3] ────────────────────────────
#let scope(..chips) = box(baseline: 0.15em)[
  #for c in chips.pos() [
    #box(
      inset: (x: 0.34em, y: 0.16em),
      outset: (y: 0.1em),
      radius: 1pt,
      stroke: 0.5pt + dim,
      text(font: font-sans, size: 0.72em, weight: 600, tracking: 0.02em, fill: ink, c),
    )#h(0.22em)
  ]
]

// ── Блоки-застереження ──────────────────────────────────────────────────
// rule — товщина лівої лінійки; що небезпечніше, то товща.
#let note-block(label, body, rule: 1pt, fill-bg: none) = block(
  width: 100%,
  breakable: true,
  inset: (left: 0.9em, right: 0.7em, top: 0.6em, bottom: 0.6em),
  stroke: (left: rule + ink),
  fill: fill-bg,
  spacing: 1.1em,
)[
  #text(font: font-sans, size: 0.76em, weight: 700, tracking: 0.06em, fill: ink, upper(label))
  #v(0.35em, weak: true)
  #body
]

#let zhyvlennya(body) = note-block("Живлення", body, rule: 1pt)
#let hrabli(body)     = note-block("Увага", body, rule: 1.6pt)
#let zakupivlya(body) = note-block("Закупівля", body, rule: 0.6pt)
#let nezvorotne(body) = note-block("Незворотне", body, rule: 3pt, fill-bg: panel)

// ── Посилання на картку ярусу 0 ─────────────────────────────────────────
#let kartka(n, target) = box[
  #text(font: font-sans, size: 0.78em, weight: 600)[→ картка К#n]
  #h(0em)
]

// ── Службові блоки ──────────────────────────────────────────────────────
#let blockquote(body) = block(
  width: 100%,
  inset: (left: 1em, top: 0.4em, bottom: 0.4em),
  stroke: (left: 2pt + hair),
  spacing: 1.1em,
  text(fill: luma(15%), body),
)

#let horizontalrule = align(center, block(spacing: 1.4em, line(length: 28%, stroke: 0.6pt + dim)))

// ── Шмуцтитул частини ───────────────────────────────────────────────────
// Частина — це справжній заголовок рівня 1, тому вона потрапляє у зміст
// і в PDF-закладки. Розділи мають рівень 2 (див. tools/build.py: усі
// заголовки джерел зсуваються на один рівень униз).
#let part-blurb = state("part-blurb", "")

#let part-divider(title, blurb: "") = {
  part-blurb.update(blurb)
  heading(level: 1, title)
}

// ── Зміст ───────────────────────────────────────────────────────────────
#let table-of-contents() = {
  set page(header: none, footer: none, numbering: none)
  show outline.entry.where(level: 1): it => {
    v(1.1em, weak: true)
    text(font: font-sans, size: 0.95em, weight: 700, it)
  }
  show outline.entry.where(level: 2): it => {
    text(size: 0.92em, it)
  }
  set text(size: 0.95em)
  set par(justify: false)
  block(above: 0em, below: 1.4em)[
    #text(font: font-sans, size: 1.7em, weight: 700)[Зміст]
    #v(0.35em, weak: true)
    #line(length: 100%, stroke: 0.8pt + ink)
  ]
  outline(title: none, depth: 2, indent: 1.1em)
  pagebreak(weak: false)
}

// ── Титульна сторінка ───────────────────────────────────────────────────
#let title-page(meta) = {
  set page(header: none, footer: none, numbering: none)
  set align(center)
  v(1fr)
  text(font: font-sans, size: 2.4em, weight: 700, tracking: -0.01em,
       hyphenate: false, meta.title)
  v(0.7em)
  line(length: 42%, stroke: 0.8pt + ink)
  v(0.7em)
  text(font: font-serif, size: 1.15em, style: "italic", fill: luma(20%), meta.subtitle)
  v(2.2em)
  text(font: font-sans, size: 1.05em, tracking: 0.04em, meta.author)
  v(1fr)
  text(font: font-sans, size: 0.8em, fill: dim)[
    #meta.edition · ревізія #meta.revision
  ]
  pagebreak(weak: false)
}

// ── Сторінка вихідних даних (зворот титулу) ─────────────────────────────
#let colophon-front(meta) = {
  set page(header: none, footer: none, numbering: none)
  set text(size: 0.82em)
  set par(justify: false, leading: 0.62em)
  v(1fr)
  text(font: font-sans, weight: 600, size: 1.05em, meta.title)
  linebreak()
  text(fill: dim, meta.subtitle)
  v(1.2em)
  [Автор — #meta.author-full. \
   Ревізія #meta.revision. #meta.edition.]
  v(1.2em)
  [*Ліцензія.* Текст довідника — Creative Commons Attribution-ShareAlike 4.0
   International (CC BY-SA 4.0). Приклади коду — MIT.]
  v(0.6em)
  [Довідник дозволено *вільно друкувати, копіювати і роздавати*, зокрема
   комерційним друком, за умови зазначення авторства; похідні матеріали
   поширюються на тих самих умовах. Повні тексти ліцензій — у репозиторії
   проєкту.]
  v(1.2em)
  [*Застереження.* Матеріал описує стандартну інженерну роботу з
   мікроконтролерами: схемотехніку, код, протоколи, живлення, ремонт.
   Автор не несе відповідальності за наслідки застосування наведених
   відомостей. Робота з мережевим живленням, літієвими акумуляторами і
   радіопередавачами регулюється окремими нормами — дотримання їх лишається
   на відповідальності читача.]
  v(1.2em)
  [*Технічні дані* наведено за документацією Espressif Systems станом на
   дату ревізії. Кремній, документація і тулчейн змінюються — звіряйте
   критичні значення з першоджерелом.]
  v(1.2em)
  [Складено вільним програмним забезпеченням: Typst, pandoc.
   Гарнітури: Libertinus, DejaVu Sans Mono.]
  v(1fr)
  pagebreak(weak: false)
}

// ── Колонтитул ──────────────────────────────────────────────────────────
// Верхній колонтитул: назва книги на парних, поточний розділ на непарних.
#let running-header(meta) = context {
  let chapters = query(selector(heading.where(level: 2)).before(here()))
  let chap = if chapters.len() > 0 { chapters.last().body } else { meta.title }
  set text(font: font-sans, size: 0.68em, fill: dim, tracking: 0.03em)
  block(width: 100%, below: 0.5em)[
    #if calc.odd(counter(page).get().first()) {
      align(right, chap)
    } else {
      align(left, meta.title)
    }
    #v(0.25em, weak: true)
    #line(length: 100%, stroke: 0.4pt + hair)
  ]
}

#let running-footer() = context {
  set text(font: font-sans, size: 0.78em, fill: ink)
  let n = counter(page).get().first()
  if calc.odd(n) { align(right, str(n)) } else { align(left, str(n)) }
}

// ── Базова типографіка, спільна для всіх цілей ──────────────────────────
#let base-styles(body, size: 9.6pt, leading: 0.62em) = {
  set text(
    font: font-serif,
    size: size,
    lang: "uk",
    hyphenate: true,
    fallback: true,
  )
  set par(justify: true, leading: leading, spacing: 1.15em, first-line-indent: 0pt)
  set raw(lang: none)

  show raw: set text(font: font-mono, size: 0.86em)
  show raw.where(block: true): it => block(
    width: 100%,
    breakable: true,
    inset: (x: 0.8em, y: 0.65em),
    radius: 2pt,
    fill: panel,
    stroke: 0.4pt + hair,
    spacing: 1.2em,
    text(size: 0.98em, it),
  )

  show link: set text(fill: ink)
  show link: underline.with(stroke: 0.4pt + hair, offset: 1.6pt, evade: true)

  set table(stroke: (x, y) => (
    top: if y == 0 { 0.9pt + ink } else if y == 1 { 0.6pt + ink } else { 0.3pt + hair },
    bottom: 0pt,
  ), inset: (x: 0.5em, y: 0.42em))
  show table.cell.where(y: 0): set text(font: font-sans, size: 0.86em, weight: 600)
  show table: set text(size: 0.92em)
  show table: set align(left + horizon)
  show table: set par(justify: false)
  show table: it => block(width: 100%, spacing: 1.3em, it)

  set list(indent: 0.7em, body-indent: 0.45em, spacing: 0.72em)
  set enum(indent: 0.7em, body-indent: 0.45em, spacing: 0.72em)

  show figure.caption: set text(font: font-sans, size: 0.8em, fill: luma(25%))

  body
}

// ── Заголовки основного тіла ────────────────────────────────────────────
// рівень 1 — частина (шмуцтитул на окремій сторінці)
// рівень 2 — розділ або картка
// рівень 3+ — підрозділи, у зміст не потрапляють
#let body-headings(body) = {
  show heading: set text(font: font-sans, fill: ink, hyphenate: false)
  show heading: set par(justify: false)

  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(above: 2.2em, below: 1.6em)[
      #line(length: 100%, stroke: 1.4pt + ink)
      #v(0.6em)
      #text(size: 1.5em, weight: 700, tracking: -0.01em, it.body)
      #v(0.4em)
      #line(length: 100%, stroke: 0.5pt + ink)
      #context {
        let b = part-blurb.get()
        if b != "" [
          #v(0.9em)
          #block(width: 88%)[
            #set text(font: font-serif, size: 0.94em, fill: luma(22%))
            #set par(justify: false, leading: 0.6em)
            #emph(b)
          ]
        ]
      }
    ]
    pagebreak(weak: true)
  }

  show heading.where(level: 2): it => {
    pagebreak(weak: true)
    block(above: 0.6em, below: 1.3em)[
      #set text(size: 1.7em, weight: 700, tracking: -0.01em)
      #it.body
      #v(0.35em, weak: true)
      #line(length: 100%, stroke: 0.8pt + ink)
    ]
  }
  show heading.where(level: 3): it => block(above: 1.7em, below: 0.75em)[
    #set text(size: 1.18em, weight: 700)
    #it.body
  ]
  show heading.where(level: 4): it => block(above: 1.3em, below: 0.55em)[
    #set text(size: 1.0em, weight: 700)
    #it.body
  ]
  show heading.where(level: 5): it => block(above: 1.1em, below: 0.4em)[
    #set text(size: 0.94em, weight: 600, style: "italic")
    #it.body
  ]
  body
}

// ── Ціль: dovidnyk (A5, основне тіло) ───────────────────────────────────
#let dovidnyk(meta, body) = {
  set document(title: meta.title, author: meta.author-full)
  set page(
    paper: "a5",
    margin: (inside: 17mm, outside: 13mm, top: 14mm, bottom: 16mm),
    binding: left,
    header: running-header(meta),
    footer: running-footer(),
  )
  show: base-styles.with(size: 9.6pt)
  show: body-headings

  title-page(meta)
  colophon-front(meta)

  table-of-contents()
  counter(page).update(1)
  body
}

// ── Ціль: kartky (A4, одна картка = одна сторінка) ──────────────────────
#let kartky(meta, body) = {
  set document(title: meta.title, author: meta.author-full)
  set page(
    paper: "a4",
    margin: (x: 12mm, y: 11mm),
    header: none,
    footer: context {
      set text(font: font-sans, size: 0.72em, fill: dim)
      grid(columns: (1fr, auto),
        align(left)[#meta.title · ревізія #meta.revision],
        align(right, str(counter(page).get().first())),
      )
    },
  )
  show: base-styles.with(size: 10pt, leading: 0.58em)
  set par(spacing: 0.85em)
  show heading: set text(font: font-sans, fill: ink, hyphenate: false)
  show heading: set par(justify: false)
  show table: set block(spacing: 0.85em)
  show raw.where(block: true): set block(spacing: 0.85em)
  // Кожна картка ярусу 0 починається з нової сторінки (Р9: одна сторінка).
  show heading.where(level: 2): it => {
    pagebreak(weak: true)
    block(above: 0em, below: 0.7em)[
      #set text(size: 1.5em, weight: 700)
      #it.body
      #v(0.25em, weak: true)
      #line(length: 100%, stroke: 1.2pt + ink)
    ]
  }
  show heading.where(level: 3): it => block(above: 0.95em, below: 0.35em)[
    #set text(size: 1.05em, weight: 700)
    #it.body
  ]
  show heading.where(level: 4): it => block(above: 0.8em, below: 0.3em)[
    #set text(size: 0.96em, weight: 600)
    #it.body
  ]
  body
}

// ── Ціль: proekty (A4, ярус 2) ──────────────────────────────────────────
#let proekty(meta, body) = {
  set document(title: meta.title, author: meta.author-full)
  set page(
    paper: "a4",
    margin: (inside: 22mm, outside: 18mm, top: 18mm, bottom: 20mm),
    binding: left,
    header: running-header(meta),
    footer: running-footer(),
  )
  show: base-styles.with(size: 10.5pt, leading: 0.7em)
  show: body-headings

  title-page(meta)
  colophon-front(meta)
  table-of-contents()
  counter(page).update(1)
  body
}

// ── Кінцева сторінка ────────────────────────────────────────────────────
#let back-matter(meta) = {
  pagebreak(weak: false)
  set page(header: none, footer: none, numbering: none)
  set align(center)
  set par(justify: false)
  v(1fr)
  line(length: 30%, stroke: 0.6pt + ink)
  v(1.4em)
  text(font: font-sans, size: 1.1em, weight: 600, meta.title)
  v(0.5em)
  text(size: 0.9em, fill: dim, meta.subtitle)
  v(1.6em)
  text(size: 0.9em)[#meta.author-full]
  v(0.4em)
  text(size: 0.85em, fill: dim)[ревізія #meta.revision]
  v(1.6em)
  block(width: 78%)[
    #set text(size: 0.82em, fill: luma(25%))
    #set par(justify: false, leading: 0.6em)
    Знайшли помилку, застаріле значення або місце, де довідник вас підвів, —
    напишіть. Виправлення входять у наступну ревізію із зазначенням, що саме
    змінилося і чому.
    #v(0.9em)
    #text(font: font-mono, size: 0.94em, meta.contact)
    #v(1.4em)
    CC BY-SA 4.0 · друкуйте і роздавайте вільно
  ]
  v(1fr)
}
