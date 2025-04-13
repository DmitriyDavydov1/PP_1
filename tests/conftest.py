import pytest


@pytest.fixture
def mask_account_rename():
    return 'Счет **8912'


@pytest.fixture
def mask_card_rename():
    return 'Visa Classic 1234 56** **** 4567'


@pytest.fixture
def sort_by_date_init():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]

@pytest.fixture
def transactions():
    return [
          {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
              "amount": "31957.58",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
          },
          {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
              "amount": "8221.37",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
          },
          {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
              "amount": "9824.07",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
          }
]

@pytest.fixture
def transaction():
    return {
                "operationAmount": {
                "amount": "31957.58",
                "currency": {
                "code": "RUB"
                }
            }
    }
