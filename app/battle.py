from typing import List
from app.knights import Knight


class BattleKnight:
    def __init__(self, knights: List[Knight]):
        self.knights = knights

    def battle_preparation(self) -> None:
        for knight in self.knights:
            knight.protection = sum(armour["protection"] for armour in knight.armour)
            knight.power += knight.weapon["power"]

            if knight.potion:
                knight.hp += knight.potion["effect"].get("hp", 0)
                knight.power += knight.potion["effect"].get("power", 0)
                knight.protection += knight.potion["effect"].get("protection", 0)

    def battle_process(self, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= max(0, knight2.power - knight1.protection)
        knight2.hp -= max(0, knight1.power - knight2.protection)
        self.check_felling_in_battle([knight1, knight2])

    @staticmethod
    def check_felling_in_battle(knights: List[Knight]) -> None:
        for knight in knights:
            if knight.hp <= 0:
                knight.hp = 0

    def show_battle_results(self) -> dict:
        return {knight.name: knight.hp for knight in self.knights}
