from app.models.knight import Knight


def compute_damage(attacker: Knight, defender: Knight) -> int:
    damage = max(attacker.current_power - defender.current_protection, 0)
    return max(defender.current_hp - damage, 0)
