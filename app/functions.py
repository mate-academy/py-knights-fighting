def apply_armour(name: dict) -> any:
    name["protection"] = 0
    for value in name["armour"]:
        name["protection"] += value["protection"]
    return name["protection"]


def apply_weapon(name: dict) -> any:
    name["power"] += name["weapon"]["power"]
    return name["power"]


def apply_potion(name: dict) -> any:
    if name["potion"] is not None:
        if "power" in name["potion"]["effect"]:
            name["power"] += name["potion"]["effect"]["power"]

        if "protection" in name["potion"]["effect"]:
            name["protection"] += name["potion"]["effect"]["protection"]

        if "hp" in name["potion"]["effect"]:
            name["hp"] += name["potion"]["effect"]["hp"]
