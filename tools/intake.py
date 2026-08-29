#!/usr/bin/env python3
"""Приймання М2: чотири механічні умови, які запис має пройти до коміту.

Не плутати з `tools/factcheck.py vorota` — ті ворота випускні, вони
питають, чи можна друкувати книгу. Ці — вхідні: чи можна взагалі
класти цей доказ у реєстр. Дефект дешевше не впустити, ніж потім
виловлювати.

Умови:
  1. YAML читається;
  2. джерело не є файлом самої книги (крім класу E й позначених
     внутрішніх звірок — див. нижче);
  3. клас A або B має непорожню cytata;
  4. взірець `zbih` компілюється — і цілком, і кожною альтернативою;
  4а. взірець не збігається з чужим текстом (див. KONTROLNI);
  4б. жодна альтернатива не є ТЕЧЕЮ — не чіпляє більше, ніж усі інші
      разом, і при цьому багато;
  5. клас E не стоїть на твердженні з числом, адресою чи GPIO
     — це не помилка, а привід переглянути: покажчик і власне
     вимірювання автора законно лишаються E.
"""
import glob, os, re, sys
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "tools"))
import factcheck  # розбір альтернатив взірця беремо в М1

KNYHA = re.compile(r'\b(manual|dodatky|kartky)/[a-z0-9]')

# Книга як джерело, названа СЛОВАМИ, а не шляхом.
#
# `KNYHA` ловить лише `manual/…`, `dodatky/…`, `kartky/…`. Але джерело
# пишуть і прозою: «Розділ 29 «Wi-Fi мовчить»», «Картка К13 (розділ 06)»,
# «Додаток F, рядок 47». Це та сама книга, і для класу A чи B це те саме
# самоцитування — а ворота його не бачили.
#
# Виміряно 2026-08-28: таких записів 15, і всі під класом E, тобто
# жодного хибного звірення. Перевірку додано не через них, а через те,
# що першого ж запису класу A з таким джерелом ворота б пропустили.
#
# Умова «і не називає зовнішнього документа» обов'язкова: «UM10204,
# розділ 7.1» і «DHT11 datasheet, розділ параметрів» — це розділи ЧУЖИХ
# документів, і їх тут ловити не можна.
ROZDIL_KNYHY = re.compile(
    r'(?:^|[^\w])(розділ|картка|картку|картки|додаток|вкладка)\s+'
    r'[A-ZА-ЯЄІЇ0-9]', re.I)
ZOVNISHNIY = re.compile(
    r'datasheet|specification|reference manual|user manual|programming guide'
    r'|documentation'
    r'|UM\d|SBOS|DS\d|IEC\s*\d|ISO\s*\d|IEEE\s*\d|RFC\s*\d|Rev\.'
    r'|esp-idf|espressif|esptool|nxp|texas|microchip|vishay|maxim|aosong'
    r'|sitronix|solomon|invensense|silicon labs|raspberry|https?://', re.I)
VNUTRISHNYA = re.compile(r'^\s*ВНУТРІШНЯ ЗВІРКА')
# Контрольні рядки: до реєстру не належать і збігтися з ними взірець
# не має права. Взірець, що збігається з усіма трьома, збігається й з
# усім реєстром — і мовчки переводить кожну одиницю в свій клас.
#
# Куплено дорого: сім таких взірців із хвилі 1 показали 8083 одиниці
# зі 8083 як клас A, тобто «книгу звірено на 100 %». Жоден із них не
# падав і не виглядав холостим. П'ять були сирими рядками таблиці —
# `| `0xe` | EXT_CPU_RESET | норма |` — де риска це не риска, а
# АБО, тож взірець читається як «порожньо або 0xe або ... або
# порожньо» і збігається з будь-чим. Два були з подвійним
# екрануванням `\\|`, що дає те саме.
#
# Це третя й найгірша форма пастки з рискою. Перші дві помітні:
# взірець або падає, або нічого не чіпає. Ця виглядає як успіх.
# **Теча взірця.** Знахідка М1 від 06:30Z 2026-08-28, і третя форма
# пастки з диз'юнкцією — після холостої й після всеосяжної.
#
# Взірець — це АБО альтернатив. Якщо одна з них чіпляє більше, ніж усі
# інші разом, і чіпляє багато, вона взірець не звужує, а ПІДМІНЯЄ.
#
# Найгірший приклад мій: доказ про непідтягнутий GPIO мав серед
# альтернатив саме слово `стан`, і воно чіпляло 242 одиниці — тобто
# доказ ставив свій клас майже на кожне твердження книги зі словом
# «стан». Взірець компілювався, не був холостим і з контрольними
# рядками не збігався, тож усі попередні ворота його пропускали.
#
# Течей у моїх взірцях було 15, у М1 — 2.
TECHA_MIN = 25   # менше — не варте тривоги, слово може бути рідкісним

KONTROLNI = ('ESP32 має два ядра',
             'Зовсім інший текст про каву',
             '12345')

SYGNAL = re.compile(r'\d+\s*(?:МГц|кГц|Гц|мА|А|В|мВ|КБ|МБ|ГБ|мс|мкс|с|°C|Ом|кОм|біт|МБіт)'
                    r'|0x[0-9a-fA-F]+|GPIO\d+')

# Твердження про покажчик — це список сторінок, а не технічне число.
# Клас E на ньому правильний: зовнішнього джерела для покажчика книги
# не існує за природою. GPIO\d+ у назві такого запису — не сигнал.
POKAZHCHYK = re.compile(r'покажчик|індекс|z-pokazhchyk|у індексі|T-Z-\d+', re.I)


def teksty_odynyc():
    """Тексти одиниць реєстру — потрібні лише для перевірки на течу."""
    try:
        import sample
        # Не власний рядок літер: у ньому не було `N`, `K`, `S`, `L`,
        # тож перевірка на течу мовчки не бачила одиниць цих станів.
        # Джерело переліку — код, і лише код.
        import factcheck
        return [o['tekst'] for k in factcheck.STATUSES
                for o in sample.odynyci(k)]
    except Exception:
        return None


teksty = None


def perevirka(shlyakh):
    bidy = []
    try:
        zapysy = yaml.safe_load(open(shlyakh)) or []
    except Exception as e:
        return [('БИТИЙ YAML', str(e).split('\n')[0][:90], '')]
    for z in zapysy:
        if not isinstance(z, dict):
            bidy.append(('НЕ ЗАПИС', str(z)[:60], ''))
            continue
        nazva = str(z.get('title', ''))[:58]
        klas = z.get('status', '?')
        dzherelo = str(z.get('source', ''))
        cytata = str(z.get('quote', '')).strip()

        # `self-consistent` (клас `S`) — це **правильна** відповідь на
        # «книга як власне джерело», а не порушення. Заведено М1
        # 2026-08-28T19:15Z саме на ці 21 запис; вимагає шляху до файлу
        # книги й проходить шар 3 проти книги, тож звірка тут не
        # обіцянка, а зроблена робота.
        #
        # `no-external-signal` лишається дозволеним із іншої причини:
        # там звірки не було й не буде.
        if (KNYHA.search(dzherelo)
                and klas not in ('no-external-signal', 'self-consistent')):
            if VNUTRISHNYA.match(dzherelo):
                bidy.append(('ВНУТРІШНЯ ЗВІРКА ПІД КЛАСОМ ' + klas, nazva, ''))
            else:
                bidy.append(('КНИГА ЯК ВЛАСНЕ ДЖЕРЕЛО', nazva, klas))
        if (klas in ('verbatim', 'derived')
                and ROZDIL_KNYHY.search(dzherelo)
                and not ZOVNISHNIY.search(dzherelo)):
            bidy.append(('КНИГА ЯК ДЖЕРЕЛО, НАЗВАНА СЛОВАМИ', nazva,
                         dzherelo[:40]))
        # Взірець, що не компілюється, — не просто мертвий запис.
        # Він валить `factcheck.py sketch` для ВСЬОГО реєстру, тобто
        # ламає рендер обом супровідникам. Три таких приїхали хвилею 1
        # (сирий текст книги з `**жирним**` у полі `zbih`: зірочка на
        # нульовій позиції — «nothing to repeat»), і через них жодна з
        # двох хвиль не з'явилася в підрахунку класів, хоч усі докази
        # були на місці. Тому умова блокуюча.
        vzir = str(z.get('match', ''))
        if vzir:
            try:
                re.compile(vzir)
                for alt in factcheck.rozbyty_alternatyvy(vzir):
                    re.compile(alt)
            except re.error as e:
                bidy.append(('ВЗІРЕЦЬ НЕ КОМПІЛЮЄТЬСЯ: %s' % e, nazva, ''))
            else:
                rx = re.compile(vzir)
                if all(rx.search(k) for k in KONTROLNI):
                    bidy.append(('ВЗІРЕЦЬ ЗБІГАЄТЬСЯ З УСІМ', nazva, ''))
                elif teksty is not None:
                    alt = factcheck.rozbyty_alternatyvy(vzir)
                    if len(alt) > 1:
                        o = sorted(((sum(1 for t in teksty
                                         if re.search(a, t)), a)
                                    for a in alt), reverse=True)
                        if (o[0][0] >= TECHA_MIN
                                and o[0][0] > sum(x for x, _ in o[1:])):
                            bidy.append(('ТЕЧА: «%s» чіпляє %d'
                                         % (o[0][1][:20], o[0][0]), nazva, ''))
        if klas in ('verbatim', 'derived') and not cytata:
            bidy.append(('КЛАС %s БЕЗ ЦИТАТИ' % klas, nazva, ''))
        if klas == 'no-external-signal' and SYGNAL.search(nazva) and not POKAZHCHYK.search(nazva):
            bidy.append(('?  E на твердженні з числом', nazva, ''))
    return bidy


def main(argv):
    global teksty
    teksty = teksty_odynyc()
    shlyakhy = argv[1:] or sorted(glob.glob('factcheck/evidence/*.yaml'))
    vsyoho = 0
    blok = 0
    for s in shlyakhy:
        b = perevirka(s)
        vsyoho += len(b)
        blok += sum(1 for x in b if not x[0].startswith('?'))
        if b:
            print(os.path.basename(s))
            for rid, nazva, dod in b:
                print('   %-32s %s %s' % (rid, nazva, dod))
    print('\nпроблем: %d у %d файлах (%d блокують, %d на перегляд)'
          % (vsyoho, len(shlyakhy), blok, vsyoho - blok))
    return 1 if blok else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
