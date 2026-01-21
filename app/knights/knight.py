from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int,) -> None:
        self.name = name.replace("_", " ").title()
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, armour: Armour) -> None:
        self.protection += armour.protection

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_potion(self, potion: Potion) -> None:
        self.power += potion.effect.get("power", 0)
        self.hp += potion.effect.get("hp", 0)
        self.protection += potion.effect.get("protection", 0)

    def check_hp(self) -> int:
        if self.hp < 0:
            self.hp = 0
        return self.hp
