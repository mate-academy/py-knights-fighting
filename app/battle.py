def check_fallen_knight(knight: dict) -> dict:
    if knight["hp"] <= 0:
        knight["hp"] = 0
        knight["fallen"] = True
    else:
        knight["fallen"] = False
    return knight


def fight(knight1: dict, knight2: dict) -> tuple:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    # check if someone fell in battle
    knight1 = check_fallen_knight(knight1)
    knight2 = check_fallen_knight(knight2)

    return knight1, knight2
