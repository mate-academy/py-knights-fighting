from typing import Dict

from app.knights.effects import apply_effects
from app.knights.armor_and_weapon import apply_armor_and_weapon


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:

    for knight in knights_config.values():
        apply_armor_and_weapon(knight)
        apply_effects(knight)

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in knights_config.values():
        knight["hp"] = max(0, knight["hp"])

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}
