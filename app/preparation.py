from typing import Any, Mapping

from app.models import Knight


def prepare_knight(config: Mapping[str, Any]) -> Knight:
    protection = sum(part["protection"] for part in config["armour"])
    power = config["power"] + config["weapon"]["power"]
    hp = config["hp"]

    potion = config["potion"]
    if potion is not None:
        effect = potion["effect"]
        power += effect.get("power", 0)
        protection += effect.get("protection", 0)
        hp += effect.get("hp", 0)

    return Knight(
        name=config["name"],
        hp=hp,
        power=power,
        protection=protection,
    )
