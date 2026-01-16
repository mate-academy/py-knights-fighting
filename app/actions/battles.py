def duel(knight1: dict, knight2: dict) -> dict:
    knight1["hp"] += knight1["add_some_abilities"]
    knight2["hp"] += knight2["add_some_abilities"]
    knight1["hp"] -= knight2["power"]
    knight2["hp"] -= knight1["power"]
