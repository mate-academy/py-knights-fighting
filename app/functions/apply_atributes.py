def apply_attributes(knight: dict) -> None:
    # Apply armour
    knight["protection"] = sum(a["protection"] for a in knight["armour"])

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if exists
    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]
        knight["power"] += potion_effect.get("power", 0)
        knight["protection"] += potion_effect.get("protection", 0)
        knight["hp"] += potion_effect.get("hp", 0)
