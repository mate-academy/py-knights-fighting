def battle_versus(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= knight2["power"] - knight1["protection"]

    knight2["hp"] -= knight1["power"] - knight2["protection"]

    knights = [knight1, knight2]

    for knight in knights:
        if knight["hp"] <= 0:
            knight["hp"] = 0
