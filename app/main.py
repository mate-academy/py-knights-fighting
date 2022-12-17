from app.data import KNIGHTS
from knights_battle.battle import knights_battle
from knights.knight import Knight


def battle(knightsconfig: dict) -> dict:
    knights_name_dct = {}
    for knight, knight_info in knightsconfig.items():
        knight = Knight(knight, knight_info["power"], knight_info["hp"])
        knight.using_armour(knight_info["armour"],
                            knight_info["weapon"]["power"])
        knight.using_potion(knight_info["potion"])
        knights_name_dct[knight.name] = knight

    first_battle = knights_battle(knights_name_dct["lancelot"],
                                  knights_name_dct["mordred"])
    second_battle = knights_battle(knights_name_dct["arthur"],
                                   knights_name_dct["red_knight"])
    result = {
        "Lancelot": first_battle["lancelot"],
        "Artur": second_battle["arthur"],
        "Mordred": first_battle["mordred"],
        "Red Knight": second_battle["red_knight"],
    }
    print(knights_name_dct)
    return result


print(battle(KNIGHTS))
