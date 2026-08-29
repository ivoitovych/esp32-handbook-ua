#!/usr/bin/env python3
"""Consistency gate over the foundation documents.

## Why this exists

The owner's complaint, measured and confirmed: *"the technology keeps
drifting — we find new classes of problem and forget the ones already
found."*

On 2026-08-28 the class vocabulary lived in **three** documents and all
three had drifted apart; the two newest classes were missing from both
non-authoritative copies. That was found by reading. Reading does not
scale and does not run in CI.

Two answers were considered and rejected:

* **merge every document into one.** A three-thousand-line file is not
  re-read whole by anybody, so drift stops being visible instead of
  stopping.
* **move content between documents on a fixed cadence.** That is a
  discipline, and this project's own law says disciplines do not hold:
  *stated mechanics hold, a named prohibition does not.* A cadence is a
  prohibition against drift.

What holds is a check. This is the check.

## What it verifies

    vocabulary   every class letter a document names must exist in the
                 code, and every code class must appear in the
                 authoritative document
    tools        every `tools/*.py` a document names must exist
    verdicts     every verdict a work-order template offers must be one
                 the intake gate knows how to check
    defects      every defect kind referenced by number must exist

## What it deliberately does NOT verify

Prose. Two documents may explain the same idea in different words and
that is not drift — `HELPERS.md` is the raw log and `METHOD.md` is
the distilled law, and both say so in their first lines. Only **facts
with one right answer** are checked here.

    tools/docs.py            check
    tools/docs.py --proba    show the check working on broken input
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FC = ROOT / "factcheck"
sys.path.insert(0, str(ROOT / "tools"))

# Хто нормативний для якого факту. Без цього рядка «полагоджують ту
# копію, що читається», і копії розходяться далі.
VLASNYK = {
    "класи доказу": "SCHEMA.md",
    "роди хиб": "DEFECTS.md",
    "вердикти наряду": "tools/intake_f.py",
}

# «Керівний» тут — не те саме, що `canonical` у `doc_kind.py`, і два
# переліки навмисно не збігаються. `doc_kind` питає, **хто власник
# змісту**: історичний документ заморожений і правити його не можна.
# Цей перелік питає інше — **чиї посилання мають лишатися дійсними**, а
# заморожений документ, що називає перейменований інструмент, бреше
# читачеві так само, як живий. Тому історичні тут є, і це не розбіжність
# воріт, а два різні питання про один файл.
#
# Теки кешу, яких у ЦЬОМУ дереві вже немає, а в чужому контейнері ще
# можуть бути. Це історія, а не означення: означення нижче, у
# `kesh_ne_v_git`, і воно питає про наявність маніфесту. Ці рядки не
# перейменовує ніщо — перейменувати минуле не можна.
HISTORICAL_CACHES = ("dzherela-kesh",)

KERIVNI = ["METHOD.md", "DEFECTS.md", "LESSONS-M2.md", "RETROSPECTIVE.md",
           "SCHEMA.md", "ARCHITECTURE.md", "HELPERS.md", "README.md",
           "MIGRATION.md", "TASK-SPEC.md",
           "REFUTED.md", "SOURCES.md", "WAVE-W1.md"]

# Той самий прохід sed, що позначив був `TASK-SPEC.md` історичним у
# `doc_kind.ISTORYCHNI`, лишив по собі **другий** слід — тут. Обидва
# рядки з `WORK-ORDER-EXAMPLE.md` (документ видалено як застарілий)
# стали `TASK-SPEC.md`, і перелік почав звітувати «14 керівних», маючи
# 13 різних. Число, яке друкує сам перелік, розійшлося з переліком.
#
# М2 знайшли й виправили випадок у `doc_kind`; цей уцілів, бо ніхто не
# питав. Тому питаємо: перевірка нижче не пускає ані дубль, ані ім'я
# неіснуючого документа.


def governing_list_sound() -> list[str]:
    """Перелік керівних — це перелік ІМЕН, і його ніхто не звіряв.

    Рід 26 у чистому вигляді, вдруге за день і в іншому файлі: прохід
    перейменування переписує ім'я, чиїм предметом було старе ім'я, і
    жодна перевірка про це не питає, бо всі питають про **зміст**
    документів, а не про сам перелік.

        KERIVNI  14 записів, 13 різних
    """
    bidy = []
    for n in sorted(set(KERIVNI)):
        if KERIVNI.count(n) > 1:
            bidy.append(f"KERIVNI: `{n}` названо {KERIVNI.count(n)} рази — "
                        f"слід перейменування, а не перелік")
        if not (FC / n).exists():
            bidy.append(f"KERIVNI: `{n}` у переліку є, документа немає")
    return bidy

# Рядок, що перелічує класи. ФОРМАТІВ ТРИ, і це не примха:
#
#     | **A** | ✅ | …        SCHEMA.md
#     | `A`   | …            ARCHITECTURE.md (до 2026-08-28)
#         A  primary …       METHOD.md
#
# Перша редакція знала лише перший. Прогін на дереві до правок зловив
# METHOD.md і НЕ зловив ARCHITECTURE.md — саме той документ, з якого
# все й почалося. Перевірка з однією формою бачить одну форму, і
# мовчить про решту так само впевнено.
# Тільки таблиця під заголовком про стани, а не будь-яка таблиця в
# документі. Перша редакція шукала `| **слово** |` по всьому файлу й
# зібрала імена полів запису та роди одиниць — тобто «класи», яких у
# коді немає, бо вони й не класи.
RE_ROZDIL_STANIV = re.compile(
    r"^##+ .*(Класи доказу|Стани перевірки|Стани)\s*$", re.M)
RE_KLAS_TABL = re.compile(
    r"^\|\s*(?:\*\*([a-z][a-z-]{3,})\*\*|`([a-z][a-z-]{3,})`)\s*\|", re.M)


def rozdil_staniv(t: str) -> str:
    """Текст лише того розділу, що описує стани."""
    m = RE_ROZDIL_STANIV.search(t)
    if not m:
        return ""
    dali = re.search(r"^##+ ", t[m.end():], re.M)
    return t[m.end():m.end() + (dali.start() if dali else len(t))]
RE_KLAS_SPYS = re.compile(r"^\s{2,}([a-z][a-z-]{3,})\s{2,}[—a-zа-яїєґ]", re.M)
RE_TUL = re.compile(r"`?(tools/[a-z0-9_.-]+\.py)`?")
RE_RID = re.compile(r"(?:рід|kind)\s+(\d{1,2})\b", re.I)


def klasy_kodu() -> set[str]:
    """Чинний словник станів — СЛОВАМИ.

    Був літерами до 2026-08-29. Літери прибрано з реєстру як
    абревіатуру: одинадцять однобуквених кодів вимагають легенди, якої
    ніхто не тримає в голові, а поруч із ними завжди стояло те саме
    слово й той самий опис.
    """
    import factcheck
    return set(factcheck.STATUSES)


def perevirka() -> list[str]:
    bidy: list[str] = []
    kod = klasy_kodu()
    avt = (FC / VLASNYK["класи доказу"]).read_text(encoding="utf-8")
    avt_klasy = {a or b for a, b in RE_KLAS_TABL.findall(rozdil_staniv(avt))}

    brak = kod - avt_klasy
    if brak:
        bidy.append(
            f"{VLASNYK['класи доказу']}: нормативний перелік не знає класів "
            f"{sorted(brak)}, які є в коді")
    zayvi = avt_klasy - kod
    if zayvi:
        bidy.append(
            f"{VLASNYK['класи доказу']}: перелічено класи {sorted(zayvi)}, "
            f"яких у коді немає")

    for imya in KERIVNI:
        p = FC / imya
        if not p.exists():
            bidy.append(f"{imya}: керівний документ відсутній")
            continue
        t = p.read_text(encoding="utf-8")

        # Копія словника класів, що розійшлася з кодом.
        nazvani = ({a or b for a, b in RE_KLAS_TABL.findall(rozdil_staniv(t))}
                   | set(RE_KLAS_SPYS.findall(t)))
        # Просіювати ТИМ, ЩО В КОДІ, і ніколи власним переліком.
        #
        # Тут стояло `set("ABCDEFGKLS")` — свій список літер, вписаний
        # рукою. М1 завів клас `N`, і перевірка, зроблена проти
        # застарілих копій словника, СХОВАЛА його власною застарілою
        # копією: `N` випадав із «названих» і одразу з'являвся у
        # «відсутніх». Документ був правий, перевірка ні.
        #
        # Формулювання М1, точніше за моє: перевірка **маскувала `N` до
        # порівняння — і не побачила б виправлення, якого сама
        # вимагала.**
        #
        # Знайшли ми це нарізно й полагодили однаково, з різницею в
        # кілька хвилин. Копія жила всередині інструмента, побудованого
        # проти копій.
        nazvani &= kod
        if len(nazvani) >= 4 and imya != VLASNYK["класи доказу"]:
            vidsutni = kod - nazvani
            if vidsutni:
                bidy.append(
                    f"{imya}: копія словника класів без {sorted(vidsutni)} — "
                    f"або доповнити, або замінити посиланням на "
                    f"{VLASNYK['класи доказу']}")

        for tul in set(RE_TUL.findall(t)):
            if not (ROOT / tul).exists():
                bidy.append(f"{imya}: названо неіснуючий {tul}")

        for n in set(RE_RID.findall(t)):
            if imya == VLASNYK["роди хиб"]:
                continue
            if not re.search(rf"^## {n}\.", (FC / VLASNYK["роди хиб"])
                             .read_text(encoding="utf-8"), re.M):
                bidy.append(f"{imya}: посилання на рід {n}, якого немає в "
                            f"{VLASNYK['роди хиб']}")

    # Вердикти наряду проти воріт, які їх приймають.
    try:
        import intake_f
        znani = set(intake_f.POTREBUYE)
    except Exception as e:
        bidy.append(f"ворота не імпортуються: {str(e)[:60]}")
        znani = set()
    # Вердикти більше не живуть у шаблоні інструмента: вони в
    # `factcheck/TASK-SPEC.md`, звідки наряд їх складає. Перевірка
    # читає **джерело**, а не одну з копій — інакше вона стереже
    # копію й мовчить про решту.
    if znani:
        try:
            import task_spec
            bloky = task_spec.bloky()
        except Exception as e:
            bidy.append(f"спека завдання не читається: {str(e)[:60]}")
            bloky = {}
        for imya, tekst in bloky.items():
            if not imya.startswith("VERDICTS"):
                continue
            vsi = set(re.findall(r"^\| `([a-z_-]+)` \|", tekst, re.M))
            chuzhi = vsi - znani
            if chuzhi:
                bidy.append(
                    f"TASK-SPEC [{imya}]: наряд пропонує вердикти "
                    f"{sorted(chuzhi)}, яких ворота не перевіряють")
    bidy += governing_list_sound()
    bidy += index_complete()
    bidy += kesh_ne_v_git()
    return bidy


def index_complete() -> list[str]:
    """Чи згадує покажчик `README.md` кожен документ теки.

    Знайдено виміром, а не на око: **17 із 32** документів не було в
    покажчику, і серед них `METHOD.md`, `RETROSPECTIVE.md`,
    `MIGRATION.md`, `TASK-SPEC.md` — тобто вся англійська половина
    технології. Читач, якому README каже «починайте звідси», не мав
    звідки дізнатися, що вони існують.

    Це рід 3 у нашому ж каталозі, вивернутий навиворіт: не нуль, що
    нічого не рахує, а покажчик, який мовчить про те, чого не назвали.
    Документ, якого немає в покажчику, не «менш важливий» — він
    невидимий, і невидимість не є рішенням.
    """
    rd = (FC / "README.md").read_text(encoding="utf-8")
    nema = [p.name for p in sorted(FC.glob("*.md")) if p.name not in rd]
    bidy = [f"README.md: покажчик не називає {n}" for n in nema]
    # І в другий бік. «Кожен документ названо» не те саме, що «покажчик
    # правдивий»: той самий прохід sed, що зіпсував `KERIVNI`, поставив
    # `TASK-SPEC.md` **двічі** — раз у керівні, раз у історичні, куди він
    # потрапив замість видаленого `WORK-ORDER-EXAMPLE.md`. Покажчик
    # називав документ і одразу суперечив собі про його рід, а перевірка
    # мовчала, бо ім'я в тексті було.
    m = re.search(r"```\n(factcheck/.*?)```", rd, re.S)
    if m:
        imena = re.findall(r"^\s{4}([A-Za-z0-9._-]+\.md)", m.group(1), re.M)
        for n in sorted(set(imena)):
            if imena.count(n) > 1:
                bidy.append(f"README.md: покажчик називає {n} "
                            f"{imena.count(n)} рази — рід не може бути двома")
            if not (FC / n).exists():
                bidy.append(f"README.md: покажчик називає {n}, "
                            f"а документа немає")
    return bidy


def proba() -> int:
    """Показ на зіпсованому вході. Перевірка, що жодного разу не
    спрацювала, невідрізненна від перевірки, якої немає."""
    import tempfile
    global FC
    spravzhnya = FC
    vypadky = [
        ("документ називає неіснуючий тул",
         {"METHOD.md": "див. `tools/nemaye-takoho.py`\n"}, True),
        ("документ посилається на неіснуючий рід",
         {"METHOD.md": "це рід 99 каталогу\n"}, True),
        ("чистий документ", {"METHOD.md": "нічого особливого\n"}, False),
    ]
    provaliv = 0
    for nazva, fajly, ocik in vypadky:
        with tempfile.TemporaryDirectory() as d:
            t = Path(d)
            for imya in KERIVNI:
                (t / imya).write_text((spravzhnya / imya).read_text("utf-8")
                                      if imya not in fajly else fajly[imya],
                                      encoding="utf-8")
            FC = t
            try:
                b = [x for x in perevirka() if "METHOD.md" in x]
            finally:
                FC = spravzhnya
            spiymav = bool(b)
            ok = "✓" if spiymav == ocik else "✗ ПРОВАЛ"
            print("   %s %-42s очікувано %-5s дістав %s"
                  % (ok, nazva, ocik, spiymav))
            provaliv += spiymav != ocik
    provaliv += cache_selftest()
    print("\nпровалів: %d" % provaliv)
    return 1 if provaliv else 0


def cache_selftest() -> int:
    """Ворота на кеш проти теки, чиє ім'я не стоїть у жодному файлі.

    Ім'я тут навмисно вигадане й ніде більше не трапляється. Саме це
    й перевіряється: якби означення кешу знову звелося до переліку
    імен, ця проба провалилася б **першою** — а перелік, який стереже
    лише те, що в ньому названо, від наступного перейменування не
    рятує (знахідка М2, рід 26 проти самих воріт).
    """
    import subprocess
    import tempfile
    global ROOT
    spravzhniy = ROOT
    provaliv = 0
    with tempfile.TemporaryDirectory() as d:
        t = Path(d)
        subprocess.run(["git", "init", "-q"], cwd=t)
        vypadky = [("кеш під невигаданим досі іменем", True),
                   ("та сама тека, лише маніфест", False)]
        (t / "kesh-yakoho-nikoly-ne-bulo").mkdir()
        (t / "kesh-yakoho-nikoly-ne-bulo" / "MANIFEST.md").write_text(
            "# manifest\n", encoding="utf-8")
        (t / "kesh-yakoho-nikoly-ne-bulo" / "chuzhyy.pdf").write_text(
            "x\n", encoding="utf-8")
        ROOT = t
        try:
            for nazva, ocik in vypadky:
                if not ocik:
                    (t / "kesh-yakoho-nikoly-ne-bulo" / "chuzhyy.pdf").unlink()
                    subprocess.run(["git", "rm", "-q", "--cached",
                                    "kesh-yakoho-nikoly-ne-bulo/chuzhyy.pdf"],
                                   cwd=t, capture_output=True)
                else:
                    subprocess.run(["git", "add", "-A"], cwd=t,
                                   capture_output=True)
                spiymav = bool(kesh_ne_v_git())
                ok = "✓" if spiymav == ocik else "✗ ПРОВАЛ"
                print("   %s %-42s очікувано %-5s дістав %s"
                      % (ok, nazva, ocik, spiymav))
                provaliv += spiymav != ocik
        finally:
            ROOT = spravzhniy
    return provaliv


def main() -> int:
    if "--proba" in sys.argv:
        return proba()
    bidy = perevirka()
    for b in bidy:
        print("   ✗ " + b)
    print("\ndocs: керівних документів %d, розбіжностей %d"
          % (len(KERIVNI), len(bidy)))
    return 1 if bidy else 0


def kesh_ne_v_git() -> list[str]:
    """Жоден файл кешу, крім маніфесту, не має бути відстеженим.

    Інцидент 2026-08-28: перейменування `dzherela-kesh` → `source-cache`
    переписало в `.gitignore` **обидва** рядки на цей шлях, зокрема той,
    чиїм предметом було старе ім'я. У контейнері, де робили
    перейменування, старого каталогу вже не було, тож наслідку не було
    видно взагалі. У другого супровідника він лишався — і 236 чужих
    документів опинилися в індексі. Спіймано вчасно, у git не потрапило.

    > Правило ігнорування для шляху — це твердження про всіх, у кого
    > той шлях **ще є**. Перейменувати його означає зняти захист рівно
    > там, де він потрібен, і ніколи там, де перейменування робили.

    Тому це не перевірка `.gitignore`, а перевірка **наслідку**:
    питаємо git, що він відстежує, а не читаємо правила й не віримо їм.
    Рід 26 у `DEFECTS.md`.

    ## Друга редакція: перша була вразлива до тієї самої вади

    Знахідка М2 від `05:26Z`, і вони її випробували, а не вичитали. У
    першій редакції теки кешу стояли переліком просто тут:

        git ls-files -- source-cache dzherela-kesh

    Вони поклали відстежений файл у `sources-v3/` — ворота промовчали.

    > Ворота, збудовані проти роду 26, вразливі до роду 26: перелік імен
    > усередині них **сам є копією імені шляху**, і наступне
    > перейменування або перепише його (знявши покриття зі старого
    > імені), або промине нове.

    Тому кеш **оголошує себе сам** — тим самим способом, яким наші
    породжені документи називають свій генератор, а всі документи —
    свій рід:

    > **Тека, у якій лежить `MANIFEST.md`, є кешем.**

    Перелік імен лишається, але вже не як означення кешу, а як
    **історія**: `dzherela-kesh` більше ніде не існує й існувати не
    буде, і саме тому його треба назвати — у чужому контейнері він ще
    є. Ці рядки не переписує жодне перейменування; вони описують минуле,
    а минуле не перейменовують.

    Чого ця форма **не** ловить, і це сказано вголос: теку кешу без
    маніфесту. Такої в нас немає й бути не має — маніфест і є те, заради
    чого кеш існує, — але перевірка про неї не знає.
    """
    import subprocess
    teky = set(HISTORICAL_CACHES)
    for p in ROOT.rglob("MANIFEST.md"):
        if ".git/" in p.as_posix():
            continue
        teky.add(p.parent.relative_to(ROOT).as_posix())
    r = subprocess.run(["git", "ls-files"], cwd=ROOT,
                       capture_output=True, text=True)
    for x in r.stdout.split():
        if x.endswith("/MANIFEST.md"):
            teky.add(x.rsplit("/", 1)[0])
    if not teky:
        return []
    r = subprocess.run(["git", "ls-files", "--", *sorted(teky)], cwd=ROOT,
                       capture_output=True, text=True)
    lyshni = [x for x in r.stdout.split()
              if x and not x.endswith("/MANIFEST.md")]
    if not lyshni:
        return []
    return [f"у git відстежено {len(lyshni)} файлів кешу — має бути лише "
            f"MANIFEST.md; перші: {', '.join(lyshni[:3])}"]


if __name__ == "__main__":
    sys.exit(main())
