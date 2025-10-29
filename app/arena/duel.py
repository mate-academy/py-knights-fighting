from typing import Dict
from app.barracks.knight_preparation import Knight


def battle(knights_dict: Dict[str, Dict]) -> Dict[str, int]:
    """Conduct battles between Lancelot vs Mordred and Arthur vs Red Knight."""
    lancelot = Knight(knights_dict["lancelot"])
    arthur = Knight(knights_dict["arthur"])
    mordred = Knight(knights_dict["mordred"])
    red_knight = Knight(knights_dict["red_knight"])

    result1 = fight(lancelot, mordred)
    result2 = fight(arthur, red_knight)

    return {**result1, **result2}


def fight(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    """Simulate a fight between two knights and return their remaining HP."""
    knight1.hp -= max(knight2.power - knight1.protection, 0)
    knight2.hp -= max(knight1.power - knight2.protection, 0)

    knight1.hp = max(knight1.hp, 0)
    knight2.hp = max(knight2.hp, 0)

    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
