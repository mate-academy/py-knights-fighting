from app.knights.knight import Knight


def knight_fight(knight1: Knight, knight2: Knight) -> dict:
    knight2.hp -= knight1.power - knight2.protection
    knight1.hp -= knight2.power - knight1.protection
    if knight1.hp < 0:
        knight1.hp = 0
    if knight2.hp < 0:
        knight2.hp = 0
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
