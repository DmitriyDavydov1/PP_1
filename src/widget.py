from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    "Функция, которая преобразует номер карты и счета"


    account_card_new = account_card.split()
    name_mask = []
    mask = ""
    for i in account_card_new:
        a = i.isalpha()
        if a:
            name_mask.append(i)
        else:
            mask = i
    if 'Счет' in name_mask:
        mask1 = get_mask_account(mask)
    elif 'Счёт' in name_mask:
        mask1 = get_mask_account(mask)
    elif 'счет' in name_mask:
        mask1 = get_mask_account(mask)
    elif 'счёт' in name_mask:
        mask1 = get_mask_account(mask)
    else:
        mask1 = get_mask_card_number(mask)
    name_mask_new = " ".join(name_mask)
    mask_account = name_mask_new + " " + mask1
    return mask_account


print(mask_account_card("Счет 12345678912345678912"))
print(mask_account_card("Visa Classic 1234567891234567"))
print(mask_account_card("Mastercard 9874567891231212"))



from datetime import datetime
def get_data(data: str): -> str:
    "Функция которая преобразует дату"


    d = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S:%F"))
    return d.strftime("%d.%M.%Y")

get_data(2018-07-11T02:26:18.671407)
