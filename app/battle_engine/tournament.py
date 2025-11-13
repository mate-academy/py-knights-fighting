from typing import Dict, List, Optional, Tuple, Any
from .battle import Battle
from ..models.knight import Knight


class Tournament:
    def __init__(self, knights_config: Dict[str, Any],
                 pairings: Optional[List[Tuple[str, str]]] = None) \
            -> None:
        self.knights_config = knights_config
        self.pairings = pairings or [
            ("lancelot", "mordred"),
            ("arthur", "red_knight")
        ]
        self.battles = []
        self.results = {}

    def prepare_knights(self) -> Dict[str, Any]:
        self.knights = {}
        for knight_key, knight_data in self.knights_config.items():
            self.knights[knight_key] = Knight(knight_data)
        return self.knights

    def execute_battles(self) -> Dict[str, int]:
        if not hasattr(self, "knights"):
            self.prepare_knights()

        self.results = {}
        self.battles = []

        for knight1_key, knight2_key in self.pairings:
            # Validate that both knights exist
            if (knight1_key not in self.knights
                    or knight2_key not in self.knights):
                raise (
                    ValueError(f"Invalid battle pairing: "
                               f"{knight1_key} vs {knight2_key}"))

            knight1 = self.knights[knight1_key]
            knight2 = self.knights[knight2_key]

            battle = Battle(knight1, knight2)
            battle_result = battle.fight()
            self.battles.append(battle)

            self.results.update(battle_result)

        return self.results

    def get_tournament_winner(self) -> Optional[str]:
        if not self.results:
            return None

        surviving_knights = \
            [name for name, hp in self.results.items() if hp > 0]

        if len(surviving_knights) == 1:
            return surviving_knights[0]
        else:
            return None  # Multiple survivors or all defeated

    def get_battle_details(self) -> List[Dict[str, Any]]:
        details = []
        for battle in self.battles:
            winner = battle.get_winner()
            winner_name = winner.name if winner else "Draw"
            details.append({
                "battle": f"{battle.knight1.name} vs {battle.knight2.name}",
                "winner": winner_name,
                "final_hp": {
                    battle.knight1.name: battle.knight1.hp,
                    battle.knight2.name: battle.knight2.hp
                }
            })
        return details
