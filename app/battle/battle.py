from app.knights.effects import apply_effects
from app.knights.armor_and_weapon import apply_armor_and_weapon

from typing import Dict


def battle(knightsconfig: Dict[str, Dict]) -> Dict[str, int]:

    for knight in knightsconfig.values():
        apply_armor_and_weapon(knight)
        apply_effects(knight)

    # Fight sequences
    lancelot = knightsconfig["lancelot"]
    mordred = knightsconfig["mordred"]
    arthur = knightsconfig["arthur"]
    red_knight = knightsconfig["red_knight"]

    # Battle sequence
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # Ensure HP doesn't go negative
    for knight in knightsconfig.values():
        knight["hp"] = max(0, knight["hp"])

    return {knight["name"]: knight["hp"] for knight in knightsconfig.values()}
