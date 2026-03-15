from typing import List, Dict


def total_protection(armour: List[Dict]) -> int:
    return sum(piece.get("protection", 0) for piece in armour)


def weapon_power(weapon: Dict) -> int:

    if not weapon:
        return 0
    return weapon.get("power", 0)


def apply_potion(stats: Dict[str, int], potion: Dict) -> Dict[str, int]:

    new_stats = stats.copy()
    if not potion:
        return new_stats
    effect = potion.get("effect", {})
    for key, delta in effect.items():
        if key in new_stats:
            new_stats[key] = new_stats.get(key, 0) + delta
    return new_stats
