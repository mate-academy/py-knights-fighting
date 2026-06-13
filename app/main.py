from app.knights.config import KnightDict
from app.preperation.prepare import prepare_knight


def battle(knights_config: dict[str, KnightDict]) -> dict[str, int]:
    for knight in knights_config.values():
        prepare_knight(knight)

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in knights_config.values():
        if knight["hp"] <= 0:
            knight["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
