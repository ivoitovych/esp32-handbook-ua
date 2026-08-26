# Фактчекінг: `manual/59-proj-monitor.md`

Одиниць твердження: **116**. Клас доказу й формат запису — `factcheck/SCHEMA.md`.

Цей файл **генерується**: текст книги береться з джерела, докази — з `factcheck/dokazy/`. Правити вручну нема сенсу.

---

<!-- fc id:T-59-001 sha:027cf49b src:manual/59-proj-monitor.md:3 klas:F -->
### T-59-001 · proza · рядок 3

**Книга каже, дослівно:**

> Пристрій міряє температуру, вологість і тиск, тримає історію й показує її у браузері.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-002 sha:622435fa src:manual/59-proj-monitor.md:3 klas:F -->
### T-59-002 · proza · рядок 3

**Книга каже, дослівно:**

> Доступний за іменем, без пошуку IP-адреси.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-003 sha:62e72694 src:manual/59-proj-monitor.md:6 klas:F -->
### T-59-003 · proza · рядок 6

**Книга каже, дослівно:**

> Це базовий проєкт: на ньому зустрічаються Wi-Fi, I²C, веб-сервер, mDNS, зберігання стану й обробка помилок.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-004 sha:3a523fc0 src:manual/59-proj-monitor.md:11 klas:F -->
### T-59-004 · proza · рядок 11

**Книга каже, дослівно:**

> **Вхід:** BME280 по I²C — температура, вологість, тиск.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-005 sha:9363613b src:manual/59-proj-monitor.md:13 klas:F -->
### T-59-005 · proza · рядок 13

**Книга каже, дослівно:**

> **Вихід:** веб-сторінка з поточними значеннями і графіком за останні години; JSON для машинного зчитування.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-006 sha:cc87583a src:manual/59-proj-monitor.md:16 klas:F -->
### T-59-006 · proza · рядок 16

**Книга каже, дослівно:**

> **Живлення:** мережа через USB.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-007 sha:71b33275 src:manual/59-proj-monitor.md:16 klas:F -->
### T-59-007 · proza · рядок 16

**Книга каже, дослівно:**

> Автономність не потрібна.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-008 sha:5451c890 src:manual/59-proj-monitor.md:18 klas:F -->
### T-59-008 · proza · рядок 18

**Книга каже, дослівно:**

> **Поведінка при відмові:** немає мережі — вимірювання продовжуються й накопичуються; датчик мовчить — пристрій живий і повідомляє про це.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-009 sha:c141e070 src:manual/59-proj-monitor.md:23 klas:F -->
### T-59-009 · kod · рядок 23

**Книга каже, дослівно:**

> ```
>    BME280 ──I²C──> ESP32 ──Wi-Fi──> роутер ──> браузер
>   (0x76)          [кільцевий буфер            (teplytsia.local)
>                    на 720 записів]
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-010 sha:648244e3 src:manual/59-proj-monitor.md:31 klas:F -->
### T-59-010 · tablycya-shapka · рядок 31

**Книга каже, дослівно:**

> | Позиція | Кількість | Примітка |

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-011 sha:bf7fec58 src:manual/59-proj-monitor.md:32 klas:F -->
### T-59-011 · komirka · рядок 32

**Книга каже, дослівно:**

> ESP32-S3-DevKitC-1 або classic DevKitC · Кількість → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-012 sha:f93103c7 src:manual/59-proj-monitor.md:32 klas:F -->
### T-59-012 · komirka · рядок 32

**Книга каже, дослівно:**

> ESP32-S3-DevKitC-1 або classic DevKitC · Примітка → будь-який із Wi-Fi

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-013 sha:82dde248 src:manual/59-proj-monitor.md:33 klas:F -->
### T-59-013 · komirka · рядок 33

**Книга каже, дослівно:**

> BME280, модуль I²C · Кількість → 1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-014 sha:33217139 src:manual/59-proj-monitor.md:33 klas:F -->
### T-59-014 · komirka · рядок 33

**Книга каже, дослівно:**

> BME280, модуль I²C · Примітка → звірити адресу: `0x76` або `0x77`

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-015 sha:17139ead src:manual/59-proj-monitor.md:34 klas:F -->
### T-59-015 · komirka · рядок 34

**Книга каже, дослівно:**

> Резистори 4.7 кОм · Кількість → 2

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-016 sha:e28e0795 src:manual/59-proj-monitor.md:34 klas:F -->
### T-59-016 · komirka · рядок 34

**Книга каже, дослівно:**

> Резистори 4.7 кОм · Примітка → підтягування I²C, якщо немає на модулі

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-017 sha:b849725c src:manual/59-proj-monitor.md:35 klas:F -->
### T-59-017 · komirka · рядок 35

**Книга каже, дослівно:**

> Дроти Dupont · Кількість → 4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-018 sha:a8265b17 src:manual/59-proj-monitor.md:36 klas:F -->
### T-59-018 · komirka · рядок 36

**Книга каже, дослівно:**

> Корпус, живлення · Примітка → розділ 54

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-019 sha:fd7a49cd src:manual/59-proj-monitor.md:39 klas:F -->
### T-59-019 · proza · рядок 39

**Книга каже, дослівно:**

> Ціни й наявність — у вкладиші ринку (Р5).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-020 sha:727227f3 src:manual/59-proj-monitor.md:43 klas:F -->
### T-59-020 · kod · рядок 43

**Книга каже, дослівно:**

> ```
> ESP32              BME280
> 3V3   ───────────  VCC
> GND   ───────────  GND
> GPIO21 ──┬───────  SDA
>          └─[4.7к]─ 3V3
> GPIO22 ──┬───────  SCL
>          └─[4.7к]─ 3V3
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-021 sha:d3c9dd2a src:manual/59-proj-monitor.md:53 klas:F -->
### T-59-021 · proza · рядок 53

**Книга каже, дослівно:**

> Підтягування обов'язкове (розділ 35).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-022 sha:4899bc0a src:manual/59-proj-monitor.md:53 klas:F -->
### T-59-022 · proza · рядок 53

**Книга каже, дослівно:**

> Багато модулів BME280 мають власні резистори — тоді зовнішні не ставити.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-023 sha:db95e0e2 src:manual/59-proj-monitor.md:58 klas:F -->
### T-59-023 · proza · рядок 58

**Книга каже, дослівно:**

> Конфігурація через `menuconfig` або `sdkconfig.defaults`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-024 sha:360842c7 src:manual/59-proj-monitor.md:63 klas:F -->
### T-59-024 · kod · рядок 63

**Книга каже, дослівно:**

> ```c
> #include "driver/i2c_master.h"
> #include "esp_log.h"
> 
> #define BME_ADDR   0x76
> #define REG_ID     0xD0
> #define REG_RESET  0xE0
> #define REG_CTRL_H 0xF2
> #define REG_CTRL_M 0xF4
> #define REG_CONFIG 0xF5
> #define REG_DATA   0xF7
> #define REG_CALIB1 0x88
> #define REG_CALIB2 0xE1
> 
> static const char *TAG = "BME";
> static i2c_master_dev_handle_t bme;
> 
> // калібрувальні коефіцієнти живуть у самому датчику
> static uint16_t T1; static int16_t T2, T3;
> static uint16_t P1; static int16_t P2, P3, P4, P5, P6, P7, P8, P9;
> static uint8_t  H1, H3; static int16_t H2, H4, H5; static int8_t H6;
> static int32_t  t_fine;
> 
> static esp_err_t bme_read(uint8_t reg, uint8_t *buf, size_t len) {
>     return i2c_master_transmit_receive(bme, &reg, 1, buf, len,
>                                        pdMS_TO_TICKS(100));
> }
> 
> static esp_err_t bme_write(uint8_t reg, uint8_t val) {
>     uint8_t b[2] = { reg, val };
>     return i2c_master_transmit(bme, b, 2, pdMS_TO_TICKS(100));
> }
> 
> esp_err_t bme_init(i2c_master_bus_handle_t bus) {
>     i2c_device_config_t cfg = {
>         .dev_addr_length = I2C_ADDR_BIT_LEN_7,
>         .device_address = BME_ADDR,
>         .scl_speed_hz = 100000,
>     };
>     ESP_RETURN_ON_ERROR(i2c_master_bus_add_device(bus, &cfg, &bme),
>                         TAG, "не додано пристрій на шину");
> 
>     // регістр ідентифікації: доводить, що обмін працює (розділ 44)
>     uint8_t id = 0;
>     ESP_RETURN_ON_ERROR(bme_read(REG_ID, &id, 1), TAG, "немає відповіді");
>     if (id != 0x60) {
>         ESP_LOGE(TAG, "чужий пристрій: id 0x%02x, очікували 0x60", id);
>         return ESP_ERR_NOT_FOUND;
>     }
> 
>     uint8_t c[26];
>     ESP_RETURN_ON_ERROR(bme_read(REG_CALIB1, c, 26), TAG, "калібрування");
>     T1 = c[0] | (c[1] << 8);   T2 = c[2] | (c[3] << 8);
>     T3 = c[4] | (c[5] << 8);   P1 = c[6] | (c[7] << 8);
>     P2 = c[8] | (c[9] << 8);   P3 = c[10] | (c[11] << 8);
>     P4 = c[12] | (c[13] << 8); P5 = c[14] | (c[15] << 8);
>     P6 = c[16] | (c[17] << 8); P7 = c[18] | (c[19] << 8);
>     P8 = c[20] | (c[21] << 8); P9 = c[22] | (c[23] << 8);
>     H1 = c[25];
> 
>     uint8_t h[7];
>     ESP_RETURN_ON_ERROR(bme_read(REG_CALIB2, h, 7), TAG, "калібрування H");
>     H2 = h[0] | (h[1] << 8);
>     H3 = h[2];
>     H4 = (h[3] << 4) | (h[4] & 0x0F);
>     H5 = (h[5] << 4) | (h[4] >> 4);
>     H6 = h[6];
> 
>     bme_write(REG_CTRL_H, 0x01);  // osrs_h = ×1
>     bme_write(REG_CONFIG, 0xA8);  // t_sb 1000 мс, фільтр ×4
>     bme_write(REG_CTRL_M, 0x27);  // osrs_t ×1, osrs_p ×1, режим normal
>     ESP_LOGI(TAG, "BME280 знайдено і налаштовано");
>     return ESP_OK;
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-025 sha:b887153b src:manual/59-proj-monitor.md:64 klas:F -->
### T-59-025 · kod-ryadok · рядок 64

**Книга каже, дослівно:**

> #include "driver/i2c_master.h"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-026 sha:14f48f1e src:manual/59-proj-monitor.md:65 klas:F -->
### T-59-026 · kod-ryadok · рядок 65

**Книга каже, дослівно:**

> #include "esp_log.h"

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-027 sha:e627b88d src:manual/59-proj-monitor.md:67 klas:F -->
### T-59-027 · kod-ryadok · рядок 67

**Книга каже, дослівно:**

> #define BME_ADDR   0x76

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-028 sha:8f633bc7 src:manual/59-proj-monitor.md:68 klas:F -->
### T-59-028 · kod-ryadok · рядок 68

**Книга каже, дослівно:**

> #define REG_ID     0xD0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-029 sha:ccdaaa21 src:manual/59-proj-monitor.md:69 klas:F -->
### T-59-029 · kod-ryadok · рядок 69

**Книга каже, дослівно:**

> #define REG_RESET  0xE0

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-030 sha:0263b9cf src:manual/59-proj-monitor.md:70 klas:F -->
### T-59-030 · kod-ryadok · рядок 70

**Книга каже, дослівно:**

> #define REG_CTRL_H 0xF2

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-031 sha:41e596ad src:manual/59-proj-monitor.md:71 klas:F -->
### T-59-031 · kod-ryadok · рядок 71

**Книга каже, дослівно:**

> #define REG_CTRL_M 0xF4

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-032 sha:35c7c342 src:manual/59-proj-monitor.md:72 klas:F -->
### T-59-032 · kod-ryadok · рядок 72

**Книга каже, дослівно:**

> #define REG_CONFIG 0xF5

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-033 sha:2e56e3a4 src:manual/59-proj-monitor.md:73 klas:F -->
### T-59-033 · kod-ryadok · рядок 73

**Книга каже, дослівно:**

> #define REG_DATA   0xF7

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-034 sha:4ad3a8c3 src:manual/59-proj-monitor.md:74 klas:F -->
### T-59-034 · kod-ryadok · рядок 74

**Книга каже, дослівно:**

> #define REG_CALIB1 0x88

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-035 sha:584d2b44 src:manual/59-proj-monitor.md:75 klas:F -->
### T-59-035 · kod-ryadok · рядок 75

**Книга каже, дослівно:**

> #define REG_CALIB2 0xE1

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-036 sha:64196cae src:manual/59-proj-monitor.md:88 klas:F -->
### T-59-036 · kod-ryadok · рядок 88

**Книга каже, дослівно:**

> pdMS_TO_TICKS(100));

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-037 sha:b49aeb96 src:manual/59-proj-monitor.md:98 klas:F -->
### T-59-037 · kod-ryadok · рядок 98

**Книга каже, дослівно:**

> .dev_addr_length = I2C_ADDR_BIT_LEN_7,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-038 sha:7b9b8843 src:manual/59-proj-monitor.md:99 klas:F -->
### T-59-038 · kod-ryadok · рядок 99

**Книга каже, дослівно:**

> .device_address = BME_ADDR,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-039 sha:bab2ac7a src:manual/59-proj-monitor.md:100 klas:F -->
### T-59-039 · kod-ryadok · рядок 100

**Книга каже, дослівно:**

> .scl_speed_hz = 100000,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-040 sha:e8502537 src:manual/59-proj-monitor.md:102 klas:F -->
### T-59-040 · kod-ryadok · рядок 102

**Книга каже, дослівно:**

> ESP_RETURN_ON_ERROR(i2c_master_bus_add_device(bus, &cfg, &bme),

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-041 sha:41f585b1 src:manual/59-proj-monitor.md:107 klas:F -->
### T-59-041 · kod-ryadok · рядок 107

**Книга каже, дослівно:**

> ESP_RETURN_ON_ERROR(bme_read(REG_ID, &id, 1), TAG, "немає відповіді");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-042 sha:73bf40aa src:manual/59-proj-monitor.md:109 klas:F -->
### T-59-042 · kod-ryadok · рядок 109

**Книга каже, дослівно:**

> ESP_LOGE(TAG, "чужий пристрій: id 0x%02x, очікували 0x60", id);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-043 sha:1b551a44 src:manual/59-proj-monitor.md:114 klas:F -->
### T-59-043 · kod-ryadok · рядок 114

**Книга каже, дослівно:**

> ESP_RETURN_ON_ERROR(bme_read(REG_CALIB1, c, 26), TAG, "калібрування");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-044 sha:ae86aa1b src:manual/59-proj-monitor.md:124 klas:F -->
### T-59-044 · kod-ryadok · рядок 124

**Книга каже, дослівно:**

> ESP_RETURN_ON_ERROR(bme_read(REG_CALIB2, h, 7), TAG, "калібрування H");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-045 sha:636dc01a src:manual/59-proj-monitor.md:134 klas:F -->
### T-59-045 · kod-ryadok · рядок 134

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "BME280 знайдено і налаштовано");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-046 sha:7100ace9 src:manual/59-proj-monitor.md:140 klas:F -->
### T-59-046 · proza · рядок 140

**Книга каже, дослівно:**

> Регістр ідентифікації читається **першим** і перевіряється.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-047 sha:0ea0eacb src:manual/59-proj-monitor.md:140 klas:F -->
### T-59-047 · proza · рядок 140

**Книга каже, дослівно:**

> Це доводить, що обмін по шині працює, ще до того, як з'явиться перше значення (розділ 44).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-048 sha:d91d9459 src:manual/59-proj-monitor.md:144 klas:F -->
### T-59-048 · proza · рядок 144

**Книга каже, дослівно:**

> Без цієї перевірки несправна шина дає нулі, які виглядають як правдоподібні дані.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-049 sha:29da9177 src:manual/59-proj-monitor.md:148 klas:F -->
### T-59-049 · proza · рядок 148

**Книга каже, дослівно:**

> Порядок трьох записів не довільний: за datasheet зміна `ctrl_hum` набуває чинності **лише після запису в `ctrl_meas`**, тому `ctrl_meas` завжди останній.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-050 sha:49eb3151 src:manual/59-proj-monitor.md:148 klas:F -->
### T-59-050 · proza · рядок 148

**Книга каже, дослівно:**

> Записаний першим, він лишив би вологість невиміряною — і датчик віддавав би нулі, схожі на дані.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-051 sha:ae5f2fa1 src:manual/59-proj-monitor.md:153 klas:F -->
### T-59-051 · proza · рядок 153

**Книга каже, дослівно:**

> Перетворення сирих відліків — за формулами з datasheet.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-052 sha:88a09b36 src:manual/59-proj-monitor.md:153 klas:F -->
### T-59-052 · proza · рядок 153

**Книга каже, дослівно:**

> Без калібрувальних коефіцієнтів значення виглядають правдоподібно і є неправильними:

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-053 sha:7bf92ad8 src:manual/59-proj-monitor.md:157 klas:F -->
### T-59-053 · kod · рядок 157

**Книга каже, дослівно:**

> ```c
> esp_err_t bme_measure(float *temp, float *hum, float *pres) {
>     uint8_t d[8];
>     ESP_RETURN_ON_ERROR(bme_read(REG_DATA, d, 8), TAG, "читання");
> 
>     int32_t adc_p = ((uint32_t)d[0] << 12) | ((uint32_t)d[1] << 4) | (d[2] >> 4);
>     int32_t adc_t = ((uint32_t)d[3] << 12) | ((uint32_t)d[4] << 4) | (d[5] >> 4);
>     int32_t adc_h = ((uint32_t)d[6] << 8)  |  (uint32_t)d[7];
> 
>     int32_t v1 = ((((adc_t >> 3) - ((int32_t)T1 << 1))) * ((int32_t)T2)) >> 11;
>     int32_t v2 = (((((adc_t >> 4) - ((int32_t)T1)) *
>                     ((adc_t >> 4) - ((int32_t)T1))) >> 12) * ((int32_t)T3)) >> 14;
>     t_fine = v1 + v2;
>     *temp = ((t_fine * 5 + 128) >> 8) / 100.0f;
> 
>     int64_t p1 = ((int64_t)t_fine) - 128000;
>     int64_t p2 = p1 * p1 * (int64_t)P6 + ((p1 * (int64_t)P5) << 17)
>                + (((int64_t)P4) << 35);
>     p1 = ((p1 * p1 * (int64_t)P3) >> 8) + ((p1 * (int64_t)P2) << 12);
>     p1 = (((((int64_t)1) << 47) + p1) * ((int64_t)P1)) >> 33;
>     if (p1 == 0) return ESP_ERR_INVALID_STATE;
>     int64_t p = 1048576 - adc_p;
>     p = (((p << 31) - p2) * 3125) / p1;
>     p1 = (((int64_t)P9) * (p >> 13) * (p >> 13)) >> 25;
>     p2 = (((int64_t)P8) * p) >> 19;
>     *pres = (((p + p1 + p2) >> 8) + (((int64_t)P7) << 4)) / 25600.0f;
> 
>     int32_t h = t_fine - 76800;
>     h = (((((adc_h << 14) - (((int32_t)H4) << 20) - (((int32_t)H5) * h)) +
>         16384) >> 15) * (((((((h * ((int32_t)H6)) >> 10) *
>         (((h * ((int32_t)H3)) >> 11) + 32768)) >> 10) + 2097152) *
>         ((int32_t)H2) + 8192) >> 14));
>     h -= (((((h >> 15) * (h >> 15)) >> 7) * ((int32_t)H1)) >> 4);
>     if (h < 0) h = 0;
>     if (h > 419430400) h = 419430400;
>     *hum = (h >> 12) / 1024.0f;
>     return ESP_OK;
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-054 sha:ffffb2b5 src:manual/59-proj-monitor.md:160 klas:F -->
### T-59-054 · kod-ryadok · рядок 160

**Книга каже, дослівно:**

> ESP_RETURN_ON_ERROR(bme_read(REG_DATA, d, 8), TAG, "читання");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-055 sha:10e4d48d src:manual/59-proj-monitor.md:199 klas:F -->
### T-59-055 · kod · рядок 199

**Книга каже, дослівно:**

> ```c
> #define ISTORIYA 720          // 12 годин при вимірюванні раз на хвилину
> 
> typedef struct {
>     int64_t chas;             // мікросекунди від старту
>     float temp, hum, pres;
>     bool valid;
> } zapys_t;
> 
> static zapys_t istoriya[ISTORIYA];
> static size_t idx = 0, kilkist = 0;
> static SemaphoreHandle_t mutex;
> 
> static void dodaty(float t, float h, float p, bool ok) {
>     xSemaphoreTake(mutex, portMAX_DELAY);
>     istoriya[idx] = (zapys_t){ esp_timer_get_time(), t, h, p, ok };
>     idx = (idx + 1) % ISTORIYA;
>     if (kilkist < ISTORIYA) kilkist++;
>     xSemaphoreGive(mutex);
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-056 sha:59d72679 src:manual/59-proj-monitor.md:200 klas:F -->
### T-59-056 · kod-ryadok · рядок 200

**Книга каже, дослівно:**

> #define ISTORIYA 720          // 12 годин при вимірюванні раз на хвилину

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-057 sha:da52f140 src:manual/59-proj-monitor.md:213 klas:F -->
### T-59-057 · kod-ryadok · рядок 213

**Книга каже, дослівно:**

> xSemaphoreTake(mutex, portMAX_DELAY);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-058 sha:05942241 src:manual/59-proj-monitor.md:217 klas:F -->
### T-59-058 · kod-ryadok · рядок 217

**Книга каже, дослівно:**

> xSemaphoreGive(mutex);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-059 sha:7c65034e src:manual/59-proj-monitor.md:221 klas:F -->
### T-59-059 · proza · рядок 221

**Книга каже, дослівно:**

> Буфер виділяється **статично**, один раз.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-060 sha:2eaae5f5 src:manual/59-proj-monitor.md:221 klas:F -->
### T-59-060 · proza · рядок 221

**Книга каже, дослівно:**

> Ніякого `malloc` у циклі (розділ 30).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-061 sha:0c21042b src:manual/59-proj-monitor.md:226 klas:F -->
### T-59-061 · kod · рядок 226

**Книга каже, дослівно:**

> ```c
> static void task_vymir(void *arg) {
>     int pomylok_pospil = 0;
>     while (1) {
>         float t, h, p;
>         esp_err_t err = bme_measure(&t, &h, &p);
>         if (err == ESP_OK) {
>             pomylok_pospil = 0;
>             dodaty(t, h, p, true);
>             ESP_LOGI(TAG, "%.2f °C, %.1f %%, %.1f гПа", t, h, p);
>         } else {
>             pomylok_pospil++;
>             dodaty(0, 0, 0, false);
>             ESP_LOGW(TAG, "датчик не відповідає (%d поспіль): %s",
>                      pomylok_pospil, esp_err_to_name(err));
>             // деградуємо, а не перезавантажуємось (розділ 32)
>         }
>         ESP_LOGD(TAG, "вільно RAM: %lu, мінімум: %lu",
>                  esp_get_free_heap_size(), esp_get_minimum_free_heap_size());
>         vTaskDelay(pdMS_TO_TICKS(60000));
>     }
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-062 sha:461edfca src:manual/59-proj-monitor.md:234 klas:F -->
### T-59-062 · kod-ryadok · рядок 234

**Книга каже, дослівно:**

> dodaty(t, h, p, true);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-063 sha:9e8becce src:manual/59-proj-monitor.md:235 klas:F -->
### T-59-063 · kod-ryadok · рядок 235

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "%.2f °C, %.1f %%, %.1f гПа", t, h, p);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-064 sha:29f9a0e7 src:manual/59-proj-monitor.md:238 klas:F -->
### T-59-064 · kod-ryadok · рядок 238

**Книга каже, дослівно:**

> dodaty(0, 0, 0, false);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-065 sha:b5ca5c99 src:manual/59-proj-monitor.md:244 klas:F -->
### T-59-065 · kod-ryadok · рядок 244

**Книга каже, дослівно:**

> esp_get_free_heap_size(), esp_get_minimum_free_heap_size());

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-066 sha:d4678ca1 src:manual/59-proj-monitor.md:245 klas:F -->
### T-59-066 · kod-ryadok · рядок 245

**Книга каже, дослівно:**

> vTaskDelay(pdMS_TO_TICKS(60000));

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-067 sha:7f8d2007 src:manual/59-proj-monitor.md:250 klas:F -->
### T-59-067 · proza · рядок 250

**Книга каже, дослівно:**

> Датчик, що замовк, не зупиняє пристрій: записується позначка про збій, і робота триває.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-068 sha:2ab58c0c src:manual/59-proj-monitor.md:250 klas:F -->
### T-59-068 · proza · рядок 250

**Книга каже, дослівно:**

> Веб-інтерфейс покаже, що дані застаріли.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-069 sha:4b754f95 src:manual/59-proj-monitor.md:255 klas:F -->
### T-59-069 · kod · рядок 255

**Книга каже, дослівно:**

> ```c
> static esp_err_t json_handler(httpd_req_t *req) {
>     char *buf = malloc(16384);
>     if (!buf) return httpd_resp_send_500(req);
> 
>     xSemaphoreTake(mutex, portMAX_DELAY);
>     int n = snprintf(buf, 16384, "{\"zapysiv\":%u,\"dani\":[", kilkist);
>     size_t start = (kilkist == ISTORIYA) ? idx : 0;
>     bool pershyy = true;                       // ← не «i == 0», див. нижче
>     for (size_t i = 0; i < kilkist && n < 16000; i++) {
>         zapys_t *z = &istoriya[(start + i) % ISTORIYA];
>         if (!z->valid) continue;
>         n += snprintf(buf + n, 16384 - n,
>                       "%s{\"t\":%lld,\"temp\":%.2f,\"hum\":%.1f,\"pres\":%.1f}",
>                       pershyy ? "" : ",",
>                       z->chas / 1000000, z->temp, z->hum, z->pres);
>         pershyy = false;
>     }
>     xSemaphoreGive(mutex);
>     snprintf(buf + n, 16384 - n, "]}");
> 
>     httpd_resp_set_type(req, "application/json");
>     esp_err_t r = httpd_resp_sendstr(req, buf);
>     free(buf);
>     return r;
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-070 sha:9e097e90 src:manual/59-proj-monitor.md:258 klas:F -->
### T-59-070 · kod-ryadok · рядок 258

**Книга каже, дослівно:**

> if (!buf) return httpd_resp_send_500(req);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-071 sha:da52f140 src:manual/59-proj-monitor.md:260 klas:F -->
### T-59-071 · kod-ryadok · рядок 260

**Книга каже, дослівно:**

> xSemaphoreTake(mutex, portMAX_DELAY);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-072 sha:05942241 src:manual/59-proj-monitor.md:273 klas:F -->
### T-59-072 · kod-ryadok · рядок 273

**Книга каже, дослівно:**

> xSemaphoreGive(mutex);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-073 sha:aa40708d src:manual/59-proj-monitor.md:274 klas:F -->
### T-59-073 · kod-ryadok · рядок 274

**Книга каже, дослівно:**

> snprintf(buf + n, 16384 - n, "]}");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-074 sha:1305725a src:manual/59-proj-monitor.md:276 klas:F -->
### T-59-074 · kod-ryadok · рядок 276

**Книга каже, дослівно:**

> httpd_resp_set_type(req, "application/json");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-075 sha:780361e1 src:manual/59-proj-monitor.md:278 klas:F -->
### T-59-075 · kod-ryadok · рядок 278

**Книга каже, дослівно:**

> free(buf);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-076 sha:87adb72b src:manual/59-proj-monitor.md:284 klas:F -->
### T-59-076 · proza · рядок 284

**Книга каже, дослівно:**

> Окремий прапорець `pershyy` замість перевірки `i == 0` — не педантизм.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-077 sha:d11cc6fe src:manual/59-proj-monitor.md:284 klas:F -->
### T-59-077 · proza · рядок 284

**Книга каже, дослівно:**

> Записи зі збоєм пропускаються через `continue`, тож індекс циклу і номер **виведеного** елемента розходяться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-078 sha:02b440af src:manual/59-proj-monitor.md:284 klas:F -->
### T-59-078 · proza · рядок 284

**Книга каже, дослівно:**

> Варіант `i ? "," : ""` при першому ж збійному запису на початку історії поставить кому перед першим елементом, і JSON стане несинтаксичним: `"dani":[,{…}]`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-079 sha:0fa06472 src:manual/59-proj-monitor.md:290 klas:F -->
### T-59-079 · proza · рядок 290

**Книга каже, дослівно:**

> Ламається це рівно тоді, коли датчик відмовив, — тобто саме тоді, коли на графік дивляться.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-080 sha:046ce956 src:manual/59-proj-monitor.md:290 klas:F -->
### T-59-080 · proza · рядок 290

**Книга каже, дослівно:**

> Це типова форма помилки в цій книзі: код правильний для щасливого шляху й невірний для того, заради якого писався.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-081 sha:8e1c5456 src:manual/59-proj-monitor.md:296 klas:F -->
### T-59-081 · proza · рядок 296

**Книга каже, дослівно:**

> Буфер тут виділяється з купи й одразу звільняється — це **не** цикл виділень, а разова операція на запит.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-082 sha:daa45c95 src:manual/59-proj-monitor.md:296 klas:F -->
### T-59-082 · proza · рядок 296

**Книга каже, дослівно:**

> Різниця з правилом розділу 30 у тому, що частота низька й розмір фіксований.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-083 sha:ffa66d5d src:manual/59-proj-monitor.md:300 klas:F -->
### T-59-083 · proza · рядок 300

**Книга каже, дослівно:**

> Уважніше треба з іншим: обробник виконується в задачі веб-сервера з обмеженим стеком.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-084 sha:99584848 src:manual/59-proj-monitor.md:300 klas:F -->
### T-59-084 · proza · рядок 300

**Книга каже, дослівно:**

> Тому 16 КБ беруться з купи, а не оголошуються як локальний масив — інакше стек переповниться (розділ 30).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-085 sha:0df2fce9 src:manual/59-proj-monitor.md:307 klas:F -->
### T-59-085 · kod · рядок 307

**Книга каже, дослівно:**

> ```c
> void app_main(void) {
>     ESP_LOGI(TAG, "старт, причина скидання: %d", esp_reset_reason());
> 
>     esp_err_t err = nvs_flash_init();
>     if (err == ESP_ERR_NVS_NO_FREE_PAGES || err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
>         ESP_ERROR_CHECK(nvs_flash_erase());
>         err = nvs_flash_init();
>     }
>     ESP_ERROR_CHECK(err);
> 
>     mutex = xSemaphoreCreateMutex();
> 
>     i2c_master_bus_config_t bus_cfg = {
>         .i2c_port = I2C_NUM_0,
>         .sda_io_num = GPIO_NUM_21,
>         .scl_io_num = GPIO_NUM_22,
>         .clk_source = I2C_CLK_SRC_DEFAULT,
>         .glitch_ignore_cnt = 7,
>     };
>     i2c_master_bus_handle_t bus;
>     ESP_ERROR_CHECK(i2c_new_master_bus(&bus_cfg, &bus));
> 
>     if (bme_init(bus) != ESP_OK) {
>         ESP_LOGE(TAG, "датчик не знайдено — працюємо без нього");
>         // не ESP_ERROR_CHECK: веб-інтерфейс має піднятися й показати проблему
>     }
> 
>     wifi_start();                 // під'єднання з повторами, розділ 39
>     mdns_init();
>     mdns_hostname_set("teplytsia");
>     mdns_service_add(NULL, "_http", "_tcp", 80, NULL, 0);
> 
>     web_start();
>     xTaskCreate(task_vymir, "vymir", 4096, NULL, 5, NULL);
> }
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-086 sha:f018579e src:manual/59-proj-monitor.md:309 klas:F -->
### T-59-086 · kod-ryadok · рядок 309

**Книга каже, дослівно:**

> ESP_LOGI(TAG, "старт, причина скидання: %d", esp_reset_reason());

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-087 sha:f3349b99 src:manual/59-proj-monitor.md:313 klas:F -->
### T-59-087 · kod-ryadok · рядок 313

**Книга каже, дослівно:**

> ESP_ERROR_CHECK(nvs_flash_erase());

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-088 sha:601ab80f src:manual/59-proj-monitor.md:316 klas:F -->
### T-59-088 · kod-ryadok · рядок 316

**Книга каже, дослівно:**

> ESP_ERROR_CHECK(err);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-089 sha:8137e868 src:manual/59-proj-monitor.md:321 klas:F -->
### T-59-089 · kod-ryadok · рядок 321

**Книга каже, дослівно:**

> .i2c_port = I2C_NUM_0,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-090 sha:b23a13d7 src:manual/59-proj-monitor.md:322 klas:F -->
### T-59-090 · kod-ryadok · рядок 322

**Книга каже, дослівно:**

> .sda_io_num = GPIO_NUM_21,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-091 sha:1599c26e src:manual/59-proj-monitor.md:323 klas:F -->
### T-59-091 · kod-ryadok · рядок 323

**Книга каже, дослівно:**

> .scl_io_num = GPIO_NUM_22,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-092 sha:ad69c01f src:manual/59-proj-monitor.md:324 klas:F -->
### T-59-092 · kod-ryadok · рядок 324

**Книга каже, дослівно:**

> .clk_source = I2C_CLK_SRC_DEFAULT,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-093 sha:be777622 src:manual/59-proj-monitor.md:325 klas:F -->
### T-59-093 · kod-ryadok · рядок 325

**Книга каже, дослівно:**

> .glitch_ignore_cnt = 7,

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-094 sha:6abf9538 src:manual/59-proj-monitor.md:328 klas:F -->
### T-59-094 · kod-ryadok · рядок 328

**Книга каже, дослівно:**

> ESP_ERROR_CHECK(i2c_new_master_bus(&bus_cfg, &bus));

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-095 sha:ea63146b src:manual/59-proj-monitor.md:331 klas:F -->
### T-59-095 · kod-ryadok · рядок 331

**Книга каже, дослівно:**

> ESP_LOGE(TAG, "датчик не знайдено — працюємо без нього");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-096 sha:f15667d5 src:manual/59-proj-monitor.md:336 klas:F -->
### T-59-096 · kod-ryadok · рядок 336

**Книга каже, дослівно:**

> mdns_init();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-097 sha:cb6701a7 src:manual/59-proj-monitor.md:337 klas:F -->
### T-59-097 · kod-ryadok · рядок 337

**Книга каже, дослівно:**

> mdns_hostname_set("teplytsia");

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-098 sha:1e052b00 src:manual/59-proj-monitor.md:338 klas:F -->
### T-59-098 · kod-ryadok · рядок 338

**Книга каже, дослівно:**

> mdns_service_add(NULL, "_http", "_tcp", 80, NULL, 0);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-099 sha:faf13c15 src:manual/59-proj-monitor.md:340 klas:F -->
### T-59-099 · kod-ryadok · рядок 340

**Книга каже, дослівно:**

> web_start();

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-100 sha:59d6968b src:manual/59-proj-monitor.md:341 klas:F -->
### T-59-100 · kod-ryadok · рядок 341

**Книга каже, дослівно:**

> xTaskCreate(task_vymir, "vymir", 4096, NULL, 5, NULL);

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-101 sha:c136ab2b src:manual/59-proj-monitor.md:346 klas:F -->
### T-59-101 · proza · рядок 346

**Книга каже, дослівно:**

> `ESP_ERROR_CHECK` тут стоїть лише навколо NVS і створення шини — того, без чого пристрій не має сенсу.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-102 sha:30cbfc2f src:manual/59-proj-monitor.md:349 klas:F -->
### T-59-102 · proza · рядок 349

**Книга каже, дослівно:**

> Навколо ініціалізації датчика його **немає** свідомо: несправний датчик не повинен перетворювати пристрій на цеглинку.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-103 sha:2351e0dd src:manual/59-proj-monitor.md:349 klas:F -->
### T-59-103 · proza · рядок 349

**Книга каже, дослівно:**

> Веб-інтерфейс має піднятися й показати, що датчик мовчить (розділ 32).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-104 sha:366e3229 src:manual/59-proj-monitor.md:356 klas:F -->
### T-59-104 · kod · рядок 356

**Книга каже, дослівно:**

> ```
> idf.py set-target esp32s3
> idf.py menuconfig          # Wi-Fi, розбивка флешу з OTA (розділ 18)
> idf.py build
> idf.py -p /dev/ttyUSB0 flash monitor
> ```

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-105 sha:6aa9cf42 src:manual/59-proj-monitor.md:357 klas:F -->
### T-59-105 · kod-ryadok · рядок 357

**Книга каже, дослівно:**

> idf.py set-target esp32s3

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-106 sha:4f160d06 src:manual/59-proj-monitor.md:358 klas:F -->
### T-59-106 · kod-ryadok · рядок 358

**Книга каже, дослівно:**

> idf.py menuconfig          # Wi-Fi, розбивка флешу з OTA (розділ 18)

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-107 sha:343d9bab src:manual/59-proj-monitor.md:359 klas:F -->
### T-59-107 · kod-ryadok · рядок 359

**Книга каже, дослівно:**

> idf.py build

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-108 sha:e801663f src:manual/59-proj-monitor.md:360 klas:F -->
### T-59-108 · kod-ryadok · рядок 360

**Книга каже, дослівно:**

> idf.py -p /dev/ttyUSB0 flash monitor

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-109 sha:b3a83074 src:manual/59-proj-monitor.md:365 klas:F -->
### T-59-109 · proza · рядок 365

**Книга каже, дослівно:**

> У лозі — `BME280 знайдено і налаштовано`.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-110 sha:fda6a9fd src:manual/59-proj-monitor.md:365 klas:F -->
### T-59-110 · proza · рядок 365

**Книга каже, дослівно:**

> Немає — сканер I²C (розділ 35). 2.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-111 sha:98a85158 src:manual/59-proj-monitor.md:365 klas:F -->
### T-59-111 · proza · рядок 365

**Книга каже, дослівно:**

> Перше вимірювання з осмисленими значеннями. 3.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-112 sha:98b2d431 src:manual/59-proj-monitor.md:365 klas:F -->
### T-59-112 · proza · рядок 365

**Книга каже, дослівно:**

> `teplytsia.local` відкривається у браузері. 4.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-113 sha:3ec3a7c7 src:manual/59-proj-monitor.md:365 klas:F -->
### T-59-113 · proza · рядок 365

**Книга каже, дослівно:**

> Від'єднати датчик на ходу: пристрій лишається живим, у лозі попередження, веб показує застарілі дані. 5.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-114 sha:f2cb8e81 src:manual/59-proj-monitor.md:365 klas:F -->
### T-59-114 · proza · рядок 365

**Книга каже, дослівно:**

> Вимкнути роутер: вимірювання тривають, після відновлення веб знову доступний. 6.

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-115 sha:cab8cb32 src:manual/59-proj-monitor.md:365 klas:F -->
### T-59-115 · proza · рядок 365

**Книга каже, дослівно:**

> Доба безперервної роботи: мінімум вільної пам'яті не зменшується (розділ 58).

**Доказ**

- **Клас:** F — не звірено

---

<!-- fc id:T-59-116 sha:26ecb42f src:manual/59-proj-monitor.md:378 klas:F -->
### T-59-116 · proza · рядок 378

**Книга каже, дослівно:**

> - **MQTT** замість або разом із веб-інтерфейсом (розділ 40); - **другий датчик** — DS18B20 на вулиці (розділ 37); - **OTA** — розбивку вже закладено (розділ 19); - **e-paper** для показу на місці (розділ 46); - **автономність**: перехід на deep sleep і ESP-NOW перетворює це на проєкт 60.

**Доказ**

- **Клас:** F — не звірено

---
