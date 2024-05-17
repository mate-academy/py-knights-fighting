from __future__ import annotations

from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: Weapon,
                 potion: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @staticmethod
    def create_knight(knight_config: dict) -> Knight:
        armour_list = [Armour(armour["part"], armour["protection"])
                       for armour in knight_config["armour"]]
        weapon = Weapon(knight_config["weapon"]["name"],
                        knight_config["weapon"]["power"])
        potion = None
        if knight_config["potion"] is not None:
            potion = Potion(knight_config["potion"]["name"],
                            knight_config["potion"]["effect"])
        return Knight(knight_config["name"],
                      knight_config["power"],
                      knight_config["hp"],
                      armour_list,
                      weapon,
                      potion)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
