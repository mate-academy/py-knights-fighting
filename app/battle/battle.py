from typing import Dict, List
from app.entities.knight import Knight


class Battle:
    def __init__(self, knights: Dict[str, Knight]) -> None:
        self.knights = knights

    def start(self, pairs: List[tuple]) -> Dict:
        for knight in self.knights.values():
            knight.prepare_for_battle()

        # BATTLE:
        for pair in pairs:
            self.fight(self.knights[pair[0]], self.knights[pair[1]])

        # Return battle results:
        return {knight.name: knight.hp for knight in self.knights.values()}

    @staticmethod
    def fight(knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= max(0, knight2.power - knight1.protection)
        knight2.hp -= max(0, knight1.power - knight2.protection)

        # check if someone fell in battle
        if knight1.hp <= 0:
            knight1.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0
