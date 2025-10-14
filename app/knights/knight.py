from typing import Dict
from .armour import Armour
from .weapon import Weapon
from .potion import Potion


class Knight:
    def __init__(self, stats: Dict) -> None:
        self.name: str = stats["name"]
        self._base_hp: int = stats["hp"]
        self._base_power: int = stats["power"]

        self.weapon = Weapon(stats.get("weapon", {}))
        self.armour = Armour(stats.get("armour", []))
        self.potion = Potion(stats.get("potion"))

        self.effective_protection: int = self._calculate_protection()
        self.effective_power: int = self._calculate_power()
        self.current_hp: int = self._calculate_max_hp()

    def _calculate_protection(self) -> int:
        total_protection = self.armour.get_total_protection()
        total_protection += self.potion.get_effect("protection")
        return total_protection

    def _calculate_power(self) -> int:
        total_power = self._base_power + self.weapon.power
        total_power += self.potion.get_effect("power")
        return total_power

    def _calculate_max_hp(self) -> int:
        start_hp = self._base_hp
        start_hp += self.potion.get_effect("hp")
        return start_hp

    def take_damage(self, opponent_power: int) -> None:

        damage_or_heal = opponent_power - self.effective_protection
        self.current_hp -= damage_or_heal

        if self.current_hp < 0:
            self.current_hp = 0

    def is_defeated(self) -> bool:
        return self.current_hp == 0
