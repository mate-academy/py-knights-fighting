"""Knight character class with combat capabilities."""

from typing import Dict, List, Optional, Any


class Knight:
    """Represents a knight with equipment and combat stats."""

    def __init__(
        self,
        name: str,
        base_power: int,
        hp: int,
        armour: Optional[List[Dict[str, Any]]] = None,
        weapon: Optional[Dict[str, Any]] = None,
        potion: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Initialize a knight with base stats and equipment.

        Args:
            name: Knight's name
            base_power: Base attack power
            hp: Hit points
            armour: List of armour pieces (optional)
            weapon: Weapon dictionary (optional)
            potion: Potion dictionary (optional)
        """
        self.name: str = name
        self.base_power: int = base_power
        self.hp: int = hp
        self.armour: List[Dict[str, Any]] = armour or []
        self.weapon: Optional[Dict[str, Any]] = weapon
        self.potion: Optional[Dict[str, Any]] = potion
        self._total_power: Optional[int] = None
        self._protection: Optional[int] = None

    @property
    def total_power(self) -> int:
        """Calculate total attack power including weapon and potions."""
        if self._total_power is None:
            power: int = self.base_power

            if self.weapon:
                power += self.weapon.get("power", 0)

            if self.potion and "effect" in self.potion:
                power += self.potion["effect"].get("power", 0)

            self._total_power = power

        return self._total_power

    @property
    def protection(self) -> int:
        """Calculate total protection from armour and potion effects."""
        if self._protection is None:
            protection: int = 0

            for armour_piece in self.armour:
                protection += armour_piece.get("protection", 0)

            if self.potion and "effect" in self.potion:
                protection += self.potion["effect"].get("protection", 0)

            self._protection = protection

        return self._protection

    def apply_potion_effects(self) -> None:
        """Apply potion effects to knight's stats."""
        if self.potion and "effect" in self.potion:
            effects: Dict[str, Any] = self.potion["effect"]

            if "hp" in effects:
                self.hp += effects["hp"]

    def take_damage(self, incoming_damage: int) -> int:
        """
        Receive damage reduced by protection.

        Args:
            incoming_damage: Raw damage before protection

        Returns:
            Actual damage taken after protection
        """
        actual_damage: int = max(0, incoming_damage - self.protection)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self) -> bool:
        """Check if knight is still alive."""
        return self.hp > 0

    def prepare_for_battle(self) -> None:
        """Prepare knight for battle by applying all effects."""
        self.apply_potion_effects()
        _ = self.total_power
        _ = self.protection

    def __repr__(self) -> str:
        """String representation of the knight."""
        return (
            f"Knight({self.name}, HP: {self.hp}, "
            f"Power: {self.total_power}, Protection: {self.protection})"
        )
