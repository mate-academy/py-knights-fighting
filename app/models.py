from dataclasses import dataclass
from typing import Any


@dataclass
class Knight:
    name: str
    human_power: int
    human_hp: int
    armour: list[dict]
    weapon: dict
    potion: dict or None

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "human_hp" and value < 0:
            value = 0
        self.__dict__[key] = value

    def protection(self) -> int:
        sum_prot = sum([armour["protection"] for armour in self.armour])
        if self.potion is not None and self.potion["effect"].get("protection"):
            return sum_prot + self.potion["effect"]["protection"]
        return sum_prot

    def power(self) -> int:
        sum_power = self.human_power + self.weapon["power"]
        if self.potion is not None and self.potion["effect"].get("power"):
            return sum_power + self.potion["effect"]["power"]
        return sum_power

    def hp(self) -> int:
        if self.potion is not None and self.potion["effect"].get("hp"):
            return self.human_hp + self.potion["effect"]["hp"]
        return self.human_hp
