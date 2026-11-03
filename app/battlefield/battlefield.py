from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.khight.knight import Knight


class Battlefield:

    knights = {}

    @classmethod
    def create_knights(cls, knights: dict) -> None:
        cls.knights.clear()

        for knight_key, knight in knights.items():

            potion = None

            if knight.get("potion"):
                potion_data = knight["potion"]
                effect = potion_data.get("effect", {})

                potion = Potion(
                    potion_data["name"],
                    effect.get("hp", 0),
                    effect.get("power", 0),
                    effect.get("protection", 0)
                )

            weapon = Weapon(
                knight["weapon"]["name"],
                knight["weapon"]["power"]
            )

            armours = [
                Armour(item["part"], item["protection"])
                for item in knight.get("armour", [])
            ]

            created_knight = Knight(
                knight["name"],
                knight["power"],
                knight["hp"],
                armours,
                weapon,
                potion
            )

            cls.knights[knight_key] = created_knight

    @staticmethod
    def duel(knight1: Knight, knight2: Knight) -> None:
        knight1.apply_buffs()
        knight2.apply_buffs()

        damage1 = knight2.power - knight1.protection
        damage2 = knight1.power - knight2.protection

        knight1.hp = max(0, knight1.hp - damage1)
        knight2.hp = max(0, knight2.hp - damage2)

        if knight1.hp == 0:
            print(f"Knight {knight1.name} fell in the battlefield")

        if knight2.hp == 0:
            print(f"Knight {knight2.name} fell in the battlefield")

    @classmethod
    def display_knights(cls) -> None:
        for knight in cls.knights.values():
            print(knight.name)
