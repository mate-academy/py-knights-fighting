from typing import Dict


def apply_armor_and_weapon(knight: Dict) -> None:
    knight["protection"] = sum(item["protection"] for item in knight["armour"])
    knight["power"] += knight["weapon"]["power"]
