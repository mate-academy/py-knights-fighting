from app.battle_preparation import prepare_knight
from app.battle import fight


def battle(knights_config: dict) -> dict:
    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    for knight in knights_config.values():
        prepare_knight(knight)

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
