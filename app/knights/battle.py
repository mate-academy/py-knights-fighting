from typing import Dict, Any
from app.knights.knight import Knight


class Battle:
    @staticmethod
    def fight(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
        knights = {
            name: Knight(data)
            for name, data in knights_config.items()
        }

        def duel(first: Knight, second: Knight) -> None:
            first.hp -= second.power - first.protection
            second.hp -= first.power - second.protection

            if first.hp < 0:
                first.hp = 0
            if second.hp < 0:
                second.hp = 0

        duel(knights["lancelot"], knights["mordred"])
        duel(knights["arthur"], knights["red_knight"])

        return {
            k.name: k.hp for k in knights.values()
        }
