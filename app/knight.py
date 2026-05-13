"""Knight class representing a single knight with their stats and equipment."""

from typing import Any, Dict, List, Optional


class Knight:
    """Represents a knight with stats, armor, weapon, and potion."""

    def __init__(self, name: str, power: int, hp: int,
                 armour: Optional[List[Dict[str, Any]]] = None,
                 weapon: Optional[Dict[str, Any]] = None,
                 potion: Optional[Dict[str, Any]] = None) -> None:
        """Initialize a knight with basic stats and equipment.

        Args:
            name: Knight's name.
            power: Base power stat.
            hp: Health points.
            armour: List of armor pieces with protection values.
            weapon: Weapon with power bonus.
            potion: Potion with effects (hp, power, protection).
        """
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion

        # Final calculated stats
        self.power = power
        self.hp = hp
        self.protection = 0

    def calculate_protection(self) -> int:
        """Calculate total protection from armor pieces.

        Returns:
            Total protection value.
        """
        protection = 0
        for armour_piece in self.armour:
            protection += armour_piece.get("protection", 0)
        return protection

    def apply_weapon(self) -> None:
        """Apply weapon power bonus to knight's power."""
        if self.weapon:
            self.power += self.weapon.get("power", 0)

    def apply_potion(self) -> None:
        """Apply potion effects to knight's stats."""
        if self.potion is None:
            return

        effect = self.potion.get("effect", {})
        self.power += effect.get("power", 0)
        self.hp += effect.get("hp", 0)
        self.protection += effect.get("protection", 0)

    def prepare_for_battle(self) -> None:
        """Prepare knight for battle by applying all equipment and potions."""
        self.protection = self.calculate_protection()
        self.apply_weapon()
        self.apply_potion()

    def take_damage(self, opponent_power: int) -> None:
        """Reduce HP based on opponent's power minus self protection.

        Args:
            opponent_power: Opponent's total power stat.
        """
        damage = max(0, opponent_power - self.protection)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def get_stats(self) -> Dict[str, int]:
        """Get current knight stats.

        Returns:
            Dictionary with hp, power, and protection.
        """
        return {
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection,
        }
