def check_fell(knight: dict) -> int:
    if knight["hp"] <= 0:
        knight["hp"] = 0
    return knight["hp"]
