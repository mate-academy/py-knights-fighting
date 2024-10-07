from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class Weapon:
    name: str
    power: int


@dataclass
class Armour:
    part: str
    protection: int


@dataclass
class Potion:
    name: str
    effect: dict


@dataclass
class Knight:
    name: str
    base_power: int
    hp: int
    armour: List[Armour] = field(default_factory=list)
    weapon: Optional[Weapon] = None
    potion: Optional[Potion] = None

    def prepare_for_battle(self) -> Dict[str, int]:
        protection = sum(a.protection for a in self.armour)
        power = self.base_power + (self.weapon.power if self.weapon else 0)

        if self.potion:
            power += self.potion.effect.get("power", 0)
            protection += self.potion.effect.get("protection", 0)
            self.hp += self.potion.effect.get("hp", 0)

        return {
            "hp": self.hp,
            "power": power,
            "protection": protection,
        }
