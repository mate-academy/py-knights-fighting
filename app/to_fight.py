def fight(fighter1: dict, fighter2: dict) -> int:
    fighter1["hp"] -= fighter2["power"] - fighter1["protection"]
    if fighter1["hp"] <= 0:
        fighter1["hp"] = 0
    return fighter1["hp"]
