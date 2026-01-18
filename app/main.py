from typing import Any

from calculate_states import attribute_calculation
from knights import KNIGHTS
from battles import calculate_battle
from knights_class import Knight


def battle(knights: dict) -> Any:
    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])

    first_fighters = attribute_calculation([lancelot, mordred])
    second_fighters = attribute_calculation([arthur, red_knight])

    return calculate_battle([first_fighters, second_fighters])


print(battle(KNIGHTS))
