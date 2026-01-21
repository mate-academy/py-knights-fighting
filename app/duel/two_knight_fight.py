def battle_for_honor(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= max(knight2["power"] - knight1.get("protection", 0), 0)
    knight2["hp"] -= max(knight1["power"] - knight2.get("protection", 0), 0)

    # check if someone fell in battle
    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0
