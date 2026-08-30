#!/usr/bin/env bash
# Докачування джерел для незвірених одиниць. Наряд — factcheck/DOKACHATY-m2.md.
#
# Кожен рядок іде через factcheck/tools/cache.py, який кладе файл у source-cache/,
# рахує sha256 і пише рядок у маніфест. Хибна адреса тут не отруює кеш
# мовчки: cache.py перевіряє, що завантажене справді відкривається, і
# невдача видно в підсумку.
set -u
cd "$(dirname "$0")/.."

VZYATY=0; NE_VYYSHLO=0
vzyaty() {
    local url="$1" chomu="$2"
    if python3 factcheck/tools/cache.py "$url" >/dev/null 2>&1; then
        echo "   ✓ $chomu"
        VZYATY=$((VZYATY+1))
    else
        echo "   ✗ $chomu  — $url"
        NE_VYYSHLO=$((NE_VYYSHLO+1))
    fi
}

E=https://www.espressif.com/sites/default/files/documentation

echo "── Espressif: взірець адреси сталий, качається без умов"
vzyaty "$E/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf"      "ESP32-S3-WROOM-1 (8 одиниць)"
vzyaty "$E/esp32-c3-mini-1_datasheet_en.pdf"                "ESP32-C3-MINI-1 (8 одиниць)"
vzyaty "$E/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf" "ESP32-WROVER-E (7 одиниць)"
vzyaty "$E/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf" "ESP32-WROOM-32D (5 одиниць)"
vzyaty "$E/esp32-c3_datasheet_en.pdf"                       "ESP32-C3 (7 одиниць)"
vzyaty "$E/esp32-s3_datasheet_en.pdf"                       "ESP32-S3 (5 одиниць)"
vzyaty "$E/esp32-s2_datasheet_en.pdf"                       "ESP32-S2"
vzyaty "$E/esp32-p4_datasheet_en.pdf"                       "ESP32-P4"
vzyaty "$E/esp32-c5_datasheet_en.pdf"                       "ESP32-C5 (2 одиниці)"
vzyaty "$E/0a-esp8266ex_datasheet_en.pdf"                   "ESP8266EX (13 одиниць)"

echo "── Texas Instruments: взірець теж сталий"
T=https://www.ti.com/lit/ds/symlink
vzyaty "$T/tca9548a.pdf"  "TCA9548A (3 одиниці)"
vzyaty "$T/uln2003a.pdf"  "ULN2003A (3 одиниці)"
vzyaty "$T/ads1256.pdf"   "ADS1256 (2 одиниці)"

echo "── Analog (Maxim): падає, доки канал іде через VPN"
A=https://www.analog.com/media/en/technical-documentation/data-sheets
vzyaty "$A/MAX1487-MAX491.pdf"  "MAX485 (7 одиниць)"
vzyaty "$A/DS3231.pdf"          "DS3231 (5 одиниць)"
vzyaty "$A/MAX98357A-MAX98357B.pdf" "MAX98357A (2 одиниці)"
vzyaty "$A/MAX17048-MAX17049.pdf"   "MAX17048 (1 одиниця)"

echo
echo "взято $VZYATY, не вийшло $NE_VYYSHLO"
echo "Не вийшло — не привід підставляти «схоже» джерело."
echo "Причину пиши у factcheck/MEREZHA-m2.md, одиниця лишається в наряді."
