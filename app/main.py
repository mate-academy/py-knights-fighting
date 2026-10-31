from app.knights import KNIGHTS
from app.apply_potion import apply_potion
from app.apply_armor_and_weapon import apply_armour
from app.apply_armor_and_weapon import apply_weapon
from app.battle import check


def battle(knights_config: dict) -> dict:
    for element in knights_config:
        knight = knights_config[element]
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    check(lancelot, mordred)
    check(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


if __name__ == "__main__":
    config_mock = KNIGHTS() if isinstance(KNIGHTS, type) else KNIGHTS
    print(battle(config_mock))
