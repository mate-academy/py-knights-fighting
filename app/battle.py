from typing import Dict
from app.knights import Knight

def duel(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    """Simulates a duel between two knights and returns their remaining HP."""
    damage_to_1: int = max(knight2.power - knight1.protection, 0)
    damage_to_2: int = max(knight1.power - knight2.protection, 0)

    knight1.hp = max(knight1.hp - damage_to_1, 0)
    knight2.hp = max(knight2.hp - damage_to_2, 0)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
