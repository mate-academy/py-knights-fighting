def fight(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])
