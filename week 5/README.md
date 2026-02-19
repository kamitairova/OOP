# Electronic Device Shopping Cart

Небольшой консольный проект магазина электроники с корзиной покупок.  
Показывает наследование в ООП: базовый класс `Device` и наследники `Smartphone`, `Laptop`, `Tablet`.

## Функции
- Просмотр списка устройств (минимум 20)
- Добавление устройств в корзину с количеством (учёт склада `stock`)
- Просмотр корзины и общая сумма
- Оформление покупки (checkout): проверка наличия, уменьшение склада, печать чека
- Скидки на товары (`apply_discount`)

## Структура проекта
```
electronic_cart/
├─ src/
│  ├─ device.py
│  ├─ cart.py
│  ├─ store_app.py
│  └─ __init__.py
├─ tests/
│  ├─ test_device.py
│  ├─ test_cart.py
│  └─ __init__.py
└─ README.md
```

## Запуск приложения
Из папки `electronic_cart`:

```bash
python -m src.store_app
```

## Тесты (pytest)
Установка pytest:

```bash
python -m pip install pytest
```

Запуск тестов:

```bash
python -m pytest -q
```

Пример успешного вывода:
```
.....                                                    [100%]
5 passed in 0.10s
```

## Пример работы (sample run)
Пример (возможный) сценарий:
1) Show Devices → выбрать устройство → ввести количество → Added to cart  
2) Show Cart → посмотреть позиции → Checkout now? (y) → чек и обновление stock
