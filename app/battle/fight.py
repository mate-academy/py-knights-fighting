from typing import Mapping, Any

from app.skil.factories import build_knights

pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]


def battle(knights: Mapping[str, Any]) -> dict[str, int]:
    """
    Accept either:
      - a raw knights config dict (like KNIGHTS), or
      - a dict[str, Knight] (already-built Knight objects).
    """
    # If passed raw dicts (values are dict), convert to Knight objects
    sample = next(iter(knights.values()))
    if isinstance(sample, dict):
        knights = build_knights(knights)

    result: dict[str, int] = {}
    for knight_a, knight_b in pairs:
        attacker = knights[knight_a]
        defender = knights[knight_b]
        damage_a_to_b = max(0, attacker.power - defender.protection)
        damage_b_to_a = max(0, defender.power - attacker.protection)
        new_hp_a = max(0, attacker.hp - damage_b_to_a)
        new_hp_b = max(0, defender.hp - damage_a_to_b)
        result[attacker.name] = new_hp_a
        result[defender.name] = new_hp_b

    return result
