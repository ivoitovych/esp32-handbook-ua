#!/usr/bin/env python3
"""Генератор заглушок ESP-IDF для компіляційної перевірки прикладів.

`kod/stubs/esp_idf_stubs.h` генерується цим інструментом і руками не
правиться. Джерело складу — самі приклади книги: беруться типи,
структури, функції й константи, які вони вживають.

Одна річ береться **не** з книги, і це принципово: **поля структур**.
Вони виписані нижче вручну зі справжніх заголовків ESP-IDF (звірено в
проході 21). Якби вони бралися з книги, перевірка перетворилася б на
тавтологію — приклад завжди узгоджений сам із собою.

Тому compile-перевірка ловить у полях саме розбіжність із ESP-IDF:
`.sda_io_num` існує, `.sda_gpio` — ні, і другий варіант не збереться.

    tools/kod-stubs.py        перегенерувати заглушки
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRUPY = ("kartky", "manual", "dodatky", "inserts")
CIL = ROOT / "kod" / "stubs" / "esp_idf_stubs.h"

# ── Поля структур: зняті із заголовків ESP-IDF release/v5.5 ───────────
# Це єдина частина, яку книга не визначає. Саме тому compile-перевірка
# тут щось означає.
STRUKT: dict[str, list[str]] = {
    "i2c_master_bus_config_t": [
        "int i2c_port", "int sda_io_num", "int scl_io_num", "int clk_source",
        "int glitch_ignore_cnt", "int intr_priority", "int trans_queue_depth",
        "struct { int enable_internal_pullup; int allow_pd; } flags"],
    "i2c_device_config_t": [
        "int dev_addr_length", "unsigned device_address", "unsigned scl_speed_hz",
        "unsigned scl_wait_us", "struct { int disable_ack_check; } flags"],
    "spi_bus_config_t": [
        "int mosi_io_num", "int miso_io_num", "int sclk_io_num",
        "int quadwp_io_num", "int quadhd_io_num", "int max_transfer_sz",
        "unsigned flags", "int intr_flags"],
    "spi_device_interface_config_t": [
        "unsigned char command_bits", "unsigned char address_bits",
        "unsigned char dummy_bits", "unsigned char mode",
        "int clock_source", "int duty_cycle_pos", "int cs_ena_pretrans",
        "int cs_ena_posttrans", "int clock_speed_hz", "int input_delay_ns",
        "int spics_io_num", "unsigned flags", "int queue_size",
        "void (*pre_cb)(void *)", "void (*post_cb)(void *)"],
    "spi_transaction_t": [
        "unsigned flags", "unsigned short cmd", "unsigned long long addr",
        "size_t length", "size_t rxlength", "void *user",
        "const void *tx_buffer", "void *rx_buffer"],
    "uart_config_t": [
        "int baud_rate", "int data_bits", "int parity", "int stop_bits",
        "int flow_ctrl", "unsigned char rx_flow_ctrl_thresh", "int source_clk"],
    "ledc_timer_config_t": [
        "int speed_mode", "int duty_resolution", "int timer_num",
        "unsigned freq_hz", "int clk_cfg", "int deconfigure"],
    "ledc_channel_config_t": [
        "int gpio_num", "int speed_mode", "int channel", "int intr_type",
        "int timer_sel", "unsigned duty", "int hpoint", "int sleep_mode",
        "struct { unsigned output_invert; } flags"],
    "gpio_config_t": [
        "unsigned long long pin_bit_mask", "int mode", "int pull_up_en",
        "int pull_down_en", "int intr_type", "int hys_ctrl_mode"],
    "adc_oneshot_unit_init_cfg_t": [
        "int unit_id", "int clk_src", "int ulp_mode", "int atten", "int bitwidth"],
    "adc_oneshot_chan_cfg_t": ["int atten", "int bitwidth"],
    "adc_cali_curve_fitting_config_t": [
        "int unit_id", "int chan", "int atten", "int bitwidth"],
    "esp_timer_create_args_t": [
        "void (*callback)(void *)", "void *arg", "int dispatch_method",
        "const char *name", "int skip_unhandled_events"],
    "twai_message_t": [
        "unsigned flags", "unsigned identifier", "unsigned data_length_code",
        "unsigned char data[8]", "unsigned extd", "unsigned rtr",
        "unsigned ss", "unsigned self", "unsigned dlc_non_comp"],
    "twai_general_config_t": [
        "int mode", "int tx_io", "int rx_io", "int clkout_io", "int bus_off_io",
        "unsigned tx_queue_len", "unsigned rx_queue_len", "unsigned alerts_enabled",
        "unsigned clkout_divider", "int intr_flags"],
    "twai_timing_config_t": [
        "unsigned brp", "unsigned char tseg_1", "unsigned char tseg_2",
        "unsigned char sjw", "int triple_sampling"],
    "twai_filter_config_t": [
        "unsigned acceptance_code", "unsigned acceptance_mask", "int single_filter"],
    "twai_status_info_t": [
        "int state", "unsigned msgs_to_tx", "unsigned msgs_to_rx",
        "unsigned tx_error_counter", "unsigned rx_error_counter",
        "unsigned tx_failed_count", "unsigned rx_missed_count",
        "unsigned arb_lost_count", "unsigned bus_error_count"],
    "esp_now_peer_info_t": [
        "unsigned char peer_addr[6]", "unsigned char lmk[16]",
        "unsigned char channel", "int ifidx", "int encrypt", "void *priv"],
    "esp_now_recv_info_t": [
        "unsigned char *src_addr", "unsigned char *des_addr", "void *rx_ctrl"],
    "esp_now_send_info_t": ["unsigned char des_addr[6]", "int tx_status"],
    "httpd_config_t": [
        "unsigned task_priority", "size_t stack_size", "int core_id",
        "unsigned short server_port", "unsigned short ctrl_port",
        "unsigned short max_open_sockets", "unsigned short max_uri_handlers",
        "int lru_purge_enable", "unsigned recv_wait_timeout",
        "unsigned send_wait_timeout", "void *global_user_ctx"],
    "httpd_uri_t": [
        "const char *uri", "int method", "esp_err_t (*handler)(httpd_req_t *r)",
        "void *user_ctx"],
    "httpd_req_t": [
        "void *handle", "int method", "char uri[512]", "size_t content_len",
        "void *aux", "void *user_ctx", "void *sess_ctx"],
    "esp_http_client_config_t": [
        "const char *url", "const char *host", "int port", "const char *path",
        "const char *cert_pem", "int method", "int timeout_ms",
        "esp_err_t (*event_handler)(void *evt)", "int transport_type",
        "int buffer_size", "int keep_alive_enable"],
    "esp_https_ota_config_t": [
        "const esp_http_client_config_t *http_config",
        "esp_err_t (*http_client_init_cb)(void *)",
        "int bulk_flash_erase", "int partial_http_download", "int max_http_request_size"],
    "esp_mqtt_client_config_t": [
        "struct { struct { const char *uri; const char *hostname; int port; } address;"
        " struct { struct { const char *data; size_t len; } certificate; } verification; } broker",
        "struct { const char *username; const char *client_id;"
        " struct { const char *password; } authentication; } credentials",
        "struct { int keepalive; int disable_clean_session;"
        " struct { const char *topic; const char *msg; int qos; int retain; } last_will; } session",
        "struct { int reconnect_timeout_ms; int network_timeout_ms; } network"],
    "wifi_config_t": [
        "struct { unsigned char ssid[32]; unsigned char password[64];"
        " unsigned char scan_method; unsigned char bssid_set;"
        " unsigned char bssid[6]; unsigned char channel;"
        " struct { signed char rssi; int authmode; } threshold; } sta;"
        " struct { unsigned char ssid[32]; unsigned char password[64];"
        " unsigned char ssid_len; unsigned char channel; int authmode;"
        " unsigned char ssid_hidden; unsigned char max_connection; } ap"],
    "wifi_ap_record_t": [
        "unsigned char bssid[6]", "unsigned char ssid[33]",
        "unsigned char primary", "int second", "signed char rssi",
        "int authmode", "int pairwise_cipher", "int group_cipher"],
    "wifi_init_config_t": [
        "int static_rx_buf_num", "int dynamic_rx_buf_num", "int tx_buf_type",
        "int static_tx_buf_num", "int dynamic_tx_buf_num", "int nvs_enable"],
    "led_strip_config_t": [
        "int strip_gpio_num", "unsigned max_leds", "int led_model",
        "struct { unsigned r; unsigned g; unsigned b; unsigned w; } color_component_format",
        "struct { unsigned invert_out; } flags"],
    "led_strip_rmt_config_t": [
        "int clk_src", "unsigned resolution_hz", "size_t mem_block_symbols",
        "struct { unsigned with_dma; } flags"],
}

# Типи книги — оголошуються в самих прикладах.
VLASNI = {"blok_t", "nalashtuvannya_t", "paket_t", "stan_t", "stan_vuzla_t",
          "zapys_t", "adc_t", "osrs_t", "vymiryuvannya_t"}
STD = {"int8_t", "int16_t", "int32_t", "int64_t", "uint8_t", "uint16_t",
       "uint32_t", "uint64_t", "size_t", "socklen_t", "ssize_t", "time_t",
       "bool_t", "wchar_t", "esp_err_t"}

# Функції, тип повернення яких книга справді використовує.
TYPOVANI = {
    "esp_timer_get_time": "int64_t", "esp_get_free_heap_size": "uint32_t",
    "esp_get_minimum_free_heap_size": "uint32_t",
    "heap_caps_get_free_size": "size_t",
    "heap_caps_get_largest_free_block": "size_t",
    "heap_caps_malloc": "void *", "heap_caps_calloc": "void *",
    "esp_err_to_name": "const char *", "pcTaskGetName": "char *",
    "xTaskGetCurrentTaskHandle": "void *", "xQueueCreate": "void *",
    "xSemaphoreCreateMutex": "void *", "xSemaphoreCreateBinary": "void *",
    "xSemaphoreCreateCounting": "void *", "xEventGroupCreate": "void *",
    "xTimerCreate": "void *", "uxTaskGetStackHighWaterMark": "uint32_t",
    "xEventGroupWaitBits": "uint32_t", "xEventGroupSetBits": "uint32_t",
    "esp_random": "uint32_t", "xPortGetCoreID": "int",
    "esp_ota_get_running_partition": "const void *",
    "esp_ota_get_next_update_partition": "const void *",
    "esp_partition_find_first": "const void *",
    "esp_reset_reason": "int", "nazva": "const char *",
}

# Уже є в стандартних заголовках або в мові.
NE_OHOLOSHUVATY = {
    "if", "for", "while", "switch", "return", "sizeof", "do", "else", "defined",
    "case", "default", "goto", "break", "continue", "struct", "union", "enum",
    "const", "volatile", "inline", "restrict", "register", "auto", "typeof",
    "__attribute__", "_Static_assert", "static_assert", "offsetof",
    "va_start", "va_end", "va_arg", "alignof", "_Alignof",
    "printf", "fprintf", "sprintf", "snprintf", "sscanf", "fopen", "fclose",
    "fgets", "fputs", "fread", "fwrite", "fflush", "malloc", "calloc", "free",
    "realloc", "strlen", "strcmp", "strncmp", "strcpy", "strncpy", "strcat",
    "strstr", "strtol", "strtoul", "atoi", "atof", "memcpy", "memset",
    "memcmp", "memmove", "abs", "exit", "fabs", "fabsf", "roundf", "powf",
    "logf", "sqrtf", "puts", "putchar", "rand", "srand",
    # макроси, які оголошуємо нижче окремо
    "pdMS_TO_TICKS", "ESP_ERROR_CHECK", "ESP_RETURN_ON_ERROR",
    "ESP_GOTO_ON_ERROR", "ESP_ERROR_CHECK_WITHOUT_ABORT",
    "ESP_LOGI", "ESP_LOGW", "ESP_LOGE", "ESP_LOGD", "ESP_LOGV",
}

RE_BLOK = re.compile(r"```c\n(.*?)```", re.S)
RE_TYP = re.compile(r"\b([A-Za-z_]\w*_t)\b")
RE_VYKLYK = re.compile(r"\b([A-Za-z_]\w*)\s*\(")
RE_MAKRO = re.compile(r"\b([A-Z][A-Z0-9_]{2,})\b")
# Константи FreeRTOS не кричать великими літерами: pdTRUE, portMAX_DELAY,
# tskIDLE_PRIORITY. Без них половина прикладів про задачі не збирається.
RE_FREERTOS = re.compile(r"\b((?:pd|port|tsk|err|queue|sem)[A-Z]\w*)\b")
# Функція, яку книга сама визначає: заглушки для неї не треба.
# Імена, які книга оголошує сама: власні #define, елементи власних enum,
# власні типи. Заглушка для них — не помилка стилю, а зіткнення імен:
# `STAN_STOP` із прикладу проєкту 62 і `STUB_STAN_STOP` не можуть жити в
# одній одиниці трансляції.
RE_VLASNYY_DEFINE = re.compile(r"^\s*#define\s+([A-Za-z_]\w*)", re.M)
# Змінна верхнього рівня, оголошена книгою: `static const uint8_t MAC[6] = …`
RE_VLASNA_ZMINNA = re.compile(
    r"^\s*(?:static\s+|const\s+|volatile\s+|RTC_DATA_ATTR\s+|DRAM_ATTR\s+)+"
    r"[A-Za-z_]\w*[\s*]+([A-Za-z_]\w*)\s*(?:\[[^\]]*\])?\s*[=;]", re.M)
RE_ENUM_TILO = re.compile(r"enum\s*(?:\w+\s*)?\{([^}]*)\}", re.S)
RE_ENUM_ELEMENT = re.compile(r"^\s*([A-Za-z_]\w*)\s*(?:=[^,\n]*)?,?\s*(?://.*)?$",
                             re.M)

RE_VYZNACHENA = re.compile(
    r"^\s*(?:static\s+|inline\s+)*"
    r"(?:void|int|char|float|double|unsigned|signed|bool|esp_err_t|"
    r"[A-Za-z_]\w*_t|const\s+char)[\s*]+"
    r"(?:IRAM_ATTR\s+|DRAM_ATTR\s+|RTC_DATA_ATTR\s+)?"
    r"(\w+)\s*\([^;]*\)\s*\{", re.M)


def main() -> int:
    typy, vyklyky, makrosy, vyznacheni = set(), set(), set(), set()
    vlasni_imena: set[str] = set()
    for g in GRUPY:
        for f in sorted((ROOT / g).glob("*.md")):
            for m in RE_BLOK.finditer(f.read_text(encoding="utf-8")):
                b = m.group(1)
                typy |= set(RE_TYP.findall(b))
                vyklyky |= set(RE_VYKLYK.findall(b))
                makrosy |= set(RE_MAKRO.findall(b))
                makrosy |= set(RE_FREERTOS.findall(b))
                vyznacheni |= set(RE_VYZNACHENA.findall(b))
                vlasni_imena |= set(RE_VLASNYY_DEFINE.findall(b))
                vlasni_imena |= set(RE_VLASNA_ZMINNA.findall(b))
                for tilo in RE_ENUM_TILO.findall(b):
                    vlasni_imena |= set(RE_ENUM_ELEMENT.findall(tilo))

    opaque = sorted(typy - VLASNI - STD - set(STRUKT))
    out = ["/* Згенеровано tools/kod-stubs.py. Руками не правити. */",
           "#ifndef ESP_IDF_STUBS_H", "#define ESP_IDF_STUBS_H", "",
           "#include <stdint.h>", "#include <stddef.h>", "#include <stdbool.h>",
           "#include <string.h>", "#include <stdio.h>", "#include <stdlib.h>",
           "#include <math.h>",
           "/* Сокети — справжні системні заголовки: книга вживає",
           "   struct sockaddr_in і його поля, і перевіряти їх треба",
           "   проти POSIX, а не проти заглушки. */",
           "#include <sys/socket.h>", "#include <netinet/in.h>",
           "#include <arpa/inet.h>", "#include <unistd.h>",
           "", "typedef int esp_err_t;", ""]
    out += [f"typedef void *{t};" for t in opaque]
    out.append("")
    for t, polya in sorted(STRUKT.items()):
        out.append("typedef struct {")
        out += [f"    {p};" for p in polya]
        out.append(f"}} {t};")
    out.append("")

    out += ["/* Логування і перевірки — макроси зі змінним числом аргументів. */"]
    for m in ("ESP_LOGI", "ESP_LOGW", "ESP_LOGE", "ESP_LOGD", "ESP_LOGV"):
        out.append(f"#define {m}(tag, ...) ((void)(tag))")
    out += ["#define ESP_ERROR_CHECK(x) ((void)(x))",
            "#define ESP_ERROR_CHECK_WITHOUT_ABORT(x) ((void)(x))",
            "#define ESP_RETURN_ON_ERROR(x, tag, ...) ((void)(x))",
            "#define ESP_GOTO_ON_ERROR(x, l, tag, ...) ((void)(x))",
            "#define IRAM_ATTR", "#define RTC_DATA_ATTR", "#define DRAM_ATTR",
            "#define pdMS_TO_TICKS(ms) ((int)(ms))",
            "#define portTICK_PERIOD_MS 1", ""]

    out.append("/* Функції ESP-IDF та FreeRTOS, що вживає книга. */")
    for f in sorted(vyklyky - NE_OHOLOSHUVATY - vyznacheni - vlasni_imena):
        if not re.fullmatch(r"[A-Za-z_]\w*", f):
            continue
        out.append(f"{TYPOVANI.get(f, 'esp_err_t')} {f}();")
    out.append("")

    out.append("/* Символьні константи. Значення довільні: перевіряється")
    out.append("   існування імені, а не число за ним. */")
    konst = sorted(m for m in makrosy
                   if m not in NE_OHOLOSHUVATY and not m.startswith("CONFIG_")
                   and m not in ("TAG", "NULL")
                   and m not in vlasni_imena)
    yak_funkciya = sorted(k for k in konst if k in vyklyky)
    konst = [k for k in konst if k not in yak_funkciya]
    if yak_funkciya:
        out.append("/* Макроси ESP-IDF, що вживаються з дужками. */")
        for k in yak_funkciya:
            out.append(f"#define {k}(...) (0)")
        out.append("")
    out.append("enum {")
    out += [f"    STUB_{k} = {i}," for i, k in enumerate(konst)]
    out.append("};")
    for k in konst:
        out += [f"#ifndef {k}", f"#define {k} STUB_{k}", "#endif"]
    out.append("#endif")

    CIL.parent.mkdir(parents=True, exist_ok=True)
    CIL.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"заглушки: типів {len(opaque)} + структур {len(STRUKT)}, "
          f"функцій {len(vyklyky - NE_OHOLOSHUVATY - vyznacheni - vlasni_imena)}, "
          f"констант {len(konst)}; власних імен книги пропущено "
          f"{len(vlasni_imena)} → {CIL.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
