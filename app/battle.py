from app.knights import Knight


def battle(knight1: Knight, knight2: Knight) -> None:

    knight2.hp -= max(0, knight1.power - knight2.protection)
    knight2.hp = max(knight2.hp, 0)

    knight1.hp -= max(0, knight2.power - knight1.protection)
    knight1.hp = max(knight1.hp, 0)
