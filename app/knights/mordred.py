def mordred(dictionary: dict) -> list:
    mordred = dictionary["mordred"]

    mordred["protection"] = 0
    for characteristic in mordred["armour"]:
        mordred["protection"] += characteristic["protection"]

    mordred["power"] += mordred["weapon"]["power"]

    if mordred["potion"] is not None:
        if "power" in mordred["potion"]["effect"]:
            mordred["power"] += mordred["potion"]["effect"]["power"]

        if "protection" in mordred["potion"]["effect"]:
            mordred["protection"] += mordred["potion"]["effect"]["protection"]

        if "hp" in mordred["potion"]["effect"]:
            mordred["hp"] += mordred["potion"]["effect"]["hp"]

    return [
        mordred["name"],
        mordred["hp"],
        mordred["protection"],
        mordred["power"]
    ]
