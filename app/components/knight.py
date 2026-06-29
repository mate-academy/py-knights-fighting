from app.components.armour import Armour
from app.components.potion import Potion
from app.components.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armours: list[Armour]) -> None:
        for armour in armours:
            self.protection += armour.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        self.power += potion.effect.get("power", 0)
        self.hp += potion.effect.get("hp", 0)
        self.protection += potion.effect.get("protection", 0)
