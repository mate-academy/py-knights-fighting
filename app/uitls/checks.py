def check_who_won_or_loose(knight_1, knight_2):
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] = max(knight_2["hp"], 0)
    knight_1["hp"] = max(knight_1["hp"], 0)
