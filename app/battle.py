from typing import Dict
from .knight import Knight


def battle(knights_config: Dict[str, dict]) -> Dict[str, int]:
    # Build Knight instances
    knights_by_key = {key: Knight(**cfg)
                      for key, cfg in knights_config.items()}

    for knight in knights_by_key.values():
        knight.prepare_for_battle()

    # Define exact battle pairs as required by the task
    battle_pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    # Execute fights with simultaneous damage
    for k1_key, k2_key in battle_pairs:
        k1 = knights_by_key[k1_key]
        k2 = knights_by_key[k2_key]
        k1.take_damage(k2.battle_power)
        k2.take_damage(k1.battle_power)

    # Return post-battle HP mapping using human-friendly names
    return {k.name: k.battle_hp for k in knights_by_key.values()}
