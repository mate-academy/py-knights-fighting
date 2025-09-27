def fight(fighter_1: dict, fighter_2: dict) -> None:
    fighter_1["hp"] -= fighter_2["power"] - fighter_1["protection"]
    fighter_2["hp"] -= fighter_1["power"] - fighter_2["protection"]

    if fighter_1["hp"] <= 0:
        fighter_1["hp"] = 0

    if fighter_2["hp"] <= 0:
        fighter_2["hp"] = 0
