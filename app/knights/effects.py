from typing import Dict


def apply_effects(knight: Dict) -> None:
    if knight["potion"] is not None:
        effects = knight["potion"]["effect"]
        knight["power"] += effects.get("power", 0)
        knight["protection"] += effects.get("protection", 0)
        knight["hp"] += effects.get("hp", 0)
