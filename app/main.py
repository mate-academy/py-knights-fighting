from app.knights import KNIGHTS
from app.apply import apply
from app.fight import fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = knights_config["lancelot"]
    apply(lancelot)

    # arthur
    arthur = knights_config["arthur"]
    apply(arthur)

    # mordred
    mordred = knights_config["mordred"]
    apply(mordred)

    # red_knight
    red_knight = knights_config["red_knight"]
    apply(red_knight)
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
