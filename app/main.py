from app.data.knights_config import KNIGHTS
from app.knight_package.knights import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    knight_names = ["lancelot", "mordred", "arthur", "red_knight"]
    knights = {name: Knight(knights_config[name]) for name in knight_names}

    for knight in knights.values():
        knight.battle_preparation()

    # BATTLE:

    duels = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for knight1_name, knight2_name in duels:
        knights[knight1_name].attack(knights[knight2_name])
        knights[knight2_name].attack(knights[knight1_name])

    # Return battle results:
    return {
        name.title().replace("_", " "): knight.hp
        for name, knight in knights.items()
    }


print(battle(KNIGHTS))
