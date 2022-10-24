from __future__ import annotations
from app.knights.inventory import Inventory


class Knight:
    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armours: list = None,
            weapon: dict = None,
            potion: dict = None,
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.items = Inventory(weapon, armours, potion)
        self.protection = 0
        self.died = False
        self.activated_items = False
        self.boost_weapon = False
        self.boost_armour = False
        self.boost_potion = False

    @classmethod
    def pars(cls, knight: dict) -> Knight:
        return cls(
            name=knight["name"],
            hp=knight["hp"],
            power=knight["power"],
            armours=knight["armour"],
            weapon=knight["weapon"],
            potion=knight["potion"],
        )

    def activate_weapon(self):
        if not self.boost_weapon:
            self.power += self.items.weapon.power

            self.boost_weapon = True
            print(f"{self.name} boosted weapon!")
        else:
            print(f"{self.name} already boost weapon!")

    def activate_armour(self):
        if self.items.armour:
            if not self.boost_armour:
                self.protection += sum([arm.protection for arm in self.items.armour])
                self.boost_armour = True
                print(f"{self.name} boosted armour!")
            else:
                print(f"{self.name} already boost armour!")

    def activate_potion(self):
        if self.items.potion:
            if not self.boost_potion:
                for key, value in self.items.potion.effect.items():
                    if key == "hp":
                        self.hp += value
                    if key == "power":
                        self.power += value
                    if key == "protection":
                        self.protection += value

                self.boost_potion = True
                print(f"{self.name} got potion effect {self.items.potion.name}!")
            else:
                print(f"{self.name} already get potion!")

    def activate_items(self):
        if not self.activated_items:
            self.activate_weapon()
            self.activate_armour()
            self.activate_potion()

            self.activated_items = True

            print(f"{self.name} updated!")
        else:
            print(f"{self.name} activated!")
