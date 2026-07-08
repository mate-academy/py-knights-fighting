def two_knights_fight(knight_1: dict, knight_2: dict) -> None:
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]
    knight_1["hp"] = max(knight_1["hp"], 0)
    knight_2["hp"] = max(knight_2["hp"], 0)
