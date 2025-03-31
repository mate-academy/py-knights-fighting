from app.knights.knight import Knight
from typing import Dict, List, Tuple


class Battle:
    def __init__(self, pairs: List[Tuple[Knight, Knight]]) -> None:
        self.pairs = pairs

    def fight(self) -> Dict[str, int]:
        results = {}
        for knight1, knight2 in self.pairs:
            knight1.take_damage(knight2.power)
            knight2.take_damage(knight1.power)
            results[knight1.name] = knight1.hp
            results[knight2.name] = knight2.hp
        return results
