from dataclasses import dataclass, field
from .equipment import Armour, Weapon, Potion


@dataclass
class Knight:
    name: str
    base_power: int
    base_hp: int
    armours: list[Armour] = field(default_factory=list)
    weapon: Weapon | None = None
    potion: Potion | None = None

    def final_stats(self) -> dict:
        stats = {"hp": self.base_hp, "power": self.base_power, "protection": 0}
        stats["protection"] = sum(a.protection for a in self.armours)
        if self.weapon:
            stats["power"] += self.weapon.power
        if self.potion:
            for stat in ["hp", "power", "protection"]:
                stats[stat] += self.potion.effect.get(stat, 0)
        return stats
