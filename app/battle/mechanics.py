from app.knights.models import Knight


def fight(knight1: "Knight", knight2: "Knight") -> dict:
    stats1 = knight1.prepare_for_battle()
    stats2 = knight2.prepare_for_battle()

    stats1["hp"] -= stats2["power"] - stats1["protection"]
    stats2["hp"] -= stats1["power"] - stats2["protection"]

    stats1["hp"] = max(stats1["hp"], 0)
    stats2["hp"] = max(stats2["hp"], 0)

    return {knight1.name: stats1["hp"], knight2.name: stats2["hp"]}
