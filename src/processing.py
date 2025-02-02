def filter_by_state(list_dict: list[dict[str, str | int]], state: str = "EXECUTED") -> list[dict[str, str | int]]:
    """Функция фильтрации операций по ключу state"""

    sort_dict = []
    for dict_i in list_dict:
        if dict_i.get("state") == state:
            sort_dict.append(dict_i.copy())
        else:
            continue

    return sort_dict


filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)


def sort_by_date(list_dict: list[dict[str, str | int]], ascending: bool = True) -> list[dict[str, str | int]]:
    """Функция сортировки операций по дате в порядке убывания"""

    sort_dict_data = sorted(list_dict, key=lambda dict_i: dict_i["date"], reverse=ascending)

    return sort_dict_data


sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)
