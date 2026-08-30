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

    factcheck/tools/docs.py            check
    factcheck/tools/docs.py --proba    show the check working on broken input
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import repo
from repo import ROOT  # noqa: E402  (root is found, not counted)
FC = ROOT / "factcheck"
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Хто нормативний для якого факту. Без цього рядка «полагоджують ту
# копію, що читається», і копії розходяться далі.
# Донедавна тут стояли три різні документи — по власнику на кожне
# питання. Після зведення двоє з трьох — це той самий `METHOD.md`, і
# `name_lists` слушно вилаявся на дубль: повторене ім'я в такому переліку
# майже завжди означає, що заміна злила два записи в один (рід 26).
#
# Тут не злиття, а справжнє зведення: власник справді один. Тож замість
# двох однакових значень — один запис, і код питає його обидва рази.
VLASNYK = {
    "технологія": "METHOD.md",
    "вердикти наряду": "factcheck/tools/intake_f.py",
}
VLASNYK["класи доказу"] = VLASNYK["роди хиб"] = VLASNYK["технологія"]

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

# Керівні документи — ті, що описують ТЕХНОЛОГІЮ, і вони лежать у
# корені `factcheck/`. Усе інше після перебудови 2026-08-29 має свою
# теку за родом: `reports/`, `history/`, `book/`, `runs/`.
#
# Перелік лишається явним, а не `glob`, навмисно: він є ТВЕРДЖЕННЯМ про
# те, що технологія складається саме з цих документів. Файл, який хтось
# додасть у корінь, має або потрапити сюди свідомо, або лежати в теці за
# родом — і `name_lists.py` стежить, щоб ім'я тут не стало іменем нічого.
KERIVNI = ["METHOD.md", "REPORT.md"]

# `README.md` не керівний документ: він нічого не вирішує й нікуди не
# переїжджає — на іншій книзі його пишуть заново. Але в корені він
# мусить бути, і це різні питання:
#
#     KERIVNI       що є технологією і що переноситься
#     U_KORENI      що людина має побачити, відкривши теку
#
# Перший раз я їх злив і викинув README разом із покажчиком, бо «два
# файли не потребують карти». Покажчик справді не потрібен; орієнтир —
# потрібен, і власник сказав це прямо. Карта й вивіска — не те саме.
U_KORENI = KERIVNI + ["README.md"]

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
#     | `A`   | …            ARCHITECTURE.md (документ згорнуто 2026-08-29)
#         A  primary …       METHOD.md
#
# Перша редакція знала лише перший. Прогін на дереві до правок зловив
# METHOD.md і НЕ зловив ARCHITECTURE.md — саме той документ, з якого
# все й почалося. Перевірка з однією формою бачить одну форму, і
# мовчить про решту так само впевнено.
#
# УВАГА: цей коментар протиставляє ДВА документи, і суцільна заміна
# `ARCHITECTURE.md` → `METHOD.md` під час згортання зробила з нього
# «зловив METHOD.md і не зловив METHOD.md» — речення без змісту. Ім'я
# згорнутого документа тут не посилання, а **свідчення про минуле**;
# рід 26, і `name_lists.py` цього не ловить, бо це проза, а не перелік.
# Тільки таблиця під заголовком про стани, а не будь-яка таблиця в
# документі. Перша редакція шукала `| **слово** |` по всьому файлу й
# зібрала імена полів запису та роди одиниць — тобто «класи», яких у
# коді немає, бо вони й не класи.
# Заголовок розділу — теж ім'я, і воно переїжджає разом із документом.
# Коли `SCHEMA.md` став англійським, цей взірець перестав знаходити
# розділ узагалі, `rozdil_staniv` повернув порожній рядок, і перевірка
# доповіла, що нормативний перелік не знає ЖОДНОГО стану з коду. Тобто
# найгучніший можливий висновок — з того, що вона нічого не прочитала.
#
# Це рід 26 у формі, якої ми ще не бачили: перейменування переписало не
# правило, а **предмет** правила, і правило лишилося цілим і сліпим.
RE_ROZDIL_STANIV = re.compile(
    r"^##+ .*(Класи доказу|Стани перевірки|Стани"
    r"|Evidence statuses|Statuses)\s*$", re.M)
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
# Тули живуть у двох теках. Взірець без `factcheck/` не просто промахує
# — він ЛОВИТЬ підрядок `tools/layer3.py` усередині
# `factcheck/tools/layer3.py`, перевіряє неіснуючий шлях і оголошує
# справний документ хибним. Промах ще видно; хибне влучання — ні.
RE_TUL = re.compile(r"`?((?:factcheck/)?tools/[a-z0-9_.-]+\.py)`?")
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
    rozdil = rozdil_staniv(avt)

    # Порожній розділ і розділ без жодного стану — різні події, і
    # плутати їх дорого. Коли `SCHEMA.md` переклали, взірець заголовка
    # перестав його знаходити, `rozdil` став порожнім — і перевірка
    # доповіла «перелік не знає одинадцяти станів», тобто зробила
    # найгучніший висновок із того, що не прочитала нічого.
    #
    # Нуль, отриманий від порожнього входу, не є виміром. Кажемо це
    # окремим рядком, щоб наступного разу було видно, який саме.
    if not rozdil.strip():
        return [f"{VLASNYK['класи доказу']}: розділу зі станами не "
                f"знайдено — переклали заголовок? Перевірка станів "
                f"НЕ виконана, а не пройдена"]
    avt_klasy = {a or b for a, b in RE_KLAS_TABL.findall(rozdil)}

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
            if not re.search(rf"^#{{2,3}} {n}\.", (FC / VLASNYK["роди хиб"])
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
    bidy += root_holds_only_governing()
    return bidy


def root_holds_only_governing() -> list[str]:
    """Чи лишається в корені `factcheck/` **лише** те, що переноситься.

    Перебудова 2026-08-29 звела корінь із 31 документа до шести — і
    майже одразу з'ясувалося, що переїзд був наполовину. Одинадцять
    інструментів далі тримали в сталій шлях `factcheck/X.md`, хоч їхні
    ж рядки допомоги вже казали `factcheck/reports/X.md`. Файли
    переїхали; ті, хто їх пише, — ні.

    Це гірше за звичайну розбіжність опису з кодом: жоден із них не
    впав би. Наступний прогін просто **створив би корінний файл
    наново**, тихо, і за тиждень у корені знову лежало б тридцять
    документів — а `git status` показував би не помилку, а роботу.

    Тому перевірка питає обидва боки:
      * що лежить у корені зараз;
      * і що будь-який інструмент **збирається** туди записати.

    Другий бік ловить ваду в день, коли її внесли, а не в день, коли
    вона вперше спрацювала.

    **Чого другий бік не вміє.** Він читає вихідний текст, а не те, що
    станеться на виконанні. Шлях, зібраний із даних —
    `katalog / imya` — він не побачить; шлях, написаний літералом у
    тимчасовому дереві, він порахує порушенням, хоч воно не порушення
    (так і сталося з показом у `language.py`). Тобто він міряє **намір,
    записаний літералом**, і про решту мовчить. Записано тут, бо міра,
    що ховає свою межу, сама була б родом 3."""
    bidy = []
    dozvoleni = set(U_KORENI)
    for p in sorted(FC.glob("*.md")):
        if p.name not in dozvoleni:
            bidy.append(f"{p.name}: лежить у корені factcheck/, "
                        f"а корінь тримає лише керівні документи")
    vzir = re.compile(r'"factcheck"\s*/\s*"([A-Z][A-Z0-9-]*\.md)"')
    for t in repo.tool_files():
        for imya in set(vzir.findall(t.read_text(encoding="utf-8"))):
            if imya not in dozvoleni:
                bidy.append(f"tools/{t.name}: пише {imya} в корінь "
                            f"factcheck/, а там лише керівні документи")
    return bidy


def index_complete() -> list[str]:
    """Раніше — чи згадує покажчик `README.md` кожен документ теки.

    Покажчик існував тому, що документів було шість і без карти читач не
    знав, який відкривати. Власник назвав це вадою, а не зручністю:
    «тека має містити два документи», і тоді покажчик описує те, що й
    так видно з `ls`.

    Перевірку знято разом із покажчиком. Лишати її означало б тримати
    механізм, чий предмет скасовано, — а такий механізм не мовчить, він
    падає на порожньому вході й виглядає як поломка.

    Її роботу перебрали дві інші: `root_holds_only_governing` не пускає
    в корінь нічого, крім двох документів, а `name_lists` стежить, щоб
    ім'я в переліку було іменем наявного файлу."""
    return []

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
        # «Чистий» випадок раніше підставляв заглушку на два слова. Поки
        # METHOD.md був лише міркуванням, заглушка справді була чистою.
        # Після зведення METHOD.md ВОЛОДІЄ переліком станів — і заглушка
        # стала порушенням, слушно: документа без розділу станів не буває.
        #
        # Тобто випадок перевіряв не «чистий документ», а «документ, у
        # якому нема чого перевіряти». Різницю видно лише тоді, коли
        # предмет перевірки переїжджає в той самий файл.
        ("чистий документ",
         {"METHOD.md": (spravzhnya / "METHOD.md").read_text("utf-8")
                       + "\n\nНічого особливого.\n"}, False),
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
