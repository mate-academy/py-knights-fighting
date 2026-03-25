from typing import List, Optional
from app.models.weapon import Weapon
from app.models.armour import Armour
from app.models.potion import Potion


class Knight:
    def __init__(
        self,
        name: str,
        hp: int,
        power: int,
        weapon: Weapon,
        armour: List[Armour],
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.base_hp = hp
        self.base_power = power
        self.weapon = weapon
        self.armour = armour or []
        self.potion = potion

        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

        self.protection += sum(a.protection for a in self.armour)
        self.power += self.weapon.power

        if self.potion:
            self.hp += self.potion.effect.get("hp", 0)
            self.power += self.potion.effect.get("power", 0)
            self.protection += self.potion.effect.get("protection", 0)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
