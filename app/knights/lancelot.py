def lancelot(dictionary: dict) -> list:
    lancelot = dictionary["lancelot"]

    lancelot["protection"] = 0
    for characteristic in lancelot["armour"]:
        lancelot["protection"] += characteristic["protection"]

    lancelot["power"] += lancelot["weapon"]["power"]

    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            lancelot["protection"] +=\
                lancelot["potion"]["effect"]["protection"]

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    return [
        lancelot["name"],
        lancelot["hp"],
        lancelot["protection"],
        lancelot["power"]
    ]
