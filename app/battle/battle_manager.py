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
        for attacker, defender in [(0, 2), (1, 3)]:
            attacker_knight = self.knights[attacker]
            defender_knight = self.knights[defender]

            defender_knight.hp -= \
                attacker_knight.power - defender_knight.protection
            attacker_knight.hp -= \
                defender_knight.power - attacker_knight.protection

            if defender_knight.hp <= 0:
                defender_knight.hp = 0

            if attacker_knight.hp <= 0:
                attacker_knight.hp = 0

        return {knight.name: knight.hp for knight in self.knights}
