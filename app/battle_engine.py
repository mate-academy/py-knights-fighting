from app.models import Knight


def duel(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.take_damage(knight_2.power)
    knight_2.take_damage(knight_1.power)
