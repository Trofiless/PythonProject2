# Виджет банковских операций

## Описание проекта

Проект представляет собой виджет для обработки банковских операций.

Реализованы следующие функции:

- маскирование номеров банковских карт;
- маскирование номеров счетов;
- преобразование даты в формат ДД.ММ.ГГГГ;
- фильтрация операций по статусу;
- сортировка операций по дате.

## Установка

Клонируйте репозиторий:
git clone <ссылка на репозиторий>
Перейдите в директорию проекта:
cd PythonProject2
Установите зависимости:
poetry install
## Использование

### Фильтрация операций по статусу
from src.processing import filter_by_state

operations = [
    {"state": "EXECUTED"},
    {"state": "CANCELED"},
]

result = filter_by_state(operations)
print(result)
### Сортировка операций по дате
from src.processing import sort_by_date

operations = [
    {"date": "2024-03-11T02:26:18.671407"},
    {"date": "2023-07-03T18:35:29.512364"},
]

result = sort_by_date(operations)
print(result)

## Модуль generators

В проект был добавлен модуль generators.py, содержащий генераторы для обработки банковских операций.

### Реализованные функции

#### filter_by_currency(transactions, currency)

Возвращает генератор транзакций, валюта которых соответствует указанной.

Пример:
usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)
#### transaction_descriptions(transactions)

Возвращает описания транзакций по одному.

Пример:
descriptions = transaction_descriptions(transactions)

for description in descriptions:
    print(description)
#### card_number_generator(start, stop)

Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

Пример:
for card in card_number_generator(1, 3):
    print(card)
Результат:
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003

## Тестирование

Для запуска всех тестов выполните команду:
poetry run pytest

Проект содержит тесты для следующих модулей:

- masks.py
- widget.py
- processing.py

Все тесты написаны с использованием библиотеки pytest.


## Автор

Elena Trofimova-Pavlova