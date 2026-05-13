"""Battle simulation logic for knights."""

from typing import Any, Dict

from app.knight import Knight


class BattleSimulation:
    """Simulates battles between knights."""

    def __init__(self, knights_config: Dict[str, Dict[str, Any]]) -> None:
        """Initialize battle simulation with knights configuration.

        Args:
            knights_config: Dictionary with knight configurations.
        """
        self.knights_config = knights_config
        self.knights: Dict[str, Knight] = {}
        self._initialize_knights()

    def _initialize_knights(self) -> None:
        """Initialize Knight objects from configuration."""
        for key, knight_data in self.knights_config.items():
            knight = Knight(
                name=knight_data["name"],
                power=knight_data["power"],
                hp=knight_data["hp"],
                armour=knight_data.get("armour", []),
                weapon=knight_data.get("weapon"),
                potion=knight_data.get("potion"),
            )
            self.knights[key] = knight

    def prepare_all_knights(self) -> None:
        """Prepare all knights for battle."""
        for knight in self.knights.values():
            knight.prepare_for_battle()

    def execute_battle_round(self, knight1_key: str, knight2_key: str) -> None:
        """Execute one battle round between two knights.

        Args:
            knight1_key: Key of first knight.
            knight2_key: Key of second knight.
        """
        knight1 = self.knights[knight1_key]
        knight2 = self.knights[knight2_key]

        # Both knights attack simultaneously
        knight1.take_damage(knight2.power)
        knight2.take_damage(knight1.power)

    def get_battle_results(self) -> Dict[str, int]:
        """Get battle results with knight names and remaining HP.

        Returns:
            Dictionary mapping knight names to their remaining HP.
        """
        return {
            knight.name: knight.hp for knight in self.knights.values()
        }

    def run_tournament(self) -> Dict[str, int]:
        """Run the complete tournament with predefined battles.

        Returns:
            Dictionary mapping knight names to their remaining HP.
        """
        self.prepare_all_knights()

        # Battle 1: Lancelot vs Mordred
        self.execute_battle_round("lancelot", "mordred")

        # Battle 2: Arthur vs Red Knight
        self.execute_battle_round("arthur", "red_knight")

        return self.get_battle_results()
