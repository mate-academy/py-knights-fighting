def knight_config(knight):
    # apply armour
    knight["protection"] = 0
    for a in knight["armour"]:
        knight["protection"] += a["protection"]
    # apply weapon
    knight["power"] += knight["weapon"]["power"]
    # apply potion if exist
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
    return knight
