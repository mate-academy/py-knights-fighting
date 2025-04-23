from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class Armour:
    part: str
    protection: int


@dataclass
class Weapon:
    name: str
    power: int


@dataclass
class PotionEffect:
    power: int = 0
    hp: int = 0
    protection: int = 0


@dataclass
class Potion:
    name: str
    effect: PotionEffect


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: List[Armour] = field(default_factory=list)
    weapon: Optional[Weapon] = None
    potion: Optional[Potion] = None
    protection: int = field(init=False)

    def __post_init__(self) -> None:
        self.protection = sum(armour.protection for armour in self.armour)
        if self.weapon:
            self.power += self.weapon.power
        if self.potion:
            self.power += self.potion.effect.power
            self.hp += self.potion.effect.hp
            self.protection += self.potion.effect.protection

    def take_damage(self, attacker_power: int) -> None:
        damage = max(0, attacker_power - self.protection)
        self.hp = max(0, self.hp - damage)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Knight:
        armour = [Armour(**a) for a in data.get("armour", [])]
        weapon = Weapon(**data["weapon"]) if data.get("weapon") else None
        potion = None
        if data.get("potion"):
            effect = PotionEffect(**data["potion"]["effect"])
            potion = Potion(name=data["potion"]["name"], effect=effect)

        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=armour,
            weapon=weapon,
            potion=potion
        )
