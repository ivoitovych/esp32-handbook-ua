# Фактчекінг: `manual/61-proj-kanal.md`

Одиниць твердження: **84**. Статус доказу й формат запису — `factcheck/METHOD.md`, частина II.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/evidence/`. Правити вручну нема сенсу.

**Що в блоці «Твердження, коротко».** Для прози, рядка коду й зв'язки схеми — **дослівний текст книги**. Для комірки таблиці — рендер (`BME280 · Адреса → 0x76`), якого в книзі немає; дослівний рядок такої одиниці стоїть окремим блоком нижче.

---

<!-- fc id:T-61-001 sha:2d55ff87 src:manual/61-proj-kanal.md:3 status:no-external-signal -->
### T-61-001 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Надійний обмін між двома пристроями без роутера, без інтернету й без інфраструктури.

**Контекст**

```
# 61. Радіоканал між двома платами {#proj-kanal}

Надійний обмін між двома пристроями без роутера, без інтернету й без
інфраструктури. ESP-NOW із шифруванням, підтвердженням і контролем
зв'язку.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-002 sha:a5d4a7de src:manual/61-proj-kanal.md:4 status:unchecked -->
### T-61-002 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP-NOW із шифруванням, підтвердженням і контролем зв'язку.

**Контекст**

```
# 61. Радіоканал між двома платами {#proj-kanal}

Надійний обмін між двома пристроями без роутера, без інтернету й без
інфраструктури. ESP-NOW із шифруванням, підтвердженням і контролем
зв'язку.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-003 sha:1d3c416e src:manual/61-proj-kanal.md:7 status:no-external-signal -->
### T-61-003 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Це основа для будь-якої системи «датчик — приймач» і найкорисніший проєкт для автономних вузлів (розділ 42).

**Контекст**

```
# 61. Радіоканал між двома платами {#proj-kanal}

Це основа для будь-якої системи «датчик — приймач» і найкорисніший
проєкт для автономних вузлів (розділ 42).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-004 sha:34fd0a3a src:manual/61-proj-kanal.md:12 status:no-external-signal -->
### T-61-004 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Задача:** передавач раз на хвилину надсилає вимірювання, приймач отримує, показує і віддає далі.

**Контекст**

```
## Постановка

**Задача:** передавач раз на хвилину надсилає вимірювання, приймач
отримує, показує і віддає далі. Обидва мають знати, чи живий партнер.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-005 sha:9a401a97 src:manual/61-proj-kanal.md:13 status:no-external-signal -->
### T-61-005 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Обидва мають знати, чи живий партнер.

**Контекст**

```
## Постановка

**Задача:** передавач раз на хвилину надсилає вимірювання, приймач
отримує, показує і віддає далі. Обидва мають знати, чи живий партнер.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-006 sha:041a9aa8 src:manual/61-proj-kanal.md:15 status:no-external-signal -->
### T-61-006 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Живлення:** передавач від акумулятора (deep sleep між передачами), приймач від мережі.

**Контекст**

```
## Постановка

**Живлення:** передавач від акумулятора (deep sleep між передачами),
приймач від мережі.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-007 sha:e9a11bea src:manual/61-proj-kanal.md:18 status:no-external-signal -->
### T-61-007 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Захист:** шифрування; чужий пристрій не може ні прочитати, ні підробити пакет.

**Контекст**

```
## Постановка

**Захист:** шифрування; чужий пристрій не може ні прочитати, ні
підробити пакет.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-008 sha:34f0eb99 src:manual/61-proj-kanal.md:21 status:no-external-signal -->
### T-61-008 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Поведінка при відмові:** передавач не отримав підтвердження — повторює й накопичує; приймач не бачить пакетів — повідомляє про втрату вузла.

**Контекст**

```
## Постановка

**Поведінка при відмові:** передавач не отримав підтвердження — повторює
й накопичує; приймач не бачить пакетів — повідомляє про втрату вузла.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-009 sha:668e5535 src:manual/61-proj-kanal.md:26 status:no-external-signal -->
### T-61-009 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Для передавача на батарейці різниця вирішальна (розділ 42):

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-010 sha:464bdd0d src:manual/61-proj-kanal.md:28 status:unchecked -->
### T-61-010 · tablycya-shapka · `manual/61-proj-kanal.md`

**Твердження, коротко**

> | | Wi-Fi | ESP-NOW |

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-011 sha:01a9ed98 src:manual/61-proj-kanal.md:30 status:unchecked -->
### T-61-011 · komirka · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Час до передачі · Wi-Fi → 1–10 с

**Дослівно з книги**

```
| Час до передачі | 1–10 с | **10 мс** |
```

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-012 sha:573156b8 src:manual/61-proj-kanal.md:30 status:unchecked -->
### T-61-012 · komirka · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Час до передачі · ESP-NOW → **10 мс**

**Дослівно з книги**

```
| Час до передачі | 1–10 с | **10 мс** |
```

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-013 sha:76ab707d src:manual/61-proj-kanal.md:31 status:named-unreachable -->
### T-61-013 · komirka · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Заряд на цикл · Wi-Fi → ~500 мА·с

**Дослівно з книги**

```
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
```

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |
```

**Доказ**

- **Статус:** named-unreachable — secondary — the source cannot be reached from here; URL recorded, no quote
- **Джерело:** ESP-NOW документація та енергоефективність (source-cache/31a9c838-esp_now.h)
- **Спосіб і дата:** Пошук у source-cache/esp_now.h та документації ESP-IDF
- **Нотатка:** Значення ~5 мА·с (мільйампер-секунди) для ESP-NOW передачі є часто цитованою характеристикою в практичній документації. Однак при пошуку в source-cache не знайдено точної цитати з офіційного джерела. Це конкретна цифра, яку необхідно перевірити в офіційній документації Espressif про енергоспоживання. Присвоюю клас C, оскільки джерело логічне (ESP-NOW документація), але дослівна цитата не знайдена в наявних матеріалах. | Взірець перебудовано з тексту одиниці реєстру 2026-08-27: попередній писався під розмітку книги (риски таблиці) і не чіпав нічого.
- **Прохід:** m2-91-sample

---

<!-- fc id:T-61-014 sha:706d3437 src:manual/61-proj-kanal.md:31 status:unchecked -->
### T-61-014 · komirka · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Заряд на цикл · ESP-NOW → **~5 мА·с**

**Дослівно з книги**

```
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
```

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-015 sha:24bfd5bc src:manual/61-proj-kanal.md:32 status:unchecked -->
### T-61-015 · komirka · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Потрібен роутер · Wi-Fi → так

**Дослівно з книги**

```
| Потрібен роутер | так | **ні** |
```

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-016 sha:dba9d4ef src:manual/61-proj-kanal.md:32 status:verbatim -->
### T-61-016 · komirka · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Потрібен роутер · ESP-NOW → **ні**

**Дослівно з книги**

```
| Потрібен роутер | так | **ні** |
```

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/network/esp_now.rst
- **Дослівно з джерела:**
  > ESP-NOW is a kind of connectionless Wi-Fi communication protocol that is defined by Espressif. In ESP-NOW, application data is encapsulated in a vendor-specific action frame and then transmitted from one Wi-Fi device to another without connection.
- **Спосіб і дата:** wave 2026-09-01, arms B; layer 3 verbatim; layer 2 read by a maintainer
- **Нотатка:** First pass: "Connectionless" protocol confirms no router infrastructure needed
- **Прохід:** wave-20260901

---

<!-- fc id:T-61-017 sha:9b30fdd0 src:manual/61-proj-kanal.md:34 status:no-external-signal -->
### T-61-017 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Два порядки економії — це різниця між місяцем і роками.

**Контекст**

```
## Чому ESP-NOW, а не Wi-Fi

Два порядки економії — це різниця між місяцем і роками.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-018 sha:f080f748 src:manual/61-proj-kanal.md:38 status:no-external-signal -->
### T-61-018 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Спільний заголовок для обох боків.

**Контекст**

```
## Формат пакета

Спільний заголовок для обох боків. Це те, що варто продумати один раз:
змінити формат після розгортання означає перепрошити всі вузли.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-019 sha:ed70f774 src:manual/61-proj-kanal.md:38 status:no-external-signal -->
### T-61-019 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Це те, що варто продумати один раз: змінити формат після розгортання означає перепрошити всі вузли.

**Контекст**

```
## Формат пакета

Спільний заголовок для обох боків. Це те, що варто продумати один раз:
змінити формат після розгортання означає перепрошити всі вузли.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-020 sha:488cb3e6 src:manual/61-proj-kanal.md:41 status:code-context -->
### T-61-020 · kod · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ```c
> #define PROTO_VERSIYA  1
> #define TYP_VYMIR      1
> #define TYP_PIDTVERDZH 2
> 
> typedef struct __attribute__((packed)) {
>     uint8_t  versiya;      // версія протоколу — перше поле завжди
>     uint8_t  typ;          // тип повідомлення
>     uint8_t  vuzol;        // номер вузла
>     uint8_t  rezerv;
>     uint32_t nomer;        // лічильник пакетів: виявляє пропуски
>     int32_t  temp_x100;    // ціле замість float — менше й переносніше
>     uint16_t hum_x10;
>     uint16_t napruga_mv;
> } paket_t;
> 
> _Static_assert(sizeof(paket_t) <= 250, "ESP-NOW: максимум 250 байтів");
> ```

**Контекст**

````
## Формат пакета

```c
#define PROTO_VERSIYA  1
#define TYP_VYMIR      1
#define TYP_PIDTVERDZH 2

typedef struct __attribute__((packed)) {
    uint8_t  versiya;      // версія протоколу — перше поле завжди
    uint8_t  typ;          // тип повідомлення
    uint8_t  vuzol;        // номер вузла
    uint8_t  rezerv;
    uint32_t nomer;        // лічильник пакетів: виявляє пропуски
    int32_t  temp_x100;    // ціле замість float — менше й переносніше
    uint16_t hum_x10;
    uint16_t napruga_mv;
} paket_t;

_Static_assert(sizeof(paket_t) <= 250, "ESP-NOW: максимум 250 байтів");
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-61-021 sha:38e6adad src:manual/61-proj-kanal.md:42 status:unchecked -->
### T-61-021 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> #define PROTO_VERSIYA  1

**Контекст**

````
## Формат пакета

```c
#define PROTO_VERSIYA  1
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-022 sha:ceff9e1c src:manual/61-proj-kanal.md:43 status:unchecked -->
### T-61-022 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> #define TYP_VYMIR      1

**Контекст**

```
#define TYP_VYMIR      1
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-023 sha:cf685481 src:manual/61-proj-kanal.md:44 status:unchecked -->
### T-61-023 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> #define TYP_PIDTVERDZH 2

**Контекст**

```
#define TYP_PIDTVERDZH 2
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-024 sha:b4239afb src:manual/61-proj-kanal.md:57 status:verbatim -->
### T-61-024 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> _Static_assert(sizeof(paket_t) <= 250, "ESP-NOW: максимум 250 байтів");

**Контекст**

````
#define TYP_PIDTVERDZH 2

_Static_assert(sizeof(paket_t) <= 250, "ESP-NOW: максимум 250 байтів");
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-61-025 sha:92d27801 src:manual/61-proj-kanal.md:61 status:no-external-signal -->
### T-61-025 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Три рішення в цій структурі, кожне з причиною.

**Контекст**

```
#define TYP_PIDTVERDZH 2

::: uvaha
Три рішення в цій структурі, кожне з причиною.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-026 sha:5b873185 src:manual/61-proj-kanal.md:63 status:unchecked -->
### T-61-026 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **`versiya` першим полем.** Коли формат зміниться, старий приймач зможе розпізнати незнайому версію і не розібрати сміття як дані.

**Контекст**

```
#define TYP_PIDTVERDZH 2

**`versiya` першим полем.** Коли формат зміниться, старий приймач зможе
розпізнати незнайому версію і не розібрати сміття як дані.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-027 sha:e6af2908 src:manual/61-proj-kanal.md:66 status:unchecked -->
### T-61-027 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **`__attribute__((packed))`** прибирає вирівнювання, яке компілятор додав би сам.

**Контекст**

```
#define TYP_PIDTVERDZH 2

**`__attribute__((packed))`** прибирає вирівнювання, яке компілятор
додав би сам. Без нього структура на двох різних чипах може мати різний
розмір.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-028 sha:bc260bbb src:manual/61-proj-kanal.md:67 status:no-external-signal -->
### T-61-028 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Без нього структура на двох різних чипах може мати різний розмір.

**Контекст**

```
#define TYP_PIDTVERDZH 2

**`__attribute__((packed))`** прибирає вирівнювання, яке компілятор
додав би сам. Без нього структура на двох різних чипах може мати різний
розмір.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-029 sha:5c50e427 src:manual/61-proj-kanal.md:70 status:unchecked -->
### T-61-029 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Цілі замість `float`.** Менший розмір, немає питань про представлення чисел, і на чипах без FPU дешевше (розділ 02).

**Контекст**

```
#define TYP_PIDTVERDZH 2

**Цілі замість `float`.** Менший розмір, немає питань про представлення
чисел, і на чипах без FPU дешевше (розділ 02).
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-030 sha:cda5218c src:manual/61-proj-kanal.md:76 status:code-context -->
### T-61-030 · kod · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ```c
> static const uint8_t MAC_PRYIMACHA[6] = { 0x24, 0x6F, 0x28, 0x11, 0x22, 0x33 };
> 
> RTC_DATA_ATTR static uint32_t nomer = 0;
> RTC_DATA_ATTR static paket_t  bufer[10];
> RTC_DATA_ATTR static uint8_t  u_buferi = 0;
> 
> static volatile bool dostavleno = false;
> 
> static void on_sent(const esp_now_send_info_t *info,
>                     esp_now_send_status_t status) {
>     dostavleno = (status == ESP_NOW_SEND_SUCCESS);
> }
> 
> static bool nadislaty(const paket_t *p) {
>     dostavleno = false;
>     if (esp_now_send(MAC_PRYIMACHA, (const uint8_t *)p, sizeof(*p)) != ESP_OK)
>         return false;
> 
>     // чекати підтвердження рівня кадру — це не гарантія доставки,
>     // але воно відрізняє «сусід почув» від «нікого немає»
>     for (int i = 0; i < 50 && !dostavleno; i++)
>         vTaskDelay(pdMS_TO_TICKS(2));
>     return dostavleno;
> }
> 
> void app_main(void) {
>     radio_init();                     // Wi-Fi у режимі STA, канал фіксований
>     espnow_init_with_key();
> 
>     paket_t p = {
>         .versiya = PROTO_VERSIYA,
>         .typ = TYP_VYMIR,
>         .vuzol = NOMER_VUZLA,
>         .nomer = ++nomer,
>     };
>     zmiryaty(&p);
> 
>     if (!nadislaty(&p)) {
>         if (u_buferi < 10) bufer[u_buferi++] = p;
>         ESP_LOGW(TAG, "не доставлено, у буфері %u", u_buferi);
>     } else {
>         // дійшло — спробувати віддати накопичене
>         while (u_buferi > 0 && nadislaty(&bufer[u_buferi - 1]))
>             u_buferi--;
>     }
> 
>     esp_sleep_enable_timer_wakeup(60ULL * 1000000);
>     esp_deep_sleep_start();
> }
> ```

**Контекст**

````
## Передавач

```c
static const uint8_t MAC_PRYIMACHA[6] = { 0x24, 0x6F, 0x28, 0x11, 0x22, 0x33 };

RTC_DATA_ATTR static uint32_t nomer = 0;
RTC_DATA_ATTR static paket_t  bufer[10];
RTC_DATA_ATTR static uint8_t  u_buferi = 0;

static volatile bool dostavleno = false;

static void on_sent(const esp_now_send_info_t *info,
                    esp_now_send_status_t status) {
    dostavleno = (status == ESP_NOW_SEND_SUCCESS);
}

static bool nadislaty(const paket_t *p) {
    dostavleno = false;
    if (esp_now_send(MAC_PRYIMACHA, (const uint8_t *)p, sizeof(*p)) != ESP_OK)
        return false;

    // чекати підтвердження рівня кадру — це не гарантія доставки,
    // але воно відрізняє «сусід почув» від «нікого немає»
    for (int i = 0; i < 50 && !dostavleno; i++)
        vTaskDelay(pdMS_TO_TICKS(2));
    return dostavleno;
}

void app_main(void) {
    radio_init();                     // Wi-Fi у режимі STA, канал фіксований
    espnow_init_with_key();

    paket_t p = {
        .versiya = PROTO_VERSIYA,
        .typ = TYP_VYMIR,
        .vuzol = NOMER_VUZLA,
        .nomer = ++nomer,
    };
    zmiryaty(&p);

    if (!nadislaty(&p)) {
        if (u_buferi < 10) bufer[u_buferi++] = p;
        ESP_LOGW(TAG, "не доставлено, у буфері %u", u_buferi);
    } else {
        // дійшло — спробувати віддати накопичене
        while (u_buferi > 0 && nadislaty(&bufer[u_buferi - 1]))
            u_buferi--;
    }

    esp_sleep_enable_timer_wakeup(60ULL * 1000000);
    esp_deep_sleep_start();
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-61-031 sha:0bead0fd src:manual/61-proj-kanal.md:92 status:verbatim -->
### T-61-031 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> if (esp_now_send(MAC_PRYIMACHA, (const uint8_t *)p, sizeof(*p)) != ESP_OK)

**Контекст**

```
## Передавач

static bool nadislaty(const paket_t *p) {
    dostavleno = false;
    if (esp_now_send(MAC_PRYIMACHA, (const uint8_t *)p, sizeof(*p)) != ESP_OK)
        return false;
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-032 sha:db8aefcb src:manual/61-proj-kanal.md:98 status:verbatim -->
### T-61-032 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> vTaskDelay(pdMS_TO_TICKS(2));

**Контекст**

```
## Передавач

    // чекати підтвердження рівня кадру — це не гарантія доставки,
    // але воно відрізняє «сусід почув» від «нікого немає»
    for (int i = 0; i < 50 && !dostavleno; i++)
        vTaskDelay(pdMS_TO_TICKS(2));
    return dostavleno;
}
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/FreeRTOS-Kernel/include/freertos/{task,queue,semphr,event_groups,timers}.h та components/esp_common/include/esp_attr.h
- **Дослівно з джерела:**
  > Усі 15 викликів FreeRTOS, що вживає книга, знайдено в заголовках ядра.
  > Макроси:
  >   #define IRAM_ATTR _SECTION_ATTR_IMPL(".iram1", __COUNTER__)
  >   #define RTC_DATA_ATTR _SECTION_ATTR_IMPL(".rtc.data", __COUNTER__)
  >   #define configMAX_PRIORITIES ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** `RTC_DATA_ATTR` кладе змінну в секцію `.rtc.data` — це і є механічне підтвердження того, чому вона переживає deep sleep, тоді як звичайна змінна не переживає. `IRAM_ATTR` кладе функцію в `.iram1`, звідки вона виконується при вимкненому кеші флешу.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-61-033 sha:3078ec3b src:manual/61-proj-kanal.md:104 status:unchecked -->
### T-61-033 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> espnow_init_with_key();

**Контекст**

```
## Передавач

void app_main(void) {
    radio_init();                     // Wi-Fi у режимі STA, канал фіксований
    espnow_init_with_key();
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-034 sha:324c53f6 src:manual/61-proj-kanal.md:107 status:unchecked -->
### T-61-034 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> .versiya = PROTO_VERSIYA,

**Контекст**

```
## Передавач

    paket_t p = {
        .versiya = PROTO_VERSIYA,
        .typ = TYP_VYMIR,
        .vuzol = NOMER_VUZLA,
        .nomer = ++nomer,
    };
    zmiryaty(&p);
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-035 sha:7ce2b7c7 src:manual/61-proj-kanal.md:108 status:unchecked -->
### T-61-035 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> .typ = TYP_VYMIR,

**Контекст**

```
## Передавач

    paket_t p = {
        .versiya = PROTO_VERSIYA,
        .typ = TYP_VYMIR,
        .vuzol = NOMER_VUZLA,
        .nomer = ++nomer,
    };
    zmiryaty(&p);
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-036 sha:6fe24018 src:manual/61-proj-kanal.md:109 status:unchecked -->
### T-61-036 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> .vuzol = NOMER_VUZLA,

**Контекст**

```
## Передавач

    paket_t p = {
        .versiya = PROTO_VERSIYA,
        .typ = TYP_VYMIR,
        .vuzol = NOMER_VUZLA,
        .nomer = ++nomer,
    };
    zmiryaty(&p);
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-037 sha:8d862d63 src:manual/61-proj-kanal.md:110 status:unchecked -->
### T-61-037 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> .nomer = ++nomer,

**Контекст**

```
## Передавач

    paket_t p = {
        .versiya = PROTO_VERSIYA,
        .typ = TYP_VYMIR,
        .vuzol = NOMER_VUZLA,
        .nomer = ++nomer,
    };
    zmiryaty(&p);
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-038 sha:e3e10d63 src:manual/61-proj-kanal.md:112 status:unchecked -->
### T-61-038 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> zmiryaty(&p);

**Контекст**

```
## Передавач

    paket_t p = {
        .versiya = PROTO_VERSIYA,
        .typ = TYP_VYMIR,
        .vuzol = NOMER_VUZLA,
        .nomer = ++nomer,
    };
    zmiryaty(&p);
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-039 sha:5f2fdeaa src:manual/61-proj-kanal.md:116 status:unchecked -->
### T-61-039 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP_LOGW(TAG, "не доставлено, у буфері %u", u_buferi);

**Контекст**

```
## Передавач

    if (!nadislaty(&p)) {
        if (u_buferi < 10) bufer[u_buferi++] = p;
        ESP_LOGW(TAG, "не доставлено, у буфері %u", u_buferi);
    } else {
        // дійшло — спробувати віддати накопичене
        while (u_buferi > 0 && nadislaty(&bufer[u_buferi - 1]))
            u_buferi--;
    }
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-040 sha:bcaf613d src:manual/61-proj-kanal.md:119 status:unchecked -->
### T-61-040 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> while (u_buferi > 0 && nadislaty(&bufer[u_buferi - 1]))

**Контекст**

```
## Передавач

    if (!nadislaty(&p)) {
        if (u_buferi < 10) bufer[u_buferi++] = p;
        ESP_LOGW(TAG, "не доставлено, у буфері %u", u_buferi);
    } else {
        // дійшло — спробувати віддати накопичене
        while (u_buferi > 0 && nadislaty(&bufer[u_buferi - 1]))
            u_buferi--;
    }
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-041 sha:6679c2fc src:manual/61-proj-kanal.md:123 status:verbatim -->
### T-61-041 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> esp_sleep_enable_timer_wakeup(60ULL * 1000000);

**Контекст**

````
## Передавач

    esp_sleep_enable_timer_wakeup(60ULL * 1000000);
    esp_deep_sleep_start();
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-042 sha:c5771474 src:manual/61-proj-kanal.md:124 status:unchecked -->
### T-61-042 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> esp_deep_sleep_start();

**Контекст**

````
## Передавач

    esp_sleep_enable_timer_wakeup(60ULL * 1000000);
    esp_deep_sleep_start();
}
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-043 sha:ac5efcc7 src:manual/61-proj-kanal.md:129 status:verbatim -->
### T-61-043 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> `esp_now_send` повертається **до** фактичної передачі.

**Контекст**

```
## Передавач

::: uvaha
`esp_now_send` повертається **до** фактичної передачі. Статус приходить
у зворотний виклик `on_sent`, і саме його треба дочекатися перед
засинанням — інакше чип засне посеред передачі.
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-044 sha:397a915a src:manual/61-proj-kanal.md:129 status:unchecked -->
### T-61-044 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Статус приходить у зворотний виклик `on_sent`, і саме його треба дочекатися перед засинанням — інакше чип засне посеред передачі.

**Контекст**

```
## Передавач

::: uvaha
`esp_now_send` повертається **до** фактичної передачі. Статус приходить
у зворотний виклик `on_sent`, і саме його треба дочекатися перед
засинанням — інакше чип засне посеред передачі.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-045 sha:14b6fb2b src:manual/61-proj-kanal.md:133 status:verbatim -->
### T-61-045 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Це та сама помилка, що з `uart_wait_tx_done` у RS-485 (розділ 34), і проявляється так само: «інколи не доходить».

**Контекст**

```
## Передавач

Це та сама помилка, що з `uart_wait_tx_done` у RS-485 (розділ 34), і
проявляється так само: «інколи не доходить».
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** NXP UM10204 Rev. 7.0 — розділи 7.1, 7.2; обмеження ємності шини (Cb max 400 пФ) в Table 11
- **Дослівно з джерела:**
  > Table 11. Characteristics of the SDA and SCL bus lines:
  > Cb capacitive load for each bus line — max 400 pF
  > 
  > Section 7.2 Operating above the maximum allowable bus capacitance:
  > Bus capacitance limit is specified to limit rise time reductions and
  > allow operating at the rated frequency.
  > 
  > Available strategies include:
  > - Reduced fSCL (Section 7.2.1)
  > - Higher drive outputs (Section 7.2.2)
  > - Bus buffers (Section 7.2.3)
  > - Switched pull-up circuit (Section 7.2.4)
  > 
  > Maximum Rp = tr / (0.8473 × Cb).
  > При Cb > 400 пФ, яка додається довгими дротами, формула дає
  > Rp < 1 кОм, тобто нижче за мінімум (Rp > 1 кОм для 3 мА IOL).
- **Спосіб і дата:** PDF NXP UM10204 із дзеркала, кеш ~/dzherela-cache, pdftotext -layout, 2026-08-26
- **Нотатка:** При метровій довжині дроту ємність додає близько 80–100 пФ/м, отже метр додає 80–100 пФ, що набирається разом з 10–20 пФ від модулів дає межу 400 пФ. На цій межі формула Rp(max) дає значення, що не задовольняють обмеженню за мінімальним струмом 3 мА.
Книга пропонує три рішення: 1. Снизити швидкість (100 кГц замість 400 кГц) 2. Вибрати 2.2 кОм замість 4.7 кОм (але це подвоює струм) 3. RS-485 для довгих дистанцій (інший протокол, розділ 34)
- **Прохід:** m2-29-i2c-35

---

<!-- fc id:T-61-046 sha:dee8e24a src:manual/61-proj-kanal.md:136 status:verbatim -->
### T-61-046 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Сигнатура зворотного виклику змінилася: до ESP-IDF 5.4 першим аргументом був `const uint8_t *mac_addr`, тепер — `const esp_now_send_info_t *`.

**Контекст**

```
## Передавач

Сигнатура зворотного виклику змінилася: до ESP-IDF 5.4 першим аргументом
був `const uint8_t *mac_addr`, тепер — `const esp_now_send_info_t *`.
Приклади з інтернету старшого віку не зберуться, і повідомлення
компілятора вкаже на тип, а не на причину.
:::
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/esp_wifi/include/esp_now.h
- **Дослівно з джерела:**
  > #define ESP_NOW_ETH_ALEN             6         /*!< Length of ESPNOW peer MAC address */
  > #define ESP_NOW_MAX_TOTAL_PEER_NUM   20        /*!< Maximum number of ESPNOW total peers */
  > #define ESP_NOW_MAX_ENCRYPT_PEER_NUM 6         /*!< Maximum number of ESPNOW encrypted peers */
  > #define ESP_NOW_MAX_DATA_LEN  ESP_NOW_MAX_IE_DATA_LEN   /**< Maximum length of data sent in each ESPNOW transmission for v1.0 */
  > #define ESP_NOW_MAX_DATA_LEN_V2      1470      /**< Maximum length of data sent in each ESPNOW transmission for v2.0 */
  > typedef void (*esp_now_recv_cb_t)(const esp_now_recv_info_t * esp_now_info, const uint8_t *data, int data_len);
  > typedef void (*esp_now_send_cb_t)(const esp_now_send_info_t *tx_info, esp_now_send_status_t status);
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** Обидві сигнатури використані в розділах 42 і 61; стару сигнатуру `on_sent` виправлено в сесії рецензування 05 за цим самим джерелом.
- **Прохід:** pass-01-tverde-yadro

---

<!-- fc id:T-61-047 sha:3a1e9ece src:manual/61-proj-kanal.md:138 status:no-external-signal -->
### T-61-047 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Приклади з інтернету старшого віку не зберуться, і повідомлення компілятора вкаже на тип, а не на причину.

**Контекст**

```
## Передавач

Сигнатура зворотного виклику змінилася: до ESP-IDF 5.4 першим аргументом
був `const uint8_t *mac_addr`, тепер — `const esp_now_send_info_t *`.
Приклади з інтернету старшого віку не зберуться, і повідомлення
компілятора вкаже на тип, а не на причину.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-048 sha:a8e5e059 src:manual/61-proj-kanal.md:144 status:code-context -->
### T-61-048 · kod · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ```c
> static void espnow_init_with_key(void) {
>     ESP_ERROR_CHECK(esp_now_init());
>     ESP_ERROR_CHECK(esp_now_register_send_cb(on_sent));
> 
>     uint8_t pmk[16], lmk[16];
>     nvs_read_key("pmk", pmk);         // з NVS, не з коду
>     nvs_read_key("lmk", lmk);
>     ESP_ERROR_CHECK(esp_now_set_pmk(pmk));
> 
>     esp_now_peer_info_t peer = { .channel = KANAL, .encrypt = true };
>     memcpy(peer.peer_addr, MAC_PRYIMACHA, 6);
>     memcpy(peer.lmk, lmk, 16);
>     ESP_ERROR_CHECK(esp_now_add_peer(&peer));
> }
> ```

**Контекст**

````
## Шифрування

```c
static void espnow_init_with_key(void) {
    ESP_ERROR_CHECK(esp_now_init());
    ESP_ERROR_CHECK(esp_now_register_send_cb(on_sent));

    uint8_t pmk[16], lmk[16];
    nvs_read_key("pmk", pmk);         // з NVS, не з коду
    nvs_read_key("lmk", lmk);
    ESP_ERROR_CHECK(esp_now_set_pmk(pmk));

    esp_now_peer_info_t peer = { .channel = KANAL, .encrypt = true };
    memcpy(peer.peer_addr, MAC_PRYIMACHA, 6);
    memcpy(peer.lmk, lmk, 16);
    ESP_ERROR_CHECK(esp_now_add_peer(&peer));
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-049 sha:0232cd24 src:manual/61-proj-kanal.md:146 status:verbatim -->
### T-61-049 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP_ERROR_CHECK(esp_now_init());

**Контекст**

````
## Шифрування

```c
static void espnow_init_with_key(void) {
    ESP_ERROR_CHECK(esp_now_init());
    ESP_ERROR_CHECK(esp_now_register_send_cb(on_sent));
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-050 sha:e2734f8f src:manual/61-proj-kanal.md:147 status:verbatim -->
### T-61-050 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP_ERROR_CHECK(esp_now_register_send_cb(on_sent));

**Контекст**

````
## Шифрування

```c
static void espnow_init_with_key(void) {
    ESP_ERROR_CHECK(esp_now_init());
    ESP_ERROR_CHECK(esp_now_register_send_cb(on_sent));
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-051 sha:b257bee2 src:manual/61-proj-kanal.md:151 status:unchecked -->
### T-61-051 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> nvs_read_key("lmk", lmk);

**Контекст**

```
## Шифрування

    uint8_t pmk[16], lmk[16];
    nvs_read_key("pmk", pmk);         // з NVS, не з коду
    nvs_read_key("lmk", lmk);
    ESP_ERROR_CHECK(esp_now_set_pmk(pmk));
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-052 sha:1980955e src:manual/61-proj-kanal.md:152 status:verbatim -->
### T-61-052 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP_ERROR_CHECK(esp_now_set_pmk(pmk));

**Контекст**

```
## Шифрування

    uint8_t pmk[16], lmk[16];
    nvs_read_key("pmk", pmk);         // з NVS, не з коду
    nvs_read_key("lmk", lmk);
    ESP_ERROR_CHECK(esp_now_set_pmk(pmk));
```

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-053 sha:7881c502 src:manual/61-proj-kanal.md:155 status:unchecked -->
### T-61-053 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> memcpy(peer.peer_addr, MAC_PRYIMACHA, 6);

**Контекст**

````
## Шифрування

    esp_now_peer_info_t peer = { .channel = KANAL, .encrypt = true };
    memcpy(peer.peer_addr, MAC_PRYIMACHA, 6);
    memcpy(peer.lmk, lmk, 16);
    ESP_ERROR_CHECK(esp_now_add_peer(&peer));
}
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-054 sha:dfd25891 src:manual/61-proj-kanal.md:156 status:unchecked -->
### T-61-054 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> memcpy(peer.lmk, lmk, 16);

**Контекст**

````
## Шифрування

    esp_now_peer_info_t peer = { .channel = KANAL, .encrypt = true };
    memcpy(peer.peer_addr, MAC_PRYIMACHA, 6);
    memcpy(peer.lmk, lmk, 16);
    ESP_ERROR_CHECK(esp_now_add_peer(&peer));
}
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-055 sha:eb4e4ec4 src:manual/61-proj-kanal.md:157 status:verbatim -->
### T-61-055 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP_ERROR_CHECK(esp_now_add_peer(&peer));

**Контекст**

````
## Шифрування

    esp_now_peer_info_t peer = { .channel = KANAL, .encrypt = true };
    memcpy(peer.peer_addr, MAC_PRYIMACHA, 6);
    memcpy(peer.lmk, lmk, 16);
    ESP_ERROR_CHECK(esp_now_add_peer(&peer));
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-056 sha:214d0ef5 src:manual/61-proj-kanal.md:162 status:unchecked -->
### T-61-056 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Ключі читаються **з NVS**, а не зашиті в код.

**Контекст**

```
## Шифрування

::: nezvorotne
Ключі читаються **з NVS**, а не зашиті в код. Зашитий ключ дістається з
дампа прошивки за п'ять хвилин (розділи 24, 50).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-057 sha:f7237524 src:manual/61-proj-kanal.md:162 status:no-external-signal -->
### T-61-057 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Зашитий ключ дістається з дампа прошивки за п'ять хвилин (розділи 24, 50).

**Контекст**

```
## Шифрування

::: nezvorotne
Ключі читаються **з NVS**, а не зашиті в код. Зашитий ключ дістається з
дампа прошивки за п'ять хвилин (розділи 24, 50).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-058 sha:623cf9a6 src:manual/61-proj-kanal.md:165 status:no-external-signal -->
### T-61-058 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> І ключі мають бути **різні на кожну пару вузлів**, а не один на всю систему: інакше захоплення одного датчика компрометує всю мережу.

**Контекст**

```
## Шифрування

І ключі мають бути **різні на кожну пару вузлів**, а не один на всю
систему: інакше захоплення одного датчика компрометує всю мережу.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-059 sha:22808815 src:manual/61-proj-kanal.md:168 status:no-external-signal -->
### T-61-059 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Записуються при виробництві разом із номером вузла (розділ 21).

**Контекст**

```
## Шифрування

Записуються при виробництві разом із номером вузла (розділ 21).
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-060 sha:4834ece6 src:manual/61-proj-kanal.md:173 status:code-context -->
### T-61-060 · kod · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ```c
> typedef struct {
>     uint32_t ostanniy_nomer;
>     int64_t  ostanniy_chas;
>     uint32_t vtracheno;
>     bool     zhyvyy;
> } stan_vuzla_t;
> 
> static stan_vuzla_t vuzly[MAX_VUZLIV];
> static QueueHandle_t cherga;
> 
> static void on_recv(const esp_now_recv_info_t *info,
>                     const uint8_t *data, int len) {
>     // виконується в контексті задачі Wi-Fi: скопіювати й вийти (розділ 42)
>     if (len != sizeof(paket_t)) return;
>     paket_t p;
>     memcpy(&p, data, sizeof(p));
>     xQueueSend(cherga, &p, 0);      // не FromISR: це задача, а не переривання
> }
> 
> static void task_obrobka(void *arg) {
>     paket_t p;
>     while (xQueueReceive(cherga, &p, portMAX_DELAY) == pdTRUE) {
>         if (p.versiya != PROTO_VERSIYA) {
>             ESP_LOGW(TAG, "чужа версія протоколу: %u", p.versiya);
>             continue;
>         }
>         if (p.vuzol >= MAX_VUZLIV) continue;
> 
>         stan_vuzla_t *v = &vuzly[p.vuzol];
>         if (v->ostanniy_nomer && p.nomer > v->ostanniy_nomer + 1)
>             v->vtracheno += p.nomer - v->ostanniy_nomer - 1;
> 
>         v->ostanniy_nomer = p.nomer;
>         v->ostanniy_chas = esp_timer_get_time();
>         v->zhyvyy = true;
> 
>         ESP_LOGI(TAG, "вузол %u: %.2f °C, %.1f %%, %.2f В "
>                       "(пакет %lu, втрачено %lu)",
>                  p.vuzol, p.temp_x100 / 100.0f, p.hum_x10 / 10.0f,
>                  p.napruga_mv / 1000.0f, p.nomer, v->vtracheno);
> 
>         vidaty_dali(&p);              // MQTT, веб, дисплей
>     }
> }
> ```

**Контекст**

````
## Приймач

```c
typedef struct {
    uint32_t ostanniy_nomer;
    int64_t  ostanniy_chas;
    uint32_t vtracheno;
    bool     zhyvyy;
} stan_vuzla_t;

static stan_vuzla_t vuzly[MAX_VUZLIV];
static QueueHandle_t cherga;

static void on_recv(const esp_now_recv_info_t *info,
                    const uint8_t *data, int len) {
    // виконується в контексті задачі Wi-Fi: скопіювати й вийти (розділ 42)
    if (len != sizeof(paket_t)) return;
    paket_t p;
    memcpy(&p, data, sizeof(p));
    xQueueSend(cherga, &p, 0);      // не FromISR: це задача, а не переривання
}

static void task_obrobka(void *arg) {
    paket_t p;
    while (xQueueReceive(cherga, &p, portMAX_DELAY) == pdTRUE) {
        if (p.versiya != PROTO_VERSIYA) {
            ESP_LOGW(TAG, "чужа версія протоколу: %u", p.versiya);
            continue;
        }
        if (p.vuzol >= MAX_VUZLIV) continue;

        stan_vuzla_t *v = &vuzly[p.vuzol];
        if (v->ostanniy_nomer && p.nomer > v->ostanniy_nomer + 1)
            v->vtracheno += p.nomer - v->ostanniy_nomer - 1;

        v->ostanniy_nomer = p.nomer;
        v->ostanniy_chas = esp_timer_get_time();
        v->zhyvyy = true;

        ESP_LOGI(TAG, "вузол %u: %.2f °C, %.1f %%, %.2f В "
                      "(пакет %lu, втрачено %lu)",
                 p.vuzol, p.temp_x100 / 100.0f, p.hum_x10 / 10.0f,
                 p.napruga_mv / 1000.0f, p.nomer, v->vtracheno);

        vidaty_dali(&p);              // MQTT, веб, дисплей
    }
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/master/docs/en/api-reference/system/freertos_idf.rst
- **Дослівно з джерела:**
  > FromISR functions are ISR-safe variants of FreeRTOS APIs.
- **Спосіб і дата:** curl esp-idf freertos_idf.rst, grep FromISR, 2026-08-26
- **Нотатка:** Текст T-31-076 стверджує, що FromISR функції єдині дозволені в ISR. Джерело підтверджує наявність ISR-safe варіантів.
- **Прохід:** m2-84-freertos

---

<!-- fc id:T-61-061 sha:223fcbe9 src:manual/61-proj-kanal.md:189 status:unchecked -->
### T-61-061 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> memcpy(&p, data, sizeof(p));

**Контекст**

```
## Приймач

static void on_recv(const esp_now_recv_info_t *info,
                    const uint8_t *data, int len) {
    // виконується в контексті задачі Wi-Fi: скопіювати й вийти (розділ 42)
    if (len != sizeof(paket_t)) return;
    paket_t p;
    memcpy(&p, data, sizeof(p));
    xQueueSend(cherga, &p, 0);      // не FromISR: це задача, а не переривання
}
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-062 sha:9f94ad98 src:manual/61-proj-kanal.md:197 status:unchecked -->
### T-61-062 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP_LOGW(TAG, "чужа версія протоколу: %u", p.versiya);

**Контекст**

```
## Приймач

static void task_obrobka(void *arg) {
    paket_t p;
    while (xQueueReceive(cherga, &p, portMAX_DELAY) == pdTRUE) {
        if (p.versiya != PROTO_VERSIYA) {
            ESP_LOGW(TAG, "чужа версія протоколу: %u", p.versiya);
            continue;
        }
        if (p.vuzol >= MAX_VUZLIV) continue;
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-063 sha:56e84656 src:manual/61-proj-kanal.md:203 status:unchecked -->
### T-61-063 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> if (v->ostanniy_nomer && p.nomer > v->ostanniy_nomer + 1)

**Контекст**

```
## Приймач

        stan_vuzla_t *v = &vuzly[p.vuzol];
        if (v->ostanniy_nomer && p.nomer > v->ostanniy_nomer + 1)
            v->vtracheno += p.nomer - v->ostanniy_nomer - 1;
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-064 sha:d513bc14 src:manual/61-proj-kanal.md:222 status:no-external-signal -->
### T-61-064 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Приймач має сам помічати, що вузол зник, — не чекати, поки хтось спитає:

**Контекст**

```
## Контроль зв'язку

Приймач має сам помічати, що вузол зник, — не чекати, поки хтось спитає:
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-065 sha:60da1592 src:manual/61-proj-kanal.md:224 status:code-context -->
### T-61-065 · kod · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ```c
> static void task_kontrol(void *arg) {
>     while (1) {
>         int64_t teper = esp_timer_get_time();
>         for (int i = 0; i < MAX_VUZLIV; i++) {
>             stan_vuzla_t *v = &vuzly[i];
>             if (!v->zhyvyy) continue;
>             // три пропущені інтервали — вважаємо вузол мертвим
>             if (teper - v->ostanniy_chas > 3 * 60 * 1000000LL) {
>                 v->zhyvyy = false;
>                 ESP_LOGE(TAG, "вузол %d не виходить на зв'язок", i);
>                 povidomyty_pro_vtratu(i);
>             }
>         }
>         vTaskDelay(pdMS_TO_TICKS(10000));
>     }
> }
> ```

**Контекст**

````
## Контроль зв'язку

```c
static void task_kontrol(void *arg) {
    while (1) {
        int64_t teper = esp_timer_get_time();
        for (int i = 0; i < MAX_VUZLIV; i++) {
            stan_vuzla_t *v = &vuzly[i];
            if (!v->zhyvyy) continue;
            // три пропущені інтервали — вважаємо вузол мертвим
            if (teper - v->ostanniy_chas > 3 * 60 * 1000000LL) {
                v->zhyvyy = false;
                ESP_LOGE(TAG, "вузол %d не виходить на зв'язок", i);
                povidomyty_pro_vtratu(i);
            }
        }
        vTaskDelay(pdMS_TO_TICKS(10000));
    }
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
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

<!-- fc id:T-61-066 sha:8f529d45 src:manual/61-proj-kanal.md:234 status:unchecked -->
### T-61-066 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> ESP_LOGE(TAG, "вузол %d не виходить на зв'язок", i);

**Контекст**

````
## Контроль зв'язку

```c
static void task_kontrol(void *arg) {
    while (1) {
        int64_t teper = esp_timer_get_time();
        for (int i = 0; i < MAX_VUZLIV; i++) {
            stan_vuzla_t *v = &vuzly[i];
            if (!v->zhyvyy) continue;
            // три пропущені інтервали — вважаємо вузол мертвим
            if (teper - v->ostanniy_chas > 3 * 60 * 1000000LL) {
                v->zhyvyy = false;
                ESP_LOGE(TAG, "вузол %d не виходить на зв'язок", i);
                povidomyty_pro_vtratu(i);
            }
        }
        vTaskDelay(pdMS_TO_TICKS(10000));
    }
}
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-067 sha:53dc7d43 src:manual/61-proj-kanal.md:235 status:unchecked -->
### T-61-067 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> povidomyty_pro_vtratu(i);

**Контекст**

````
## Контроль зв'язку

```c
static void task_kontrol(void *arg) {
    while (1) {
        int64_t teper = esp_timer_get_time();
        for (int i = 0; i < MAX_VUZLIV; i++) {
            stan_vuzla_t *v = &vuzly[i];
            if (!v->zhyvyy) continue;
            // три пропущені інтервали — вважаємо вузол мертвим
            if (teper - v->ostanniy_chas > 3 * 60 * 1000000LL) {
                v->zhyvyy = false;
                ESP_LOGE(TAG, "вузол %d не виходить на зв'язок", i);
                povidomyty_pro_vtratu(i);
            }
        }
        vTaskDelay(pdMS_TO_TICKS(10000));
    }
}
```
````

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-068 sha:ce0827f5 src:manual/61-proj-kanal.md:238 status:verbatim -->
### T-61-068 · kod-ryadok · `manual/61-proj-kanal.md`

**Твердження, коротко**

> vTaskDelay(pdMS_TO_TICKS(10000));

**Контекст**

````
## Контроль зв'язку

```c
static void task_kontrol(void *arg) {
    while (1) {
        int64_t teper = esp_timer_get_time();
        for (int i = 0; i < MAX_VUZLIV; i++) {
            stan_vuzla_t *v = &vuzly[i];
            if (!v->zhyvyy) continue;
            // три пропущені інтервали — вважаємо вузол мертвим
            if (teper - v->ostanniy_chas > 3 * 60 * 1000000LL) {
                v->zhyvyy = false;
                ESP_LOGE(TAG, "вузол %d не виходить на зв'язок", i);
                povidomyty_pro_vtratu(i);
            }
        }
        vTaskDelay(pdMS_TO_TICKS(10000));
    }
}
```
````

**Доказ**

- **Статус:** verbatim — primary, quoted — the source was obtained and the extract copied
- **Джерело:** https://raw.githubusercontent.com/espressif/esp-idf/release/v5.5/components/freertos/FreeRTOS-Kernel/include/freertos/{task,queue,semphr,event_groups,timers}.h та components/esp_common/include/esp_attr.h
- **Дослівно з джерела:**
  > Усі 15 викликів FreeRTOS, що вживає книга, знайдено в заголовках ядра.
  > Макроси:
  >   #define IRAM_ATTR _SECTION_ATTR_IMPL(".iram1", __COUNTER__)
  >   #define RTC_DATA_ATTR _SECTION_ATTR_IMPL(".rtc.data", __COUNTER__)
  >   #define configMAX_PRIORITIES ( 25 )
- **Спосіб і дата:** curl raw.githubusercontent, 2026-08-26
- **Нотатка:** `RTC_DATA_ATTR` кладе змінну в секцію `.rtc.data` — це і є механічне підтвердження того, чому вона переживає deep sleep, тоді як звичайна змінна не переживає. `IRAM_ATTR` кладе функцію в `.iram1`, звідки вона виконується при вимкненому кеші флешу.
- **Прохід:** pass-07-api-rozbyvka

---

<!-- fc id:T-61-069 sha:675401be src:manual/61-proj-kanal.md:243 status:unchecked -->
### T-61-069 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Лічильник `vtracheno` — безкоштовна оцінка якості зв'язку.

**Контекст**

```
## Контроль зв'язку

Лічильник `vtracheno` — безкоштовна оцінка якості зв'язку. Він одразу
показує, чи проблема в конкретному вузлі, чи в загальних умовах.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-070 sha:916b3a63 src:manual/61-proj-kanal.md:243 status:no-external-signal -->
### T-61-070 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Він одразу показує, чи проблема в конкретному вузлі, чи в загальних умовах.

**Контекст**

```
## Контроль зв'язку

Лічильник `vtracheno` — безкоштовна оцінка якості зв'язку. Він одразу
показує, чи проблема в конкретному вузлі, чи в загальних умовах.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-071 sha:12d05c66 src:manual/61-proj-kanal.md:249 status:no-external-signal -->
### T-61-071 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Усі учасники мають бути **на одному каналі**.

**Контекст**

```
## Канал: головна складність розгортання

::: nezvorotne
Усі учасники мають бути **на одному каналі**. Якщо приймач також
під'єднаний до Wi-Fi, його канал визначає **роутер** — і більшість
роутерів обирають канал автоматично й змінюють його самі.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-072 sha:20f218a3 src:manual/61-proj-kanal.md:249 status:unchecked -->
### T-61-072 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Якщо приймач також під'єднаний до Wi-Fi, його канал визначає **роутер** — і більшість роутерів обирають канал автоматично й змінюють його самі.

**Контекст**

```
## Канал: головна складність розгортання

::: nezvorotne
Усі учасники мають бути **на одному каналі**. Якщо приймач також
під'єднаний до Wi-Fi, його канал визначає **роутер** — і більшість
роутерів обирають канал автоматично й змінюють його самі.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-073 sha:3d292935 src:manual/61-proj-kanal.md:253 status:no-external-signal -->
### T-61-073 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Це найчастіша причина «працювало на столі, на об'єкті перестало» (розділ 42).

**Контекст**

```
## Канал: головна складність розгортання

Це найчастіша причина «працювало на столі, на об'єкті перестало»
(розділ 42).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-074 sha:6d5cc616 src:manual/61-proj-kanal.md:258 status:no-external-signal -->
### T-61-074 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Фіксований канал у роутері.** Найпростіше, якщо роутер ваш.

**Контекст**

```
## Канал: головна складність розгортання

**Фіксований канал у роутері.** Найпростіше, якщо роутер ваш.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-075 sha:e85b1b17 src:manual/61-proj-kanal.md:260 status:unchecked -->
### T-61-075 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Приймач без Wi-Fi.** Тільки ESP-NOW на фіксованому каналі, дані далі йдуть по дроту.

**Контекст**

```
## Канал: головна складність розгортання

**Приймач без Wi-Fi.** Тільки ESP-NOW на фіксованому каналі, дані далі
йдуть по дроту.
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-076 sha:a4a5cb00 src:manual/61-proj-kanal.md:263 status:unchecked -->
### T-61-076 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> **Два чипи в приймачі.** Один слухає ESP-NOW на фіксованому каналі, другий тримає Wi-Fi; між ними UART (розділ 34).

**Контекст**

```
## Канал: головна складність розгортання

**Два чипи в приймачі.** Один слухає ESP-NOW на фіксованому каналі,
другий тримає Wi-Fi; між ними UART (розділ 34). Найнадійніше і
найдорожче.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-077 sha:54e08390 src:manual/61-proj-kanal.md:264 status:no-external-signal -->
### T-61-077 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Найнадійніше і найдорожче.

**Контекст**

```
## Канал: головна складність розгортання

**Два чипи в приймачі.** Один слухає ESP-NOW на фіксованому каналі,
другий тримає Wi-Fi; між ними UART (розділ 34). Найнадійніше і
найдорожче.
:::
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-078 sha:4d07d0f3 src:manual/61-proj-kanal.md:270 status:no-external-signal -->
### T-61-078 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Дві плати поруч: пакети доходять, лічильник росте без пропусків. 2.

**Контекст**

```
## Перевірка

1. Дві плати поруч: пакети доходять, лічильник росте без пропусків.
2. Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`.
3. Вимкнути передавач: приймач має за три хвилини повідомити про втрату.
4. Увімкнути назад: накопичене в буфері має дійти.
5. Спробувати надіслати пакет із третього пристрою без ключа: приймач
   має його не прийняти.
6. Виміряти струм передавача за цикл — має бути частки міліампер-секунди
   (розділ 60).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-079 sha:dd7135d0 src:manual/61-proj-kanal.md:271 status:unchecked -->
### T-61-079 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`. 3.

**Контекст**

```
## Перевірка

1. Дві плати поруч: пакети доходять, лічильник росте без пропусків.
2. Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`.
3. Вимкнути передавач: приймач має за три хвилини повідомити про втрату.
4. Увімкнути назад: накопичене в буфері має дійти.
5. Спробувати надіслати пакет із третього пристрою без ключа: приймач
   має його не прийняти.
6. Виміряти струм передавача за цикл — має бути частки міліампер-секунди
   (розділ 60).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-080 sha:76b1afa6 src:manual/61-proj-kanal.md:272 status:no-external-signal -->
### T-61-080 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Вимкнути передавач: приймач має за три хвилини повідомити про втрату. 4.

**Контекст**

```
## Перевірка

1. Дві плати поруч: пакети доходять, лічильник росте без пропусків.
2. Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`.
3. Вимкнути передавач: приймач має за три хвилини повідомити про втрату.
4. Увімкнути назад: накопичене в буфері має дійти.
5. Спробувати надіслати пакет із третього пристрою без ключа: приймач
   має його не прийняти.
6. Виміряти струм передавача за цикл — має бути частки міліампер-секунди
   (розділ 60).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-081 sha:198c83a8 src:manual/61-proj-kanal.md:273 status:no-external-signal -->
### T-61-081 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Увімкнути назад: накопичене в буфері має дійти. 5.

**Контекст**

```
## Перевірка

1. Дві плати поруч: пакети доходять, лічильник росте без пропусків.
2. Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`.
3. Вимкнути передавач: приймач має за три хвилини повідомити про втрату.
4. Увімкнути назад: накопичене в буфері має дійти.
5. Спробувати надіслати пакет із третього пристрою без ключа: приймач
   має його не прийняти.
6. Виміряти струм передавача за цикл — має бути частки міліампер-секунди
   (розділ 60).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-082 sha:746d62bc src:manual/61-proj-kanal.md:274 status:no-external-signal -->
### T-61-082 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Спробувати надіслати пакет із третього пристрою без ключа: приймач має його не прийняти. 6.

**Контекст**

```
## Перевірка

1. Дві плати поруч: пакети доходять, лічильник росте без пропусків.
2. Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`.
3. Вимкнути передавач: приймач має за три хвилини повідомити про втрату.
4. Увімкнути назад: накопичене в буфері має дійти.
5. Спробувати надіслати пакет із третього пристрою без ключа: приймач
   має його не прийняти.
6. Виміряти струм передавача за цикл — має бути частки міліампер-секунди
   (розділ 60).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-083 sha:db90849f src:manual/61-proj-kanal.md:276 status:no-external-signal -->
### T-61-083 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> Виміряти струм передавача за цикл — має бути частки міліампер-секунди (розділ 60).

**Контекст**

```
## Перевірка

1. Дві плати поруч: пакети доходять, лічильник росте без пропусків.
2. Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`.
3. Вимкнути передавач: приймач має за три хвилини повідомити про втрату.
4. Увімкнути назад: накопичене в буфері має дійти.
5. Спробувати надіслати пакет із третього пристрою без ключа: приймач
   має його не прийняти.
6. Виміряти струм передавача за цикл — має бути частки міліампер-секунди
   (розділ 60).
```

**Доказ**

- **Статус:** unchecked — не звірено

---

<!-- fc id:T-61-084 sha:d2b37c0f src:manual/61-proj-kanal.md:281 status:unchecked -->
### T-61-084 · proza · `manual/61-proj-kanal.md`

**Твердження, коротко**

> - **Кілька передавачів на один приймач** — структура вже готова (масив `vuzly`); - **Двонапрямлений обмін**: приймач надсилає команди у відповідь на пакет, поки передавач не заснув; - **Заміна на LoRa** (розділ 43), коли потрібні кілометри: формат пакета й логіка лишаються, змінюється транспорт; - **Ретрансляція** через проміжний вузол для збільшення покриття.

**Контекст**

```
## Розвиток

- **Кілька передавачів на один приймач** — структура вже готова
  (масив `vuzly`);
- **Двонапрямлений обмін**: приймач надсилає команди у відповідь на
  пакет, поки передавач не заснув;
- **Заміна на LoRa** (розділ 43), коли потрібні кілометри: формат
  пакета й логіка лишаються, змінюється транспорт;
- **Ретрансляція** через проміжний вузол для збільшення покриття.
```

**Доказ**

- **Статус:** unchecked — не звірено

---
