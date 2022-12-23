def red_knight_points(knights_config: dict) -> dict:
    # red_knight
    red_knight = knights_config

    # apply armour
    red_knight["protection"] = 0
    for properties in red_knight["armour"]:
        red_knight["protection"] += properties["protection"]

    # apply weapon
    red_knight["power"] += red_knight["weapon"]["power"]

    # apply potion if exist
    if red_knight["potion"] is not None:
        if "power" in red_knight["potion"]["effect"]:
            red_knight["power"] \
                += red_knight["potion"]["effect"]["power"]

        if "protection" in red_knight["potion"]["effect"]:
            red_knight["protection"] \
                += red_knight["potion"]["effect"]["protection"]

        if "hp" in red_knight["potion"]["effect"]:
            red_knight["hp"] += red_knight["potion"]["effect"]["hp"]
    return red_knight
