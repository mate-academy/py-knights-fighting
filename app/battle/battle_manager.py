from app.knights.knight import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class BattleManager:
    def __init__(self, knights_config: tuple) -> None:
        self.knights = [
            Knight(
                knight_data["name"],
                knight_data["power"],
                knight_data["hp"],
                [
                    Armour(armour["part"],
                           armour["protection"])
                    for armour in knight_data["armour"]
                ],
                Weapon(knight_data["weapon"]["name"],
                       knight_data["weapon"]["power"]),
                Potion(knight_data["potion"]["name"],
                       knight_data["potion"]["effect"])
                if knight_data["potion"]
                else None,
            )
            for knight_data in knights_config.values()
        ]

    def apply_attributes(self) -> None:
        for knight in self.knights:
            knight.apply_armour()
            knight.apply_weapon()
            knight.apply_potion()

    @staticmethod
    def duel(knight_1: Knight, knight_2: Knight) -> None:
        knight_2.hp -= knight_1.power - knight_2.protection
        knight_1.hp -= knight_2.power - knight_1.protection

        knight_1.hp = 0 if knight_1.hp <= 0 else knight_1.hp
        knight_2.hp = 0 if knight_2.hp <= 0 else knight_2.hp

    def battle(self) -> dict[str, int]:

        lancelot = self.knights[0]
        mordred = self.knights[2]
        arthur = self.knights[1]
        red_knight = self.knights[3]

        knights = [lancelot, mordred, arthur, red_knight]

        for knight in range(0, len(knights), 2):
            if knight + 1 < len(knights):
                self.duel(knights[knight], knights[knight + 1])

        return {
            knight.name: knight.hp for knight in self.knights
        }
