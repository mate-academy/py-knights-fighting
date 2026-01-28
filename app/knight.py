from app.armour import Armour
from app.weapon import Weapon
from app.potion import Potion


class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.base_power = power
        self.hp = hp
        self.armour = [Armour(**a) for a in armour]
        self.weapon = Weapon(**weapon)
        self.potion = Potion(**potion) if potion else None
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.protection = sum([a.protection for a in self.armour])
        self.power = self.base_power + self.weapon.power
        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= max(0, damage - self.protection)
        if self.hp < 0:
            self.hp = 0
