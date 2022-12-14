def preparations(knights: dict) -> None:

    for knight_name, knight in knights.items():
        knight["protection"] = 0

        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]

        # apply weapon
        knight["power"] += knight["weapon"]["power"]

        # apply potion if exist
        if knight["potion"] is not None:
            for char in ["power", "protection", "hp"]:
                if char in knight["potion"]["effect"]:
                    knight[char] += knight["potion"]["effect"][char]
