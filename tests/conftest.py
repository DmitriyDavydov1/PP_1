import pytest


@pytest.fixture
def mask_account_rename():
    return 'Счет **8912'


@pytest.fixture
def mask_card_rename():
    return 'Visa Classic 1234 56** **** 4567'
