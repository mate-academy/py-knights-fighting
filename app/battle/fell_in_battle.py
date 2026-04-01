def fell_in_battle(knight: dict) -> int:
    if knight["hp"] <= 0:
        knight["hp"] = 0
    return knight["hp"]
