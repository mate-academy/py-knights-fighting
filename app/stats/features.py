def knight_features(all_knights, knight_name):
    knight = all_knights[knight_name]
    knight["protection"] = 0
    for part in knight["armour"]:
        knight["protection"] += part["protection"]
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        stats = ("hp", "protection", "power")
        for stat in stats:
            if stat in knight["potion"]["effect"]:
                knight[stat] += knight["potion"]["effect"][stat]
    return knight
