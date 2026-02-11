from app.models import Knight


def duel(knight_a: Knight, knight_b: Knight) -> None:
    """Execute a simultaneous strike between two knights."""
    # We store powers first to ensure the strikes are simultaneous
    power_a = knight_a.power
    power_b = knight_b.power
    knight_a.take_damage(power_b)
    knight_b.take_damage(power_a)
