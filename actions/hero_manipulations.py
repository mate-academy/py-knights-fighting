from characters.knight import Knight
from items.potion import Potion
from items.armour import Armour
from items.weapon import Weapon
from typing import Type


class HeroManipulations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def add_to_classes(hero: dict) -> None:
        Knight(hero)
        Weapon(hero["weapon"], hero["name"])

        Potion(hero["potion"], hero["name"])

        hero_armour = 0
        for armour in hero["armour"]:
            hero_armour += armour["protection"]

        Armour(hero_armour, hero["name"])

    @staticmethod
    def hero_status(warriors_class: Type[Knight]) -> dict:
        status = {}

        for name, parameters in warriors_class.heroes.items():
            status[name] = parameters.hp

        return status
