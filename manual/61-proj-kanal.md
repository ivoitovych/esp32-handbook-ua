# 61. Радіоканал між двома платами {#proj-kanal}

Надійний обмін між двома пристроями без роутера, без інтернету й без
інфраструктури. ESP-NOW із шифруванням, підтвердженням і контролем
зв'язку.

Це основа для будь-якої системи «датчик — приймач» і найкорисніший
проєкт для автономних вузлів (розділ 42).

## Постановка

**Задача:** передавач раз на хвилину надсилає вимірювання, приймач
отримує, показує і віддає далі. Обидва мають знати, чи живий партнер.

**Живлення:** передавач від акумулятора (deep sleep між передачами),
приймач від мережі.

**Захист:** шифрування; чужий пристрій не може ні прочитати, ні
підробити пакет.

**Поведінка при відмові:** передавач не отримав підтвердження — повторює
й накопичує; приймач не бачить пакетів — повідомляє про втрату вузла.

## Чому ESP-NOW, а не Wi-Fi

Для передавача на батарейці різниця вирішальна (розділ 42):

| | Wi-Fi | ESP-NOW |
|---|---|---|
| Час до передачі | 1–10 с | **10 мс** |
| Заряд на цикл | ~500 мА·с | **~5 мА·с** |
| Потрібен роутер | так | **ні** |

Два порядки економії — це різниця між місяцем і роками.

## Формат пакета

Спільний заголовок для обох боків. Це те, що варто продумати один раз:
змінити формат після розгортання означає перепрошити всі вузли.

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

::: uvaha
Три рішення в цій структурі, кожне з причиною.

**`versiya` першим полем.** Коли формат зміниться, старий приймач зможе
розпізнати незнайому версію і не розібрати сміття як дані.

**`__attribute__((packed))`** прибирає вирівнювання, яке компілятор
додав би сам. Без нього структура на двох різних чипах може мати різний
розмір.

**Цілі замість `float`.** Менший розмір, немає питань про представлення
чисел, і на чипах без FPU дешевше (розділ 02).
:::

## Передавач

```c
static const uint8_t MAC_PRYIMACHA[6] = { 0x24, 0x6F, 0x28, 0x11, 0x22, 0x33 };

RTC_DATA_ATTR static uint32_t nomer = 0;
RTC_DATA_ATTR static paket_t  bufer[10];
RTC_DATA_ATTR static uint8_t  u_buferi = 0;

static volatile bool dostavleno = false;

static void on_sent(const uint8_t *mac, esp_now_send_status_t status) {
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

::: uvaha
`esp_now_send` повертається **до** фактичної передачі. Статус приходить
у зворотний виклик `on_sent`, і саме його треба дочекатися перед
засинанням — інакше чип засне посеред передачі.

Це та сама помилка, що з `uart_wait_tx_done` у RS-485 (розділ 34), і
проявляється так само: «інколи не доходить».
:::

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

::: nezvorotne
Ключі читаються **з NVS**, а не зашиті в код. Зашитий ключ дістається з
дампа прошивки за п'ять хвилин (розділи 24, 50).

І ключі мають бути **різні на кожну пару вузлів**, а не один на всю
систему: інакше захоплення одного датчика компрометує всю мережу.

Записуються при виробництві разом із номером вузла (розділ 21).
:::

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
    // виконується в контексті Wi-Fi: скопіювати й вийти (розділ 42)
    if (len != sizeof(paket_t)) return;
    paket_t p;
    memcpy(&p, data, sizeof(p));
    xQueueSendFromISR(cherga, &p, NULL);
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

## Контроль зв'язку

Приймач має сам помічати, що вузол зник, — не чекати, поки хтось спитає:

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

Лічильник `vtracheno` — безкоштовна оцінка якості зв'язку. Він одразу
показує, чи проблема в конкретному вузлі, чи в загальних умовах.

## Канал: головна складність розгортання

::: nezvorotne
Усі учасники мають бути **на одному каналі**. Якщо приймач також
під'єднаний до Wi-Fi, його канал визначає **роутер** — і більшість
роутерів обирають канал автоматично й змінюють його самі.

Це найчастіша причина «працювало на столі, на об'єкті перестало»
(розділ 42).

Три робочі варіанти:

**Фіксований канал у роутері.** Найпростіше, якщо роутер ваш.

**Приймач без Wi-Fi.** Тільки ESP-NOW на фіксованому каналі, дані далі
йдуть по дроту.

**Два чипи в приймачі.** Один слухає ESP-NOW на фіксованому каналі,
другий тримає Wi-Fi; між ними UART (розділ 34). Найнадійніше і
найдорожче.
:::

## Перевірка

1. Дві плати поруч: пакети доходять, лічильник росте без пропусків.
2. Рознести на робочу відстань, тиждень роботи: подивитися `vtracheno`.
3. Вимкнути передавач: приймач має за три хвилини повідомити про втрату.
4. Увімкнути назад: накопичене в буфері має дійти.
5. Спробувати надіслати пакет із третього пристрою без ключа: приймач
   має його не прийняти.
6. Виміряти струм передавача за цикл — має бути частки міліампер-секунди
   (розділ 60).

## Розвиток

- **Кілька передавачів на один приймач** — структура вже готова
  (масив `vuzly`);
- **Двонапрямлений обмін**: приймач надсилає команди у відповідь на
  пакет, поки передавач не заснув;
- **Заміна на LoRa** (розділ 43), коли потрібні кілометри: формат
  пакета й логіка лишаються, змінюється транспорт;
- **Ретрансляція** через проміжний вузол для збільшення покриття.
