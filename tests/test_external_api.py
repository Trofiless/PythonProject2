from unittest.mock import Mock, patch

from src.external_api import convert_currency


def test_convert_currency_rub():

    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}

    with patch("src.external_api.requests.get") as mock_get:

        result = convert_currency(transaction)

    assert result == 1000.0

    mock_get.assert_not_called()


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_convert_currency_usd(mock_get, mock_getenv):

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    mock_getenv.return_value = "test_api_key"

    mock_response = Mock()

    mock_response.json.return_value = {"result": 9500.0}

    mock_get.return_value = mock_response

    result = convert_currency(transaction)

    assert result == 9500.0

    mock_get.assert_called_once()

    mock_getenv.assert_called_once_with("API_KEY")


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_convert_currency_eur(mock_get, mock_getenv):

    transaction = {"operationAmount": {"amount": "50", "currency": {"code": "EUR"}}}

    mock_getenv.return_value = "test_api_key"

    mock_response = Mock()

    mock_response.json.return_value = {"result": 5000.0}

    mock_get.return_value = mock_response

    result = convert_currency(transaction)

    assert result == 5000.0

    mock_get.assert_called_once()

    mock_getenv.assert_called_once_with("API_KEY")
