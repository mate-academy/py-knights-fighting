from .knight import Knight


def simulate_fight(knight_a: Knight, knight_b: Knight) -> None:
    """
    Simulates a single round of combat between two knights.
    
    The knights simultaneously deal damage to each other.
    """
    
    # Зберігаємо ефективну силу (виправлено E261)
    power_a = knight_a.effective_power
    
    # Зберігаємо ефективну силу (виправлено E261)
    power_b = knight_b.effective_power
    
    # Виправлення E501: ці рядки тепер коротші
    knight_a.take_damage(power_b)
    knight_b.take_damage(power_a)
