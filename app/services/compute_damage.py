from app.models.knight import Knight


def compute_damage(attacker: Knight, defender: Knight) -> int:
    return max(attacker.current_power - defender.current_protection, 0)
