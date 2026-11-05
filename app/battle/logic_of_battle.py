from app.knights.config import Knights


def battle_begin(knight1: Knights, knight2: Knights) -> None:

    # knight1 versus knight2
    knight1.stats["hp"] -= knight2.stats["power"] - knight1.stats["protection"]
    knight2.stats["hp"] -= knight1.stats["power"] - knight2.stats["protection"]

    # check if someone fell in battle
    if knight1.stats["hp"] <= 0:
        knight1.stats["hp"] = 0

    if knight2.stats["hp"] <= 0:
        knight2.stats["hp"] = 0
