from app.data import KNIGHTS
from app.battle import knights_battle
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    knights_dict = {}

    for knight, knight_info in knights_config.items():
        knight = Knight(knight, knight_info["power"], knight_info["hp"])
        knight.using_armour(knight_info["armour"])
        knight.using_weapon(knight_info["weapon"]["power"])
        knight.using_potion(knight_info["potion"])
        knights_dict[knight.name] = knight

    first_battle = knights_battle(
        knights_dict["lancelot"],
        knights_dict["mordred"]
    )
    second_battle = knights_battle(
        knights_dict["arthur"],
        knights_dict["red_knight"]
    )

    result = {
        "Lancelot": first_battle["lancelot"],
        "Artur": second_battle["arthur"],
        "Mordred": first_battle["mordred"],
        "Red Knight": second_battle["red_knight"]
    }

    return result


print(battle(KNIGHTS))
