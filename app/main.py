from app.battle.fight_and_check_hp import check_hp, fight
from app.battle.Knight import Knight


def battle(knights_config: dict) -> dict:
    knights = [
        knights_config["lancelot"],
        knights_config["arthur"],
        knights_config["mordred"],
        knights_config["red_knight"]
    ]

    for knight in knights:
        new_knight_instance = Knight(knight)
        new_knight_instance.apply_point()
        new_knight_instance.apply_armour()
        new_knight_instance.apply_weapon()

    fight(knights[0], knights[2])

    check_hp(knights[0])
    check_hp(knights[2])

    fight(knights[1], knights[3])

    check_hp(knights[1])
    check_hp(knights[3])

    return {
        knight["name"]: knight["hp"]
        for knight in knights[:]
    }
