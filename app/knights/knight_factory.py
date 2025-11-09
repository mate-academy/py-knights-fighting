"""Factory for creating knights from configuration."""

from typing import Dict, Any

from app.knights.knight import Knight


class KnightFactory:
    """Factory class for creating Knight instances from configuration."""

    @staticmethod
    def create_knight(config: Dict[str, Any]) -> Knight:
        """
        Create a Knight instance from a configuration dictionary.

        Args:
            config: Dictionary containing knight configuration

        Returns:
            Knight instance
        """
        return Knight(
            name=config.get("name"),
            base_power=config.get("power"),
            hp=config.get("hp"),
            armour=config.get("armour"),
            weapon=config.get("weapon"),
            potion=config.get("potion")
        )

    @staticmethod
    def create_knights_from_config(
        knights_config: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Knight]:
        """
        Create multiple knights from a configuration dictionary.

        Args:
            knights_config: Dictionary mapping knight IDs to configurations

        Returns:
            Dictionary mapping knight IDs to Knight instances
        """
        knights: Dict[str, Knight] = {}
        for knight_id, config in knights_config.items():
            knights[knight_id] = KnightFactory.create_knight(config)

        return knights
