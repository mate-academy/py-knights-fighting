from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list[Armour],
                 weapon: Weapon, potion: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_buffs(self) -> None:
        if self.armour:
            self.apply_armour()
        if self.potion:
            self.apply_potion()
        self.apply_weapon()

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        self.hp += self.potion.hp_buff or 0
        self.power += self.potion.power_buff or 0
        self.protection += self.potion.protection_buff or 0
