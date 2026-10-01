from unittest.mock import patch

from src import main


def test_main_json_empty():

    with patch(
        "builtins.input",
        side_effect=["1", "EXECUTED", "нет", "нет", "нет"],
    ), patch(
        "src.main.load_operations",
        return_value=[],
    ):

        main.main()


def test_main_csv_empty():

    with patch(
        "builtins.input",
        side_effect=["2", "EXECUTED", "нет", "нет", "нет"],
    ), patch(
        "src.main.get_transactions_csv",
        return_value=[],
    ):

        main.main()


def test_main_excel_empty():

    with patch(
        "builtins.input",
        side_effect=["3", "EXECUTED", "нет", "нет", "нет"],
    ), patch(
        "src.main.get_transactions_excel",
        return_value=[],
    ):

        main.main()
