def preparation(knight: dict) -> dict:
    # apply armour
    knight["protection"] = 0
    for new_value in knight["armour"]:
        knight["protection"] += new_value["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"] is not None:
        affected_attributes = ["power", "protection", "hp"]
        for attribute in affected_attributes:
            if attribute in knight["potion"]["effect"]:
                knight[attribute] += knight["potion"]["effect"][attribute]
    return knight
