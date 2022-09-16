def knight_stat(all_knights, knight_name):
    knight = all_knights[knight_name]
    # apply armour
    knight["protection"] = 0
    for part in knight["armour"]:
        knight["protection"] += part["protection"]
        # apply weapon
    knight["power"] += knight["weapon"]["power"]
    # apply potion if exist

    if knight["potion"] is not None:
        stats = ("hp", "protection", "power")
        for stat in stats:
            if stat in knight["potion"]["effect"]:
                knight[stat] += knight["potion"]["effect"][stat]
    return knight
