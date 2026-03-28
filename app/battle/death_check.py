def death_check(knight: dict) -> None:
    if knight["hp"] <= 0:
        knight["hp"] = 0
