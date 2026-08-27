#!/usr/bin/env python3
"""Ворота М2: чотири механічні умови, які запис має пройти до коміту.

Не замінює tools/factcheck.py — це передфільтр для свіжих доказів,
щоб дефект не потрапив у реєстр і не мусив звідти виловлюватися.

Умови:
  1. YAML читається;
  2. джерело не є файлом самої книги (крім класу E й позначених
     внутрішніх звірок — див. нижче);
  3. клас A або B має непорожню cytata;
  4. клас E не стоїть на твердженні з числом, адресою чи GPIO.
"""
import glob, os, re, sys
import yaml

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
        if klas in ('A', 'B') and not cytata:
            bidy.append(('КЛАС %s БЕЗ ЦИТАТИ' % klas, nazva, ''))
        if klas == 'E' and SYGNAL.search(nazva) and not POKAZHCHYK.search(nazva):
            bidy.append(('E НА ТВЕРДЖЕННІ З ЧИСЛОМ', nazva, ''))
    return bidy


def main(argv):
    shlyakhy = argv[1:] or sorted(glob.glob('factcheck/dokazy/*.yaml'))
    vsyoho = 0
    for s in shlyakhy:
        b = perevirka(s)
        vsyoho += len(b)
        if b:
            print(os.path.basename(s))
            for rid, nazva, dod in b:
                print('   %-32s %s %s' % (rid, nazva, dod))
    print('\nпроблем: %d у %d файлах' % (vsyoho, len(shlyakhy)))
    return 1 if vsyoho else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
