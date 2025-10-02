from __future__ import annotations

from app.knight.prepare import PrepareKnight
from app.battle.battle import knight_battle


def battle(knights_config: dict) -> dict:
    knight_instance = PrepareKnight(knights_config)
    knights = knight_instance.get_all_prepared_knight()

    battle_pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for first_pair, second_pair in battle_pairs:
        knight_battle(
            first_knight=knights[first_pair],
            second_knight=knights[second_pair]
        )

    return {
        knight["name"]: knight["hp"] for knight in knights.values()
    }
