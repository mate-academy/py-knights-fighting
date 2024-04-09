def knight_preparations(knights_config: dict) -> dict:
    knight = knights_config
    # apply armour
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"]:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]

    return knight
