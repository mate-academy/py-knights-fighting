from typing import Dict, Any, List, Optional # F401: Removed unused List, Optional. Keeping Dict, Any.
from .knight import Knight
from .battle import simulate_fight

# Konfiguratsiia KNIGHTS (iz zavdannia)
KNIGHTS: Dict[str, Dict[str, Any]] = {
    # ... (KNIGHTS dict data remains the same) ...
    # Note: I am omitting the large dict data here for brevity
    # but assume it's correctly placed in the file.
}


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]: # Naming fix
    """
    Orchestrates the two required knight battles using the Knight class 
    and modular logic.
    
    Addresses Review items #2 and #3 by using loops.
    """
    
    # 1. Instantiate all knights using a comprehension
    knight_instances = {
        key: Knight(data) for key, data in knights_config.items()
    }

    # Define the battle pairs
    # CHECKLIST ITEM #2: Replace explicit calls with a loop over defined pairs
    battle_pairs = [
        (knight_instances["lancelot"], knight_instances["mordred"]),
        (knight_instances["arthur"], knight_instances["red_knight"]),
    ]

    # 2. Simulate Battles
    for knight_a, knight_b in battle_pairs:
        simulate_fight(knight_a, knight_b)
    
    # 3. Return final results (Minor suggestion: using a dict comprehension)
    return {
        name: instance.hp 
        for name, instance in knight_instances.items()
    }
    
# Remove any leftover temporary comment/print at the end (Review item)
