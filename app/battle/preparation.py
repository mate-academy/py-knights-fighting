from __future__ import annotations
from typing import List, Dict, TypedDict


class Armour(TypedDict):
    name: str
    protection: int


class Weapon(TypedDict):
    name: str
    power: int


class Potion(TypedDict):
    name: str
    effect: Dict[str, int]


class KnightType(TypedDict):
    name: str
    power: int
    hp: int
    armour: List[Armour | None]
    weapon: Weapon
    potion: Potion | None


class Knights:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: List[Armour] | None,
            weapon: Weapon,
            potion: Potion | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon.get("power")
        self.weapon_name = weapon.get("name")
        self.protection = 0
        self.potion = potion

    def apply_weapon(self) -> Knights:
        self.power += self.weapon
        return self

    def apply_armour(self) -> Knights:
        self.protection += sum(part.get("protection") for part in self.armour)
        return self

    def apply_potion(self) -> Knights:
        if self.potion:
            for effect, effect_stats in self.potion["effect"].items():
                self.__dict__[effect] += effect_stats
        return self

    @staticmethod
    def get_ready_for_battle(knight_unprepared: Knights) -> None:
        knight_unprepared.apply_weapon().apply_armour().apply_potion()
