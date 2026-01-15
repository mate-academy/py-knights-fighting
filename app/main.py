from typing import Tuple, Dict
from app.knights.config import KNIGHTS
from app.knights.knight import Knight
from app.battle.fight import fight


def battle() -> Tuple[Dict[str, int], Dict[str, int]]:
    """Run battles between predefined pairs of knights."""

    # Create Knight objects from config
    knights = {name: Knight(**stats) for name, stats in KNIGHTS.items()}

    # Define battle pairs
    battle_pairs = [
        (knights["lancelot"], knights["mordred"]),
        (knights["arthur"], knights["red_knight"])
    ]

    # Run battles and collect results
    results = [fight(k1, k2) for k1, k2 in battle_pairs]

    return tuple(results)
