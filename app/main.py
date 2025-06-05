from typing import Dict, Any
from app.knights.equipment import Armour, Weapon, Potion
from app.knights.knight import Knight
from app.knights.battle import battle_all


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    """
    Accepts a configuration dictionary for knights in the following format:
    {
        "lancelot": {
            "name": "Lancelot",
            "power": 35,
            "hp": 100,
            "armour": [ {"part": "...", "protection": ...}, ... ],
            "weapon": {"name": "...", "power": ...},
            "potion": {"name": "...", "effect": {...}}  # or None
        },
        "arthur": { ... },
        "mordred": { ... },
        "red_knight": { ... },
    }

    Creates Knight instances (with their Armour, Weapon, and Potion objects), runs the duels,
    and returns a dictionary mapping each knight's display name to remaining HP.

    Args:
        knights_config (Dict[str, Any]): A nested dict describing each knight's base stats,
            equipped armour pieces, weapon, and optionally a potion.

    Returns:
        Dict[str, int]: A mapping { "Lancelot": remaining_hp, "Arthur": remaining_hp, ... }.
    """
    knights_objs: Dict[str, Knight] = {}

    for key, data in knights_config.items():
        # 1) Build list of Armour objects (if any)
        armour_list = [
            Armour(part=a["part"], protection=a["protection"])
            for a in data.get("armour", []) or []
        ]

        # 2) Instantiate Weapon if provided
        weapon_data = data.get("weapon")
        if weapon_data:
            weapon = Weapon(name=weapon_data["name"], power=weapon_data["power"])
        else:
            weapon = None

        # 3) Instantiate Potion if provided
        potion_data = data.get("potion")
        if potion_data:
            potion = Potion(name=potion_data["name"], effect=potion_data["effect"])
        else:
            potion = None

        # 4) Create Knight instance
        knight = Knight(
            name=data["name"],
            base_power=data["power"],
            base_hp=data["hp"],
            armour=armour_list,
            weapon=weapon,
            potion=potion,
        )

        knights_objs[key] = knight

    # 5) Run the two duels and return results
    return battle_all(knights_objs)
