from typing import Any, Dict, Optional

from app.knights.equipment import ArmourPart, Potion, Weapon
from app.knights.knight import Knight


def create_potion(config: Optional[Dict[str, Any]]) -> Optional[Potion]:
    if config is None:
        return None
    return Potion(name=config["name"], effect=config["effect"])


def create_knight(config: Dict[str, Any]) -> Knight:
    return Knight(
        name=config["name"],
        base_power=config["power"],
        base_hp=config["hp"],
        weapon=Weapon(
            name=config["weapon"]["name"],
            power=config["weapon"]["power"],
        ),
        armour=[
            ArmourPart(part=part["part"], protection=part["protection"])
            for part in config.get("armour", [])
        ],
        potion=create_potion(config.get("potion")),
    )


def create_knights(
    knights_config: Dict[str, Dict[str, Any]],
) -> Dict[str, Knight]:
    return {
        key: create_knight(config)
        for key, config in knights_config.items()
    }
