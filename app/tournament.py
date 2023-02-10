# from __future__ import annotations
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
            knight_one, knight_two = self.ready_knights(pair)
            if knight_one and knight_two:
                fight_duel(knight_one, knight_two)
                self.resolve_fight(knight_one, knight_two)
        return self.tournament_journal

    def ready_knights(self, knight_pair: str) -> tuple:
        knight_one_name, knight_two_name = knight_pair.split(" vs ")
        knight_one = self.knights[knight_one_name]
        knight_two = self.knights[knight_two_name]
        knight_one.use_items()
        knight_two.use_items()
        return knight_one, knight_two

    def resolve_fight(self, knight_one: Knight, knight_two: Knight) -> None:
        """
        get results of the fight to store in tournament_journal
        may be modified to get needed format and info
        """
        self.tournament_journal[knight_one.name] = knight_one.hp
        self.tournament_journal[knight_two.name] = knight_two.hp
