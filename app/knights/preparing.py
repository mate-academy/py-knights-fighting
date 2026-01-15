from app.knights.knight import Knight


def knights_preparing(knights: dict) -> list:
    knights_prepared = []
    for knight in knights.values():
        knight["power"] += knight["weapon"]["power"]
        knight["protect"] = 0
        for armour in knight["armour"]:
            knight["protect"] += armour["protection"]
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]
            if "protection" in knight["potion"]["effect"]:
                knight["protect"] += knight["potion"]["effect"]["protection"]
            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]
        knights_prepared.append(Knight(knight.get("name"),
                                       knight.get("power"),
                                       knight.get("hp"),
                                       knight.get("protect")))
    return knights_prepared
