from typing import Dict

from app.knights.effects import apply_effects
from app.knights.armor_and_weapon import apply_armor_and_weapon


def battle(knight_sconfig: Dict[str, Dict]) -> Dict[str, int]:

    for knight in knight_sconfig.values():
        apply_armor_and_weapon(knight)
        apply_effects(knight)

    lancelot = knight_sconfig["lancelot"]
    mordred = knight_sconfig["mordred"]
    arthur = knight_sconfig["arthur"]
    red_knight = knight_sconfig["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in knight_sconfig.values():
        knight["hp"] = max(0, knight["hp"])

    return {knight["name"]: knight["hp"] for knight in knight_sconfig.values()}
