def red_knight(dictionary: dict) -> list:
    red_knight = dictionary["red_knight"]

    red_knight["protection"] = 0
    for characteristic in red_knight["armour"]:
        red_knight["protection"] += characteristic["protection"]

    red_knight["power"] += red_knight["weapon"]["power"]

    if red_knight["potion"] is not None:
        if "power" in red_knight["potion"]["effect"]:
            red_knight["power"] += red_knight["potion"]["effect"]["power"]

        if "protection" in red_knight["potion"]["effect"]:
            red_knight["protection"] +=\
                red_knight["potion"]["effect"]["protection"]

        if "hp" in red_knight["potion"]["effect"]:
            red_knight["hp"] += red_knight["potion"]["effect"]["hp"]

    return [
        red_knight["name"],
        red_knight["hp"],
        red_knight["protection"],
        red_knight["power"]
    ]
