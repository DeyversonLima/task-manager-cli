from unittest.mock import patch
from app.currency_api import get_dollar_exchange_rate


@patch("app.currency_api.requests.get")
def test_get_dollar_exchange_rate(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "USDBRL": {
            "bid": "5.67"
        }
    }
    result = get_dollar_exchange_rate()
    assert result == "\n💵 Dólar hoje: R$ 5.67"
