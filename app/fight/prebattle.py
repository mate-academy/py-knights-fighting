from typing import Dict, Any
from app.knights.knight import Knight
from app.knights.equipment import Weapon, ArmourPart, Potion


def prepare_knight(knight_config: Dict[str, Any]) -> Knight:
    armour_objects = [
        ArmourPart(parts=a["part"], protection=a["protection"])
        for a in knight_config.get("armour", [])
    ]
    weapon_config = knight_config["weapon"]
    weapon_object = Weapon(
        name=weapon_config["name"],
        power=weapon_config["power"]
    )

    potion_object = None
    potion_config = knight_config.get("potion")
    if potion_config:
        potion_object = Potion(
            name=potion_config["name"],
            effect=potion_config["effect"]
        )
    return Knight(
        name=knight_config["name"],
        power=knight_config["power"],
        hp=knight_config["hp"],
        weapon=weapon_object,
        armour=armour_objects,
        potion=potion_object,
    )


def prepare_all_knights(knights_data: Dict[str, Dict]) -> Dict[str, Knight]:
    ready_knights = {}
    for key, config in knights_data.items():
        ready_knights[key] = prepare_knight(config)
    return ready_knights
