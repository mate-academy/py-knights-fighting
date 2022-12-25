def knight_points(knights_config: dict) -> dict:
    # knight

    knight = knights_config

    # apply armour
    knight["protection"] = 0
    for properties in knight["armour"]:
        knight["protection"] += properties["protection"]

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
