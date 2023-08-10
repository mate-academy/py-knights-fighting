from __future__ import annotations  # Enable forward annotations

from typing import Dict

from app.Knights import Knight


class Battle:
    @staticmethod
    def make_ready_2_battle(
            knights_dic: Dict[str, Knight]
    ) -> None:
        for knight in knights_dic.values():
            if knight.potion:
                knight.potion_effect()
            knight.apply_armour()
            knight.add_weapon(knight.weapon)
            knight.apply_weapon()

    @staticmethod
    def make_fight(
            knights: Dict[str, Knight]
    ) -> None:
        # 1 Lancelot vs Mordred:
        knights["Lancelot"].hp -= (
            knights["Mordred"].power - knights["Lancelot"].protection
        )
        knights["Mordred"].hp -= (
            knights["Lancelot"].power - knights["Mordred"].protection
        )

        # 2 Arthur vs Red Knight:
        knights["Arthur"].hp -= (
            knights["Red Knight"].power - knights["Arthur"].protection
        )
        knights["Red Knight"].hp -= (
            knights["Arthur"].power - knights["Red Knight"].protection
        )

    @staticmethod
    def is_anyone_alive(
            knights: Dict[str, Knight]
    ) -> None:
        for fighter in knights.values():
            if fighter.hp <= 0:
                fighter.hp = 0

    @staticmethod
    def return_result(
            knights: Dict[str, Knight]
    ) -> Dict[str, int]:
        return {
            "Lancelot": knights["Lancelot"].hp,
            "Arthur": knights["Arthur"].hp,
            "Mordred": knights["Mordred"].hp,
            "Red Knight": knights["Red Knight"].hp,
        }
