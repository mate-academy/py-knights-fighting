from app.models.knight import Knight


def fight(knight_a: Knight, knight_b: Knight) -> None:
    knight_a.take_damage(knight_b.power)
    knight_b.take_damage(knight_a.power)
