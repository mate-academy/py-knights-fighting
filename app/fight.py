def fighting(knight_1: dict, knight_2: dict) -> dict:

    # Scramble
    knight_1["hp"] = max(
        0, knight_1["hp"] - (knight_2["power"] - knight_1["protection"])
    )
    knight_2["hp"] = max(
        0, knight_2["hp"] - (knight_1["power"] - knight_2["protection"])
    )

    # Return combat result:
    return {
        knight_1["name"]: knight_1["hp"],
        knight_2["name"]: knight_2["hp"],
    }
