from app.knight.armour import Armour
from app.knight.weapon import Weapon
from app.knight.potion import Potion


class Knight:
    def __init__(self, parameters: dict) -> None:
        self.name = parameters["name"]
        self.power = parameters["power"]
        self.hp = parameters["hp"]
        self.armour = [Armour(a) for a in parameters["armour"]]
        self.weapon = Weapon(parameters["weapon"])
        self.potion = None if parameters["potion"] is None \
            else Potion(parameters["potion"])
        self.protection = 0

    def __repr__(self) -> str:
        return f"{self.name.upper()} power {self.power} hp {self.hp}"

    def __str__(self) -> str:
        return f"{self.name.upper()} power {self.power} hp {self.hp}"

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part.protection

    def equip_weapon(self) -> None:
        self.power += self.weapon.power

    def use_potion(self) -> None:
        if self.potion is not None:
            self.power += self.potion.power
            self.hp += self.potion.hp
            self.protection += self.potion.protection
