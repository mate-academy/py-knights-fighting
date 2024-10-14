from typing import List, Optional
from app.knights_equipment.armour import Armour
from app.knights_equipment.potion import Potion
from app.knights_equipment.weapon import Weapon


class Knight:
    protection = 0

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Optional[List[Armour]],
            weapon: Weapon,
            potion: Optional[Potion] = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour if armour else []
        self.weapon = Weapon(weapon.name, weapon.power)
        self.potion = potion if potion else None

    def calculate_protection(self) -> int:
        """
        Calculate knight's protection
        at the beginning protection for all knight = 0
        sum of all armour's protection values and potion's protection
        """
        self.protection = 0

        for armour in self.armour:
            self.protection += armour.protection

        if self.potion is not None:
            if "protection" in self.potion.effect.keys():
                self.protection += self.potion.effect["protection"]

        print(f"{self.name} has protection = {self.protection}")
        return self.protection

    def calculate_power(self) -> int:
        """
        Calculate knight's power
        knight's power + weapon power + potion's power
        """

        if self.weapon:
            self.power += self.weapon.power

        if self.potion is not None:
            if "power" in self.potion.effect.keys():
                self.power += self.potion.effect["power"]

        print(f"{self.name} knight has power = {self.power}")
        return self.power

    def calculate_hp(self) -> int:
        """
        Calculate knight's hp
        knight's power + weapon power + potion's power
        """

        if self.potion is not None:
            if "hp" in self.potion.effect.keys():
                self.hp += self.potion.effect["hp"]

        print(f"{self.name} knight has hp = {self.hp}")
        return self.hp
