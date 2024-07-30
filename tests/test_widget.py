import pytest

from src.widget import mask_account_card, get_data


def test_mask_account_card_account(mask_account_rename):
    assert mask_account_card('Счет 12345678912345678912') == mask_account_rename


@pytest.mark.parametrize('account_init, account_rename',
                         [
                             ('Счет 12345678912345678912', 'Счет **8912'),
                             ('Счет 1234567891234567895', 'Счет Неправильный номер счета'),
                             ('Счёт 12345678912345678523', 'Счёт **8523'),
                             ('счёт 12345678912345678523', 'счёт **8523')
                         ])
def test_mask_account_card_account_par(account_init, account_rename):
    assert mask_account_card(account_init) == account_rename


def test_mask_account_card_card(mask_card_rename):
    assert mask_account_card('Visa Classic 1234567891234567') == mask_card_rename


@pytest.mark.parametrize('mask_init, mask_rename',
                         [
                             ('Visa Classic 1234567891234567', 'Visa Classic 1234 56** **** 4567'),
                             ('Momentum 5914567891234567', 'Momentum 5914 56** **** 4567'),
                             ('Master card 1236547891234567', 'Master card 1236 54** **** 4567'),
                             ('Visa Classic 12345678912347', 'Visa Classic Неправильный номер карты')
                         ])
def test_mask_account_card_card_par(mask_init, mask_rename):
    assert mask_account_card(mask_init) == mask_rename


@pytest.mark.parametrize('data_init, data_rename',
                         [
                             ('2018-07-11T02:26:18.671407', '11.07.2018'),
                             ('2019-02-28T02:26:18.671', '28.02.2019'),
                             ('2023-06-01T01:06:54.51', '01.06.2023'),
                             ('2016-01-01T00:00:00.51', '01.01.2016'),
                             ('', ''),
                         ])
def test_get_data(data_init, data_rename):
    assert get_data(data_init) == data_rename
