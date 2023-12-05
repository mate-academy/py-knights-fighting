from app.knights.knight import Knight


def final_battle(knight1: Knight, knight2: Knight) -> dict:
    result = {}
    knight1.hp -= knight2.power - knight1.protection
    if knight1.hp < 0:
        knight1.hp = 0
    result[knight1.name] = knight1.hp
    knight2.hp -= knight1.power - knight2.protection
    if knight2.hp < 0:
        knight2.hp = 0
    result[knight2.name] = knight2.hp
    return result
