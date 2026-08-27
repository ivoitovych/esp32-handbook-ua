# Кеш зовнішніх джерел — маніфест

**Генерується** `tools/kesh.py`. Самі файли в git **не входять**: це
чужий матеріал під копірайтом, і перевидавати його ми не маємо права
(докладно — у шапці `tools/kesh.py`).

У git іде цей перелік. За ним будь-хто завантажує ті самі файли й
звіряє `sha256`: збігся — читає дослівно те саме, що цитував автор
доказу.

```sh
tools/kesh.py <URL>      завантажити й записати сюди
tools/kesh.py --check    звірити хеші наявних файлів
```

| Файл | sha256 | Байтів | Коли | URL |
|---|---|---|---|---|
| `0a-esp8266ex_datasheet_en.pdf` | `3a038e2fd3040ad06d95d41b16afc8292090339e9f8e728ce46a83db439cecf1` | 1244466 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf> |
| `ads1256.pdf` | `9da3323db162b59329ec1a865829441ff1605279cd802fe879649b6f54e100e6` | 811009 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/ads1256.pdf> |
| `esp-idf-esp_err.h` | `dcea6a47531d34026f988052a143fd3a9a9af4b176dbc86931dc3c519275afad` | 6648 | 2026-08-26 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h> |
| `esp32-c3-mini-1_datasheet_en.pdf` | `de7361381348d82a1abd337f10170be7a420675987568f71fe3c5b100deed270` | 1056106 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf> |
| `esp32-c3_datasheet_en.pdf` | `833fc000b4b3c3d39c496fcbd597fed5806956503ce7390b19cc8ae82f19f968` | 900158 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf> |
| `esp32-c5_datasheet_en.pdf` | `324eb57b2b1ccfc06002712ecbb05e62ad490217ad3e0c0e6de89bc03f599878` | 788087 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-c5_datasheet_en.pdf> |
| `esp32-p4_datasheet_en.pdf` | `fb4f3e91cc2ac519ec08cdec3dac9cb62b546cf5402ead1c5b83595a21bb6bc6` | 1576185 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-p4_datasheet_en.pdf> |
| `esp32-s2_datasheet_en.pdf` | `7c0c54f11e79cc77b09ae070221f056e2c21a3746a8f3a23a0371c4efcf8e02d` | 838510 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf> |
| `esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf` | `27d71971da07c280c6068d08c74720d1a25b8f20cf8494dc1765bdd28d40d435` | 1280501 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf> |
| `esp32-s3_datasheet_en.pdf` | `2d5a7cb7fd559d8d972bd88db32669c0196d23f22d7afaafb0f63d099b589a3f` | 1098115 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf> |
| `esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf` | `a3f8da7e17d03c0600af4ba62eb161411762de9d93e46755fae6178a294e5216` | 866305 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf> |
| `esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf` | `611e8506f352225e9ab09b4c2c3286885022b2f77a44ee8f0ab88a6302616f32` | 1425347 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf> |
| `esptool-boot-mode-selection.rst` | `2c3d8a8f37bf708f274b81a31521eb9489a70ff9a3041d2c5570d3bc7daa193c` | 21956 | 2026-08-26 | <https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst> |
| `tca9548a.pdf` | `2137822fd7128945ea44e83f4e100a932b30964d763715eeffe217ee6080a2dc` | 2772549 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/tca9548a.pdf> |
| `uk_UA.aff` | `2219dd15e9802adebc45722c60943b1472640260491af38dd3e43b07e75585e6` | 211759 | 2026-08-26 | <https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.aff> |
| `uk_UA.dic` | `2e5a9e67be63bdb089b3459addb5d71113319d13768e277bcae20f3cc1ad5a93` | 8919324 | 2026-08-26 | <https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.dic> |
| `uln2003a.pdf` | `0151daa4ffa9135f013c2c0e0150520c86f02154ce7d6d37e8ce9dbd91e79649` | 1850859 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/uln2003a.pdf> |

Файлів: **17**, разом **25.7 МБ** (межа 1.0 ГБ).

