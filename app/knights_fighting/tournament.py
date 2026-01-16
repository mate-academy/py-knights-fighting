from __future__ import annotations

from app.knights_fighting.boosts import Potion
from app.knights_fighting.equipment import Armour, Weapon
from app.knights_fighting.knight import Knight


def convert_knight_from_dict(dict_: dict) -> Knight:
    knight = Knight(dict_["name"], dict_["power"], dict_["hp"])

    for armour in dict_["armour"]:
        knight.armour.append(Armour(**armour))

    weapon = dict_["weapon"]
    if weapon:
        knight.weapon = Weapon(**weapon)

    potion = dict_["potion"]
    if potion:
        knight.potion = Potion(**potion)

    return knight


class Tournament:
    def __init__(
            self,
            knights: dict,
            opponents_board: list[tuple[str, str]]
    ) -> None:
        """
        Tournament initialization.

        :param knights: dict with all the data about the knights
            participating in the tournament.
        :param opponents_board: List[Tuple[opponent_name, opponent_name]].
            All opponent names must be contained in knights.keys()
        """
        self.knights: dict[str, Knight] = dict()
        self.opponents_board = opponents_board

        for knight_name in knights:
            data = knights[knight_name]
            self.knights[knight_name] = convert_knight_from_dict(data)

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
