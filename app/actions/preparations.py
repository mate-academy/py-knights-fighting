def battle_preparations(knights_config: dict) -> dict:
    new_knights = knights_config.copy()
    for key, value in knights_config.items():
        # apply armour
        value["protection"] = 0
        for protections in value["armour"]:
            value["protection"] += protections["protection"]

        # apply weapon
        value["power"] += value["weapon"]["power"]

        # apply potion if exist
        if value["potion"] is not None:
            if "power" in value["potion"]["effect"]:
                value["power"] += value["potion"]["effect"]["power"]
            if "protection" in value["potion"]["effect"]:
                value["protection"] += value["potion"]["effect"]["protection"]
            if "hp" in value["potion"]["effect"]:
                value["hp"] += value["potion"]["effect"]["hp"]

        new_knights[key] = value
    return new_knights
