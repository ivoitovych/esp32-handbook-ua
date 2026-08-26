# Фактчекінг, прохід 11: шляхи в menuconfig

Дата: 2026-08-26. Звірено всі назви меню й пунктів `menuconfig`, які
називає книга, проти самих файлів `Kconfig`, з яких `menuconfig` дерево
й будує.

**Три виправлення, одне доповнення.**

## Чому це окрема категорія

Помилка тут коштує дорого відносно свого розміру. Читач відкриває
`menuconfig`, шукає названий пункт, не знаходить — і не має способу
зрозуміти, чи пункт перейменували, чи він дивиться не туди. Пошук
клавішею `/` виручає лише того, хто знає ім'я символа (`CONFIG_…`), а
книга дає назви меню.

Джерело — `Kconfig`, тобто буквальне першоджерело: рендер меню є
похідним від нього.

## Виправлення 1: меню зветься `Log`, не `Log output`

Книга давала `Log output` у двох місцях. Насправді:

```
components/log/Kconfig:        menu "Log"
                                   rsource "./Kconfig.level"
components/log/Kconfig.level:  menu "Log Level"
                                   choice LOG_DEFAULT_LEVEL
                                       bool "Default log verbosity"
```

Тобто повний шлях — `Component config` → `Log` → `Log Level` →
`Default log verbosity`: змінилася і назва меню, і глибина. Назва
`Log output` — від старіших версій ESP-IDF.

Сам пункт `Default log verbosity` існує дослівно, і типове значення
справді `Info`.

## Виправлення 2: відкат лежить у підменю

Книга: `Bootloader config` → `App rollback support`.

Насправді:

```
menu "Application Rollback"
    config BOOTLOADER_APP_ROLLBACK_ENABLE
        bool "Enable app rollback support"
```

Пропущено цілий рівень. Поруч видно `Enable app anti-rollback support` —
інший механізм (заборона встановлювати старішу версію через eFuse),
якого книга не описує й ні з чим не плутає.

## Виправлення 3: таблиця розділу 11 плутала рівні

Частина рядків називала пункт без шляху, і читач мусив здогадуватися, чи
це корінь, чи `Component config`. Тепер шлях повний скрізь, а правило
назване прямо:

> Три перші пункти меню — `Serial flasher config`, `Partition Table` і
> `Bootloader config` — лежать у корені, решта всередині
> `Component config`.

Правило не довільне: у корінь потрапляє `Kconfig.projbuild` компонента,
у `Component config` — звичайний `Kconfig`. Практично це означає, що в
корені живе те, що стосується збірки й прошивки взагалі, а не окремого
компонента.

Заразом уточнено рядок про оптимізацію: було `Compiler options` →
`-Os`, стало `Compiler options` → `Optimization Level` →
`Optimize for size`.

## Доповнення: чому `esp_log_level_set` мовчки не працює

Найцінніше в проході, і знайдене випадково — у сусідньому пункті того
самого меню.

Книга правильно писала, що підняти рівень у runtime можна лише для того,
що не вирізане при компіляції. Але єдиним виходом називала «збирати з
`Debug`» — а це псує головне: пристрій починає сипати налагоджувальним
логом постійно.

`Kconfig.level` розводить два різні поняття:

```
choice LOG_DEFAULT_LEVEL
    bool "Default log verbosity"
    help
        By default, this setting limits which log statements
        are compiled into the program. … To allow increasing log
        level above the default at runtime, see the next option.

choice LOG_MAXIMUM_LEVEL
    bool "Maximum log verbosity"
    default LOG_MAXIMUM_EQUALS_DEFAULT
    help
        This config option sets the highest log verbosity that it's
        possible to select at runtime by calling esp_log_level_set().
```

| Параметр | Що робить |
|---|---|
| `Default log verbosity` | рівень, з яким прошивка стартує |
| `Maximum log verbosity` | до чого можна підняти в runtime |

Пара `Default = Info`, `Maximum = Debug` дає рівно те, чого хоче
розділ 25: тихий пристрій, який на команду піднімає детальність
потрібної підсистеми без перезбирання.

Ключова подробиця, теж із джерела: типове значення `Maximum` —
`Same as default`. Тобто запасу за замовчуванням **немає**, і саме тому
пастка трапляється: людина викликає `esp_log_level_set`, нічого не
відбувається, помилки теж немає.

Додано в розділ 25 блоком уваги. `esp_log_level_set` при цьому працює
типово — `LOG_DYNAMIC_LEVEL_CONTROL` має `default y`.

## Що звірено без розбіжностей

`Compiler options` → `Optimization Level` → `Debug without optimization
(-O0)` у розділі 27 — дослівно, включно з твердженням, що `Debug (-Og)`
є значенням за замовчуванням (`default COMPILER_OPTIMIZATION_DEBUG`).

`Component config` → `FreeRTOS` → `Kernel` →
`configCHECK_FOR_STACK_OVERFLOW` з типовим `Check using canary bytes
(Method 2)` — дослівно (доказ уже стояв із проходу 6; ця звірка
незалежна й дала те саме).

`Component config` → `Bluetooth` → `Host` — дослівно, разом із назвами
варіантів `Bluedroid - Dual-mode` і `NimBLE - BLE only`.

`Component config` → `ESP System Settings` → `CPU frequency`,
`Component config` → `ESP PSRAM`, `Component config` → `Core dump`,
`Serial flasher config`, `Partition Table` — усі існують під цими
назвами.

## Стан реєстру після проходу

| Клас | Було (прохід 10) | Стало |
|---|---|---|
| A — первинне дослівне | 676 | **693** |
| B — первинне похідне | 27 | 27 |
| C — джерело недосяжне | 186 | 186 |
| D — обчислення | 25 | 25 |
| F — не звірено | 6696 | 6694 |
| **Усього одиниць** | 7610 | **7625** |

## Перевірки

```
tools/review.py     90 файлів, 0 знахідок
make arytmetyka     30 перевірок, 0 розбіжностей
tools/build.py      dovidnyk 406 с. · kartky 15 с. · proekty 28 с.
                    карток поза сторінкою: 0
```
