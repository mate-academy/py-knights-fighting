from app.equipment import Armour
from app.equipment import Weapon
from app.equipment import Potion


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: Armour = None,
            weapon: Weapon = None,
            potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        if self.armour is not None:
            self.protection += self.armour.protection

    def apply_weapon(self) -> None:
        if self.weapon is not None:
            self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            effects = self.potion.effect
            self.power += effects.get("power", 0)
            self.hp += effects.get("hp", 0)
            self.protection += effects.get("protection", 0)
            self.potion = None
