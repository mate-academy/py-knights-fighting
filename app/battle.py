def knight_fighting(knight_1: dict, knight_2: dict) -> None:
    damage_to_1 = max(0, knight_2["power"] - knight_1["protection"])
    damage_to_2 = max(0, knight_1["power"] - knight_2["protection"])

    knight_1["hp"] -= damage_to_1
    knight_2["hp"] -= damage_to_2

    if knight_1["hp"] < 0:
        knight_1["hp"] = 0
    if knight_2["hp"] < 0:
        knight_2["hp"] = 0
