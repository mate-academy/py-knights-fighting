from app.knight.one_knight import Knight


def all_knights_create(all_knights_dict: dict) -> list:
    knights_list = []
    for i in all_knights_dict.values():
        one_knight = Knight.one_knight_create({i["name"]: i})
        knights_list.append(one_knight)
    return knights_list
