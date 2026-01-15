from dataclasses import dataclass
from typing import List, Optional, Dict
from .armour import Armour
from .weapon import Weapon
from .potion import Potion


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: List[Armour]
    weapon: Weapon
    potion: Optional[Potion] = None
    protection: int = 0

    def __post_init__(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        if self.potion:
            self.apply_potion()

    def apply_armour(self) -> None:
        """Calculate total protection from all armour pieces"""
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self) -> None:
        """Add weapon power to knight's base power"""
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        """Apply potion effects to knight's stats"""
        if not self.potion:
            return

        effects = self.potion.effect
        self.power += effects.get("power", 0)
        self.protection += effects.get("protection", 0)
        self.hp += effects.get("hp", 0)

    def attack(self, opponent: "Knight") -> None:
        """Attack another knight, reducing their HP"""
        damage = max(0, self.power - opponent.protection)
        opponent.hp = max(0, opponent.hp - damage)

    @classmethod
    def from_config(cls, config: Dict) -> None:
        """Create Knight instance from configuration dictionary"""
        armour = [Armour(**a) for a in config.get("armour", [])]
        weapon = Weapon(**config["weapon"])
        potion = Potion(**config["potion"]) if config.get("potion") else None

        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=armour,
            weapon=weapon,
            potion=potion
        )
