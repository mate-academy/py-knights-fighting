from typing import Dict
from battle.knight import Knight

def simulate_duel(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    print(f"\n--- Битва між {knight1.name} та {knight2.name} ---")
    while knight1.is_alive() and knight2.is_alive():
        knight1.attack(knight2)
        if not knight2.is_alive():
            break
        knight2.attack(knight1)
        if not knight1.is_alive():
            break
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
