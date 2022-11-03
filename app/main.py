from __future__ import annotations

from app.knight.info import KNIGHTS
from app.knight.warior import Knight


def battle(config: dict) -> dict:
    result = {}
    lancelot = Knight("lancelot", config)
    mordred = Knight("mordred", config)
    artur = Knight("arthur", config)
    red_knight = Knight("red_knight", config)
    pairs = [[lancelot, mordred], [artur, red_knight]]
    for pair in pairs:
        pair[0].prepare_for_tournament()
        pair[1].prepare_for_tournament()
        result.update(pair[0].fight(pair[1]))
    return result


print(battle(KNIGHTS))
