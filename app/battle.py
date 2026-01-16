from __future__ import annotations
from app.preparations import Knight


class Battle:
    def __init__(self, knight: Knight, opponent: Knight) -> None:
        # here we can store info about battle (used equipment, time, etc.)
        # also can move battle logic to function, for make it easy to modify
        knight.hp = (
            max(0, knight.hp - (opponent.power - knight.protection))
        )
        opponent.hp = (
            max(0, opponent.hp - (knight.power - opponent.protection))
        )
