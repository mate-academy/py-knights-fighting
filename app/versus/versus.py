def versus(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]
    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0
