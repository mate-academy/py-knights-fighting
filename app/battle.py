from typing import List, Dict
from knights import Knight


class Battle:
    def __init__(self, knights: List[Knight]) -> None:
        self.knights = knights

    def start(self) -> Dict[str, int]:
        for knight in self.knights:
            knight.initialize()

        battles = [(0, 1), (2, 3)]  # Lancelot vs Mordred, Arthur vs Red Knight

        results = {}
        for knight_index1, knight_index2 in battles:
            knight1, knight2 = self.knights[knight_index1], \
                self.knights[knight_index2]
            while knight1.hp > 0 and knight2.hp > 0:
                knight2.hp -= knight1.power - knight2.protection
                knight1.hp -= knight2.power - knight1.protection

            results[knight1.name] = max(knight1.hp, 0)
            results[knight2.name] = max(knight2.hp, 0)

        return results
