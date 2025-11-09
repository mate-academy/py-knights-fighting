"""Main battle orchestration module."""

from typing import Dict, Any

from app.config import KNIGHTS
from app.knights.knight_factory import KnightFactory
from app.battle.battle_manager import BattleManager


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    """
    Orchestrate a battle between knights.

    This function conducts two duels:
    1. Lancelot vs Mordred
    2. Arthur vs Red Knight

    Args:
        knights_config: Dictionary containing knight configurations

    Returns:
        Dictionary mapping knight names to their remaining HP
    """
    knights = KnightFactory.create_knights_from_config(knights_config)

    battle_manager = BattleManager()

    battle_manager.prepare_knights(knights.values())

    battle_manager.duel(knights["lancelot"], knights["mordred"])
    battle_manager.duel(knights["arthur"], knights["red_knight"])

    return battle_manager.get_results(knights.values())


if __name__ == "__main__":
    print(battle(KNIGHTS))
