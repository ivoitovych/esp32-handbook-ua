# Додаток C. Повні шпаргалки команд {#dod-komandy}

Розгорнута версія картки [К10](#k-komandy).

**Синтаксис esptool v5** (дефіси, без `.py`). Для v4 — підкреслення і
суфікс `.py`. Перевірити своє: `esptool version`.

## esptool

### Розвідка

```
esptool --port /dev/ttyUSB0 chip-id          # сімейство, ревізія, MAC
esptool --port /dev/ttyUSB0 flash-id         # виробник і обсяг флешу
esptool --port /dev/ttyUSB0 read-mac
esptool version
```

### Читання

```
esptool --port PORT read-flash 0 ALL dump.bin           # повний дамп
esptool --port PORT read-flash 0 0x400000 dump.bin      # 4 МБ явно
esptool --port PORT read-flash 0x9000 0x6000 nvs.bin    # лише NVS
esptool --port PORT read-flash 0x8000 0x1000 pt.bin     # таблиця розділів
```

Розмір файлу має **точно** дорівнювати запитаному. Менший — обірваний
дамп; повторити на `--baud 115200`.

### Запис

```
esptool --port PORT --baud 460800 write-flash -z \
  0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 app.bin

esptool --port PORT write-flash 0x0 merged.bin          # зібраний образ
esptool --port PORT verify-flash 0x10000 app.bin        # звірити
```

### Стирання

```
esptool --port PORT erase-flash                  # ⛔ усе, спершу дамп
esptool --port PORT erase-region 0x9000 0x6000   # лише NVS
```

### Складання образу

```
esptool --chip esp32 merge-bin -o vyrib.bin --flash-mode dio --flash-size 4MB \
  0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 app.bin
```

`--chip` тут **обов'язковий**: порту немає, автовизначенню нема звідки
взятися. Без нього esptool одразу відповідає `Specify the --chip
argument`. Значення має збігатися з чипом, під який зібрано прошивку, — і
з адресою бутлоадера з таблиці нижче.

### Корисні прапорці

| Прапорець | Навіщо |
|---|---|
| `--baud 115200` | коли обривається на високій швидкості |
| `-z` | стиснення при передачі. **Уже ввімкнене** — крім `--no-stub` |
| `-u` | вимкнути стиснення |
| `--no-stub` | коли клон не приймає допоміжну програму |
| `--before no-reset` | коли на платі немає DTR/RTS і скидання робиться рукою |
| `--after no-reset` | лишити чип у завантажувачі: кілька команд поспіль |
| `--after watchdog-reset` | [[S3]] [[C3]] застряг у download mode через native USB |
| `--chip esp32s3` | коли автовизначення заважає |

Про `-z` варто знати точно: стиснення ввімкнене **за замовчуванням**,
тож у звичайній команді цей прапорець нічого не змінює. Сенс він має
рівно в одному випадку — разом із `--no-stub`, де стиснення типово
вимкнене.

`--before default-reset` і `--after hard-reset` — теж значення за
замовчуванням; писати їх, щоб «керувати скиданням», сенсу немає. Корисні
саме інші значення, наведені в таблиці.

## espefuse

::: nezvorotne
Лише читання безпечне. `burn-*` пропалює біти **фізично й назавжди**
(розділ 20).
:::

```
espefuse --port PORT summary        # безпечно: подивитися стан
```

## idf.py

### Проєкт

```
idf.py create-project imya
idf.py create-component imya
idf.py set-target esp32s3       # ⚠ стирає sdkconfig
idf.py menuconfig               # пошук усередині — клавіша /
```

### Збирання і прошивка

```
idf.py build
idf.py -p /dev/ttyUSB0 flash
idf.py -p /dev/ttyUSB0 monitor          # вихід Ctrl+]
idf.py -p /dev/ttyUSB0 flash monitor    # найчастіша команда
idf.py -p /dev/ttyUSB0 app-flash        # лише застосунок, швидше
idf.py fullclean                        # коли збирання поводиться дивно
idf.py merge-bin -o vyrib.bin           # один образ; адреси — з конфігурації
```

`idf.py merge-bin` кращий за `esptool merge-bin` завжди, коли проєкт під
рукою: адресу бутлоадера, чип, режим і частоту флешу він бере з
конфігурації, а не з набраного вручну рядка. Без `-o` результат —
`build/merged-binary.bin`.

### Аналіз

```
idf.py size                 # скільки зайнято флешу і RAM
idf.py size-components      # ХТО САМЕ займає — найкорисніша
idf.py size-files
```

### Діагностика

```
idf.py coredump-info        # розбір coredump із флешу
idf.py coredump-debug       # GDB на збереженому стані
idf.py openocd gdb          # покрокове налагодження (S3, C3)
idf.py monitor              # з розшифровкою backtrace на льоту
```

### Компоненти

```
idf.py add-dependency "espressif/led_strip^3.0.3"
idf.py reconfigure
```

## Розшифровка backtrace вручну

```
xtensa-esp32-elf-addr2line   -pfiaC -e build/app.elf 0x400d1234 0x400d5678
xtensa-esp32s3-elf-addr2line -pfiaC -e build/app.elf 0x42001234
riscv32-esp-elf-addr2line    -pfiaC -e build/app.elf 0x42001234
```

`-i` обов'язковий: без нього inline-кадри зникають.

## Монітори портів

| Програма | Вихід | Особливість |
|---|---|---|
| `idf.py monitor` | `Ctrl+]` | розшифровує backtrace; скидання `Ctrl+T`, `Ctrl+R` |
| `picocom -b 115200 /dev/ttyUSB0` | `Ctrl+A`, `Ctrl+X` | найпростіший |
| `minicom -D /dev/ttyUSB0 -b 115200` | `Ctrl+A`, `X` | |
| `screen /dev/ttyUSB0 115200` | `Ctrl+A`, `K` | є майже скрізь |

Запис логу у файл:

```
picocom -b 115200 /dev/ttyUSB0 | tee log-2026-08-26.txt
```

## Порти

```
ls /dev/ttyUSB* /dev/ttyACM*     # що є
ls -l /dev/serial/by-id/         # стабільні імена для скриптів
dmesg | tail -20                 # що ядро побачило
lsof /dev/ttyUSB0                # хто тримає порт
sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
```

`/dev/ttyUSB*` — зовнішній міст. `/dev/ttyACM*` — native USB [[S3]] [[C3]].

## PlatformIO

```
pio run                    # зібрати
pio run -e s3              # конкретне середовище
pio run -t upload
pio device monitor
pio run -t clean
pio pkg update
```

## Адреси у флеші

| Що | classic, S2 | S3, C3, C6, H2 | P4, C5, H4 |
|---|---|---|---|
| bootloader | `0x1000` | `0x0` | `0x2000` |
| таблиця розділів | `0x8000` | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` | `0x10000` |
| `nvs` (типово) | `0x9000` | `0x9000` | `0x9000` |
| зібраний `merge-bin` | `0x0` | `0x0` | `0x0` |

Адресу бутлоадера задає ROM чипа (`CONFIG_BOOTLOADER_OFFSET_IN_FLASH`), і
в ESP-IDF вона не налаштовується. Правила «що новіше, то ближче до нуля»
немає: у P4, C5 і H4 перші два сектори віддані під ключі шифрування
флешу, і бутлоадер зсунуто на `0x2000`.

## Розбір таблиці розділів із дампа

```
dd if=dump.bin of=pt.bin bs=1 skip=$((0x8000)) count=$((0x1000))
python $IDF_PATH/components/partition_table/gen_esp32part.py pt.bin
```

## Розвідка чужої прошивки

```
strings -n 6 dump.bin | less
strings -n 6 dump.bin | grep -iE "v[0-9]+\.[0-9]+|20[0-9]{2}-"
strings -n 6 dump.bin | grep -iE "http|mqtt|ssid|pass"
```

Розділ 24.

## Генерація NVS для серії

```
nvs_partition_gen.py generate config-0042.csv nvs-0042.bin 0x6000
esptool --port PORT write-flash 0x9000 nvs-0042.bin
```
