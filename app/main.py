from app.knights_original_list import KNIGHTS
from app.battle_preparations import Knights


def battle(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:

    lancelot = Knights(knights_config["lancelot"])
    arthur = Knights(knights_config["arthur"])
    mordred = Knights(knights_config["mordred"])
    red_knight = Knights(knights_config["red_knight"])
    # -------------------------------------------------------------------------------
    # BATTLE:

    # # 1 Lancelot vs Mordred:
    lancelot.holding_a_battle(mordred)

    # # 2 Arthur vs Red Knight:
    arthur.holding_a_battle(red_knight)

    # Return battle result:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
