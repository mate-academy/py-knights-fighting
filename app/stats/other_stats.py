def armor(name: dict) -> dict:
    name["protection"] = 0
    for ab in name["armour"]:
        name["protection"] += ab["protection"]
    return name


def weapon(name: dict) -> dict:
    name["power"] += name["weapon"]["power"]
    return name
