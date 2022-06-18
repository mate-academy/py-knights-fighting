from app.knights import knights
import app.battle_preparation as bp
import app.fight as fgt


def battle(knights_config):
    # BATTLE PREPARATIONS:
    # lancelot
    lancelot = knights_config["lancelot"]

    # arthur
    arthur = knights_config["arthur"]

    # mordred
    mordred = knights_config["mordred"]

    # red_knight
    red_knight = knights_config["red_knight"]

    bp.battle_preparation(red_knight, lancelot, arthur, mordred)

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    fgt.fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fgt.fight(arthur, red_knight)
    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(knights))
