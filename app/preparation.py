def battle_preparation(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    prepared_knights = {}
    # lancelot
    lancelot = knights_config["lancelot"]

    # apply armour
    lancelot["protection"] = 0
    for a in lancelot["armour"]:
        lancelot["protection"] += a["protection"]

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            lancelot["protection"] += lancelot["potion"]["effect"]["protection"]

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    prepared_knights["lancelot"] = lancelot

    # arthur
    arthur = knights_config["arthur"]

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

    prepared_knights["arthur"] = arthur

    # mordred
    mordred = knights_config["mordred"]

    # apply armour
    mordred["protection"] = 0
    for a in mordred["armour"]:
        mordred["protection"] += a["protection"]

    # apply weapon
    mordred["power"] += mordred["weapon"]["power"]

    # apply potion if exist
    if mordred["potion"] is not None:
        if "power" in mordred["potion"]["effect"]:
            mordred["power"] += mordred["potion"]["effect"]["power"]

        if "protection" in mordred["potion"]["effect"]:
            mordred["protection"] += mordred["potion"]["effect"]["protection"]

        if "hp" in mordred["potion"]["effect"]:
            mordred["hp"] += mordred["potion"]["effect"]["hp"]

    prepared_knights["mordred"] = mordred

    # red_knight
    red_knight = knights_config["red_knight"]

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

    prepared_knights["red_knight"] = red_knight

    return prepared_knights
