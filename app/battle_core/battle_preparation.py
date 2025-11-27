from typing import List

from app.entities.knight import Knight
from app.factory.knight_factory import KnightFactory


class TournamentPreparation:
    """
    Prepares all knights for the tournament. The class loads knight data,
    converts it into fully equipped Knight instances and forms tournament
    fight pairs based on the provided pairing configuration.

    :param participants: dict with raw knight configuration data
    :param tournament_pairs: list of pairs defining duel matchups
    """
    def __init__(
        self, participants: dict, tournament_pairs: List[tuple[str, str]]
    ) -> None:
        self.participants = participants
        self.tournament_pairs = tournament_pairs

    def take_all_participants(self) -> dict[str, Knight]:
        """
        Creates and prepares all knights for the tournament. Returns a
        dictionary where keys are knight names and values are Knight
        instances ready for battle.

        :return: dict[str, Knight] - all prepared participants keyed by name
        """
        knights = KnightFactory(self.participants).create_all_knights()
        return {knight.name: knight for knight in knights}

    def get_tournament_net(self) -> list[tuple[Knight, Knight]]:
        """
        Builds the tournament duel network. Each pair of names from the
        configuration is converted into a pair of Knight instances that
        will participate in a duel.

        :return: list[tuple[Knight, Knight]] - ordered duel match pairs
        """
        participants = self.take_all_participants()
        return [
            (participants[first], participants[second])
            for first, second in self.tournament_pairs
        ]


class Duel:
    """
    Represents a single duel between two knights. Both fighters strike
    once, and the resulting updated Knight states are returned.

    :param first_fighter: Knight - attacker in the first strike
    :param second_fighter: Knight - attacker in the second strike
    """
    def __init__(self, first_fighter: Knight, second_fighter: Knight) -> None:
        self.first_fighter = first_fighter
        self.second_fighter = second_fighter

    def fight(self) -> tuple[Knight, Knight]:
        """
        Executes the duel. Each fighter performs one attack on the other,
        updating the opponent's health. The resulting knight states are
        returned as a tuple.

        :return: tuple[Knight, Knight] - fighters after the duel
        """
        self.first_fighter.attack(self.second_fighter)
        self.second_fighter.attack(self.first_fighter)
        return self.first_fighter, self.second_fighter


class Battle:
    """
    Simulates the full tournament battle process. Receives prepared duel
    pairs and executes all fights, storing final HP values for every
    participant.

    :param tournament_pairs: list of duel pairs with Knight instances
    """
    def __init__(self, tournament_pairs: List[tuple[Knight, Knight]]) -> None:
        self.tournament_pairs = tournament_pairs
        self.battle_result: dict[str, int] = {}

    def battle_start(self) -> None:
        """
        Launches the complete set of duels defined in the tournament grid.
        Each duel result updates the internal battle_result dictionary,
        mapping knight names to their final HP values.

        :return: None
        """
        for first, second in self.tournament_pairs:
            fighter_1, fighter_2 = Duel(first, second).fight()

            self.battle_result[fighter_1.name] = fighter_1.hp
            self.battle_result[fighter_2.name] = fighter_2.hp

    def tournament_result(self) -> dict[str, int]:
        """
        Returns the final tournament results after all duels have finished.
        The dictionary contains knight names mapped to their remaining HP.

        :return: dict[str, int] - final HP values for all participants
        """
        return self.battle_result
