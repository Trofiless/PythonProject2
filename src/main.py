from src.processing import (
    filter_by_state,
    sort_by_date,
    process_bank_search,
)

from src.reader import get_transactions_csv, get_transactions_excel

from src.utils import load_operations


def main():

    print("Программа: Привет! Добро пожаловать в программу работы " "с банковскими транзакциями.")

    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    choice = input("Пользователь: ")

    if choice == "1":

        print("Программа: Для обработки выбран JSON-файл.")

        operations = load_operations("data/operations.json")

    elif choice == "2":

        print("Программа: Для обработки выбран CSV-файл.")

        operations = get_transactions_csv("data/transactions.csv")

    else:

        print("Программа: Для обработки выбран XLSX-файл.")

        operations = get_transactions_excel("data/transactions_excel.xlsx")

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

        print("Программа: Введите статус, по которому необходимо выполнить фильтр")

    operations = filter_by_state(operations, state)

    print(f'Программа: Операции отфильтрованы по статусу "{state}"')

    sort_answer = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ")

    if sort_answer.lower() == "да":

        sort_order = input("Программа: Отсортировать по возрастанию или по убыванию?\n" "Пользователь: ")

        if sort_order.lower() == "по возрастанию":

            operations = sort_by_date(operations, reverse=False)

        else:

            operations = sort_by_date(operations, reverse=True)

    ruble_answer = input("Программа: Выводить только рублевые транзакции? Да/Нет\n" "Пользователь: ")

    if ruble_answer.lower() == "да":

        operations = [
            operation
            for operation in operations
            if operation.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    search_answer = input(
        "Программа: Отфильтровать список транзакций по определенному слову " "в описании? Да/Нет\n" "Пользователь: "
    )

    if search_answer.lower() == "да":

        search = input("Пользователь: ")

        operations = process_bank_search(operations, search)

    print("Программа: Распечатываю итоговый список транзакций...")

    if not operations:

        print("Программа: Не найдено ни одной транзакции, " "подходящей под ваши условия фильтрации")

        return

    print(f"Программа:\nВсего банковских операций в выборке: {len(operations)}")

    for operation in operations:

        print(operation)


if __name__ == "__main__":

    main()
