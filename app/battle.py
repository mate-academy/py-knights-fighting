def knight_battle(knight_one: dict, knight_two: dict) -> None:
    knight_one["hp"] -= knight_two["power"] - knight_one["protection"]
    knight_two["hp"] -= knight_one["power"] - knight_two["protection"]

    if knight_one.get("hp") <= 0:
        knight_one["hp"] = 0

    if knight_two.get("hp") <= 0:
        knight_two["hp"] = 0
