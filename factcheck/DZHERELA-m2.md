# Кеш першоджерел — М2

**Формат колонок — той самий, що в `dzherela-kesh/MANIFEST.md`** (`tools/kesh.py`),
щоб рядки можна було злити механічно.

## Чому окремий файл, а не спільний маніфест

`tools/kesh.py` **перегенеровує** `MANIFEST.md` із вмісту свого каталогу.
Каталоги в нас різні, тож кожна перегенерація стирала б рядки другого
супровідника: не конфлікт злиття, а тиха втрата. Тому реєстр М2 живе
окремим файлом у моїй зоні, за правилом «один власник на запис».

Якщо `kesh.py` навчиться **доповнювати** маніфест замість переписувати —
зіллємо в один; рядки для цього вже в потрібному вигляді.

## Чому самі PDF не в git

Те саме, до чого незалежно дійшли обидва: datasheet виробника — чужий
матеріал під копірайтом. Дозволено завантажувати й користуватися,
перевидавати — ні. Книга стоїть на тезі «джерело назване чесно»;
порушення авторського права в службовому каталозі підриває саме її.

У git іде те, що робить звірку відтворюваною: URL, дата, розмір і
`sha256`. За ним будь-хто дістає той самий файл і доводить, що читав те
саме — це сильніше за спільний файл, бо доводить і те, що джерело за
URL не підмінили.

## Перевірка при завантаженні

`file` має сказати `PDF`. Причина — `semtech.com` віддає HTML-заглушку
рівно на 21 151 байт із кодом `200`; без перевірки вона лягає в кеш як
«отриманий документ».

| Файл | sha256 | Байтів | Коли | URL |
|---|---|---|---|---|
| `atmega328p.pdf` | `b9b9d83cda56a95d999ea8d54fe5a540748ae9020e5e7ae19b913d384ba9320e` | 33319446 | 2026-08-26 | <https://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061B.pdf> |
| `ch340.pdf` | `04c805e8242885fd1cf21f05dbfd9d16b9fa38f0439ce0d3c6d7f74ebe4cf4af` | 147893 | 2026-08-26 | <https://cdn.sparkfun.com/datasheets/Dev/Arduino/Other/CH340DS1.PDF> |
| `cp2102.pdf` | `f025d9c738e4906544bbae493d5ff4a8d9746df247c92a329f4ed94799220e59` | 2172800 | 2026-08-26 | <https://www.silabs.com/documents/public/data-sheets/cp2102-9.pdf> |
| `ds18b20.pdf` | `39d191cd1fb657e43eac061f605bbd375d3c42dc40e7839c17fa0675bb0404d8` | 261896 | 2026-08-26 | — |
| `esp32-datasheet.pdf` | `a7917e6b47528c9dcab06837a49d452e582751335797db879f1cf2d17cd29adf` | 989523 | 2026-08-26 | — |
| `esp32-wroom-32e.pdf` | `4c7a345d1c1bfec34c38665639e39a7f43b79a35a12f6adcc2c7c0f83850f8b8` | 1230114 | 2026-08-26 | — |
| `hc-sr04.pdf` | `4ebdc3e1f70d84a1ca856d8fcd7f8b1f9e548a94e4012cd86d14ca0b30543b06` | 80625 | 2026-08-26 | <https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf> |
| `i2c-um10204.pdf` | `dc91f00f65584e06ef36e26c93bf9d91a95fb3c8a1830a9223e53caf678b36af` | 750958 | 2026-08-26 | <https://www.pololu.com/file/0J435/UM10204.pdf> |
| `ili9341.pdf` | `a9bbfdf6d078f54a6aca7a56cba91246905358d3a4ed738817bfd3f582b5741c` | 3667641 | 2026-08-26 | <https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf> |
| `ina219.pdf` | `58004eda854d07478e6fc6f4398c114f60a3bcf18d4877471c7c1a306d1fa1cb` | 892731 | 2026-08-26 | <https://www.ti.com/lit/ds/symlink/ina219.pdf> |
| `mcp23017.pdf` | `14159c6f5655e943e93ed1e34947e46844f114ec893f305a889898828e4055cb` | 865289 | 2026-08-26 | <https://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf> |
| `pcf8574.pdf` | `e632c2d07e07f559e5e13e6f55743c33522b859f5f32e8461bcda39ac33640a6` | 2808690 | 2026-08-26 | <https://www.ti.com/lit/ds/symlink/pcf8574.pdf> |
| `rfm69hcw.pdf` | `ff8efc4e1fe4135400760b9da1cfcabd52fe929e1be5ecee8bc03d1512f3c45c` | 1244847 | 2026-08-26 | — |
| `rp2040.pdf` | `be56fbb75ba0ae9e26558a73c93ac3e75c2ad4e6878d3b6703de2a76d886ea8c` | 5301205 | 2026-08-26 | <https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf> |
| `ssd1306.pdf` | `d55f875357de96d8c0e92153a389acc57e8bab4db7a0687f2e0bd3362f0036f6` | 1876686 | 2026-08-26 | <https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf> |
| `sx1276.pdf` | `6c24c19ee54309633d4a9057bb8663d1aacdb7f456bebcc6973728a07bd7854e` | 3268248 | 2026-08-26 | — |
