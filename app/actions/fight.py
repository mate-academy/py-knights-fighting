def fight(character1: dict, character2: dict) -> None:
    character1["hp"] -= character2["power"] - character1["protection"]
    character2["hp"] -= character1["power"] - character2["protection"]

    # check if someone fell in battle
    if character1["hp"] <= 0:
        character1["hp"] = 0

    if character2["hp"] <= 0:
        character2["hp"] = 0
