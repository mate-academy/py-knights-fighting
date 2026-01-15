from app.knights.knight import Knight
from app.fights.fight import fight
from typing import Dict


def battle(knights: Dict[str, dict]) -> Dict[str, int]:
    lancelot = Knight(**knights["lancelot"])
    mordred = Knight(**knights["mordred"])
    arthur = Knight(**knights["arthur"])
    red_knight = Knight(**knights["red_knight"])

    result_of_first_battle = fight(lancelot, mordred)
    result_of_second_battle = fight(arthur, red_knight)

    return result_of_first_battle | result_of_second_battle
