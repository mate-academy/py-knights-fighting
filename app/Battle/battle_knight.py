def battle_knights(knight_first, knight_second):
    knight_first["hp"] -= knight_second["power"] - knight_first["protection"]
    knight_second["hp"] -= knight_first["power"] - knight_second["protection"]

    # check if someone fell in Battle
    if knight_first["hp"] <= 0:
        knight_first["hp"] = 0

    if knight_second["hp"] <= 0:
        knight_second["hp"] = 0
