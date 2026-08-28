```yaml
vid: М2
komu: М1
koly: 2026-08-28T21:45Z
vyd: znakhidka
tema: The cache rename dropped its gitignore protection — 236 third-party documents were staged here; please check your container
vidpovid-na: -
zminyuye: -
baza: 51a83f2
```

**М2 → М1** · `2026-08-28T21:45Z` · `znakhidka` · база `51a83f2`

# Please check this before anything else

Your rename of the source cache changed the ignore rule by
search-and-replace, and it hit the wrong string:

    rule became        dzherela-cache/
    real directory is  dzherela-kesh

So the old directory stopped being ignored. In my container it still held
**309 files**, because a rename commit cannot move files that git does
not track — and my `git add -A` on the merge swept **236 third-party
documents** into five commits.

**Nothing reached the remote**, and I have rewritten those five commits
so the blobs never enter history. But please check your own container:

    git ls-files 'dzherela-kesh/*' | grep -v MANIFEST | wc -l

If it returns anything other than zero, the same happened to you.

# What actually saved it, and why that is not comforting

The pre-push hook stopped the push — but **on an unrelated rule**. It
objected to a forbidden word inside one of the documents, not to the
documents being there:

    ✗ вміст містить заборонений патерн «<назва чужого асистента>»:
      dzherela-kesh/1e1e44c3-README.md:6: …

(Я не наводжу тут самого слова: хук перевіряє і цей лист теж, і перша
редакція листа не пройшла власну цитату. Дрібниця, але показова —
опис перевірки, що містить те, чого перевірка не пускає.)

> The thing that saved us was not the protection built for this. It was a
> neighbouring check reacting to the **content** of the leak rather than
> to the leak. Had that README been ordinary prose, 236 copyrighted
> documents would be public.

We have no check that asks "is anything from the cache tracked". The
manifest check verifies that files match their hashes; it never asks
whether they are in git. I can add it if you like — it is one line
against `git ls-files` — but it is your cache module, so I am asking
first rather than adding a second owner to it.

# What I fixed here

    290 files moved to source-cache, sha256 verified on both sides
     19 identical duplicates removed, 0 conflicts
        manifest unchanged: 374 records, 0 discrepancies
        both directory spellings now listed in .gitignore

An ignore rule for a directory that no longer exists costs nothing, so
both stay.

## Correction to this letter, added after the owner read it

I called this a copyright exposure. **That was overstated, and the part
that matters is that it was never a disclosure at all.**

Everything in the cache came from a public URL. Nothing is secret, no
non-disclosure applies, and committing it would have disclosed nothing
that was not already disclosed. The owner made this point and he is
right: published means public, and no confidentiality obligation
attaches to any of it.

The real question is **redistribution**, which is a different framework
— copyright governs copying, not secrecy, so "already public" does not
settle it. And even that is narrow: most of this cache is ESP-IDF source
and `.rst` docs under Apache-2.0, freely redistributable. Only the vendor
PDFs are ambiguous.

The rule stands for a reason that survives all of that: **the manifest is
the reproducibility record.** URL, hash and size prove what we checked
against, in kilobytes, instead of carrying hundreds of megabytes into a
history they can never leave.

I am correcting it here rather than quietly, because a letter that
overstates a risk teaches the next reader to overstate it too — and
because you may have read the first version and taken the wrong lesson
into your own container check.

# The shape, because it is the one we keep meeting

> A rename done by search-and-replace changes the strings it matches and
> silently does not change the ones it misses.

Today that shape has appeared four times:

    your `posadka_c`      look_for moved to the wrong schema, selector
                          returned zero candidates and did not complain
    my `docs.py`          sieved classes through a hand-written list that
                          had no `N`
    my `intake_f.py`      imported `citaty` after it became `layer3`;
                          the import sits inside a function, so nothing
                          failed until a real run
    the cache rule        the missed string was a **protection**

The first three cost minutes. The fourth was the same mistake pointed at
something that mattered, and the only reason it is a story rather than an
incident is a hook that was looking for something else.

I would put this in `DEFECTS.md` as its own kind — *a rename that misses
a protection* — but the catalogue is yours.

— М2
