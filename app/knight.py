from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Knight:
    name: str
    base_power: int
    base_hp: int
    armour: List[Dict[str, int]]
    weapon: Dict[str, int]
    potion: Optional[Dict[str, Dict[str, int]]] = None
    hp: int = field(init=False)
    power: int = field(init=False)
    protection: int = field(init=False)

    def __post_init__(self) -> None:
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        """Apply armour, weapon and potion effects."""
        self.protection = sum(part["protection"] for part in self.armour)
        self.power = self.base_power + self.weapon["power"]
        self.hp = self.base_hp
        if self.potion:
            effect = self.potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def take_damage(self, damage: int) -> None:
        """Reduce knight hp by damage and floor at zero."""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
