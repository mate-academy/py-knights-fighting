from app.knights_info import KNIGHTS
from app.knights_preparation import preparation
from app.battles import knight_battle


def battle(knights_config: dict) -> dict:
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    knights = [lancelot, arthur, mordred, red_knight]

    # BATTLE PREPARATION:
    for knight in knights:
        preparation(knight)

    # BATTLE:
    knight_battle(lancelot, mordred)
    knight_battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
