def preparation_red_knight(knight_config: dict) -> dict:
    red_knight = knight_config["red_knight"]

    red_knight["protection"] = 0
    for armour in red_knight["armour"]:
        red_knight["protection"] += armour["protection"]

    red_knight["power"] += red_knight["weapon"]["power"]

    if red_knight["potion"] is not None:
        if "power" in red_knight["potion"]["effect"]:
            red_knight["power"] += red_knight["potion"]["effect"]["power"]

        if "protection" in red_knight["potion"]["effect"]:
            protect = red_knight["potion"]["effect"]["protection"]
            red_knight["protection"] += protect

        if "hp" in red_knight["potion"]["effect"]:
            red_knight["hp"] += red_knight["potion"]["effect"]["hp"]

    return red_knight
