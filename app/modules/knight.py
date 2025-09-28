from app.modules.armour import Armour
from app.modules.weapon import Weapon
from app.modules.potion import Potion


class Knight:
    name: str
    power: int
    hp: int
    armour: list[Armour]
    weapon: Weapon
    potion: Potion
    protection: int

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion,
    ) -> None:
        self.name = name
        self.__power = power
        self.__hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.__protection = 0

    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, value: int) -> None:
        self.__power = value

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, value: int) -> None:
        self.__hp = value

    @property
    def protection(self) -> int:
        return self.__protection

    @protection.setter
    def protection(self, value: int) -> None:
        self.__protection = value

    def before_battle(self) -> None:
        if hasattr(self.potion, "effect"):
            self.power = self.__power + self.weapon.power \
                + self.potion.effect[0]
            self.hp = self.__hp + self.potion.effect[1]
            self.protection = self.__protection
            for item in self.armour:
                self.protection += item.protection
            self.protection += self.potion.effect[2]
        else:
            self.power = self.__power + self.weapon.power
            self.hp = self.__hp
            self.protection = self.__protection
            for item in self.armour:
                self.protection += item.protection

    def take_damage(self, damage: int) -> None:
        self.__hp -= (damage - self.protection)
        if self.__hp < 0:
            self.__hp = 0

    def attack(self, other: "Knight") -> None:
        """lancelot["hp"] -= mordred["power"] - lancelot["protection"]"""
        other.take_damage(self.power)