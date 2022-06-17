def apply_armour(knight):
    knight["protection"] = 0
    if knight["armour"]:
        for man in knight["armour"]:
            knight["protection"] += man["protection"]
