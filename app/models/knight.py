from app.models.potion import Potion
from app.models.armour import Armour
from app.models.weapon import Weapon


class Knight:

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
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.total_protection = 0
        self.total_power = 0
