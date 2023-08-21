from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]

            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]

            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
