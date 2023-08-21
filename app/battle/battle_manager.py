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
                    Armour(a["part"],
                           a["protection"]) for a in knight_data["armour"]
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

    def battle(self) -> dict[str, int]:
        lancelot = self.knights[0]
        mordred = self.knights[2]
        arthur = self.knights[1]
        red_knight = self.knights[3]

        lancelot.hp -= mordred.power - lancelot.protection
        mordred.hp -= lancelot.power - mordred.protection

        if lancelot.hp <= 0:
            lancelot.hp = 0

        if mordred.hp <= 0:
            mordred.hp = 0

        arthur.hp -= red_knight.power - arthur.protection
        red_knight.hp -= arthur.power - red_knight.protection

        if arthur.hp <= 0:
            arthur.hp = 0

        if red_knight.hp <= 0:
            red_knight.hp = 0

        return {
            knight.name: knight.hp for knight in self.knights
        }
