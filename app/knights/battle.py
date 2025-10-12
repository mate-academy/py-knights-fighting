from __future__ import annotations
from typing import Dict
from app.knights.knight import Knight


def duel(left: Knight, right: Knight) -> Dict[str, int]:
    left_damage = max(0, right.power - left.protection)
    right_damage = max(0, left.power - right.protection)

    left.hp = max(0, left.hp - left_damage)
    right.hp = max(0, right.hp - right_damage)

    return {left.name: left.hp, right.name: right.hp}
