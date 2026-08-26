# 59. Моніторинг датчиків з веб-інтерфейсом {#proj-monitor}

Пристрій міряє температуру, вологість і тиск, тримає історію й показує
її у браузері. Доступний за іменем, без пошуку IP-адреси.

Це базовий проєкт: на ньому зустрічаються Wi-Fi, I²C, веб-сервер,
mDNS, зберігання стану й обробка помилок.

## Постановка

**Вхід:** BME280 по I²C — температура, вологість, тиск.

**Вихід:** веб-сторінка з поточними значеннями і графіком за останні
години; JSON для машинного зчитування.

**Живлення:** мережа через USB. Автономність не потрібна.

**Поведінка при відмові:** немає мережі — вимірювання продовжуються й
накопичуються; датчик мовчить — пристрій живий і повідомляє про це.

## Блок-схема

```
   BME280 ──I²C──> ESP32 ──Wi-Fi──> роутер ──> браузер
  (0x76)          [кільцевий буфер            (teplytsia.local)
                   на 720 записів]
```

## Складові

| Позиція | Кількість | Примітка |
|---|---|---|
| ESP32-S3-DevKitC-1 або classic DevKitC | 1 | будь-який із Wi-Fi |
| BME280, модуль I²C | 1 | звірити адресу: `0x76` або `0x77` |
| Резистори 4.7 кОм | 2 | підтягування I²C, якщо немає на модулі |
| Дроти Dupont | 4 | |
| Корпус, живлення | — | розділ 54 |

Ціни й наявність — у вкладиші ринку (Р5).

## Піни за платами

Проєкт розрахований на дві плати, і **піни в них різні**. Спочатку
оберіть рядок, далі читайте схему з ним.

| Сигнал | classic DevKitC | S3-DevKitC-1 |
|---|---|---|
| `SDA` | `GPIO21` | `GPIO8` |
| `SCL` | `GPIO22` | `GPIO9` |

::: nezvorotne
[[S3]] **`GPIO22` на S3 не існує.** У S3 немає пінів 22–25 узагалі — це
видно прямо в ESP-IDF, де маска дійсних пінів їх вирізає. Схема з
`GPIO22`, перенесена з classic, не запрацює: `i2c_new_master_bus`
поверне `ESP_ERR_INVALID_ARG`, і шина лишиться німою.

Драйвер при цьому **називає причину в консолі** — типово, без жодного
налаштування:

```
E (315) i2c.master: i2c_new_master_bus(1049): invalid SDA/SCL pin number
```

Тобто ловиться це за секунду, **якщо дивитися в лог**. Мовчазним воно
стає лише тоді, коли код повернення не перевіряють, а лог гортають повз:
без `ESP_ERROR_CHECK` програма спокійно йде далі до першої транзакції з
дескриптором, якого немає.

Це загальне правило для всіх проєктів цієї частини: **BOM із двома
сімействами означає дві розпіновки**, і жодну з них не можна отримати
з іншої заміною одного числа (додаток A).
:::

## Схема

Нижче — варіант для classic. Для S3 підставте піни з таблиці вище.

```
ESP32              BME280
3V3   ───────────  VCC
GND   ───────────  GND
SDA   ──┬────────  SDA        classic: GPIO21   S3: GPIO8
        └─[4.7к]─ 3V3
SCL   ──┬────────  SCL        classic: GPIO22   S3: GPIO9
        └─[4.7к]─ 3V3
```

Підтягування обов'язкове (розділ 35). Багато модулів BME280 мають власні
резистори — тоді зовнішні не ставити.

## Код

Проєкт ESP-IDF. Конфігурація через `menuconfig` або
`sdkconfig.defaults`.

### Читання датчика

Піни винесені в одне місце нагорі — так їх видно й так вони не
розповзаються по коду:

```c
// Піни за платою. Одне місце на весь проєкт.
#if CONFIG_IDF_TARGET_ESP32S3
#  define PIN_SDA  GPIO_NUM_8
#  define PIN_SCL  GPIO_NUM_9
#else                       // ESP32 classic
#  define PIN_SDA  GPIO_NUM_21
#  define PIN_SCL  GPIO_NUM_22
#endif
```

`CONFIG_IDF_TARGET_*` виставляє сама збірка після `idf.py set-target`,
тож перемикання плати не потребує правок у коді (розділ 11).

```c
#include "driver/i2c_master.h"
#include "esp_log.h"

#define BME_ADDR   0x76
#define REG_ID     0xD0
#define REG_RESET  0xE0
#define REG_CTRL_H 0xF2
#define REG_CTRL_M 0xF4
#define REG_CONFIG 0xF5
#define REG_DATA   0xF7
#define REG_CALIB1 0x88
#define REG_CALIB2 0xE1

static const char *TAG = "BME";
static i2c_master_dev_handle_t bme;

// калібрувальні коефіцієнти живуть у самому датчику
static uint16_t T1; static int16_t T2, T3;
static uint16_t P1; static int16_t P2, P3, P4, P5, P6, P7, P8, P9;
static uint8_t  H1, H3; static int16_t H2, H4, H5; static int8_t H6;
static int32_t  t_fine;

static esp_err_t bme_read(uint8_t reg, uint8_t *buf, size_t len) {
    return i2c_master_transmit_receive(bme, &reg, 1, buf, len,
                                       pdMS_TO_TICKS(100));
}

static esp_err_t bme_write(uint8_t reg, uint8_t val) {
    uint8_t b[2] = { reg, val };
    return i2c_master_transmit(bme, b, 2, pdMS_TO_TICKS(100));
}

esp_err_t bme_init(i2c_master_bus_handle_t bus) {
    i2c_device_config_t cfg = {
        .dev_addr_length = I2C_ADDR_BIT_LEN_7,
        .device_address = BME_ADDR,
        .scl_speed_hz = 100000,
    };
    ESP_RETURN_ON_ERROR(i2c_master_bus_add_device(bus, &cfg, &bme),
                        TAG, "не додано пристрій на шину");

    // регістр ідентифікації: доводить, що обмін працює (розділ 44)
    uint8_t id = 0;
    ESP_RETURN_ON_ERROR(bme_read(REG_ID, &id, 1), TAG, "немає відповіді");
    if (id != 0x60) {
        ESP_LOGE(TAG, "чужий пристрій: id 0x%02x, очікували 0x60", id);
        return ESP_ERR_NOT_FOUND;
    }

    uint8_t c[26];
    ESP_RETURN_ON_ERROR(bme_read(REG_CALIB1, c, 26), TAG, "калібрування");
    T1 = c[0] | (c[1] << 8);   T2 = c[2] | (c[3] << 8);
    T3 = c[4] | (c[5] << 8);   P1 = c[6] | (c[7] << 8);
    P2 = c[8] | (c[9] << 8);   P3 = c[10] | (c[11] << 8);
    P4 = c[12] | (c[13] << 8); P5 = c[14] | (c[15] << 8);
    P6 = c[16] | (c[17] << 8); P7 = c[18] | (c[19] << 8);
    P8 = c[20] | (c[21] << 8); P9 = c[22] | (c[23] << 8);
    H1 = c[25];

    uint8_t h[7];
    ESP_RETURN_ON_ERROR(bme_read(REG_CALIB2, h, 7), TAG, "калібрування H");
    H2 = h[0] | (h[1] << 8);
    H3 = h[2];
    // старший байт H4 і H5 знаковий — розширення знака обов'язкове
    H4 = ((int16_t)(int8_t)h[3] * 16) | (h[4] & 0x0F);
    H5 = ((int16_t)(int8_t)h[5] * 16) | (h[4] >> 4);
    H6 = (int8_t)h[6];

    bme_write(REG_CTRL_H, 0x01);  // osrs_h = ×1
    bme_write(REG_CONFIG, 0xA8);  // t_sb 1000 мс, фільтр ×4
    bme_write(REG_CTRL_M, 0x27);  // osrs_t ×1, osrs_p ×1, режим normal
    ESP_LOGI(TAG, "BME280 знайдено і налаштовано");
    return ESP_OK;
}
```

::: uvaha
Регістр ідентифікації читається **першим** і перевіряється. Це доводить,
що обмін по шині працює, ще до того, як з'явиться перше значення
(розділ 44).

Без цієї перевірки несправна шина дає нулі, які виглядають як
правдоподібні дані.
:::

Порядок трьох записів не довільний: за datasheet зміна `ctrl_hum`
набуває чинності **лише після запису в `ctrl_meas`**, тому `ctrl_meas`
завжди останній. Записаний першим, він лишив би вологість невиміряною —
і датчик віддавав би нулі, схожі на дані.

::: uvaha
Два зсуви в розборі калібрування виглядають однаково і такими не є.
`H4` і `H5` — **знакові** 16-бітові величини, і старший байт кожної
береться зі знаком: `(int16_t)(int8_t)h[3] * 16`, а не `h[3] << 4`.
Різниця виникає лише тоді, коли в старшому байті виставлено сьомий біт,
тобто на частині екземплярів датчика — і виявляється як стабільно
неправильна вологість при правильних температурі й тиску.

Це те місце, де варто звірятися з референсною реалізацією виробника, а
не з чужим прикладом: у прикладах в інтернеті ця помилка трапляється
частіше, ніж правильний варіант.
:::

Перетворення сирих відліків — за формулами з datasheet. Без
калібрувальних коефіцієнтів значення виглядають правдоподібно і є
неправильними:

```c
esp_err_t bme_measure(float *temp, float *hum, float *pres) {
    uint8_t d[8];
    ESP_RETURN_ON_ERROR(bme_read(REG_DATA, d, 8), TAG, "читання");

    int32_t adc_p = ((uint32_t)d[0] << 12) | ((uint32_t)d[1] << 4) | (d[2] >> 4);
    int32_t adc_t = ((uint32_t)d[3] << 12) | ((uint32_t)d[4] << 4) | (d[5] >> 4);
    int32_t adc_h = ((uint32_t)d[6] << 8)  |  (uint32_t)d[7];

    int32_t v1 = ((((adc_t >> 3) - ((int32_t)T1 << 1))) * ((int32_t)T2)) >> 11;
    int32_t v2 = (((((adc_t >> 4) - ((int32_t)T1)) *
                    ((adc_t >> 4) - ((int32_t)T1))) >> 12) * ((int32_t)T3)) >> 14;
    t_fine = v1 + v2;
    *temp = ((t_fine * 5 + 128) >> 8) / 100.0f;

    int64_t p1 = ((int64_t)t_fine) - 128000;
    int64_t p2 = p1 * p1 * (int64_t)P6 + ((p1 * (int64_t)P5) << 17)
               + (((int64_t)P4) << 35);
    p1 = ((p1 * p1 * (int64_t)P3) >> 8) + ((p1 * (int64_t)P2) << 12);
    p1 = (((((int64_t)1) << 47) + p1) * ((int64_t)P1)) >> 33;
    if (p1 == 0) return ESP_ERR_INVALID_STATE;
    int64_t p = 1048576 - adc_p;
    p = (((p << 31) - p2) * 3125) / p1;
    p1 = (((int64_t)P9) * (p >> 13) * (p >> 13)) >> 25;
    p2 = (((int64_t)P8) * p) >> 19;
    *pres = (((p + p1 + p2) >> 8) + (((int64_t)P7) << 4)) / 25600.0f;

    int32_t h = t_fine - 76800;
    h = (((((adc_h << 14) - (((int32_t)H4) << 20) - (((int32_t)H5) * h)) +
        16384) >> 15) * (((((((h * ((int32_t)H6)) >> 10) *
        (((h * ((int32_t)H3)) >> 11) + 32768)) >> 10) + 2097152) *
        ((int32_t)H2) + 8192) >> 14));
    h -= (((((h >> 15) * (h >> 15)) >> 7) * ((int32_t)H1)) >> 4);
    if (h < 0) h = 0;
    if (h > 419430400) h = 419430400;
    *hum = (h >> 12) / 1024.0f;
    return ESP_OK;
}
```

### Кільцевий буфер історії

```c
#define ISTORIYA 720          // 12 годин при вимірюванні раз на хвилину

typedef struct {
    int64_t chas;             // мікросекунди від старту
    float temp, hum, pres;
    bool valid;
} zapys_t;

static zapys_t istoriya[ISTORIYA];
static size_t idx = 0, kilkist = 0;
static SemaphoreHandle_t mutex;

static void dodaty(float t, float h, float p, bool ok) {
    xSemaphoreTake(mutex, portMAX_DELAY);
    istoriya[idx] = (zapys_t){ esp_timer_get_time(), t, h, p, ok };
    idx = (idx + 1) % ISTORIYA;
    if (kilkist < ISTORIYA) kilkist++;
    xSemaphoreGive(mutex);
}
```

Буфер виділяється **статично**, один раз. Ніякого `malloc` у циклі
(розділ 30).

### Задача вимірювання

```c
static void task_vymir(void *arg) {
    int pomylok_pospil = 0;
    while (1) {
        float t, h, p;
        esp_err_t err = bme_measure(&t, &h, &p);
        if (err == ESP_OK) {
            pomylok_pospil = 0;
            dodaty(t, h, p, true);
            ESP_LOGI(TAG, "%.2f °C, %.1f %%, %.1f гПа", t, h, p);
        } else {
            pomylok_pospil++;
            dodaty(0, 0, 0, false);
            ESP_LOGW(TAG, "датчик не відповідає (%d поспіль): %s",
                     pomylok_pospil, esp_err_to_name(err));
            // деградуємо, а не перезавантажуємось (розділ 32)
        }
        ESP_LOGD(TAG, "вільно RAM: %lu, мінімум: %lu",
                 esp_get_free_heap_size(), esp_get_minimum_free_heap_size());
        vTaskDelay(pdMS_TO_TICKS(60000));
    }
}
```

Датчик, що замовк, не зупиняє пристрій: записується позначка про збій, і
робота триває. Веб-інтерфейс покаже, що дані застаріли.

### Веб-сервер

```c
static esp_err_t json_handler(httpd_req_t *req) {
    char *buf = malloc(16384);
    if (!buf) return httpd_resp_send_500(req);

    xSemaphoreTake(mutex, portMAX_DELAY);
    int n = snprintf(buf, 16384, "{\"zapysiv\":%u,\"dani\":[", kilkist);
    size_t start = (kilkist == ISTORIYA) ? idx : 0;
    bool pershyy = true;                       // ← не «i == 0», див. нижче
    for (size_t i = 0; i < kilkist && n < 16000; i++) {
        zapys_t *z = &istoriya[(start + i) % ISTORIYA];
        if (!z->valid) continue;
        n += snprintf(buf + n, 16384 - n,
                      "%s{\"t\":%lld,\"temp\":%.2f,\"hum\":%.1f,\"pres\":%.1f}",
                      pershyy ? "" : ",",
                      z->chas / 1000000, z->temp, z->hum, z->pres);
        pershyy = false;
    }
    xSemaphoreGive(mutex);
    snprintf(buf + n, 16384 - n, "]}");

    httpd_resp_set_type(req, "application/json");
    esp_err_t r = httpd_resp_sendstr(req, buf);
    free(buf);
    return r;
}
```

::: uvaha
Окремий прапорець `pershyy` замість перевірки `i == 0` — не педантизм.
Записи зі збоєм пропускаються через `continue`, тож індекс циклу і номер
**виведеного** елемента розходяться. Варіант `i ? "," : ""` при першому
ж збійному запису на початку історії поставить кому перед першим
елементом, і JSON стане несинтаксичним: `"dani":[,{…}]`.

Ламається це рівно тоді, коли датчик відмовив, — тобто саме тоді, коли на
графік дивляться. Це типова форма помилки в цій книзі: код правильний для
щасливого шляху й невірний для того, заради якого писався.
:::

::: uvaha
Буфер тут виділяється з купи й одразу звільняється — це **не** цикл
виділень, а разова операція на запит. Різниця з правилом розділу 30 у
тому, що частота низька й розмір фіксований.

Уважніше треба з іншим: обробник виконується в задачі веб-сервера з
обмеженим стеком. Тому 16 КБ беруться з купи, а не оголошуються як
локальний масив — інакше стек переповниться (розділ 30).
:::

### Головна функція

```c
void app_main(void) {
    ESP_LOGI(TAG, "старт, причина скидання: %d", esp_reset_reason());

    esp_err_t err = nvs_flash_init();
    if (err == ESP_ERR_NVS_NO_FREE_PAGES || err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        ESP_ERROR_CHECK(nvs_flash_erase());
        err = nvs_flash_init();
    }
    ESP_ERROR_CHECK(err);

    mutex = xSemaphoreCreateMutex();

    i2c_master_bus_config_t bus_cfg = {
        .i2c_port = I2C_NUM_0,
        .sda_io_num = PIN_SDA,   // classic 21 / S3 8 — див. таблицю пінів
        .scl_io_num = PIN_SCL,   // classic 22 / S3 9
        .clk_source = I2C_CLK_SRC_DEFAULT,
        .glitch_ignore_cnt = 7,
    };
    i2c_master_bus_handle_t bus;
    ESP_ERROR_CHECK(i2c_new_master_bus(&bus_cfg, &bus));

    if (bme_init(bus) != ESP_OK) {
        ESP_LOGE(TAG, "датчик не знайдено — працюємо без нього");
        // не ESP_ERROR_CHECK: веб-інтерфейс має піднятися й показати проблему
    }

    wifi_start();                 // під'єднання з повторами, розділ 39
    mdns_init();
    mdns_hostname_set("teplytsia");
    mdns_service_add(NULL, "_http", "_tcp", 80, NULL, 0);

    web_start();
    xTaskCreate(task_vymir, "vymir", 4096, NULL, 5, NULL);
}
```

::: nezvorotne
`ESP_ERROR_CHECK` тут стоїть лише навколо NVS і створення шини — того,
без чого пристрій не має сенсу.

Навколо ініціалізації датчика його **немає** свідомо: несправний датчик
не повинен перетворювати пристрій на цеглинку. Веб-інтерфейс має
піднятися й показати, що датчик мовчить (розділ 32).
:::

## Збирання і перевірка

```
idf.py set-target esp32s3
idf.py menuconfig          # Wi-Fi, розбивка флешу з OTA (розділ 18)
idf.py build
idf.py -p /dev/ttyUSB0 flash monitor
```

Порядок перевірки:

1. У лозі — `BME280 знайдено і налаштовано`. Немає — сканер I²C
   (розділ 35).
2. Перше вимірювання з осмисленими значеннями.
3. `teplytsia.local` відкривається у браузері.
4. Від'єднати датчик на ходу: пристрій лишається живим, у лозі
   попередження, веб показує застарілі дані.
5. Вимкнути роутер: вимірювання тривають, після відновлення веб знову
   доступний.
6. Доба безперервної роботи: мінімум вільної пам'яті не зменшується
   (розділ 58).

## Розвиток

- **MQTT** замість або разом із веб-інтерфейсом (розділ 40);
- **другий датчик** — DS18B20 на вулиці (розділ 37);
- **OTA** — розбивку вже закладено (розділ 19);
- **e-paper** для показу на місці (розділ 46);
- **автономність**: перехід на deep sleep і ESP-NOW перетворює це на
  проєкт 60.
