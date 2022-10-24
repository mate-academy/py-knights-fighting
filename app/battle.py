def battle_func(knight1: dict, knight2: dict,
                knight3: dict, knight4: dict) -> dict:
    # 1 knight1 vs knight2:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]

    # check if someone fell in battle
    if knight1["hp"] <= 0:
        knight1["hp"] = 0

    if knight2["hp"] <= 0:
        knight2["hp"] = 0

    # 2 knight3 vs knight4:
    knight3["hp"] -= knight4["power"] - knight3["protection"]
    knight4["hp"] -= knight3["power"] - knight4["protection"]

    # check if someone fell in battle
    if knight3["hp"] <= 0:
        knight3["hp"] = 0

    if knight4["hp"] <= 0:
        knight4["hp"] = 0

    # Return battle results:
    return {
        knight1["name"]: knight1["hp"],
        knight2["name"]: knight2["hp"],
        knight3["name"]: knight3["hp"],
        knight4["name"]: knight4["hp"],
    }
