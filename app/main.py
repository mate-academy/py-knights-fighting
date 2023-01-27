from app.battle.batlle_of_knights import battle_for_two
from app.knight.model import Knight
from app.knight.knight_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    knight_dict = {}

    for knight, knight_info in knights_config.items():
        knight = Knight(knight, knight_info["power"], knight_info["hp"])
        knight.apply_armour(knight_info["armour"])
        knight.apply_weapon(knight_info["weapon"]["power"])
        knight.apply_potion(knight_info["potion"])
        knight_dict[knight.name] = knight

    first_battle = battle_for_two(
        knight_dict["lancelot"],
        knight_dict["mordred"]
    )

    second_battle = battle_for_two(
        knight_dict["arthur"],
        knight_dict["red_knight"]
    )

    result = {
        "Lancelot": first_battle["lancelot"],
        "Artur": second_battle["arthur"],
        "Mordred": first_battle["mordred"],
        "Red Knight": second_battle["red_knight"]
    }

    return result


print(battle(KNIGHTS))
