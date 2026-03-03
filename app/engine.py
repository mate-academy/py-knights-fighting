from __future__ import annotations
from app.models import Knight


def fight(attacker: Knight, defender: Knight) -> None:
    """
    Execute a combat turn between two knights.

    Calculating damage based on attacker's power and defender's protection,
    updating the defender's HP and ensuring it doesn't drop below zero.
    """
    damage = attacker.power - defender.protection

    if damage > 0:
        defender.hp -= damage

    if defender.hp < 0:
        defender.hp = 0
