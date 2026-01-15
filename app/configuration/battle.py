from app.models.knight import Knight


def knight_duel(knight1: Knight, knight2: Knight) -> None:
    knight1.hp = max(knight1.hp - (knight2.power - knight1.protection), 0)
    knight2.hp = max(knight2.hp - (knight1.power - knight2.protection), 0)
