from app.data import KNIGHTS
from app.fight import knights_fight
from app.knight import Knight


def battle(knights: dict) -> dict:
    knights_dict = {}

    for knight, knight_info in knights.items():
        knight = Knight(knight, knight_info["power"], knight_info["hp"])
        knight.is_armour(knight_info["armour"])
        knight.is_weapon(knight_info["weapon"]["power"])
        knight.is_potion(knight_info["potion"])
        knights_dict[knight.name] = knight

    first_fight = knights_fight(
        knights_dict["lancelot"],
        knights_dict["mordred"]
    )
    second_fight = knights_fight(
        knights_dict["arthur"],
        knights_dict["red_knight"]
    )

    result = {
        "Lancelot": first_fight["lancelot"],
        "Artur": second_fight["arthur"],
        "Mordred": first_fight["mordred"],
        "Red Knight": second_fight["red_knight"]
    }
    return result


print(battle(KNIGHTS))
