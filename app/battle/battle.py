from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.charcters.knightinfo import Knight


class Battle:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        damage1 = max(0, knight2.power - knight1.protection)
        damage2 = max(0, knight1.power - knight2.protection)
        knight1.hp = max(0, knight1.hp - damage1)
        knight2.hp = max(0, knight2.hp - damage2)
