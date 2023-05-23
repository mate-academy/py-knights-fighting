from app.helpers import get_knights, fight_duel
from app.knight import Knight


class Tournamet:
    """
    Tournamet object initializes with config - knights stats as dictionary
    battle function is where all flow goes:
    1. knights passed in dictionary are instantiated of Knight class
    with necessary info during initialization of Tournament
    2. knights are getting out of dict and readied when it is their turn,
    pairs and turns are decided beforehand and passed as list of strings
    3. when duel begins each knight suffers an attack from the opponent
    damage done is calculated by power of the second and protection of first
    4. after duel fought results are stored in journal in dictionary
    in form <Name: health_points_after_duel>
    5. after all duels are over the journal with results is retured
    """
    def __init__(self, config: dict, dueling_pairs: list) -> None:
        self.knights = get_knights(config)
        self.dueling_pairs = dueling_pairs
        self.tournament_journal = dict()

    def battle(self) -> dict:
        """main tournament flow function"""
        for pair in self.dueling_pairs:
            first_knight, second_knight = self.ready_knights(pair)
            if first_knight and second_knight:
                fight_duel(first_knight, second_knight)
                self.resolve_fight(first_knight, second_knight)
        return self.tournament_journal

    def ready_knights(self, knight_pair: tuple) -> tuple:
        first_knight_name, second_knight_name = knight_pair
        first_knight = self.knights[first_knight_name]
        second_knight = self.knights[second_knight_name]
        first_knight.use_items()
        second_knight.use_items()
        return first_knight, second_knight

    def resolve_fight(
        self,
        first_knight: Knight,
        second_knight: Knight
    ) -> None:
        """
        get results of the fight to store in tournament_journal
        may be modified to get needed format and info
        """
        self.tournament_journal[first_knight.name] = first_knight.hp
        self.tournament_journal[second_knight.name] = second_knight.hp
