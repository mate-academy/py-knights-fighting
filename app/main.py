from knights.knight_stats import Knight
def simulate_battle(knight1, knight2):
    # Calculate damage dealt to each other
    knight1_damage = knight1.calculate_damage(knight2)
    knight2_damage = knight2.calculate_damage(knight1)
    
    # Apply damage
    knight1.hp = max(0, knight1.hp - knight2_damage)
    knight2.hp = max(0, knight2.hp - knight1_damage)

def battle(knights_config):
    knights = {name: Knight(**stats) for name, stats in knights_config.items()}
    
    # Simulate the specified battles
    simulate_battle(knights["lancelot"], knights["mordred"])
    simulate_battle(knights["arthur"], knights["red_knight"])
    
    return {knight.name: knight.hp for knight in knights.values()}
