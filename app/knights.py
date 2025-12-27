from app.ammunition.armour import Armour
from app.ammunition.potion import Potion
from app.ammunition.weapon import Weapon


class Knight:
    """"Knight transformed from incoming dict key to class"""
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list["Armour"],
        weapon: "Weapon",
        potion: "Potion"
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        """"Use all items"""
        self.wear_armor()
        self.use_potion()
        self.take_sword()

    def wear_armor(self) -> None:
        """"Add values from items to class instance"""
        for element in self.armour:
            self.protection += element.protection

    def use_potion(self) -> None:
        """"Add values from items to class instance"""
        if self.potion is None:
            return
        buffs = self.potion.to_dict()
        self.hp += buffs["hp"]
        self.power += buffs["power"]
        self.protection += buffs["protection"]

    def take_sword(self) -> None:
        """"Add values from items to class instance"""
        self.power += self.weapon.power
