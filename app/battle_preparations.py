def use_power_ups(knight: dict) -> None:
    knight["protection"] = 0

    for armour_piece in knight["armour"]:
        knight["protection"] += armour_piece["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight.get("potion", False):
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]
        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
