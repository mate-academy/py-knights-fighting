from dataclasses import dataclass
from typing import List

from app.models.equipment import Weapon, Armor
from app.models.potion import Potion


@dataclass
class Knight:
    """Class representing a knight with armor, weapon, and potion"""
    name: str
    power: int
    hp: int
    armor: List[Armor]
    weapon: Weapon
    potion: Potion = None

    def prepare_for_battle(self) -> None:
        """Apply armor, weapon, and potion effects before battle"""
        self._apply_armor()
        self._apply_weapon()
        self._apply_potion()

    def _apply_armor(self) -> None:
        """Calculate total protection from armor pieces"""
        self.protection = sum(
            armor_piece.protection
            for armor_piece in self.armor
        )

    def _apply_weapon(self) -> None:
        """Apply weapon effects to the knight's power"""
        self.power += self.weapon.power

    def _apply_potion(self) -> None:
        """Apply potion effects if available"""
        if self.potion is not None:
            effect = self.potion.effect
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]

    def take_damage(self, opponent_power: int) -> int:
        """Calculate and apply damage from an opponent"""
        damage = max(0, opponent_power - self.protection)
        self.hp = max(0, self.hp - damage)
        return damage
