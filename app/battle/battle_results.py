def results_hp(knight1: dict, knight2: dict) -> tuple:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight2["hp"] -= knight1["power"] - knight2["protection"]
    return knight1["hp"], knight2["hp"]
