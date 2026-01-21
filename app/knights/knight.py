from __future__ import annotations
from app.knights.armors import Armour, Weapon, Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp

    def update_knight(
            self,
            knights_in_dictionary: dict,
            knight: str
    ) -> Knight:
        self.armour = [
            Armour(unit["part"], unit["protection"])
            for unit in knights_in_dictionary[knight]["armour"]
        ]
        self.weapon = Weapon(
            knights_in_dictionary[knight]["weapon"]["name"],
            knights_in_dictionary[knight]["weapon"]["power"]
        )
        if knights_in_dictionary[knight]["potion"]:
            self.potion = Potion(
                knights_in_dictionary[knight]["potion"]["name"],
                knights_in_dictionary[knight]["potion"]["effect"]
            )
        return self

    def apply_equipment(self) -> Knight:
        if hasattr(self, "weapon"):
            self.power += self.weapon.power
        if hasattr(self, "armour"):
            self.protection = 0
            self.protection += sum(unit.protection for unit in self.armour)
        if hasattr(self, "potion"):
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]
            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]
            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
        return self
