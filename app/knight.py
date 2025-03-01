from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion
from dataclasses import dataclass


@dataclass()
class Knight:
    name: str
    power: int
    hp: int
    armour: list
    weapon: Weapon | dict
    potion: Potion | dict = None
    protection: int = 0

    def __post_init__(self) -> None:
        self.weapon = Weapon(**self.weapon)

        if self.armour:
            self.armour = [Armour(**part) for part in self.armour]

        if self.potion:
            self.potion = Potion(**self.potion)

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            for effect, value in self.potion.effect.items():
                if hasattr(self, effect):
                    setattr(self, effect, getattr(self, effect) + value)
