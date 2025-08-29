from dataclasses import dataclass, field
from typing import List, Dict, Optional




@dataclass
class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: List[Dict[str, int]]
    weapon: dict[str, int]
    potion: Optional[Dict[str, Dict[str, int]]]

    hp: int = field(init=False)
    power: int = field(init=False)
    protection: int = field(init=False)

    def __post_init__(self):
        self.hp = self.base_hp
        self.power = self.base_power
        self.protection = 0

    def prepare_to_battle(self):

        self.protection = 0
        for inventory in self.armour:
            self.protection += inventory['protection']


        self.power += self.weapon['power']

        if self.potion is not None:
            for stat in self.potion["effect"]:
                if stat == "hp":
                    self.hp += self.potion["effect"][stat]
                elif stat == "protection":
                    self.protection += self.potion["effect"][stat]
                elif stat == "power":
                    self.power += self.potion["effect"][stat]

                self.hp = max(self.hp, 0)


    def attack(self,other):

        dmg = self.power - other.protection
        other.hp -= dmg

        if other.hp <= 0:
            other.hp = 0

    def fight(self,other):

        while self.hp > 0 and other.hp > 0:
            self.attack(other)
            if other.hp > 0:
                other.attack(self)
        return self.hp, other.hp













