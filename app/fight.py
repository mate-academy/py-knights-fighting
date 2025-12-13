def fight(knight_1: dict, knight_2: dict) -> dict:

    knight_1["hp"] -= knight_2.get("power") - knight_1.get("protection")
    knight_2["hp"] -= knight_1.get("power") - knight_2.get("protection")

    # check if someone fell in battle
    for knight in (knight_1, knight_2):
        if knight.get("hp") <= 0:
            knight["hp"] = 0

    return {
        knight_1["name"]: knight_1["hp"],
        knight_2["name"]: knight_2["hp"],
    }
