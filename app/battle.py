from typing import Tuple

from app.knight import Knight


def calculate_damage(attacker: Knight, defender: Knight) -> int:
    return max(0, attacker.power - defender.protection)


def fight(knight_a: Knight, knight_b: Knight) -> Tuple[Knight, Knight]:
    damage_to_a = calculate_damage(knight_b, knight_a)
    damage_to_b = calculate_damage(knight_a, knight_b)

    knight_a.take_damage(damage_to_a)
    knight_b.take_damage(damage_to_b)

    return knight_a, knight_b
