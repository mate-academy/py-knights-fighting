# app/battle.py
from __future__ import annotations
from typing import Dict
from app.knight import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def conduct(self) -> Dict[str, int]:
        self.knight1.prepare_for_battle()
        self.knight2.prepare_for_battle()

        damage_knight1 = max(0, self.knight2.power - self.knight1.protection)
        damage_knight2 = max(0, self.knight1.power - self.knight2.protection)

        self.knight1.hp -= damage_knight1
        self.knight2.hp -= damage_knight2

        self.knight1.hp = max(0, self.knight1.hp)
        self.knight2.hp = max(0, self.knight2.hp)

        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
