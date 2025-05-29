from typing import Dict, List, Optional

from .armour import Armour
from .potion import Potion
from .weapon import Weapon


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        armour: List[Armour],
        potion: Optional[Potion] = None
    ) -> None:
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion

    @property
    def total_protection(self) -> int:
        protection = sum(armour.protection for armour in self.armour)
        if self.potion and "protection" in self.potion.effect:
            protection += self.potion.effect["protection"]
        return max(0, protection)

    @property
    def total_power(self) -> int:
        power = self.base_power + self.weapon.power
        if self.potion and "power" in self.potion.effect:
            power += self.potion.effect["power"]
        return power

    @property
    def total_hp(self) -> int:
        hp = self.base_hp
        if self.potion and "hp" in self.potion.effect:
            hp += self.potion.effect["hp"]
        return hp

    def prepare_for_battle(self) -> Dict[str, int]:
        return {
            "name": self.name,
            "hp": self.total_hp,
            "power": self.total_power,
            "protection": self.total_protection,
        }

    def __repr__(self) -> str:
        return (
            f"Knight(name='{self.name}', power={self.base_power}, "
            f"hp={self.base_hp}, weapon={self.weapon}, "
            f"armour={self.armour}, potion={self.potion})"
        )
