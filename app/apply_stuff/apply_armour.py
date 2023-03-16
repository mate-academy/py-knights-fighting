def apply_armour(knight: dict) -> None:
    knight["protection"] = 0
    for armour in knight.get("armour"):
        knight["protection"] += armour.get("protection")
