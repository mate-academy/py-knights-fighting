def fights_arthur(knightsConfig):
    arthur = knightsConfig["arthur"]

    # apply armour
    arthur["protection"] = 0
    for a in arthur["armour"]:
        arthur["protection"] += a["protection"]

    # apply weapon
    arthur["power"] += arthur["weapon"]["power"]

    # apply potion if exist
    if arthur["potion"] is not None:
        if "power" in arthur["potion"]["effect"]:
            arthur["power"] += arthur["potion"]["effect"]["power"]

        if "protection" in arthur["potion"]["effect"]:
            arthur["protection"] += arthur["potion"]["effect"]["protection"]

        if "hp" in arthur["potion"]["effect"]:
            arthur["hp"] += arthur["potion"]["effect"]["hp"]