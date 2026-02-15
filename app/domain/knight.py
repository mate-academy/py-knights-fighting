from dataclasses import dataclass
from registry import ItemRegistry, Loadout

@dataclass(slots=True)
class Knight:
    name: str
    hp: int
    power: int
    protection: int
    registry: ItemRegistry
    equipment: Loadout