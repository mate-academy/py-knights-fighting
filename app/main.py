from knights.knight import Knight

from battle.preparations import Preparations
from battle.battle import Battle

from typing import Any


def battle(knights_config: Any) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    preparation = Preparations()

    preparation.preparation(lancelot)
    preparation.preparation(arthur)
    preparation.preparation(mordred)
    preparation.preparation(red_knight)

    _battle = Battle()

    _battle.knight_battle(lancelot, mordred)
    _battle.knight_battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
