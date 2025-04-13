from unittest.mock import Mock, patch, MagicMock

from src.external_api import API_KEY, amount_transaction_in_rubles

# Функция для мокирования API-ответа
def create_mock_response(json_data, status_code: int) -> MagicMock:
    """Создает мок-объект ответа."""
    mock_response = MagicMock()
    mock_response.json.return_value = json_data
    mock_response.status_code = status_code
    return mock_response

@patch("requests.get")
def test_usd_transaction(mock_get: MagicMock) -> None:
    """Проверяет, что функция правильно обрабатывает транзакции в долларах (USD), мокируя API-запрос."""

    transaction = {"operationAmount": {"amount": "8221.37", "currency": {"code": "RUB"}}}
    mock_response = create_mock_response({"result": 8221.37}, 200)
    mock_get.return_value = mock_response
    result = amount_transaction_in_rubles(transaction)
    assert result == 8221.37
