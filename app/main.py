# app/main.py

from typing import Dict, List, Optional, Tuple

from app.constants import KNIGHTS
from app.equipment import ArmourPart, Potion, Weapon
from app.knight import Knight


def _perform_duel(knight1: Knight, knight2: Knight) -> None:
    """Each knight attacks the other once."""
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)


def battle(
    knights_config: Dict[str, Dict],
    duels: Optional[List[Tuple[str, str]]] = None,
) -> Dict[str, int]:
    # Default duel pairings if none provided
    if duels is None:
        duels = [("lancelot", "mordred"), ("arthur", "red_knight")]

    # Create Knight instances from config
    knights: Dict[str, Knight] = {}
    for key, data in knights_config.items():
        armour_objs = [ArmourPart.from_dict(a) for a in data.get("armour", [])]
        weapon_obj = Weapon.from_dict(data["weapon"])
        potion_obj = (
            Potion.from_dict(data["potion"]) if data.get("potion") else None
        )
        knights[key] = Knight(
            name=data["name"],
            base_hp=data["hp"],
            base_power=data["power"],
            armour=armour_objs,
            weapon=weapon_obj,
            potion=potion_obj,
        )

    # Run all specified duels
    for name1, name2 in duels:
        _perform_duel(knights[name1], knights[name2])

    # Return final HP values
    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
