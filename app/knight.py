from collections.abc import Mapping
from typing import Any


def prepare_knight(knight_config: Mapping[str, Any]) -> dict[str, Any]:
    armour = knight_config.get("armour", [])
    protection = sum(item["protection"] for item in armour)
    weapon = knight_config["weapon"]

    stats = {
        "name": knight_config["name"],
        "hp": knight_config["hp"],
        "power": knight_config["power"] + weapon["power"],
        "protection": protection,
    }

    potion = knight_config.get("potion")
    if potion is not None:
        for stat, change in potion["effect"].items():
            stats[stat] += change

    return stats
