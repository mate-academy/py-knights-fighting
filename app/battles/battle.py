"""Battle and tournament orchestration module."""

from typing import Any
from app.knights.knight import Knight

DEFAULT_MATCHUPS = [
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
]


class Battle:
    """Manages combat between two knights."""

    def __init__(
        self,
        first_knight: Knight,
        second_knight: Knight,
    ) -> None:
        self.first_knight = first_knight
        self.second_knight = second_knight

    def resolve(self) -> None:
        self.first_knight.fight(self.second_knight)


class Tournament:
    """Manages tournament rounds and results."""

    def __init__(
        self,
        knights: dict[str, Knight],
        matchups: list[tuple[str, str]] | None = None,
    ) -> None:
        self.knights = knights
        self.matchups = matchups if matchups is not None else DEFAULT_MATCHUPS

    @classmethod
    def from_config(
        cls,
        knights_config: dict[str, Any],
        matchups: list[tuple[str, str]] | None = None,
    ) -> "Tournament":
        knights = {
            knight_key: Knight.from_dict(knight_data)
            for knight_key, knight_data in knights_config.items()
        }
        return cls(knights=knights, matchups=matchups)

    def prepare_participants(self) -> None:
        for knight in self.knights.values():
            knight.prepare_for_battle()

    def conduct_matches(self) -> None:
        for first_key, second_key in self.matchups:
            battle_duel = Battle(
                self.knights[first_key],
                self.knights[second_key],
            )
            battle_duel.resolve()

    def get_results(self) -> dict[str, int]:
        return {
            knight.name: knight.hp
            for knight in self.knights.values()
        }

    def run(self) -> dict[str, int]:
        self.prepare_participants()
        self.conduct_matches()
        return self.get_results()
