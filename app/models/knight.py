from dataclasses import dataclass, field
from typing import List, Optional
from .armour import Armour
from .magic import Magic
from .potion import Potion
from .weapon import Weapon


@dataclass
class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: List[Armour] = field(default_factory=list)
    weapon: Optional[Weapon] = None
    potion: Optional[Potion] = None
    magic: Optional[Magic] = None

    # Computed stats
    power: int = field(init=False)
    hp: int = field(init=False)
    protection: int = field(init=False)

    def __post_init__(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        self.apply_magic()

    def apply_armour(self) -> None:
        self.protection = sum(
            a.protection for a in self.armour
        ) if self.armour else 0

    def apply_weapon(self) -> None:
        if self.weapon:
            self.power = self.base_power + self.weapon.power
        else:
            self.power = self.base_power

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.get_effect()
            self.power += effect.get("power", 0)
            self.hp = self.base_hp + effect.get("hp", 0)
            self.protection += effect.get("protection", 0)
        else:
            self.hp = self.base_hp

    def apply_magic(self) -> None:
        if self.magic:
            magic_power = self.magic.get_power()
            self.power += magic_power

    def take_damage(self, damage: int) -> None:
        actual_damage = max(damage - self.protection, 0)
        self.hp = max(self.hp - actual_damage, 0)

    def is_defeated(self) -> bool:
        return self.hp <= 0
