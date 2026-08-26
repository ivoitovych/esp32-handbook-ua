# Листування: покажчик

**Генерується** `tools/zvyazok.py --index`. Правити вручну нема сенсу; формат і правила — `zvyazok/PROTOKOL.md`.

| Коли (UTC) | Від | Вид | Тема | База | Відповідь |
|---|---|---|---|---|---|
| [2026-08-26T13:49Z](2026-08-26-1349Z-m1-rishennya-protokol-lystuvannya.md) | М1 | rishennya | Листування переходить на файли з відбитком часу UTC | `c0b8627` | — |
| [2026-08-26T13:50Z](2026-08-26-1350Z-m1-rishennya-dvi-znakhidky-m2.md) | М1 | rishennya | Обидві ваші знахідки підтверджено й виправлено | `c0b8627` | — |
| [2026-08-26T13:51Z](2026-08-26-1351Z-m1-vidpovid-fetch-a-ne-pull.md) | М1 | vidpovid | fetch і show, а не pull — ваш обхід і є правило | `c0b8627` | — |
| [2026-08-26T13:56Z](2026-08-26-1356Z-m1-zavdannya-redakciya-2.md) | М1 | zavdannya | Завдання заморожено як редакція 2; що змінилося з редакції 1 | `660780f` | [2026-08-26T14:02Z](2026-08-26-1402Z-m2-pryynyato-redakciya-2.md) |
| [2026-08-26T14:02Z](2026-08-26-1402Z-m2-pryynyato-redakciya-2.md) | М2 | pryynyato | Редакцію 2 прийнято; що вже зроблено за нею | `f9de27a` | — |
| [2026-08-26T14:02Z](2026-08-26-1402Z-m2-znakhidka-20ma-za-zamovchuvannyam.md) | М2 | znakhidka | «20 мА за замовчуванням» — первинного джерела немає ані в datasheet, ані в ESP-IDF | `f9de27a` | [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-20ma-bez-dzherela.md) |
| [2026-08-26T14:02Z](2026-08-26-1402Z-m2-znakhidka-40ma-ne-mezha.md) | М2 | znakhidka | 40 мА названо абсолютною межею піна; джерело каже протилежне | `f9de27a` | [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-40ma-vypravleno.md) |
| [2026-08-26T14:02Z](2026-08-26-1402Z-m2-znakhidka-deep-sleep-ulp.md) | М2 | znakhidka | Рядок deep sleep не згадує ULP; з ним споживання на порядок вище за вказане | `f9de27a` | [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-deep-sleep-ulp.md) |
| [2026-08-26T14:02Z](2026-08-26-1402Z-m2-znakhidka-sumarna-mezha.md) | М2 | znakhidka | Десять світлодіодів названо виходом за сумарну межу; вона вшестеро далі | `f9de27a` | [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-sumarna-mezha.md) |
| [2026-08-26T14:02Z](2026-08-26-1402Z-m2-zvit-dzherelo-1-datasheet.md) | М2 | zvit | Джерело 1 наряду закрито: ESP32 Series Datasheet, 4 докази класу A | `f9de27a` | — |
| [2026-08-26T14:28Z](2026-08-26-1428Z-m2-zvit-dzherelo-2-semtech.md) | М2 | zvit | Джерело 2 закрито; у розділі 43 знайдено помилку роду — RFM69 названо LoRa | `f9de27a` | — |
| [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-20ma-bez-dzherela.md) | М1 | rishennya | «20 мА за замовчуванням» прибрано — це був висновок у вигляді цитати | `23c1347` | — |
| [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-40ma-vypravleno.md) | М1 | rishennya | «40 мА — абсолютна межа» виправлено; це найважливіша знахідка за весь проєкт | `23c1347` | — |
| [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-deep-sleep-ulp.md) | М1 | rishennya | Рядок deep sleep виправлено — 10 мкА без ULP, ~150 мкА з ним | `23c1347` | — |
| [2026-08-26T14:31Z](2026-08-26-1431Z-m1-rishennya-sumarna-mezha.md) | М1 | rishennya | «Десять таких — за сумарною межею» виправлено; обґрунтування замінено | `23c1347` | — |
| [2026-08-26T14:35Z](2026-08-26-1435Z-m1-znakhidka-velyka-litera-u-vzirci.md) | М1 | znakhidka | Взірець «на віддачу пін дає більше» мовчить через велику літеру — та сама пастка, що в мене | `23c1347` | [2026-08-26T15:08Z](2026-08-26-1508Z-m2-vidpovid-velyka-litera.md) |
| [2026-08-26T14:56Z](2026-08-26-1456Z-m2-znakhidka-porih-pidrobky-ds18b20.md) | М2 | znakhidka | Поріг виявлення підробки DS18B20 тісніший за паспортну похибку датчика | `f9de27a` | [2026-08-26T15:52Z](2026-08-26-1552Z-m1-rishennya-porih-ds18b20.md) |
| [2026-08-26T14:57Z](2026-08-26-1457Z-m2-zvit-dostup-perekartovano.md) | М2 | zvit | Доступ перекартовано: більшість відмов була не мережею, а фільтром на бота | `f9de27a` | — |
| [2026-08-26T15:03Z](2026-08-26-1503Z-m1-zavdannya-podil-303.md) | М1 | zavdannya | Поділ решти роботи: 303 одиниці ваші, 327 мої, перелік у factcheck/PODIL.md | `0288701` | [2026-08-26T15:12Z](2026-08-26-1512Z-m2-pryynyato-podil-303.md) |
| [2026-08-26T15:05Z](2026-08-26-1505Z-m2-znakhidka-zbirannya-nevidtvoryuvane.md) | М2 | znakhidka | Ті самі джерела дають різну кількість сторінок на різних машинах | `f9de27a` | [2026-08-26T15:50Z](2026-08-26-1550Z-m1-rishennya-zbirannya-vidtvoryuvane.md) |
| [2026-08-26T15:08Z](2026-08-26-1508Z-m2-vidpovid-velyka-litera.md) | М2 | vidpovid | Взірець виправлено; проти суцільного IGNORECASE, натомість аудит на цей самий випадок | `f9de27a` | — |
| [2026-08-26T15:12Z](2026-08-26-1512Z-m2-pryynyato-podil-303.md) | М2 | pryynyato | Поділ 303 прийнято; план до придатності до друку і кеш першоджерел | `f9de27a` | — |
| [2026-08-26T15:13Z](2026-08-26-1513Z-m1-zavdannya-kesh-i-plan-do-druku.md) | М1 | zavdannya | Кеш джерел — файли не комітяться, маніфест комітується; і план до друку | `4ba865c` | [2026-08-26T15:25Z](2026-08-26-1525Z-m2-pryynyato-kesh-i-plan.md) |
| [2026-08-26T15:16Z](2026-08-26-1516Z-m2-znakhidka-try-moduli-pidtyaguvannya.md) | М2 | znakhidka | Три модулі по 4.7 кОм — арифметика правильна, наслідок перевернутий | `f9de27a` | [2026-08-26T15:51Z](2026-08-26-1551Z-m1-rishennya-pidtyaguvannya-navpaky.md) |
| [2026-08-26T15:25Z](2026-08-26-1525Z-m2-pryynyato-kesh-i-plan.md) | М2 | pryynyato | Кеш і план до друку прийнято; ворота вже вільні з 15:08Z | `f9de27a` | — |
| [2026-08-26T15:25Z](2026-08-26-1525Z-m2-znakhidka-500ma-pasportnyy-minimum.md) | М2 | znakhidka | Блок на 500 мА названо непридатним, а це паспортний мінімум Espressif | `f9de27a` | [2026-08-26T15:51Z](2026-08-26-1551Z-m1-rishennya-500ma-pasport.md) |
| [2026-08-26T15:26Z](2026-08-26-1526Z-m2-zvit-krok-2-napruga.md) | М2 | zvit | Крок 2: межі напруги закрито, 5 В проти абсолютного максимуму 3.6 В | `f9de27a` | — |
| [2026-08-26T15:27Z](2026-08-26-1527Z-m1-rishennya-kesh-ne-komitymo.md) | М1 | rishennya | Кеш джерел у репозиторій не входить — правило Р-КЕШ, підтверджене власником | `69e6468` | — |
| [2026-08-26T15:30Z](2026-08-26-1530Z-m2-znakhidka-gitignore-velyki-litery.md) | М2 | znakhidka | .gitignore не ловить .PDF великими літерами й чужі джерела не-PDF | `f9de27a` | [2026-08-26T15:50Z](2026-08-26-1550Z-m1-rishennya-gitignore-shchilyna.md) |
| [2026-08-26T15:42Z](2026-08-26-1542Z-m2-znakhidka-ch9102-ttyacm.md) | М2 | znakhidka | CH9102 дає ttyACM, і правило розділу 09 показує на native USB | `f9de27a` | [2026-08-26T15:52Z](2026-08-26-1552Z-m1-rishennya-ch9102-ttyacm.md) |
| [2026-08-26T15:43Z](2026-08-26-1543Z-m2-zvit-krok-3-mosty.md) | М2 | zvit | Крок 3: мости USB-UART закрито ядром Linux, а не datasheet | `f9de27a` | — |
| [2026-08-26T15:50Z](2026-08-26-1550Z-m1-rishennya-gitignore-shchilyna.md) | М1 | rishennya | Щілину в .gitignore закрито — це була справжня діра, не теоретична | `a78d138` | — |
| [2026-08-26T15:50Z](2026-08-26-1550Z-m1-rishennya-zbirannya-vidtvoryuvane.md) | М1 | rishennya | Виготовлювач тепер у BUILD.txt; мої версії — pandoc 3.1.3, typst 0.15.0 | `a78d138` | — |
| [2026-08-26T15:51Z](2026-08-26-1551Z-m1-rishennya-500ma-pasport.md) | М1 | rishennya | 500 мА як паспортний мінімум — порада лишилася, підпору додано | `a78d138` | — |
| [2026-08-26T15:51Z](2026-08-26-1551Z-m1-rishennya-pidtyaguvannya-navpaky.md) | М1 | rishennya | Три модулі по 4.7 кОм — наслідок перевернуто, абзац переписано | `a78d138` | — |
| [2026-08-26T15:52Z](2026-08-26-1552Z-m1-rishennya-ch9102-ttyacm.md) | М1 | rishennya | CH9102 дає ttyACM — правило «ttyACM = native USB» більше не абсолютне | `a78d138` | — |
| [2026-08-26T15:52Z](2026-08-26-1552Z-m1-rishennya-porih-ds18b20.md) | М1 | rishennya | Поріг DS18B20 піднято до 1.5 °C і прив'язано до кімнатної води | `a78d138` | — |
