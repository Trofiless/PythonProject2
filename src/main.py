from src.processing import (
    filter_by_state,
    process_bank_search,
    sort_by_date,
)

from src.reader import get_transactions_csv, get_transactions_excel

from src.utils import load_operations

from src.masks import get_mask_account, get_mask_card_number

from src.widget import get_date


def format_operation(operation: dict) -> str:
    """Форматирует банковскую операцию для вывода пользователю."""

    date = get_date(operation["date"])

    description = operation["description"]

    amount = operation["operationAmount"]["amount"]

    currency = operation["operationAmount"]["currency"]["name"]

    result = f"{date} {description}\n"

    if "from" in operation:

        from_value = operation["from"]

        parts = from_value.rsplit(" ", 1)

        if len(parts) == 2 and parts[1].isdigit():

            name, number = parts

            if name == "Счет":

                from_value = f"{name} {get_mask_account(number)}"

            else:

                from_value = f"{name} {get_mask_card_number(number)}"

        result += from_value

    if "to" in operation:

        to_value = operation["to"]

        parts = to_value.rsplit(" ", 1)

        if len(parts) == 2 and parts[1].isdigit():

            name, number = parts

            if name == "Счет":

                to_value = f"{name} {get_mask_account(number)}"

            else:

                to_value = f"{name} {get_mask_card_number(number)}"

        if "from" in operation:

            result += f" -> {to_value}"

        else:

            result += to_value

    result += f"\nСумма: {amount} {currency}"

    return result


def main() -> None:
    """Запускает основную логику программы."""

    print("Программа: Привет! Добро пожаловать в программу работы " "с банковскими транзакциями.")

    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON файла\n"
        "2. Получить информацию о транзакциях из CSV файла\n"
        "3. Получить информацию о транзакциях из XLSX файла"
    )

    choice = input("Пользователь: ")

    if choice == "1":

        print("Программа: Для обработки выбран JSON файл.")

        operations = load_operations("data/operations.json")

    elif choice == "2":

        print("Программа: Для обработки выбран CSV файл.")

        operations = get_transactions_csv("data/transactions.csv")

    elif choice == "3":

        print("Программа: Для обработки выбран XLSX файл.")

        operations = get_transactions_excel("data/transactions_excel.xlsx")

    else:

        print("Программа: Некорректный пункт меню.")

        return

    available_states = ["EXECUTED", "CANCELED", "PENDING"]

    while True:

        state = input(
            "Программа: Введите статус, по которому необходимо выполнить фильтр\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Пользователь: "
        ).upper()

        if state in available_states:

            break

        print(f'Программа: Статус операции "{state}" недоступен.')

    operations = filter_by_state(operations, state)

    print(f'Программа: Операции отфильтрованы по статусу "{state}"')

    sort_answer = input("Программа: Отсортировать операции по дате? Да/Нет\n" "Пользователь: ")

    if sort_answer.lower() == "да":

        sort_order = input("Программа: Отсортировать по возрастанию или по убыванию?\n" "Пользователь: ")

        operations = sort_by_date(
            operations,
            reverse=sort_order.lower() == "по убыванию",
        )

    ruble_answer = input("Программа: Выводить только рублевые транзакции? Да/Нет\n" "Пользователь: ")

    if ruble_answer.lower() == "да":

        operations = [
            operation for operation in operations if operation["operationAmount"]["currency"]["code"] == "RUB"
        ]

    search_answer = input(
        "Программа: Отфильтровать список транзакций по определенному " "слову в описании? Да/Нет\n" "Пользователь: "
    )

    if search_answer.lower() == "да":

        search = input("Пользователь: ")

        operations = process_bank_search(operations, search)

    print("Программа: Распечатываю итоговый список транзакций...\n")

    if not operations:

        print("Программа: Не найдено ни одной транзакции, " "подходящей под ваши условия фильтрации")

        return

    print(f"Программа:\nВсего банковских операций в выборке: " f"{len(operations)}\n")

    for operation in operations:

        print(format_operation(operation))

        print()


if __name__ == "__main__":

    main()
