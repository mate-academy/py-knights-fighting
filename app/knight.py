from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Knight:
    name: str
    hp: int
    power: int
    armour: List[Dict[str, int]]
    weapon: Dict[str, int]
    potion: Optional[Dict[str, Any]]
    protection: int = 0

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> "Knight":
        return cls(
            name=config["name"],
            hp=config["hp"],
            power=config["power"],
            armour=config.get("armour", []),
            weapon=config["weapon"],
            potion=config.get("potion"),
        )

    def apply_armour(self) -> None:
        self.protection = sum(
            part.get("protection", 0) for part in self.armour
        )

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        if self.potion is None:
            return
        effect = self.potion.get("effect", {})
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, amount: int) -> None:
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
