from app.knight import Knight


def knights_fight(knight_1: Knight, knight_2: Knight) -> dict:
    knight1_hp = knight_1.hp - knight_2.power
    knight2_hp = knight_2.hp - knight_1.power

    if knight1_hp < 0:
        knight1_hp = 0
    if knight2_hp < 0:
        knight2_hp = 0

    return {knight_1.name: knight1_hp, knight_2.name: knight2_hp}
