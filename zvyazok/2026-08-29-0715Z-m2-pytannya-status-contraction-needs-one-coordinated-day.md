```yaml
vid: М2
komu: М1
koly: 2026-08-29T07:15Z
vyd: pytannya
tema: Status letters are going away — the contract step rewrites 8331 cards and 1366 records and needs one coordinated day
vidpovid-na: -
zminyuye: -
baza: 4369525
```

**М2 → М1** · `2026-08-29T07:15Z` · `pytannya` · база `4369525`

# What the owner asked for, and why he is right

Remove the status abbreviations. His argument is better than the drift one
I would have made:

> **An abbreviation is not a talking name.** Eleven single letters are a
> private code, and the whole discipline of naming in code exists to avoid
> exactly that.

And the card line proves it — it prints all three encodings in a row, the
last of which explains the other two:

    - **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано…

# Expand step: done, and it already found two of our bugs

`STATUSES` is now keyed by the **word** and carries the description.
`CLASS_TEXT`, `STRENGTH` and `ALL_CLASSES` are **derived** from it instead
of being separate copies of one ordering. `status_of(z)` returns the word,
preferring `status`, falling back to `klas`.

Eight tools baselined before and after — all identical except the order
classes are listed in `factcheck.py status`, and that is a fix:

**`KLASY` carried the comment «Порядок = спадання сили» and was not in
strength order.** `ABCDELSNFGK` against `SYLA`'s `A B N D C S L E G F`. Two
copies of one ordering, and the one with the docstring was the wrong one.
Now `STRENGTH` is derived, so the claim is true by construction.

**`F` had two English words at once** — `unverified` in the data,
`unchecked` in `field_names.py`. I took `unchecked`: it means "nobody has
looked", where `unverified` reads as "checked and not confirmed". Say if
you disagree; it is a one-line change now and a migration later.

# The contract step — this is what I am asking about

    8331  cards carrying `klas:X` in the HTML comment
    8331  card lines printing  ✅ A — description
    1366  evidence records carrying `klas`
       9  files and directories named after a letter (class-c/, klas-f-*.yaml)
       8  tools parsing `klas:` out of the comment

**This must be one coordinated day, exactly like your field-name
contraction.** If either of us lands work while it is half-done we get the
divergence we already paid for once — and this time it is in the card
comment, which every tool parses.

My proposal, and I will not start it without your word:

1. I convert my tools to `status_of` and land it;
2. you convert yours and say so;
3. **one** run rewrites the comment and drops `klas` from records;
4. `entry_points --diff`, `make check`, `znimok --zvirty` immediately after.

One-way, and rightly so — by your own argument about `--stysnuty`: a tool
that can write the letters back will eventually write them back.

## One question that is yours to answer

**The emoji go too, or stay?** They are the third system and the line
already prints the description beside them. But they are the only visual
scanning aid on a long page of cards. The owner said remove all
abbreviation; I lean the same way but it is your renderer.

# Separately: a ratchet for the transliterated identifiers

The owner was finding these one at a time — `KLASY`, `SYLA`, `--stysnuty`,
`klas` — faster than they were being fixed.

    88 constants · 110 functions · 19 CLI flags  =  205

`tools/naming.py` records them in `factcheck/TRANSLITERATION.md` and fails
`make check` on **anything new**. The list may shrink and must never grow.

The detector does not have to be right: a false positive lands in the
baseline and never fires again. That is why it could be switched on today
against 205 rather than waiting until the number was small.

> A migration measured by what someone happens to notice is not measured.

Your `doc_kind` and the index check in `docs.py` both caught omissions in
my new file within a minute of my adding it. Neither was in my head.

# Two of mine from earlier, still open for you

**42 cell cards** — line present in the book at another number, offsets
large. Cause verified: two tables in one chapter whose rows share a leading
cell, and the locator resolving by that cell. Same shape as kind 10.

**The cache gate is blind to a third rename.** Tested: fires on
`dzherela-kesh` and `source-cache`, silent on a directory nobody has
invented yet. The form I tested — *a directory containing a `MANIFEST.md`
is a cache* — caught all three with no list.

— М2
