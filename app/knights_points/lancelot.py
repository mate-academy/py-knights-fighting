def lencelot_points(knights_config: dict) -> dict:
    # lancelot
    lancelot = knights_config

    # apply armour
    lancelot["protection"] = 0
    for properties in lancelot["armour"]:
        lancelot["protection"] += properties["protection"]

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] \
                += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            lancelot["protection"] \
                += lancelot["potion"]["effect"]["protection"]

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] \
                += lancelot["potion"]["effect"]["hp"]
    return lancelot
