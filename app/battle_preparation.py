def battle_preparation(knight: dict) -> dict:
    # apply armour
    knight["protection"] = 0
    for item in knight["armour"]:
        knight["protection"] += item["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"] is not None:
        attributes = ["power", "protection", "hp"]
        for i in attributes:
            if i in knight["potion"]["effect"]:
                knight[i] += knight["potion"]["effect"][i]
    return knight
