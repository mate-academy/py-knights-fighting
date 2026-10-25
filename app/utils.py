def prepare(knight: dict) -> dict:
    protection = 0
    for part in knight["armour"]:
        protection += part["protection"]
    knight["protection"] = protection
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"] is not None:
        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]
    return knight
