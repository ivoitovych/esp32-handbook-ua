.DEFAULT_GOAL := help
.PHONY: help setup all intake docs dovidnyk kartky proekty linkcheck cross-refs pins refuted struct-fields correspondence split-queue cache layer3 modality calques spelling budgets arithmetic stale schema self-checks reproducible cache-vs-book layer1 coverage check release release-check entry-points \
        check-attribution preview clean

PY := python3

help:
	@echo "ESP32: практичний довідник — цілі збирання"
	@echo ""
	@echo "  make setup              налаштувати клон: хуки, ідентичність, залежності"
	@echo "  make all                зібрати всі PDF"
	@echo "  make dovidnyk           основна книга, A5  → build/esp32-dovidnyk.pdf"
	@echo "  make kartky             картки ярусу 0, A4 → build/esp32-kartky.pdf"
	@echo "  make proekty            проєкти ярусу 2, A4→ build/esp32-proekty.pdf"
	@echo ""
	@echo "  make check              linkcheck + budgets + авторство"
	@echo "  make linkcheck          якорі, посилання, зображення (Р7)"
	@echo "  make budgets            обсяги розділів і карток (Р9)"
	@echo "  make check-attribution  author/committer і повідомлення всіх комітів"
	@echo ""
	@echo "  make preview T=dovidnyk сторінки ціллю в build/<T>/preview.png"
	@echo "  make clean              прибрати build/"

setup:
	@git config core.hooksPath .githooks
	@git config commit.gpgsign false
	@git config tag.gpgsign false
	@sh -c '. ./.githooks/identity.conf; \
	  git config user.name  "$$EXPECTED_NAME"; \
	  git config user.email "$$EXPECTED_EMAIL"; \
	  echo "ідентичність: $$EXPECTED_NAME <$$EXPECTED_EMAIL>"'
	@command -v pandoc >/dev/null 2>&1 || \
	  echo "  ! немає pandoc — apt-get install pandoc"
	@$(PY) -c "import typst" 2>/dev/null || \
	  echo "  ! немає typst — pip install typst"
	@$(PY) -c "import yaml" 2>/dev/null || \
	  echo "  ! немає pyyaml — pip install pyyaml"
	@echo "готово: хуки авторства увімкнено"

all:
	@$(PY) tools/build.py

dovidnyk kartky proekty:
	@$(PY) tools/build.py $@

linkcheck:
	@$(PY) tools/linkcheck.py

cross-refs:
	@$(PY) tools/cross_refs.py

pins:
	@$(PY) tools/pins.py

refuted:
	@$(PY) tools/refuted.py

struct-fields:
	@$(PY) tools/struct_fields.py

# Листування супровідників: форма, зв'язність, перелік відкритого.
correspondence:
	@$(PY) tools/correspondence.py

# Третій шар фактчекінгу: чи стоїть цитата за названою адресою.
#
# Ворота вибіркові й свідомо. Розбіжність цитати може бути хибною
# тривогою (переніс рядка, таблиця в PDF), тому вона лишається звітом:
# 51 запис у черзі. А вигадане джерело, заглушка в кеші й доказ класу
# `F` не можуть бути нічим, крім помилки, — і на них скрипт падає.
layer3:
	@$(PY) tools/layer3.py --zvit

# Модальність: припис у книзі проти дозволу в джерелі. Звіт, не
# ворота — припис може бути обґрунтованим, і судить це людина.
# Знайшов цей рід не інструмент, а помічник; інструмент дописано
# після, і його перша редакція давала 88 % хибних спрацювань.
modality:
	@$(PY) tools/modality.py

# Кальки з російської. Ворота, а не звіт: перелік короткий і містить
# лише однозначні заміни, тож знахідка тут — завжди помилка.
calques:
	@$(PY) tools/calques.py

# Поділ незвіреного між супровідниками за досяжністю джерела.
split-queue:
	@$(PY) tools/split_queue.py

# Кеш зовнішніх джерел: звірити sha256 наявних файлів із маніфестом.
cache:
	@$(PY) tools/cache.py --check

# Чи може доказ перевірити **третя сторона**. `--check` питає лише
# про мій кеш; кеш у git не входить (копірайт), тож єдиний місток
# назовні — рядок маніфесту. Доказ поза маніфестом відтворний тільки
# в тому контейнері, де його писали.
reproducible:
	@$(PY) tools/cache.py --vidtvornist

# Чи не потрапив файл книги в кеш джерел. Ворота, не звіт:
# доказ, що доводить книгу книгою, проходить усі три шари, і
# жодна інша перевірка його не бачить.
cache-vs-book:
	@$(PY) tools/cache_vs_book.py --tykho

# Узгодженість керівних документів (М2). Не проза — лише факти, що
# мають одну правильну відповідь: словник класів проти коду, названі
# інструменти, посилання на роди хиб, вердикти наряду проти воріт.
#
# Заведено після того, як словник класів розійшовся в ТРЬОХ документах
# і це знайшлося читанням. Читання не масштабується й не працює в CI.
docs:
	@$(PY) tools/docs.py

# Ворота прийому (М2): чи придатний запис доказу до того, як стане
# частиною реєстру. Компіляція взірця, теча, клас без цитати, книга як
# власне джерело.
#
# Досі цієї цілі не було, і ворота не запускав НІХТО: `make check` був
# зелений, поки перевірка з двадцятьма однією блокуючою знахідкою
# просто не викликалася. Це не «лічильник показав нуль» — це рід
# гірший: перевірка є, працює, і її не існує в обігу.
#
# Умова М2 для внесення у `check` була названа прямо: «додамо, коли
# розберемо ці 21». Розібрано — і не поодинці, а класом. Двадцять один
# із них був одним родом: внутрішня звірка книги проти себе під класом
# `verbatim`. Клас `S` (М1, 19:15Z) дає їм правильне ім'я, вимагає
# шляху до файлу книги й **проводить їх через шар 3 проти книги**:
# 22 із 22 зійшлися дословно. Двадцять другий — мій, стояв під
# `arithmetic` без жодної арифметики.
#
#   блокуючих знахідок   21 → 0
#
# Тепер ціль у `check`. Якщо М2 вважає, що рішення передчасне, —
# рядок знімається одним словом, і це нормально.
intake:
	@$(PY) tools/intake.py

# Шар 1 як скрипт (М2): чи стоїть твердження картки в книзі, чи стоїть
# там контекст і — головне — **чи містить контекст своє твердження**.
# Останнього ми не перевіряли ніколи: контекст, що не містить свого
# твердження, гірший за відсутній, бо обіцяє оточення, а дає чуже.
layer1:
	@$(PY) tools/layer1.py

# Покриття (М2): чи кожен змістовний рядок книги став одиницею. Питання
# зворотне до очевидного — «чи має одиниця картку» правда за побудовою.
# Текст, якого розбирач не бачив, не має ні картки, ні класу й не
# потрапляє в жоден підрахунок: він не незвірений, він невидимий.
coverage:
	@$(PY) tools/coverage.py

# Правопис: перелік невідомих слів. Звіт, не ворота — судити про
# українську має людина, інструмент лише скорочує їй роботу.
spelling:
	@$(PY) tools/spelling.py

# Зібрати й покласти у release/ те, що бачить читач на GitHub.
release:
	@$(PY) tools/build.py --strict
	@cp build/esp32-*.pdf build/BUILD.txt release/
	@echo "release: оновлено з відбитком джерел"

# Випускні ворота (Р-VYPUSK). Відрізняються від `check` не суворістю
# правил, а тим, що попередження стають помилками: під час писання
# відсутній розділ і знахідка рецензента — робочий стан, у випуску —
# зупинка. Ціль має завершуватися нулем перед кожним тегом релізу.
release-check:
	@echo "── маніфест, посилання, піни, арифметика"
	@$(PY) tools/linkcheck.py
	@$(PY) tools/cross_refs.py
	@$(PY) tools/pins.py
	@$(PY) tools/refuted.py
	@$(PY) tools/struct_fields.py
	@$(PY) tools/arithmetic.py >/dev/null && echo "arytmetyka: збіглося"
	@echo "── листування (строго: відкрите питання зупиняє випуск)"
	@$(PY) tools/correspondence.py --suvoro
	@$(PY) tools/cache.py --check
	@echo "── рецензійні перевірки (строго)"
	@$(PY) tools/review.py --strict >/dev/null && echo "review: 0 знахідок"
	@echo "── реєстр фактчекінгу"
# Чи реєстр іще про **цю** книгу.
#
# Реєстр генерується з книги, тож правка книги його не ламає — вона його
# **відсуває**, тихо: доказ лишається прив'язаним до старого
# формулювання, а `src:рядок` починає показувати мимо. Чотири дні
# `stale` мав це ловити й не ловив (він перевіряв, чи існує файл), і
# шість правок друкованого накладу пройшли повз лічильник.
#
# Тут це звіт, а не зупинка: розходження нормальне рівно доти, доки
# наступний `sketch` його не прибрав. Зупиняти випуск має `vorota` —
# але побачити розходження треба **до** того, як хтось візьме з реєстру
# номер рядка й піде за ним у книгу.
	@$(PY) tools/factcheck.py stale
	@$(PY) tools/factcheck.py vorota
# Третій шар у випускних воротах — **звичайний режим, не `--suvoro`**.
#
# Він розрізняє рівно те, що потрібне на випуску: вигадане джерело,
# заглушка замість документа й запис класу `F` у полі доказу — це
# помилки, які зупиняють; недосяжне джерело й розбіжна цитата —
# звіт, а не зупинка.
#
# Довго його тут не було, і це виглядало як зважене рішення: `make
# check` червонів через чужі записи, а друк ішов. Зовнішня рецензія
# назвала це правильно — **проєкт, чия головна сила в перевірності
# доказів, не має випускатися з відомо зламаним інваріантом.**
	@$(PY) tools/layer3.py
	@echo "── повне збирання без пропусків"
	@$(PY) tools/build.py --strict
	@echo "── авторство"
	@$(MAKE) --no-print-directory check-attribution
	@$(PY) tools/pdf-smoke.py
	@echo "release-check: усе пройдено"

budgets:
	@$(PY) tools/budgets.py --pages

check: self-checks docs intake linkcheck cross-refs pins refuted struct-fields correspondence cache layer3 modality calques budgets arithmetic stale schema reproducible cache-vs-book layer1 coverage check-attribution

arithmetic:
	@python3 tools/arithmetic.py

# Чи реєстр іще про **цю** книгу — див. докстрінг `stale`.
# Звіт, не зупинка: розходження нормальне доти, доки
# наступний `sketch` його не прибрав. Але побачити його
# треба **до** того, як хтось візьме з реєстру номер рядка
# й піде за ним у книгу.
stale:
	@python3 tools/factcheck.py stale

# Схема запису доказу й контракт картки. Порушень зараз нуль — тож
# лишилося зробити її воротами; поки звіт, бо шість записів М2 чекають
# на переведення в `looked-not-found`, і після нього це стане ворітьми.
schema:
	@python3 tools/schema.py

# Самоперевірки: показ кожної перевірки на **навмисно зіпсованому**
# вході. Правило проєкту каже, що перевірка без такого показу не
# відрізняється від відсутньої, — і саме тому самоперевірки треба
# кликати, а не мати.
#
# Досі їх не кликав НІХТО: обидві жили в скриптах під прапорцем, і
# `make check` запускав `techa` без нього. Того дня, коли переведення
# імен полів зламало запасний вираз у `techa.znayty`, самоперевірка це
# **побачила** — показала «очікували течу, дістали чисто» — і сказала
# це в порожню кімнату. Червона перевірка, якої ніхто не кличе,
# рівно так само зелена.
self-checks:
	@$(PY) tools/schema.py --samoperevirka
	@$(PY) tools/leak.py --samoperevirka
	@$(PY) tools/task_spec.py --samoperevirka

# Кожна точка входу технології, а не лише ті, що у воротах.
#
# `make check` кличе 18 цілей; точок входу 54, у 42 інструментах, і 22
# інструменти поза воротами. Саме там вижили всі дев'ять зламів
# переведення імен полів 2026-08-28, і саме там їх знайшов цей гарнес.
#
# Це не ворота: прогін довгий і потрібен навколо змін, що мають
# **зберігати поведінку** — перейменувань, переїздів, рефакторингів.
#
#   tools/entry_points.py --capture /tmp/do
#   …зміна…
#   tools/entry_points.py --capture /tmp/pislya
#   tools/entry_points.py --diff /tmp/do /tmp/pislya
entry-points:
	@$(PY) tools/entry_points.py --missing

check-attribution:
	@sh -c '. ./.githooks/identity.conf; \
	  bad=0; \
	  for sha in $$(git rev-list HEAD 2>/dev/null); do \
	    an=$$(git log -1 --format="%an" $$sha); ae=$$(git log -1 --format="%ae" $$sha); \
	    cn=$$(git log -1 --format="%cn" $$sha); ce=$$(git log -1 --format="%ce" $$sha); \
	    if [ "$$an" != "$$EXPECTED_NAME" ] || [ "$$ae" != "$$EXPECTED_EMAIL" ] || \
	       [ "$$cn" != "$$EXPECTED_NAME" ] || [ "$$ce" != "$$EXPECTED_EMAIL" ]; then \
	      echo "  ✗ $$(git rev-parse --short $$sha) author=$$an <$$ae> committer=$$cn <$$ce>"; \
	      bad=1; \
	    fi; \
	    if git log -1 --format="%B" $$sha | grep -qiE "co-authored-by|assisted-by|generated with"; then \
	      echo "  ✗ $$(git rev-parse --short $$sha) запис співавторства у повідомленні"; \
	      bad=1; \
	    fi; \
	  done; \
	  if [ $$bad -eq 0 ]; then \
	    echo "авторство: усі коміти — $$EXPECTED_NAME <$$EXPECTED_EMAIL>, записів співавторства немає"; \
	  fi; \
	  exit $$bad'

T ?= dovidnyk
preview:
	@$(PY) tools/build.py $(T)
	@$(PY) tools/preview.py $(T)

clean:
	@rm -rf build
	@echo "прибрано build/"
