from app.equipment.weapon import Weapon
from app.equipment.armour import Armour
from app.equipment.potion import Potion


class Knight:
    knights = {}

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            armour: list[Armour | None],
            potion: Potion | None
    ) -> None:
        self.name = name
        self.weapon = weapon
        self.armours = armour
        self.potion = potion
        self.power = power + weapon.power + potion.power
        self.hp = hp + potion.hp
        self.protection = self.calculate_protection()
        self.knights[self.name] = self

    def calculate_protection(self) -> int:
        total = 0
        for armor in self.armours:
            total += armor.protection

        total += self.potion.protection
        return total

    def set_hp(self, hp: int) -> None:
        if hp < 0:
            self.hp = 0
        else:
            self.hp = hp

    def __str__(self) -> str:
        return f"Knight {self.name}, hp = {self.hp}, " \
            f"power = {self.power}, protection = {self.protection}"
