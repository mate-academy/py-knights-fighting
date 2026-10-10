from typing import Any, Dict, Iterable, Tuple

from app.battle.duel import fight
from app.knights.factory import create_knights


def run_battle(
    knights_config: Dict[str, Dict[str, Any]],
    battle_pairs: Iterable[Tuple[str, str]],
) -> Dict[str, int]:
    knights = create_knights(knights_config)

    for first_key, second_key in battle_pairs:
        fight(knights[first_key], knights[second_key])

    return {knight.name: knight.hp for knight in knights.values()}
