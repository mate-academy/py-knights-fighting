from app.knight.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> dict:
    knight1.hp -= knight2.power - knight1.protection
    if knight1.hp <= 0:
        knight1.hp = 0
    knight2.hp -= knight1.power - knight2.protection
    if knight2.hp <= 0:
        knight2.hp = 0
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
