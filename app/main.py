from typing import Dict
from .knights.knight_stats import Knight


def simulate_battle(knight1: Knight, knight2: Knight) -> None:

    knight1_damage = knight1.calculate_damage(knight2)
    knight2_damage = knight2.calculate_damage(knight1)

    knight1.hp = max(0, knight1.hp - knight2_damage)
    knight2.hp = max(0, knight2.hp - knight1_damage)


def battle(knights_config: Dict[str, Dict[str, int]]) -> Dict[str, int]:

    knights = {name: Knight(**stats) for name, stats in knights_config.items()}

    simulate_battle(knights["lancelot"], knights["mordred"])
    simulate_battle(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
