from app.battle import knights_battle
from app.knight.data import KNIGHTS
from app.knight.modified import ModifiedKnight


def battle(knights_config: dict) -> dict:
    knights_dict = {}

    for knight, knight_config in knights_config.items():
        knight = ModifiedKnight(knight,
                                knight_config["power"],
                                knight_config["hp"])

        knight.mod_armour(knight_config["armour"])
        knight.mod_weapon(knight_config["weapon"])
        knight.mod_potion(knight_config["potion"])

        knights_dict[knight.name] = knight

    first_battle = knights_battle(
        knights_dict["lancelot"],
        knights_dict["mordred"]
    )
    second_battle = knights_battle(
        knights_dict["arthur"],
        knights_dict["red_knight"]
    )

    return {
        "Lancelot": first_battle["lancelot"],
        "Artur": second_battle["arthur"],
        "Mordred": first_battle["mordred"],
        "Red Knight": second_battle["red_knight"]
    }


print(battle(KNIGHTS))
