def battle_finish(knight_one: dict, knight_two: dict) -> None:
    knight_one["hp"] -= knight_two["power"] - knight_one["protection"]
    knight_two["hp"] -= knight_one["power"] - knight_two["protection"]

    # check if someone fell in battle
    if knight_one["hp"] <= 0:
        knight_one["hp"] = 0

    if knight_two["hp"] <= 0:
        knight_two["hp"] = 0
