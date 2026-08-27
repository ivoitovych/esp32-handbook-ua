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
| `20-bekap.md` | `eb97efa99cc66e56c5bb1387c5a94367fb410d7c7212ee282f681eca54968a0e` | 12411 | 2026-08-27 | <https://raw.githubusercontent.com/ivoitovych/esp32-handbook-ua/main/manual/20-bekap.md> |
| `21-seriyna.md` | `a0797835bda1ee558455e6ab0bbca9aedae9c480c00afe948befd0b5057e214d` | 12483 | 2026-08-27 | <https://raw.githubusercontent.com/ivoitovych/esp32-handbook-ua/main/manual/21-seriyna.md> |
| `22-zberezhennya-stanu.md` | `4944762be4187edaeddbf2befd902ae6c1b41dd1d92c41cd85f72eb201c8c94d` | 9624 | 2026-08-27 | <https://raw.githubusercontent.com/ivoitovych/esp32-handbook-ua/main/manual/22-zberezhennya-stanu.md> |
| `23-triazh.md` | `ce0a35ad537a910076218abf4bc32d27e155c22e4ae0cfed7b546d5ba7d70de1` | 12120 | 2026-08-27 | <https://raw.githubusercontent.com/ivoitovych/esp32-handbook-ua/main/manual/23-triazh.md> |
| `README.md` | `b098cb53f4810301ab31d26d3cc0c24310c960c66d7c40453a91be81dc2e5103` | 4439 | 2026-08-27 | <https://raw.githubusercontent.com/adafruit/Adafruit_SSD1306/master/README.md> |
| `a4988.pdf` | `c7341f95ab7d571d219ad2cdf495641da84a2452bcd196ffbda0f5ad93504ca0` | 1088839 | 2026-08-27 | <https://www.pololu.com/file/0J450/a4988.pdf> |
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
| `esp32_api_reference_guide_en.pdf` | `52047976bcb1d83c0d20f796452f5bee659fdb48af5e36bf1ee2c52024c48755` | 13745 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32_api_reference_guide_en.pdf> |
| `esp32_datasheet_en.pdf` | `a7917e6b47528c9dcab06837a49d452e582751335797db879f1cf2d17cd29adf` | 989523 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf> |
| `esp32_technical_reference_manual_en.pdf` | `4ba58e9fa0405ec2bf80b912a29b483f6edc8c4b2b1058201913a2fe37e582f0` | 10173126 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf> |
| `esptool-boot-mode-selection.rst` | `2c3d8a8f37bf708f274b81a31521eb9489a70ff9a3041d2c5570d3bc7daa193c` | 21956 | 2026-08-26 | <https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst> |
| `index.rst` | `dd1bab05c2269d9bc04ef36e395d6b2238066136e0fc1e5662c272a1846eddbd` | 4055 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/bluetooth/index.rst> |
| `tca9548a.pdf` | `2137822fd7128945ea44e83f4e100a932b30964d763715eeffe217ee6080a2dc` | 2772549 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/tca9548a.pdf> |
| `uk_UA.aff` | `2219dd15e9802adebc45722c60943b1472640260491af38dd3e43b07e75585e6` | 211759 | 2026-08-26 | <https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.aff> |
| `uk_UA.dic` | `2e5a9e67be63bdb089b3459addb5d71113319d13768e277bcae20f3cc1ad5a93` | 8919324 | 2026-08-26 | <https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.dic> |
| `uln2003a.pdf` | `0151daa4ffa9135f013c2c0e0150520c86f02154ce7d6d37e8ce9dbd91e79649` | 1850859 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/uln2003a.pdf> |

Файлів: **27**, разом **38.0 МБ** (межа 1.0 ГБ).

