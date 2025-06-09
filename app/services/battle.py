from app.models.knight import Knight


def duel(knight1: Knight, knight2: Knight) -> None:
    dmg1 = max(knight2.power - knight1.protection, 0)
    dmg2 = max(knight1.power - knight2.protection, 0)
    knight1.hp = max(knight1.hp - dmg1, 0)
    knight2.hp = max(knight2.hp - dmg2, 0)
