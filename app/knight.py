def prepare_knight(knight: dict) -> None:
    knight["protection"] = 0

    for armor in knight["armour"]:
        knight["protection"] += armor["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value
