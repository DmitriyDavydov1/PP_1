from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == ''


def test_get_mask_card_number():
    assert get_mask_card_number('1234123568659845') == '1234 12** **** 9845'


def test_get_mask_card_number_len():
    assert get_mask_card_number('123412356865984521') == 'Неправильный номер карты'


def test_get_mask_account_empty():
    assert get_mask_account('') == ''


def test_get_mask_account():
    assert get_mask_account('12365498712365489782') == '**9782'


def test_get_mask_account_len():
    assert get_mask_account('498712') == 'Неправильный номер счета'
