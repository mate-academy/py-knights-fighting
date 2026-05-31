from typing import Any

KnightConfig = dict[str, Any]


def strip_knight(knight: KnightConfig) -> KnightConfig:
    p_knight = {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"],
        "protection": 0,
    }

    for armour_part in knight["armour"]:
        p_knight["protection"] += armour_part["protection"]

    p_knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]

        p_knight["hp"] += potion_effect.get("hp", 0)
        p_knight["power"] += potion_effect.get("power", 0)
        p_knight["protection"] += potion_effect.get("protection", 0)

    return p_knight
