from app.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> Knight:
    knight1.hp -= max(knight2.power - knight1.protection, 0)
    knight2.hp -= max(knight1.power - knight2.protection, 0)

    knight1.hp = max(knight1.hp, 0)
    knight2.hp = max(knight2.hp, 0)

    return knight1, knight2
