def configurations(stat):
    stat["protection"] = 0
    for a in stat["armour"]:
        stat["protection"] += a["protection"]

    # apply weapon
    stat["power"] += stat["weapon"]["power"]

    # apply potion if exist
    if stat["potion"] is not None:
        if "power" in stat["potion"]["effect"]:
            stat["power"] += stat["potion"]["effect"]["power"]

        if "protection" in stat["potion"]["effect"]:
            stat["protection"] += stat["potion"]["effect"]["protection"]

        if "hp" in stat["potion"]["effect"]:
            stat["hp"] += stat["potion"]["effect"]["hp"]
