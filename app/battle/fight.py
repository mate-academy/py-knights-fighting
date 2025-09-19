from app.knights.knight import Knight


def battle(knight1: Knight, knight2: Knight) -> str:
    k1 = knight1.final_stats()
    k2 = knight2.final_stats()
    while k1["hp"] > 0 and k2["hp"] > 0:
        k1_damage = max(k2["power"] - k1["protection"], 0)
        k2_damage = max(k1["power"] - k2["protection"], 0)
        k1["hp"] = max(k1["hp"] - k1_damage, 0)
        k2["hp"] = max(k2["hp"] - k2_damage, 0)
    if k1["hp"] == 0 and k2["hp"] == 0:
        return "Draw"
    if k1["hp"] > 0:
        return knight1.name
    return knight2.name
