from app.models.armours import Armours
from app.models.potion import Potion
from app.models.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = Armours(armour)
        self.weapon = Weapon(weapon)
        self.potion = Potion(potion) if potion else None
        self.protection = 0
