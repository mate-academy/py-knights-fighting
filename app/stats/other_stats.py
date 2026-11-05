def armor(knight: dict) -> dict:
    knight["protection"] = 0
    for ab in knight["armour"]:
        knight["protection"] += ab["protection"]
    return knight


def weapon(knight: dict) -> dict:
    knight["power"] += knight["weapon"]["power"]
    return knight
