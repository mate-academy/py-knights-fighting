from app.combat.battle_preparations import (apply_armour,
                                            apply_weapon,
                                            apply_potion)
from app.combat.fighting import (check_if_knight_fell,
                                 calculate_health_remainder)
from app.warriors.config import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    for knight in knights_config.values():
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    calculate_health_remainder(knight=lancelot, enemy=mordred)
    calculate_health_remainder(knight=mordred, enemy=lancelot)

    # 2 Arthur vs Red Knight:
    calculate_health_remainder(knight=arthur, enemy=red_knight)
    calculate_health_remainder(knight=red_knight, enemy=arthur)

    # check if someone fell in battle
    for knight in knights_config.values():
        check_if_knight_fell(knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
