from typing import Dict, Any
from knights_data import KNIGHTS


def apply_potion(knight: Dict[str, Any]) -> Dict[str, Any]:
    if knight.get("potion") is not None:
        potion_effect = knight["potion"].get("effect", {})
        attributes_to_update = ["power", "protection", "hp"]

        for attribute in attributes_to_update:
            if attribute in potion_effect:
                knight[attribute] += potion_effect[attribute]

    return knight


def apply_weapon(knight: Dict[str, Any]) -> Dict[str, Any]:
    if "weapon" in knight:
        knight["power"] += knight["weapon"].get("power", 0)

    return knight
    
