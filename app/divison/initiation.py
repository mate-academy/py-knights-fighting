def init(knights: dict) -> dict:
    for key, value in knights.items():
        value["protection"] = 0

        for am in value["armour"]:
            value["protection"] += am["protection"]

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

    return knights
