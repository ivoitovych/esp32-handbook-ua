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
| `esp-idf-esp_err.h` | `dcea6a47531d34026f988052a143fd3a9a9af4b176dbc86931dc3c519275afad` | 6648 | 2026-08-26 | <https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h> |
| `esptool-boot-mode-selection.rst` | `2c3d8a8f37bf708f274b81a31521eb9489a70ff9a3041d2c5570d3bc7daa193c` | 21956 | 2026-08-26 | <https://raw.githubusercontent.com/espressif/esptool/master/docs/en/advanced-topics/boot-mode-selection.rst> |

Файлів: **2**, разом **0.0 МБ** (межа 1.0 ГБ).

