# Migration worklist: transliterated tokens → English

> **transient** — a snapshot of one sweep, not a registry. Regenerate
> the numbers with `factcheck/tools/naming.py --inventory`.

Swept 2026-09-14. Six helpers over 385 files, merged and
filtered against whole-morpheme matching. The `suggest` column is the
helpers' proposal and is **not** authority: several are wrong, and the
migration should read each one before renaming.

Distinct tokens with a proposal: **94**.

| token | suggested | kind | files |
|---|---|---|---|
| `dzherelo` | `source` | parameter | 50 |
| `ne-tverdzhennya` | `not-assertion` | string-value | 49 |
| `shukaty` | `search` | string-value | 46 |
| `bulo-shukaty` | `was-seeking` | dict-key | 35 |
| `imya` | `name` | parameter | 7 |
| `KESH` | `CACHE` | constant | 7 |
| `zapysy` | `records` | variable | 7 |
| `perevirka` | `verify` | function_name | 6 |
| `klas` | `class` | string-value | 5 |
| `ryadky` | `rows` | variable | 5 |
| `samoperevirka` | `--self-check` | cli_flag | 5 |
| `odynyci` | `units` | variable | 4 |
| `verdykt` | `verdict` | variable | 4 |
| `naryad` | `order` | string-value | 3 |
| `zhyvlennya` | `power` | dict-key | 3 |
| `_kesh_tekst` | `_cache_text` | variable | 2 |
| `imya_dlya` | `name_for` | function_name | 2 |
| `nasinnya` | `seed` | variable | 2 |
| `nazva_zapysu` | `record_name` | function_name | 2 |
| `odynycya` | `unit` | dict-key | 2 |
| `prokhid` | `pass_id` | variable | 2 |
| `ryadok` | `row` | variable | 2 |
| `zapysaty` | `write` | function_name | 2 |
| `znaydeni` | `found` | function | 2 |
| `znaydeno` | `found` | variable | 2 |
| `znayty` | `find` | function_name | 2 |
| `_KESH_VZIRCIV` | `_CACHE_SAMPLES` | variable | 1 |
| `_vzirets` | `_sample` | function_name | 1 |
| `cytata` | `quote` | dict-key | 1 |
| `dzherela` | `sources` | function_name | 1 |
| `dzherelo_rozvyazne` | `source_resolved` | function_name | 1 |
| `dzherelo_vseredyni` | `source_inside` | function_name | 1 |
| `formatuvaty_dokaz` | `format_proof` | function_name | 1 |
| `IMYA` | `name` | constant | 1 |
| `kesh` | `cache` | parameter | 1 |
| `kesh_fayly` | `cache_files` | function | 1 |
| `klasy` | `statuses` | function | 1 |
| `klyuch_sortuvannya` | `sort_key` | function | 1 |
| `kontekst_bez_tverdzhennya` | `context_without_claim` | variable | 1 |
| `mira_zavdannya` | `measure_tasks` | function | 1 |
| `nalashtovana` | `configured` | variable | 1 |
| `NASINNYA` | `seed` | constant | 1 |
| `NE_OHOLOSHUVATY` | `dont_declare` | constant | 1 |
| `ne_tverdzhennya` | `not_claim` | variable | 1 |
| `NEDOSYAZHNE` | `UNREACHABLE` | variable | 1 |
| `nevrakhovani` | `unaccounted` | variable | 1 |
| `normalizuvaty` | `normalize` | function_name | 1 |
| `notatky` | `notes` | function | 1 |
| `OCHIKUVANNYA` | `expectations` | constant | 1 |
| `ODYNYCI` | `units` | constant | 1 |
| `perevir_kartky` | `check_cards` | function | 1 |
| `perevir_zapysy` | `check_records` | function | 1 |
| `perevireno` | `checked` | variable | 1 |
| `perevirka_budovy` | `verify_structure` | function_name | 1 |
| `pidtverdzheno` | `confirmed` | string-value | 1 |
| `POTREBUYE_CYTATY` | `requires_quote` | constant | 1 |
| `POYASNENNYA` | `EXPLANATION` | variable | 1 |
| `PYTANNYA` | `questions` | constant | 1 |
| `RE_CYTATA` | `quote_regex` | constant | 1 |
| `RE_DZHERELO_VSEREDYNI` | `RE_SOURCE_INSIDE` | variable | 1 |
| `RE_IMYA` | `RE_NAME` | variable | 1 |
| `RE_KOD_TVERDZHENNYA` | `RE_CLAIM_CODE` | variable | 1 |
| `RE_NE_TVERDZHENNYA` | `not_claim_regex` | constant | 1 |
| `RE_TVERDZHENNYA` | `RE_CLAIM` | variable | 1 |
| `RE_ZAPYS` | `RE_RECORD` | variable | 1 |
| `rodyny` | `families` | variable | 1 |
| `rozryad` | `rank` | variable | 1 |
| `ryadky_z_koordynat` | `rows_from_coordinates` | function_name | 1 |
| `ryadok_dlya` | `row_for` | function_name | 1 |
| `slova_vzirtsya` | `pattern_words` | function | 1 |
| `SLOVO` | `word` | constant | 1 |
| `SLOVO_V_LITERU` | `WORD_TO_LETTER` | variable | 1 |
| `STARI_VERDYKTY` | `OLD_VERDICTS` | variable | 1 |
| `tekst_dzherela` | `source_text` | function_name | 1 |
| `transliterovane` | `is_transliterated` | function | 1 |
| `TYPOVANI` | `typed` | dict | 1 |
| `uvaha` | `attention` | dict-key | 1 |
| `verdykt_z` | `verdict_from` | function | 1 |
| `vymiryuvane` | `measurement` | variable | 1 |
| `vyvesty_imya` | `output_name` | function_name | 1 |
| `vzir` | `pattern` | variable | 1 |
| `vzirets` | `pattern` | variable | 1 |
| `vzirets_dlya` | `sample_for` | function_name | 1 |
| `vzirets_z` | `pattern_from` | function | 1 |
| `VZIRTSI` | `patterns` | constant | 1 |
| `zapysaty_ledger` | `write_ledger` | function_name | 1 |
| `zapysiv` | `records` | variable | 1 |
| `znachennya` | `value` | function_name | 1 |
| `znayty_dokument` | `find_document` | function_name | 1 |
| `znayty_ryadok` | `find_row` | function_name | 1 |
| `zvedennya` | `summary` | function | 1 |
| `zvireno` | `verified` | variable | 1 |
| `zvirka` | `verify` | function_name | 1 |
| `zvirty` | `verify` | function_name | 1 |
