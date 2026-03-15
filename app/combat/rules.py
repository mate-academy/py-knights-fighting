from typing import Dict, Tuple


def apply_damage(a_stats: Dict[str, int],
                 b_stats: Dict[str, int]) -> Tuple[int, int]:
    a_hp = a_stats.get("hp", 0)
    b_hp = b_stats.get("hp", 0)
    damage_to_a = max(0,
                      b_stats.get("power", 0) - a_stats.get("protection", 0))
    damage_to_b = max(0,
                      a_stats.get("power", 0) - b_stats.get("protection", 0))
    a_hp -= damage_to_a
    b_hp -= damage_to_b
    return a_hp, b_hp
