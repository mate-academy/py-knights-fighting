from app.actions.calculation import calculation


def duel(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0


# preset battle
def battle(knight_dict: dict) -> dict:
    lancelot = knight_dict["lancelot"]
    arthur = knight_dict["arthur"]
    mordred = knight_dict["mordred"]
    red_knight = knight_dict["red_knight"]
    knights = [lancelot, arthur, mordred, red_knight]

    for knight in knights:
        calculation(knight)

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        knight["name"]: knight["hp"] for knight in knights
    }
