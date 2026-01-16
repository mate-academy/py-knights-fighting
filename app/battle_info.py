from typing import Dict

from app.knight_config import KNIGHT_CONFIG


def apply_effects(character: KNIGHT_CONFIG) -> None:
    character["protection"] = sum(
        armor_piece["protection"] for armor_piece in character["armour"]
    )

    character["power"] += character["weapon"]["power"]

    if character["potion"] is not None:
        for effect_type, value in character["potion"]["effect"].items():
            if effect_type in character:
                character[effect_type] += value


def battle(knights_config: Dict[str, KNIGHT_CONFIG]) -> Dict[str, int]:
    for knight in knights_config.values():
        apply_effects(knight)

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for attacker_name, defender_name in battles:
        attacker = knights_config[attacker_name]
        defender = knights_config[defender_name]

        damage_to_defender = max(attacker["power"] - defender["protection"], 0)
        damage_to_attacker = max(defender["power"] - attacker["protection"], 0)

        defender["hp"] -= damage_to_defender
        attacker["hp"] -= damage_to_attacker

        defender["hp"] = max(defender["hp"], 0)
        attacker["hp"] = max(attacker["hp"], 0)

    return {knight["name"]: knight["hp"] for knight in knights_config.values()}
