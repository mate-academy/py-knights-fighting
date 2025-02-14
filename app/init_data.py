from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: list
    weapon: dict
    potion: None | dict
    protection: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        self.protection = sum(
            [protection["protection"] for protection in self.armour]
        )
        self.power += self.weapon["power"]
        if self.potion:
            self.hp += self.potion["effect"].get("hp", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)

    def __sub__(self, other: Knight) -> None:
        self.hp = max(0, self.hp - max(0, other.power - self.protection))
        other.hp = max(0, other.hp - max(0, self.power - other.protection))
