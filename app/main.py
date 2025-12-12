from app.battle.battle import start_battle
from app.util.knights_picker import get_knight_pairs
from app.util.knights_list import knights


def battle(base_knights_config: dict = knights) -> dict:

    knights_pairs = get_knight_pairs(base_knights_config)
    result = start_battle(knights_pairs)

    return result
