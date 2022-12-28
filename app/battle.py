def battle_between_two_knights(knight: dict, another_knight: dict) -> None:
    knight["hp"] -= another_knight["power"] - knight["protection"]
    another_knight["hp"] -= knight["power"] - another_knight["protection"]

    # check if someone fell in battle
    if knight["hp"] <= 0:
        knight["hp"] = 0

    if another_knight["hp"] <= 0:
        another_knight["hp"] = 0
