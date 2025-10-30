from typing import Dict

from app.barracks.knight_preparation import Knight


def battle(knights_dict: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    """Conduct battles between Lancelot vs Mordred and Arthur vs Red Knight."""
    knights: Dict[str, Knight] = {
        key: Knight(data)
        for key, data in knights_dict.items()
        if key in ("lancelot", "arthur", "mordred", "red_knight")
    }

    result1: Dict[str, int] = fight(knights["lancelot"], knights["mordred"])
    result2: Dict[str, int] = fight(knights["arthur"], knights["red_knight"])

    return {**result1, **result2}


def fight(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    """Simulate a fight between two knights and return their remaining HP."""
    knight1.hp -= max(knight2.power - knight1.protection, 0)
    knight2.hp -= max(knight1.power - knight2.protection, 0)

    knight1.hp = max(knight1.hp, 0)
    knight2.hp = max(knight2.hp, 0)

    return {knight1.name: knight1.hp, knight2.name: knight2.hp}
