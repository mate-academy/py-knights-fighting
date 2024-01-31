def check_hp(knight: dict) -> None:
    if knight["hp"] <= 0:
        knight["hp"] = 0


def fight(knight_1: dict, knight_2: dict) -> None:
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]
