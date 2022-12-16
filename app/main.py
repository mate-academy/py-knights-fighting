from app.data import KNIGHTS
from knights_battle.battle import knights_battle
from knights.knight import Knight


def battle(knightsconfig: dict) -> dict:
    knights_name_lst = []
    for name, knight_info in knightsconfig.items():
        name = Knight(name, knight_info["power"], knight_info["hp"])
        name.using_armour(knight_info["armour"],
                          knight_info["weapon"]["power"])
        name.using_potion(knight_info["potion"])
        knights_name_lst.append(name)

    first_battle = knights_battle(knights_name_lst[0], knights_name_lst[2])
    second_battle = knights_battle(knights_name_lst[1], knights_name_lst[3])
    result = {
        "Lancelot": first_battle["lancelot"],
        "Artur": second_battle["arthur"],
        "Mordred": first_battle["mordred"],
        "Red Knight": second_battle["red_knight"],
    }
    print(knights_name_lst.append)
    return result


print(battle(KNIGHTS))
