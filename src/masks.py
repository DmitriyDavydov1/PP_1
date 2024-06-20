def get_mask_card_number(mask_card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается
     в формате XXXX XX** **** XXXX. Т. е. видны первые 6 цифр и последние 4, номер разбит по блокам по 4 цифры,
    разделенным пробелами."""
    digit_1_blok = mask_card[:-12]
    digit_2_blok = mask_card[-8:-4]
    digit_4_blok = mask_card[-4:]
    mask_card_number = digit_1_blok + " " + digit_2_blok[0:2] + "**" + " " + "****" + " " + digit_4_blok
    return mask_card_number


get_mask_card_number(mask_card=input())


def get_mask_account(mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается
    в формате **XXXX. Т. е. видны только последние 4 цифры."""
    mask_account = "**" + mask_account[-4:]
    return mask_account


get_mask_account(mask_account=input())
