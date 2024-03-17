from app.models.knight import Knight
from typing import Dict


class Battle:
    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= max(0, knight2.power - knight1.protection)
        knight2.hp -= max(0, knight1.power - knight2.protection)

    @staticmethod
    def calculate_result(knights: Dict[str, Knight]) -> Dict[str, int]:
        for knight in knights.values():
            knight.prepare_for_battle()
        Battle.fight(knights["Lancelot"], knights["Mordred"])
        Battle.fight(knights["Arthur"], knights["Red Knight"])
        return {k.name: max(0, k.hp) for k in knights.values()}
