from knights import KNIGHTS
from preparation import prepare_knights
from fight import fight


def prepare_battle(knights_config: dict) -> dict:
    return prepare_knights(knights_config)


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights_config = prepare_battle(knights_config)

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1. Lancelot vs Mordred
    fight(lancelot, mordred)

    # 2. Arthur vs Red Knight
    fight(arthur, red_knight)

    # Return battle results
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
