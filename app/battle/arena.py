from typing import Generator

from app.adapters.arena_config import ArenaConfig
from app.fighters.knight import Knight


class Arena:
    """
    Represents a battle arena, where knight battle simulation takes place

    Attributes:
        knights: list of all knights
        knight_pairs: tuple of knights who fight each other

    Methods:
        fight_preparations: call each knight's preparation methods
        fight: commence a fight between two knights
    """
    def __init__(self, arena_config: ArenaConfig) -> None:
        self.knights = list(
            Knight(knight_config)
            for knight_config
            in arena_config.knight_configs
        )

        self.knight_pairs = list(
            self.make_knight_pairs(arena_config.matchups)
        )

    def __str__(self) -> str:
        return str(self.knights)

    def ready_and_fight_all_pairs(self) -> dict[str, int]:
        fights_results = {}

        for i, knight_pair in enumerate(self.knight_pairs):
            Arena.ready(knight_pair)

            fights_results.update(Arena.fight(knight_pair))

        return fights_results

    @staticmethod
    def ready(knight_pair: tuple[Knight, Knight]) -> None:
        for knight in knight_pair:
            knight.equip_all_armour()
            knight.equip_best_weapon()
            knight.drink_best_potion()

    @staticmethod
    def fight(knight_pair: tuple[Knight, Knight]) -> dict[str, int]:
        first_knight, second_knight = knight_pair

        first_knight.attack(second_knight)

        second_knight.attack(first_knight)

        return {
            first_knight.name: first_knight.hp,
            second_knight.name: second_knight.hp
        }

    def get_knight_by_name(self, name: str) -> Knight:
        if self.knights is not None:
            for knight in self.knights:
                if knight.name == name:
                    return knight

    def make_knight_pairs(
            self,
            name_pairs: list[tuple[str, str]]
    ) -> Generator[tuple[Knight, Knight], None, None]:
        for name_pair in name_pairs:
            yield (
                self.get_knight_by_name(name_pair[0]),
                self.get_knight_by_name(name_pair[1]),
            )
