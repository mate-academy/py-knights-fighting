# app/battles/battle.py

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.roles.knights import Knight


class Battle:
    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def fight(self) -> dict[str, int]:
        self._prepare_players()
        self._exchange_attacks()
        self._clamp_health()

        return self._get_health_status()

    def _prepare_players(self) -> None:
        self.knight1.prepare_for_battle()
        self.knight2.prepare_for_battle()

    def _exchange_attacks(self) -> None:
        self.knight1.hp -= max(0, self.knight2.power - self.knight1.protection)
        self.knight2.hp -= max(0, self.knight1.power - self.knight2.protection)

    def _clamp_health(self) -> None:
        self.knight1.hp = max(0, self.knight1.hp)
        self.knight2.hp = max(0, self.knight2.hp)

    def _get_health_status(self) -> dict[str, int]:
        return {
            self.knight1.name: self.knight1.hp,
            self.knight2.name: self.knight2.hp,
        }
