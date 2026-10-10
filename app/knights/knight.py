from dataclasses import dataclass, field
from typing import List, Optional

from app.knights.equipment import ArmourPart, Potion, Weapon


@dataclass
class Knight:
    name: str
    base_power: int
    base_hp: int
    weapon: Weapon
    armour: List[ArmourPart] = field(default_factory=list)
    potion: Optional[Potion] = None

    def __post_init__(self) -> None:
        self.hp = self.base_hp + self._potion_effect("hp")

    @property
    def power(self) -> int:
        return (
            self.base_power
            + self.weapon.power
            + self._potion_effect("power")
        )

    @property
    def protection(self) -> int:
        armour_protection = sum(part.protection for part in self.armour)
        return armour_protection + self._potion_effect("protection")

    @property
    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int) -> None:
        self.hp = max(0, self.hp - max(0, damage))

    def _potion_effect(self, key: str) -> int:
        if self.potion is None:
            return 0
        return self.potion.effect.get(key, 0)
