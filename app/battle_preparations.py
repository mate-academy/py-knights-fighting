from typing import Dict, Any, List


def apply_equipment(knight: Dict[str, Any]) -> None:
    knight["protection"] = sum(
        a.get("protection", 0) for a in knight.get("armour", [])
    )

    weapon = knight.get("weapon")
    if weapon:
        knight["power"] += weapon.get("power", 0)

    potion = knight.get("potion")
    if potion:
        effects = potion.get("effect", {})
        knight["power"] += effects.get("power", 0)
        knight["protection"] += effects.get("protection", 0)
        knight["hp"] += effects.get("hp", 0)


def prepare_all_knights(
    knights_config: Dict[str, Dict[str, Any]], knight_names: List[str]
) -> None:
    for name in knight_names:
        apply_equipment(knights_config[name])
