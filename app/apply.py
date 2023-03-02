def apply(knight: dict) -> None:
    # apply armour
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"] is not None:
        characteristics = ["power", "protection", "hp"]
        for character in characteristics:
            if character in knight["potion"]["effect"]:
                knight[character] += knight["potion"]["effect"][character]
