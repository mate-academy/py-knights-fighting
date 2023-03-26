from app.battle.battle_preparation import get_equipment
from app.battle.fighting import fight
from app.battle.knights_characteristics import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights_config["lancelot"]
    get_equipment(lancelot)

    # arthur
    arthur = knights_config["arthur"]
    get_equipment(arthur)

    # mordred
    mordred = knights_config["mordred"]
    get_equipment(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]
    get_equipment(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)
    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
