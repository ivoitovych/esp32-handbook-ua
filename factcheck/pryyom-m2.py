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
VNUTRISHNYA = re.compile(r'^\s*ВНУТРІШНЯ ЗВІРКА')
SYGNAL = re.compile(r'\d+\s*(?:МГц|кГц|Гц|мА|А|В|мВ|КБ|МБ|ГБ|мс|мкс|с|°C|Ом|кОм|біт|МБіт)'
                    r'|0x[0-9a-fA-F]+|GPIO\d+')

# Твердження про покажчик — це список сторінок, а не технічне число.
# Клас E на ньому правильний: зовнішнього джерела для покажчика книги
# не існує за природою. GPIO\d+ у назві такого запису — не сигнал.
POKAZHCHYK = re.compile(r'покажчик|індекс|z-pokazhchyk|у індексі|T-Z-\d+', re.I)


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
        nazva = str(z.get('nazva', ''))[:58]
        klas = z.get('klas', '?')
        dzherelo = str(z.get('dzherelo', ''))
        cytata = str(z.get('cytata', '')).strip()

        if KNYHA.search(dzherelo) and klas != 'E':
            if VNUTRISHNYA.match(dzherelo):
                bidy.append(('ВНУТРІШНЯ ЗВІРКА ПІД КЛАСОМ ' + klas, nazva, ''))
            else:
                bidy.append(('КНИГА ЯК ВЛАСНЕ ДЖЕРЕЛО', nazva, klas))
        # Взірець, що не компілюється, — не просто мертвий запис.
        # Він валить `factcheck.py sketch` для ВСЬОГО реєстру, тобто
        # ламає рендер обом супровідникам. Три таких приїхали хвилею 1
        # (сирий текст книги з `**жирним**` у полі `zbih`: зірочка на
        # нульовій позиції — «nothing to repeat»), і через них жодна з
        # двох хвиль не з'явилася в підрахунку класів, хоч усі докази
        # були на місці. Тому умова блокуюча.
        vzir = str(z.get('zbih', ''))
        if vzir:
            try:
                re.compile(vzir)
                for alt in factcheck.rozbyty_alternatyvy(vzir):
                    re.compile(alt)
            except re.error as e:
                bidy.append(('ВЗІРЕЦЬ НЕ КОМПІЛЮЄТЬСЯ: %s' % e, nazva, ''))
        if klas in ('A', 'B') and not cytata:
            bidy.append(('КЛАС %s БЕЗ ЦИТАТИ' % klas, nazva, ''))
        if klas == 'E' and SYGNAL.search(nazva) and not POKAZHCHYK.search(nazva):
            bidy.append(('?  E на твердженні з числом', nazva, ''))
    return bidy


def main(argv):
    shlyakhy = argv[1:] or sorted(glob.glob('factcheck/dokazy/*.yaml'))
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
