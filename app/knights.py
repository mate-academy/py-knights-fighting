from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: Armour,
                 weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour if armour is not None else []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        # apply armour
    def apply_armour(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

    # apply weapon
    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    # apply potion if exist
    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion.effect:
                self.power += self.potion.effect["power"]

            if "protection" in self.potion.effect:
                self.protection += self.potion.effect["protection"]

            if "hp" in self.potion.effect:
                self.hp += self.potion.effect["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
