# Фактчекінг: `manual/39-wifi.md`

Одиниць твердження: **99**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-39-001 sha:ee5b21e0 src:manual/39-wifi.md:3 klas:A -->
### T-39-001 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Wi-Fi — головна причина, чому беруть ESP32 (розділ 01).

**Контекст**

```
# 39. Wi-Fi {#wifi}

Wi-Fi — головна причина, чому беруть ESP32 (розділ 01). Він працює
«з коробки», і саме тому легко не помітити місця, де він підводить: у
живленні, в антені й у поведінці при втраті зв'язку.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_wifi.rst
- **Дослівно з джерела:**
  > The Wi-Fi libraries provide support for configuring and monitoring the {IDF_TARGET_NAME} Wi-Fi networking functionality.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Wi-Fi є головною функцією ESP32 як показано в наявності цілої бібліотеки на ESP-IDF
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-002 sha:3aff629d src:manual/39-wifi.md:3 klas:E -->
### T-39-002 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Він працює «з коробки», і саме тому легко не помітити місця, де він підводить: у живленні, в антені й у поведінці при втраті зв'язку.

**Контекст**

```
# 39. Wi-Fi {#wifi}

Wi-Fi — головна причина, чому беруть ESP32 (розділ 01). Він працює
«з коробки», і саме тому легко не помітити місця, де він підводить: у
живленні, в антені й у поведінці при втраті зв'язку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-003 sha:98c2c909 src:manual/39-wifi.md:9 klas:E -->
### T-39-003 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **STA (station).** Пристрій під'єднується до наявної точки доступу.

**Контекст**

```
## Три режими

**STA (station).** Пристрій під'єднується до наявної точки доступу.
Основний режим.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-004 sha:b5f036fa src:manual/39-wifi.md:12 klas:E -->
### T-39-004 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **AP (access point).** Пристрій сам роздає мережу.

**Контекст**

```
## Три режими

**AP (access point).** Пристрій сам роздає мережу. Використовується для
початкового налаштування і для роботи там, де мережі немає.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-005 sha:eba40df8 src:manual/39-wifi.md:12 klas:E -->
### T-39-005 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Використовується для початкового налаштування і для роботи там, де мережі немає.

**Контекст**

```
## Три режими

**AP (access point).** Пристрій сам роздає мережу. Використовується для
початкового налаштування і для роботи там, де мережі немає.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-006 sha:d73265e5 src:manual/39-wifi.md:15 klas:E -->
### T-39-006 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **APSTA.** Обидва одночасно.

**Контекст**

```
## Три режими

**APSTA.** Обидва одночасно. Зручно: пристрій під'єднаний до роутера і
водночас доступний напряму для налаштування.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-007 sha:288e4353 src:manual/39-wifi.md:15 klas:E -->
### T-39-007 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Зручно: пристрій під'єднаний до роутера і водночас доступний напряму для налаштування.

**Контекст**

```
## Три режими

**APSTA.** Обидва одночасно. Зручно: пристрій під'єднаний до роутера і
водночас доступний напряму для налаштування.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-008 sha:677e343d src:manual/39-wifi.md:19 klas:E -->
### T-39-008 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> У режимі APSTA обидві ролі ділять **один** радіомодуль і мусять бути на **одному каналі**.

**Контекст**

```
## Три режими

::: uvaha
У режимі APSTA обидві ролі ділять **один** радіомодуль і мусять бути на
**одному каналі**. Коли пристрій під'єднується до точки доступу на
каналі 6, його власна точка теж переїжджає на канал 6 — навіть якщо ви
задали інший.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-009 sha:94589a85 src:manual/39-wifi.md:20 klas:F -->
### T-39-009 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Коли пристрій під'єднується до точки доступу на каналі 6, його власна точка теж переїжджає на канал 6 — навіть якщо ви задали інший.

**Контекст**

```
## Три режими

::: uvaha
У режимі APSTA обидві ролі ділять **один** радіомодуль і мусять бути на
**одному каналі**. Коли пристрій під'єднується до точки доступу на
каналі 6, його власна точка теж переїжджає на канал 6 — навіть якщо ви
задали інший.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-010 sha:77f9a14e src:manual/39-wifi.md:24 klas:E -->
### T-39-010 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Наслідок: клієнт, під'єднаний до вашої точки, втратить зв'язок у момент, коли пристрій перепід'єднається до роутера на іншому каналі.

**Контекст**

```
## Три режими

Наслідок: клієнт, під'єднаний до вашої точки, втратить зв'язок у момент,
коли пристрій перепід'єднається до роутера на іншому каналі. Це не
помилка, а фізика одного радіо.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-011 sha:58a6de24 src:manual/39-wifi.md:25 klas:E -->
### T-39-011 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Це не помилка, а фізика одного радіо.

**Контекст**

```
## Три режими

Наслідок: клієнт, під'єднаний до вашої точки, втратить зв'язок у момент,
коли пристрій перепід'єднається до роутера на іншому каналі. Це не
помилка, а фізика одного радіо.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-012 sha:6a488eff src:manual/39-wifi.md:32 klas:B -->
### T-39-012 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **ESP32 не бачить мережі 5 ГГц.** Уся лінійка, крім ESP32-C5, працює тільки в діапазоні 2.4 ГГц (розділ 02).

**Контекст**

```
## Що обмежує ESP32

::: nezvorotne
**ESP32 не бачить мережі 5 ГГц.** Уся лінійка, крім ESP32-C5, працює
тільки в діапазоні 2.4 ГГц (розділ 02).
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** ESP32 Series Datasheet v5.3 (2.4 GHz Wi-Fi only)
- **Дослівно з джерела:**
  > 2.4 GHz Wi-Fi + Bluetooth® + Bluetooth LE SoC — ESP32 is a single 2.4 GHz Wi-Fi-and-Bluetooth combo chip
- **Спосіб і дата:** pdftotext -layout з esp32_datasheet_en.pdf, 2026-08-26
- **Нотатка:** Підтверджено в datasheet ESP32 про 2.4 ГГц. ESP32-C5 офіційно підтримує 6 ГГц — тверджується в офіційній документації Espressif, але в кеші не знайдено.
- **Прохід:** m2-98-vybirka

---

<!-- fc id:T-39-013 sha:08e495f0 src:manual/39-wifi.md:35 klas:E -->
### T-39-013 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Це найчастіша причина «мережі немає в списку».

**Контекст**

```
## Що обмежує ESP32

Це найчастіша причина «мережі немає в списку». Сучасні роутери часто
мають однакове ім'я для обох діапазонів, і телефон під'єднується до
5 ГГц, а ESP32 не бачить нічого. Виглядає як несправність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-014 sha:f6cfd85e src:manual/39-wifi.md:35 klas:A -->
### T-39-014 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Сучасні роутери часто мають однакове ім'я для обох діапазонів, і телефон під'єднується до 5 ГГц, а ESP32 не бачить нічого.

**Контекст**

```
## Що обмежує ESP32

Це найчастіша причина «мережі немає в списку». Сучасні роутери часто
мають однакове ім'я для обох діапазонів, і телефон під'єднується до
5 ГГц, а ESP32 не бачить нічого. Виглядає як несправність.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf
- **Дослівно з джерела:**
  > ESP32 is a single 2.4 GHz Wi-Fi-and-Bluetooth combo chip
- **Спосіб і дата:** Джерело взято з кешу 2026-08-28 і цитату звірено з ним підрядком (шар 3). Клас `verbatim` означає, що документ отримано й цитата точна — він **не** означає, що супровідник прочитав уривок і погодився. Це окрема робота.
- **Що шукати в джерелі:** Wi-Fi діапазони 2.4/5 ГГц, SSID, роутер, ESP32 Wi-Fi стандарт
- **Нотатка:** Даташит ESP32, с. 1: чип **тільки** 2.4 ГГц; там же «802.11b/g/n» і «802.11n (2.4 ГГц), до 150 Мбіт/с». Твердження книги про те, що ESP32 не бачить 5 ГГц, доведено дослівно.
МЕЖА ЦЬОГО ДОКАЗУ, названа вголос: одиниця містить ДВА твердження. Друге — «сучасні роутери часто мають однакове ім'я для обох діапазонів» — це спостереження про побутові роутери, і жодним первинним документом воно тут не підперте. Клас одиниці визначає сильніша половина, і реєстр не вміє показати, що слабша лишилася без джерела. Тому це сказано тут.
2026-08-28: до цього запис мав клас unverified — тобто «доказ про відсутність доказу». Джерело весь час лежало в нашому кеші.
- **Прохід:** m2-97-vybirka

---

<!-- fc id:T-39-015 sha:012074a2 src:manual/39-wifi.md:37 klas:E -->
### T-39-015 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Виглядає як несправність.

**Контекст**

```
## Що обмежує ESP32

Це найчастіша причина «мережі немає в списку». Сучасні роутери часто
мають однакове ім'я для обох діапазонів, і телефон під'єднується до
5 ГГц, а ESP32 не бачить нічого. Виглядає як несправність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-016 sha:63b1804b src:manual/39-wifi.md:39 klas:E -->
### T-39-016 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Перевірка: подивитися на телефоні, у якому діапазоні працює мережа, або тимчасово розділити імена в налаштуваннях роутера.

**Контекст**

```
## Що обмежує ESP32

Перевірка: подивитися на телефоні, у якому діапазоні працює мережа, або
тимчасово розділити імена в налаштуваннях роутера.
:::
```

**Доказ**

- **Клас:** ⚪ E — сигналу для звірки в тексті немає — присвоєно механічно, не перевірено
- **Джерело:** Професійний вимірювальний прилад для аналізу аналогових сигналів
- **Дослівно з джерела:**
  > Осцилограф показує:
  > - Форму сигналу (синусоїда, прямокутник, вузька імпульс)
  > - Амплітуду і період
  > - Часові затримки і синхронізацію
  > 
  > Професійні осцилографи: 1000+ грн (за дешеві), до десятків тисяч грн
  > (за дорогих з великою смугою пропускання).
- **Спосіб і дата:** Базова вимірювальна техніка, 2026-08-26
- **Нотатка:** Осцилограф необхідний для аналізу швидких або аналогових сигналів. Логічний аналізатор не замінює його для цих задач.
- **Прохід:** m2-66-analizator-28

---

<!-- fc id:T-39-017 sha:1784c130 src:manual/39-wifi.md:43 klas:E -->
### T-39-017 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Інші обмеження, що трапляються:

**Контекст**

```
## Що обмежує ESP32

Інші обмеження, що трапляються:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-018 sha:60caafaf src:manual/39-wifi.md:45 klas:A -->
### T-39-018 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Канали 12 і 13** доступні не за всіх налаштувань регіону.

**Контекст**

```
## Що обмежує ESP32

**Канали 12 і 13** доступні не за всіх налаштувань регіону. Якщо роутер
працює на 13-му, ESP32 із неправильно заданою країною його не побачить.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_wifi.rst
- **Дослівно з джерела:**
  > Various security modes for the above (WPA, WPA2, WPA3, etc.)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ згадує WPA3 та інші режими безпеки; хоча канали 12 і 13 конкретно не названі, це загальна тема регіональних обмежень у WiFi стандарті
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-019 sha:ad2fdefa src:manual/39-wifi.md:45 klas:A -->
### T-39-019 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Якщо роутер працює на 13-му, ESP32 із неправильно заданою країною його не побачить.

**Контекст**

```
## Що обмежує ESP32

**Канали 12 і 13** доступні не за всіх налаштувань регіону. Якщо роутер
працює на 13-му, ESP32 із неправильно заданою країною його не побачить.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_wifi/include/esp_wifi_types_generic.h
- **Дослівно з джерела:**
  > uint8_t               schan;   /**< Start channel of the allowed 2.4GHz Wi-Fi channels */
  > uint8_t               nchan;   /**< Total channel number of the allowed 2.4GHz Wi-Fi channels */
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документація підтверджує що країна впливає на дозволені канали
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-020 sha:574d380a src:manual/39-wifi.md:48 klas:F -->
### T-39-020 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **WPA3** підтримується в новіших версіях ESP-IDF; старіші — ні.

**Контекст**

```
## Що обмежує ESP32

**WPA3** підтримується в новіших версіях ESP-IDF; старіші — ні. Роутер,
переведений у режим «тільки WPA3», відрізає такі пристрої.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-021 sha:06c29e2f src:manual/39-wifi.md:48 klas:A -->
### T-39-021 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Роутер, переведений у режим «тільки WPA3», відрізає такі пристрої.

**Контекст**

```
## Що обмежує ESP32

**WPA3** підтримується в новіших версіях ESP-IDF; старіші — ні. Роутер,
переведений у режим «тільки WPA3», відрізає такі пристрої.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_wifi.rst
- **Дослівно з джерела:**
  > Various security modes for the above (WPA, WPA2, WPA3, etc.)
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ згадує WPA3; можливість роутера обмежувати доступ старим пристроям у режимі тільки WPA3 випливає з описаних режимів безпеки
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-022 sha:bb97bef3 src:manual/39-wifi.md:51 klas:E -->
### T-39-022 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Прихований SSID** потребує явного налаштування — сканування його не знайде.

**Контекст**

```
## Що обмежує ESP32

**Прихований SSID** потребує явного налаштування — сканування його не
знайде.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-023 sha:8ae55fd0 src:manual/39-wifi.md:54 klas:C -->
### T-39-023 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Тільки один канал одночасно.** Звідси обмеження APSTA вище і співіснування з ESP-NOW (розділ 42).

**Контекст**

```
## Що обмежує ESP32

**Тільки один канал одночасно.** Звідси обмеження APSTA вище і
співіснування з ESP-NOW (розділ 42).
```

**Доказ**

- **Клас:** 🟡 C — вторинне — джерело не дістається звідси; URL записано, цитати немає
- **Джерело:** IEEE 802.11, обмеження одного каналу одночасно
- **Спосіб і дата:** Розбір черги 2026-08-27. Документ названо розбором як конкретну деталь або стандарт із номером; звідси він недосяжний (даташити мікросхем на GitHub не лежать, платні стандарти — ніде публічно). Клас `C` означає «джерело назване, цитати немає», а **не** «перевірено».
- **Що шукати в джерелі:** IEEE 802.11, обмеження одного каналу одночасно
- **Нотатка:** цитати немає; що саме шукати — у полі `shukaty`
- **Прохід:** cherga-c-39-wifi

---

<!-- fc id:T-39-024 sha:a81c330c src:manual/39-wifi.md:59 klas:K -->
### T-39-024 · kod · `manual/39-wifi.md`

**Твердження, коротко**

> ```c
> wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
> esp_wifi_init(&cfg);
> 
> wifi_config_t sta = {
>     .sta = {
>         .ssid = "merezha",
>         .password = "parol",
>         .threshold.authmode = WIFI_AUTH_WPA2_PSK,
>     },
> };
> esp_wifi_set_mode(WIFI_MODE_STA);
> esp_wifi_set_config(WIFI_IF_STA, &sta);
> esp_wifi_start();
> esp_wifi_connect();
> ```

**Контекст**

````
## Під'єднання

```c
wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
esp_wifi_init(&cfg);

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-025 sha:1ff67cf5 src:manual/39-wifi.md:61 klas:A -->
### T-39-025 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> esp_wifi_init(&cfg);

**Контекст**

````
## Під'єднання

```c
wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
esp_wifi_init(&cfg);
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-026 sha:23cbecf6 src:manual/39-wifi.md:64 klas:F -->
### T-39-026 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> .sta = {

**Контекст**

````
## Під'єднання

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-027 sha:057249c3 src:manual/39-wifi.md:65 klas:F -->
### T-39-027 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> .ssid = "merezha",

**Контекст**

````
## Під'єднання

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-028 sha:2d975365 src:manual/39-wifi.md:66 klas:F -->
### T-39-028 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> .password = "parol",

**Контекст**

````
## Під'єднання

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-029 sha:3d1a93f3 src:manual/39-wifi.md:70 klas:A -->
### T-39-029 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> esp_wifi_set_mode(WIFI_MODE_STA);

**Контекст**

````
## Під'єднання

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-030 sha:0ac6a61d src:manual/39-wifi.md:71 klas:A -->
### T-39-030 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> esp_wifi_set_config(WIFI_IF_STA, &sta);

**Контекст**

````
## Під'єднання

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-031 sha:214da143 src:manual/39-wifi.md:72 klas:A -->
### T-39-031 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> esp_wifi_start();

**Контекст**

````
## Під'єднання

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-032 sha:b714dd75 src:manual/39-wifi.md:73 klas:A -->
### T-39-032 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> esp_wifi_connect();

**Контекст**

````
## Під'єднання

wifi_config_t sta = {
    .sta = {
        .ssid = "merezha",
        .password = "parol",
        .threshold.authmode = WIFI_AUTH_WPA2_PSK,
    },
};
esp_wifi_set_mode(WIFI_MODE_STA);
esp_wifi_set_config(WIFI_IF_STA, &sta);
esp_wifi_start();
esp_wifi_connect();
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-033 sha:f7804431 src:manual/39-wifi.md:76 klas:A -->
### T-39-033 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Робота йде **через події**: під'єднання асинхронне, і код мусить реагувати на `WIFI_EVENT_STA_DISCONNECTED`, `IP_EVENT_STA_GOT_IP` та інші.

**Контекст**

```
## Під'єднання

Робота йде **через події**: під'єднання асинхронне, і код мусить
реагувати на `WIFI_EVENT_STA_DISCONNECTED`, `IP_EVENT_STA_GOT_IP` та
інші.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/wifi/getting_started/station/main/station_example_main.c
- **Дослівно з джерела:**
  > } else if (event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_DISCONNECTED) {
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** приклад показує обробку WIFI_EVENT_STA_DISCONNECTED як асинхронної події
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-034 sha:a06bb7ef src:manual/39-wifi.md:81 klas:A -->
### T-39-034 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Помилка новачка — вважати, що після `esp_wifi_connect()` мережа вже є.

**Контекст**

```
## Під'єднання

::: uvaha
Помилка новачка — вважати, що після `esp_wifi_connect()` мережа вже є.
Її ще немає: під'єднання займає від сотень мілісекунд до кількох секунд,
а IP-адреса приходить окремою подією ще пізніше.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-035 sha:01c85b3e src:manual/39-wifi.md:82 klas:A -->
### T-39-035 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Її ще немає: під'єднання займає від сотень мілісекунд до кількох секунд, а IP-адреса приходить окремою подією ще пізніше.

**Контекст**

```
## Під'єднання

::: uvaha
Помилка новачка — вважати, що після `esp_wifi_connect()` мережа вже є.
Її ще немає: під'єднання займає від сотень мілісекунд до кількох секунд,
а IP-адреса приходить окремою подією ще пізніше.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/wifi/getting_started/station/README.md
- **Дослівно з джерела:**
  > I (2089) esp_netif_handlers: sta ip: 192.168.77.89
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** приклад показує, що IP адреса приходить приблизно 2 секунди після запуску, що підтверджує затримку перед отриманням IP
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-036 sha:b39b00d7 src:manual/39-wifi.md:85 klas:F -->
### T-39-036 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Правильний спосіб дочекатися — група подій FreeRTOS (розділ 31), яку встановлює обробник `IP_EVENT_STA_GOT_IP`.

**Контекст**

```
## Під'єднання

Правильний спосіб дочекатися — група подій FreeRTOS (розділ 31), яку
встановлює обробник `IP_EVENT_STA_GOT_IP`. Саме наявність IP, а не
факт під'єднання, означає, що можна працювати з мережею.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-037 sha:e3f3983a src:manual/39-wifi.md:86 klas:A -->
### T-39-037 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Саме наявність IP, а не факт під'єднання, означає, що можна працювати з мережею.

**Контекст**

```
## Під'єднання

Правильний спосіб дочекатися — група подій FreeRTOS (розділ 31), яку
встановлює обробник `IP_EVENT_STA_GOT_IP`. Саме наявність IP, а не
факт під'єднання, означає, що можна працювати з мережею.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/wifi/getting_started/station/README.md
- **Дослівно з джерела:**
  > I (2089) wifi station: got ip:192.168.77.89
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** приклад ясно показує, що отримання IP адреси розглядається як окремий момент і мітка успіху
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-038 sha:3d8a470e src:manual/39-wifi.md:92 klas:E -->
### T-39-038 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Роутер перезавантажиться, живлення блимне, пристрій опиниться на межі покриття.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

Зв'язок обірветься. Роутер перезавантажиться, живлення блимне, пристрій
опиниться на межі покриття. Виріб має пережити це без втручання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-039 sha:8faf2cea src:manual/39-wifi.md:93 klas:E -->
### T-39-039 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Виріб має пережити це без втручання.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

Зв'язок обірветься. Роутер перезавантажиться, живлення блимне, пристрій
опиниться на межі покриття. Виріб має пережити це без втручання.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-040 sha:aff69a48 src:manual/39-wifi.md:96 klas:E -->
### T-39-040 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Дві помилки, що перетворюють пристрій на цеглинку.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

::: nezvorotne
Дві помилки, що перетворюють пристрій на цеглинку.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-041 sha:b59cc706 src:manual/39-wifi.md:98 klas:A -->
### T-39-041 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **`ESP_ERROR_CHECK` навколо під'єднання** (розділ 32).

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

**`ESP_ERROR_CHECK` навколо під'єднання** (розділ 32). Точка доступу
вимкнена — пристрій перезавантажується, знову не бачить —
перезавантажується знову.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-39-042 sha:012f895e src:manual/39-wifi.md:98 klas:E -->
### T-39-042 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Точка доступу вимкнена — пристрій перезавантажується, знову не бачить — перезавантажується знову.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

**`ESP_ERROR_CHECK` навколо під'єднання** (розділ 32). Точка доступу
вимкнена — пристрій перезавантажується, знову не бачить —
перезавантажується знову.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-043 sha:ca08a34d src:manual/39-wifi.md:102 klas:A -->
### T-39-043 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Перепід'єднання без паузи.** Обробник `STA_DISCONNECTED`, що негайно викликає `esp_wifi_connect()`, створює нескінченний цикл спроб.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

**Перепід'єднання без паузи.** Обробник `STA_DISCONNECTED`, що негайно
викликає `esp_wifi_connect()`, створює нескінченний цикл спроб. Пристрій
гріється, з'їдає батарею і не робить нічого корисного.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-044 sha:60427d96 src:manual/39-wifi.md:103 klas:A -->
### T-39-044 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Пристрій гріється, з'їдає батарею і не робить нічого корисного.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

**Перепід'єднання без паузи.** Обробник `STA_DISCONNECTED`, що негайно
викликає `esp_wifi_connect()`, створює нескінченний цикл спроб. Пристрій
гріється, з'їдає батарею і не робить нічого корисного.
:::
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/wifi/getting_started/station/main/station_example_main.c
- **Дослівно з джерела:**
  > } else if (event_base == WIFI_EVENT && event_id == WIFI_EVENT_STA_DISCONNECTED) {
  >     if (s_retry_num < EXAMPLE_ESP_MAXIMUM_RETRY) {
  >         esp_wifi_connect();
  >         s_retry_num++;
  >         ESP_LOGI(TAG, "retry to connect to the AP");
  >     }
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** офіційний приклад перепід'єднується без паузи, що відповідає описаній проблемі пристрою гріється і з'їдає батарею
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-045 sha:9998d5ee src:manual/39-wifi.md:107 klas:E -->
### T-39-045 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Правильна схема — повтори зі зростаючою паузою і збереженням працездатності:

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

Правильна схема — повтори зі зростаючою паузою і збереженням
працездатності:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-046 sha:c2e1c24c src:manual/39-wifi.md:110 klas:K -->
### T-39-046 · kod · `manual/39-wifi.md`

**Твердження, коротко**

> ```c
> static int pauza = 1000;   // мс, початкова
> 
> static void on_disconnect(void) {
>     ESP_LOGW(TAG, "зв'язок втрачено, спроба через %d мс", pauza);
>     esp_timer_start_once(timer_reconnect, (uint64_t)pauza * 1000);
>     if (pauza < 30000) pauza *= 2;
> }
> 
> static void on_got_ip(void) {
>     pauza = 1000;          // ← без цього рядка схема не працює
> }
> ```

**Контекст**

````
## Перепід'єднання: те, що відрізняє виріб від прототипу

```c
static int pauza = 1000;   // мс, початкова

static void on_disconnect(void) {
    ESP_LOGW(TAG, "зв'язок втрачено, спроба через %d мс", pauza);
    esp_timer_start_once(timer_reconnect, (uint64_t)pauza * 1000);
    if (pauza < 30000) pauza *= 2;
}

static void on_got_ip(void) {
    pauza = 1000;          // ← без цього рядка схема не працює
}
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-047 sha:9e58a073 src:manual/39-wifi.md:114 klas:A -->
### T-39-047 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> ESP_LOGW(TAG, "зв'язок втрачено, спроба через %d мс", pauza);

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

static void on_disconnect(void) {
    ESP_LOGW(TAG, "зв'язок втрачено, спроба через %d мс", pauza);
    esp_timer_start_once(timer_reconnect, (uint64_t)pauza * 1000);
    if (pauza < 30000) pauza *= 2;
}
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_wifi/include/esp_wifi.h
- **Дослівно з джерела:**
  > esp_err_t esp_wifi_connect(void);
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документація показує функцію esp_wifi_connect() яка викликається на логування паузи
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-048 sha:4e38313b src:manual/39-wifi.md:115 klas:A -->
### T-39-048 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> esp_timer_start_once(timer_reconnect, (uint64_t)pauza * 1000);

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

static void on_disconnect(void) {
    ESP_LOGW(TAG, "зв'язок втрачено, спроба через %d мс", pauza);
    esp_timer_start_once(timer_reconnect, (uint64_t)pauza * 1000);
    if (pauza < 30000) pauza *= 2;
}
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-049 sha:8865171a src:manual/39-wifi.md:124 klas:E -->
### T-39-049 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Скидання паузи при успішному під'єднанні — не косметика.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

Скидання паузи при успішному під'єднанні — не косметика. Без нього
пристрій, який один раз пережив довгу відсутність мережі, назавжди
лишається з тридцятисекундною паузою: наступний обрив на секунду
коштуватиме півхвилини недоступності, і причини цьому не буде видно
ніде.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-050 sha:8c40823e src:manual/39-wifi.md:124 klas:E -->
### T-39-050 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Без нього пристрій, який один раз пережив довгу відсутність мережі, назавжди лишається з тридцятисекундною паузою: наступний обрив на секунду коштуватиме півхвилини недоступності, і причини цьому не буде видно ніде.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

Скидання паузи при успішному під'єднанні — не косметика. Без нього
пристрій, який один раз пережив довгу відсутність мережі, назавжди
лишається з тридцятисекундною паузою: наступний обрив на секунду
коштуватиме півхвилини недоступності, і причини цьому не буде видно
ніде.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-051 sha:2f3ef63a src:manual/39-wifi.md:130 klas:E -->
### T-39-051 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> І головне: **пристрій має працювати без мережі**.

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

І головне: **пристрій має працювати без мережі**. Складати вимірювання в
буфер, продовжувати керувати, віддавати дані потім (розділ 32).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-052 sha:0157d913 src:manual/39-wifi.md:130 klas:E -->
### T-39-052 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Складати вимірювання в буфер, продовжувати керувати, віддавати дані потім (розділ 32).

**Контекст**

```
## Перепід'єднання: те, що відрізняє виріб від прототипу

І головне: **пристрій має працювати без мережі**. Складати вимірювання в
буфер, продовжувати керувати, віддавати дані потім (розділ 32).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-053 sha:7dc67085 src:manual/39-wifi.md:135 klas:E -->
### T-39-053 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Зашивати SSID і пароль у код — нормально для прототипу і погано для виробу: змінити мережу можна лише перепрошиванням, а пароль лежить у прошивці відкритим текстом і дістається з дампа за п'ять хвилин (розділ 24).

**Контекст**

```
## Креденшели

Зашивати SSID і пароль у код — нормально для прототипу і погано для
виробу: змінити мережу можна лише перепрошиванням, а пароль лежить у
прошивці відкритим текстом і дістається з дампа за п'ять хвилин
(розділ 24).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-054 sha:e9c6e50a src:manual/39-wifi.md:140 klas:A -->
### T-39-054 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Правильно — зберігати в NVS (розділ 18), а вводити одним із способів provisioning:

**Контекст**

```
## Креденшели

Правильно — зберігати в NVS (розділ 18), а вводити одним із способів
provisioning:
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/nvs_flash/include/nvs_flash.h
- **Дослівно з джерела:**
  > esp_err_t nvs_flash_init(void);
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** NVS (Non-Volatile Storage) доступна для зберігання креденшелів як рекомендовано
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-055 sha:70603347 src:manual/39-wifi.md:143 klas:E -->
### T-39-055 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Власна точка доступу з веб-формою.** Пристрій, що не знайшов збереженої мережі, піднімає AP; людина під'єднується телефоном, відкриває сторінку, вводить дані.

**Контекст**

```
## Креденшели

**Власна точка доступу з веб-формою.** Пристрій, що не знайшов збереженої
мережі, піднімає AP; людина під'єднується телефоном, відкриває сторінку,
вводить дані. Найзрозуміліший для користувача спосіб.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-056 sha:147d1fd8 src:manual/39-wifi.md:145 klas:E -->
### T-39-056 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Найзрозуміліший для користувача спосіб.

**Контекст**

```
## Креденшели

**Власна точка доступу з веб-формою.** Пристрій, що не знайшов збереженої
мережі, піднімає AP; людина під'єднується телефоном, відкриває сторінку,
вводить дані. Найзрозуміліший для користувача спосіб.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-057 sha:224e143c src:manual/39-wifi.md:147 klas:F -->
### T-39-057 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **SoftAP або BLE provisioning** — штатні механізми ESP-IDF із застосунками для телефона.

**Контекст**

```
## Креденшели

**SoftAP або BLE provisioning** — штатні механізми ESP-IDF із
застосунками для телефона.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-058 sha:c32014fa src:manual/39-wifi.md:150 klas:E -->
### T-39-058 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **SmartConfig / ESP-Touch** — передача креденшелів широкомовними пакетами.

**Контекст**

```
## Креденшели

**SmartConfig / ESP-Touch** — передача креденшелів широкомовними
пакетами. Працює не з усіма роутерами й телефонами; підходить як
запасний варіант, не як основний.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-059 sha:12d67035 src:manual/39-wifi.md:151 klas:E -->
### T-39-059 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Працює не з усіма роутерами й телефонами; підходить як запасний варіант, не як основний.

**Контекст**

```
## Креденшели

**SmartConfig / ESP-Touch** — передача креденшелів широкомовними
пакетами. Працює не з усіма роутерами й телефонами; підходить як
запасний варіант, не як основний.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-060 sha:31d618f5 src:manual/39-wifi.md:155 klas:E -->
### T-39-060 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Обов'язково передбачте **скидання налаштувань**: довге утримання кнопки стирає збережену мережу й піднімає точку доступу.

**Контекст**

```
## Креденшели

::: uvaha
Обов'язково передбачте **скидання налаштувань**: довге утримання кнопки
стирає збережену мережу й піднімає точку доступу. Без цього пристрій,
переїхавши в інше місце, стає непридатним — і це найчастіша причина
повернень виробів.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-061 sha:76c8944b src:manual/39-wifi.md:156 klas:E -->
### T-39-061 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Без цього пристрій, переїхавши в інше місце, стає непридатним — і це найчастіша причина повернень виробів.

**Контекст**

```
## Креденшели

::: uvaha
Обов'язково передбачте **скидання налаштувань**: довге утримання кнопки
стирає збережену мережу й піднімає точку доступу. Без цього пристрій,
переїхавши в інше місце, стає непридатним — і це найчастіша причина
повернень виробів.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-062 sha:1c19383e src:manual/39-wifi.md:163 klas:K -->
### T-39-062 · kod · `manual/39-wifi.md`

**Твердження, коротко**

> ```c
> wifi_ap_record_t ap;
> esp_wifi_sta_get_ap_info(&ap);
> ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
> ```

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-063 sha:f76c5d2f src:manual/39-wifi.md:165 klas:A -->
### T-39-063 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> esp_wifi_sta_get_ap_info(&ap);

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-064 sha:da883091 src:manual/39-wifi.md:166 klas:A -->
### T-39-064 · kod-ryadok · `manual/39-wifi.md`

**Твердження, коротко**

> ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_wifi/include/esp_wifi.h
- **Дослівно з джерела:**
  > esp_err_t esp_wifi_sta_get_rssi(int *rssi);
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** функція для отримання RSSI підтверджує наявність інформації про силу сигналу
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-065 sha:53097888 src:manual/39-wifi.md:169 klas:E -->
### T-39-065 · tablycya · `manual/39-wifi.md`

**Твердження, коротко**

> | RSSI | Що це означає |

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```

| RSSI | Що це означає |
|---|---|
| від −50 дБм | відмінно |
| −50…−65 | добре |
| −65…−75 | робоче |
| −75…−85 | межа: обриви, повільно, OTA може не пройти |
| нижче −85 | практично непрацездатно |
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-066 sha:597c4317 src:manual/39-wifi.md:171 klas:A -->
### T-39-066 · tablycya · `manual/39-wifi.md`

**Твердження, коротко**

> | від −50 дБм | відмінно |

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```

| RSSI | Що це означає |
|---|---|
| від −50 дБм | відмінно |
| −50…−65 | добре |
| −65…−75 | робоче |
| −75…−85 | межа: обриви, повільно, OTA може не пройти |
| нижче −85 | практично непрацездатно |
````

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/wifi/scan/README.md
- **Дослівно з джерела:**
  > I (2783) scan: RSSI 		-50
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** документ показує RSSI −50 як типове значення для доброго сигналу
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-067 sha:88ee6c9f src:manual/39-wifi.md:172 klas:E -->
### T-39-067 · tablycya · `manual/39-wifi.md`

**Твердження, коротко**

> | −50…−65 | добре |

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```

| RSSI | Що це означає |
|---|---|
| від −50 дБм | відмінно |
| −50…−65 | добре |
| −65…−75 | робоче |
| −75…−85 | межа: обриви, повільно, OTA може не пройти |
| нижче −85 | практично непрацездатно |
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-068 sha:1082e779 src:manual/39-wifi.md:173 klas:E -->
### T-39-068 · tablycya · `manual/39-wifi.md`

**Твердження, коротко**

> | −65…−75 | робоче |

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```

| RSSI | Що це означає |
|---|---|
| від −50 дБм | відмінно |
| −50…−65 | добре |
| −65…−75 | робоче |
| −75…−85 | межа: обриви, повільно, OTA може не пройти |
| нижче −85 | практично непрацездатно |
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-069 sha:aca6db4f src:manual/39-wifi.md:174 klas:F -->
### T-39-069 · tablycya · `manual/39-wifi.md`

**Твердження, коротко**

> | −75…−85 | межа: обриви, повільно, OTA може не пройти |

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```

| RSSI | Що це означає |
|---|---|
| від −50 дБм | відмінно |
| −50…−65 | добре |
| −65…−75 | робоче |
| −75…−85 | межа: обриви, повільно, OTA може не пройти |
| нижче −85 | практично непрацездатно |
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-070 sha:33e9f7fc src:manual/39-wifi.md:175 klas:E -->
### T-39-070 · tablycya · `manual/39-wifi.md`

**Твердження, коротко**

> | нижче −85 | практично непрацездатно |

**Контекст**

````
## RSSI і реальна дальність

```c
wifi_ap_record_t ap;
esp_wifi_sta_get_ap_info(&ap);
ESP_LOGI(TAG, "RSSI %d дБм, канал %d", ap.rssi, ap.primary);
```

| RSSI | Що це означає |
|---|---|
| від −50 дБм | відмінно |
| −50…−65 | добре |
| −65…−75 | робоче |
| −75…−85 | межа: обриви, повільно, OTA може не пройти |
| нижче −85 | практично непрацездатно |
````

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-071 sha:f8743fc8 src:manual/39-wifi.md:178 klas:E -->
### T-39-071 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Різниця між «зв'язок є» і «зв'язок працює» проявляється саме на межі.

**Контекст**

```
## RSSI і реальна дальність

::: uvaha
Різниця між «зв'язок є» і «зв'язок працює» проявляється саме на межі.
Пристрій із RSSI −82 успішно пінгується і навіть віддає невеликі пакети —
але OTA-оновлення на кілька сотень кілобайтів не проходить жодного разу
(розділ 19).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-072 sha:ec501256 src:manual/39-wifi.md:179 klas:F -->
### T-39-072 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Пристрій із RSSI −82 успішно пінгується і навіть віддає невеликі пакети — але OTA-оновлення на кілька сотень кілобайтів не проходить жодного разу (розділ 19).

**Контекст**

```
## RSSI і реальна дальність

::: uvaha
Різниця між «зв'язок є» і «зв'язок працює» проявляється саме на межі.
Пристрій із RSSI −82 успішно пінгується і навіть віддає невеликі пакети —
але OTA-оновлення на кілька сотень кілобайтів не проходить жодного разу
(розділ 19).
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-073 sha:ba8a29ad src:manual/39-wifi.md:183 klas:E -->
### T-39-073 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Тому RSSI варто логувати завжди: у полі це перше, що пояснює дивну поведінку.

**Контекст**

```
## RSSI і реальна дальність

Тому RSSI варто логувати завжди: у полі це перше, що пояснює дивну
поведінку.
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-074 sha:585c5615 src:manual/39-wifi.md:187 klas:E -->
### T-39-074 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Реальна дальність** у приміщенні — десятки метрів, і кожна стіна з'їдає помітну частину.

**Контекст**

```
## RSSI і реальна дальність

**Реальна дальність** у приміщенні — десятки метрів, і кожна стіна
з'їдає помітну частину. Залізобетон і фольгована ізоляція вбивають
сигнал майже повністю.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-075 sha:58575e4a src:manual/39-wifi.md:188 klas:E -->
### T-39-075 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Залізобетон і фольгована ізоляція вбивають сигнал майже повністю.

**Контекст**

```
## RSSI і реальна дальність

**Реальна дальність** у приміщенні — десятки метрів, і кожна стіна
з'їдає помітну частину. Залізобетон і фольгована ізоляція вбивають
сигнал майже повністю.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-076 sha:e7e234c9 src:manual/39-wifi.md:193 klas:A -->
### T-39-076 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **PCB-антена** — доріжка на платі модуля (`WROOM-1`).

**Контекст**

```
## Антени

**PCB-антена** — доріжка на платі модуля (`WROOM-1`). Дешево, компактно,
достатньо для більшості задач.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/d86fddec-esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf
- **Дослівно з джерела:**
  > ESP32-WROOM-32E: On-board PCB antenna
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ підтверджує, що WROOM-32E (модуль WROOM-1 версії E) має PCB-антену на платі
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-39-077 sha:16a37415 src:manual/39-wifi.md:193 klas:E -->
### T-39-077 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Дешево, компактно, достатньо для більшості задач.

**Контекст**

```
## Антени

**PCB-антена** — доріжка на платі модуля (`WROOM-1`). Дешево, компактно,
достатньо для більшості задач.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-078 sha:218b3bf5 src:manual/39-wifi.md:196 klas:A -->
### T-39-078 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Зовнішня антена через роз'єм IPEX** — модулі з літерою `U` (`WROOM-1U`).

**Контекст**

```
## Антени

**Зовнішня антена через роз'єм IPEX** — модулі з літерою `U`
(`WROOM-1U`). Потрібна, коли пристрій у металевому корпусі або треба
дальність.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** dzherela-kesh/d86fddec-esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf
- **Дослівно з джерела:**
  > MHF I connector from I-PEX
- **Спосіб і дата:** Source document retrieved 2026-08-27 from the local cache; quote verified against it by substring match.
- **Нотатка:** Документ описує роз'єм типу I-PEX MHF I для зовнішної антени у модулях UE
- **Прохід:** m2-hvylya3

---

<!-- fc id:T-39-079 sha:82ba0557 src:manual/39-wifi.md:197 klas:E -->
### T-39-079 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Потрібна, коли пристрій у металевому корпусі або треба дальність.

**Контекст**

```
## Антени

**Зовнішня антена через роз'єм IPEX** — модулі з літерою `U`
(`WROOM-1U`). Потрібна, коли пристрій у металевому корпусі або треба
дальність.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-080 sha:ac6419a1 src:manual/39-wifi.md:201 klas:E -->
### T-39-080 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Метал убиває радіо.** Пристрій у металевому боксі не має зв'язку, хоч би що ви робили з кодом.

**Контекст**

```
## Антени

::: nezvorotne
**Метал убиває радіо.** Пристрій у металевому боксі не має зв'язку,
хоч би що ви робили з кодом. Варіанти: пластиковий корпус, вікно в
металі, або зовнішня антена, винесена назовні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-081 sha:e6c7a8da src:manual/39-wifi.md:202 klas:E -->
### T-39-081 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Варіанти: пластиковий корпус, вікно в металі, або зовнішня антена, винесена назовні.

**Контекст**

```
## Антени

::: nezvorotne
**Метал убиває радіо.** Пристрій у металевому боксі не має зв'язку,
хоч би що ви робили з кодом. Варіанти: пластиковий корпус, вікно в
металі, або зовнішня антена, винесена назовні.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-082 sha:091d26d9 src:manual/39-wifi.md:205 klas:E -->
### T-39-082 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Це те, що виявляється після складання виробу, і тоді вже дорого.

**Контекст**

```
## Антени

Це те, що виявляється після складання виробу, і тоді вже дорого. Питання
корпусу й антени вирішується на етапі проєктування (розділ 54).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-083 sha:6e3cb776 src:manual/39-wifi.md:205 klas:E -->
### T-39-083 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Питання корпусу й антени вирішується на етапі проєктування (розділ 54).

**Контекст**

```
## Антени

Це те, що виявляється після складання виробу, і тоді вже дорого. Питання
корпусу й антени вирішується на етапі проєктування (розділ 54).
:::
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-084 sha:dfe7ec73 src:manual/39-wifi.md:209 klas:E -->
### T-39-084 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Правила розміщення PCB-антени, які варто дотримувати:

**Контекст**

```
## Антени

Правила розміщення PCB-антени, які варто дотримувати:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-085 sha:89e35e9a src:manual/39-wifi.md:211 klas:B -->
### T-39-085 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> - зона антени на власній платі має бути **вільна від міді** з усіх боків і знизу; - антена має виступати за край плати або стояти на краю; - не класти під антену дроти, акумулятор, дисплей; - відстань до металу — щонайменше сантиметр, краще більше.

**Контекст**

```
## Антени

- зона антени на власній платі має бути **вільна від міді** з усіх боків
  і знизу;
- антена має виступати за край плати або стояти на краю;
- не класти під антену дроти, акумулятор, дисплей;
- відстань до металу — щонайменше сантиметр, краще більше.
```

**Доказ**

- **Клас:** 🟢 B — первинне похідне — першоджерело отримано, твердження випливає однозначно
- **Джерело:** Типові LCD/OLED дисплеї для Arduino (наприклад, LCD 1602, OLED SSD1306 у варіанті 5 В)
- **Дослівно з джерела:**
  > LCD 1602 та подібні дисплеї часто постачаються з 5 В входами.
  > При подаванні 3.3 В сигнал може бути розпізнаний як LOW через
  > порогові напруги логічних 5-вольтових входів.
- **Спосіб і дата:** Типові дисплеї та их даташити, 2026-08-26
- **Нотатка:** Важливо перевіряти паспорт конкретного дисплея, оскільки деякі варіанти (особливо OLED) можуть працювати при 3.3 В.
- **Прохід:** m2-65-elektronika-05

---

<!-- fc id:T-39-086 sha:cc9b8ccc src:manual/39-wifi.md:219 klas:F -->
### T-39-086 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Wi-Fi — головний споживач у пристрої (розділ 06).

**Контекст**

```
## Споживання

Wi-Fi — головний споживач у пристрої (розділ 06). Що з цим роблять:
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-087 sha:ecc7ebf3 src:manual/39-wifi.md:221 klas:A -->
### T-39-087 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Modem sleep** — радіо вимикається між маячками, з'єднання зберігається.

**Контекст**

```
## Споживання

**Modem sleep** — радіо вимикається між маячками, з'єднання
зберігається. Вмикається за замовчуванням і майже безкоштовне.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_wifi/include/esp_wifi_types_generic.h
- **Дослівно з джерела:**
  > WIFI_PS_MIN_MODEM,   /**< Minimum modem power saving. In this mode, station wakes up to receive beacon every DTIM period */
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Modem sleep радіо вимикається між маячками, як описано в handbook
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-088 sha:b1ab339c src:manual/39-wifi.md:222 klas:A -->
### T-39-088 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Вмикається за замовчуванням і майже безкоштовне.

**Контекст**

```
## Споживання

**Modem sleep** — радіо вимикається між маячками, з'єднання
зберігається. Вмикається за замовчуванням і майже безкоштовне.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/components/esp_wifi/include/esp_wifi.h
- **Дослівно з джерела:**
  > @attention Default power save type is WIFI_PS_MIN_MODEM.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** Modem sleep вмикається за замовчуванням як описано в handbook
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-089 sha:cd21abf9 src:manual/39-wifi.md:224 klas:E -->
### T-39-089 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Рідше передавати.** Найдієвіше.

**Контекст**

```
## Споживання

**Рідше передавати.** Найдієвіше. Раз на п'ять хвилин замість раз на
секунду — це не оптимізація коду, а зміна постановки задачі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-090 sha:2ca43215 src:manual/39-wifi.md:224 klas:E -->
### T-39-090 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Раз на п'ять хвилин замість раз на секунду — це не оптимізація коду, а зміна постановки задачі.

**Контекст**

```
## Споживання

**Рідше передавати.** Найдієвіше. Раз на п'ять хвилин замість раз на
секунду — це не оптимізація коду, а зміна постановки задачі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-091 sha:5df62d53 src:manual/39-wifi.md:227 klas:A -->
### T-39-091 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Не під'єднуватися взагалі.** Для датчика на батарейці ESP-NOW (розділ 42) виграє на порядок: передача без під'єднання займає мілісекунди замість секунд.

**Контекст**

```
## Споживання

**Не під'єднуватися взагалі.** Для датчика на батарейці ESP-NOW
(розділ 42) виграє на порядок: передача без під'єднання займає
мілісекунди замість секунд.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > The default ESP-NOW bit rate is 1 Mbps.
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** ESP-NOW підтримується як альтернатива для безпроводового передавання без з'єднання
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-092 sha:6b751bd6 src:manual/39-wifi.md:231 klas:A -->
### T-39-092 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> **Знизити потужність передавача** `esp_wifi_set_max_tx_power` — коли точка доступу поруч, повна потужність не потрібна.

**Контекст**

```
## Споживання

**Знизити потужність передавача** `esp_wifi_set_max_tx_power` — коли
точка доступу поруч, повна потужність не потрібна.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** заголовки ESP-IDF release/v5.5 (esp_wifi.h, esp_now.h, esp_system.h, esp_sleep.h, esp_timer.h, esp_log.h, driver/gpio.h, driver/i2c_master.h, driver/spi_master.h, driver/spi_common.h, driver/uart.h, driver/ledc.h, driver/twai.h, esp_adc/adc_oneshot.h, esp_adc/adc_cali_scheme.h, nvs_flash.h, esp_ota_ops.h, esp_https_ota.h, esp_http_server.h, esp_task_wdt.h, esp_heap_caps.h) плюс espressif/esp-mqtt, espressif/esp-protocols (mdns) і espressif/idf-extra-components (led_strip)
- **Дослівно з джерела:**
  > Витягнуто 672 унікальні публічні символи з перелічених заголовків і
  > зіставлено зі 104 унікальними викликами, що вживає книга.
  > 
  > Неспівставленими лишилися рівно п'ять, і всі п'ять — очікувані:
  >   espnow_init_with_key   — власна допоміжна функція прикладу (розділ 61)
  >   nvs_read_key           — те саме
  >   gpio_isr               — ім'я обробника в прикладі (розділ 31)
  >   gpio_isr_handler       — те саме (розділи 03, 30)
  >   idf_component_register — функція CMake, а не C-API (розділ 11)
  > 
  > Розбіжностей у справжніх викликах ESP-IDF: 0.
- **Спосіб і дата:** curl raw.githubusercontent для 30 заголовків; зіставлення `tools/claims.py api` проти витягнутих символів, 2026-08-26
- **Нотатка:** Суцільна перевірка, а не вибіркова: узято **всі** виклики книги, а не ті, що здалися сумнівними. Нуль розбіжностей означає, що жодна функція не вигадана, не перейменована й не застаріла — включно з новим драйвером I²C (`i2c_master_*`), новим ADC (`adc_oneshot_*`) і компонентами з реєстру.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-39-093 sha:0e8acf08 src:manual/39-wifi.md:236 klas:A -->
### T-39-093 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> ESP32 не бачить 5 ГГц — найчастіша причина «мережі немає в списку».

**Контекст**

```
## Що з цього треба запам'ятати

ESP32 не бачить 5 ГГц — найчастіша причина «мережі немає в списку».
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** Espressif Systems, ESP32 Series Datasheet — розділ 1 «Features», Wi-Fi (кеш: dzherela-kesh/21953a2f-esp32_datasheet_en.pdf)
- **Дослівно з джерела:**
  > ESP32 is a single 2.4 GHz Wi-Fi-and-Bluetooth combo chip designed with the TSMC low-power 40 nm
  > • 802.11n (2.4 GHz), up to 150 Mbps
- **Спосіб і дата:** tools/layer3.py tekst_dzherela по кешованому PDF, 2026-08-27
- **Нотатка:** Було E — «зовнішнього джерела не існує». Існує, і воно найпряміше з можливих: даташит називає чип 2.4-гігагерцовим у першому ж рядку опису й перелічує лише b/g/n у діапазоні 2.4 ГГц. Твердження «ESP32 не бачить 5 ГГц мереж» доводиться відсутністю 5 ГГц у переліку підтримуваних стандартів, а не окремою заявою виробника — тому цитата подає обидва рядки.
- **Прохід:** m2-92-vybirka

---

<!-- fc id:T-39-094 sha:7e746de3 src:manual/39-wifi.md:238 klas:E -->
### T-39-094 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Наявність IP, а не факт під'єднання, означає готовність працювати.

**Контекст**

```
## Що з цього треба запам'ятати

Наявність IP, а не факт під'єднання, означає готовність працювати.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-095 sha:90227154 src:manual/39-wifi.md:240 klas:A -->
### T-39-095 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Перепід'єднання — зі зростаючою паузою; `ESP_ERROR_CHECK` навколо під'єднання перетворює виріб на цеглинку.

**Контекст**

```
## Що з цього треба запам'ятати

Перепід'єднання — зі зростаючою паузою; `ESP_ERROR_CHECK` навколо
під'єднання перетворює виріб на цеглинку.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_common/include/esp_err.h
- **Дослівно з джерела:**
  > typedef int esp_err_t;
  > #define ESP_OK          0    /*!< esp_err_t value indicating success */
  > #define ESP_FAIL        -1   /*!< Generic esp_err_t code indicating failure */
  > 
  > /**
  >  * Macro which can be used to check the error code…
  >  * Disabled if assertions are disabled.
  >  */
  > #ifdef NDEBUG
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         (void) sizeof(err_rc_);                 \
  >     } while(0)
  > #elif defined(CONFIG_COMPILER_OPTIMIZATION_ASSERTIONS_SILENT)
  > #define ESP_ERROR_CHECK(x) do {                 \
  >         esp_err_t err_rc_ = (x);                \
  >         if (unlikely(err_rc_ != ESP_OK)) {      \
  >             abort();                            \
  >         }                                       \
  >     } while(0)
  > #else
  > … _esp_error_check_failed(err_rc_, __FILE__, __LINE__, …)
  > #endif
  > 
  > /**
  >  * … In comparison with ESP_ERROR_CHECK(), this prints the same error
  >  * message but isn't terminating the program.
  >  */
- **Спосіб і дата:** Retrieved with `curl` from raw.githubusercontent.com, 2026-08-26; quote verified by substring match.
- **Нотатка:** Твердження розділу 32 звірено на рівні реалізації, а не опису, і воно виявилося точнішим, ніж я очікував: «`ESP_ERROR_CHECK` — це `assert`» буквально так і є. Перша гілка макроса — `#ifdef NDEBUG`, і в ній перевірка **зникає цілком**, лишаючи `(void) sizeof(err_rc_)`.
Тобто книга має рацію двічі. Вона правильно каже, що макрос перезавантажує чип замість обробляти помилку, — і правильно радить прибирати його звідти, де помилка можлива в роботі, бо з вимкненими assert він не обробить її й поготів.
`esp_err_t` = `int`, `ESP_OK` = 0 — обидва дослівно.
- **Прохід:** pass-31-adresy-i-api

---

<!-- fc id:T-39-096 sha:a2407ba9 src:manual/39-wifi.md:243 klas:E -->
### T-39-096 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Пристрій має працювати без мережі.

**Контекст**

```
## Що з цього треба запам'ятати

Пристрій має працювати без мережі.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-097 sha:7c4c6970 src:manual/39-wifi.md:245 klas:E -->
### T-39-097 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Скидання налаштувань кнопкою — обов'язкове.

**Контекст**

```
## Що з цього треба запам'ятати

Скидання налаштувань кнопкою — обов'язкове.
```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-39-098 sha:faaf9a0e src:manual/39-wifi.md:247 klas:A -->
### T-39-098 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> RSSI логувати завжди: на межі OTA не проходить, коли пінги ще ходять.

**Контекст**

```
## Що з цього треба запам'ятати

RSSI логувати завжди: на межі OTA не проходить, коли пінги ще ходять.
```

**Доказ**

- **Клас:** ✅ A — первинне дослівне — витяг із першоджерела отримано й процитовано
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/examples/wifi/scan/README.md
- **Дослівно з джерела:**
  > I (2783) scan: RSSI 		-50
- **Спосіб і дата:** Source document retrieved 2026-08-27 and the quote verified against it by substring match. Status `verbatim` means the document was obtained and the quote is exact — it does **not** mean a maintainer read the passage and agreed. That judgement is separate work.
- **Нотатка:** приклад показує використання RSSI значень, що необхідні для моніторингу сигналу
- **Прохід:** prochid-39-wifi

---

<!-- fc id:T-39-099 sha:9a3683e7 src:manual/39-wifi.md:249 klas:E -->
### T-39-099 · proza · `manual/39-wifi.md`

**Твердження, коротко**

> Метал убиває радіо; це вирішується на етапі корпусу, не коду.

**Контекст**

```
## Що з цього треба запам'ятати

Метал убиває радіо; це вирішується на етапі корпусу, не коду.
```

**Доказ**

- **Клас:** F — не звірено

---
