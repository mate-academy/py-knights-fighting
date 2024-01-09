def battles(knight_1: dict, knight_2: dict) -> list:
    battle_list = []
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]

    if knight_1["hp"] <= 0:
        knight_1["hp"] = 0

    if knight_2["hp"] <= 0:
        knight_2["hp"] = 0
    battle_list.append(knight_1)
    battle_list.append(knight_2)

    return battle_list
