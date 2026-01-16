def arthur(dictionary: dict) -> list:
    arthur = dictionary["arthur"]

    arthur["protection"] = 0
    for characteristic in arthur["armour"]:
        arthur["protection"] += characteristic["protection"]

    arthur["power"] += arthur["weapon"]["power"]

    if arthur["potion"] is not None:
        if "power" in arthur["potion"]["effect"]:
            arthur["power"] += arthur["potion"]["effect"]["power"]

        if "protection" in arthur["potion"]["effect"]:
            arthur["protection"] += arthur["potion"]["effect"]["protection"]

        if "hp" in arthur["potion"]["effect"]:
            arthur["hp"] += arthur["potion"]["effect"]["hp"]

    return [
        arthur["name"],
        arthur["hp"],
        arthur["protection"],
        arthur["power"]
    ]
