from .knight import Knight


def simulate_fight(knight_a: Knight, knight_b: Knight) -> None:
    """
    Simulates a single round of combat between two knights.
    
    The knights simultaneously deal damage to each other.
    """
    
    power_a = knight_a.effective_power
    power_b = knight_b.effective_power
    
    knight_a.take_damage(power_b)
    knight_b.take_damage(power_a)
