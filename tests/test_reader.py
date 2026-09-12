from unittest.mock import Mock, patch

from src.reader import get_transactions_csv, get_transactions_excel


@patch("src.reader.pd.read_csv")
def test_get_transactions_csv(mock_read_csv):

    mock_df = Mock()

    mock_df.to_dict.return_value = [{"id": 1, "state": "EXECUTED"}]

    mock_read_csv.return_value = mock_df

    result = get_transactions_csv("fake_path.csv")

    assert isinstance(result, list)

    assert len(result) > 0

    assert isinstance(result[0], dict)

    mock_read_csv.assert_called_once()


@patch("src.reader.pd.read_excel")
def test_get_transactions_excel(mock_read_excel):

    mock_df = Mock()

    mock_df.to_dict.return_value = [{"id": 1, "state": "EXECUTED"}]

    mock_read_excel.return_value = mock_df

    result = get_transactions_excel("fake_path.xlsx")

    assert isinstance(result, list)

    assert len(result) > 0

    assert isinstance(result[0], dict)

    mock_read_excel.assert_called_once()
