from app.knight import Knight


def knights_battle(knight1: Knight, knight2: Knight) -> dict:
    knight1_hp = knight1.hp - knight2.power
    knight2_hp = knight2.hp - knight1.power

    if knight1_hp < 0:
        knight1_hp = 0
    if knight2_hp < 0:
        knight2_hp = 0

    return {knight1.name: knight1_hp, knight2.name: knight2_hp}
