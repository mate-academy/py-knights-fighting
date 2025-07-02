from app.knight import Knight


def battle(knight1: Knight, knight2: Knight) -> dict:
    hp1 = knight1.hp - max(0, knight2.power - knight1.protection)
    hp2 = knight2.hp - max(0, knight1.power - knight2.protection)

    hp1 = max(0, hp1)
    hp2 = max(0, hp2)

    return {knight1.name: hp1, knight2.name: hp2}
