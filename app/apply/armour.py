def apply_armour(knight: dict) -> int:
    knight["protection"] = 0
    for part in knight["armour"]:
        knight["protection"] += part["protection"]
    return knight["protection"]
