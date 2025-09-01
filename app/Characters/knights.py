from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: List[Dict[str, int]]
    weapon: dict[str, int]
    potion: Optional[Dict[str, Dict[str, int]]]

    protection: int = field(init=False)

    def __post_init__(self) -> None:
        self.protection = 0

    def prepare_to_battle(self) -> None:

        self.protection = 0
        for inventory in self.armour:
            self.protection += inventory["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            for stat in self.potion["effect"]:
                if stat == "hp":
                    self.hp += self.potion["effect"][stat]
                elif stat == "protection":
                    self.protection += self.potion["effect"][stat]
                elif stat == "power":
                    self.power += self.potion["effect"][stat]

                self.hp = max(self.hp, 0)

    def attack(self, other: "Knight") -> None:

        dmg = self.power - other.protection
        other.hp -= dmg

        if other.hp <= 0:
            other.hp = 0

    def fight(self, other: "Knight") -> tuple[int, int]:

        while self.hp > 0 and other.hp > 0:
            self.attack(other)
            if other.hp > 0:
                other.attack(self)
        return self.hp, other.hp
