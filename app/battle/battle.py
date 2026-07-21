from app.knights.knight import Knight


def fight(knight_a: Knight, knight_b: Knight) -> None:
    """Two knights simultaneously deal damage to each other."""
    a_power = knight_a.power
    b_power = knight_b.power

    knight_a.receive_damage(b_power)
    knight_b.receive_damage(a_power)
