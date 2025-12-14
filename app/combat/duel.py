from app.domain.knight import Knight


def duel(knight_a: Knight, knight_b: Knight) -> None:
    """
    Conducts a duel.
    Mutates the HP of both knights.
    """

    knight_a.hp -= knight_b.power - knight_a.protection
    knight_b.hp -= knight_a.power - knight_b.protection
