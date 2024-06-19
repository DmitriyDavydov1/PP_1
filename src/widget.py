def mask_account_card(account_card: str) -> str:
    account_card_new = account_card.split()
    name_mask = []
    mask = []
    mask_card = []
    mask_account = []
    for i in account_card_new:
        a = i.isalpha()
        if a:
            name_mask.append(i)
        else:
            mask.append(i)
    if len(mask) == 16:
        mask_new = get_mask_card_number(mask_card=mask)
    else:
        mask_new = get_mask_account(mask_account=mask)
    name_mask_new = " ".join(name_mask)
    mask_account_card = name_mask_new + mask_new

    return mask_account_card


print(mask_account_card)