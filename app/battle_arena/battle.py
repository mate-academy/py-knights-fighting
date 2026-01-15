from __future__ import annotations

from app.battle_arena.equipped_knight import EquippedKnight as Knight


class Battle:

    @staticmethod
    def versus(knight_one: Knight, knight_two: Knight) -> None:
        knight_one.hp -= knight_two.power - knight_one.protection
        knight_two.hp -= knight_one.power - knight_two.protection
        if knight_one.hp < 0:
            knight_one.hp = 0
        if knight_two.hp < 0:
            knight_two.hp = 0

    @staticmethod
    def battle(lancelot: Knight,
               mordred: Knight,
               artur: Knight,
               red_knight: Knight) -> dict:
        Battle.versus(lancelot, mordred)
        Battle.versus(artur, red_knight)
        return {
            lancelot.name: lancelot.hp,
            artur.name: artur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp
        }
