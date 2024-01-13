def battle_preparation(knights: dict) -> dict:
    for knight in knights.values():
        knight["protection"] = sum(armour["protection"]
                                   for armour in knight["armour"])
        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            for stat in ["power", "protection", "hp"]:
                if stat in knight["potion"]["effect"]:
                    knight[stat] += knight["potion"]["effect"][stat]

    return knights
