def apply_effects(knight):
    # Apply armour
    knight["protection"] = sum(a["protection"] for a in knight["armour"])

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if it exists
    if knight["potion"] is not None:
        potion_effects = knight["potion"]["effect"]
        if "power" in potion_effects:
            knight["power"] += potion_effects["power"]
        if "protection" in potion_effects:
            knight["protection"] += potion_effects["protection"]
        if "hp" in potion_effects:
            knight["hp"] += potion_effects["hp"]
