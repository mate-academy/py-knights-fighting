from app.knights import KNIGHTS
from app.battle_preparation import battle_preparation
from app.battle import k_battle


def battle(knights_config: dict) -> dict:
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]
    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        battle_preparation(knight)

    k_battle(lancelot, mordred)
    k_battle(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
