from __future__ import annotations

from app.knights_fighting.knight import Knight


class Tournament:
    def __init__(
            self,
            knights: dict,
            opponents_board: list[tuple[str, str]]
    ) -> None:
        """
        opponents_board - List[Tuple[opponent_name, opponent_name]]

        All opponent names must be contained in knights.keys()
        """
        self.knights: dict[str, Knight] = dict()
        self.opponents_board = opponents_board

        for knight_name in knights:
            data = knights[knight_name]
            self.knights[knight_name] = Knight.convert_from_dict(data)

    def prepare(self) -> None:
        """Applies boosts and abilities"""
        for knight in self.knights.values():
            knight.apply_boosts()

    def battle(self) -> dict[str, int]:
        """
        Returns a dict with the health of the knights
        after the battle. -> Dict[name, hp]
        """
        result = dict()

        for name1, name2 in self.opponents_board:
            opponent1 = self.knights[name1]
            opponent2 = self.knights[name2]

            opponent1.hurt(opponent2.get_attack_damage())
            opponent2.hurt(opponent1.get_attack_damage())

            result[opponent1.name] = opponent1.hp
            result[opponent2.name] = opponent2.hp

        return result
