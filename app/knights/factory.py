from typing import Any

from app.knights.models import Knight, Armour, Weapon, Potion


def prepare_knight(config: dict[str, Any]) -> Knight:
    armour = [Armour(**part) for part in config.get("armour", [])]
    weapon = Weapon(**config["weapon"])
    potion_data = config.get("potion")
    potion = Potion(**potion_data) if potion_data else None

    return Knight(
        name=config["name"],
        base_power=config["power"],
        base_hp=config["hp"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )
