from typing import Any
from app.knights_templates.knights import KNIGHTS


def apply_effects(knight: dict) -> Any:
    knight["protection"] = sum(part["protection"] for part in knight["armour"])
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"]:
        potion_effect = knight["potion"]["effect"]
        knight["power"] += potion_effect.get("power", 0)
        knight["protection"] += potion_effect.get("protection", 0)
        knight["hp"] += potion_effect.get("hp", 0)


def battle(knights_config: dict) -> dict:
    knights = knights_config.copy()

    for knight_name, knight in knights.items():
        apply_effects(knight)

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for attacker, defender in battles:
        attacker_hp = knights[attacker]["hp"]
        attacker_power = knights[attacker]["power"]
        attacker_protection = knights[attacker]["protection"]
        defender_hp = knights[defender]["hp"]
        defender_power = knights[defender]["power"]
        defender_protection = knights[defender]["protection"]

        attacker_damage = defender_power - attacker_protection
        defender_damage = attacker_power - defender_protection

        knights[attacker]["hp"] = max(0, attacker_hp - attacker_damage)
        knights[defender]["hp"] = max(0, defender_hp - defender_damage)

    # Check if someone fell in battle
    for knight in knights.values():
        if knight["hp"] <= 0:
            knight["hp"] = 0

    # Return battle results
    return {knight["name"]: knight["hp"] for knight in knights.values()}


print(battle(KNIGHTS))
