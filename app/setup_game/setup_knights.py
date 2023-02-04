from typing import List, Union

from app.items.armour import Armour
from app.items.potions import Potion
from app.items.weapons import Weapon
from app.players.knight import Knight
from app.setup_game.setup_items import get_potion, get_armour


class KnightSetup:

    @staticmethod
    def get_knight_potion(knight: dict) -> Union[Potion, None]:
        potion_object = knight.get("potion", None)
        if potion_object:
            potion_instance = get_potion(
                potion_object.get("name"),
                potion_object.get("effect"),
            )
        else:
            return None
        return potion_instance

    @staticmethod
    def get_knight_armour(knight: dict) -> List[Armour]:
        armour_instances = []

        for armour_part in knight["armour"]:
            armour_instances.append(
                get_armour(
                    armour_part["part"],
                    armour_part["protection"]
                ))

        return armour_instances

    @staticmethod
    def get_knight_weapon(knight: dict) -> Weapon:
        weapon_name = knight["weapon"]["name"]
        weapon_power = knight["weapon"]["power"]
        return Weapon(weapon_name, weapon_power)

    @classmethod
    def get_knight_instance(cls, name: str, knight: dict) -> Knight:
        knight_power = knight["power"]
        knight_hp = knight["hp"]

        armour_instances = cls.get_knight_armour(knight)
        weapon_instance = cls.get_knight_weapon(knight)
        potion_instance = cls.get_knight_potion(knight)

        knight_instance = Knight(
            name=name,
            power=knight_power,
            hp=knight_hp,
            armour=armour_instances,
            weapon=weapon_instance,
            potion=potion_instance
        )
        return knight_instance
