from src.masks import get_mask_account
from src.masks import get_mask_card_number
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """Функция, которая преобразует номер карты и счета"""

    account_card_new = account_card.split()
    name_mask = []
    mask = ""
    for i in account_card_new:
        a = i.isalpha()
        if a:
            name_mask.append(i)
        else:
            mask = i
    if "Счет" in name_mask or "Счёт" in name_mask or "счет" in name_mask or "счёт" in name_mask:
        mask1 = get_mask_account(mask)
    else:
        mask1 = get_mask_card_number(mask)
    mask_account = " ".join(name_mask) + " " + mask1
    return mask_account


def get_data(data_string: str) -> str:
    """Функция, которая преобразует дату"""

    if data_string == "":
        return ""
    else:
        d = datetime.strptime(data_string, format("%Y-%m-%dT%H:%M:%S.%f"))
        return d.strftime(format("%d.%m.%Y"))
