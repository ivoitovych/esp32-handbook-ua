# К10. Шпаргалка команд {#k-komandy}

Синтаксис esptool **v5** (дефіси, без `.py`). Для v4 — підкреслення і
суфікс `.py`: `esptool.py write_flash`. Перевірити своє: `esptool version`.

## esptool

```
esptool --port /dev/ttyUSB0 chip-id            # що за чип і ревізія
esptool --port /dev/ttyUSB0 flash-id           # обсяг і виробник флешу
esptool --port /dev/ttyUSB0 read-flash 0 ALL dump.bin      # повний дамп
esptool --port /dev/ttyUSB0 write-flash -z 0x10000 app.bin # залити
esptool --port /dev/ttyUSB0 verify-flash 0x10000 app.bin   # звірити
esptool --port /dev/ttyUSB0 erase-flash        # стерти все (⚠ див. К2)
esptool --port /dev/ttyUSB0 --baud 115200 ...  # повільніше, надійніше
esptool merge-bin -o all.bin --flash-mode dio \
  0x1000 boot.bin 0x8000 pt.bin 0x10000 app.bin   # 0x1000 → classic; S3/C3: 0x0
```

## idf.py

```
idf.py create-project my-project    # новий проєкт (назва латиницею)
idf.py set-target esp32s3           # ⚠ стирає sdkconfig
idf.py menuconfig                   # налаштування
idf.py build                        # зібрати
idf.py -p /dev/ttyUSB0 flash        # залити
idf.py -p /dev/ttyUSB0 monitor      # монітор з розшифровкою backtrace
idf.py -p /dev/ttyUSB0 flash monitor  # найчастіша команда
idf.py fullclean                    # коли збирання поводиться незрозуміло
idf.py size                         # скільки зайнято флешу і RAM
idf.py coredump-info                # розбір coredump із флешу
```

## Монітор

`idf.py monitor`: вийти — `Ctrl+]`. Скинути плату — `Ctrl+T`, потім `Ctrl+R`.

```
minicom -D /dev/ttyUSB0 -b 115200    # вийти: Ctrl+A, потім X
screen /dev/ttyUSB0 115200           # вийти: Ctrl+A, потім K
picocom -b 115200 /dev/ttyUSB0       # вийти: Ctrl+A, потім Ctrl+X
```

## Порт

```
ls /dev/ttyUSB* /dev/ttyACM*     # Linux: що є
dmesg | tail                     # що ядро побачило при під'єднанні
sudo usermod -aG dialout $USER   # права; далі ПЕРЕЗАЙТИ в систему
lsof /dev/ttyUSB0                # хто тримає порт
```

`/dev/ttyUSB*` — зовнішній міст (CP2102, CH340).
`/dev/ttyACM*` — native USB [[S3]] [[C3]].

## Адреси

| Що | classic / S2 | S3 / C3+ |
|---|---|---|
| bootloader | `0x1000` | `0x0` |
| partition table | `0x8000` | `0x8000` |
| застосунок | `0x10000` | `0x10000` |
| зібраний `merge-bin` | `0x0` | `0x0` |
