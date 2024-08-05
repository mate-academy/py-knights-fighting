from typing import Dict
from knight import Knight


def calculate_damage(attacker: "Knight", defender: "Knight") -> int:
    damage = attacker.total_power - defender.total_protection
    return max(damage, 0)


def battle(knight1: "Knight", knight2: "Knight") -> Dict[str, int]:
    knight1_damage = calculate_damage(knight2, knight1)
    knight2_damage = calculate_damage(knight1, knight2)

    knight1.total_hp -= knight1_damage
    knight2.total_hp -= knight2_damage

    knight1.total_hp = max(knight1.total_hp, 0)
    knight2.total_hp = max(knight2.total_hp, 0)

    return {knight1.name: knight1.total_hp, knight2.name: knight2.total_hp}
