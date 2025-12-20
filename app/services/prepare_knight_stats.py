from typing import Any


def prepare_knight_stats(knight_config: dict[str, Any]) -> dict:

    stats = {
        "hp": knight_config["hp"],
        "power": knight_config["power"],
        "protection": 0
    }
    for part in knight_config["armour"]:
        stats["protection"] += part["protection"]
    stats["power"] += knight_config["weapon"]["power"]
    if knight_config["potion"] is not None:
        potion_effect = knight_config["potion"]["effect"]
        stats["hp"] += potion_effect.get("hp", 0)
        stats["power"] += potion_effect.get("power", 0)
        stats["protection"] += potion_effect.get("protection", 0)
    return stats
