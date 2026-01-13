from app.knights import KNIGHTS
from app.prebattle import preparations


def battle(knightsconfig: dict) -> dict:
    preparations(knightsconfig)
    # 1 Lancelot vs Mordred:
    battle_pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]
    for k1, k2 in battle_pairs:
        knight1 = knightsconfig[k1]
        knight2 = knightsconfig[k2]
        knight1["hp"] -= knight2["power"] - knight1["protection"]
        knight2["hp"] -= knight1["power"] - knight2["protection"]
        if knight1["hp"] < 0:
            knight1["hp"] = 0
        if knight2["hp"] < 0:
            knight2["hp"] = 0
    return {
        knightsconfig["lancelot"]["name"]: knightsconfig["lancelot"]["hp"],
        knightsconfig["arthur"]["name"]: knightsconfig["arthur"]["hp"],
        knightsconfig["mordred"]["name"]: knightsconfig["mordred"]["hp"],
        knightsconfig["red_knight"]["name"]: knightsconfig["red_knight"]["hp"],
    }


battle(KNIGHTS)
