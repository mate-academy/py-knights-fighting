from typing import Any

KnightConfig = dict[str, Any]
PreparedKnight = dict[str, Any]


def prepare_knight(knight: KnightConfig) -> PreparedKnight:
    prepared_knight = {
        "name": knight["name"],
        "hp": knight["hp"],
        "power": knight["power"],
        "protection": 0,
    }

    for armour_part in knight["armour"]:
        prepared_knight["protection"] += armour_part["protection"]

    prepared_knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]

        prepared_knight["hp"] += potion_effect.get("hp", 0)
        prepared_knight["power"] += potion_effect.get("power", 0)
        prepared_knight["protection"] += potion_effect.get("protection", 0)

    return prepared_knight
