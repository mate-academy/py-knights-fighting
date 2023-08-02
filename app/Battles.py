from typing import Dict
from app.knights import apply_armour, apply_weapon, apply_potion


def calculate_damage(attacker: Dict[str, int], 
                     defender: Dict[str, int]) -> int:
    return max(attacker["power"] - defender["protection"], 0)


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    for knight_name, knight in knights_config.items():
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot_damage = calculate_damage(lancelot, mordred)
    mordred_damage = calculate_damage(mordred, lancelot)
    lancelot["hp"] -= mordred_damage
    mordred["hp"] -= lancelot_damage

    # 2 Arthur vs Red Knight:
    arthur_damage = calculate_damage(arthur, red_knight)
    red_knight_damage = calculate_damage(red_knight, arthur)
    arthur["hp"] -= red_knight_damage
    red_knight["hp"] -= arthur_damage

    # check if someone fell in battle
    for knight in [lancelot, mordred, arthur, red_knight]:
        if knight["hp"] <= 0:
            knight["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
