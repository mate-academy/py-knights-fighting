from typing import Dict

from app.knight import Knight


class Battle:
    def __init__(self, knights: Dict[str, Knight]) -> None:
        self.knights = knights

    def fight(self, attacker_key: str, defender_key: str) -> None:
        attacker = self.knights[attacker_key]
        defender = self.knights[defender_key]

        attacker_damage = max(0, defender.power - attacker.protection)
        defender_damage = max(0, attacker.power - defender.protection)

        attacker.take_damage(attacker_damage)
        defender.take_damage(defender_damage)

    def run(self) -> Dict[str, int]:
        for knight in self.knights.values():
            knight.prepare_for_battle()

        self.fight("lancelot", "mordred")
        self.fight("arthur", "red_knight")

        return {
            knight.name: knight.hp for knight in self.knights.values()
        }
