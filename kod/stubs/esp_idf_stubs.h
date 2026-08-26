/* Згенеровано tools/kod-stubs.py. Руками не правити. */
#ifndef ESP_IDF_STUBS_H
#define ESP_IDF_STUBS_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/* Сокети — справжні системні заголовки: книга вживає
   struct sockaddr_in і його поля, і перевіряти їх треба
   проти POSIX, а не проти заглушки. */
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

typedef int esp_err_t;

typedef void *BaseType_t;
typedef void *EventGroupHandle_t;
typedef void *QueueHandle_t;
typedef void *SemaphoreHandle_t;
typedef void *TimerHandle_t;
typedef void *UBaseType_t;
typedef void *adc_cali_handle_t;
typedef void *adc_oneshot_unit_handle_t;
typedef void *esp_mqtt_client_handle_t;
typedef void *esp_now_send_status_t;
typedef void *esp_timer_handle_t;
typedef void *httpd_handle_t;
typedef void *i2c_master_bus_handle_t;
typedef void *i2c_master_dev_handle_t;
typedef void *led_strip_handle_t;
typedef void *spi_device_handle_t;

typedef struct {
    int unit_id;
    int chan;
    int atten;
    int bitwidth;
} adc_cali_curve_fitting_config_t;
typedef struct {
    int atten;
    int bitwidth;
} adc_oneshot_chan_cfg_t;
typedef struct {
    int unit_id;
    int clk_src;
    int ulp_mode;
    int atten;
    int bitwidth;
} adc_oneshot_unit_init_cfg_t;
typedef struct {
    const char *url;
    const char *host;
    int port;
    const char *path;
    const char *cert_pem;
    int method;
    int timeout_ms;
    esp_err_t (*event_handler)(void *evt);
    int transport_type;
    int buffer_size;
    int keep_alive_enable;
} esp_http_client_config_t;
typedef struct {
    const esp_http_client_config_t *http_config;
    esp_err_t (*http_client_init_cb)(void *);
    int bulk_flash_erase;
    int partial_http_download;
    int max_http_request_size;
} esp_https_ota_config_t;
typedef struct {
    struct { struct { const char *uri; const char *hostname; int port; } address; struct { struct { const char *data; size_t len; } certificate; } verification; } broker;
    struct { const char *username; const char *client_id; struct { const char *password; } authentication; } credentials;
    struct { int keepalive; int disable_clean_session; struct { const char *topic; const char *msg; int qos; int retain; } last_will; } session;
    struct { int reconnect_timeout_ms; int network_timeout_ms; } network;
} esp_mqtt_client_config_t;
typedef struct {
    unsigned char peer_addr[6];
    unsigned char lmk[16];
    unsigned char channel;
    int ifidx;
    int encrypt;
    void *priv;
} esp_now_peer_info_t;
typedef struct {
    unsigned char *src_addr;
    unsigned char *des_addr;
    void *rx_ctrl;
} esp_now_recv_info_t;
typedef struct {
    unsigned char des_addr[6];
    int tx_status;
} esp_now_send_info_t;
typedef struct {
    void (*callback)(void *);
    void *arg;
    int dispatch_method;
    const char *name;
    int skip_unhandled_events;
} esp_timer_create_args_t;
typedef struct {
    unsigned long long pin_bit_mask;
    int mode;
    int pull_up_en;
    int pull_down_en;
    int intr_type;
    int hys_ctrl_mode;
} gpio_config_t;
typedef struct {
    unsigned task_priority;
    size_t stack_size;
    int core_id;
    unsigned short server_port;
    unsigned short ctrl_port;
    unsigned short max_open_sockets;
    unsigned short max_uri_handlers;
    int lru_purge_enable;
    unsigned recv_wait_timeout;
    unsigned send_wait_timeout;
    void *global_user_ctx;
} httpd_config_t;
typedef struct {
    void *handle;
    int method;
    char uri[512];
    size_t content_len;
    void *aux;
    void *user_ctx;
    void *sess_ctx;
} httpd_req_t;
typedef struct {
    const char *uri;
    int method;
    esp_err_t (*handler)(httpd_req_t *r);
    void *user_ctx;
} httpd_uri_t;
typedef struct {
    int dev_addr_length;
    unsigned device_address;
    unsigned scl_speed_hz;
    unsigned scl_wait_us;
    struct { int disable_ack_check; } flags;
} i2c_device_config_t;
typedef struct {
    int i2c_port;
    int sda_io_num;
    int scl_io_num;
    int clk_source;
    int glitch_ignore_cnt;
    int intr_priority;
    int trans_queue_depth;
    struct { int enable_internal_pullup; int allow_pd; } flags;
} i2c_master_bus_config_t;
typedef struct {
    int strip_gpio_num;
    unsigned max_leds;
    int led_model;
    struct { unsigned r; unsigned g; unsigned b; unsigned w; } color_component_format;
    struct { unsigned invert_out; } flags;
} led_strip_config_t;
typedef struct {
    int clk_src;
    unsigned resolution_hz;
    size_t mem_block_symbols;
    struct { unsigned with_dma; } flags;
} led_strip_rmt_config_t;
typedef struct {
    int gpio_num;
    int speed_mode;
    int channel;
    int intr_type;
    int timer_sel;
    unsigned duty;
    int hpoint;
    int sleep_mode;
    struct { unsigned output_invert; } flags;
} ledc_channel_config_t;
typedef struct {
    int speed_mode;
    int duty_resolution;
    int timer_num;
    unsigned freq_hz;
    int clk_cfg;
    int deconfigure;
} ledc_timer_config_t;
typedef struct {
    int mosi_io_num;
    int miso_io_num;
    int sclk_io_num;
    int quadwp_io_num;
    int quadhd_io_num;
    int max_transfer_sz;
    unsigned flags;
    int intr_flags;
} spi_bus_config_t;
typedef struct {
    unsigned char command_bits;
    unsigned char address_bits;
    unsigned char dummy_bits;
    unsigned char mode;
    int clock_source;
    int duty_cycle_pos;
    int cs_ena_pretrans;
    int cs_ena_posttrans;
    int clock_speed_hz;
    int input_delay_ns;
    int spics_io_num;
    unsigned flags;
    int queue_size;
    void (*pre_cb)(void *);
    void (*post_cb)(void *);
} spi_device_interface_config_t;
typedef struct {
    unsigned flags;
    unsigned short cmd;
    unsigned long long addr;
    size_t length;
    size_t rxlength;
    void *user;
    const void *tx_buffer;
    void *rx_buffer;
} spi_transaction_t;
typedef struct {
    unsigned acceptance_code;
    unsigned acceptance_mask;
    int single_filter;
} twai_filter_config_t;
typedef struct {
    int mode;
    int tx_io;
    int rx_io;
    int clkout_io;
    int bus_off_io;
    unsigned tx_queue_len;
    unsigned rx_queue_len;
    unsigned alerts_enabled;
    unsigned clkout_divider;
    int intr_flags;
} twai_general_config_t;
typedef struct {
    unsigned flags;
    unsigned identifier;
    unsigned data_length_code;
    unsigned char data[8];
    unsigned extd;
    unsigned rtr;
    unsigned ss;
    unsigned self;
    unsigned dlc_non_comp;
} twai_message_t;
typedef struct {
    int state;
    unsigned msgs_to_tx;
    unsigned msgs_to_rx;
    unsigned tx_error_counter;
    unsigned rx_error_counter;
    unsigned tx_failed_count;
    unsigned rx_missed_count;
    unsigned arb_lost_count;
    unsigned bus_error_count;
} twai_status_info_t;
typedef struct {
    unsigned brp;
    unsigned char tseg_1;
    unsigned char tseg_2;
    unsigned char sjw;
    int triple_sampling;
} twai_timing_config_t;
typedef struct {
    int baud_rate;
    int data_bits;
    int parity;
    int stop_bits;
    int flow_ctrl;
    unsigned char rx_flow_ctrl_thresh;
    int source_clk;
} uart_config_t;
typedef struct {
    unsigned char bssid[6];
    unsigned char ssid[33];
    unsigned char primary;
    int second;
    signed char rssi;
    int authmode;
    int pairwise_cipher;
    int group_cipher;
} wifi_ap_record_t;
typedef struct {
    struct { unsigned char ssid[32]; unsigned char password[64]; unsigned char scan_method; unsigned char bssid_set; unsigned char bssid[6]; unsigned char channel; struct { signed char rssi; int authmode; } threshold; } sta; struct { unsigned char ssid[32]; unsigned char password[64]; unsigned char ssid_len; unsigned char channel; int authmode; unsigned char ssid_hidden; unsigned char max_connection; } ap;
} wifi_config_t;
typedef struct {
    int static_rx_buf_num;
    int dynamic_rx_buf_num;
    int tx_buf_type;
    int static_tx_buf_num;
    int dynamic_tx_buf_num;
    int nvs_enable;
} wifi_init_config_t;

/* Логування і перевірки — макроси зі змінним числом аргументів. */
#define ESP_LOGI(tag, ...) ((void)(tag))
#define ESP_LOGW(tag, ...) ((void)(tag))
#define ESP_LOGE(tag, ...) ((void)(tag))
#define ESP_LOGD(tag, ...) ((void)(tag))
#define ESP_LOGV(tag, ...) ((void)(tag))
#define ESP_ERROR_CHECK(x) ((void)(x))
#define ESP_ERROR_CHECK_WITHOUT_ABORT(x) ((void)(x))
#define ESP_RETURN_ON_ERROR(x, tag, ...) ((void)(x))
#define ESP_GOTO_ON_ERROR(x, l, tag, ...) ((void)(x))
#define IRAM_ATTR
#define RTC_DATA_ATTR
#define DRAM_ATTR
#define pdMS_TO_TICKS(ms) ((int)(ms))
#define portTICK_PERIOD_MS 1

/* Функції ESP-IDF та FreeRTOS, що вживає книга. */
esp_err_t HTTPD_DEFAULT_CONFIG();
esp_err_t TWAI_FILTER_CONFIG_ACCEPT_ALL();
esp_err_t TWAI_GENERAL_CONFIG_DEFAULT();
esp_err_t TWAI_TIMING_CONFIG_500KBITS();
esp_err_t WIFI_INIT_CONFIG_DEFAULT();
esp_err_t accept();
esp_err_t adc_cali_create_scheme_curve_fitting();
esp_err_t adc_cali_raw_to_voltage();
esp_err_t adc_oneshot_config_channel();
esp_err_t adc_oneshot_new_unit();
esp_err_t adc_oneshot_read();
esp_err_t bind();
esp_err_t close();
esp_err_t do_work();
esp_err_t ds18b20_read();
esp_err_t esp_deep_sleep_start();
const char * esp_err_to_name();
uint32_t esp_get_free_heap_size();
uint32_t esp_get_minimum_free_heap_size();
esp_err_t esp_https_ota();
esp_err_t esp_log_level_set();
esp_err_t esp_mqtt_client_init();
esp_err_t esp_mqtt_client_publish();
esp_err_t esp_mqtt_client_register_event();
esp_err_t esp_mqtt_client_start();
esp_err_t esp_now_add_peer();
esp_err_t esp_now_init();
esp_err_t esp_now_register_recv_cb();
esp_err_t esp_now_register_send_cb();
esp_err_t esp_now_send();
esp_err_t esp_now_set_pmk();
esp_err_t esp_ota_mark_app_valid_cancel_rollback();
int esp_reset_reason();
esp_err_t esp_restart();
esp_err_t esp_sleep_enable_timer_wakeup();
esp_err_t esp_sleep_get_wakeup_cause();
esp_err_t esp_sntp_init();
esp_err_t esp_sntp_setoperatingmode();
esp_err_t esp_sntp_setservername();
esp_err_t esp_task_wdt_add();
esp_err_t esp_task_wdt_reset();
esp_err_t esp_timer_create();
int64_t esp_timer_get_time();
esp_err_t esp_timer_start_once();
esp_err_t esp_timer_start_periodic();
esp_err_t esp_wifi_connect();
esp_err_t esp_wifi_init();
esp_err_t esp_wifi_set_config();
esp_err_t esp_wifi_set_mode();
esp_err_t esp_wifi_sta_get_ap_info();
esp_err_t esp_wifi_start();
esp_err_t fileno();
esp_err_t fsync();
esp_err_t gpio_config();
esp_err_t gpio_dump_io_configuration();
esp_err_t gpio_get_level();
esp_err_t gpio_install_isr_service();
esp_err_t gpio_isr_handler_add();
esp_err_t gpio_set_level();
size_t heap_caps_get_free_size();
size_t heap_caps_get_largest_free_block();
void * heap_caps_malloc();
esp_err_t htonl();
esp_err_t htons();
esp_err_t httpd_register_uri_handler();
esp_err_t httpd_req_recv();
esp_err_t httpd_resp_send_500();
esp_err_t httpd_resp_sendstr();
esp_err_t httpd_resp_set_type();
esp_err_t httpd_start();
esp_err_t i2c_master_bus_add_device();
esp_err_t i2c_master_probe();
esp_err_t i2c_master_transmit();
esp_err_t i2c_master_transmit_receive();
esp_err_t i2c_new_master_bus();
esp_err_t led_strip_new_rmt_device();
esp_err_t led_strip_refresh();
esp_err_t led_strip_set_pixel();
esp_err_t ledc_channel_config();
esp_err_t ledc_timer_config();
esp_err_t listen();
esp_err_t mdns_hostname_set();
esp_err_t mdns_init();
esp_err_t mdns_instance_name_set();
esp_err_t mdns_service_add();
esp_err_t nasos_keruvaty();
const char * nazva();
esp_err_t nvs_flash_erase();
esp_err_t nvs_flash_init();
esp_err_t nvs_read_key();
esp_err_t obrobyty();
esp_err_t obsluhovuvaty();
esp_err_t onovyty_indykaciyu();
esp_err_t operatsiya();
esp_err_t portYIELD_FROM_ISR();
esp_err_t povidomyty_pro_vtratu();
esp_err_t radio_init();
esp_err_t read_sensor();
esp_err_t riven_ye();
esp_err_t robota();
esp_err_t rtc_chas();
esp_err_t sd_mount();
esp_err_t sd_unmount();
esp_err_t setenv();
esp_err_t skynuty_bufer();
esp_err_t socket();
esp_err_t spi_bus_add_device();
esp_err_t spi_bus_initialize();
esp_err_t spi_device_transmit();
esp_err_t twai_driver_install();
esp_err_t twai_get_status_info();
esp_err_t twai_receive();
esp_err_t twai_start();
esp_err_t twai_transmit();
esp_err_t tzset();
esp_err_t uart_driver_install();
esp_err_t uart_param_config();
esp_err_t uart_read_bytes();
esp_err_t uart_set_pin();
esp_err_t uart_wait_tx_done();
esp_err_t uart_write_bytes();
uint32_t uxTaskGetStackHighWaterMark();
esp_err_t vTaskDelay();
esp_err_t vidaty_dali();
esp_err_t web_start();
esp_err_t wifi_start();
void * xEventGroupCreate();
uint32_t xEventGroupWaitBits();
void * xQueueCreate();
esp_err_t xQueueReceive();
esp_err_t xQueueReset();
esp_err_t xQueueSend();
esp_err_t xQueueSendFromISR();
void * xSemaphoreCreateMutex();
esp_err_t xSemaphoreGive();
esp_err_t xSemaphoreTake();
esp_err_t xTaskCreate();
esp_err_t xTaskCreatePinnedToCore();
void * xTimerCreate();
esp_err_t xTimerStart();
esp_err_t zmiryaty();

/* Символьні константи. Значення довільні: перевіряється
   існування імені, а не число за ним. */
/* Макроси ESP-IDF, що вживаються з дужками. */
#define HTTPD_DEFAULT_CONFIG(...) (0)
#define TWAI_FILTER_CONFIG_ACCEPT_ALL(...) (0)
#define TWAI_GENERAL_CONFIG_DEFAULT(...) (0)
#define TWAI_TIMING_CONFIG_500KBITS(...) (0)
#define WIFI_INIT_CONFIG_DEFAULT(...) (0)
#define portYIELD_FROM_ISR(...) (0)

enum {
    STUB_ADC = 0,
    STUB_ADC1_6 = 1,
    STUB_ADC_ATTEN_DB_12 = 2,
    STUB_ADC_BITWIDTH_DEFAULT = 3,
    STUB_ADC_CHANNEL = 4,
    STUB_ADC_CHANNEL_3 = 5,
    STUB_ADC_CHANNEL_6 = 6,
    STUB_ADC_UNIT_1 = 7,
    STUB_ADDR = 8,
    STUB_AF_INET = 9,
    STUB_BIT0 = 10,
    STUB_BIT1 = 11,
    STUB_BME = 12,
    STUB_BME280 = 13,
    STUB_BUFER_ROZMIR = 14,
    STUB_CAN = 15,
    STUB_EET = 16,
    STUB_ESP = 17,
    STUB_ESP32 = 18,
    STUB_ESP_ERR_INVALID_STATE = 19,
    STUB_ESP_ERR_NOT_FOUND = 20,
    STUB_ESP_ERR_NO_MEM = 21,
    STUB_ESP_ERR_NVS_NEW_VERSION_FOUND = 22,
    STUB_ESP_ERR_NVS_NO_FREE_PAGES = 23,
    STUB_ESP_EVENT_ANY_ID = 24,
    STUB_ESP_FAIL = 25,
    STUB_ESP_LOG_DEBUG = 26,
    STUB_ESP_LOG_INFO = 27,
    STUB_ESP_LOG_WARN = 28,
    STUB_ESP_NOW_SEND_SUCCESS = 29,
    STUB_ESP_OK = 30,
    STUB_ESP_SNTP_OPMODE_POLL = 31,
    STUB_FILE = 32,
    STUB_GPIO3 = 33,
    STUB_GPIO34 = 34,
    STUB_GPIO_INTR_DISABLE = 35,
    STUB_GPIO_INTR_NEGEDGE = 36,
    STUB_GPIO_MODE_INPUT = 37,
    STUB_GPIO_MODE_OUTPUT = 38,
    STUB_GPIO_NUM_0 = 39,
    STUB_GPIO_NUM_1 = 40,
    STUB_GPIO_NUM_10 = 41,
    STUB_GPIO_NUM_13 = 42,
    STUB_GPIO_NUM_16 = 43,
    STUB_GPIO_NUM_17 = 44,
    STUB_GPIO_NUM_18 = 45,
    STUB_GPIO_NUM_19 = 46,
    STUB_GPIO_NUM_2 = 47,
    STUB_GPIO_NUM_21 = 48,
    STUB_GPIO_NUM_22 = 49,
    STUB_GPIO_NUM_23 = 50,
    STUB_GPIO_NUM_4 = 51,
    STUB_GPIO_NUM_5 = 52,
    STUB_GPIO_NUM_6 = 53,
    STUB_GPIO_NUM_7 = 54,
    STUB_GPIO_NUM_8 = 55,
    STUB_GPIO_NUM_9 = 56,
    STUB_GPIO_PULLDOWN_DISABLE = 57,
    STUB_GPIO_PULLUP_DISABLE = 58,
    STUB_GPIO_PULLUP_ENABLE = 59,
    STUB_HTTP_GET = 60,
    STUB_I2C_ADDR_BIT_LEN_7 = 61,
    STUB_I2C_CLK_SRC_DEFAULT = 62,
    STUB_I2C_NUM_0 = 63,
    STUB_IDLE = 64,
    STUB_INADDR_ANY = 65,
    STUB_IPPROTO_TCP = 66,
    STUB_IRAM_ATTR = 67,
    STUB_ISR = 68,
    STUB_KANAL = 69,
    STUB_LEDC_CHANNEL_0 = 70,
    STUB_LEDC_LOW_SPEED_MODE = 71,
    STUB_LEDC_TIMER_0 = 72,
    STUB_LEDC_TIMER_13_BIT = 73,
    STUB_M10 = 74,
    STUB_MALLOC_CAP_8BIT = 75,
    STUB_MALLOC_CAP_DMA = 76,
    STUB_MALLOC_CAP_SPIRAM = 77,
    STUB_MAX_VUZLIV = 78,
    STUB_MOUNT = 79,
    STUB_MQTT = 80,
    STUB_NOMER_VUZLA = 81,
    STUB_NOW = 82,
    STUB_NVS = 83,
    STUB_OTA = 84,
    STUB_PIN_1WIRE = 85,
    STUB_PIN_CS_SD = 86,
    STUB_PIN_DE = 87,
    STUB_PIN_DILNYK_EN = 88,
    STUB_PIN_MISO = 89,
    STUB_PIN_MOSI = 90,
    STUB_PIN_SCK = 91,
    STUB_PIN_SCL = 92,
    STUB_PIN_SDA = 93,
    STUB_PIN_STOP = 94,
    STUB_PIN_ZHYVLENNYA_PERYFERIYI = 95,
    STUB_PORT = 96,
    STUB_PUMP = 97,
    STUB_RAM = 98,
    STUB_REG_CTRL = 99,
    STUB_REZHYM_RS485 = 100,
    STUB_RSSI = 101,
    STUB_RTC_DATA_ATTR = 102,
    STUB_SOCK_STREAM = 103,
    STUB_SPI2_HOST = 104,
    STUB_SPI_DMA_CH_AUTO = 105,
    STUB_STA = 106,
    STUB_TWAI_MODE_NORMAL = 107,
    STUB_UART = 108,
    STUB_UART_DATA_8_BITS = 109,
    STUB_UART_HW_FLOWCTRL_DISABLE = 110,
    STUB_UART_NUM_1 = 111,
    STUB_UART_PARITY_DISABLE = 112,
    STUB_UART_PIN_NO_CHANGE = 113,
    STUB_UART_PORT = 114,
    STUB_UART_SCLK_DEFAULT = 115,
    STUB_UART_STOP_BITS_1 = 116,
    STUB_WDT = 117,
    STUB_WIFI_AUTH_WPA2_PSK = 118,
    STUB_WIFI_IF_STA = 119,
    STUB_WIFI_MODE_STA = 120,
    STUB_pdFALSE = 121,
    STUB_pdTRUE = 122,
    STUB_portMAX_DELAY = 123,
};
#ifndef ADC
#define ADC STUB_ADC
#endif
#ifndef ADC1_6
#define ADC1_6 STUB_ADC1_6
#endif
#ifndef ADC_ATTEN_DB_12
#define ADC_ATTEN_DB_12 STUB_ADC_ATTEN_DB_12
#endif
#ifndef ADC_BITWIDTH_DEFAULT
#define ADC_BITWIDTH_DEFAULT STUB_ADC_BITWIDTH_DEFAULT
#endif
#ifndef ADC_CHANNEL
#define ADC_CHANNEL STUB_ADC_CHANNEL
#endif
#ifndef ADC_CHANNEL_3
#define ADC_CHANNEL_3 STUB_ADC_CHANNEL_3
#endif
#ifndef ADC_CHANNEL_6
#define ADC_CHANNEL_6 STUB_ADC_CHANNEL_6
#endif
#ifndef ADC_UNIT_1
#define ADC_UNIT_1 STUB_ADC_UNIT_1
#endif
#ifndef ADDR
#define ADDR STUB_ADDR
#endif
#ifndef AF_INET
#define AF_INET STUB_AF_INET
#endif
#ifndef BIT0
#define BIT0 STUB_BIT0
#endif
#ifndef BIT1
#define BIT1 STUB_BIT1
#endif
#ifndef BME
#define BME STUB_BME
#endif
#ifndef BME280
#define BME280 STUB_BME280
#endif
#ifndef BUFER_ROZMIR
#define BUFER_ROZMIR STUB_BUFER_ROZMIR
#endif
#ifndef CAN
#define CAN STUB_CAN
#endif
#ifndef EET
#define EET STUB_EET
#endif
#ifndef ESP
#define ESP STUB_ESP
#endif
#ifndef ESP32
#define ESP32 STUB_ESP32
#endif
#ifndef ESP_ERR_INVALID_STATE
#define ESP_ERR_INVALID_STATE STUB_ESP_ERR_INVALID_STATE
#endif
#ifndef ESP_ERR_NOT_FOUND
#define ESP_ERR_NOT_FOUND STUB_ESP_ERR_NOT_FOUND
#endif
#ifndef ESP_ERR_NO_MEM
#define ESP_ERR_NO_MEM STUB_ESP_ERR_NO_MEM
#endif
#ifndef ESP_ERR_NVS_NEW_VERSION_FOUND
#define ESP_ERR_NVS_NEW_VERSION_FOUND STUB_ESP_ERR_NVS_NEW_VERSION_FOUND
#endif
#ifndef ESP_ERR_NVS_NO_FREE_PAGES
#define ESP_ERR_NVS_NO_FREE_PAGES STUB_ESP_ERR_NVS_NO_FREE_PAGES
#endif
#ifndef ESP_EVENT_ANY_ID
#define ESP_EVENT_ANY_ID STUB_ESP_EVENT_ANY_ID
#endif
#ifndef ESP_FAIL
#define ESP_FAIL STUB_ESP_FAIL
#endif
#ifndef ESP_LOG_DEBUG
#define ESP_LOG_DEBUG STUB_ESP_LOG_DEBUG
#endif
#ifndef ESP_LOG_INFO
#define ESP_LOG_INFO STUB_ESP_LOG_INFO
#endif
#ifndef ESP_LOG_WARN
#define ESP_LOG_WARN STUB_ESP_LOG_WARN
#endif
#ifndef ESP_NOW_SEND_SUCCESS
#define ESP_NOW_SEND_SUCCESS STUB_ESP_NOW_SEND_SUCCESS
#endif
#ifndef ESP_OK
#define ESP_OK STUB_ESP_OK
#endif
#ifndef ESP_SNTP_OPMODE_POLL
#define ESP_SNTP_OPMODE_POLL STUB_ESP_SNTP_OPMODE_POLL
#endif
#ifndef FILE
#define FILE STUB_FILE
#endif
#ifndef GPIO3
#define GPIO3 STUB_GPIO3
#endif
#ifndef GPIO34
#define GPIO34 STUB_GPIO34
#endif
#ifndef GPIO_INTR_DISABLE
#define GPIO_INTR_DISABLE STUB_GPIO_INTR_DISABLE
#endif
#ifndef GPIO_INTR_NEGEDGE
#define GPIO_INTR_NEGEDGE STUB_GPIO_INTR_NEGEDGE
#endif
#ifndef GPIO_MODE_INPUT
#define GPIO_MODE_INPUT STUB_GPIO_MODE_INPUT
#endif
#ifndef GPIO_MODE_OUTPUT
#define GPIO_MODE_OUTPUT STUB_GPIO_MODE_OUTPUT
#endif
#ifndef GPIO_NUM_0
#define GPIO_NUM_0 STUB_GPIO_NUM_0
#endif
#ifndef GPIO_NUM_1
#define GPIO_NUM_1 STUB_GPIO_NUM_1
#endif
#ifndef GPIO_NUM_10
#define GPIO_NUM_10 STUB_GPIO_NUM_10
#endif
#ifndef GPIO_NUM_13
#define GPIO_NUM_13 STUB_GPIO_NUM_13
#endif
#ifndef GPIO_NUM_16
#define GPIO_NUM_16 STUB_GPIO_NUM_16
#endif
#ifndef GPIO_NUM_17
#define GPIO_NUM_17 STUB_GPIO_NUM_17
#endif
#ifndef GPIO_NUM_18
#define GPIO_NUM_18 STUB_GPIO_NUM_18
#endif
#ifndef GPIO_NUM_19
#define GPIO_NUM_19 STUB_GPIO_NUM_19
#endif
#ifndef GPIO_NUM_2
#define GPIO_NUM_2 STUB_GPIO_NUM_2
#endif
#ifndef GPIO_NUM_21
#define GPIO_NUM_21 STUB_GPIO_NUM_21
#endif
#ifndef GPIO_NUM_22
#define GPIO_NUM_22 STUB_GPIO_NUM_22
#endif
#ifndef GPIO_NUM_23
#define GPIO_NUM_23 STUB_GPIO_NUM_23
#endif
#ifndef GPIO_NUM_4
#define GPIO_NUM_4 STUB_GPIO_NUM_4
#endif
#ifndef GPIO_NUM_5
#define GPIO_NUM_5 STUB_GPIO_NUM_5
#endif
#ifndef GPIO_NUM_6
#define GPIO_NUM_6 STUB_GPIO_NUM_6
#endif
#ifndef GPIO_NUM_7
#define GPIO_NUM_7 STUB_GPIO_NUM_7
#endif
#ifndef GPIO_NUM_8
#define GPIO_NUM_8 STUB_GPIO_NUM_8
#endif
#ifndef GPIO_NUM_9
#define GPIO_NUM_9 STUB_GPIO_NUM_9
#endif
#ifndef GPIO_PULLDOWN_DISABLE
#define GPIO_PULLDOWN_DISABLE STUB_GPIO_PULLDOWN_DISABLE
#endif
#ifndef GPIO_PULLUP_DISABLE
#define GPIO_PULLUP_DISABLE STUB_GPIO_PULLUP_DISABLE
#endif
#ifndef GPIO_PULLUP_ENABLE
#define GPIO_PULLUP_ENABLE STUB_GPIO_PULLUP_ENABLE
#endif
#ifndef HTTP_GET
#define HTTP_GET STUB_HTTP_GET
#endif
#ifndef I2C_ADDR_BIT_LEN_7
#define I2C_ADDR_BIT_LEN_7 STUB_I2C_ADDR_BIT_LEN_7
#endif
#ifndef I2C_CLK_SRC_DEFAULT
#define I2C_CLK_SRC_DEFAULT STUB_I2C_CLK_SRC_DEFAULT
#endif
#ifndef I2C_NUM_0
#define I2C_NUM_0 STUB_I2C_NUM_0
#endif
#ifndef IDLE
#define IDLE STUB_IDLE
#endif
#ifndef INADDR_ANY
#define INADDR_ANY STUB_INADDR_ANY
#endif
#ifndef IPPROTO_TCP
#define IPPROTO_TCP STUB_IPPROTO_TCP
#endif
#ifndef IRAM_ATTR
#define IRAM_ATTR STUB_IRAM_ATTR
#endif
#ifndef ISR
#define ISR STUB_ISR
#endif
#ifndef KANAL
#define KANAL STUB_KANAL
#endif
#ifndef LEDC_CHANNEL_0
#define LEDC_CHANNEL_0 STUB_LEDC_CHANNEL_0
#endif
#ifndef LEDC_LOW_SPEED_MODE
#define LEDC_LOW_SPEED_MODE STUB_LEDC_LOW_SPEED_MODE
#endif
#ifndef LEDC_TIMER_0
#define LEDC_TIMER_0 STUB_LEDC_TIMER_0
#endif
#ifndef LEDC_TIMER_13_BIT
#define LEDC_TIMER_13_BIT STUB_LEDC_TIMER_13_BIT
#endif
#ifndef M10
#define M10 STUB_M10
#endif
#ifndef MALLOC_CAP_8BIT
#define MALLOC_CAP_8BIT STUB_MALLOC_CAP_8BIT
#endif
#ifndef MALLOC_CAP_DMA
#define MALLOC_CAP_DMA STUB_MALLOC_CAP_DMA
#endif
#ifndef MALLOC_CAP_SPIRAM
#define MALLOC_CAP_SPIRAM STUB_MALLOC_CAP_SPIRAM
#endif
#ifndef MAX_VUZLIV
#define MAX_VUZLIV STUB_MAX_VUZLIV
#endif
#ifndef MOUNT
#define MOUNT STUB_MOUNT
#endif
#ifndef MQTT
#define MQTT STUB_MQTT
#endif
#ifndef NOMER_VUZLA
#define NOMER_VUZLA STUB_NOMER_VUZLA
#endif
#ifndef NOW
#define NOW STUB_NOW
#endif
#ifndef NVS
#define NVS STUB_NVS
#endif
#ifndef OTA
#define OTA STUB_OTA
#endif
#ifndef PIN_1WIRE
#define PIN_1WIRE STUB_PIN_1WIRE
#endif
#ifndef PIN_CS_SD
#define PIN_CS_SD STUB_PIN_CS_SD
#endif
#ifndef PIN_DE
#define PIN_DE STUB_PIN_DE
#endif
#ifndef PIN_DILNYK_EN
#define PIN_DILNYK_EN STUB_PIN_DILNYK_EN
#endif
#ifndef PIN_MISO
#define PIN_MISO STUB_PIN_MISO
#endif
#ifndef PIN_MOSI
#define PIN_MOSI STUB_PIN_MOSI
#endif
#ifndef PIN_SCK
#define PIN_SCK STUB_PIN_SCK
#endif
#ifndef PIN_SCL
#define PIN_SCL STUB_PIN_SCL
#endif
#ifndef PIN_SDA
#define PIN_SDA STUB_PIN_SDA
#endif
#ifndef PIN_STOP
#define PIN_STOP STUB_PIN_STOP
#endif
#ifndef PIN_ZHYVLENNYA_PERYFERIYI
#define PIN_ZHYVLENNYA_PERYFERIYI STUB_PIN_ZHYVLENNYA_PERYFERIYI
#endif
#ifndef PORT
#define PORT STUB_PORT
#endif
#ifndef PUMP
#define PUMP STUB_PUMP
#endif
#ifndef RAM
#define RAM STUB_RAM
#endif
#ifndef REG_CTRL
#define REG_CTRL STUB_REG_CTRL
#endif
#ifndef REZHYM_RS485
#define REZHYM_RS485 STUB_REZHYM_RS485
#endif
#ifndef RSSI
#define RSSI STUB_RSSI
#endif
#ifndef RTC_DATA_ATTR
#define RTC_DATA_ATTR STUB_RTC_DATA_ATTR
#endif
#ifndef SOCK_STREAM
#define SOCK_STREAM STUB_SOCK_STREAM
#endif
#ifndef SPI2_HOST
#define SPI2_HOST STUB_SPI2_HOST
#endif
#ifndef SPI_DMA_CH_AUTO
#define SPI_DMA_CH_AUTO STUB_SPI_DMA_CH_AUTO
#endif
#ifndef STA
#define STA STUB_STA
#endif
#ifndef TWAI_MODE_NORMAL
#define TWAI_MODE_NORMAL STUB_TWAI_MODE_NORMAL
#endif
#ifndef UART
#define UART STUB_UART
#endif
#ifndef UART_DATA_8_BITS
#define UART_DATA_8_BITS STUB_UART_DATA_8_BITS
#endif
#ifndef UART_HW_FLOWCTRL_DISABLE
#define UART_HW_FLOWCTRL_DISABLE STUB_UART_HW_FLOWCTRL_DISABLE
#endif
#ifndef UART_NUM_1
#define UART_NUM_1 STUB_UART_NUM_1
#endif
#ifndef UART_PARITY_DISABLE
#define UART_PARITY_DISABLE STUB_UART_PARITY_DISABLE
#endif
#ifndef UART_PIN_NO_CHANGE
#define UART_PIN_NO_CHANGE STUB_UART_PIN_NO_CHANGE
#endif
#ifndef UART_PORT
#define UART_PORT STUB_UART_PORT
#endif
#ifndef UART_SCLK_DEFAULT
#define UART_SCLK_DEFAULT STUB_UART_SCLK_DEFAULT
#endif
#ifndef UART_STOP_BITS_1
#define UART_STOP_BITS_1 STUB_UART_STOP_BITS_1
#endif
#ifndef WDT
#define WDT STUB_WDT
#endif
#ifndef WIFI_AUTH_WPA2_PSK
#define WIFI_AUTH_WPA2_PSK STUB_WIFI_AUTH_WPA2_PSK
#endif
#ifndef WIFI_IF_STA
#define WIFI_IF_STA STUB_WIFI_IF_STA
#endif
#ifndef WIFI_MODE_STA
#define WIFI_MODE_STA STUB_WIFI_MODE_STA
#endif
#ifndef pdFALSE
#define pdFALSE STUB_pdFALSE
#endif
#ifndef pdTRUE
#define pdTRUE STUB_pdTRUE
#endif
#ifndef portMAX_DELAY
#define portMAX_DELAY STUB_portMAX_DELAY
#endif
#endif
