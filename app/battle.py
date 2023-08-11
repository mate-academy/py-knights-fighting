from __future__ import annotations  # Enable forward annotations

from typing import Dict

from app.Knights import Knight


class Battle:

    @staticmethod
    def make_fight(
            knights: Dict[str, Knight],
            fighter1: str,
            fighter2: str,
    ) -> None:
        knights[fighter1].hp -= (
            knights[fighter2].power - knights[fighter1].protection
        )
        knights[fighter2].hp -= (
            knights[fighter1].power - knights[fighter2].protection
        )

    @staticmethod
    def is_anyone_alive(
            knights: Dict[str, Knight]
    ) -> None:
        for fighter in knights.values():
            fighter.hp = 0 if fighter.hp <= 0 else fighter.hp

    @staticmethod
    def return_result(
            knights: Dict[str, Knight]
    ) -> Dict[str, int]:
        return {
            fighter.name: fighter.hp
            for fighter in knights.values()
        }
