def setting_knight(knight: dict):
    # apply armour
    knight["protection"] = 0
    for item in knight["armour"]:
        knight["protection"] += item["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion
    if knight["potion"] is not None:
        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

    return knight
