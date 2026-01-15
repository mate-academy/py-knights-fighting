from app.knight.armour import Armour
from app.knight.weapon import Weapon
from app.knight.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def calculate_stats(self) -> None:
        # apply armour
        for arm in self.armour:
            self.protection += arm.protection

        # apply weapon
        self.power += self.weapon.power

        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]

            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]

            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]
