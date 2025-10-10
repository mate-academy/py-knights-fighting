# ... (Imports and KNIGHTS dict remain the same) ...

# Fix E302: Add an extra blank line here

def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]: # Fix M083
    """
    Orchestrates the two required knight battles using the Knight class and modular logic.
    """
    
    # 1. Створення екземплярів лицарів
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])
    
    # 2. Симуляція боїв (Lines 82 and 103 are likely here, need careful wrapping)
    simulate_fight(lancelot, mordred) # Check E501 if this line or similar lines are too long
    simulate_fight(arthur, red_knight)
    
    # 3. Повернення фінальних результатів
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
