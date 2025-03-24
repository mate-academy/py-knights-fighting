from typing import Type

from app.Armour import Armour
from app.Knight import Knight
from app.Potion import Potion
from app.Weapon import Weapon


class KnightsManager:

    def __init__(self) -> None:
        self.__all_knights = {}

    @property
    def all_knights(self) -> dict:
        return self.__all_knights

    def load_knights_config(self, knights_dict: dict) -> None:
        for knight_name, knight_dict in knights_dict.items():
            new_knight = self.new_knight_from_dict(knight_dict)

            if knight_dict["armour"]:
                new_armours_list = self.new_knight_armours_from_list(
                    knight_dict["armour"])
                new_knight.add_armours(new_armours_list)

            if knight_dict["weapon"]:
                new_weapon = self.new_equipment(Weapon, knight_dict["weapon"])
                new_knight.equip_weapon(new_weapon)

            if knight_dict["potion"]:
                new_potion = self.new_equipment(Potion, knight_dict["potion"])
                new_knight.equip_potion(new_potion)

            self.__all_knights.update({f"{knight_name}": new_knight})

    def new_knight_armours_from_list(
            self,
            knight_armours_list: list[dict]
    ) -> list[Armour]:
        armours_list = []
        for armour in knight_armours_list:
            new_armour = self.new_equipment(Armour, armour)
            armours_list.append(new_armour)
        return armours_list

    def get_knight_by_name(self, name: str) -> Knight:
        if name not in self.all_knights:
            raise ValueError(f'"{name}" not in knights list')
        return self.all_knights.get(name)

    def knights_summary(self) -> dict:
        return {knight.name: knight.hp for knight in self.all_knights.values()}

    @staticmethod
    def new_knight_from_dict(knight_dict: dict) -> Knight:
        return Knight(
            name=knight_dict["name"],
            power=knight_dict["power"],
            hp=knight_dict["hp"],
        )

    @staticmethod
    def new_equipment(equipment_class: Type,
                      equipment_dict: dict
                      ) -> Armour | Weapon | Potion:
        return equipment_class(**equipment_dict)

    @staticmethod
    def fight_between(knight1: Knight, knight2: Knight) -> None:
        knight1.fight_with(knight2)

    def __repr__(self) -> str:
        return "all_knights:\n" + "\n".join(
            [
                f"{index}: {repr(knight)}"
                for index, knight in enumerate(self.all_knights.values())
            ]
        )
