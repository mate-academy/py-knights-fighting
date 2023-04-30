from app.info import KNIGHTS
from app.battle import knight_battle
from app.preparation import preparation


def battle(knights_config: dict) -> dict:
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]
    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        preparation(knight)

    knight_battle(lancelot, mordred)
    knight_battle(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
