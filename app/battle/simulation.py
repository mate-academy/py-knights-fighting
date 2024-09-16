from app.knight.constructor import Knight


def attack(knight1: Knight, knight2: Knight) -> int:
    knight1.hp -= knight2.power - knight1.protection

    if knight1.hp <= 0:
        knight1.hp = 0
    return knight1.hp
