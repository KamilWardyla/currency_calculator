from unittest import mock
from currency_calculator.__main__ import calculate, get_exchange_rate


def test_calculate():
    amount = 100.0
    currency = 'USD'

    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'rates': [{'mid': 3.80}]}

    with mock.patch('requests.get', return_value=mock_response):
        result = calculate(amount, currency)

    assert result == 380.0


def test_get_exchange_rate():
    currency = 'USD'
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'rates': [{'mid': 3.80}]}

    with mock.patch('requests.get', return_value=mock_response):
        exchange_rate = get_exchange_rate(currency)

    assert exchange_rate == 3.80
