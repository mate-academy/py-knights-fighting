def get_ready(knights_config: dict) -> dict:
    # lancelot
    lancelot = knights_config["lancelot"]

    # apply armour
    lancelot["protection"] = 0
    for part in lancelot["armour"]:
        lancelot["protection"] += part["protection"]

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    if lancelot["potion"] is not None:
        for effect in lancelot["potion"]["effect"]:
            lancelot[effect] += lancelot["potion"]["effect"][effect]

    # arthur
    arthur = knights_config["arthur"]

    # apply armour
    arthur["protection"] = 0
    for part in arthur["armour"]:
        arthur["protection"] += part["protection"]

    # apply weapon
    arthur["power"] += arthur["weapon"]["power"]

    # apply potion if exist
    if arthur["potion"] is not None:
        for effect in arthur["potion"]["effect"]:
            arthur[effect] += arthur["potion"]["effect"][effect]

    # mordred
    mordred = knights_config["mordred"]

    # apply armour
    mordred["protection"] = 0
    for part in mordred["armour"]:
        mordred["protection"] += part["protection"]

    # apply weapon
    mordred["power"] += mordred["weapon"]["power"]

    # apply potion if exist
    if mordred["potion"] is not None:
        for effect in mordred["potion"]["effect"]:
            mordred[effect] += mordred["potion"]["effect"][effect]

    # red_knight
    red_knight = knights_config["red_knight"]

    # apply armour
    red_knight["protection"] = 0
    for part in red_knight["armour"]:
        red_knight["protection"] += part["protection"]

    # apply weapon
    red_knight["power"] += red_knight["weapon"]["power"]

    # apply potion if exist
    if red_knight["potion"] is not None:
        for effect in red_knight["potion"]["effect"]:
            red_knight[effect] += red_knight["potion"]["effect"][effect]

    return knights_config
