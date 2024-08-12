from typing import Generator, Any


def filter_by_currency(transactions: list, code_transactions: str) -> Any:
    """Функция возвращающая итератор, который поочередно выдает транзакции, где валюта соответствует заданной"""
    filtered_transactions = list(
        filter(
            lambda transaction: transaction.get("operationAmount").get("currency").get("code") == code_transactions,
            transactions,
        )
    )
    if len(filtered_transactions) > 0:
        return iter(filtered_transactions)
    else:
        return


def transaction_descriptions(transactions: list) -> Any:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """Функция может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for x in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(x))] + str(x)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
