from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.knight.knight import Knight


class Battle:
    """A class to represent a battle between two knights.
    """
    results = dict()

    def __init__(self, knight1: "Knight", knight2: "Knight") -> None:
        """Initializes a Battle object and simulates the battle.

        :param knight1: The first knight.
        :type knight1: Knight
        :param knight2: The second knight.
        :type knight2: Knight
        """
        self.battle = f"{knight1.name} vs {knight2.name}"
        knight1.hp = max(
            knight1.hp - (knight2.power - knight1.protection),
            0
        )
        knight2.hp = max(
            knight2.hp - (knight1.power - knight2.protection),
            0
        )
        Battle.results[knight1.name] = knight1.hp
        Battle.results[knight2.name] = knight2.hp
