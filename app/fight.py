from app.knights import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.get_power() - knight1.get_protection()
    knight2.hp -= knight1.get_power() - knight2.get_protection()

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0
