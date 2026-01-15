
def config_duel(knight1: dict, knight2: dict) -> None:
    knight1["hp"] -= max(knight2["power"] - knight1["protection"], 0)
    knight2["hp"] -= max(knight1["power"] - knight2["protection"], 0)
    knight1["hp"] = max(knight1["hp"], 0)
    knight2["hp"] = max(knight2["hp"], 0)
