from __future__ import annotations  # Enable forward annotations

from typing import List, Optional

from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: Optional[List[dict]] = [],
        weapon: Optional[dict] = None,
        potion: Optional[dict] = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def potion_effect(self) -> None:
        for effect, value in self.potion.effect.items():
            if effect == "hp":
                self.hp += value
            elif effect == "protection":
                self.protection += value
            elif effect == "power":
                self.power += value

    def add_weapon(self, weapon: dict) -> None:
        self.weapon = Weapon(weapon["name"], weapon["power"])

    def apply_weapon(
        self,
    ) -> None:
        self.power += self.weapon.power

    def add_armour(self, armour: dict) -> None:
        if armour:
            self.armour = []
            for fighter in armour:
                self.armour.append(
                    Armour(
                        fighter["part"],
                        fighter["protection"]
                    )
                )

    def apply_armour(
        self,
    ) -> None:
        for armour_add in self.armour:
            self.protection += armour_add.protection

    @staticmethod
    def create_dict_of_knghtes(
        persons: dict,
    ) -> dict[str, Knight]:
        knights_dict = {}

        for person in persons.values():
            knight = Knight(
                name=person["name"],
                power=person["power"],
                hp=person["hp"],
                weapon=person["weapon"],
            )
            knight.add_armour(person["armour"])
            if person["potion"]:
                knight.potion = Potion()
                knight.potion.name = person["potion"]["name"]
                knight.potion.effect = person["potion"]["effect"]
            knights_dict[knight.name] = knight

        for knight in knights_dict.values():
            if knight.potion:
                knight.potion_effect()
            knight.apply_armour()
            knight.add_weapon(knight.weapon)
            knight.apply_weapon()

        return knights_dict
