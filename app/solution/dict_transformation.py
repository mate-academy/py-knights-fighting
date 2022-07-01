def transformation(name: str, knights: dict) -> list:
    knight = knights.get(name)
    knight["protection"] = 0
    for a in knight["armour"]:
        knight["protection"] += a["protection"]
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]
        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
    info = [knight["name"], knight["power"], knight["hp"], knight["protection"]]
    return info
