from characters.knights import Knights
from items.potion import Potion
from items.armour import Armour
from items.weapon import Weapon
from typing import Type


class HeroManipulations:
    def __init__(self) -> None:
        pass

    @staticmethod
    def add_to_classes(hero: dict) -> None:
        Knights(hero)
        Weapon(hero["weapon"], hero["name"])
        if hero["potion"]:
            Potion(hero["potion"], hero["name"])
        for armour in hero["armour"]:
            Armour(armour, hero["name"])

    @staticmethod
    def hero_status(warriors_class: Type[Knights]) -> dict:
        status = {}

        for key, value in warriors_class.heroes.items():
            status[key] = value.hp

        return status
