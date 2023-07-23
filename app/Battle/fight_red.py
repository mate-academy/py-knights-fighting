def fights_red(knightsConfig):
    red_knight = knightsConfig["red_knight"]

    # apply armour
    red_knight["protection"] = 0
    for a in red_knight["armour"]:
        red_knight["protection"] += a["protection"]

    # apply weapon
        red_knight["power"] += red_knight["weapon"]["power"]

    # apply potion if exist
    if red_knight["potion"] is not None:
        if "power" in red_knight["potion"]["effect"]:
            red_knight["power"] += red_knight["potion"]["effect"]["power"]

    if "protection" in red_knight["potion"]["effect"]:
        red_knight["protection"] += red_knight["potion"]["effect"]["protection"]

    if "hp" in red_knight["potion"]["effect"]:
        red_knight["hp"] += red_knight["potion"]["effect"]["hp"]