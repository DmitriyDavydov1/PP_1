import masks


def mask_account_card(account_card: str, ) -> str:
    account_card_new = account_card.split()
    name_mask = []
    mask = ""
    for i in account_card_new:
        a = i.isalpha()
        if a:
            name_mask.append(i)
        else:
            mask = i
    print(name_mask)
    print(mask)
    if 'Счет' or 'Счёт' or "счет" or 'счёт' in name_mask:
        mask1 = masks.get_mask_account(mask)
    else:
        mask1 = masks.get_mask_card_number(mask)
    name_mask_new = " ".join(name_mask)
    mask_account = name_mask_new + " " + mask1
    return mask_account


print(mask_account_card("Visa 1234567891234567"))
