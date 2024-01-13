from __future__ import annotations
from app.Kings_fighting.kings_start_position import King


class Battle:

    results_of_battle = {}

    @classmethod
    def kings_fighting(cls, first_king: King, second_king: King) -> None:
        kick_first = King.__sub__(first_king, second_king)
        kick_second = King.__sub__(second_king, first_king)
        cls.results_of_battle[first_king.name] = max(0, kick_first.hp)
        cls.results_of_battle[second_king.name] = max(0, kick_second.hp)
