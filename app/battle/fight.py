from app.knights.knight import Knight


def one_vs_one(knight1: Knight, knight2: Knight) -> tuple[int, int]:
    k1 = knight1.final_stats()
    k2 = knight2.final_stats()
    while k1["hp"] > 0 and k2["hp"] > 0:
        k1_damage = max(k2["power"] - k1["protection"], 0)
        k2_damage = max(k1["power"] - k2["protection"], 0)
        k1["hp"] = max(k1["hp"] - k1_damage, 0)
        k2["hp"] = max(k2["hp"] - k2_damage, 0)
    return k1["hp"], k2["hp"]


def battle(knights_config: dict) -> dict[str, int]:
    lancelot = knights_config["Lancelot"]
    mordred = knights_config["Mordred"]
    arthur = knights_config["Arthur"]
    red_knight = knights_config["Cavaleiro Vermelho"]

    l_hp, m_hp = one_vs_one(lancelot, mordred)
    a_hp, r_hp = one_vs_one(arthur, red_knight)

    return {
        "Lancelot": l_hp,
        "Arthur": a_hp,
        "Mordred": m_hp,
        "Cavaleiro Vermelho": r_hp,
    }
