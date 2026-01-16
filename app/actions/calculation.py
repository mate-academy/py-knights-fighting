def calculation(knight: dict) -> dict:

    # armour
    knight["protection"] = 0
    for new_value in knight["armour"]:
        knight["protection"] += new_value["protection"]

    # weapon
    knight["power"] += knight["weapon"]["power"]

    # potion
    if knight["potion"] is not None:
        possible_attributes = ["power", "protection", "hp"]
        for attribute in possible_attributes:
            if attribute in knight["potion"]["effect"]:
                knight[attribute] += knight["potion"]["effect"][attribute]
    return knight
