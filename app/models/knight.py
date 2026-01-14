from dataclasses import dataclass, field
from typing import List, Optional

from app.models.equipment import Armour, Weapon, Potion


@dataclass
class Knight:
    name: str
    hp: int
    power: int
    armour: List[Armour]
    weapon: Weapon
    potion: Optional[Potion]

    protection: int = field(init=False)

    def __post_init__(self) -> None:
        self.protection = 0

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        return cls(
            name=config["name"],
            hp=config["hp"],
            power=config["power"],
            armour=[Armour(**a) for a in config["armour"]],
            weapon=Weapon(**config["weapon"]),
            potion=Potion(**config["potion"]) if config["potion"] else None,
        )

    def prepare_for_battle(self) -> None:
        self._apply_armour()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armour(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

    def _apply_weapon(self) -> None:
        self.power += self.weapon.power

    def _apply_potion(self) -> None:
        if not self.potion:
            return

        for stat, value in self.potion.effect.items():
            setattr(self, stat, getattr(self, stat) + value)

    def take_damage(self, enemy_power: int) -> None:
        damage = enemy_power - self.protection
        self.hp = max(self.hp - damage, 0)
