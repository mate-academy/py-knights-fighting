def fighting(knight_1: dict, knight_2: dict) -> dict:

    # Scramble
    knight_1["hp"] -= knight_2["power"] - knight_1["protection"]
    knight_2["hp"] -= knight_1["power"] - knight_2["protection"]

    # Check if someone fell in battle
    if knight_1["hp"] <= 0:
        knight_1["hp"] = 0

    if knight_2["hp"] <= 0:
        knight_2["hp"] = 0

    # Return combat result:
    return {
        knight_1["name"]: knight_1["hp"],
        knight_2["name"]: knight_2["hp"],
    }
