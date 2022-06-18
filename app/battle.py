def battles(knight_1, knight_2):
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]

    # check if someone fell in battle
    if knight_1["hp"] <= 0:
        knight_1["hp"] = 0

    if knight_2["hp"] <= 0:
        knight_2["hp"] = 0

    return {knight_1["name"]: knight_1["hp"],
            knight_2["name"]: knight_2["hp"]}
