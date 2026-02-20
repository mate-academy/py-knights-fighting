from typing import Dict

from app.championship.knight import Knight
from app.championship.battle import Battle


class Event:
    def __init__(self, knights_dict: dict, versus: Dict[str, str]) -> None:
        self.knights_dict = knights_dict
        self.prepared_knights = {}
        self.results = {}
        self.versus = {}

        for knight1, knight2 in versus.items():
            knight1 = knight1.lower().replace(" ", "_")
            knight2 = knight2.lower().replace(" ", "_")
            self.versus[knight1] = knight2

        self.preparation()

    def preparation(self) -> None:

        for knight_name, knight_data in self.knights_dict.items():
            prepared_knight = Knight(knight_data)
            prepared_knight.preparation()
            self.prepared_knights[knight_name.lower()] = prepared_knight

    def start(self) -> None:
        for knight1_name, knight2_name in self.versus.items():
            knight1 = self.prepared_knights[knight1_name.lower()]
            knight2 = self.prepared_knights[knight2_name.lower()]

            battle = Battle(knight1, knight2)
            self.results.update(battle.fight())

    def get_results(self) -> dict[str, int]:
        return self.results
