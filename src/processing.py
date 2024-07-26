def filter_by_state(list_dict: list[dict[str, str | int]], state: str = "EXECUTED") -> list[dict[str, str | int]]:
    """Функция фильтрации операций по ключу state"""

    sort_dict = []
    for dict_i in list_dict:
        if dict_i.get("state") == state:
            sort_dict.append(dict_i.copy())
        else:
            continue

    return sort_dict


def sort_by_date(list_dict: list[dict[str, str | int]], ascending: bool = True) -> list[dict[str, str | int]]:
    """Функция сортировки операций по дате в порядке убывания"""

    sort_dict_data = sorted(list_dict, key=lambda dict_i: dict_i["date"], reverse=ascending)

    return sort_dict_data
