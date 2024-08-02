from typing import Dict

from app.knights.equipment import Armour, Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: [Dict] = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = [Armour(**a) for a in armour]
        self.weapon = Weapon(**weapon)
        self.potion = Potion(**potion) if potion else None
        self.power = 0
        self.hp = 0
        self.protection = 0
        self.apply_equipment()

    def apply_equipment(self) -> None:
        self.power = self.base_power + self.weapon.power
        self.hp = self.base_hp
        self.protection = sum([a.protection for a in self.armour])
        if self.potion:
            self.power += self.potion.effect.get("power", 0)
            self.hp += self.potion.effect.get("hp", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
