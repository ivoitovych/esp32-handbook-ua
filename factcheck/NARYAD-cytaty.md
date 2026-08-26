# Наряд: 19 цитат, яких немає в джерелі

**Генерується** `tools/naryad.py`. Питання **не** про цитату.

Третій шар уже сказав, що цитати за адресою немає. Причина відома і
здебільшого та сама: супровідник **причепурив** цитату — скоротив
`{IDF_TARGET_STRAP_BOOT_2_GPIO}` до `{STRAP_BOOT_2_GPIO}`, зібрав рядок
таблиці рукою, переставив відступи. Це брак реєстру, і його виправляє
супровідник.

**Твоє питання інше й важливіше: чи правильне те, що написано в книзі.**

Цитата може бути причесана, а факт — правильний. Може бути й навпаки:
причесування іноді ховає те, що джерело каже щось інше. Книга йде в
друк, тож нас цікавить саме другий випадок.

По кожному запису:

1. завантаж джерело (`curl` на `raw.githubusercontent.com`);
2. знайди місце, про яке йдеться;
3. відповідай **одним із трьох**:

| Вердикт | Коли |
|---|---|
| `pidtverdzheno` | джерело каже те саме; наведи **дослівний** рядок звідти |
| `sperechayetsya` | джерело каже **інакше** — це знахідка, опиши точно |
| `ne_vyrishyv` | джерело недосяжне або місця не знайшов |

`sperechayetsya` — те, заради чого це робиться. Не бійся його ставити:
книгу ще можна виправити. Але став його, лише коли **бачиш** інший
текст, а не коли пам'ятаєш інакше.

Цитату копіюй дослівно: вона перевіряється підрядком.

**YAML:** якщо значення містить `: ` або починається з лапки — бери все
значення в одинарні лапки.

Формат:

```yaml
- zapys: pass-26-strapping
  nazva: Рівні strapping і недійсна комбінація — усі сімейства
  verdykt: pidtverdzheno
  dzherelo: https://raw.githubusercontent.com/...
  cytata: |
    дослівний рядок із джерела
  komentar: одне речення
```

## Пакет 1

**`m2-62-bootlog-k06`** · T-K06-045: На 115200 нічого, на 74880 осмислений текст — це ESP8266

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `74880.*осмислений текст.*ESP8266`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flesh`** · Етап 1 — ROM bootloader зашитий у кремній

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `Етап 1.*ROM bootloader.*кремній`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flesh`** · Етап 2 — другий бутлоадер bootloader.bin у флеші

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `Етап 2.*другий бутлоадер.*bootloader`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flesh`** · Адреса bootloader.bin для ESP32 чипів — 0x1000

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `Адреса.*bootloader.*0x1000`
- третій шар: 1 з 1 рядків

**`m2-82-boot-flesh`** · GPIO0 як ключовий strapping-пін для вибору режиму завантаження

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: ``GPIO0`.*strapping.*download`
- третій шар: 1 з 1 рядків


## Пакет 2

**`m2-82-boot-flesh`** · Розділи ota_0 та ota_1 у таблиці розділів для OTA

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- у книзі шукати за взірцем: ``ota_0`.*`ota_1``
- третій шар: 2 з 2 рядків

**`m2-83-esptool`** · esptool версія v4 та v5 у ESP-IDF

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `v4.*v5|esptool.*version`
- третій шар: 2 з 2 рядків

**`m2-83-esptool`** · Адреса bootloader.bin для ESP32 — 0x1000

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `0x1000.*classic|адреса.*0x1000`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Адреса merge-bin завжди на 0x0 незалежно від конфігурації

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `0x0.*незалежно`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Таблиця розділів за замовчуванням на адресі 0x8000

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- у книзі шукати за взірцем: `partition.*table.*0x8000`
- третій шар: 1 з 1 рядків


## Пакет 3

**`m2-83-esptool`** · MAC-адреса унікальна від заводу і лежить в eFuse

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `MAC-адреса.*унікальна.*eFuse`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Команда esptool flash-id додає інформацію про флеш

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `flash-id.*шапка`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Максимальна швидкість baudu для більшості мостів 460800

- джерело: https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst
- у книзі шукати за взірцем: `460800`
- третій шар: 1 з 1 рядків

**`m2-83-esptool`** · Розміри флешу 2 МБ або 4 МБ для ESP32 модулів

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst
- у книзі шукати за взірцем: `2.*МБ|4.*МБ`
- третій шар: 1 з 1 рядків

**`m2-84-freertos`** · Пріоритет задачі від 0 до configMAX_PRIORITIES мінус 1

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `0.*configMAX_PRIORITIES|пріоритет.*0`
- третій шар: 2 з 2 рядків


## Пакет 4

**`m2-84-freertos`** · Core 0 (PRO_CPU) переважно займає радіостек, Core 1 (APP_CPU) — застосунок

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `Core.*0.*Core.*1|APP_CPU|PRO_CPU`
- третій шар: 3 з 3 рядків

**`m2-84-freertos`** · Функції FromISR єдині дозволені в обробнику переривання

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `FromISR|обробнику переривання`
- третій шар: 1 з 1 рядків

**`m2-84-freertos`** · Бітові прапори WIFI_OK та TIME_OK в event group

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- у книзі шукати за взірцем: `WIFI_OK|TIME_OK|BIT0|BIT1`
- третій шар: 1 з 1 рядків

**`m2-84-freertos`** · Реле на GPIO при зависанні переходить в безпечний стан

- джерело: https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst
- у книзі шукати за взірцем: `реле.*GPIO|зависанні`
- третій шар: 1 з 1 рядків

