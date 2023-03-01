def amply_potion(knight):
    stats = ["power", "protection", "hp"]
    if knight["potion"] is not None:
        for stat in stats:
            if stat in knight["potion"]["effect"]:
                knight[stat] += knight["potion"]["effect"][stat]
