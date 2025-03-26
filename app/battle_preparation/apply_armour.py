def apply_armour(knight_armour):
    knight_armour["protection"] = 0
    if "armour" in knight_armour and knight_armour["armour"]:
        for a in knight_armour["armour"]:
            knight_armour["protection"] += a["protection"]
    return knight_armour["protection"]
