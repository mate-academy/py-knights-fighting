from .knight import Knight

def simulate_fight(knight_a: Knight, knight_b: Knight) -> None:
    """
    Симулює одночасний обмін шкодою між двома лицарями.
    """
    
    power_a = knight_a.effective_power
    power_b = knight_b.effective_power
    
    knight_a.take_damage(power_b)
    knight_b.take_damage(power_a)
