def apply_armour(knight: dict) -> None:
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]
