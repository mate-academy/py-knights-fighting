"""Battle management and combat resolution."""

from typing import Dict, List, Iterable, Any

from app.knights.knight import Knight


class BattleManager:
    """Manages combat between knights."""

    def __init__(self) -> None:
        """Initialize battle manager."""
        self.battle_log: List[Dict[str, Any]] = []

    def duel(self, knight1: Knight, knight2: Knight) -> None:
        """
        Conduct a duel between two knights.

        Both knights attack simultaneously, dealing damage to each other.

        Args:
            knight1: First knight
            knight2: Second knight
        """
        damage_to_knight2: int = knight1.total_power
        damage_to_knight1: int = knight2.total_power

        knight1.take_damage(damage_to_knight1)
        knight2.take_damage(damage_to_knight2)

        self.battle_log.append({
            "duel": f"{knight1.name} vs {knight2.name}",
            "knight1_hp": knight1.hp,
            "knight2_hp": knight2.hp
        })

    def prepare_knights(self, knights: Iterable[Knight]) -> None:
        """
        Prepare all knights for battle.

        Args:
            knights: List of Knight instances
        """
        for knight in knights:
            knight.prepare_for_battle()

    def get_results(self, knights: Iterable[Knight]) -> Dict[str, int]:
        """
        Get battle results as a dictionary.

        Args:
            knights: List of Knight instances

        Returns:
            Dictionary mapping knight names to remaining HP
        """
        return {knight.name: knight.hp for knight in knights}

    def clear_log(self) -> None:
        """Clear battle log."""
        self.battle_log = []
