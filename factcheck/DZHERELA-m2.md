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
| `bh1750.pdf` | `190cbb7fcedf92c1d863888f50440114f0c3c048997bdbb97aa027a31a5495c3` | 427456 | 2026-08-26 | <https://www.pololu.com/file/0J1112/BH1750FVI.pdf> |
| `bme280.pdf` | `a2ccdb449fec94380742fe8eec851a11d9bd4142252d332b34682b4deecd7d89` | 1663806 | 2026-08-26 | <https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf> |
| `bmp280.pdf` | `473ff27d9df698b4757e36b36209f83b9f637b592c999d5fabe2a9453a488da6` | 1162932 | 2026-08-26 | <https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf> |
| `cdc-acm.c` | `0c9bca8f51278dcb87a952889cbd23f459cf0ea8d2a3d84cd2b8a2d08a941029` | 61131 | 2026-08-26 | <https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/class/cdc-acm.c> |
| `ch340.pdf` | `04c805e8242885fd1cf21f05dbfd9d16b9fa38f0439ce0d3c6d7f74ebe4cf4af` | 147893 | 2026-08-26 | <https://cdn.sparkfun.com/datasheets/Dev/Arduino/Other/CH340DS1.PDF> |
| `ch341.c` | `42dfb2e94a8e8a82cedc464a71e41f721caa36917d31d81dd792cb5ea4c03f2f` | 23133 | 2026-08-26 | <https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/serial/ch341.c> |
| `cp2102.pdf` | `f025d9c738e4906544bbae493d5ff4a8d9746df247c92a329f4ed94799220e59` | 2172800 | 2026-08-26 | <https://www.silabs.com/documents/public/data-sheets/cp2102-9.pdf> |
| `cp210x.c` | `8aa7d881db52ae9a7ff1b2d4e854474aae75542aec0abeded40cc69fd9cd2eb9` | 66727 | 2026-08-26 | <https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/serial/cp210x.c> |
| `ds18b20.pdf` | `39d191cd1fb657e43eac061f605bbd375d3c42dc40e7839c17fa0675bb0404d8` | 261896 | 2026-08-26 | — |
| `dw01.pdf` | `0f01ee674b66a5f92abe08bf9bd337b3a47484de49e97c77542e7b0a7cbbc0b7` | 616224 | 2026-08-26 | <http://www.ic-fortune.com/upload/Download/DW01A-DS-12_EN.pdf> |
| `esp32-datasheet.pdf` | `a7917e6b47528c9dcab06837a49d452e582751335797db879f1cf2d17cd29adf` | 989523 | 2026-08-26 | — |
| `esp32-wroom-32e.pdf` | `4c7a345d1c1bfec34c38665639e39a7f43b79a35a12f6adcc2c7c0f83850f8b8` | 1230114 | 2026-08-26 | — |
| `ftdi_sio_ids.h` | `eb445be64a4e96745c996d8481fb772ba0f8f2c9668f8adcf09c3be1ec9edbf7` | 62099 | 2026-08-26 | <https://raw.githubusercontent.com/torvalds/linux/master/drivers/usb/serial/ftdi_sio_ids.h> |
| `hc-sr04.pdf` | `4ebdc3e1f70d84a1ca856d8fcd7f8b1f9e548a94e4012cd86d14ca0b30543b06` | 80625 | 2026-08-26 | <https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf> |
| `i2c-um10204.pdf` | `dc91f00f65584e06ef36e26c93bf9d91a95fb3c8a1830a9223e53caf678b36af` | 750958 | 2026-08-26 | <https://www.pololu.com/file/0J435/UM10204.pdf> |
| `ili9341.pdf` | `a9bbfdf6d078f54a6aca7a56cba91246905358d3a4ed738817bfd3f582b5741c` | 3667641 | 2026-08-26 | <https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf> |
| `ina219.pdf` | `58004eda854d07478e6fc6f4398c114f60a3bcf18d4877471c7c1a306d1fa1cb` | 892731 | 2026-08-26 | <https://www.ti.com/lit/ds/symlink/ina219.pdf> |
| `ina226.pdf` | `c9b67f886d4a5241a5e070723f7b61867409eeb27eed768b9cdd9cb17e03ca2d` | 1516957 | 2026-08-26 | <https://www.ti.com/lit/ds/symlink/ina226.pdf> |
| `lghg2.pdf` | `13a74b9690c20f28f6ac36e12b06f8cce7b944d57c78682ff92131292f303b4f` | 345290 | 2026-08-26 | <https://www.batteryspace.com/prod-specs/9989.specs.pdf> |
| `lgmj1.pdf` | `c43a6ba93862318906a7fe8f2e34593890b1aa340ee59ff87e81bcfd8f1e8fc7` | 334905 | 2026-08-26 | <https://enerpower.de/wp-content/uploads/2016/03/Specification_INR18650MJ1.pdf> |
| `max31855.pdf` | `45904b81e79c46af49fd5c880df7ec04678c8599be9df73cea8422d241ceb7a2` | 1015656 | 2026-08-26 | <https://cdn-shop.adafruit.com/datasheets/MAX31855.pdf> |
| `max6675.pdf` | `f354adbf8b44b2b4d90840bf67c810386c717d80e943d828404f1add0c286bf9` | 133173 | 2026-08-26 | <https://cdn-shop.adafruit.com/datasheets/MAX6675.pdf> |
| `mcp23017.pdf` | `14159c6f5655e943e93ed1e34947e46844f114ec893f305a889898828e4055cb` | 865289 | 2026-08-26 | <https://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf> |
| `mcp2515.pdf` | `f2cf92a2d1ed42b285bf1e2395b859c91114f6a6774d90cf3e4ccda36b840aca` | 1164914 | 2026-08-26 | <https://ww1.microchip.com/downloads/en/DeviceDoc/MCP2515-Stand-Alone-CAN-Controller-with-SPI-20001801J.pdf> |
| `mpu6050.pdf` | `ccaa6312b9d86a9da79e26e511101e1150dc85a48255600010a854369cf7c05d` | 665861 | 2026-08-26 | <https://cdn.sparkfun.com/datasheets/Sensors/Accelerometers/RM-MPU-6000A.pdf> |
| `ncr18650b.pdf` | `b7aef4119cd1528c5eb7d584570ab0a7f33dafb274eb71047ced694202ace761` | 470950 | 2026-08-26 | <https://www.batteryspace.com/prod-specs/NCR18650B.pdf> |
| `pcf8574.pdf` | `e632c2d07e07f559e5e13e6f55743c33522b859f5f32e8461bcda39ac33640a6` | 2808690 | 2026-08-26 | <https://www.ti.com/lit/ds/symlink/pcf8574.pdf> |
| `rfm69hcw.pdf` | `ff8efc4e1fe4135400760b9da1cfcabd52fe929e1be5ecee8bc03d1512f3c45c` | 1244847 | 2026-08-26 | — |
| `rp2040.pdf` | `be56fbb75ba0ae9e26558a73c93ac3e75c2ad4e6878d3b6703de2a76d886ea8c` | 5301205 | 2026-08-26 | <https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf> |
| `samsung25r.pdf` | `938499741cdc4fde9e36521691521c2020c888f2a87c29fabdcce2941f63db76` | 881239 | 2026-08-26 | <https://www.powerstream.com/p/INR18650-25R-datasheet.pdf> |
| `samsung30q.pdf` | `39dbe4cd8bdd56273526e323581c09589dd95ff02868fc868f52b0048e14ddd2` | 5320021 | 2026-08-26 | <https://bluerobotics.com/wp-content/uploads/2018/10/INR18650-30Q-Data-Sheet.pdf> |
| `sht3x.pdf` | `095b1853e7f4328f5897c9ca6c392a7dd8b0202eda66b0a2629f9cb840dd496d` | 810136 | 2026-08-26 | <https://sensirion.com/media/documents/213E6A3B/63A5A569/Datasheet_SHT3x_DIS.pdf> |
| `sht4x.pdf` | `8db4a43f17149b76811cfb504caaeca4ef844ddc710cb9b45905c51c7ddfe3c2` | 1049911 | 2026-08-26 | <https://sensirion.com/media/documents/33FD6951/6A7C10A0/HT_DS_Datasheet_SHT4x_V7.3.pdf> |
| `ssd1306.pdf` | `d55f875357de96d8c0e92153a389acc57e8bab4db7a0687f2e0bd3362f0036f6` | 1876686 | 2026-08-26 | <https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf> |
| `st7789.pdf` | `8ecf0e438aa25554efc473a4cfe6e436f3fb33e68cd876b25041557235d04ca1` | 3203151 | 2026-08-26 | <https://newhavendisplay.com/appnotes/datasheets/LCDs/ST7789V.pdf> |
| `sx1276.pdf` | `6c24c19ee54309633d4a9057bb8663d1aacdb7f456bebcc6973728a07bd7854e` | 3268248 | 2026-08-26 | — |
| `tp4056.pdf` | `cdafa22618e7221fa93b8d432237cafb246a515606eef2672f50230d5ae205ce` | 60920 | 2026-08-26 | <https://dlnmh9ip6v2uc.cloudfront.net/datasheets/Prototyping/TP4056.pdf> |
| `vtc6.pdf` | `ff42082f0d94c311bfd9a8b24211c5d522aeee161adb7473731e9fe94fcc9f08` | 275509 | 2026-08-26 | <https://www.murata.com/-/media/webrenewal/products/batteries/cylindrical/datasheet/us18650vtc6-product-datasheet.ashx> |
