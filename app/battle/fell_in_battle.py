def fell_in_battle(knight):
    if knight["hp"] <= 0:
        knight["hp"] = 0
    return knight["hp"]
