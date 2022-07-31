def setting_name(name: dict):
    # apply armour
    name["protection"] = 0
    if len(name["armour"]) != 0:
        for a in name["armour"]:
            name["protection"] += a["protection"]

    # apply weapon
    name["power"] += name["weapon"]["power"]

    # apply potion if exist
    if name["potion"] is not None:
        if "power" in name["potion"]["effect"]:
            name["power"] += name["potion"]["effect"]["power"]

        if "protection" in name["potion"]["effect"]:
            name["protection"] += name["potion"]["effect"]["protection"]

        if "hp" in name["potion"]["effect"]:
            name["hp"] += name["potion"]["effect"]["hp"]
    return name
