"""Main entry point for the knights championship simulation."""

from typing import Any
from app.battles.battle import Tournament
from app.knights.constants import KNIGHTS


__all__ = ["battle", "KNIGHTS"]


def battle(knights_config: dict[str, Any]) -> dict[str, int]:
    tournament = Tournament.from_config(knights_config)
    return tournament.run()
