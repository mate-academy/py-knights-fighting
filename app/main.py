from app.preparation import set_stats_hero
from app.data_of_knights import KNIGHTS
from app.check_fell import check_fell


def battle(main_dict_knights: dict) -> dict:
    preparation = set_stats_hero(main_dict_knights)

    lancelot = preparation["lancelot"]
    mordred = preparation["mordred"]
    arthur = preparation["arthur"]
    red_knight = preparation["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

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
