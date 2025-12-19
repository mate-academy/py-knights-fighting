from app.models.knight import Knight


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.receive_damage(knight2.power - knight1.protection)
    knight2.receive_damage(knight1.power - knight2.protection)
