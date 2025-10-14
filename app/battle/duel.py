from app.knights.knight import Knight


def simulate_duel(knight_a: Knight, knight_b: Knight) -> None:
    knight_b.take_damage(knight_a.effective_power)
    knight_a.take_damage(knight_b.effective_power)
