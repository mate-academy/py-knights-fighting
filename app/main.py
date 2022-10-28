from app.preparation import get_ready
from app.data_of_knights import KNIGHTS
from app.check_fell import check_fell


def battle(main_dict_knights: dict) -> dict:
    preparation = get_ready(main_dict_knights)
    count = 0
    heroes = [person for person in preparation]
    for fight in range(2):
        first, second = preparation[heroes[count]], preparation[heroes[count + 2]]

        first["hp"] -= second["power"] - first["protection"]
        second["hp"] -= first["power"] - second["protection"]
        count += 1

    for person in preparation:
        check = check_fell(preparation[person]["hp"])
        preparation[person]["hp"] = check

    return {
        preparation["lancelot"]["name"]: preparation["lancelot"]["hp"],
        preparation["arthur"]["name"]: preparation["arthur"]["hp"],
        preparation["mordred"]["name"]: preparation["mordred"]["hp"],
        preparation["red_knight"]["name"]: preparation["red_knight"]["hp"],
    }


print(battle(KNIGHTS))
