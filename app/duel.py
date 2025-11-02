from app.knight import Knight


def duel(knight1: Knight, knight2: Knight) -> dict:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
