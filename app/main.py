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
        kn = Knight(knight)
        kn.apply_point()
        kn.apply_armour()
        kn.apply_weapon()

    fight(knights[0], knights[2])

    check_hp(knights[0])
    check_hp(knights[2])

    fight(knights[1], knights[3])

    check_hp(knights[1])
    check_hp(knights[3])

    return {
        knights[0]["name"]: knights[0]["hp"],
        knights[1]["name"]: knights[1]["hp"],
        knights[2]["name"]: knights[2]["hp"],
        knights[3]["name"]: knights[3]["hp"],
    }
