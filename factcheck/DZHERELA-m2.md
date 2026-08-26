# Кеш першоджерел — М2

Реєстр документів, які М2 отримав і тримає локально для звірки.

## Чому не в репозиторії

Самі PDF лежать **поза деревом** — у `~/dzherela-cache/`. Причин дві, і
обидві важать більше за зручність.

**Право.** Datasheet виробника поширювати не можна: це його документ, а
не наш. Книга під власною ліцензією, і класти в неї чужі PDF — міняти її
правовий стан заради кількох мегабайтів зручності.

**Вага.** Кеш іде до гігабайта. Репозиторій книги на 400 сторінок важить
менше за один datasheet ATmega328P.

Натомість тут — те, що робить звірку **відтворюваною**: звідки взято,
коли, скільки сторінок і відбиток файлу. Цього досить, щоб будь-хто
дістав той самий документ і переконався, що це той самий.

## Правило

Кожен доказ класу `A` називає документ у полі `dzherelo` і спосіб у
`sposib`. Цей файл додає до них третє — **тотожність**: за `sha256` і
кількістю сторінок видно, що читали саме цей файл, а не інший з тією
самою назвою.

Перевірка при завантаженні обов'язкова (`~/dzherela-cache/vzyaty.sh`):
`file` має сказати `PDF`. Причина — у звіті про Semtech: `semtech.com`
віддає HTML-заглушку рівно на 21 151 байт із кодом `200`, і без цієї
перевірки вона лягає в кеш як «отриманий документ».

## Документи

| Документ | sha256 (16) | Обсяг | Узято | Звідки |
|---|---|---|---|---|
| `atmega328p` | `b9b9d83cda56a95d` | 653 с. | 2026-08-26 | https://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061B.pdf |
| `ch340` | `04c805e8242885fd` | 6 с. | 2026-08-26 | https://cdn.sparkfun.com/datasheets/Dev/Arduino/Other/CH340DS1.PDF |
| `cp2102` | `f025d9c738e49065` | 26 с. | 2026-08-26 | https://www.silabs.com/documents/public/data-sheets/cp2102-9.pdf |
| `hc-sr04` | `4ebdc3e1f70d84a1` | 3 с. | 2026-08-26 | https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf |
| `i2c-um10204` | `dc91f00f65584e06` | 62 с. | 2026-08-26 | https://www.pololu.com/file/0J435/UM10204.pdf |
| `ili9341` | `a9bbfdf6d078f54a` | 245 с. | 2026-08-26 | https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf |
| `ina219` | `58004eda854d0747` | 38 с. | 2026-08-26 | https://www.ti.com/lit/ds/symlink/ina219.pdf |
| `mcp23017` | `14159c6f5655e943` | 42 с. | 2026-08-26 | https://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf |
| `pcf8574` | `e632c2d07e07f559` | 42 с. | 2026-08-26 | https://www.ti.com/lit/ds/symlink/pcf8574.pdf |
| `rp2040` | `be56fbb75ba0ae9e` | 642 с. | 2026-08-26 | https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf |
| `ssd1306` | `d55f875357de96d8` | 65 с. | 2026-08-26 | https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf |
