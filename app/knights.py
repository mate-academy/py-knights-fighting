from dataclasses import dataclass, field


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: list
    weapon: dict
    potion: dict
    protection: int = field(default=0)
