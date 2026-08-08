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