def fight(knight1: dict, knight2: dict) -> int:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    return knight1["hp"]
