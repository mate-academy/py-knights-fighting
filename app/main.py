from app.data import KNIGHTS
from app.pvp_battle import knight_battle
from app.knights_config import KnightInfo


def battle(knights_config: dict) -> dict:

    knights = {}

    for knight, knight_info in knights_config.items():
        knight = KnightInfo(knight, knight_info["power"], knight_info["hp"])
        knight.using_armour(knight_info["armour"])
        knight.using_potion(knight_info["potion"])
        knight.using_weapon(knight_info["weapon"]["power"])
        knights[knight.name] = knight

    first_battle = knight_battle(
        knights["lancelot"],
        knights["mordred"]
    )

    second_battle = knight_battle(
        knights["arthur"],
        knights["red_knight"]
    )

    return {
        "Lancelot": first_battle["lancelot"],
        "Artur": second_battle["arthur"],
        "Mordred": first_battle["mordred"],
        "Red Knight": second_battle["red_knight"]
    }


print(battle(KNIGHTS))
