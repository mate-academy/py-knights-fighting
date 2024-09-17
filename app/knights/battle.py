from typing import Dict
from .stats import Knight


def battle(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    stats1 = knight1.calculate_stats()
    stats2 = knight2.calculate_stats()

    stats1["hp"] -= max(0, stats2["power"] - stats1["protection"])
    stats2["hp"] -= max(0, stats1["power"] - stats2["protection"])

    return {
        knight1.name: max(0, stats1["hp"]),
        knight2.name: max(0, stats2["hp"]),
    }
