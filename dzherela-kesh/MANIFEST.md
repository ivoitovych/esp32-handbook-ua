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
| `README.md` | `8c5a56fb8e19800c184ca5c78dde9a83d717444e6b50f523ea77bb26a0cdb3b1` | 12015 | 2026-08-27 | <https://raw.githubusercontent.com/micropython/micropython/master/ports/esp32/README.md> |
| `README.rst` | `5b49bf214fbd76a5e355e9cff7ff6fe6261259eff79cc6644a619cc444579206` | 18458 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/tools/mass_mfg/docs/README.rst> |
| `__init__.py` | `c96e9c960bf0bf9663fd7cec6c29915a348b80df788b3c457477d88aede93d6a` | 44437 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esptool/master/esptool/__init__.py> |
| `_cmds_loader___init___.py` | `c96e9c960bf0bf9663fd7cec6c29915a348b80df788b3c457477d88aede93d6a` | 44437 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esptool/master/esptool/{cmds,loader,__init__}.py> |
| `_esp_image_format_bootloader_utility_flash_partitions_.c` | `25f16aa394cdcee2958433a92afc255f7bbebc315f969af5695914bb665c5efc` | 3086 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/bootloader_support/src/{esp_image_format,bootloader_utility,flash_partitions}.c> |
| `_idf_component.yml_CHANGELOG.md_` | `b445b45b8ce496848e247b569090efc3ea1a8680b8e69a7309dbdeeb97eb9d51` | 1667 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/idf-extra-components/master/led_strip/{idf_component.yml,CHANGELOG.md}> |
| `_uart_pins.h_spi_pins.h_` | `c0e51fcd72a4ec38ebef9cc8593283e04f44434c57ec1bef200141c596b8edf4` | 717 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/{uart_pins.h,spi_pins.h}> |
| `a4988.pdf` | `c7341f95ab7d571d219ad2cdf495641da84a2452bcd196ffbda0f5ad93504ca0` | 1088839 | 2026-08-27 | <https://www.pololu.com/file/0J450/a4988.pdf> |
| `adc_calibration.rst` | `2fe4b4935252588fb3911cfdba600d0043c60bc9dcdce31ea63ee5cf8f63ed0b` | 11532 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/adc/adc_calibration.rst> |
| `adc_channel.h` | `ad7978d63111bb7d12764085155be0f35ea4a445c0af0949a54cb5ec42cbfa61` | 557 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32c3/include/soc/adc_channel.h> |
| `ads1256.pdf` | `9da3323db162b59329ec1a865829441ff1605279cd802fe879649b6f54e100e6` | 811009 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/ads1256.pdf> |
| `app_image_format.rst` | `ae53fe65b424900f3550f3ac419403dc80b0b3a9914321f0cda19c995bf2de9a` | 8485 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/app_image_format.rst> |
| `basic-options.rst` | `37c6cf71585569e62125bfe866c17f80ee3f3aa783fe7d29b809a8a68a5a1335` | 4080 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esptool/master/docs/en/esptool/basic-options.rst> |
| `bme280.c` | `7de1e7d3082b85e90db1daa34573ba77553a7caf44e06e216de5216b7ed4fa12` | 51082 | 2026-08-27 | <https://raw.githubusercontent.com/boschsensortec/BME280_SensorAPI/master/bme280.c> |
| `bootloader.rst` | `fa10719e3ce94193a4d2cb265aaa9ce957077982ae04844f164b86963bc4322f` | 20757 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/bootloader.rst> |
| `core_dump.rst` | `63d630020e8f1d97b0bb118a61e92424124191cb70490147872967868324cf11` | 14648 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/core_dump.rst> |
| `dac_channel.h` | `a561529fc5840f6a8dc994ed234f01787d08dceffc769a6f9bd8a4c222133854` | 605 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2}/include/soc/dac_channel.h> |
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
| `esp32.inc` | `8355c2b476ccb510e434be2b408b2215069dedb53aa29d6f713148dc5eb1cc97` | 4564 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32.inc> |
| `esp32.py` | `ef2909c2434abd9043aea0d17a35f37658661be75f4e6d6f9cf056f89ed53521` | 16331 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esptool/master/esptool/targets/esp32.py> |
| `esp32_api_reference_guide_en.pdf` | `52047976bcb1d83c0d20f796452f5bee659fdb48af5e36bf1ee2c52024c48755` | 13745 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32_api_reference_guide_en.pdf> |
| `esp32_datasheet_en.pdf` | `a7917e6b47528c9dcab06837a49d452e582751335797db879f1cf2d17cd29adf` | 989523 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf> |
| `esp32_technical_reference_manual_en.pdf` | `4ba58e9fa0405ec2bf80b912a29b483f6edc8c4b2b1058201913a2fe37e582f0` | 10173126 | 2026-08-27 | <https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf> |
| `esp32s3.inc` | `f4ffd123b1b671c058d38cfdfe21fc45a2e18eab7aff66ac850c1310cd73145e` | 4325 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio/esp32s3.inc> |
| `esp_crt_bundle.rst` | `4da6e1916a3afd725bb20aa3c37ce29ac558f8ad5ab0ddd24705198d0c03c1fb` | 7413 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/protocols/esp_crt_bundle.rst> |
| `esp_err.h` | `464ca4563b4cce491b3f6bfdc183d78528f65e50cbf5859d54230b654f981b4e` | 6624 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_common/include/esp_err.h> |
| `esp_now.rst` | `208e0e2c84ea54deffef68ea33cdfa97a4747aa8e71452f59a223b06a25b1874` | 11049 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst> |
| `esp_wifi.h` | `c4d568f9f0aa2f705bf6ec56b436a9d1e421bfaaa7e9fadec2eac2c364e3856f` | 78574 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_wifi/include/esp_wifi.h> |
| `esp_wifi.rst` | `bcc959ba939b4f94baf3b432903593bd772f985e413989214cd68ce56948d790` | 1387 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_wifi.rst> |
| `esp_wifi_types_generic.h` | `5454faef80ff2a105964f744726b60da0e0de9243eda28d859165ef86894490f` | 109155 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_wifi/include/esp_wifi_types_generic.h> |
| `esptool-boot-mode-selection.rst` | `2c3d8a8f37bf708f274b81a31521eb9489a70ff9a3041d2c5570d3bc7daa193c` | 21956 | 2026-08-26 | <https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst> |
| `establish-serial-connection.rst` | `bba80744dd1096733b2fd95a15a0b9b627741161c1b04c0f59bf31622cb4fd73` | 16750 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/establish-serial-connection.rst> |
| `flash-encryption.rst` | `a26497b185a754f866b924f93a8cb5a30ce95126fccaa127c850830a445d5058` | 90146 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/security/flash-encryption.rst> |
| `freertos.rst` | `cc699fdf7c4104c089a11b88587cf25afe83063c0628495e626d3db0550dafb2` | 9140 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos.rst> |
| `freertos_additions.rst` | `6b5f4f0c117b0296083e33f9b74b4011dd994678d92eede99667b64b1d98dc84` | 27480 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_additions.rst> |
| `freertos_idf.rst` | `a940425a9a17bec45ae79862d9985f263f873c787825563bde0dc4d492db4b43` | 31616 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst> |
| `gpio.rst` | `22e98c6beecd66bbad413748dc75a5047df5141e20a47748be276eab2ed5ce6d` | 10017 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gpio.rst> |
| `gpio_example_main.c` | `64cc3c1e28607dfa4ea411efe9c16cd83e07b93336ba9c499f8de530c5eabd67` | 4534 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/examples/peripherals/gpio/generic_gpio/main/gpio_example_main.c> |
| `gptimer.rst` | `b905858318435572d27c068f501c60f51901c04ece5756c4ffe50b77386c6433` | 27339 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/gptimer.rst> |
| `i2c.rst` | `39caf24f3f913292f8692dca67d295ca88c9c5201aa41fc489a10581fcedfcba` | 37533 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/i2c.rst> |
| `i2s.rst` | `5274a975617950a9860ee528cf75cabfe0256d4c7ecdd6a040845d6f9bf49298` | 86349 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/i2s.rst> |
| `idf-monitor.rst` | `655dcbe404b5275416f328c6861ad32cc1dfc9574a338f1af83f5f6abaf8ea71` | 26095 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/tools/idf-monitor.rst> |
| `idf-py.rst` | `128b7ca5b2ad71e11bdf8ff85e5ed7fd132b32e3ef21ccc90f336bb0589f7213` | 33214 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/tools/idf-py.rst> |
| `index.rst` | `2d85ddc9a6c38282afe73f8552b2565918d3729201dc2588d7852f68b5e49343` | 12667 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/get-started/index.rst> |
| `ldo_regulator.rst` | `c990aa81a666b41bfb1611df49a865a6b64372752e3379d6023b7374fc92cb01` | 4142 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/ldo_regulator.rst> |
| `ledc.rst` | `b98e37635f4dba363025b4174bf1d548f3d89bdf751705e6f730a05bb7827ef3` | 23515 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/ledc.rst> |
| `loader.py` | `0422e31127c8769c4a9486a28d5d668246fee143ab38320de7bbf6d6c11767aa` | 90127 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esptool/master/esptool/loader.py> |
| `log.rst` | `0ac055b9da921788c10c23c9633cc17773b0a3d92e69c1f3814d12282d69699b` | 41899 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/log.rst> |
| `machine.Pin.rst` | `bc97c94b8d09b0df4d3721ac0a79beb8ed0d41a8926c38cac727e7e93a6d45f7` | 12871 | 2026-08-27 | <https://raw.githubusercontent.com/micropython/micropython/master/docs/library/machine.Pin.rst> |
| `main.cpp` | `3a80fad62e9a4243aeb67ed1215fac81f47ba4ddc707db57850ec8cab68f1291` | 3048 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/arduino-esp32/master/cores/esp32/main.cpp> |
| `mcpwm_gen.rst` | `f78586c8cbc4caf6afde556bc780a82c0ca41cfdac7dfd884f3b8213fd8600ea` | 21556 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/mcpwm/mcpwm_gen.rst> |
| `mem_alloc.rst` | `cd79c74f6992e44b9f059e1f46ad19674d2226ad09e29ba06b44ed31b4f1d1b3` | 12661 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/mem_alloc.rst> |
| `memory-types.rst` | `40603321e949a896f6631a3020593d16bbeea7ae2f19f02d5857c7ce0d90f44f` | 13479 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/memory-types.rst> |
| `modbus.rst` | `e5294f6386cb79a0bd3e00e026a28ad325dce03e50edf4d920157743c20ab91d` | 961 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/protocols/modbus.rst> |
| `nvs_flash.h` | `0cd52e051a4d2ea17d2be9d412c2be965d9bb4bc614b81cda8ae5d6d77e9c86a` | 14970 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/components/nvs_flash/include/nvs_flash.h> |
| `ota.rst` | `b4df399efef9465532ecf746d312f614d922d08f8e7df40246cb38ad9c4d9ede` | 23919 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/ota.rst> |
| `partition-tables.rst` | `222c4845f8bd62d2727e7e2475e88f4bae4b7ab683c0bfd133763e79e5ac8371` | 29439 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/partition-tables.rst> |
| `pcnt.rst` | `a29e5761494d2ba48a39cef8722b5b55e3c225842683b7d8eed18da4d4c6d0f1` | 28563 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/pcnt.rst> |
| `pins_arduino.h` | `d8d56d687a293fa3a63a9f4ef1cd8f1eb2d9ff8f69424e60c37291e0f6eff7e0` | 980 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/arduino-esp32/master/variants/{esp32,esp32s3,esp32c3}/pins_arduino.h> |
| `platform.json` | `cfd206f4dabb664c5485124d5d9049e19abdcd807e144cf4e615205f96b0ae01` | 3877 | 2026-08-27 | <https://raw.githubusercontent.com/platformio/platform-espressif32/master/platform.json> |
| `platformio.ini` | `fe88a97fafd1036607d468367a3ce9c41be6eac46decb14f761dd9943ac7a331` | 1238 | 2026-08-27 | <https://raw.githubusercontent.com/platformio/platform-espressif32/master/examples/arduino-blink/platformio.ini> |
| `power_management.rst` | `a6e13363da26c28f9155f167ab09e49fa6cc3e2e0ddc35b995bea4a73c2ecb07` | 16913 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/power_management.rst> |
| `repl.rst` | `35fd321aeb4f4ea16a7e4e9336cb387d3a8650cd71d801526585b0fde9686031` | 10435 | 2026-08-27 | <https://raw.githubusercontent.com/micropython/micropython/master/docs/reference/repl.rst> |
| `reproducible-builds.rst` | `d7f1fd56e5193c75cb4e53f1f28bb1af584bf5fd98690867616608bee38b9e63` | 4867 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/reproducible-builds.rst> |
| `rmt.rst` | `93d528af698e62d64aa4b8ed3feef038218865df75e9d5e81e6d86bc37d23e75` | 55645 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/rmt.rst> |
| `sleep_modes.rst` | `a7ef3429b4b34f28cf92e00b555e110d11509817e0678d6434559d8a6368921e` | 45730 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/sleep_modes.rst> |
| `soc.h` | `0e897ca9260a40c63b7bcfaf45cea8da28e1e0250dec87f60b3330fa78dc4455` | 11486 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s2,esp32s3,esp32c3,esp32c6,esp32h2}/include/soc/soc.h> |
| `soc_caps.h` | `66b9da3debe8edfcbe5b76b16296415d0479df91db5721a8198e4afe214800df` | 24083 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/{esp32,esp32s3,esp32c3}/include/soc/soc_caps.h> |
| `spi_pins.h` | `c6517df7ce16e6772493cfbcf2398886317de45689c0c3a935ed18725b4f057f` | 1986 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/soc/esp32/include/soc/spi_pins.h> |
| `spiffs.rst` | `08ffca4518f5e9b999a3194c1ac8c12e422ca2b28b3d690e299fb2132caead62` | 8404 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/storage/spiffs.rst> |
| `startup.rst` | `1b0565862158869ff52d508c5ee66f8fccfbd5a9b44905fa95ff3569b2607f1b` | 14452 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/startup.rst> |
| `station_example_main.c` | `b406938b3a63ed2a03b041fd148cebc39e9c2e895f53016ca5e5e57ad9fa002b` | 7473 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/examples/wifi/getting_started/station/main/station_example_main.c> |
| `tca9548a.pdf` | `2137822fd7128945ea44e83f4e100a932b30964d763715eeffe217ee6080a2dc` | 2772549 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/tca9548a.pdf> |
| `tips-and-quirks.rst` | `a5f3543e992985fcea9c468a01d362f6912b913ed86ee07649904a7317760d30` | 22323 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-guides/jtag-debugging/tips-and-quirks.rst> |
| `uart.rst` | `61a4f976f204a7ace10ef42884bd6022b45f8675c45f3c07ee6ef2d22e8f618c` | 26802 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/peripherals/uart.rst> |
| `uart_pins.h` | `de6879e2b5014756ae945dc1caab06d57e2be6db6ddf2b255a77f5227728d018` | 1341 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/components/soc/esp32/include/soc/uart_pins.h> |
| `uk_UA.aff` | `2219dd15e9802adebc45722c60943b1472640260491af38dd3e43b07e75585e6` | 211759 | 2026-08-26 | <https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.aff> |
| `uk_UA.dic` | `2e5a9e67be63bdb089b3459addb5d71113319d13768e277bcae20f3cc1ad5a93` | 8919324 | 2026-08-26 | <https://raw.githubusercontent.com/LibreOffice/dictionaries/master/uk_UA/uk_UA.dic> |
| `uln2003a.pdf` | `0151daa4ffa9135f013c2c0e0150520c86f02154ce7d6d37e8ce9dbd91e79649` | 1850859 | 2026-08-27 | <https://www.ti.com/lit/ds/symlink/uln2003a.pdf> |
| `ulp.rst` | `af73bb6f8071e0ab2fc6eb923f87719df033a58765f6eeda17018d3be06b4180` | 2155 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/ulp.rst> |
| `wdts.rst` | `aab5499bba67e15e1327504328a9aa74ab88c82cb90f9c27d500d5b5d773c6af` | 16181 | 2026-08-27 | <https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/wdts.rst> |

Файлів: **95**, разом **39.5 МБ** (межа 1.0 ГБ).

