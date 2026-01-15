from typing import Dict, List, Tuple

from app.battle_system import BattleSystem
from app.knight import Knight


class Tournament:
    """
    Class to manage tournaments involving knights.

    The Tournament class is responsible for managing a collection of
    knights and conducting battles between them. It initializes its
    list of knights based on a provided configuration and uses the
    BattleSystem to simulate battles between them. This class serves
    the purpose of organizing, processing, and summarizing the battles
    conducted within a fictional knight-based tournament.

    """
    def __init__(self, knights_config: Dict[str, Dict]) -> None:
        """
        Initializes the knights configuration from the given
        dictionary and creates a dictionary of knight instances.
        Each key in the input dictionary corresponds to a knight,
        and its configuration is used to create a Knight instance.

        :param knights_config: A dictionary where the keys are strings
            representing knight identifiers, and the values are dictionaries
            containing configuration details for each knight.
        :type knights_config: Dict[str, Dict]
        """
        self.knights = {}
        for key, config in knights_config.items():
            self.knights[key] = Knight.from_config(config)

    def conduct_battles(self,
                        battles: List[Tuple[str, str]]
                        ) -> Dict[str, int]:
        """
        Conduct a series of battles between knights and
        return their remaining health points.

        This method receives a list of battles, represented a
        s pairs of keys that correspond to knights. Using these keys,
        the method retrieves the respective knight objects
        from the knights dataset and conducts a duel between
        the two using the BattleSystem class. The resulting health
        points of each knight after the duel are then recorded
        in a dictionary, which is returned as the method's output.

        :param battles: A list of tuples where each
            tuple contains two strings. Each string
            represents the key of a knight involved in a battle.
        :return: A dictionary mapping each knight's name to their
            remaining health points after their respective battles.
        :rtype: Dict[str, int]
        """
        results = {}

        for knight1_key, knight2_key in battles:
            knight1 = self.knights[knight1_key]
            knight2 = self.knights[knight2_key]

            BattleSystem.fight(knight1, knight2)

            results[knight1.name] = knight1.hp
            results[knight2.name] = knight2.hp

        return results
