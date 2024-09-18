from __future__ import annotations
from app.people.knight import Knight


class Championship:

    @staticmethod
    def duel(knight1: Knight, knight2: Knight) -> None:
        if isinstance(knight1, Knight) and isinstance(knight2, Knight):
            knight1.hp = (knight1.hp_total + knight1.protection
                          - knight2.power_total)
            knight2.hp = (knight2.hp_total + knight2.protection
                          - knight1.power_total)
            if knight1.hp <= 0:
                knight1.hp = 0
            if knight2.hp <= 0:
                knight2.hp = 0

    @staticmethod
    def statistics() -> dict:
        result = {}
        for knight_instance in Knight.knights_dict.values():
            if isinstance(knight_instance, Knight):
                result.update({knight_instance.name: knight_instance.hp})
        return result
