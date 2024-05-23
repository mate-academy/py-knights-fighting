from app.potion import Potion
from app.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list, weapon: Weapon, potion: Potion | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
