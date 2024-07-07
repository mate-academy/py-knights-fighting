from app.battle_preparations import use_power_ups
from app.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:
    for knight in knights_config.values():
        use_power_ups(knight)

    lancelot = knights_config["lancelot"]
    arthur = knights_config["arthur"]
    mordred = knights_config["mordred"]
    red_knight = knights_config["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    lancelot["hp"] = max(0, lancelot["hp"])
    mordred["hp"] = max(0, mordred["hp"])
    arthur["hp"] = max(0, arthur["hp"])
    red_knight["hp"] = max(0, red_knight["hp"])

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
