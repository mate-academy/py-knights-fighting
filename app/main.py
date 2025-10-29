from typing import Dict
from app.knight import Knight


def duel(attacker: Knight, defender: Knight) -> None:
    damage_to_defender: int = max(0, attacker.total_power
                                  - defender.total_protection)
    damage_to_attacker: int = max(0, defender.total_power
                                  - attacker.total_protection)
    attacker.take_damage(damage_to_attacker)
    defender.take_damage(damage_to_defender)


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    knights: Dict[str, Knight] = {
        key: Knight({key: data}) for key, data in knights_config.items()
    }
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])
    return {knight.name: knight.total_hp for knight in knights.values()}
