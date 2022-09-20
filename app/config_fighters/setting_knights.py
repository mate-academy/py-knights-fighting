def setting_knight(knight: dict):
    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply armour
    knight["protection"] = 0
    if "armour" in knight:
        knight["protection"] += knight["armour"]["protection"]

    # apply potion
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
    return knight
