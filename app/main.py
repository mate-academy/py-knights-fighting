from __future__ import annotations

from app.knight_battle.battle import Battle
from app.knight_info.knight import get_knight


def battle(knights_config: dict) -> dict:
    knights = get_knight(knights_config)

    first_battle = Battle()
    first_battle.battle(knights[0], knights[2])

    second_battle = Battle()
    second_battle.battle(knights[1], knights[3])

    return {
        knights[0].name: knights[0].hp,
        knights[2].name: knights[2].hp,
        knights[1].name: knights[1].hp,
        knights[3].name: knights[3].hp,
    }
