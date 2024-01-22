from __future__ import annotations
from app.Knights_fighting.knights_start_position import Knight


class Battle:

    results_of_battle = {}

    @classmethod
    def knights_fighting(
        cls,
        first_knight: Knight,
        second_knight: Knight
    ) -> None:
        kick_first = Knight.__sub__(first_knight, second_knight)
        kick_second = Knight.__sub__(second_knight, first_knight)
        cls.results_of_battle[first_knight.name] = max(0, kick_first.hp)
        cls.results_of_battle[second_knight.name] = max(0, kick_second.hp)
