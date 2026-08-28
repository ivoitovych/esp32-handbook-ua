.DEFAULT_GOAL := help
.PHONY: help setup all dovidnyk kartky proekty linkcheck posylannya piny sprostovane polya zvyazok podil kesh citaty kalky pravopys budgets arytmetyka stale skhema vidtvornist bez-knyhy check release release-check \
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

posylannya:
	@$(PY) tools/posylannya.py

piny:
	@$(PY) tools/piny.py

sprostovane:
	@$(PY) tools/sprostovane.py

polya:
	@$(PY) tools/polya.py

# Листування супровідників: форма, зв'язність, перелік відкритого.
zvyazok:
	@$(PY) tools/zvyazok.py

# Третій шар фактчекінгу: чи стоїть цитата за названою адресою.
#
# Ворота вибіркові й свідомо. Розбіжність цитати може бути хибною
# тривогою (переніс рядка, таблиця в PDF), тому вона лишається звітом:
# 51 запис у черзі. А вигадане джерело, заглушка в кеші й доказ класу
# `F` не можуть бути нічим, крім помилки, — і на них скрипт падає.
citaty:
	@$(PY) tools/citaty.py --zvit

# Модальність: припис у книзі проти дозволу в джерелі. Звіт, не
# ворота — припис може бути обґрунтованим, і судить це людина.
# Знайшов цей рід не інструмент, а помічник; інструмент дописано
# після, і його перша редакція давала 88 % хибних спрацювань.
modalnist:
	@$(PY) tools/modalnist.py

# Кальки з російської. Ворота, а не звіт: перелік короткий і містить
# лише однозначні заміни, тож знахідка тут — завжди помилка.
kalky:
	@$(PY) tools/kalky.py

# Поділ незвіреного між супровідниками за досяжністю джерела.
podil:
	@$(PY) tools/podil.py

# Кеш зовнішніх джерел: звірити sha256 наявних файлів із маніфестом.
kesh:
	@$(PY) tools/kesh.py --check

# Чи може доказ перевірити **третя сторона**. `--check` питає лише
# про мій кеш; кеш у git не входить (копірайт), тож єдиний місток
# назовні — рядок маніфесту. Доказ поза маніфестом відтворний тільки
# в тому контейнері, де його писали.
vidtvornist:
	@$(PY) tools/kesh.py --vidtvornist

# Чи не потрапив файл книги в кеш джерел. Ворота, не звіт:
# доказ, що доводить книгу книгою, проходить усі три шари, і
# жодна інша перевірка його не бачить.
bez-knyhy:
	@$(PY) tools/kesh-bez-knyhy.py --tykho

# Правопис: перелік невідомих слів. Звіт, не ворота — судити про
# українську має людина, інструмент лише скорочує їй роботу.
pravopys:
	@$(PY) tools/pravopys.py

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
	@$(PY) tools/posylannya.py
	@$(PY) tools/piny.py
	@$(PY) tools/sprostovane.py
	@$(PY) tools/polya.py
	@$(PY) tools/arytmetyka.py >/dev/null && echo "arytmetyka: збіглося"
	@echo "── листування (строго: відкрите питання зупиняє випуск)"
	@$(PY) tools/zvyazok.py --suvoro
	@$(PY) tools/kesh.py --check
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
	@$(PY) tools/citaty.py
	@echo "── повне збирання без пропусків"
	@$(PY) tools/build.py --strict
	@echo "── авторство"
	@$(MAKE) --no-print-directory check-attribution
	@$(PY) tools/pdf-smoke.py
	@echo "release-check: усе пройдено"

budgets:
	@$(PY) tools/budgets.py --pages

check: linkcheck posylannya piny sprostovane polya zvyazok kesh citaty modalnist kalky budgets arytmetyka stale skhema vidtvornist bez-knyhy check-attribution

arytmetyka:
	@python3 tools/arytmetyka.py

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
skhema:
	@python3 tools/skhema.py

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
